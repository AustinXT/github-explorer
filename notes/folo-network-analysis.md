## 仓库基本数据
- Star / Fork / Watcher: 37,931 / 2,015 / 146
- 语言: TypeScript (95.4%), Swift (2.1%), CSS (1.1%), JavaScript (0.7%), HTML (0.2%), Kotlin (0.2%), Shell (0.2%)
- License: GNU Affero General Public License v3.0 (AGPL-3.0)
- 创建时间: 2024-04-08 | 最近推送: 2026-04-05
- 话题标签: reader, rss, rss-reader, ai, rsshub
- 已归档: 否 | 是Fork: 否
- 主页: https://app.folo.is
- 磁盘占用: ~73 MB
- Issue 总数: 380 | PR 总数: 8
- 默认分支: dev

## 作者画像
- 组织ID: RSSNext | 口号: "Open Information!" | 官网: https://rssnext.org/
- 粉丝: 1,247 | 公开仓库: 17 | 账号创建: 2021-12-03（约4.3年）
- 此 repo 投入权重: **极高** — Folo 是该组织的旗舰项目（37.9k star），其余仓库均为 Folo 的配套设施（rsshub-docs, follow.is, follow-contracts, follow-email-worker 等）
- 作者类型: **开源组织/初创团队** — RSSNext 由 Natural Selection Labs（DIYgod 所在公司，位于新加坡）孵化，非纯粹个人项目
- 贡献集中度: **小团队主导**
  - Top 3 贡献者占据绝大多数 commits：Innei (2,842), DIYgod (1,847), hyoban (990)
  - 第 4 名 lawvs (375) 开始急剧下降，后续贡献者均为个位数到两位数
  - 核心开发由 3 人驱动，约 30 名社区贡献者参与
- 核心人物分析:
  - **Innei**（最大贡献者）: 数字游民/设计工程师，LobeHub 成员，Gen-Z，粉丝 3,316，公开仓库 310，维护 mx-space、Afilmory 等项目，典型的多产全栈开发者
  - **DIYgod**（第二贡献者）: RSSHub 创始人，Natural Selection Labs 成员，位于新加坡，粉丝 15,747，知名中文开源开发者，个人影响力极大（「写代码是热爱，写到世界充满爱」），RSSHub 43k star 验证其在 RSS 生态的统治级地位
  - **hyoban**（第三贡献者）: 990 次提交，核心架构贡献者
- 背景推断: Folo 由 RSSHub 创始人 DIYgod 领衔的团队打造，是 RSSHub 生态的自然延伸——从「RSS 源聚合」走向「RSS 阅读器」。团队有 Natural Selection Labs 商业实体支撑，技术实力和 RSS 领域经验均属顶尖。

## 社区热度
- 热度级别: **S 级（现象级）** — 37.9k star，在 RSS 阅读器品类中仅次于 RSSHub 本身（43k），远超所有竞品阅读器
- 增长模式: **持续高增长型**
  - 2024-04 创建 → 2024-10 达到 ~10,000 star（6 个月破万）
  - 2024-12 达到 ~20,000 star（8 个月破两万）
  - 2025-08 达到 ~30,000 star（16 个月破三万）
  - 2026-02 达到 ~37,000 star（22 个月接近四万）
  - 2026-04-03 最近一天仍有 ~20 个新 star，日均增长保持稳定
- 近期趋势: 增长速度在 2024 年下半年最快（可能受产品发布和 HN 曝光驱动），2025 年后进入稳健增长期，日增长略有放缓但仍保持可观水平
- 套利判断: **非刷星项目** — 增长曲线平滑且持续两年，早期有明显的自然传播拐点（2024-05-03 出现一波密集 star，疑似 HN/Product Hunt 曝光），后续增长匀速健康，具有真实用户基础

## 生态网络
- 上游依赖:
  - **RSSHub** (DIYgod/RSSHub, 43k star) — Folo 的核心 RSS 源供给，两个项目同属一个组织
  - **RSSHub-Radar** (DIYgod/RSSHub-Radar, 7.1k star) — 浏览器发现 RSS 源的扩展，与 Folo 形成完整工具链
  - React 19, Electron 38, Expo SDK 53, Fastify 5, Drizzle ORM, Zustand, Jotai, TanStack Query
- 同类项目（TypeScript RSS 生态）:
  - fluent-reader (9.2k star) — Electron 桌面 RSS 阅读器
  - wewe-rss (9.1k star) — 微信公众号 RSS 生成
  - DailyHotApi (3.7k star) — 热榜聚合 API
  - huntly (2.3k star) — AI 信息中心
  - fusion (2.0k star) — 轻量自托管 RSS 阅读器

## 官方文档洞察
- 价值主张: 「AI 驱动的无噪音信息阅读器」— 将多源内容组织进统一时间线，通过 AI 实现翻译、摘要、标签分类，消除信息噪音
- 目标用户: 重度信息消费者、RSS 老用户、开发者、追求跨平台同步的阅读者、想替代社交媒体 doom-scrolling 的用户
- 差异化叙事: 「Your thoughts are what you read」— 不只是技术工具，而是信息消费哲学的体现。强调「开放信息」理念，与封闭的算法推荐形成对比
- 设计哲学: 全平台覆盖（Web/Desktop/iOS/Android/Linux），精致 UI（明暗主题自适应），社区驱动（Discord 活跃），BYOK（自带 AI Key）尊重用户选择
- 技术路线图: 未公开正式路线图。从近期动态看：移动端持续完善（App Store/Google Play 已上架）、MCP Server 集成（AI 工程师生态）、付费功能规划中（ToS 已提及但尚未推出）
- 架构文章要点（DeepWiki）:
  - pnpm monorepo 架构，Turbo 编排构建
  - 三平台应用共享代码：Desktop (Electron), Mobile (Expo/React Native), SSR (Fastify)
  - 数据层使用 Drizzle ORM 抽象，支持 SQLite（移动端）和 IndexedDB（桌面端）
  - 内部包体系 @follow/* 实现高度模块化
  - 代码签名：Windows (SignPath), macOS/iOS (Apple Developer Program)
- 外部深度视角:
  - **Privacy Guides 社区讨论**: 用户对 Folo 的隐私性存疑——Brave Shields 拦截到大量追踪器，云端托管模式意味着开发者可看到用户的 RSS 订阅列表。部分用户对「AI 无处不在」表示反感，但也有用户认可 AI 摘要是真实有用的功能。UI 获得好评，但也有人认为对 RSS 阅读器来说过于复杂。OpenRSS 指出 Folo 未使用正规 User-Agent 抓取 feed（存在争议）
  - **Zapier 2026 年最佳 RSS 阅读器**: Folo 入选主流评测榜单
  - **多平台评价 4.8/5**: 应用商店评分高，用户称赞 AI 摘要节省时间、多平台体验流畅

## 竞品清单
| 竞品 | Star | 语言 | 定位 | 差异点 |
|------|------|------|------|--------|
| **NetNewsWire** (Ranchero-Software) | 9,897 | Swift | macOS/iOS 原生 RSS 阅读器 | 纯本地、无 AI、Apple 生态专属，隐私友好 |
| **fluent-reader** (yang991178) | 9,219 | TypeScript | Electron 桌面 RSS 阅读器 | Fluent UI 设计，纯桌面，无 AI，无云同步 |
| **ReadYou** (ReadYouApp) | 7,041 | Kotlin | Android Material You RSS 阅读器 | Android 专属，本地优先，Material Design |
| **FreshRSS** (FreshRSS) | — | PHP | 自托管 RSS 阅读器 | 功能最全的自托管方案，类 Inoreader 体验 |
| **Miniflux** (miniflux) | — | Go | 极简自托管 RSS 阅读器 | 极致简洁高性能，开发者向 |

Folo 的独特定位：**唯一同时具备 AI 能力 + 全平台覆盖 + 云同步 + 开源** 的 RSS 阅读器。竞品要么缺 AI（NetNewsWire、FreshRSS），要么缺跨平台（ReadYou、fluent-reader），要么非开源（Feedly、Inoreader）。

## 关键 Issue 信号
1. **#4651 — 「新版本 UI 和交互非常陌生」**(35 评论, closed, enhancement)
   - 揭示了一次重大 UI 重构引发的用户反弹。说明团队在积极迭代设计，但变更幅度大导致老用户不适应。产品处于快速演进期，设计语言尚未完全稳定。
   - https://github.com/RSSNext/Folo/issues/4651

2. **#4646 — 「Subscription limit（订阅限制）」**(30 评论, closed, bug + platform:desktop)
   - 涉及订阅数量上限的争议，可能与未来付费模式相关。社区对免费层级的限制较敏感，这是商业化路径的关键信号。
   - https://github.com/RSSNext/Folo/issues/4646

3. **#2473 — 「每次登录都需要重新登录」**(56 评论, closed, bug)
   - 最高评论数的 Issue，反映了早期严重的认证/会话持久化问题。已修复，但说明云服务稳定性曾是用户痛点。
   - https://github.com/RSSNext/Folo/issues/2473

## 知识入口
- DeepWiki: https://deepwiki.com/RSSNext/Folo — **可用**，包含完整架构分析（monorepo 结构、状态管理、数据库抽象、平台适配等）
- Zread.ai: https://zread.ai/RSSNext/Folo — **不可用**（403 Forbidden）
- 关联论文: 无直接关联论文。arxiv 上的 FOLIO 等为同名但无关的 NLP/逻辑推理数据集
- 在线 Demo: https://app.folo.is — **官方 Web App**，可直接注册使用
- HN 讨论: https://news.ycombinator.com/item?id=46033915 — Show HN 帖子
- Discord 社区: https://discord.gg/AwWcAQ7euc
- X/Twitter: https://x.com/folo_is
- MCP Server: https://www.pulsemcp.com/servers/hyoban-folo-rss-reader — Folo RSS MCP Server（AI 工程师可集成）

## 项目展示素材
### README 媒体
1. **Folo Mobile 展示图** — 移动端 App 界面截图
   `https://github.com/user-attachments/assets/35747716-28bf-413a-822b-aa49d49f1aa0`

2. **Folo Desktop 展示图** — 桌面端界面截图
   `https://github.com/user-attachments/assets/198a0165-b8c9-45c1-9116-b473a13a8d0c`

3. **Star History 动态图** — GitHub Star 增长曲线
   `https://github.com/user-attachments/assets/a08f9437-b24c-4388-8f01-2826e09eeaf2`

### 筛选说明
- 排除了约 15 个 shields.io badges（star 计数、下载量、版本号、商店链接等）
- 排除了 2 个 App Store/Google Play 商标图片（纯 badge 性质）
- 排除了 ossinsight 统计嵌入图（动态生成，非产品展示）
- 排除了 Logo SVG（icon.svg，不适合展示）
- 排除了 2 个顶部小装饰图（cbe924f2、6997a236，高度仅 60px）
- 保留了最具代表性的 3 张：移动端、桌面端、增长曲线

## 快速判断
- 是否值得深入: **强烈推荐** — 37.9k star 的现象级开源 RSS 阅读器，AI + RSS 的结合点具有话题性，RSSHub 创始人背书确保技术可信度，产品已全平台上线且用户评价极高
- 初步定位: 「RSSHub 生态的消费端闭环」— 从 RSS 源聚合（RSSHub）到 AI 阅读器（Folo），构建了开源世界最完整的 RSS 工具链。适合写「开源 AI 阅读器如何挑战 Feedly/Inoreader」的角度
- 作者可信度: **极高** — DIYgod 是中文开源圈最知名的 RSS 领域开发者（RSSHub 43k star），Innei 是活跃的全栈开发者（LobeHub 成员），有 Natural Selection Labs 商业实体支撑
- 竞品格局: RSS 阅读器市场高度碎片化，Folo 凭借「AI + 全平台 + 开源 + 云同步」的组合拳占据独特生态位。主要威胁来自隐私敏感用户的抗拒（云端模式 vs 本地优先）和商业化路径的不确定性（付费功能尚未推出）
