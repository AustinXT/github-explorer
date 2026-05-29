## 动机与定位

- **要解决的问题**: 终端 AI 编程助手（coding agent CLI）存在启动慢（Node.js/Python 运行时 500ms+）、内存占用大（Electron/V8 数 GB）、流式输出不稳定、扩展系统不安全等问题。pi_agent_rust 旨在提供一个从零开始的 Rust 重写方案，以单二进制文件、<100ms 启动、50MB 以下空闲内存、安全的扩展运行时为核心目标。

- **为什么现有方案不够**: 原始项目 Pi Agent（TypeScript/Node.js by Mario Zechner）虽然功能完善，但受限于 Node.js 运行时的固有开销。作者在 1M/5M 级 session 的端到端基准测试中证实：Rust 版本比 Node 快 4-5x，比 Bun 快 2-3x；内存占用降低 8-13x。此外，原版扩展系统缺乏多层安全防线（capability gating + exec mediation + trust lifecycle），这在自主 agent 场景下是重大隐患。

- **目标用户**: 使用终端开发的程序员，尤其是已在使用 Pi Agent / OpenClaw 的用户群体；对性能和安全有高要求的 AI agent 基础设施开发者；边缘计算/嵌入式设备（Raspberry Pi）上运行 AI agent 的探索者。

## 作者视角

### 问题发现
Jeff Emanuel 的问题来源是 **深度 dogfooding**。他本人是 agentic_coding_flywheel_setup（1,291 stars）的作者，日常大量使用 AI coding agent。在长 session 场景下反复遭遇 Node.js 版本的性能瓶颈——5M token 级 session 的恢复/追加流程在原版需要近 6 秒，这对交互式工作流是不可接受的。

**时机选择**：Rust 2024 edition（edition = "2024"，需 rustc 1.85+）刚发布，异步生态（asupersync 替代 tokio 用于结构化并发）趋于成熟；同时 agentic coding 从 2024-2025 进入爆发期，安全的自主 agent 成为刚需而非 nice-to-have。

### 解法哲学
- **性能优先但不牺牲安全**：`#![forbid(unsafe_code)]` 从项目第一天起就写死在 lib.rs 和 main.rs 里。release profile 开 LTO、单 codegen-unit、strip，CI 有 22MB 的二进制体积预算门禁。jemalloc 作为默认 allocator（feature gate），针对分配密集路径优化。
- **深度安全而非表面合规**：extension 安全不是简单的 "allow/deny capability"，而是一个四层防线——(1) capability gating (2) exec mediation with AST-level command analysis (3) trust lifecycle state machine (quarantined -> restricted -> trusted) (4) tamper-evident runtime risk ledger。这在开源 agent 工具中是独一无二的深度。
- **不做的事情比做的事情更说明价值观**：明确不移植 Web UI、Slack bot、GPU pods、npm 包系统。Unix 哲学——专注做好终端 CLI 这一件事。
- **开放生态策略**：MIT + Rider 许可；提供稳定的 `sdk` 模块（lib.rs 中明确标注 API stability policy）；支持 JS/WASM 两种扩展运行时。

### 背景知识迁移
Jeff Emanuel 的金融/对冲基金背景带来了几个独特的 insight：

1. **高频交易中的确定性调度思想** → hostcall 调度器。Scheduler 模块实现了严格的不变量（I1-I5：单 macrotask/tick、microtask 耗尽、stable timer ordering、无重入、total order），这是从金融系统的确定性重放需求中迁移来的。
2. **AMAC（Asynchronous Memory Access Chaining）** → hostcall 批量执行器。这是一个来自数据库/HPC 领域的技术（论文级），通过交错多个独立 hostcall 状态机来隐藏 LLC miss 延迟，根据 stall rate 动态切换批处理/顺序模式。
3. **S3-FIFO 缓存策略** → hostcall 队列准入。将 web cache 研究（SOSP'23 的 S3-FIFO 论文）中的三队列准入策略（small/main/ghost）应用于 hostcall 优先级管理。
4. **从 beads_rust (747 stars) 中的结构化并发经验** → asupersync 框架的设计——自建 async runtime 而非直接用 tokio，以获得对 extension JS runtime 事件循环的完全确定性控制。

### 战略图景
pi_agent_rust 是 Jeff Emanuel "agentic coding flywheel" 生态的**核心运行时引擎**：
- `asupersync`（自建 async runtime）→ 底层基础设施
- `rich_rust`（Rich 的 Rust 移植）→ 终端渲染层
- `charmed_rust`（bubbletea/lipgloss 的 Rust 移植）→ TUI 框架
- `sqlmodel_rust`（ORM）→ 数据持久化
- `beads_rust`（issue tracking）→ 开发工具链
- `pi_agent_rust` → 上层产品（消费以上所有库）

开源策略是 **genuinely open**（MIT license + rider，无 enterprise 版本迹象），但自建整个依赖栈的做法本身就是护城河——同时控制 runtime + 渲染 + TUI + ORM 的能力使得深度优化成为可能，而竞品只能在第三方依赖之上做有限调优。

## 架构与设计决策

### 目录结构概览
项目约 55.6 万行 Rust 源码（src/），加 26.5 万行集成测试（tests/）。分层清晰：

```
src/
├── main.rs / lib.rs        # 入口 + 模块声明 + jemalloc 全局分配器
├── cli.rs / config.rs      # CLI 解析 + 多层配置合并
├── provider.rs + providers/ # LLM 后端抽象层（9 个 provider 实现）
├── agent.rs / agent_cx.rs   # Agent 循环 + 消息队列 + 工具执行编排
├── session.rs / session_*   # JSONL 会话持久化 + SQLite 索引 + V2 分段日志
├── tools.rs                 # 8 个内置工具（read/bash/edit/write/grep/find/ls/hashline_edit）
├── extensions*.rs           # 扩展系统核心（50K 行！最大模块）
├── extensions_js.rs         # QuickJS 运行时桥接 + TypeScript 转译
├── hostcall_*.rs            # 5 个 hostcall 子系统（queue/rewrite/superinstructions/trace_jit/amac/io_uring_lane）
├── scheduler.rs             # 确定性事件循环调度器
├── sse.rs                   # SSE 流解析器（带 event type interning）
├── sdk.rs                   # 稳定的库 API 表面
└── interactive/             # TUI 模块（bubbletea 架构）
```

### 关键设计决策

1. **决策**: 自建 async runtime（asupersync）替代 tokio
   - 问题: 需要对 JS extension 的事件循环行为获得确定性控制；tokio 的 work-stealing scheduler 无法保证 hostcall 的全序执行
   - 方案: 自建 `asupersync` crate，包含结构化并发原语、内置 HTTP/TLS/SQLite、deterministic timer driver；通过 `Cx` context 传播取消/预算信号
   - Trade-off: 自建 runtime 意味着需要维护更多代码、放弃 tokio 生态的兼容性，但换来了对调度行为的完全控制和可重放的测试能力
   - 可迁移性: 低（与项目深度耦合）

2. **决策**: 三层 hostcall 执行优化管线（Interpreter → Superinstruction → Trace-JIT）
   - 问题: Extension hostcall 是热路径，频繁的模式匹配（match dispatch）有可观的调度开销
   - 方案: Tier-0 顺序 dispatch → Tier-1 superinstruction 融合（识别重复 opcode 窗口，编译为融合计划）→ Tier-2 trace-JIT（将稳定的 superinstruction 编译为带 guard 的预编译分发表）。每层有独立的热度阈值和去优化回退路径
   - Trade-off: 显著增加代码复杂度（4 个 hostcall_*.rs 模块），但对高频 extension 场景提供阶梯式性能提升
   - 可迁移性: 高——这个三级执行管线的设计模式适用于任何有 "频繁调度同类操作" 的系统（插件系统、RPC 框架、数据库查询执行器）

3. **决策**: 两阶段 exec 安全防线 + AST 级命令分析
   - 问题: Extension 执行 shell 命令是最危险的能力；简单的字符串黑名单容易被 heredoc/反引号/管道绕过
   - 方案: (1) Capability gate 检查 exec 权限 → (2) `classify_dangerous_command()` 使用 ast-grep 进行 AST 级别的命令分析，识别 12+ 种危险命令类别（RecursiveDelete, DeviceWrite, ForkBomb, DiskWipe, ReverseShell, PipeToShell 等）→ (3) DCG/heredoc 包装器检测（防止将危险命令隐藏在多行 heredoc 中）
   - Trade-off: AST 解析比正则匹配慢，但安全性质的差异是根本性的（正则无法处理 shell 语法的嵌套和转义）
   - 可迁移性: 高——任何需要安全执行用户/AI 提供的 shell 命令的系统都可以采用这种分层模式

4. **决策**: Session Store V2 分段追加日志 + 偏移索引
   - 问题: 大型 session（5M token）的完整 JSONL 文件在重新打开时需要全量解析，导致数秒延迟
   - 方案: V2 存储引入分段写入（SegmentFrame）+ 偏移索引（OffsetIndexEntry with CRC32C），支持 O(index + tail) 的快速恢复；每个 frame 带 payload_sha256 用于完整性校验；genesis chain hash 用于链式审计
   - Trade-off: 增加了存储复杂度和双写维护成本，但将 5M session 的恢复时间从 396ms（Node）/155ms（Bun）降到 58ms
   - 可迁移性: 高——分段追加日志 + 偏移索引是通用的持久化模式

5. **决策**: SSE event type interning + scanned_len 优化
   - 问题: LLM streaming API 每个 SSE event 都会产生 event type 字符串分配；每次 feed 都需要从头扫描 buffer 寻找换行符
   - 方案: `intern_event_type()` 将已知的 30+ 种 event type（Anthropic/OpenAI/Gemini 的标准事件名）映射到 `Cow::Borrowed` 静态字符串，消除逐事件分配；`scanned_len` 字段记录已扫描的位置，避免重复扫描 buffer 前部
   - Trade-off: 微小的代码复杂度增加，换来流式解析路径上的零分配和线性扫描
   - 可迁移性: 高——任何处理 SSE/streaming 的系统都可以采用 string interning

6. **决策**: Extension trust lifecycle 状态机
   - 问题: 二元的 "允许/拒绝" 不足以处理 extension 信任随时间变化的场景（初次安装、发现异常、恢复信任）
   - 方案: 三态状态机 Quarantined → Restricted → Trusted，每次转换需要 operator acknowledgment + 原因记录 + audit event 产生。支持即时 demotion（kill switch）和分级 promotion
   - Trade-off: 比简单 allow/deny 模型复杂得多，但提供了企业级的 extension 治理能力
   - 可迁移性: 中——适用于任何有 plugin/extension 生态的产品

7. **决策**: `#![forbid(unsafe_code)]` + clippy pedantic + nursery 级别 lint
   - 问题: 安全关键型应用需要最大化编译期保证
   - 方案: 从 lib.rs 和 main.rs 同时禁止 unsafe code；Cargo.toml 中启用 `pedantic` 和 `nursery` 级别的 clippy lint 作为 warning
   - Trade-off: 某些性能优化不可行（如 SIMD、自定义内存布局），但通过 jemalloc + 算法优化弥补；少量第三方 crate 内部可能有 unsafe，但项目代码本身保持 zero unsafe
   - 可迁移性: 高——任何 Rust 项目都应考虑这种 lint 策略

## 创新点

1. **三级 Hostcall 执行管线（Interpreter → Superinstruction → Trace-JIT）**
   - 描述: 将编译器优化中的超级指令融合（superinstruction）和 trace-JIT 概念应用到 extension hostcall dispatch 中。Tier-0 是标准 match dispatch；Tier-1 通过滑动窗口频率分析识别重复 opcode 序列，编译为融合计划；Tier-2 将稳定计划编译为带 guard 检查的预编译分发表，guard 失败时自动去优化回退
   - 新颖度: 5/5 | 实用性: 4/5 | 可迁移性: 4/5
   - 适用场景: 任何有高频同类调度的系统——plugin runtime, RPC server, database query executor, game engine scripting host

2. **AMAC 风格的交错批量 Hostcall 执行器**
   - 描述: 借鉴 HPC/数据库领域的 AMAC（Asynchronous Memory Access Chaining）技术，当 hostcall 工作集超过 LLC 时，通过交错多个独立状态机来隐藏 cache miss 延迟。内置 stall 检测（100us 阈值）+ EMA 平滑 + 动态切换阈值
   - 新颖度: 5/5 | 实用性: 3/5 | 可迁移性: 3/5
   - 适用场景: 内存密集型批处理系统、数据库扫描引擎、大规模 RPC 服务

3. **S3-FIFO 准入策略用于 Hostcall 队列**
   - 描述: 将 SOSP'23 论文中的 S3-FIFO 缓存准入策略（small/main/ghost 三队列）应用到 hostcall 队列管理中，提供公平性保证和 per-owner 配额管理，带完整的 fairness instability 检测和自动 fallback
   - 新颖度: 4/5 | 实用性: 3/5 | 可迁移性: 4/5
   - 适用场景: 任何需要公平调度 + 频率感知准入的队列系统

4. **BRAVO 风格的 Contention 自适应策略**
   - 描述: Hostcall 队列的元数据锁使用 BRAVO（Biased Read-Write Locking）风格的自适应策略——通过滑动窗口观察读写比、P95 等待时间和写超时率，自动在 Balanced/ReadBiased/WriterRecovery 三种模式间切换，带 rollback 防护
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 4/5
   - 适用场景: 任何读写混合的并发数据结构

5. **AST 级 Shell 命令危险性分类**
   - 描述: 使用 ast-grep（tree-sitter 系列解析器）对 extension 要执行的 shell 命令进行 AST 级分析，识别 12+ 种危险类别；特别能检测隐藏在 heredoc/反引号/管道中的危险命令，这是简单正则/字符串匹配根本无法做到的
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 5/5
   - 适用场景: 任何需要安全执行 AI 生成 shell 命令的系统（coding agent, CI/CD, chatbot）

6. **确定性重放追踪束（Replay Trace Bundle）**
   - 描述: Extension runtime 的所有事件（调度/入队/策略决策/取消/重试/完成/失败）按照严格的 logical clock + canonical rank 排序记录，支持事后确定性重放。这使得并发环境下的 race condition 和尾部异常可以离线复现和比较
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 4/5
   - 适用场景: 分布式系统调试、金融交易审计、安全事件取证

7. **QuickJS + Wasmtime 双运行时 Extension Host**
   - 描述: 同时支持 JS（via QuickJS with SWC TypeScript transpilation）和 WASM（via wasmtime component model）两种 extension 运行时。QuickJS 桥接采用 Promise-based hostcall 架构，WASM host 包含完整的 Emscripten polyfill（虚拟文件系统、内存页限制等）
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 3/5
   - 适用场景: 任何需要同时支持 JS 和 WASM 插件的应用

## 可复用模式

1. **三级执行管线模式**: Interpreter → Fusion → JIT with guard-based deopt — 适用场景: 高频调度系统的渐进式优化
2. **分段追加日志 + 偏移索引**: 对大型 append-only 数据的快速随机访问和恢复 — 适用场景: 日志系统、事件溯源、session 持久化
3. **Capability Gate + Mediation + Trust Lifecycle 三层安全模型**: 从权限检查到命令级分析到运行时信任管理的分层防线 — 适用场景: 任何 plugin/extension 系统
4. **SSE Event Type Interning**: 将有限域的字符串映射到 `Cow::Borrowed` 避免逐事件堆分配 — 适用场景: 高吞吐流式协议解析
5. **Shadow Dual Execution + Automatic Backoff**: 采样执行两条路径（fast/compat），比较结果一致性，在偏差时自动退回安全路径 — 适用场景: 渐进式优化部署、灰度策略
6. **Canonical JSON Hashing (直接 feed hasher)**: 排序 key + 直接向 SHA-256 hasher 写入，跳过中间 String 分配 — 适用场景: 任何需要确定性 JSON 签名的场景
7. **VCR 录制/重放测试基础设施**: 录制真实 HTTP streaming 响应并确定性重放，用于 provider 测试 — 适用场景: 依赖外部 API 的系统测试
8. **Flake Classifier + CI 重试策略**: 将测试失败分类为 transient（可自动重试）和 deterministic（需修复），避免 CI 噪声 — 适用场景: 大规模 CI/CD 系统

## 竞品交叉分析

### vs oh-my-pi (2,109 stars, TypeScript)
- **pi_agent_rust 更好**: 性能（4-5x faster, 8-13x less memory）；安全模型深度（AST-level exec mediation, trust lifecycle）；单二进制分发无需 Node.js runtime
- **竞品更好**: 生态成熟度（更多现有 extension）；TypeScript 写 extension 的开发者友好性（虽然 pi_agent_rust 也支持 JS extension）；社区规模和文档丰富度
- **不同目标**: oh-my-pi 是 Pi 生态的增强套件（更多便利功能），pi_agent_rust 是底层引擎的重写（更好的性能和安全基础）
- **用户迁移成本**: 中等。Session 格式兼容（JSONL v3），但 extension 可能需要适配新的 hostcall ABI 和安全策略

### vs shai (589 stars, Rust, OVH)
- **pi_agent_rust 更好**: 功能范围（完整的 extension system, session branching, multi-provider, TUI）；安全模型深度；性能基准透明度
- **竞品更好**: 企业背景（OVH 支持）意味着潜在的长期维护保证；更简单的代码库意味着更低的学习曲线
- **不同目标**: shai 专注于终端编程辅助的窄场景，pi_agent_rust 是完整的 coding agent 平台
- **用户迁移成本**: 高。完全不同的架构、配置和 session 格式

### vs OpenClaw (430K 行代码)
- **pi_agent_rust 更好**: 性能（明确的端到端基准测试证据）；内存占用；启动速度；extension 安全模型；代码体量更可控
- **竞品更好**: 开箱即用的用户体验；更大的用户社区和生态；更成熟的产品打磨
- **不同目标**: OpenClaw 是面向终端用户的产品壳（最大化易用性），pi_agent_rust 是面向性能和安全的引擎层（最大化可靠性）
- **用户迁移成本**: 低-中。pi_agent_rust 的 README 明确以 "Pi/OpenClaw 用户" 为目标受众，Session 格式兼容

### 综合竞争结论
- **差异化护城河**: 技术护城河最深——自建 5 层依赖栈（runtime + TUI framework + renderer + ORM + issue tracker）使得性能优化可以跨层进行，竞品无法复制。安全模型的深度（三级执行管线 + AST 命令分析 + trust lifecycle + 确定性重放）也是显著的技术壁垒
- **竞争风险**: 最大风险来自 OpenClaw / Pi 原版社区的"足够好"效应——如果大多数用户的 session 不超过 100K token，性能差距不够痛。另一个风险是单人维护的 55 万行 Rust 代码的长期可持续性
- **生态定位**: 作为 Pi 生态的"高性能安全引擎层"，类似于 Node.js 生态中 Bun/Deno 对 Node 的关系——同协议但不同运行时实现。长期可能成为需要企业级安全保证的 coding agent 部署的首选 runtime

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | 良好 | `#![forbid(unsafe_code)]` + clippy pedantic/nursery；但 1,885 个 unwrap + 4,651 个 expect 数量偏高（56 万行代码中），部分可进一步收敛为 Result 传播 |
| 文档质量 | 优秀 | 98 万行 markdown 文档（包括生成的 JSON contract 文档）；README 16.4 万行极为详尽；有 PROPOSED_ARCHITECTURE.md、CONFORMANCE.md、BENCHMARKS.md、160+ 篇 docs/ 目录文档 |
| 测试覆盖 | 充分 | 263 个集成测试文件（26.5 万行）；7 个 benchmark suite；8 个 fuzz target；proptest property-based 测试；VCR 录制/重放测试基础设施 |
| CI/CD | 完善 | 6 个 GitHub Actions 工作流（ci.yml 2004 行！bench.yml, conformance.yml, fuzz.yml, publish.yml, release.yml）；跨平台矩阵；perf gate；binary size budget |
| 错误处理 | 良好 | thiserror（结构化错误）+ anyhow（边界层）双层策略；error_hints 模块提供用户友好的错误建议；但 unwrap/expect 使用可进一步改善 |

### 质量检查清单
- [x] 有测试（单元/集成/E2E/Fuzz/Property-based）
- [x] 有 CI/CD 配置（6 个工作流，含性能门禁和体积预算）
- [x] 有文档（极为丰富：PROPOSED_ARCHITECTURE、CONFORMANCE、BENCHMARKS、160+ docs/）
- [x] 错误处理规范（thiserror + anyhow 双层策略）
- [x] 有 linter / formatter 配置（clippy pedantic + nursery）
- [x] 有 CHANGELOG
- [x] 有 LICENSE（MIT + Rider）
- [ ] 有示例代码 / examples 目录（无独立 examples 目录，但 README 中有丰富示例）
- [x] 依赖版本锁定（Cargo.lock 已提交）
