# OpenSpec 深度分析报告

> GitHub: https://github.com/Fission-AI/OpenSpec

## 一句话总结
YC W26 入选的 Spec-Driven Development（SDD）框架，在 AI 编码助手和人类之间插入一层轻量级规格协议，以「fluid not rigid / brownfield-first」的哲学支持 30+ 个 AI 工具，8 个月 37K+ Stars。

## 值得关注的理由
- **SDD 赛道第二名**：37.4K Stars，仅次于 GSD（48K），定义了「AI 写代码前先写 spec」的工作范式
- **YC W26 背书**：Y Combinator Winter 2026 批次，Demo Day 2026-03-24，partner Jared Friedman
- **真正的工具无关**：24 个 AI 工具适配（Claude Code / Cursor / Copilot / Gemini CLI 等），自身零 AI API 调用

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/Fission-AI/OpenSpec |
| Star / Fork | 37,427 / 2,512 |
| 代码行数 | 44,351（TypeScript 34,522 行 + Markdown 31,820 行） |
| 项目年龄 | 8 个月（2025-08-05 创建） |
| 开发阶段 | Post-1.0 稳定期（v1.2.0，30+ 标签版本） |
| 贡献模式 | 单人创始人驱动（Tabish Bidiwale 占 85%+，~25 位贡献者） |
| 热度定位 | 大众热门（37K+ stars，npm 月下载 ~249K） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Tabish Bidiwale（@TabishB），悉尼大学计算机科学毕业（2019），在量子计算公司 Q-CTRL 工作约 5.5 年，从 Graduate 成长到 Senior Software Engineer & Team Lead，经历了 $113M Series B 融资。2025 年离职创办 Fission-AI，以 OpenSpec 入选 Y Combinator W26 批次。一个从量子计算团队 Lead 转型为 AI 开发工具 solo founder 的创业故事。

### 问题判断
在 Q-CTRL 领导工程团队期间，Tabish 观察到 AI 编码助手会重复人类团队的 misalignment 失败模式——当需求仅存在于聊天记录中时，AI 的输出不可预测。brownfield 项目中尤为严重：AI 缺乏对已有代码库的「契约式理解」，没有 spec，只能靠 chat history 猜测意图。

### 解法哲学
四条核心哲学直接回应了竞品的痛点：
- **Fluid not rigid** → 对标 GitHub Spec Kit 的 rigid phase gates
- **Easy not complex** → 对标 GSD 的重量级 meta-prompting
- **Brownfield-first** → delta spec 机制让用户描述「变更什么」而非「系统是什么」
- **Built for AI coding assistants** → 零 AI API 调用，生成的是「AI 能理解的结构化指令文件」

### 战略意图
成为 AI 编码工具链的「中间层协议」——不绑定任何特定 AI 工具，而是成为所有工具都需要的 spec 标准。这与 OpenAPI 之于 REST API、Protocol Buffers 之于 RPC 的定位类似。YC 入选 + npm 月下载 249K + 24 个工具适配，已经在向这个方向靠近。即将推出的 Workspaces 功能（团队/多仓库场景）预示了商业化路径。

## 核心价值提炼

### 创新之处

1. **Artifact DAG Schema——声明式 workflow 定义**（新颖度 5/5 | 实用性 5/5 | 可迁移性 5/5）
   将 AI 编码 workflow 的 artifact 依赖关系抽象为 YAML DAG schema。使用 Kahn 算法计算拓扑排序，`getNextArtifacts(completed)` 查询当前可执行项。proposal → specs + design → tasks → apply 的四步工作流完全数据驱动，用户可自定义 schema 改变 artifact 种类和依赖。

2. **Brownfield Delta Spec 格式**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   使用 `## ADDED / MODIFIED / REMOVED / RENAMED Requirements` 的 Markdown 约定描述增量变更。格式足够简单让 AI 能可靠生成，又足够结构化让程序能准确解析。合并引擎按固定顺序执行（RENAME → REMOVE → MODIFY → ADD），带交叉冲突检测和 Zod schema 校验。

3. **24 工具统一适配层**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   核心接口 `ToolCommandAdapter` 只有两个方法（`getFilePath` + `formatFile`）。从同一份 CommandContent 生成 24 个 AI 工具各自格式的文件（Claude Code 用 YAML frontmatter MD、Cursor 用不同的 frontmatter、Gemini CLI 用 TOML 等）。添加新工具只需一个 adapter 文件 + registry 注册一行。

4. **零运行时 AI 依赖**（新颖度 4/5 | 实用性 5/5 | 可迁移性 3/5）
   OpenSpec 自身不调用任何 AI API——它生成的是「给 AI 读的指令文件」，真正的 AI 调用由用户的编码助手执行。避免了 API key 管理、模型选择、成本控制等复杂性，实现了真正的工具无关。

5. **Context/Rules 注入机制**（新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5）
   `config.yaml` 的 `context`（项目背景）和 `rules`（per-artifact 规则）在指令生成时注入 AI 上下文，但明确标注「这些是给你的约束，不要写入产出文件」。解决了 AI 倾向于将系统提示复制到输出中的常见问题。

### 可复用的模式与技巧

1. **声明式 DAG Schema + Kahn 拓扑排序**：数据驱动的多步骤 workflow 编排，适用于任何 AI workflow 场景
2. **Adapter Pattern + Static Registry**：核心接口 2 个方法 + 注册表模式，极低成本添加新适配器。适用于多平台适配
3. **三级配置解析**（project > user > package）：类似 ESLint 的配置继承策略，适用于 CLI 工具
4. **Delta 操作排序**（RENAME → REMOVE → MODIFY → ADD）：确保合并幂等性的标准操作排序
5. **双轨 Delivery**（Skills + Commands）：同时生成 SKILL.md 和斜杠命令文件，覆盖不同 AI 工具的消费方式

### 关键设计决策

1. **Markdown 作为 spec 格式**：不使用 JSON/YAML 结构化格式，而是用 Markdown + 约定标题层级。AI 生成 Markdown 的可靠性远高于结构化格式，同时人类可直接阅读编辑。

2. **多进程无状态 CLI**：每次命令执行都从文件系统读取状态（spec 文件、config.yaml），不维护守护进程。简化了部署和调试，但牺牲了性能（每次需要解析整个 spec 目录）。

3. **PostHog 遥测（可关闭）**：匿名使用数据收集，支持 `DO_NOT_TRACK=1` 或 `OPENSPEC_TELEMETRY=0` 关闭，CI 环境自动禁用。为 YC 的增长指标提供数据支撑。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | OpenSpec | GSD (48K) | GitHub Spec Kit | Kiro (AWS) | Intent |
|------|----------|-----------|-----------------|------------|--------|
| 部署方式 | npm CLI | meta-prompt 注入 | Python CLI | 独立 IDE | SaaS |
| 工具绑定 | 24 个工具 | 工具无关（纯 prompt） | Copilot 优先 | Bedrock 锁定 | 自有 agent |
| workflow 刚性 | 可自定义 DAG | 固定多步骤 | 刚性 phase gates | IDE 内置 | 双向同步 |
| brownfield | Delta spec 原生 | 弱 | 弱 | 弱 | 强（living spec） |
| AI API 调用 | 无 | 无 | 有 | 有 | 有 |
| 商业化 | Workspaces（规划中） | 未知 | GitHub 生态 | AWS 生态 | SaaS 订阅 |

### 差异化护城河
- **工具无关 + 零 AI 依赖**：24 个适配器覆盖主流 AI 编码工具，不锁定任何平台
- **Brownfield 杀手锏**：delta spec 是对已有项目最友好的增量变更方式，竞品多数只擅长 greenfield
- **YC 品牌 + 增长数据**：8 个月 37K Stars + npm 249K 月下载，在 VC 和开发者社区双重验证

### 竞争风险
- GSD（48K Stars）在 Star 数上领先，且更重量级的方案在企业级场景可能更受欢迎
- 24 个适配器的维护成本随 AI 工具生态变化持续增长，单人维护模式不可持续
- 商业化路径尚不清晰——Workspaces 仍在 beta 招募阶段

### 生态定位
SDD（Spec-Driven Development）方法论的轻量级标杆实现。在 GSD（重量级）和 Kiro（平台锁定）之间，占据了「轻量 + 工具无关 + brownfield」的独特交叉位置。中文社区已有多个独立翻译 fork（776 Stars 的 cn 版），国际化势头良好。

## 套利机会分析
- **信息差**: 中等。37K Stars 说明英文社区已有广泛认知，但中文社区虽有翻译 fork，深度分析文章仍少。SDD 方法论本身值得科普
- **技术借鉴**: (1) Artifact DAG Schema + Kahn 算法的声明式 workflow 编排可用于任何 AI 工具链；(2) 24 工具适配层的 Adapter + Registry 模式是多平台适配的最佳实践；(3) Delta Spec 的 Markdown 约定格式可用于任何增量变更场景
- **生态位**: AI 编码工具链的「中间层协议」——类似 OpenAPI 之于 REST API
- **趋势判断**: SDD 是 2026 年 AI 编程的热门方法论（Medium 上出现「SDD is eating software engineering」），OpenSpec 处于风口。但 Post-1.0 后开发节奏明显放缓（2026-02 后几乎无实质提交），需关注项目活跃度走向

## 风险与不足
1. **单人创始人瓶颈**：Tabish 贡献 85%+ 代码，bus factor 为 1。YC 背景意味着可能很快招人，但目前仍是风险
2. **Post-1.0 活跃度下降**：2025-08 到 2026-01 密集迭代，2026-02 后提交骤减。可能在专注商业化（Workspaces），但也可能是精力转移
3. **Delta merge 并行冲突**：两个 change 并行修改同一 requirement 时后者覆盖前者，3-way merge 方案仍在规划中（#843）
4. **社区健康度偏低**：GitHub Community Profile 仅 37%，缺少 Code of Conduct、Contributing Guide、Issue/PR Template
5. **24 适配器维护成本**：AI 工具生态变化极快，每个工具的命令格式更新都需要同步 adapter
6. **商业化路径未明**：Workspaces 仍在 beta 招募，无定价信息，当前完全免费
7. **遥测争议风险**：内置 PostHog 遥测虽可关闭，但可能引起隐私敏感用户的反感

## 行动建议
- **如果你要用它**: `npx @fission-ai/openspec init` 即可在现有项目中初始化。从 `/opsx:propose` → `/opsx:apply` → `/opsx:archive` 三步工作流开始。brownfield 项目优先选择 OpenSpec 而非 Spec Kit/Kiro
- **如果你要学它**: 重点关注 `src/core/artifact-graph/`（DAG 引擎 + Kahn 拓扑排序）、`src/core/command-generation/`（24 工具适配层的 Adapter 模式）、`src/core/specs-apply.ts`（Delta spec 合并引擎）、`schemas/spec-driven/schema.yaml`（声明式 workflow 定义）
- **如果你要 fork 它**: (1) 实现 3-way delta merge 解决并行冲突；(2) 添加 Contributing Guide 和 Issue Template 提升社区健康度；(3) 为中文社区构建官方本地化版本（已有 776 Stars 的非官方中文 fork）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/Fission-AI/OpenSpec](https://deepwiki.com/Fission-AI/OpenSpec) |
| 官方文档 | [openspec.dev](https://openspec.dev/) |
| YC Profile | [ycombinator.com/companies/openspec](https://www.ycombinator.com/companies/openspec) |
| npm 包 | [@fission-ai/openspec](https://www.npmjs.com/package/@fission-ai/openspec) |
| Discord | [discord.gg/YctCnvvshC](https://discord.gg/YctCnvvshC) |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| 在线 Demo | 无（CLI 工具，需本地安装） |
