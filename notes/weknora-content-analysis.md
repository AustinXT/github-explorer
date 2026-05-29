# WeKnora 内容分析（Phase 3）

> 仓库：[Tencent/WeKnora](https://github.com/Tencent/WeKnora) | 分析日期：2026-03-22

## 动机与定位

WeKnora 定位为**基于大语言模型的文档理解与语义检索框架**，核心解决"企业复杂异构文档的智能问答"问题。与通用 LLM 应用平台（Dify）不同，WeKnora 聚焦于 RAG 管线的精细化工程，特别是多模态文档解析和检索质量优化。

项目的战略意图明确：
1. **微信生态绑定** — 官网 weknora.weixin.qq.com，SaaS 版通过微信对话开放平台（chatbot.weixin.qq.com）提供，天然获取微信生态用户
2. **企业 IM 连接器** — 原生支持企微/飞书/Slack，将知识库能力直接注入办公场景
3. **私有化部署优先** — Docker Compose 一键部署，面向对数据安全敏感的企业客户

## 作者视角

### 技术选型动机
- 选择 Go 作为后端主力（~12 万行非测试代码），追求高并发下的稳定性和部署简洁性（单二进制 + Docker）
- docreader（文档解析器）使用 Python gRPC 服务，利用 Python 生态丰富的文档解析库（markitdown、MinerU 等）
- Vue 3 前端，82 个 .vue 组件，功能完整但不过度复杂
- 使用 `dig` 做依赖注入容器，这在 Go 项目中较为少见但提升了模块解耦

### 核心痛点解决
knowledge.go 被修改 140 次、是最热文件（9092 行），反映出**知识管理是最核心也最复杂的业务逻辑**，涉及：文件上传、URL 导入、远程文件、手动录入、FAQ 批量导入、异步解析、图谱构建等多个入口的统一处理。

## 架构与设计决策

### 目录结构概览

```
WeKnora/
├── cmd/server/main.go        # Go 服务入口（Gin + dig DI 容器）
├── internal/                  # Go 后端核心（359 个 Go 文件，~10.8 万行）
│   ├── agent/                 # ReAct Agent 引擎 + 工具注册
│   │   ├── engine.go          # Agent 执行循环（Think-Act-Observe）
│   │   ├── skills/            # Progressive Disclosure 技能系统
│   │   └── tools/             # 15+ 内置工具（搜索/图谱/数据分析/MCP/沙箱执行）
│   ├── application/           # 业务层
│   │   ├── repository/        # 数据访问（支持 7 种向量库后端）
│   │   │   └── retriever/     # Postgres/SQLite/ES(v7+v8)/Qdrant/Milvus/Weaviate
│   │   └── service/           # 核心服务
│   │       ├── chat_pipline/  # RAG 管线（插件化事件驱动）
│   │       ├── retriever/     # 混合检索引擎（向量+关键词+RRF 融合）
│   │       ├── llmcontext/    # LLM 上下文管理（压缩策略 + Redis/内存存储）
│   │       ├── file/          # 多存储后端（Local/MinIO/COS/S3/TOS）
│   │       ├── memory/        # 用户级记忆图谱
│   │       └── web_search/    # 搜索引擎（DuckDuckGo/Bing/Google）
│   ├── im/                    # IM 集成层（Adapter 模式）
│   │   ├── wecom/             # 企业微信（WebSocket + Webhook 双模式）
│   │   ├── feishu/            # 飞书
│   │   └── slack/             # Slack
│   ├── infrastructure/        # 基础设施
│   │   ├── chunker/           # 文本分块器（递归分割 + 受保护区域）
│   │   └── docparser/         # 文档解析引擎注册（gRPC/HTTP/内置）
│   ├── mcp/                   # MCP 客户端管理（连接池 + 空闲清理）
│   ├── models/                # 模型适配层
│   │   ├── chat/              # 20+ LLM 提供商适配
│   │   ├── embedding/         # 8 种 Embedding 适配
│   │   ├── rerank/            # 5 种 Rerank 适配
│   │   └── vlm/               # VLM 多模态适配
│   ├── sandbox/               # 技能沙箱（Docker/本地双模式）
│   ├── event/                 # 事件总线（Agent 流式交互）
│   └── stream/                # 流管理器
├── docreader/                 # Python 文档解析微服务（gRPC）
│   ├── parser/                # 15 种文档格式解析器（PDF/Word/Excel/Image/Web...）
│   ├── ocr/                   # OCR 引擎（PaddleOCR + VLM）
│   └── splitter/              # 文本分割器（Python 版本）
├── frontend/                  # Vue 3 + Vite 前端
├── mcp-server/                # 独立 MCP 服务端（Python，暴露 WeKnora API）
├── skills/preloaded/          # 预置技能（引文生成/文档协作/数据处理/文档分析）
├── migrations/                # 数据库迁移（ParadeDB + 版本化迁移）
└── docker/                    # Dockerfile 集合
```

### 关键设计决策

**1. RAG 管线：插件化事件驱动架构**

这是 WeKnora 最核心的架构决策。`chat_pipline` 采用 Plugin + EventManager 模式，将 RAG 流程拆解为独立插件：

```
Query → Rewrite → Search/SearchParallel → Rerank → FilterTopK → Merge → ChatCompletion
                     ↓                                   ↓
              SearchEntity(图谱)                   Memory(记忆检索)
```

- 每个插件实现 `Plugin` 接口（`OnEvent` + `ActivationEvents`）
- 通过 `EventManager.Register` 注册，`Trigger` 触发
- 插件链通过闭包构建中间件链，支持 `next()` 级联调用
- 优势：新增检索策略只需添加插件，不修改主流程

**2. 混合检索 + RRF 融合**

检索层实现了完整的混合检索：
- `CompositeRetrieveEngine`：组合模式，将多个检索引擎统一为一个接口
- `KeywordsVectorHybridRetrieveEngineService`：支持向量检索 + 关键词检索并行执行
- RRF（Reciprocal Rank Fusion）：向量权重 0.7 + 关键词权重 0.3，k=60，标准 RRF 参数
- 当召回量不足时触发 Query Expansion，并发生成查询变体、跨目标检索

**3. Agent 引擎：ReAct 循环 + Progressive Disclosure**

Agent 采用经典 ReAct（Reason + Act）循环：
- 每轮调用 LLM 获取 tool_calls → 并行执行工具 → 将结果追加到消息历史 → 下一轮
- 通过 `EventBus` 实时推送思考/工具调用/结果事件，前端流式展示
- Skills 系统借鉴 Claude Code 的 Progressive Disclosure 模式（3 层：元数据→指令→资源）
- 15+ 内置工具覆盖：知识搜索、图谱查询、数据分析、沙箱脚本执行、MCP 工具调用

**4. 文档解析微服务化**

docreader 独立为 Python gRPC 微服务，通过 Chain of Responsibility（责任链）模式处理文档：
- PDFParser 尝试 MinerU → MarkitdownParser 兜底
- 支持格式：PDF/Word(docx+doc)/Excel/PPT/Image/Markdown/HTML/Web
- OCR 双引擎：PaddleOCR（本地）+ VLM（远程大模型 OCR）
- Go 侧的 `chunker` 移植了 Python splitter，并增加了**受保护区域**保护（LaTeX 公式、Markdown 表格/图片/链接、代码块不被拆分）

**5. 多后端向量存储策略**

支持 7 种向量数据库后端，每种通过 Repository 接口抽象：
- 轻量级：SQLite-vec（嵌入式）、PostgreSQL(pgvector + ParadeDB)
- 专业级：Elasticsearch(v7/v8)、Qdrant、Milvus、Weaviate
- 图谱：Neo4j（GraphRAG 知识图谱检索）

**6. IM 集成：Adapter 模式**

统一的 `Adapter` 接口抽象 IM 平台差异：
- `IncomingMessage`：统一的入站消息结构（平台/类型/用户/内容/文件）
- `ReplyMessage`：统一的出站消息结构（支持流式分块回复）
- 每个平台实现自己的 WebSocket/Webhook 连接管理
- 内置命令系统：/help, /clear, /info, /search, /stop

**7. 依赖注入容器（dig）**

使用 Uber 的 `dig` 库管理所有依赖，`container.go` 集中注册 60+ 组件：
- 数据库、Redis、文件服务、模型服务、Agent 配置、IM 适配器等
- 统一的 `ResourceCleaner` 处理优雅退出时的资源清理
- 这种模式在 Go 社区中不常见，但显著降低了组件间耦合

## 创新点

1. **父子分块策略（Parent-Child Chunking）**：将文档分为父块（大上下文）和子块（精确匹配），检索时命中子块后可展开到父块上下文，显著提升答案完整性。`merge_expand.go` 中对短上下文（<350 字符）自动扩展邻居块

2. **Pipeline 级 Query Expansion**：当初始召回量不足时，自动生成查询变体（同义词、相关概念），并发检索后合并结果，这在同类产品中不常见

3. **Skills 系统的 Progressive Disclosure**：借鉴 Claude Code 的 3 层渐进加载模式，技能在系统提示中只暴露名称和描述（Level 1），Agent 按需通过 `read_skill` 工具加载完整指令（Level 2），进一步通过 `execute_skill_script` 在沙箱中执行脚本（Level 3）

4. **MCP 安全策略**：主动禁用 stdio 传输模式（安全考量），仅允许 SSE/HTTP Streamable，并实现连接池 + 空闲清理

5. **图谱增强检索**：将向量检索、关键词检索、图谱实体检索三路并行（`PluginSearchParallel`），通过知识图谱补充结构化关系信息

6. **分块器保护区域**：文本分割时通过正则表达式检测 LaTeX 公式、Markdown 表格、代码块等结构化内容，确保不在这些区域内部切分

## 可复用模式

1. **Plugin + EventManager 管线模式** — 将复杂处理流程拆解为独立插件，通过事件驱动串联。适用于任何多步骤数据处理管线。核心代码在 `internal/application/service/chat_pipline/chat_pipline.go`

2. **CompositeRetrieveEngine** — 组合模式统一多个检索后端，对外暴露统一的 Retrieve 接口。可直接复用于任何需要多数据源聚合检索的场景

3. **RRF 融合算法** — `knowledgebase_search_fusion.go` 中的 RRF 实现简洁完整（~50 行），可直接复用于任何混合检索场景

4. **IM Adapter 抽象** — `internal/im/adapter.go` 定义的统一 IM 接口，可作为多平台 Bot 开发的起始模板

5. **LLM Context Manager** — `internal/application/service/llmcontext/` 中的上下文管理模式（自动压缩 + 多后端存储），解决长对话 token 超限问题

6. **沙箱执行模式** — `internal/sandbox/` 中的 Docker/本地双模式沙箱，带脚本验证器（白名单校验），适用于任何需要安全执行用户代码的场景

## 竞品交叉分析

### vs Dify（134K stars）
- **定位差异**：Dify 是通用 LLM 应用开发平台（Workflow + Agent + RAG），WeKnora 聚焦文档理解和 RAG 管线
- **检索深度**：WeKnora 的 RAG 管线更精细（Query Expansion、父子分块、图谱增强、RRF 融合），Dify 的检索相对标准化
- **工作流**：Dify 有成熟的可视化 Workflow 编排，WeKnora 偏向 Agent Skills 的代码化扩展
- **生态**：Dify 社区活跃度远高，WeKnora 外部 PR 仅 2 个
- **部署**：两者都支持 Docker 部署，但 WeKnora 组件更多（Go App + Python docreader + 数据库），复杂度更高

### vs RAGFlow（76K stars）
- **共同点**：都聚焦深度文档理解 + RAG，都重视文档解析质量
- **文档解析**：RAGFlow 自研 DeepDoc 解析引擎，WeKnora 集成 MinerU + markitdown + PaddleOCR
- **检索策略**：两者都支持混合检索，但 WeKnora 增加了图谱检索和 Query Expansion
- **Agent**：RAGFlow 的 Agent 能力较弱，WeKnora 有完整的 ReAct Agent + 工具系统 + Skills

### vs FastGPT（27K stars）
- **相似度高**：两者都是知识库问答 + 可视化编排，目标用户群体重叠
- **技术栈**：FastGPT 使用 TypeScript（Next.js），WeKnora 使用 Go + Vue
- **差异化**：WeKnora 在 IM 集成（企微/飞书/Slack）和 MCP 支持上更完善
- **社区**：FastGPT 社区更活跃，文档更完善

### 总结定位
WeKnora 的竞争优势在于：**腾讯品牌背书 + 微信生态绑定 + 精细化 RAG 管线 + IM 原生集成**。劣势在于：社区参与极低（仅 2 个外部 PR）、部署复杂度高、文档建设滞后。

## 代码质量

### 整体评估
- **规模**：Go ~12 万行（非测试），Python ~8500 行，前端 82 个 Vue 组件
- **架构成熟度**：高。清晰的分层（handler → service → repository），接口驱动设计（`internal/types/interfaces/` 下 30+ 接口定义），DI 容器管理依赖
- **代码风格**：规范。注释充分（中英双语），包级别文档完整，命名清晰
- **日志覆盖**：优秀。pipeline 每个阶段都有结构化日志（PipelineInfo/Warn/Error），Agent 每轮都有详细的执行追踪

### 质量检查清单

| 维度 | 评分 | 说明 |
|------|------|------|
| 测试覆盖 | **偏低** | 仅 28 个测试文件，~5200 行测试代码，相对 12 万行主代码，覆盖率估计 <10%。关键路径（agent engine、RAG pipeline）缺少集成测试 |
| 错误处理 | **良好** | 自定义错误类型（`PluginError`），错误传播链完整，pipeline 各阶段都有错误兜底策略 |
| 安全性 | **良好** | API Key AES-256-GCM 加密存储、SSRF 安全 HTTP 客户端、沙箱脚本白名单验证、MCP stdio 传输禁用、SQL 验证增强 |
| 可观测性 | **优秀** | 集成 OpenTelemetry（Jaeger 后端），每个服务调用都有 span 追踪，pipeline 结构化日志完整 |
| 并发安全 | **良好** | 关键共享状态使用 `sync.RWMutex`，goroutine 池（ants）控制并发，MCP 连接管理有 double-check locking |
| 配置管理 | **良好** | config.yaml 中心化配置 + 环境变量覆盖 + prompt 模板外部化（可热替换提示词而不改代码） |
| 数据库迁移 | **良好** | 使用 golang-migrate 版本化迁移，ParadeDB 初始化脚本分离 |
| 依赖管理 | **中等** | go.mod 依赖 50+ 三方库，部分依赖较重（Milvus client、Neo4j driver）可能不需要时仍被编译 |
| knowledge.go 巨文件 | **需重构** | 单文件 9092 行，承载了太多职责（文件上传/URL解析/FAQ/图谱/标签/手动内容/多模态），应拆分为子服务 |
| 前端代码组织 | **良好** | 标准 Vue 3 结构（api/components/views/stores/composables），i18n 国际化支持 |
