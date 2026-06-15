# 6 年 31K stars：Chatwoot 如何用 Rails 重写 Zendesk

> GitHub: https://github.com/chatwoot/chatwoot

## 一句话总结

Chatwoot 是印度系创业团队用 Rails 7.1 + Vue 3 打造的「全渠道 + AI 原生」开源客服平台，对标 Zendesk / Intercom，已通过 YC 与 SOC 2 验证，全球 SMB 自托管市场的首选替代品。

## 值得关注的理由

1. **开源客服赛道已稳居头部**：31.2K stars、3.8K+ 贡献者、6 年持续高频迭代（近 30 天 133 commits），是开源 helpdesk 第一梯队里唯一兼具「全渠道 + AI + 多语」的 Rails 项目。
2. **Open-core + Captain AI 双引擎**：社区版是漏斗，企业版（SLA / Custom Roles / Audit / SAML）是利润中心；Captain AI 用 pgvector 做 RAG、用 Liquid 模板做 prompt、用 `method_missing` 做 Tool Registry——把 LLM 接到 Rails 业务对象的工程范式值得任何 AI 应用借鉴。
3. **真实多租户 + 全渠道架构的可迁移性**：11+ 渠道（WhatsApp / Facebook / Instagram / Telegram / Line / Twitter / SMS / Email / API / Web Widget）的 polymorphic Channel 抽象 + Wisper 事件总线 + `prepend_mod_with` EE 注入模式，是任何 SaaS 想做「多集成 + 多租户 + 收费分层」的可复用模板。

## 项目展示

![Chatwoot Dashboard Light](https://www.chatwoot.com/images/dashboard.webp)
*坐席端 Dashboard：左侧 inbox + 中间 conversation + 右侧 contact + Captain AI 浮窗*

![Dashboard Dark](https://www.chatwoot.com/images/dashboard-dark.webp)
*同一界面 Dark Mode 视觉，坐席最常用形态*

![WhatsApp Channel](https://www.chatwoot.com/images/hero/whatsapp-img.png)
*全渠道 WhatsApp 集成：客户在 WhatsApp、坐席在 Chatwoot 里回复*

![Customer Chat Hero](https://www.chatwoot.com/images/hero/customer.png)
*客户侧对话场景：跨渠道消息聚合视图*

![Captain AI Hero](https://www.chatwoot.com/images/hero/captain-head.svg)
*Captain AI Agent 品牌标识，AI Copilot + Agent 双形态*

> 备注：仓库 README 中的 `github/screenshots/*.png` 旧路径在当前 develop 分支已失效（verified=false），官网媒体是当前最佳展示源。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/chatwoot/chatwoot |
| Star / Fork | 31,211 / 7,586 |
| Watcher / Open Issues+PRs | 273 / ~800+ |
| 代码行数 | 962,683 行（JSON 67% i18n 资源 / Ruby 15% / JavaScript 10% / YAML 6% / Vue 1%）；剔除 i18n 后真实业务代码约 32 万行 |
| 语言 | Ruby 47% + Vue 27% + JavaScript 22.5% + HTML/SCSS 3% |
| 项目年龄 | 82 个月（2019-08 首次提交） |
| 开发阶段 | 密集开发（近 30 天 133 commits，近 90 天 389 commits，月均 ~130） |
| 开发模式 | 职业项目（周末 8.7%，深夜 20%，印度时区 + 全球客户） |
| 贡献模式 | 小团队核心 + 社区协作（383 贡献者，Top 5 占 99.2%，主作者 Shivam Mishra 22.9%） |
| 热度定位 | 大众热门（开源 helpdesk 头部） |
| 质量评级 | 代码 A- / 文档 B+ / 测试 A- / CI/CD A / 错误处理 A |
| License | 主仓 MIT（`/`）+ Enterprise（`enterprise/` 私有 EE 许可证） |
| 最新版本 | v4.14.2（共 148 个 tag，100 个 Release，语义化版本） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Chatwoot 团队核心是 YC W21 批次的印度系创业团队（核心工程师 Sojan Jose / Pranav Raj S / Muhsin Keloth / Shivam Mishra 等，常见 Kerala/India 工程师命名）。账号 2016-11 注册，但 Chatwoot 主仓 2019-08 才正式开源——先在 status / docs / chatwoot-cli 等基础设施仓库试水，再把核心产品开源。这一时序反映「先把 SaaS 跑通、再以开源为获客漏斗」的典型 PLG 路径。

### 问题判断

团队看到了一个具体痛点：现代 SMB 客服团队每天要同时面对 WhatsApp / Facebook / Instagram / Email / Telegram / 网站聊天 / Telegram 群消息等十余个渠道，客户数据却散落各处。闭源 SaaS（Zendesk / Intercom）单价高、数据托管在第三方；其他开源（Zammad / osTicket / FreeScout）停留在「传统工单 + 邮件」语义，对现代全渠道、AI、知识库门户支持不足。时机成熟于两个外部条件：（1）2020 前后 WhatsApp Business API 全面开放，使多渠道客服成为可解工程问题；（2）2023 之后 LLM 普及让「AI 自动回复」从营销词变成可落地功能。Chatwoot 的 B 轮融资也正发生在此节点。

### 解法哲学

- **Open-core 而非全闭源**：核心 inbox + 多渠道 + 知识库 + Captain 全部 OSS；EE（`enterprise/` 目录）只放 SLA、Custom Roles、Audit、SAML、Voice 等付费能力。社区版是销售漏斗，EE 是利润中心。
- **Rails 全栈 + Vue 3 前端单仓**：不做前后端分离微服务（dashboard / widget / portal / sdk / v3 都在同一仓），以降低自托管门槛、保持迭代速度——`docker-compose up` 即可起整套。
- **Channel Adapters 抽象外部世界**：WhatsApp / Facebook / Instagram / Telegram / Line / Twitter / SMS / Email / API / Web Widget 全部统一抽象为 `Inbox.channel`（polymorphic），业务侧只面对 `Conversation` + `Message` 两类核心实体。
- **明确不做的**：没有 microservice 拆分、没有重客户端 SPA 单独部署、没有强类型前端（仅 PropsType）、没有自研 IM 协议——坚持 Rails convention over configuration，让中小团队 5 分钟起项目。

### 战略意图

社区版（OSS）= 全渠道 inbox + 知识库 + Captain 基础 + Linear/Slack/Shopify 集成；企业版（EE）= SLA / Custom Roles / Audit / SAML / Captain 高级 / Voice；云端 SaaS = chatwoot.com 托管 + SOC 2 Type II；周边仓库 = `chatwoot/ai-agents`（独立 agent SDK）、`chatwoot/mobile-app`（独立 Flutter 移动端）、`chatwoot/cwctl`（Go CLI）、`chatwoot/charts`（Helm）——构成完整产品矩阵。开源策略是 **genuine open-core**（不是只读源码的伪开源），社区版功能已可支撑中小团队 80% 场景。

> 官方工程博客覆盖「File Upload 调优 / React Native 深链 / LocalTunnel webhook / Bot 架构 / v3 路线 / Captain AI」等技术决策；DeepWiki 已收录完整架构快照。本次分析未找到有独立分析深度的第三方文章。

## 核心价值提炼

### 创新之处

1. **Open-core `prepend_mod_with` 注入模式（仿 GitLab EE）**：用 Ruby `prepend` 语义让 enterprise 模块在 OSS 之前插入；`ChatwootApp.extensions` 控制注册；`config.paths['app/views'].unshift('enterprise/app/views')` 让视图也可被覆盖——同一分支、同一 PR 流程、同一测试套件。
2. **Captain 工具注册表（`method_missing` 把 LLM tool name 变成可调用方法）**：LLM 返回的 tool name 直接映射到内部 `execute`，业务对象无需通过 LangChain.rb 这类框架桥接。
3. **pgvector + neighbor gem 把 RAG 检索压进 Postgres**：`ArticleEmbedding has_neighbors :embedding, normalize: true` + `using ivfflat` 索引——知识库检索走 SQL 不走外部向量库，复用 PG 的事务 / 备份 / 索引 / 权限。
4. **多租户 `pubsub_token` = HMAC 房间名 + ActionCable 鉴权**：不维护「用户连接 ↔ 房间」关系表，contact 和 user 共用同一 `RoomChannel` 协议。`ActionCableBroadcastJob` 异步广播解决「推送失败拖慢主链路」。
5. **Captain CustomTool 的「租户自带 HTTP tool」抽象**：租户在 UI 配置 `endpoint_url` / `http_method` / `param_schema` / `request_template` / `response_template` / `auth_type`；`SafeEndpointValidatable` 强制 SSRF 防护（防 169.254.169.254、127.0.0.1、内网 IP 段）——LLM 通过 OpenAI function-call 协议调用租户自有 API。
6. **Liquid 模板同时复用为 Message 模板 + Canned Response + Captain Prompt**：`app/models/concerns/liquidable.rb` 在消息模板上跑 `{% raw %}` 包裹的 Liquid；`app/drops/` 提供 conversation/contact/inbox 的 drop；Captain system prompt 同样用 Liquid 子模板复用——把 Shopify 生态的成熟方案引入客服场景。
7. **Wisper + Sync/Async 双 Dispatcher 事件总线**：业务动作同时推同步 WebSocket listener（`ActionCableListener`）与异步 Sidekiq listener（`WebhookListener` / `AutomationRuleListener` / `CampaignListener` / `ReportingEventListener` 等 10+）——同步保用户体验、异步保业务解耦。

### 可复用的模式与技巧

1. **Polymorphic Channel + 独立 Service 包**：用 polymorphic `Inbox.channel` 抽象外部系统，每个 provider 一个子目录（`app/services/<provider>/`）配 `incoming_*` / `send_on_*` / `webhook_*` / `*_template_*`——加新渠道成本固定，新人也能照葫芦画瓢。
2. **Wisper + Sync/Async 双 Dispatcher**：业务事件同时推同步 WebSocket listener 与异步 Sidekiq listener；同步是「用户体验」、异步是「业务解耦」。
3. **Open-core `prepend_mod_with` 注入**：任何想做免费/付费分层的 Rails 应用都可复用（GitLab 已用、Chatwoot 已用）。
4. **HMAC 房间名**：让 WebSocket 鉴权与房间名合二为一，省去「用户连接 ↔ 房间」关系表。
5. **PG + pgvector 单库 RAG**：不引入专用向量库，复用 PG 的事务 / 备份 / 索引 / 权限。
6. **Liquid drop 抽象领域对象**：模板里的 `{{ contact.name }}` 用 `ContactDrop.new(contact).name` 而不是直接暴露 AR 对象——安全沙箱 + 模板复用。
7. **Service Object + Builder 分工**：复杂业务用 `Service`（执行态变更），创建型用 `Builder`（决定是否复用 / 新建）。
8. **PG `ivfflat` + `DISTINCT ON` 联合使用**：「每个 conversation 最后一条用户消息」比 `ROW_NUMBER() OVER` 在 PG 上更省。
9. **WhatsApp incoming 原子去重（Redis SET NX）**：`lock_message_source_id!` 防止 Meta 重复投递或多 worker 并发处理同一消息——任何接 webhook 都需要的幂等范式。

### 关键设计决策

| 决策 | 问题 | 方案 | Trade-off | 可迁移性 |
|------|------|------|-----------|----------|
| 多租户 = Account 实体 + 复合索引 + pubsub_token | SaaS 多租户数据隔离 + ActionCable 路由 | 所有核心实体 `belongs_to :account` + HMAC token 作为房间名 | 无法用 PG RLS 兜底，显式带 account 上下文 → 换 Rails 直观、单实例多租户免运维 | 高 |
| Channel 抽象 = Polymorphic + 子类 + 独立 Service 包 | 10+ 第三方渠道鉴权/格式/限流差异巨大 | `Inbox.channel` polymorphic + 每渠道独立 service 子目录 | 新渠道需建 4-8 个文件跨 4 目录 → 换每渠道独立可替换、可降级 | 中 |
| 事件总线 = Wisper + 双 Dispatcher + Listener 注册表 | 一次业务动作需驱动 WS / Webhook / Automation / SLA 等 10+ 下游 | SyncDispatcher 给 ActionCable，AsyncDispatcher 经 Sidekiq 落 critical 队列 | 同步 listener 阻塞请求线程 → 换实时刻画即时生效 | 高 |
| Open-core 注入 = `prepend_mod_with` | OSS/EE 同分支但需差异化 | Ruby `prepend` + `config.paths['app/views'].unshift` | 调试栈阅读门槛上升 + EE 模块必须与 OSS 同名同签名 → 换同一 PR/测试流程 | 高 |
| Captain AI = 独立 enterprise/lib + Liquid prompt + Tool Registry + pgvector RAG | 让 LLM 基于知识库回答 + 调用业务工具 | `method_missing` tool 路由 + `ArticleEmbedding has_neighbors` + `SafeEndpointValidatable` SSRF 防护 | OSS 完全不依赖 OpenAI → 干净隔离，但 EE 测试需 stub | 高 |
| ActionCable pubsub_token + `ActionCableBroadcastJob` | WS 推送不阻塞主请求 | HMAC 房间名 + Sidekiq 异步广播 | 多一跳延迟 ~10ms → 换失败可重试 + 主链路不被拖慢 | 中 |
| Service + Builder 分工 | 业务动作复杂化 | `app/services/<domain>/<verb>_service.rb` + `app/builders/` 创建型 | 命名边界靠 code review 维护 → 换每类动作一个入口、好测试 | 高 |
| Conversation 状态机 = enum + 多 scope + 复合索引 | 工单状态/优先级/分配/SLA 可观测 | `enum status` + 复合索引 + `DISTINCT ON` 拿最后用户消息 | enum 扩展要写 migration → 换查询计划稳定 | 高 |
| Markdown → 渠道特定格式 = 策略模式 | 同一段消息发到 11 渠道语法不同 | `Messages::MarkdownRendererService` 用 `CHANNEL_RENDERERS` 字典映射 | 每加渠道需新增方法分支 → 换渲染与业务逻辑解耦 | 中 |
| Webhook 投递 + 重试 = Sidekiq + RetryableError | 第三方 webhook 带退避重试 + 失败可查 | `lib/webhooks/trigger.rb` 自定义 `RetryableError` + `AgentBots::WebhookJob` retry_on | 默认 3s 重试偏短 → 换与 Rails/Sidekiq 同套机制 | 高 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Chatwoot | Zammad | FreeScout | osTicket | Intercom/Zendesk（闭源） |
|------|---------|--------|---------|---------|----------------------|
| Stars | 31.2K | 5.7K | ~3K | ~3K | N/A |
| 技术栈 | Rails 7.1 + Vue 3 + Postgres | Rails 5 + Vue 2 | PHP + MySQL | PHP + MySQL | 闭源 |
| 全渠道 | 11+ 渠道 | 主要 email + 部分社交 | 仅 email | 仅 email/ticket | 全渠道（Fin AI 等） |
| AI 能力 | Captain（pgvector RAG + Tool Registry + Custom Tool） | 几乎为零 | 几乎为零 | 几乎为零 | Fin AI（闭源、烧钱） |
| 自托管 | 一行 docker-compose | 支持但运维重 | 支持但功能弱 | 支持但功能弱 | 不支持 |
| 数据主权 | 完全可控 | 完全可控 | 完全可控 | 完全可控 | 不可控 |
| 商业模式 | Open-core + 云端 SaaS | 完全开源 + 商业支持 | 完全开源 | 完全开源 | 纯 SaaS 按席位 |
| 移动端 | Flutter 独立 app（928 stars） | 弱 | 弱 | 无 | 强 |
| 实时协作 | ActionCable WebSocket | 弱 | 无 | 无 | 强 |
| 多语实时 | Captain 多语翻译 + 35+ 语言 | 部分 | 弱 | 弱 | 强 |
| 合规 | SOC 2 Type II（云端） | 自管 | 自管 | 自管 | 强 |

### 差异化护城河

- **技术护城河**：11+ 渠道 polymorphic Channel 抽象 + Captain AI（pgvector RAG + Tool Registry + Custom Tool + SSRF 防护）+ ActionCable 实时 + Open-core `prepend_mod_with` 注入 = 「多渠道 + AI 平台」组合难以复制。
- **生态护城河**：Crowdin 多语翻译 35+ 语言、Shopify/Linear/Slack/Dialogflow 集成、Helm chart、cwctl Go CLI、独立 mobile app、ai-agents 独立 SDK。
- **信任护城河**：YC W21 背书 + SOC 2 Type II 合规 + 9.6 年账号 + 70 仓库 + 1162 stars + 主仓 31K stars 的开源信任。

### 竞争风险

- **最可能的颠覆者**：Intercom 的 Fin AI（闭源、烧钱、品牌强）——若大企业客户对自托管意愿下降、对 Fin 的现成知识库垂手可得，可能把 Chatwoot 压回 SMB 市场。
- **次要风险**：Zammad 在 IT 服务台深耕（流程引擎完备、SLA 强）、Microsoft Dynamics 365 Customer Service 在企业 CRM 套件中夹击、Freshdesk 在中端 SaaS 持续渗透。
- **自家风险**：bus factor 高——Top 5 员工贡献 99.2% commits，团队扩展速度跟不上业务扩展速度；fix commit 占比 46% > feature 32%，refactor 仅 2.5%，技术债在被堆积。

### 生态定位

客服细分赛道的「开源 + AI 原生 + 全渠道」瑞士军刀；与 LangChain 生态通过 ruby_llm 桥接，与 Shopify 生态通过 Liquid 模板桥接，与 Vector DB 生态通过 pgvector 单库桥接——少有的「客服 + 业务系统 + AI」三位一体开源标杆。填补了「Zendesk 太贵 + Zammad 太旧 + Intercom 太封闭」的市场空白。

## 套利机会分析

- **信息差**：已被充分发现（31K stars、YS 报道多次），不存在套利空间；属于「已被低估的低成本 Zendesk 替代」叙事里的头部赢家。
- **技术借鉴**（高价值）：
  - **`prepend_mod_with` Open-core 模式** → 可直接迁移到任何想分社区/企业版的 Rails 应用（GitLab 模式 + Chatwoot 验证）
  - **Captain Tool Registry（`method_missing` 路由 LLM function call）** → 可迁移到任何想把 LLM 接到业务系统的项目，比 LangChain.rb 抽象更轻
  - **PG + pgvector 单库 RAG** → 中小团队 AI 应用不需要 Pinecone / Weaviate / Qdrant，复用 PG 即可
  - **Polymorphic Channel + 独立 Service 包** → 可迁移到 notification 多通道、payment provider、storage backend 等场景
  - **Wisper + Sync/Async 双 Dispatcher** → 可迁移到任何「关键路径同步 + 非关键路径异步」的事件驱动设计
- **生态位**：开源客服赛道的「Rails 唯一 + AI 唯一」组合位；与 Zammad / FreeScout / osTicket 形成「现代 vs 传统」分层，与 Zendesk / Intercom 形成「开源 vs 闭源」分层。
- **趋势判断**：在增长（近 90 天 389 commits、月均 ~130、版本 v4.14.2 持续推进）；符合 LLM agent 化 + 自托管 + 开源合规三大趋势；比闭源 SaaS 有「数据主权」后发优势，比传统开源有「AI 原生」先发优势。

## 风险与不足

- **bus factor 高**：Top 5 员工贡献 99.2% commits，外围 378 贡献者多数每人 1-2 个 PR。一旦核心 2-3 人离职节奏会断。
- **技术债堆积**：fix 占比 46% > feature 32%，refactor 仅 2.5%——说明稳定期靠打补丁过日子，未做大架构重构。
- **注释比极低（1.5%）**：典型 SaaS 创业团队风格——优先 ship 代码，文档/注释滞后，新人上手成本高。
- **README 媒体路径失效**：`github/screenshots/*.png` 旧路径在 develop 分支已不存在（verified=false），新截图迁移到官网 `chatwoot.com/images/`——造成 README 视觉断档，新访客第一印象打折。
- **长期未解决的 issue**：#8869 Office 365 邮件接入稳定性（跨多年未根治）、#2011 Google 多语翻译（6 年未结，最终靠 Captain 间接落地）——第三方 SaaS API 集成稳定性是 self-hosted 用户的长期痛点。
- **AI 投入集中在企业版**：Captain AI 主体在 `enterprise/` 目录，OSS 版只能用基础能力——开源铁杆粉丝会介意。
- **深夜提交占比 20%**：印度时区团队 + 欧美客户的异步 review 跨时区压力，长期看是员工 burnout 隐患。

## 行动建议

### 如果你要用它

- **场景判断**：年客服量 1k-100k 单、需要 5+ 渠道接入、有数据主权诉求、有工程团队能 5×8 小时运维、有意愿试 AI agent——选 Chatwoot 自托管。
- **如果你是 10 人以下初创**：考虑 Chatwoot 云端 SaaS（chatwoot.com），避免运维负担。
- **如果你的核心是工单流程**：Zammad 更适合（流程引擎完备、SLA 强）。
- **如果你是个人站长邮件客服**：FreeScout 更轻（PHP 单体、5 分钟装好）。
- **如果你的预算充裕且不愿运维**：Zendesk / Intercom / Freshdesk 更省心。
- **迁移成本**：从 Zendesk / Intercom 迁移需要重写自动化规则（macros / triggers 对应 Chatwoot 的 automation_rules + macros + sla），建议先并行 2-3 个月再切流量。

### 如果你要学它

重点关注以下文件/模块（按学习优先级排序）：

1. **`config/initializers/01_inject_enterprise_edition_module.rb`** + **`enterprise/app/`**——Open-core `prepend_mod_with` 模式的完整实现，看 30+ 关键类末尾的 `xxx.prepend_mod_with('Xxx')` 钩子
2. **`app/models/inbox.rb`** + **`app/models/channel/*.rb`**（11 个）——Polymorphic Channel 抽象，看一个外部系统怎么被「同类化」
3. **`app/dispatchers/`** + **`app/listeners/`**（13 个）+ **`lib/events/types.rb`**——Wisper + Sync/Async 双 Dispatcher 事件总线
4. **`enterprise/app/services/captain/tool_registry_service.rb`** + **`enterprise/lib/captain/prompts/*.liquid`**——LLM Tool Registry + Liquid prompt 模板
5. **`enterprise/app/models/article_embedding.rb`**——`has_neighbors :embedding, normalize: true` 一行启用 pgvector RAG
6. **`app/models/concerns/liquidable.rb`** + **`app/drops/`**——Liquid drop 安全沙箱化领域对象
7. **`config/application.rb`**——EE eager_load + 视图前插 + APM 按需加载 + 加密按需加载的整体架构入口
8. **`AGENTS.md`**——团队给 LLM 写的开发规范（EE/OSS 双仓协作 checklist、Vue Composition API、commit message、PR 描述）
9. **`.circleci/config.yml`** + **`.github/workflows/`**（9 个）——完整 CI/CD 流水线（lint / frontend-tests / backend-tests / EE-spec + Dependabot + 安全扫描）

### 如果你要 fork 它

可改进的方向：

- **降 bus factor**：把 Top 5 员工的核心知识文档化（目前 1.5% 注释比是反例）
- **加 CHANGELOG**：目前无集中 CHANGELOG.md，发布历史在 release tag / GitHub Releases，缺少「breaking change」摘要
- **加 examples/ 目录**：目前仓库内无 examples/，新人需翻 docs/chatwoot.com 才能跑通常见场景
- **补 README 截图**：把官网媒体（dashboard / captain）回填到 `github/screenshots/`，避免 verified=false 路径失效
- **拆 captain 出 enterprise**：OSS 铁杆粉丝介意 AI 投入集中在 EE，可考虑把 Captain 基础能力下沉到 OSS，高阶工具留 EE
- **补 type-safe 前端**：当前仅 PropsType 检查，迁移到 TypeScript 可降低 dashboard 端的运行时错误
- **加 GraphQL 层**：当前 RESTful API + Swagger 维护成本高，移动端 + 第三方集成若上 GraphQL 会显著降低接入成本

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [https://deepwiki.com/chatwoot/chatwoot](https://deepwiki.com/chatwoot/chatwoot)（已收录，2026-06-12 索引，14 章节覆盖技术栈 / 多租户 / Captain AI / 部署） |
| Zread.ai | 未单独验证 |
| 关联论文 | 无（客服平台领域无 arXiv 适用论文） |
| 在线 Demo | 官网 [https://www.chatwoot.com](https://www.chatwoot.com) 提供云端试用入口；自托管可 `docker-compose up` 起 demo |
| 官方工程博客 | [https://www.chatwoot.com/blog](https://www.chatwoot.com/blog)（Captain AI 架构 / File Upload 调优 / React Native 深链 / Bot 架构 / v3 路线） |
| 源码仓库（核心） | `config/application.rb` / `config/routes.rb` / `app/models/{account,inbox,conversation,message}.rb` / `app/services/base/send_on_channel_service.rb` / `app/dispatchers/` / `enterprise/app/services/captain/tool_registry_service.rb` |