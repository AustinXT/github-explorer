## 仓库基本数据
- Star / Fork / Watcher: 47,673 / 7,680 / 284
- 语言: TypeScript (96.9%), Shell (1.5%), JavaScript (1.1%), CSS (0.3%), HTML (0.2%), Dockerfile (0.1%)
- License: MIT — 完全商业可用
- 创建时间: 2026-03-02 | 最近推送: 2026-04-05
- 话题标签: 无（仓库未设置 topics）
- 已归档: 否 | 是Fork: 否
- 主页: https://paperclip.ing
- npm 包: paperclipai（最新版 2026.403.0，最近发布 2026-04-04）
- 磁盘占用: ~13.8 MB

## 作者画像
- 组织/ID: paperclipai (Paperclip) | 类型: GitHub Organization
- Bio: "The zero-human business building company - manage business goals, not pull requests"
- 官网: https://paperclip.ing
- 粉丝: 962 | 公开仓库: 8 | 账号创建: 2026-02-27（仅 ~5 周前）
- 核心开发者: **cryppadotta (Dotta)** — 1,152 commits，占绝对主导地位
  - Dotta 背景: CEO of Forgotten Runes Wizards Cult（知名 NFT/Web3 项目），Crypto-quant，2018 年创建 ERC721 软件许可协议 Dotlicense
  - GitHub: 745 粉丝，18 个公开仓库，账号自 2017 年
- 此 repo 投入权重: **极高** — 是组织的核心旗舰项目，其余 7 个仓库（pr-reviewer, companies-tool, companies, docs, clipmart, paperclip-website, .github）均为配套生态
- 作者类型: **创业公司/开源组织** — 有明确的产品愿景和商业方向
- 贡献集中度: **单人主导** — cryppadotta 贡献 1,152 次，第二名 devinfoley 仅 56 次，前两名之后贡献数急剧下降。约 30 位贡献者，但 Dotta 占比约 80%+
- 背景推断: Dotta 是 Web3/加密领域资深开发者，从 NFT 项目转向 AI Agent 赛道。具有创业经验和产品思维，不是纯学术型开发者。Paperclip 是他全力投入的新赌注。

## 社区热度
- 热度级别: **大众热门** — 47,673 stars，已进入 GitHub 顶级开源项目行列
- 增长模式: **爆发型 + 持续高速增长**
  - 2026-03-04 创建（首个 star 记录为 2026-03-04T17:40:20Z）
  - ~Mar 08: 接近 0 → Mar 15: ~10,000 → Mar 22: ~20,000 → Mar 29: ~30,000 → Apr 05: ~40,000+
  - 仅用约 1 个月从 0 涨到 47,000+ stars，平均每天 ~1,500 stars
  - 三周内突破 30,000 stars（据媒体报道确认）
- 近期趋势: **仍在高速增长中**，最近一周从 ~40K 涨到 ~47.7K
- 套利判断: **已无信息差** — 项目已经爆发，大量媒体覆盖（Towards AI、eWeek、Medium、MindStudio 等均有专题文章）。但项目仅 1 个月大，仍处于早期阶段，如果关注的是「早期参与生态建设」仍有空间。

## 生态网络
- 上游依赖: Node.js 20+, pnpm 9.15+, PostgreSQL (内嵌), React, Express, Drizzle ORM
- 下游生态:
  - **Clipmart**（即将推出）: 预制公司模板市场，一键导入完整组织结构
  - **awesome-paperclip** (gsxdsm): 社区插件和资源收集
  - **paperclip-plugin-company-wizard** (Yesterday-AI): 模板引导插件，70 stars
  - **Agent 适配器**: 支持 Claude Code, OpenClaw, Codex, Cursor, Gemini CLI, Bash, HTTP
- npm 包: paperclipai — 通过 `npx paperclipai onboard --yes` 一键安装
- 同类项目: CrewAI, AutoGen, HumanLayer, LangGraph（见竞品清单）

## 官方文档洞察

| 要素 | 内容 |
|------|------|
| **价值主张** | 「If OpenClaw is an employee, Paperclip is the company」— 不是又一个 Agent 框架，而是管理 Agent 团队的公司级编排系统 |
| **目标用户** | 技术型创业者、运营多个 AI Agent 的开发者、想构建「零人公司」的用户 |
| **差异化叙事** | 不做 chatbot、不做 workflow builder、不做 prompt manager — 做的是 Agent 的「公司操作系统」，用组织架构（org chart）+ 目标体系 + 预算治理来替代临时的脚本拼凑 |
| **设计哲学** | 原子执行、持久 Agent 状态、运行时技能注入、带回滚的治理、目标感知执行、可移植公司模板、真正的多公司隔离 |
| **技术路线图** | 已完成: 插件系统、OpenClaw 集成、公司导入导出、AGENTS.md 配置、技能管理器、定时任务、预算控制。计划中: Artifacts & Deployments、CEO Chat、MAXIMIZER MODE、多用户、云沙箱 Agent、云部署、桌面 App |
| **公开的架构文章** | 官方博客无深度技术文章，但 DeepWiki 已生成完整架构文档（三层架构: React 前端 + Express 后端 + PostgreSQL 数据层） |

## 竞品清单

| 项目 | Stars | 定位 | 与 Paperclip 的差异 |
|------|-------|------|---------------------|
| **CrewAI** (crewAIInc/crewAI) | 48,098 | 角色扮演式多 Agent 协作框架 | 框架级——提供 Agent 编排原语；Paperclip 是应用级——提供完整的公司管理 UI 和治理 |
| **HumanLayer** (humanlayer/humanlayer) | 10,276 | AI 编码 Agent 编排层 | 专注代码开发场景的多 Claude 会话管理；Paperclip 面向通用业务编排 |
| **AutoGen** (microsoft/autogen) | ~37,000+ | 微软的多 Agent 对话框架 | 学术/研究导向，强调 Agent 间对话；Paperclip 强调公司治理和预算控制 |
| **LangGraph** (langchain-ai/langgraph) | ~15,000+ | 基于图的 Agent 工作流框架 | 底层编排库，需自行构建 UI；Paperclip 开箱即用 |
| **Dify** (langgenius/dify) | ~70,000+ | LLM 应用开发平台 | 更广泛的 LLM 应用平台，非专注于多 Agent 公司编排 |

**竞品格局总结**: Paperclip 在「公司隐喻 + 多 Agent 治理」这个精确定位上暂无直接竞品，但 CrewAI 在 star 数上几乎持平，且覆盖面更广。Paperclip 的独特性在于它不是一个框架而是一个产品——自带 UI、预算系统、审计日志。

## 关键 Issue 信号

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| #1971 | fix(issues): recover stale execution run lock on checkout | 148 | Open | 核心运行时稳定性问题，社区高度关注 |
| #187 | Feature Request: Support for Local LLMs via Ollama | 23 | Open | 社区强烈需求本地模型支持，已有 PR #2362 添加 Qwen Ollama 适配器 |
| #1413 | feat(ui): Add Conversations Panel (Chat) | 18 | Open | 用户需要 Agent 与管理者之间的实时对话通道 |
| #2776 | feat: add secrets.write capability to plugin system | 18 | Open | 插件系统安全能力扩展 |
| #1077 | Allow manager agents to interrupt subordinate task runs | 15 | Closed | 管理层级中断机制——已实现 |
| #251 | fix(heartbeat): prevent false process_lost failures | 15 | Closed | 心跳机制的可靠性修复——已解决 |
| #131 | Add automated response eval harness | 3 | Open | 质量评估自动化，方向正确但关注度不高 |

**Issue 信号总结**: 总 Issue 722 个、PR 1,039 个，对于仅 1 个月的项目来说异常活跃。核心关注点集中在运行时稳定性、本地模型支持、Agent 间通信和插件安全——符合早期快速迭代阶段的特征。

## 知识入口
- DeepWiki: https://deepwiki.com/paperclipai/paperclip — **已收录**，有完整架构文档
- Zread.ai: **未收录**（403 错误）
- 关联论文: **无** — arxiv 搜索结果均为经典的「回形针最大化器」AI 安全思想实验论文，与本项目无关
- 在线 Demo: **无公开在线 playground** — 纯自托管，需本地运行 `npx paperclipai onboard --yes`
- 外部教程/评测:
  - [Paperclip AI Review (Mr Delegate)](https://mrdelegate.ai/blog/paperclip-ai-review/)
  - [Paperclip Review 2026 (Vibe Coding App)](https://vibecoding.app/blog/paperclip-review)
  - [OpenClaw vs Paperclip (Flowtivity)](https://flowtivity.ai/blog/openclaw-vs-paperclip-ai-agent-framework-comparison/)
  - [Paperclip Explained (Towards AI)](https://pub.towardsai.net/paperclip-the-open-source-operating-system-for-zero-human-companies-2c16f3f22182)
  - [Paperclip: Company OS (Substack)](https://nervegna.substack.com/p/paperclip-the-company-os-your-agents)
  - [Discord 社区](https://discord.gg/m4HZY7xNG3)

## 项目展示素材

1. **头图**: `https://raw.githubusercontent.com/paperclipai/paperclip/master/doc/assets/header.png` — 项目主横幅，展示品牌标识
2. **演示视频**: `https://github.com/user-attachments/assets/773bdfb2-6d1e-4e30-8c5f-3487d5b70c8f` — README 内嵌的产品演示视频（GitHub user-attachments 托管）
3. **尾图**: `https://raw.githubusercontent.com/paperclipai/paperclip/master/doc/assets/footer.jpg` — 品牌收尾图

## 快速判断
- 是否值得深入: **是** — 47K+ stars、极速增长、清晰的产品定位、活跃的开发节奏、MIT 开源，且处于 AI Agent 编排这一热门赛道的差异化位置
- 初步定位: **AI Agent 多智能体编排的「公司操作系统」** — 不是框架而是产品，用组织架构隐喻重新定义了多 Agent 管理范式
- 作者可信度: **中高** — Dotta 有 Web3 创业背景和技术实力，但 Paperclip 项目极其年轻（仅 1 个月），组织账号也才 5 周。长期维护承诺尚需观察。从 NFT 转向 AI 的跨界跳跃需要关注后续投入持续性
- 竞品格局: **细分蓝海** — 在「Agent-as-Company」这个精确定位上暂无直接竞品。CrewAI 是最大的间接竞争对手但定位为框架而非产品。市场正在快速形成中，Paperclip 抢占了叙事高地
