# 3 个月 17.7K star：约旦团队用 Rust 写了「Agent 操作系统」OpenFang，把企业级安全栈做进了 32MB 单文件

> GitHub: https://github.com/rightnow-ai/openfang

## 一句话总结

OpenFang 是一个用 Rust 写成的「Agent 操作系统」——把 9 种原语（kernel / runtime / memory / channels / skills / hands / security / protocols / desktop）编译成一个 32MB 单二进制，内置 7 个垂直场景「Hand」、40 个 IM 渠道适配器、16 层独立安全模块、同时支持 MCP / A2A / OFP 三种开放协议，是目前唯一走「全功能 OS 范式」、而不是「Python 插件框架范式」的开源 LLM agent 项目。

## 值得关注的理由

- **范式突破**：3.3 个月、20 万行 Rust、17.7K star，把「LLM agent = LLM + tool calling」的「框架范式」推到了「agent = 长程自治进程」的「OS 范式」，对需要 7×24 部署的工程团队有真价值。
- **安全栈一次给齐**：Merkle 哈希链审计、Ed25519 清单签名、WASM 双计费沙箱、taint lattice、capability 继承校验、HMAC-SHA256 mutual auth——这些 Python 系 agent 框架要自己拼，OpenFang 全部内置。
- **生态战略精准**：`openfang-migrate` 专门用来把 OpenClaw 用户虹吸过来，加上 21 个 tool name 映射 + ClawHub 客户端 + FangHub 双市场，是「从竞品抢用户」的产品级打法。

## 项目展示

![OpenFang Logo](https://raw.githubusercontent.com/rightnow-ai/openfang/main/public/assets/openfang-logo.png) — 类型: hero

![OpenFang vs OpenClaw vs ZeroClaw 对比](https://raw.githubusercontent.com/rightnow-ai/openfang/main/public/assets/openfang-vs-claws.png) — 类型: screenshot（性能/形态对比）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/rightnow-ai/openfang |
| Star / Fork | 17,752 / 2,258（watchers 124） |
| 代码行数 | 201,584 行（Rust 80.5% / JSON 6.6% / JS 5.1% / TOML 3.1%） |
| 项目年龄 | 3.3 个月（首次提交 2026-02-26） |
| 开发阶段 | 密集开发（但已显放缓，5-12 后主分支静默） |
| 贡献模式 | 职业项目 + 社区（78 人，主作者 jaberjaber23 占 71%） |
| 热度定位 | 大众热门 · 高速增长（13 天净增 152★） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[优秀] CI[优秀] 错误处理[优秀] |
| License | MIT + Apache 2.0 双协议 |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

OpenFang 来自 **RightNow AI**（约旦，账号 2025-08 创建），是一家做「GPU AI Code Editor」的 AI 基础设施初创。母公司旗下还有 `autokernel`（Python 自动内核生成，1.4K★）、`picolm`（C 推理引擎，1.6K★）、`qwen3.5-triton`（Triton 内核）、`StreamIndex`、`ouroboros` 等横跨 ML 编译器 / 推理运行时 / agent runtime 的硬核底层项目。**整个团队的气质是「OS 工程师 + ML 编译器」的组合**——这解释了为什么 OpenFang 会本能地引入 capability gate、heartbeat、merkle audit、graceful shutdown 这些「非 agent 领域」的设计。

### 问题判断

主流 LLM agent 框架（CrewAI、AutoGen、LangGraph、OpenClaw）本质都是「等你来 prompt 的聊天机器人框架」：Python 包装、依赖繁重、冷启动 2.5–6 秒、内存 180–394 MB，运行时 24/7 自治能力几乎为零；生产部署要的 capability gating、SSRF 防护、审计可追溯、merkle 链、prompt-injection 扫描在 Python 系中要自己拼。**作者把问题重新定义为「一个能在无人值守下持续工作的进程级 OS」**——而这个目标用 Python 根本不可能达到。

### 解法哲学

- **Measured, not marketed**（README 显式声明）——用「实测 vs 对手」的冷启动、内存、bin 大小表格代替营销话术；
- **九种 primitive 编译到一起**（kernel / runtime / memory / channels / wire / skills / hands / api / cli）——不是「插件化」，而是「单体编译为 32MB 二进制」，这是对 LangChain 式「插件森林」的明确反向选择；
- **Security-first**——16 层安全是「独立可测、无单点失败」的设计原则；
- **明确不做什么**：不搞插件市场泛滥、不搞云绑定、不搞 telemetry、不断送 API key 到云。

### 战略意图

- **OpenFang 不是商品**：RightNow 的 GPU Code Editor 才是真正的旗舰产品，OpenFang 是它的 runtime 底座；
- **Open-core 倾向中等偏弱**：MIT 协议、零云依赖、零 telemetry、单二进制 32MB 即可独立运行，与 crewAI/AutoGen（公司主导）形成鲜明对比；
- **生态战略精准**：「承接 OpenClaw 移民」——专门有 `openfang-migrate` 把 YAML/JSON5 → TOML、21 个 tool name 映射、FangHub + ClawHub 双市场——这是有意识地从已停摆 / 质量下滑的 OpenClaw 虹吸用户。

## 核心价值提炼

### 创新之处

1. **Hands 范式：HAND.toml + 内嵌 playbook + manifest signing**
   - 一个 Hand = manifest + 多阶段 system prompt（500+ word 专家程序手册）+ SKILL.md 领域知识 + 工具白名单 + 审批闸门
   - 7 个 Hand 覆盖短视频剪辑、潜在客户挖掘、OSINT 情报、超级预测、深度研究、Twitter 自治、浏览器自动化
   - 新颖度 3/5 · 实用性 5/5 · 可迁移性 4/5

2. **LoopGuard 5 维防护**（开源 LLM agent 框架罕见）
   - Hash 计数 + 全局熔断（30 次总调用直接 kill loop）
   - Outcome-aware 同样 call+result 哈希计数（默认阈值 2 警告、3 block）
   - Ping-pong 检测（A-B-A-B 滑动窗）
   - Poll 工具例外（shell_exec 阈值 ×3）
   - Warning bucket + Backoff 建议（5s→10s→30s→60s 渐进）
   - 新颖度 4/5 · 实用性 5/5 · 可迁移性 5/5

3. **Taint lattice + sink 检查**（学术 lattice 模型工程化到 LLM 工具调用层）
   - 5 个标签（ExternalNetwork / UserInput / Pii / Secret / UntrustedAgent）组成 TaintSet
   - 外部数据进系统自动打 label
   - shell_exec / net_fetch 等 sink 在数据进入时 check_sink，命中就阻断
   - 解决「LLM 工具调用层的 confused deputy 攻击」
   - 新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5

4. **WASM 双计费 + watchdog 沙箱**
   - `consume_fuel(true)` 限指令数 + `epoch_interruption(true)` 限墙钟时间
   - 独立 watchdog 线程超时强制 `increment_epoch()`
   - 任何 guest 写得多畸形，host 一定能在 N 秒内夺回控制权
   - 新颖度 3/5 · 实用性 5/5 · 可迁移性 5/5

5. **Merkle hash-chain 审计 + 可选 SQLite 持久化**
   - `hash = SHA256(seq ‖ ts ‖ agent_id ‖ action ‖ detail ‖ outcome ‖ prev_hash)`
   - 篡改任一条会让所有后续 hash 全部失配
   - 合规场景（金融 / 医疗 / 审计）直接可用
   - 新颖度 2/5（思路来自区块链） · 实用性 5/5 · 可迁移性 5/5

6. **Tauri 2.0 内嵌 kernel + 随机端口**
   - 桌面 app 直接 `cargo build` 后内嵌 `OpenFangKernel`，不用起 daemon
   - 随机挑端口并通过 IPC 命令 `get_port` 告诉 WebView
   - 所有想发桌面 + 不想维护 daemon 的 Rust 团队都能借鉴

### 可复用的模式与技巧

- **KernelHandle trait 解循环依赖**（决策 #1）——任何需要「上层反向调用下层服务」的 Rust 多 crate 项目都适用
- **3-driver 覆盖 N-provider 模式**（LlmDriver trait + Anthropic / Gemini / OpenAI-compat 三个 native driver 覆盖 25+ provider）——任何对接多 API 协议的集成层都能套
- **SQLite + `Arc<Mutex<Connection>>` + `spawn_blocking`**（6 个 store 共享连接）——Rust 桌面 / 边缘应用最经济的持久化方案
- **Capability 继承校验**（spawn 时 `validate_capability_inheritance()`）——任何「用户可定义权限的 agent 系统」都该有
- **Session Repair 7 步修复管线**（orphan / 错位 / 缺失 / duplicate / 空消息的 LLM 消息历史自愈）——所有 LLM chat 应用都需要这层
- **Block-Aware LLM 压缩器**（按 `ContentBlock` 类型分别处理 + 三阶段回退 full→chunked→minimal）——长期会话 LLM 应用的标配
- **OFP 协议 + HMAC-SHA256 + nonce + 常时比较**（用 `subtle` crate 做 `ConstantTimeEq`）——所有需要轻量 P2P 鉴权的项目
- **渠道格式化器 + 限流桥**（`TelegramHTML / SlackMrkdwn / PlainText` 三方言 + per-user rate limit）——机器人矩阵项目

### 关键设计决策

1. **KernelHandle trait 打破循环依赖**
   - 问题：`openfang-runtime` 的工具需要调用 kernel，但 kernel 又依赖 runtime。直接互引会形成循环。
   - 方案：trait 在 runtime 中定义，`OpenFangKernel` 在 kernel crate 中 `impl KernelHandle`。
   - Trade-off：多一层间接 + dyn dispatch
   - 换来：crate 边界清晰、可单独测试、可替换实现（mock kernel 做集成测试）

2. **WASM 双计费（fuel + epoch + watchdog）**
   - 单一 fuel 计量能挡 CPU-bound 死循环，但挡不了 I/O 阻塞、syscall hang、大线性内存分配
   - `consume_fuel` + `epoch_interruption` + 独立 watchdog 线程强制 `increment_epoch()`
   - Trade-off：实现复杂度上升（必须有一个独立 OS 线程做 tick）
   - 换来：「无论 guest 写得多畸形，host 一定能在 N 秒内夺回控制权」

3. **LlmDriver 抽象：3 个 native driver 覆盖 27+ provider**
   - `LlmDriver` trait（`complete` + `stream` + `key_required`）只有 3 个 native 实现——AnthropicDriver / GeminiDriver / OpenAiCompatDriver
   - Trade-off：新 provider 加入要写 config 而非新 driver
   - 换来：driver 数量从 20+ 降到 3，bug 表面积大幅缩小

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | OpenFang | ZeroClaw | OpenClaw | LangGraph | AutoGen |
|------|---------|---------|--------|--------|--------|
| 形态 | Rust 单二进制 OS | Rust 单二进制 | TS Node.js | Python 框架 | Python 框架 |
| 渠道适配器 | 40 | 15 | 多 | 0（用户自己拼） | 0 |
| 内置 Hands | 7 | 0 | 0 | 0 | 0 |
| 安全层数 | 16 | 6 | 3 | 1 | 1 |
| 冷启动 | 180ms | 10ms | 5.98s | N/A（Python） | ~4s |
| 内存 | 40MB | <10MB | ~500MB | 200MB+ | 200MB+ |
| Bin 大小 | 32MB | 8.8MB | N/A（需 Node） | N/A | N/A |
| LLM provider | 27+（3 driver 覆盖） | 28 | 25+ | 任意 | 任意 |
| 协议 | MCP + A2A + OFP | MCP | MCP | MCP | MCP |
| 状态 | 活跃 | 活跃 | 维护 | 活跃 | **已转维护** |
| 路线 | 「Agent OS」 | 极致嵌入式 | Node.js 全栈 | 状态化图编排 | 群聊 agent |

### 差异化护城河

- **技术护城河**：单二进制 + WASM 双计费 + merkle + 16 层安全 + cap inheritance + taint——这套组合在 Rust agent 领域几无对手
- **生态护城河**：40 渠道 + 60 skill + FangHub/ClawHub 双市场 + 7 Hands + MCP/A2A/OpenAI 三大协议——「渠道 + 内容 + 接入」三重生态
- **信任护城河**：MIT 协议、零 telemetry、单文件 32MB、零云依赖——非常适合 on-prem 部署 / 内网 agent 场景
- **迁徙护城河**：`openfang-migrate` 直接接住 OpenClaw + LangChain + AutoGPT 用户

### 竞争风险

- **最可能替代**：crewAI / LangGraph 如果发力 Rust 客户端或企业版；或 Anthropic / Google 自家推出「first-party agent OS」绑定自家模型
- **最可能忽视**：单点性能上输给 ZeroClaw（嵌入式场景，10ms vs 180ms）
- **最可能分裂**：MCP + A2A + OFP 三协议并存，若 MCP 真的成为标准，OFP 可能被边缘化

### 生态定位

**生产级 Rust Agent OS 之王** + **OpenClaw 移民总站**。在「框架 vs OS」光谱上，OpenFang 是目前唯一走「全功能 OS」路线、且真的把 16 层安全做齐的开源项目。

## 套利机会分析

- **信息差**：极小——3 个月 17.7K star、13 天净增 152★、登上 Hacker News 多次，**明显被高估风险**而非被低估。但对中文圈读者来说，深度解构 OpenFang 仍属稀缺内容
- **技术借鉴**：
  - 「Agent OS」框架（kernel / scheduler / audit 心智建模 LLM agent）
  - 安全默认开（capability + taint + merkle + WASM dual-meter 组合）
  - 迁徙战略（`openfang-migrate` + 21 tool 映射 + ClawHub 客户端）
- **生态位**：填补「想 7×24 部署 agent 又不想自己拼安全栈」的开源空白
- **趋势判断**：在增长，符合「agent 从玩具到生产」的技术趋势；比 LangGraph / AutoGen 有后发优势（Rust 单二进制、OS 心智、零云依赖）

## 风险与不足

- **预 1.0，API 仍可能 breaking**：minor 间 schema 变化，依赖前需固定版本
- **单人主导风险**：jaberjaber23 占 71% commit，关键决策单点；5-12 后主分支静默存在「版本封板 / 团队休假 / 内部转向」三种可能
- **OFP 协议是私货**：MCP / A2A 是开放标准，OFP 是自家协议；若 MCP 成为事实标准，OFP 会被边缘化
- **无形式化验证**：安全栈 16 层是「可读的实现」而非「形式化证明」
- **修复 commit 占比偏高**（39.5%）：3.3 个月项目，bug 率仍处于早期迭代期
- **没有 hosted demo / playground**：要部署才能体验，对评估期读者门槛略高

## 行动建议

- **如果你要用它**：
  - 适合场景：需要 7×24 长程 agent、内网 on-prem 部署、对安全 / 合规有要求、想替代 OpenClaw
  - 不适合：想快速搭一个聊天 demo、深度学习 LangChain 已有积累
  - 用前固定版本（pre-1.0），跑 30 天稳定性观察，关注 5-12 后的主分支动向

- **如果你要学它**：
  - 重点关注 `crates/openfang-runtime/src/loop_guard.rs`（5 维防护）
  - `crates/openfang-runtime/src/session_repair.rs`（消息历史自愈）
  - `crates/openfang-types/src/taint.rs`（lattice 模型）
  - `crates/openfang-runtime/src/sandbox.rs`（WASM 双计费）
  - `crates/openfang-kernel/src/capabilities.rs`（capability inheritance）
  - `docs/security.md`（把每个安全系统都标注了源文件 + 关键结构体）

- **如果你要 fork 它**：
  - 把 OFP 协议抽出来做成独立 crate，专注 P2P + HMAC-SHA256 mutual auth
  - 把 Hands 抽出来做成垂直能力包框架（HAND.toml + SKILL.md + 工具白名单 + 审批门）
  - 把 LoopGuard 抽出来做成独立的 LLM-as-loop-controller 防护 crate
  - 把 taint + sink 抽出来做成 LLM agent 通用安全库

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| 在线 Demo | 无（需本地部署，docs/quickstart.md 给出单命令起服务） |
| 关键文档 | [architecture.md](https://github.com/rightnow-ai/openfang/blob/main/docs/architecture.md) · [security.md](https://github.com/rightnow-ai/openfang/blob/main/docs/security.md) · [benchmarks.md](https://github.com/rightnow-ai/openfang/blob/main/docs/benchmarks.md) |
