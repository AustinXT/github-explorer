"""掘金 (juejin.cn) adapter —— 浏览器自动化（无开放发布 API）。

掘金编辑器是 markdown 原生（CodeMirror），需登录态。发布流程：写正文 → 填标题
→ 点「发布」打开抽屉 → 选分类 + 加标签(2-5) + (可选)封面/简介 → 确定并发布。

导流到公众号：掘金对正文硬导流敏感，正文禁二维码；框架渲染已在文末追加
「全网同名，微信搜一搜即达」软导流页脚（WECHAT_MP_NAME 控制），合规且足够。
"""
from __future__ import annotations

from ..base import Article, register
from ..browser import BrowserAdapter


@register
class JuejinAdapter(BrowserAdapter):
    name = "juejin"
    editor_url = "https://juejin.cn/editor/drafts/new"

    def field_notes(self, article: Article) -> dict:
        return {
            "分类": "按报告主题选（后端 / 人工智能 / 前端 / 开源…）",
            "标签": "、".join(article.tags) if article.tags
            else "在抽屉里搜并选 2-5 个相关标签（如 GitHub、开源、AI）",
            "封面": "可留空让掘金自动生成，或用 GitHub 社交卡",
            "简介": article.digest or "取报告「一句话总结」前 ~100 字",
        }

    def playbook(self, article: Article, content_path: str, existing_url: str) -> list:
        if existing_url:
            head = [
                f"该报告此前已发到掘金：{existing_url}",
                "→ 这是【更新】：navigate 到该文章的编辑页（文章页右上「编辑」或创作者中心草稿/文章列表进入），其余步骤同新建。",
            ]
        else:
            head = [
                "这是【新建】文章。",
                f"navigate 到掘金 markdown 编辑器：{self.editor_url}",
            ]
        return head + [
            "确认右上角已是登录态（有头像）。未登录则先让用户在该浏览器登录掘金，不要代登录。",
            f"读取渲染好的正文：{content_path}（已含导流页脚）。",
            "把正文 markdown 灌入左侧编辑器：优先用 javascript_tool 定位 CodeMirror 实例设值；"
            "不行则点编辑器聚焦后用剪贴板粘贴（设系统剪贴板 + Cmd/Ctrl+V），避免逐字键入。",
            f"标题栏填：{article.title}",
            "若掘金提示「检测到外链图片，是否上传到掘金」→ 点上传，把外链图转存到掘金图床（避免防盗链/失效）。",
            "点右上「发布」打开发布抽屉。",
            "在抽屉里：① 选「分类」 ② 添加「标签」2-5 个 ③（可选）设封面 ④（可选）填简介。具体见 field_notes。",
            "点「确定并发布」。",
            "发布成功后复制文章 URL（形如 https://juejin.cn/post/<id>）。",
            "回写历史：python3 scripts/syndicate_publish.py "
            f"{_report_hint(article)} --channel juejin --record --state published "
            "--url <文章URL> --post-id <id>",
        ]


def _report_hint(article: Article) -> str:
    return str(article.source_path) if article.source_path else "<报告.md>"
