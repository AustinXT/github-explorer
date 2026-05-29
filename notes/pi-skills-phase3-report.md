# Phase 3：内容分析报告 — badlogic/pi-skills

## 动机与定位

- **要解决的问题**: AI 编码代理（如 Claude Code、Codex CLI、Amp、Droid）的能力边界止步于代码生成和文件操作，缺乏与"真实世界"的交互能力——不能搜索网页、不能操作浏览器、不能读邮件/日历/网盘、不能做语音转录。pi-skills 提供一组模块化的"技能插件"，为这些代理补充实际业务所需的外部交互能力。

- **为什么现有方案不够**:
  1. Claude Code 内置工具集（10+ 工具、万级 token 系统提示）重视安全防护但过于臃肿，与 pi 生态"4 个核心工具 + 约 200 token 提示"的极简哲学相悖。
  2. 各代理平台（Claude Code、Codex CLI、Amp、Droid）的技能发现机制各不相同（如 Claude Code 仅查找一级深度 `SKILL.md`），缺乏跨平台通用的技能格式。pi-skills 用统一的 `SKILL.md` + 辅助脚本格式，以最低共同约束兼容所有主流平台。
  3. 现有方案要么过于通用（缺乏针对性），要么过于耦合（绑定某一平台），没有一个项目同时做到"每个技能完全独立 + 跨平台 + 可 git clone 一键安装"。

- **目标用户**: 使用 pi-coding-agent、Claude Code、Codex CLI、Amp 或 Droid 的开发者，特别是需要让 AI 代理执行超越纯代码操作（搜索、浏览器自动化、Google Workspace 交互、语音转录）的场景。

---

## 作者视角

### 问题发现

Mario Zechner 的问题发现完全来自 **dogfooding**（自用实践）。他是 pi-mono 生态的创建者，pi-coding-agent 是其核心产品。在日常使用 pi-coding-agent 进行编码时，他反复遇到代理"无法走出编辑器"的瓶颈——需要搜索文档、需要检查网页渲染、需要处理邮件和日程——这些都是实际开发者的日常需求，但所有编码代理都没有内置支持。

时机选择方面：2025 年底正值 AI 编码代理爆发期（Claude Code、Codex CLI、Amp、Droid 等密集发布），各平台开始支持"技能/工具扩展"机制，这为 pi-skills 提供了一个标准化技能格式的跨平台窗口期。如果早两年做，代理生态尚未成熟，技能扩展机制不存在；如果晚两年做，各平台可能已形成各自封闭的技能生态。

### 解法哲学

**极简 Unix 哲学**：
- 每个技能是一个独立目录，包含一个 `SKILL.md`（供 LLM 阅读的指令文件）加若干轻量脚本。没有框架、没有抽象层、没有 SDK。
- "如果我不需要它，就不会构建它"——8 个技能，985 行源代码，没有一行是多余的。
- 不做运行时框架，不做技能注册表，不做版本管理——用 `git clone` 安装，用文件系统组织，用 symlink 解决平台适配。

**透明优先于防护**：
- 所有操作对 LLM 和用户完全可见，不做后台魔法。每个脚本都是可独立运行的 CLI 工具（`#!/usr/bin/env node`），人类可以直接执行和调试。
- 拒绝 Claude Code 式的复杂权限系统和沙箱机制，信任用户和 LLM。

**开放生态策略**：
- MIT 许可证，genuinely open。
- 用最低共同约束兼容所有平台（frontmatter 元数据 + markdown 指令 + 脚本文件），不锁定任何平台。

**明确选择不做**：
- 不做技能的自动发现/安装/更新机制（对比 eljulians/skillfile）
- 不做 IDE 深度集成（对比 Claude Code 原生技能系统）
- 不做权限/沙箱/安全控制（对比 Claude Code 的防护栏）
- 不做 TypeScript/编译步骤——所有代码直接可执行

### 背景知识迁移

1. **游戏引擎 → AI 代理**: Mario Zechner 作为 libGDX（知名 Java 游戏框架）的创建者，深谙"极简核心 + 可选模块"的设计哲学。libGDX 的成功经验（核心尽量小，功能通过扩展添加）被直接迁移到 pi 生态——4 个核心工具 + 技能插件体系。
2. **编译器工程 → 上下文工程**: 编译器需要高效管理有限的"寄存器"资源，类似地 LLM 的上下文窗口也是稀缺资源。作者对上下文工程的强调（"200 token 提示优于万 token 提示"）体现了编译器领域"资源约束下的优化思维"。
3. **CLI 工具文化 → SKILL.md 格式**: 每个技能本质上是一组 CLI 工具加一个"使用手册"（SKILL.md），这是经典 Unix 工具哲学（`man` 页面 + 可组合命令）在 LLM 时代的复兴。

### 战略图景

- **定位**: pi-skills 是 pi-mono 生态的外围扩展层，不是核心产品。核心是 pi-coding-agent（25,623 stars），pi-skills 是"技能商店"雏形。
- **商业化意图**: 无明显商业化信号。MIT 许可，无 SaaS/托管版迹象，无企业功能区分。更接近"开源工具箱"定位。
- **开源策略**: genuinely open——接受外部 PR（Michael Renner 贡献了 Brave API 迁移），不设贡献门槛。
- **远期图景**: 如果 pi-mono 成为编码代理的标准之一，pi-skills 将成为其技能生态的种子库，类似 Homebrew 之于 macOS 的角色——一个社区驱动的技能仓库。

---

## 架构与设计决策

### 目录结构概览

```
pi-skills/
├── README.md                    # 项目总览 + 多平台安装指南
├── LICENSE                      # MIT
├── .gitignore                   # node_modules/, .DS_Store
├── brave-search/                # 技能：网页搜索
│   ├── SKILL.md                 # LLM 指令文件
│   ├── search.js                # 搜索脚本（199 行）
│   ├── content.js               # 内容提取脚本（86 行）
│   ├── package.json             # 依赖声明
│   └── package-lock.json        # 依赖锁定
├── browser-tools/               # 技能：浏览器自动化
│   ├── SKILL.md                 # LLM 指令文件（含效率指南）
│   ├── browser-start.js         # 启动 Chrome（86 行）
│   ├── browser-nav.js           # 页面导航（44 行）
│   ├── browser-eval.js          # JS 执行（53 行）
│   ├── browser-screenshot.js    # 截图（34 行）
│   ├── browser-pick.js          # 交互式元素选取（162 行）
│   ├── browser-cookies.js       # Cookie 查看（35 行）
│   ├── browser-content.js       # 内容提取（103 行）
│   ├── browser-hn-scraper.js    # HN 爬虫示例（108 行）
│   ├── package.json             # 依赖声明
│   └── package-lock.json        # 依赖锁定
├── gccli/                       # 技能：Google Calendar
│   └── SKILL.md                 # 纯指令文件（引用全局 CLI 工具）
├── gdcli/                       # 技能：Google Drive
│   └── SKILL.md                 # 纯指令文件
├── gmcli/                       # 技能：Gmail
│   └── SKILL.md                 # 纯指令文件
├── transcribe/                  # 技能：语音转录
│   ├── SKILL.md                 # LLM 指令文件
│   ├── transcribe.sh            # Shell 脚本（31 行）
│   └── .gitignore               # config
├── vscode/                      # 技能：VS Code diff
│   └── SKILL.md                 # 纯指令文件
└── youtube-transcript/          # 技能：YouTube 字幕
    ├── SKILL.md                 # LLM 指令文件
    ├── transcript.js            # 提取脚本（44 行）
    └── package.json             # 依赖声明
```

项目采用完全扁平的目录结构，每个技能一个独立目录。没有共享代码、没有 monorepo 工具链、没有构建系统。这是刻意的设计：每个技能是完全自包含的可部署单元。

### 关键设计决策

1. **决策**: SKILL.md 作为"LLM 可读的 man page"
   - **问题**: LLM 代理需要知道如何使用一个技能（能做什么、怎么调用、参数格式），但传统的文档（README）是写给人看的，API 定义（OpenAPI/JSON Schema）是给机器解析的，两者都不够理想。
   - **方案**: 用 YAML frontmatter（name + description）做结构化元数据 + markdown 正文做自然语言指令。`{baseDir}` 占位符在运行时替换为技能目录的实际路径。SKILL.md 既是人类可读文档，也是 LLM 直接消费的指令。
   - **Trade-off**: 牺牲了机器可解析的严格类型约束（如 JSON Schema 定义参数类型），换来了极低的创建门槛（写 markdown 即可）和对 LLM 的天然亲和力。
   - **可迁移性**: **高** — 任何需要"教 LLM 使用工具"的场景都可复用此模式。

2. **决策**: 每个脚本是独立的可执行 CLI 工具
   - **问题**: 代理需要执行外部操作，但常见做法是通过 SDK/API 调用，这需要运行时框架和进程内集成。
   - **方案**: 每个操作对应一个独立的 `#!/usr/bin/env node`（或 `#!/bin/bash`）脚本，通过 shell 命令行调用，输入是命令行参数，输出是 stdout 文本。
   - **Trade-off**: 牺牲了调用效率（每次启动新进程）和类型安全（文本输入输出），换来了语言无关性（Node.js、Bash 混用）、可调试性（人类可直接运行）和最大的兼容性（任何能执行 shell 命令的代理都能使用）。
   - **可迁移性**: **高** — "工具即 CLI"是一种通用的代理工具设计模式。

3. **决策**: puppeteer-core 的 connect 模式（而非 launch 模式）
   - **问题**: 浏览器自动化有两种模式——启动新浏览器实例（launch）或连接到已运行的浏览器（connect）。Launch 模式简单但每次创建新实例，connect 模式复杂但可复用已有会话。
   - **方案**: `browser-start.js` 负责启动 Chrome 并开启 `--remote-debugging-port=9222`，后续所有工具（nav、eval、screenshot 等）通过 `puppeteer.connect({browserURL: "http://localhost:9222"})` 连接到这个持久实例。
   - **Trade-off**: 牺牲了"开箱即用"（需要先运行 start），换来了：(1) 用户可以在同一浏览器中看到代理操作；(2) 支持 `--profile` 复用用户已有的登录状态和 Cookie；(3) 多个工具共享同一浏览器实例，避免重复启动开销。
   - **可迁移性**: **中** — 适用于所有需要有状态浏览器会话的自动化场景，但对无头环境（CI/CD）不友好。

4. **决策**: Readability + Turndown 管线做"网页 → Markdown"转换
   - **问题**: LLM 需要消费网页内容，但原始 HTML 充满噪音（导航、广告、脚本），浪费宝贵的上下文窗口。
   - **方案**: 使用 Mozilla Readability 提取正文 → TurndownService（含 GFM 插件）转换为 Markdown。额外清理规则包括：移除空链接、合并多余空格、压缩换行。`search.js` 中内容截断至 5000 字符。
   - **Trade-off**: 牺牲了页面完整性（导航结构、侧边栏、互动元素均被剔除），换来了对 LLM 高度友好的干净文本。
   - **可迁移性**: **高** — 任何需要向 LLM 提供网页内容的场景都可复用此管线。

5. **决策**: Google Workspace 技能仅包含 SKILL.md（无代码）
   - **问题**: Gmail/Drive/Calendar 的 CLI 工具已作为独立 npm 包存在（`@mariozechner/gmcli` 等），技能层只需教 LLM 如何使用。
   - **方案**: gccli、gdcli、gmcli 三个技能目录各只含一个 SKILL.md 文件，引导 LLM 使用全局安装的 CLI 工具。
   - **Trade-off**: 牺牲了自包含性（依赖外部全局安装的工具），换来了关注点分离——CLI 工具本身在 pi-mono 或独立仓库中维护和发布。
   - **可迁移性**: **中** — 适用于已有 CLI 工具需要被 LLM 代理调用的场景。

6. **决策**: browser-pick.js 的交互式 DOM 元素选取
   - **问题**: 当用户告诉代理"点击那个按钮"时，代理需要精确定位 DOM 元素，但页面结构可能非常复杂。
   - **方案**: 注入一个 `window.pick()` 函数到页面中，创建浮动覆盖层、高亮追踪层和底部提示栏，支持单选、Cmd/Ctrl 多选和 Enter 确认。返回选中元素的 CSS 选择器、HTML 片段和父元素链。
   - **Trade-off**: 牺牲了全自动化能力（需要人类在屏幕前交互），换来了精准的元素定位和人机协作的自然体验。
   - **可迁移性**: **中** — 适用于所有需要"人在回路"的浏览器自动化场景。

7. **决策**: browser-eval.js 中 AsyncFunction 的动态构造
   - **问题**: 需要在浏览器页面中执行任意 JavaScript，包括异步代码。
   - **方案**: 使用 `const AsyncFunction = (async () => {}).constructor; return new AsyncFunction(\`return (${code})\`)();` 将用户输入的代码字符串包装为异步函数执行。
   - **Trade-off**: 牺牲了安全性（任意代码执行），换来了极大的灵活性——代理可以执行任何 JavaScript。
   - **可迁移性**: **中** — 适用于受信任环境中的浏览器脚本注入。

---

## 创新点

1. **SKILL.md 作为"LLM 原生"工具文档格式**
   - **描述**: 用 YAML frontmatter 做结构化元数据 + Markdown 做自然语言指令，创造了一种"LLM 可读的 man page"格式。不同于 OpenAPI/JSON Schema（面向机器解析），也不同于 README（面向人类阅读），SKILL.md 是面向 LLM 阅读而优化的文档格式——简洁、示例丰富、包含"When to Use"决策指引。
   - **新颖度**: 3/5 | **实用性**: 5/5 | **可迁移性**: 5/5
   - **适用场景**: 任何需要教 LLM 使用外部工具的系统；代理技能生态的文档标准化。

2. **browser-pick.js 的"人在回路"元素选取**
   - **描述**: 在无障碍地突破"代理看到的 DOM"和"用户看到的页面"之间鸿沟的方案。通过注入交互式选取器，让人类用鼠标精确指定目标元素，代理再基于选取结果执行操作。这是一种优雅的人机协作模式——代理不试图完全理解页面，而是请求人类指引。
   - **新颖度**: 4/5 | **实用性**: 4/5 | **可迁移性**: 3/5
   - **适用场景**: 浏览器自动化中的模糊意图场景；Web 测试中的元素定位辅助。

3. **browser-tools SKILL.md 中的"效率指南"**
   - **描述**: SKILL.md 不仅告诉 LLM 能做什么，还教它如何高效地做——"DOM Inspection Over Screenshots"、"Complex Scripts in Single Calls"、"Batch Interactions"。这是"上下文工程"理念的具体实践：用少量额外提示大幅提升 LLM 的工具调用效率。
   - **新颖度**: 4/5 | **实用性**: 5/5 | **可迁移性**: 5/5
   - **适用场景**: 任何 LLM 工具文档——在"能做什么"之外增加"应该怎么做"的指导。

4. **CDP 直连模式 + profile 复制的浏览器自动化**
   - **描述**: 通过 `rsync` 复制用户的 Chrome profile（排除 Session 相关文件），让自动化浏览器继承用户的登录态、Cookie 和扩展。这解决了浏览器自动化中的"认证鸿沟"——大多数自动化工具每次从零开始，需要重新登录。
   - **新颖度**: 3/5 | **实用性**: 4/5 | **可迁移性**: 3/5（macOS 专属路径）
   - **适用场景**: 需要访问登录态内容的自动化场景；代理辅助的网站操作。

5. **Readability + Turndown + 正则清理 三阶段内容提取管线**
   - **描述**: 三阶段管线：(1) Mozilla Readability 提取正文 → (2) Turndown + GFM 插件转 Markdown → (3) 正则清理空链接/多余空白/多余换行。这在 `search.js`、`content.js` 和 `browser-content.js` 中被重复使用（代码有轻微重复但保持了各脚本的独立性）。
   - **新颖度**: 2/5 | **实用性**: 5/5 | **可迁移性**: 5/5
   - **适用场景**: 任何需要将网页内容供给 LLM 消费的场景。

---

## 可复用模式

1. **SKILL.md 模式**: YAML frontmatter 元数据 + Markdown 自然语言指令 + `{baseDir}` 路径占位符 = LLM 原生的工具文档格式。适用场景：为任何 AI 代理系统设计可发现、可理解的工具扩展。

2. **CLI-as-Tool 模式**: 每个代理能力封装为独立的可执行脚本，通过 shell 命令行调用，文本输入输出。适用场景：需要语言无关、进程隔离、人类可调试的代理工具集。

3. **Connect-to-Persistent-Browser 模式**: 分离"启动浏览器"和"使用浏览器"两个阶段，通过 CDP 远程调试端口保持持久会话。适用场景：需要有状态浏览器交互的自动化。

4. **HTML-to-LLM-Markdown 管线**: Readability → Turndown(GFM) → 正则清理，含 5000 字符截断。适用场景：任何需要从网页提取 LLM 可消费内容的系统。

5. **Profile-Rsync 认证继承**: 用 rsync 复制 Chrome profile（排除 Session 文件和 Singleton 锁），继承用户的登录态。适用场景：需要复用已有认证的浏览器自动化。

6. **LLM 效率提示嵌入工具文档**: 在工具使用说明中嵌入"反模式 → 正确模式"的效率指南（如"Don't take screenshots, Do parse DOM"）。适用场景：任何需要引导 LLM 高效使用工具的场景。

---

## 竞品交叉分析

### vs pchalasani/claude-code-tools（1,593 stars）

- **我们更好**: pi-skills 跨平台兼容（支持 5 个代理平台），而 claude-code-tools 仅限 Claude Code。pi-skills 的技能更多样化（搜索、浏览器、Google Workspace、转录、YouTube），claude-code-tools 更偏向开发者工具增强。
- **竞品更好**: claude-code-tools 与 Claude Code 深度集成，可能在 Claude Code 生态内提供更流畅的体验；拥有更高的 star 数和社区认知度。
- **不同目标**: pi-skills 是跨平台技能库，核心追求"平台无关性"；claude-code-tools 是 Claude Code 专属增强工具，追求"平台深度集成"。
- **用户迁移成本**: 低。两者技能互不冲突，可以并行使用。

### vs twostraws/SwiftUI-Agent-Skill（2,930 stars）

- **我们更好**: pi-skills 覆盖通用场景（搜索、浏览器、邮件等），应用面更广；SwiftUI-Agent-Skill 仅限 SwiftUI 领域。
- **竞品更好**: SwiftUI-Agent-Skill 在 SwiftUI 领域的深度远超 pi-skills 所能提供的任何通用工具。更高的 star 数表明更大的社区影响力。
- **不同目标**: 完全错位竞争。pi-skills 做"通用外部交互能力"，SwiftUI-Agent-Skill 做"特定领域知识增强"。两者互补而非替代。
- **用户迁移成本**: 不适用，两者解决不同问题。

### vs 0xranx/OpenContext（450 stars）

- **我们更好**: pi-skills 提供的是可执行的"动作能力"（搜索、浏览、发邮件），而 OpenContext 提供的是"上下文数据"（个人知识库）。pi-skills 让代理能做更多事，OpenContext 让代理知道更多事。
- **竞品更好**: OpenContext 在"个人上下文记忆"这个维度上更专注，可能提供更好的个人化体验。
- **不同目标**: pi-skills = 能力扩展（做什么），OpenContext = 知识扩展（知道什么）。互补关系。
- **用户迁移成本**: 不适用，两者可以同时安装。

### vs eljulians/skillfile（69 stars）

- **我们更好**: pi-skills 提供的是具体的、可执行的技能实现，而 skillfile 是一个技能搜索/安装/管理平台（元层）。pi-skills 有实际功能代码，skillfile 解决的是发现和分发问题。
- **竞品更好**: skillfile 如果生态建立，可以成为 pi-skills 等技能库的"App Store"，解决技能发现和版本管理问题——这些 pi-skills 目前完全没有。
- **不同目标**: pi-skills = 技能实现，skillfile = 技能平台。前者可以被后者索引和分发。
- **用户迁移成本**: 不适用，两者可互补。

### vs Claude Code 原生技能系统

- **我们更好**: pi-skills 跨平台兼容，不绑定 Anthropic 生态；技能创建门槛更低（写 markdown + 脚本即可）；更透明（无黑盒封装）。
- **竞品更好**: Claude Code 原生技能系统拥有平台级支持（自动发现、权限管理、沙箱隔离）、海量用户基数、以及 Anthropic 持续投入的工程资源。IDE 集成（VS Code 扩展）也是 pi-skills 不具备的。
- **不同目标**: pi-skills 追求"极简、透明、跨平台"，Claude Code 原生系统追求"安全、集成、平台深度"。
- **用户迁移成本**: 中等。Claude Code 原生技能格式与 SKILL.md 格式不完全兼容（Claude Code 仅查找一级深度），需要用 symlink 适配。

### 综合竞争结论

- **差异化护城河**:
  - **技术护城河**: 无显著技术壁垒，核心代码不足 1000 行，但"极简"本身是一种设计立场。
  - **生态护城河**: 来自 pi-mono 生态（25,623 stars），pi-skills 是 pi-coding-agent 的"官方技能库"，与主项目的生态绑定是最大优势。
  - **信任护城河**: Mario Zechner 15 年开源声誉（libGDX 等项目），在独立开发者社区有高可信度。

- **竞争风险**: 最可能被 **Claude Code 原生技能系统** 替代——随着 Anthropic 不断丰富内置技能和第三方技能生态，pi-skills 的价值可能被逐步吸收。特别是如果 Claude Code 原生支持搜索、浏览器自动化、Google Workspace 集成等功能。

- **生态定位**: pi-skills 在技术生态中扮演"早期技能模板库"的角色——它展示了"AI 代理技能应该是什么样的"（极简、独立、跨平台），但随着生态成熟，具体的技能实现可能被平台原生能力取代，而"SKILL.md 格式"和"极简设计哲学"可能作为设计影响存续更久。

---

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | 良好 | 代码简洁清晰，985 行实现 8 个技能。命名规范、结构一致。存在轻微代码重复（htmlToMarkdown 函数在 3 个文件中重复定义），但这是刻意的设计选择（保持各脚本独立性）。 |
| 文档质量 | 优秀 | 745 行 Markdown 文档，每个技能都有详尽的 SKILL.md。browser-tools 的效率指南尤为出色。README 包含所有平台的安装说明。 |
| 测试覆盖 | 无 | 没有任何测试文件。对于工具性脚本集，可以理解（每个脚本都是可手动验证的 CLI 工具），但在回归防护上有缺失。 |
| CI/CD | 无 | 没有 .github 目录，没有任何 CI/CD 配置。 |
| 错误处理 | 一般 | 基本的错误处理存在（API 错误、连接超时、文件不存在），但不统一。部分用 process.exit(1)，部分用 try-catch，缺乏标准化的错误报告格式。 |

### 质量检查清单

- [ ] 有测试（单元/集成/E2E）
- [ ] 有 CI/CD 配置
- [x] 有文档（不仅是 README）— 每个技能都有详尽的 SKILL.md
- [x] 错误处理规范（基本存在，但不够统一）
- [ ] 有 linter / formatter 配置
- [ ] 有 CHANGELOG
- [x] 有 LICENSE — MIT
- [x] 有示例代码 / examples — browser-hn-scraper.js 是一个完整的示例；SKILL.md 中嵌入了丰富的使用示例
- [x] 依赖版本锁定（lock file）— brave-search 和 browser-tools 都有 package-lock.json
