# simstudioai/sim 网络分析报告

## 仓库基本数据
- Star / Fork / Watcher: 27,110 / 3,440 / 133
- 语言: TypeScript (71.1%), MDX (28.4%), CSS (0.1%), Python (0.1%), 其他 (<0.1%)
- License: Apache License 2.0
- 创建时间: 2025-01-05 | 最近推送: 2026-03-21
- 话题标签: agentic-workflow, agents, ai, nextjs, typescript, agent-workflow, aiagents, anthropic, artificial-intelligence, deepseek, gemini, low-code, no-code, openai, rag, react, automation, chatbot
- 已归档: 否 | 是Fork: 否

## 作者画像
- **组织**: simstudioai（Sim），2025-02-15 创建，533 followers
- **简介**: "Sim is the open-source platform to build, deploy, and orchestrate AI agents."
- **官网**: https://sim.ai
- **公开仓库**: 仅 1 个（sim），说明组织高度聚焦单一产品
- **融资**: 2025年11月完成 $7M Series A，由 Standard Capital 领投，Perplexity Fund、SV Angel、Y Combinator 跟投，天使投资人包括 Paul Graham、Paul Bucheit、Ali Rowghani、Kaz Nejatian
- **YC 背景**: Y Combinator 校友项目

### 核心贡献者
| 排名 | 用户 | 贡献数 | 备注 |
|------|------|--------|------|
| 1 | waleedlatif1 (Waleed) | 2,027 | 创始人/CEO，San Francisco，Sim公司 |
| 2 | emir-karabeg | 668 | 核心团队 |
| 3 | icecrasher321 | 608 | 核心团队 |
| 4 | Sg312 | 255 | 核心团队 |
| 5 | aadamgough | 99 | 活跃贡献者 |
| 6 | TheodoreSpeaks | 19 | 贡献者 |

- 总贡献者约 30 人，核心团队 4-5 人，绝大部分代码由创始团队完成
- 社区贡献者多为单次贡献（1 commit），外部贡献生态尚在早期

## 社区热度
### Star 增长趋势
- 仓库创建于 2025-01-05，至今约 14.5 个月积累 27,110 stars
- 平均月增长约 1,870 stars
- 最近 4 天 star 采样（2026-03-18 ~ 03-21）：18 + 22 + 37 + 23 = 100 stars / 4 天，日均约 25 stars
- 增长节奏稳健，未见断崖式波动

### 关键增长里程碑
- Series A（2025年11月）时已达 18,000 stars，60,000+ 开发者注册
- 截至当前（2026-03）27,110 stars，过去 ~4 个月增长 ~9,000 stars
- Fork 数 3,440（Fork/Star 比约 12.7%），说明有大量用户在尝试自部署或二次开发

### Issue / PR 活跃度
- 总 Issue: 104 | 总 PR: 115
- Issue 数量偏少，可能通过 Discord 等渠道处理用户反馈

## 生态网络
### 同 Topic 头部项目（agentic-workflow）
| 项目 | Star | 描述 |
|------|------|------|
| langgenius/dify | 133,852 | 生产级 agentic workflow 开发平台 |
| infiniflow/ragflow | 75,714 | RAG + Agent 引擎 |
| daytonaio/daytona | 68,888 | AI 生成代码安全运行基础设施 |
| FlowiseAI/Flowise | 50,948 | 可视化 AI Agent 构建 |
| bytedance/deer-flow | 32,417 | 开源 SuperAgent |
| **simstudioai/sim** | **27,110** | **AI Agent 构建与编排平台** |
| ruvnet/ruflo | 22,251 | Claude Agent 编排平台 |

Sim 在 agentic-workflow 生态中排名第 6，在专注"可视化 Agent 构建"细分方向上仅次于 Flowise。

### 技术栈生态
- **框架**: Next.js (App Router) + React 19 + Bun
- **数据库**: PostgreSQL 17 + pgvector + Drizzle ORM
- **认证**: Better Auth
- **UI**: Shadcn + Tailwind CSS
- **状态管理**: Zustand
- **流程编辑器**: ReactFlow
- **文档**: Fumadocs（MDX）
- **Monorepo**: Turborepo
- **实时**: Socket.io
- **后台任务**: Trigger.dev
- **远程代码执行**: E2B

## 官方文档洞察
### 官网 (sim.ai)
- **价值主张**: "The open-source platform to build AI agents and run your agentic workforce"
- **目标用户**: 开发者（60,000+）、专业团队、企业组织，兼顾技术与非技术用户
- **差异化叙事**: 以"Figma-like canvas"类比，强调可视化低代码构建 AI Agent 的民主化，定位于"复杂 SDK 与过度简化平台之间的桥梁"
- **设计哲学**: 暗色主题、视觉优先、低代码交互、实时协作（共享光标）

### 定价
| 方案 | 价格 | 额度 |
|------|------|------|
| Community | 免费 | 1,000 credits |
| Pro | $25/月 | 6,000 credits/月 |
| Max | $100/月 | 25,000 credits/月 |
| Enterprise | 定制 | 定制基础设施 |

### 文档站 (docs.sim.ai)
10 大模块，160+ 集成工具文档，覆盖触发器、Blocks、Tools、MCP、知识管理、表格、变量、执行与权限等，文档完善度较高。

### 集成能力
- **LLM 提供商**: OpenAI, Anthropic, Google Gemini, xAI, Mistral, Perplexity, DeepSeek, Ollama, vLLM
- **业务集成**: Slack, GitHub, Gmail, HubSpot, Salesforce, Notion, Google Drive/Sheets, Stripe, Jira, Linear, Airtable, Discord, Microsoft Teams, Outlook, Telegram 等
- **总计**: 1,000+ 集成，300+ 工具

## 竞品清单
| 竞品 | 类型 | Star | 差异化 |
|------|------|------|--------|
| **Dify** (langgenius/dify) | 开源 | 133.8k | 更成熟的 LLMOps 平台，侧重 prompt 工程和 RAG pipeline |
| **Flowise** (FlowiseAI/Flowise) | 开源 | 50.9k | 更轻量的可视化 LangChain 构建器，专注 chatbot |
| **n8n** | 开源（Fair Use） | ~60k+ | 传统自动化为主 + AI 增强，7000+ 应用连接器，AI Agent 能力较新 |
| **Zapier** | 商业 | - | 最广泛的应用连接（7000+），非开源，AI 功能为辅 |
| **Activepieces** | 开源 | ~10k+ | 开源无代码自动化，易用但 AI Agent 能力有限 |
| **Node-RED** | 开源 | ~22k | IoT 导向的流式编辑器，生态成熟但非 AI-native |
| **Coze Studio** (字节) | 商业 | - | 字节跳动旗下 AI Bot 构建平台，中国市场为主 |

**Sim 的竞争定位**: 在"开源 + AI-native + 可视化 + 生产级"交叉领域独特定位。相比 Dify 更强调可视化 canvas 体验；相比 n8n/Zapier 更 AI-native；相比 Flowise 更面向生产级全栈 Agent 编排。

## 关键 Issue 信号
### 高讨论度 PR（已合并）
| # | 标题 | 评论数 | 信号 |
|---|------|--------|------|
| #3433 | feat(selectors): add dropdown selectors for 14 integrations | 31 | 集成扩展是核心方向 |
| #3464 | feat(mothership): billing | 28 | 商业化计费系统建设中 |
| #3558 | feat(sim-mailer): email inbox with chat history and plan gating | 26 | 构建通信功能 + 套餐分层 |
| #3230 | feat(knowledge): connectors, user exclusions, expanded tools | 21 | 知识库能力持续增强 |
| #3475 | feat(files): inline file viewer with text editing | 19 | 文件管理能力扩展 |

### 活跃 PR（进行中）
| # | 标题 | 评论数 | 信号 |
|---|------|--------|------|
| #3426 | feat(blocks): add execute command block for self-hosted | 19 | 自托管能力增强 |
| #3563 | feat(meta-ads): add meta ads integration | 14 | 广告平台集成 |
| #3605 | feat(concurrency): bullmq based concurrency control | 10 | 生产级并发控制 |
| #3030 | improvement(workflow): remove useEffect anti-patterns | 6 | 代码质量优化 |

**信号总结**: 当前开发重心在——商业化（billing/plan gating）、集成扩展（Meta Ads、MCP）、基础设施成熟度（并发控制、命令执行）、以及用户体验（product tour、UI polish）。

## 知识入口
| 平台 | URL | 状态 |
|------|-----|------|
| DeepWiki | https://deepwiki.com/simstudioai/sim | 可用，内容丰富，含系统架构图、Monorepo 结构、数据库 schema、安全模型等 |
| Zread.ai | https://zread.ai/simstudioai/sim | 可用，33 页文档，涵盖 Get Started、Deep Dive（执行引擎、Blocks、数据库、实时、AI 集成、企业特性） |
| 官方文档 | https://docs.sim.ai | 可用，10 大模块，160+ 集成文档 |
| Discord | https://discord.gg/Hr4UWYEcTT | 社区渠道 |
| Twitter/X | https://x.com/simdotai | 官方社交账号 |

## 项目展示素材
| 序号 | 类型 | URL | 描述 |
|------|------|-----|------|
| 1 | GIF | https://raw.githubusercontent.com/simstudioai/sim/main/apps/sim/public/static/workflow.gif | Workflow Builder 可视化构建演示 |
| 2 | GIF | https://raw.githubusercontent.com/simstudioai/sim/main/apps/sim/public/static/copilot.gif | Copilot AI 辅助生成节点演示 |
| 3 | GIF | https://raw.githubusercontent.com/simstudioai/sim/main/apps/sim/public/static/knowledge.gif | 知识库文档上传与向量检索演示 |

## 快速判断
- **项目阶段**: 成长期（Series A 已完成，产品已上线，商业化进行中）
- **增长质量**: 优秀——14.5 个月 27k stars，YC 背书 + 顶级天使投资人，日均仍保持 ~25 stars 稳定增长
- **团队实力**: 精干核心团队（4-5人），创始人 Waleed 位于 San Francisco，YC 校友
- **技术成熟度**: 中高——现代技术栈（Next.js + Bun + PostgreSQL + ReactFlow），Monorepo 架构，正在补齐生产级能力（并发控制、企业特性）
- **社区健康度**: 中等偏早期——外部贡献者多为单次贡献，社区主要在 Discord 而非 GitHub Issues
- **商业前景**: 明确——已有定价体系（Free/Pro/Max/Enterprise），正在构建 billing 系统，100+ 企业在生产环境使用
- **风险信号**: Fork/Star 比偏高（12.7%），需关注是否存在刷星或 fork-and-abandon 现象；核心代码高度集中于创始团队，bus factor 偏低
- **值得关注**: 在"开源 AI Agent 可视化编排"赛道中增速最快的新玩家之一，YC + Paul Graham 等顶级背书，Apache 2.0 许可证友好
