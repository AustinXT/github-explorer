# Memos 内容分析笔记

## 架构概览

### 技术栈

**后端**: Go 1.26.1 + Echo v5 (HTTP) + gRPC-Gateway + ConnectRPC
**前端**: React 18 + TypeScript + Vite 7 + TailwindCSS 4 + Radix UI + TanStack React Query
**数据库**: SQLite (默认) / MySQL / PostgreSQL (三驱动抽象)
**部署**: Docker (~20MB), Alpine 3.21, 单二进制
**协议**: Protobuf + gRPC-Gateway (REST) + ConnectRPC (浏览器)
**构建**: pnpm (前端) + Go build (后端)

### 目录结构

```
cmd/memos/          - 入口 (cobra CLI)
internal/           - 内部工具包 (profile, util, version)
plugin/             - 插件系统 (cron, email, filter, httpgetter, idp, markdown, scheduler, storage, webhook)
proto/              - Protobuf 定义 (api/v1 + store)
server/             - HTTP 服务器
  auth/             - 认证系统 (JWT + PAT)
  router/api/v1/    - API 路由 (gRPC-Gateway + ConnectRPC)
  router/fileserver/ - 文件服务
  router/frontend/  - 前端静态文件
  router/mcp/       - MCP 协议服务端
  router/rss/       - RSS 订阅
  runner/           - 后台任务 (S3 预签名)
store/              - 数据存储层
  db/               - 数据库驱动 (sqlite/mysql/postgres)
  cache/            - 内存缓存
  migration/        - 数据库迁移
web/                - 前端 (React)
  src/components/   - 52 个组件
  src/pages/        - 15 个页面
  src/locales/      - 33 种语言
```

### 核心设计模式

#### 1. 三数据库驱动抽象 (Driver Interface)

`store/driver.go` 定义了统一的 `Driver` 接口，包含所有数据操作方法。
`store/db/db.go` 通过工厂模式根据 profile 创建 sqlite/mysql/postgres 驱动。
这使得数据库切换对上层完全透明。

#### 2. Protocol-First API 设计

使用 Protobuf 定义 API (proto/api/v1/)，同时生成：
- gRPC-Gateway (REST API): `/api/v1/*`
- ConnectRPC (浏览器直连): `/memos.api.v1.*`
- OpenAPI 规范: `proto/gen/openapi.yaml`

7 个服务：Instance, Auth, User, Memo, Attachment, Shortcut, IdentityProvider

#### 3. CEL 表达式过滤引擎

`plugin/filter/` 实现了基于 Google CEL 的过滤系统：
- 解析 CEL 表达式 → IR 中间表示 → SQL 片段
- 自动处理三种数据库方言的 JSON 字段、占位符、布尔语义差异
- 示例：`has_task_list && visibility == "PUBLIC"` → SQL WHERE 子句

#### 4. 自定义 Markdown 解析引擎

`plugin/markdown/` 基于 goldmark 构建，功能包括：
- 自定义 #tag 扩展和解析
- AST 遍历提取元数据（标签、属性、标题）
- 单次解析提取所有数据 (ExtractAll)
- HTML 渲染（用于 RSS）
- Markdown 往返渲染（tag 重命名）
- 纯文本摘要生成

#### 5. MCP 协议集成

`server/router/mcp/` 实现了完整的 MCP (Model Context Protocol) 服务端：
- 工具：memo CRUD、tag 管理、附件管理、关系管理、表情反应
- 资源：memo 资源暴露
- 提示：预定义 prompt
- 使用 Streamable HTTP 传输

#### 6. SSE 实时推送

`server/router/api/v1/sse_hub.go` 实现了 Server-Sent Events hub：
- 事件类型：memo.created/updated/deleted, reaction.upserted/deleted
- 非阻塞广播，慢客户端事件丢弃
- 32 事件缓冲区

#### 7. 内存缓存系统

`store/cache/cache.go` 实现了通用缓存：
- TTL + 最大条目数
- 定期清理 + LRU 淘汰（20% 批量）
- 原子计数器 + sync.Map
- 缓存 instance settings、users、user settings

### 前端架构

- React 18 + React Router v7
- @connectrpc/connect-web 直连后端 ConnectRPC
- TanStack React Query 数据管理
- Radix UI + shadcn/ui 组件库
- Tailwind CSS v4
- Biome (代替 ESLint/Prettier)
- 33 种语言国际化 (i18n)
- 富文本特性：KaTeX 数学公式、Mermaid 图表、代码高亮、Leaflet 地图

### 认证系统

- JWT Access Token (15分钟短期) - 无状态验证
- Refresh Token - 数据库端校验，支持撤销
- Personal Access Token (PAT) - 长期令牌，用于 API/MCP 访问
- OAuth2 (外部身份提供商)

### 可见性模型

三级可见性：
- PUBLIC: 所有人可见
- PROTECTED: 登录用户可见
- PRIVATE: 仅创建者可见

### 创新亮点

1. **MCP 集成**: 笔记应用原生支持 MCP 协议，可被 AI Agent 直接操作
2. **CEL 过滤引擎**: 使用 Google CEL 作为查询语言，比传统 SQL 拼接更安全优雅
3. **三协议并行**: gRPC-Gateway + ConnectRPC + REST 同时支持
4. **自定义 Markdown 扩展**: goldmark + 自定义 tag 解析，AST 级操作
5. **极简部署模型**: 单二进制 + 前端嵌入 + SQLite 默认，真正一条命令部署
