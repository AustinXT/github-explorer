#!/usr/bin/env python3
"""
从 trending deduped 数据里挑下一个要分析的仓库。

去重逻辑：
  - 命中 src/analysis_report/{owner}_{repo}.md 的视为已分析
  - 命中 docs/analysis_report/repos.md 里 "❌ <url>" 的视为黑名单

排序：trending_days desc, stars desc

输出：
  - stdout: 选中的 URL（一行）
  - $GITHUB_OUTPUT: repo_url=<url> / repo_name=<owner/repo> / repo_slug=<owner_repo>
  - 无候选: exit 78（GitHub Actions 视为 neutral skip）
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRENDING_JSON = ROOT / "src" / "trending_repo" / "all_repos_deduped.json"
ANALYSIS_DIR = ROOT / "src" / "analysis_report"
BLACKLIST_FILE = ROOT / "docs" / "analysis_report" / "repos.md"


def load_candidates() -> list[dict]:
    if not TRENDING_JSON.exists():
        print(f"ERR: 找不到候选源 {TRENDING_JSON}", file=sys.stderr)
        sys.exit(1)
    with TRENDING_JSON.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        print(f"ERR: {TRENDING_JSON} 顶层不是 list", file=sys.stderr)
        sys.exit(1)
    return data


def load_analyzed_slugs() -> set[str]:
    if not ANALYSIS_DIR.exists():
        return set()
    return {p.stem for p in ANALYSIS_DIR.glob("*.md")}


def load_blacklist_urls() -> set[str]:
    if not BLACKLIST_FILE.exists():
        return set()
    urls: set[str] = set()
    pattern = re.compile(r"^[❌×x]\s+(https?://github\.com/[\w.-]+/[\w.-]+)")
    for line in BLACKLIST_FILE.read_text(encoding="utf-8").splitlines():
        m = pattern.match(line.strip())
        if m:
            urls.add(m.group(1).rstrip("/"))
    return urls


def slug_of(name: str) -> str:
    return name.replace("/", "_")


def select(candidates: list[dict], analyzed: set[str], blacklist: set[str]) -> dict | None:
    pool = []
    for item in candidates:
        name = (item.get("name") or "").strip()
        url = (item.get("url") or "").strip().rstrip("/")
        if not name or not url or "/" not in name:
            continue
        if slug_of(name) in analyzed:
            continue
        if url in blacklist:
            continue
        pool.append(item)
    pool.sort(
        key=lambda x: (int(x.get("trending_days") or 0), int(x.get("stars") or 0)),
        reverse=True,
    )
    return pool[0] if pool else None


def emit_github_output(picked: dict) -> None:
    out_path = os.environ.get("GITHUB_OUTPUT")
    if not out_path:
        return
    name = picked["name"]
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(f"repo_url={picked['url']}\n")
        f.write(f"repo_name={name}\n")
        f.write(f"repo_slug={slug_of(name)}\n")
        f.write(f"repo_stars={picked.get('stars', 0)}\n")


def main() -> int:
    candidates = load_candidates()
    analyzed = load_analyzed_slugs()
    blacklist = load_blacklist_urls()

    print(
        f"候选 {len(candidates)} | 已分析 {len(analyzed)} | 黑名单 {len(blacklist)}",
        file=sys.stderr,
    )

    picked = select(candidates, analyzed, blacklist)
    if picked is None:
        print("没有可分析的新仓库", file=sys.stderr)
        return 78

    print(
        f"选中: {picked['name']} (stars={picked.get('stars')}, "
        f"trending_days={picked.get('trending_days')})",
        file=sys.stderr,
    )
    print(picked["url"])
    emit_github_output(picked)
    return 0


if __name__ == "__main__":
    sys.exit(main())
