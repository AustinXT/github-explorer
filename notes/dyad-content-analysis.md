# Dyad (dyad-sh/dyad) 内容分析报告

## 1. 动机与定位

### 核心叙事
Dyad 的定位极其清晰：做 Lovable / v0 / Bolt.new 的**本地开源替代品**。README 开篇即点明——"like Lovable, v0, or Bolt, but running right on your machine"。这种定位抓住了 AI 应用构建赛道中一个关键空白：云端产品收费高、数据不可控、存在厂商锁定。

### 文档体系分析
项目文档体系非常成熟，远超同类早期项目：

- **`docs/architecture.md`**：高层架构说明，包含 FAQ 解释了关键设计权衡（为何不用真正的 tool calling、为何不更 agentic、为何发送整个代码库）
- **`docs/agent_architecture.md`**：Agent v2 的详细架构文档
- **`AGENTS.md`**：面向 AI Agent 的开发指南（Claude Code / Codex 等可直接读取）
- **`rules/` 目录**：11 个专题规则文件，覆盖 IPC 架构、E2E 测试、Git 工作流、数据库、组件库等
- **`rules/product-principles.md`**：6 条产品设计原则，每条附带"Test"检验标准
- **`plans/` 目录**：未来规划文档，包含 cloud sandboxes、mobile 支持、Convex 后端等
- **`.claude/skills/`**：24 个 Claude Code skill，自动化 lint、PR 审查、E2E 调试等

### 目标用户
双层用户画像：
1. **非技术用户**：通过 AI 对话快速生成全栈 Web 应用，免费入门
2. **开发者**：BYOK（自带 API Key）、代码完全可控、可导出到任何 IDE

---

## 2. 作者视角价值分析

### Will Chen 的技术背景与产品选择的对应关系

**Google Mesop 经验的延续**：Will Chen 在 Google 做 Mesop（Python Web UI 框架，6.5K stars），核心理念是降低 Web 开发门槛。Dyad 是同一理念的 AI 时代升级——从"简化框架"到"AI 直接生成"。

**全栈 Web + AI 工具链的精准结合**：
- 选择 Electron 而非 Web 应用，体现了对"本地运行"价值主张的坚守
- 选择 Vercel AI SDK 作为 LLM 抽象层，而非自建——这是 Google 工程师"不重复造轮"的务实风格
- 选择 SQLite (better-sqlite3) + Drizzle ORM 做本地数据持久化——极简但 production-ready

**Bus Factor = 1 的风险与机遇**：
84.2% 提交来自 Will Chen，但项目文档化程度极高（AGENTS.md、rules/、plans/），说明他有意识地降低 Bus Factor 风险。24 个 Claude Code skill 表明他正在用 AI Agent 扩展自己的产能——这是 solo founder 的现代生存策略。

---

## 3. 架构与设计决策

### 3.1 整体架构

```
Electron App (v40.0.0)
├── Main Process (Node.js)
│   ├── IPC Host (40+ handler 模块)
│   ├── 数据库层 (SQLite + Drizzle ORM)
│   ├── 进程管理器 (子应用运行)
│   ├── Git 操作 (dugite + isomorphic-git)
│   ├── AI Agent 核心 (Vercel AI SDK)
│   └── 外部集成 (Supabase / Neon / Vercel / MCP)
├── Preload (安全 IPC 桥接)
├── Renderer Process (React 19)
│   ├── TanStack Router (路由)
│   ├── TanStack Query (数据获取)
│   ├── Jotai (状态管理)
│   ├── Base UI / shadcn-style 组件
│   └── Monaco Editor / Lexical Editor
└── Worker Processes
    ├── TypeScript 类型检查 Worker
    └── HTTP/WS 代理 Worker (dyad-shim 注入)
```

### 3.2 代码规模
- **574 个源文件** (.ts/.tsx)，约 **97,610 行代码**
- **125 个 E2E 测试文件** (Playwright)
- **20+ 个单元测试文件** (Vitest)
- **20 个数据库迁移文件** (Drizzle)
- 版本号 **v0.40.0**，总计 **1,238 次提交**，全部在 2025 年

### 3.3 IPC 架构（核心设计亮点）

Dyad 最值得学习的架构决策是**契约驱动的 IPC 系统**：

```typescript
// src/ipc/contracts/core.ts 定义了三种 IPC 模式
interface IpcContract    // 请求-响应（invoke/response）
interface EventContract  // 推送事件（main → renderer）
interface StreamContract // 流式传输（chat streaming）
```

关键设计：
- **单一数据源**：所有 channel 名、输入输出 schema（Zod）在 `src/ipc/types/*.ts` 定义
- **自动生成客户端**：`createClient(contracts)` 自动生成类型安全的调用方法
- **自动白名单**：preload 的 channel 白名单从 contracts 自动派生，无需手动维护
- **运行时校验**：`createTypedHandler` 在 handler 层做 Zod 运行时校验

这种模式优雅地解决了 Electron 应用最大的痛点——IPC 的类型安全和可维护性。

### 3.4 AI Agent 架构（双模式设计）

**模式一：Classic Mode（XML 伪工具调用）**
- LLM 返回自定义 XML 标签（`<dyad-write>`, `<dyad-delete>` 等）
- 前端 `DyadMarkdownParser.tsx` 解析并渲染 30+ 种 `<dyad-*>` 标签
- 后端 `response_processor.ts` 执行文件操作
- 优点：单次请求完成多个操作，成本低
- 这一设计直接借鉴了 Lovable/Bolt 等产品的系统提示策略

**模式二：Agent v2（Pro 模式，真正的 Tool Calling）**
- 位于 `src/pro/` 目录（FSL-1.1 许可证）
- 使用 Vercel AI SDK 的 `streamText` + 标准 tool calling
- **25 个工具**：write_file, edit_file, search_replace, grep, code_search, web_search, web_crawl, web_fetch, generate_image, planning_questionnaire, run_type_checks 等
- 每个工具有 `ToolDefinition` 标准接口：name, description, inputSchema (Zod), execute, buildXml, defaultConsent
- 工具执行结果通过 `buildXml()` 转换为 XML 标签，实现与 Classic Mode 相同的 UI 渲染路径
- 支持 consent 机制：ask/always/never 三级权限控制

**关键设计权衡**（来自 `docs/architecture.md`）：
- 为何不更 agentic？**成本控制**。复杂 agent 循环可能单次请求花费数美元
- 为何发送整个代码库？**简单有效**。配合 Smart Context（用小模型预筛文件）
- XML vs Tool Calling？Classic Mode 用 XML 因为可以并行调用且 JSON 中代码质量下降；Agent v2 转向标准 tool calling

### 3.5 代理服务器架构（Preview 核心）

`worker/proxy_server.js` 是一个零依赖的 HTTP/WS 代理 worker：
- 拦截用户应用的 localhost 服务
- **HTML 注入**：在响应中注入 `dyad-shim.js`（导航拦截）、`dyad-logs.js`（日志捕获）、`dyad-component-selector-client.js`（可视化编辑组件选择）等
- 支持 WebSocket 代理（HMR 热更新）
- 实现了应用预览中的错误捕获、导航追踪、截图、可视化编辑等功能

### 3.6 数据库设计

SQLite + Drizzle ORM，关键表：
- **apps**：应用元数据 + 外部集成 ID（GitHub, Supabase, Neon, Vercel）
- **chats**：对话，支持上下文压缩（compaction）
- **messages**：消息，支持 approval_state（approved/rejected）和 AI 消息原始格式存储（aiMessagesJson）
- **prompts**：用户自定义提示词

亮点：上下文压缩（compaction）机制——当对话过长时，用小模型生成摘要替换历史消息，保留 backup 文件可回溯。

### 3.7 依赖选择分析

| 领域 | 选择 | 分析 |
|------|------|------|
| AI SDK | Vercel AI SDK (`ai` v6) | 统一抽象层，支持 8+ LLM 提供商 |
| 前端路由 | TanStack Router | 非 React Router/Next.js，类型安全更好 |
| 数据获取 | TanStack Query | 配合 IPC 使用，缓存和状态管理 |
| 状态管理 | Jotai | 原子化状态，适合 Electron renderer |
| UI 组件 | Base UI (`@base-ui/react`) | 明确禁止 Radix UI，headless 组件 |
| 编辑器 | Monaco Editor | 代码编辑和文件查看 |
| 富文本 | Lexical | 聊天输入框 |
| Git | dugite + isomorphic-git | dugite 提供 bundled git 二进制 |
| 数据库 | better-sqlite3 + Drizzle ORM | 本地持久化，迁移管理 |
| 打包 | Electron Forge | 跨平台打包和签名 |
| 搜索 | @vscode/ripgrep | 借用 VS Code 的 ripgrep 二进制 |
| CSS | Tailwind CSS 4 | 最新版本 |
| Linting | oxlint + oxfmt | 非 ESLint/Prettier，性能更好 |
| TypeScript 检查 | tsgo (TypeScript native preview) | Go 实现的 TS 编译器，更快 |
| 画布 | Konva + react-konva | 可视化编辑 annotator |

---

## 4. 创新点识别

### 4.1 XML Tool Calling 到标准 Tool Calling 的双模式并存
业界罕见的渐进式迁移策略——Classic Mode（免费用户）用 XML 伪工具调用，Pro Mode 用标准 tool calling，但两者共享同一套 UI 渲染路径（通过 `buildXml()` 桥接）。

### 4.2 代理注入式预览架构
不是简单地 iframe 加载 localhost，而是通过 Worker Thread 代理服务器拦截所有 HTTP/WS 流量，动态注入监控脚本（错误捕获、导航拦截、组件选择器、截图客户端）。这使得 Dyad 能在不修改用户代码的情况下实现可视化编辑、实时日志、错误追踪。

### 4.3 Agent Tool Consent 系统
每个工具有 `defaultConsent` 配置，支持三级控制（ask/accept-once/accept-always）。Planning Questionnaire 工具可以向用户提问（支持 text/radio/checkbox），实现交互式需求澄清。

### 4.4 上下文压缩（Compaction）
长对话自动压缩：用小模型生成摘要替换历史消息，支持 mid-turn compaction（在 agent 工具循环中间压缩），备份文件可供 AI 后续搜索。

### 4.5 Turbo File Edit
`edit_file` 工具中引入了 Turbo Edit 模式——主模型只输出"sketched edit"（伪代码级别的编辑意图），再由 Dyad 云端的小模型（`/tools/turbo-file-edit`）精确应用。这降低了主模型的 token 消耗。

### 4.6 AI Agent 自动化开发流程
`.claude/skills/` 包含 24 个 Claude Code skill，覆盖从 lint、PR 审查、E2E 调试到 beta 发布的完整工作流。这是 solo founder 用 AI 放大产能的极致实践。

---

## 5. 可复用模式

### 5.1 契约驱动 IPC 模式
`defineContract` + `createClient` + `createTypedHandler` 三件套，可直接移植到任何 Electron 应用。核心价值：类型安全、自动白名单、运行时校验。

### 5.2 Tool Definition 标准化接口
```typescript
interface ToolDefinition<T> {
  name: string;
  description: string;
  inputSchema: ZodSchema<T>;
  defaultConsent: "always" | "ask";
  modifiesState: boolean;
  execute: (args: T, ctx: AgentContext) => Promise<ToolResult>;
  buildXml: (args: Partial<T>, isComplete: boolean) => string | undefined;
  getConsentPreview: (args: T) => string;
}
```
统一的工具定义接口，使得添加新工具只需创建文件、注册到 `TOOL_DEFINITIONS` 数组。

### 5.3 Scaffold 模式
`scaffold/` 目录包含完整的 Vite + React + shadcn/ui 模板项目，新建应用时复制此模板。模板使用 Radix UI（用户项目），而 Dyad 自身使用 Base UI——清晰区分。

### 5.4 代理注入架构
`worker/proxy_server.js` + 多个客户端注入脚本的组合模式，可用于任何需要在 iframe 中监控/增强第三方 Web 应用的场景。

---

## 6. 竞品交叉分析

| 维度 | Dyad | Bolt.new | Lovable/v0 | Cursor/Windsurf |
|------|------|----------|------------|-----------------|
| 运行位置 | 本地 (Electron) | 浏览器 (WebContainer) | 云端 | 本地 (VS Code fork) |
| 开源 | Apache 2.0 + FSL 1.1 | 开源 | 闭源 | 闭源 |
| 成本 | 免费层 + $20/月 Pro | 免费层 + 付费 | 付费为主 | 付费为主 |
| AI 模式 | XML伪调用 + Tool Calling | WebContainer + AI | 云端 AI | Agentic IDE |
| 代码所有权 | 完全本地 Git | 有限 | 有限 | 完全本地 |
| 数据库支持 | Supabase + Neon | 有限 | 有限 | 无 |
| 部署 | Vercel 集成 | 内置 | 内置 | 无 |
| 可视化编辑 | 有（annotator） | 无 | 有 | 无 |
| MCP 支持 | 有 | 无 | 无 | 有 |

**Dyad 的差异化护城河**：
1. **本地运行 + 开源**：唯一同时满足这两点的 AI 应用构建器
2. **成本意识设计**：整个架构围绕"减少 LLM 调用次数"优化（XML 批量操作、全码库上下文、Turbo Edit）
3. **集成深度**：同时支持 Supabase、Neon、Vercel 和 MCP，从原型到部署全链路
4. **代码可导出**：生成的项目使用标准框架（React/Vite），无 Dyad 特有依赖

**相对弱势**：
1. Bus Factor = 1，社区贡献者数量有限
2. 依赖 Electron 桌面安装，无法像 Bolt.new 那样零安装使用
3. Pro 功能依赖 Dyad 云端引擎（engine.dyad.sh），与"完全本地"定位有一定张力

---

## 7. 代码质量评估

### 7.1 测试覆盖
- **125 个 E2E 测试**（Playwright）：覆盖聊天、应用管理、设置、Agent 工具等核心流程
- **20+ 个单元测试**（Vitest）：覆盖搜索替换处理器、路径安全、Git 工具等
- CI 配置（374 行）支持多平台构建、E2E 分片并行、flakiness 追踪

### 7.2 代码规范
- **Linting**：oxlint（比 ESLint 更快的 Rust 实现）
- **Formatting**：oxfmt（替代 Prettier）
- **类型检查**：tsgo（TypeScript 的 Go 实现预览版），比 tsc 更快
- **Pre-commit hooks**：husky + lint-staged
- **Code Review**：AI 自动审查（Claude PR Review、BugBot）+ 22 个 GitHub Actions workflows

### 7.3 安全实践
- Electron 安全 fuses 全部启用（RunAsNode 禁用、Cookie 加密、ASAR 完整性校验）
- preload 严格白名单校验 IPC channel
- 路径操作全部使用 `safeJoin` 防止目录穿越
- `dyad-media://` 自定义协议有路径遍历防护
- 密钥存储使用 Electron safeStorage 加密
- Agent 工具 consent 系统防止未授权操作

### 7.4 架构健康度
- **优秀**：IPC 契约驱动、工具标准化接口、关注点分离清晰
- **值得注意**：`src/pro/` 与 `src/` 的边界有少量耦合（`chat_stream_handlers.ts` 直接引用 pro 模块），pro 目录中的 import 路径很深（7 层 `../../`）
- **技术债**：Classic Mode 和 Agent v2 并行维护两套 AI 处理逻辑，长期需要收敛

### 7.5 开发者体验
- 丰富的 `rules/` 文档指导贡献者
- `.claude/skills/` 实现 AI 辅助开发工作流
- `plans/` 目录透明化产品路线图
- Storybook 支持组件开发预览
- 强制 CLA 签署（`CLA.md` + GitHub workflow）
