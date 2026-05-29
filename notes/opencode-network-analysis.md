# anomalyco/opencode 网络分析报告

> 更新时间：2026-03-22

## 仓库基本数据

| 指标 | 数据 |
|------|------|
| Star / Fork / Watcher | 127,390 / 13,463 / 493 |
| 主语言 | TypeScript（最初用 Go 编写，后重写为 TypeScript） |
| 其他语言 | MDX（7MB）、CSS（540KB）、Rust（86KB，Tauri桌面端）、Astro、JavaScript、Shell、Nix、Dockerfile |
| License | MIT |
| 创建时间 | 2025-04-30 |
| 最近推送 | 2026-03-22（当日活跃开发中） |
| 默认分支 | dev |
| 归档状态 | 否 |
| 官网 | https://opencode.ai |
| 磁盘占用 | ~218 MB |
| Issues 总数 | 5,535 |
| PR 总数 | 1,746 |
| 最新版本 | v1.2.27（2026-03-16），近一周内发布 3 个版本 |
| npm 月下载量 | 178 万（opencode-ai） |

## 作者画像

### 组织信息

| 属性 | 详情 |
|------|------|
| 所属组织 | anomalyco / Anomaly（前身为 sst） |
| 组织简介 | "For whatever you build." |
| 组织官网 | https://anoma.ly |
| 公开仓库 | 64 个（anomalyco）|
| 粉丝 | 3,587 |
| 创建时间 | 2020-06-07 |

### 核心团队

- **Jay V**（CEO）与 **Frank Wang**（CTO）：滑铁卢大学工程系同窗，共同创办 Anomaly 和 Serverless Stack (SST)，**YC 2021 校友**
- **Dax Raad (thdxr)**：核心贡献者 #1（1,934 commits），SST 与 OpenCode 的技术灵魂人物，纽约，3,967 粉丝，同时运营 withbumi
- **Adam (adamdotdevin)**：核心贡献者 #2（1,824 commits），公司 @anomalyco，1,616 粉丝
- **rekram1-node**：核心贡献者 #3（1,053 commits）
- **jayair**（Jay V 本人）：353 commits
- **fwang**（Frank Wang 本人）：191 commits

### 贡献集中度

| 指标 | 数据 |
|------|------|
| Top 3 贡献者占比 | ~60%（4,811 / ~8,000 总 commits） |
| 贡献者总数 | 800+（官网宣称）|
| Bot 贡献 | actions-user 981 commits, opencode-agent[bot] 269 commits |
| 投入权重 | 极高，团队全职投入，融资支持 |

### 作者类型判断

**商业公司驱动的开源项目**。团队背景：YC 校友，有 SST（全栈框架，广受好评）的成功前史，从 Serverless 基础设施转向 AI 编码代理赛道。公司已完成融资（金额未披露），通过 OpenCode Zen（托管优化模型）产生商业收入。

## 社区热度

### 热度级别：**S 级（超级热门）**

| 维度 | 评估 |
|------|------|
| Star 数 | 127,390 —— 全球 AI 编码代理领域 Star 数最高的开源项目 |
| 月活用户 | 500 万+（官网数据）/ 65 万+（TFN 报道数据） |
| 增长速度 | 2025-12 至 2026-01 期间两周内增长 18,000 stars；一个月内从 39.8K 涨至 71.9K |
| 发布频率 | 极高，2026 年 3 月前半月即发布 5 个版本 |

### 增长模式

**爆发式增长 + 持续攀升**。关键增长节点：

1. **2025-12 下旬**：v1.0 重写发布，支持 Claude Max 订阅路由，引发爆发式关注
2. **2026-01-09**：Anthropic 封锁第三方工具伪装 Claude Code 访问消费者订阅认证，引发争议性讨论，反而推高知名度
3. **2026-01 至今**：稳定高速增长，从 ~50K 增至 127K+

### 套利判断

**无明显刷 Star 迹象**。增长与产品发布节点、媒体报道、社区争议事件强相关，属于真实有机增长。项目有实际的月活用户数、下载量和商业收入支撑。

## 生态网络

### 上游依赖 / 技术栈

| 类别 | 技术 |
|------|------|
| 运行时 | Bun |
| 前端框架 | Solid.js（响应式 UI） |
| 桌面端 | Tauri（Rust） |
| 数据库 | SQLite + Drizzle ORM |
| 服务端 | Hono 框架（HTTP/SSE 服务器） |
| 文档 | Astro |
| AI 集成 | 75+ LLM 供应商 |
| LSP | 20+ 语言支持 |

### 衍生生态项目

| 项目 | Star | 说明 |
|------|------|------|
| NoeFabris/opencode-antigravity-auth | 9,719 | Google Antigravity OAuth 认证插件 |
| alvinunreal/oh-my-opencode-slim | 2,252 | 精简优化分支，减少 token 消耗 |
| numman-ali/opencode-openai-codex-auth | 1,825 | OpenAI ChatGPT Plus/Pro OAuth 认证插件 |
| Opencode-DCP/opencode-dynamic-context-pruning | 1,491 | 动态上下文裁剪插件，优化 token 使用 |

### 活跃 Fork

| Fork | Star | 说明 |
|------|------|------|
| winmin/evil-opencode | 202 | 安全研究方向 |
| DNGriffin/whispercode | 136 | 语音驱动变体 |
| Latitudes-Dev/shuvcode | 94 | 定制化变体 |

### 同类项目 / 生态位

| 项目 | Star | 定位 |
|------|------|------|
| Anthropic Claude Code | - | 商业闭源，付费 CLI 编码代理（Opus 4.6, SWE-bench 80.8%） |
| paul-gauthier/aider | 39K+ | 开源 Git-native 编码助手 |
| cline/cline | - | VS Code 扩展，500万+ 安装 |
| OpenAI Codex CLI | - | OpenAI 官方 CLI 编码代理 |
| Google Gemini CLI | - | Google 官方 CLI 编码代理 |
| jameswilson/plandex | - | 2M 上下文窗口的终端编码代理 |

## 官方文档洞察

### 价值主张
"The open source coding agent." —— 开源 AI 编码代理，零摩擦使用（无需注册、无需信用卡）。

### 目标用户
- 偏好终端工作流的开发者
- 注重隐私的企业团队（不存储任何代码或上下文数据）
- 需要模型灵活性的开发者（支持 75+ 供应商，包括本地模型）
- 跨平台用户（终端、桌面、VS Code、Web）

### 差异化叙事
1. **开源 vs 闭源**：对标 Claude Code / Cursor 等商业工具，强调开源透明
2. **供应商中立**：不绑定任何单一 AI 供应商，支持 Claude、GPT、Gemini、本地模型等
3. **隐私优先**："不存储任何代码或上下文数据"，适合隐私敏感环境
4. **零摩擦哲学**：唯一主流编码代理无需注册即可使用

### 设计哲学
- 客户端-服务器架构：支持远程驱动（手机端控制电脑上的 Agent）
- 三种代理模式：build（完全权限开发）、plan（只读分析）、general（委托复杂任务）
- 插件系统 + MCP 支持，高度可扩展

### 技术路线图
- **OpenCode Zen**：经过测试和基准测试的优化编码代理模型集合（商业化方向）
- 持续扩展多客户端（终端、桌面、VS Code、Web）
- 增强 LSP 集成和代码格式化能力

### 外部深度视角

- **Daniel Miessler 测评**：OpenCode 在复杂工作流中表现与 Claude Code 相当，后者的"秘密武器"（上下文管理、内存优化、跨文件追踪）是可复制的工程技术而非不可企及的专有技术。OC 当前劣势主要在实用性层面（无法复制粘贴对话、无法排队请求），非核心智能差异。
- **DataCamp 对比**：Claude Code 在代码理解深度和 SWE-bench 评分上领先；OpenCode 在模型灵活性和免费使用上占优。
- **Morph LLM 评测**：15 个 AI 编码代理中，仅 3 个改变了团队交付方式，OpenCode 位列其中。
- **NxCode 排名**：2026 年 AI 编码工具前 10 排名中，OpenCode 是开源阵营的头部项目。

## 竞品清单

| # | 竞品 | 类型 | 核心差异 |
|---|------|------|----------|
| 1 | **Claude Code** | 商业闭源 CLI | 最强代码理解（Opus 4.6, SWE-bench 80.8%），1M 上下文，$20-100/月 |
| 2 | **Aider** | 开源 CLI | Git-native 工作流，自动 commit，39K+ stars |
| 3 | **Cline** | 开源 VS Code 扩展 | 500万+ 安装，跨 IDE 支持 |
| 4 | **Gemini CLI** | Google 官方免费 CLI | 免费层最佳（60 req/min Gemini 2.5 Pro），Plan Mode |
| 5 | **OpenAI Codex CLI** | OpenAI 官方 CLI | OpenAI 生态集成，Codex 模型优化 |

## 关键 Issue 信号

| # | Issue | 评论数 | 状态 | 信号解读 |
|---|-------|--------|------|----------|
| 1 | [#7410 Broken Claude Max](https://github.com/anomalyco/opencode/issues/7410) | 392 | Open | Claude Max 订阅集成是最热门话题，反映用户对低成本使用顶级模型的强需求 |
| 2 | [#8030 Copilot auth premium requests](https://github.com/anomalyco/opencode/issues/8030) | 202 | Open | GitHub Copilot 认证过快消耗高级请求，供应商集成的持续挑战 |
| 3 | [#631 Windows Support](https://github.com/anomalyco/opencode/issues/631) | 202 | Open | Windows 支持长期诉求，跨平台覆盖仍有短板 |
| 4 | [#18267 Claude code OAuth broked](https://github.com/anomalyco/opencode/issues/18267) | 130 | Open | Claude OAuth 认证问题，与 Anthropic 政策博弈持续 |
| 5 | [#1686 Add OpenAI auth login](https://github.com/anomalyco/opencode/issues/1686) | 126 | Closed | 已实现 OpenAI 认证，供应商集成是核心优先事项 |
| 6 | [#1505 shift+enter keybinding](https://github.com/anomalyco/opencode/issues/1505) | 117 | Closed | TUI 键绑定问题，反映终端 UI 的交互细节挑战 |
| 7 | [#811 Text rendering very slow](https://github.com/anomalyco/opencode/issues/811) | 84 | Closed | 性能问题已修复，TUI 渲染性能是早期痛点 |
| 8 | [#4283 Copy To Clipboard not working](https://github.com/anomalyco/opencode/issues/4283) | 76 | Open | 基础交互功能缺陷，终端环境的固有局限 |

**Issue 信号总结**：高评论 Issue 集中在两个方向：(1) 第三方供应商认证集成（Claude Max、Copilot、OpenAI OAuth）—— 反映"供应商中立"定位的实际摩擦；(2) 终端 UI 基础体验问题（键绑定、渲染、剪贴板）—— TUI 方案固有的交互挑战。

## 知识入口

| 类型 | 链接 | 可用性 |
|------|------|--------|
| DeepWiki | https://deepwiki.com/anomalyco/opencode | 可用（HTTP 200），包含架构、功能、设计决策的详细解读 |
| Zread.ai | https://zread.ai/anomalyco/opencode | 待验证 |
| 关联论文 | 无直接关联论文。arxiv 上有同名但不同项目（OpenCoder、OpenCodeInterpreter、OpenCodeReasoning） | 间接相关 |
| 在线 Demo | 无独立 Demo；可通过 `curl -fsSL https://opencode.ai/install \| bash` 一键安装体验 | 安装即用 |
| 官方文档 | https://opencode.ai/docs/ | 可用 |
| 中文教程 | https://blog.mkacg.com/2026/01/28/opencode-tutorial/ | 可用 |

## 项目展示素材

### README 媒体

| 文件 | URL | 说明 |
|------|-----|------|
| screenshot.png | `https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/web/src/assets/lander/screenshot.png` | 产品截图，展示终端 UI 界面 |
| logo-ornate-dark.svg | `https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/console/app/src/asset/logo-ornate-dark.svg` | 深色主题 Logo |
| logo-ornate-light.svg | `https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/console/app/src/asset/logo-ornate-light.svg` | 浅色主题 Logo |

### 筛选说明

README 中的图片以 Logo 和产品截图为主，已排除 badge/shield 类图片。图片 URL 基于 `DEFAULT_BRANCH=dev` 构建。官网 opencode.ai 可能包含更多展示素材（如视频），但 README 本身偏简洁。

## 快速判断

### 是否值得深入
**强烈推荐深入分析。** 这是 2025-2026 年 AI 编码代理赛道最重要的开源项目之一，127,390 Star 使其成为全球 Star 数最高的 AI 编码代理。npm 月下载量 178 万，活跃度极高。

### 初步定位
**开源终端 AI 编码代理的事实标准**。对标 Claude Code、Cursor 等商业产品，以"开源 + 供应商中立 + 隐私优先"三角定位抢占市场。从 SST（Serverless 全栈框架）团队孵化，延续其"开发者工具"基因。

### 作者可信度
**高度可信**。YC 2021 校友，有 SST 的成功开源项目背景（SST 本身是知名的 AWS 全栈框架），核心团队稳定且全职投入，已完成融资，有商业收入（OpenCode Zen），800+ 贡献者的社区规模验证了项目的社区吸引力。

### 竞品格局
**AI 编码代理赛道进入"军备竞赛"阶段**：
- **商业闭源**：Claude Code（Anthropic）、Codex CLI（OpenAI）、Gemini CLI（Google）—— 各大模型厂商均推出自有 CLI 工具
- **开源阵营**：OpenCode 处于绝对领先位置（127K stars），Aider 是老牌竞品但 Star 差距 3 倍+，Cline 在 IDE 插件赛道领先
- **关键博弈**：OpenCode 与商业工具的竞争焦点在供应商认证（Claude Max/Copilot OAuth），Anthropic 等厂商正在收紧第三方接入，这是 OpenCode 模式的最大风险点
- **衍生生态**：已形成丰富的插件生态（认证插件、上下文优化插件等），最热门衍生项目近万 Star，说明社区深度参与
- **护城河**：OpenCode 的核心壁垒不在模型能力（依赖外部供应商），而在编排智能（上下文管理、工具系统）和生态粘性（800+ 贡献者、500万月活、178万 npm 月下载），以及"零摩擦"的分发策略
