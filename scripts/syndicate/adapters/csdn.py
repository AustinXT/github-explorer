"""CSDN adapter —— 浏览器自动化（无开放发布 API）。

CSDN 有 markdown 编辑器（editor.csdn.net/md），需登录态。发布流程：写正文 →
填标题 → 点「发布文章」→ 弹窗填 标签 / 分类专栏 / 封面 / 文章类型(原创) /
可见范围 → 发布。

导流到公众号：**CSDN 禁止出现「微信公众号」字样**（用户实测/平台规则），故本
adapter 置 name_wechat=False —— 页脚仍点名账号「智能时代蛮子」+「全网同名，
搜一搜即达」，只是不出现「微信公众号 / 微信」这几个字，靠同名让读者自行搜到，
不触发 CSDN 关键词拦截。
"""
from __future__ import annotations

from ..base import Article, register
from ..browser import BrowserAdapter


@register
class CsdnAdapter(BrowserAdapter):
    name = "csdn"
    editor_url = "https://editor.csdn.net/md/"
    name_wechat = False   # CSDN 禁止「微信公众号」字样：页脚保留账号名但不点名微信

    def field_notes(self, article: Article) -> dict:
        return {
            "标签": "、".join(article.tags) if article.tags
            else "在发布弹窗搜并选相关标签（如 github、开源、人工智能）",
            "分类专栏": "可选；若有「开源项目解析」类专栏则归入",
            "文章类型": "原创",
            "可见范围": "全部可见",
            "封面": "可留空自动，或上传 GitHub 社交卡",
            "导流": "⚠️ CSDN 禁止「微信公众号 / 微信」字样——页脚已自动改为只点名「智能时代蛮子」+「全网同名，搜一搜即达」；勿在正文/二维码另加微信字样",
        }

    def playbook(self, article: Article, content_path: str, existing_url: str) -> list:
        if existing_url:
            head = [
                f"该报告此前已发到 CSDN：{existing_url}",
                "→ 这是【更新】：从该文章页进入「编辑」，其余步骤同新建。",
            ]
        else:
            head = [
                "这是【新建】文章。",
                f"navigate 到 CSDN markdown 编辑器：{self.editor_url}",
            ]
        return head + [
            "确认已登录 CSDN（右上有头像）。未登录则先让用户在该浏览器登录，不要代登录。",
            f"读取渲染好的正文：{content_path}（已含导流页脚）。",
            "把正文 markdown 灌入左侧编辑器：优先用 javascript_tool 给 CodeMirror/textarea 设值；"
            "不行则聚焦编辑器后用剪贴板粘贴（设系统剪贴板 + Cmd/Ctrl+V），勿逐字键入。",
            f"标题栏填：{article.title}",
            "（可选）若要二维码导流：在正文末插入公众号二维码图片 + 「扫码关注公众号」一行。",
            "点右上「发布文章」打开发布弹窗。",
            "在弹窗里：① 加「标签」 ②（可选）选分类专栏 ③ 文章类型选「原创」 ④ 可见范围「全部可见」 ⑤（可选）封面。见 field_notes。",
            "点「发布文章」。",
            "成功后复制文章 URL（形如 https://blog.csdn.net/<用户名>/article/details/<id>）。",
            "回写历史：python3 scripts/syndicate_publish.py "
            f"{_report_hint(article)} --channel csdn --record --state published "
            "--url <文章URL> --post-id <id>",
        ]


def _report_hint(article: Article) -> str:
    return str(article.source_path) if article.source_path else "<报告.md>"
