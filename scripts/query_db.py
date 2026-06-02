#!/usr/bin/env python3
"""命令行 SQL 查询工具：在 db.sqlite 上跑 ad-hoc 分析。

这是 SQLite 引入后「数据规整 + 跨表分析」价值的主要兑现载体。
site/ 不直接受益（仍读 JSON），但开发者可用本工具做：
    - 报告分布统计（按 author / language / heat / mtime）
    - 数据规整性巡检（重复 URL / 孤立标签 / 非规范字段）
    - 跨表关联（大牛 star 但未分析、Trending 上榜但未分析等，待阶段 2/3 解锁）

用法：
    python3 scripts/query_db.py --sql "SELECT COUNT(*) FROM reports"
    python3 scripts/query_db.py --preset by-language
    python3 scripts/query_db.py --preset by-author
    python3 scripts/query_db.py --preset tag-distribution
    python3 scripts/query_db.py --preset orphan-urls
    python3 scripts/query_db.py --list-presets
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from init_db import DB_PATH  # noqa: E402


PRESETS: dict[str, tuple[str, str]] = {
    "by-language": (
        "按语言分布",
        "SELECT language, COUNT(*) AS n FROM reports "
        "WHERE language IS NOT NULL GROUP BY language ORDER BY n DESC",
    ),
    "by-author": (
        "按 author 分布（slug 前缀）",
        "SELECT SUBSTR(slug, 1, INSTR(slug, '_') - 1) AS author, COUNT(*) AS n "
        "FROM reports WHERE INSTR(slug, '_') > 0 "
        "GROUP BY author ORDER BY n DESC LIMIT 30",
    ),
    "by-mtime": (
        "按月份发表数",
        "SELECT SUBSTR(mtime, 1, 7) AS month, COUNT(*) AS n "
        "FROM reports GROUP BY month ORDER BY month DESC",
    ),
    "by-heat": (
        "按热度等级分布",
        "SELECT COALESCE(heat, '未标') AS heat, COUNT(*) AS n "
        "FROM reports GROUP BY heat ORDER BY n DESC",
    ),
    "tag-distribution": (
        "标签分布（含未分类）",
        "SELECT COALESCE(rt.tag, 'uncategorized') AS tag, COUNT(DISTINCT r.slug) AS n "
        "FROM reports r LEFT JOIN report_tags rt USING(slug) "
        "GROUP BY tag ORDER BY n DESC",
    ),
    "tag-pairs": (
        "标签共现 Top 20",
        "SELECT t1.tag AS a, t2.tag AS b, COUNT(*) AS n "
        "FROM report_tags t1 JOIN report_tags t2 USING(slug) "
        "WHERE t1.tag < t2.tag GROUP BY a, b ORDER BY n DESC LIMIT 20",
    ),
    "orphan-urls": (
        "数据规整巡检：缺失 original_url 的报告",
        "SELECT slug, title FROM reports WHERE original_url IS NULL ORDER BY mtime DESC",
    ),
    "unhealthy-published": (
        "数据规整巡检：published_state 与 published_at 不匹配",
        "SELECT slug, published_state, published_at FROM reports "
        "WHERE (published_state = 'published' AND published_at IS NULL) "
        "OR (published_state IS NULL AND published_at IS NOT NULL)",
    ),
    "publish-summary": (
        "发布漏斗：分析→待发布→已发布的转化",
        "SELECT COALESCE(published_state, 'untouched') AS state, COUNT(*) AS n "
        "FROM reports GROUP BY state ORDER BY n DESC",
    ),
    "stars-top": (
        "Star 数 Top 20",
        "SELECT slug, stars, language FROM reports "
        "WHERE stars IS NOT NULL ORDER BY stars DESC LIMIT 20",
    ),
}


def print_table(headers: list[str], rows: list[tuple]) -> None:
    if not rows:
        print("(no rows)")
        return
    widths = [len(h) for h in headers]
    str_rows = [[("" if v is None else str(v)) for v in row] for row in rows]
    for row in str_rows:
        for i, v in enumerate(row):
            widths[i] = max(widths[i], len(v))
    fmt = "  ".join(f"{{:<{w}}}" for w in widths)
    print(fmt.format(*headers))
    print("  ".join("-" * w for w in widths))
    for row in str_rows:
        print(fmt.format(*row))
    print(f"\n({len(rows)} row{'s' if len(rows) != 1 else ''})")


def run_sql(sql: str) -> int:
    if not DB_PATH.exists():
        print(f"❌ {DB_PATH} 不存在，先运行：python3 scripts/init_db.py init", file=sys.stderr)
        return 1
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        cur = conn.execute(sql)
        headers = [d[0] for d in cur.description] if cur.description else []
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(f"❌ SQL 错误: {e}", file=sys.stderr)
        return 2
    finally:
        conn.close()
    print_table(headers, rows)
    return 0


def list_presets() -> int:
    print("可用预设查询（--preset <name>）：")
    for name in sorted(PRESETS):
        desc, _ = PRESETS[name]
        print(f"  {name:<22} {desc}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--sql", help="任意 SQL 查询")
    g.add_argument("--preset", help="使用预设查询")
    g.add_argument("--list-presets", action="store_true", help="列出所有预设")
    args = p.parse_args(argv)

    if args.list_presets:
        return list_presets()
    if args.preset:
        if args.preset not in PRESETS:
            print(f"❌ 未知 preset: {args.preset}", file=sys.stderr)
            list_presets()
            return 1
        desc, sql = PRESETS[args.preset]
        print(f"=== {desc} ===")
        return run_sql(sql)
    return run_sql(args.sql)


if __name__ == "__main__":
    raise SystemExit(main())
