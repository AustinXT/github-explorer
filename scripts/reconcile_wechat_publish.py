#!/usr/bin/env python3
"""对账：用公众号真实「已群发」事实校对 publish_history.jsonl 的 state。

背景：publish_history.jsonl 是 append-only 状态机 SoR，pending→published 的翻转
只在有人显式跑 record_publish.py --state published 时发生。但文章是推到草稿箱、再由
人在公众号后台手动群发的——群发那一刻没有任何自动化回写 SoR，于是大量「其实已经发出去
了」的报告会永远停在 pending。本脚本拉公众号 freepublish/batchget（订阅号自动降级草稿
箱）→ 归一化标题匹配 analysis_report 的报告 H1 → 与 publish_history 的「每 slug 最新
态」比对，打印差异。

两种模式：
  · 默认 dry-run：只打印差异，并给出可直接复制执行的 record_publish 翻正命令，不写文件。
  · --apply    ：对「实际已发但 SoR≠published」和「公众号已发但 SoR 无记录」两桶，直接
                 调 src/scripts/record_publish.py 把 state 翻正为 published。record_publish
                 自带 (slug,state) 幂等，重复跑不会产生重复行。

复用 sync_wechat_status.py / _wechat_api.py 里已验证的拉取与匹配逻辑。

环境变量：WECHAT_APPID / WECHAT_APPSECRET（建议放 .env），经反代访问时另需
WECHAT_API_BASE / WECHAT_PROXY_TOKEN。用法：
  set -a && source .env && set +a && python3 scripts/reconcile_wechat_publish.py
  ... --include-drafts          # 同时看草稿箱（草稿无 url，update_time 为草稿时间）
  ... --min-confidence low      # 把低置信度命中也算进来（默认 medium）
  ... --apply --min-confidence high   # 高置信回写并 record_publish 翻正
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from _wechat_api import get_access_token, load_wechat_env  # noqa: E402
from sync_wechat_status import (  # noqa: E402
    WechatApiError,
    build_match_dict,
    date_from_ts,
    dedupe_by_slug,
    fetch_all,
    load_analysis_h1s,
    match_articles,
    parse_drafts,
    parse_freepublish,
)

REPO_ROOT = SCRIPTS_DIR.parent
PUBLISH_JSONL = REPO_ROOT / "src" / "data" / "publish_history.jsonl"
RECORD_PUBLISH = REPO_ROOT / "src" / "scripts" / "record_publish.py"


def load_latest_state(path: Path) -> dict[str, dict]:
    """读 publish_history.jsonl → 每 slug 取 recorded_at 最大的那条（= v_publish_latest）。"""
    latest: dict[str, dict] = {}
    if not path.is_file():
        return latest
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        slug = (rec.get("slug") or "").strip().lower()
        if not slug:
            continue
        prev = latest.get(slug)
        if prev is None or (rec.get("recorded_at") or "") > (prev.get("recorded_at") or ""):
            latest[slug] = rec
    return latest


def apply_fix(slug: str, title: str, wx_date: str, jsonl_path: Path,
              ci_run_id: str | None) -> bool:
    """调 record_publish.py 把某 slug 翻正为 published。返回是否成功。

    record_publish 自带 (slug,state) 幂等：已是 published 的会被它跳过、不重复 append。
    """
    cmd = [
        sys.executable, str(RECORD_PUBLISH),
        "--slug", slug,
        "--state", "published",
        "--published-at", wx_date,
        "--title", title,
        "--reason", "对账回写",
        "--out", str(jsonl_path),
    ]
    if ci_run_id:
        cmd += ["--ci-run-id", ci_run_id]
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout or "").strip()
    err = (r.stderr or "").strip()
    if r.returncode != 0:
        print(f"      ✗ record_publish 失败 (rc={r.returncode}): {err or out}")
        return False
    print(f"      ✓ {out or 'recorded'}")
    return True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--include-drafts", action="store_true",
                   help="同时拉草稿箱 material/batchget_material（草稿无 url）")
    p.add_argument("--min-confidence", choices=["high", "medium", "low"], default="medium",
                   help="算作命中的最低置信度（默认 medium）")
    p.add_argument("--apply", action="store_true",
                   help="回写：对「实际已发但 SoR≠published」「公众号已发但 SoR 无记录」"
                        "两桶调 record_publish 翻正为 published（默认只 dry-run）")
    p.add_argument("--ci-run-id", default=None,
                   help="GitHub Actions runId，--apply 时透传给 record_publish 便于审计")
    p.add_argument("--analysis-dir", type=Path, default=None,
                   help="analysis_report 目录，默认 <repo>/src/analysis_report")
    p.add_argument("--h1-json", type=Path, default=None,
                   help="预生成的 slug→H1 字典 JSON；给了则不扫 analysis-dir（SSH 跳板时由 runner 预算）")
    p.add_argument("--publish-jsonl", type=Path, default=None,
                   help="publish_history.jsonl 路径，默认 <repo>/src/data/publish_history.jsonl")
    args = p.parse_args()

    conf_rank = {"high": 3, "medium": 2, "low": 1, "none": 0}
    min_rank = conf_rank[args.min_confidence]
    jsonl_path = args.publish_jsonl or PUBLISH_JSONL

    # ── 1. 取真实公众号文章 ──────────────────────────────────────────────
    wx_env = load_wechat_env()
    print(f"[1/4] 获取 access_token（{wx_env['api_base']}）")
    token = get_access_token(wx_env)
    print("  ✓ token 就绪")

    articles = []
    print("[2/4] 拉公众号已群发图文（freepublish/batchget）")
    fallback = args.include_drafts
    try:
        raw = fetch_all(wx_env, token, "/cgi-bin/freepublish/batchget", {"no_content": 1})
    except WechatApiError as e:
        if e.errcode == 48001:
            print(f"  ⚠ {e}  ← 订阅号无 freepublish 权限，自动降级到草稿箱")
            fallback, raw = True, []
        else:
            sys.exit(f"ERR: {e}")
    articles.extend(parse_freepublish(raw))
    print(f"  ✓ freepublish 素材 {len(raw)} → {len(articles)} 篇文章")

    if fallback:
        print("[2b] 拉草稿箱（material/batchget_material type=news）")
        try:
            raw_d = fetch_all(wx_env, token, "/cgi-bin/material/batchget_material", {"type": "news"})
        except WechatApiError as e:
            sys.exit(f"ERR: {e}")
        drafts = parse_drafts(raw_d)
        articles.extend(drafts)
        print(f"  ✓ 草稿 {len(raw_d)} 素材，新增 {len(drafts)} 篇")

    # ── 2. 匹配标题 → slug（仅用 analysis_report H1，不依赖已删除的 publish.md）──
    print("[3/4] 加载报告 H1 标题字典并匹配")
    h1s = load_analysis_h1s(h1_json=args.h1_json, analysis_dir=args.analysis_dir)
    match_dict = build_match_dict(rows=[], h1s=h1s)
    results = match_articles(articles, match_dict)

    hit = [r for r in results if r.slug and conf_rank[r.confidence] >= min_rank]
    low = [r for r in results if r.slug and 0 < conf_rank[r.confidence] < min_rank]
    unmatched = [r for r in results if not r.slug or r.confidence == "none"]
    by_slug = dedupe_by_slug(hit)  # 每 slug 取 update_time 最大者
    print(f"  ✓ 公众号文章 {len(results)} 篇 → 命中 {len(by_slug)} slug"
          f"（≥{args.min_confidence}），低置信 {len(low)}，未匹配 {len(unmatched)}")

    # ── 3. 与 SoR 比对 ───────────────────────────────────────────────────
    print("[4/4] 与 publish_history.jsonl（每 slug 最新态）比对\n")
    latest = load_latest_state(jsonl_path)

    to_fix, consistent, sor_missing = [], [], []
    for slug, mr in by_slug.items():
        wx_date = date_from_ts(mr.article.update_time)
        sor = latest.get(slug)
        if sor is None:
            sor_missing.append((slug, mr, wx_date))
        elif sor.get("state") == "published":
            consistent.append((slug, mr, wx_date, sor))
        else:
            to_fix.append((slug, mr, wx_date, sor))

    matched_slugs = set(by_slug)
    sor_published_unhit = [
        (s, r) for s, r in latest.items()
        if r.get("state") == "published" and s not in matched_slugs
    ]
    sor_pending_unhit = [
        (s, r) for s, r in latest.items()
        if r.get("state") in ("pending", "draft") and s not in matched_slugs
    ]

    print("=" * 72)
    print(f"公众号命中 slug {len(by_slug)} 个  |  SoR 唯一 slug {len(latest)} 个")
    state_dist = Counter(r.get("state") for r in latest.values())
    print("SoR 最新态分布: " + "  ".join(f"{k}={v}" for k, v in state_dist.most_common()))
    print("=" * 72)

    print(f"\n🔴 [实际已发，但 SoR 仍非 published] {len(to_fix)} 条 —— 需翻正")
    for slug, mr, wx_date, sor in sorted(to_fix, key=lambda x: x[2]):
        print(f"  · {slug}")
        print(f"      SoR: state={sor.get('state')!r} reason={sor.get('reason')!r}"
              f"  ｜  公众号: 已发 {wx_date} [{mr.confidence} ratio={mr.ratio:.2f}]")
        print(f"      公众号标题: {mr.article.title!r}")
        if mr.article.url:
            print(f"      url: {mr.article.url}")
        print(f"      翻正命令: python3 src/scripts/record_publish.py --slug {slug} "
              f"--state published --published-at {wx_date} "
              f"--title {json.dumps(mr.article.title, ensure_ascii=False)}")

    print(f"\n🟠 [公众号已发，但 SoR 无任何记录] {len(sor_missing)} 条")
    for slug, mr, wx_date in sorted(sor_missing, key=lambda x: x[2]):
        print(f"  · {slug}  ｜ 公众号已发 {wx_date} [{mr.confidence} ratio={mr.ratio:.2f}]")
        print(f"      翻正命令: python3 src/scripts/record_publish.py --slug {slug} "
              f"--state published --published-at {wx_date} "
              f"--title {json.dumps(mr.article.title, ensure_ascii=False)}")

    print(f"\n🟡 [SoR=published 但本次公众号列表未命中] {len(sor_published_unhit)} 条（标题不匹配或超出列表窗口，需人工瞄一眼）")
    for slug, sor in sorted(sor_published_unhit):
        print(f"  · {slug}  ｜ SoR published_at={sor.get('published_at')} title={sor.get('title')!r}")

    print(f"\n🟢 [一致：SoR=published 且公众号命中] {len(consistent)} 条")
    date_mismatch = [(s, sor.get("published_at"), wx) for s, mr, wx, sor in consistent
                     if sor.get("published_at") and sor.get("published_at") != wx]
    if date_mismatch:
        print(f"      其中发布日期与公众号 update_time 不一致 {len(date_mismatch)} 条（仅供参考，update_time 含改稿）:")
        for s, sor_d, wx in date_mismatch[:20]:
            print(f"        · {s}  SoR={sor_d}  公众号={wx}")

    print(f"\n⚪ [SoR=pending/draft 且公众号未命中] {len(sor_pending_unhit)} 条（大概率确实还没发，符合预期）")

    if low:
        print(f"\n🔎 [低置信度命中 — 默认不算数，--min-confidence low 可纳入] {len(low)} 条")
        for r in sorted(low, key=lambda x: -x.ratio)[:20]:
            print(f"  · 公众号 {r.article.title!r} → 候选 {r.slug} ratio={r.ratio:.2f}")

    if unmatched:
        print(f"\n❓ [公众号上有，但项目里找不到对应报告] {len(unmatched)} 条")
        for r in unmatched:
            print(f"  · {r.article.title!r}  ({date_from_ts(r.article.update_time)})")

    # ── 4. 回写（--apply）或收尾（dry-run）─────────────────────────────────
    if not args.apply:
        print("\n（dry-run 完毕，未改动任何文件。确认无误后逐条执行上面的翻正命令，"
              "或加 --apply 自动回写。）")
        return 0

    pending_fixes = [(slug, mr, wx_date) for slug, mr, wx_date, _ in to_fix]
    pending_fixes += [(slug, mr, wx_date) for slug, mr, wx_date in sor_missing]
    print(f"\n✍️  [--apply] 回写 {len(pending_fixes)} 条到 {jsonl_path}")
    applied = 0
    for slug, mr, wx_date in sorted(pending_fixes, key=lambda x: x[2]):
        print(f"  · {slug}  ← published {wx_date}")
        if apply_fix(slug, mr.article.title, wx_date, jsonl_path, args.ci_run_id):
            applied += 1
    print(f"\n（--apply 完毕：{applied}/{len(pending_fixes)} 条已交 record_publish 处理；"
          "幂等去重后实际新增以 git diff 为准。）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
