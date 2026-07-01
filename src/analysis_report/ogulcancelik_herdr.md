# GitHub推荐：3 个月 8.9K★ 的 herdr：单作者如何把 agent 多路复用做到终端里

> GitHub: https://github.com/ogulcancelik/herdr

## 一句话总结

herdr 是一个把 17+ AI 编码 agent 当 pane 多路复用的 Rust 终端应用，用 vendored libghostty-vt 保证 pane 里跑 lazygit / vim / Claude Code 自己的 TUI 时仍像「真终端」，并通过 JSON socket + 二进制 socket 双协议让 agent 能脚本化驱动彼此。

## 值得关注的理由

1. **2026 年首个 agent-native terminal multiplexer**：在 tmux 不认识 agent 语义态、Web 调度面板（vibe-kanban）脱离终端体验的真空里，herdr 切下了「TUI + 真终端 + agent-aware」这个精确交集。
2. **3 个月、974 commits、66 个 release、88% 单作者占比**——一个 side-project 强度的全栈独立开发者，正在以每天 ~10 commit 的节奏把 libghostty-vt + 17 个 agent 适配层 + headless server + manifest 远程热更新一起打通。
3. **设计纪律罕见地严格**：`AppState` 完全无 PTY/无 async 的纯数据架构 + section-isolated 热配置 + manifest-as-data + vendored deps with patch log——这是「为什么能撑住 1k+ commits 不崩」的根本，也是最值得抄的工程范例。

## 项目展示

1. ![herdr logo](https://raw.githubusercontent.com/ogulcancelik/herdr/master/assets/logo.png) — 品牌标识，hero 性质
2. ![iPhone 上 SSH 进 herdr 跑 agent 会话](https://herdr.dev/assets/mobile-agent-session-v2.jpeg) — 「从手机 attach 终端跑 agent」差异化亮点
3. ![iPhone 上的 agent switcher 菜单](https://herdr.dev/assets/mobile-switch-menu-v2.jpeg) — 移动端响应式 TUI 的真实场景
4. ![README star-history 曲线](https://api.star-history.com/svg?repos=ogulcancelik/herdr&type=Date) — 增长曲线（3 个月跃升 8.9k）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/ogulcancelik/herdr |
| Star / Fork | 8,987 / 537 |
| 代码行数 | 453,462（Zig 43.1%, Rust 36.1%, C++ 7.2%, C Header 4.4%, 其他 9.0%） |
| 项目年龄 | 3.3 个月（首提交 2026-03-23） |
| 开发阶段 | 密集开发 |
| 开发模式 | 业余 Side Project（深夜占比 45.4%, 周末占比 23.9%） |
| 贡献模式 | 单人主导（Ogulcan Celik 占比 ~87.8%, 真人贡献者约 5–6 人） |
| 热度定位 | 大众热门（574 stars/千日, fix:feature ≈ 3:1 仍在打磨期） |
| 质量评级 | 代码 A, 文档 A, 测试 A-（13.5K 行 integration test） |
| License | Other（自定义 / 非 OSI 标准——需注意） |
| 最新版本 | v0.7.1（共 66 个 tag, ~1.5 天/版） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Ogulcan Celik（GitHub `ogulcancelik`，博客 `oddbit.ai`），2014 年注册的 12 年老账号，公开 36 个仓库但 herdr 一枝独秀（8.9k★）。他在做 herdr **之前**就是 AI agent 生态的重度使用者——同账号下还维护 `pi-extensions`（159★）和 herdr 的两个 plugin 样板。商业公司背景不明显，是个 side-project 阶段的全栈独立开发者。

### 问题判断

当开发者从「本地 IDE 跑一个 Claude」进化到「远端服务器并行跑 5–10 个 coding agent」时，会同时撞到三堵墙：

- tmux 持久化但**不认识 agent 语义态**——你只知道 shell 进程在跑，不知道它是「blocked / working / done」
- Web 调度面板（vibe-kanban / Conductor）能识别状态但**把终端包进了 GUI**——破坏了「从手机 SSH 进服务器」「agent 自己开 lazygit/btop」的场景
- 现有 LLM 框架（rig / agentos）能解决 SDK 问题，但**不解决「一眼看完 N 个 agent」**

herdr 的赌注是：**agent 编排会成为 dev tool 的下一个分层，终端形态对资深工程师仍然最高效**。

### 解法哲学

- **One binary, not an app**：单一 ~10MB Rust 二进制，无 GUI、无 Electron、无账号、无 telemetry
- **状态/运行时分离**：`AppState` 完全无 PTY/无 async（AGENTS.md 第一条原则），headless server 与 TUI 共享同一份状态机
- **manifest-as-data**：agent 识别规则是版本化的 TOML，不动 Rust 引擎就能适配新 agent / 新版本
- **真终端渲染**：vendored libghostty-vt 让 pane 内部跑 Claude Code 自己的 TUI 时仍像真终端——这是 Web 面板永远做不到的

### 战略意图

短期补 agent 兼容 + Windows beta；中期走「server-owned runtime protocol with the TUI as one client」（任何终端/Web/CLI 都能 attach，AGENTS.md 明确写）；长期押注「agent 编排」分层。开源策略是 genuinely open 但 license 是自定义「Other」——这是早期采用者而非企业客户导向的信号。

## 核心价值提炼

### 创新之处

1. **Manifest-based agent detection engine + 远程热更新**（新颖 4/5, 实用 5/5, 可迁移 5/5）
   agent UI 文案变 → 加个 TOML 规则 + 升 `version = "2026.06.10.3"`，CI 用 `agent_detection_manifest_check.py` 验证，后台 `manifest_update` 还可从 herdr.dev 拉更新。任何 scraping / policy / build 状态推断场景都适用。

2. **PTY live handoff with fd passing**（新颖 5/5, 实用 4/5, 可迁移 3/5）
   `HandoffRuntimeState` 序列化 PTY master fd + scrollback ANSI + keyboard protocol + agent input state，新进程 `from_handoff_fd` 接住——零中断迁移，是 #614/#712/#719/#765 反复打磨的核心能力。

3. **Validated section-level config reload**（新颖 3/5, 实用 5/5, 可迁移 5/5）
   `apply_live_config` 按 section 隔离：单个 section 解析失败时该 section 完全保留旧值；`validated_sidebar_bounds` 防 `min > max` 让 `u16::clamp` panic。任何「配置 reload 不该让服务宕」的服务都该抄。

4. **CJK-IME prefix-mode 输入法切换**（新颖 5/5, 实用 4/5, 可迁移 3/5）
   macOS 中文 IME 下按 `Ctrl+B` 会被输入法截获——herdr 进 prefix mode 时主动 `TISSelectInputSource` 切到 ASCII layout，退出时恢复。vim/tmux/lazygit 的「中文用户快捷键不灵」老问题可借鉴。

5. **双 socket 协议架构**（新颖 4/5, 实用 5/5, 可迁移 5/5）
   `herdr.sock`（JSON + schemars 自动 schema）给 agent 编程控制用；`herdr-client.sock`（length-prefixed binary frame + dirty-patch 流）给远程 attach 用。任何「GUI/TUI + 脚本 + 远程」三件套产品都会撞到同样需求。

### 可复用的模式与技巧

- **State / Runtime 分离 + Test on Bytes, Not Terminals**：`AppState` 是纯 `Clone/Serialize` 数据，所有 action 在纯状态上跑测试，13.5K 行 integration test 全跑在 mock PTY 字节流上
- **Pending Confirmation State Machine**：状态变更前 N 次确认 + 时间窗上限（`pending_idle_confirmation: u8 = 3` + 700ms cap），防 latch
- **Vendored Dep with Explicit Patch Log**：`vendor/libghostty-vt.patches.md` 记录每个 patch 的 upstream PR + verification 步骤——「我知道我改了什么、什么时候能拿掉」的纪律
- **Self-Describing Tool for Its Own AIs**：`SKILL.md`（给消费 herdr 的 agent）+ `AGENTS.md`（给修改 herdr 的 agent）+ `.codex/ .pi/ .zed/`（各 agent 的工作目录配置）——任何「未来想被 AI 用户使用」的开源工具都该考虑这个双向飞轮

### 关键设计决策

1. **决策**: vendored libghostty-vt（Zig + C++）嵌入 Rust 二进制
   - 问题：想在用户 terminal 里「画」出真终端，不重新发明轮子
   - 方案：编译期 build.rs 把 libghostty-vt 编成静态库，bindgen 生成 `ghostty/bindings.rs` 供 Rust 调用
   - Trade-off：1,446 次 vendor 目录修改的「隐藏技术债」+ Zig toolchain 构建复杂度，换来「largest 终端兼容 + 真 vt 处理」
   - 可迁移性：中——patch 治理纪律比技术本身更值得抄

2. **决策**: 双 socket 协议（JSON + Binary）
   - 问题：agent 想编程控制面板 vs 远程 attach 需要流式渲染
   - 方案：`herdr.sock`（schemars schema 文档化）+ `herdr-client.sock`（length-prefixed frame + dirty-patch）
   - Trade-off：两套路径管理
   - 可迁移性：高

3. **决策**: `AppState` 完全无 PTY/无 async，`TerminalRuntime` 通过 `TerminalId` 在 Registry 里单独存活
   - 问题：测试要求纯函数式状态变更 + headless server 跑同一份状态机
   - 方案：严格执行 AGENTS.md 第一条「State is separated from runtime」
   - Trade-off：多一层 `workspace.tab.pane → terminal_id → runtime` 映射
   - 可迁移性：高——这是「为什么 herdr 能撑住 1k+ commits 不崩」的关键

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | herdr | tmux / Zellij | BloopAI/vibe-kanban | 0xPlaygrounds/rig | rivet-dev/agentos |
|------|-------|---------------|---------------------|-------------------|-------------------|
| 形态 | TUI 二进制 | TUI 二进制 | Web/Electron 面板 | Rust 库 | Linux VM runtime |
| 终端保真度 | 高（vendored libghostty-vt） | 高 | 低（GUI 重画） | N/A | N/A |
| Agent 语义态 | ✅ Idle/Working/Blocked/Done | ❌ 需写 hook | ✅ 卡片化展示 | N/A | ⚠️ runtime 层 |
| 远端 attach | ✅ 原生 SSH + 手机响应式 | ✅ SSH 转发 | ❌ 需浏览器 | N/A | ⚠️ VM 访问 |
| 单二进制 | ✅ ~10MB | ✅ | ❌ 200MB+ Electron | ✅（库） | ❌ VM |
| 账号/telemetry | ❌ 无 | ❌ 无 | ⚠️ 通常有 | N/A | N/A |
| Stars | 8.9K | 35K / 25K+ | 27.2K | 7.8K | 3.4K |

### 差异化护城河

**「在终端里 + 真终端 + agent-aware」三件事的交集**——同时具备真 terminal（lazygit 能跑）+ 远端可访问（SSH 直连）+ agent 状态感知（侧栏红点）。同时无 GUI / 无账号 / 单二进制——这四点是 Web 调度面板永远追不上的护城河。

### 竞争风险

- **上游 libghostty-vt 变化**：跟 Zig 项目的 ABI 对齐负担重（vendor 1,446 次修改）
- **GUI manager 抄作业**：cmux / Conductor 哪天支持「终端模式」或「SSH 远端 attach」，护城河会缩水
- **agent 厂商内化**：Claude Code 自己的 TUI 越做越复杂，自带 session 管理——herdr 的「agent 多路复用」价值会被侵蚀
- **License 是自定义 Other**：企业采用前需要 legal review

### 生态定位

**「agent-first tmux」**——在 dev tool 分层里占「agent 的终端/调度器」层；与 vibe-kanban 同层但坚持 terminal-only；与 IDE 内 AI 助手（Cursor/Copilot）互补，不竞争；与 rig / agentos 互补（一个上层一个底层）。

## 套利机会分析

- **信息差**：8.9K★ 在 3 个月龄的项目中已经进入「大众热门」门槛（574 stars/千日），但 vendor 的 libghostty-vt 维护成本、fix:feature = 3:1 的早中期形态、自定义 License 都是「关注度高但工程成熟度落后于热度的典型」——属于「看着热闹、真要 fork 之前要再想一下」
- **技术借鉴**：`AppState` 纯函数式 + section-isolated 配置 + manifest-as-data + vendored-deps patch log 这四套组合，可以直接迁移到任何「长跑 TUI + 热配置 + 外部规则适配」的产品
- **生态位**：填补了「终端原生 + agent 感知 + 远端可附着」三个属性的精确交集，这个位置在 2026 年不会被 tmux/vibe-kanban 正面侵蚀
- **趋势判断**：处于增长期（commit 节奏仍在加速、月均 300+），但 v0.7.x 还没跨 1.0 门槛；Agent 状态识别协议（manifest version）一旦稳定化，护城河会显著加深；Windows GA 是下一波用户增长的关键节点

## 风险与不足

- **85.8% 单作者占比**：bus factor = 1，任何 burnout / 转向都会导致项目停滞
- **License 是自定义 Other**：非 OSI 标准，企业采用前需 legal review（理论上比 MIT/Apache 严苛，但合规团队可能拒绝）
- **vendor libghostty-vt**：跟 Zig 上游对齐是结构性负担，1,446 次 commit 的 patch base 是潜在合并地狱
- **fix:feature = 3:1 + Test 仅 1.5%**：典型早中期形态，自动化覆盖不够支撑快速迭代
- **agent 状态检测本质是启发式**：issue #198「status latches on working」揭示某些 case 会卡住，需要各家 agent CLI 维持「逐 agent 适配层」
- **企业 logo 墙「used in the wild」**：JetBrains / Google / NVIDIA / ByteDance 等 logo 在官网首页醒目列出，但缺乏第三方佐证，使用前需自行验证

## 行动建议

- **如果你要用它**：适合「在远端 Mac Mini / VPS / 沙箱 VM 上并行跑 ≥3 个 coding agent，且经常需要从手机 SSH 进去看一眼」的场景。如果你只需要本地单 agent 协作，herdr 的额外复杂度不划算。如果你想要 Web 拖拽 UX，vibe-kanban 更合适
- **如果你要学它**：
  - 必读 `src/app/mod.rs`（4,568 行应用层主入口，看 state/actions/runtime 三层如何分层）
  - 必读 `src/terminal/runtime_registry.rs`（state/runtime 分离最干净的范例）
  - 必读 `src/pane/agent_detection.rs`（pending idle confirmation 状态机）
  - 必读 `src/detect/manifests/claude.toml`（manifest-as-data 范例）
  - 必读 `AGENTS.md`（项目自己写给 AI 协作者的规约）
  - 必读 `vendor/libghostty-vt.patches.md`（vendored deps 治理纪律）
  - 必读 `justfile`（test/lint/ci/windows-lint 任务编排）
- **如果你要 fork 它**：可以改进的方向——
  - 把 license 换成 MIT 或 Apache-2.0 降低企业采用门槛
  - 增加 refactor/test commit 比例（当前 4.5%，目标 ≥25%）以支撑 1.0 跨越
  - 用 git subtree 或 cargo workspace 把 libghostty-vt 拆成独立 crate，方便社区分摊维护
  - 增加 LSP / DAP 适配，让 pane 不仅是 terminal 也是 IDE 视图

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/ogulcancelik/herdr（已收录，12 节结构化分析，最近索引 2026-06-30） |
| Zread.ai | 未收录（HTTP 403，建议人工浏览器复验） |
| 关联论文 | 无（工程实现而非研究项目） |
| 在线 Demo | 无（官网 https://herdr.dev 提供 iPhone SSH 真实截图 + ASCII TUI 截图） |