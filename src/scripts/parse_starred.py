#!/usr/bin/env python3
"""从 src/data/starred_seed.json 读取大牛 Star 快照，配合 src/data/users.yaml 写入 db.sqlite。

数据流：
    src/data/users.yaml        ──┐  (用户清单 + name/bio/tags/排序，权威源)
    src/data/starred_seed.json ──┤  parse → users / user_tags / user_starred / user_starred_snapshot
                                  └─ reportSlug 派生由 v_user_starred 视图完成（URL 已规范化）

注意 SoR 与导出的分离（同 publish_history.jsonl ≠ reports.json）：
    - starred_seed.json 是 SoR（手工/外部 Starlight2 抓取维护），本脚本只读它、不回写。
    - starred.json 仍由 `scripts/init_db.py export-json` 从 DB dump（含派生 reportSlug），供 site/ 读取。

starred_seed.json 结构：
    {"users": [{"login", "fetchedAt", "rangeStart", "items": [
        {"name", "url", "stars", "description", "starredAt"}, ...]}, ...]}
（用户级 name/bio/tags/排序以 users.yaml 为准，seed 内同名字段忽略。）
"""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
USERS_FILE = ROOT / "src" / "data" / "users.yaml"
SEED_FILE = ROOT / "src" / "data" / "starred_seed.json"

sys.path.insert(0, str(ROOT / "src" / "scripts"))
from init_db import get_connection, ensure_schema, normalize_url  # noqa: E402


def load_seed() -> dict[str, dict]:
    """读 starred_seed.json，返回 {login: {fetchedAt, rangeStart, items}}。"""
    doc = json.loads(SEED_FILE.read_text(encoding="utf-8"))
    seed: dict[str, dict] = {}
    for u in doc.get("users") or []:
        login = u.get("login")
        if not login:
            continue
        seed[login] = {
            "fetchedAt": u.get("fetchedAt"),
            "rangeStart": u.get("rangeStart"),
            "items": u.get("items") or [],
        }
    return seed


def seed_users(conn: sqlite3.Connection, users: list[dict]) -> None:
    """全量重建 users + user_tags（保持与 users.yaml 同步）。

    user_starred 通过 ON DELETE CASCADE 也会被一并清理，下一步 seed_starred 重新写入。"""
    with conn:
        # 先 DELETE users —— FK CASCADE 会清掉 user_tags / user_starred / user_starred_snapshot
        conn.execute("DELETE FROM users")
        for i, u in enumerate(users):
            login = u.get("login")
            if not login:
                continue
            conn.execute(
                "INSERT INTO users (login, name, bio, sort_order) VALUES (?, ?, ?, ?)",
                (login, u.get("name") or login, u.get("bio"), i),
            )
            for j, tag in enumerate(u.get("tags") or []):
                conn.execute(
                    "INSERT OR IGNORE INTO user_tags (login, tag, position) VALUES (?, ?, ?)",
                    (login, tag, j),
                )


def write_starred(conn: sqlite3.Connection, login: str, parsed: dict) -> int:
    """写一位大牛的 starred 快照。返回写入的 item 数。"""
    with conn:
        # snapshot 头信息
        conn.execute(
            "INSERT OR REPLACE INTO user_starred_snapshot (login, fetched_at, range_start) "
            "VALUES (?, ?, ?)",
            (login, parsed["fetchedAt"], parsed["rangeStart"]),
        )
        # items 全量重写（同一 login 下）
        conn.execute("DELETE FROM user_starred WHERE login=?", (login,))
        n = 0
        for pos, item in enumerate(parsed["items"]):
            url = normalize_url(item["url"])
            conn.execute(
                "INSERT OR IGNORE INTO user_starred "
                "(login, url, name, stars, description, starred_at, position) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (login, url, item["name"], item["stars"], item["description"], item["starredAt"], pos),
            )
            n += 1
        return n


def main() -> int:
    if not USERS_FILE.exists():
        print(f"❌ 缺少 {USERS_FILE}", file=sys.stderr)
        return 1
    if not SEED_FILE.exists():
        print(f"❌ 缺少 {SEED_FILE}", file=sys.stderr)
        return 1
    users_doc = yaml.safe_load(USERS_FILE.read_text(encoding="utf-8")) or {}
    users = users_doc.get("users") or []
    seed = load_seed()

    conn = get_connection()
    ensure_schema(conn)
    try:
        seed_users(conn, users)
    except sqlite3.IntegrityError as e:
        print(f"❌ seed users 失败: {e}", file=sys.stderr)
        return 2

    total_items = 0
    per_user: list[tuple[str, str | None, int]] = []
    for u in users:
        login = u.get("login")
        if not login:
            continue
        parsed = seed.get(login)
        if parsed is None:
            print(f"⚠️  {login}: starred_seed.json 中缺少该用户的快照")
            per_user.append((login, None, 0))
            continue
        try:
            n = write_starred(conn, login, parsed)
        except sqlite3.IntegrityError as e:
            print(f"❌ {login}: 写入 user_starred 失败: {e}", file=sys.stderr)
            return 3
        total_items += n
        per_user.append((login, parsed["fetchedAt"], n))

    # 统计已分析（reportSlug 不为 NULL）的命中数 —— 通过视图查
    total_analyzed = conn.execute(
        "SELECT COUNT(*) FROM v_user_starred WHERE report_slug IS NOT NULL"
    ).fetchone()[0]
    conn.close()

    print(f"✅ 写入 {len(users)} 位大牛 → db.sqlite (users + user_starred*)")
    print(f"   总 starred 条目: {total_items}")
    print(f"   其中已分析（视图 v_user_starred 命中）: {total_analyzed}")
    for login, fetched, n in per_user:
        print(f"     {login:<14} fetched={fetched}  items={n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
