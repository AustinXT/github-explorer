#!/usr/bin/env python3
"""解析 github-trending-archive 数据，输出 trending 快照 SoR：src/data/trending_snapshots.jsonl。

每行一个快照，自带完整字段，供 seed_trending.py 灌库、site/ 直接读取：
    {"period_type","period_key","url","name","language","description","stars","forks","rank"}

去重汇总 all_repos_deduped.json 与人类可读榜单不再由本脚本产出：
前者改由 `init_db.py export-json` 从 DB 派生（按 url 去重，权威）；
选题用站点 /trending 与 select_next_repo.py。
"""

import json
import re
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

ARCHIVE_DIR = Path("/tmp/github-trending-archive/data")
OUTPUT_DIR = Path(__file__).parent
# SoR 落到 src/data/（与 publish_history.jsonl 同处）
SNAPSHOTS_FILE = OUTPUT_DIR.parent / "data" / "trending_snapshots.jsonl"

# 半年范围：2025-09-22 到 2026-04-06
START_DATE = datetime(2025, 9, 22)
END_DATE = datetime(2026, 4, 6)


def _snapshot_rows(period_type: str, period_key: str, repos: list[dict]) -> list[dict]:
    """把一期 repo 列表转为 jsonl 行（rank = 列表序，1-based）。仅保留有 url 的条目。"""
    rows = []
    for rank, r in enumerate(repos, start=1):
        url = r.get("url")
        if not url:
            continue
        rows.append({
            "period_type": period_type,
            "period_key": period_key,
            "url": url,
            "name": r.get("name", ""),
            "language": r.get("language"),
            "description": r.get("description") or "",
            "stars": int(r.get("stars") or 0),
            "forks": int(r.get("forks") or 0),
            "rank": rank,
        })
    return rows


def parse_md_file(filepath: Path) -> list[dict]:
    """解析单个 markdown 文件，提取 repo 列表。"""
    text = filepath.read_text(encoding="utf-8")
    repos = []

    # 按 ### **Repository:** 分割
    blocks = re.split(r"### \*\*Repository:\*\*", text)
    for block in blocks[1:]:  # 跳过第一个空块
        repo = {}

        # 名称和链接
        m = re.search(r"\[([^\]]+)\]\(([^)]+)\)", block)
        if m:
            repo["name"] = m.group(1)
            repo["url"] = m.group(2)

        # 语言
        m = re.search(r"\*\*Language:\*\*\s*(.+)", block)
        if m:
            repo["language"] = m.group(1).strip()

        # Stars
        m = re.search(r"\*\*Stars:\*\*\s*([\d,]+)", block)
        if m:
            repo["stars"] = int(m.group(1).replace(",", ""))

        # Forks
        m = re.search(r"\*\*Forks:\*\*\s*([\d,]+)", block)
        if m:
            repo["forks"] = int(m.group(1).replace(",", ""))

        # 描述
        m = re.search(r"\*\*Description:\*\*\s*(.+)", block)
        if m:
            repo["description"] = m.group(1).strip()

        if repo.get("name"):
            repos.append(repo)

    return repos


def get_iso_week(date: datetime) -> str:
    """返回 ISO 周标识，如 2025-W39。"""
    iso = date.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def get_month(date: datetime) -> str:
    return date.strftime("%Y-%m")


def main():
    daily_data: dict[str, list[dict]] = {}   # date_str -> repos（原始序）
    weekly_data = defaultdict(dict)           # week -> {name: repo}（保留星标最高）
    monthly_data = defaultdict(dict)          # month -> {name: repo}

    current = START_DATE
    while current <= END_DATE:
        date_str = current.strftime("%Y-%m-%d")
        month_str = current.strftime("%Y-%m")
        filepath = ARCHIVE_DIR / month_str / f"{date_str}.md"

        if filepath.exists():
            repos = parse_md_file(filepath)
            daily_data[date_str] = repos

            week_key = get_iso_week(current)
            month_key = get_month(current)
            for r in repos:
                name = r["name"]
                if name not in weekly_data[week_key] or r.get("stars", 0) > weekly_data[week_key][name].get("stars", 0):
                    weekly_data[week_key][name] = r
                if name not in monthly_data[month_key] or r.get("stars", 0) > monthly_data[month_key][name].get("stars", 0):
                    monthly_data[month_key][name] = r

        current += timedelta(days=1)

    # 汇总快照行：daily（按日期）→ weekly（按周）→ monthly（按月）
    rows: list[dict] = []
    for date_str in sorted(daily_data):
        rows += _snapshot_rows("daily", date_str, daily_data[date_str])
    for week_key in sorted(weekly_data):
        repos_list = sorted(weekly_data[week_key].values(), key=lambda x: x.get("stars", 0), reverse=True)
        rows += _snapshot_rows("weekly", week_key, repos_list)
    for month_key in sorted(monthly_data):
        repos_list = sorted(monthly_data[month_key].values(), key=lambda x: x.get("stars", 0), reverse=True)
        rows += _snapshot_rows("monthly", month_key, repos_list)

    SNAPSHOTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with SNAPSHOTS_FILE.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"时间范围: {START_DATE.date()} ~ {END_DATE.date()}")
    print(f"每日 {len(daily_data)} 期 / 每周 {len(weekly_data)} 期 / 每月 {len(monthly_data)} 期")
    print(f"✅ 写入 {len(rows)} 条快照 → {SNAPSHOTS_FILE.relative_to(OUTPUT_DIR.parent.parent)}")


if __name__ == "__main__":
    main()
