# Data Formulator 内容分析（What & How）

> 仓库: [microsoft/data-formulator](https://github.com/microsoft/data-formulator)
> 分析日期: 2026-03-22

---

## 动机与定位

Data Formulator 定位为**概念驱动的 AI 数据可视化工具**，解决数据分析中一个被长期忽视的核心痛点：**数据转换与可视化创建之间的断裂**。

传统工作流中，用户需要在 Python/R 中手动编写数据清洗和变换脚本，然后切换到 Tableau/Excel 等工具进行图表制作。这两个步骤的认知负担和工具切换成本极高。Data Formulator 的核心洞察是：**可视化意图本身就包含了数据变换的隐式规范** —— 当用户说"按月份展示各地区销售趋势"时，这句话同时定义了分组聚合逻辑和折线图的编码方案。

项目的学术根基来自 Chenglong Wang 在程序合成（Program Synthesis）领域的多年研究：将用户的高层意图（自然语言 + 图表规范）自动翻译为精确的数据变换代码。

---

## 作者视角

### 问题发现

Chenglong Wang 从博士阶段开始研究"用示例编程"（Programming by Example），核心思考是：如何让非程序员通过声明意图而非编写代码来操作数据？Data Formulator 是这一研究方向从学术论文到可用产品的自然延伸。

关键洞察来自对现有工具的批判性观察：
- **Tableau 模式**：图表类型丰富但数据变换能力弱，遇到复杂转换必须回到代码
- **Notebook 模式**：数据处理自由度高但可视化交互性差，每次修改都要重写代码
- **纯 AI 对话模式**（如 ChatGPT 生成 matplotlib）：缺乏结构化的编码通道控制，用户很难精确调整

### 解法哲学

Data Formulator 的解法哲学可以概括为三个层次：

1. **概念编码架构（Concept-Driven Encoding）**：用户通过拖放字段到可视化通道（x/y/color/size）来"声明"意图，AI 负责生成底层数据变换代码。这不是简单的 NL2Code，而是一个**混合规范**系统——结构化的图表规范 + 自然语言补充说明。

2. **数据线程（Data Thread）**：每次变换生成新的派生表，形成可追溯的数据血缘链。用户不会覆盖原始数据，而是不断分支探索。这与版本控制的"分支"思想一致。

3. **人机混合控制（AI + Direct Manipulation）**：AI 负责繁重的代码生成，用户保持对图表类型选择、字段映射的直接控制权。这避免了纯对话式 AI 的黑箱问题。

### 背景知识迁移

- **程序合成 → 数据变换**：将 PBE（Programming by Example）的思想迁移到数据分析——用户的图表编码就是"示例"，AI 推断完整的变换程序
- **Vega-Lite 语法 → 语义类型系统**：将 Vega-Lite 的 Grammar of Graphics 理论深度整合到语义类型推断中，让 AI 生成的代码能自动适配可视化需求
- **SWE-Agent 模式 → DataAgent**：将软件工程领域的自主代理（observe-think-act 循环）迁移到数据探索场景

### 战略图景

从版本演进可以看出清晰的产品化路径：
- v0.1：学术验证（单表、基础图表）
- v0.2：工程化（DuckDB 大数据支持、多表）
- v0.5：Agent 化（自主探索、数据提取、报告生成）
- v0.6：数据源扩展（URL/数据库连接、实时刷新）
- v0.7：企业级（Workspace/Data Lake、身份管理、Azure Blob、安全加固）

这是一条典型的"研究原型 → 开发工具 → 企业平台"的产品化路线。

---

## 架构与设计决策

### 目录结构概览

```
data-formulator/
├── src/                          # React 前端 (~66K 行 TS/TSX)
│   ├── app/                      # Redux 状态管理核心
│   │   ├── dfSlice.tsx           # 全局状态定义与 reducer
│   │   ├── store.ts              # Redux 持久化 (localforage)
│   │   ├── useFormulateData.ts   # 数据公式化核心 hook
│   │   └── utils.tsx             # Vega 图表组装等工具
│   ├── lib/agents-chart/         # 语义图表引擎（纯 TS，无 React 依赖）
│   │   ├── core/                 # 语义类型、布局计算、溢出过滤
│   │   ├── vegalite/             # Vega-Lite 后端模板 (~15 种图表)
│   │   ├── echarts/              # ECharts 后端模板 (~20 种图表)
│   │   ├── chartjs/              # Chart.js 后端模板
│   │   └── gofish/               # GoFish 后端模板
│   ├── views/                    # 视图组件
│   │   ├── DataThread.tsx        # 数据线程面板 (2497行，最大组件)
│   │   ├── VisualizationView.tsx # 可视化主视图
│   │   ├── ChatThreadView.tsx    # 对话线程视图
│   │   └── EncodingShelfCard.tsx # 编码架组件
│   ├── components/               # 核心类型定义与图表模板
│   │   └── ComponentType.tsx     # DictTable/Chart/Trigger 等核心类型
│   └── data/                     # 数据类型与工具
├── py-src/data_formulator/       # Python 后端 (~18K 行)
│   ├── app.py                    # Flask 主应用
│   ├── agents/                   # AI Agent 系统
│   │   ├── data_agent.py         # 自主探索 Agent (observe-think-act)
│   │   ├── agent_data_rec.py     # 数据推荐 Agent (核心 prompt 工程)
│   │   ├── agent_data_transform.py # 数据变换 Agent
│   │   ├── agent_interactive_explore.py # 交互式探索建议
│   │   ├── agent_chart_insight.py # 图表洞察 Agent
│   │   ├── agent_report_gen.py   # 报告生成 Agent
│   │   └── client_utils.py       # LiteLLM 多模型适配
│   ├── sandbox/                  # 代码执行沙箱
│   │   ├── local_sandbox.py      # 本地沙箱 (audit hooks)
│   │   └── docker_sandbox.py     # Docker 沙箱 (最大隔离)
│   ├── datalake/                 # 数据湖管理
│   │   ├── workspace.py          # 工作空间（文件级持久化）
│   │   └── metadata.py           # 表元数据管理
│   ├── data_loader/              # 外部数据源连接器 (~10 种)
│   ├── workflows/                # 图表生成工作流
│   │   ├── create_vl_plots.py    # Vega-Lite 图表组装
│   │   └── chart_semantics.py    # Python 端语义类型系统
│   └── code_signing.py           # HMAC 代码签名安全机制
└── embed/                        # iframe 嵌入模式
```

### 关键设计决策

**决策 1：前后端分离的语义类型系统（双端镜像）**

这是最独特的架构决策。项目在 TypeScript（前端）和 Python（后端）**分别**维护了一套语义类型系统：

- 前端 `agents-chart/core/semantic-types.ts`：~60 种语义类型（DateTime/Year/Revenue/Percentage/Country...），驱动图表编码类型推断、零基线决策、色彩方案推荐、格式化等**可视化渲染决策**
- 后端 `workflows/chart_semantics.py`：镜像的类型注册表，负责结构性类型决策（nominal/ordinal/temporal/quantitative），生成 Vega-Lite spec

设计注释明确写道："Python 端聚焦结构性类型决策（直接影响图表形状），美化细节由前端处理。" 这种分层体现了**关注点分离**的极致——后端负责"画什么"，前端负责"怎么画好看"。

**决策 2：三阶段图表组装管线（Phase 0 → 1 → 2）**

图表渲染不是简单的 spec 生成，而是一个三阶段管线：

- Phase 0（语义解析）：将字段语义类型 + 数据特征解析为 `ChannelSemantics`（包含编码类型、格式、聚合默认值、零基线决策、颜色方案等）
- Phase 1（布局计算）：基于弹性模型计算子图尺寸、步长、facet 网格、溢出裁剪。使用"气压模型"计算连续轴拉伸、"弹簧模型"计算离散轴间距
- Phase 2（实例化）：各渲染后端（Vega-Lite/ECharts/Chart.js/GoFish）将抽象布局转为具体 spec

关键创新：布局结果是**目标无关的**（`LayoutResult` 只描述抽象尺寸和步长），各后端独立翻译。这使得新增渲染后端只需实现 `instantiate()` 方法。

**决策 3：LLM 生成代码 + 安全沙箱执行**

AI 生成的 Python 代码在沙箱中执行：
- `LocalSandbox`：持久化子进程 + Python audit hooks，阻止文件写入、网络访问、危险模块导入
- `DockerSandbox`：只读挂载工作区，最大隔离
- `code_signing.py`：HMAC-SHA256 签名机制，确保只有服务器生成的代码才能被重新执行（防止前端篡改代码注入）

这个三层安全模型（审计钩子 + 容器隔离 + 代码签名）是认真考虑过生产部署的标志。

**决策 4：DataAgent 的 SWE-Agent 式自主探索循环**

`data_agent.py` 实现了一个 observe-think-act 循环：
- `visualize`：调用子代理生成数据变换 + 图表
- `clarify`：暂停循环，向用户提问
- `present`：汇总发现，终止循环

每一步的观察（数据样本 + 图表图片）都追加到轨迹上下文，使 LLM 在后续迭代中拥有完整的探索历史。这借鉴了 SWE-Agent 的架构模式，但适配到了数据探索场景。

**决策 5：Redux 持久化 + 数据血缘追踪**

前端状态通过 `redux-persist` + `localforage` 持久化到浏览器 IndexedDB。每个 `DictTable` 包含 `derive` 字段，记录：
- `source`：来源表列表
- `code`：生成代码
- `codeSignature`：代码签名
- `trigger`：触发该派生的用户操作（指令 + 图表规范）
- `dialog`：LLM 对话日志

这使得整个数据探索过程完全可追溯、可重放。

**决策 6：多图表渲染后端抽象**

通过 `ChartTemplateDef` 接口统一四种渲染后端（Vega-Lite/ECharts/Chart.js/GoFish），每种后端独立提供模板集合。这种插件架构允许：
- Vega-Lite：学术级精确可视化（核心支持）
- ECharts：丰富的交互式图表（~20 种，包括漏斗图/桑基图/旭日图等）
- Chart.js：轻量级 canvas 渲染
- GoFish：微软内部实验性渲染库

---

## 创新点

1. **概念编码 + NL 混合规范**：用户通过图表通道映射（结构化）+ 自然语言补充（非结构化）来表达意图，AI 将其翻译为数据变换代码。这比纯 NL2Viz 更精确、比纯直接操作更灵活。

2. **语义类型驱动的智能图表引擎**：60+ 种语义类型不仅用于类型推断，还驱动零基线决策、色彩方案选择、轴格式化、溢出策略等全链路可视化优化。这远超 Vega-Lite 原生的四种基础类型（N/O/Q/T）。

3. **弹性布局算法**：用物理模型（气压模型 + 弹簧模型）自动计算图表尺寸。连续轴使用标记横截面"气压"检测拥挤度，离散轴使用弹性步长分配。这解决了固定尺寸图表在不同数据规模下的适配问题。

4. **数据线程（Data Thread）**：可视化探索的版本控制——每次 AI 辅助变换产生新的派生表，形成有向无环图（DAG）结构。用户可以在任意节点分支探索，不丢失历史上下文。

5. **代码签名安全模型**：HMAC-SHA256 签名确保只有服务器原始生成的代码才能被重新执行。这是 LLM 代码生成场景下的重要安全创新，解决了"代码存储在客户端 → 可能被篡改 → 回传服务器执行"的信任链问题。

---

## 可复用模式

1. **语义类型注册表模式**：用类型注册表（而非 if-else 链）管理数据类型到可视化决策的映射。每个类型条目包含 family、category、vis_encodings、agg_role、domain_shape 五个维度，可直接复用到任何需要数据语义理解的场景。

2. **三阶段管线模式**（Resolve → Layout → Instantiate）：将图表生成分为目标无关的语义决策、目标无关的布局计算、目标特定的实例化，是渲染引擎设计的经典分层。

3. **Agent 的 observe-think-act 循环 + 轨迹管理**：DataAgent 的设计模式可以复用到任何自主 Agent 场景——维护消息轨迹、支持暂停/恢复（clarify → resume）、限制最大迭代次数。

4. **HMAC 代码签名模式**：在 LLM 生成代码的场景中，用 HMAC 签名建立代码来源信任链。sign_result → 存储签名 → verify_code → 仅执行已签名代码。

5. **持久化子进程沙箱**：预热子进程（warm worker）+ audit hooks 的沙箱模式，在安全性和性能之间取得平衡。避免每次执行都启动新进程。

6. **LiteLLM 多模型统一接入**：通过 `Client` 类 + `litellm` 库统一接入 OpenAI/Azure/Anthropic/Gemini/Ollama，用 endpoint + model + api_key 三元组抽象不同服务商。

---

## 竞品交叉分析

| 维度 | Data Formulator | PyGWalker | Graphic-Walker | Metabase | Julius AI |
|------|----------------|-----------|----------------|----------|-----------|
| **核心交互** | 概念编码 + NL 混合 | Tableau 式拖放 | Grammar of Graphics 拖放 | SQL 查询 + 仪表盘 | 纯对话 |
| **AI 能力** | 数据变换代码生成 + 自主探索 Agent | 无 AI | 无 AI | 有限（SQL 生成） | 完整 AI 对话 |
| **数据变换** | AI 自动生成 Python | 有限（内置变换） | 有限 | SQL | AI 生成 Python |
| **图表引擎** | 4 后端 (VL/EC/CJ/GF)，30+ 种 | Graphic-Walker | 自有引擎 | 自有引擎 | Matplotlib/Plotly |
| **语义类型** | 60+ 种，驱动全链路优化 | 基础类型 | 基础类型 | 无 | 无 |
| **数据血缘** | 完整 DAG + 代码溯源 | 无 | 无 | 有限 | 无 |
| **安全模型** | 沙箱 + 代码签名 | N/A | N/A | 权限系统 | 托管环境 |
| **部署模式** | 本地/Docker/云 | Python 包 | npm 组件 | 自托管/云 | SaaS |
| **开源** | MIT | Apache-2.0 | Apache-2.0 | AGPL-3.0 | 闭源 |

### 综合竞争结论

Data Formulator 在竞品格局中占据**独特的生态位**：它是目前唯一一个将"语义类型系统 + AI 代码生成 + 直接操作 + 数据血缘追踪"四个能力整合在一个工具中的开源项目。

**相对优势**：
- 对比 PyGWalker/Graphic-Walker：Data Formulator 有 AI 驱动的数据变换能力，这两者完全依赖用户手动操作
- 对比 Julius AI：Data Formulator 提供结构化的编码通道控制，而非纯黑箱对话；开源且可本地部署
- 对比 Metabase/Superset：Data Formulator 面向分析师的探索性分析，而非运营的仪表盘监控

**潜在劣势**：
- 需要 LLM API Key，增加使用门槛和成本
- 前端代码量大（66K 行），学习和贡献门槛较高
- 缺乏测试（未发现任何测试文件），对于企业级工具存在质量风险
- 性能：每次可视化创建都涉及 LLM 调用 + Python 代码执行，延迟不可避免

---

## 代码质量

### 质量检查清单

| 检查项 | 评估 | 说明 |
|--------|------|------|
| **代码组织** | 优秀 | 前后端分离清晰，agents-chart 库完全独立于 UI 框架。模块化良好，每个 Agent 职责单一 |
| **类型安全** | 良好 | TypeScript 全面使用，核心类型定义详细（`ChannelSemantics`、`ChartTemplateDef` 等）。Python 端使用 type hints |
| **注释质量** | 优秀 | 核心模块有详细的架构注释（如 `types.ts` 的三阶段管线说明、`chart_semantics.py` 的职责说明）。代码签名模块有完整的安全说明 |
| **错误处理** | 良好 | Agent 路由有全局错误处理器，沙箱有超时和异常捕获。LLM 调用有 backoff 重试 |
| **安全性** | 优秀 | 三层安全模型（audit hooks + Docker + HMAC 签名），API Key 不硬编码，输入 HTML 转义 |
| **测试覆盖** | 极差 | **未发现任何自动化测试文件**（无 test_*.py、无 *.test.ts、无 *.spec.ts）。对于 18K+ 行后端和 66K+ 行前端代码，这是一个严重的质量风险 |
| **依赖管理** | 良好 | 使用 uv.lock 锁定 Python 依赖，yarn.lock 锁定前端依赖。pyproject.toml 规范 |
| **性能考虑** | 良好 | 持久化子进程沙箱避免冷启动；前端 localforage 异步存储；图表缩略图缓存；Redux 选择器优化 |
| **可扩展性** | 优秀 | 图表后端插件架构；数据加载器接口化（10 种数据源）；LLM 适配统一抽象 |
| **文档** | 良好 | README 详尽，DEVELOPMENT.md 有开发指南，数据加载器有独立 README。代码内文档充分 |

**总体评分：7.5/10**

主要扣分项是测试覆盖的完全缺失。一个目标企业级部署的工具（带安全沙箱、代码签名、多租户工作空间），却没有任何自动化测试来保障这些关键路径的正确性，这是目前最大的技术债务。

代码本身的设计质量很高，尤其是语义类型系统和三阶段管线的抽象层次。注释和类型定义的完整度在开源项目中属于上乘水平。可以看出作者具有扎实的系统设计功底和学术严谨性。
