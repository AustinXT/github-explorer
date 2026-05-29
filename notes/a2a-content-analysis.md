# A2A (Agent-to-Agent Protocol) 内容分析

> 仓库: [a2aproject/A2A](https://github.com/a2aproject/A2A) | 22.7K Star | v1.0.0 GA (2026-03-12)

---

## 动机与定位

**核心问题**：AI Agent 生态碎片化。各框架（LangGraph、CrewAI、ADK、AutoGen）构建的 Agent 无法互相通信，只能通过将 Agent 包装成 Tool 来勉强协作，这严重限制了 Agent 的自主性和多轮对话能力。

**定位决策**：A2A 明确选择了"Agent-to-Agent"而非"Agent-to-Tool"的定位，与 MCP（Anthropic）形成互补关系：
- **MCP = Agent-to-Tool**：连接 Agent 与数据源/工具，无状态、结构化输入输出
- **A2A = Agent-to-Agent**：Agent 作为对等实体（peer）协作，有状态、多轮对话、任务追踪

这个"Agents Are Not Tools"的核心洞察是协议设计的哲学基石。文档中反复强调 Agent 是"不透明的"（opaque）——协作双方无需暴露内部状态、记忆或工具实现。

**协议层次**：三层架构设计清晰分离关注点：
1. **Layer 1 - Canonical Data Model**：Protobuf 定义的核心数据结构（协议无关）
2. **Layer 2 - Abstract Operations**：抽象操作语义（11 个核心操作）
3. **Layer 3 - Protocol Bindings**：具体传输绑定（JSON-RPC / gRPC / HTTP+JSON）

---

## 作者视角

### 核心团队画像

**治理结构**：TSC（技术指导委员会）8 席位，代表科技行业最强阵容：
| 公司 | 角色 |
|------|------|
| Google | 发起者，Todd Segal（Principal Engineer）主导 |
| Microsoft | Darrel Miller（Partner API Architect）—— 深厚的 API 标准化经验 |
| Cisco | 网络协议基因 |
| AWS / Salesforce / ServiceNow / SAP / IBM Research | 企业级需求代言人 |

**设计思维来源**：从 TSC 构成可以看出 Google API Design Guide 的深刻影响：
- `a2a.proto` 使用 `google.api.annotations` / `google.api.field_behavior`
- 错误模型采用 `google.rpc.Status` + `google.rpc.ErrorInfo`
- 命名遵循 Google AIP（API Improvement Proposals）
- gRPC 优先的设计思路（proto 为 normative source of truth）

**SDK 维护者分布**：
- Python SDK 维护者最多（14 人 maintain + 6 admin），是核心实现
- .NET SDK 由 Microsoft 贡献者主导（含 @stephentoub 等知名 .NET 开发者）
- Java SDK 有 Red Hat 工程师参与（@fjuma, @kabir）
- 这说明协议已获得多家大厂实质性投入

### 设计哲学

作者团队在文档中反复强调五个设计原则：
1. **Simple**：复用 HTTP/JSON-RPC/SSE 等成熟标准
2. **Enterprise Ready**：认证/授权/隐私/追踪对齐企业实践
3. **Async First**：原生支持长时间运行任务和 human-in-the-loop
4. **Modality Agnostic**：支持文本/文件/结构化数据/多媒体
5. **Opaque Execution**：Agent 无需暴露内部实现

---

## 架构与设计决策

### ADR-001：ProtoJSON 序列化（2025-11-18）

这是目前唯一正式发布的 ADR，但极为重要：

**决策**：采用 ProtoJSON 作为 JSON 序列化的规范标准。

**争议点**：
- Enum 值从 `kebab-case` 变为 `SCREAMING_SNAKE_CASE`（如 `"completed"` → `"TASK_STATE_COMPLETED"`），开发者不习惯
- 丧失 roundtrip 能力（ProtoJSON 不保留未知字段）
- 某些字段名受 proto 关键字限制而不够直观

**为什么仍选择 ProtoJSON**：
- 跨语言工具链支持成熟
- 消除手动定义日期/数字等类型处理规则的需要
- 确定性的演进路径

**影响**：这是 v0.3 → v1.0 最大的 breaking change 来源，说明团队愿意为长期一致性牺牲短期兼容性。

### Proto 作为 Single Source of Truth

`specification/a2a.proto`（796 行）是**唯一的规范性定义**。JSON Schema 和 SDK 类型都从它生成：

```
a2a.proto → (buf 工具链) → 多语言 SDK 类型 / JSON Schema / 文档表格
```

这个决策的深远影响：
- 使用 `buf.yaml` 进行 lint 和 breaking change 检测
- 协议中立性——gRPC/REST/JSON-RPC 都是平等的 binding
- 减少规范偏移（specification drift）

### 核心数据模型设计

**Task 状态机**（8 个状态，3 类）：
```
起始: SUBMITTED → WORKING
终态: COMPLETED | FAILED | CANCELED | REJECTED
中断: INPUT_REQUIRED | AUTH_REQUIRED
```

关键设计决策：
- **Task 不可变性**：终态后不可重启，新交互必须创建新 Task。这大大简化了实现和追踪。
- **contextId 分组**：多个 Task 可通过 contextId 关联，实现"一次对话，多个任务"的范式
- **Message vs Task 二分法**：简单交互返回 Message（无状态），复杂交互返回 Task（有状态）

**Part 的统一化重设计**（v1.0 重大变更）：
- v0.3: TextPart / FilePart / DataPart 三种类型 + `kind` 鉴别器
- v1.0: 单一 `Part` message，用 `oneof content { text, raw, url, data }` 区分
- 去掉 `kind` 字段，改用 JSON 成员名判断类型（member-based discrimination）

### Agent Card：去中心化发现机制

Agent Card 是协议中最巧妙的设计之一。它借鉴了多个成熟模式：
- **Well-Known URI**（RFC 8615）：`/.well-known/agent-card.json`——类似 OAuth 的 `.well-known/openid-configuration`
- **自描述能力声明**：类似 OpenAPI spec，但面向 Agent 而非 API
- **JWS 签名验证**（RFC 7515 + RFC 8785 JCS）：确保 Agent Card 完整性
- **Extended Agent Card**：认证后可获取更详细的能力描述——分层信息披露

**v1.0 的关键重构**：`supportedInterfaces[]` 替代了原来的 `url` + `preferredTransport`，每个 interface 独立指定 protocol binding 和 protocol version，支持同一 Agent 同时暴露多种协议。

### 安全模型

安全设计遵循"不发明新标准"原则：
- **传输层**：HTTPS 强制要求（生产环境）
- **认证**：委托给标准 HTTP 机制（OAuth2 / OIDC / API Key / mTLS）
- **SecurityScheme 对齐 OpenAPI 3.2**：直接复用了 OpenAPI 的安全方案定义
- **v1.0 现代化**：移除 Implicit/Password OAuth 流（已被 OAuth BCP 废弃），新增 Device Code 流 + PKCE 支持
- **Push Notification 安全**：完整的 SSRF 防护指南 + JWT/JWKS 认证流

### 多租户支持

v1.0 新增 `tenant` 字段到所有请求消息，实现原生多租户：
- 每个 `AgentInterface` 可指定默认 tenant
- 支持单一端点服务多个 Agent 实例
- 这对企业 SaaS 部署至关重要

---

## 创新点

### 1. "Opaque Agent" 范式
与传统的微服务 API 设计不同，A2A 将 Agent 视为黑盒。不需要了解对方的 prompt、memory、tools。这是一个真正面向 Agent 时代的协议设计哲学，而非简单地复用 REST/RPC 模式。

### 2. 三种更新交付机制的统一
Polling（GetTask）+ Streaming（SSE）+ Push Notification（Webhook）三种机制共用同一套 `StreamResponse` 数据模型。这使得客户端可以根据场景灵活选择而不需要处理不同的数据格式。

### 3. Extension 机制的治理框架
Extension 不仅仅是技术扩展点，还定义了完整的治理生命周期：
- Proposal → Maintainer Sponsorship → Experimental → TSC Vote → Official → (可能) Core
- 四种扩展类型：Data-only / Profile / Method / State Machine
- URI 作为版本标识，breaking change 必须换 URI

### 4. llms.txt 文件
提供了面向 LLM 的协议摘要（`docs/llms.txt`），方便 AI 助手理解协议内容。这是一种新兴的"AI-first 文档"模式。

### 5. Proto-First 多绑定等价性
三种协议绑定（JSON-RPC、gRPC、HTTP+JSON）保证语义等价。选择 proto 作为 normative source 而非 OpenAPI，是因为 proto 可以同时生成 gRPC 和 REST 绑定。

---

## 可复用模式

### 1. 分层规范架构
```
Data Model → Abstract Operations → Protocol Bindings
```
任何需要支持多种传输协议的标准都可以采用此模式。将数据模型和操作语义与具体传输解耦。

### 2. Agent Card / Well-Known URI 发现模式
通过标准化的 JSON 元数据文件 + Well-Known URI，实现去中心化的服务发现。可复用于任何需要自描述能力的系统。

### 3. ADR（Architecture Decision Record）流程
`adrs/` 目录 + 模板化的 ADR 格式（Status / Context / Decision Drivers / Consequences），可以作为开源项目架构决策透明化的范本。

### 4. TSC 多厂商治理模型
8 家公司代表的 TSC + Linux Foundation 治理 + 18 个月 Startup Phase 后转 Steady State。这是企业级开源协议项目的可复用治理框架。

### 5. Extension 渐进式标准化路径
`experimental-ext-*` → `ext-*` → core 的毕业路径。允许社区创新而不碎片化核心标准。

### 6. 版本协商机制
每个 `AgentInterface` 独立声明 `protocolVersion`，客户端从 `supportedInterfaces[]` 中选择兼容版本。这种模式可以用于任何需要多版本并存的协议。

---

## 竞品交叉分析

| 维度 | A2A | MCP (Anthropic) | LangGraph/CrewAI | OpenAI Agents SDK |
|------|-----|-----------------|------------------|-------------------|
| **定位** | Agent-to-Agent 通信协议 | Agent-to-Tool 连接协议 | Agent 编排框架 | Agent 开发工具包 |
| **关系** | 互补（明确声明） | 互补（被引用） | 可作为 A2A 的实现框架 | 竞争（封闭 vs 开放） |
| **标准化** | 开放标准(LF) | 开放标准(Anthropic) | 框架级（非协议） | 供应商锁定 |
| **传输** | HTTP/gRPC/JSON-RPC | stdio/HTTP/SSE | 进程内/Python 调用 | HTTP |
| **状态管理** | Task 状态机 + contextId | 无（无状态工具调用） | Graph State | 内部状态 |
| **发现** | Agent Card + Well-Known URI | MCP Server manifest | 无标准机制 | 无标准机制 |
| **多轮对话** | 原生支持 | 不支持 | 框架内支持 | SDK 内支持 |
| **企业就绪** | 完整安全/治理框架 | 基础 | 需自行实现 | 依赖 OpenAI 平台 |
| **治理** | Linux Foundation TSC | Anthropic 主导 | OSS（各自维护） | 闭源 |

**关键洞察**：A2A 和 MCP 不是竞争关系而是互补关系。一个 Agent 可以同时作为 A2A Server（对外协作）和 MCP Client（内部使用工具）。文档用"汽修店"比喻说明：A2A 处理店员间的对话协作，MCP 处理技师与诊断工具的交互。

**A2A 相对 Agent 框架的优势**：框架是"how to build an agent"，A2A 是"how agents talk to each other"。你可以用任何框架构建 A2A 兼容的 Agent。

---

## 代码质量

### 规范质量

**Proto 定义（796 行）**：
- 结构清晰，注释详尽，每个字段都有文档说明
- 使用 `google.api.field_behavior` 标注必填/可选
- 使用 `google.api.http` 注解定义 REST 映射
- 通过 `buf.yaml` 启用 STANDARD + COMMENTS lint 规则
- 有 `.api-linter.yaml` 配置 Google API linter
- `buf.lock` 锁定依赖版本

**规范文档（3,585 行）**：
- 严格使用 RFC 2119 关键词（MUST/SHOULD/MAY）
- Mermaid 图表辅助理解
- 每个操作都有 Inputs/Outputs/Errors/Behavior 四段式描述
- 使用 `{{ proto_to_table() }}` 宏从 proto 自动生成表格，确保文档与定义同步

### 工程实践

- **CHANGELOG.md** 使用 Conventional Commits 自动生成
- **版本语义化**：0.1.0 → 0.2.x → 0.3.0 → 1.0.0，每个版本有明确的 breaking changes 文档
- **迁移指南**：`whats-new-v1.md` 提供了逐字段的 v0.3 → v1.0 迁移指导，包含代码示例
- **.gitvote.yml** 用于 TSC 投票
- **lychee.toml** 用于链接检查
- **.prettierrc / .ruff.toml** 代码格式化
- **mkdocs.yml** 配置完整的文档站点，含版本化（mike）、搜索、重定向映射
- 大量 redirect 规则保持旧链接可用，体现对向后兼容的重视

### 不足之处

- 目前仅有 1 个正式 ADR（ProtoJSON），考虑到协议做了大量设计决策，ADR 覆盖不足
- 没有 SDK 仓库在本 repo 中（分散在 `a2a-python`、`a2a-js` 等独立仓库），需要跨仓库追踪
- 缺少一致性测试套件（TCK 刚启动，尚未成熟）
- Extension 机制虽然设计精良，但目前仅有 4 个示例 extension，生态尚待发展
- `a2a.proto` 的 Go 包名仍使用 `google.golang.org/lf/a2a/v1`，暗示从 Google 迁移到 LF 的过渡尚未完全完成

---

*分析时间: 2026-03-22 | 基于 v1.0.0 (commit at /tmp/repo-miner-A2A)*
