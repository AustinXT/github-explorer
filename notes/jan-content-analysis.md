# Jan (janhq/jan) 内容分析

## 项目定位
Jan 是一个开源的 ChatGPT 替代品，主打 100% 本地离线运行。由 Menlo Research Pte. Ltd.（新加坡注册）开发，定位为"将最好的开源 AI 带入易用产品"。

## 技术架构

### 整体架构：Tauri + React + Rust + 扩展系统
```
┌─────────────────────────────────────────────────────┐
│                    Jan Desktop App                   │
├─────────────────┬───────────────────────────────────┤
│   web-app/      │          src-tauri/                │
│   React + Vite  │          Rust Backend              │
│   TanStack      │  ┌────────────────────────────┐   │
│   Router        │  │ core/                       │   │
│   Tailwind CSS  │  │  ├── app (设置/常量)         │   │
│   Radix UI      │  │  ├── downloads (下载管理)    │   │
│   AI SDK        │  │  ├── extensions (扩展系统)   │   │
│   i18n          │  │  ├── filesystem (文件系统)   │   │
│                 │  │  ├── mcp (MCP 协议)          │   │
│                 │  │  ├── server (API 服务器)     │   │
│                 │  │  ├── threads (对话线程)      │   │
│                 │  │  ├── system (系统信息)       │   │
│                 │  │  └── updater (自动更新)      │   │
│                 │  ├────────────────────────────┤   │
│                 │  │ plugins/                    │   │
│                 │  │  ├── tauri-plugin-llamacpp  │   │
│                 │  │  ├── tauri-plugin-hardware  │   │
│                 │  │  ├── tauri-plugin-mlx       │   │
│                 │  │  ├── tauri-plugin-foundation│   │
│                 │  │  │   -models                │   │
│                 │  │  ├── tauri-plugin-vector-db │   │
│                 │  │  └── tauri-plugin-rag       │   │
│                 │  └────────────────────────────┘   │
├─────────────────┴───────────────────────────────────┤
│                   extensions/                        │
│  ├── llamacpp-extension (llama.cpp 推理引擎)         │
│  ├── mlx-extension (Apple MLX，仅 macOS)             │
│  ├── foundation-models-extension (Apple FMs)         │
│  ├── assistant-extension (助手管理)                   │
│  ├── conversational-extension (对话管理)              │
│  ├── download-extension (模型下载)                    │
│  ├── rag-extension (RAG 检索增强生成)                 │
│  └── vector-db-extension (向量数据库)                 │
├─────────────────────────────────────────────────────┤
│          Native Inference Servers                    │
│  ├── mlx-server/ (Swift, Apple MLX)                  │
│  └── foundation-models-server/ (Swift, Apple FMs)    │
└─────────────────────────────────────────────────────┘
```

### 前端技术栈
- **框架**: React 19 + TypeScript 5.9
- **路由**: TanStack Router（文件系统路由）
- **构建**: Vite 6.3
- **UI 组件**: Radix UI + Tailwind CSS 4 + shadcn/ui 风格
- **AI 集成**: Vercel AI SDK（@ai-sdk/anthropic, @ai-sdk/openai, @ai-sdk/xai）
- **状态管理**: 自定义 hooks + stores
- **国际化**: react-i18next
- **测试**: Vitest + Testing Library

### 后端技术栈
- **桌面框架**: Tauri 2.8（从 Electron 迁移，2025年3月开始）
- **语言**: Rust（edition 2021）
- **HTTP**: hyper 0.14（本地 API 服务器）
- **MCP**: rmcp 0.8.5（Model Context Protocol 客户端）
- **数据库**: SQLite（通过 sqlx，移动端）
- **CLI**: clap + dialoguer + indicatif

### 推理引擎集成方式
1. **llama.cpp**: 通过 Tauri 插件 `tauri-plugin-llamacpp` + TypeScript 扩展 `llamacpp-extension`
   - Rust 层处理进程管理、GGUF 解析、设备检测
   - 支持 CUDA 后端
2. **Apple MLX**: 通过 Swift 原生 `mlx-server/` + Tauri 插件，仅 macOS
3. **Apple Foundation Models**: 通过 Swift 原生 `foundation-models-server/`，仅 macOS
4. **云端 API**: 通过 Vercel AI SDK 直接连接 OpenAI/Anthropic/Groq/MiniMax 等

### 关键功能路由
- `/` — 首页
- `/hub` — 模型中心（浏览/下载模型）
- `/threads/$threadId` — 对话线程
- `/project/$projectId` — 项目（新功能）
- `/settings/*` — 设置（含 general, providers, mcp-servers, claude-code, extensions, hardware 等）
- `/local-api-server` — 本地 API 服务器管理
- `/system-monitor` — 系统监控
- `/logs` — 日志查看

### Monorepo 结构
- 根 `package.json` 定义 yarn workspaces: `core`, `web-app`
- `core/`: 共享类型定义和浏览器端 API
- `web-app/`: 前端应用
- `extensions/`: 独立的扩展包
- `src-tauri/`: Rust 后端 + Tauri 插件
- `docs/`: Next.js 文档站点

## 架构演进
1. **初期（2023-08）**: 初始项目结构
2. **Electron 时代（2023-10 ~ 2025-03）**: Issue #175 开始的 Electron 架构
3. **Tauri 迁移（2025-03-24）**: "feat: tauri toolkit" 首个提交
4. **Electron 废弃（2025-05~06）**: CI/CD 完全切换到 Tauri
5. **当前（2026-03）**: Tauri 2.x 稳定版本，支持桌面 + 移动端

## 设计亮点
1. **插件化推理引擎**: 不同推理后端通过 Tauri 插件隔离，可选编译
2. **MCP 协议集成**: 使用 rmcp crate 实现 MCP 客户端，支持 SSE/Streamable HTTP/子进程传输
3. **混合模式**: 本地模型和云端 API 统一 UI
4. **OpenAI 兼容 API**: 本地 localhost:1337 服务器，可供其他应用使用
5. **Claude Code 集成**: 设置页面中有 Claude Code 专项配置
6. **跨平台策略**: 桌面（Win/Mac/Linux）+ 移动端（iOS/Android via Tauri）

## 潜在风险
1. **Tauri 迁移尚新**: 2025年3月才开始，可能存在稳定性问题
2. **双层扩展系统**: TypeScript 扩展 + Rust 插件并存，架构复杂度高
3. **Apple 平台依赖**: MLX 和 Foundation Models 仅 macOS，平台差异大
4. **OpenClaw 被移除**: 最近移除了 OpenClaw 沙箱功能，功能方向仍在探索
5. **许可证变更**: 从 MIT 变为 Apache 2.0 + "Menlo Research" 版权
