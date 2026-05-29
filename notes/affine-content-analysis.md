# AFFiNE 内容分析

## 项目定位

AFFiNE 定位为 "Notion + Miro" 的开源替代品，是一个集文档编辑、白板绘图和数据库管理于一体的"超融合"知识操作系统。口号是 "Write, Draw and Plan All at Once"。

## 技术架构

### Monorepo 结构（Yarn Berry Workspaces）

```
AFFiNE/
├── blocksuite/          # 自研编辑器框架（核心差异化）
│   ├── framework/       # 底层框架（store, std, sync, global）
│   ├── affine/          # AFFiNE 专属 block 实现
│   │   ├── all/         # 聚合包 @blocksuite/affine
│   │   ├── blocks/      # 各种 block 类型
│   │   ├── components/  # UI 组件
│   │   ├── data-view/   # 数据库视图
│   │   ├── gfx/         # 图形渲染（白板）
│   │   ├── inlines/     # 行内元素（链接、公式等）
│   │   ├── rich-text/   # 富文本编辑
│   │   ├── widgets/     # 工具栏、菜单等
│   │   ├── model/       # 数据模型
│   │   └── shared/      # 共享工具
│   └── integration-test/
├── packages/
│   ├── frontend/
│   │   ├── core/        # React 前端核心
│   │   ├── component/   # UI 组件库
│   │   ├── apps/
│   │   │   ├── web/     # Web 应用
│   │   │   ├── electron/ # 桌面端 (Electron)
│   │   │   ├── ios/     # iOS (Capacitor)
│   │   │   ├── android/ # Android (Capacitor)
│   │   │   └── mobile/  # 移动端共享
│   │   ├── native/      # Rust native 模块
│   │   ├── i18n/        # 国际化
│   │   ├── track/       # 埋点追踪
│   │   └── templates/   # 模板
│   ├── backend/
│   │   ├── server/      # NestJS 后端（GraphQL API）
│   │   └── native/      # Rust native 模块
│   └── common/
│       ├── infra/       # 基础设施抽象 (@toeverything/infra)
│       ├── nbstore/     # 数据存储层
│       ├── y-octo/      # 自研 Yjs CRDT 实现 (Rust)
│       ├── graphql/     # GraphQL schema
│       └── ...
├── tools/               # 构建工具、CLI
└── tests/               # E2E 测试套件
```

### 核心技术选型

| 层级 | 技术 | 说明 |
|------|------|------|
| 编辑器框架 | BlockSuite (自研) | 基于 Lit Web Components 的 block 编辑器 |
| 前端框架 | React 19 | 应用层 UI |
| 状态管理 | @toeverything/infra | 自研依赖注入 + 响应式框架 |
| 样式 | vanilla-extract | CSS-in-TS |
| 桌面端 | Electron 39 | 跨平台桌面应用 |
| 移动端 | Capacitor 7 | 跨平台移动应用 |
| 后端框架 | NestJS 11 | Node.js 服务端 |
| API | GraphQL (Apollo) | 前后端通信 |
| 数据库 | Prisma + PostgreSQL | 数据持久化 |
| 缓存/队列 | Redis + BullMQ | 任务队列、缓存 |
| CRDT | y-octo (自研, Rust) | Yjs 兼容的 CRDT 实现 |
| 原生模块 | Rust (NAPI-RS) | 性能关键路径 |
| 可观测性 | OpenTelemetry | 全链路监控 |
| CI/CD | GitHub Actions | 持续集成 |
| 部署 | Helm/Docker | Kubernetes 部署 |
| AI | Copilot (Gemini 等) | AI 辅助写作 |
| MCP | Model Context Protocol | AI Agent 集成 |
| 付费 | RevenueCat | iOS/Android 订阅 |

### 自研组件（关键技术壁垒）

1. **BlockSuite**: 自研 block 编辑器框架，基于 Web Components (Lit)，支持文档和白板的"超融合"编辑体验。70+ 子包，是 AFFiNE 最核心的差异化资产。
2. **y-octo**: Rust 实现的 Yjs CRDT，提供本地优先的协作能力。
3. **@toeverything/infra**: 自研的依赖注入和响应式框架，用于管理应用状态。
4. **nbstore**: 统一的数据存储抽象层。

## 许可证策略

采用**双许可模式**:
- **前端代码** (blocksuite/, packages/frontend/): MIT 许可
- **后端代码** (packages/backend/, packages/common/native/): Enterprise Edition License
  - 开发测试免费
  - 生产环境需要企业订阅

这是一种常见的开源商业化策略（类似 GitLab CE/EE），允许社区自由使用前端编辑器，但后端服务的生产使用需要付费。

## 全平台覆盖

- **Web**: app.affine.pro
- **Desktop**: Electron (Windows/macOS/Linux)
- **iOS**: 原生 Swift + Capacitor
- **Android**: Kotlin + Capacitor
- **自托管**: Docker Compose + Helm Charts

## AI 集成

- **Copilot**: 集成 AI 写作助手，支持 Gemini 等模型
- **MCP**: 支持 Model Context Protocol，允许 AI Agent 读写文档
- **功能**: 写作辅助、大纲转幻灯片、文章总结为思维导图、代码原型生成

## 测试策略

- **单元测试**: Vitest
- **E2E 测试**: Playwright，覆盖 7 个平台变体
  - affine-local, affine-cloud, affine-desktop, affine-desktop-cloud
  - affine-mobile, affine-cloud-copilot, blocksuite
- **集成测试**: BlockSuite 独立测试套件

## 开发节奏

- 提交活跃度在 2025 年 Q3/Q4 明显下降
- 2026 年初有回升趋势
- Canary 版本几乎每日发布，显示持续交付能力强
- 大量依赖更新（renovate bot），说明维护意识好
