# MCP Apps (ext-apps) 深度分析报告

> GitHub: https://github.com/modelcontextprotocol/ext-apps

## 一句话总结
MCP 协议的首个官方扩展，定义了「AI 对话中嵌入交互式 UI」的行业标准，由 Anthropic 主导并与 OpenAI 联合标准化，已收编主要竞争方案成为事实标准。

## 值得关注的理由
- **AI UI 的行业标准**：首次解决 LLM 工具从「纯文本输出」到「交互式 UI 输出」的跨越，Anthropic + OpenAI 联合背书
- **已收编竞品**：MCP-UI 和 OpenAI Apps SDK 均被纳入统一标准，ChatGPT、Claude、VS Code 等已 Day-1 支持
- **npm 月下载 382 万**：对于诞生不到 5 个月的 SDK 来说极为强劲，实际采用率远超 Star 数所暗示的水平

## 项目展示

![Excalidraw in Claude](https://raw.githubusercontent.com/modelcontextprotocol/ext-apps/main/media/excalidraw.gif)

Excalidraw 作为 MCP App 在 Claude 对话中运行的演示——展示了交互式画布 UI 在 AI 对话流中的内嵌渲染。

![Color Picker Demo](https://raw.githubusercontent.com/modelcontextprotocol/ext-apps/main/media/claude-colorpicker-apps.gif)

Color Picker MCP App 演示——用户在 Claude 对话中直接操作交互式颜色选择器。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/modelcontextprotocol/ext-apps |
| Star / Fork | 1,992 / 248 |
| 代码行数 | 59,700（TypeScript 46.4%, JSON 30.7%, CSS 8.0%） |
| 项目年龄 | 4.5 个月（2025-11-21 创建） |
| 开发阶段 | 快速迭代趋稳（v1.5.0，30 个版本，平均 5 天/版本） |
| 贡献模式 | 小团队主导 + 社区协作（45 位贡献者，Olivier Chafik 占 35%） |
| 热度定位 | 中等热度（2K stars），但 npm 月下载 382 万——工具库典型比例 |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[良好] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
项目由 MCP 官方组织（Anthropic 主导）维护。核心开发者 Olivier Chafik（@ochafik）是 Anthropic Staff SWE，前 Google 工程师，拥有 16 年经验，贡献了 35% 的 commit。规范共同制定者 Ido Salomon（@idosal）是 MCP-UI 创始人、前 Palo Alto Networks 安全工程师。值得注意的是，Claude AI 本身也是贡献者（43 commits）。

### 问题判断
MCP 工具只能返回文本和结构化数据，无法在 AI 对话中嵌入交互式 UI（图表、表单、画布、视频播放器）。社区已自发探索（MCP-UI 项目证明了可行性），但各 Host 各自实现导致碎片化——服务器开发者需为不同 Host 维护不同适配器，安全模型也不一致。时机在于 MCP 协议已被广泛采纳（45K 粉丝的官方组织），UI 需求成为下一个必须解决的瓶颈。

### 解法哲学
「协议优先，收编而非竞争」——不重新发明轮子，而是将 MCP-UI 和 OpenAI Apps SDK 的最佳实践提炼为正式的 MCP 扩展规范（SEP-1865）。核心原则：
1. **重用 MCP 基础设施**：不另起协议，直接在 JSON-RPC 2.0 上扩展 `ui/` 命名空间方法
2. **安全默认值**：所有 CSP 和沙箱配置默认为最严格策略（`default-src 'none'`）
3. **渐进增强**：Host 不支持 UI 时工具照常以纯文本工作，零破坏性
4. **框架无关**：核心 SDK 零框架依赖，React/Vue/Svelte/Solid/Preact/Vanilla JS 均支持

### 战略意图
这是 Anthropic 与 OpenAI **罕见的联合标准化**行为。通过将 MCP-UI 和 Apps SDK 收编为同一规范，MCP Apps 成为 AI UI 交互的事实标准。Day-1 即有 Claude、ChatGPT、VS Code、Goose、Postman 等客户端支持，两周内超过 75 个应用上线 Claude。长期来看，MCP Apps 占据的是「AI 交互范式从文本到图形界面」这一历史性转变的基础设施位置。

## 核心价值提炼

### 创新之处

1. **`ui://` 协议方案 + 工具元数据绑定**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   将 UI 资源声明为 MCP 资源（`ui://` URI scheme），通过 `_meta.ui.resourceUri` 在工具定义中引用。Host 在连接时即可发现、预取、审查所有 UI 模板。解耦了 UI 模板（静态）和工具数据（动态），支持缓存和预加载。

2. **声明式 CSP + 权限协商**（新颖度 5/5 | 实用性 5/5 | 可迁移性 5/5）
   `McpUiResourceCsp`（connectDomains, resourceDomains, frameDomains, baseUriDomains）+ `McpUiResourcePermissions`（camera, microphone, geolocation, clipboardWrite）。将 CSP 从「Host 单方面设定」变为「Server 声明 + Host 审批」的双方协商。消除了 `unsafe-eval` 泛滥问题。

3. **工具可见性控制 (`visibility: ["model" | "app"]`)**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   区分工具的受众：`"model"` 意味着 AI 可见可调用，`"app"` 意味着只有 UI 可调用（如刷新按钮、表单提交）。比 OpenAI 的双字段方案更优雅。

4. **双层 iframe 沙箱架构（Sandbox Proxy）**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   Web 端使用 Sandbox Proxy 作为中间层实现 origin 隔离 + CSP 强制执行。Desktop 端可直接单层 iframe。将 Web 安全最佳实践标准化为协议的一部分。

5. **Agent Skills 元编程**（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）
   自带 4 个 Agent Skills（`create-mcp-app`, `migrate-oai-app`, `add-app-to-server`, `convert-web-app`），让 AI 编码助手可以直接创建/迁移 MCP App——「用 AI 构建 AI 工具的 UI」的元层面创新。

### 可复用的模式与技巧

1. **PostMessageTransport**: 190 行实现将任何 JSON-RPC 协议桥接到 iframe/Worker 通信，只需实现 `Transport` 接口
2. **ProtocolWithEvents**: 将 Protocol 的单 handler 模型扩展为 DOM 风格事件系统（`on*` setter + `addEventListener`），带双重注册保护，279 行零依赖
3. **Type-Driven Schema Generation**: `spec.types.ts` → `ts-to-zod` → `generated/schema.ts` → CI 验证一致性。一处定义，多处使用
4. **声明式安全协商**: Server 声明 CSP 和权限需求，Host 审查并执行，默认最严格策略
5. **渐进增强 Capability Negotiation**: `getUiCapability()` 检查 Host 能力，不支持时优雅降级为纯文本
6. **核心无依赖 + 可选框架绑定**: SDK 核心零框架依赖，React hooks 作为子路径导出——SDK 设计的黄金模式

### 关键设计决策

1. **三方架构（Server ↔ Host ↔ View）**：View 通过 Host 代理与 Server 通信，Host 可审查、过滤、记录所有通信。增加一层间接性，换来完整的安全审计能力。

2. **JSON-RPC 2.0 over postMessage**：复用 MCP 的 JSON-RPC 协议而非自定义消息格式，免费获得 MCP SDK 的类型系统、错误处理、超时机制。

3. **预声明资源而非内联嵌入**：服务器通过 `resources/list` 预声明 `ui://` 资源，比 MCP-UI 的内联方式更繁琐，但获得预取/缓存/安全审查能力。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | MCP Apps | MCP-UI (前身) | OpenAI Apps SDK | ACP | LangChain |
|------|----------|--------------|----------------|-----|-----------|
| 定位 | AI UI 标准协议 | MCP UI 客户端 SDK | ChatGPT UI 扩展 | Agent 通信 | Agent 编排 |
| 协议 | JSON-RPC 2.0 (MCP) | 自定义消息 | 私有 | 自有协议 | 无统一协议 |
| 跨 Host | 是（Claude/ChatGPT/VS Code 等） | 部分 | 仅 ChatGPT | 不适用 | 不适用 |
| 安全模型 | 双层 iframe + 声明式 CSP | 基础 iframe | 平台内置 | 不适用 | 不适用 |
| 框架支持 | 6 个前端框架 | React 为主 | React | 不适用 | 不适用 |
| 状态 | 活跃，v1.5.0 | 被整合，保留为 Host SDK | 合并入 MCP Apps | 独立发展 | 不同层面 |

### 差异化护城河
- **标准化护城河**：Anthropic + OpenAI 联合背书 + 正式 MCP 扩展规范（SEP-1865），竞品难以绕过
- **网络效应护城河**：Day-1 即有 6+ 客户端支持，两周内 75+ 应用上线，先发优势极强
- **生态护城河**：25 个示例应用 + 4 个 Agent Skills + 完善文档，开发者入门成本极低

### 竞争风险
- MCP Apps 的主要风险不是竞品，而是**协议采纳的广度**——如果 Google（Vertex AI）或 AWS 选择自建标准而非采纳 MCP Apps，可能形成标准分裂
- 依赖 Olivier Chafik 一人（35% commits）的关键人风险

### 生态定位
占据「AI 交互从文本到图形界面」这一历史性转变的基础设施层。不是应用层产品，而是协议层标准——类似于 HTTP 之于 Web、WebSocket 之于实时通信。

## 套利机会分析
- **信息差**: Star 数（2K）严重低估实际影响力（npm 月下载 382 万）。中文社区对 MCP Apps 的报道几乎为零，但它定义的标准已被 ChatGPT 和 Claude 同时采纳
- **技术借鉴**: (1) PostMessageTransport 模式可直接复用于任何跨 iframe 通信场景；(2) 声明式 CSP 协商模式适用于所有嵌入第三方内容的安全场景；(3) Type-Driven Schema Generation 管线值得所有 TypeScript SDK 借鉴
- **生态位**: AI UI 交互的事实标准，填补了「LLM 工具输出可视化」的根本性空白
- **趋势判断**: 处于基础设施成熟化阶段（v1.0 → v1.5，迭代趋稳）。随着更多 Host 采纳，SDK 下载量将继续指数增长。这是 AI 开发者必须掌握的新范式

## 风险与不足
1. **关键人依赖**：Olivier Chafik 贡献 35% 的 commit，是项目的技术灵魂。虽然有 45 位贡献者，但核心架构决策高度集中
2. **标准分裂风险**：Google 和 AWS 尚未明确表态采纳 MCP Apps，如果选择自建标准，生态可能碎片化
3. **安全攻击面**：尽管安全模型设计精良（双层 iframe + 声明式 CSP），但 iframe 沙箱逃逸和 postMessage 劫持仍是理论风险
4. **`app.ts` 缺少独立单元测试**：核心 View 端类（1,508 行）主要通过 `app-bridge.test.ts` 间接测试，直接测试覆盖不足
5. **React 一等公民偏向**：虽然支持 6 个框架，但只有 React 有一等 hooks 集成（`useApp`, `useAutoResize` 等），其他框架开发者需自行包装
6. **TODO 残留**：`assertCapabilityForMethod` 和 `assertNotificationCapability` 仍标记为 TODO，capability 验证尚未完全实现

## 行动建议
- **如果你要用它**: 现在就开始。v1.5.0 已稳定，25 个示例覆盖主流场景。从 `basic-server-react`（或你偏好的框架）模板开始，或直接用 `create-mcp-app` Agent Skill 让 AI 帮你搭建
- **如果你要学它**: 重点关注 `src/app-bridge.ts`（Host 端核心，理解三方架构）、`src/app.ts`（View 端核心，理解 connect 流程）、`specification/2026-01-26/apps.mdx`（稳定版规范，理解协议设计）、`src/message-transport.ts`（190 行，理解 postMessage 桥接模式）
- **如果你要 fork 它**: (1) 为 `app.ts` 添加独立单元测试；(2) 为 Vue/Svelte/Solid 提供一等框架绑定（类似 React hooks）；(3) 实现 `assertCapabilityForMethod` TODO；(4) 探索 SharedArrayBuffer 或 BroadcastChannel 替代 postMessage 以降低延迟

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/modelcontextprotocol/ext-apps](https://deepwiki.com/modelcontextprotocol/ext-apps) |
| Zread.ai | 未收录 |
| 官方博客 | [初始公告](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) / [正式发布](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) |
| API 文档 | [apps.extensions.modelcontextprotocol.io/api](https://apps.extensions.modelcontextprotocol.io/api/) |
| 规范 PR | [modelcontextprotocol/modelcontextprotocol#1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865) |
| 关联论文 | 无 |
| 在线 Demo | 本地运行 `npm start` → localhost:8080 |
