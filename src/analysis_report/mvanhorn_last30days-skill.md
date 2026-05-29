# last30days-skill 深度分析报告

> GitHub: https://github.com/mvanhorn/last30days-skill

## 一句话总结
Lyft 联合创始人打造的 AI Agent 实时研究技能——聚合 10+ 社区平台过去 30 天的真实讨论，用参与度加权评分和跨源去重，为 LLM 补上时效性短板。

## 值得关注的理由
- **解决 LLM 的核心短板**：训练数据滞后是所有 LLM 的天然缺陷，last30days 通过实时聚合 Reddit/X/YouTube/HN/Polymarket 等 10+ 平台，让 AI Agent 能回答「最近 30 天社区真实在讨论什么」
- **消费产品级的开发者工具**：渐进式源解锁（零配置 3 源 → 逐步解锁 10+ 源）+ 质量评分反馈环，将 SaaS 增长策略引入 AI 技能生态，是 Skill 设计的标杆
- **创业者视角的独特信号源**：集成 Polymarket 预测市场（真金白银的信号）、跨平台参与度评分、实体驱动钻取搜索，不只是搜索聚合而是信号质量工程

## 项目展示

![SwimMom 研究报告示例](https://raw.githubusercontent.com/mvanhorn/last30days-skill/main/assets/swimmom-mockup.jpeg)

研究输出效果展示——last30days 为用户生成带有来源引用和参与度评分的综合研究报告

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/mvanhorn/last30days-skill |
| Star / Fork | 18,664 / 1,503 |
| 代码行数 | 37,093 行（Python 58.3%, JavaScript 29.0%, TypeScript 3.8%） |
| 项目年龄 | 约 2.3 个月（2026-01-23 创建） |
| 开发阶段 | 密集开发（月均 115 次提交，v2.1 到 v2.9 仅用 17 天） |
| 贡献模式 | 单人主导（mvanhorn 85%，j-sperling 11.5%，共 8 人） |
| 热度定位 | 大众热门（2.5 个月 18.6K stars，社交媒体引爆式增长） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分（42 个测试文件）] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Matt Van Horn，硅谷连续创业者。曾联合创办 Zimride（后更名为 Lyft，美国第二大网约车平台，已 IPO）和 June Intelligent Oven（「自动驾驶烤箱」，被 Weber 收购）。GitHub 15.5 年历史，386 个公开仓库。Bio 写道「Building again, more soon. Vibe coding Last30Days research tool」，处于新创业探索期，last30days 是其「vibe coding」的实验作品。

### 问题判断
Van Horn 作为连续创业者，核心能力是判断「下一步该做什么」。这需要高质量的实时情报——不是搜索引擎的泛泛结果，而是社区实际在讨论、投票、下注的内容。LLM 的训练数据天然滞后数月，当你需要判断一个技术/产品的真实口碑时，Reddit 评论往往比官方博客更有价值。这个问题来自真实的创业决策场景。

时机精准：2026 年初 AI Agent 技能生态（OpenClaw/Claude Plugins）刚起步，需要高质量的原生技能来定义最佳实践。Van Horn 以创业者的速度（2.5 个月 269 次提交）抢占了「实时社区研究」这个关键生态位。

### 解法哲学
**渐进式解锁（Progressive Unlocking）**——整个项目最核心的设计哲学：

- **零配置即可用**：3 个免费数据源（Reddit 公开 JSON、Hacker News Algolia API、Polymarket Gamma API）不需要任何 API Key
- **Setup Wizard 引导升级**：安装向导自动提取浏览器 Cookie、一键安装 yt-dlp，消费产品级的 NUX 体验
- **质量反馈驱动**：`quality_nudge.py` 每次搜索后告诉用户「你只用了 3/5 核心源，缺 X 和 YouTube」，形成正向升级循环
- **明确不做什么**：不做持续监控 SaaS、不做通用搜索引擎、不做自有前端 UI——专注做 AI Agent 原生的研究技能

### 战略意图
last30days 正在从「单次搜索工具」向「持续情报系统」演进。`store.py` 实现了 SQLite 持久化层，`briefing.py` 实现了晨报生成，`watchlist.py` 支持话题追踪。这构成了完整的研究自动化闭环：关注 → 定期采集 → 累积 → 综合报告。同时支持 Claude Code Plugin、Gemini CLI Extension、Codex CLI 三种安装方式，覆盖所有主流 AI IDE 生态——这是平台级思维。

## 核心价值提炼

### 创新之处

1. **渐进式源解锁 + 质量评分反馈环**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   零配置 3 源即可用，每次运行后 `quality_nudge.py` 告知缺失源及获取方式。用消费产品增长策略（漏斗 + nudge）驱动开发者工具的功能激活。任何需要多 API Key 配置的开发者工具都可以借鉴。

2. **预测市场作为研究信号源**（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）
   将 Polymarket 赔率和交易量纳入研究信号，五因子加权评分（文本相关性 30%、24h 交易量 30%、流动性 15%、价格变动 15%、竞争性 10%）。「真金白银」的信号质量远高于社区讨论。

3. **两阶段补充搜索 + 实体驱动钻取**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   Phase 1 广泛搜索后，`entity_extract.py` 提取高频 @handle 和 r/subreddit，Phase 2 对这些实体做定向无关键词搜索——发现原始查询遗漏的内容。

4. **查询类型驱动的动态源优先级**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `query_type.py` 用纯正则将查询分为 7 类，每类有独立源分层（Tier 1/2/3）、WebSearch 惩罚系数、排序权重。「how_to」查询 YouTube 为 Tier 1，「prediction」查询 Polymarket 为 Tier 1。零 LLM 调用实现智能源选择。

5. **比较模式三路并行研究**（新颖度 3/5 | 实用性 5/5 | 可迁移性 3/5）
   查询「X vs Y」时自动运行三个并行流程——分别研究 X、Y、以及「X vs Y」直接比较——然后综合为对比报告。

### 可复用的模式与技巧

| 模式 | 描述 | 适用场景 |
|------|------|----------|
| 三层降级链 | ScrapeCreators → 公开 JSON → LLM 代理搜索，每层独立、自动降级、用户无感知 | 任何外部 API 集成的高可用设计 |
| Python 数据层 + SKILL.md 行为层 | Python 负责采集/评分/去重，SKILL.md 负责意图理解/综合叙事 | AI Skill 最佳实践架构 |
| 多维参与度评分 | Reddit: 0.50*score + 0.35*comments + 0.05*ratio + 0.10*top_comment_score | 任何需要排序社区内容的系统 |
| 子进程生命周期管理 | 全局 PID 注册 + atexit 清理 + SIGALRM 看门狗 | 多子进程并发的 Python 工具 |
| 零依赖 HTTP 客户端 | 纯 urllib.request + 手写重试，零 pip 依赖 | 受限环境运行的 Python 工具 |
| 浏览器 Cookie 自动提取 | 读取 Firefox/Chrome/Safari Cookie 数据库，替代 API Key | 需要平台认证的爬虫工具 |

### 关键设计决策

| 决策 | Trade-off |
|------|-----------|
| 纯 stdlib HTTP 客户端 | 牺牲 requests 的便利 API，换来零外部依赖的可移植性 |
| 三层 Reddit 降级链 | 代码复杂度增加（3 个模块），换来 100% 可用率 |
| 查询类型正则分类（非 LLM） | 可能误分类，但零延迟零成本 |
| 内嵌 Bird v0.8.0 做 X 搜索 | 引入 Node.js 依赖，换来免费无限次 X 搜索 |
| SKILL.md 881 行行为定义 | 维护成本高，换来 Agent 行为高度可预测 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | last30days | RivalSearchMCP | Perplexity Deep Research | social-media-research | Xpoz |
|------|-----------|---------------|------------------------|----------------------|------|
| 平台覆盖 | 10+ 源 | Web + Reddit + HN | 通用搜索 | Reddit + X | 多平台 |
| 参与度评分 | 多维加权 | 无 | 无 | 无 | 有 |
| 配置门槛 | 零配置 3 源 | 零配置 | 开箱即用（SaaS） | 需 API Key | 付费 |
| Agent 原生 | Claude/Gemini/Codex | Claude/Cursor | 非 Agent 原生 | Claude | N/A |
| 去重/验证 | 跨源交叉验证 | 无 | 无 | 无 | 有 |
| 价格 | 免费/MIT | 免费 | $20/月 | 免费 | 商业 |

### 差异化护城河
last30days 的核心壁垒是「多平台社区信号 + 参与度评分 + AI Agent 原生集成」三位一体。竞品要么缺平台覆盖度，要么缺评分体系，要么不是 Agent 原生的。渐进式解锁策略是增长引擎——用户一旦体验到 3 源的价值，自然会追加配置。

### 竞争风险
- 平台 API 变动是最大风险（Reddit 已经历过一次），但三层降级架构提供了充分缓冲
- Perplexity 若推出 Agent Skill 版本，在通用搜索维度上有优势
- 作者单人依赖，若不持续维护可能被后来者超越

### 生态定位
AI Agent 技能生态的**标杆项目**——不只是功能定位，其架构设计（Python 数据层 + SKILL.md 行为层、渐进式配置、质量评分反馈）定义了 AI Skill 开发的最佳实践。OpenClaw 质量评分 149/200，多个技能市场已收录。

## 套利机会分析
- **信息差**: 项目已充分曝光（18.6K stars），但其架构模式（渐进式解锁、降级链、查询类型分层）的可迁移价值尚未被其他 Skill 开发者充分借鉴
- **技术借鉴**: 「Python 数据层 + SKILL.md 行为层」分离模式可直接用于任何 AI Skill 开发；渐进式源解锁策略可用于需要多 API Key 的工具；多维参与度评分公式可用于任何社区内容排序场景
- **生态位**: 填补了「LLM 训练数据滞后」和「通用搜索缺乏社区信号」之间的空白，是 AI Agent 获取实时社区情报的最佳入口
- **趋势判断**: AI Agent 技能生态正处于爆发期，first-mover 在「实时研究」赛道有明确优势。但竞争将随生态成熟而加剧

## 风险与不足
- **单人依赖风险**：mvanhorn 贡献 85% 代码，最近提交 3 月 30 日后趋缓，持续维护存在不确定性
- **无 CI/CD**：42 个测试文件但没有自动化运行，依赖手动 `evaluate_search_quality.py` 评测
- **平台 API 脆弱性**：依赖 10+ 个外部平台，API 变动（如 Reddit 限流、X 封锁）是持续风险
- **浏览器 Cookie 依赖**：X 搜索依赖浏览器 Cookie 提取，格式变动或安全策略变化可能导致失效
- **SKILL.md 维护成本**：881 行的 Agent 行为定义，随功能扩展维护负担将持续增加
- **无静态类型检查**：有 type hints 但未配置 mypy/pyright，大型重构时缺乏保护

## 行动建议
- **如果你要用它**: 零配置即可体验（3 源），推荐先用 `last30days "你关心的话题"` 试跑一次。如果结果有价值，再按 Setup Wizard 解锁 Exa（免费 1,000 次/月）和 YouTube。对比 Perplexity，last30days 的优势在于社区参与度评分和跨源验证
- **如果你要学它**: 重点关注 `scripts/lib/query_type.py`（查询类型分层设计）→ `scripts/lib/score.py`（多维评分引擎）→ `scripts/lib/dedupe.py`（混合去重算法）→ `SKILL.md`（Agent 行为定义最佳实践）
- **如果你要 fork 它**: 最有价值的方向是 (1) 添加更多数据源（微信公众号、知乎、V2EX 等中文社区）(2) 增强持续监控能力（基于 watchlist + briefing 构建定时任务）(3) 添加 CI/CD 和静态类型检查

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/mvanhorn/last30days-skill](https://deepwiki.com/mvanhorn/last30days-skill) |
| Zread.ai | 未收录 |
| OpenClaw API 指南 | [openclawapi.org/en/blog/2026-03-25-last30days-skill](https://openclawapi.org/en/blog/2026-03-25-last30days-skill) |
| 关联论文 | 无 |
| 在线 Demo | 无（需安装到 Claude Code / Gemini CLI / Codex CLI） |
