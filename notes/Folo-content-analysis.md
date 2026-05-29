## 动机与定位
- 要解决的问题: 现代信息消费者面临碎片化的信息源——RSS、博客、播客、视频、社交媒体分散在不同平台，导致信息过载与注意力浪费。Folo 要将多源内容聚合进一条统一时间线，通过 AI 实现降噪。
- 为什么现有方案不够: NetNewsWire 仅覆盖 Apple 生态且无 AI；fluent-reader 只有桌面端没有云同步；ReadYou 限于 Android；FreshRSS/Miniflux 是自托管方案需运维能力，面向开发者。没有一款产品同时做到「全平台 + AI 能力 + 云同步 + 开源」。
- 目标用户: 重度信息消费者（记者、研究员、投资人）、RSS 老用户希望升级体验、追求跨设备无缝切换的阅读者、开发者社区。

## 作者视角
### 问题发现
DIYgod 创建 RSSHub 时解决了「RSS 源获取」的问题——让任何网站都能生成 RSS。但源有了，读在哪里？现有 RSS 阅读器要么功能简陋、要么平台单一、要么界面老旧。Folo（原名 Follow）是 RSSHub 生态的自然延伸：从「供给侧」走向「消费侧」。

### 解法哲学
「Your thoughts are what you read」——将信息消费视为塑造思维的行为，而非被动接收。核心哲学体现在三方面：
1. **无噪音（Noise-free）**: 不做算法推荐，用户自主控制订阅；AI 做辅助（翻译、摘要、分类）而非主导
2. **开放信息（Open Information）**: AGPL 开源 + 支持标准协议（RSS/Atom/JSON Feed），反对信息围墙
3. **BYOK（Bring Your Own Key）**: AI 功能允许用户使用自己的 API Key，不绑定特定服务商

### 背景知识迁移
- **Innei**：设计工程师 + 数字游民，带来精致 UI 审美和全平台体验的执着
- **DIYgod**：RSSHub 创始人（15.7k 粉丝），深刻理解 RSS 生态痛点和开源社区运营
- **LobeHub 经验**：团队有 AI 产品化经验，将 AI 融入阅读器而非堆砌功能
- **Natural Selection Labs**：商业实体支撑，具备从开源到可持续商业化的路径经验

### 战略图景
RSSHub（供给侧聚合）→ Folo（消费侧阅读器）→ 付费订阅/MCP Server 集成 → 构建「开放信息生态」完整闭环。Folo 是这条价值链上的核心消费入口，承载商业化希望（付费功能、AI 配额、List 订阅）。

## 架构与设计决策

### 目录结构概览
采用 pnpm monorepo + Turborepo 管理的三平台共享架构：

```
├── apps/
│   ├── desktop/          # Electron 桌面应用（主渲染器同时作为 Web 应用）
│   │   ├── layer/main/   # Electron 主进程
│   │   └── layer/renderer/ # React 渲染器（核心 UI 代码）
│   ├── mobile/           # React Native (Expo) 移动应用
│   ├── ssr/              # Fastify SSR 服务（外部分享页）
│   ├── cli/              # 命令行工具 (folocli)
│   └── landing/          # 落地页
├── packages/
│   ├── internal/         # 跨平台共享包
│   │   ├── store/        # Zustand 状态管理（核心业务逻辑）
│   │   ├── database/     # Drizzle ORM + SQLite（多后端适配）
│   │   ├── components/   # 共享 UI 组件
│   │   ├── shared/       # 桥接层、设置接口、认证
│   │   ├── models/       # 数据模型类型
│   │   ├── hooks/        # 共享 React Hooks
│   │   ├── atoms/        # Jotai 原子状态
│   │   ├── constants/    # 共享常量
│   │   ├── utils/        # 工具函数
│   │   └── ...
│   └── readability/      # 网页正文提取（发布为独立 npm 包）
├── plugins/              # ESLint 插件等工具
└── locales/              # i18n 翻译文件（5 语言，按领域分目录）
```

分层逻辑：`packages/internal` 是平台无关的业务核心，三个 app 分别引入并接入平台特定实现。状态管理（store）和数据层（database）完全共享，UI 组件部分共享。

### 关键设计决策

1. **决策**: 三端共享核心 store + 平台特定 DB 实现
   - 问题: 桌面（Web/Electron）、移动端（React Native）、SSR 三个运行环境需要统一的业务逻辑，但底层存储 API 完全不同
   - 方案: `@follow/store` 封装纯业务逻辑（Zustand + Immer），通过 `@follow/database` 抽象数据层。数据库有三个实现文件：`db.desktop.ts`（wa-sqlite + IndexedDB VFS 用于 Web/Electron）、`db.rn.ts`（expo-sqlite 用于 React Native）、`db.ts`（声明文件，构建时根据平台条件替换）
   - Trade-off: 牺牲了平台原生数据库的深度优化（如 iOS Core Data），换来了业务逻辑 100% 复用和维护效率
   - 可迁移性: 高 — 任何多端应用都可参考这种「共享 store + 平台适配 DB」模式

2. **决策**: Morph 层（数据变形层）实现 API/DB/Store 三态转换
   - 问题: API 返回的数据结构、SQLite 存储的结构、前端 Store 需要的结构三者不一致
   - 方案: `store/src/morph/` 下设三个变形器：`api.ts`（API → Store）、`db-store.ts`（DB → Store）、`store-db.ts`（Store → DB），集中管理数据映射
   - Trade-off: 引入了映射层的维护成本，但彻底解耦了三层的数据格式依赖
   - 可迁移性: 高 — 适用于任何前端需要对接多数据源的场景

3. **决策**: Transaction 模式实现乐观更新 + 回滚
   - 问题: 离线优先应用需要乐观更新 UI，但网络请求可能失败需要回滚
   - 方案: `createTransaction()` 提供流式 API——`.store()`（乐观更新）→ `.request()`（实际请求）→ `.persist()`（持久化），失败时自动触发 `.rollback()`
   - Trade-off: 增加了写操作的代码复杂度，但换来了流畅的离线体验
   - 可迁移性: 高 — 通用的乐观更新模式，适用于任何离线优先应用

4. **决策**: Zustand + Immer + MapSet 的状态管理组合
   - 问题: RSS 阅读器状态极其复杂——多视图（文章/图片/视频/音频/社交/通知）、多维索引（按 Feed/类别/收件箱/列表/视图）
   - 方案: Zustand 提供 Store 框架，Immer 实现不可变更新，`enableMapSet()` 启用 Set/Map 支持。EntryState 用 6 个 Set 索引同一份 entry 数据（byView、byCategory、byFeed、byInbox、byList、全局 Set）
   - Trade-off: 内存换查询速度，写入时维护多份索引有一致性风险
   - 可迁移性: 中 — 多维索引模式适用于需要多视角查看同一数据集的场景

5. **决策**: AI 功能架构——AbstractChat 继承 + Block/Slice 状态分离
   - 问题: AI 聊天需要管理消息流、上下文 block（当前阅读内容、feed 信息等）、持久化、标题生成等复杂状态
   - 方案: 继承 Vercel AI SDK 的 `AbstractChat` 创建 `ZustandChat`，将 AI SDK 状态同步到 Zustand store。将「上下文 block」和「聊天消息」拆分为独立 Slice（`block.slice` + `chat.slice`），通过 `createAIChatStore` 组合
   - Trade-off: 强依赖 Vercel AI SDK 框架，但获得了流式传输、工具调用等开箱即用能力
   - 可迁移性: 中 — 「AbstractChat + 自定义 State」模式可迁移到任何使用 AI SDK 的项目

6. **决策**: wa-sqlite + IndexedDB VFS 作为 Web 端持久化方案
   - 问题: 浏览器没有原生 SQLite，但需要与移动端共享 Drizzle ORM schema
   - 方案: 使用 wa-sqlite（WebAssembly SQLite 编译版）+ IDBMirrorVFS（将数据镜像到 IndexedDB），配合 ResourceLock 实现并发控制
   - Trade-off: WASM 有初始加载开销，IndexedDB 性能不如原生 SQLite，但实现了 Web/Desktop/Mobile 统一的 SQL 查询能力
   - 可迁移性: 高 — 任何需要在 Web 端使用 SQLite 的项目都可参考

7. **决策**: Command 系统（命令面板 + 快捷键统一管理）
   - 问题: 桌面应用有大量快捷键和操作入口（菜单、命令面板、右键菜单），需要统一注册和管理
   - 方案: `FollowCommandManager` 注册全局、条目、布局、时间线、设置等 9 类命令，所有操作通过 Command ID 引用，支持快捷键绑定
   - Trade-off: 前期需要为每个操作注册命令，但后续扩展性极好
   - 可迁移性: 高 — VS Code 风格的命令系统，适用于任何复杂桌面应用

8. **决策**: 平台感知的路由策略
   - 问题: Electron 和浏览器的路由机制不同（hash vs history），调试代理模式又需要特殊处理
   - 方案: 运行时检测 `IN_ELECTRON` 或 `__DEBUG_PROXY__`，动态选择 `createHashRouter` 或 `createBrowserRouter`，同时支持文件系统路由自动生成
   - Trade-off: 路由层多了一层抽象，但实现了「一套代码三种运行模式」
   - 可迁移性: 中 — 适用于 Electron + Web 双端应用

## 创新点

1. **Morph 数据变形层**
   - 描述: 创建专门的 Morph 类（`APIMorph`、`DbStoreMorph`、`StoreDbMorph`），将 API 响应、SQLite 行、Store 状态之间的转换集中到独立模块。不同于传统的 DTO/VO 映射散布各处，Folo 将变形逻辑封装为单例类，映射关系一目了然
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 5/5
   - 适用场景: 任何需要在多层（API/缓存/UI状态）之间转换数据的全栈应用

2. **Transaction 流式乐观更新**
   - 描述: 自定义 `Transaction` 类提供链式 API `.store()` → `.request()` → `.persist()` + `.rollback()`，将乐观更新、API 调用、本地持久化编排为一个事务。支持同步/异步自由混合
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 5/5
   - 适用场景: 离线优先应用、协同编辑、需要乐观 UI 的任何场景

3. **多维 Set 索引的 Entry 状态**
   - 描述: 用 6 个 `Record<Key, Set<EntryId>>` 索引同一份 Entry 数据（byView、byCategory、byFeed、byInbox、byList + 全局 entryIdSet），利用 Immer MapSet 插件实现不可变更新。查询任意维度的 entry 列表都是 O(1) 集合查找
   - 新颖度: 3/5 | 实用性: 4/5 | 可迁移性: 3/5
   - 适用场景: 信息聚合类应用需要按多种维度组织同一份数据

4. **ZustandChat — AI SDK 状态桥接**
   - 描述: 继承 Vercel AI SDK 的 `AbstractChat`，重写 `state` 为 `ZustandChatState`，将 AI SDK 的消息流、状态变更自动同步到 Zustand store。既享受 AI SDK 的流式传输能力，又保持了与应用其他部分状态管理的一致性
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 4/5
   - 适用场景: 任何在 React 应用中集成 AI 聊天且使用 Zustand 管理状态的项目

5. **上下文 Block 系统**
   - 描述: AI 聊天不是独立窗口，而是能感知当前阅读上下文。通过 `BlockSlice` 管理「mainView」「mainEntry」「mainFeed」「unreadOnly」等特殊 block 类型，AI 能自动获取用户正在看的内容作为对话上下文
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 3/5
   - 适用场景: 将 AI 对话嵌入内容消费场景的应用（笔记工具、文档阅读器）

6. **跨平台 SQLite 统一层**
   - 描述: 通过条件文件（`db.desktop.ts` / `db.rn.ts`）+ 声明文件（`db.ts`）实现同一个 Drizzle schema 在 Web（wa-sqlite + IndexedDB VFS）和 React Native（expo-sqlite）上运行。ResourceLock 确保 Web 端并发安全
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 4/5
   - 适用场景: 需要 Web + Mobile 共享结构化数据层的跨平台应用

7. **Custom Integration 系统**
   - 描述: 允许用户创建自定义集成（Fetch Template / URL Scheme Template），通过占位符系统（title、url、contentMarkdown、summary 等）将 entry 数据注入到用户自定义的 HTTP 请求或 URL Scheme 中，实现与 Notion、Readwise 等外部工具的无代码对接
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 3/5
   - 适用场景: 需要与外部服务集成且希望用户自助配置的应用

## 可复用模式
1. **createJSContext — 依赖注入容器**: 不使用 React Context，用闭包实现跨平台的 provide/consumer 模式 — 适用场景: 需要在非 React 代码中共享依赖（如 Store 层访问 API Client）
2. **Morph 单例变形器**: 集中管理 API↔Store↔DB 的数据映射 — 适用场景: 多层数据转换的全栈应用
3. **Transaction 乐观更新**: store→request→persist 三阶段事务 + rollback — 适用场景: 离线优先应用
4. **条件文件 + 声明文件的平台适配**: `db.ts`（声明）+ `db.desktop.ts`/`db.rn.ts`（实现），构建时替换 — 适用场景: 跨平台共享包需要不同底层实现
5. **createZustandStore 工厂 + 全局调试 Proxy**: 所有 store 自动注册到 `globalThis.store`，开发时可在控制台直接读写状态 — 适用场景: 复杂状态调试
6. **Command 注册系统**: 统一的命令 ID + Hook 注册 + 快捷键绑定 — 适用场景: 桌面应用命令面板
7. **NDJSON 流式解析**: `readNdjsonStream` 处理流式 API 响应，逐行解析 JSON — 适用场景: 任何需要流式处理大量 JSON 数据的场景
8. **Hydrate 模式**: 启动时从本地 DB 批量加载数据到内存 Store，实现秒开 — 适用场景: 离线优先应用的冷启动优化

## 竞品交叉分析

### vs NetNewsWire
- 我们更好: 全平台覆盖（Windows/Linux/Android/Web）、AI 翻译摘要、云同步、社交内容类型支持、命令行工具
- 竞品更好: macOS/iOS 原生性能极致、零依赖零后端、隐私性更强（纯本地）、Apple 生态深度集成
- 不同目标: NetNewsWire 面向 Apple 用户的极简本地阅读；Folo 面向跨平台重度信息消费者
- 用户迁移成本: 低 — OPML 导入即可，但会失去 Apple 原生体验

### vs fluent-reader
- 我们更好: 全平台（fluent-reader 仅桌面）、AI 能力、云同步、移动端、社区活跃度更高
- 竞品更好: 更轻量（纯 Electron 无后端）、完全离线、启动更快
- 不同目标: fluent-reader 做桌面级「够用就好」的 RSS 阅读；Folo 做全平台信息枢纽
- 用户迁移成本: 低 — OPML 导入

### vs ReadYou
- 我们更好: 全平台（ReadYou 仅 Android）、AI 能力、云同步、桌面体验
- 竞品更好: Material You 原生 Android 设计、更低电量消耗、更小安装包
- 不同目标: ReadYou 做 Android 最佳本地 RSS 体验；Folo 做跨平台
- 用户迁移成本: 中 — OPML 导入可行，但需放弃 Material You 原生体验

### vs FreshRSS / Miniflux
- 我们更好: 开箱即用（无需自托管）、精致 UI、AI 能力、移动端原生体验、无运维成本
- 竞品更好: 完全自主控制数据、零费用（除服务器）、可深度定制、PHP/Go 生态成熟
- 不同目标: FreshRSS/Miniflux 面向有运维能力的技术用户；Folo 面向希望「即用」的普通用户
- 用户迁移成本: 中 — 需要从自托管迁移到 Folo 云服务，数据主权降低

### 综合竞争结论
- 差异化护城河: 「AI + 全平台 + 云同步 + 开源」的四维组合独一无二；RSSHub 生态导流是竞品无法复制的渠道优势；活跃的开发节奏（197k 行 TS、2330 个源文件）构建了技术壁垒
- 竞争风险: (1) 订阅数量限制（#4646）和付费功能可能导致开源社区分裂；(2) UI 重构引发的用户反弹（#4651）说明设计语言尚未稳定；(3) 云服务稳定性曾是痛点（#2473），基础设施可靠性需持续投入
- 生态定位: Folo 是 RSSNext 组织从「信息供给」到「信息消费」战略的核心产品，定位为「开放信息生态」的消费入口。CLI 工具和 MCP Server 规划进一步将其推向开发者生态

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | A- | 197k 行 TypeScript，strict 模式，避免 any（AGENTS.md 明确禁止），Immer 保证不可变更新，架构分层清晰 |
| 文档质量 | B+ | 4,446 行 Markdown，AGENTS.md 极其详尽（170 行），CONTRIBUTING.md 覆盖四种开发模式，但缺少独立架构文档 |
| 测试覆盖 | B- | 有单元测试（vitest）+ E2E（Playwright 桌面端，Maestro 移动端），但测试文件仅约 30 个，相对 2330 个源文件覆盖率偏低 |
| CI/CD | A | 17 个 GitHub Actions 工作流覆盖 lint/typecheck/test/构建/部署/发布/签名，Turbo 缓存加速，支持 Android/iOS/Desktop/Web/Cloudflare 全链路 |
| 错误处理 | B+ | 自定义错误工具函数、Sentry 集成、Transaction 回滚机制、数据库迁移失败自动重建，但部分 catch 块使用空处理 |

### 质量检查清单
- [x] TypeScript strict 模式
- [x] ESLint + Prettier 统一格式化（eslint.config.mjs + prettier，pre-commit hook 通过 simple-git-hooks + lint-staged 强制执行）
- [x] CI 流水线（lint → typecheck → test → build 全覆盖）
- [x] 代码签名（Windows: SignPath.io，macOS/iOS: Apple Developer Program）
- [x] 构建产物验证（GitHub artifact attestations）
- [x] 多平台 E2E 测试（Playwright + Maestro）
- [x] i18n 完善（5 种语言，按领域分组，lint 规则去重）
- [x] 依赖管理（nolyfill 优化 polyfill、pnpm overrides 统一版本、patchedDependencies 修复上游问题）
- [x] 安全（DOMPurify 清洗 readability 内容防 XSS、AGPL 许可证）
- [ ] 独立架构文档（依赖 AGENTS.md 和代码注释，缺少 ADR 或设计文档目录）
- [ ] 测试覆盖率报告（无覆盖率阈值设定）
- [ ] API 文档（CLI 有 skill.md，但 internal packages 缺少 API docs）
