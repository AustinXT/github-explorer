#!/usr/bin/env python3
"""用 tmp/wechat_match.json 的 mapping 写回 src/publish.md。

对每条 mapping：
  · 若 slug 已在 publish.md 表里：状态列 → send_date（除非已是日期且不同，则保留 + 警告）
                                  标题列 → 公众号标题（始终覆盖，按用户要求）
  · 若 slug 不在表里：在「## 不发布列表」之前新增一行

「## 不发布列表」段下的所有内容原样保留。

用法：
  scripts/apply_wechat_mapping.py             # dry-run
  scripts/apply_wechat_mapping.py --apply
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PUBLISH_MD = REPO_ROOT / "src" / "publish.md"
MATCH_JSON = REPO_ROOT / "tmp" / "wechat_match.json"

ROW_RE = re.compile(
    r"^\|\s*\[(?P<filename>[^\]]+\.md)\]\([^)]*\)\s*\|\s*(?P<title>[^|]+?)\s*\|\s*(?P<status>[^|]+?)\s*\|\s*$"
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def build_row(slug: str, title: str, status: str) -> str:
    filename = f"{slug}.md"
    return f"| [{filename}](analysis_report/{filename}) | {title} | {status} |\n"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--apply", action="store_true", help="真改 publish.md；默认 dry-run")
    p.add_argument("--mapping", type=Path, default=MATCH_JSON)
    p.add_argument("--publish-md", type=Path, default=PUBLISH_MD)
    args = p.parse_args()

    if not args.mapping.is_file():
        sys.exit(f"ERR: 找不到 {args.mapping}，先跑 scripts/match_wechat_to_slugs.py")

    data = json.loads(args.mapping.read_text(encoding="utf-8"))
    entries: list[dict] = data.get("entries", [])
    # 同 slug 多条：取 send_date 最大的（最新发布的胜出）
    by_slug: dict[str, dict] = {}
    for e in entries:
        slug = e.get("slug")
        if not slug:
            continue
        prev = by_slug.get(slug)
        if prev is None or (e.get("send_date") or "") > (prev.get("send_date") or ""):
            by_slug[slug] = e
    print(f"mapping 条目 {len(entries)}，去重后 {len(by_slug)} 个 slug")

    text = args.publish_md.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    insertion_idx = None      # 「## 不发布列表」前一行的索引
    rows_in_publish: dict[str, tuple[int, str, str, str]] = {}  # slug → (line_no, filename, title, status)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("## 不发布列表"):
            insertion_idx = i
            break
        m = ROW_RE.match(line)
        if not m:
            continue
        filename = m.group("filename").strip()
        slug = filename[:-3] if filename.endswith(".md") else filename
        rows_in_publish[slug] = (i, filename, m.group("title").strip(), m.group("status").strip())
    if insertion_idx is None:
        # 没有「不发布列表」段，则插到文件末尾
        insertion_idx = len(lines)

    changes_update: list[dict] = []   # 现有行的变更
    keep_unchanged: list[str] = []    # 已对齐无需变更的 slug
    additions: list[dict] = []        # 待新增的行
    conflicts: list[dict] = []        # 现有日期跟公众号 send_date 冲突的

    for slug, e in by_slug.items():
        wx_title = e.get("wechat_title") or ""
        wx_date = e.get("send_date") or ""
        existing = rows_in_publish.get(slug)
        if existing is None:
            additions.append({"slug": slug, "title": wx_title, "date": wx_date})
            continue
        line_no, filename, old_title, old_status = existing
        # 状态列处理
        if DATE_RE.match(old_status):
            new_status = old_status  # 已是日期，保留
            if wx_date and old_status != wx_date:
                conflicts.append({
                    "slug": slug, "publish_md_date": old_status, "wechat_send_date": wx_date,
                })
        elif old_status == "待发布":
            new_status = wx_date or old_status
        else:
            new_status = wx_date or old_status
        new_title = wx_title or old_title
        if new_title == old_title and new_status == old_status:
            keep_unchanged.append(slug)
            continue
        changes_update.append({
            "slug": slug, "line_no": line_no, "filename": filename,
            "old_title": old_title, "new_title": new_title,
            "old_status": old_status, "new_status": new_status,
        })

    # 已发布表里有但 mapping 没命中的（保留原状）
    not_in_mapping = sorted(set(rows_in_publish) - set(by_slug))

    # 打印 diff summary
    print()
    print("=" * 70)
    print(f"待新增 (publish.md 没有的 slug)       : {len(additions)} 条")
    print(f"待更新 (现有行的标题/状态有变化)      : {len(changes_update)} 条")
    print(f"已对齐 (现有行跟公众号侧一致)         : {len(keep_unchanged)} 条")
    print(f"日期冲突 (publish.md 与公众号不一致)  : {len(conflicts)} 条")
    print(f"publish.md 有但 mapping 没命中        : {len(not_in_mapping)} 条")
    print("=" * 70)

    if additions:
        print(f"\n[待新增 {len(additions)} 条]  按 send_date desc 排")
        for a in sorted(additions, key=lambda x: x["date"] or "", reverse=True)[:20]:
            print(f"  + {a['slug']:50s}  {a['date']}  «{a['title'][:36]}»")
        if len(additions) > 20:
            print(f"  ... 还有 {len(additions) - 20} 条")

    if changes_update:
        print(f"\n[待更新 {len(changes_update)} 条]")
        for c in changes_update:
            marks = []
            if c["old_status"] != c["new_status"]:
                marks.append(f"状态 {c['old_status']!r}→{c['new_status']!r}")
            if c["old_title"] != c["new_title"]:
                marks.append(f"标题 «{c['old_title'][:24]}»→«{c['new_title'][:24]}»")
            print(f"  ~ {c['slug']:50s}  {' / '.join(marks)}")

    if conflicts:
        print(f"\n[⚠ 日期冲突 {len(conflicts)} 条] publish.md 现有日期与公众号 send_date 不一致 (保留 publish.md)")
        for c in conflicts:
            print(f"    {c['slug']:50s}  publish.md={c['publish_md_date']}  wechat={c['wechat_send_date']}")

    if not_in_mapping:
        print(f"\n[publish.md 有但 mapping 没命中 {len(not_in_mapping)} 条] 保留原状")
        for s in not_in_mapping[:10]:
            print(f"    {s}")
        if len(not_in_mapping) > 10:
            print(f"    ... 还有 {len(not_in_mapping) - 10} 条")

    if not args.apply:
        print("\n(dry-run。加 --apply 真正写入 publish.md。)")
        return 0

    if not changes_update and not additions:
        print("\n没有需要写入的变更。")
        return 0

    # 应用变更
    new_lines = list(lines)
    for c in changes_update:
        new_lines[c["line_no"]] = build_row(c["slug"], c["new_title"], c["new_status"])

    # 新增行：在 insertion_idx 前插入（按 send_date desc 排）
    addition_rows = [
        build_row(a["slug"], a["title"], a["date"] or "待发布")
        for a in sorted(additions, key=lambda x: x["date"] or "", reverse=True)
    ]
    # 插入前确保空白格式正常（如果 insertion_idx 处是空行就直接插入；否则插入后跟空行）
    new_lines = new_lines[:insertion_idx] + addition_rows + new_lines[insertion_idx:]

    tmp = args.publish_md.with_suffix(args.publish_md.suffix + ".tmp")
    tmp.write_text("".join(new_lines), encoding="utf-8")
    tmp.replace(args.publish_md)
    print(f"\n✅ 已写入 {args.publish_md.relative_to(REPO_ROOT)}")
    print(f"   新增 {len(additions)} 行 + 更新 {len(changes_update)} 行")
    print("\n后续：python3 scripts/build_reports_index.py  # 同步进 reports.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
