#!/usr/bin/env python3
"""解析 src/starred_repo/{login}.md 数据快照，配合 src/data/users.yaml 写入 db.sqlite。

数据流：
    src/data/users.yaml          ──┐
    src/starred_repo/{login}.md  ──┤  parse → users / user_tags / user_starred / user_starred_snapshot
                                    └─ reportSlug 派生由 v_user_starred 视图完成（URL 已规范化，无需 join 时 lower）

starred.json 不再由本脚本写出，统一由 `scripts/init_db.py export-json` 从 DB dump。
site/ 仍读 JSON 不变。

输入行格式：
    - [owner/repo](url) ⭐stars — description [YYYY-MM-DD]
"""
from __future__ import annotations

import re
import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
USERS_FILE = ROOT / "src" / "data" / "users.yaml"
STARRED_DIR = ROOT / "src" / "starred_repo"

sys.path.insert(0, str(ROOT / "scripts"))
from init_db import get_connection, ensure_schema, normalize_url  # noqa: E402


LINE_RE = re.compile(
    r"^\s*[-*]\s+\[([^\]]+)\]\(([^)]+)\)\s*⭐\s*(\d+)\s*(?:—|--|-)\s*(.*?)\s*\[(\d{4}-\d{2}-\d{2})\]\s*$"
)
HEADER_RE = re.compile(
    r"^数据获取日期:\s*(\d{4}-\d{2}-\d{2})\s*\|\s*筛选范围:\s*(\d{4}-\d{2}-\d{2})\s*至今"
)


def parse_starred_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fetched_at = None
    range_start = None
    items: list[dict] = []

    for line in text.splitlines():
        if fetched_at is None:
            m = HEADER_RE.match(line.strip())
            if m:
                fetched_at, range_start = m.group(1), m.group(2)
                continue
        m = LINE_RE.match(line)
        if m:
            name, url, stars, desc, star_date = m.groups()
            items.append({
                "name": name.strip(),
                "url": url.strip(),
                "stars": int(stars),
                "description": desc.strip(),
                "starredAt": star_date,
            })

    return {"fetchedAt": fetched_at, "rangeStart": range_start, "items": items}


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
    users_doc = yaml.safe_load(USERS_FILE.read_text(encoding="utf-8")) or {}
    users = users_doc.get("users") or []

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
        path = STARRED_DIR / f"{login}.md"
        if not path.exists():
            print(f"⚠️  {login}: 缺少 starred 快照 {path.relative_to(ROOT)}")
            per_user.append((login, None, 0))
            continue
        parsed = parse_starred_file(path)
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
