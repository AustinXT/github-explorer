## 动机与定位
- 要解决的问题: Go 生态缺少一个**生产级的 AI Agent 开发框架**。现有方案要么是通用 LLM 包装器（LangChainGo），要么是绑定特定云厂商生态（Eino/CloudWeGo），无法满足 Google Cloud 生态中用 Go 构建多 Agent、可编排、可观测的 AI 应用需求。
- 为什么现有方案不够: (1) LangChainGo 缺乏原生的多 Agent 编排、Agent 间转移、工作流控制能力；(2) 竞品多为 Python-first 思维的 Go 移植，没有利用 Go 的并发原语和 `iter.Seq2` 等现代语言特性；(3) 缺少与 Google AI 平台（Gemini、Vertex AI、A2A 协议）深度集成的方案。
- 目标用户: 使用 Go 构建云原生 Agent 应用的后端工程师和 SRE 团队，特别是已在 Google Cloud 生态中的团队。次要用户是希望利用 Go 的性能和类型安全来构建生产级 Agent 系统的独立开发者。

## 作者视角
### 问题发现
Google Cloud AI 团队在推进 Gemini 多语言 SDK 生态时发现：Python ADK 虽然功能完备，但云原生场景（微服务、高并发、容器化部署）的核心语言是 Go。Google 内部大量基础设施使用 Go，外部客户的后端也以 Go 为主。缺少 Go 版 ADK 意味着这些用户被迫用 Python 写 Agent 逻辑然后通过 gRPC/REST 桥接，增加了系统复杂度。问题发现的路径是**由内部平台需求驱动**，而非社区自发。

### 解法哲学
**"Code-first, 不发明新概念"**。ADK-Go 的核心价值观是：
1. **Go 惯用法优先**：用 `iter.Seq2`（Go 1.23+ 推送迭代器）实现事件流而非 channel，用 interface 而非反射来定义扩展点，用标准 `context.Context` 贯穿调用链。
2. **组合优于继承**：Agent 是 interface，不是 base class。LLMAgent、SequentialAgent、ParallelAgent 都通过组合 `agent.Agent` base 实现构建，避免了 Python 版的深继承链。
3. **与 Python 版对齐但不照搬**：CONTRIBUTING.md 明确要求 "alignment with adk-python"，但 Go 版在流式处理、并发工具调用等方面做了 Go 原生重设计。

### 背景知识迁移
1. **Google 内部服务框架经验** -> 六层架构分离（Agent / Runner / Session / Model / Tool / Plugin），与 Google 内部微服务的关注点分离一脉相承。
2. **gRPC/Protobuf 生态设计模式** -> Request/Response 结构化的 Service 接口（`session.Service`、`artifact.Service`），与 gRPC service 定义风格一致。
3. **OpenTelemetry 生态** -> 一等公民级别的可观测性集成，每个 Agent 调用、LLM 调用、Tool 调用都有独立的 trace span。
4. **A2A (Agent-to-Agent) 协议** -> 将跨进程、跨语言的 Agent 互操作标准化，这是 Google 推动的开放标准，ADK-Go 是其参考实现。

### 战略图景
ADK-Go 是 Google AI 平台战略的**关键基础设施层**：
- **纵向**：Gemini API -> genai SDK -> ADK -> Agent 应用，形成从模型到应用的完整链路。
- **横向**：ADK-Python / ADK-Go / ADK-Java / ADK-TypeScript 构成多语言统一框架，通过 A2A 协议实现跨语言 Agent 互操作。
- **生态锁定**：虽然声称"模型无关"，但深度绑定 `google.golang.org/genai`，Gemini 是唯一开箱即用的模型实现。其他模型需要自行实现 `model.LLM` 接口。

## 架构与设计决策

### 目录结构概览
项目采用**扁平化包结构**，每个顶层目录对应一个核心领域：

```
agent/          -- Agent 接口与实现（llmagent, workflowagents, remoteagent）
runner/         -- 运行时引擎，管理 Agent 执行生命周期
session/        -- 会话管理（内存、数据库、Vertex AI 三种后端）
model/          -- LLM 抽象层（Gemini、Apigee 实现）
tool/           -- 工具系统（functiontool、mcptoolset、geminitool）
plugin/         -- 插件系统（横切关注点：日志、重试、函数调用修改）
telemetry/      -- OpenTelemetry 可观测性
server/         -- HTTP 服务层（REST API、A2A 协议服务器）
artifact/       -- 文件/二进制产物管理
memory/         -- Agent 记忆（跨会话语义搜索）
cmd/            -- CLI 工具和 launcher
internal/       -- 内部实现（不暴露给用户的核心逻辑）
```

分层逻辑遵循**由外到内的依赖方向**：`runner` 依赖 `agent`、`session`、`model`，但反过来不成立。`internal/llminternal` 是实际的 LLM 调用流程引擎，被 `agent/llmagent` 包装为用户友好的 API。

### 关键设计决策

1. **决策**: 使用 Go 1.23+ `iter.Seq2` 作为事件流传输机制
   - 问题: Agent 执行过程中需要流式产生事件（LLM 响应、工具调用结果、Agent 转移等），需要一种既支持流式又支持错误传播的机制。
   - 方案: 所有 `Agent.Run()` 和 `Runner.Run()` 返回 `iter.Seq2[*session.Event, error]`，即 Go 推送迭代器。调用方通过 `for event, err := range agent.Run(ctx)` 消费事件流。
   - Trade-off: 牺牲了 Go 1.22 及以下版本的兼容性（需要 Go 1.25.0），换来了比 channel 更简洁的流式 API——无需手动关闭 channel、无 goroutine 泄漏风险、天然支持 `yield` 中断。比 callback 更清晰的控制流。
   - 可迁移性: 高 -- 任何需要流式生产-消费模式的 Go 项目都可以采用此模式替代 channel。

2. **决策**: 基于 interface 的 Agent 抽象 + 工厂函数构造
   - 问题: 需要支持多种 Agent 类型（LLM Agent、工作流 Agent、远程 A2A Agent），同时保持统一的组合和编排能力。
   - 方案: 定义 `agent.Agent` 接口（`Name()`, `Description()`, `Run()`, `SubAgents()`），各种 Agent 通过各自包的 `New()` 工厂函数创建。内部通过 `internal()` 方法暴露私有状态给框架层。
   - Trade-off: 接口中包含 `internal() *agent` 私有方法使得用户无法直接实现该接口（需要通过 `agent.New()` 包装），牺牲了扩展性换来了框架对 Agent 生命周期的完全控制。
   - 可迁移性: 中 -- "interface + 工厂函数 + internal 私有方法"模式适合需要控制实例化的框架设计。

3. **决策**: 请求处理器管道（Request/Response Processor Pipeline）
   - 问题: LLM 调用前后需要大量预处理（注入指令、加载工具、处理历史消息、Agent 转移逻辑等）和后处理（NL 规划、代码执行结果），这些逻辑需要解耦和可扩展。
   - 方案: `internal/llminternal/base_flow.go` 中定义 `DefaultRequestProcessors` 和 `DefaultResponseProcessors`，是一组有序的处理函数。每个处理器接收 `(ctx, req, flow)` 并可修改请求或产生事件。
   - Trade-off: 处理器顺序隐含依赖（如 `contentsRequestProcessor` 必须在 `nlPlanningRequestProcessor` 之前），用注释而非类型系统保证，增加了维护复杂度。换来了清晰的关注点分离和独立可测试性。
   - 可迁移性: 高 -- 中间件/管道模式是通用架构模式，适用于任何需要多步骤请求处理的系统。

4. **决策**: 多 Agent 转移通过 `transfer_to_agent` 工具函数实现
   - 问题: 当一个 Agent 判断另一个 Agent 更适合回答当前问题时，需要一种机制实现 Agent 间的控制转移。
   - 方案: 不引入特殊的路由协议，而是将 Agent 转移建模为一个普通的工具调用 `transfer_to_agent(agent_name)`。框架在请求预处理阶段自动注入可转移目标的描述和转移工具的声明。
   - Trade-off: 优雅地复用了 LLM 的 function calling 能力做路由决策（无需额外的路由模型），但依赖 LLM 正确调用工具，可能产生错误的转移。
   - 可迁移性: 高 -- "将系统能力建模为工具"是一种通用的 Agent 设计模式。

5. **决策**: 并行工具调用使用 goroutine + sync.WaitGroup
   - 问题: LLM 可能在一次响应中请求多个工具调用，串行执行效率低。
   - 方案: `handleFunctionCalls` 为每个 `FunctionCall` 启动一个 goroutine，使用 `sync.WaitGroup` 等待所有完成，然后合并结果为单个事件。
   - Trade-off: 利用了 Go 原生的轻量级并发能力，显著提升多工具场景的吞吐量。但合并事件时需处理 `StateDelta` 冲突（通过 `deepMergeMap`），引入了状态合并的复杂性。
   - 可迁移性: 中 -- Go 特定的并发模式，但 goroutine + WaitGroup 的多任务合并模式可推广。

6. **决策**: Session 状态三级作用域（app:/user:/temp:）
   - 问题: Agent 系统中的状态有不同的生命周期和共享范围需求——有些状态跨用户共享，有些仅当前会话有效。
   - 方案: 通过 key 前缀约定 (`app:`、`user:`、`temp:`) 区分状态作用域。`app:` 跨用户共享，`user:` 同一用户跨会话共享，`temp:` 仅当次调用有效。
   - Trade-off: 简单的字符串前缀约定，零运行时开销，但依赖开发者遵守命名规范，缺乏编译期检查。
   - 可迁移性: 高 -- 通过 key 前缀管理状态作用域的模式适用于任何 key-value 状态管理系统。

7. **决策**: Plugin 系统作为横切关注点的统一注入点
   - 问题: 日志、监控、重试等横切关注点散落在 Agent/Model/Tool 各层，需要统一的注入机制。
   - 方案: `plugin.Plugin` 提供从 `OnUserMessage` 到 `AfterTool` 的 12 个生命周期钩子。`PluginManager` 通过 `context.Value` 在整个调用链中传递，各层在适当时机调用对应的 plugin 回调。
   - Trade-off: 全生命周期的钩子提供了极大的灵活性（可实现缓存、审计、限流等），但 context 传递 plugin manager 是一种隐式依赖，增加了调试难度。
   - 可迁移性: 高 -- 生命周期钩子模式广泛适用于框架设计。

## 创新点

1. **iter.Seq2 驱动的流式 Agent 编排**
   - 描述: 将 Go 1.23+ 的推送迭代器语义应用于 AI Agent 的事件流传输，实现了"写同步代码，得流式行为"的开发体验。`for event, err := range agent.Run(ctx)` 替代了传统的 channel + goroutine 模式。这在 Go AI 框架中尚属首创。
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 4/5
   - 适用场景: 任何需要流式处理且希望避免 channel 管理复杂性的 Go 项目（日志流处理、实时数据管道等）。

2. **Agent 转移即工具调用（Transfer-as-Tool）**
   - 描述: 将多 Agent 路由决策建模为 LLM 工具调用，通过 `transfer_to_agent` 函数实现。框架自动注入转移目标描述和约束（`DisallowTransferToParent`、`DisallowTransferToPeers`），让 LLM 在充分信息下做路由决策。
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 5/5
   - 适用场景: 任何多 Agent 系统的路由设计——无需额外的路由模型或规则引擎。

3. **Branch 隔离的并行 Agent 执行**
   - 描述: `parallelagent` 通过 `Branch` 机制为每个并行子 Agent 创建隔离的事件可见域。Branch 格式为 `parent.child`，通过字符串前缀匹配实现事件过滤。结合 `errgroup` 和 `ackChan` 确保事件有序提交到 session。
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 3/5
   - 适用场景: 需要并行执行多个子任务但要求结果隔离的编排系统。

4. **流式 FunctionCall 聚合器（Streaming Response Aggregator）**
   - 描述: `streamingResponseAggregator` 处理 Gemini 流式返回的 `PartialArgs`，通过 JSON Path 增量合并函数参数，并正确处理 text/thought/functionCall 的交错序列。支持 `WillContinue` 信号实现跨 chunk 的函数调用重组。
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 3/5
   - 适用场景: 任何需要处理流式 function calling 响应的 LLM 集成。

5. **Human-in-the-Loop 工具确认机制**
   - 描述: 通过 `tool.ConfirmationProvider` 和 `ToolConfirmation` 实现了声明式的工具调用确认流程。工具可通过 `RequireConfirmation` 标志或动态 `RequireConfirmationProvider` 函数决定是否需要人工审批，框架自动处理确认/拒绝的事件流。
   - 新颖度: 3/5 | 实用性: 4/5 | 可迁移性: 4/5
   - 适用场景: 高风险操作的 Agent 系统（财务操作、数据删除、系统配置变更）。

## 可复用模式

1. **推送迭代器流式管道**: 用 `iter.Seq2[T, error]` + `yield` 构建生产者-消费者管道，替代 channel——适用于 Go 1.23+ 的任何流式数据处理。
2. **请求处理器链**: `[]func(ctx, req) error` 有序处理器数组，每个处理器可修改请求或产生副作用——适用于任何需要多步骤请求预处理的系统（API Gateway、中间件链）。
3. **interface + 工厂函数 + internal 方法**: 通过 interface 暴露公共 API，工厂函数控制实例化，`internal()` 私有方法暴露框架内部状态——适用于需要控制扩展点的框架。
4. **Context 传递框架状态**: 通过 `context.Value` 传递 `PluginManager`、`ParentMap`、`RunConfig` 等框架状态——适用于 Go 中需要隐式传递横切关注点的场景。
5. **深度合并 Map 状态**: `deepMergeMap` 递归合并并行操作产生的状态增量——适用于任何并行任务的状态聚合。
6. **Branch 前缀事件过滤**: 用带分隔符的字符串路径实现层级化的可见域隔离——适用于多租户、多分支的事件系统。

## 竞品交叉分析

### vs LangChainGo
- ADK-Go 更好: 原生多 Agent 编排（sequential/parallel/loop/transfer）、A2A 跨进程 Agent 互操作、OpenTelemetry 深度集成、Plugin 系统横切关注点注入
- 竞品更好: 支持 10+ 模型提供商（OpenAI、Anthropic、Cohere 等开箱即用），社区更成熟，RAG 工具链更丰富
- 不同目标: LangChainGo 定位为通用 LLM 应用工具箱，ADK-Go 定位为 Agent 编排框架。LangChainGo 更适合单 Agent + 多工具场景，ADK-Go 更适合多 Agent 协作场景。

### vs cloudwego/eino
- ADK-Go 更好: 多 Agent 编排架构完整度更高、A2A 协议支持、会话管理（多后端 session service）、HITL 确认机制
- 竞品更好: 万级 QPS 高吞吐设计、与 CloudWeGo 微服务生态深度集成、更成熟的中文社区支持
- 不同目标: Eino 面向字节跳动式的超高并发在线 AI 服务，ADK-Go 面向结构化的 Agent 编排和企业 AI 应用

### vs Firebase Genkit (Go)
- ADK-Go 更好: 完整的多 Agent 系统（Genkit 几乎没有 Agent 概念）、工作流编排、Agent 转移、Plugin 系统
- 竞品更好: 入门门槛更低（更少的概念）、更好的 RAG 原语支持、与 Firebase 生态集成
- 不同目标: Genkit 定位为"快速构建 AI 增强应用"，ADK-Go 定位为"构建复杂 Agent 系统"

### 综合竞争结论
- 差异化护城河: (1) Google 官方维护 + Gemini 深度优化；(2) A2A 协议参考实现，跨语言 Agent 互操作的标准制定者地位；(3) 与 Vertex AI 服务（Session、Memory）的原生集成；(4) 多语言 ADK 统一架构的 Go 实现。
- 竞争风险: (1) 模型无关性名不副实——仅 Gemini 开箱即用，其他模型需自行适配 `model.LLM` 接口；(2) Go AI 生态整体弱于 Python，社区贡献者基数小；(3) 功能与 Python 版存在差距（如 Issue #540 反映的 skills 缺失）。
- 生态定位: Google AI 平台 Go 语言入口，承担将 Gemini 推入 Go 云原生生态的战略任务。不追求"通用 AI 框架"定位，而是"Google AI 最佳实践的 Go 实现"。

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | 良好 | 遵循 Google Go Style Guide，interface 定义清晰，职责分离合理。部分 TODO 注释反映仍在活跃开发中。`internal` 包隔离做得好。 |
| 文档质量 | 一般 | README 精简但缺少架构文档。代码注释质量高（特别是 `agent/context.go` 的调用层级说明），但缺少独立的设计文档和 ADR。总计 434 行 markdown（不含 README）。 |
| 测试覆盖 | 基本 | 83 个测试文件，约 32,733 行测试代码（与 29,568 行源码比例约 1.1:1）。核心路径有测试，使用 httprr 做 HTTP 录制回放测试。但部分模块标注 `TODO: test coverage`（如 geminiModel）。 |
| CI/CD | 完善 | GitHub Actions 包含 build/test/lint（golangci-lint v2.3.1）+ nightly 检查。测试启用 race detector、shuffle、count=1。有 PR 模板和 Issue 模板。 |
| 错误处理 | 规范 | 126 处使用 `errors` 包，广泛使用 `fmt.Errorf("...: %w", err)` 包装错误。定义了专用错误类型（`ErrStateKeyNotExist`、`ErrConfirmationRequired`）。工具执行有 panic recovery。 |

### 质量检查清单
- [x] 有 CI/CD 流水线（go.yml + nightly.yml）
- [x] 有 linter 配置（golangci-lint）
- [x] 有 Issue/PR 模板
- [x] 有贡献指南（CONTRIBUTING.md 含测试要求）
- [x] 使用 Apache 2.0 开源许可
- [x] 核心接口有 godoc 注释
- [x] 测试使用 race detector
- [x] 错误链式传播（%w）
- [x] panic recovery（functiontool.Run）
- [ ] 独立的架构设计文档（ADR/设计文档）
- [ ] CHANGELOG / 版本发布说明
- [ ] 基准测试（benchmark）
- [ ] 非 Google 模型的官方适配
