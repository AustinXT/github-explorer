# calcom/cal.com Phase 1：网络分析报告

> GitHub: https://github.com/calcom/cal.com
> 分析时间: 2026-03-22

---

## 1.1 仓库基本数据

| 维度 | 数据 |
|------|------|
| 名称 | cal.com |
| 描述 | Scheduling infrastructure for absolutely everyone. |
| 主页 | https://cal.com |
| Star / Fork | 40,659 / 12,264 |
| Watchers | 179 |
| Open Issues（含 PR） | 1,384 |
| 许可证 | AGPLv3（自定义，SPDX 标记为 NOASSERTION） |
| 主语言 | TypeScript（29.8M，占 97%+） |
| 其他语言 | CSS (401K), HTML (147K), PLpgSQL (59K), JavaScript (72K), Shell (14K), Mermaid (21K), Apex (15K), PHP (1.3K), MDX (1.7K), Dockerfile (4K) |
| 仓库大小 | 1.14 GB |
| 创建时间 | 2021-03-22（已 5 年整） |
| 最近推送 | 2026-03-21（昨天） |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 默认分支 | main |
| Topics | `open-source` `typescript` `nextjs` `next-auth` `postgresql` `prisma` `t3-stack` `tailwindcss` `trpc` `turborepo` `zod` |
| 最新版本 | v6.2.0（2026-03-01） |
| Docker 拉取量 | 3,769,951 |
| 社区健康度 | 100%（README, CONTRIBUTING, CODE_OF_CONDUCT, PR Template 齐全） |
| Discussions | 已启用 |

**技术栈**：Next.js + tRPC + React + Tailwind CSS + Prisma + PostgreSQL + Redis + Turborepo + Zod

---

## 1.2 作者画像

### 组织信息

| 维度 | 数据 |
|------|------|
| 组织 | Cal.com, Inc.（@calcom） |
| 描述 | Scheduling infrastructure for absolutely everyone. |
| 官网 | https://cal.com |
| 公开仓库数 | 42 |
| GitHub 关注者 | 1,761 |
| 创建时间 | 2021-02-16 |
| 融资 | $32.4M 总融资（Seed + Series A），Series A $25M 由 Seven Seven Six 领投（2022-04），估值约 $150M（2024） |
| 营收 | $5.1M（2024），较 2023 年 $1.6M 增长 3.2 倍 |
| 投资方 | Seven Seven Six（Alexis Ohanian 的基金）、OSS Capital、Obvious Ventures 等 8 家机构 |

### 创始人

**Peer Richelsen** (@PeerRich)
- Cal.com 联合创始人
- GitHub 1,120 followers，930 次代码贡献
- Twitter: @peer_rich
- 个人页: https://cal.com/peer

### 组织活跃仓库 Top 5

| 仓库 | 最近推送 | Stars | 语言 |
|------|---------|-------|------|
| companion | 2026-03-22 | 8 | TypeScript |
| wp-plugin | 2026-03-21 | 15 | PHP |
| cal.com | 2026-03-21 | 40,659 | TypeScript |
| help | 2026-03-18 | 5 | MDX |
| sans-ui | 2026-03-17 | 107 | JavaScript |

注：`cosscom/coss`（9,471 stars）是 cal.com 的新控股公司，定位为 "cal.com 的 Alphabet"。

### 核心贡献者 Top 10

| 排名 | 用户 | 贡献次数 | 角色推测 |
|------|------|---------|---------|
| 1 | zomars | 1,418 | 核心维护者 |
| 2 | emrysal | 1,083 | 核心开发 |
| 3 | PeerRich | 930 | 联合创始人 |
| 4 | hariombalhara | 865 | 核心开发 |
| 5 | crowdin-bot | 764 | 翻译机器人 |
| 6 | sean-brydon | 682 | 核心开发 |
| 7 | Udit-takkar | 570 | 核心开发 |
| 8 | hbjORbj | 559 | 核心开发 |
| 9 | anikdhabal | 525 | 社区贡献者 |
| 10 | keithwillcode | 517 | 核心开发 |

**贡献者特征**：核心团队 8-10 人，社区贡献者活跃（可见 gitstart-calcom、calcom-bot 等自动化贡献，以及 Algora 赏金机制吸引社区开发者）。crowdin-bot（764 贡献）说明国际化工作量巨大。

---

## 1.3 社区热度

### Star 增长趋势

- **创建初期**（2021-03）：首批 star 2021-03-25 起
- **首次爆发**（2021-04-15）：单日密集 star，间隔仅秒级 -- 典型 Hacker News / Product Hunt 首页效应
- **当前节奏**（2026-02 采样页 400）：仍保持日均数 star 的稳定增长
- **总量里程碑**：40,659 stars -- 开源日历/调度领域绝对第一

### 活跃度指标

- 最近 5 个 commit（2026-03-18 ~ 03-19）：feat、fix、refactor 并行，开发节奏紧凑
- 最新版本 v6.2.0（2026-03-01），v6.1.x 密集补丁（2 月内 4 个 patch）
- Pull Requests 总数 381 open，Issues 1,003 open
- README 展示 monthly commit activity badge，表明持续高频开发

### 产品里程碑标记

- Product Hunt #1 Product of the Month
- Hacker News #1（至少两次，ID 34507672 和 26817795）
- Trustpilot 4.7 星评分

---

## 1.4 生态网络

### 开源调度领域竞争格局

| 项目 | Stars | 语言 | 定位 |
|------|-------|------|------|
| **calcom/cal.com** | **40,659** | TypeScript | 开源调度基础设施，全功能 Calendly 替代品 |
| cosscom/coss | 9,471 | TypeScript | Cal.com 控股公司（COSS = Commercial Open Source Software） |
| lukevella/rallly | 5,010 | TypeScript | 开源会议投票/协调工具 |
| Easy!Appointments | 3,000+ | PHP | 轻量级预约系统，面向小企业 |
| Croodle | - | - | 隐私优先的群组日程协调 |

**Cal.com 在开源调度领域具有压倒性优势**，stars 数量是第二名 Rallly 的 8 倍。其生态还包括：
- **WordPress 插件**（wp-plugin，15 stars）
- **Framer 插件**（framer-plugin）
- **示例代码库**（examples）
- **帮助文档**（help，MDX 格式）
- **UI 组件库**（sans-ui，107 stars）
- **Docker 官方镜像**（377 万+ 拉取）

### 上下游生态

- **上游依赖**：Next.js, tRPC, Prisma, Tailwind, Radix UI, Daily.co（视频）
- **下游集成**：Google Calendar, Outlook, Zoom, Stripe, Zapier 等 100+ 集成
- **API 平台**：v2 REST API (NestJS)，支持 OAuth、Managed Users，第三方可深度集成
- **嵌入 SDK**：embed-core（JS）+ Platform Atoms（React），支持白标

---

## 1.5 官方文档与博客洞察

### 官网（cal.com）

- **定位语**：Open Scheduling Infrastructure
- **核心卖点**：开源、自托管、白标、API-first、全功能免费版
- **产品形态**：SaaS（cal.com 托管）+ 自部署（Docker/源码）双模式

### 文档（cal.com/docs → API v2 文档）

文档覆盖三大支柱：
1. **认证体系**：OAuth、API Keys（cal_ / cal_live_ 前缀）、Bearer Token
2. **访问层级**：Teams / Organizations / Platform 三级权限
3. **速率限制**：基础 120 req/min，可升级

**关键洞察**：文档重心从"如何使用 Cal.com"转向"如何将 Cal.com 作为基础设施嵌入你的产品"——这是从 SaaS 工具到 Platform 的战略转型信号。Platform 旧版注册已废弃，转向 OAuth-first，说明正在整合企业集成入口。

### 博客（cal.com/blog）

- 内容方向：Calendly 替代品对比（SEO 策略）、开源日历指南、产品更新
- 近期聚焦：Cal.ai（AI 调度助手）、信用系统（SMS）、OAuth 开发者设置

---

## 1.6 竞品清单

### 商业竞品

| 产品 | 定位 | 定价 | 特点 |
|------|------|------|------|
| **Calendly** | 市场领导者 | Free（1 event type）/ $10-$16/mo | 100+ 原生集成，企业级，但封闭、Trustpilot 仅 1.7 星 |
| **SavvyCal** | 开发者友好 | 付费订阅 | 日历叠加视图，简洁交互，但无开源 |
| **TidyCal** | 极简预算型 | 一次性买断（AppSumo） | 功能极简，适合个人 |
| **Zcal** | 免费增值 | 免费计划慷慨 | 轻量，功能有限 |
| **YouCanBookMe** | 中小企业 | 付费 | 定制化强，针对服务型业务 |
| **Chili Piper** | 企业销售 | 高端定价 | 面向 B2B 销售团队的会议路由 |
| **Koalendar** | 简单免费 | 免费 | 极简主义，无团队功能 |
| **Zeeg** | 欧洲市场 | 免费/付费 | GDPR 合规优先 |

### Cal.com 竞争优势

1. **开源 + 自托管**：唯一提供完整自部署能力的企业级调度工具
2. **免费版功能丰富**：无限事件类型、日历连接、工作流、嵌入（Calendly 免费版严格限制）
3. **白标能力**：可深度定制 UI，适合 SaaS 产品嵌入
4. **团队定价优势**：$15/用户/月 vs Calendly $20/用户/月
5. **API-first 架构**：v2 API + 嵌入 SDK，开发者体验优越
6. **数据主权**：AGPLv3 保障用户数据控制权

### Cal.com 劣势

1. **部署复杂度**：自托管需要技术能力（PostgreSQL + Redis + Next.js）
2. **集成数量**：原生集成少于 Calendly 的 100+
3. **品牌知名度**：Calendly 仍是"调度=Calendly"的品类代名词
4. **收入规模**：$5.1M vs Calendly 估值数十亿，资源差距大

---

## 1.7 关键 Issue 信号

### 最高评论数 Issues（社区需求信号）

| # | 标题 | 评论 | 状态 | 信号 |
|---|------|------|------|------|
| 3457 | All CalDav Issues here! | 113 | Closed | CalDAV 集成曾是最大痛点，已修复 |
| 5756 | Proton Calendar Integration | 100 | **Open** | 隐私用户强烈需求，社区长期追踪 |
| 1985 | BigBlueButton Integration | 61 | Open | 开源视频会议集成，有 $50 赏金 |
| 23104 | Local dev crazy slow | 67 | Closed | Monorepo 开发体验痛点，已解决 |
| 25556 | OAuth client developer settings page | 27 | Closed | Platform 战略的关键基础设施 |

### 最高反应数 Issues（用户投票信号）

| # | 标题 | 反应数 | 评论 | 状态 |
|---|------|--------|------|------|
| 15 | Check availability in multiple calendars | 38 | 10 | Closed（核心功能已实现） |
| 5756 | Proton Calendar Integration | 34 | 100 | Open |
| 23104 | Local dev crazy slow | 33 | 67 | Closed |
| 8904 | User specified local language (i18n) | 27 | 18 | Open |
| 12 | Docker support | 27 | 4 | Closed（Docker 镜像已提供） |
| 22 | Kubernetes Support | 23 | 8 | Closed |

### Issue 趋势解读

1. **集成需求是第一驱动力**：Proton Calendar、BigBlueButton、KYZON 等集成请求最热门
2. **基础设施已成熟**：Docker (#12)、K8s (#22)、多日历 (#15) 等早期核心需求均已关闭
3. **开发者体验被重视**：monorepo 慢（#23104）引发强烈反响并被解决
4. **社区参与机制**：Algora 赏金（$50 标签）+ GitStart 外包 + Devin AI 辅助 PR
5. **当前活跃方向**：OAuth 平台化（#25556）、AI 自助服务（#22995）、组织级管理（#25067）

---

## 1.8 知识入口

| 平台 | URL | 状态 |
|------|-----|------|
| DeepWiki | https://deepwiki.com/calcom/cal.com | **可用** -- 完整架构文档，含 12 个主要模块（Event Types、Booking Lifecycle、Scheduling、API、Frontend、Organizations、Platform、Automation 等） |
| Zread.ai | https://zread.ai/repo/calcom/cal.com | 页面存在但需 JS 动态加载，内容未直接可用 |
| 官方文档 | https://cal.com/docs | API v2 参考文档，OAuth/API Key 认证 |
| 官方博客 | https://cal.com/blog | 产品更新、对比文章、开源指南 |
| GitHub Discussions | https://github.com/calcom/cal.com/discussions | 已启用，社区交流活跃 |

### DeepWiki 架构概览

DeepWiki 提供了最完整的技术文档：
- **Monorepo 结构**：Turborepo + Yarn Workspaces
- **核心应用**：`@calcom/web`（Next.js 主应用 :3000）、`@calcom/api-v2`（NestJS REST API）、`@calcom/console`（管理后台）
- **关键包**：`@calcom/prisma`、`@calcom/trpc`、`@calcom/features`、`@calcom/ui`（Radix + Tailwind）
- **嵌入层**：`@calcom/embed-core`（JS SDK）、`@calcom/platform/atoms`（React 白标组件）
- **技术版本**：Next.js 16, React 18, TypeScript 5.9, Prisma 6, Turborepo 2.7, Yarn 4.12

---

## 1.9 项目展示素材

### README 主图

![Cal.com Banner](https://user-images.githubusercontent.com/8019099/210054112-5955e812-a76e-4160-9ddd-58f2c72f1cce.png)

Cal.com 产品主界面展示

### 功能演示 GIF

![Cal.com Demo](https://private-user-images.githubusercontent.com/8019099/250881880-407e727e-ff19-4ca4-bcae-049dca05cf02.gif)

预约流程动画演示

### 嵌入演示

![Book with Cal](https://cal.com/book-with-cal-dark.svg)

"Book with Cal" 嵌入按钮

### 荣誉徽章

- Product Hunt #1 Product of the Month: `https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg`
- Hacker News #1: `https://img.shields.io/badge/Hacker%20News-%231-%23FF6600`
- 开源授权: `https://img.shields.io/badge/license-AGPLv3-purple`
- 免费定价: `https://img.shields.io/badge/Pricing-Free-brightgreen`
- Maker Grant: `https://cal.com/maker-grant.svg`

---

## 1.10 快速判断

### 一句话定位

开源调度基础设施的事实标准 -- 五年 40K stars，从 "Calendly 替代品" 成长为可嵌入的调度平台（Scheduling Infrastructure），AGPLv3 许可 + 商业化双轨运行。

### 项目成熟度：成长期 → 扩张期

- **代码成熟**：v6.2.0，主版本迭代 6 次，API v2 已独立为 NestJS 服务
- **商业成熟**：$5.1M ARR（2024），$32.4M 融资，20K 客户
- **社区成熟**：40K stars，12K forks，100% 社区健康度，赏金机制完善
- **仍在快速进化**：Cal.ai（AI 调度）、Platform Atoms（白标组件）、COSS 控股公司结构

### 值得关注的信号

1. **从工具到平台的转型**：API v2 独立服务 + OAuth 开发者门户 + 嵌入 SDK = 正在成为"调度领域的 Stripe"
2. **AI 战略落地**：Cal.ai 自助服务（#22995）、信用系统（SMS #20126）-- 向 AI Agent 调度方向延伸
3. **COSS 公司架构**：cosscom/coss 仓库（9.5K stars）暗示 cal.com 可能是更大商业开源布局的第一块拼图
4. **AGPLv3 的双刃剑**：保护开源贡献不被白嫖，但也增加企业采用的法律审查成本
5. **Proton Calendar 整合**（#5756, 100 评论）是当前社区最强烈的需求，反映隐私敏感用户群体的重要性

### 风险点

- 仓库 1.14GB，monorepo 巨大（开发者入门门槛高，#23104 已修复部分）
- 营收 $5.1M 对比 Calendly 级别的市场仍有量级差距
- AGPLv3 对部分企业场景可能构成采用障碍

---

*Sources:*
- [Cal.com vs Calendly 2026 Comparison - YouCanBookMe](https://youcanbook.me/blog/calendly-vs-cal-dot-com)
- [Cal.com vs Calendly - Efficient App](https://efficient.app/compare/cal-vs-calendly)
- [Cal.com Review 2026 - Efficient App](https://efficient.app/apps/cal)
- [Cal.com vs Calendly - FluentBooking](https://fluentbooking.com/articles/cal-com-vs-calendly/)
- [Top 3 Open-Source Calendly Alternatives 2025](https://blog.houseoffoss.com/post/top-3-open-source-alternatives-to-calendly-in-2025-cal-com-easy-appointments-and-croodle)
- [Cal.com Alternatives - Zeeg](https://zeeg.me/en/blog/post/cal-com-alternatives)
- [SavvyCal vs TidyCal vs Cal.com - Cyber Snowden](https://cybersnowden.com/savvycal-vs-tidycal-vs-cal-com/)
- [Cal.com Funding - Getlatka](https://getlatka.com/companies/calcom)
- [Cal.com Funding - Clay](https://www.clay.com/dossier/calcom-funding)
- [DeepWiki - calcom/cal.com](https://deepwiki.com/calcom/cal.com)
