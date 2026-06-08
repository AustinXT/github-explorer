#!/usr/bin/env python3
"""resource-miner 确定性数据采集（对标 collect_repo_facts.py，换成「资源视角」）。

repo-miner 的 Phase 2 测「代码规模」（tokei 行数），但资源类仓库（awesome 列表 /
教程课程书 / 非典型项目）没有代码架构，硬套会得「近零代码行 = 已放弃」的错误结论。
本脚本复用 collect_repo_facts 的网络/作者/提交节奏/贡献者采集，**替换**代码规模为
「内容规模 + 策展元分析」，并新增：
  - content_scale  : 仓库体积 / 文件类型直方图 / 顶层目录即分类 / README 大纲 / 外链数
  - automation_sig : 提交时刻的分钟级聚集度 → 是否 cron 驱动的自动化策展流水线
  - detected_type  : awesome | learning | atypical（启发式，--type 可覆盖）

用法：
    python3 src/scripts/collect_resource_facts.py <LOCAL_PATH> \
        [--full-name owner/repo] [--type awesome|learning|atypical] [--out PATH] [--no-network]

输出契约同 collect_repo_facts：JSON 写 --out（缺省 tmp/resource-facts-<repo>.json），
路径打印到 stdout 供 prompt 捕获后 Read。所有指标单独 try，缺失记 null + _warnings，
绝不因单项失败中断整体采集。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

# 与 collect_repo_facts 同目录（src/scripts/），直接 import 复用其确定性采集与容错原语。
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collect_repo_facts as crf  # noqa: E402

# 共用同一个 WARNINGS 列表：被复用函数（crf.collect_*）内部 crf.warn 的告警也会汇入。
WARNINGS = crf.WARNINGS
warn = crf.warn
git = crf.git


# ============================================================ 内容规模与策展元分析

# 遍历时跳过的目录（版本控制 / 依赖 / 构建产物，避免污染内容统计）
_SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build", ".next", "vendor"}
_README_CANDIDATES = ("README.md", "readme.md", "README.MD", "Readme.md", "README.rst", "README")
_MAX_FILES = 300_000  # 安全上限，防超大仓库遍历失控


def _fmt_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f}{unit}" if unit != "B" else f"{int(size)}B"
        size /= 1024.0
    return f"{size:.1f}TB"


def _find_readme(repo: str) -> str | None:
    for name in _README_CANDIDATES:
        p = os.path.join(repo, name)
        if os.path.isfile(p):
            return p
    # 兜底：任意大小写 readme.*
    try:
        for fn in os.listdir(repo):
            if fn.lower().startswith("readme"):
                return os.path.join(repo, fn)
    except OSError:
        pass
    return None


def _analyze_readme(repo: str) -> dict:
    out = {
        "path": None, "bytes": None, "heading_count": None, "h2_count": None,
        "has_toc": None, "link_count": None, "list_link_items": None,
    }
    p = _find_readme(repo)
    if not p:
        warn("未找到 README")
        return out
    out["path"] = os.path.relpath(p, repo)
    try:
        text = open(p, encoding="utf-8", errors="replace").read()
    except OSError as e:
        warn(f"读取 README 失败: {e}")
        return out
    out["bytes"] = len(text.encode("utf-8"))
    out["heading_count"] = len(re.findall(r"^#{1,6}\s+\S", text, re.M))
    out["h2_count"] = len(re.findall(r"^##\s+\S", text, re.M))
    # TOC 判定：显式「目录/Table of Contents/Contents」或开头有大量锚点链接
    has_toc = bool(re.search(r"(?im)^#{1,3}\s*(目录|table of contents|contents)\b", text))
    if not has_toc:
        anchor_links = len(re.findall(r"\]\(#", text[:4000]))
        has_toc = anchor_links >= 5
    out["has_toc"] = has_toc
    # 链接密度（awesome 列表的核心指标）
    out["link_count"] = len(re.findall(r"\[[^\]]+\]\([^)]+\)", text))
    out["list_link_items"] = len(re.findall(r"^\s*[-*+]\s+\[", text, re.M))
    return out


def collect_content_scale(repo: str) -> dict:
    """替换 collect_code_scale：测内容规模而非代码规模。"""
    out = {
        "total_bytes": None, "total_human": None, "file_count": None,
        "ext_histogram": [], "main_ext": None, "top_dirs": [],
        "markdown_files": None, "readme": _analyze_readme(repo),
        "total_link_count": None, "truncated": False,
    }
    total_bytes = 0
    file_count = 0
    ext = Counter()
    topdir_files = Counter()
    md_files = []
    truncated = False
    try:
        for root, dirs, files in os.walk(repo):
            dirs[:] = [d for d in dirs if d not in _SKIP_DIRS]
            rel = os.path.relpath(root, repo)
            topseg = (rel.split(os.sep)[0] if rel != "." else "(root)")
            for fn in files:
                fp = os.path.join(root, fn)
                try:
                    sz = os.path.getsize(fp)
                except OSError:
                    sz = 0
                total_bytes += sz
                file_count += 1
                e = (os.path.splitext(fn)[1].lower() or "(noext)")
                ext[e] += 1
                topdir_files[topseg] += 1
                if e in (".md", ".markdown", ".mdx") and len(md_files) < 50:
                    md_files.append(fp)
                if file_count >= _MAX_FILES:
                    truncated = True
                    break
            if truncated:
                break
    except OSError as e:
        warn(f"遍历仓库失败: {e}")

    out["total_bytes"] = total_bytes
    out["total_human"] = _fmt_size(total_bytes)
    out["file_count"] = file_count
    out["truncated"] = truncated
    out["markdown_files"] = sum(c for e, c in ext.items() if e in (".md", ".markdown", ".mdx"))
    hist = ext.most_common(15)
    out["ext_histogram"] = [{"ext": e, "files": c} for e, c in hist]
    out["main_ext"] = hist[0][0] if hist else None
    # 顶层目录即分类
    out["top_dirs"] = [
        {"dir": d, "files": c} for d, c in topdir_files.most_common(20)
    ]
    # 全仓 markdown 外链总数（awesome 列表覆盖度信号；README 之外的拆分列表也计入）
    total_links = 0
    for fp in md_files:
        try:
            t = open(fp, encoding="utf-8", errors="replace").read()
            total_links += len(re.findall(r"\[[^\]]+\]\([^)]+\)", t))
        except OSError:
            continue
    out["total_link_count"] = total_links
    return out


# ============================================================ 自动化签名（cron 检测）

def collect_automation_signature(repo: str) -> dict:
    """从提交时刻的「分钟级聚集度」判断是否 cron 驱动的自动化策展流水线。

    用每个 commit 的作者本地时刻（git %ai 自带时区，反映提交者挂钟时间）：
    把 commit 落到 (星期, HH:MM) 与 HH 两种桶，算 top 桶占比。高度聚集 → 疑似定时自动化。
    """
    out = {
        "sample": None, "top_minute_bucket": None, "top_minute_share": None,
        "top3_hour_share": None, "distinct_minute_buckets": None,
        "signature": None,
    }
    lines = [ln for ln in git(repo, "log", "--format=%ai").splitlines() if ln.strip()]
    if not lines:
        warn("无提交记录，跳过自动化签名")
        return out
    minute_buckets = Counter()  # (weekday, "HH:MM")
    hour_buckets = Counter()    # HH
    n = 0
    for ln in lines:
        # 形如 "2023-05-01 21:20:13 +0800"
        m = re.match(r"\d{4}-\d{2}-\d{2}\s+(\d{2}):(\d{2}):\d{2}\s", ln.strip())
        if not m:
            continue
        d = crf._parse_iso(ln.strip())
        if d is None:
            continue
        hh, mm = m.group(1), m.group(2)
        wd = d.isoweekday()
        minute_buckets[(wd, f"{hh}:{mm}")] += 1
        hour_buckets[hh] += 1
        n += 1
    if n == 0:
        return out
    out["sample"] = n
    out["distinct_minute_buckets"] = len(minute_buckets)
    (top_wd_hm, top_cnt) = minute_buckets.most_common(1)[0]
    out["top_minute_bucket"] = f"周{top_wd_hm[0]} {top_wd_hm[1]}"
    out["top_minute_share"] = round(top_cnt / n * 100, 1)
    top3_hours = sum(c for _h, c in hour_buckets.most_common(3))
    out["top3_hour_share"] = round(top3_hours / n * 100, 1)

    # 分级启发式：分钟级单桶占比高、或时刻桶极少而样本大 → 强自动化信号
    minute_share = out["top_minute_share"]
    if n >= 20 and (minute_share >= 30 or (out["distinct_minute_buckets"] <= max(8, n * 0.25))):
        out["signature"] = "高（提交时刻高度聚集，疑似定时自动化流水线）"
    elif n >= 20 and out["top3_hour_share"] >= 60:
        out["signature"] = "中（集中在固定时段，可能半自动化）"
    else:
        out["signature"] = "低（提交时刻分散，以人工提交为主）"
    return out


# ============================================================ 子类型识别

_AWESOME_RE = re.compile(r"awesome", re.I)
_LEARNING_KW = re.compile(
    r"roadmap|tutorial|course|courses|book|books|handbook|guide|guides|curriculum|"
    r"interview|primer|cheat-?sheet|cookbook|lecture|learn|learning|notes|"
    r"教程|学习|路线|面试|入门|从入门|实战|课程|手册|指南",
    re.I,
)


def detect_type(repo: str, full_name: str | None, network: dict | None,
                content_scale: dict, override: str | None) -> dict:
    out = {"detected_type": None, "source": None, "signals": {}}
    if override in ("awesome", "learning", "atypical"):
        out.update(detected_type=override, source="override")
        return out

    name = (full_name or os.path.basename(repo) or "").lower()
    topics = []
    if network and isinstance(network.get("repo_basics"), dict):
        topics = [str(t).lower() for t in (network["repo_basics"].get("topics") or [])]
    desc = ""
    if network and isinstance(network.get("repo_basics"), dict):
        desc = str(network["repo_basics"].get("description") or "").lower()

    readme = content_scale.get("readme") or {}
    link_items = readme.get("list_link_items") or 0
    readme_links = readme.get("link_count") or 0
    headings = readme.get("heading_count") or 0
    md_files = content_scale.get("markdown_files") or 0

    sig = out["signals"]
    sig["name_has_awesome"] = bool(_AWESOME_RE.search(name)) or any("awesome" in t for t in topics)
    sig["learning_kw"] = bool(_LEARNING_KW.search(name)) or any(_LEARNING_KW.search(t) for t in topics) \
        or bool(_LEARNING_KW.search(desc))
    sig["readme_list_link_items"] = link_items
    sig["readme_link_count"] = readme_links
    sig["readme_heading_count"] = headings
    # awesome 特征：README 是高密度链接清单（列表项多且以链接为主）
    link_list_dominant = link_items >= 40 and readme_links >= 60
    sig["link_list_dominant"] = link_list_dominant

    # 优先级：名字含 awesome（最强信号）> 学习关键词（教程/路线图等学习资料常也是链接密集，
    # 但本质是学习材料，须先于「链接密集→awesome」判定）> 纯链接密集清单 > 多章节文档 > 其它
    if sig["name_has_awesome"]:
        out["detected_type"] = "awesome"
    elif sig["learning_kw"]:
        out["detected_type"] = "learning"
    elif link_list_dominant:
        out["detected_type"] = "awesome"
    elif headings >= 15 and md_files >= 1:
        out["detected_type"] = "learning"
    else:
        out["detected_type"] = "atypical"
    out["source"] = "heuristic"
    return out


# ============================================================ 主流程

def main() -> int:
    ap = argparse.ArgumentParser(description="resource-miner 确定性数据采集（资源视角）")
    ap.add_argument("local_path", help="已 clone 的本地仓库路径")
    ap.add_argument("--full-name", help="owner/repo，缺省从 git remote 推断")
    ap.add_argument("--type", dest="type_override",
                    choices=["awesome", "learning", "atypical"],
                    help="强制子类型，缺省由启发式判定")
    ap.add_argument("--out", help="JSON 落地路径，缺省 tmp/resource-facts-<repo>.json")
    ap.add_argument("--no-network", action="store_true",
                    help="只采离线指标（git/文件系统），跳过 gh 联网采集")
    args = ap.parse_args()

    repo = os.path.abspath(args.local_path)
    if not os.path.isdir(os.path.join(repo, ".git")):
        print(f"ERR: {repo} 不是 git 仓库（缺 .git）", file=sys.stderr)
        return 2

    full_name = crf.infer_full_name(repo, args.full_name)
    repo_short = (full_name.split("/")[-1] if full_name else os.path.basename(repo))

    # 内容规模（离线，先采，detect_type 要用）
    content_scale = collect_content_scale(repo)

    # 网络（联网 gh，先采以拿 topics/description 喂给 detect_type）
    network = None
    if not args.no_network and full_name:
        network = crf.collect_network(full_name, repo)
    elif not full_name:
        warn("无法确定 full_name（owner/repo），跳过 Phase 1 网络采集")

    type_info = detect_type(repo, full_name, network, content_scale, args.type_override)

    facts = {
        "schema_version": 1,
        "kind": "resource",
        "full_name": full_name,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "detected_type": type_info["detected_type"],
        "type_source": type_info["source"],
        "type_signals": type_info["signals"],
        # 内容规模与策展元分析（替换 code_scale）
        "content_scale": content_scale,
        # 更新节奏（复用 dev_rhythm）+ 自动化签名
        "update_rhythm": {
            **crf.collect_dev_rhythm(repo),
            "automation_signature": collect_automation_signature(repo),
        },
        # 演化轨迹（复用：tags / commit 类型分布 / 热点目录）
        "evolution": crf.collect_evolution(repo, full_name if not args.no_network else None),
        # 贡献者（复用）
        "contributors": crf.collect_contributors(repo),
        # 网络（复用：repo_basics/heat_level/author/community/ecosystem/issues/media）
        "network": network,
        "_warnings": WARNINGS,
    }

    out_path = args.out or os.path.join("tmp", f"resource-facts-{repo_short}.json")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)

    print(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
