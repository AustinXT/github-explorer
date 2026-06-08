# 37k star 的 GA 开源替代 Umami：不写 cookie、不存 IP，怎么还能把访客数算对

> GitHub: https://github.com/umami-software/umami

## 一句话总结

Umami 是隐私优先的开源网页分析平台——Google Analytics / Mixpanel / Amplitude 的轻量替代品，追踪脚本 <2KB、不写 cookie、不存 IP、不做指纹，却靠「轮换盐值确定性哈希」把同一访客的多次请求归到一个会话，开箱即 GDPR 合规。它由前 Adobe 数字营销工程师 Mike Cao 主导的 Cao 家族团队打磨 5.9 年至 37k star，走「开源自托管 + Umami Cloud + VC 融资」的商业闭环。

## 值得关注的理由

1. **「隐私即架构」的工程范本**：合规不是一个可勾选的开关，而是写死在数据模型里——IP 和 UA 只在内存里过手（算会话哈希、查 GeoIP、过滤 bot），落库表里**根本没有 IP 字段**。这是 GDPR/CCPA 约束下做数据产品的标准答案。
2. **cookieless 会话归因的事实标准做法**：`sessionId = hash(websiteId, ip, userAgent, monthlySalt)`，盐值按月轮换、visit 按 30 分钟窗口、会话连续性靠内存 token 而非 cookie——既能归因又不留持久标识。这套「轮换盐 + 确定性哈希」值得任何隐私敏感系统借鉴。
3. **「隐私 × 轻量 × 功能够用」的稀缺交点**：比 Plausible/GoatCounter 功能全（已含会话回放、漏斗、Cohort、v3 可定制看板），又比 Matomo/PostHog 轻；双数仓（Prisma + ClickHouse）让同一产品覆盖个人到大流量两端。

## 项目展示

![Umami logo](https://content.umami.is/website/images/umami-logo.png)
Umami——隐私优先的开源网页分析平台。

> README 偏文字说明，产品仪表盘截图建议从官网 https://umami.is 或文档站 https://docs.umami.is 取材。可在 [Umami Cloud 免费 Hobby 版](https://umami.is) 直接体验。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/umami-software/umami |
| Star / Fork | 37,068 / 7,255 |
| 代码规模 | 真实约 **47k 行**（44k TS/TSX + 1.9k SQL）；cloc 总 141k 行中 JSON 59.8% 是虚高——i18n 翻译 67k（**52 语言**）+ 地图数据 17k（datamaps.world + iso-3166-2）+ lock 12k |
| 项目年龄 | 70.8 个月（约 5.9 年，2020-07 创建） |
| 开发阶段 | 密集开发（v3 攻坚后 v3.1 收尾，近一年 1121 commit） |
| 贡献模式 | 核心团队 + 活跃社区（Cao 三人组 Mike/Francis/Brian 占 ~57% commits，423 贡献者长尾） |
| 热度定位 | 大众热门（高速增长，隐私分析赛道头部） |
| 质量评级 | 代码[优·全 TS+zod+Prisma] 文档[良] 测试[中·核心归因缺单测] CI[良] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

灵魂人物 **Mike Cao（@mikecao）**——UC Davis 毕业，早年创业（CampusEngine），后在 **Adobe 数字营销平台**任工程师，深知企业级分析栈（GA360/Adobe Analytics）的复杂与笨重。2020 年他对 GA「又慢又复杂」忍无可忍，一个月写出 Umami 第一版开源，靠 Reddit 走红。核心由「Cao 三人组」（Mike + Francis + Brian Cao，疑家族团队）把控约 57% 提交，外加 423 名社区贡献者。2022 年成立公司，**Race Capital 领投 150 万美元 pre-seed**——是 VC 背书的商业化开源，而非单人项目。

### 问题判断

网页分析的「重 × 慢 × 隐私不友好」三重痛点：GA 脚本臃肿拖慢页面、配置复杂、默认采集个人数据并写 cookie（触发 GDPR/cookie 横幅）、数据所有权归 Google。Cao 的判断是典型的「内行做减法」——不是不懂大而全，而是刻意只保留 80% 用户真正看的那 20% 指标，并把「隐私合规」从负担变成默认卖点。

### 解法哲学

- **隐私是默认，不是选项**：无 cookie、无指纹、不存原始 IP 写死在数据流里，而非可勾选的合规开关。
- **轻量内嵌**：追踪脚本 minify 后 <2KB，用 `__COLLECT_*__` 占位符在构建期注入端点，零运行时配置开销。
- **自托管优先 + 可选增强**：单 PostgreSQL 起步，数据量大了再插 ClickHouse/Kafka/Redis——能力随规模线性叠加，而非一开始就逼用户上重型栈。
- **明确不做什么**：不做用户级跨站追踪、不做 PII 画像。

### 战略意图

开源自托管做流量与心智 → Umami Cloud（Hobby 免费 → Pro $20/月 → Business $200/月）做收入 → Race Capital 融资做加速。技术上正从「极简访问统计」向「产品分析/BI」演进：v3 的 Boards 可定制看板 + 会话回放 + 漏斗/Cohort，是向 PostHog 腹地的小步试探，但坚持「轻量隐私」的差异化锚点。选 MIT 协议（而非 Plausible 的 AGPL）是刻意的生态友好选择，降低商业集成阻力。

## 核心价值提炼

### 创新之处

1. **轮换盐确定性哈希做 cookieless 会话归因**（新颖 4 / 实用 5 / 可迁移 5）：`sessionId = uuid(websiteId, ip, userAgent, sessionSalt)`（SHA-512 确定性哈希），`sessionSalt` 默认按月轮换，`visitId` 按小时 + 30 分钟空闲窗口；会话连续性靠服务端加密 token 存进 JS 内存变量、后续请求带 `x-umami-cache` 头——**不写 cookie 也能归因**。Trade-off：盐轮换让同一访客跨月被算成新访客（这正是隐私的代价与卖点）。
2. **隐私即架构（IP/UA 只过手不落库）**（新颖 3 / 实用 5 / 可迁移 5）：IP 与 UA 仅在内存里临时用于算 session 哈希、查 GeoIP、过滤 bot、IGNORE_IP 黑名单；落库的只有 browser/os/device/country/region/city——ClickHouse `website_event` 表与 `saveEvent` 参数里根本没有 ip 字段。合规从数据模型层面缺省。
3. **追踪脚本零依赖 + 构建期端点注入**（新颖 3 / 实用 5 / 可迁移 5）：纯 IIFE，配置从 `currentScript` 的 `data-*` 属性读，`__COLLECT_API_HOST__` 等占位符由 rollup 在构建期替换、terser 压缩到 <2KB；SPA 通过 hook `history.pushState/replaceState` 自动追页，上报用 `fetch(keepalive, credentials:'omit')` 杜绝 cookie。
4. **双数仓「同名双实现」查询层**（新颖 4 / 实用 4 / 可迁移 3）：`runQuery({ [PRISMA]: fn, [CLICKHOUSE]: fn })` 按 env 分发，每个查询**手写两套 SQL**（PG 用 `count(distinct)`/`{{p::uuid}}`，ClickHouse 用 `uniq()`/`{p:UUID}`）——不是 ORM 抽象掉方言，而是显式并存，让各库都能用原生最优写法（ClickHouse 无事件过滤时自动改读 `website_event_stats_hourly` 小时级预聚合，性能数量级提升）。
5. **会话录制复用主会话 + 采样 + 默认脱敏**（新颖 3 / 实用 4 / 可迁移 4）：基于 rrweb，默认只录 15% 会话（`data-sample-rate`），`maskLevel` 默认屏蔽所有输入框，事件满 100 条或每 10s flush，`waitForSession` 轮询拿到 tracker 的 cache token 才开录——不另起一套会话。
6. **营销级渠道归因词典 + 六大平台 Click ID 捕获**（新颖 3 / 实用 4 / 可迁移 4）：内置 SEARCH/SOCIAL/SHOPPING/PAID 渠道分类词典 + gclid/fbclid/msclkid/ttclid/li_fat_id/twclid 解析 + Web Vitals（CLS 用 session-window、INP 取 p98）——这是营销人才知道的「渠道归因」刚需，体现作者的 Adobe 数字营销背景。

### 可复用的模式与技巧

1. **构建期占位符注入**（`__TOKEN__` + rollup replace）替代运行时配置读取，做到 SDK 零配置开销。
2. **轮换盐 + 确定性哈希 ID**：把「可识别原始数据」转成「周期性不可逆派生 ID」，隐私与归因兼得。
3. **同名双实现 + 分发器**（`runQuery({a, b})`）：当抽象会损失性能时，显式并存比强行统一更优。
4. **逐资源 `can{View,Update,Delete}` 守卫 + 统一短路链**（admin→share→owner→team-role），新增资源类型零心智负担。
5. **多入口收敛到单一处理函数**：像素 GIF（`/p`）/ 跟踪链接（`/q`）/ JS 三入口都内部转发到同一个 `api/send` POST。
6. **派生字段只过手不持久化**：敏感数据用完即弃，从数据模型杜绝 PII 泄露面。
7. **采集层优雅降级**：Redis/ClickHouse/Kafka/读副本全部 `env ? 启用 : 跳过`，单库可跑、重型栈可叠。

### 关键设计决策

- **RBAC = 角色权限表 + 逐资源 can* 守卫**：`ROLES`/`PERMISSIONS`/`ROLE_PERMISSIONS` 映射 + 每类资源一个 permissions 文件，走统一短路链「admin → shareToken → 个人 ownership → 团队角色权限」，显式易审计。
- **可配置脚本名/端点绕广告拦截**：`TRACKER_SCRIPT_NAME`/`COLLECT_API_ENDPOINT` 环境变量在 `next.config.ts` 生成 rewrites，自托管者可把脚本伪装成任意业务文件名，解决 `script.js`//api/send` 被拦截器黑名单导致数据缺失的高频痛点（Issue #2264）。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Umami | Plausible | Matomo | PostHog | GoatCounter |
|------|--------|--------|--------|--------|--------|
| Star/量级 | 37k | ~22k | ~20k | ~28k | ~5k |
| License | MIT | AGPL | GPL | MIT | EUPL |
| 定位 | 隐私轻量分析 | 极简隐私 | 全功能 GA 替代 | 一体化产品分析 | 极轻个人 |
| 脚本体积 | <2KB | ~2.5KB | 重 | 较重 | 极轻 |
| Cookie | 无 | 无 | 默认有 | 默认有 | 无 |
| 进阶能力 | 回放/漏斗/Cohort/Boards | 克制 | 最全 | 最全(开关/实验) | 最少 |
| 自托管 | ✅ | ✅ | ✅ | ✅ | ✅ |

### 差异化护城河

①「隐私优先 × 轻量自托管 × 功能够用」三者交点目前没有同等强势者——比 Plausible/GoatCounter 全，比 Matomo/PostHog 轻；②MIT 协议 + 分钟级 Docker 部署 + 单库起步带来极低采用门槛，形成 37k★ 社区飞轮；③双数仓让同一产品覆盖个人到大流量两端，云托管低价卡位性价比。

### 竞争风险

1. **两线作战风险**：向上（PostHog）做 BI、向下（Plausible）守极简，易丧失「简单」初心。
2. **自托管迁移/升级稳定性是最大摩擦**：高赞 Issue 几乎全是 Prisma 迁移 P3009（#2645）、1.x→2.0 docker 迁移（#1887）、小版本迁移崩（#1406）——既是痛点也是云托管卖点。
3. **统计口径差异**：cookieless 月度盐轮换导致同一访客跨月算新访客，对要求精确归因的用户是硬伤。
4. **新秀逼近**：Rybbit（12k★）在体验层快速逼近。

### 生态定位

开源网页分析「隐私 × 轻量 × 自托管」象限的事实标杆，正以 Boards/回放/漏斗向「轻量产品分析」温和扩张，但锚点始终是隐私与轻量。

## 套利机会分析

- **信息差**：37k star 头部项目，知名度高、不存在「被低估」红利。内容价值在「拆解它的隐私工程（cookieless 归因 + IP 不落库）+ 商业化闭环」，而非介绍它能做网页统计。
- **技术借鉴**：轮换盐确定性哈希、隐私即架构（敏感字段只派生不落库）、构建期占位符注入、双数仓同名双实现、多入口收敛——这些脱离分析场景，对任何「隐私敏感数据产品」「嵌入式 SDK」「OLTP/OLAP 双引擎」都直接可抄。
- **商业借鉴**：「开源自托管（MIT 生态友好）+ 低价云托管 + VC 融资」是开源商业化的清晰范式。
- **趋势判断**：踩中隐私合规 + 自托管 + GA 替代三股趋势，作为「事实标杆」生命力强；v3 Boards/BI 化是增长新点，但要守住「简单」初心。

## 风险与不足

1. **核心团队集中**：Cao 三人组占 ~57% commits，核心高度依赖家族团队。
2. **自托管迁移稳定性**：数据库迁移/大版本升级是社区最大摩擦点。
3. **核心逻辑缺单测**：会话归因/双数仓查询/隐私哈希等关键逻辑只有 6 个 lib 纯函数单测，依赖 E2E 与人工，覆盖偏薄。
4. **cookieless 统计口径**：月度盐轮换使长期留存/跨月访客统计失真。
5. **无 CHANGELOG 文件**：靠 110 个 tag/GitHub Releases 替代。

## 行动建议

- **如果你要用它**：要隐私合规、轻量、自托管、数据自己掌控的网页分析——它是「隐私 × 轻量」象限最佳选择，单 PostgreSQL + Docker 分钟级起；不想运维选 Umami Cloud（Hobby 免费）；要极简纯净选 Plausible；要工程团队全栈产品分析选 PostHog；个人博客选 GoatCounter。
- **如果你要学它**：重点读 `src/tracker/index.js`（<2KB 追踪脚本）、`src/app/api/send/route.ts` + `src/lib/crypto.ts`（cookieless 会话归因）、`src/lib/db.ts` + `src/queries/sql/`（双数仓同名双实现）、`src/permissions/`（RBAC 短路链）、`src/recorder/index.js`（采样 + 脱敏会话录制）。
- **如果你要 fork 它**：方向是把它的隐私工程（轮换盐归因、IP 不落库）搬到你自己的数据产品；或补强核心归因/查询逻辑的单测覆盖。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [已收录（安装/架构/多数据库/追踪 API/会话回放）](https://deepwiki.com/umami-software/umami) |
| Zread.ai | 未确认（直连 HTTP 403） |
| Docker | `ghcr.io/umami-software/umami`（postgresql/mysql 标签，分钟级部署） |
| 官方文档 / Demo | https://umami.is / https://docs.umami.is（Umami Cloud 免费 Hobby 版可体验） |
| 关联论文 | 无（工程产品） |
