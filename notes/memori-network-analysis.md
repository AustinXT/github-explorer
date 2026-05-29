# Memori 网络分析报告

> 仓库: [GibsonAI/Memori](https://github.com/GibsonAI/Memori) (实际重定向至 MemoriLabs/Memori)
> 分析时间: 2026-03-22

## 仓库基本数据

- **Star / Fork / Watcher**: 12,422 / 1,114 / 54
- **语言**: Python (85.2%), TypeScript (9.5%), Jupyter Notebook (4.8%), Makefile (0.3%), JavaScript (0.2%), Dockerfile (0.1%)
- **License**: Apache 2.0
- **创建时间**: 2025-07-24 | **最近推送**: 2026-03-20
- **话题标签**: agent, ai, long-short-term-memory, memory, python, rag, aiagent, chatgpt, state-management, memori-ai, memory-management, llm, awesome, agent-memory, ai-memory, memory-mcp, openclaw-memory
- **已归档**: 否 | **是 Fork**: 否
- **主页**: https://memorilabs.ai
- **磁盘占用**: ~28 MB
- **默认分支**: main
- **Open Issues**: 15 | **Open PRs**: 4
- **项目存活时长**: 约 8 个月（2025年7月至今），持续活跃开发

## 作者画像

- **ID**: GibsonAI (现为 MemoriLabs) | **名称**: Memori Labs
- **简介**: "The memory fabric for enterprise AI"
- **位置**: Los Angeles, CA | **公司**: 无（独立公司）
- **博客**: https://memorilabs.ai/
- **粉丝**: 127 | **公开仓库**: 2 | **账号年龄**: ~2.2 年（2024-01-29 创建）
- **此 repo 投入权重**: **高** — 组织仅有 2 个公开仓库，另外 2 个是 fork 的 crewAI 相关项目，Memori 是唯一核心产品
- **作者类型**: **创业公司/开源组织** — MemoriLabs 是专注 AI 记忆层的创业公司，已有商业产品 Memori Cloud
- **贡献集中度**: **小团队主导** — 核心贡献者 5 人：
  - harshalmore31 (175 commits) — 主力开发者
  - Boburmirzo (105 commits) — Microsoft 开发者布道师，可能是 DevRel 合作
  - devwdave (38 commits) — Dave Heritage, Memori Labs 员工，负责社区响应
  - mcmontero (27 commits) — Michael Montero, Struck Studio 创始人 & Montero Ventures，可能是联合创始人/投资人
  - rpkruse (24 commits) — Ryan Kruse, 协作者身份回复 Issues
  - 其余贡献者均为 1-13 次提交的社区成员
- **背景推断**: 团队具有企业 AI 和数据库背景，GibsonAI 最初可能是一家数据库公司（仓库中有 GibsonAI 数据库集成），后转型/扩展为 AI 记忆层产品公司。有 Microsoft DevRel 人员深度参与，说明已建立一定的行业关系网络。

## 社区热度

- **热度级别**: **大众热门** — 12,422 Star，已进入万星俱乐部
- **增长模式**: **爆发型 + 持续增长**
  - 2025-07-25 首个 Star → 2025-08-19 达到 ~3,000 Star（首月爆发）
  - 2025-11-13 ~ 2025-11-23 达到 ~6,000 Star（中期稳定增长）
  - 2025-12-03 ~ 2025-12-04 达到 ~9,000 Star
  - 2026-02-05 ~ 2026-02-16 达到 ~12,000 Star
  - 2026-03-21 仍有新增 Star（最近 24 小时内有新增）
- **近期趋势**: 最近一周（2026-03-13 至 2026-03-21）仍有持续新增 Star，增长未停滞。项目从 2025 年 7 月创建至今 8 个月增至 12K+ Star，平均每月 ~1,500 Star。
- **套利判断**: 非低估项目，Star 数量与项目质量基本匹配。作为企业级 AI 记忆层产品，已建立品牌认知。但 Fork 数 (1,114) 与 Star 数比例偏高（~9%），有部分「刷星」嫌疑或 Fork 后即放弃的情况。Watcher 数仅 54，与 12K Star 不成比例，进一步暗示部分 Star 可能来自短期热度而非深度关注。

## 生态网络

- **上游依赖**: OpenAI API、Anthropic API、Google Gemini、AWS Bedrock、DeepSeek、Grok (xAI) 等 LLM 提供商；PostgreSQL、MySQL、SQLite、MongoDB 等数据库；LangChain、Pydantic AI、Agno 等框架；OpenClaw 网关
- **同类项目**:
  - [mem0ai/mem0](https://github.com/mem0ai/mem0) — 50,613 Star, "Universal memory layer for AI Agents"，最大竞品
  - [letta-ai/letta](https://github.com/letta-ai/letta) — 21,686 Star, "Platform for building stateful agents with persistent memory"
  - [topoteretes/cognee](https://github.com/topoteretes/cognee) — 14,442 Star, "Knowledge Engine for AI Agent Memory"
  - [MemTensor/MemOS](https://github.com/MemTensor/MemOS) — AI memory OS for LLM and Agent systems

## 官方文档洞察

- **官方主页**: https://memorilabs.ai — 功能完整的企业官网，含产品介绍、文档、博客
- **价值主张**: "The memory fabric for enterprise AI" — 为企业 AI 提供记忆基础设施，帮助 AI 应用"保持上下文活跃"，降低 LLM 成本最高达 98%
- **目标用户**: 部署 AI Agent 的企业组织、构建生产级 AI 应用的开发者、客服系统团队、需要上下文 AI 交互的电商平台
- **差异化叙事**:
  1. **SQL 原生** — 不依赖向量数据库，使用关系型数据库作为记忆存储，降低运维复杂度
  2. **自动分类** — 对话自动被分类为事实、偏好、规则和摘要
  3. **可解释性** — 每个返回结果包含溯源信息，可追溯到实体、时间和来源
  4. **零延迟增强** — 通过异步后台处理实现记忆增强，不影响请求延迟
- **设计哲学**: 生产级可靠性 + 最小接入摩擦（"一行代码"集成）+ 企业级安全（PCI/SOC 2）+ 数据主权
- **技术路线**: 双 SDK（Python + TypeScript）、MCP 协议支持、OpenClaw 插件、Memori Cloud 托管服务 + BYODB 自托管选项
- **基准测试**: LoCoMo 基准 81.95% 准确率，仅使用 4.97% 的 full-context tokens，优于 Zep、LangMem、Mem0

## 竞品清单

| 项目 | Star | 定位 | 语言 | 差异化 |
|------|------|------|------|--------|
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 50.6K | 通用 AI Agent 记忆层 | Python | 向量数据库驱动，生态最大，有 Chrome 扩展和 MCP server |
| [letta-ai/letta](https://github.com/letta-ai/letta) | 21.7K | 有状态 Agent 构建平台 | Python | 包含记忆但定位更广，是完整 Agent 平台 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 14.4K | AI Agent 知识引擎 | Python | 知识图谱驱动，6 行代码接入 |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 新项目 | AI 记忆操作系统 | Python | 强调跨任务技能复用和记忆进化 |
| Zep (zep-ai) | — | 时序化记忆管理 | Python | 强调时序和情节记忆，结构化交互序列 |

**竞品格局分析**: Memori 处于快速增长期，已是第三大 AI 记忆开源项目。其核心差异化在于 SQL 原生架构和企业级定位，但 mem0 (50K+ Star) 的先发优势和生态宽度显著领先。

## 关键 Issue 信号

| # | 标题 | 评论 | 状态 | 信号 |
|---|------|------|------|------|
| [#61](https://github.com/MemoriLabs/Memori/pull/61) | feat: Add automated workflows for dependency updates, documentation | 27 | Closed | 社区贡献活跃 |
| [#101](https://github.com/MemoriLabs/Memori/pull/101) | fixed performance and bugs | 22 | Closed | 性能优化阶段 |
| [#147](https://github.com/MemoriLabs/Memori/pull/147) | cleanup! | 18 | Closed | 代码清理重构 |
| [#137](https://github.com/MemoriLabs/Memori/pull/137) | feat: multi-user and multi-assistant support | 16 | Closed | 企业多租户能力 |
| [#368](https://github.com/MemoriLabs/Memori/issues/368) | Cloud API endpoints return 401 Unauthorized | 1 | Open | Cloud 产品稳定性 |
| [#366](https://github.com/MemoriLabs/Memori/issues/366) | Allow Batch/On-Demand Memory Extraction | 0 | Open | 功能需求 |
| [#362](https://github.com/MemoriLabs/Memori/issues/362) | Empty string query crashes with SQL error | 1 | Open | 安全性/健壮性 |
| [#303](https://github.com/MemoriLabs/Memori/issues/303) | How to delete user memories? | 1 | Open | 基础功能缺失 |
| [#287](https://github.com/MemoriLabs/Memori/issues/287) | Official Memori MCP server | 0 | Open | MCP 生态对接 |
| [#250](https://github.com/MemoriLabs/Memori/issues/250) | Support Local/Custom OpenAI-Compatible Endpoints | 0 | Open | 本地部署需求 |

**Issue 信号解读**: 团队响应及时（协作者在数天内回复），但部分基础功能（删除记忆、本地 LLM 支持）尚未实现。Cloud 产品存在稳定性问题（401 错误）。社区有真实使用反馈，非纯 Star 空壳。

## 知识入口

- **DeepWiki**: [https://deepwiki.com/GibsonAI/Memori](https://deepwiki.com/GibsonAI/Memori) — 已收录，包含完整架构文档
- **Zread.ai**: [https://zread.ai/GibsonAI/Memori](https://zread.ai/GibsonAI/Memori) — 已收录，包含项目概览和文档
- **关联论文**: 未在 arXiv 发现关联论文；项目自有基准测试白皮书（LoCoMo benchmark）
- **在线 Playground**: [https://memorilabs.ai/playground](https://memorilabs.ai/playground) — 官方交互式 Playground，可体验记忆创建、查询和知识图谱可视化
- **官方文档**: [https://memorilabs.ai/docs/memori-cloud/](https://memorilabs.ai/docs/memori-cloud/) (Cloud) | [https://memorilabs.ai/docs/memori-byodb/](https://memorilabs.ai/docs/memori-byodb/) (BYODB)
- **Discord**: [https://discord.gg/abD4eGym6v](https://discord.gg/abD4eGym6v)
- **外部分析**: [MarkTechPost 报道](https://www.marktechpost.com/2025/09/08/gibsonai-releases-memori-an-open-source-sql-native-memory-engine-for-ai-agents/) | [Bright Coding 分析](https://www.blog.brightcoding.dev/2025/09/05/memori-the-open-source-memory-engine-turning-llms-into-context-aware-human-like-agents/)

## 项目展示素材

1. **Banner 图**: https://s3.us-east-1.amazonaws.com/images.memorilabs.ai/banner.png — 项目 Banner，展示品牌标识
2. **LoCoMo 基准测试结果图**: https://s3.us-east-1.amazonaws.com/images.memorilabs.ai/docs/memori-locomo-benchmark.webp — 展示 Memori 在 LoCoMo 基准中的准确率和标准差对比

## 快速判断

- **是否值得深入**: **是** — 万星项目，活跃开发（最近 2 天有 push），企业级定位明确，有真实商业产品（Memori Cloud），AI Agent 记忆层是当前 AI 基础设施热门赛道
- **初步定位**: LLM/AI Agent 的 SQL 原生持久化记忆层，强调企业级场景（多租户、可解释性、数据主权）。对标 mem0 但以 SQL 原生架构和企业合规为差异化卖点
- **作者可信度**: **中高** — 创业公司专注单一产品，有商业网站和 Cloud 服务，团队成员具有企业背景（含 Microsoft DevRel 合作），但公司历史较短（~2 年），核心团队规模较小（5 人）
- **竞品格局**: **细分市场** — AI 记忆层整体是红海（mem0 50K Star 领先，letta 21K，cognee 14K），但 Memori 在 SQL 原生 + 企业合规这一细分领域有差异化定位。市场仍在快速发展，尚未形成赢家通吃格局
