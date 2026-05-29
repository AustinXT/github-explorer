## 动机与定位

- **要解决的问题**: 信息过载时代，开发者和知识工作者需要快速消化来自多种媒体（网页、PDF、YouTube 视频、播客、音频/视频文件）的内容。现有工具要么只支持单一格式，要么封闭在 SaaS 中，缺乏本地化、可定制的 AI 摘要方案。
- **为什么现有方案不够**: 上游工具如 Jina Reader 和 Firecrawl 只做"提取"不做"摘要"，且不支持视频/音频/播客。下游 SaaS 摘要工具不开源、不可本地运行、无法与终端工作流或浏览器深度集成。没有一个工具同时覆盖 CLI + 浏览器扩展 + 全媒体格式 + 多 LLM 提供商这个组合。
- **目标用户**: 以 CLI 为核心工作流的开发者、内容消费密集型的研究者和知识工作者。次要用户为非技术用户（通过浏览器扩展 Side Panel 的零门槛使用路径）。

## 作者视角

### 问题发现

Peter Steinberger 是 PSPDFKit（PDF SDK，1 亿欧元级退出）的创始人，日常消费大量技术内容（博客、视频、播客）。这是一个典型的 **dogfooding 项目**——自己就是核心用户。从 CHANGELOG 和功能迭代看，每个功能都对应真实使用场景（播客通勤时的摘要需求、YouTube 技术演讲的幻灯片提取、浏览器侧边栏实时摘要）。

时机选择的合理性：2025-2026 年正是 LLM API 成本大幅下降、多模态模型（Gemini、GPT-4o）成熟的窗口期。两年前模型能力不足以支撑可靠的全媒体摘要，两年后市场可能已被大厂产品覆盖。当前是用开源 CLI 工具建立用户习惯和技术品牌的最佳窗口。

### 解法哲学

**"全媒体覆盖 + 多后端灵活性"**——这不是 Unix 哲学的"只做一件事"，而是围绕"摘要"这个核心动词做到极致覆盖。具体价值观体现为：

1. **用户不应关心后端细节**：`--model auto` 自动选择最优模型，token 数量自动匹配上下文窗口，cost 自动估算。用户只需传入 URL。
2. **渐进式复杂性**：零配置可用（`npx -y @steipete/summarize "url"`），但高级用户可配置模型规则、CLI 提供商优先级、缓存策略等。
3. **本地优先**：守护进程运行在 `127.0.0.1`，Whisper 优先本地运行，缓存使用本地 SQLite，不依赖远程服务。
4. **多提供商冗余**：6 个原生 LLM 提供商（OpenAI/Anthropic/Google/xAI/Z.AI/NVIDIA）+ OpenRouter 中继 + 4 个 CLI 提供商（Claude/Codex/Gemini/Agent）+ 6 个转录提供商。任何单点故障不影响可用性。

**明确选择不做的事情**：不做实时对话（Chat 功能仅限于浏览器扩展内对当前页面的问答）；不做云端托管版；不做用户数据收集。

### 背景知识迁移

1. **PDF 处理经验 → 文档提取管线**：PSPDFKit 的 PDF 处理经验直接影响了项目对 PDF/文档格式的专业支持，包括通过 `markitdown` 预处理、多种 Markdown 转换模式（readability/LLM/off）的灵活性。
2. **iOS SDK 产品化经验 → CLI 工具的产品化程度**：成熟的版本管理（lockstep 版本、Homebrew tap、Bun 编译二进制、npm 双包发布）、完善的发布流程（RELEASING.md 详细到每一步）、跨平台守护进程支持（launchd/systemd/Windows Scheduled Task）。这不是业余爱好项目的水平。
3. **移动端/桌面端集成经验 → 浏览器扩展架构**：Chrome Side Panel + 本地守护进程的架构设计，让浏览器扩展具备了原生应用级别的能力（调用 ffmpeg、yt-dlp、Whisper 等本地工具），这在纯浏览器扩展中是不可能的。

### 战略图景

这个项目是 Peter Steinberger 从 PSPDFKit 退出后的 **个人品牌基础设施**。从多个信号判断：

- **核心产品而非副业**：Star 数最高的自有项目，持续高频迭代（0.10→0.12 在 2 个月内），接受大量外部贡献。
- **genuinely open 而非 open-core**：MIT 许可证，无企业版、无付费功能、无 SaaS。npm 发布的包与 GitHub 源码完全一致。
- **潜在商业化路径保持开放**：`summarize-core` 作为独立包发布，提供库级别的 API（`createLinkPreviewClient`），这是一个明确的 B2B 嵌入信号。如果未来做 SaaS，核心提取和提示词模块已经解耦。
- **生态枢纽角色**：通过 OpenRouter 免费模型预设（`refresh-free`）降低使用门槛，将 LLM 提供商竞争转化为自身优势。

## 架构与设计决策

### 目录结构概览

```
steipete/summarize
├── packages/core/          # @steipete/summarize-core：纯提取+提示词库，无 CLI 依赖
│   └── src/
│       ├── content/        # URL 分类、链接预览、转录提供商（YouTube/播客/通用）
│       ├── prompts/        # 摘要提示词模板和长度规格
│       ├── transcription/  # Whisper/ONNX 转录引擎
│       └── shared/         # 共享类型合约
├── src/                    # CLI 主包：LLM 调用、缓存、终端 UI、守护进程
│   ├── llm/                # 多提供商 LLM 适配层
│   ├── daemon/             # 本地 HTTP 守护进程（SSE 流式推送）
│   ├── run/                # CLI 执行管线（输入解析→提取→摘要→输出）
│   ├── slides/             # 视频幻灯片提取（场景检测+OCR）
│   ├── tty/                # 终端 UI（主题、进度条、Markdown 渲染）
│   └── config/             # 配置解析和合并
├── apps/chrome-extension/  # 浏览器扩展（Preact + WXT 框架）
│   └── src/entrypoints/
│       ├── sidepanel/      # Side Panel 主 UI（60+ 文件，完整 MVC 架构）
│       ├── background/     # Service Worker
│       └── options/        # 选项页
└── tests/                  # 371 个测试文件，49K 行测试代码
```

分层逻辑：**core（可嵌入库）→ CLI（终端应用）→ daemon（桥接层）→ extension（浏览器前端）**。依赖方向严格单向，core 不知道 CLI 的存在。

### 关键设计决策

1. **决策**: Gateway-Style Model ID 统一寻址
   - 问题: 需要支持 6+ 个 LLM 提供商，每个有不同的模型命名体系，用户不应关心后端差异。
   - 方案: `<provider>/<model>` 格式（如 `google/gemini-3-flash`），加上模型别名自动解析（`grok-4` → `xai/grok-4`）、Anthropic 版本别名映射（`claude-sonnet-4` → `claude-sonnet-4-0`），以及 OpenRouter 的透明回退。
   - Trade-off: 增加了一层抽象和解析逻辑（model-id.ts + provider-profile.ts），但用户只需记住一种格式。失去了对某些提供商专有功能的直接访问。
   - 可迁移性: **高** — 任何需要多 LLM 后端的项目都可以复用这个模式。

2. **决策**: Auto Model Selection with Rule-Based Fallback Chains
   - 问题: 用户可能没有所有提供商的 API Key，需要自动选择最优且可用的模型。
   - 方案: `model-auto-rules.ts` 定义规则矩阵（按内容类型 + token 数量 band 匹配候选列表），运行时按 env 中的 key 可用性、上下文窗口容量、成本估算逐一过滤，生成有序尝试列表。CLI 提供商（claude/codex/gemini/agent）作为额外回退层前置。
   - Trade-off: 复杂度高（model-auto.ts 近 400 行），但实现了"零配置即可用"的核心体验。用户可能不清楚实际使用了哪个模型（通过 `--verbose` 可查看）。
   - 可迁移性: **高** — 规则引擎模式适用于任何多后端选择场景。

3. **决策**: 本地 HTTP 守护进程 + SSE 流式推送桥接浏览器扩展
   - 问题: 浏览器扩展无法执行本地二进制（ffmpeg、yt-dlp、Whisper），也无法进行长时间运算。
   - 方案: 在 `127.0.0.1:8787` 运行 HTTP 守护进程，通过 token 认证、CORS 限制（仅信任 chrome-extension://、moz-extension:// 和 localhost），以 SSE 流式推送摘要进度和结果。守护进程通过 launchd/systemd/Scheduled Task 自启动。
   - Trade-off: 增加了安装步骤和系统集成复杂度（跨平台服务管理），但让浏览器扩展获得了原生应用级能力。纯 HTTP（无 WebSocket）简化了实现且 SSE 天然支持重连。
   - 可迁移性: **高** — "本地守护进程桥接浏览器扩展"模式可复用于任何需要本地工具链的浏览器扩展。

4. **决策**: SQLite 缓存（支持 Node.js 和 Bun 双运行时）
   - 问题: 需要持久化缓存提取结果、转录、摘要，避免重复 LLM 调用和媒体下载。
   - 方案: 使用 `node:sqlite`（Node 22+ 实验性）和 `bun:sqlite` 的运行时检测，WAL 模式 + 增量清理 + LRU 淘汰，按 kind（extract/summary/transcript/chat/slides）分类存储。
   - Trade-off: 依赖 Node.js 实验性 API（需要抑制 ExperimentalWarning），但避免了引入额外的原生依赖（如 better-sqlite3）。SQLite 比文件系统缓存更可靠且支持原子操作。
   - 可迁移性: **中** — 模式可复用，但 Node.js SQLite API 稳定性仍需观察。

5. **决策**: Monorepo 分包：core 与 CLI 解耦
   - 问题: 第三方开发者可能只需要内容提取和提示词模块，不需要 CLI 的终端 UI 和大量依赖。
   - 方案: `@steipete/summarize-core` 仅包含内容提取（link-preview、transcript）、提示词模板和共享类型，依赖轻量（cheerio、jsdom、readability）。CLI 包依赖 core 并增加 LLM 调用、缓存、终端 UI。
   - Trade-off: 增加了发布和版本管理复杂度（lockstep 版本、发布顺序），但实现了清晰的 API 边界。
   - 可迁移性: **高** — monorepo + workspace 分包是成熟模式。

## 创新点

1. **多层转录回退链**
   - 描述: YouTube 转录支持 6 层回退（youtubei API → captionTracks → Apify → yt-dlp+本地 Whisper → yt-dlp+云端转录[Groq→AssemblyAI→Gemini→OpenAI→FAL]），播客支持 RSS transcript → Whisper 回退。每层失败自动降级，对用户透明。
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 4/5
   - 适用场景: 任何需要可靠获取媒体内容文本的应用。

2. **视频幻灯片提取与 OCR 对齐**
   - 描述: 通过 ffmpeg 场景检测（`showinfo` 过滤器）+ 自适应阈值校准 + 最小间隔过滤，从视频中提取关键帧作为"幻灯片"。可选 Tesseract OCR，OCR 结果与转录时间戳对齐，在终端内联渲染图片（支持 iTerm/Kitty/WezTerm 协议）。
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 3/5
   - 适用场景: 教育/会议视频分析、技术演讲笔记生成。

3. **`refresh-free` 动态免费模型发现**
   - 描述: 自动从 OpenRouter `/models` API 发现 `:free` 模型，过滤小模型（<27B），并发测试响应质量和延迟，挑选"聪明+快速"组合写入配置。用户可零成本使用 LLM 摘要。
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 4/5
   - 适用场景: 任何使用 OpenRouter 的 LLM 应用可以复用此模式发现最优免费模型。

4. **本地守护进程 + 浏览器扩展 SSE 架构**
   - 描述: 将重计算卸载到本地进程，浏览器扩展变成轻量 SSE 消费者。支持会话复用（新客户端连接时回放缓冲区）、keepalive 心跳、跨平台自启动。
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 5/5
   - 适用场景: 任何需要本地工具链支持的浏览器扩展（翻译、代码分析、媒体处理等）。

5. **LiteLLM 目录集成的智能模型选择**
   - 描述: 使用 LiteLLM 开源模型目录（缓存在本地）进行运行时 token 限制检查和成本估算，在摘要开始前就预判模型是否能处理当前内容量，并在候选列表中跳过容量不足的模型。
   - 新颖度: 3/5 | 实用性: 4/5 | 可迁移性: 4/5
   - 适用场景: 多模型 LLM 应用的 preflight 检查。

## 可复用模式

1. **Gateway-Style Provider Routing**: 统一 `<provider>/<model>` 寻址 + 别名映射 + 自动回退链 — 适用于: 任何多 LLM 后端应用
2. **Cascading Fallback Chain**: 多层服务降级（转录、模型选择、网页提取），每层独立失败隔离 — 适用于: 依赖外部 API 的可靠性关键路径
3. **Local Daemon Bridge**: 本地 HTTP 服务 + SSE + token 认证 + 跨平台自启动 — 适用于: 浏览器扩展需要本地能力的场景
4. **Runtime-Detected SQLite Cache**: Node.js/Bun 双运行时自动检测 + WAL 模式 + LRU 淘汰 — 适用于: 需要轻量持久化缓存的 CLI 工具
5. **Dynamic Free Model Discovery**: API 驱动的模型发现 + 并发健康检查 + 质量/速度平衡选择 — 适用于: OpenRouter 或类似聚合平台的消费者应用
6. **Monorepo Core/CLI 分包**: 提取层作为独立轻量包，CLI 层增加 UX 依赖 — 适用于: 同时需要库 API 和 CLI 的 Node.js 项目

## 竞品交叉分析

### vs Jina Reader

- **我们更好**: Jina Reader 只做 URL→文本提取，Summarize 在提取之上加了 LLM 摘要、视频/音频转录、幻灯片提取、浏览器扩展。Summarize 支持本地文件和 stdin 输入。
- **竞品更好**: Jina Reader 的网页提取更专业（JavaScript 渲染、反爬虫绕过），部署为云端服务延迟更低，且有专门的 embedding 服务。
- **不同目标**: Jina 面向 RAG 管线的工程团队（嵌入式服务），Summarize 面向终端用户的信息消费场景（CLI + 浏览器）。
- **用户迁移成本**: Summarize 可以将 Jina 作为 `--firecrawl` 的替代方案接入（目前未直接集成），迁移成本低。

### vs Firecrawl

- **我们更好**: Firecrawl 主要做网页爬取和提取（SaaS），不支持视频/音频/播客/本地文件，不做 AI 摘要。Summarize 的 Firecrawl 集成是可选回退（`--firecrawl auto`），把 Firecrawl 变成了自己的供应商。
- **竞品更好**: Firecrawl 的 JavaScript 渲染和反反爬能力更强，支持批量爬取和结构化提取，有完整的 REST API 和多语言 SDK。
- **不同目标**: Firecrawl 面向需要大规模网页数据的开发团队，Summarize 面向单 URL 级别的内容消费。
- **用户迁移成本**: 两者不直接竞争。Summarize 实际上是 Firecrawl 的下游消费者。

### vs ChatGPT/Claude Web UI 摘要

- **我们更好**: 开源、可本地运行、支持 CLI 自动化/管道化、多模型切换、缓存避免重复调用、成本可控（包括零成本免费模型路径）。隐私性更好（本地提取，只发送文本到 LLM）。
- **竞品更好**: ChatGPT/Claude 的 UI 更友好、上下文记忆更强、支持多轮深度对话、无需安装。
- **不同目标**: ChatGPT/Claude 是通用对话 AI，Summarize 是专注于"给我一个 URL 的快速摘要"的精确工具。
- **用户迁移成本**: 极低——Summarize 本身调用这些模型的 API，是互补而非替代。

### 综合竞争结论

- **差异化护城河**: **架构护城河**（CLI + 守护进程 + 浏览器扩展的完整链路，新进者难以快速复制）+ **生态护城河**（同时支持 6 个 LLM 提供商 + OpenRouter + 4 个 CLI 后端 + 6 个转录服务的集成广度）+ **信任护城河**（Peter Steinberger 的开发者影响力 + MIT 开源 + npm 14K 周下载量建立的社区信任）。
- **竞争风险**: 最大风险来自 **LLM 提供商自身的内置摘要功能**（如 Google Gemini 的"Summarize this page"、OpenAI 的 ChatGPT 插件）。如果主流浏览器或 AI 助手内置了一键摘要，Summarize 的浏览器扩展价值会下降。CLI 和库的价值相对稳固。
- **生态定位**: 在 "原始内容 → 结构化文本 → AI 摘要" 管线中，Summarize 占据了"最后一公里"的全栈位置。上游依赖提取工具（Readability、Cheerio、Firecrawl），下游对接 LLM API。核心竞争力是把这条管线做到足够稳健和易用。

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | 优秀 | TypeScript 严格模式，类型安全贯穿全项目。Provider profile 用 Record 类型保证完备性。错误处理精细（区分 AbortError/TimeoutError/API Error，带重试逻辑）。33K 行 src + 13K 行 core，代码组织清晰。 |
| 文档质量 | 优秀 | 4672 行 Markdown 文档。docs/ 下 30 个专题文档覆盖各子系统。RELEASING.md 详细到每条命令。README 非常完整（724 行）。有 Jekyll 文档站点。 |
| 测试覆盖 | 充分 | 371 个测试文件，49K 行测试代码（约为 src 代码量的 1.5 倍）。覆盖率阈值 75%（branches/functions/lines/statements）。包含单元测试、集成测试和 E2E 测试（Playwright）。有 live 测试（真实 API 调用）。 |
| CI/CD | 完善 | GitHub Actions CI 支持 Node 22/24 矩阵测试。流程包含 lint → test:coverage → build → pack 验证。有 GitHub Pages 部署。完整的发布脚本（npm + Homebrew + GitHub Release + Chrome/Firefox 扩展）。 |
| 错误处理 | 规范 | 多层错误处理：AbortController 超时、重试逻辑（指数退避）、provider 特定错误映射（Anthropic 模型访问错误、Google 空响应回退）、EPIPE 安全退出、ANSI 剥离后的友好错误消息。 |

### 质量检查清单

- [x] 有测试（单元/集成/E2E）— 371 文件，vitest + Playwright
- [x] 有 CI/CD 配置 — GitHub Actions，Node 22/24 矩阵
- [x] 有文档（不仅是 README）— docs/ 下 30 个专题文档 + Jekyll 站点
- [x] 错误处理规范 — 超时重试、provider 错误映射、友好消息
- [x] 有 linter / formatter 配置 — oxlint（type-aware）+ oxfmt
- [x] 有 CHANGELOG — 37K 字符，逐版本详细记录
- [x] 有 LICENSE — MIT
- [ ] 有示例代码 / examples 目录 — README 中有大量用例，但无独立 examples 目录
- [x] 依赖版本锁定（lock file）— pnpm-lock.yaml（248K）
