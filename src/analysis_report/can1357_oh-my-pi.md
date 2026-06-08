# 逆向传奇下场做 Claude Code 替代：oh-my-pi 用哈希锁住 AI 编辑、把脏活下沉 Rust（5 个月 1.1 万 Star）

> 一句话总结：oh-my-pi（命令 omp）是逆向工程传奇 can1357（VTIL/NoVmp 作者）联手 libGDX 作者 Mario Zechner 打造的终端 AI 编码 agent——用整文件哈希快照锁住编辑、规避 LLM 改文件的行号漂移，把 grep/shell/沙箱等热路径全部下沉到 Rust 原生，再叠加 40+ provider 自由路由与 IDE 级 LSP/调试器能力。5 个月冲到 1.1 万 Star、约 7600 commit、21 万行测试，技术深度在开源 AI 编码 agent 里属第一梯队;但逆向接入 Cursor 后端的 ToS 争议、双人主导的 bus factor 是绕不开的风险。

---

## 值得关注的理由

- **「逆向工程师视角做 agent」的罕见样本**。别人当「提示词工程」处理的编辑漂移、工具容错、性能，can1357 当成协议/系统问题：把性能热路径（grep/shell/ast/pty/token 计数）全部用 Rust 链入进程、无 fork-exec、单二进制跨 5 平台无 WSL。这种底层功底在纯应用层 TS agent 里很少见。
- **hashline 是最可复用的技术亮点**。用整文件哈希快照标签做「你改的是你读的版本」的乐观并发锁，编辑走行号/tree-sitter 块操作，文件漂移即三路合并恢复或硬拒绝——优雅解决了主流 agent 用 str_replace「string-not-found 重试循环」、行号 diff 漂移改错位置的顽疾。
- **「benchmaxxed」工具 harness 把弱模型拉满**。README 给出可验证数字：Grok Code Fast 通过率 6.7%→68.3%、MiniMax 2.1×、Grok 4 Fast 输出 token −61%——印证作者「The Harness Problem」的论点（很多模型「不行」其实是工具框架在拖垮）。
- **工程严谨度远超同类 agent**。932 个测试文件 / 约 21 万行测试、TUI 差分渲染回归 + 压力测试、专门的编辑基准包、跨平台 CI matrix——区别于大量零测试的 agent 项目。
- **顶级技术血统 + 罕见协作**：can1357（逆向/内核传奇）+ badlogic（Mario Zechner，libGDX 作者，omp 是其 Pi 的 fork 且本人深度参与）+ 自建 AI bot 自维护。

---

## 项目展示

README/官网 omp.sh 含各差异化特性的 TUI 演示截图：

![oh-my-pi hero](https://raw.githubusercontent.com/can1357/oh-my-pi/main/assets/hero.png)

> 官网 <https://omp.sh>（含 LSP/DAP 调试器/浏览器/subagent 等特性演示）;社交卡片兜底：`https://opengraph.githubassets.com/1/can1357/oh-my-pi`

---

## 项目画像

| 维度 | 数据 |
|---|---|
| 全名 | `can1357/oh-my-pi`（命令 `omp`） |
| 定位 | 终端 AI 编码 agent（Claude Code 竞品），Bun(TS) + Rust monorepo |
| Star / Fork | 11,164 ⭐ / 943 🍴（CSV 抓取 9,360，爆发型增长） |
| License | MIT |
| 代码规模 | 账面 67.3 万行;真实原创 ~34-42 万（剥离生成 protobuf 1.5万 + models.json 6万 + vendored brush 3.4万 + 测试 21万） |
| 语言 | TypeScript 73% + Rust 8% + Python 6%;注释比 0.153 |
| 建库时间 | 2025-12-31（极新，约 5 个月） |
| 开发节奏 | 约 7,622 commit（~50/天）;最新 tag v15.10.3 |
| 贡献者 | 30 人，can1357 ~4780（主力）+ badlogic 1343 + roboomp 390（自建 AI bot） |
| 作者 | can1357（Can Bölük，VTIL/NoVmp/Blackbone 逆向传奇）+ Mario Zechner（libGDX） |
| 上游 | badlogic 的 Pi（pi-mono）的 fork，「Pi + batteries included」 |

> 说明：depth-1 克隆使 facts 的 dev_rhythm 失真，提交节奏/贡献者均以 gh api 为准;code_scale 准确。

---

## 作者视角

### 问题发现

作者 **Can Bölük（can1357，逆向/Windows 内核圈传奇，VTIL/NoVmp/Blackbone 作者）** 把逆向工程师的视角带进 agent。hashline 的 `prompt.md` 本身就像一份对模型行为缺陷做防御性设计的规约——满篇「stale-tag rejection 要 STOP」「elided region 视为未读」「范围越窄爆炸半径越小」这类对 LLM 失效模式的工程化约束。三类痛点他都选择从底层重做：编辑漂移、弱模型被 harness 拖垮、性能/可移植性、provider 锁定。

### 解法哲学

- **底层重做**：性能热路径（grep/shell/ast/pty/token 计数）全部下沉 Rust（`crates/`，~27K 行），链入进程跑 libuv 线程池，无 fork-exec，单二进制覆盖 5 平台、Windows 不需 WSL。
- **benchmaxxed harness**：每个工具针对「让最弱模型也做对」调优——`read` 用 tree-sitter 结构摘要而非 dump 全文、pi-shell 内置输出最小化器把 `npm install` 刷屏压成一行、每个工具调用强制带 `_i`（intent）字段逼模型先声明意图。
- **provider 自由**：40+ provider、按角色路由、fallback 链、轮换凭据，拒绝单后端锁定（代价见安全节）。

### 背景知识迁移

逆向功底 → 手工重建 Cursor 私有后端协议（`agent.proto` 3526 行 → 15274 行生成 protobuf client）;系统/内核功底 → `pi-iso` 跨平台隔离 PAL（APFS `clonefile`、Linux `overlayfs`、Windows `ProjFS`、`git worktree` 兜底）把「子 agent 各一份 COW 工作树」做成零深拷贝。这套「把脏活下沉原生 + 对不可靠组件做防御性契约」正是逆向工程师改造黑盒系统的惯性思维。

### 战略图景

omp 是 **Mario Zechner（badlogic，libGDX 作者）的 pi-mono 的 fork** 且本人深度参与（#2 贡献者），把 Pi 的「终端优先编码 UX」扩成 batteries-included。`python/robomp/`（roboomp）是自建的自托管 GitHub triage bot，驱动 `omp --mode rpc` 在 per-issue 工作树里自动分类/复现/修 bug/开 PR——**用自己维护自己**，部分解释了极高提交频率。provider 自由是护城河，但逆向 Cursor 一条把可持续性押在了别人的私有协议稳定性与 ToS 容忍度上。

---

## 核心价值提炼

### 创新点

**1. hashline 哈希锚定编辑** — 新颖度 5/5 · 实用性 5/5 · 可迁移性 5/5

**整文件 xxHash32 快照标签做乐观并发锁** + 行号/tree-sitter 块操作 + 漂移三路合并恢复/失败硬拒。section header 带 4-hex 标签 `[path#TAG]`（整文件规范化文本的 xxHash32 低 16 位）;`SnapshotStore` 记「全文→标签」，落地时 `computeFileHash(live)===expected` 判定文件在 read 与 edit 间是否漂移;漂移则把编辑 apply 到历史快照、`fuzzFactor:0` 精确三路合并到现盘，失败抛 `MismatchError` 带富诊断逼模型重读。**校正**：这是「快照标签 + 乐观并发控制」（哈希粒度=整文件），README「edit by content hash / point at anchors」是营销化表述，并非逐行内容寻址——把校验成本从「每行哈希」降到「一次整文件哈希」，token 极省。适用：任何 LLM-改文件流水线，可直接替换 str_replace/行号 diff 的脆弱性。**omp 最大且最可复用的技术资产。**

**2. benchmaxxed 工具 harness（弱模型适配）** — 新颖度 4/5 · 实用性 5/5 · 可迁移性 4/5

`read` 用 tree-sitter 结构摘要 + 选择器恢复提示;pi-shell 输出最小化器;强制 `_i` intent 注入为 schema 首属性;流中 steering 中断（time-traveling stream rules：正则命中即中断 token 流、注入规则、从同点重试，且注入存活于 compaction）。让便宜/小模型可用。

**3. Rust 进程内 harness（无 fork-exec + 会话存活 shell + 共享缓存）** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 3/5

grep/glob/find/ast/pty/token 计数全部 N-API 链入进程（`pi-natives`），`fs_cache` 以 mtime 为键被 read/grep/lsp 共享;`pi-shell` 基于 vendored brush 做进程内 bash，会话跨调用存活。对延迟/跨平台（含 Windows 无 WSL）敏感的 CLI agent。

**4. 跨平台 COW 工作树隔离（pi-iso）** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 3/5

APFS clonefile / overlayfs / ProjFS / git worktree 四后端统一 PAL + git diff 抽取变更，subagent 各一份零深拷贝隔离副本再安全合并。**注意：是隔离/可回滚设施，非对抗恶意代码的安全沙箱。**

**5. 40+ provider 角色路由 + fallback + 轮换凭据** — 新颖度 3/5 · 实用性 5/5 · 可迁移性 4/5

按意图路由角色（default/smol 廉价子 agent/slow 深推理/plan/commit）+ fallback 链（配额墙时下一个接管）+ 路径作用域角色 + 轮换凭据。

**6. 文件系统抽象一切 + BM25 工具召回** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 5/5

GitHub PR/issue、子 agent 输出、skill/rule/conflict 都是「路径」（`pr://`/`issue://`/`agent://`/`conflict://`...），复用同一 `read`/`search`/`write`;隐藏工具不进上下文，靠 `search_tool_bm25` 按需召回。工具爆炸时的上下文预算管理范式。

**7. 逆向 Cursor 私有协议接入** — 新颖度 5/5（工程量惊人）· 实用性 3/5 · 可迁移性 1/5

手工重建 .proto + Connect/HTTP2 直连。强依赖他方私有协议 + ToS 风险（见安全节）。

### 可复用模式

1. **整文件指纹乐观锁 + 漂移恢复**：廉价整文件哈希做「你改的是你读的版本」证明，漂移即三路合并或硬拒 — 所有不可靠生产者写文件的场景。
2. **注入式 BlockResolver seam**：纯核心声明契约、宿主注入 tree-sitter 实现，库零语言依赖 — 可测试/可替换重依赖的库设计。
3. **声明式工具描述符**（schema 类型化 + 审批 tier + 并发模式 + 发现模式）— 任何 tool-calling agent。
4. **强制 intent 字段 + schema 首属性重排**：低成本提升弱模型可控性与可观测性。
5. **输出最小化器**：把刷屏命令输出压成摘要省 token — 任何把命令输出喂 LLM 的系统。
6. **能力即路径 + BM25 按需召回**：统一 FS 接口收敛多能力 + 隐藏工具降上下文负担。

### 关键设计决策

- **agent-session loop + compaction**：`coding-agent/src/session/agent-session.ts`（9862 行）主循环 + `packages/agent/`（与应用解耦的 agent 运行时：`agent-loop.ts` runLoop/executeToolCalls 并行调度 + `compaction/` 长上下文压缩纯函数）。`executeToolCalls` 并行跑工具、支持流中 steering 中断;provider 感知（GPT-5 走 `apply_patch`、按模型设批量上限）。
- **hashline 漂移恢复双护栏**：外部写入合并 + 会话链 replay（行数相等 + 锚点行内容一致双护栏），即便都满足仍发 `RECOVERY_SESSION_REPLAY_WARNING` 让调用方核对——诚实标注不确定性。多 section 走 preflight 全内存预演，天然 all-or-nothing。
- **tree-sitter 块操作**：模型只指构造体起始行，tree-sitter 解析整个语法块闭合边界，模型永不数结尾行。

---

## 竞品格局

| 竞品 | 定位 | 优势 | 劣势/差异 |
|---|---|---|---|
| **oh-my-pi（本项目）** | 终端 AI 编码 agent | hashline 编辑可靠、Rust 原生 harness、40+ provider、IDE 级（LSP/DAP/浏览器）、工程严谨 | 逆向 Cursor ToS 风险、bus factor、跨平台维护负担、红海后来者 |
| **Claude Code**（Anthropic 官方） | 赛道标杆，闭源 | 一手模型协同、原生二进制、生态最成熟、品牌背书 | 闭源、绑 Anthropic;omp 开源 + provider 自由 + IDE 集成更深 |
| **OpenAI Codex CLI** | OpenAI 官方 | 多榜领先、OAuth 订阅 | 绑 OpenAI |
| **OpenCode**（sst） | 开源 TUI 标杆 | 15 万 star/650 万 MAU、生态最大 | omp 以原生性能 + IDE 深度差异化 |
| **Aider** | 开源结对编程 | 410 万安装、Git 集成深 | 编辑走 diff/str_replace，无内建 LSP/调试器/沙箱 |
| **Crush**（Charm） | TUI agent 颜值流 | 终端体验好 | 工具/provider 广度不及 omp |
| **Cursor**（IDE） | 闭源 IDE | Composer + 一体化 | **被 omp 逆向接入后端**（见安全节争议） |
| **Pi**（badlogic 上游） | 极简编码 agent | omp 之根、轻量 | omp = 「Pi + batteries included」重型 fork |

**关键对照轴**：① Rust 原生性能 + pi-iso 隔离 vs 纯 TS/Python;② hashline 快照锁编辑 vs 行号/str_replace;③ 40+ provider（含逆向 Cursor）vs 绑单厂商;④ benchmaxxed harness（省 token/提弱模型）vs 通用;⑤ MIT 全开源 vs Claude Code/Cursor 闭源。

**综合结论**——护城河：① 逆向工程师底层功底（性能/隔离/协议全部下沉重做）;② hashline（最可复用、最难被表面抄走的编辑机制）;③ Rust 原生 harness + 跨平台 COW 隔离;④ 40+ provider 路由自由;⑤ 工程严谨（21 万行测试 + 跨平台 CI + self-hosting bot）。竞争风险：① 逆向 Cursor 的 ToS/可持续性;② AI 编码 agent 红海，官方随时碾压;③ **bus factor**——核心 can1357 + badlogic 双人主导 67 万行体量，结构性脆弱;④ 跨 5 平台 + vendored brush + 原生绑定的维护负担;⑤ long-context compaction 可靠性是共性难题。生态定位：面向重度终端/多模型用户的「最全能开源编码 agent surface」，技术深度领先而非用户体验普惠领先。

---

## 套利机会分析

- **对做 AI-改文件工具的开发者（最大价值）**：hashline 的「整文件指纹乐观锁 + 漂移三路合并/硬拒」可直接替换 str_replace/行号 diff 的脆弱性——是当前最优雅的 LLM 编辑落地方案，`packages/hashline/` 是无 FS 依赖的纯库可借鉴。
- **对做 agent 框架的人**：声明式工具描述符（schema + 审批 tier + 并发 + 发现）+ 强制 intent 字段 + 输出最小化器 + 能力即路径 + BM25 召回，是一整套可复用的 harness 范式。
- **对追求性能/跨平台的 CLI 工程师**：「热路径下沉 Rust 原生（N-API）+ 进程内会话存活 shell + 共享 mtime 缓存 + 单二进制 5 平台」是完整参考。
- **对想用弱模型省成本的团队**：benchmaxxed harness 把弱模型拉满的机制（结构摘要 read / 最小化器 / intent / steering）值得借鉴。
- **对内容创作者**：「逆向传奇做编码 agent」「hashline 解决 AI 编辑漂移」「Pi 原作者参与 fork」「逆向 Cursor 的 ToS 之争」都是有张力的选题。

---

## 安全与合规（重点专节）

- **pi-iso 隔离（正向，但需正名）**：`crates/pi-iso/` 提供 COW 工作树隔离（APFS clonefile / overlayfs / ProjFS / worktree），让 subagent 在隔离副本里改动、再用 git diff 安全合并。**这是「工作区隔离 + 可回滚」的性能/正确性设施，不是对抗恶意代码执行的安全沙箱**——它不限制 agent 跑出来的命令访问网络或隔离区外资源。把它当安全边界会高估防护。
- **逆向 Cursor 后端的 ToS 与可持续性风险（中立）**：`packages/ai/src/providers/cursor/` 手工重建了 Cursor 私有 agent 协议（3526 行 .proto → 15274 行生成 client），以伪装客户端版本串经 Connect/HTTP2 直连 `api2.cursor.sh`，使用户能用自有 Cursor 订阅额度在 omp 跑模型。**中立评估**：① 用第三方客户端访问 Cursor 私有 API、以非官方方式消耗订阅额度，**很可能违反 Cursor 服务条款**，存在账号封禁风险;② 强依赖未公开、可随时变更的私有协议——Cursor 一次后端改动即可让该 provider 失效，可持续性不在 omp 掌控。这是「provider 自由」战略的代价。（本报告不提供任何绕用/规避指引。）
- **全权限编码 agent 的执行风险**：omp 默认能跑 bash、改文件、驱动浏览器（含 stealth 反检测）、连 SSH。审批 tier（read/write/exec）与 ACP 的权限请求提供门控，但默认交互模式下仍是高权限主体——配合不可信仓库/prompt injection 时风险面大。
- **极高频迭代 + AI bot 自维护的质量**：~7622 commit / 5 个月、roboomp 自动开 PR 修 bug。好处是迭代快、dogfooding 充分;隐忧是 AI 生成改动占比高时回归/微妙正确性 bug 累积——但测试体量（932 文件）与 CI matrix 较强，部分对冲。

---

## 风险与不足

- **逆向 Cursor 的 ToS/可持续性**：很可能违反 Cursor 服务条款（封号风险）+ 强依赖随时可变的私有协议（随时失效）。
- **bus factor**：核心由 can1357 + badlogic 双人主导 67 万行体量，结构性脆弱。
- **pi-iso 非安全沙箱**：是隔离/可回滚设施，全权限 agent 默认执行面大。
- **红海竞争**：AI 编码 agent 极卷，OpenAI/Anthropic 官方随时碾压;omp 技术深度领先但用户体验普惠/生态规模不及 OpenCode/Aider。
- **跨平台维护负担**：5 平台 + vendored brush + 原生绑定，Windows 已暴露多工具失败（#1771）。
- **long-context compaction 可靠性**：compaction 后丢已批准 plan 文件（#1246）等——所有 agent 的共性难题。
- **营销表述与实现差**：hashline「content hash」实为整文件快照标签，读者需自行校正。

---

## 行动建议

- **用它**：`curl -fsSL https://omp.sh/install | sh` 或 `bun install -g @oh-my-pi/pi-coding-agent`（需 bun ≥ 1.3.14）;在隔离环境运行高权限 agent;逆向 provider 慎用（ToS/封号风险）。
- **学它（首选）**：精读 `packages/hashline/src/`（整文件快照锁 + 漂移恢复，最可复用）+ `packages/agent/src/agent-loop.ts`（工具调度 + steering）+ `crates/pi-shell`/`pi-iso`（Rust 进程内 shell + COW 隔离）+ `packages/ai/src/`（provider 路由）。
- **fork 它**：MIT 可二次开发;`hashline` 是无 FS 依赖纯库，可单独取用做 LLM 编辑层。
- **客观看卖点**：hashline 是整文件快照锁（非逐行内容哈希）;benchmaxxed 数字来自官方;逆向 provider 不可持续。

---

## 知识入口

| 入口 | 链接 | 用途 |
|---|---|---|
| GitHub 仓库 | <https://github.com/can1357/oh-my-pi> | 源码 / Issue |
| 官网 | <https://omp.sh> | 特性演示 + 安装 + 文档 |
| 核心库 | 仓库内 `packages/hashline/src/` | 整文件快照锁编辑（最可复用资产） |
| Rust 核心 | 仓库内 `crates/pi-shell` / `pi-iso` / `pi-natives` | 进程内 shell + COW 隔离 + 原生绑定 |
| 作者博客 | blog.can.ac（尤其「The Harness Problem」） | 理解 benchmaxxed 哲学 |
| 作者逆向项目 | VTIL / NoVmp / NtRays / Blackbone | 理解技术基因 |
| 上游 | badlogic 的 Pi（earendil-works/pi） | omp 之根 |
| DeepWiki | <https://deepwiki.com/can1357/oh-my-pi> | AI 架构导览 |
