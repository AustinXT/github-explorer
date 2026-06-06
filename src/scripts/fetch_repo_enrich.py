#!/usr/bin/env python3
"""抓取报告对应 GitHub 仓库的实时元数据 → 写 src/data/repo_enrich.json。

build_reports_index.py 解析 md 时，若「项目画像」表缺失或格式不标准会留下大量
NULL（stars/forks/language/license/age）。本脚本对所有已有 original_url 的报告，
用 gh CLI 调 GitHub API 补齐这些客观字段，落地为入 Git 的缓存，供 build 兜底读取。

数据流：
    reports.json(originalUrl) → gh api repos/{owner}/{repo} → repo_enrich.json
    build_reports_index.py 解析 md 后，对仍为 None 的字段用本缓存兜底（md/SoR 优先）。

字段：stars / forks / language / license(SPDX) / age_months / description。
key 为 normalize_url(original_url)，与 reports.original_url 对齐，直接 = 即可命中。

依赖：gh CLI（CI 用 GH_TOKEN，本地用 `gh auth login` 的凭证）。

环境变量：
  REPO_ENRICH_LIMIT  仅抓前 N 个（调试用，默认 0 = 全部）

容错：单个 repo 抓取失败（404/改名/私有化/限流）时保留旧缓存中该条，不删数据。
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS_JSON = ROOT / "src" / "data" / "reports.json"
ENRICH_JSON = ROOT / "src" / "data" / "repo_enrich.json"

# init_db.py 与本文件同目录，复用全局 URL 规范化（rstrip('/') + lower）
sys.path.insert(0, str(ROOT / "src" / "scripts"))
from init_db import normalize_url  # noqa: E402

LIMIT = int(os.environ.get("REPO_ENRICH_LIMIT", "0"))

OWNER_REPO_RE = re.compile(r"https?://github\.com/([^/]+)/([^/#?]+)", re.I)


class RepoUnavailable(Exception):
    """repo 不存在 / 改名 / 私有化（gh api 404）。"""


def load_report_urls() -> list[str]:
    """从 reports.json 取所有非空 originalUrl，normalize 后去重保序。"""
    if not REPORTS_JSON.exists():
        return []
    data = json.loads(REPORTS_JSON.read_text(encoding="utf-8"))
    seen: set[str] = set()
    urls: list[str] = []
    for r in data:
        u = normalize_url(r.get("originalUrl"))
        if u and u not in seen:
            seen.add(u)
            urls.append(u)
    return urls


def load_cache() -> dict[str, dict]:
    if not ENRICH_JSON.exists():
        return {}
    try:
        return json.loads(ENRICH_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def parse_owner_repo(url: str) -> tuple[str, str] | None:
    m = OWNER_REPO_RE.match(url)
    if not m:
        return None
    owner, repo = m.group(1), m.group(2)
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not owner or not repo:
        return None
    return owner, repo


def gh_repo(owner: str, repo: str) -> dict:
    proc = subprocess.run(
        ["gh", "api", f"repos/{owner}/{repo}"], capture_output=True, text=True
    )
    if proc.returncode != 0:
        err = proc.stderr.strip()
        if "Not Found" in err or "HTTP 404" in err:
            raise RepoUnavailable(err)
        raise RuntimeError(err or f"gh api 退出码 {proc.returncode}")
    return json.loads(proc.stdout)


def age_months_from(created_at: str | None) -> float | None:
    """created_at（ISO 8601）→ 距今月数（天数 / 30.44），与 parse_age_months 语义对齐。"""
    if not created_at:
        return None
    try:
        dt = datetime.strptime(created_at[:10], "%Y-%m-%d")
    except ValueError:
        return None
    days = (datetime.now() - dt).days
    return round(days / 30.44, 1) if days >= 0 else None


def build_entry(data: dict, fetched_at: str) -> dict:
    lic = (data.get("license") or {}).get("spdx_id")
    # NOASSERTION = 有 LICENSE 文件但 GitHub 无法识别；None/NONE = 无许可证。均保持 NULL。
    if lic in (None, "", "NOASSERTION", "NONE"):
        lic = None
    return {
        "stars": int(data.get("stargazers_count") or 0),
        "forks": int(data.get("forks_count") or 0),
        "language": data.get("language") or None,
        "license": lic,
        "age_months": age_months_from(data.get("created_at")),
        "description": data.get("description") or "",
        "fetched_at": fetched_at,
    }


def main() -> int:
    urls = load_report_urls()
    if not urls:
        print(f"ERR: {REPORTS_JSON} 无可用 originalUrl", file=sys.stderr)
        return 1
    if LIMIT > 0:
        urls = urls[:LIMIT]
    cache = load_cache()
    fetched_at = datetime.now().strftime("%Y-%m-%d")

    ok = fail = skip = 0
    for i, url in enumerate(urls, 1):
        pr = parse_owner_repo(url)
        if not pr:
            skip += 1
            print(f"  [{i}/{len(urls)}] 跳过非标准 url: {url}", file=sys.stderr)
            continue
        owner, repo = pr
        try:
            data = gh_repo(owner, repo)
        except RepoUnavailable:
            fail += 1
            print(f"  [{i}/{len(urls)}] 404 跳过（保留旧缓存）: {owner}/{repo}", file=sys.stderr)
            continue
        except Exception as e:  # noqa: BLE001 — 单 repo 失败不应中断整体
            fail += 1
            print(f"  [{i}/{len(urls)}] 抓取失败（保留旧缓存）: {owner}/{repo}: {e}", file=sys.stderr)
            continue
        cache[url] = build_entry(data, fetched_at)
        ok += 1
        if i % 25 == 0 or i == len(urls):
            print(f"  ... {i}/{len(urls)} (ok={ok} fail={fail} skip={skip})", file=sys.stderr)

    ordered = {k: cache[k] for k in sorted(cache)}
    ENRICH_JSON.write_text(
        json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"✅ 写入 {len(ordered)} 条 → {ENRICH_JSON.relative_to(ROOT)}"
        f"  (本次 ok={ok} fail={fail} skip={skip}, fetched_at={fetched_at})",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
