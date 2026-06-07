"""博客园 (cnblogs) MetaWeblog adapter —— 国内少见的可编程发布平台。

为什么先做博客园：8 个目标渠道里只有它有真正的开放发布 API（MetaWeblog
XML-RPC），无需浏览器/cookie，能在 CI 里全自动跑通，验证骨架成本最低。

凭据（放 .env.local，不入 Git）：
  CNBLOGS_BLOGAPP    博客标识，即 www.cnblogs.com/<blogapp>/ URL 里的那段
  CNBLOGS_USERNAME   博客园登录名
  CNBLOGS_TOKEN      MetaWeblog 访问令牌（后台「设置 → 博客设置 → MetaWeblog 访问令牌」，
                     不是登录密码）
  CNBLOGS_RPC_URL    可选，默认 https://rpc.cnblogs.com/metaweblog/<blogapp>
  CNBLOGS_CATEGORIES 可选，逗号分隔的分类名（如「[随笔分类]开源」）

MetaWeblog 方法：
  metaWeblog.newPost(blogid, user, token, struct, publish) -> postid(str)
  metaWeblog.editPost(postid, user, token, struct, publish) -> bool
其中 publish=False 存草稿、True 直接公开；blogid 传 blogapp 即可（博客园容错）。

待办（未来增强）：正文外链图可用 metaWeblog.newMediaObject 重托管到博客园
图床，规避个别图源的防盗链；当前先原样保留（GitHub 资产图一般可直显）。
"""
from __future__ import annotations

import xmlrpc.client

from ..base import Article, BaseAdapter, PublishResult, RenderedArticle, env, register


@register
class CnblogsAdapter(BaseAdapter):
    name = "cnblogs"
    content_format = "html"

    def _conf(self) -> dict:
        blogapp = env("CNBLOGS_BLOGAPP")
        rpc = env("CNBLOGS_RPC_URL") or (
            f"https://rpc.cnblogs.com/metaweblog/{blogapp}" if blogapp else ""
        )
        return {
            "blogapp": blogapp,
            "username": env("CNBLOGS_USERNAME"),
            "token": env("CNBLOGS_TOKEN"),
            "rpc": rpc,
            "categories": [c.strip() for c in env("CNBLOGS_CATEGORIES").split(",") if c.strip()],
        }

    def check_auth(self) -> None:
        c = self._conf()
        missing = [k for k in ("blogapp", "username", "token") if not c[k]]
        if missing:
            raise RuntimeError(
                "博客园缺少凭据: "
                + ", ".join("CNBLOGS_" + m.upper() for m in missing)
                + "（放进 .env.local，见 scripts/syndicate/README.md）"
            )

    def publish(
        self,
        article: Article,
        rendered: RenderedArticle,
        *,
        publish: bool,
        existing_post_id: str | None = None,
    ) -> PublishResult:
        c = self._conf()
        server = xmlrpc.client.ServerProxy(c["rpc"], allow_none=True)
        struct = {
            "title": rendered.title,
            "description": rendered.content,           # HTML 正文
            "categories": c["categories"],
            "mt_keywords": ",".join(article.tags),
        }
        api = server.metaWeblog
        if existing_post_id:
            api.editPost(existing_post_id, c["username"], c["token"], struct, publish)
            post_id = str(existing_post_id)
        else:
            post_id = str(api.newPost(c["blogapp"], c["username"], c["token"], struct, publish))
        return PublishResult(
            post_id=post_id,
            url=f"https://www.cnblogs.com/{c['blogapp']}/p/{post_id}.html",
            state="published" if publish else "draft",
        )
