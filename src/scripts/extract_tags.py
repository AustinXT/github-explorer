#!/usr/bin/env python3
"""基于 src/data/tag-rules.yaml 的关键词，对 db.sqlite 中 reports 自动打标签，写入 report_tags。

数据流（详见 .claude/plans/splendid-swinging-meteor.md）：
    src/data/tag-rules.yaml  ──┐
    src/data/tags.yaml.manual ─┤  启动 seed → tags / tag_rules / report_tag_locks
    db.sqlite.reports          ┤
                              parse + match → report_tags

tags.yaml 不再由本脚本写出，统一由 `scripts/init_db.py export-json` 从 DB dump。
site/ 仍读 YAML 不变。

「整套保护」语义保持不变：
    tags.yaml.manual: ['continuedev_continue', ...] 中的 slug，重跑本脚本不会改动其标签。
    在 DB 中由 report_tag_locks 表承载这个语义；受保护 slug 的 report_tags 行被原样保留。

'uncategorized' 是 site/ 用的兜底字符串，不入 tags / report_tags 表。
"""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RULES_FILE = ROOT / "src" / "data" / "tag-rules.yaml"
TAGS_FILE = ROOT / "src" / "data" / "tags.yaml"

sys.path.insert(0, str(ROOT / "src" / "scripts"))
from init_db import get_connection, ensure_schema  # noqa: E402


def load_rules() -> list[dict]:
    rules = yaml.safe_load(RULES_FILE.read_text(encoding="utf-8")) or []
    if not isinstance(rules, list):
        raise SystemExit("tag-rules.yaml 顶层必须是 list")
    return rules


def load_manual_slugs() -> list[str]:
    """从 tags.yaml 读 manual 列表。文件不存在或字段缺失时返回 []。"""
    if not TAGS_FILE.exists():
        return []
    doc = yaml.safe_load(TAGS_FILE.read_text(encoding="utf-8")) or {}
    return list(doc.get("manual") or [])


def seed_tags_and_rules(conn: sqlite3.Connection, rules: list[dict]) -> None:
    """把 tag-rules.yaml 全量 sync 到 tags + tag_rules 表。
    使用 DELETE + INSERT 而非 UPSERT，以便从 DB 中移除已从 YAML 删除的旧 tag。"""
    with conn:
        conn.execute("DELETE FROM tag_rules")
        # 不能直接 DELETE FROM tags（report_tags 有外键引用）。
        # 采取「标记 + diff」策略：先收集 YAML 中的 tag 集合，删 DB 中不在 YAML 的（且无 report_tags 引用的）。
        yaml_tags = {r["tag"] for r in rules if r.get("tag")}
        db_tags = {row[0] for row in conn.execute("SELECT tag FROM tags").fetchall()}
        # 删除 YAML 中已移除的 tag。若仍被 report_tags 引用则 FK ON DELETE CASCADE 会级联清掉
        # —— 但这是脚本作者的预期：tag 规则被删 ⇒ 其上的关联也清理。
        for t in db_tags - yaml_tags:
            conn.execute("DELETE FROM tags WHERE tag=?", (t,))
        # upsert tags + 重建 tag_rules
        for i, r in enumerate(rules):
            tag = r.get("tag")
            if not tag:
                continue
            label = r.get("label") or tag
            conn.execute(
                "INSERT INTO tags (tag, label, sort_order) VALUES (?, ?, ?) "
                "ON CONFLICT(tag) DO UPDATE SET label=excluded.label, sort_order=excluded.sort_order",
                (tag, label, i),
            )
            for kw in r.get("match") or []:
                conn.execute(
                    "INSERT OR IGNORE INTO tag_rules (tag, keyword) VALUES (?, ?)",
                    (tag, kw.lower()),
                )


def seed_locks(conn: sqlite3.Connection, manual_slugs: list[str]) -> None:
    """把 tags.yaml.manual 全量 sync 到 report_tag_locks 表。"""
    with conn:
        conn.execute("DELETE FROM report_tag_locks")
        for slug in manual_slugs:
            # 仅当该 slug 在 reports 表里时才插入（外键约束保证）
            row = conn.execute("SELECT 1 FROM reports WHERE slug=?", (slug,)).fetchone()
            if row:
                conn.execute("INSERT INTO report_tag_locks (slug) VALUES (?)", (slug,))


def assemble_searchtext(row: dict) -> str:
    parts: list[str] = []
    for key in ("title", "summary", "original_url", "heat", "stage"):
        v = row.get(key)
        if v:
            parts.append(str(v))
    parts.extend(row.get("highlights") or [])
    return " ".join(parts).lower()


def match_tags(text: str, rules: list[dict]) -> list[str]:
    tags: list[str] = []
    for rule in rules:
        tag = rule.get("tag")
        kws = rule.get("match") or []
        if not tag or not kws:
            continue
        if any(kw.lower() in text for kw in kws):
            tags.append(tag)
    return tags  # 注意：空列表表示 uncategorized，由 dump_tags_entries 兜底，不入 DB


def fetch_reports_with_highlights(conn: sqlite3.Connection) -> list[dict]:
    out: list[dict] = []
    rows = conn.execute(
        "SELECT slug, title, summary, original_url, heat, stage FROM reports ORDER BY slug"
    ).fetchall()
    for slug, title, summary, original_url, heat, stage in rows:
        hl = [r[0] for r in conn.execute(
            "SELECT text FROM report_highlights WHERE slug=? ORDER BY position", (slug,)
        ).fetchall()]
        out.append({
            "slug": slug,
            "title": title,
            "summary": summary,
            "original_url": original_url,
            "heat": heat,
            "stage": stage,
            "highlights": hl,
        })
    return out


def write_report_tags(conn: sqlite3.Connection, slug_to_tags: dict[str, list[str]]) -> None:
    """非锁定 slug 的 report_tags 全量重写；锁定 slug 保留 DB 中原值。"""
    with conn:
        locked = {row[0] for row in conn.execute("SELECT slug FROM report_tag_locks").fetchall()}
        for slug, tags in slug_to_tags.items():
            if slug in locked:
                continue
            conn.execute("DELETE FROM report_tags WHERE slug=?", (slug,))
            for tag in tags:
                if tag == "uncategorized":
                    continue
                conn.execute(
                    "INSERT INTO report_tags (slug, tag) VALUES (?, ?)",
                    (slug, tag),
                )


def main() -> int:
    rules = load_rules()
    manual_slugs = load_manual_slugs()

    conn = get_connection()
    ensure_schema(conn)

    # 检查 reports 已 seed
    n = conn.execute("SELECT COUNT(*) FROM reports").fetchone()[0]
    if n == 0:
        print("❌ reports 表为空，请先运行 build_reports_index.py", file=sys.stderr)
        return 1

    try:
        seed_tags_and_rules(conn, rules)
        seed_locks(conn, manual_slugs)
    except sqlite3.IntegrityError as e:
        print(f"❌ seed 失败（schema 约束违规）: {e}", file=sys.stderr)
        return 2

    reports = fetch_reports_with_highlights(conn)
    slug_to_tags: dict[str, list[str]] = {}
    stats = {"auto": 0, "manual_kept": 0, "uncategorized": 0}
    locked = {row[0] for row in conn.execute("SELECT slug FROM report_tag_locks").fetchall()}

    for r in reports:
        slug = r["slug"]
        if slug in locked:
            stats["manual_kept"] += 1
            continue
        text = assemble_searchtext(r)
        tags = match_tags(text, rules)
        if not tags:
            stats["uncategorized"] += 1
        else:
            stats["auto"] += 1
        slug_to_tags[slug] = tags

    try:
        write_report_tags(conn, slug_to_tags)
    except sqlite3.IntegrityError as e:
        print(f"❌ 写入 report_tags 失败: {e}", file=sys.stderr)
        return 3

    # 统计：每个 tag 命中数
    tag_count = dict(conn.execute(
        "SELECT tag, COUNT(*) FROM report_tags GROUP BY tag ORDER BY COUNT(*) DESC"
    ).fetchall())
    conn.close()

    print(f"✅ 写入 report_tags → db.sqlite")
    print(f"   自动命中: {stats['auto']}, 保留人工: {stats['manual_kept']}, 未分类: {stats['uncategorized']}")
    print("   各标签分布（命中报告数）:")
    for t, n in tag_count.items():
        print(f"     {t:<22} {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
