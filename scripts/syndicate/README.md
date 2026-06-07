# syndicate —— 一文多发框架

把现有「单渠道公众号发布」泛化成「一份报告 → 多个渠道」的 `publisher + adapter`
结构。新接一个平台 = 写一个 adapter，主流程不动。每个外发渠道自动追加
「导流公众号页脚」，把外部读者引回公众号。

> 已落地：通用骨架 + 渲染层 + per-channel 发布历史 + **两个真渠道**
> （`cnblogs` 博客园 MetaWeblog、`wechat` 公众号复用 wechat_publish.py）。
> 掘金/CSDN/知乎/思否等无开放 API 的渠道，计划走 Claude-in-Chrome 浏览器半自动。

## 架构

```
scripts/syndicate_publish.py        CLI 入口
scripts/syndicate/
  base.py        Article / RenderedArticle / PublishResult / BaseAdapter / 注册表 / 报告解析 / .env.local 加载
  render.py      Markdown → html|markdown + 导流公众号页脚
  history.py     publish_history.jsonl 的 per-channel 读写 + 幂等查询
  adapters/
    cnblogs.py   博客园 MetaWeblog adapter（框架渲染 html）
    wechat.py    公众号 adapter（self_render，复用 scripts/wechat_publish.py 全套图片/渲染/草稿逻辑）
```

两类 adapter：
- **普通**（cnblogs）：框架 `render()` 出 html/markdown（含导流页脚）→ adapter 只管投递。
- **自渲染**（wechat，`self_render=True`）：渲染与 API 深度耦合（外链图重托管到
  mmbiz、CSS 全内联、传封面、入草稿箱），且公众号是导流终点不该带自身 CTA，
  故跳过框架 render，直接调 `wechat_publish.publish_report()`。

设计原则（与现有管线对齐，不另起一套）：

- **slug** = 报告文件名 stem 小写（同 `wechat_publish.py` / `build_reports_index.py`）
- **canonical_url** = 站点报告页 `SITE_URL + PUBLIC_BASE_PATH + /reports/{slug}/`，
  作为 SEO 正本回链 + 导流落点（POSSE：自有站点是正本，外发只是 silo）
- **发布历史** = `src/data/publish_history.jsonl`（append-only SoR，入 Git），
  新增 `channel` / `post_id` / `url` 三个可选字段；`db.sqlite` 由 CI 据此重建
- **幂等** = 按 `(slug, channel)` 在 jsonl 查最近 `post_id`，有则 editPost、无则 newPost

## 用法

```bash
# 列出已注册渠道
python3 scripts/syndicate_publish.py --list

# dry-run：解析 + 渲染 + 判断新建/更新，不联网、不写历史（渲染结果落 tmp/）
python3 scripts/syndicate_publish.py src/analysis_report/1panel-dev_maxkb.md --channel cnblogs --dry-run

# 存草稿（默认，便于人工复核）
python3 scripts/syndicate_publish.py src/analysis_report/1panel-dev_maxkb.md --channel cnblogs

# 直接公开
python3 scripts/syndicate_publish.py src/analysis_report/1panel-dev_maxkb.md --channel cnblogs --publish

# 已发过会自动 editPost 更新；强制新建：
python3 scripts/syndicate_publish.py <report.md> --channel cnblogs --force-new

# 公众号（需先有同名 .meta.json，由 md2wechat 产出）；止于草稿箱，群发仍在后台人工
python3 scripts/syndicate_publish.py src/analysis_report/apache_superset.md --channel wechat --dry-run
python3 scripts/syndicate_publish.py src/analysis_report/apache_superset.md --channel wechat
```

## 凭据（放 `.env.local`，不入 Git）

自动加载仓库根的 `.env.local` / `.env`（不覆盖已有环境变量）。

### 博客园 cnblogs

```ini
CNBLOGS_BLOGAPP=your-blog-id        # www.cnblogs.com/<blogapp>/ 里的那段
CNBLOGS_USERNAME=your-login-name
CNBLOGS_TOKEN=your-metaweblog-token # 后台「设置 → 博客设置 → MetaWeblog 访问令牌」，不是登录密码
# CNBLOGS_RPC_URL=...               # 可选，默认 https://rpc.cnblogs.com/metaweblog/<blogapp>
# CNBLOGS_CATEGORIES=[随笔分类]开源  # 可选，逗号分隔
```

### 微信公众号 wechat

复用现有公众号管线的环境变量（同 `scripts/wechat_publish.py`）：

```ini
WECHAT_APPID=...          # 必需
WECHAT_APPSECRET=...      # 必需
WECHAT_API_BASE=...       # 反代 base url（直连官方留空）
WECHAT_PROXY_TOKEN=...    # 反代鉴权 header
```

前置：报告需有同名 `.meta.json`（title/digest/author/theme），由 md2wechat 产出。
公众号止于「入草稿箱」，`--publish` 对它无效，群发上线仍在公众号后台人工完成。

### 导流页脚（所有外发渠道通用，公众号自身不带）

```ini
WECHAT_MP_NAME=你的公众号名          # 渲染时追加「全网同名，微信搜一搜即达」CTA
# SITE_URL / PUBLIC_BASE_PATH 复用站点约定，决定 canonical 回链
```

## 报告 frontmatter（可选）

报告无需 frontmatter 也能发（标题取首个 H1、来源取 `> GitHub:` 行、canonical 自动推导）。
需要覆盖时可在 md 顶部加 YAML frontmatter：

```yaml
---
title: 自定义标题
tags: [AI, RAG]
canonical_url: https://example.com/custom    # 覆盖默认 canonical
syndicate: false        # 该篇不外发；或 [cnblogs] 仅发指定渠道
---
```

## 新增一个 adapter

1. 在 `adapters/` 下新建 `<platform>.py`，写 `BaseAdapter` 子类：
   - `name` / `content_format`（`'html'` 或 `'markdown'`）
   - `check_auth()` 校验凭据
   - `publish(article, rendered, *, publish, existing_post_id)` 返回 `PublishResult`
   - 类上加 `@register`
2. 在 `adapters/__init__.py` import 它
3. 凭据加进本 README + `.env.local`

## 与现有公众号管线的关系

- 公众号已迁成 `wechat` adapter：CLI 内部调 `wechat_publish.publish_report()`，
  复用其图片重托管/CSS 内联/封面/草稿箱逻辑（未重写）。`wechat_publish.py` 的
  独立 CLI（`python3 scripts/wechat_publish.py <md>`）契约不变，CI 自动分析与
  ali-demo runner 仍可照常调用。
- CI 自动分析记录历史仍走 `src/scripts/record_publish.py`（channel 隐式 = wechat）；
  本 adapter 是「统一调度」下的等价手动/本地路径，两者都写
  `publish_history.jsonl(channel=wechat)`，不冲突。
- DB 里 `v_publish_latest` 已收窄为「仅 wechat」，其它渠道记录不会污染
  `reports.published_*`（= 公众号发布状态）；多渠道状态查 `v_publish_channel_latest`。
- 路线：接 Claude-in-Chrome 驱动掘金/CSDN/知乎/思否 → 腾讯云/阿里云走半官方同步。
