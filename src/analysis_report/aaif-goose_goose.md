# Goose 一年半 48K stars：Block 捐给 Linux 基金会的「AI 代理界的 Kubernetes」怎么做到中立而不死

> GitHub: https://github.com/aaif-goose/goose

## 一句话总结

Goose 是一个由 Block, Inc. 捐给 Linux 基金会 AAIF（Agentic AI Foundation）的本地优先、模型无关、跨表面的开源 AI 代理——10 个 Rust crate + Electron 前端，约 18 万行 Rust 代码 + 528 名贡献者、近一年日均 9 次提交，用 MCP（能力侧）+ ACP（客户端互联侧）双标准把自己接入开放生态，已发布到 v1.37 并正全力推进 v2 RC。

## 值得关注的理由

- **现象级 + 中立治理组合**：48.6K stars / 5.1K forks，2025–2026 现象级 AI 代理之一；同时挂靠在 Linux 基金会旗下（与 Kubernetes 同级治理），在企业采购的「可信」维度上有独家优势。
- **「加 provider = 加 JSON 文件」的极致可扩展性**：约 30 个 LLM 后端用 declarative JSON 配置覆盖，runtime 通过 `${ENV_VAR}` 懒展开、支持 UI 端改值不需要重启——是「数据驱动 vs 代码驱动」哲学的工业级范例。
- **三套 UI 并行重写期**：v1.x 桌面应用（`ui/desktop`）、Goose 2（`ui/goose2`）、v2（`ui-v2/src`）同时存在并热改，是当前工程团队投入产出最剧烈的窗口期。

## 项目展示

![Goose Icon](https://aaif.io/wp-content/uploads/2026/04/goose_icon.svg)
*基金会官网项目主 Logo——「Goose Doubles Down on Open」是其最新的公开定位标语。*

![Interactive Loop diagram](https://goose-docs.ai/assets/images/interactive-loop-55558c45ba877033b3bd355c500150ef.png)
*官方文档站的「6-step 交互循环」示意图：Human Request → Provider Chat → Model Extension Call → Response to Model → Context Revision → Model Response——把 AI 代理从「chat」拉回到「自治循环」。*

![Goose Doubles Down on Open hero](https://aaif.io/wp-content/uploads/2026/06/goose-doubles-down-on-open-hero-1-1024x572.png)
*v1.36/v1.37 公告博客封面，主题是把治理加固到 Linux 基金会旗下，呼应「中立而不死」的开源治理路线。*

> 仓库 README 本身没有可收录的展示图（5 个媒体元素全部为 shields.io / Linux Foundation / Repology badge）；上面三张均来自 goose-docs.ai 架构页与 AAIF 博客，是该项目当前对外传播的主视觉。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/aaif-goose/goose |
| Star / Fork | 48,573 / 5,098（监视 245） |
| 代码行数 | tokei 全仓 ~63 万行（含 JSON 53.4%、Rust 25.9%、TSX 9.3%、TS 4.6%、YAML 3.6%）；Rust workspace 合计 ~18 万行、406 个 .rs 文件 |
| 项目年龄 | 21.5 个月（首次提交 2024-08-23；2026-06-10 最新提交） |
| 开发阶段 | 密集开发（近 30 天 282 commit，近 365 天 3,339 commit；日均 9+ commit） |
| 贡献模式 | 职业项目（周内 93.5%、深夜 12.1%）；528 名贡献者、Apache-2.0、Block 创建、AAIF 治理 |
| 热度定位 | 大众热门（48.6K stars，AI 代理赛道第一梯队） |
| 质量评级 | 代码 优秀（Rust 1.91.1 pinned、clippy 0-warning strict、cargo-deny + cargo-machete）<br>文档 优秀（README + CONTRIBUTING + GOVERNANCE + per-MCP-server 用法 + AGENTS.md）<br>测试 充分（23 个集成测试 + recipe-style self-test + self-referential CI） |

> 注：2026-03-25 Block 把 repo 从 `block/goose` 正式移交到 Linux 基金会新成立的子基金会 AAIF（Agentic AI Foundation）——`aaif-goose` 这个 Org 是 2026-03-25 才创建的「中转账号」，目前只托管 5 个仓库，goose 是唯一旗舰。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Block, Inc.（Jack Dorsey 旗下，原 Square + Cash App + Tidal + TBD）的工程师团队。Block 的核心场景是金融与支付（merchant 工具、Square 生态、Cash App 后端），大量涉及「跑数据查询 → 改 SQL → 写脚本 → 跑测试」的连续工作流，而且必须在 **本地** 完成（合规与数据敏感性）——这就是 goose 起点的 dogfooding 痛点。

核心团队 12 人：7 位 Core Maintainer（Bradley Axen、Alex Hancock、Michael Neale、Douwe Osinga、Jack Amadeo、Jasper Hugo、Lifei Zhou）+ 5 位 Maintainer（Abhijay Jain、Adrian Cole、Angie Jones、Rizèl Scarlett、The-Best-Codes）。Bradley Axen 保留 deadlock tiebreaker。提交集中度上 spencrmartin 占 9.5%（847 commit）、Michael Neale 729、Alex Hancock 495、Jack Amadeo 476、Douwe Osinga 436——头部 5 人合计已超过 60%。

### 问题判断

作者看到了三件多数 AI 编程代理项目没做的事：

1. **「surface 单点」问题**：Cline / Cursor 强绑 VS Code；Aider / OpenHands 强绑终端；Claude Code / Devin 是商业闭环。要一个能在桌面、CLI、API 三端都跑、并且能跨表面切换的代理。
2. **「模型锁定」问题**：商业代理几乎全部锁单一模型（Claude Code 锁 Claude，Cursor 锁 OpenAI/Anthropic）。要一个把模型当 backend、能塞进任何 LLM 的代理。
3. **「治理真空」问题**：2024–2025 涌现的开源 AI 代理项目背后，几乎都有商业母公司（LangChain、Anthropic、Cognition、Aider 等都是公司主体），要一个由 **中立基金会** 治理、不被单一厂商战略转向绑架的项目。

### 解法哲学

- **Foundation governance over vendor governance**：选 Kubernetes 的中立化路径，把项目捐给 Linux 基金会旗下 AAIF，与 OpenJS、PyCA、CNCF 同级。信任护城河，而不是性能护城河。
- **Standards over proprietary**：MCP（能力侧，70+ 现成扩展）+ ACP（client 互联侧，能把 Claude Code / Codex 当 provider）双标准。goose 不是「另一个 LangChain」，而是「能把生态里所有 LangChain 都装进来的容器」。
- **Local-first + Rust**：性能与可移植性优先；CLI 跨平台可用、单一二进制，避开 Electron-only 或 Python-only 代理的部署痛点。
- **Beyond autocomplete**：6-step loop（Human Request → Provider Chat → Model Extension Call → Response to Model → Context Revision → Model Response）——代理是「会读 context、调用 extension、修订自己上下文、再生成响应」的自治循环，与 Cursor 的 inline-complete 完全错位。
- **「Add a provider by adding a JSON file」**：约 30 个 declarative JSON provider 把新增 LLM 后端降到 30 行配置、不用 Rust 重编译——典型 Unix-philosophy 数据驱动选择。
- **「Subscription reuse via ACP」**：明确选择 *不* 与 Claude/ChatGPT/Gemini 订阅抢市场，而是把这些订阅当 backend 用。商业模式的颠覆式差异化——比 OpenRouter 这种纯 API proxy 走得远。

**明确「不做什么」**：不绑 IDE（vs Cline）、不做 SaaS（vs Devin）、不做 inline autocomplete（vs Cursor）、不做单一模型锁定（vs Cursor/Claude Code）、不强制走云（vs Devin / OpenHands 云端 sandbox）。

### 战略意图

当前明显是 **genuinely open** 而非 open-core：CLI / Server / Desktop 三端完全开源，唯一付费面是 Block 自己的 fork（内部定制版）。`CUSTOM_DISTROS.md`（28K 字节）留有商业化钩子：第三方可通过 custom providers / extensions / branding 做受控分发。Block 作为 AAIF 的「Founding Platinum Member」保留品牌投入。

战略意图是当 **「AI 代理领域的 Kubernetes」**——中立 foundation + 跨表面 + 双标准 + Rust 本地优先。这是它在 Claude Code / Cursor / Devin 之外的差异化锚点。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序：

1. **Layered Provider System（Canonical Rust + Declarative JSON）**：用 `include_dir!` 把 30+ 个 JSON provider 配置嵌入二进制，runtime 通过 `register_declarative_provider` 映射到 openai / ollama / anthropic 三个 engine 的 Rust 实现；`env_vars` + `${VAR}` 懒展开支持 UI 后改值不需要重启；`preserves_thinking` / `dynamic_models` / `skip_canonical_filtering` 等 per-provider flag 让同一套通用代码覆盖绝大多数 LLM。新颖度 4/5、实用性 5/5、可迁移性 5/5。
2. **ACP Subscription Reuse 作为 Provider（goose → Claude Code / Codex）**：goose 不是「又一个 Anthropic API 客户端」，而是「能用 ChatGPT Plus / Claude Pro / Gemini Advanced 订阅当 LLM 后端」的代理。`mode_mapping` 把 goose 内部 4 种 GooseMode 映射到被调 agent 的 4 种 permission 模式，跨 runtime `env_remove`（`env_remove: ["CLAUDECODE"]`）解决嵌套 session 检测，`network_access=true` 解决 HTTP MCP 与 sandbox 冲突。新颖度 4/5、实用性 4/5。
3. **Tool-Pair 渐进式压缩 + Middle-Out 删除**：用 `[0%,10%,20%,50%,100%]` 五档 middle-out 算法从 message 中段删 tool response 直至 compaction 成功；与常规「删最早」策略相比，middle-out 保留了「最近上下文」+「最初意图」两端，最具信息密度的「中段」被裁掉。新颖度 3/5、实用性 5/5。
4. **Dual Message Visibility Metadata（agent_only × user_visible）**：`MessageMetadata::with_agent_invisible()` / `agent_only()` 把「是否对 model 可见」「是否对 user 可见」做成正交两 bit——compaction 后的 summary 是 agent_only（UI 不显示但模型继续读到），被压缩掉的原 message 变成 agent_invisible（保留在 session 文件以保证可重放但下一轮不会被发到 provider）。新颖度 3/5、实用性 5/5。
5. **Stop Hook with Block Cap（防 plugin bug 死循环）**：`Stop` hook 阻塞主 loop；deny 时写 user message 让模型继续尝试，超过 `stop_hook_block_cap`（默认 8）才硬结束。Plugin bug 不会让代理永远转，但合法 hook 也能阻止代理提前结束。新颖度 3/5、实用性 5/5。
6. **Self-Referential CI（goose reviews goose, solves goose issues, writes goose release notes）**：`.github/workflows/goose-pr-reviewer.yml` / `goose-issue-solver.yml` / `goose-release-notes.yml` 三个 workflow 直接 fork 自己的 goose 跑这些任务。这是开源项目里第一次有项目把「AI 代理维护自己」做成显式工程实践——Block 把自家产品当内部基础设施 dogfood 的延伸，也是「AI 代理必须用 AI 代理」这一叙事的最佳广告位。新颖度 5/5、实用性 3/5（自家才适用）。

### 可复用的模式与技巧

- **Declarative Configuration with Engine Dispatch**：30 个 JSON 文件走 3 个 Rust adapter，`engine` 字段选 adapter，`models` / `env_vars` / `preserves_thinking` 字段做 per-instance 配置，运行时懒展开 `${VAR}`。**适用：多 backend 中间件（数据库驱动、API gateway、邮件 client）。**
- **Tool Categorization → Matched Hook**：`categorize_tool(name)` 把 tool 名分 Shell/Read/Write/Other 四类，对应不同 `BeforeShellExecution` / `BeforeReadFile` / `PostToolUse` hook 的 matcher_context（command 字符串 / file path）。**适用：带 audit log / pre-commit / scanner 的 agent runtime。**
- **Compact with Three Continuation Texts**：普通 compact、tool-loop compact、手动 compact 三种用不同 continuation text 引导模型下一步行为（continue conversation vs continue calling tools vs acknowledge user request）。**适用：需要告诉模型「现在发生了什么」的上下文治理系统。**
- **Provider-as-Foreign-Process via stdio JSON-RPC + env_remove 防嵌套**：用子进程 + stdio 当 provider；用 `env_remove` 防被调进程的「我是子进程」检测；用 `mode_mapping` 把语义对齐。**适用：想让现有 CLI 工具成为自己 backend 的项目。**
- **Progressive Compaction with Middle-Out Removal**：`[0%,10%,20%,50%,100%]` 五档 + middle-out。**适用：长 session 的上下文压缩。**
- **OpenAPI 自动生成前后端**：`crates/goose-server` + `just generate-openapi` 生成 `ui/desktop/openapi.json` + TS types，desktop app 与 server 通过 OpenAPI/REST 通信，避免手写 RPC。**适用：Rust 后端 + TS/JS 前端的全栈项目。**
- **`include_dir!` 内嵌静态资源**：把 JSON provider 配置 + prompt 模板等静态文件编译进二进制，运行时不需要外部文件路径。**适用：单二进制发布、容器化部署。**

### 关键设计决策

1. **MCP boundary as the only extension integration surface**：所有外部能力都走 MCP，`crates/goose/src/providers/formats/rmcp` 已是 v1.4。Extension manager 通过 `rmcp::transport` 支持 stdio 子进程 + streamable_http_client + 容器化三种部署形态。`extension_malware_check` 在加载前对 extension 做静态检查。代价是牺牲了「比 MCP 协议更紧的耦合」，换来「任何 MCP server 即 goose extension」——MCP 生态的 70+ 工具（GitHub、JetBrains、Playwright、Firecrawl、Apify、Speech、Neon、Alby 等）零成本接入。
2. **ACP Client Interconnect（goose 本身既是被 ACP 调的 agent，也是 delegate 给别的 ACP client 的 provider）**：`crates/goose/src/providers/codex_acp.rs` 和 `claude_acp.rs` 各 ~100 行，分别 fork `codex-acp`（zed-industries 出）和 `claude-agent-acp`（agentclientprotocol 出）子进程，通过 ACP 协议 JSON-RPC over stdio 通信，把它们的对话能力当 provider 用。`mode_mapping: HashMap<GooseMode, String>` 把 goose 内部的 `Auto/Approve/SmartApprove/Chat` 四种 mode 映射到 Claude Code 的 `bypassPermissions/default/acceptEdits/plan`、Codex 的 `danger-full-access/workspace-write/read-only`。
3. **Hook System（`HookManager` + `HookEvent::BeforeShellExecution` / `BeforeReadFile` / `PostToolUse` / `Stop` / `SessionStart` 等生命周期事件）**：`crates/goose/src/agents/agent.rs` 里 `tool_inspection_manager` 是 Rust 内置 inspectors（permission inspector / judge / security / adversary / egress / repetition）；`hook_manager` 是用户配 plugin 走的扩展点。`Stop` hook 是**阻塞的**——deny 时把 deny reason 写进 user message 逼模型继续尝试，超过 `GOOSE_STOP_HOOK_BLOCK_CAP`（默认 8）才硬结束。
4. **四种 GooseMode（Auto / SmartApprove / Approve / Chat）+ permission gate**：`GooseMode` 是 4 态 enum，每种 mode 映射到具体策略——`Chat` 时 tool call 被替换成 `CHAT_MODE_TOOL_SKIPPED_RESPONSE`；`Approve`/`SmartApprove`/`Auto` 分别对应不同的「哪些 tool request 进入 `needs_approval` 集合」逻辑。`ToolInspectionManager` 是分诊台——`tool_inspection_manager.inspect_tools` 先做静态规则检查（inspector 链：`PermissionInspector` → `RepetitionInspector` → `AdversaryInspector` → `EgressInspector`），再交给 `PermissionCheckResult`（approved/needs_approval/denied 三段）。
5. **`preserves_thinking` per-provider + thinking block 在 assistant tool-call 消息上的回传**：Gemini / Claude / Kimi / DeepSeek 各自对「是否需要把 reasoning_content echo 回下一轮」的策略不同——Gemini thinking 不回传就会丢上下文，Kimi 必须回传 reasoning_content。`provider_registry.rs` 在每个 declarative JSON 里给 `preserves_thinking: bool`，`agent.rs:reply_internal` 把 thinking content 单独抽出、构造独立的 `Message::new(role=Assistant, content=[Thinking])`。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Goose | Cline | Aider | Continue | OpenHands | Claude Code | Cursor |
|------|-------|-------|-------|----------|-----------|-------------|--------|
| Stars | 48.6K | ~50K+ | ~35K+ | ~30K+ | ~50K+ | 闭源商业 | 闭源商业 |
| Surface | Desktop+CLI+API | VS Code 内 | 终端 | 多 IDE | 云端为主 | CLI | IDE |
| 模型锁定 | 15+ LLM provider | 多 provider | 多 provider | BYO model | 多 provider | Claude | OpenAI/Claude |
| 治理 | LF AAIF（中立） | 个人维护 | 个人维护 | 公司主体 | 公司主体 | Anthropic | Cursor 公司 |
| 安全 | 4-mode + inspector 链 | permission | 无 | permission | sandbox | permission | permission |
| MCP/ACP 双标准 | ✓ | 仅 MCP | 否 | 仅 MCP | MCP | 否 | 否 |
| Subscription Reuse | ✓ (via ACP) | 否 | 否 | 否 | 否 | 否（自家订阅） | 否 |
| Local-first | ✓ | ✓ | ✓ | ✓ | 部分 | ✓ | ✗ |

### 差异化护城河

- **信任护城河（Foundation governance + Apache-2.0 + CC-BY-4.0 文档）**：唯一由 Linux 基金会子基金会治理的 AI 代理项目。在企业采购的「可信」维度上有独家优势。
- **生态护城河（MCP + ACP 双标准 + 528 contributors）**：70+ MCP extension 零成本接入；ACP 让它能 delegate 给 Claude Code / Codex 等商业 CLI。
- **架构护城河（跨表面 + Rust 本地优先 + 30+ JSON provider）**：Desktop/CLI/API 三端一套代码；Rust 性能与可移植性。

技术护城河（agent loop）反而不强——核心 6-step loop 是行业共识，差异化主要在治理与生态层。

### 竞争风险

最大风险是 **Claude Code（Anthropic 背书 + 商业化深耕 + Claude 模型原生优化）** 与 **Cursor（IDE 入口 + 商业模型碾压）**。这两个不会取代 goose 但会吃掉最大的用户群。Goose 的真实威胁不是「被取代」，而是「被迫退到 Linux 基金会标准化研究项目」的位置——既不商业化也不大众化。

### 生态定位

「Linux 基金会的 AI 代理」——Kubernetes 在容器编排的位置。不是最快、不是最 fancy，但是中立、可信赖、长期。填补的是「开源 + 中立 + 跨表面 + 双标准」的生态空白。

## 套利机会分析

- **信息差**：项目知名度高（48.6K stars），但其内部架构的「数据驱动 + standards over proprietary」哲学在中文社区讨论度不高。DeepWiki 收录的中文转写、JSON provider 模式拆解、ACP mode_mapping 实现细节都是可挖掘的内容。
- **技术借鉴**：`include_dir!` + declarative JSON provider 模式可迁移到任何「多 backend 接入 + 不希望每加一个就重编译」的中间件；middle-out compaction 可迁移到任何长会话的上下文压缩；agent_only × user_visible 双 metadata 可迁移到任何 multi-audience 消息流系统。
- **生态位**：填补「中立 foundation + 跨表面 + 双标准 + Rust 本地」的空白。在 AI 代理赛道的 Kubernetes 位置。
- **趋势判断**：v1.37 → v2 RC 的过渡期是关键窗口；UI 重写（ui/desktop → ui/goose2 / ui-v2）会带来短期不稳定但长期是好事。比 Cursor / Claude Code 的后发优势是 Foundation governance 与 Subscription Reuse。

## 风险与不足

- **Provider 适配层稳定性**：[#3571](https://github.com/aaif-goose/goose/issues/3571) 揭示 v1.1.3 跨日 API auth / 404 错误，p1 级别无人响应——版本切换时 provider 层仍是高风险区。
- **Onboarding + Linux + MCP 三向交叉**：[#2351](https://github.com/aaif-goose/goose/issues/2351) 揭示 extension 添加在 Linux 上的可用性痛点，是社区反复出现的摩擦源。
- **UI 重写期不稳定**：`ui/desktop` + `ui/goose2` + `ui-v2/src` 三套并行 UI，262 次 openapi.json 修改、196 次 main.ts 修改说明前端架构正在剧烈变化——用户在此期间可能面临频繁升级破坏。
- **「Foundation governance 是双刃剑」**：Block 作为 Founding Platinum Member 仍有相当话语权，捐赠不等于完全中立；merit-based 晋升路径在「公司化」项目里是否能完全跑通还需观察。
- **社区贡献集中度高**：Top 5 贡献者占 60%+ commits，528 个「社区层」贡献者合计仍然有限——社区驱动深度低于 Kubernetes / Rust 核心项目。

## 行动建议

### 如果你要用它

- **首选场景**：需要跨表面（桌面 + CLI + API 三端都要）、本地优先（数据敏感）、多模型切换（不被单一 LLM 锁死）、订阅复用（用现有 Claude/ChatGPT/Gemini 订阅）、企业治理（需要中立 foundation）。
- **不推荐场景**：只要 IDE 内联补全（用 Cursor / Copilot）、只要 terminal 极致轻量（用 Aider）、只要 autonomous SWE benchmark（用 OpenHands）、只要云端外包（用 Devin）。
- **vs 竞品选择**：追求「中立 + 可信赖 + 跨表面」选 goose；追求「极致 UX + 商业模型碾压」选 Cursor / Claude Code；追求「极简 terminal + Python 启动快」选 Aider。

### 如果你要学它

重点关注的文件与模块：

- `crates/goose/src/agents/agent.rs`（247 次修改）—— agent 主循环，6-step loop 的具体实现
- `crates/goose/src/providers/`（含 `declarative/` 目录 30+ JSON 文件）—— Layered Provider System 范本
- `crates/goose/src/context_mgmt/mod.rs` —— middle-out compaction + tool-pair summarization 实现
- `crates/goose/src/security/` —— prompt-injection 检测 + permission inspector 链
- `crates/goose/src/providers/codex_acp.rs` + `claude_acp.rs` —— ACP client interconnect 范本（每文件 ~100 行）
- `crates/goose/src/agents/extension.rs` —— MCP extension 加载、permission snapshot、malware check
- `AGENTS.md` —— 给 AI agent 看的工程规范，是「AI 工具写 AI 工具」的 meta 实践
- `.github/workflows/goose-pr-reviewer.yml` / `goose-issue-solver.yml` / `goose-release-notes.yml` —— self-referential CI 范本

### 如果你要 fork 它

可改进的方向：

- **Provider Layer**：增加 Anthropic prompt caching 的 declarative JSON 支持（目前 `preserves_thinking` 字段已经开了口子）
- **UI 重写**：选 `ui/goose2` 或 `ui-v2` 之一作为新 base，避免三套并行 UI
- **ACP 反向**：把自己做成 goose 的 ACP server（被 goose 调用），而不只是 client
- **Self-Hosting 简化**：CUSTOM_DISTROS.md 28K 字节，对自部署企业仍是门槛；可考虑加 Docker compose / Kubernetes Helm chart
- **自定义 extension 市场**：目前 70+ MCP extension 是松散的，缺少官方 registry 与评分系统

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/aaif-goose/goose（commit c365e7b9，2026-05-02） |
| Zread.ai | 未收录（HTTP 403 / Cloudflare 拦截） |
| 关联论文 | 无（goose 是工程产品，未在 arXiv 发表） |
| 在线 Demo | 无公开 playground（goose 是本地运行 agent；官网 https://goose-docs.ai/ 提供桌面/CLI 下载，docs 提供 recipe 示例） |
| 官方文档 | https://goose-docs.ai/ |
| 基金会页 | https://aaif.io/projects/goose |
| 架构图 | https://goose-docs.ai/assets/images/interactive-loop-55558c45ba877033b3bd355c500150ef.png |