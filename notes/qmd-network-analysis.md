# tobi/qmd 网络分析报告

## 仓库基本数据

| 指标 | 值 |
|------|-----|
| 名称 | qmd (Query Markup Documents) |
| 描述 | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
| URL | https://github.com/tobi/qmd |
| Stars | 16,407 |
| Forks | 984 |
| Watchers | 65 |
| Issues | 160（开放） |
| PRs | 92 |
| 主语言 | TypeScript（815K）|
| 其他语言 | Python（167K）、Shell（19K）、Nix（2.5K）、Just（1K）、Dockerfile（0.9K） |
| 许可证 | MIT |
| 创建时间 | 2025-12-08 |
| 最后推送 | 2026-03-14 |
| 最后更新 | 2026-03-22 |
| 磁盘占用 | 7.2 MB |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 默认分支 | main |
| 最新版本 | v2.0.1（2026-03-11） |

**要点**：项目仅存在约 3.5 个月，已积累 16K+ Stars，增长极为迅猛。TypeScript 为主，附带 Python 脚本（可能用于模型微调/数据处理）。MIT 许可证对商用和二次开发友好。

## 作者画像

| 指标 | 值 |
|------|-----|
| 用户名 | tobi |
| 真名 | Tobias Lutke |
| 公司 | Shopify |
| 地点 | Ottawa, Canada |
| 博客 | tobi.lutke.com |
| 粉丝 | 4,487 |
| 公开仓库 | 85 |
| GitHub 注册 | 2008-02-17 |

**身份**：Shopify 创始人兼 CEO，加拿大科技圈顶级人物，GitHub 上拥有 4,400+ 粉丝。

**近期活跃仓库**：

| 仓库 | Stars | 语言 | 最后推送 |
|------|-------|------|----------|
| amux | 18 | TypeScript | 2026-03-18 |
| ac-tracer | 8 | Lua | 2026-03-18 |
| frameling | 2 | Shell | 2026-01-25 |
| AudioPriorityBar | 625 | Swift | 2025-12-29 |
| dotfiles | 20 | Shell | 2025-06-06 |
| cow-tree | 4 | C | 2024-07-14 |

**画像总结**：Tobi 是典型的"CEO 黑客"——Shopify 掌门人，同时保持高强度个人编程习惯。qmd 是他"为自己造工具"理念的产物，他在 X 上公开表示"QMD 是我最好的工具之一，每天都在用"。这种创始人背书+个人使用+开源的模式，为项目带来了天然的流量和信任度。

## 社区热度

### Star 增长趋势

| 月份 | 新增 Stars | 累计（约） |
|------|-----------|-----------|
| 2025-12 | 599 | 599 |
| 2026-01 | 4,258 | 4,857 |
| 2026-02 | 6,202 | 11,059 |
| 2026-03（至22日） | 5,350 | 16,409 |

**增长分析**：
- 创建首月（2025-12 部分月份）收获 ~600 Stars，说明 Tobi 的影响力带来了冷启动流量
- 2026-01 爆发增长至 4,258，可能是 Hacker News 帖子和社交媒体传播
- 2026-02 达到峰值 6,202，项目进入主流视野
- 2026-03 保持高位 5,350，增长未见衰退迹象
- **月均增长 ~5,000 Stars**，属于现象级开源项目增速

### 贡献者分布

| 贡献者 | 提交数 | 角色 |
|--------|--------|------|
| tobi | 298 | 核心作者（~90% 提交） |
| claude | 5 | AI 辅助编程 |
| shreyaskarnik | 4 | 社区贡献者 |
| mbrendan | 3 | 社区贡献者 |
| burke | 3 | 社区贡献者 |
| 其他 25 人 | 1-2 | 社区贡献者 |

**贡献模式**：高度集中的个人项目，tobi 占绝对主导。值得注意的是 `claude` 作为贡献者出现，说明作者在使用 AI 辅助开发。社区贡献者约 30 人，以小修复和功能 PR 为主。v1.1.2 版本一次性合并了 13 个社区 PR，表明作者愿意接受外部贡献。

### 发版节奏

- v1.1.0 → 2026-02-20
- v1.1.1 → 2026-03-06
- v1.1.2 → 2026-03-07
- v1.1.5 → 2026-03-08
- v1.1.6 → 2026-03-09
- v2.0.0 → 2026-03-10
- v2.0.1 → 2026-03-11

**3 月上旬连续 6 天发布 6 个版本**，从 1.1.0 跳跃到 2.0.0，发版密度极高，处于活跃冲刺阶段。

## 生态网络

### 直接生态

| 项目/工具 | 关系 | 说明 |
|-----------|------|------|
| [lazyqmd](https://alexanderzeitler.com/articles/introducing-lazyqmd-a-tui-for-qmd/) | TUI 前端 | 社区开发的终端 UI 包装器 |
| [openclaw/skills/qmd](https://playbooks.com/skills/openclaw/skills/qmd) | AI Skill 集成 | QMD 作为 AI agent skill 被注册 |
| [Ghost](https://news.ycombinator.com/item?id=47007379) | 衍生项目 | 基于 QMD 的 Claude Code 会话记忆工具 |
| node-llama-cpp | 核心依赖 | 本地 LLM 推理引擎 |
| sqlite-vec | 核心依赖 | 向量索引扩展 |
| better-sqlite3 | 核心依赖 | SQLite 绑定 |
| Claude Desktop / Claude Code | 集成目标 | 通过 MCP Server 对接 |
| Duffel | 生态引用 | HN 上提到的搜索工作区工具引用 QMD |

### 技术栈定位

QMD 处于 **"本地 AI 搜索基础设施"** 层，连接了：
- 上游：GGUF 模型生态（Qwen3-Reranker、嵌入模型）
- 中游：MCP 协议生态（Claude Code、Claude Desktop）
- 下游：个人知识管理、AI Agent 工作流

## 官方文档洞察

### README 要点
- 定位清晰：**本地全栈搜索引擎**，支持 BM25 + 语义搜索 + LLM 重排序
- 三种使用方式：CLI 工具、SDK 库、MCP Server
- 安装方式：npm/bun 全局安装或 npx 直接运行
- 专门强调 AI Agent 友好（`--json`、`--files` 输出格式）
- MCP Server 支持 stdio 和 HTTP 两种传输方式
- SDK 从 v1.1.6 开始提供，v2.0.0 宣布稳定 API

### DeepWiki 架构洞察
- 内容可寻址存储：文档以 SHA-256 哈希标识，自动去重
- 三级检索：BM25 → 向量语义 → HyDE（假设性回答嵌入）
- 融合策略：Reciprocal Rank Fusion（RRF），原始查询 2x 权重
- 智能分块：~900 token，优先在 markdown 标题处切分
- 位置感知混合：top-3 候选 75% 检索权重，rank 11+ 仅 40%
- 模型自动下载：嵌入（300MB）、重排序（640MB）、查询扩展（1.1GB）

## 竞品清单

| 竞品 | 语言 | 特点 | 与 QMD 的差异 |
|------|------|------|---------------|
| [Semantra](https://github.com/freedmand/semantra) | Python | 语义搜索 + Web UI | 仅语义搜索，无 BM25/重排序，无 MCP |
| [Open Semantic Search](https://opensemanticsearch.org/) | Python/Java | 企业级全文搜索 + NER + 知识图谱 | 重量级服务器方案，非 CLI 本地工具 |
| [Recoll](https://www.recoll.org/) | C++ | 桌面全文搜索，近期实验语义搜索 | 传统桌面搜索，非 AI-native |
| ripgrep / fzf | Rust | 极速文本搜索 | 纯文本匹配，无语义理解 |
| Apple Spotlight | 系统内置 | 系统级搜索 | 无语义搜索、无 Agent 集成 |

**QMD 的独特定位**：唯一同时满足以下条件的工具——(1) 完全本地、(2) 混合搜索（BM25+向量+LLM重排序）、(3) CLI 优先、(4) MCP Server 原生支持 AI Agent 集成、(5) Markdown/知识库专精。

## 关键 Issue 信号

| # | 标题 | 评论 | 状态 | 信号 |
|---|------|------|------|------|
| [#114](https://github.com/tobi/qmd/issues/114) | [FEATURE]: models via API | 9 | open | 社区要求远程模型 API 支持，需求强烈 |
| [#291](https://github.com/tobi/qmd/issues/291) | RERANK_CONTEXT_SIZE too small — crashes on CJK | 8 | open | CJK（中日韩）内容支持问题，国际化痛点 |
| [#356](https://github.com/tobi/qmd/issues/356) | bin/qmd fails via bun global symlink | 5 | open | 安装/运行时兼容性问题 |
| [#247](https://github.com/tobi/qmd/issues/247) | Query Expansion model finetuning — benchmarks | 5 | open | 作者寻求社区帮助微调模型 |
| [#239](https://github.com/tobi/qmd/issues/239) | Opt-in Cohere Rerank API | 5 | open | CPU 上非英文重排序极慢 |
| [#212](https://github.com/tobi/qmd/issues/212) | qmd embed hangs on Apple Silicon M1 | 5 | open | 硬件兼容性问题 |
| [#141](https://github.com/tobi/qmd/issues/141) | Extremely slow on WSL2 | 5 | open | WSL 环境性能差 |

**Issue 信号解读**：
- **性能瓶颈**：重排序在 CPU 上慢（尤其非英文）、M1 挂起、WSL2 性能差 → GPU 加速是刚需
- **国际化**：CJK 内容支持尚有 bug，但已有多语言嵌入模型支持（QMD_EMBED_MODEL）
- **远程模型需求**：#114 和 #239 都指向社区希望可选的远程 API 后端，目前仅本地推理
- **安装体验**：bun 和 npm 的安装路径仍有边缘问题

### 最新 PR 动向（2026-03-19~21）

| PR | 标题 | 方向 |
|----|------|------|
| #451 | 时间相关性增强 | 搜索质量 |
| #449 | tree-sitter AST 感知代码分块 | 代码搜索 |
| #446 | OpenAI 兼容端点的远程推理 | 远程 API |
| #444 | Modal.com 远程 GPU 推理后端 | 远程 GPU |
| #442 | Bun 并行初始化的 SQLite 竞态修复 | 稳定性 |

社区 PR 正在推动项目从"纯本地"向"可选远程"方向演进。

## 知识入口

| 平台 | URL | 状态 |
|------|-----|------|
| DeepWiki | https://deepwiki.com/tobi/qmd | 已收录，包含架构和搜索原理详解 |
| Zread.ai | https://zread.ai/tobi/qmd | 已收录，提供概览和学习路径 |
| Hacker News | https://news.ycombinator.com/item?id=46689289 | 主帖，标题"QMD - Quick Markdown Search" |
| Hacker News (Show HN) | https://news.ycombinator.com/item?id=44593721 | 早期展示帖 |
| X (Twitter) | https://x.com/tobi/status/2013217570912919575 | 作者亲自推广 |
| npm | @tobilu/qmd | npm 包已发布 |
| GitHub Releases | https://github.com/tobi/qmd/releases | 完整版本历史 |

## 项目展示素材

### 一句话介绍
> An on-device search engine for everything you need to remember. Index your markdown notes, meeting transcripts, documentation, and knowledge bases. Search with keywords or natural language.

### 核心卖点
- **三合一搜索**：BM25 全文 + 向量语义 + LLM 重排序，全部本地运行
- **Agent 原生**：MCP Server 内置，Claude Code 一键集成
- **零依赖外部服务**：通过 node-llama-cpp + GGUF 模型实现完全离线
- **SDK 可编程**：v2.0 提供稳定的 TypeScript SDK，可嵌入自定义应用

### 技术架构图
README 中引用 `assets/qmd-architecture.png` 架构图。

### 典型用法
```sh
qmd collection add ~/notes --name notes
qmd embed
qmd query "quarterly planning process"  # 混合搜索 + 重排序
```

## 快速判断

| 维度 | 评分 | 说明 |
|------|------|------|
| 作者影响力 | ★★★★★ | Shopify CEO，科技圈 S 级影响力 |
| 项目活跃度 | ★★★★★ | 3 月连发 6 版本，社区 PR 持续涌入 |
| 技术深度 | ★★★★☆ | BM25+向量+LLM 混合检索，RRF 融合，位置感知混合，架构专业 |
| 增长势头 | ★★★★★ | 3.5 个月 16K Stars，月均 5K，现象级增速 |
| 社区参与 | ★★★★☆ | 30+ 贡献者，160 Issues，92 PRs，生态工具已出现 |
| 实用性 | ★★★★☆ | 作者每天自用，解决真实痛点，但 GPU 依赖和安装体验仍有门槛 |
| 竞争壁垒 | ★★★★☆ | 唯一的"本地混合搜索 + MCP Agent 集成"方案，定位独特 |

**总体判断**：**高价值、高动量项目**。Tobias Lutke 的个人品牌 + Shopify CEO 光环为项目带来了顶级流量，但项目本身的技术含量也配得上这个关注度。QMD 精准填充了"本地 AI 搜索 + Agent 工具链"的空白，是 MCP 生态中少有的"搜索基础设施"级项目。主要风险在于：(1) 高度依赖单一作者；(2) GPU/性能问题限制了非 Mac 用户体验；(3) 项目仍处于早期快速迭代阶段，API 刚刚稳定。
