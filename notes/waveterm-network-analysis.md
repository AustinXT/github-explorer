# Wave Terminal 网络分析报告

> 仓库: [wavetermdev/waveterm](https://github.com/wavetermdev/waveterm)
> 分析时间: 2026-03-22

## 仓库基本数据

- **Star / Fork / Watcher**: 18,479 / 829 / 74
- **语言**: Go (48.5%), TypeScript (43.1%), CSS (5.6%), SCSS (1.7%), Shell (0.9%)
- **License**: Apache-2.0
- **创建时间**: 2022-06-08 | **最近推送**: 2026-03-21
- **话题标签**: command-line, developer-tools, linux, macos, terminal, windows, productivity, terminal-emulators
- **已归档**: 否 | **是Fork**: 否
- **主页**: https://www.waveterm.dev
- **磁盘用量**: ~54 MB
- **总 Issue**: 318 | **总 PR**: 46
- **最新版本**: v0.14.3 (2026-03-12)

## 作者画像

### 组织: wavetermdev

- **名称**: Wave Terminal
- **简介**: An open-source, cross-platform terminal for seamless workflows
- **官网**: https://waveterm.dev
- **位置**: United States of America
- **公开仓库**: 15 | **关注者**: 294
- **创建时间**: 2022-12-10

### 核心贡献者

| 贡献者 | 提交数 | 身份 |
|--------|--------|------|
| **sawka** (Mike Sawka) | 888 | 创始人, Command Line Inc, 旧金山, 2012年注册 GitHub, 123 followers |
| **esimkowitz** (Evan Simkowitz) | 743 | 前 Wave 高级控制系统工程师 (ex-@wavetermdev, ex-Microsoft), 137 followers |
| dependabot[bot] | 344 | 自动依赖更新 |
| wave-builder[bot] | 221 | 构建机器人 |
| **oneirocosm** | 205 | 核心开发者 |
| adred | 63 | 贡献者 |
| Copilot | 55 | AI 辅助 |

**分析**: 项目高度集中在 2-3 位核心开发者。sawka（Mike Sawka）是创始人，拥有 Command Line Inc 公司背景。第二贡献者 esimkowitz 个人简介标注为 "ex-@wavetermdev"，说明已经离开团队。社区贡献者相对较少（仅约 20 位外部贡献者，多为 1 次提交）。

### 组织其他项目

- **waveterm** (18,479 stars) - 主项目
- **xterm.js** (fork) - 终端前端组件 fork
- **waveapps** (8 stars) - Wave 应用扩展
- **waveterm-docs** (8 stars) - 文档站
- **chocolatey** (3 stars) - Windows 包管理分发

## 社区热度

### Star 增长趋势

API 首页数据显示早期 star（2023年11月）出现明显爆发，2023-11-23 单日获得大量 star，表明该日期有重大宣传事件（可能为 Product Hunt 发布或 HN 帖子）。

### 近期开发活跃度（最近12周 commit 数）

| 周起始日 | Commits |
|----------|---------|
| 2025-12-28 | 9 |
| 2026-01-04 | 6 |
| 2026-01-11 | 0 |
| 2026-01-18 | 10 |
| 2026-01-25 | 11 |
| 2026-02-01 | 10 |
| 2026-02-08 | 21 |
| 2026-02-15 | 23 |
| 2026-02-22 | 36 |
| 2026-03-01 | 35 |
| 2026-03-08 | 40 |
| 2026-03-15 | 18 |

**趋势**: 开发活跃度呈明显上升趋势。从 2025 年底的每周 6-11 次提交，到 2026 年 3 月已增长至每周 35-40 次提交，表明项目正在加速开发。

### 发布节奏

- v0.14.3 (2026-03-12)
- v0.14.2 (2026-03-12)
- v0.14.2-beta.2 (2026-03-12)
- v0.14.2-beta.1 (2026-03-10)
- v0.14.2-beta.0 (2026-03-06)

发布频率高，有 beta 预发布流程，表明项目工程化程度较好。

## 生态网络

### 项目定位

Wave Terminal 定位为 **AI 原生、跨平台的现代终端模拟器**，融合了终端、文件编辑器、Web 浏览器和 AI 助手的功能，类似终端中的 IDE 体验。

### 技术生态

- **前端**: Electron + React + TypeScript, 使用 Jotai 状态管理
- **后端**: Go 语言实现, SQLite 持久化存储
- **AI 集成**: 支持 OpenAI、Claude、Gemini、Azure、Perplexity、Ollama、LM Studio
- **终端核心**: fork 了 xterm.js 作为终端渲染组件
- **远程连接**: 自研 SSH 持久化会话, wsh 命令系统

### 关联项目

Wave 生态中的关键依赖/关联:
- xterm.js (fork) - 终端渲染引擎
- waveapps - 扩展应用框架
- wsh - CLI 工具, 用于终端与 Wave 工作区交互

## 官方文档洞察

### 官网 (waveterm.dev)

- **价值主张**: "Upgrade Your Command Line" — 升级你的命令行体验
- **核心卖点**: 将图形化工具直接集成到终端环境中，消除开发者在终端和浏览器间的频繁切换

### 文档站 (docs.waveterm.dev)

文档结构完善，覆盖:
- Wave AI 上下文感知助手（含 Claude Code 集成）
- 工作区管理、可持久化会话
- 远程 SSH 连接管理
- 自定义 Widget 开发
- wsh CLI 系统
- 配置与密钥管理

### 外部评价

- SourceForge 和 Slashdot 均有 Wave Terminal 评价页面
- 被 ItsFoss 收录为 "7 个来自未来的 Linux 终端" 之一
- Apidog 有完整使用教程
- DEV Community 有用户自发推荐文章
- 修复了一个影响 Claude Code 用户的长期 Bug（终端窗口意外跳转）

## 竞品清单

### 直接竞品（现代终端模拟器）

| 项目 | Stars | 语言 | 特点 |
|------|-------|------|------|
| [alacritty/alacritty](https://github.com/alacritty/alacritty) | 63,068 | Rust | GPU 加速, 极简高性能 |
| [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | 48,009 | Zig | GPU 加速, 原生 UI, 2024 年新星 |
| [vercel/hyper](https://github.com/vercel/hyper) | 44,707 | TypeScript | Electron 架构, 插件生态 |
| [kovidgoyal/kitty](https://github.com/kovidgoyal/kitty) | 31,979 | - | GPU 加速, 功能丰富 |
| [wezterm/wezterm](https://github.com/wezterm/wezterm) | 25,072 | Rust | GPU 加速, Lua 脚本配置 |
| [raphamorim/rio](https://github.com/raphamorim/rio) | 6,558 | Rust | 硬件加速, 轻量 |

### 同类定位竞品（AI + 终端）

| 项目 | 说明 |
|------|------|
| **Warp** (闭源) | AI 原生终端, Rust 编写, 商业化产品, 最直接的竞品 |
| **Tabby** | GPU 加速终端, 插件化, TypeScript |

### 竞争格局分析

- Wave (18.5K stars) 在 star 数上低于 Alacritty (63K)、Ghostty (48K)、Hyper (44.7K) 等头部选手
- 但 Wave 的差异化在于 **AI 原生 + 图形化工作区 + 持久化 SSH 会话** 的组合
- 最直接的竞争对手是 **Warp**（闭源商业产品），Wave 作为开源替代具有优势
- 传统 GPU 终端（Alacritty、Kitty）侧重性能和极简，与 Wave 的 "终端IDE" 定位形成差异化

## 关键 Issue 信号

### 最热门 Open Issues

| # | 标题 | 评论数 | 标签 |
|---|------|--------|------|
| [#1605](https://github.com/wavetermdev/waveterm/issues/1605) | [Bug]: remote connections not available in dropdown | 30 | bug |
| [#987](https://github.com/wavetermdev/waveterm/issues/987) | [Bug]: timeout waiting for connserver to register | 19 | bug |
| [#1982](https://github.com/wavetermdev/waveterm/issues/1982) | Link to local Ollama | 17 | - |
| [#1629](https://github.com/wavetermdev/waveterm/issues/1629) | [Bug]: No blocks and no wsh installed | 16 | bug, triage |

### 活跃 PR

| # | 标题 | 评论数 |
|---|------|--------|
| [#2940](https://github.com/wavetermdev/waveterm/pull/2940) | feat(term): add sixel rendering | 4 |
| [#2835](https://github.com/wavetermdev/waveterm/pull/2835) | Tab background glow on process exit/bell | 4 |
| [#2789](https://github.com/wavetermdev/waveterm/pull/2789) | feat: Tab base directory with VS Code style redesign | 4 |

### Issue 信号解读

- **远程连接稳定性**是最大痛点（#1605, #987 均为连接相关 Bug，评论最多）
- **Ollama 本地模型集成**需求强烈（#1982, 17 评论），社区对 AI 功能有明确期待
- 项目正在推进 **sixel 渲染**（图形协议支持）和 **VS Code 风格重设计**，发展方向明确
- Bug 类 Issue 占主导，说明项目处于快速迭代期，功能丰富但稳定性仍需打磨

## 知识入口

### 官方资源

- **官网**: https://www.waveterm.dev
- **文档**: https://docs.waveterm.dev
- **下载**: https://www.waveterm.dev/download
- **Discord**: https://discord.gg/XfvZ334gwU
- **X/Twitter**: https://x.com/wavetermdev

### 第三方知识源

- **DeepWiki**: https://deepwiki.com/wavetermdev/waveterm — 有详细的架构分析（Electron+Go 双进程架构、WaveObj 状态模型、RPC 通信机制）
- **arxiv.org**: 未发现相关学术论文
- **ItsFoss**: [7 Linux Terminals From the Future](https://itsfoss.com/modern-linux-terminals/) — 将 Wave 列为未来型终端之一
- **Apidog**: [How to Use Wave](https://apidog.com/blog/wave-open-source-terminal-wave/) — 详细使用教程
- **DEV Community**: [Using WAVE as new terminal](https://dev.to/diegoleteliers10/using-wave-as-new-terminal-3eee) — 用户体验分享
- **Hashnode**: [Introducing Wave Terminal](https://waveterm.hashnode.dev/introducing-wave-terminal) — 官方介绍博文

## 项目展示素材

### 展示图片

| 说明 | URL |
|------|-----|
| Logo (深色) | https://raw.githubusercontent.com/wavetermdev/waveterm/main/assets/wave-dark.png |
| Logo (浅色) | https://raw.githubusercontent.com/wavetermdev/waveterm/main/assets/wave-light.png |
| 主截图 | https://raw.githubusercontent.com/wavetermdev/waveterm/main/assets/wave-screenshot.webp |

### 一句话描述

> An open-source, AI-integrated, cross-platform terminal for seamless workflows

## 快速判断

- **是否值得深入**: 是。项目处于快速上升期（提交频率近3个月翻倍），AI 终端赛道明确，开源 Apache-2.0 许可证友好，18.5K star 证明市场认可。
- **初步定位**: AI 原生的现代终端模拟器，融合 IDE 理念（内嵌编辑器、文件预览、AI 助手、Web 浏览），定位于 "终端工作台" 而非单纯的终端模拟器。与 Warp 形成开源 vs 闭源的直接竞争关系。
- **作者可信度**: 高。创始人 Mike Sawka 为硅谷连续创业者（Command Line Inc），团队虽小但工程化水平高（完善的 CI/CD、beta 发布流程、多平台支持）。需关注第二核心开发者 esimkowitz 已离职的影响。
- **竞品格局**: 现代终端赛道竞争激烈。性能派（Alacritty/Ghostty/Kitty）专注速度，Wave 走差异化路线（AI + 图形化 + 持久 SSH）。最大威胁是闭源的 Warp（资金充足、用户量大），Wave 的优势在于开源和可自托管 AI 模型。Star 数中等偏上（18.5K），但增长势头良好。
