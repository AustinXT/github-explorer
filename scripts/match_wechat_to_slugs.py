#!/usr/bin/env python3
"""把公众号已发文章按 GitHub URL 反查本地 slug，产出 mapping JSON。

输入：
  tmp/wechat_published.json   # 来自 tmp/fetch_wechat_published.js 在 mp 后台抓的
  tmp/local_gh_index.json     # 本地 {owner/repo (lowercase) → slug} 字典
                              # 如果不存在，会现场扫 src/analysis_report/*.md 重建
输出：
  tmp/wechat_match.json       # [{slug, wechat_title, wechat_url, send_date, github_url, confidence}]
  tmp/wechat_articles/*.html  # 文章页面缓存（便于复跑不再 curl）

用法：
  scripts/match_wechat_to_slugs.py            # 跑全量
  scripts/match_wechat_to_slugs.py --limit 5  # 只跑前 5 条调试
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TMP = REPO_ROOT / "tmp"
ARTICLE_CACHE = TMP / "wechat_articles"
WECHAT_JSON = TMP / "wechat_published.json"
LOCAL_INDEX = TMP / "local_gh_index.json"
MATCH_OUT = TMP / "wechat_match.json"

GH_RE = re.compile(r"https?://github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?=[/?#\"<>\\\s]|$)")
# 排除明显不是 repo 的 GitHub 路径
GH_OWNER_BLACKLIST = {
    "user-attachments", "assets", "raw.githubusercontent.com", "marketplace",
    "features", "pricing", "topics", "trending", "explore", "settings", "orgs", "sponsors",
}
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"


def build_local_index() -> dict[str, str]:
    """扫 src/analysis_report/*.md，每篇取第一个 github URL → slug。lowercase。"""
    out: dict[str, str] = {}
    for md in (REPO_ROOT / "src" / "analysis_report").glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        m = GH_RE.search(text)
        if m:
            out[m.group(1).rstrip("/").lower()] = md.stem
    return out


H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
TITLE_SUFFIXES = ["深度分析报告", "深度分析", "分析报告"]
STRIP_CHARS = "「」『』\"\"''《》()【】[]————，,。：:；;！!？?"


def _norm(s: str) -> str:
    if not s:
        return ""
    s = unicodedata.normalize("NFKC", s).lower()
    for ch in STRIP_CHARS:
        s = s.replace(ch, "")
    s = re.sub(r"\s+", " ", s).strip()
    for suf in TITLE_SUFFIXES:
        if s.endswith(suf):
            s = s[: -len(suf)].strip()
            break
    return s


def build_title_index() -> dict[str, str]:
    """slug → 归一化后的 H1。用 H1 反查 slug 用 inverse。"""
    out: dict[str, str] = {}
    for md in (REPO_ROOT / "src" / "analysis_report").glob("*.md"):
        try:
            head = md.read_text(encoding="utf-8", errors="ignore").splitlines()[:5]
        except OSError:
            continue
        for line in head:
            m = H1_RE.match(line)
            if m:
                key = _norm(m.group(1))
                if key:
                    out[key] = md.stem
                break
    return out


def title_fallback_match(wechat_title: str, title_idx: dict[str, str]) -> tuple[str | None, float]:
    """对完全没 GitHub URL 的 case，用归一化标题模糊匹配。返回 (slug, ratio)。"""
    q = _norm(wechat_title)
    if not q or not title_idx:
        return None, 0.0
    scored = sorted(
        ((slug, difflib.SequenceMatcher(None, q, k).ratio()) for k, slug in title_idx.items()),
        key=lambda x: -x[1],
    )
    if not scored:
        return None, 0.0
    # 也尝试用"包含关系"做补丁（如 "DeerFlow 深度分析报告" ↔ "deerflow 深度分析报告"）
    for k, slug in title_idx.items():
        if (q and (q in k or k in q)) and abs(len(q) - len(k)) < 5:
            return slug, 0.95
    best_slug, best_ratio = scored[0]
    return best_slug, best_ratio


def fetch_article(url: str, cache_path: Path, *, timeout: int = 20) -> str:
    """带磁盘缓存的文章页 fetch。"""
    if cache_path.is_file() and cache_path.stat().st_size > 1024:
        return cache_path.read_text(encoding="utf-8", errors="ignore")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read().decode("utf-8", errors="ignore")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(body, encoding="utf-8")
    return body


def extract_github_repo(html: str) -> tuple[str | None, list[str]]:
    """从文章 HTML 找 GitHub URL。返回 (最显著的 owner/repo, 所有候选列表)。
    选择标准：出现次数最多的 owner/repo；并列时取首次出现的。
    """
    found = []
    for m in GH_RE.finditer(html):
        repo = m.group(1).rstrip("/").lower()
        if "/" not in repo:
            continue
        owner = repo.split("/", 1)[0]
        if owner in GH_OWNER_BLACKLIST:
            continue
        found.append(repo)
    if not found:
        return None, []
    counts = Counter(found)
    # 按 (出现次数 desc, 首次出现 index asc) 排序
    first_idx = {r: found.index(r) for r in counts}
    ranked = sorted(counts.keys(), key=lambda r: (-counts[r], first_idx[r]))
    return ranked[0], ranked


def fmt_date(ts: int | None) -> str:
    if not ts:
        return ""
    return datetime.fromtimestamp(int(ts)).strftime("%Y-%m-%d")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--limit", type=int, default=0, help="只处理前 N 条，0 = 全量")
    p.add_argument("--sleep", type=float, default=0.7, help="curl 间隔秒")
    p.add_argument("--input", type=Path, default=WECHAT_JSON)
    p.add_argument("--output", type=Path, default=MATCH_OUT)
    args = p.parse_args()

    if not args.input.is_file():
        sys.exit(f"ERR: 找不到 {args.input}，请先在 mp 后台跑 tmp/fetch_wechat_published.js")

    if LOCAL_INDEX.is_file():
        local_idx: dict[str, str] = json.loads(LOCAL_INDEX.read_text(encoding="utf-8"))
        print(f"[本地字典] 从 {LOCAL_INDEX} 读到 {len(local_idx)} 项")
    else:
        local_idx = build_local_index()
        LOCAL_INDEX.write_text(json.dumps(local_idx, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[本地字典] 现扫 → {len(local_idx)} 项，落 {LOCAL_INDEX}")

    data = json.loads(args.input.read_text(encoding="utf-8"))
    # 用 album_title 字符串比较，避开 JS 大整数精度问题
    articles = [
        r for r in data.get("all", [])
        if r.get("album_title") == "Github 项目分析报告"
    ]
    if args.limit:
        articles = articles[: args.limit]
    print(f"[公众号侧] 处理 {len(articles)} 篇")

    title_idx = build_title_index()
    print(f"[标题字典] H1 共 {len(title_idx)} 项（用于无 GitHub URL 的 fallback）")

    ARTICLE_CACHE.mkdir(parents=True, exist_ok=True)
    matched, no_gh, no_local = [], [], []
    for i, art in enumerate(articles, 1):
        url = art.get("content_url") or ""
        if not url.startswith("http"):
            print(f"  [{i}/{len(articles)}] 跳过：无 content_url")
            continue
        # 缓存 key：用 mp.weixin.qq.com/s/{id} 里的 id
        key = url.rstrip("/").split("/")[-1].split("?")[0] or f"art{art.get('appmsgid')}"
        cache = ARTICLE_CACHE / f"{key}.html"
        cached = cache.is_file() and cache.stat().st_size > 1024
        try:
            html = fetch_article(url, cache)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            print(f"  [{i}/{len(articles)}] curl 失败 {key}: {e}")
            continue

        gh, all_cands = extract_github_repo(html)
        title_short = art["title"][:40]

        if gh:
            slug = local_idx.get(gh)
            if slug:
                matched.append({
                    "slug": slug,
                    "wechat_title": art["title"],
                    "wechat_url": url,
                    "send_date": fmt_date(art.get("send_time")),
                    "github_url": f"https://github.com/{gh}",
                    "github_repo": gh,
                    "match_method": "github_url",
                    "read_num": art.get("read_num"),
                    "candidates": all_cands[:3],
                })
                print(f"  [{i}/{len(articles)}] ✓ {slug:50s} ← github.com/{gh}{' [cached]' if cached else ''}")
                if not cached and args.sleep > 0:
                    time.sleep(args.sleep)
                continue
            no_local.append({
                "title": art["title"], "url": url,
                "github_repo": gh, "candidates": all_cands[:3],
            })
            print(f"  [{i}/{len(articles)}] ⚠ github.com/{gh}  → 本地无对应报告  ({title_short}…)")
        else:
            # fallback：用归一化标题匹配
            slug, ratio = title_fallback_match(art["title"], title_idx)
            if slug and ratio >= 0.7:
                matched.append({
                    "slug": slug,
                    "wechat_title": art["title"],
                    "wechat_url": url,
                    "send_date": fmt_date(art.get("send_time")),
                    "github_url": None,
                    "github_repo": None,
                    "match_method": f"title_fuzzy(ratio={ratio:.2f})",
                    "read_num": art.get("read_num"),
                })
                print(f"  [{i}/{len(articles)}] ✓ {slug:50s} ← title fuzzy {ratio:.2f}  ({title_short}…)")
            else:
                no_gh.append({"title": art["title"], "url": url, "best_title_match": slug, "ratio": ratio})
                print(f"  [{i}/{len(articles)}] ✗ 无 github URL + title fallback miss: {title_short}…")
        if not cached and args.sleep > 0:
            time.sleep(args.sleep)

    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "input": str(args.input),
        "matched": len(matched),
        "no_github_url_in_article": len(no_gh),
        "no_local_report": len(no_local),
        "entries": matched,
        "no_github_url": no_gh,
        "no_local_report_details": no_local,
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print()
    print("=" * 60)
    print(f"✓ matched           : {len(matched)}")
    print(f"  无 github URL      : {len(no_gh)}")
    print(f"  本地无对应报告     : {len(no_local)}")
    print(f"  输出 → {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
