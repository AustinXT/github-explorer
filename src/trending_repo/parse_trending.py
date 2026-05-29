#!/usr/bin/env python3
"""解析 github-trending-archive 数据，输出每日/每周/每月/去重后的 trending repos。"""

import json
import re
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

ARCHIVE_DIR = Path("/tmp/github-trending-archive/data")
OUTPUT_DIR = Path(__file__).parent

# 半年范围：2025-09-22 到 2026-04-06
START_DATE = datetime(2025, 9, 22)
END_DATE = datetime(2026, 4, 6)


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
    daily_dir = OUTPUT_DIR / "daily"
    weekly_dir = OUTPUT_DIR / "weekly"
    monthly_dir = OUTPUT_DIR / "monthly"
    daily_dir.mkdir(exist_ok=True)
    weekly_dir.mkdir(exist_ok=True)
    monthly_dir.mkdir(exist_ok=True)

    all_repos = {}  # name -> best record (highest stars)
    weekly_data = defaultdict(dict)   # week -> {name: repo}
    monthly_data = defaultdict(dict)  # month -> {name: repo}

    current = START_DATE
    daily_count = 0

    while current <= END_DATE:
        date_str = current.strftime("%Y-%m-%d")
        month_str = current.strftime("%Y-%m")
        filepath = ARCHIVE_DIR / month_str / f"{date_str}.md"

        if filepath.exists():
            repos = parse_md_file(filepath)

            # 每日输出
            daily_file = daily_dir / f"{date_str}.json"
            daily_file.write_text(
                json.dumps(repos, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            daily_count += 1

            # 聚合到周和月
            week_key = get_iso_week(current)
            month_key = get_month(current)
            for r in repos:
                name = r["name"]

                # 周聚合：保留星标最高的记录
                if name not in weekly_data[week_key] or r.get("stars", 0) > weekly_data[week_key][name].get("stars", 0):
                    weekly_data[week_key][name] = r

                # 月聚合
                if name not in monthly_data[month_key] or r.get("stars", 0) > monthly_data[month_key][name].get("stars", 0):
                    monthly_data[month_key][name] = r

                # 全局去重：保留星标最高的记录
                if name not in all_repos or r.get("stars", 0) > all_repos[name].get("stars", 0):
                    all_repos[name] = {**r, "last_seen": date_str}
                else:
                    all_repos[name].setdefault("first_seen", date_str)

        current += timedelta(days=1)

    # 输出每周数据
    for week_key, repos_dict in sorted(weekly_data.items()):
        repos_list = sorted(repos_dict.values(), key=lambda x: x.get("stars", 0), reverse=True)
        (weekly_dir / f"{week_key}.json").write_text(
            json.dumps(repos_list, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # 输出每月数据
    for month_key, repos_dict in sorted(monthly_data.items()):
        repos_list = sorted(repos_dict.values(), key=lambda x: x.get("stars", 0), reverse=True)
        (monthly_dir / f"{month_key}.json").write_text(
            json.dumps(repos_list, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # 计算每个 repo 的上榜天数
    # 重新扫描统计
    trending_days = defaultdict(int)
    current = START_DATE
    while current <= END_DATE:
        date_str = current.strftime("%Y-%m-%d")
        month_str = current.strftime("%Y-%m")
        filepath = ARCHIVE_DIR / month_str / f"{date_str}.md"
        if filepath.exists():
            repos = parse_md_file(filepath)
            for r in repos:
                trending_days[r["name"]] += 1
        current += timedelta(days=1)

    # 输出去重后的全量 repo
    deduped = []
    for name, r in all_repos.items():
        r["trending_days"] = trending_days.get(name, 0)
        deduped.append(r)

    deduped.sort(key=lambda x: x.get("trending_days", 0), reverse=True)

    (OUTPUT_DIR / "all_repos_deduped.json").write_text(
        json.dumps(deduped, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 输出 trending_repos_top.md（上榜 >= 3 天的仓库）
    min_days = 3
    top_repos = [r for r in deduped if r.get("trending_days", 0) >= min_days]
    lines = [f"# GitHub Trending Repos (trending_days >= {min_days})"]
    lines.append(f"\n共 {len(top_repos)} 个仓库（筛选自 {len(deduped)} 个）\n")
    for r in top_repos:
        name = r.get("name", "")
        url = r.get("url", f"https://github.com/{name}")
        stars = r.get("stars", 0)
        days = r.get("trending_days", 0)
        lang = r.get("language", "Unknown")
        desc = r.get("description", "")
        # 截断过长描述
        if len(desc) > 100:
            desc = desc[:100]
        lines.append(f"- [{name}]({url}) - ⭐ {stars} | 🔥 {days}天 | {lang} | {desc}")
    lines.append("")
    (OUTPUT_DIR / "trending_repos_top.md").write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    # 打印统计
    print(f"时间范围: {START_DATE.date()} ~ {END_DATE.date()}")
    print(f"每日文件: {daily_count} 个 → daily/")
    print(f"每周文件: {len(weekly_data)} 个 → weekly/")
    print(f"每月文件: {len(monthly_data)} 个 → monthly/")
    print(f"去重 repo: {len(deduped)} 个 → all_repos_deduped.json")
    print(f"上榜最多: {deduped[0]['name']} ({deduped[0]['trending_days']} 天)")


if __name__ == "__main__":
    main()
