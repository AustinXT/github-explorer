## 仓库基本数据

| 指标 | 值 |
|------|-----|
| 仓库名 | openai/codex |
| 描述 | Lightweight coding agent that runs in your terminal |
| URL | https://github.com/openai/codex |
| Stars | 73,298 |
| Forks | 10,301 |
| Watchers | 419 |
| Issues（总计） | ~16,867（含 PR） |
| Pull Requests | 208 |
| 主语言 | Rust（20.6 MB），次语言 Python（638 KB）、TypeScript（307 KB）、JavaScript（61 KB）、Shell（21 KB） |
| 许可证 | Apache-2.0 |
| 创建时间 | 2025-04-13（首次提交 2025-04-16） |
| 最近推送 | 2026-04-05 |
| 磁盘大小 | 380 MB |
| 是否 Fork | 否 |
| 是否归档 | 否 |
| 默认分支 | main |
| 发布版本数 | 674 个（含大量 alpha 预发布） |
| npm 发布版本 | 1,683 个（@openai/codex） |
| 当前稳定版 | 0.118.0（npm latest），alpha 已至 0.119.0-alpha.11 |
| 安装方式 | `npm i -g @openai/codex` 或 `brew install --cask codex` |

**关键观察**：仓库创建不到一年即达 7.3 万 Stars，增速极为凶猛。674 个 Release 意味着约每天 2 个版本（含 alpha），开发节奏极快。

## 作者画像

### 组织：OpenAI

| 指标 | 值 |
|------|-----|
| 名称 | OpenAI |
| 官网 | https://openai.com/ |
| GitHub 粉丝 | 117,388 |
| 公开仓库 | 238 |
| 创建时间 | 2015-10-03 |

OpenAI 是全球领先的 AI 研究公司，GPT 系列和 ChatGPT 的缔造者。Codex CLI 是其开发者工具战略的重要一环——将 AI 编程能力从云端延伸到终端。

### 核心贡献者（Top 10）

| 排名 | 用户名 | 提交数 | 角色推断 |
|------|--------|--------|----------|
| 1 | bolinfest (Michael Bolin) | 782 | 项目负责人/架构师，前 Meta 工程师，705 followers |
| 2 | jif-oai | 683 | 核心开发者 |
| 3 | aibrahim-oai (Ahmed Ibrahim) | 465 | 核心开发者，负责实时音频/多 Agent/Node 发布 |
| 4 | pakrym-oai | 356 | 核心开发者 |
| 5 | etraut-openai (Eric Traut) | 216 | 核心开发者，TUI/Auth/测试修复 |
| 6 | nornagon-openai | 199 | 核心开发者 |
| 7 | dylan-hurd-oai | 181 | 核心开发者 |
| 8 | dependabot[bot] | 126 | 自动依赖更新 |
| 9 | owenlin0 | 111 | 核心开发者 |
| 10 | charley-oai | 103 | 核心开发者 |

**特征**：几乎所有活跃贡献者用户名都带 `-oai` 或 `-openai` 后缀，说明是 OpenAI 全职员工团队。团队规模至少 25+ 工程师，这对于一个 CLI 工具来说是非常庞大的投入。npm maintainers 列出 12 人。

## 社区热度

### Star 增长

- 仓库创建于 2025-04-13，不到一年达到 73,298 Stars
- 日均增 Star 约 200+，增长曲线非常陡峭
- Fork 数 10,301，Fork/Star 比约 14%，显示大量开发者不仅关注还实际下载使用

### Issue 活跃度

- 总 Issue 编号已达 #16,867，开放的 Issue 数量极大
- 仅 2026-04-05 一天就有 30+ 个新 Issue 被提交
- Issue 涵盖 bug、enhancement、多个平台标签（CLI/app/extension/TUI/windows/iOS/jetbrains）
- 说明用户基数大且使用深度高，但也暴露了产品稳定性仍在快速迭代中

### PR 活跃度

- 208 个 PR，全部由 OpenAI 内部员工提交
- **外部贡献仅限邀请制**——社区只能通过 Issue 反馈，不接受主动 PR
- 这是一个高度封闭的开发模式，开源但不开放协作

### 社区健康度评分

GitHub 社区评分 75/100。缺少 Code of Conduct 和 Issue Template。

## 生态网络

### 产品矩阵

Codex 不是一个单独的 CLI，而是 OpenAI 编程 Agent 生态的核心：

1. **Codex CLI** — 终端编码 Agent（本仓库核心，Rust 实现）
2. **Codex Desktop App** — 桌面应用（`codex app` 命令启动）
3. **Codex VS Code Extension** — IDE 集成
4. **Codex JetBrains Plugin** — JetBrains IDE 集成
5. **Codex Web** — 云端 Agent（chatgpt.com/codex）
6. **Codex iOS App** — 移动端（从 Issue 标签可见）
7. **Codex SDK** — TypeScript + Python SDK，支持嵌入式调用

### 技术栈

- **核心引擎**：Rust（codex-rs），monorepo 包含 60+ crate
- **Node 包装层**：codex-cli（npm 分发）
- **构建系统**：Bazel + Cargo 双轨并行，Nix flake 支持
- **沙箱**：macOS Seatbelt、Linux bubblewrap、Windows 沙箱
- **协议**：MCP（Model Context Protocol）集成
- **模型**：GPT-5 及 OpenAI 系列模型

### 开源基金

OpenAI 为 Codex 生态设立了 **100 万美元开源基金**，向使用 Codex CLI 的开源项目发放最高 25,000 美元 API 额度资助。这是一个明确的生态扩张策略。

### SDK 生态

- **TypeScript SDK**（@openai/codex-sdk）：通过 JSONL over stdin/stdout 与 CLI 交互
- **Python SDK**（实验性）：基于 app-server JSON-RPC v2 over stdio

## 官方文档洞察

### README 特点

- 极其精简，核心信息就是安装和启动
- 支持 npm、Homebrew、GitHub Release 二进制下载三种安装方式
- 强调与 ChatGPT 订阅计划集成（Plus/Pro/Team/Edu/Enterprise）
- 文档外链到 developers.openai.com/codex

### 文档体系

docs/ 目录下有 24 个文档，覆盖：
- 认证（authentication.md）
- 配置（config.md、example-config.md）
- 沙箱安全（sandbox.md、execpolicy.md）
- 技能系统（skills.md）
- TUI 设计（6 篇 TUI 相关文档）
- 贡献指南（contributing.md、CLA.md）
- 开源基金（open-source-fund.md）

### AGENTS.md

项目自带 AGENTS.md（OpenAI 版本的 CLAUDE.md），包含详细的 Rust 代码规范、模块大小限制（500 LoC 目标，800 LoC 上限）、测试流程等。这说明 Codex 团队自己也在大量使用 Codex 进行开发（dogfooding）。

## 竞品清单

| 产品 | 公司 | Stars | 特点 | 与 Codex 的关系 |
|------|------|-------|------|----------------|
| **Claude Code** | Anthropic | 109,338 | 终端 AI 编码 Agent，Claude 模型 | **直接竞品**，Stars 更多（109K vs 73K），市场先发优势 |
| **Aider** | 独立开源 | 42,859 | 支持多模型的终端 AI 编码助手 | 间接竞品，多模型策略，社区驱动 |
| **GitHub Copilot CLI** | GitHub/Microsoft | 9,814 | Copilot 终端版 | 间接竞品，微软生态 |
| **Plandex** | 独立开源 | 15,205 | 大型项目 AI 编码 Agent | 间接竞品，专注大型项目 |
| **Cursor** | Anysphere | N/A（非开源核心） | AI 代码编辑器 | IDE 层面竞品 |
| **Windsurf** | Codeium | N/A | AI 代码编辑器 | IDE 层面竞品 |

**竞争格局判断**：Codex CLI 是 OpenAI 对 Anthropic Claude Code 的直接回应。Claude Code 于 2025-02-22 开源（早 Codex 两个月），目前 Stars 领先约 36K。但 Codex 背靠 OpenAI 的 ChatGPT 订阅用户池和 100 万美元开源基金，生态扩张能力极强。

## 关键 Issue 信号

### 严重 Bug 信号

1. **#16866** macOS 内核崩溃（kernel panic）— v0.118.0 在 Apple Silicon 上导致 os_refcnt 溢出，1 天内 2 次崩溃
2. **#16862** CLI 关闭终端后留下僵尸进程，CPU 占用 80-100%
3. **#16828** Linux 长时间运行内存泄漏，可导致主机冻结
4. **#16857** 桌面应用「思考中」动画导致 GPU 高占用

### 平台兼容性

- Windows 支持问题密集：PowerShell 7 选择、MCP 启动崩溃、VSCodium 远程连接等
- CJK 文本渲染损坏（#16840）、CJK 输入法导航（#16829）— 东亚用户体验待优化

### 功能方向信号

- **WebRTC 实时音频**（#16805-#16807）：正在从 WebSocket 迁移到 WebRTC，支持实时语音交互
- **多 Agent**：MultiAgentV2 子 Agent 生成（#16746）
- **exec-server**：沙箱执行服务器 MVP（#16814）
- **MCP 集成**：深度支持 Model Context Protocol

### 关键判断

Issue 数量巨大但 Bug 密度也高，说明产品处于快速迭代期，稳定性尚未收敛。团队响应速度快（大部分 Issue 有回复），但外部贡献渠道封闭。

## 知识入口

### 官方渠道

- **开发者文档**：https://developers.openai.com/codex
- **GitHub 仓库**：https://github.com/openai/codex
- **ChatGPT Codex Web**：https://chatgpt.com/codex
- **IDE 集成**：https://developers.openai.com/codex/ide
- **安全漏洞报告**：https://bugcrowd.com/engagements/openai

### 学习路径

1. 安装：`npm i -g @openai/codex` 或 `brew install --cask codex`
2. 入门：docs/getting-started.md
3. 配置：docs/config.md + docs/example-config.md
4. 安全模型：docs/sandbox.md + docs/execpolicy.md
5. 技能系统：docs/skills.md
6. SDK 开发：sdk/typescript/ 和 sdk/python/

### 代码入口

- Rust 核心：`codex-rs/core/`（codex-core crate）
- TUI 界面：`codex-rs/tui/`
- CLI 入口：`codex-rs/cli/`
- Node 包装：`codex-cli/`
- 沙箱实现：`codex-rs/linux-sandbox/`、`codex-rs/sandboxing/`

## 项目展示素材

### 一句话定位

「OpenAI 官方出品的终端 AI 编码 Agent，Rust 实现，Claude Code 的直接竞品」

### 关键数据点

- 7.3 万 Stars，创建不到一年
- 674 个 Release，1,683 个 npm 版本——日均 2+ 版本的极速迭代
- 25+ 人 OpenAI 全职工程师团队
- 100 万美元开源基金
- Rust 核心引擎 + 60+ crate 的 monorepo
- 覆盖 CLI/Desktop/IDE/Web/iOS/SDK 的全平台矩阵

### 视觉素材

- 官方 splash 图：https://github.com/openai/codex/blob/main/.github/codex-cli-splash.png
- TUI 界面风格文档：codex-rs/tui/styles.md

## 快速判断

### 值得深入分析吗？

**强烈推荐**。理由：

1. **战略意义极高**：这是 OpenAI 与 Anthropic（Claude Code）在终端 AI 编码 Agent 领域的正面交锋，代表了 AI 编程工具的最前沿
2. **技术含量高**：Rust 实现的 monorepo，涵盖沙箱安全、MCP 协议、多 Agent 编排、实时音频等先进技术
3. **公众号选题价值**：OpenAI vs Anthropic 的竞品对比角度天然吸引关注
4. **生态布局完整**：CLI + Desktop + IDE + Web + SDK + 开源基金，这不是一个简单的 CLI 工具，而是 OpenAI 开发者平台战略的核心载体

### 风险提示

- 开发模式高度封闭（不接受外部 PR），开源社区参与感低
- Bug 密度高，产品成熟度尚在早期
- 强绑定 OpenAI 模型和 ChatGPT 订阅，用户迁移成本高
- 版本号还在 0.x，尚未达到 1.0 稳定版

### 与 Claude Code 的核心差异

| 维度 | Codex CLI | Claude Code |
|------|-----------|-------------|
| 实现语言 | Rust | TypeScript |
| Stars | 73K | 109K |
| 开源时间 | 2025-04 | 2025-02 |
| 绑定模型 | GPT-5 / OpenAI | Claude |
| 贡献模式 | 邀请制，仅内部 | 开放社区贡献 |
| 产品矩阵 | CLI+App+IDE+Web+iOS+SDK | CLI+IDE |
| 特色功能 | 实时语音、多 Agent、开源基金 | Agent SDK、MCP 原生 |
| 沙箱实现 | 自建（Seatbelt/bubblewrap/Windows） | 自建 |
