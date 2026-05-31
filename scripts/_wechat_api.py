"""微信公众号 API 的最小共享层。

被 wechat_publish.py（入草稿箱）和 sync_wechat_status.py（拉已发布列表）共用。
所有 HTTP 走 urllib，与 wechat_publish.py 原实现保持一致，零额外依赖。

环境变量：
  必需 WECHAT_APPID / WECHAT_APPSECRET
  可选 WECHAT_API_BASE      默认 https://api.weixin.qq.com
  可选 WECHAT_PROXY_TOKEN   反代鉴权 header，直连官方时留空
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_API_BASE = "https://api.weixin.qq.com"
TOKEN_CACHE_PATH = Path("tmp/wechat_token.json")
TOKEN_EXPIRY_SLACK = 300


def env(name: str, *, required: bool = True, default: str = "") -> str:
    v = os.environ.get(name, "") or default
    if required and not v:
        sys.exit(f"ERR: 缺少环境变量 {name}")
    return v


def load_wechat_env() -> dict[str, str]:
    """读取 WECHAT_* 环境变量，缺关键字段直接退出。"""
    return {
        "appid": env("WECHAT_APPID"),
        "appsecret": env("WECHAT_APPSECRET"),
        "api_base": env(
            "WECHAT_API_BASE", required=False, default=DEFAULT_API_BASE
        ).rstrip("/"),
        "proxy_token": env("WECHAT_PROXY_TOKEN", required=False),
    }


def proxy_headers(env_dict: dict[str, str]) -> dict[str, str]:
    return {"X-Proxy-Token": env_dict["proxy_token"]} if env_dict["proxy_token"] else {}


class HttpError(RuntimeError):
    """非 fatal 的 HTTP 错误，可被调用方 catch"""


def http(
    url: str,
    *,
    headers: dict | None = None,
    data: bytes | None = None,
    method: str | None = None,
    timeout: int = 30,
    raise_on_error: bool = False,
) -> bytes:
    req = urllib.request.Request(url, data=data, method=method)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        msg = f"HTTP {e.code} 调用 {url[:80]}…\n  body: {body[:500]}"
        if raise_on_error:
            raise HttpError(msg) from e
        sys.exit(f"ERR: {msg}")
    except urllib.error.URLError as e:
        msg = f"网络错误 调用 {url[:80]}…\n  {e.reason}"
        if raise_on_error:
            raise HttpError(msg) from e
        sys.exit(f"ERR: {msg}")


def http_json(url: str, **kw) -> dict:
    raw = http(url, **kw)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        sys.exit(f"ERR: 非 JSON 响应 from {url[:80]}…\n  {raw[:300]!r}")


def check_wechat_ok(resp: dict, context: str) -> None:
    if resp.get("errcode"):
        sys.exit(
            f"ERR: 微信 API 错误 [{context}] "
            f"errcode={resp['errcode']} errmsg={resp.get('errmsg', '')}"
        )


def _load_cached_token() -> str | None:
    if not TOKEN_CACHE_PATH.is_file():
        return None
    try:
        cached = json.loads(TOKEN_CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if cached.get("expires_at", 0) > time.time() + TOKEN_EXPIRY_SLACK:
        return cached.get("access_token")
    return None


def _store_token(access_token: str, expires_in: int) -> None:
    TOKEN_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    TOKEN_CACHE_PATH.write_text(
        json.dumps({
            "access_token": access_token,
            "expires_at": int(time.time()) + int(expires_in or 0),
        }),
        encoding="utf-8",
    )


def get_access_token(env_dict: dict[str, str], *, force_refresh: bool = False) -> str:
    if not force_refresh:
        cached = _load_cached_token()
        if cached:
            return cached
    url = (
        f"{env_dict['api_base']}/cgi-bin/token?grant_type=client_credential"
        f"&appid={urllib.parse.quote(env_dict['appid'])}"
        f"&secret={urllib.parse.quote(env_dict['appsecret'])}"
    )
    r = http_json(url, headers=proxy_headers(env_dict))
    check_wechat_ok(r, "get token")
    if "access_token" not in r:
        sys.exit(f"ERR: 响应里没 access_token: {r}")
    _store_token(r["access_token"], r.get("expires_in", 7200))
    return r["access_token"]


def wechat_post(
    env_dict: dict[str, str],
    path: str,
    body: Any,
    access_token: str,
    *,
    timeout: int = 30,
) -> dict:
    """POST JSON 到微信 API（自带 access_token query 参数 + 反代 header）。"""
    url = (
        f"{env_dict['api_base']}{path}"
        f"?access_token={urllib.parse.quote(access_token)}"
    )
    return http_json(
        url,
        headers={**proxy_headers(env_dict), "Content-Type": "application/json"},
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        method="POST",
        timeout=timeout,
    )
