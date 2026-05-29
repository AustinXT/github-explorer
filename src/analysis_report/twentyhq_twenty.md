# Twenty — 开源 CRM 的现代架构实验

> **仓库**: twentyhq/twenty | **Stars**: 27,000+ | **语言**: TypeScript 76.2% + TSX 22.0%
> **协议**: AGPL-3.0（核心）+ 商业许可（Enterprise 模块）| **公司**: Twenty PBC（YC S23）

---

## 动机与定位

- **要解决的问题**: CRM 市场被 Salesforce 垄断，价格高昂且数据锁定。中小企业被迫在「昂贵但功能齐全」和「免费但体验极差」之间做选择。
- **为什么现有方案不够**: SuiteCRM/EspoCRM 基于 PHP 技术栈，UI 停留在 2010 年代水平。Frappe CRM 功能有限。HubSpot 免费版引你入瓮后提价。没有一个开源 CRM 能提供 Notion/Airtable/Linear 级别的现代 UX。
- **目标用户**: 快速成长的中小企业、注重数据主权的组织、需要开发者友好型 CRM 的技术团队。

## 作者视角

### 问题发现

Charles Bochet（1,361 commits）为核心的法国团队在 CRM 领域发现了一个结构性矛盾：CRM 是企业最核心的数据系统，但最流行的产品（Salesforce）却用锁定策略对抗用户利益。这不仅是技术问题，更是商业模式问题——他们选择注册为 PBC（Public Benefit Corporation）来从法律层面绑定「用户利益优先」的承诺。

### 解法哲学

Twenty 的核心哲学是「客户数据的操作系统」——通过 Import → Customize → Automate 三步流程，将 CRM 从封闭的 SaaS 产品转变为可编程的数据平台。他们采用 AGPL 协议确保开源承诺，同时用 `@license Enterprise` 注解标记 222 个企业版文件，构建双轨商业模式。

### 背景知识迁移

YC S23 孵化带来的不只是资金，更是对「如何做一个开发者生态」的理解。项目中的 MCP Server 集成、Twenty Apps 平台、Client SDK 都体现了平台化思维——这在法国 SaaS 圈较少见，但在 YC 生态中是标配。

### 战略图景

Twenty 正在走一条「开源核心 + 企业增值」的经典路线，但技术选择极其激进——全 TypeScript、Nx monorepo、metadata-driven architecture。这不是渐进改良，而是从零构建一个 Salesforce 的现代替代品。AI Agent 集成（MCP Server、Workflow AI Agent）表明他们将 AI 视为下一代 CRM 的差异化竞争力。

---

## 架构与设计决策

### 目录结构概览

```
twenty/                              # Nx monorepo, 19 个 packages
├── packages/
│   ├── twenty-server/               # NestJS 后端（核心引擎）
│   │   └── src/
│   │       ├── engine/              # 引擎层（平台能力）
│   │       │   ├── api/             #   GraphQL + REST + MCP 三套 API
│   │       │   ├── core-modules/    #   70+ 核心模块（auth, billing, workflow...）
│   │       │   ├── metadata-modules/ #  元数据模块（动态 schema 驱动）
│   │       │   ├── twenty-orm/      #   自定义 ORM 层（workspace 感知）
│   │       │   └── workspace-*/     #   多租户工作区管理
│   │       └── modules/             # 业务模块层（CRM 域对象）
│   │           ├── company, person, opportunity  # 标准 CRM 对象
│   │           ├── connected-account, calendar   # 集成
│   │           └── workflow                     # 自动化工作流
│   ├── twenty-front/                # React 前端
│   │   └── src/modules/
│   │       ├── views/               # 视图系统（table/kanban/calendar/board）
│   │       ├── object-record/       # 通用记录 UI（30+ 子模块）
│   │       ├── object-metadata/     # 元数据驱动 UI
│   │       └── workflow/            # 工作流可视化编辑器
│   ├── twenty-ui/                   # 共享 UI 组件库（Storybook）
│   ├── twenty-shared/               # 前后端共享类型和工具
│   ├── twenty-apps/                 # 第三方 App 平台
│   ├── twenty-client-sdk/           # 客户端 SDK（自动生成）
│   ├── twenty-e2e-testing/          # Playwright E2E 测试
│   ├── twenty-docker/               # Docker + K8s + Helm 部署
│   └── twenty-companion/            # 桌面伴侣应用（会议录制）
```

### 关键设计决策

#### 1. 元数据驱动的动态 GraphQL Schema

- **决策**: 通过 `ObjectMetadataEntity` 和 `FieldMetadataEntity` 描述数据模型，运行时动态生成 GraphQL schema 和 TypeORM entity schema。
- **问题**: CRM 需要允许用户自定义对象和字段，但传统方案需要硬编码每个实体或使用 EAV 模式。
- **方案**: 三层元数据架构——`metadata-modules/` 定义元数据结构，`workspace-schema-builder` 根据 metadata 生成 GraphQL SDL，`entity-schema.factory` 根据 metadata 生成 TypeORM EntitySchema。每个 workspace 有独立的 PostgreSQL schema，物理隔离租户数据。
- **Trade-off**: 增加了系统复杂度（元数据层本身需要大量维护），但换来了完全的运行时可定制性和多租户隔离。
- **可迁移性**: 5/5 —— 任何需要运行时动态 schema 的 SaaS 平台都可以借鉴此模式。

#### 2. TwentyORM — Workspace 感知的自定义 ORM 层

- **决策**: 在 TypeORM 之上构建 `WorkspaceRepository<T>` 和 `WorkspaceEntityManager`，自动注入 workspace 隔离、权限检查、feature flag。
- **问题**: TypeORM 不原生支持多 schema 多租户，且需要细粒度的字段级权限控制。
- **方案**: `WorkspaceRepository` 继承 TypeORM `Repository`，重写 `createQueryBuilder` 返回 `WorkspaceSelectQueryBuilder`，自动附加权限过滤条件。通过 `WorkspaceSchemaManagerService` 管理表/列/索引/枚举/外键的 DDL 操作。
- **Trade-off**: 与 TypeORM 深度耦合，升级 TypeORM 版本风险高。但避免了重复造轮子，且权限控制与数据访问无缝集成。
- **可迁移性**: 4/5 —— 多租户 SaaS 的常见需求，模式可复用。

#### 3. 三套并行 API（GraphQL + REST + MCP）

- **决策**: 同时提供 GraphQL API（主 API）、REST API、MCP（Model Context Protocol）API。
- **问题**: 不同消费者需要不同的 API 风格——前端用 GraphQL，第三方集成用 REST，AI Agent 用 MCP。
- **方案**: GraphQL 通过 `WorkspaceSchemaFactory` 动态生成 schema + resolver；REST 通过 `RestApiModule` 提供；MCP 通过 `McpProtocolService` 实现 JSON-RPC 协议，内建 `get_tool_catalog → learn_tools → execute_tool` 三步工作流。MCP Server 排除了 `code_interpreter` 和 `http_request` 等敏感工具。
- **Trade-off**: 三套 API 的维护成本高，但覆盖了所有消费场景，尤其是 MCP 的 AI Agent 集成是前瞻性布局。
- **可迁移性**: 3/5 —— MCP 集成模式可直接用于任何需要 AI Agent 访问的 SaaS。

#### 4. Nx Monorepo + Yarn 4 Workspaces

- **决策**: 使用 Nx 管理 19 个 packages，Yarn 4 作为包管理器。
- **问题**: 前后端 + SDK + 部署配置 + E2E 测试需要统一管理，同时保持各包独立构建和发布。
- **方案**: `workspaceLayout` 将 apps 和 libs 都放在 `packages/` 下。Nx 的 `targetDefaults` 定义了 build/lint/test/typecheck/storybook 等标准化任务，支持缓存和增量构建。自定义 `lint:diff-with-main` 任务只检查变更文件。
- **Trade-off**: 学习曲线陡峭，新人上手成本高。但换来了一致性和高效的 CI/CD。
- **可迁移性**: 4/5 —— 适合任何中大型全栈项目。

#### 5. 工作流引擎

- **决策**: 构建完整的可视化工作流引擎，支持 Trigger → Step → Action 链式执行。
- **问题**: CRM 自动化是核心需求（邮件触发、状态变更、数据同步）。
- **方案**: 四层架构——`workflow-builder`（可视化编辑器后端）、`workflow-trigger`（事件触发器，支持自动化触发）、`workflow-runner`（执行引擎，基于 BullMQ 队列）、`workflow-executor`（步骤执行器）。支持的 Action 类型包括：AI Agent、Code、HTTP Request、If/Else、Iterator、Filter、Form、Mail Sender、Record CRUD 等 12 种。
- **Trade-off**: 工作流引擎是系统中最复杂的部分，测试和维护成本极高。但这是对标 Salesforce Flow 的必要投入。
- **可迁移性**: 4/5 —— 通用的工作流引擎模式，可用于任何需要自动化的 SaaS。

#### 6. 双轨许可模式

- **决策**: 核心代码 AGPL-3.0，企业功能用 `/* @license Enterprise */` 注解标记（222 个文件）。
- **问题**: 需要同时满足开源社区贡献和商业变现。
- **方案**: Enterprise 模块包括 billing、SSO、enterprise key validation 等。运行时通过 `EnterpriseModule` 和 `EnterprisePlanService` 检查许可证有效性。
- **Trade-off**: 社区可能对「开源但部分功能需要付费」有争议，但这是 YC 公司的现实选择。
- **可迁移性**: 3/5 —— Open Core 模式的标准实现。

---

## 创新点

### 1. MCP Server 的渐进式工具发现协议 — 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

Twenty 实现了一个精心设计的 MCP Server，其工具发现协议分为三步：`get_tool_catalog`（发现可用工具）→ `learn_tools`（获取工具的描述和输入 schema）→ `execute_tool`（执行工具）。还支持 `load_skill` 加载预定义技能（如创建工作流或仪表板的向导）。这种设计避免了 AI Agent 一次性加载所有工具信息的 token 浪费，是 MCP 协议的最佳实践。

### 2. 元数据驱动的全栈动态 Schema — 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5

从 `FieldMetadataEntity` 的类型定义到 `EntitySchemaFactory` 的 TypeORM schema 生成，再到 `WorkspaceSchemaFactory` 的 GraphQL schema 生成，整个数据模型在运行时完全由元数据驱动。这意味着用户可以创建自定义对象、添加自定义字段，前后端自动适配——无需任何代码变更。

### 3. Twenty Apps 平台 — 新颖度 3/5 | 实用性 4/5 | 可迁移性 3/5

提供 `create-twenty-app` 脚手架和 `twenty-client-sdk`（自动生成的类型安全 API 客户端），允许第三方开发者构建 Twenty 应用。已有 `hello-world`、`postcard`、`call-recording`（集成 Recall.ai 的会议录制）等示例。这是走向「CRM App Store」的基础设施。

### 4. Workspace Schema 物理隔离 — 新颖度 2/5 | 实用性 5/5 | 可迁移性 4/5

每个 workspace 使用独立的 PostgreSQL schema（通过 `getWorkspaceSchemaName` 生成），而非共享表加 tenant_id 列。`WorkspaceSchemaManagerService` 管理表、列、索引、枚举、外键的完整生命周期。DDL 操作有锁保护（`assertDDLNotLocked`），支持热升级场景。

### 5. AI Agent 工作流步骤 — 新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5

Workflow 引擎中的 `ai-agent` action 类型允许工作流中嵌入 AI Agent 执行。配合 `ai-agent-execution`、`ai-agent-monitor`、`ai-agent-role` 等元数据模块，构建了一个完整的 AI Agent 执行和监控框架。这是将 AI 深度集成到业务流程而非仅作为聊天机器人的典型案例。

---

## 可复用模式

### 1. 元数据驱动的动态 API 生成

**模式**: 将业务实体的 schema 定义为元数据（数据库表），运行时根据元数据生成 API schema（GraphQL SDL + resolver）和数据访问层（TypeORM EntitySchema）。

**适用场景**: 任何需要运行时自定义数据模型的 SaaS 平台（CMS、Form Builder、Low-Code 平台）。

**关键代码路径**:
- `/packages/twenty-server/src/engine/metadata-modules/object-metadata/object-metadata.entity.ts`
- `/packages/twenty-server/src/engine/metadata-modules/field-metadata/field-metadata.entity.ts`
- `/packages/twenty-server/src/engine/api/graphql/workspace-schema.factory.ts`
- `/packages/twenty-server/src/engine/twenty-orm/factories/entity-schema.factory.ts`

### 2. MCP 渐进式工具发现

**模式**: AI Agent 工具发现分步进行——先目录、再 schema、再执行——而非一次性暴露所有工具。

**适用场景**: 任何需要 AI Agent 集成的 SaaS 产品。

**关键代码路径**:
- `/packages/twenty-server/src/engine/core-modules/tool-provider/tools/`
- `/packages/twenty-server/src/engine/api/mcp/services/mcp-protocol.service.ts`

### 3. 多租户 Schema 物理隔离 + 权限注入

**模式**: 每个租户独立 PostgreSQL schema，ORM 层自动注入 workspace 隔离和权限过滤。

**适用场景**: 多租户 SaaS，特别是需要强数据隔离的 B2B 产品。

**关键代码路径**:
- `/packages/twenty-server/src/engine/twenty-orm/repository/workspace.repository.ts`
- `/packages/twenty-server/src/engine/twenty-orm/workspace-schema-manager/workspace-schema-manager.service.ts`

### 4. Open Core 双轨许可实现

**模式**: 通过文件头注解 `/* @license Enterprise */` 标记商业代码，运行时检查许可证。

**适用场景**: 希望同时开源和商业化的项目。

---

## 竞品交叉分析

### vs SuiteCRM（5,347 stars）

| 维度 | Twenty | SuiteCRM |
|------|--------|----------|
| 技术栈 | TypeScript/React/NestJS | PHP/SugarCRM 遗产 |
| UI/UX | Notion 级别现代 UI | 传统企业 UI |
| 可定制性 | 元数据驱动，运行时动态 | PHP 代码级定制 |
| 部署 | Docker/K8s/Helm | 传统 LAMP |
| 社区 | YC 背书，增长快 | 长期积累，稳定 |
| 成熟度 | 40 个月，v1.20.6 | 10+ 年，功能完整 |

**结论**: Twenty 在技术栈和 UX 上碾压 SuiteCRM，但在 CRM 功能深度（高级报表、复杂工作流、行业解决方案）上仍需追赶。

### vs EspoCRM（2,857 stars）

二十的差异化在于元数据驱动的动态 schema 和 MCP AI 集成。EspoCRM 更成熟但技术栈陈旧。

### vs Frappe CRM（2,507 stars）

Frappe 依托 Frappe/ERPNext 生态，功能覆盖更广（含 ERP）。Twenty 更专注 CRM 领域，UX 更现代。

### vs HubSpot CRM（闭源）

HubSpot 在营销自动化和内容管理方面远超 Twenty。Twenty 的优势在于开源免费、数据主权、可定制性。

### vs Salesforce（闭源）

Salesforce 是行业标准，有完整的生态系统（AppExchange、Sales Cloud、Service Cloud 等）。Twenty 还处于对标基础功能的阶段，但在 MCP AI 集成方面展现了差异化方向。

### 综合竞争结论

Twenty 在开源 CRM 赛道具有最强的技术基础（现代 TypeScript 全栈、元数据驱动架构）和最大的社区（27,000+ stars）。其核心竞争优势是「现代 UX + 开源免费 + AI 原生」。风险在于 CRM 功能深度仍需大量投入才能满足企业级需求。AI Agent 集成方向正确，但需要更多实际应用场景验证。

---

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | A | 严格 TypeScript（禁止 any），oxlint 自定义规则，命名规范清晰（禁止缩写），文件大小限制（组件 300 行/服务 500 行）。自定义 oxlint 插件 `twenty-oxlint-rules`。 |
| 文档质量 | A | 完整的 CLAUDE.md 开发指南，Nx workspace 配置清晰，代码注释关注 WHY 而非 WHAT。`.cursor/rules/` 提供详细的开发规范。 |
| 测试覆盖 | B+ | Server 498 个测试文件，Front 607 个测试文件，合计 1,105 个。无 integration-spec 文件（集成测试通过 CI 中直接启动服务完成）。E2E 测试使用 Playwright。Storybook 组件测试通过 Chromatic 进行视觉回归。测试策略为 70% unit / 20% integration / 10% E2E。 |
| CI/CD | A | 30+ GitHub Actions workflows，包括 per-package CI（server/front/ui/docs/sdk）、视觉回归测试、国际化同步、preview 环境、CD deploy。支持 merge queue 和 breaking changes 检测。 |
| 错误处理 | B+ | 全局 `UnhandledExceptionFilter`，细粒度的业务异常（`WorkspaceDataSourceException`、`PermissionsException` 等），使用 `@lingui/core` 的 `msg` 标记用户友好的错误消息以支持 i18n。 |
| 架构一致性 | A | 三层分离清晰：engine（平台能力）→ metadata-modules（元数据）→ modules（业务逻辑）。每个模块遵循一致的目录结构（constants/dtos/services/types/utils）。 |

---

## 总结

Twenty 是一个技术野心极大的项目——它不是在现有 CRM 上改良，而是用现代技术栈从零构建一个平台级的 CRM 基础设施。其元数据驱动的动态 schema 生成、Workspace 感知的自定义 ORM、MCP Server 的渐进式工具发现这三个设计决策，构成了一个完整的「CRM 操作系统」技术栈。

项目最大的风险在于复杂度——metadata-driven architecture 本身的维护成本极高，且团队需要在平台建设和 CRM 功能深度之间分配有限的资源。但从 40 个月 11,252 commits、387 个版本的节奏来看，团队的执行力足以支撑这个野心。

对于技术学习者，Twenty 是研究「如何构建一个现代 SaaS 平台」的极佳案例——从多租户数据隔离到动态 API 生成，从 AI 集成到双轨商业模式，几乎涵盖了构建企业级 SaaS 的所有关键决策。
