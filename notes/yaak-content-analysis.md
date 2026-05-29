# mountain-loop/yaak 内容分析

## 3.1 动机：为什么 Insomnia 创始人要重新做一个？

### 背景推演

Gregory Schier 于 2023-02-15 创建了 Yaak 的第一个 commit（"Initial setup Vite Tauri"），此时距 Insomnia 被 Kong 收购（2019年）已过四年。从代码历史和产品定位可推断以下动机链：

1. **Insomnia 方向偏离**：Kong 收购后，Insomnia 引入了强制云同步、账户登录等要求，与 Schier 的"离线优先、隐私至上"理念冲突。README 明确写道："No telemetry, no VC funding, and no cloud lock-in。"
2. **技术栈重选**：Insomnia 基于 Electron + Node.js，Yaak 选择 Tauri + Rust + React，追求更小体积和更高性能。这不是渐进式改进，而是彻底的技术重构。
3. **商业模式回归独立**：Yaak 通过社区购买 license 盈利（README："Development is funded by community-purchased licenses"），拒绝 VC 路线，保持个人控制权。
4. **修复架构债务**：Insomnia 经过多年迭代积累了大量遗留代码，从零开始可以做出更好的架构决策（如插件系统、模板引擎等）。

### 第一手证据

- 项目首个 commit 时间：2023-02-15 16:58:56 PST
- 仓库明确提供 Insomnia 导入器（`plugins/importer-insomnia`，支持 v4 和 v5 格式）
- 官网有专门的对比页面：yaak.app/alternatives/insomnia
- 4,433 个 commit，97.1% 来自 Gregory Schier 一人，持续开发三年

---

## 3.2 架构分析

### 整体架构：三层分离

```
┌────────────────────────────────────────────────────┐
│                  前端层 (React)                      │
│  src-web/ (37,534 行 TS/TSX)                        │
│  96 个组件 · 102 个 hooks · TanStack Router         │
│  Jotai 状态管理 · CodeMirror 编辑器 · Tailwind CSS  │
├────────────────────────────────────────────────────┤
│               Tauri 桥接层                           │
│  crates-tauri/ (6,684 行 Rust)                      │
│  yaak-app: 主入口、Tauri commands、窗口管理         │
│  yaak-license: 商业许可验证                          │
│  yaak-fonts / yaak-mac-window: 平台特定              │
│  yaak-tauri-utils: 共享 Tauri 工具                   │
├────────────────────────────────────────────────────┤
│               核心业务层 (纯 Rust)                   │
│  crates/ (23,662 行 Rust) — 无 Tauri 依赖           │
│  15 个 crate，详见下方                               │
├────────────────────────────────────────────────────┤
│               插件层 (TypeScript)                    │
│  plugins/ (35 个内置) + plugins-external/ (3 个)     │
│  packages/plugin-runtime: Node.js sidecar 进程      │
│  通过 WebSocket 与 Rust 后端双向通信                 │
└────────────────────────────────────────────────────┘
```

### Rust Crate 拓扑（15 个共享 crate + 5 个 Tauri crate + 1 个 CLI crate）

**核心层级**：
| Crate | 职责 | 关键依赖 |
|-------|------|----------|
| `yaak-core` | 抽象 trait（AppContext）,解耦 Tauri | 无外部依赖 |
| `yaak-common` | 跨平台工具函数、serde 助手 | 无 Tauri |
| `yaak-models` | SQLite 数据层（r2d2 连接池）、67 个迁移文件、2,560 行模型定义 | r2d2, rusqlite, sea-query |
| `yaak-crypto` | 加密管理器（master key + workspace key 层级加密）| keyring |
| `yaak-templates` | 模板解析器和渲染器（`${var}` 和函数调用语法）| 无 |
| `yaak-tls` | TLS 配置（客户端证书、证书验证策略）| rustls, rustls-platform-verifier |
| `yaak-http` | HTTP 客户端（连接池、cookie 管理、DNS 解析器、压缩解码）| reqwest, hyper-util |
| `yaak-grpc` | gRPC 客户端（反射、动态消息编码/解码、流式调用）| tonic, prost-reflect |
| `yaak-sse` | Server-Sent Events 类型定义 | 极小 |
| `yaak-ws` | WebSocket 连接管理 | tokio-tungstenite |
| `yaak-plugins` | 插件管理器（Node.js sidecar 启动、WebSocket 通信、事件协议）| tokio |
| `yaak-sync` | 文件系统同步（workspace 镜像到本地文件夹、双向同步操作）| notify (fswatch) |
| `yaak-git` | Git 操作封装（clone, commit, push, pull, branch 管理）| git2 |
| `yaak-api` | Yaak 自有 API 客户端（更新检查、license 验证）| reqwest, sysproxy |
| `yaak` | 高层编排（send, render, plugin_events 的统一入口）| 依赖上述多数 crate |

### 正在进行的架构演进：Tauri 解耦

`.claude-context.md` 文件揭示了一个重要的正在进行的架构重构——**将 Tauri 从核心逻辑中完全分离**：

- 目标：让 Yaak 以 CLI 形式独立运行（不依赖 Tauri 桌面框架）
- 已完成：yaak-models, yaak-http, yaak-common, yaak-crypto, yaak-grpc 已无 Tauri 依赖
- 待完成：yaak-git, yaak-plugins（最复杂,13 个文件深度集成）, yaak-sync, yaak-ws
- CLI 产品已发布：`crates-cli/yaak-cli`，支持 send/workspaces/requests 等命令
- 使用 `init_standalone()` 模式让 CLI 共享桌面应用的同一 SQLite 数据库

### 数据存储

- **主数据库**：SQLite（r2d2 连接池,最大 100 连接）
- **Blob 数据库**：独立 SQLite（存储响应体等大对象,最大 50 连接）
- **加密**：两层体系——master key（OS keychain 存储）+ workspace key（每工作区独立）
- **迁移**：67 个 SQL 迁移文件，从 2023-02-25 至 2026-03-01，自建迁移系统（兼容 sqlx 表结构）

### 插件系统架构

```
Rust 进程                          Node.js Sidecar
┌──────────────┐    WebSocket     ┌──────────────────┐
│ PluginManager│◄─────────────────►│ plugin-runtime   │
│  (server_ws) │                   │  (index.ts)      │
│              │ InternalEvent     │                  │
│              │ (JSON over WS)    │  ┌────────────┐ │
│              │                   │  │PluginHandle│ │
│              │                   │  │  (worker)  │ │
│              │                   │  └────────────┘ │
└──────────────┘                   └──────────────────┘
```

- Rust 端启动 yaaknode（打包的 Node.js 二进制）作为 sidecar
- 通过 WebSocket 双向通信，使用 `InternalEvent` 作为统一消息格式
- 每个插件在独立的 PluginHandle/Worker 中运行
- 事件类型超过 40 种（boot, terminate, import, filter, auth, template 函数等）

### 前端架构

- **路由**：TanStack Router（文件系统路由）
- **状态管理**：Jotai（原子化状态）
- **UI**：102 个自定义 hooks + 96 个组件，全部手写（无 UI 库依赖）
- **编辑器**：CodeMirror 6，包含自定义 Twig 模板语法高亮
- **主题**：60+ 个内置主题（通过 plugin 加载），CSS 变量驱动
- **类型安全**：ts-rs 从 Rust struct 自动生成 TypeScript 类型（17 个文件使用 `#[ts(...)]`）

---

## 3.3 创新点

### 1. 纯 Rust 的 HTTP 事务引擎

Yaak 没有使用 reqwest 的高层 redirect 处理，而是自己实现了 `HttpTransaction`（931 行），手动管理：
- 重定向链（区分 307/308 保持方法 vs 303/301/302 降级为 GET）
- Cookie 注入/收集
- DNS 事件采集
- 压缩解码（gzip, brotli, deflate, zstd 四种）
- 自定义 DNS 解析器（`LocalhostResolver`）支持 DNS 覆写

### 2. 模板引擎（yaak-templates）

独立实现的模板语言，支持：
- 变量插值 `${variable}`
- 函数调用 `${uuid()}`, `${timestamp()}`
- 嵌套渲染（最大深度 50 层）
- Base64 编码的特殊字符参数
- 通过插件系统可扩展新函数（15 个内置模板函数插件）

### 3. Workspace-to-Filesystem 双向同步

`yaak-sync` crate 使用 `notify`（fswatch）监听文件变化，实现：
- 工作区内容镜像为本地 YAML 文件
- 支持 Git 版本控制或 Dropbox 同步
- 六种同步操作类型：FsCreate/FsUpdate/FsDelete + DbCreate/DbUpdate/DbDelete
- 冲突检测与处理

### 4. 内置 Git 操作

`yaak-git` crate + 前端 11 个 Git 组件，实现了完整的 Git 工作流：
- clone, init, commit, push, pull（含 force reset 和 merge 两种策略）
- 分支管理（创建/删除/重命名/checkout/merge）
- 远程管理、凭证管理
- 状态展示（uncommitted changes, diverged 检测）

### 5. MCP Server 集成

`plugins-external/mcp-server` 作为内置插件运行，在 `127.0.0.1:64343` 提供 MCP 服务：
- 使用 Hono + StreamableHTTPTransport
- 暴露 httpRequest, folder, workspace, window, toast 五类工具
- 让 Claude Code 等 AI 工具可以通过 MCP 协议直接操作 Yaak

### 6. 架构级的 CLI/桌面共享

通过 `yaak-core` 的 `AppContext` trait 和 `init_standalone()` 模式，实现：
- 同一份业务逻辑代码在 Tauri 桌面和 CLI 中复用
- CLI 可直接读写桌面应用的同一 SQLite 数据库
- 插件系统在 CLI 模式下同样可用

---

## 3.4 竞品交叉分析

### vs Insomnia（同一作者的前作）

| 维度 | Insomnia | Yaak |
|------|----------|------|
| 技术栈 | Electron + Node.js | Tauri + Rust + React |
| 安装包大小 | ~200MB+ | 显著更小（Tauri 优势） |
| 强制登录 | Kong 收购后引入 | 无，离线优先 |
| 数据存储 | 云端 + 本地 | 纯本地 SQLite |
| 协议支持 | REST, GraphQL | REST, GraphQL, gRPC, WebSocket, SSE |
| 插件系统 | 有但受限 | 完善的 Node.js sidecar 架构 |
| 加密 | 云端加密 | 本地两层加密（master key + workspace key） |
| Git 集成 | 无 | 内置完整 Git 工作流 |
| AI 集成 | 无 | MCP Server 内置 |
| 商业模式 | Kong 企业产品 | 独立开发者 + 社区 license |

**核心差异**：Yaak 是 Schier 对"API 客户端应该怎么做"的重新思考——隐私优先、本地数据、不依赖云端。

### vs Bruno（31K star）

| 维度 | Bruno | Yaak |
|------|-------|------|
| 技术栈 | Electron + React | Tauri + Rust + React |
| 数据存储 | 文件系统（.bru 格式） | SQLite + 文件系统同步 |
| 协议 | REST, GraphQL | REST, GraphQL, gRPC, WebSocket, SSE |
| 加密 | 无内置 | 两层加密体系 |
| Git | 通过文件系统天然支持 | 内置 Git 操作 UI |
| 插件 | 有限的脚本支持 | 完整的 TypeScript 插件系统 |
| CLI | 有（bru CLI） | 有（yaak CLI，共享数据库） |

**Yaak 优势**：协议覆盖更广（gRPC/WS/SSE），加密更完善，插件系统更强大。
**Bruno 优势**：文件系统原生存储更简单直接，社区更大。

### vs Hoppscotch（70K star）

- Hoppscotch 是 Web-based，Yaak 是桌面应用——不同使用场景
- Yaak 的 gRPC 和 WebSocket 支持更深入
- Hoppscotch 有团队协作功能，Yaak 通过 Git sync 间接实现

---

## 3.5 代码质量评估

### 优点

1. **模块化出色**：21 个 Rust crate 职责清晰，正在进行的 Tauri 解耦证明架构具有良好的可分离性
2. **类型安全贯穿全栈**：Rust struct 通过 ts-rs 自动生成 TypeScript 类型，17 个文件使用自动绑定，消除手动类型同步的风险
3. **自建而非依赖**：模板引擎、HTTP 事务管理、迁移系统均为自建，减少外部依赖风险
4. **测试覆盖合理**：21 个 Rust 文件包含 `#[cfg(test)]`，18 个 TypeScript 测试文件，关键插件（importers, auth）均有测试
5. **错误处理规范**：所有 crate 都有独立的 `error.rs`，使用 `thiserror` 提供有意义的错误类型链
6. **commit 纪律良好**：4,433 个 commit，消息简洁清晰，开发持续三年无中断

### 风险点

1. **Bus Factor = 1**：97.1% 的 commit 来自一人，PR 政策严格限制社区贡献（仅限 bug fix），这是最大的项目风险
2. **前端组件规模大**：96 个组件 + 102 个 hooks，完全手写无 UI 库，维护负担重
3. **yaak-app/src/lib.rs 过大**：1,941 行，承担了太多 Tauri command 定义，应进一步拆分
4. **插件系统复杂度**：Rust-Node.js WebSocket 通信 + 40+ 事件类型，是 Tauri 解耦的最大难点
5. **Issues 禁用**：外迁到 feedback.yaak.app，降低了开源社区参与的便利性

### 代码规模统计

| 层 | 语言 | 行数 |
|----|------|------|
| 共享 Rust crate | Rust | 23,662 |
| Tauri 专用 crate | Rust | 6,684 |
| 前端 | TypeScript/TSX | 37,534 |
| 插件 | TypeScript | 11,819 |
| **总计** | | **~79,699** |

### AI 辅助开发的证据

项目包含 `.claude-context.md`（83 行）和 `AGENTS.md`（2 行），说明作者正在使用 Claude Code 辅助开发。`.claude-context.md` 详细描述了 Tauri 解耦的进度和模式，这是为 AI 编写的上下文文档。
