# supermemoryai/supermemory 网络分析报告

## 仓库基本数据

| 指标 | 值 |
|---|---|
| 全名 | supermemoryai/supermemory |
| 描述 | Memory engine and app that is extremely fast, scalable. The Memory API for the AI era. |
| URL | https://github.com/supermemoryai/supermemory |
| 主页 | https://supermemory.ai/docs |
| Stars | 17,050 |
| Forks | 1,694 |
| Watchers | 70 |
| Open Issues | 3 |
| Pull Requests 总数 | 11 |
| 许可证 | MIT |
| 主语言 | TypeScript |
| 其他语言 | Python, MDX, JavaScript, CSS, HTML |
| 创建时间 | 2024-02-27 |
| 最后推送 | 2026-03-21 |
| 最后更新 | 2026-03-21 |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 磁盘占用 | ~163 MB |
| 默认分支 | main |
| Topics | cloudflare-pages, cloudflare-workers, drizzle-orm, tailwindcss, typescript, cloudflare-kv, postgres, remix, vite, agent-memory, ai-memory, memory |

## 作者画像

### 组织信息
| 指标 | 值 |
|---|---|
| 账号 | supermemoryai (组织) |
| 简介 | Give infinite context to your LLMs. |
| 网站 | https://supermemory.com |
| 地区 | United States of America |
| 公开仓库 | 23 |
| 关注者 | 816 |
| 创建时间 | 2024-06-06 |

### 核心创始人
- **Dhravya Shah** (@Dhravya) — 20 岁，2x 收购经历，783 次提交（占绝对主导），3,439 followers，坐标旧金山。TechCrunch 报道过的 19 岁（当时）AI 创业者。

### 组织旗下活跃仓库（按最近推送排序）
| 仓库 | Stars | 语言 | 说明 |
|---|---|---|---|
| supermemory | 17,050 | TypeScript | 核心产品 — 记忆引擎 |
| python-sdk | 0 | Python | Python SDK |
| sdk-ts | 16 | TypeScript | TypeScript SDK |
| skills | 1 | — | Agent Skills 仓库 |
| openclaw-supermemory | 614 | TypeScript | OpenClaw 插件 |
| memorybench | 203 | TypeScript | 记忆系统基准测试框架 |
| claude-supermemory | 2,329 | JavaScript | Claude Code 插件 |
| opencode-supermemory | 834 | TypeScript | OpenCode 插件 |
| cursor-supermemory | 13 | TypeScript | Cursor 插件 |
| code-chunk | 165 | TypeScript | 代码分块工具 |

### 主要贡献者（前 10）
| 贡献者 | 提交数 |
|---|---|
| Dhravya | 783 |
| MaheshtheDev | 200 |
| yxshv | 112 |
| CodeTorso | 104 |
| Kinfe123 | 43 |
| aryasaatvik | 27 |
| nexxeln | 22 |
| Prasanna721 | 21 |
| CodeWithShreyans | 20 |
| ThakerKush | 15 |

> 项目由创始人 Dhravya 主导驱动，贡献高度集中（占总提交的 ~55%），其余为早期社区贡献者。近期 PR 显示有新的外部贡献者（如 ishaanxgupta、ved015）参与。

## 社区热度

### Star 增长轨迹
| 时间节点 | 大致 Star 数 | 说明 |
|---|---|---|
| 2024-04-15 | ~1 - 30 | 首批 star，项目刚启动约 2 个月 |
| 2024-08-15 | ~5,000 | 4 个月内达到 5K，增速快 |
| 2025-07 | ~10,000 | 约 1 年后突破 10K |
| 2026-01-26 | ~15,000 | 持续稳定增长 |
| 2026-03-14 | ~17,000 | 最近仍在活跃增长中 |
| 2026-03-22（今天）| 17,050 | 当前值 |

### 增长特征
- **爆发期**：2024 年 4-8 月快速冲至 5K，伴随 HN/社交媒体传播。
- **稳健增长期**：2024-08 至 2026-03 持续线性增长，约 ~500-700 stars/月。
- **无衰退迹象**：2026 年 3 月仍有每日新增 star 活动。

### 开发活跃度
- 最近 10 次提交全部在 2026-03-14 ~ 2026-03-21 之间，涵盖 feat/fix/docs/perf 各类。
- 目前有 ~10 个 open PR，多为外部社区贡献的 SDK 集成（voltagent、Cartesia、ADK）。

## 生态网络

### 技术栈依赖
- **运行时/部署**：Cloudflare Workers / Pages
- **前端**：Remix + Vite + TailwindCSS
- **数据库**：PostgreSQL + Drizzle ORM + Cloudflare KV
- **包管理**：Bun + Turborepo（monorepo）
- **向量搜索**：自研向量图引擎（ontology-aware edges）

### 官方集成生态
| 集成方向 | 平台 |
|---|---|
| AI 框架 | Vercel AI SDK, LangChain, LangGraph, OpenAI Agents SDK, Mastra, Agno, CrewAI |
| AI 客户端 | Claude Desktop, Cursor, Windsurf, VS Code, Claude Code, OpenCode, OpenClaw |
| 数据连接器 | Google Drive, Gmail, Notion, OneDrive, GitHub, Web Crawler |
| MCP 协议 | 支持 MCP 标准协议，可直接接入任何 MCP 客户端 |
| SDK | TypeScript (npm), Python (PyPI) |

### 被引用/集成状态
- Vercel AI SDK 社区 Provider 列表收录 supermemory
- n8n 工作流集成支持
- 多个第三方 Medium/DEV 文章引用为 AI 记忆方案

## 官方文档洞察

### 文档入口
- 主文档站：https://supermemory.ai/docs
- 快速开始：https://supermemory.ai/docs/quickstart
- API 参考：完整 REST API + SDK 参考
- 概念解释：Memory vs RAG 专文、架构设计博客

### 核心概念
1. **Memory ≠ RAG**：Memory 追踪用户事实随时间的变化（覆盖、矛盾解决、自动遗忘），RAG 是无状态文档检索。Supermemory 同时运行两者。
2. **用户画像（User Profiles）**：自动维护的 static（长期事实）+ dynamic（近期上下文）双层画像，单次调用 ~50ms。
3. **Container Tags**：多租户隔离方案，按用户/项目/客户分隔记忆空间。
4. **自动遗忘**：临时信息（如"明天有考试"）过期后自动清除，矛盾自动解决。

### 定价
| 层级 | 价格 | Token/月 | 查询/月 | 存储 |
|---|---|---|---|---|
| Free | $0 | 1M | 10K | 无限 |
| Pro | $19/月 | 3M | 100K | 无限 |
| Scale | $399/月 | 80M | 20M | 无限 |
| Enterprise | 定制 | 无限 | 无限 | 无限 |

### 融资信息
- 2025 年 10 月完成 **$3M 种子轮**，由 Susa Ventures 领投，天使投资人包括 Dane Knecht（Cloudflare CTO）、Theo Browne、David Cramer 等。

## 竞品清单

| 竞品 | Stars/规模 | 定位 | 差异点 |
|---|---|---|---|
| **Mem0** (mem0ai/mem0) | ~25K+ stars | AI Agent 记忆层，YC 支持 | 细粒度记忆控制，图谱特性；开源自部署 + 云端双模式 |
| **Zep** (getzep/zep) | ~3K+ stars | 时序知识图谱记忆 | 侧重时序推理和事实变化追踪，企业级 |
| **Letta** (letta-ai/letta，原 MemGPT) | ~15K+ stars | LLM 自主管理记忆的 Agent 运行时 | 类 OS 分层架构（core/archival/recall），Agent 自决定存取 |
| **LangMem** (langchain-ai) | LangGraph 生态内 | LangGraph 长期记忆模块 | 专注工作记忆压缩，JSON 文档存储 |
| **Graphlit** | 商业产品 | 非结构化数据 RAG 平台 | 侧重文档处理管线，非记忆引擎 |
| **SuperLocalMemory** | 新兴 | 本地优先的隐私记忆方案 | 完全本地化，适合数据主权场景 |

### Supermemory 的差异化优势
1. **基准测试第一**：LongMemEval / LoCoMo / ConvoMem 三大基准全部排名第一
2. **一体化**：Memory + RAG + User Profiles + Connectors + File Processing 在一个 API 中
3. **性能**：宣称召回速度比 Zep 快 10x，比 Mem0 快 25x（sub-300ms）
4. **开发者体验**：API surface 极简，MCP 一键安装，SDK 支持主流框架

## 关键 Issue 信号

### 高讨论量 Issue/PR（历史）
| # | 标题 | 评论数 | 状态 | 信号 |
|---|---|---|---|---|
| #443 | feat: layout design with theme improvements | 17 | closed | UI 演进活跃 |
| #506 | It's not working locally | 15 | closed | 本地部署有门槛，需关注 DX |
| #440 | feat: Raycast extension for supermemory | 15 | closed | 社区驱动的平台集成 |
| #384 | feat: Integrations page with shortcuts & auto API Key generation | 12 | closed | 集成管理需求 |
| #599 | feat(tools): allow passing apiKey via options for browser support | 9 | closed | 浏览器端使用需求 |
| #163 | pnpm | 8 | closed | 早期包管理器迁移 |
| #663 | pipecat-sdk | 8 | closed | 语音/实时 AI SDK 集成 |

### 当前活跃 Open PR
| # | 标题 | 评论数 | 信号 |
|---|---|---|---|
| #791 | voltagent-sdk | 4 | 社区贡献新 SDK 集成 |
| #769 | Vercel AI SDK backfilling | 4 | 框架集成完善 |
| #744 | Supermemory-Cartesia SDK | 4 | 语音 AI 集成 |
| #733 | fix(mcp): register handler on bare /mcp path | 3 | MCP 协议兼容修复 |
| #786 | perf(middleware): await background task cancellation on timeout | 3 | 性能优化 |
| #755 | Supermemory ADK SDK | 1 | Google ADK 集成 |

> **趋势信号**：当前 open PR 多为外部 SDK 集成请求，表明社区正在积极将 Supermemory 接入各类 AI Agent 框架。

## 知识入口

| 来源 | 链接 | 说明 |
|---|---|---|
| DeepWiki | https://deepwiki.com/supermemoryai/supermemory | 有完整架构解析，含客户端层、核心服务、部署架构 |
| Zread.ai | https://zread.ai/supermemoryai/supermemory | 有 31+ 篇结构化文档，覆盖 API、架构、Memory Graph、贡献者等 |
| 官方文档 | https://supermemory.ai/docs | 完整 API 参考 + 概念文档 + 快速开始指南 |
| 官方博客 | https://supermemory.ai/blog | 架构设计深度文章（Memory Engine 脑结构灵感） |
| TechCrunch | https://techcrunch.com/2025/10/06/... | 融资报道，创始人故事 |
| DEV Community | https://dev.to/.../5-ai-agent-memory-systems-compared... | 5 大记忆系统对比（含基准数据） |
| LogRocket Blog | https://blog.logrocket.com/building-ai-apps-mem0-supermemory/ | Mem0 vs Supermemory 实操对比 |
| Medium | https://medium.com/@bumurzaqov2/top-10-ai-memory-products-2026... | 2026 年 AI 记忆产品 Top 10 |
| Better Stack | https://betterstack.com/community/guides/ai/memory-with-supermemory/ | Supermemory 集成教程 |

## 项目展示素材

### Logo & 品牌
- Logo SVG：`apps/web/public/logo-fullmark.svg`（深色）/ `apps/web/public/logo-light-fullmark.svg`（浅色）
- 品牌色：蓝色调

### 截图
- 产品仪表盘截图（README 内嵌 GitHub user-attachments 图片）
- 架构总览图（宽 1414px）
- 插件展示图（Claude Code / OpenCode / OpenClaw）
- 消费端应用截图（app.supermemory.ai，宽 1705px）

### 标语
- "State-of-the-art memory and context engine for AI."
- "Your AI forgets everything between conversations. Supermemory fixes that."
- "Give your AI a memory. It's about time."
- "The Memory API for the AI era."

### 基准成绩亮点
- LongMemEval: 81.6% — #1
- LoCoMo: #1
- ConvoMem: #1

### 代码示例
- TypeScript/Python 双语快速开始代码（5 行核心代码）
- MCP 一行安装命令：`npx -y install-mcp@latest https://mcp.supermemory.ai/mcp --client claude --oauth=yes`

## 快速判断

| 维度 | 评级 | 说明 |
|---|---|---|
| **热度** | ★★★★★ | 17K stars，持续增长无衰退，AI 记忆赛道明星项目 |
| **活跃度** | ★★★★★ | 每天有提交，open PR 活跃，社区持续贡献 SDK 集成 |
| **商业化** | ★★★★☆ | 已融资 $3M，有清晰定价和商业模式，免费层慷慨 |
| **技术深度** | ★★★★★ | 三大基准第一，自研向量图引擎，Memory vs RAG 深度区分 |
| **生态整合** | ★★★★★ | 覆盖所有主流 AI 框架/客户端/MCP 协议，连接器丰富 |
| **文档质量** | ★★★★☆ | 官方文档完整，有架构博客，但本地部署文档曾有用户反馈问题 |
| **竞争壁垒** | ★★★★☆ | 基准领先 + 生态广度是壁垒；但赛道拥挤（Mem0/Zep/Letta），需持续领先 |

### 一句话总结
Supermemory 是 2024-2026 年 AI Agent 记忆基础设施赛道的领跑者，由 20 岁创始人 Dhravya Shah 驱动，以三大基准第一的技术实力、极简 API 设计和广泛的框架集成构建起竞争力。项目处于快速商业化阶段（$3M 融资 + SaaS 定价），核心风险在于赛道竞争激烈（Mem0 星数更高、Letta 架构差异化明显）以及开源代码与商业服务的边界管理。
