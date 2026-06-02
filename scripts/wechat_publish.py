#!/usr/bin/env python3
"""
读分析报告的 .md + .meta.json，确定性地转 HTML 后走反代入微信草稿箱。

为什么独立成脚本（不依赖 md2wechat 输出 HTML）：
  实测 LLM 转 HTML 不可靠 —— 把 `![alt](url)` 错转成嵌套 a 标签、
  把数字列表拆成游离段落、相邻 ul 不合并 等等。这些都被 Python
  markdown 库一次性解决。md2wechat skill 只负责润色 md
  （引号替换、lint、摘要）和输出元数据 JSON。

输入：
  argv[1]: 报告 .md 路径（如 src/analysis_report/gin-gonic_gin.md）
           会自动推出同名 .meta.json

环境变量：
  必需：WECHAT_APPID / WECHAT_APPSECRET
  必需：WECHAT_API_BASE      反代 base url，如 https://wx.nightvoyager.top
  必需：WECHAT_PROXY_TOKEN   反代鉴权 header
  可选：DEFAULT_COVER_URL    封面拉取失败时用这个兜底，默认 picsum
  可选：BLOG_BASE_URL        阅读原文指向的博客 base，
                             默认 https://blog.nightvoyager.top/github-explorer/reports

产出：
  tmp/last_publish.json  {media_id, thumb_media_id, title, ...}
  非 0 退出 = 发布失败
"""
from __future__ import annotations

import json
import mimetypes
import sys
import time
import urllib.parse
from pathlib import Path

from _wechat_api import (
    HttpError,
    check_wechat_ok,
    env,
    get_access_token,
    http,
    http_json,
    http_json_with_retry,
    load_wechat_env,
    proxy_headers,
)

try:
    import markdown
    from premailer import transform as inline_css
    from bs4 import BeautifulSoup
except ImportError as e:
    sys.exit(
        f"ERR: 缺少 Python 包 ({e})。\n"
        "  本地: python3 -m venv venv && venv/bin/pip install premailer beautifulsoup4 markdown\n"
        "  CI:  setup_ci_env.sh 已 pip install premailer beautifulsoup4 markdown"
    )


# 微信公众号排版 CSS — 与 ci/skills/md2wechat/assets/wechat.css 同步
# 仅使用标签选择器（微信会清掉 class 属性）+ !important（防止微信内部样式覆盖）
DEFAULT_CSS = """
body { max-width: 680px; margin: 0 auto; padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #3e3e3e; background: #fff; }
p { font-size: 15px !important; line-height: 2 !important; margin: 0 !important;
    padding: 0.5em 1.2em !important; text-align: justify !important; }
p + p { margin-top: 0 !important; }
h2 { font-size: 18px !important; color: #e51f42 !important; text-align: center !important;
    margin: 24px 0 !important; padding: 0 !important; }
h3 { font-size: 15px !important; font-weight: bold !important; color: #3e3e3e !important;
    text-align: left !important; margin: 16px 0 !important; padding: 0 0 0 1.2em !important; }
h4 { font-size: 15px !important; color: rgb(0,122,170) !important; margin: 12px 0 8px 0 !important; }
ul, ol { padding-left: 2em !important; margin: 1em 0 !important; font-size: 15px !important; }
li { margin: 0.5em 0 !important; line-height: 1.8em !important; font-size: 15px !important;
    color: #3e3e3e !important; }
ul ul, ul ol, ol ul, ol ol { margin: 0 !important; padding-left: 1.2em !important; }
blockquote { border-left: 4px solid #888 !important; padding: 8px 16px !important;
    margin: 1em 0 !important; color: #666 !important; background: #f9f9f9 !important; }
blockquote > p { margin: 0.5em 0 !important; padding: 0 !important; }
pre { font-size: 14px !important; line-height: 1.4em !important; color: #3e3e3e !important;
    background: #f8f8f8 !important; padding: 12px 16px !important; border-radius: 4px !important;
    overflow: auto !important; margin: 1em 0 !important; }
code { background: #f4f4f4 !important; color: #c7254e !important; padding: 2px 4px !important;
    border-radius: 3px !important; font-size: 90% !important; }
pre code { background: transparent !important; color: inherit !important; padding: 0 !important; }
strong { font-weight: bold !important; color: #3e3e3e !important; }
a { color: rgb(0,122,170) !important; text-decoration: none !important; }
img { max-width: 100% !important; height: auto !important; display: block !important;
    margin: 1em auto !important; border-radius: 4px !important; }
table { border-collapse: collapse !important; width: 100% !important; margin: 1em 0 !important;
    font-size: 14px !important; }
th, td { border: 1px solid #ddd !important; padding: 6px 10px !important; text-align: left !important; }
th { background: #f4f4f4 !important; font-weight: bold !important; }
hr { border: none !important; border-top: 1px solid #ddd !important; margin: 1.5em 0 !important; }
""".strip()


def build_multipart(filename: str, data: bytes, field: str = "media") -> tuple[str, bytes]:
    boundary = f"----wechat-{int(time.time()*1000)}"
    mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="{field}"; filename="{filename}"\r\n'
        f"Content-Type: {mime}\r\n\r\n"
    ).encode("utf-8") + data + f"\r\n--{boundary}--\r\n".encode("utf-8")
    return boundary, body


def merge_adjacent_uls(soup: BeautifulSoup) -> int:
    """合并相邻 <ul>，避免每条 li 单独被一个 ul 包导致行距过大。返回合并次数。"""
    merged = 0
    while True:
        round_merged = 0
        for ul in soup.find_all("ul"):
            sib = ul.next_sibling
            # 跳过纯空白文本节点
            while sib is not None and getattr(sib, "name", None) is None:
                if str(sib).strip():
                    break
                sib = sib.next_sibling
            if sib is not None and getattr(sib, "name", None) == "ul":
                for li in list(sib.find_all("li", recursive=False)):
                    ul.append(li.extract())
                sib.decompose()
                round_merged += 1
        if round_merged == 0:
            break
        merged += round_merged
    return merged


def upload_external_images(
    soup: BeautifulSoup,
    *,
    access_token: str,
    api_base: str,
    proxy_headers: dict,
) -> tuple[int, int]:
    """所有非 mmbiz 的 <img src> 下载后通过 uploadimg 换成 mmbiz URL。
    返回 (成功数, 失败数)。失败时保持原 src，不中断流程。"""
    ok = 0
    fail = 0
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if not src or "mmbiz." in src:
            continue
        try:
            img_data = http(src, timeout=20, raise_on_error=True)
        except HttpError as e:
            print(f"  ⚠ 下载失败 {src[:60]}…  {str(e)[:80]}", file=sys.stderr)
            fail += 1
            continue
        try:
            url = f"{api_base}/cgi-bin/media/uploadimg?access_token={urllib.parse.quote(access_token)}"
            filename = src.rsplit("/", 1)[-1].split("?", 1)[0] or "img"
            if "." not in filename:
                filename += ".png"
            boundary, body = build_multipart(filename, img_data)
            r = http_json_with_retry(
                url,
                headers={
                    **proxy_headers,
                    "Content-Type": f"multipart/form-data; boundary={boundary}",
                },
                data=body,
                method="POST",
                timeout=60,
            )
        except SystemExit as e:
            print(f"  ⚠ uploadimg 失败 {src[:60]}…  {e}", file=sys.stderr)
            fail += 1
            continue
        if r.get("url"):
            img["src"] = r["url"]
            print(f"  ✓ {src[:50]}… → mmbiz")
            ok += 1
        else:
            print(f"  ⚠ uploadimg 响应缺 url: {r}", file=sys.stderr)
            fail += 1
    return ok, fail


def compact_lists(soup: BeautifulSoup) -> None:
    """删掉 ul/ol 内部子节点之间的空白文本节点。

    微信 draft API 把 `<li>` 之间的换行符渲染成空 li（数字 1/3/5 全空），
    必须让 list 内 HTML 紧贴成一行。
    """
    for parent in soup.find_all(["ul", "ol"]):
        for child in list(parent.children):
            if child.name is None and not str(child).strip():
                child.extract()


def promote_strong_colon(soup: BeautifulSoup) -> int:
    """把列表项里 `<strong>X</strong>：Y` 改写为 `<strong>X：</strong>Y`。

    公众号 Web 后台编辑器会把 <li> 内容外包 <p>，叠加 wechat.css 的
    p { text-align: justify }，导致 `</strong>` 紧跟的全角冒号被推到下一行
    （移动端不外包 <p>，所以无此问题）。把冒号挪进 strong 让编辑器视为同一
    个不可拆分块，绕过该换行触发。返回处理过的列表项数。
    """
    from bs4 import NavigableString
    count = 0
    for li in soup.find_all("li"):
        for strong in li.find_all("strong"):
            nxt = strong.next_sibling
            if not isinstance(nxt, NavigableString):
                continue
            text = str(nxt)
            if text and text[0] in ("：", ":"):
                strong.append(text[0])
                nxt.replace_with(text[1:])
                count += 1
    return count


def md_to_html(md_text: str) -> str:
    """Markdown → 微信兼容 HTML 片段（含 <style> 头）。

    md.Markdown 的 'extra' 扩展已包含 tables / fenced_code / abbr 等 GFM 子集；
    'sane_lists' 让数字开头被正确识别为 ol。
    """
    md = markdown.Markdown(extensions=["extra", "sane_lists"])
    body = md.convert(md_text)
    soup = BeautifulSoup(body, "html.parser")
    # 删掉所有 H1：微信编辑器有独立标题字段，正文不应再出现 H1
    for h1 in soup.find_all("h1"):
        h1.decompose()
    compact_lists(soup)
    promote_strong_colon(soup)
    return f"<style>{DEFAULT_CSS}</style>\n{soup}"


def fetch_cover(theme: str, fallback_url: str) -> bytes:
    # picsum 替代已下线的 source.unsplash.com，根据 theme 散列保证同篇文章稳定取相似图
    seed = abs(hash(theme)) % 1_000_000
    candidates = [
        f"https://picsum.photos/seed/{seed}/900/383",
        fallback_url,
    ]
    for url in candidates:
        if not url:
            continue
        try:
            return http(url, timeout=20)
        except SystemExit:
            continue
    sys.exit(f"ERR: 拉取封面图失败，theme={theme}")


def main() -> int:
    if len(sys.argv) < 2:
        sys.exit("用法: wechat_publish.py <report.md>")

    md_path = Path(sys.argv[1])
    meta_path = Path(str(md_path.with_suffix("")) + ".meta.json")

    if not md_path.is_file():
        sys.exit(f"ERR: 找不到 md {md_path}")
    if not meta_path.is_file():
        sys.exit(f"ERR: 找不到 metadata {meta_path}（md2wechat 这一步没输出元数据）")

    md_text = md_path.read_text(encoding="utf-8")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    print(f"[0a] 用 markdown 库转 HTML（确定性结构）")
    raw_html = md_to_html(md_text)
    print(f"  ✓ {len(md_text)} → {len(raw_html)} bytes")

    title = meta.get("title") or md_path.stem
    digest = (meta.get("digest") or "")[:120]
    author = meta.get("author") or ""
    theme = meta.get("theme") or "stars,universe,dark"

    wx_env = load_wechat_env()
    api_base = wx_env["api_base"]
    fallback_cover = env(
        "DEFAULT_COVER_URL", required=False,
        default="https://picsum.photos/900/383",
    )
    blog_base = env(
        "BLOG_BASE_URL", required=False,
        default="https://blog.nightvoyager.top/github-explorer/reports",
    ).rstrip("/")
    # 博客 slug = 文件名 stem 小写（与 build_reports_index.py 的 normalization 对齐）
    slug = md_path.stem.lower()
    content_source_url = f"{blog_base}/{slug}/"

    proxy_h = proxy_headers(wx_env)

    # ─── Step 1: access_token ─────────────────────────────────
    print(f"[1/4] 获取 access_token（{api_base}）")
    access_token = get_access_token(wx_env)
    print(f"  ✓ token 就绪（含 tmp/wechat_token.json 缓存）")

    # ─── Step 1b: HTML 预处理 ─────────────────────────────────
    print("[1b] HTML 预处理：合并相邻 ul + 外链图片转 mmbiz")
    soup = BeautifulSoup(raw_html, "html.parser")
    merged = merge_adjacent_uls(soup)
    print(f"  ✓ 合并了 {merged} 个相邻 ul")
    img_ok, img_fail = upload_external_images(
        soup,
        access_token=access_token,
        api_base=api_base,
        proxy_headers=proxy_h,
    )
    print(f"  ✓ 图片 {img_ok} 成功 / {img_fail} 失败")

    # ─── Step 1c: CSS 内联 ────────────────────────────────────
    # 微信 draft/add 接口会剥 <style> 标签（与编辑器粘贴模式不同），
    # 必须把 CSS 内联到每个元素的 style 属性
    pre_inline = str(soup)
    html = inline_css(
        pre_inline,
        remove_classes=False,
        keep_style_tags=False,
        strip_important=False,
        disable_validation=True,
    )
    print(f"[1c] CSS 内联完成（{len(pre_inline)} → {len(html)} bytes）")

    # ─── Step 2: 拉封面 ───────────────────────────────────────
    print(f"[2/4] 拉封面（theme={theme}）")
    cover_data = fetch_cover(theme, fallback_cover)
    cover_path = Path("tmp/wechat_cover.jpg")
    cover_path.parent.mkdir(parents=True, exist_ok=True)
    cover_path.write_bytes(cover_data)
    print(f"  ✓ {len(cover_data)} bytes")

    # ─── Step 3: 上传封面到素材库 ─────────────────────────────
    print("[3/4] 上传封面到素材库（走反代）")
    upload_url = (
        f"{api_base}/cgi-bin/material/add_material"
        f"?access_token={urllib.parse.quote(access_token)}&type=image"
    )
    boundary, body = build_multipart("cover.jpg", cover_data)
    r = http_json_with_retry(
        upload_url,
        headers={
            **proxy_h,
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        data=body,
        method="POST",
        timeout=60,
    )
    check_wechat_ok(r, "upload material")
    if "media_id" not in r:
        sys.exit(f"ERR: 上传封面响应缺 media_id: {r}")
    thumb_media_id = r["media_id"]
    print(f"  ✓ media_id={thumb_media_id[:12]}…")

    # ─── Step 4: 入草稿箱 ─────────────────────────────────────
    print("[4/4] 入草稿箱")
    draft_url = (
        f"{api_base}/cgi-bin/draft/add"
        f"?access_token={urllib.parse.quote(access_token)}"
    )
    draft_body = json.dumps({
        "articles": [{
            "title": title,
            "author": author,
            "digest": digest,
            "content": html,
            "content_source_url": content_source_url,  # 「阅读原文」按钮指向博客
            "thumb_media_id": thumb_media_id,
            "need_open_comment": 0,
            "only_fans_can_comment": 0,
        }],
    }, ensure_ascii=False).encode("utf-8")
    r = http_json(
        draft_url,
        headers={**proxy_h, "Content-Type": "application/json"},
        data=draft_body,
        method="POST",
        timeout=60,
    )
    check_wechat_ok(r, "add draft")
    if "media_id" not in r:
        sys.exit(f"ERR: 草稿响应缺 media_id: {r}")
    draft_media_id = r["media_id"]
    print(f"  ✓ draft media_id={draft_media_id}")

    # 产物落地
    result = {
        "media_id": draft_media_id,
        "thumb_media_id": thumb_media_id,
        "title": title,
        "content_source_url": content_source_url,
        "report": str(md_path),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    Path("tmp").mkdir(exist_ok=True)
    Path("tmp/last_publish.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"✅ 已入草稿箱：{title}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
