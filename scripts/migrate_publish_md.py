#!/usr/bin/env python3
"""一次性把 src/publish.md 的发布记录导出为 src/data/publish_history.jsonl。

执行后：
  - publish_history.jsonl 成为发布历史的 SoR（append-only）
  - publish.md 转为只读归档（README 标注）；auto-analyze.yml 改调 record_publish.py append jsonl

覆盖 publish.md 中三种行格式（build_reports_index.parse_publish_index 已修复）：
  1. 4 列链接行 / published
  2. 2 列链接行 / excluded
  3. 3 列裸文件名行 / pending (auto-analyze 追加的「已入草稿」)

recorded_at 取值：
  - 有 published_at → published_at + 'T00:00:00Z'
  - 否则 → publish.md 文件 mtime 的 ISO 字符串

幂等：append 之前先去重，若 jsonl 已存在同 (slug, state, published_at) 组合则跳过该行。
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLISH_MD = ROOT / "src" / "publish.md"
PUBLISH_JSONL = ROOT / "src" / "data" / "publish_history.jsonl"

sys.path.insert(0, str(ROOT / "src" / "scripts"))
from build_reports_index import parse_publish_index  # noqa: E402


def existing_keys(jsonl_path: Path) -> set[tuple]:
    """已存在的 (slug, state, published_at) 集合，用于去重幂等。"""
    if not jsonl_path.exists():
        return set()
    out: set[tuple] = set()
    for line in jsonl_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        out.add((obj.get("slug"), obj.get("state"), obj.get("published_at")))
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dry-run", action="store_true", help="只打印将写入的行，不修改 jsonl")
    p.add_argument("--out", type=Path, default=PUBLISH_JSONL, help=f"目标 jsonl 路径，默认 {PUBLISH_JSONL.relative_to(ROOT)}")
    args = p.parse_args(argv)

    if not PUBLISH_MD.exists():
        print(f"❌ 找不到 {PUBLISH_MD}", file=sys.stderr)
        return 1

    md_mtime = datetime.fromtimestamp(PUBLISH_MD.stat().st_mtime, tz=timezone.utc).isoformat()
    publish_index = parse_publish_index()

    seen = existing_keys(args.out) if not args.dry_run else set()
    new_lines: list[dict] = []
    skipped = 0
    for slug, info in publish_index.items():
        state = info.get("state")
        if state is None:
            continue
        pub_at = info.get("at")
        key = (slug, state, pub_at)
        if key in seen:
            skipped += 1
            continue
        recorded_at = f"{pub_at}T00:00:00Z" if pub_at else md_mtime
        new_lines.append({
            "recorded_at": recorded_at,
            "slug": slug,
            "title": info.get("title"),
            "state": state,
            "published_at": pub_at,
            "reason": info.get("reason"),
            "ci_run_id": None,
        })

    # 按 recorded_at 排序输出（让 jsonl 时间序列更清晰）
    new_lines.sort(key=lambda r: (r["recorded_at"], r["slug"]))

    if args.dry_run:
        print(f"# Dry-run：将向 {args.out.relative_to(ROOT)} append {len(new_lines)} 行（已存在跳过 {skipped} 行）")
        for line in new_lines[:5]:
            print(json.dumps(line, ensure_ascii=False))
        if len(new_lines) > 5:
            print(f"... +{len(new_lines) - 5} 行")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("a", encoding="utf-8") as f:
        for line in new_lines:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")

    by_state: dict[str, int] = {}
    for line in new_lines:
        by_state[line["state"]] = by_state.get(line["state"], 0) + 1

    print(f"✅ append {len(new_lines)} 行 → {args.out.relative_to(ROOT)}（跳过已存在 {skipped} 行）")
    for s, n in sorted(by_state.items()):
        print(f"   {s:<10} {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
