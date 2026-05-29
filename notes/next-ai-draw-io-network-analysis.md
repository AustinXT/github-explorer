## 仓库基本数据

| 指标 | 值 |
|------|------|
| 名称 | next-ai-draw-io |
| 描述 | A next.js web application that integrates AI capabilities with draw.io diagrams |
| URL | https://github.com/DayuanJiang/next-ai-draw-io |
| 主页 | https://next-ai-drawio.jiang.jp/ |
| Stars | 26,109 |
| Forks | 2,746 |
| Watchers | 87 |
| Issues | 115（总计） |
| Pull Requests | 28（总计） |
| 许可证 | Apache License 2.0 |
| 主语言 | TypeScript（93.6%） |
| 其他语言 | JavaScript（4.7%）、CSS（1.2%）、HTML（0.4%）、Dockerfile（0.1%） |
| 创建时间 | 2025-03-23 |
| 最近推送 | 2026-04-04 |
| 最近更新 | 2026-04-05 |
| 磁盘占用 | 5.6 MB |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 默认分支 | main |
| Topics | ai, diagrams, productivity |
| 当前版本 | v0.4.14（2026-03-30 发布） |
| 社区健康度 | 71% |

## 作者画像

| 指标 | 值 |
|------|------|
| 用户名 | DayuanJiang |
| 姓名 | Dayuan Jiang |
| 所在地 | 东京（Tokyo） |
| 个人博客 | www.jiang.jp |
| 公开仓库 | 32 个 |
| Followers | 240 |
| Following | 1 |
| 注册时间 | 2017-12-10 |
| 身份 | 旅日华人，Generative AI 工程师，在日本生活 8 年以上 |

**背景分析**：Dayuan Jiang 是一位定居东京的 AI 工程师，个人博客 jiang.jp 专注于 NLP、LLM 和 Web 开发。从仓库列表来看，他 fork 了 claude-code、Vercel AI SDK（nim）、ml-engineering 等项目，表明对 AI 基础设施有深度关注。此前没有高 Star 项目，next-ai-draw-io 是其第一个爆款开源作品。

**近期活跃仓库**（按推送时间排序）：

| 仓库 | 语言 | Stars | 是否 Fork |
|------|------|-------|-----------|
| next-ai-draw-io | TypeScript | 26,109 | 否 |
| claude-code | - | 0 | 是 |
| nim (Vercel AI SDK) | TypeScript | 1 | 是 |
| ai | TypeScript | 0 | 是 |
| ml-engineering | Python | 1 | 是 |
| sdk-python | - | 0 | 是 |
| ChatGPT-Next-Web-base | TypeScript | 2 | 是 |
| japanese_blog | Jupyter Notebook | 0 | 否 |

**贡献者分布**：

| 贡献者 | 提交数 | 角色 |
|--------|--------|------|
| DayuanJiang | 477 | 核心维护者，占 77% 提交 |
| Biki-dev | 29 | 活跃贡献者（UI 修复） |
| renovate[bot] | 29 | 自动化依赖更新 |
| ElshadHu | 15 | 贡献者 |
| broBinChen | 13 | 贡献者 |
| shibamudi | 13 | 贡献者 |
| 其他 24 人 | 1-5 | 社区贡献者 |

项目以作者个人驱动为主，有 30 位贡献者参与，社区参与度中等偏上。

## 社区热度

### Star 增长趋势

- **创建日期**：2025-03-23，最早 Star 记录为 2025-03-24
- **里程碑**：2025 年 12 月 12 日单日增长 1,038 Stars，登上 GitHub Trending 第 2 名
- **爆发期**：2025 年 12 月单周增长超过 4,500 Stars
- **当前规模**：26,109 Stars（截至 2026-04-05）
- **近 7 天增长**：+592 Stars（HelloGitHub 数据）
- **增长轨迹**：从 2025-03 创建到现在约一年，增长曲线呈爆发式上升后进入稳定增长阶段

### 发布节奏

| 版本 | 发布日期 |
|------|----------|
| v0.4.14 | 2026-03-30 |
| v0.4.13 | 2026-03-07 |
| v0.4.12 | 2026-01-24 |
| v0.4.11 | 2026-01-18 |
| v0.4.10 | 2026-01-09 |

发布频率约 3-4 周一个版本，开发节奏稳定。最近 10 次提交（截至 2026-04-03）均为功能增加和 bug 修复，活跃度很高。

### 外部平台评价

- **HelloGitHub**：评分 9.0/10（13 人评价），48 人投票、42 人收藏，好评率 84%
- **Hacker News**：Show HN 帖子引发关注（2025-12）
- **TrendShift**：获得 TrendShift 徽章（排名 #15449）
- **SourceForge**：已被镜像收录
- **ByteIota**：专题报道「AI Diagram Generator Hits #2 on GitHub」

## 生态网络

### 技术栈依赖

- **前端框架**：Next.js 16.x + React 19.x
- **AI 集成**：Vercel AI SDK（`ai` + `@ai-sdk/*`）
- **图表渲染**：react-drawio（基于 draw.io）
- **桌面端**：Electron（支持 Windows/macOS/Linux）
- **MCP 协议**：`@next-ai-drawio/mcp-server`（支持 Claude Desktop、Cursor、VS Code）

### AI 模型支持（14 个 Provider）

ByteDance Doubao（赞助商）、AWS Bedrock（默认）、OpenAI、Anthropic、Google AI、Google Vertex AI、Azure OpenAI、Ollama、OpenRouter、DeepSeek、SiliconFlow、ModelScope、SGLang、Vercel AI Gateway

### 部署平台支持

Vercel、Tencent EdgeOne Pages、Cloudflare Workers、Docker、Electron 桌面应用

### 赞助关系

字节跳动 Doubao（豆包）赞助了 Demo 站点的 API Token 用量，Demo 站默认使用 glm-4.7 模型。

## 官方文档洞察

- **官方文档站**：https://next-ai-drawio.jiang.jp/（Live Demo 兼文档入口）
- **Provider 配置指南**：`docs/en/ai-providers.md`
- **Docker 部署指南**：`docs/en/docker.md`
- **Cloudflare 部署指南**：`docs/en/cloudflare-deploy.md`
- **FAQ**：`docs/en/FAQ.md`
- **多语言 README**：支持英文、中文（`docs/cn/README_CN.md`）、日文（`docs/ja/README_JA.md`）
- **阮一峰周刊推荐**：作者曾向「阮一峰周刊」自荐（issue #8386）

### DeepWiki 洞察

DeepWiki 已收录该项目，提供了详细的架构分析：
- 三层架构设计（前端 React 组件层、后端 Next.js API 层、AI 集成层）
- 核心端点 `/api/chat` 使用流式响应（`ai.streamText()`）
- AI 工具调用机制：`display_diagram`、`edit_diagram`、`append_diagram`
- XML 自动修复机制：对 AI 生成的 XML 应用 13 步自动修复流程
- 状态管理：`DiagramContext` 维护 20 版本历史缓冲

**DeepWiki 地址**：https://deepwiki.com/DayuanJiang/next-ai-draw-io

## 竞品清单

| 项目 | 类型 | 特点 | 差异化 |
|------|------|------|--------|
| **Eraser DiagramGPT** | SaaS（闭源） | GPT-4 驱动，支持 ER 图、云架构图、时序图 | 闭源 SaaS，功能更专注但不可自部署 |
| **Excalidraw** | 开源白板 | 手绘风格，实时协作，极简 UI | 侧重快速草图，非结构化图表生成 |
| **Mermaid** | 开源图表 | 文本描述转图表，嵌入文档 | 代码驱动，无可视化编辑器 |
| **PlantUML** | 开源 UML | 文本转 UML，集成广泛 | 专注 UML，不支持自由绘图 |
| **ConceptViz** | AI 图表工具 | 纯文本转图表，速度快 | 功能较简单，无 draw.io 兼容 |
| **Draft1.ai** | AI 图表 SaaS | 类 draw.io 的 AI 图表生成 | 闭源，竞品定位最接近 |
| **draw.io（原生）** | 开源图表编辑器 | 功能最全的图表编辑器 | 无 AI 能力，纯手动操作 |

**next-ai-draw-io 的独特定位**：唯一一个将 AI 对话能力与 draw.io 原生 XML 格式深度结合的开源项目。既保留了 draw.io 的完整编辑能力（包括 AWS/GCP/Azure 云架构图标），又支持自然语言交互式创建和修改，且支持 14 种 AI Provider 和自部署。

## 关键 Issue 信号

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| [#287](https://github.com/DayuanJiang/next-ai-draw-io/issues/287) | MCP Server is now available in Preview! | 21 | Open | MCP 集成是社区最关注的方向 |
| [#574](https://github.com/DayuanJiang/next-ai-draw-io/pull/574) | Feat/gcp vertex ai | 13 | Closed | 企业级云 AI 需求强烈 |
| [#703](https://github.com/DayuanJiang/next-ai-draw-io/pull/703) | Turn off certain features of quota popup for self-hosting | 9 | Closed | 自部署用户体验优化 |
| [#513](https://github.com/DayuanJiang/next-ai-draw-io/pull/513) | feat: add all Draw.io themes to settings panel | 7 | Open | 用户对主题定制有需求 |
| [#657](https://github.com/DayuanJiang/next-ai-draw-io/pull/657) | Fix: path handling with basepath | 5 | Closed | 部署兼容性问题 |
| [#711](https://github.com/DayuanJiang/next-ai-draw-io/issues/711) | Enable minimal chat panel when self-hosted | 5 | Open | 自部署定制需求 |
| [#550](https://github.com/DayuanJiang/next-ai-draw-io/pull/550) | Add setting for Enter/Ctrl+Enter to send messages | 4 | Closed | 用户体验细节关注 |
| [#704](https://github.com/DayuanJiang/next-ai-draw-io/pull/704) | Make quota management extensible and modular | 4 | Closed | 配额管理模块化 |

**Issue 信号分析**：社区关注的焦点集中在三个方向——(1) MCP/Agent 集成生态扩展；(2) 自部署场景的定制化需求；(3) 更多 AI Provider 的接入支持。

## 知识入口

| 平台 | 地址 | 状态 |
|------|------|------|
| DeepWiki | https://deepwiki.com/DayuanJiang/next-ai-draw-io | 已收录，含架构分析 |
| Zread.ai | https://zread.ai/repo/DayuanJiang/next-ai-draw-io | 无法访问（403） |
| HelloGitHub | https://hellogithub.com/en/repository/DayuanJiang/next-ai-draw-io | 已收录，评分 9.0/10 |
| Hacker News | https://news.ycombinator.com/item?id=46106523 | Show HN 讨论帖 |

## 项目展示素材

### 视频演示

- **主演示视频**（README 嵌入）：https://github.com/user-attachments/assets/9d60a3e8-4a1c-4b5e-acbb-26af2d3eabd1

### 示例图表（SVG，可直接使用）

| 示例 | 地址 | 说明 |
|------|------|------|
| Transformer 动画连接器 | https://raw.githubusercontent.com/DayuanJiang/next-ai-draw-io/main/public/animated_connectors.svg | Transformer 架构动画连接线 |
| GCP 架构图 | https://raw.githubusercontent.com/DayuanJiang/next-ai-draw-io/main/public/gcp_demo.svg | 含原生 GCP 图标 |
| AWS 架构图 | https://raw.githubusercontent.com/DayuanJiang/next-ai-draw-io/main/public/aws_demo.svg | 含原生 AWS 图标 |
| Azure 架构图 | https://raw.githubusercontent.com/DayuanJiang/next-ai-draw-io/main/public/azure_demo.svg | 含原生 Azure 图标 |
| 猫咪素描 | https://raw.githubusercontent.com/DayuanJiang/next-ai-draw-io/main/public/cat_demo.svg | 展示自由绘图能力 |
| 架构图 | https://raw.githubusercontent.com/DayuanJiang/next-ai-draw-io/main/public/architecture.png | 系统架构示意图 |
| 示例截图 | https://raw.githubusercontent.com/DayuanJiang/next-ai-draw-io/main/public/example.png | 应用界面示例 |

## 快速判断

| 维度 | 评估 |
|------|------|
| **热度** | 极高。26K+ Stars，GitHub Trending #2，单日峰值 1,038 Stars，近 7 天仍增长 592 |
| **质量信号** | 强。Apache 2.0 许可、TypeScript 强类型、13 步 XML 自动修复、20 版本历史缓冲 |
| **作者可信度** | 中高。旅日华人 AI 工程师，虽无此前爆款项目但技术深度可见，博客持续输出 |
| **维护状态** | 活跃。约 3 周一个版本，最近提交距今 3 天，477 次个人提交 |
| **社区生态** | 中等偏上。30 位贡献者、21 评论的 MCP 讨论帖、ByteDance 赞助 |
| **差异化** | 明确。唯一将 AI 对话 + draw.io XML 原生编辑 + 14 Provider + 自部署结合的开源方案 |
| **风险点** | 作者单点依赖（77% 提交）、复杂图表（>50 元素）AI 生成质量受限、依赖高端模型 |
| **建议** | 值得深度分析。定位清晰、增长强劲、技术实现有独到之处（XML 自动修复机制），适合公众号选题 |
