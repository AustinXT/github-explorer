# OpenCode 内容分析报告（Phase 3：What & How）

> 仓库：[anomalyco/opencode](https://github.com/anomalyco/opencode)
> 分析时间：2026-03-22
> 版本：v1.2.27

---

## 3.1 动机与定位

### 核心价值主张

"The open source AI coding agent" —— 一个开源、供应商中立、隐私优先的终端 AI 编码代理。

### 与 Claude Code 的差异化叙事（来自 README FAQ）

| 维度 | OpenCode | Claude Code |
|------|---------|-------------|
| 开源 | 100% 开源 MIT | 商业闭源 |
| LLM 锁定 | 供应商中立，支持 20+ 提供商 | 仅 Anthropic |
| LSP 支持 | 开箱即用，内置 30+ 语言服务器 | 无原生 LSP |
| UI 哲学 | TUI 优先，由 neovim 用户和 terminal.shop 创作者打造 | 终端工具 |
| 架构 | Client/Server 分离，支持远程驱动 | 单体 CLI |
| 桌面端 | Tauri 桌面应用（BETA） | 无 |

### 安装覆盖面

覆盖了所有主流包管理器：npm/bun/pnpm/yarn、Homebrew、Scoop/Choco、pacman/AUR、mise、Nix，还提供一键 curl 安装脚本。README 翻译为 21 种语言，显示出全球化雄心。

---

## 3.2 作者视角价值分析

### 为什么 Anomaly（前 SST）做这个项目？

1. **SST 到 Anomaly 的战略转型**：团队从 Serverless 基础设施转向 AI 开发工具，OpenCode 是核心赌注产品
2. **商业模式**：开源核心 + "OpenCode Zen" 付费 LLM 代理（models.dev 中 opencode 提供商），免费用户可使用免费模型（`apiKey: "public"`）
3. **生态控制点**：通过 models.dev 控制模型定义标准，通过插件/技能系统构建生态
4. **技术品味信号**：AGENTS.md 中的代码风格指南极其严格（单词命名、禁止解构、禁止 else），体现了团队的工程审美

### 增长数据

STATS.md 记录了精确的下载量增长：
- 2025-06-29 起步日下载 58,209
- 2025-09-02 达到 487,558 累计下载
- 日均增长约 6,500-10,000 次
- 增长曲线稳定上升，未见衰减

---

## 3.3 架构与设计决策

### Monorepo 结构（19 个包）

```
packages/
├── opencode/        # 核心引擎（270 个 TS 源文件，37,098 行）
├── app/             # Web 前端（SolidJS）
├── console/         # 控制台管理界面
├── desktop/         # Tauri 桌面应用
├── desktop-electron/ # Electron 桌面版
├── sdk/             # TypeScript SDK（自动生成）
├── ui/              # 共享 UI 组件库
├── web/             # 官网/文档
├── plugin/          # 插件类型定义
├── util/            # 共享工具库
├── function/        # Serverless 函数
├── identity/        # 身份认证
├── enterprise/      # 企业版
├── containers/      # 容器化
├── extensions/      # 扩展
├── storybook/       # UI 组件文档
├── script/          # 构建脚本
├── slack/           # Slack 集成
└── docs/            # 文档站
sdks/
└── vscode/          # VS Code 扩展
```

### 核心引擎架构（packages/opencode/src/）

```
src/
├── agent/           # 代理定义与管理（build/plan/general/explore/compaction/title/summary）
├── provider/        # LLM 提供商抽象（20+ 提供商）
├── session/         # 会话管理、消息处理、流式推理、压缩
├── tool/            # 内置工具（17 个：bash/read/edit/write/glob/grep/task 等）
├── server/          # HTTP API 服务器（Hono 框架）
├── cli/             # CLI 入口（yargs + 20+ 子命令）
├── mcp/             # Model Context Protocol 客户端
├── lsp/             # LSP 客户端（30+ 内置语言服务器）
├── config/          # 分层配置系统（managed > project > global > remote）
├── permission/      # 精细权限控制系统
├── plugin/          # 插件加载与钩子
├── skill/           # 技能系统（SKILL.md 发现机制）
├── snapshot/        # Git 快照（Effect 层实现，用于变更追踪和回滚）
├── storage/         # SQLite 持久化（Drizzle ORM）
├── acp/             # Agent Client Protocol 支持（Zed 编辑器集成）
├── bus/             # 事件总线
├── effect/          # Effect 库集成层
├── worktree/        # Git Worktree 管理
├── format/          # 代码格式化（Effect 层）
├── patch/           # 补丁应用
├── pty/             # 伪终端
├── share/           # 会话分享
├── shell/           # Shell 集成
├── file/            # 文件操作
└── filesystem/      # 文件系统抽象
```

### 关键设计决策

#### 1. AI SDK 作为 LLM 统一层

使用 Vercel 的 `ai` SDK（v5.0.124）作为所有 LLM 交互的统一抽象层。这是一个关键决策：
- `provider.ts` 中硬编码了 16 个 bundled providers 的工厂函数映射
- 每个提供商通过 `CUSTOM_LOADERS` 定制特殊行为（如 Anthropic 的 interleaved-thinking，OpenAI 的 responses API）
- 模型元数据从 `models.dev` 获取（自有服务），支持本地缓存和快照

```typescript
// 20+ 提供商的 SDK 工厂映射
const BUNDLED_PROVIDERS: Record<string, (options: any) => SDK> = {
  "@ai-sdk/anthropic": createAnthropic,
  "@ai-sdk/openai": createOpenAI,
  "@ai-sdk/google": createGoogleGenerativeAI,
  "@ai-sdk/amazon-bedrock": createAmazonBedrock,
  "@ai-sdk/azure": createAzure,
  "@openrouter/ai-sdk-provider": createOpenRouter,
  // ... 16 个提供商
}
```

#### 2. 按模型家族定制 System Prompt

`session/system.ts` 根据模型 ID 选择不同的系统提示词：
- `anthropic.txt` —— Claude 系列（105 行）
- `beast.txt` —— GPT-4/o1/o3（147 行）
- `codex.txt` —— GPT-5 等（79 行）
- `gemini.txt` —— Gemini 系列（155 行）
- `trinity.txt` —— Trinity 系列（97 行）
- `default.txt` —— 其他模型（105 行）

这表明团队对每个模型家族的行为差异有深入理解，针对性优化 prompt。

#### 3. Agent 系统（多角色架构）

内置 7 个代理角色，分为主代理和子代理：

| 代理 | 模式 | 用途 |
|------|------|------|
| build | primary | 默认全权限开发代理 |
| plan | primary | 只读分析模式，禁止编辑 |
| general | subagent | 复杂搜索和多步任务 |
| explore | subagent | 代码库快速探索 |
| compaction | hidden | 上下文压缩 |
| title | hidden | 会话标题生成 |
| summary | hidden | 会话摘要生成 |

权限系统基于 glob 模式匹配，每个代理有独立的权限规则集。

#### 4. Effect 库的渐进式集成

Effect 库未全面替换传统异步模式，而是被用于特定的状态管理和服务化场景：
- `InstanceState`：基于 Effect 的 ScopedCache，按工作目录缓存状态
- `Snapshot`（快照系统）：完全用 Effect 的 Layer/Service 模式实现
- `Format`（格式化）：Effect Service 模式
- 日常业务逻辑仍大量使用 `async/await` 和 Promise

这种"渐进式 effectify"策略务实：在需要生命周期管理和资源清理的场景使用 Effect，其他地方保持简单。

#### 5. Client/Server 分离架构

```
CLI/TUI ──┐
Web App ──┤
Desktop ──┼── HTTP API (Hono) ── 核心引擎
VS Code ──┤
ACP ──────┘
```

- 所有客户端通过 HTTP API 与核心引擎交互
- Hono 框架提供 OpenAPI 规范自动生成
- 支持 mDNS 发现（Bonjour），实现局域网内远程控制
- WebSocket 支持实时通信

#### 6. 精细的权限控制

Permission 系统基于 tool + glob 模式的三级控制（allow/deny/ask）：
```typescript
// 默认权限示例
{
  "*": "allow",
  doom_loop: "ask",           // 循环检测需询问
  read: {
    "*": "allow",
    "*.env": "ask",           // 敏感文件需确认
    "*.env.example": "allow",
  },
}
```

#### 7. SQLite 作为持久化层

使用 Drizzle ORM + SQLite（Bun 原生驱动或 better-sqlite3），存储：
- 会话和消息历史
- 权限审批记录
- 项目配置

包含从 JSON 到 SQLite 的迁移脚本（`json-migration.ts`），带进度条 UI。

---

## 3.4 创新点识别

### 1. 内置 30+ 语言的 LSP 支持（核心差异化）

`lsp/server.ts`（2,093 行）内置了 30+ 种语言的 LSP 服务器定义：
- TypeScript、Deno、Vue、ESLint、Oxlint、Biome
- Go、Rust、Python(Pyright/Ty)、Ruby、Elixir、Zig
- C#、F#、Swift、Java、Kotlin、Dart
- YAML、Lua、PHP、Prisma、Bash、Terraform、LaTeX、OCaml、Svelte、Astro

每个 LSP 服务器都有自动发现机制（检测项目文件决定是否启动）和智能根目录检测。AI 代理可以在编辑后获取 LSP 诊断反馈，形成"编辑-诊断-修复"循环。

### 2. models.dev —— 模型元数据即服务

`models.dev` 是一个独立的模型注册服务（`https://models.dev/api.json`），提供：
- 所有模型的能力矩阵（推理、温度、工具调用、附件支持）
- 成本信息（输入/输出/缓存读写价格）
- 上下文窗口和输出限制
- 多模态能力

贡献新提供商只需向 models.dev 仓库提交 PR，无需修改 opencode 代码。

### 3. 上下文压缩（Compaction）机制

当 token 使用量接近模型上下文限制时，自动触发压缩：
- 使用专用 "compaction" 代理生成压缩摘要
- `prune()` 函数从后向前遍历，保留最近 40K token 的工具调用输出，擦除更早的输出
- 保护特定工具（如 skill）的输出不被裁剪

### 4. 技能系统（SKILL.md 发现）

通过 Markdown 前置元数据定义技能：
- 扫描 `.opencode/skills/`、`.claude/skills/`、`.agents/skills/` 目录
- 每个 SKILL.md 包含名称、描述和完整指令
- 支持运行时动态加载，与 Claude Code 的 slash command 概念类似

### 5. Agent Client Protocol (ACP) 支持

实现了 ACP v1 协议，允许 Zed 等编辑器直接调用 opencode 作为 AI 后端：
```json
{
  "agent_servers": {
    "OpenCode": {
      "command": "opencode",
      "args": ["acp"]
    }
  }
}
```

### 6. 工具调用自动修复

`llm.ts` 中的 `experimental_repairToolCall`：当模型输出的工具名称大小写错误时，自动修复为小写匹配；无法修复则路由到 "invalid" 工具返回错误信息。

### 7. SSE 超时守卫

`provider.ts` 中的 `wrapSSE()` 函数：对流式响应的每个数据块设置超时，防止提供商端卡死导致永久挂起。

---

## 3.5 竞品交叉分析

| 维度 | OpenCode | Claude Code | Aider | Cline | Goose |
|------|---------|-------------|-------|-------|-------|
| 开源 | MIT | 闭源 | Apache-2.0 | Apache-2.0 | Apache-2.0 |
| 语言 | TypeScript | 未知 | Python | TypeScript | Go |
| LLM 支持 | 20+ 提供商 | Anthropic | 多家 | 多家 | 多家 |
| LSP 集成 | 30+ 内置 | 无 | 无 | VS Code 继承 | 无 |
| 界面 | TUI + Web + Desktop | CLI | CLI | VS Code 扩展 | CLI |
| MCP 支持 | 完整客户端 | 完整 | 无 | 有限 | 有 |
| ACP 支持 | 有（Zed） | 无 | 无 | 无 | 无 |
| 架构 | Client/Server | 单体 | 单体 | 扩展 | 单体 |
| 会话压缩 | 自动 | 自动 | 手动 | 无 | 未知 |
| 快照/回滚 | Git 快照 | 有 | Git 集成 | 无 | 无 |

### OpenCode 的独特优势

1. **LSP 集成**是最大差异化：AI 编辑后可立即获取类型检查和 lint 结果，形成闭环
2. **Client/Server 架构**使其成为唯一支持远程驱动的 AI 编码代理（手机控制电脑编码）
3. **供应商中立 + 免费层**（opencode 提供商的免费模型）降低了入门门槛

### OpenCode 的劣势

1. TypeScript + Bun 运行时依赖，相比 Go（Goose）或 Python（Aider）的可移植性略差
2. 商业模式依赖 OpenCode Zen 付费代理，但 models.dev 的开放性可能被竞品利用

---

## 3.6 代码质量评估

### 测试覆盖

- **测试文件数**：118 个测试文件
- **测试代码量**：33,516 行（与源码 37,098 行接近 1:1 比例）
- **测试覆盖范围**：覆盖了所有核心模块（account、acp、agent、auth、cli、config、control-plane、effect、file、filesystem、format、ide、lsp、mcp、memory、patch、permission、plugin、project、provider、pty、question、server、session、share、skill、snapshot、storage、tool、util）
- **测试策略**：AGENTS.md 明确"避免 mock，测试真实实现"

### CI/CD

33 个 GitHub Actions 工作流：
- `test.yml` / `typecheck.yml` —— 测试和类型检查
- `publish.yml` —— 发布流程
- `sign-cli.yml` —— CLI 签名
- `deploy.yml` —— 部署
- `review.yml` —— 代码审查自动化
- `pr-standards.yml` / `pr-management.yml` —— PR 管理
- `daily-issues-recap.yml` / `daily-pr-recap.yml` —— 每日汇总
- `stale-issues.yml` —— 过期 issue 管理
- `nix-eval.yml` / `nix-hashes.yml` —— Nix 构建
- `docs-locale-sync.yml` —— 文档本地化同步

### 代码风格

- Prettier（无分号，120 字符宽度）
- Husky 提交钩子
- 严格的命名规范（单词优先，禁止不必要的驼峰）
- TypeScript 严格模式，使用 `tsgo`（Go 版 TypeScript 编译器预览版）做类型检查

### 架构质量

- **优点**：模块边界清晰，每个模块使用 namespace 封装，通过 Instance.state() 管理生命周期
- **优点**：配置系统层次分明（managed > project > global > remote > well-known）
- **优点**：事件总线解耦各模块通信
- **关注点**：Effect 库的使用不一致——Snapshot 和 Format 完全 Effect 化，其他模块仍是传统异步，过渡期架构存在认知负担
- **关注点**：`provider.ts` 文件较大（480+ 行），provider 特定逻辑分散在 CUSTOM_LOADERS 中

---

## 关键发现总结

### 技术价值最高的三个模块

1. **LSP 集成系统**（`lsp/server.ts` + `lsp/client.ts`）—— 30+ 语言的自动检测和启动，形成 AI 编辑的闭环反馈
2. **Provider 抽象层**（`provider/`）—— 20+ LLM 提供商的统一接入，含 SSE 超时、工具调用修复等鲁棒性设计
3. **Permission 系统**（`permission/`）—— 基于 glob 模式的精细权限控制，支持工具级和文件级粒度

### 可复用的设计模式

1. **Instance.state() 模式**：per-directory 的状态缓存 + 自动清理，适合多工作区场景
2. **models.dev 元数据服务**：将模型能力定义外部化，新模型无需改代码
3. **按模型家族定制 System Prompt**：每个模型系列有独立的 prompt 优化
4. **SKILL.md 发现机制**：Markdown 前置元数据定义能力，文件系统即注册中心

### 风险信号

1. Effect 库的渐进式迁移可能长期拖延，造成两种风格共存的维护负担
2. 对 Bun 运行时的深度依赖（`bun:sqlite`、`Bun.$`、`bun-pty`）限制了可移植性
3. 商业化路径依赖 OpenCode Zen 付费代理，但开源属性使竞品可以 fork 后接入自有 LLM
