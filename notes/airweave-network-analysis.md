# airweave-ai/airweave 网络分析报告

> 分析日期：2026-03-22 | 数据来源：GitHub API、Web 搜索

## 仓库基本数据

| 指标 | 数据 |
|------|------|
| Star / Fork / Watcher | 6,046 / 733 / 35 |
| 主要语言 | Python（10.7M 字节）, TypeScript（2.3M 字节）, MDX（562K 字节） |
| License | MIT License |
| 创建时间 | 2024-12-24 |
| 最近推送 | 2026-03-21 |
| 磁盘占用 | 330 MB |
| 已归档 | 否 |
| 是Fork | 否 |
| 主页 | https://airweave.ai |
| Issue 总数 | 42 |
| PR 总数 | 59 |
| 默认分支 | main |
| 当前版本 | v0.9.42（2026-03-21 发布） |
| 话题标签 | llm, rag, search, agent-infrastructure, ai, ai-agents, ai-infrastructure, api, context-retrieval, data-connectors, developer-tools, enterprise-data, information-retrieval, integration, open-source, retrieval, retrieval-augmented-generation, sdk, search-api, semantic-search |

**定位**: 面向 AI Agent 和 RAG 系统的开源上下文检索层（Context Retrieval Layer）。连接 50+ 应用、工具和数据库，持续同步数据并通过统一的 LLM 友好搜索接口暴露，使 AI Agent 能在单次请求中从多个数据源检索相关、可靠、最新的上下文信息。

## 作者画像

### 组织信息
- **组织**: airweave-ai（Airweave），2024-12-24 创建
- **简介**: "Context retrieval layer for AI"
- **官网**: https://airweave.ai
- **公开仓库**: 11 个（主仓库 + SDK + 示例 Agent + 插件）
- **GitHub 关注者**: 116 followers
- **融资**: 2025年7月完成 $6M Seed 轮，由 FCVC 领投，LUX Capital、Y Combinator、Orange Collective、Pioneer Fund 跟投，Elasticsearch 创始人 Shay Banon 等天使参与
- **YC 背景**: Y Combinator 校友项目
- **创始人**: Lennert Jansen 和 Rauf Akdemir（CTO）

### 核心贡献者

| 排名 | 用户 | 贡献数 | 身份/背景 |
|------|------|--------|-----------|
| 1 | orhanrauf (Rauf Akdemir) | 1,539 | 联合创始人/CTO，旧金山，"i love cooking food and code" |
| 2 | marc-rutzou (Marc Rutzou) | 1,038 | 核心团队，阿姆斯特丹，2025-04加入 GitHub |
| 3 | felixschmetz (Felix) | 889 | 核心团队，阿姆斯特丹，背景 Uber + ETH Zurich |
| 4 | lennertjansen | 261 | 联合创始人 |
| 5 | EwanTauran | 229 | 核心团队 |
| 6 | hiddeco | 118 | 活跃贡献者（安全/认证方向） |
| 7 | danielsteman | 105 | 贡献者 |
| 8 | BRama10 | 69 | 贡献者 |

- 总贡献者约 30 人，核心团队 5-6 人
- 近期（2026-03）提交主要由 felixschmetz 主导（大规模重构），orhanrauf 和 hiddeco 参与安全加固
- 团队分布在旧金山和阿姆斯特丹两地

## 社区热度

### Star 增长趋势（月度分布）

| 月份 | 新增 Star | 累计 | 备注 |
|------|-----------|------|------|
| 2024-12 | 15 | 15 | 项目创建月 |
| 2025-01 | 86 | 101 | 早期增长 |
| 2025-02 | 172 | 273 | 稳步增长 |
| 2025-03 | 264 | 537 | 加速增长 |
| 2025-04 | 130 | 667 | 增速回落 |
| 2025-05 | **1,775** | 2,442 | **爆发式增长**（可能上了 Trending/HN） |
| 2025-06 | 203 | 2,645 | 回归常态 |
| 2025-07 | 123 | 2,768 | 正常增长（融资公告月） |
| 2025-08 | 50 | 2,818 | 低谷 |
| 2025-09 | 129 | 2,947 | 恢复 |
| 2025-10 | **1,291** | 4,238 | **第二波爆发** |
| 2025-11 | 993 | 5,231 | 持续高热度 |
| 2025-12 | 225 | 5,456 | 降温 |
| 2026-01 | 101 | 5,557 | 节后低谷 |
| 2026-02 | 214 | 5,771 | 恢复 |
| 2026-03 | 275 | 6,046 | 当前月（进行中） |

**增长模式分析**：
- 有两次明显的爆发期：2025-05（+1,775）和 2025-10/11（+2,284），贡献了总 star 的 67%
- 2025年5月的爆发可能与 GitHub Trending 或 Hacker News 曝光相关
- 2025年10-11月的第二波爆发可能与产品发布、融资宣传或 MCP 生态热度相关
- 非爆发期月均增长约 100-250，说明项目有稳定的自然增长基底

### SDK 使用量
- **PyPI（airweave-sdk）**: 最近月下载 11,633 次，最近周 2,303 次，日均约 459 次
- **npm（@airweave/sdk）**: 最近月下载 15,234 次

### 社区渠道
- **Discord**: https://discord.gg/gDuebsWGkn（Server ID: 1323415085011701870）
- **Twitter/X**: [@airweave_ai](https://x.com/airweave_ai)
- **文档**: https://docs.airweave.ai

## 生态网络

### 组织内相关项目

| 仓库 | Star | 描述 |
|------|------|------|
| airweave-ai/airweave | 6,046 | 核心平台 |
| airweave-ai/error-monitoring-agent | 303 | 基于 Airweave 的智能错误监控 Agent |
| airweave-ai/cli | 34 | 命令行工具 |
| airweave-ai/python-sdk | 10 | Python SDK |
| airweave-ai/slack-knowledge-assistant | 10 | Slack 知识助手示例 |
| airweave-ai/typescript-sdk | 4 | TypeScript SDK |
| airweave-ai/claude-plugin | 2 | Claude Code/Cowork 插件 |
| airweave-ai/sales-context-agent | 2 | 销售上下文 Agent 示例 |
| airweave-ai/vercel-ai-sdk | 1 | Vercel AI SDK 集成 |
| airweave-ai/cursor-plugin | 0 | Cursor 插件 |
| airweave-ai/discord-bot | 1 | Discord 机器人 |

### 框架集成
- **LlamaIndex**: 已作为官方 Tool 集成（[Airweave - LlamaIndex](https://developers.llamaindex.ai/python/framework-api-reference/tools/airweave/)）
- **MCP**: 支持 MCP 协议，可被 Claude Desktop、Cursor、VS Code、OpenAI 等直接查询
- **Vercel AI SDK**: 官方集成
- **Harbor**: 作为 Satellite 组件集成（[Harbor Wiki](https://github.com/av/harbor/wiki/2.3.48-Satellite-Airweave)）

### 技术栈依赖
- **前端**: React/TypeScript + ShadCN UI
- **后端**: FastAPI（Python）
- **数据库**: PostgreSQL（元数据）+ Vespa（向量搜索）
- **编排**: Temporal（工作流）+ Redis（消息/缓存）
- **部署**: Docker Compose（开发）/ Kubernetes（生产）
- **支持的 LLM**: OpenAI、Anthropic、Groq、Cohere、Cerebras、Together 等

## 竞品识别

| 竞品 | 定位 | 差异点 |
|------|------|--------|
| **Unstructured** | 非结构化数据 ETL 管道 | 专注文档解析和格式转换，不提供搜索接口 |
| **LlamaIndex** | LLM 数据框架 | 全栈 RAG 框架，但需开发者自行组装管道；Airweave 已集成为其 Tool |
| **LangChain** | LLM 应用开发框架 | 更通用的 Agent 框架，不专注数据同步和搜索基础设施 |
| **Airbyte** | 数据集成/ETL | 通用 ELT 工具，不针对 AI/LLM 场景优化 |
| **Nango** | API 集成平台 | 专注 OAuth/API 集成，不提供向量化和搜索能力 |
| **Composio** | AI Agent 工具集成 | 专注 Agent 的 Action 执行，Airweave 专注 Context Retrieval |
| **Pathway** | 实时 AI 数据管道 | 侧重流处理和实时 RAG，Airweave 侧重多源同步搜索 |

**Airweave 差异化**：
- 定位为"共享检索基础设施"（Shared Retrieval Infrastructure），强调作为 AI 系统和数据源之间的中间层
- 同时提供认证、同步、索引、搜索全链路能力，开箱即用
- 支持 MCP 协议，可直接被 AI 助手查询
- 云托管版本（app.airweave.ai）降低使用门槛

## 关键 Issue 和 PR

### 近期活跃 PR（开放中）

| 编号 | 标题 | 方向 |
|------|------|------|
| #1658 | RBAC gating for API keys and auth | 安全/权限 |
| #1627 | Gemini Embedding 2 multimodal（PDF/图片/音视频） | 多模态嵌入 |
| #1619 | Structural Context Extraction Workflow | 上下文提取 |
| #1595 | Source rate limit config management | 速率限制 |
| #1580 | GitHub connector OAuth | 新连接器 |
| #1544 | Browse tree node selection with targeted sync | 精细化同步 |
| #1509 | Agentic search conversation style | Agent 搜索 |
| #1173 | Calendly connector | 新连接器 |
| #1136 | Neo4j Graph Database Connector | 图数据库 |

### 近期发布版本（v0.9.38-v0.9.42）

密集发布（2026-03-21 当天发布 5 个版本），主要集中在：
- 安全加固（CASA 系列：默认账户移除、API 凭证迁移至 header、constant-time 比较、redirect session 加固）
- 架构重构（Source 合约 v2 DI、Sync Pipeline 协议化、Converter 领域化）
- 三层搜索（instant/classic/agentic）
- OAuth 流程优化

**开发节奏极快**，表明项目处于活跃迭代期，正在进行安全审计+架构升级。

## 知识入口

| 平台 | 链接 | 说明 |
|------|------|------|
| DeepWiki | https://deepwiki.com/airweave-ai/airweave | AI 生成的项目知识库 |
| Zread | https://zread.ai/airweave-ai/airweave | 仓库阅读器 |
| 官方文档 | https://docs.airweave.ai | 完整的产品文档 |
| MCP 注册 | https://mcp.aibase.com/server/1639703157334614736 | MCP 服务器登记 |
| YC 页面 | https://www.ycombinator.com/companies/airweave | Y Combinator 公司页 |
| 云平台 | https://app.airweave.ai | 托管版本 |

## 项目展示素材

### README 亮点
- 有高质量 Logo（支持暗/亮模式切换）
- 嵌入演示视频（GitHub 托管）
- 清晰的架构说明（What → Where → How 三步解释）
- 集成图标矩阵（36+ 应用 SVG 图标展示）
- 快速开始只需 3 行命令（`git clone` + `cd` + `./start.sh`）
- CI 徽章完整（Code Quality、ESLint、System Tests、PyPI Downloads、Discord）
- 提供 "Set Up with Cursor" 按钮

### 视觉资产
- Logo SVG（暗色/亮色版本）
- 36+ 集成应用 SVG 图标
- 演示视频
- 官网 https://airweave.ai 提供 Academy 教程入口

## 综合评估

| 维度 | 评分 | 说明 |
|------|------|------|
| 项目成熟度 | ★★★☆☆ | v0.9.x 尚未到 1.0，但功能已相当完整，有云托管版 |
| 社区规模 | ★★★☆☆ | 6K+ star，但核心贡献者仍以团队为主，社区贡献较少 |
| 增长势头 | ★★★★☆ | 月均增长稳定，有过两次爆发，SDK 下载量可观 |
| 技术深度 | ★★★★☆ | 全栈平台，50+ 集成器，多种搜索模式，MCP 支持 |
| 商业前景 | ★★★★☆ | YC 背书 + $6M 融资 + 云托管版，商业化路径清晰 |
| 生态整合 | ★★★★☆ | LlamaIndex、MCP、Vercel AI SDK 多方集成 |
| 开发活跃度 | ★★★★★ | 极高频提交和发布，日均多次合并，正在进行架构大重构 |
| 文档质量 | ★★★★☆ | 独立文档站 + Academy + SDK 文档，较为完善 |

**总结**：Airweave 是一个由 YC 背书、获得 $6M 种子轮融资的开源 AI 上下文检索平台。项目定位精准（Agent 的共享检索基础设施），技术栈完整，集成生态丰富。目前处于高速迭代期（v0.9.x → 1.0），团队正在进行安全审计和架构升级。主要风险是社区外部贡献较少（核心开发高度集中于团队内部）、Star 增长有明显的脉冲式特征（需关注自然增长可持续性）。在 AI Agent 基础设施赛道中，其"统一检索层"的差异化定位使其与 LlamaIndex/LangChain 等框架形成互补而非直接竞争。
