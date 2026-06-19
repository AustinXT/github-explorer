#!/usr/bin/env python3
"""
校验「仓库分析请求」issue：
    1. 解析 issue body 中的 GitHub URL
    2. URL 格式 + 仓库公开存在性（gh CLI）
    3. 是否已被分析过（reports.json + src/analysis_report/）

用法：
    GITHUB_TOKEN=... python3 validate_submission.py <issue_number_or_body_file>

输出：
    标准输出打印 owner / repo / url（成功）；
    错误时打印「ERROR: ...」并以非 0 退出。
    GITHUB_OUTPUT 写入 repo_url / owner / repo / username / slug / report_path
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = ROOT / "src" / "analysis_report"
REPORTS_JSON = ROOT / "src" / "data" / "reports.json"

URL_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?(?:/|$)")
# 兼容 issue form 的「### GitHub 仓库 URL\n\n<value>」段落
FORM_FIELD_RE = re.compile(
    r"###\s*GitHub\s*仓库\s*URL\s*\n+(?P<value>.+?)(?:\n###|\Z)", re.S | re.I
)


def emit_output(key: str, value: str) -> None:
    out_path = os.environ.get("GITHUB_OUTPUT")
    if out_path:
        with open(out_path, "a", encoding="utf-8") as f:
            # 多行安全用 heredoc 形式
            if "\n" in value:
                f.write(f"{key}<<EOF\n{value}\nEOF\n")
            else:
                f.write(f"{key}={value}\n")
    print(f"::set {key}={value}")


def fail(msg: str, comment: str | None = None) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    emit_output("ok", "false")
    emit_output("error", msg)
    if comment:
        emit_output("comment", comment)
    sys.exit(1)


def extract_url(body: str) -> str | None:
    """优先匹配 issue form 字段；找不到则在全文搜 URL"""
    m = FORM_FIELD_RE.search(body)
    if m:
        candidate = m.group("value").strip().splitlines()[0].strip()
        if URL_RE.match(candidate):
            return candidate
    m = URL_RE.search(body)
    if m:
        # 还原完整 URL（match.group(0) 可能带尾部 / 或 ; 等）
        return f"https://github.com/{m.group(1)}/{m.group(2)}"
    return None


_RATE_LIMIT_PAT = re.compile(r"(rate limit|secondary rate|API rate limit exceeded)", re.I)
_RETRY_AFTER_PAT = re.compile(r"retry[- ]after[:= ]+(\d+)", re.I)


def _gh_api_with_retry(args: list[str], *, timeout: int = 20) -> subprocess.CompletedProcess:
    """gh api 调用，对 rate-limit 类错误退避后重试一次。

    GitHub 在 secondary rate limit 时 stderr 会带 'rate limit' / 'Retry-After'，
    短暂 sleep 后通常恢复。其它错误（404 / 403 权限 / 网络）维持原行为，
    由调用方处理。
    """
    r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    if r.returncode == 0:
        return r
    stderr = r.stderr or ""
    if not _RATE_LIMIT_PAT.search(stderr):
        return r
    # 解析 Retry-After，缺失或异常时默认 30s；上限 60s 防止卡住
    m = _RETRY_AFTER_PAT.search(stderr)
    delay = 30
    if m:
        try:
            delay = max(1, min(60, int(m.group(1))))
        except ValueError:
            pass
    print(
        f"WARN: gh api 触发 rate limit，{delay}s 后重试一次",
        file=sys.stderr,
    )
    time.sleep(delay)
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout)


def repo_exists_public(owner: str, name: str) -> tuple[bool, str | None]:
    """用 gh api 检查仓库是否公开存在"""
    try:
        r = _gh_api_with_retry(["gh", "api", f"repos/{owner}/{name}"], timeout=20)
    except FileNotFoundError:
        return False, "gh CLI 未安装"
    except subprocess.TimeoutExpired:
        return False, "调用 gh api 超时"
    if r.returncode != 0:
        return False, r.stderr.strip().splitlines()[-1] if r.stderr else "未知错误"
    try:
        info = json.loads(r.stdout)
    except json.JSONDecodeError:
        return False, "gh api 返回非 JSON"
    if info.get("private"):
        return False, "该仓库为私有，无法分析"
    if info.get("archived"):
        return True, "warn:仓库已归档（仍可分析，但可能信息陈旧）"
    return True, None


def already_analyzed(owner: str, name: str) -> str | None:
    """返回已存在的报告 slug，否则 None"""
    slug = f"{owner}_{name}".lower()
    if REPORTS_JSON.exists():
        for r in json.loads(REPORTS_JSON.read_text(encoding="utf-8")):
            if r.get("slug") == slug:
                return slug
            if r.get("originalUrl"):
                orig = r["originalUrl"].rstrip("/").lower()
                if orig == f"https://github.com/{owner}/{name}".lower():
                    return r["slug"]
    # 直接看文件（大小写不敏感）
    for p in REPORTS_DIR.glob("*.md"):
        if p.stem.lower() == slug:
            return p.stem
    return None


def main() -> int:
    if len(sys.argv) < 2:
        fail("缺少参数：issue body 文件路径", "内部错误，请联系维护者")
    body_path = Path(sys.argv[1])
    if not body_path.exists():
        fail(f"找不到 body 文件 {body_path}")

    body = body_path.read_text(encoding="utf-8")
    url = extract_url(body)
    if not url:
        fail(
            "未找到合法的 GitHub 仓库 URL",
            "❌ **校验失败**：未在 issue 中找到 GitHub 仓库 URL。请用「提交仓库分析请求」模板重新提交。",
        )

    m = URL_RE.match(url)
    if not m:
        fail(f"URL 解析失败：{url}", f"❌ **校验失败**：URL `{url}` 格式不正确。")
    # URL_RE 的 (?:\.git)? 已剥过 .git，这里用 removesuffix 兜底（语义=去后缀）。
    # 切勿用 rstrip(".git")：它把 ".git" 当字符集合，会误删名字末尾的 ./g/i/t，
    # 例如 mini-swe-agent → mini-swe-agen，导致 gh api 404。
    owner, name = m.group(1), m.group(2).removesuffix(".git")
    url = f"https://github.com/{owner}/{name}"

    existing = already_analyzed(owner, name)
    if existing:
        fail(
            f"已存在报告 {existing}",
            f"⏭ **跳过**：该仓库已分析过，见 [`{existing}.md`](../blob/main/src/analysis_report/{existing}.md)。",
        )

    ok, note = repo_exists_public(owner, name)
    if not ok:
        fail(
            f"仓库校验失败: {note}",
            f"❌ **校验失败**：{note}。请确认 URL 指向公开仓库。",
        )

    warn = note if note and note.startswith("warn:") else None

    print(f"✅ {url}")
    emit_output("ok", "true")
    emit_output("repo_url", url)
    emit_output("owner", owner)
    emit_output("repo", name)
    slug = f"{owner}_{name}".lower()
    emit_output("slug", slug)
    emit_output("report_path", f"src/analysis_report/{owner}_{name}.md")
    if warn:
        emit_output("warning", warn)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
