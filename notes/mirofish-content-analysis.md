## 动机与定位

MiroFish 定位为"简洁通用的群体智能引擎，预测万物"。其核心命题是：**通过构建高保真的平行数字世界，让成千上万具备独立人格、长期记忆与行为逻辑的智能体自由交互，从群体涌现中推演未来走向**。

项目解决的核心问题是：传统预测方法（统计模型、专家判断、预测市场）难以捕捉个体互动引发的群体涌现效应。MiroFish 的差异化在于，它不做"数据拟合式预测"，而是"社会模拟式预测"——把种子信息（新闻、政策、小说）注入一个由 LLM 驱动的 Agent 社会，通过模拟社交媒体上的发帖、点赞、转发、评论等真实交互行为，观察群体行为的自然涌现来生成预测结论。

用户画像分两层：
- **宏观决策者**：政策预演、公关危机推演、金融信号推测（"决策者的预演实验室"）
- **微观个人**：小说结局推演、脑洞探索（"个人用户的创意沙盒"）

## 作者视角

### 问题发现

郭航江作为北邮大四学生，抓住了一个精准的交叉空白：

1. **学术工具的产品化空白**：OASIS（CAMEL-AI）是一个强大的多智能体社交模拟框架，但它是面向研究者的 Python 库，没有 UI，没有端到端的产品流程。普通用户无法使用。
2. **预测市场的方法论空白**：Polymarket/Metaculus 依赖人类群体智慧做预测，MiroFish 用 AI Agent 群体替代人类群体——这是"预测市场"概念在 AI 时代的范式迁移。
3. **Zep Cloud 的应用场景空白**：Zep 作为 Agent 记忆层，缺少杀手级应用案例。MiroFish 将其用作知识图谱+Agent 长期记忆的统一存储，是 Zep 最复杂的开源应用之一。

### 解法哲学

"LLM as Simulator"哲学——不把 LLM 当计算器，而当社会模拟器：

1. **种子驱动**：用户上传的文档（PDF/MD/TXT）是"种子材料"，LLM 从中提取实体关系构建知识图谱，而非要求用户手动定义参数。
2. **五阶段管线自动化**：从文档上传到生成预测报告全程自动化，每个阶段用 LLM 做决策（本体设计、人设生成、仿真参数配置、报告撰写），最大程度降低用户认知负担。
3. **双平台并行模拟**：同时在 Twitter 和 Reddit 两个平台模拟，捕捉不同社交媒体生态下的群体行为差异——这是对真实世界多平台舆论场的映射。

### 背景知识迁移

作者将以下知识交叉融合：
- **社会科学**（Agent-Based Modeling）+ **NLP**（LLM 驱动的 Agent）+ **图数据库**（Zep 知识图谱）+ **全栈工程**（Vue3+Flask）
- 前作 BettaFish（微舆舆情分析）的经验迁移——从"分析过去"到"预测未来"的思路升级
- Claude Code（Vibe Coding）10 天完成开发——代码结构清晰体现了 AI 辅助编程的特征：模块化好、注释详尽、prompt 工程精细

### 战略图景

从战略上看，MiroFish 的路径是：
1. **短期**：开源引爆（8 万 Stars 已实现）→ 形成开发者社区
2. **中期**：盛大集团 3000 万投资 → 产品化（SaaS 服务）
3. **长期**：成为"群体智能引擎"的基础设施，类似 ChatGPT 之于对话 AI 的位置

AGPLv3 许可证 + 招聘信息表明这是一个有明确商业化意图的开源项目。

## 架构与设计决策

### 目录结构概览

```
MiroFish/
├── frontend/                    # Vue 3 + Vite + D3.js 前端
│   └── src/
│       ├── components/          # 五步骤组件（Step1-Step5） + GraphPanel + HistoryDatabase
│       ├── views/               # 路由视图页面
│       ├── api/                 # Axios API 封装（graph/simulation/report）
│       ├── router/              # Vue Router 路由定义
│       └── store/               # 简易状态管理
├── backend/                     # Python 3.11 + Flask 后端
│   ├── app/
│   │   ├── api/                 # 三组蓝图：graph_bp / simulation_bp / report_bp
│   │   ├── services/            # 核心业务逻辑（12 个服务模块，约 11,000 行）
│   │   ├── models/              # 数据模型（Project + Task）
│   │   └── utils/               # 工具类（LLM客户端/文件解析/日志/重试/Zep分页）
│   └── scripts/                 # OASIS 模拟脚本（作为子进程运行）
├── docker-compose.yml           # Docker 单服务部署
├── Dockerfile                   # Python 3.11 + Node.js 多阶段构建
└── package.json                 # 根级 npm 脚本协调前后端
```

**代码规模**：后端 Python 约 20,600 行，前端 Vue/JS 约 20,600 行，总计约 41,200 行有效代码。

### 关键设计决策

**决策 1：Zep Cloud 作为统一知识层（最大胆也是最有争议的决策）**

MiroFish 选择 Zep Cloud 而非 Neo4j 等传统图数据库作为核心知识存储，一个 `ZEP_API_KEY` 承载了三重角色：
- **知识图谱存储**：`GraphBuilderService` 通过 `zep_cloud.client.Zep` 创建 Standalone Graph，使用动态本体（`EntityModel`/`EdgeModel` 子类的运行时动态创建）
- **Agent 长期记忆**：`ZepGraphMemoryManager` 在模拟运行时将 Agent 每轮行为（发帖、点赞、评论）实时写入图谱，形成时序记忆
- **检索引擎**：`ZepToolsService` 提供 `InsightForge`（多维度混合检索）、`PanoramaSearch`（全貌搜索含过期事实）、`QuickSearch`（轻量搜索）三级检索能力

优点：架构极简，单一 API 打通知识存储+记忆管理+语义检索。
代价：强依赖 SaaS 服务（Issue #23 和 #156 反映的用户痛点），离线部署困难。

**决策 2：子进程隔离的模拟执行架构**

OASIS 模拟不是在 Flask 进程内执行，而是通过 `subprocess.Popen` 启动独立的 Python 子进程：
```
Flask Backend → subprocess → run_parallel_simulation.py → OASIS Twitter + Reddit
```

进程间通信（IPC）使用文件系统：
- `commands/` 目录：Flask 写入命令（如 Interview 请求）
- `responses/` 目录：模拟脚本写入响应
- `run_state.json`：运行状态文件供 API 查询

这个设计看似"原始"，却是处理 OASIS 异步模拟的务实选择：OASIS 内部使用 asyncio 事件循环，与 Flask 的同步模型不兼容；子进程隔离避免了事件循环冲突，文件 IPC 确保了跨平台兼容（Windows 的 `sys.platform == 'win32'` 兼容代码遍布）。

**决策 3：LLM 驱动的全自动配置生成**

传统模拟工具需要用户手动设置大量参数。MiroFish 用 LLM 替代了所有参数配置：

1. **本体生成**（`OntologyGenerator`）：分析文档后，LLM 自动设计实体类型（固定 10 个，含 2 个兜底类型 Person/Organization）和关系类型（6-10 个）
2. **Agent 人设生成**（`OasisProfileGenerator`）：从 Zep 图谱节点读取实体信息，用 LLM 二次丰富生成包含年龄/性别/MBTI/职业/兴趣的详细人设
3. **模拟参数生成**（`SimulationConfigGenerator`）：LLM 分步生成时间配置（含中国时区作息模型）、事件配置、Agent 活动配置、平台配置

其中中国作息时间模型（`CHINA_TIMEZONE_CONFIG`）是一个有趣的细节——凌晨 0-5 点活跃度系数 0.05，晚间 19-22 点系数 1.5，这使得模拟的社交媒体活动节奏更贴近真实中国互联网。

**决策 4：ReACT 模式的报告生成 Agent**

`ReportAgent` 采用 ReACT（Reasoning + Acting）模式生成预测报告：

1. **规划阶段**：获取图谱统计 + 样本事实 → LLM 生成 2-5 章节大纲
2. **生成阶段**：每章节循环调用工具（至少 3 次，最多 5 次）→ 基于检索结果撰写内容
3. **工具集**：`insight_forge`（深度洞察检索）、`panorama_search`（广度全貌搜索）、`quick_search`（快速搜索）、`interview_agents`（真实 Agent 采访）
4. **分章节流式输出**：每完成一章就保存为独立 `section_XX.md`，前端可轮询获取

报告 Agent 的 prompt 设计值得注意——它被赋予"上帝视角"观察模拟世界，核心规则是"所有内容必须来自模拟世界中发生的事件和 Agent 言行"，强制 Agent 基于证据写报告而非凭空编造。

**决策 5：前端五步骤线性流程设计**

```
Step1(图谱构建) → Step2(环境搭建) → Step3(开始模拟) → Step4(报告生成) → Step5(深度互动)
```

对应 Vue 组件 `Step1GraphBuild` → `Step5Interaction`，其中：
- `GraphPanel.vue`（1,423 行）：D3.js 力导向图谱可视化，支持实时更新
- `Step4Report.vue`（5,150 行）：最复杂的组件，含报告渲染 + Agent 日志实时展示 + 章节增量加载
- `Step5Interaction.vue`（2,574 行）：与模拟 Agent 对话 + ReportAgent 对话双模式

## 创新点

1. **"社会模拟即预测"范式**：将 Agent-Based Social Simulation 从学术工具转化为面向普通用户的预测产品，这在开源社区中是首创。OASIS 提供模拟引擎，MiroFish 提供端到端产品体验。

2. **GraphRAG + Agent 记忆的统一架构**：通过 Zep Cloud 将知识图谱构建、Agent 实时记忆更新、语义检索统一在一个 API 下，实现了"图谱随模拟进化"——每一轮模拟中 Agent 的行为都会更新知识图谱，使图谱成为一个动态的"世界记忆"。

3. **LLM 驱动的全自动仿真参数化**：从文档到模拟，所有中间步骤（本体设计、人设生成、参数配置）都由 LLM 自动完成。用户只需"上传文档 + 描述预测需求"，系统自动完成其余工作。这极大降低了社会模拟的使用门槛。

4. **双平台并行模拟设计**：同时在 Twitter 和 Reddit 两个模拟平台运行，捕捉不同社交媒体生态下的群体行为差异。Twitter 侧重快速传播（CREATE_POST/REPOST/LIKE），Reddit 侧重深度讨论（CREATE_COMMENT/SEARCH_POSTS），两者互补形成更全面的预测。

5. **可回溯的时序记忆图谱**：Zep 的 `valid_at`/`invalid_at`/`expired_at` 机制使得模拟中的关系具有时间维度，`PanoramaSearch` 工具可以区分"当前有效事实"和"历史/过期事实"，支持分析舆情演变过程。

## 可复用模式

1. **"子进程 + 文件 IPC"的异步任务模式**：当需要在 Web 服务中运行重型异步任务（特别是有自己的 asyncio 事件循环的）时，用 `subprocess.Popen` + 文件系统通信是一种简单有效的隔离方案。MiroFish 的 `SimulationRunner` + `SimulationIPCClient` 实现了完整的命令/响应模式，可作为参考。

2. **LLM 驱动的动态本体设计模式**：让 LLM 分析文档后自动设计实体类型和关系类型，然后用 Python 的 `type()` 动态创建 Pydantic 模型子类。这个"LLM 设计 schema → 动态创建类 → 注入图数据库"的模式可复用于任何需要自适应 schema 的场景。

3. **ReACT 报告生成模式**：先规划大纲 → 每章节循环调用工具（强制最少调用次数）→ 基于检索结果写作 → 分章节流式保存。这个"规划-检索-写作"的三阶段模式适用于任何需要基于知识库生成长文档的场景。

4. **中国作息时间模型**：`CHINA_TIMEZONE_CONFIG` 将一天分为死寂/早间/工作/高峰/夜间五段，赋予不同活跃度系数。这个模型可复用于任何需要模拟中国互联网用户行为节奏的场景。

5. **OpenAI 兼容的 LLM 客户端封装**：`LLMClient` 通过 `LLM_BASE_URL` + `LLM_API_KEY` + `LLM_MODEL_NAME` 三参数支持任何 OpenAI 格式 API（默认推荐阿里百炼 qwen-plus），并内置 `<think>` 标签过滤（兼容推理模型）和 markdown 代码块清理。

## 竞品交叉分析

| 维度 | MiroFish | camel-ai/oasis | nikmcfly/MiroFish-Offline | Polymarket/Metaculus |
|------|----------|----------------|--------------------------|---------------------|
| **定位** | 端到端预测产品 | 学术模拟框架 | MiroFish 离线版 | 预测市场平台 |
| **用户** | 普通用户 + 决策者 | AI 研究者 | 技术用户 | 交易者 + 研究者 |
| **预测方法** | AI Agent 社会模拟 | Agent 社交模拟（库级别） | 同 MiroFish（本地化） | 人类群体智慧 + 概率定价 |
| **记忆层** | Zep Cloud（SaaS） | 无持久化记忆 | Neo4j + Ollama（本地） | N/A |
| **图谱** | Zep Standalone Graph | 无 | Neo4j | N/A |
| **UI** | Vue 3 完整 Web UI | 无 UI（纯代码） | 有（社区维护） | 完善的交易 UI |
| **部署** | Docker / 源码 | pip install | Docker（本地） | SaaS |
| **Stars** | 38.2K | 3.6K | 1K | N/A |

### 综合竞争结论

MiroFish 在"AI 社会模拟预测"赛道中占据了**产品化先发优势**：它是唯一一个将 OASIS 学术引擎包装成端到端产品的项目。38K Stars 的社区关注度远超上游引擎 OASIS 的 3.6K。

但其核心风险在于：
1. **Zep 单点依赖**：知识图谱、Agent 记忆、检索能力全部依赖 Zep Cloud SaaS，一旦 Zep 服务变更（定价、API 废弃），整个产品受影响。离线版 MiroFish-Offline（Neo4j+Ollama）正是社区对此痛点的回应。
2. **预测质量验证缺失**：与 Polymarket 不同，MiroFish 目前没有预测结果的回测机制。模拟出来的"未来"缺乏与真实结果的对照验证。
3. **成本不可控**：每次模拟需要大量 LLM API 调用（10+ Agent x 数十轮 x 双平台），README 明确提示"消耗较大"。Polymarket 靠市场机制运行，MiroFish 的每次预测都是烧钱。

与 Polymarket 的本质差异是**方法论层面**的：Polymarket 汇聚真人智慧，MiroFish 用 AI Agent 替代真人。这两种路径在预测准确性上谁更优，目前没有定论——MiroFish 的创新价值正在于它开辟了这条"AI 群体模拟预测"的新路径。

## 代码质量

### 质量检查清单

| 维度 | 评估 | 说明 |
|------|------|------|
| **模块化** | 优 | 后端 12 个 service 模块职责清晰（图谱构建/本体生成/Agent人设/模拟配置/模拟运行/记忆更新/报告Agent/Zep检索等），前端五步骤组件一一对应 |
| **错误处理** | 良 | API 层有统一的 try-except + traceback 返回；`requestWithRetry` 实现指数退避重试；但部分 service 层错误被静默吞没（如 `_wait_for_episodes` 中的 `pass`） |
| **代码注释** | 优 | 中文注释详尽，每个 API 接口有完整的请求/响应文档；Prompt 模板有清晰的规则标注（正确示例/错误示例）；体现 AI 辅助编码的特征 |
| **测试覆盖** | 差 | 仅有 1 个测试脚本（`test_profile_format.py`），无单元测试、无集成测试。`pyproject.toml` 声明了 pytest 依赖但实际无测试代码 |
| **安全性** | 中 | CORS 设置为 `origins: "*"`（过于宽松）；API 无认证机制；traceback 直接返回给前端（生产环境信息泄露风险）；`.env.example` 设计合理但 `SECRET_KEY` 有硬编码默认值 |
| **类型安全** | 中 | 大量使用 `dataclass` 定义数据结构，但缺少 Python 类型检查工具（无 mypy 配置）；前端使用 Options/Composition API 混合但无 TypeScript |
| **性能** | 中 | `TaskManager` 和 `ProjectManager` 使用文件系统 JSON 存储（非数据库），不适合高并发场景；图谱数据每次全量获取（`fetch_all_nodes/edges`）无分页缓存 |
| **可观测性** | 优 | `ReportLogger`（JSONL 结构化日志）+ `ReportConsoleLogger`（文本日志）双日志系统；前端可实时查看 Agent 执行日志；模拟运行状态文件 `run_state.json` 支持实时监控 |
| **部署** | 良 | Docker + docker-compose 一键部署；GitHub Actions 自动构建镜像推送 GHCR；提供国内加速镜像地址（`ghcr.nju.edu.cn`）|
| **跨平台** | 良 | Windows 兼容代码覆盖多处（UTF-8 编码修复、`builtins.open` 猴子补丁、信号处理适配），说明开发者重视非 Linux 用户体验 |
| **依赖管理** | 良 | 使用 `uv` 管理 Python 依赖（现代化），`uv.lock` 锁定版本；但 `zep-cloud==3.13.0` 和 `camel-oasis==0.2.5` 版本锁定过严，可能影响安全更新 |

**总体评价**：这是一个典型的"10 天 Vibe Coding"产物——架构设计和 prompt 工程水平远高于代码工程规范。项目在产品完整性和用户体验上做得出色（端到端流程闭环、UI 精致、文档详尽），但在工程基础设施上有明显短板（无测试、无类型检查、无认证、文件系统存储）。对于一个获得 3000 万投资的项目，下一步最需要补强的是测试覆盖和安全加固。
