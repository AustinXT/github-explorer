# Triplit 深度分析报告

> GitHub: https://github.com/aspen-cloud/triplit

## 一句话总结

TypeScript 全栈同步数据库——客户端和服务端共享同一查询引擎 + 增量视图维护（IVM）实时更新 + 双缓冲同步协议实现乐观更新，是 local-first 赛道中唯一的「端到端全栈」开源方案，但自 2025-09 以来开发活动接近停滞。

## 值得关注的理由

1. **数据库内核技术在浏览器中的落地**：查询编译器（声明式查询 → Step[] 执行计划）、增量视图维护（View Graph 拓扑序更新）、混合逻辑时钟（HLC）——这些是成熟的数据库技术，被成功移植到 TypeScript/浏览器环境
2. **端到端共享查询引擎**：客户端和服务端运行完全相同的 `EntityStoreQueryEngine`，只是底层 KV Store 不同（BTree/IndexedDB/SQLite/LMDB 等 7 种后端），这在 local-first 领域是独特的
3. **双缓冲同步协议**：`KVDoubleBuffer` 的 active/locked 切换让乐观更新和同步完全解耦，解决了「边写边发」的竞态问题——设计简单但极其有效

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/aspen-cloud/triplit |
| Star / Fork | 3,075 / 108 |
| 代码行数 | 86,011 行（TypeScript 91.6%，24 个 monorepo 子包） |
| 项目年龄 | 26 个月（首次提交 2023-07-20） |
| 开发阶段 | 活跃度骤降（2025-09 后提交接近零，核心风险） |
| 贡献模式 | 小团队（3 人核心占 89% commits，23 位贡献者） |
| 热度定位 | 中等热度（3K stars，npm 月下载 13.5 万） |
| 质量评级 | 代码[优秀] 文档[良好] 测试[中等] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Aspen Cloud，小型创业公司，3 人核心团队：Will Ernst（40.3% commits）、pbohlman（33.1%）、Matt Linkous（15.6%）。专注 local-first 实时数据库，在 Local First Web 社区中推广「Full Stack Database」概念。

### 问题判断

团队观察到 Web/移动开发中数据获取和同步代码占据了大量应用代码（fetch + cache + retry + offline + 实时更新），而 local-first 社区虽活跃但现有方案要么只解决客户端部分（RxDB），要么绑定特定后端（ElectricSQL → Postgres）。没有一个方案真正做到「同一个查询引擎跑在客户端和服务端」。

### 解法哲学

1. **查询引擎优先**：不是「给同步加查询能力」，而是「造一个真正的数据库引擎，让它可以在任何 JS 环境运行」
2. **增量视图维护（IVM）**：数据变更时不重新执行完整查询，而是增量更新已有结果——数据库领域的经典技术，被迁移到客户端实时场景
3. **Entity-level 重写**：从最初的 Triple Store 架构（项目名 「Triplit」 即来源于此）迁移到 Entity Store，认识到 entity-level 粒度对实际应用更实用

### 战略意图

「开源核心 + 托管服务」商业模式。AGPL-3.0 许可证推动商业用户使用托管方案。24 个包覆盖全栈能力（DB/Client/Server + React/Vue/Svelte/Angular/Solid/TanStack 绑定），试图成为 Firebase 的开源替代品。但开发活动停滞使战略执行存疑。

## 核心价值提炼

### 创新之处

1. **端到端共享查询引擎**（新颖度 5/5 | 实用性 5/5 | 可迁移性 3/5）
   客户端和服务端运行完全相同的 `EntityStoreQueryEngine`，查询编译器生成 SCAN/FILTER/SORT/LIMIT/SUBQUERY 等步骤的执行计划。其他方案通常是客户端一套逻辑、服务端另一套。

2. **View Graph 驱动的 IVM 实时查询**（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）
   `IVM` 类维护视图依赖图（View Graph），数据变更时按拓扑序增量更新受影响的视图节点。子查询被「抽取」为独立视图节点实现共享——多个查询依赖相同子查询时只维护一份视图。

3. **双缓冲同步协议**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   `KVDoubleBuffer` 的三层存储：确认数据 + locked buffer（等待发送）+ active buffer（当前写入）。客户端永远写入 active，同步引擎只发送 locked，ACK 后合并到 data store。解决了「边写边发」的竞态。

4. **权限即过滤器注入**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）
   将 RBAC 权限转化为查询 where 条件在 `prepareQuery()` 阶段注入。`ACCESS_DENIED_FILTER = [false]` 确保无权限时返回空结果而非抛错。比中间件拦截更优雅。

5. **Schema-as-Data 迁移检查**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）
   Schema 存储为 `_metadata._schema` 普通实体，`diffSchemas()` 不仅检测结构差异，还检查现有数据是否违反新约束。`compatibilityList` 允许客户端快速通过兼容性检查。

### 可复用的模式与技巧

1. **KV Store 跨平台抽象**：`KVStore` + `KVStoreTransaction` 接口 + 7 种后端实现（BTree/IndexedDB/SQLite/LMDB/Expo SQLite/Bun SQLite/Cloudflare DO），通过 `scope()` 实现命名空间隔离
2. **双缓冲写入模式**：`KVDoubleBuffer` 的 active/locked 切换可用于任何「边写边同步」场景（日志上报、分析事件批量发送等）
3. **查询编译器管道**：声明式查询 → 预处理（权限+变量）→ 编译（步骤计划）→ 执行的管道设计
4. **Session Proxy 模式**：`createSession()` 使用 `Proxy` 在不复制 DB 实例的情况下注入 session 上下文
5. **权限即过滤器**：将 RBAC 转为查询 where 条件的模式，适合行级安全（RLS）场景
6. **Checkpointed Query Sync**：客户端重连时发送 `QueryState`（时间戳 + 已知实体 ID），服务端只返回增量变更

### 关键设计决策

1. **自建查询引擎而非用 SQL**：TypeScript 原生查询编译器 + 步骤式执行，牺牲了 SQL 生态兼容性，换来了浏览器内运行和端到端类型安全。
2. **7 种 KV Store 后端**：同一引擎适配浏览器/Node/React Native/Edge Workers，牺牲了针对特定后端的优化机会。
3. **AGPL-3.0 许可证**：保护商业化路径但阻碍了社区采用，竞品（RxDB/ElectricSQL/InstantDB）全部使用 Apache-2.0。
4. **从 Triple Store 到 Entity Store 的迁移**：认识到 entity-level 粒度更实用，但遗留了命名混淆（项目名仍叫 Triplit）。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Triplit | RxDB | ElectricSQL | InstantDB |
|------|---------|------|-------------|-----------|
| 核心模型 | 自建 Entity Store + IVM | 可插拔后端 | Postgres 逻辑复制 | 自建 Triple Store |
| 查询引擎 | 客户端/服务端共享 | 仅客户端 | Postgres SQL | 仅客户端 Datalog |
| 存储后端 | 7 种 | 10+ 种 | Postgres only | 自管 |
| 框架绑定 | 6 个 | 3 个 | 1 个 | 1 个 |
| 许可证 | AGPL-3.0 | Apache-2.0 | Apache-2.0 | Apache-2.0 |
| Stars | 3K | 23K | 10K | 9.8K |

### 差异化护城河

- **技术护城河**：端到端共享查询引擎 + IVM 视图图是独特的技术方案，竞品难以快速复制
- **全栈覆盖**：从 DB 到 6 个框架绑定的完整覆盖，是唯一的「端到端全栈」开源方案

### 竞争风险

- **AGPL 许可证**是最大的商业采用障碍
- **开发停滞**（自 2025-09）使可靠性存疑，而竞品仍在活跃
- **社区规模差距**显著（3K vs 10-23K），生态和贡献者远少于竞品

### 生态定位

在 local-first 赛道中填补了「TypeScript 全栈同步数据库」的空白——不绑定 Postgres，不需要额外的后端 API，客户端和服务端共享查询引擎。

## 套利机会分析

- **信息差**: 中等。3K stars 但 npm 月下载 13.5 万，说明实际使用者比 star 数暗示的更多。IVM 和双缓冲同步的技术深度被低估。
- **技术借鉴**: KV Store 跨平台抽象（7 种后端）、双缓冲同步协议、查询编译器管道、权限即过滤器——这四个模式可直接迁移到其他项目。
- **生态位**: 「TypeScript 全栈同步数据库」这个定位独特且有需求，但开发停滞留下了空白。
- **趋势判断**: Local-first 是长期趋势，但 Triplit 的开发停滞是严重警告信号。如果团队不恢复活跃，生态位可能被 ElectricSQL 或新进入者占据。

## 风险与不足

1. **开发活动停滞**：自 2025-09 以来 commit 接近零，GitHub participation 近 12 周全部返回 0——核心风险
2. **AGPL-3.0 许可证**：三个主要竞品都是 Apache-2.0，AGPL 是商业采用的最大障碍
3. **sync-engine.ts 过于庞大**：1,200+ 行单文件，triplit-client.ts 1,000+ 行，应进一步拆分
4. **IVM 核心逻辑注释稀少**：`updateQueryResultsInPlace` 等关键函数缺少文档注释
5. **50+ TODO 注释**：表明有大量已知技术债务
6. **`structuredClone` 性能隐患**：`bufferChanges()` 中的使用在大数据量场景下可能成为瓶颈
7. **client/sync 层测试薄弱**：测试主要集中在 db 包，同步和客户端层覆盖不足

## 行动建议

- **如果你要用它**: 适合需要完整离线支持 + 实时同步 + 不想绑定 Postgres 的 TypeScript 全栈项目。但需密切关注开发活动是否恢复。如果 AGPL 不可接受，考虑 ElectricSQL（Postgres 绑定但 Apache-2.0）或 InstantDB。npm 月下载 13.5 万说明有实际生产使用。
- **如果你要学它**: 重点关注 `packages/db/src/` 下的四个核心模块：(1) `query-planner/query-compiler.ts`（查询编译器）；(2) `ivm/ivm.ts` + `ivm/view-graph.ts`（增量视图维护）；(3) `double-buffer.ts`（双缓冲同步）；(4) `entity-store-with-outbox.ts`（乐观更新三层存储）。这是学习「如何在浏览器中构建数据库引擎」的最佳代码。
- **如果你要 fork 它**: (1) 将许可证改为 Apache-2.0 以扩大采用；(2) 拆分 sync-engine.ts 和 triplit-client.ts；(3) 为 IVM 核心逻辑添加文档注释；(4) 优化 `structuredClone` 在大数据量场景的性能。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/aspen-cloud/triplit |
| Zread.ai | https://zread.ai/repo/aspen-cloud/triplit |
| 关联论文 | 无 |
| 在线 Demo | https://triplit.dev |
