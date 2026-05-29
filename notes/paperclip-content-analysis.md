## 动机与定位

- **要解决的问题**: 当你用 20 个 Claude Code 终端、若干 Codex 实例、几个 Cursor 窗口同时处理业务时，你面对的不再是「怎么让一个 Agent 更好」的问题，而是「怎么让一群 Agent 像公司一样运转」的问题——谁在做什么、花了多少钱、目标对齐了没、出问题谁负责、重启后状态还在不在。Paperclip 要解决的就是这个「AI Agent 公司化运营」的编排、治理和可观测性问题。
- **为什么现有方案不够**: CrewAI、AutoGen、LangGraph 等框架解决的是「Agent 之间如何对话/协作」的底层编排问题——它们是构建 Agent 的工具，而不是运营 Agent 团队的工具。它们没有组织架构（Org Chart）、没有预算控制、没有审批门禁、没有持久化的任务系统和审计日志。用它们管理 20 个 Agent，就像用消息队列来管理一个公司——技术上可行，产品上不够。
- **目标用户**: 技术型创业者（solo-entrepreneur）、同时运营多个 AI Agent 做实际业务的开发者、想要构建「零人公司」的早期探索者。核心画像是：已经在用 Claude Code / Codex / Cursor 做事，但发现手动协调多个 Agent 已不可持续的人。

## 作者视角

### 问题发现
Dotta（核心开发者，1,152 commits）的背景是 Web3/NFT 领域的连续创业者——他创建了 Forgotten Runes Wizards Cult（知名 NFT 项目）和 ERC721 软件许可协议 Dotlicense。从「管理去中心化数字资产」到「管理去中心化 AI 劳动力」，这个问题发现过程是自然的迁移：当你真的试图让 AI Agent 代替人类员工做业务时，你发现缺的不是更好的 Agent，而是更好的「公司操作系统」。项目的口号——「Manage business goals, not pull requests」——直接反映了这种从实际运营中提炼出的需求。

### 解法哲学
Paperclip 的核心哲学是**「控制平面，而非执行平面」**（Control Plane, not Execution Plane）。它不告诉你怎么构建 Agent，它告诉你怎么运行一个由 Agent 组成的公司。这个哲学选择带来了几个关键推论：

1. **Agent 不可知论**——只要能接收心跳信号，就能被「雇用」（If it can receive a heartbeat, it's hired）
2. **公司隐喻即架构**——Org Chart、预算、审批门禁、治理 不是比喻，是实际的数据模型和执行约束
3. **人类始终是董事会**——Board Operator 拥有不受限制的干预权，可以在任何层级任何时间介入

### 背景知识迁移
Dotta 从 Web3 领域带来了几个关键的跨域 insight：

- **治理即代码**: Web3 世界里 DAO 的治理机制（投票、提案、执行）被迁移为 Paperclip 的 Board Approval Gates
- **Token 经济学 → Token 预算学**: 加密资产的精确计量思维被应用到 LLM token 消耗的预算控制——月度预算、硬止损、自动暂停
- **可组合性**: Web3 的「乐高积木式组合」思想体现在 Paperclip 的 Adapter 架构——任何 Agent 运行时都可以通过适配器接入

### 战略图景
Paperclip 的 GOAL.md 直接写明了终极愿景：「Paperclip-powered companies to collectively generate economic output that rivals the GDP of the world's largest countries」。这不是一个工具项目，而是一个平台项目。Paperclip → ClipMart（公司模板市场）→ 云部署 → 自治经济层。Dotta 想做的是「自治公司的 AWS」——你在上面创建公司就像在 AWS 上启动实例。

## 架构与设计决策

### 目录结构概览
标准 pnpm monorepo 架构，清晰的分层：

```
paperclip/
├── server/        — Express REST API + 编排服务（核心）
├── ui/            — React + Vite 前端（Board 操作界面）
├── packages/
│   ├── db/        — Drizzle ORM schema + 迁移（PostgreSQL）
│   ├── shared/    — 跨层类型、校验器、常量
│   ├── adapter-utils/   — Adapter 接口定义
│   ├── adapters/  — 8 个内置 Adapter（Claude/Codex/Cursor/Gemini/OpenCode/Pi/Hermes/OpenClaw）
│   └── plugins/   — 插件 SDK + 示例插件
├── skills/        — Agent Skill（Paperclip 心跳协议）
├── cli/           — CLI 客户端
└── doc/           — 设计文档（70+ 文件，43,000+ 行 Markdown）
```

### 关键设计决策

1. **决策**: 「Company-Scoped Everything」——所有业务实体都强制归属一个 Company
   - 问题: 多公司运行在同一实例上时，如何保证数据隔离
   - 方案: 数据库层面 `company_id` 贯穿所有核心表（agents、issues、goals、projects、approvals、costs），路由层面强制 company access check
   - Trade-off: 增加了每次查询的 JOIN 成本和开发时的心智负担，换来了真正的多租户隔离能力
   - 可迁移性: 高——任何多租户 SaaS 都可以采用此模式

2. **决策**: 原子任务签出（Atomic Issue Checkout）
   - 问题: 多个 Agent 可能同时尝试认领同一个任务
   - 方案: `POST /api/issues/{id}/checkout` 使用数据库级原子操作，409 Conflict 直接拒绝，不重试。Issue 表中 `checkout_run_id` 字段与 `execution_locked_at` 时间戳绑定
   - Trade-off: 简单直接，但不支持协作式任务（两个 Agent 合作完成一个 Issue）；优先保证不做重复工作
   - 可迁移性: 高——任何需要分布式任务分配的系统都适用

3. **决策**: Adapter 作为可插拔的三层模块（Server + UI + CLI）
   - 问题: 不同 Agent 运行时（Claude Code、Codex、Cursor、HTTP webhook）有完全不同的调用方式、输出格式和配置需求
   - 方案: 每个 Adapter 包含三个模块——Server 侧的 `execute()`/`testEnvironment()`/`sessionCodec()`/`listSkills()`，UI 侧的 stdout 解析器和配置表单，CLI 侧的终端格式化。通过 `ServerAdapterModule` 接口统一注册到 Mutable Registry（支持运行时外部插件覆盖内置 Adapter）
   - Trade-off: 接口较重（一个完整 Adapter 需要实现 10+ 个可选函数），但换来了真正的「Any Agent, Any Runtime」
   - 可迁移性: 中——适用于需要对接多种执行引擎的编排系统

4. **决策**: 嵌入式 PostgreSQL（PGlite）作为默认开发模式
   - 问题: 开发者不想为了试用一个项目去安装和配置 PostgreSQL
   - 方案: 当 `DATABASE_URL` 未设置时，自动启动嵌入式 PostgreSQL，数据存储在 `~/.paperclip/instances/default/db`
   - Trade-off: 开发体验极佳（`pnpm dev` 即启动），但嵌入式 PG 在生产环境不推荐使用
   - 可迁移性: 高——任何需要数据库的本地工具都可以采用此模式

5. **决策**: 心跳（Heartbeat）协议而非常驻进程
   - 问题: Agent 不应该也不需要持续运行——它们需要被唤醒、做事、退出
   - 方案: 心跳触发源包括定时器、任务分配、@提及、手动触发、审批决议。Agent 在每次心跳中执行标准流程：身份确认 → 获取分配 → 签出任务 → 理解上下文 → 做事 → 更新状态 → 委派子任务
   - Trade-off: 增加了上下文重建成本（每次心跳需要重新获取状态），但换来了资源效率和更好的审计能力
   - 可迁移性: 高——适用于任何周期性执行的 Agent 系统

6. **决策**: 插件系统采用 Worker 进程隔离 + Capability-Based 权限
   - 问题: 如何让第三方扩展 Paperclip 功能而不破坏核心治理
   - 方案: 插件通过 manifest 声明 capabilities，运行在独立 Worker 进程中，通过 RPC 与主进程通信。完整的生命周期状态机（installed → ready → disabled → error → uninstalled）
   - Trade-off: 隔离带来的安全性换取了插件与宿主之间的通信延迟
   - 可迁移性: 中——适用于需要扩展系统的平台型产品

## 创新点

1. **「公司隐喻」作为一等架构**
   - 描述: 不是把公司比喻用在文档里，而是把 Org Chart、报告线、预算、审批门禁、董事会治理直接编码为数据模型和 API 约束。Agent 有老板、有职称、有工作描述、有月薪（预算）。这种做法在 AI Agent 编排领域是独特的。
   - 新颖度: 5/5 | 实用性: 4/5 | 可迁移性: 3/5
   - 适用场景: 任何需要对 AI Agent 进行层级化、治理化管理的场景

2. **可移植公司模板（Company Portability）**
   - 描述: 整个公司——包括组织架构、Agent 配置、技能、项目、甚至种子任务——可以导出为一个可移植的 JSON manifest，然后导入到另一个 Paperclip 实例中。支持模板导出（只有结构）和快照导出（结构+状态），处理了 slug 碰撞、secret 擦洗等边缘情况。
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 4/5
   - 适用场景: 任何需要「复制整套配置」的平台型产品——从基础设施即代码到 SaaS 模板市场

3. **心跳协议 + Session 持续性**
   - 描述: Agent 通过心跳被唤醒，但 session 在心跳之间是持久化的——`session_id_before` 和 `session_id_after` 被记录在 `heartbeat_runs` 表中，Agent 可以在下次心跳中恢复上下文而非从零开始。配合 `SessionCompactionPolicy`，还支持上下文压缩策略。
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 4/5
   - 适用场景: 任何间歇性执行的 Agent 系统

4. **Adapter Override 热替换**
   - 描述: 外部 Adapter 插件可以在运行时覆盖内置 Adapter，且支持 pause/resume。覆盖时保留 builtin fallback，暂停时自动回退。这使得 Adapter 的升级和实验变得安全。
   - 新颖度: 3/5 | 实用性: 4/5 | 可迁移性: 3/5
   - 适用场景: 需要支持运行时插件热替换的扩展系统

5. **执行工作区（Execution Workspace）管理**
   - 描述: Agent 的工作不是在「某个目录」中进行，而是在受管理的工作区中进行——支持 Git Worktree 自动创建、运行时服务（如 dev server）的生命周期管理、工作区继承（follow-up issue 继承父 issue 的工作区）。
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 3/5
   - 适用场景: AI 编码 Agent 需要在真实代码仓库中工作的场景

## 可复用模式

1. **Mutable Registry with Builtin Fallback**: Adapter Registry 采用 `Map<string, Module>` + `builtinFallbacks Map` + `pausedOverrides Set` 的三层结构，支持运行时注册/注销/覆盖/暂停/恢复——适用场景: 任何需要支持插件覆盖内置实现的注册表系统
2. **Atomic Checkout Pattern**: 通过数据库原子操作 + HTTP 409 Conflict 实现单一 assignee 任务签出——适用场景: 分布式任务队列、工单系统
3. **Heartbeat-as-Protocol**: 将 Agent 执行定义为「被触发的短窗口」而非「常驻进程」，配合 session 持久化实现跨心跳的上下文延续——适用场景: 定时任务驱动的 Agent 系统
4. **Company-Scoped Multi-Tenancy**: 所有表带 `company_id`，路由层强制检查——适用场景: 任何多租户 SaaS
5. **Plugin Lifecycle State Machine**: 完整的 `installed → ready → disabled → error → upgrade_pending → uninstalled` 状态机 + Worker 进程隔离——适用场景: 需要可靠插件管理的平台
6. **Embedded DB for Zero-Config Dev**: 检测 `DATABASE_URL` 是否设置，未设置则自动启动嵌入式 PGlite——适用场景: 任何需要 PostgreSQL 但希望零配置启动的本地工具

## 竞品交叉分析

### vs CrewAI
- Paperclip 更好: 真正的公司级治理（Org Chart、预算硬止损、审批门禁、审计日志）；持久化状态和任务系统；多公司隔离；Web UI 运营界面
- CrewAI 更好: 更轻量、更快上手；对单次多 Agent 协作任务的表达力更强（角色定义 + 任务编排更简洁）；更成熟的社区生态（48K stars）
- 不同目标: CrewAI 是「用 Agent 组队完成一个任务」的框架；Paperclip 是「用 Agent 组建一个持续运营的公司」的平台
- 用户迁移成本: 高——两者不是替代关系而是不同层级，可以在 Paperclip 内通过 Adapter 使用 CrewAI Agent

### vs AutoGen
- Paperclip 更好: 产品化程度远超（完整 UI、CLI、Docker 部署）；面向业务运营而非研究实验；预算控制和成本追踪
- AutoGen 更好: 更强的 Agent 间对话编排能力；微软背书和学术生态；更多的 Agent pattern 支持
- 不同目标: AutoGen 是多 Agent 对话研究框架；Paperclip 是 Agent 公司运营平台
- 用户迁移成本: 低——可以通过 HTTP Adapter 将 AutoGen Agent 接入 Paperclip

### vs LangGraph
- Paperclip 更好: 开箱即用的完整产品（不需要写代码来定义工作流）；公司级治理和预算控制；持久化任务管理
- LangGraph 更好: 更灵活的图式工作流定义；更底层的控制能力；与 LangChain 生态深度集成
- 不同目标: LangGraph 是构建 Agent 工作流的库；Paperclip 是管理 Agent 团队的应用
- 用户迁移成本: 低——LangGraph Agent 可以通过 HTTP Adapter 接入 Paperclip

### vs Dify
- Paperclip 更好: 专注多 Agent 公司编排而非通用 LLM 应用；组织架构和治理模型；真正的多 Agent 协调（不只是流水线）
- Dify 更好: 更成熟的产品（70K+ stars）；更广泛的 LLM 应用场景支持（RAG、工作流、知识库）；更好的可视化工作流编辑器
- 不同目标: Dify 是「构建 AI 应用」的平台；Paperclip 是「运行 AI 公司」的控制平面
- 用户迁移成本: 高——完全不同的产品思路，互补大于竞争

### 综合竞争结论
- **差异化护城河**: 「公司隐喻作为一等架构」这个定位在目前的 Agent 编排领域是独特的。竞品都在做「Agent 框架」，Paperclip 在做「Agent 公司的操作系统」。这不仅是定位差异，而是架构差异——Org Chart、Budget、Approval、Governance 深入数据模型和 API 约束。
- **竞争风险**: CrewAI 或 LangGraph 如果向上层应用演进，可能会侵入 Paperclip 的领地。Dify 如果增加多 Agent 组织管理功能也会形成竞争。但复制整个公司治理模型的成本很高。
- **生态定位**: Paperclip 不与 Agent 框架竞争，而是在它们之上提供管理层——通过 Adapter 机制可以将任何框架构建的 Agent 接入。这使得 Paperclip 在生态中处于「编排层」而非「框架层」。

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | ⭐⭐⭐⭐ | TypeScript strict mode，清晰的分层架构，Drizzle ORM 类型安全，pnpm workspace 组织。无 linter/formatter 配置文件是一个缺失 |
| 文档质量 | ⭐⭐⭐⭐⭐ | 43,000+ 行 Markdown，设计文档覆盖从 GOAL 到 SPEC 到 Implementation 到 Plugin Spec。doc/plans/ 下有 20+ 个带日期的计划文档。外部文档站（docs/）使用 Mintlify |
| 测试覆盖 | ⭐⭐⭐⭐ | 111 个 server 测试文件 + 41 个 UI 测试文件 + 14 个 packages 测试文件 + E2E 测试（Playwright）+ Release Smoke 测试 + Promptfoo 评估。覆盖面广 |

### 质量检查清单
- [x] 有测试（166+ 测试文件，含单元/E2E/release smoke/LLM evals）
- [x] 有 CI/CD 配置（6 个 GitHub Actions workflow: pr.yml / e2e.yml / release.yml / docker.yml / release-smoke.yml / refresh-lockfile.yml）
- [x] 有文档（内部 doc/ + 外部 docs/ Mintlify 站点 + AGENTS.md + CONTRIBUTING.md）
- [x] 错误处理规范（统一的 conflict/notFound/unprocessable 错误工厂 + HTTP 状态码约定）
- [ ] 有 linter/formatter 配置（未发现 ESLint / Prettier / Biome 配置文件）
- [x] 有 CHANGELOG（11 个包各自维护 CHANGELOG + releases/ 目录下的版本发布说明）
- [x] 有 LICENSE（MIT）
- [x] 有示例代码（4 个插件示例: hello-world / file-browser / kitchen-sink / authoring-smoke）
- [x] 依赖版本锁定（pnpm-lock.yaml，12,293 行；packageManager 字段锁定 pnpm@9.15.4）
