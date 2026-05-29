## 动机与定位

- **要解决的问题**: AI Agent 桌面协作的碎片化 -- 用户需要在多个 CLI Agent（Claude Code、Codex、Gemini CLI 等）之间切换，缺乏统一的 GUI 界面；同时 Claude Cowork 等商业产品仅支持 macOS + 单一模型 + 高昂月费（$100），普通用户和中小团队无法负担。
- **为什么现有方案不够**: (1) Claude Cowork 仅 macOS、仅 Claude、$100/月，锁死生态；(2) LibreChat 等开源方案侧重聊天而非桌面 Agent 自动化；(3) CLI Agent 没有文件预览、定时任务、远程访问等桌面级体验；(4) 各 Agent 的 MCP 工具需要重复配置。
- **目标用户**: 需要 AI 辅助日常办公的个人用户和小团队，尤其是中国开发者与非技术用户（"让普通人像用 APP 一样使用 Claude Code"）。

## 作者视角

### 问题发现
iOfficeAI 团队从"智能办公"（Smart Office. Simple AI.）的视角切入，发现了一个被行业忽视的缝隙：AI Agent 工具都在追求"更强的 Agent 能力"，但没有人关注"如何让普通人无门槛地使用这些 Agent"。Anthropic 推出 Claude Cowork 验证了"桌面 AI Agent"的市场需求，但其封闭性和高价格留下了巨大的开源替代空间。

### 解法哲学
**"Cowork 平台"而非"又一个聊天客户端"**：AionUi 的核心哲学是将自身定位为"Agent 协作平台"，而非简单的 AI 对话界面。这体现在三个层面：
1. **内置 Agent 引擎** -- 开箱即用，零配置，降低入门门槛
2. **多 Agent 统一管理** -- 自动检测已安装的 CLI Agent，统一接口和 MCP 配置
3. **远程可达** -- 通过 WebUI / Telegram / 飞书 / 钉钉将 Agent 能力延伸到手机端

### 背景知识迁移
团队将多个领域的知识融入设计：
- **VSCode/Figma 的扩展系统理念** -- 扩展系统的 manifest 校验、API 版本兼容性检查、沙箱隔离等设计直接借鉴了 Figma 的 iframe 沙箱和 VSCode 的 contributes 模式
- **企业 IM 集成经验** -- 飞书互动卡片、钉钉 AI Card 流式更新、Telegram 内联键盘等深度集成，反映团队在企业办公场景的积累
- **Electron 桌面应用工程** -- 成熟的多进程架构、IPC 桥接、fork worker 隔离等

### 战略图景
短期看是"Claude Cowork 开源替代"，中期目标是"AI Agent 桌面操作系统"：
- 扩展系统支持 ACP Adapter、Channel Plugin、MCP Server、Assistant、Skill、Theme、Model Provider、Settings Tab、WebUI 贡献共 10 种扩展点
- OpenClaw Gateway 集成暗示了与更大 Agent 生态的对接意图
- 定时任务（Cron）和远程访问使其从"人机对话"进化为"24/7 无人值守 Agent"

## 架构与设计决策

### 目录结构概览

```
src/
├── index.ts              # Electron 主进程入口 (636行)，应用生命周期管理
├── preload.ts            # Electron contextBridge，暴露安全 IPC API
├── types.d.ts            # 全局类型声明
│
├── common/               # 跨进程共享代码
│   ├── adapter/          # IPC 桥接核心 (ipcBridge.ts 是最核心文件)
│   │   ├── ipcBridge.ts  # 定义所有 IPC 通道的类型化接口
│   │   ├── main.ts       # 主进程端适配器：IPC + WebSocket 双路广播
│   │   └── browser.ts    # 渲染进程端适配器
│   ├── api/              # 多模型 API 客户端（协议转换层）
│   ├── chat/             # 聊天协议、消息类型、斜杠命令
│   ├── config/           # 配置、存储、常量、预设
│   ├── types/            # 共享类型（ACP/Codex/数据库等）
│   └── utils/            # 通用工具函数
│
├── process/              # 主进程代码
│   ├── agent/            # Agent 系统（核心）
│   │   ├── acp/          # ACP 协议适配器（CLI Agent 统一接入）
│   │   ├── codex/        # OpenAI Codex Agent 深度集成
│   │   ├── gemini/       # Gemini 内置 Agent 引擎
│   │   ├── openclaw/     # OpenClaw Gateway WebSocket 连接
│   │   └── nanobot/      # NanoBot Agent 适配
│   ├── bridge/           # IPC Bridge 处理器（30个文件，每个对应一个功能域）
│   ├── channels/         # 远程通道系统（Telegram/飞书/钉钉）
│   ├── extensions/       # 扩展系统（加载器/注册表/生命周期/沙箱/解析器）
│   ├── resources/        # 内置资源（12个 Assistant + 14个 Skill）
│   ├── services/         # 服务层（数据库/Cron/i18n/MCP）
│   ├── task/             # Agent 任务管理（WorkerTaskManager/AgentFactory）
│   ├── webserver/        # WebUI 服务器（Express + WebSocket + JWT 认证）
│   ├── worker/           # Worker 进程（gemini/acp/codex/nanobot/openclaw）
│   └── utils/            # 主进程工具（托盘/菜单/缩放/深度链接等）
│
└── renderer/             # 渲染进程代码（React UI）
    ├── components/       # UI 组件（agent/base/chat/layout/settings/media/Markdown）
    ├── hooks/            # React Hooks（agent/assistant/chat/context/file/mcp/system/ui）
    ├── pages/            # 页面（conversation/cron/guid/login/settings）
    ├── services/         # 前端服务（i18n 国际化）
    ├── styles/           # 样式和主题
    └── utils/            # 前端工具（chat/file/model/theme/ui/workspace）
```

**规模统计**：713 个源文件（.ts/.tsx），138,449 行代码，99 个测试文件。

### 关键设计决策

**1. 三进程隔离架构**
- Main Process：业务逻辑、数据库（SQLite via better-sqlite3）、IPC 处理
- Renderer Process：React 19 UI，不可直接访问 Node.js API
- Worker Processes：通过 fork 机制隔离 Agent 执行，每种 Agent 独立 worker（gemini.ts、acp.ts、codex.ts 等）
- 通信统一通过 `@office-ai/platform` 的 bridge 抽象，在 `ipcBridge.ts` 中定义全部类型化通道

**2. Agent 系统：双轨设计**
- **内置 Agent 引擎**（Gemini）：直接调用 `@google/genai` SDK，内置工具系统（文件操作、Web搜索、图片生成），支持 Google OAuth 登录免费使用
- **外部 Agent 管理**（ACP 协议）：通过 `AcpDetector` 自动检测已安装的 CLI Agent（Claude Code、Codex、Qwen Code 等 16+种），通过 `AcpAdapter` 统一消息格式，`AcpConnection` 管理子进程生命周期
- **AgentFactory + WorkerTaskManager**：工厂模式创建 Agent 实例，统一的任务管理器控制并发和生命周期

**3. IPC Bridge 分域设计**
Bridge 按功能域拆分为 30 个独立文件（conversationBridge、geminiBridge、channelBridge、mcpBridge、cronBridge 等），每个文件注册该域的 Provider（请求-响应）和 Emitter（事件推送）。`ipcBridge.ts` 作为类型定义中心，被修改 141 次是因为每个新功能都需要在此注册通道。

**4. 远程通道系统（Channels）**
采用分层插件架构：
- Plugin Layer：平台适配（Telegram/飞书/钉钉各有独立 Plugin + Adapter）
- Gateway Layer：统一消息路由（PluginManager + ActionExecutor）
- Core Layer：会话管理（SessionManager，per-chat 隔离）+ 配对授权（PairingService，6位数字码）
- Agent Layer：事件总线（ChannelEventBus）+ 消息服务（ChannelMessageService）
- 关键特性：统一消息协议（IUnifiedIncomingMessage / IUnifiedOutgoingMessage）、500ms 节流流式更新、Agent 双路广播（IPC + EventBus 并行）

**5. 扩展系统：VSCode + Figma 混合模式**
- Manifest 声明式注册（`aion-extension.json`），支持 Zod 严格校验
- 10 种 Contribution 类型：ACP Adapter、MCP Server、Assistant、Agent、Skill、Channel Plugin、Theme、Settings Tab、WebUI（API/WS/中间件/静态资源）、Model Provider
- 生命周期钩子：onInstall / onActivate / onDeactivate / onUninstall
- 沙箱隔离：Worker Thread 隔离执行、Permission 声明（storage/network/shell/filesystem/clipboard/activeUser/events）
- 引擎兼容性检查 + 依赖拓扑排序 + 热重载

**6. 多模型协议转换**
`common/api/` 实现了 ProtocolConverter 抽象：
- `OpenAI2GeminiConverter`：OpenAI 格式请求转 Gemini API
- `OpenAI2AnthropicConverter`：OpenAI 格式请求转 Anthropic API
- `RotatingApiClient`：API Key 轮换（多 Key 负载均衡 + 自动重试）
- `ApiKeyManager`：密钥管理，支持逗号分隔多 Key

**7. 流式消息优化**
`StreamingMessageBuffer` 将数据库写入从"每 chunk 一次 UPDATE"优化为"300ms 或 20 chunk 批量写入"，性能提升约 100 倍。

## 创新点

1. **Agent 协作平台范式** -- 不是做"又一个 AI 聊天框"，而是做"Agent 桌面操作系统"。将多个独立 CLI Agent 统一到一个 GUI 下协同工作，这种"Cowork"范式在开源领域首创。

2. **MCP 统一管理** -- 用户只需在 AionUi 中配置一次 MCP Server，所有 Agent（Claude Code、Codex、Gemini 等）自动同步使用，解决了各 Agent 独立配置 MCP 的痛点。通过 `mcpServices/agents/` 下的 per-agent 适配器实现。

3. **Agent 双路广播机制** -- Agent 消息同时通过 IPC（桌面 UI）和 ChannelEventBus（远程 IM）双路分发，桌面端和移动端实时同步，互不干扰。

4. **统一消息协议 + 三级降级策略** -- Channels 系统通过统一的 `IUnifiedIncomingMessage / IUnifiedOutgoingMessage` 屏蔽平台差异；钉钉插件实现了 AI Card -> sessionWebhook -> Open API 三级降级。

5. **扩展系统沙箱隔离** -- 借鉴 Figma iframe 沙箱模型，用 Worker Thread 隔离扩展代码执行，通过结构化消息传递（SandboxMessage 协议）实现主进程与沙箱的安全通信。

6. **内置 Skill 系统** -- 通过 Markdown 文件定义 Skill（如 pptx/docx/xlsx/pdf），Agent 可以 `activate_skill` 动态加载能力文档。Skill 与 Assistant 的组合机制允许灵活构建领域专家。

## 可复用模式

1. **IPC Bridge 类型化分域模式** -- 使用 `bridge.buildProvider<Response, Params>(channel)` 和 `bridge.buildEmitter<Event>(channel)` 构建类型安全的 IPC 通道。按功能域拆分文件（30 个 bridge 文件），每个域独立注册。适用于任何 Electron 多进程应用。

2. **Agent 工厂 + 检测器模式** -- `AgentFactory` 注册创建函数 + `AcpDetector` 自动检测环境中的 CLI 工具。检测逻辑（`execSync` 检查 CLI 存在性）和工厂注册分离，易于扩展新 Agent。

3. **统一消息协议模式** -- `IUnifiedIncomingMessage / IUnifiedOutgoingMessage` 解耦平台差异，BasePlugin 抽象类定义生命周期状态机（created -> initializing -> ready -> starting -> running -> stopping -> stopped），适用于任何多平台消息集成场景。

4. **流式消息缓冲模式** -- `StreamingMessageBuffer` 的定期批量写入策略（300ms 间隔 / 20 chunk 阈值），通用于任何需要持久化流式数据的场景。

5. **协议转换器模式** -- `ProtocolConverter<TInput, TOutput, TResponse>` 抽象 + `RotatingApiClient` 的 Key 轮换机制，适用于多 LLM 提供商集成。

6. **扩展 Manifest 声明式注册** -- 类似 VSCode 的 `contributes` 机制，通过 Zod Schema 校验 manifest，支持依赖检查 + 引擎兼容性 + 拓扑排序。10 种 contribution 类型覆盖了桌面 AI 应用的全部扩展点。

## 竞品交叉分析

| 维度 | AionUi | Claude Cowork | OpenWork | Eigent AI | LibreChat | OpenClaw |
|:-----|:-------|:-------------|:---------|:---------|:---------|:--------|
| **定位** | Multi-Agent Cowork 平台 | macOS 桌面 AI Agent | 开源 Cowork 替代 | 本地多 Agent 并行 | AI 聊天平台 | CLI Agent 生态 |
| **开源** | Apache-2.0 | 闭源 | 开源 | 开源 | MIT | 开源 |
| **平台** | macOS/Windows/Linux | 仅 macOS | macOS | 跨平台 | Web | CLI |
| **模型** | 20+ 平台 | 仅 Claude | 多模型 | 多模型 | 多模型 | 多模型 |
| **内置 Agent** | Gemini 引擎，零配置 | Claude Agent | 依赖外部 | 依赖外部 | 无 Agent | CLI Agent |
| **多 Agent** | 16+ 种自动检测 | 无 | 有限 | 核心特性 | 无 | 核心特性 |
| **远程访问** | WebUI + Telegram + 飞书 + 钉钉 | 无 | 无 | 无 | Web 原生 | 无 |
| **定时任务** | Cron 系统 | 无 | 无 | 无 | 无 | 无 |
| **扩展系统** | 10 种扩展点 + 沙箱 | 无 | 有限 | 无 | 插件系统 | 扩展系统 |
| **办公能力** | PPT/Word/Excel/PDF 生成 | 文件操作 | 文件操作 | 文件操作 | 无 | 文件操作 |

**差异化优势**：
- vs Claude Cowork：跨平台 + 多模型 + 免费 + 远程访问 + 定时任务
- vs OpenWork/Eigent AI：更完善的远程通道集成（IM 平台深度对接）和扩展生态
- vs LibreChat：桌面 Agent 能力（文件操作/自动化）而非纯聊天
- vs OpenClaw：GUI 桌面体验 + 办公文档处理 + IM 远程集成

**潜在威胁**：OpenClaw 的快速增长（10万+ Star）可能在 Agent 引擎层面构成竞争。AionUi 通过集成 OpenClaw Gateway（`openclaw/` 目录）的策略是明智的"化竞为友"。

## 代码质量

| 维度 | 评级 | 说明 |
|:-----|:-----|:-----|
| 类型安全 | A | TypeScript 严格模式，Zod 运行时校验，无 `any`（oxlint 规则），路径别名 |
| 代码规范 | A | Oxlint + Oxfmt（Rust 高性能工具链），lint-staged + Husky pre-commit |
| 测试覆盖 | B- | 99 个测试文件，Vitest 4 + Playwright E2E，但 coverage threshold 为 0（informational），实际覆盖率可能偏低 |
| CI/CD | A | 7 个 GitHub Workflows：PR 检查（code quality + build test）、构建发布、Homebrew 更新、GPT PR 评审 |
| 文档质量 | A- | CLAUDE.md + AGENTS.md 提供 AI Agent 开发指引，Skills 索引清晰，内部 ARCHITECTURE.md 详细，但用户文档依赖 GitHub Wiki |
| 架构清晰度 | A | 三进程严格隔离，Bridge 分域设计，扩展系统层次分明，命名规范一致 |
| 依赖管理 | B+ | 依赖数量较多（136 个 dependencies），但有 resolutions/overrides 管理冲突，engines 锁定 Node 22-24 |
| 安全性 | B+ | JWT 认证、CSRF 保护、Rate Limiting、沙箱隔离、路径遍历检查；凭据仅 Base64 编码而非加密 |
| 国际化 | A | i18next + 8 种语言，i18n 类型自动生成，扩展系统支持 i18n 贡献 |
| 性能优化 | A- | 流式消息缓冲（100x 提升）、500ms 节流、Worker 进程隔离、Sentry 监控 |

### 质量检查清单

- [x] TypeScript 严格模式 + 路径别名
- [x] Linter (Oxlint) + Formatter (Oxfmt) + pre-commit hooks
- [x] 单元测试 (Vitest) + DOM 测试 (jsdom) + E2E 测试 (Playwright)
- [x] CI/CD 自动化（PR checks + build + release）
- [x] GPT 辅助代码审查 (gpt-pr-assessment.yml)
- [x] Codecov 集成（但 threshold 为 informational）
- [x] Sentry 错误监控
- [x] 安全中间件（CSRF / Rate Limit / JWT）
- [x] 扩展沙箱隔离（Worker Thread）
- [x] Apache-2.0 许可证 + SPDX 文件头
- [ ] Coverage threshold 实际为 0，未强制执行
- [ ] 凭据存储使用 Base64 而非真正加密
- [ ] `src/index.ts` 636 行，入口文件偏大（可进一步拆分）
