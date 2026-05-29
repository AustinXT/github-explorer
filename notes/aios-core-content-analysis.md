# aios-core 内容分析

> 仓库: [SynkraAI/aios-core](https://github.com/SynkraAI/aios-core) | 分析时间: 2026-03-22

## 动机与定位

AIOX（Artificial Intelligence Orchestration eXperience）的核心命题是：**AI 辅助开发的最大瓶颈不在代码生成，而在计划一致性和上下文丢失**。项目用 README 原话概括了两个关键创新：

1. **Agentic Planning（代理式规划）**：analyst/pm/architect 三个 Agent 协作产出 PRD 和架构文档，通过 human-in-the-loop 精炼，而非让 AI 直接生成代码。
2. **Contextualized Development（上下文化开发）**：SM（Scrum Master）Agent 将规划文档转化为"超详细 Story 文件"，Dev Agent 打开 Story 即可获得完整实现上下文——消除了"AI 编码但不知道为什么"的问题。

定位差异化：不做通用 Agent 框架，而是垂直于**全栈开发场景的 Agile 工作流**。口号"CLI First"表明它不是一个有 UI 的产品，而是一个嵌入 IDE/CLI 的开发方法论工具。

## 作者视角

从代码和文档中可以清晰看到作者的思维模型：

- **教育者心态**：README 提供葡萄牙语/西班牙语/中文多语言文档，每个 Agent 都有"persona"设定（zodiac、archetype、greeting），这种"角色扮演式"设计降低了新手心理门槛，符合 Alan Nicolas 教育机构背景。
- **方法论先于代码**：205 个 task 文件、1179 个 markdown 文件（共 44 万行），markdown 文档量远超代码量（21 万行 JS/TS），本质上是用代码去**执行**一套开发方法论，而非构建传统软件产品。
- **Constitution 思维**：设立了一个"宪法"文件（`constitution.md`），定义不可违反的原则（CLI First、Agent 权限分离、Story-Driven Development），并通过代码级 Gate 自动执行。这体现了对"AI 越权"的深度焦虑。
- **品牌困境**：代码中同时存在 `aios-core`、`aiox-core`、`AIOX-FullStack` 多个名称，v5.0.3 仍保留 v4.0.0 注释，反映品牌重塑执行不彻底。

## 架构与设计决策

### 整体架构

```
aiox-core/
├── bin/                    # CLI 入口（aiox.js, aiox-init.js, aiox-graph.js）
├── packages/               # Monorepo 子包
│   ├── installer/          # 安装向导（wizard + detection + merger）
│   ├── aiox-install/       # 安装工具
│   ├── aiox-pro-cli/       # Pro 版 CLI
│   └── gemini-aiox-extension/ # Gemini CLI 适配
├── .aiox-core/             # 核心框架（被安装到目标项目）
│   ├── core/               # 运行时核心
│   │   ├── orchestration/  # 多 Agent 编排引擎
│   │   ├── synapse/        # 8 层上下文注入管道
│   │   ├── ids/            # 增量开发系统（实体注册表）
│   │   ├── memory/         # Gotchas 记忆系统
│   │   ├── quality-gates/  # 3 层质量门禁
│   │   ├── code-intel/     # 代码智能（MCP Provider 适配）
│   │   ├── events/         # 事件总线
│   │   ├── session/        # 会话检测
│   │   └── mcp/            # MCP 配置迁移/管理
│   ├── development/        # Agent 定义和开发资产
│   │   ├── agents/         # 11 个 Agent 角色定义（.md + MEMORY.md）
│   │   ├── agent-teams/    # 团队配置（fullstack, qa-focused 等）
│   │   ├── tasks/          # 205 个可执行任务文件
│   │   ├── templates/      # 模板（story, PRD, 架构等）
│   │   └── checklists/     # 质量检查清单
│   ├── workflow-intelligence/ # 工作流建议引擎
│   ├── hooks/              # Git hooks
│   └── data/               # 工作流链、实体注册表等配置
├── .claude/                # Claude Code 原生集成
│   ├── rules/              # 10 条规则文件
│   ├── hooks/              # 6 个 hook（权限控制、读保护等）
│   └── commands/skills/    # 命令和技能
├── .cursor/rules/agents/   # Cursor IDE Agent 镜像
├── .gemini/rules/          # Gemini CLI Agent 镜像
└── tests/                  # 337 个测试文件（8050 行）
```

### 关键设计决策

**1. Agent 即 Markdown 文件**

Agent 不是代码模块，而是结构化 YAML 嵌入 Markdown 的"人格定义文件"。例如 `sm.md` 定义了 River（Scrum Master）的激活指令、命令列表、依赖任务、人格特征。这些文件被 IDE 加载后，AI 模型按照 YAML 中的 `activation-instructions` 执行角色切换。

**设计意义**：Agent 的"智能"完全依赖 LLM 的指令遵循能力，框架不做推理，只做编排和约束。

**2. Synapse 引擎：8 层上下文注入**

```
L0-Constitution → L1-Global → L2-Agent → L3-Workflow → L4-Task → L5-Squad → L6-Keyword → L7-StarCommand
```

这是一个分层上下文管道，根据当前 token 使用百分比（bracket-aware filtering）动态裁剪注入的上下文。L0（宪法规则）永远注入，L7（Star 命令上下文）按需注入。设计目标是在有限 context window 内最大化有效信息密度。

**3. IDS（增量开发系统）：实体注册表**

维护一个 745 项实体注册表（`entity-registry.yaml`），包含所有 task、template、checklist 的路径、用途、依赖关系、校验和。支持自动更新（RegistryUpdater）、自修复（RegistryHealer）和断路器（CircuitBreaker）。本质是一个**开发资产的知识图谱**。

**4. 工作流链与 Handoff**

`workflow-chains.yaml` 定义了 Agent 间的标准交接流程（SM → PO → Dev → QA）。每次 Agent 完成任务后写入 handoff artifact，下一个 Agent 激活时自动读取并建议下一步命令。

**5. 多 IDE 同步**

同一套 Agent 定义维护在 `.aiox-core/development/agents/`，通过 `sync:ide` 脚本同步到 `.claude/`、`.cursor/`、`.gemini/` 等 IDE 配置目录。实现了"一处定义，多处生效"。

**6. Hook 驱动的权限控制**

通过 Claude Code 的 PreToolUse hook 实现硬性约束：
- `enforce-git-push-authority.sh`：非 @devops Agent 一律拦截 `git push`
- `read-protection.py`：关键文件（Agent 定义、配置等）不允许部分读取
- `enforce-architecture-first.py`：强制先做架构再编码

这是目前所见的**最深度 Claude Code hook 集成**。

### 不是 Monorepo，是安装器 + 框架

虽然 `package.json` 定义了 workspaces，但 `packages/` 下只有 4 个子包（installer、aiox-install、pro-cli、gemini-extension），核心逻辑全在 `.aiox-core/`。运行 `npx aiox-core install` 会将 `.aiox-core/` 目录复制到目标项目。本质上是一个**脚手架/安装器 + 嵌入式框架**。

## 创新点

### 1. Story-Driven Context Injection（故事驱动的上下文注入）
将 Agile 的 User Story 概念转化为 AI 开发的"上下文载体"。Story 文件不仅是需求描述，还是 Dev Agent 的完整执行脚本——包含实现步骤、架构指导、CodeRabbit 集成配置、质量门禁标准。**这消除了 AI 编码时最大的痛点：不知道业务背景和架构约束。**

### 2. Constitutional AI Governance（宪法式 AI 治理）
将 Anthropic 的"Constitutional AI"思想应用到开发工具层面——定义不可违反的原则，通过代码级 Gate 自动执行。这比简单的 system prompt 规则更可靠，因为 hook 在 LLM 外部运行。

### 3. 8 层 Synapse Context Pipeline
分层注入 + bracket-aware token 预算管理，是对"如何在有限 context window 内最大化有效信息"的工程化解答。目前未见其他开源项目有类似深度的上下文管理方案。

### 4. Agent Memory 模式
每个 Agent 拥有独立 MEMORY.md，存储学到的模式（项目结构约定、编码风格等），跨 session 持久化。配合 `gotchas-memory.js`（重复错误自动捕获为 gotcha），形成了简易的"项目级学习"能力。

### 5. Workflow Intelligence（工作流智能）
不仅定义工作流链，还通过 ConfidenceScorer、SuggestionEngine、WaveAnalysis 提供基于历史的下一步建议和并行执行分析。

## 可复用模式

| 模式 | 描述 | 适用场景 |
|------|------|----------|
| **Agent-as-Markdown** | 用 YAML-in-Markdown 定义 Agent 行为，IDE 直接加载 | 任何需要 Agent 角色切换的 CLI 工具 |
| **Constitution + Gate** | 定义不可违反原则 + 自动化执行 gate | AI 辅助开发中的安全边界 |
| **Handoff Artifact** | Agent 间通过文件系统传递结构化交接信息 | 多 Agent 协作场景 |
| **Entity Registry** | 开发资产的自更新知识图谱（路径/用途/依赖/校验和） | 大型项目的资产管理 |
| **Bracket-Aware Context** | 根据 token 预算动态裁剪上下文层 | 任何 LLM 应用的 context 管理 |
| **Hook-Based Authority** | 用 IDE hook 实现 Agent 权限控制 | Claude Code / Cursor 集成 |
| **Task-as-Executable-Workflow** | 每个 task 文件包含完整执行流程（含 elicitation 交互点） | 可复用的 AI 工作流定义 |
| **Multi-IDE Sync** | 一处定义 Agent，同步到多个 IDE 格式 | 多 IDE 支持的工具 |

## 竞品交叉分析

| 维度 | AIOX (aios-core) | MetaGPT (65K⭐) | CrewAI (47K⭐) | AutoGen (56K⭐) |
|------|-------------------|------------------|----------------|-----------------|
| **定位** | 全栈开发 Agile 工作流 | 软件公司模拟 | 通用 Agent 编排 | 多 Agent 对话 |
| **Agent 定义** | Markdown + YAML 人格 | Python 类 + SOP | Python 类 + Role | Python 类 + Config |
| **编排模型** | Story-Driven 线性链 + Gate | SOP 瀑布流 | 任务图/顺序/层级 | 对话协议 |
| **运行时** | 无（依赖 LLM IDE） | Python 进程 | Python 进程 | Python 进程 |
| **上下文管理** | 8 层 Synapse Pipeline | 全局共享内存 | 短期/长期记忆 | 对话历史 |
| **IDE 集成** | Claude/Cursor/Gemini/Codex | 无 | 无 | 无 |
| **代码执行** | 由 LLM IDE 执行 | 内置沙箱 | 内置工具 | 代码执行器 |
| **学习曲线** | 高（方法论+角色+命令） | 中 | 低 | 中 |
| **独特优势** | 深度 IDE 集成 + Agile 方法论 | 最完整的软件开发模拟 | 最简洁的 API | 最灵活的对话模式 |

**关键差异**：AIOX 是唯一不自己运行 Agent 的框架——它依赖 Claude Code/Cursor 等 IDE 的 LLM 来执行 Agent 逻辑。这意味着：
- 优势：零基础设施成本，用户自带 LLM
- 劣势：完全依赖 IDE 的 hook/command 能力，跨 IDE 体验参差不齐（README 诚实标注了 Cursor/Copilot 的 hook 缺失）

## 代码质量

### 测试覆盖
- 测试文件：337 个（8,050 行）
- 源代码文件：630 个（211,601 行）
- **测试代码占比约 3.8%**，略高于之前评估的 1.5%，但仍偏低
- 使用 Jest（主） + Mocha（health-check）双框架
- 有 CI pipeline（GitHub Actions），含 path-based 智能跳过（docs-only PR 不跑测试）

### 正面信号
- **完善的 CI/CD**：GitHub Actions 含变更检测、并发控制、权限最小化
- **lint-staged + Husky**：Pre-commit 执行 ESLint + Prettier + 语义 lint
- **semantic-release**：自动版本管理
- **TypeScript 类型检查**（`tsc --noEmit`），虽然源码是 JS
- **Schema 验证**：使用 ajv 做配置验证
- **自修复机制**：Registry 有断路器、自愈、备份
- **文档完整度极高**：多语言 README、用户指南、架构文档、安装指南

### 风险信号
- **Markdown 占比过高**（442K 行 vs 212K 行 JS）：大量逻辑以自然语言"规则"形式存在，LLM 遵循度无法保证
- **测试覆盖不足**：核心模块（synapse、orchestration、ids）的单元测试少
- **品牌不一致**：代码中多处名称混用（aios/aiox/AIOX-FullStack），增加理解成本
- **无 Pro 实际内容**：`pro/` 目录下 squads 为空，feature-registry.yaml 不存在，Pro 版商业化仍在早期
- **过度工程化风险**：205 个 task、1179 个 md 文件、745 个实体注册——对于一个 2.4K Star 的项目来说，元数据/规则的复杂度远超实际使用
- **单一运行时依赖**：完全依赖 Claude Code hook 系统，hook 能力降级时（如 Cursor）整个治理体系失效
