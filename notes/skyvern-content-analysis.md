# Skyvern 内容分析报告（Phase 3）

## 动机与定位

Skyvern 的核心动机是**解决传统浏览器自动化的脆弱性问题**。传统方案（Selenium/Playwright 脚本）依赖 DOM 选择器和 XPath，网站一改版就全部失效。Skyvern 的解法是：用视觉语言模型（VLM）"看"网页截图，理解页面语义，再生成对应的 Playwright 操作指令。

**定位层次**：
- **SDK 层**：Playwright 的 AI 增强扩展（`pip install skyvern`），保持 Playwright API 兼容性的同时加入 `page.act()`, `page.extract()`, `page.validate()`, `page.prompt()` 四个 AI 命令
- **平台层**：提供可视化 Workflow 引擎、浏览器会话管理、凭证管理、代理网络等企业级功能
- **商业层**：Cloud 托管服务（含反爬检测、CAPTCHA 解码器、代理 IP 池）

项目 slogan：**"用 LLM 和计算机视觉自动化基于浏览器的工作流"**。其设计哲学受 BabyAGI / AutoGPT 启发，但关键差异是赋予了 Agent 真实的浏览器操作能力。

## 作者视角

### 问题发现视角
团队从推荐引擎（Wyvern）转型而来，核心洞察是：**企业级浏览器自动化的痛点不在于"写脚本"，而在于"维护脚本"**。每一次网站改版都意味着重写选择器，这个维护成本在规模化时呈指数增长。

### 解法哲学
**"视觉优先 + 结构化降级"**的混合策略：
1. 优先用截图 + VLM 理解页面（对抗布局变化）
2. 同时提取 DOM 结构作为辅助信息（提供精确交互点）
3. 保留传统 Playwright 选择器作为兜底（确保确定性操作不走 AI）

这不是纯粹的"AI 替代一切"，而是**AI 增强**——让开发者在需要精确控制时用传统方法，在需要灵活性时用 AI。

### 背景知识迁移
- 从推荐引擎（Wyvern）带来了**对 ML Pipeline 的工程化能力**：模型选择、A/B 实验框架（`experimentation/`）、成本跟踪
- 从 Y Combinator 和 VC 融资中获得了**产品化思维**：SDK 优先、文档完善、集成生态（Zapier/Make/N8N/MCP）

### 战略图景
Skyvern 不只是做一个工具，而是在构建**浏览器自动化的基础设施层**：
- 多引擎架构（Skyvern V1/V2、OpenAI CUA、Anthropic CUA、UI-TARS）表明他们在做"模型无关"的抽象层
- Workflow 引擎 + 脚本缓存 = 可复用的自动化资产
- MCP 集成 = 融入 AI Agent 生态

## 架构与设计决策

### 目录结构概览

```
skyvern/                     # 核心 Python 包（~155,000 行代码）
├── forge/                   # 核心引擎（最热模块）
│   ├── agent.py             # ForgeAgent - 主控制循环（4,873 行，最大单文件）
│   ├── agent_functions.py   # 辅助函数（SVG/CSS shape 转换等）
│   ├── forge_app.py         # 应用初始化和全局状态
│   ├── prompts/skyvern/     # 75+ 个 Jinja2 提示模板
│   └── sdk/
│       ├── api/llm/         # LLM 多模型适配层（LiteLLM）
│       ├── workflow/        # Workflow 引擎
│       │   ├── models/block.py  # 6,890 行，27+ 种 Block 类型
│       │   └── service.py       # 5,241 行，工作流执行服务
│       ├── db/              # 数据库层（PostgreSQL + Alembic）
│       ├── cache/           # 缓存层
│       └── services/        # Bitwarden/1Password 凭证集成
├── webeye/                  # 浏览器视觉引擎
│   ├── actions/             # 动作定义、解析、执行（handler.py 4,191 行）
│   ├── scraper/             # 页面抓取（DOM → 结构化数据）
│   ├── browser_factory.py   # 浏览器实例管理
│   ├── cdp_download_interceptor.py  # CDP 下载拦截
│   └── real_browser_manager.py      # 远程浏览器管理
├── library/                 # SDK 公共接口
│   ├── skyvern_browser_page.py      # SkyvernBrowserPage（核心 Page 包装）
│   ├── skyvern_browser_page_ai.py   # AI 操作的 API 调用实现
│   └── ai_locator.py               # AILocator（延迟解析的代理 Locator）
├── core/script_generations/ # 脚本生成和录制重放
├── services/                # 业务服务（任务、工作流、OTP、录制等）
├── schemas/                 # Pydantic 数据模型
└── cli/                     # CLI 工具和 MCP 集成
skyvern-frontend/            # React 前端（可视化 Workflow Builder）
skyvern-ts/                  # TypeScript SDK 客户端
tests/                       # 134 个测试文件（~31,000 行）
```

### 关键设计决策

#### 1. 四大 AI 页面命令的实现

四个命令在 `SkyvernBrowserPage`（`skyvern/library/skyvern_browser_page.py`）中定义，继承自 `SkyvernPage`：

- **`page.act(prompt)`**：调用 `SdkSkyvernPageAi.ai_act()`，通过 API 向服务端发送 `RunSdkActionRequestAction_AiAct`，服务端截图 + DOM 分析后生成动作序列
- **`page.extract(prompt, schema)`**：类似机制，使用 `extract-information` 提示模板
- **`page.validate(prompt)`**：向 VLM 发送验证提示，返回布尔值
- **`page.prompt(prompt, schema)`**：通用 LLM 调用，支持自定义 schema

每个命令本质上都是：**截图 → 提取 DOM → 构建提示 → LLM 推理 → 解析响应 → 执行动作**。

#### 2. 三种交互模式的架构设计

这是通过 `AILocator`（`skyvern/library/ai_locator.py`）实现的巧妙分层：

```
模式 1：传统 Playwright    page.click("#submit-button")     → 直接调用原生 Playwright
模式 2：AI 自然语言        page.click(prompt="Click login") → AILocator 代理，VLM 定位元素
模式 3：AI 降级兜底        page.click("#btn", prompt="...")  → 先尝试选择器，失败时 AI 兜底
```

`AILocator` 是一个**延迟代理**——创建时是同步的，真正的 AI 解析推迟到第一次操作调用时。它通过 `__getattribute__` 魔术方法拦截所有 Playwright Locator 方法：
- 链式方法（nth/first/locator 等）返回新的 `AILocator` 保持链式调用
- 操作方法（click/fill 等）先 `await _resolve()` 解析出真实 Locator 再执行

#### 3. 脚本缓存机制

`skyvern/webeye/actions/caching.py` 实现了**基于元素哈希的动作计划复用**：

- 每个页面元素被计算 SHA256 哈希（包含标签名、属性、文本内容）
- 首次成功执行后，动作计划（Action Plan）连同元素哈希存入数据库
- 后续相同 URL + 导航目标的任务，通过 `retrieve_action_plan()` 查找缓存
- 匹配逻辑：遍历缓存动作，逐个检查元素哈希是否在当前页面存在且唯一
  - 唯一匹配 → 复用
  - 多个匹配或无匹配 → 停止复用，回退到 LLM
- 通过 `source_action_id` 链追踪已执行的缓存动作，确保不重复

这实现了"首次 LLM 推理 + 后续缓存执行"的模式，解释了官方声称的 **10-100x 提速**。

#### 4. Workflow 引擎设计

核心在 `skyvern/forge/sdk/workflow/`，采用**基于 Block 的 DAG 执行模型**：

- `Block`（基类）：27+ 种类型，涵盖导航、提取、代码执行、循环、条件分支、文件处理、邮件发送、HTTP 请求等
- `ForLoopBlock`：支持数据迭代，可嵌套任意 Block，支持自然语言循环变量（通过 LLM 提取）
- `ConditionalBlock`：条件分支，支持 Jinja2 表达式求值
- `TaskV2Block`：新一代任务 Block，代表 Skyvern 2.0 的方向
- `WorkflowRunContext`：上下文管理器，维护参数值、输出传递、Secret 解密

每个 Block 通过 `next_block_label` 指向下一个 Block，形成 DAG。`WorkflowService`（5,241 行）负责执行调度，包括并行执行、超时控制、Webhook 回调等。

#### 5. 视觉理解工作流程

完整的"看→想→做"循环在 `ForgeAgent.agent_step()` 中：

1. **截图（Scrape）**：`browser_state.scrape_website()` → 截取页面截图 + 提取 DOM 树 → `ScrapedPage`
2. **构建提示（Build Prompt）**：将 DOM HTML + 截图 + 导航目标 + 动作历史填入 Jinja2 模板（`extract-action.j2`）
3. **LLM 推理（Extract Actions）**：发送给 VLM，返回 JSON 格式的动作数组（含 reasoning、confidence、action_type、element_id 等）
4. **解析动作（Parse）**：`parse_actions()` 将 JSON 解析为强类型 `Action` 对象
5. **执行动作（Execute）**：`ActionHandler` 根据动作类型分发到具体处理器（click、input_text、select_option 等）
6. **验证完成（Verify）**：通过 `check-user-goal` 提示模板验证目标是否达成

关键细节：截图时会在每个可交互元素上**画 bounding box 并标注 ID**，使 VLM 能准确指定操作目标。

#### 6. 多模型支持架构

`LLMConfigRegistry`（`config_registry.py`）+ `LLMAPIHandlerFactory`（`api_handler_factory.py`）实现了极其全面的模型支持：

- **OpenAI**：GPT-5 全系列（5/5-mini/5-nano/5.1/5.2/5.4）、GPT-4 系列、O3/O4-mini
- **Anthropic**：Claude 3/3.5/3.7/4/4.5/4.6 全系列
- **Bedrock**：AWS 托管的 Claude 和 Amazon Nova
- **Google Vertex AI**：Gemini 系列（通过缓存管理器优化）
- **Azure OpenAI**：企业部署
- **OpenRouter**：聚合 API
- **自定义**：任意 LiteLLM 兼容模型

通过 LiteLLM 作为统一抽象层，加上 Router 模式实现了**多模型负载均衡和自动降级**。

独立的 CUA（Computer Use Agent）引擎：
- `RunEngine.openai_cua`：OpenAI Computer Use API（`computer-use-preview`）
- `RunEngine.anthropic_cua`：Anthropic Computer Use（Claude 3.7+ 支持）
- `RunEngine.ui_tars`：字节 UI-TARS（Seed1.5-VL），代码中标注源自 ByteDance-Seed

#### 7. 推测执行（Speculative Execution）

`SpeculativePlan` 机制允许在当前步骤执行时，**提前为下一步准备截图和 LLM 响应**：
- 当前步骤执行动作的同时，异步触发下一步的页面抓取和提示构建
- 如果页面状态未变化（元素哈希匹配），直接复用预计算的 LLM 响应
- 这是对"截图→LLM→执行"流水线的**并行化优化**

## 创新点

### 1. AILocator —— 延迟 AI 解析的代理模式
将 AI 元素定位包装为 Playwright Locator 的代理对象，支持链式调用和延迟解析。这让 AI 定位在接口层面与传统选择器完全一致，是优雅的 API 设计。

### 2. 元素哈希缓存 —— 跨会话动作复用
不是简单的 URL 匹配，而是通过元素内容哈希实现精细粒度的动作缓存。页面局部变化不影响未变化部分的缓存命中。

### 3. 三引擎并存的 CUA 架构
同时支持 OpenAI CUA、Anthropic CUA、UI-TARS 三种视觉控制引擎，通过统一的 `RunEngine` 枚举和 `LLMCaller` 抽象实现无缝切换。这在同类产品中独一无二。

### 4. 推测执行流水线
借鉴 CPU 推测执行思想，在浏览器自动化场景中实现步骤级的并行预取，减少等待延迟。

### 5. Jinja2 驱动的提示工程
75+ 个提示模板文件，覆盖从动作提取到表单理解到日期格式检查的各种场景。提示中强制 VLM 输出 `user_detail_query`（信息无关的泛化提问）和 `user_detail_answer`（具体回答），实现了**提示的可复用性和可审计性**。

### 6. SVG/CSS Shape 到语义描述的转换
`agent_functions.py` 中的 SVG → LLM 描述 → 语义标注流程，解决了图标类元素无文本标签时 VLM 无法识别的问题。

## 可复用模式

### 1. 双模式 API 设计模式
传统 API + AI 增强的共存设计（`page.click(selector)` vs `page.click(prompt=...)`），适用于任何需要渐进式 AI 增强的工具类库。

### 2. 延迟代理 Locator 模式
`AILocator` 的 `__getattribute__` + `_resolve()` 模式可推广到任何需要延迟异步初始化的代理对象。

### 3. 基于内容哈希的增量缓存
元素哈希 → 动作缓存的模式可应用于任何页面操作自动化场景（RPA、测试自动化等）。

### 4. 多 LLM Provider 统一抽象
`LLMConfigRegistry` + `LiteLLM Router` + 自动降级策略，是构建多模型 AI 应用的成熟参考架构。

### 5. Block-based Workflow DAG
27+ 种 Block 类型的 Workflow 引擎设计，可作为无代码/低代码自动化平台的参考架构。

## 竞品交叉分析

### vs browser-use（81,796 stars）
| 维度 | Skyvern | browser-use |
|------|---------|-------------|
| **架构重量** | 重型（155K 行 Python + 前端 + DB） | 轻量（纯 Python 库） |
| **SDK 接口** | Playwright 兼容 + 4 个 AI 命令 | Agent-first API |
| **缓存优化** | 元素哈希缓存 + 推测执行 | 无（每次重新推理） |
| **Workflow** | 27+ Block 类型的可视化编排 | 无内置 Workflow |
| **模型支持** | 30+ 模型配置 + 3 种 CUA 引擎 | LangChain 集成 |
| **定位** | 企业级平台 | 开发者工具 |

Skyvern 的护城河在于**企业级完整性**（缓存、Workflow、凭证管理、录制回放），browser-use 的优势在于**轻量和易上手**。

### vs UI-TARS-desktop（字节，28,976 stars）
| 维度 | Skyvern | UI-TARS-desktop |
|------|---------|-----------------|
| **范围** | 浏览器自动化 | 桌面全应用 |
| **交互方式** | DOM 结构 + 截图双通道 | 纯视觉（截图 + 坐标） |
| **模型** | 模型无关（支持 UI-TARS 作为引擎之一） | 专有 UI-TARS 模型 |
| **集成** | 已将 UI-TARS 集成为引擎选项 | 独立桌面应用 |

有趣的是，Skyvern 已经将 UI-TARS 集成为其 CUA 引擎之一（代码中有 `UITarsLLMCaller`，注释标明源自 ByteDance-Seed），这说明 Skyvern 的多引擎架构有很强的扩展性。

### vs Claude Computer Use
| 维度 | Skyvern | Claude Computer Use |
|------|---------|---------------------|
| **粒度** | DOM 元素级操作 | 像素级鼠标/键盘操作 |
| **可靠性** | DOM 结构提供更高确定性 | 纯视觉可能误点 |
| **速度** | 脚本缓存后极快 | 每步都需要视觉推理 |
| **关系** | 已集成 Anthropic CUA 作为引擎选项 | 底层能力提供方 |

Skyvern 与 Claude Computer Use 是**互补而非竞争**关系——Skyvern 将其作为三种 CUA 引擎之一整合，并在上层提供 Workflow、缓存、Session 管理等企业级包装。

## 代码质量

### 整体评估

**优势**：
- **类型注解全面**：全面使用 Python 类型提示和 Pydantic BaseModel，所有 API 数据模型强类型化
- **结构化日志**：统一使用 structlog，日志中携带完整上下文（task_id, step_id, workflow_run_id 等）
- **分层清晰**：webeye（浏览器层）→ forge（引擎层）→ services（业务层）→ library（SDK 层）
- **提示模板外置**：75+ 个 Jinja2 模板独立管理，避免提示硬编码
- **OpenTelemetry 追踪**：`@traced()` 装饰器贯穿关键路径

**待改进**：
- **agent.py 过于庞大**：4,873 行的单文件，`ForgeAgent` 类承担了太多职责（任务管理、步骤执行、多引擎分发、错误处理、清理），应拆分为多个模块
- **block.py 同样庞大**：6,890 行，27+ 种 Block 类型全部在同一文件中
- **异常处理过度**：`execute_step()` 方法有 10+ 个不同的 except 分支，部分逻辑重复
- **测试覆盖率未知**：测试文件数量（134 个，约 31,000 行）与核心代码量（155,000 行）比例约 1:5，相对合理但未见覆盖率报告

### 质量检查清单

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 类型注解 | 优秀 | 全面的 Python 类型提示 + Pydantic 模型 |
| 错误处理 | 良好 | 自定义异常体系完整，但 agent.py 过度捕获 |
| 日志系统 | 优秀 | structlog + OpenTelemetry 双轨追踪 |
| 文档注释 | 良好 | 公共 API 有 docstring，内部方法较少 |
| 配置管理 | 优秀 | Pydantic Settings + 环境变量，支持多环境 |
| 数据库迁移 | 优秀 | Alembic 管理，版本化迁移 |
| 安全性 | 良好 | Jinja2 SandboxedEnvironment、Webhook 签名、凭证加密 |
| 依赖管理 | 良好 | uv.lock 锁定，pyproject.toml 规范 |
| CI/CD | 良好 | Docker Compose + Kubernetes 部署配置 |
| 单一职责 | 待改进 | agent.py（4,873 行）和 block.py（6,890 行）需要拆分 |
| 测试体系 | 中等 | 有单元测试 + 冒烟测试 + SDK 测试，但覆盖率未量化 |
