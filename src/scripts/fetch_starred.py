#!/usr/bin/env python3
"""抓取大牛 starred 快照 → 重写 src/data/starred_seed.json（starred 信号的上游采集）。

遍历 src/data/users.yaml 白名单，用 gh CLI 调 GitHub API 拿每人最近 N 页 starred，
组装成 parse_starred.py 期望的 schema 后全量覆盖 starred_seed.json。

字段权威性：login/name/bio/tags 以 users.yaml 为准（与 parse_starred.py 一致）；
items / fetchedAt / rangeStart 由本次抓取生成。

依赖：gh CLI（CI 用 GH_TOKEN，本地用 `gh auth login` 的凭证）+ pyyaml。

环境变量：
  STARRED_PAGES     每人抓取页数（默认 2，每页 100 → ~200 个最近 star）
  STARRED_PER_PAGE  每页条数（默认 100，GitHub 上限）

容错：单个用户抓取失败时打印警告并沿用旧 seed 中该用户的条目，避免丢数据。
全部用户都失败则 exit 1。
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
USERS_YAML = ROOT / "src" / "data" / "users.yaml"
SEED_JSON = ROOT / "src" / "data" / "starred_seed.json"

PAGES = int(os.environ.get("STARRED_PAGES", "2"))
PER_PAGE = int(os.environ.get("STARRED_PER_PAGE", "100"))


def load_users() -> list[dict]:
    with USERS_YAML.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("users", [])


def load_old_seed() -> dict[str, dict]:
    """旧 seed 按 login 索引，作为单用户抓取失败时的 fallback。"""
    if not SEED_JSON.exists():
        return {}
    try:
        with SEED_JSON.open(encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}
    return {u.get("login"): u for u in data.get("users", []) if u.get("login")}


def gh_starred_page(login: str, page: int) -> list[dict]:
    """调 gh api 拿一页 starred（带 star+json header 以返回 starred_at）。"""
    cmd = [
        "gh", "api",
        "-H", "Accept: application/vnd.github.star+json",
        f"users/{login}/starred?per_page={PER_PAGE}&page={page}",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"gh api 退出码 {proc.returncode}")
    return json.loads(proc.stdout)


def fetch_user_items(login: str) -> list[dict]:
    """抓取一位大牛最近 PAGES 页 starred，映射为 seed items（按 star 时间倒序）。"""
    items: list[dict] = []
    for page in range(1, PAGES + 1):
        rows = gh_starred_page(login, page)
        if not rows:
            break  # 没有更多 star
        for it in rows:
            repo = it.get("repo") or {}
            url = repo.get("html_url")
            name = repo.get("full_name")
            if not url or not name:
                continue
            starred_at = (it.get("starred_at") or "")[:10]
            items.append({
                "name": name,
                "url": url,
                "stars": int(repo.get("stargazers_count") or 0),
                "description": repo.get("description") or "",
                "starredAt": starred_at,
            })
        if len(rows) < PER_PAGE:
            break  # 最后一页
    return items


def build_user_entry(user: dict, items: list[dict], fetched_at: str) -> dict:
    """组装 seed schema 的 user 条目（name/bio/tags 取自 users.yaml）。"""
    starred_dates = [it["starredAt"] for it in items if it.get("starredAt")]
    range_start = min(starred_dates) if starred_dates else fetched_at
    return {
        "login": user["login"],
        "name": user.get("name") or user["login"],
        "bio": user.get("bio") or "",
        "tags": user.get("tags") or [],
        "fetchedAt": fetched_at,
        "rangeStart": range_start,
        "items": items,
    }


def main() -> int:
    users = load_users()
    if not users:
        print(f"ERR: {USERS_YAML} 没有 users", file=sys.stderr)
        return 1
    old_seed = load_old_seed()
    fetched_at = datetime.now().strftime("%Y-%m-%d")

    out_users: list[dict] = []
    ok, failed = 0, 0
    for user in users:
        login = (user.get("login") or "").strip()
        if not login:
            continue
        try:
            items = fetch_user_items(login)
            out_users.append(build_user_entry(user, items, fetched_at))
            ok += 1
            print(f"  {login:<16} items={len(items)}", file=sys.stderr)
        except Exception as e:  # noqa: BLE001 — 单用户失败不应中断整体
            failed += 1
            old = old_seed.get(login)
            if old:
                # 沿用旧条目，但同步 users.yaml 的 name/bio/tags
                old.update({
                    "name": user.get("name") or login,
                    "bio": user.get("bio") or "",
                    "tags": user.get("tags") or [],
                })
                out_users.append(old)
                print(f"  {login:<16} 抓取失败，沿用旧 seed（{len(old.get('items', []))} 条）：{e}",
                      file=sys.stderr)
            else:
                print(f"  {login:<16} 抓取失败且无旧数据，跳过：{e}", file=sys.stderr)

    if ok == 0:
        print("ERR: 所有用户抓取均失败", file=sys.stderr)
        return 1

    SEED_JSON.write_text(
        json.dumps({"users": out_users}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    total = sum(len(u.get("items", [])) for u in out_users)
    print(f"✅ 写入 {len(out_users)} 位大牛 / {total} 条 starred → {SEED_JSON.relative_to(ROOT)}"
          f"  (成功 {ok} / 失败 {failed}, fetchedAt={fetched_at})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
