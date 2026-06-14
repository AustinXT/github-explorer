# 20K stars · 4 年：vhs 把终端录屏变成可 diff 的源码

> GitHub: https://github.com/charmbracelet/vhs

## 一句话总结

把「录制终端 GIF」从手工录屏重写成「一份声明式 `.tape` 源码 → 可复现的 GIF/MP4/WebM + 可断言的文本快照」，让 README 里的演示 GIF 像代码一样进版本控制、进 PR review、进 CI 视觉回归。

## 值得关注的理由

- **把演示材料也变成 source artifact** — 一段 30 秒的 GIF，对应的就是 30 行可 diff 的 `.tape`，从此 README Demo 不再是「录一次定终身」。
- **声明式同步原语终结 Sleep 调试地狱** — `Wait /prompt$/`、`Wait+Screen /regex/` 用正则 + 10ms 轮询，让 tape 对启动速度、网络延迟免疫（Issue #70 推动）。
- **SSH-as-Rendering-FaaS 是行业首创** — `ssh vhs.charm.sh < demo.tape > out.gif` 一行完成上传+渲染+下载，给受限网络/CI 提供零依赖的渲染能力。
- **20K stars 跨入头部，4 年仍然只是 v0.11.0** — 项目已经从「密集开发」进入「稳定维护 + 生态扩张」期，但仍持续有新 issue 推动设计（ttyd/go-rod 脆弱性议题 #232/#233/#45）。

## 项目展示

![Welcome to VHS (neofetch demo)](https://stuff.charm.sh/vhs/examples/neofetch_3.gif)

这是 README 顶部的 hero GIF——一个完整的「vhs 录制自家产品 neofetch」的演示，**录制对象本身是工具**。

![Demo GIF produced by the VHS code above](https://stuff.charm.sh/vhs/examples/demo.gif)

README 第一节的「demo.tape」实时录制产物——这一张 GIF 的源码就是同目录的 `demo.tape` 几十行文本。

![Width / Height / LetterSpacing demo](https://stuff.charm.sh/vhs/examples/width.gif)

三件布局/字号/字间距 demo 之一，演示 `.tape` 中的 `Set Width/Height/LetterSpacing` 全程可参数化。

> 官网（charm.land/vhs）当前是 301 重定向到 GitHub README，无独立 hero 视频；上面 4 张图全部来自 `stuff.charm.sh/vhs/examples/`，README 长期引用。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/charmbracelet/vhs |
| Star / Fork | 19,957 / 436（Watcher: 31） |
| 代码行数 | 16,204（Go 33.7% 5,461 行 / JSON 66.0% 10,689 行（单文件聚合） / Dockerfile+Makefile+Shell 0.3%） |
| 项目年龄 | 46.9 个月（首次提交 2022-07-19） |
| 总 commits | 751（最近一次 2026-05-04） |
| 开发阶段 | 低维护（近 30 天 0 commit、近 90 天 4 commit、近 365 天 38 commit） |
| 贡献模式 | 小团队 + 社区（62 名贡献者，Top Maas Lalani 61.6%，Charm 团队 caarlos0/Ayman Bagabas 维护） |
| 热度定位 | 大众热门（heat_level：20k★ 跨入 4 位数头部） |
| 增长模式 | 高速增长（基于 156 个 stargazer 采样，跨度 15 天，平均 ~10 star/天） |
| 质量评级 | 代码良好 / 文档优秀 / 测试基本（缺 E2E）/ CI 完善 |
| License | MIT |
| Release | v0.11.0（共 15 个 tag，从 v0.0.1 → v0.11.0 几乎每个 minor 都打 tag） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Charmbracelet 是一家专做「让命令行变 glamorous」的开源组织，旗下 lipgloss（终端样式）、bubbletea（TUI 框架）、glamour（Markdown 渲染）、gum（交互输入）、glow（Markdown 阅读器）构成完整的「终端美学」栈。Maas Lalani 是 vhs 的主要创作者（贡献占比 61.6%），核心维护者还包括 Charm 团队创始人 caarlos0、工程师 Ayman Bagabas 等。

### 问题判断

CLI/TUI 工具作者最深的一个痛点是：**怎么让用户在不跑工具的情况下也能感受到它的体验？** 现有解法是手工录屏 → ScreenToGif/LICEcap → 后期调色 → README 嵌入 GIF。这个流程有三个硬伤：

1. **不可复现**：每次录制结果因字体度量、光标闪烁、随机抖动 bit-flake，CI 跑视觉回归成笑话。
2. **不可 review**：PR 改一行逻辑，GIF 必须重新录，「视频长什么样」在 code review 里无从下手。
3. **不可入库**：GIF 是二进制，无 diff、无 blame、无 history。

Charm 自身是 TUI 重度用户（dogfooding 链路：bubbletea/lipgloss/gum 都是自家产品），所以痛点先在自己团队炸开——vhs 的产品形态直接来自「把自家工程实践沉淀成工具」。

### 解法哲学

**声明式胜过程序式**：不写「在第 N 帧按 K 键」，而是写「Wait /prompt$/ → Type "y" → Enter」，让 tape 在不同终端速度下都稳健——这是把 GUI 自动化测试的最佳实践（Selenium 的 `wait_for_*`）移植到 CLI 录制。

**显式选了什么不做**：
- 不做交互式录制为主路径（核心是 write-not-record；`vhs record` 只是辅助）。
- 不做云端 SaaS 版编辑器（云端只托管产物 `vhs.charm.sh`）。
- 不做窗口级录制（只录 terminal 字符 canvas——这就是「Glaze 你的 CLI」哲学的延伸）。

**AI-aesthetic 同源**：与 lipgloss/glamour 的视觉语言统一（macaron 调色板、SVG 徽章），让生成的 GIF 在视觉上「看着就是 Charmbracelet 出品」——这是生态品牌策略，不是技术策略。

### 战略意图

vhs 是 Charmbracelet「TUI 美学品牌」的产品化收口——CLI 作者工具链上唯一需要「出镜」的环节。crush（25.3k★，AI 终端客户端）和 bubbletea 是赚眼球的核心，vhs 是让这些工具「绕过录屏」的基础设施。**商业化路径**：vhs.charm.sh 是 SaaS 形态的「分享层」（`publish.go` 直接 SSH 到 ghost.charm.sh:22 传 GIF），托管/分享是商业化探索而非编辑器 SaaS。**开源策略**：genuinely open（MIT），核心渲染管线全在仓库内，仅云端托管是闭源服务。

## 核心价值提炼

### 创新之处

按新颖度×实用性排序：

1. **`.tape` DSL 作为可 diff 的视频源文件**（新颖度 4/5 · 实用性 5/5）— `lexer/parser/token` 三件套解析出 `[]Command`，改动一行就是改动一段视频的某个时间点，整份 `.tape` 可走 PR review。
2. **`vhs serve` SSH-as-Rendering-FaaS**（新颖度 5/5 · 实用性 4/5）— 客户端 `ssh vhs.charm.sh < demo.tape > out.gif` 一行完成上传+渲染+下载，首次把 SSH 协议用于无客户端二进制分发。
3. **`.txt` / `.ascii` / `.test` 文本断言输出**（新颖度 4/5 · 实用性 5/5）— 每次执行命令都把 `term.buffer.active` 序列化写入文本文件，可作为 golden test 与 `diff` 工具对接，把视觉测试变成 CI friendly。
4. **`Wait+Screen /regex/` 声明式同步原语**（新颖度 3/5 · 实用性 5/5）— 放弃 `Sleep`，用正则 + 10ms 轮询 + 超时让 tape 对启动速度免疫；`Wait+Line` 限定单行，`Wait+Screen` 全屏扫。
5. **`vhs record` PTY→.tape 反向翻译器**（新颖度 4/5 · 实用性 4/5）— 录制时把 PTY escape sequence 翻回 tape 指令（`\x1b[A` 翻回 `Up`），并自动插入 `Sleep 500ms`、合并连续同指令为 `Left 3`。
6. **`Set Theme {...}` 内联 JSON + Levenshtein 模糊匹配**（新颖度 3/5 · 实用性 4/5）— 300+ 主题查表 + JSON 内联覆盖 + 拼错时给「did you mean」。

### 可复用的模式与技巧

1. **三段式 DSL 骨架（token + lexer + parser）** — 适用任何需要「带行号错误的小型 DSL」。vhs 是教科书实现（`token/lexer/parser` 三包独立 + `IsSetting/IsCommand/IsModifier` 分类谓词），零外部 parser generator 依赖。
2. **SSH-as-FaaS 模式（wish + `charmbracelet/ssh`）** — 适用受限网络下需要零依赖 RPC。`charmbracelet/wish` 提供 middleware 链 + auth + host key 一站式。
3. **「正则 + 轮询 + 超时」声明式同步** — 适用所有「等待不确定耗时的事件」。`WaitTick = 10ms` + 正则匹配 + 超时，是替代 `Sleep` 的通用解。
4. **「浏览器 canvas → ffmpeg palette」动效录制管线** — 适用需要高品质 GIF/WebM/MP4 的 web 动效录制。ttyd 起 xterm.js → go-rod 抓 canvas → ffmpeg `palettegen+paletteuse` 产 256 色 GIF。
5. **「keymap 表 + 修饰键链式语法」**（`Ctrl+Shift+Tab`） — 适用任何需要解析「按键组合 DSL」的工具。
6. **「设置必须在初始化阶段」的硬约束**（`evaluator.go:155-159`） — 适用所有「运行时改配置会破坏渲染/状态机」的系统。

### 关键设计决策

1. **`Set` 命令必须在 `.tape` 顶端（除 `TypingSpeed`）**
   - 问题：渲染期改 `FontFamily`/`FontSize` 会让 xterm.js canvas 维度跳变，FFmpeg palettegen 会算出错的调色板。
   - 方案：解析期在 `Set Shell`/`Env` 提前执行（`evaluator.go:32-39` 特殊处理），其余 `Set` 在第一个非-Set 命令前批处理；执行期遇到 `Set` 打印 WARN 但 ignore。
   - Trade-off：让用户在错误位置用错 `Set` 时立刻得到清晰错误，**而不是渲染出来奇怪的 GIF**；代价是少数动态需求无法满足（注释明确说「future」可解）。
   - 可迁移性：高。

2. **渲染管线走「xterm.js canvas → go-rod screenshot → ffmpeg palette filter」三跳**
   - 问题：Go 库选项不多（img 库只能产静态 PNG，eogif 类工具画质差）。
   - 方案：`vhs.go:Start` 起 ttyd → go-rod 拉 Chrome → 每帧抓 `canvas.xterm-text-layer` + `canvas.xterm-cursor-layer` 两个 PNG → `video.go:buildFFopts` 调 ffmpeg `palettegen+paletteuse` 产 256 色调色板 GIF。
   - Trade-off：画质高（与手工录屏同档），且 cursor/text 双层 PNG 让光标动画与文本独立（背景不闪）；代价是必须本地装 ttyd + ffmpeg + Chrome + 图形栈，**Docker 是必备**。

3. **`vhs serve` 把虚拟终端暴露为 SSH 服务**
   - 问题：浏览器+ffmpeg 渲染管线重，想让远程/CI 用户复用渲染能力。
   - 方案：用 `charmbracelet/wish` 起 SSH server；客户端把 `.tape` 通过 stdin 传过来，服务端 `Evaluate()` 后把渲染出的 GIF 通过 stdout 返回。
   - Trade-off：零额外协议设计（复用 SSH 认证、加密、复用通道）；代价是 GIF 是二进制必须 stdout 一次写完，无法流式。

4. **错误处理带 token 行号**（`error.go:printError`）
   - 问题：用户改 `.tape` 改错了，CLI 报错要能精确到行。
   - 方案：画 Rust 风格的 `12 │ Type "foo"` + `^` 下划线指错位置；`evaluator.go:33-39` 把多个 parser 错误聚合成 `InvalidSyntaxError{errs}` 一次性输出。
   - Trade-off：让 `.tape` 的写作者体验接近现代编译器；代价是错误消息长度增加，但 CLI 场景下值得。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | vhs | asciinema (~24k★) | terminalizer (~14k★) | terminal-to-gif (<1k★) |
|------|-----|-------------------|---------------------|------------------------|
| 产物 | GIF/MP4/WebM + 文本快照 | 可播放 HTML/文本（.cast） | GIF/MP4 | GIF |
| 配置语言 | `.tape` DSL（声明式） | 无 DSL（手工录制） | `.yml` 配置 | 无（库形态） |
| 可 diff / 可 review | ✅ 一等公民 | ❌ JSONL 事件流 | ❌ yml 录制导向 | ❌ |
| CI 集成（`vhs-action`） | ✅ | 弱（需 asciicast2gif 二次转换） | ❌ | ❌ |
| 文本断言输出 | ✅ `.txt` / `.ascii` / `.test` | ✅ `.cast` 可解析 | ❌ | ❌ |
| 远端渲染 | ✅ `vhs serve` (SSH) | ❌ | ❌ | ❌ |
| 文件体积 | MB 级（GIF） | KB 级（cast） | MB 级 | MB 级 |
| 维护活跃度 | 2026 仍在更新 | 活跃 | 2020 后停滞 | 散点 |
| 浏览器/Chrome 依赖 | 强依赖（go-rod） | 无 | 弱依赖（可选浏览器录制） | 无 |
| 生态背书 | Charmbracelet 全家桶 | 独立 + 大社区 | 独立 | 个人 |

### 差异化护城河

**生态护城河 >> 技术护城河**：
- Charmbracelet 全家桶（bubbletea/gum/glow/catwalk/crush）的 demo 全部用 vhs 录制，形成天然的「我们内部产品都用自己」背书。
- vhs.charm.sh 是 SaaS 形态的分享层，远端渲染能力是技术护城河 + 商业化探索。
- `.tape` DSL 的设计、`SSH serve` 都是可被复制的——竞品真正难以追赶的是 **生态绑定 + 视觉品牌一致性**。

### 竞争风险

- **asciinema 若推出「产 GIF 模式 + 远端渲染」**会直接侵蚀 vhs 核心场景：asciinema 的 KB 级输出、可复制文本、播放器生态是其结构性优势。
- **LLM 时代录屏可被「代码截图 + 文本解释」替代**：当 AI 阅读代码就能理解功能时，GIF 的存在感可能被削弱。
- **强依赖 ttyd + go-rod + Chrome + ffmpeg**：Issue #232/#233/#45 揭示在容器/CI 中权限受限时 vhs 直接 panic 而非优雅降级——这是严肃 CI 集成的最大踩坑点。

### 生态定位

在整个 CLI/TUI 工具链上扮演「**视觉化层**」——介于 README 写作工具（ScreenToGif 类）和测试工具（snapshot 类）之间，独占「声明式视频」这一格。属于细分蓝海（DSL 化终端录制 + CI 集成这条赛道上几乎独占）。

## 套利机会分析

- **信息差**：20K stars 已经偏饱和，套利窗口已过。但「声明式录制 + 文本断言」这套范式仍未广泛传播——做对比教程（vhs vs asciinema vs terminalizer）仍能拿到关注。
- **技术借鉴**：三段式 DSL 骨架、`Wait/regex/` 同步原语、SSH-as-FaaS、浏览器 canvas + ffmpeg 录制管线——任意一项都可以单独提炼成博文或迁移到自家项目。
- **生态位**：vhs 填补「CLI 工具的演示材料应当可复现、可 review、可测试」这一空白，**这个空白仍未被任何中文社区项目填补**——做中文本地化增强（如中文字体支持、本地化主题集）有空间。
- **趋势判断**：vhs 进入低维护期，但 Charm 生态整体仍扩张（crush 25.3k★ 是新一代主力）。作为生态基础设施，vhs 不会被弃——但增长会放缓，转向「让现有 .tape 生态更稳定」。

## 风险与不足

- **强依赖链脆弱**：ttyd + go-rod + Chrome + ffmpeg 四件套，任意一个不匹配都导致 panic（Issue #232）。严肃 CI 必须用官方 Dockerfile。
- **维护节奏放缓**：近 30 天 0 commit、近 365 天仅 38 commit，已经进入稳定期。新需求（如运行时改主题）官方明确标注「future」。
- **`Sleep` 仍是某些场景的最终回退**：纯进度条动画等待不到，`Wait+Screen` 必须有可观测字符串（注释里写得很明确）。
- **`Set` 硬约束的反面**：少数动态需求（如「在命令执行过程中切主题」）目前不支持。
- **错误消息多语言缺失**：所有错误信息英文，国内用户首次接触 CLI 报错时认知成本稍高。
- **图像版本管理**：GIF 走 git LFS 还是普通文件？CHANGELOG.md 没有，发行说明散落在 GitHub Releases——这是周边工具链的不完整。

## 行动建议

- **如果你要用它**：作为 CLI/TUI 工具的 README Demo 录制器，无脑选 vhs——DSL 可 diff、CI 可集成（`vhs-action`）、主题库 300+。如果只是写教学文档或想要 KB 级文件，选 asciinema。
- **如果你要学它**：
  - **DSL 怎么写**：`lexer/lexer.go`（手写状态机）+ `token/token.go`（关键字表）+ `parser/parser.go`（Pratt top-down）三件套是教科书级别的小型 DSL 实现。
  - **声明式同步怎么写**：`command.go` 的 `ExecuteWait` 用 `term.buffer.active.getLine(...).translateToString()` 周期性 poll + 正则匹配。
  - **跨域知识迁移**：`wish`/`charmbracelet/ssh` 的 SSH-as-RPC、`xterm.js` + `go-rod` 的「用浏览器当 VCS-y emulator」、FFmpeg `palettegen+paletteuse` 的 GIF 高画质技巧。
- **如果你要 fork 它**：可以做：
  - **中文本地化增强**：内置中文字体（如「Noto Sans CJK SC」）、中文主题集、中文错误消息。
  - **跨平台精简依赖**：去掉 go-rod 强依赖，改用纯 Go 的 xterm 渲染（如 `creack/pty` + `manifoldco/promptui` 风格）。
  - **diff-aware CI**：让 PR review 时直接渲染「新增的 `.tape` 行对应的 GIF 帧」作为 review artifact。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录（403） |
| Zread.ai | https://zread.ai/charmbracelet/vhs（2025-04-18 索引，含架构总览 + Tape Format 子页） |
| 关联论文 | 无（非学术项目） |
| 在线 Demo | 无独立 playground；可通过 https://vhs.charm.sh 浏览/发布他人作品；本地 `vhs serve` 可起 SSH playground |
| 官方文档 | https://github.com/charmbracelet/vhs#readme（charm.land/vhs 是 301 重定向） |
| Charm 博客 | charm.land/blog 一篇「VHS GIF Hosting!」(Maas Lalani, 2022-12-19) |
