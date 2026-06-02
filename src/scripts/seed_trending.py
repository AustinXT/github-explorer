#!/usr/bin/env python3
"""读取 src/data/trending_snapshots.jsonl 灌入 db.sqlite。

数据流：
    src/data/trending_snapshots.jsonl (由 parse_trending.py 从外部 archive 生成，SoR)
        ↓ upsert
    db.sqlite.trending_repos + trending_snapshots

每行一个快照，自带完整字段：
    {"period_type","period_key","url","name","language","description","stars","forks","rank"}
    period_key:  daily → 'YYYY-MM-DD' / weekly → 'YYYY-Www' / monthly → 'YYYY-MM'

URL 入库前 rstrip('/').lower() 规范化（与 reports / user_starred 一致），
让 v_user_starred / reports.original_url 的 join 不需要 LOWER()。

幂等：同一 (period_type, period_key, url) 多次 seed 不重复（用 INSERT OR REPLACE）。
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOTS_FILE = ROOT / "src" / "data" / "trending_snapshots.jsonl"

sys.path.insert(0, str(ROOT / "src" / "scripts"))
from init_db import get_connection, ensure_schema, normalize_url  # noqa: E402


PERIOD_TYPES = ("daily", "weekly", "monthly")

# 校验 period_key 格式
PERIOD_KEY_PATTERNS = {
    "daily":   re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "weekly":  re.compile(r"^\d{4}-W\d{2}$"),
    "monthly": re.compile(r"^\d{4}-\d{2}$"),
}


def upsert_repo(conn: sqlite3.Connection, row: dict, normalized_url: str) -> None:
    """upsert trending_repos：URL 是 PK，已有则更新 name/language/description（保留最新观察值）。"""
    conn.execute(
        "INSERT INTO trending_repos (url, name, language, description) VALUES (?, ?, ?, ?) "
        "ON CONFLICT(url) DO UPDATE SET "
        "  name=excluded.name, language=excluded.language, description=excluded.description",
        (
            normalized_url,
            row.get("name", ""),
            row.get("language"),
            row.get("description") or "",
        ),
    )


def seed_snapshots(conn: sqlite3.Connection) -> tuple[int, dict[str, int]]:
    """读 trending_snapshots.jsonl 全量灌库。返回 (snapshot_count, per_period_counts)。"""
    if not SNAPSHOTS_FILE.is_file():
        print(f"❌ 缺少 {SNAPSHOTS_FILE.relative_to(ROOT)}", file=sys.stderr)
        return 0, {}
    n_snap = 0
    per_period: dict[str, int] = {pt: 0 for pt in PERIOD_TYPES}
    with SNAPSHOTS_FILE.open(encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"⚠️  skip 第 {lineno} 行: {e}")
                continue
            period_type = row.get("period_type")
            period_key = row.get("period_key")
            pattern = PERIOD_KEY_PATTERNS.get(period_type)
            if pattern is None:
                print(f"⚠️  skip 第 {lineno} 行: 未知 period_type '{period_type}'")
                continue
            if not period_key or not pattern.match(period_key):
                print(f"⚠️  skip 第 {lineno} 行: period_key '{period_key}' 不符合 {period_type} 格式")
                continue
            url = normalize_url(row.get("url"))
            if not url:
                continue
            upsert_repo(conn, row, url)
            conn.execute(
                "INSERT OR REPLACE INTO trending_snapshots "
                "(period_type, period_key, url, stars, forks, rank) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (
                    period_type,
                    period_key,
                    url,
                    int(row.get("stars") or 0),
                    int(row.get("forks") or 0),
                    int(row.get("rank") or 0),
                ),
            )
            n_snap += 1
            per_period[period_type] = per_period.get(period_type, 0) + 1
    return n_snap, per_period


def main() -> int:
    conn = get_connection()
    ensure_schema(conn)
    if conn.execute("SELECT COUNT(*) FROM schema_version WHERE version >= 3").fetchone()[0] == 0:
        print("❌ schema v3 未应用，请检查 init_db.py", file=sys.stderr)
        return 1

    # 全量重建：先清空所有快照与 repo 池
    try:
        with conn:
            conn.execute("DELETE FROM trending_snapshots")
            conn.execute("DELETE FROM trending_repos")
    except sqlite3.IntegrityError as e:
        print(f"❌ 清空旧数据失败: {e}", file=sys.stderr)
        return 2

    try:
        with conn:
            grand_total, per_period = seed_snapshots(conn)
    except sqlite3.IntegrityError as e:
        print(f"❌ seed 失败（schema 约束）: {e}", file=sys.stderr)
        return 3

    for pt in PERIOD_TYPES:
        print(f"  {pt:<8} {per_period.get(pt, 0):>5} 快照行")

    n_repos = conn.execute("SELECT COUNT(*) FROM trending_repos").fetchone()[0]
    print(f"✅ trending 灌库完成: {n_repos} 个唯一 repo，{grand_total} 条快照")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
