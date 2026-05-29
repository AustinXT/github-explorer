# jarrodwatts/claude-hud 深度分析报告

> GitHub: https://github.com/jarrodwatts/claude-hud

## 一句话总结

Claude Code 的实时运行状态仪表盘插件——通过解析 stdin JSON + transcript JSONL 双数据源，在终端 statusline 上展示上下文使用率、活动工具、运行中 Agent 和 Todo 进度，零运行时依赖、进程级隔离，3 个月 10K star。

## 值得关注的理由

1. **精准的痛点 + 原生 API 利用**：Claude Code 用户最关心"上下文用了多少？离 autocompact 多远？当前在执行什么？"——claude-hud 直接使用 Claude Code 的 statusline API，无需 tmux/分屏，是最自然的集成方式。在"实时运行状态可视化"这个细分赛道几乎无直接竞品
2. **零依赖 + 进程隔离的极致工程**：`dependencies` 为空，仅用 Node.js 内建模块。每次渲染是独立进程调用，通过文件缓存跨进程共享状态——崩溃隔离、内存零泄漏、不影响 Claude Code 主进程
3. **Claude Code 插件开发的参考实现**：`.claude-plugin/` 元数据 + `commands/*.md` 声明式安装向导 + statusline API + transcript JSONL 解析——这套模式是开发 Claude Code 插件的标准范式

## 项目展示

README 中的预览截图展示了 HUD 在终端中的实际效果：上下文使用率进度条（三级颜色）、模型/计划标签、活动工具列表、Agent 状态、Todo 进度、Git 信息，以 Expanded 或 Compact 两种布局呈现。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/jarrodwatts/claude-hud |
| Star / Fork | 10,416 / 446 |
| 代码行数 | 8,704 (JavaScript 52%, TypeScript 37%, JSON 10%) |
| 项目年龄 | 3 个月（2026-01-02 创建） |
| 开发阶段 | 快速迭代（v0.0.10，爆发-沉淀-迭代模式） |
| 贡献模式 | 独立开发（Jarrod Watts 占 64%，30 位社区贡献者） |
| 热度定位 | 大众热门（3 个月 10K star，Claude Code 插件生态头部） |
| 质量评级 | 代码[A] 文档[A+] 测试[A] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Jarrod Watts (@jarrodwatts)，悉尼，澳洲开发者。144 个公开仓库，977 GitHub followers。在 Claude Code 插件生态爆发初期精准抓住了"运行状态可视化"这个垂直方向。

### 问题判断

Claude Code 用户在长会话中面临一个持续的焦虑：**不知道上下文还剩多少、不知道当前在执行什么、不知道离 autocompact 还有多远**。这些信息虽然存在于 Claude Code 内部，但没有一个持续可见的展示方式。statusline API 的推出让这个问题有了原生解决方案。

### 解法哲学

"极致轻量 + 原生集成"——核心原则：
1. **零运行时依赖**：仅用 Node.js 内建模块，不引入任何第三方包
2. **进程隔离**：每次渲染是独立进程，通过文件缓存共享状态
3. **声明式安装**：setup.md 和 configure.md 是纯 Markdown，利用 Claude 自动执行安装向导（"AI-as-installer"）
4. **双数据源融合**：stdin JSON（Claude Code 主动推送）+ transcript JSONL（文件系统解析）互补

### 战略意图

个人开源项目，通过 Claude Code 插件市场分发。在 Claude Code 生态的工具层建立影响力。

## 核心价值提炼

### 创新之处

1. **双数据源融合架构**（新颖度 4/5 × 实用性 5/5）
   stdin JSON 提供实时上下文数据（model/token usage/cwd），transcript JSONL 提供工具调用/Agent/Todo 状态。两个数据源互补，构建了完整的 Claude Code 运行时视图

2. **Autocompact Buffer 估算**（新颖度 4/5 × 实用性 5/5）
   `getBufferedPercent()` 模拟 Claude Code 的 autocompact 行为——低使用率不加 buffer，高使用率逐渐增加 buffer 占比，使显示百分比更接近用户感知的真实值

3. **"AI-as-installer" 声明式命令**（新颖度 4/5 × 实用性 4/5）
   `commands/setup.md`（288 行）和 `configure.md`（306 行）是纯 Markdown 文件，定义多步骤安装和配置流程。Claude 读取 Markdown 中的指令自动执行——用自然语言编写安装脚本

4. **零依赖进程隔离**（新颖度 3/5 × 实用性 5/5）
   每次 statusline 渲染是独立 Node.js 进程，通过文件缓存跨进程共享状态。崩溃不影响 Claude Code、内存零泄漏、零依赖安装

5. **Extra Command 扩展点**（新颖度 3/5 × 实用性 4/5）
   `--extra-cmd` 允许注入自定义 shell 命令，输出 `{ label: string }` 即可在 HUD 显示，带完善的安全消毒（strip ANSI/bidi/控制字符）

### 可复用的模式与技巧

1. **Claude Code 插件开发范式**：`.claude-plugin/plugin.json` + `commands/*.md` 声明式命令 + statusline API。任何 Claude Code 插件可参考
2. **DI 友好的 main 函数**：`main(overrides: Partial<MainDeps>)` 所有 I/O 可替换，无需 mock 框架即可测试。适用于所有 CLI 工具
3. **跨进程文件缓存**：usage API 结果和 speed tracker 数据通过文件缓存在独立进程间共享。适用于所有"每次调用是独立进程"的场景
4. **Transcript JSONL 解析**：流式解析 Claude Code 写出的 JSONL 获取工具调用/Agent/Todo 状态。标准的 Claude Code 内部状态获取方法
5. **Grapheme-aware 终端渲染**：`Intl.Segmenter` 正确计算 CJK/emoji 宽度 + 智能分段换行

### 关键设计决策

| 决策 | 牺牲了什么 | 换来了什么 |
|------|-----------|-----------|
| 零运行时依赖 | 需自实现 HTTP/JSON/色彩等基础功能 | 极速安装、零冲突、零 CVE 风险 |
| 进程隔离（每次渲染新进程） | 启动开销（~50ms） | 崩溃隔离、内存零泄漏 |
| 文件缓存替代内存状态 | I/O 开销 | 跨进程状态共享、重启无丢失 |
| Markdown 声明式安装 | 安装依赖 Claude 正确理解指令 | 零摩擦安装体验 |
| 双数据源（stdin + transcript） | 复杂度（两套解析逻辑） | 数据完整性（实时数据 + 历史工具状态） |

## 竞品格局与定位

### 竞品对比

| 维度 | claude-hud | 其他 Claude 插件 |
|------|-----------|-----------------|
| 定位 | 实时运行状态可视化 | Agent/Memory/Prompt |
| 赛道 | 独占（无直接竞品） | 高度竞争 |
| Star | 10,416 | 变化大 |
| 数据源 | stdin + transcript 双源 | 各异 |
| 依赖 | 零 | 通常有多个 |

### 差异化护城河

1. **赛道独占**：在 Claude Code 插件中唯一做"实时运行状态 HUD"的项目
2. **原生 API 集成**：使用 Claude Code 的 statusline API，不是 hack 或 workaround
3. **工程质量极高**：零依赖 + 进程隔离 + 完善测试 + 商业级文档

### 竞争风险

- 如果 Anthropic 将 HUD 功能内置到 Claude Code 中，该项目将失去存在意义
- statusline API 如果变更，需要及时适配
- 单人维护（Bus Factor = 1）

### 生态定位

Claude Code 插件生态中的"仪表盘"——填补了"用户需要实时感知 Claude Code 运行状态"的空白。与 Memory/Prompt/Agent 类插件互补。

## 套利机会分析

- **信息差**: Claude Code 的 statusline API 和 transcript JSONL 格式尚未被广泛利用——将这些 API 用于构建其他类型的 Claude Code 监控/分析工具是直接的信息差
- **技术借鉴**: (1) 零依赖进程隔离模式；(2) DI 友好 main 函数；(3) Transcript JSONL 解析；(4) Autocompact buffer 估算算法；(5) Markdown 声明式安装向导
- **生态位**: Claude Code 生态的"可观测性层"
- **趋势判断**: Claude Code 用户量爆发推动插件生态增长，HUD 作为基础设施级插件需求持续

## 风险与不足

1. **Anthropic 内置风险**：如果 Claude Code 原生提供 HUD 功能，该项目将被淘汰
2. **Bus Factor = 1**：Jarrod Watts 一人维护
3. **API 依赖**：依赖 Claude Code 的 stdin JSON 格式和 transcript JSONL 格式，API 变更需及时适配
4. **Windows/PowerShell 兼容性**：Issue #196 等暴露的跨平台问题
5. **Usage API 稳定性**：429 限流和认证问题（Issue #235）

## 行动建议

- **如果你要用它**: 通过 Claude Code 插件市场安装或 `/claude-hud:setup` 命令。适合所有 Claude Code 重度用户，特别是关心上下文窗口使用率和工具执行状态的场景
- **如果你要学它**: 重点关注以下文件：
  - `src/index.ts` — 入口编排：数据采集 → 渲染的完整流程
  - `src/stdin.ts` — Claude Code stdin JSON 数据格式和解析
  - `src/transcript.ts` — Transcript JSONL 解析（工具/Agent/Todo 状态提取）
  - `src/usage-api.ts` — OAuth + Anthropic Usage API 客户端（含缓存/退避策略）
  - `src/render/index.ts` (467 行) — Expanded/Compact 双模式渲染 + 终端自适应
  - `commands/setup.md` (288 行) — "AI-as-installer" 声明式安装向导
- **如果你要 fork 它**: 可改进方向：
  - 添加 Web UI dashboard 模式（浏览器访问而非终端 statusline）
  - 历史会话统计和分析（token 消耗趋势、工具使用频率）
  - 多会话并行监控

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/jarrodwatts/claude-hud](https://deepwiki.com/jarrodwatts/claude-hud) |
| Zread.ai | [zread.ai/jarrodwatts/claude-hud](https://zread.ai/jarrodwatts/claude-hud) |
| 作者博客 | [jarrodwatts.com](https://jarrodwatts.com) |
| 关联论文 | 无 |
| 在线 Demo | 无（Claude Code 插件需本地安装） |
