# BettaFish 内容分析报告

## 动机与定位

BettaFish（微舆）的核心动机是**用多智能体系统解决舆情分析领域的"信息茧房"问题**。传统舆情分析产品（清博大数据、鹰眼舆情等）以数据看板为核心，用户被动接收预设维度的数据，缺乏对话式交互和深度推理能力。作者将问题重新定义为：用户只需像聊天一样提出分析需求，系统自动完成跨平台数据采集、多维度分析和报告生成的全流程。

项目定位清晰且分三层递进：
1. **入口定位**：舆情分析——覆盖国内外 30+ 社交媒体平台，对标付费企业方案
2. **技术定位**：多智能体协作系统——不依赖 LangChain/LlamaIndex，从零实现完整 Agent 框架
3. **愿景定位**："始于舆情，而不止于舆情"——目标是成为通用数据分析引擎，通过修改 Agent 工具集和 prompt 即可迁移至金融、医疗等垂直领域

README 中明确给出了与 Manus、MiniMax、ChatGPT、Perplexity 的对比链接，说明作者有意识地将项目置于"AI 深度研究"赛道而非传统舆情软件赛道中竞争。

## 作者视角

### 问题发现

作者（北邮背景，上海盛大公司）从三个层面发现了问题空缺：
1. **技术空缺**：开源社区缺少专门面向舆情场景的多智能体系统，现有 Agent 框架（AutoGen、PraisonAI）均为通用框架，无法开箱即用地处理多平台数据采集+分析的闭环
2. **产品空缺**：商业舆情产品价格昂贵、以数据看板为主、缺乏深度推理能力
3. **范式空缺**：单一 LLM 做分析容易产生幻觉和同质化（Issue #132 正是此问题的体现），需要多模型协同和辩论机制来提升可靠性

### 解法哲学

作者的解法哲学可总结为**"专业分工 + 论坛辩论"**：
- **专业分工**：每个 Agent 绑定专属工具集和专属 LLM（InsightEngine 用 Kimi K2 处理 50 万上下文、MediaEngine 用 Gemini 2.5 Pro 处理多模态、QueryEngine 用 DeepSeek 做搜索推理），而非所有 Agent 共用一个模型
- **论坛辩论**：通过 ForumEngine 的文件日志间接通信机制，让不同模型的"思维方式"碰撞，避免直接 API 调用导致的信息同质化
- **自研优先**：完全不依赖 LangChain 等框架，所有 Agent 逻辑用纯 Python 模块化实现。代价是代码冗余（三个 Engine 的 base_node.py、summary_node.py 几乎完全相同），收益是完全可控和可定制

### 背景知识迁移

从代码结构可以看出几个知识迁移方向：
1. **编译器中间表示（IR）思想**迁移至报告生成：ReportEngine 定义了完整的 IR Schema（`ir/schema.py`），将报告抽象为 Block 类型（heading/paragraph/table/kpiGrid/widget 等 16 种），先生成 IR JSON 再渲染为 HTML/PDF/Markdown，这是典型的编译器前端-后端分离思想
2. **微服务架构**迁移至 Agent 系统：每个 Engine 是独立的 Streamlit 应用，通过 Flask 主应用协调启动，各 Engine 通过文件系统（logs/forum.log）松耦合通信
3. **NLP 工程经验**：内置 5 种情感分析模型（BERT LoRA 微调、GPT-2 Adapter Tuning、多语言 Sentiment、传统机器学习、小参数 Qwen3 微调），显示作者有扎实的 NLP 工程背景

### 战略图景

BettaFish + MiroFish 构成"数据分析三板斧"的完整战略图景：
- **BettaFish**：数据收集与分析（舆情监测+多智能体分析）
- **MiroFish**：群体智能预测引擎（38.1K Stars）
- **闭环**：从原始数据 → 智能分析 → 趋势预测的完整链路

这个战略选择非常清晰——先在舆情分析领域建立用户基础和技术积累，再扩展至预测和决策支持，最终形成通用数据分析引擎。

## 架构与设计决策

### 目录结构概览

```
BettaFish/                          # 164个Python文件，53,827行代码
├── app.py (1,348行)                # Flask主应用入口，管理子进程生命周期
├── config.py                       # Pydantic Settings，支持.env和环境变量
├── QueryEngine/                    # 搜索Agent（DeepSeek）
│   ├── agent.py                    # 统一的 DeepSearchAgent 类
│   ├── llms/base.py                # OpenAI 兼容客户端封装
│   ├── nodes/                      # 节点链：Search→Summary→Reflection→Formatting
│   ├── tools/                      # Tavily搜索工具集（6种搜索工具）
│   ├── prompts/                    # JSON Schema约束的提示词
│   └── state/                      # 状态管理
├── MediaEngine/                    # 多模态Agent（Gemini 2.5 Pro）
│   ├── tools/                      # Bocha多模态搜索（5种工具，含视频截图分析）
│   └── ...（结构与QueryEngine同构）
├── InsightEngine/                  # 数据库Agent（Kimi K2，500K上下文）
│   ├── tools/                      # 本地数据库查询5工具+情感分析+关键词优化
│   └── ...（结构与QueryEngine同构）
├── ReportEngine/                   # 报告生成Agent
│   ├── core/                       # template_parser + chapter_storage + stitcher
│   ├── ir/                         # 中间表示Schema（16种Block类型）
│   ├── nodes/                      # 模板选择→布局→篇幅→章节生成
│   ├── renderers/                  # HTML(6,536行)/PDF/Markdown渲染器
│   └── report_template/            # 6套中文报告模板
├── ForumEngine/                    # 论坛引擎
│   ├── monitor.py (858行)          # 基于文件变化的日志监控器
│   └── llm_host.py                 # 论坛主持人（Qwen3模型）
├── MindSpider/                     # AI爬虫系统
│   ├── BroadTopicExtraction/       # 广域话题提取
│   ├── DeepSentimentCrawling/      # 深度舆情爬取
│   └── schema/                     # 数据库Schema（PostgreSQL/MySQL双支持）
├── SentimentAnalysisModel/         # 5种情感分析模型
├── SingleEngineApp/                # 单引擎Streamlit独立应用
├── utils/                          # 通用工具（forum_reader、retry_helper）
└── tests/                          # 单元测试（ForumEngine监控+ReportEngine安全性）
```

### 关键设计决策

**决策1：五大Engine各自独立，通过文件系统通信**

三个分析 Engine（Query/Media/Insight）以独立 Streamlit 应用运行在不同端口（8501/8502/8503），Flask 主应用（端口 5000）通过 subprocess 管理它们的生命周期。Agent 间不直接调用 API，而是通过 `logs/forum.log` 文件进行间接通信。

优点：松耦合、易于调试（日志可人工审查）、天然支持异步并行。
代价：文件 I/O 成为通信瓶颈，需要文件锁（`threading.Lock`）防止并发写入冲突。

**决策2：节点链（Node Chain）架构**

每个 Engine 内部采用固定节点链：`ReportStructureNode → FirstSearchNode → FirstSummaryNode → [ReflectionNode → ReflectionSummaryNode]×N → ReportFormattingNode`。节点基类 `BaseNode`（抽象类）和 `StateMutationNode`（状态变更节点）提供统一的 `validate_input()` + `run()` 接口。

这是对 LangGraph 节点概念的朴素实现——没有图结构、没有条件分支，但足够覆盖"搜索-总结-反思"的循环模式。

**决策3：ReportEngine 的 IR 中间表示**

ReportEngine 是整个系统最复杂的模块（html_renderer.py 单文件 6,536 行）。它引入了编译器级别的 IR（Intermediate Representation）设计：
- 定义了 16 种 Block 类型（heading/paragraph/table/swotTable/pestTable/kpiGrid/widget 等）
- 12 种内联标记（bold/italic/code/link/math/highlight 等）
- 章节级 JSON Schema 校验（`ir/validator.py`）
- DocumentComposer 装订器：排序章节、注入唯一锚点、补齐元数据

这使得报告从"LLM 直出 HTML"升级为"LLM 生成结构化 IR → 校验 → 多格式渲染"，大幅提升了报告质量的可控性。

**决策4：多 LLM 策略与成本优化**

系统配置了 7 种不同的 LLM 角色：
| 角色 | 推荐模型 | 场景适配 |
|------|---------|---------|
| InsightEngine | Kimi K2 (500K上下文) | 大规模数据库结果分析 |
| MediaEngine | Gemini 2.5 Pro | 多模态内容理解 |
| QueryEngine | DeepSeek | 搜索推理 |
| ReportEngine | Gemini 2.5 Pro | 长文本报告生成 |
| MindSpider | DeepSeek | 爬虫任务规划 |
| ForumHost | Qwen3/Qwen-Plus | 论坛主持 |
| KeywordOptimizer | Qwen-Plus | SQL关键词优化 |

每个角色独立配置 API Key、Base URL 和模型名称，既避免了单模型依赖风险，也允许用户根据预算选择不同厂商。

**决策5：代码复制而非共享基类**

三个分析 Engine 的 `base_node.py`、`summary_node.py`、`search_node.py`、`formatting_node.py` 几乎完全相同（仅日志消息和少量代码风格差异）。这是有意为之的设计：每个 Engine 是独立包，可以单独修改而不影响其他 Engine。代价是维护成本高，修一个 bug 需要同步修改三处。

## 创新点

### 1. ForumEngine 的发布-订阅+审核模式

这是 BettaFish 最具原创性的设计。具体机制：

```
Agent发言 → 写入各自log文件(insight.log/media.log/query.log)
              ↓
LogMonitor 轮询检测文件变化 → 识别SummaryNode输出 → 提取内容
              ↓
写入 forum.log（统一格式：[时间] [AGENT_NAME] 内容）
              ↓
每5条Agent发言 → 触发ForumHost（Qwen3模型）生成主持人发言
              ↓
主持人发言写入 forum.log（[时间] [HOST] 内容）
              ↓
各Agent下轮循环时通过 forum_reader.py 读取HOST发言 → 注入prompt
```

关键设计特征：
- **间接通信**：Agent 之间不直接对话，而是通过文件系统和主持人中转。这避免了"Agent A 直接调用 Agent B"导致的信息同质化
- **审核机制**：ForumHost 不仅总结，还会"纠正错误""指出逻辑矛盾"，起到质量门控作用
- **主持人用不同模型**：ForumHost 使用 Qwen3（与三个分析 Agent 的 DeepSeek/Gemini/Kimi 均不同），进一步降低同质化风险
- **文件级去耦合**：如果 ForumEngine 崩溃，三个分析 Agent 仍可独立运行

### 2. 无框架依赖的纯 Python Agent 实现

整个 Agent 系统不依赖 LangChain、LlamaIndex、AutoGen 等任何 Agent 框架，所有组件（节点链、状态管理、工具调用、提示词管理、重试机制）均为纯 Python 实现。核心抽象仅有：
- `BaseNode` 抽象基类（validate_input + run）
- `State` 数据类（管理段落/搜索历史/报告结构）
- `LLMClient`（基于 OpenAI SDK 的流式客户端封装）

这使得代码极易理解（不需要学习框架概念），但也导致了三个 Engine 之间大量代码重复。

### 3. ReportEngine 的 IR 驱动报告生成

将 LLM 报告生成从"一次性输出 HTML"升级为多阶段流水线：
```
模板选择 → 文档布局设计 → 篇幅规划（Word Budget）→ 分章节 JSON 生成 → IR 校验 → 装订 → 多格式渲染
```

IR Schema 支持 SWOT 分析表、PEST 分析表、KPI 网格等专业商业分析组件，这在开源 LLM 报告工具中非常少见。

### 4. 多模态爬虫集成

MindSpider 不仅爬取文本内容，还通过 Playwright 浏览器自动化+Gemini 2.5 Pro 实现视频截图分析、结构化信息卡片提取（天气、股票、日历等搜索引擎结构化数据）。

## 可复用模式

### 1. 文件日志通信模式
适用场景：需要多个异构 Agent 协作但又希望避免强耦合的系统。通过文件系统作为"消息队列"，配合文件位置追踪（`file_positions`）实现增量读取，再加入"主持人"角色做信息整合和引导，是一种轻量级的多 Agent 协作方案。

### 2. IR 驱动的 LLM 报告生成
适用场景：任何需要 LLM 生成结构化文档的系统。定义 Block Schema → LLM 按章节生成 JSON → 校验 → 装订为完整 IR → 多格式渲染，比直接让 LLM 输出 HTML/Markdown 更可控。

### 3. 多 LLM 角色分配策略
适用场景：需要多个 LLM 协同工作的系统。根据任务特点选择最适合的模型（长上下文用 Kimi K2、多模态用 Gemini、推理用 DeepSeek），而非所有任务共用一个"最强"模型。

### 4. Pydantic Settings + .env 双层配置
适用场景：需要灵活配置的 Python 应用。`config.py` 使用 `pydantic-settings` 实现类型安全的配置管理，支持环境变量和 `.env` 文件自动加载，前端页面可动态修改配置并写回 `.env` 文件。

### 5. 指数退避重试装饰器
`utils/retry_helper.py` 提供了通用的 `with_retry` 和 `with_graceful_retry` 装饰器，支持自定义重试次数、初始延迟、退避因子和最大延迟，适用于所有网络 API 调用场景。

## 竞品交叉分析

| 维度 | BettaFish | PraisonAI (5.7K Stars) | AG2/AutoGen (4.3K Stars) | 清博大数据（商业）|
|------|-----------|----------------------|------------------------|-----------------|
| **定位** | 舆情分析专用多Agent系统 | 通用AI Agent框架 | 通用多Agent对话框架 | 企业级舆情监测SaaS |
| **Agent框架** | 纯Python自研 | 基于CrewAI/AutoGen | 微软自研 | 非Agent架构 |
| **数据采集** | 内置MindSpider爬虫 | 无内置 | 无内置 | 商业数据源 |
| **多模态** | 视频截图分析+结构化卡片 | 有限支持 | 文本为主 | 文本+图片 |
| **报告生成** | IR驱动+6套模板+HTML/PDF | 无专业报告 | 无专业报告 | 固定模板 |
| **部署难度** | 高（需配7个LLM API Key+数据库）| 中等 | 中等 | 即开即用 |
| **定制成本** | 低（纯Python易改） | 低 | 中等 | 高（闭源SaaS）|
| **LLM成本** | 多模型组合，可控 | 单模型 | 单模型 | 不透明 |

### 综合竞争结论

BettaFish 在开源舆情分析赛道处于**绝对领先地位**（39.6K Stars，领先第二名 38 倍），但其竞争对手实际上并非同赛道产品，而是：
1. **向上竞争**：与 Manus、Perplexity 等 AI 深度研究产品竞争"谁能生成更好的研究报告"
2. **向下防守**：防止通用 Agent 框架（AutoGen、PraisonAI）加装舆情插件后入侵其领地
3. **侧面竞争**：与商业舆情产品竞争"付费 vs. 开源+API费用"的性价比

其核心壁垒在于：**舆情场景的垂直深度**（内置爬虫+数据库+情感分析+专业报告模板）和 **ForumEngine 的创新协作机制**。但其最大劣势是**部署门槛**（Issue #44, #49, #561 均指向此问题），需要配置 7 个 LLM API Key + 数据库 + 多个第三方搜索 API。

## 代码质量

### 质量检查清单

| 检查项 | 状态 | 说明 |
|--------|------|------|
| **代码量** | 164个Python文件，53,827行 | 项目规模较大 |
| **测试覆盖** | 较弱 | 仅3个测试文件（test_monitor.py、test_report_engine_sanitization.py、test_json_parser.py + test_chart_validator.py），无系统性集成测试 |
| **CI/CD** | 基础 | 仅有 Docker Image CI（tag触发构建推送到GHCR），无单元测试CI、无代码质量检查CI |
| **文档质量** | 优秀 | README 约4,741行Markdown（含中英双语），目录结构树详尽，配置说明清晰 |
| **Docker支持** | 完善 | 提供 Dockerfile + docker-compose.yml，支持 PostgreSQL 数据库容器 |
| **配置管理** | 优秀 | Pydantic Settings 类型安全，支持 .env 文件+环境变量，前端可动态修改 |
| **错误处理** | 较好 | 全面的 try/except、graceful retry、loguru日志 |
| **代码重复** | 严重 | 三个Engine的 base_node/summary_node/search_node/formatting_node 几乎完全相同 |
| **类型标注** | 中等 | 核心模块有类型标注，部分工具函数缺失 |
| **安全性** | 中等 | ReportEngine有XSS清洗测试，但全局API Key管理依赖.env文件 |
| **许可证** | GPL-2.0 | 强传染性许可证，商业使用受限 |
| **依赖管理** | 较重 | requirements.txt 包含 torch、transformers、playwright、weasyprint 等重量级依赖 |
| **代码风格** | 中等 | requirements.txt 列出了 black 和 flake8，但无 pre-commit 钩子或 CI 检查 |

### 主要代码质量问题

1. **三 Engine 代码重复率 > 90%**：`base_node.py`、`summary_node.py`、`search_node.py`、`formatting_node.py` 在三个 Engine 中几乎完全相同，仅日志消息措辞略有差异。应提取为共享基础包。

2. **html_renderer.py 单文件 6,536 行**：这是整个项目最大的单文件，职责过重，包含了所有 Block 类型的 HTML 渲染逻辑、CSS 样式生成、交互组件等，应按 Block 类型拆分为独立渲染器。

3. **sys.path.append 硬编码**：多处使用 `sys.path.append(os.path.dirname(os.path.dirname(...)))` 来解决模块导入问题，这是缺乏正式包管理（pyproject.toml/setup.py）的表现。

4. **缺少集成测试**：整个系统的端到端流程（用户提问→Agent分析→论坛协作→报告生成）没有自动化测试覆盖，全靠人工验证。

5. **裸 except 和 bare except**：`monitor.py` 中存在 `except:` 裸捕获（第376、387行），会隐藏意外错误。
