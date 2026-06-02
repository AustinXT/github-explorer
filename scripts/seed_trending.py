#!/usr/bin/env python3
"""遍历 src/trending_repo/{daily,weekly,monthly}/*.json 灌入 db.sqlite。

数据流：
    src/trending_repo/{period}/*.json (由 parse_trending.py 从外部 archive 生成)
        ↓ upsert
    db.sqlite.trending_repos + trending_snapshots

period_key 直接取文件名（去 .json）：
    daily   → 'YYYY-MM-DD'
    weekly  → 'YYYY-Www'
    monthly → 'YYYY-MM'

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

ROOT = Path(__file__).resolve().parent.parent
TRENDING_DIR = ROOT / "src" / "trending_repo"

sys.path.insert(0, str(ROOT / "scripts"))
from init_db import get_connection, ensure_schema, normalize_url  # noqa: E402


PERIOD_TYPES = ("daily", "weekly", "monthly")

# 校验 period_key 格式
PERIOD_KEY_PATTERNS = {
    "daily":   re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "weekly":  re.compile(r"^\d{4}-W\d{2}$"),
    "monthly": re.compile(r"^\d{4}-\d{2}$"),
}


def upsert_repo(conn: sqlite3.Connection, item: dict, normalized_url: str) -> None:
    """upsert trending_repos：URL 是 PK，已有则更新 name/language/description（保留最新观察值）。"""
    conn.execute(
        "INSERT INTO trending_repos (url, name, language, description) VALUES (?, ?, ?, ?) "
        "ON CONFLICT(url) DO UPDATE SET "
        "  name=excluded.name, language=excluded.language, description=excluded.description",
        (
            normalized_url,
            item.get("name", ""),
            item.get("language"),
            item.get("description") or "",
        ),
    )


def seed_period(conn: sqlite3.Connection, period_type: str) -> tuple[int, int]:
    """seed 一个 period_type 下的所有 JSON 文件。返回 (snapshot_count, file_count)。"""
    period_dir = TRENDING_DIR / period_type
    if not period_dir.is_dir():
        print(f"⚠️  {period_dir.relative_to(ROOT)} 不存在，跳过", file=sys.stderr)
        return 0, 0
    files = sorted(period_dir.glob("*.json"))
    pattern = PERIOD_KEY_PATTERNS[period_type]
    n_snap = 0
    n_file = 0
    for f in files:
        period_key = f.stem
        if not pattern.match(period_key):
            print(f"⚠️  skip {f.relative_to(ROOT)}: period_key '{period_key}' 不符合 {period_type} 格式")
            continue
        try:
            items = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(f"⚠️  skip {f.relative_to(ROOT)}: {e}")
            continue
        if not isinstance(items, list):
            print(f"⚠️  skip {f.relative_to(ROOT)}: 顶层不是 list")
            continue
        for rank, item in enumerate(items, start=1):
            url = normalize_url(item.get("url"))
            if not url:
                continue
            upsert_repo(conn, item, url)
            conn.execute(
                "INSERT OR REPLACE INTO trending_snapshots "
                "(period_type, period_key, url, stars, forks, rank) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (
                    period_type,
                    period_key,
                    url,
                    int(item.get("stars") or 0),
                    int(item.get("forks") or 0),
                    rank,
                ),
            )
            n_snap += 1
        n_file += 1
    return n_snap, n_file


def main() -> int:
    conn = get_connection()
    ensure_schema(conn)
    if conn.execute("SELECT COUNT(*) FROM schema_version WHERE version >= 3").fetchone()[0] == 0:
        print("❌ schema v3 未应用，请检查 init_db.py", file=sys.stderr)
        return 1

    # 全量重建：先清空所有快照（trending_repos 在 trending_snapshots CASCADE 下保留 URL 不再被引用的旧记录，
    # 但 trending_snapshots 全清后 trending_repos 会变成「历史 URL 池」—— 这不影响功能）。
    # 更干净的做法：也清 trending_repos
    try:
        with conn:
            conn.execute("DELETE FROM trending_snapshots")
            conn.execute("DELETE FROM trending_repos")
    except sqlite3.IntegrityError as e:
        print(f"❌ 清空旧数据失败: {e}", file=sys.stderr)
        return 2

    grand_total = 0
    for pt in PERIOD_TYPES:
        try:
            with conn:
                n_snap, n_file = seed_period(conn, pt)
        except sqlite3.IntegrityError as e:
            print(f"❌ seed {pt} 失败（schema 约束）: {e}", file=sys.stderr)
            return 3
        grand_total += n_snap
        print(f"  {pt:<8} {n_file:>4} 文件, {n_snap:>5} 快照行")

    n_repos = conn.execute("SELECT COUNT(*) FROM trending_repos").fetchone()[0]
    print(f"✅ trending 灌库完成: {n_repos} 个唯一 repo，{grand_total} 条快照")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
