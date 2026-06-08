# OpenFang：3 个月 17.7k star，专打 OpenClaw 安全痛点的 Rust Agent OS

> GitHub: https://github.com/rightnow-ai/openfang

## 一句话总结

OpenFang 把操作系统的进程治理范式（调度、配额、能力隔离、审计、优雅重启）整套搬到 AI Agent 上，用 20 万行 Rust 编译成单个 ~32MB 二进制，主打「比 OpenClaw 更安全、比 Python 框架更轻、还能 7×24 自主干活」的差异化身位。

## 值得关注的理由

1. **现象级增长 + 真实工程量的罕见组合**：3.3 个月从 0 冲到 17.7k stars，但底下是 14 个 crate、20 万行 Rust、2698 个测试函数的硬工程——既能当传播案例研究，也能当架构学习样本。
2. **「OS 思维套 Agent」是稀缺视角**：作者来自 GPU/系统级背景（RightNow Labs），把 WASM 双计量沙箱、Merkle 审计链、能力继承校验这些系统安全范式迁移到 Agent 域，是应用层框架作者写不出来的。
3. **教科书级的「竞品狙击」打法**：内置 `openfang migrate --from openclaw` 迁移器，把 OpenClaw 的安全争议直接翻译成自己的卖点并接住其迁移流量——是产品定位与增长工程的现成范本。

## 项目展示

![OpenFang Logo](https://raw.githubusercontent.com/RightNow-AI/openfang/main/public/assets/openfang-logo.png)

> OpenFang 项目 Logo。

![OpenFang vs OpenClaw vs ZeroClaw](https://raw.githubusercontent.com/RightNow-AI/openfang/main/public/assets/openfang-vs-claws.png)

> 核心对标定位图：OpenFang 把自己卡在 OpenClaw（TS，~500MB，安全层 3）与 ZeroClaw（Rust，~8.8MB，安全层 6）之间的「均衡点」——~180ms 冷启、~40MB 内存、安全层 16。这张图是其传播主武器。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/rightnow-ai/openfang |
| Star / Fork | 17,755 / 2,258 |
| 代码行数 | 201,495（Rust 80.5%、JSON 6.6%、JS 5.1%、TOML 3.1%） |
| 项目年龄 | 3.3 个月（首次提交 2026-02-26） |
| 开发阶段 | 密集开发（近 90 天 481 commit，3 个月发 100 个版本） |
| 贡献模式 | 单人主导 + 社区补充（核心作者约 48%，78 名提交者） |
| 热度定位 | 大众热门（接住 OpenClaw 安全争议的迁移流量） |
| 质量评级 | 代码「良好」 文档「良好」 测试「优秀」 |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

开发方是组织 **RightNow-AI / RightNow Labs**（产品 rightnowai.co，定位「GPU AI Code Editor」，位置约旦）。组织年轻（账号 0.8 年），但此前已有 GPU/AI 基础设施作品（autokernel、picolm、qwen3.5-triton，均有千级 star）。OpenFang 是其绝对旗舰，17.7k stars 远超组织内任何其它项目。核心作者 jaberjaber23 贡献约 48%，属「核心少数 + 社区」结构——可信度中-高，扣分项是组织年轻、项目 pre-1.0、营销痕迹重。

### 问题判断

作者看到的是 Agent 框架混战中两个被忽视的痛点同时成熟：**资源臃肿**（OpenClaw ~500MB / ~6s 冷启）与**安全失控**（OpenClaw 被 Cisco/Palo Alto 安全团队称为「security nightmare」）。时机选择极其精准——趁安全争议爆发、用户开始迁移的窗口，用 Rust 切「又轻又安全又自治」的身位。这不是凭空创新，而是 dogfooding（团队本就有系统能力）+ 竞品狙击的双驱动。

### 解法哲学

旗帜鲜明的「**大而全 + 一切打进一个二进制**」，与 ZeroClaw 的极简主义正相反。所有东西 `include_str!()` 编译进二进制：60 个 skills、9 个 Hands、SKILL.md 全部内嵌，「No downloading, no pip install, no Docker pull」。明确**不做**的：不依赖外部运行时、不做云 SaaS 锁定（OpenAI 兼容 + 自托管优先）、不让敏感动作无人值守（Browser Hand 强制审批门）。性能 vs 易用上明显偏性能——代价是上手摩擦（#444 配置 bug、测评普遍反映学习曲线陡）。

### 战略意图

典型的 **open-core / 流量入口**布局。OpenFang 是 RightNow 商业产品的开源旗舰与品牌放大器，变现伏笔已埋进代码：FangHub 自有技能市场、企业级路线图（工作队列 `metering.rs`、预算治理、多租户 RBAC `auth.rs`）、`infisical-sync` 等企业凭据集成。核心产品是基础设施（Agent OS），变现大概率走托管 / 企业版 / 市场抽成。

## 核心价值提炼

### 创新之处

1. **WASM 双计量沙箱（fuel + epoch 看门狗线程）**：用 `consume_fuel` 给确定性指令预算 + 独立线程看门狗 `increment_epoch()` 控 wall-clock，CPU 与时间双维度强制可终止不可信代码，trap 时精确区分 `OutOfFuel` 与 `Interrupt`。新颖度 4/5 · 实用性 5/5 · 可迁移性 5/5。
2. **OS 进程模型套到 Agent**：quota / scheduler / supervisor / heartbeat / 能力继承 / 优雅重启恢复，整套操作系统治理范式迁移到 Agent 域。新颖度 4/5 · 实用性 4/5 · 可迁移性 3/5。
3. **Merkle 哈希链审计 + 信息流 taint tracking**：每条审计项含前项哈希（篡改即断链），数据从源到汇带 taint 标签传播。新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5。
4. **三驱动吃 27 家供应商 + 运行时启发式 Router**：只实现 Anthropic / Gemini / OpenAI-compat 三个原生驱动，OpenAI-compat 单驱动靠换 base_url 覆盖 18+ 家；`ModelRouter` 按「token 量×tools 数×代码标记×对话深度」打分，运行时动态选 Simple/Medium/Complex 三档模型 + 自动 fallback。新颖度 3/5 · 实用性 5/5 · 可迁移性 5/5。
5. **畸形工具调用恢复层**：从弱模型吐出的破损输出（XML 参数块、箭头语法、裸 JSON、`--arg` 风格）里抢救工具调用，是「真支持 27 家」的韧性底座。新颖度 3/5 · 实用性 5/5 · 可迁移性 4/5。

### 可复用的模式与技巧

1. **`KernelHandle` trait 注入打破循环依赖**：底层 crate 定义 trait、上层实现、`Arc<dyn Trait>` 回注——解决分层 workspace 中「下层需回调上层」的经典死结，Rust 工作区教科书范式。
2. **trait + 运行时策略链（Router/Fallback）替代编译期绑定**：多后端动态选择/降级的网关型系统通用。
3. **deny-first 能力检查 + 工具列表预过滤**：先鉴权再解析参数、把能力外的工具在喂 LLM 前就剔除，防 LLM 幻觉出越权工具名。
4. **多层 loop 防护**：`LoopGuard`（SHA256 哈希去重 + warn3/block5/熔断30）+ `session_repair`（每轮修复孤儿 ToolResult）+ 续写/深度上限 + 超时 + 结果截断——把 Agent 从 demo 推向「能无人值守长跑」的必备工程。
5. **`Zeroizing<String>` + `Debug` 脱敏管理密钥生命周期**：密钥用完即从内存擦除、日志自动打码，任何持有凭据的服务都该抄。
6. **`Arc<Mutex<Connection>>` + `spawn_blocking` 桥接同步 SQLite 到 async**：不引入 async SQLite 驱动也能线程安全异步访问。

### 关键设计决策

- **`KernelHandle` trait 解循环依赖**：runtime 的「跨 Agent 工具」需调 kernel，而 kernel 依赖 runtime；用底层定义 trait、上层实现注入化解，换来干净单向分层。可迁移性高。
- **能力继承校验防子 Agent 提权**：`validate_capability_inheritance()` 在 spawn 时强制「子能力 ⊆ 父能力」，`CapabilityManager` 用 `DashMap` 无锁并发。安全换极小性能。
- **Hand = 声明式自治能力包**：`HAND.toml`（tools/settings/requirements/dashboard）+ 多阶段 system prompt + SKILL.md + 审批护栏，全 `include_str!` 编译进二进制。牺牲热更新换零依赖、装上即用。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | OpenFang | OpenClaw | ZeroClaw | CrewAI/LangGraph |
|------|----------|----------|----------|------------------|
| 语言 / 体积 | Rust / ~32MB | TS / ~500MB | Rust / ~8.8MB | Python / 解释型 |
| 冷启 / 内存 | ~180ms / 40MB | ~6s / 394MB | ~10ms / 5MB | ~3s / 200MB+ |
| 安全层 | 16（WASM 沙箱+审计链） | 3 | 6 | 基本无 |
| 内置自治 Hands | 7+ | 0 | 0 | 0 |
| Stars | 17.7k | ~347k | 小众 | 数万级 |
| 工具生态 | ~63 内置 | ClawHub 成熟 | 少 | 200+（CrewAI） |

### 差异化护城河

- **技术**：「单二进制 + 16 层安全 + WASM 沙箱 + OS 级治理」的组合在 Rust 阵营目前最全，复刻成本高（20 万行、多 crate 深度耦合的安全/调度子系统）。
- **信任**：可审计 / 可自托管 / Merkle 审计链，正中企业与安全敏感方痛点。
- **渠道**：40 个适配器（尤其飞书 / 钉钉 / 企微等国内企业 IM 是真实现），即时可用的分发优势。

### 竞争风险

最大风险不是技术差距，而是**生态与信任的夹击**：若 OpenClaw 补齐安全层、或 ZeroClaw 加上 Hands，差异化会被两头挤压。更现实的是 pre-1.0 稳定性 / 上手摩擦（#444 配置 bug、文档数字自相矛盾、营销痕迹重）侵蚀早期口碑，以及单一核心作者（~48%）+ 年轻组织的可持续性存疑。工具生态 63 vs 200+ 是中期短板。

### 生态定位

「OpenClaw 难民的安全替代 + Rust 阵营的全功能 Agent OS 头部」，卡在 ZeroClaw（极简）与 CrewAI（生态）之间的均衡身位，靠迁移器把 OpenClaw 流量导入自有 FangHub 生态。

## 套利机会分析

- **信息差**：项目曝光已饱和（全网充斥 SEO 软文），**不属于被低估的潜力股**——star 含金量需对营销打折。真正的信息差在「它的工程实现」而非「它的存在」：多数人只看了对标图，没读过它的 loop 防护与沙箱代码。
- **技术借鉴**：WASM 双计量沙箱、deny-first 能力模型、LoopGuard、密钥 `Zeroizing` 这几套可直接迁移到自己的插件 / Agent 系统，价值远超「再造一个 Agent 框架」。
- **生态位**：填补了「Rust 原生 + 全功能 + 可审计」的 Agent 运行时空白；国内企业 IM 渠道（飞书全双工等）是它意外的本地化优势。
- **趋势判断**：增长仍在加速但已踩在 OpenClaw 浪潮的尾部，后发优势主要来自「安全」叙事；需警惕浪潮退去后能否靠产品力留存。

## 风险与不足

- **测试充分但工程整洁度有缺口**：存在严重 god-file（routes.rs 12975 行、kernel.rs 9415 行、main.rs 7478 行、agent_loop.rs 5493 行），crate 内模块化不足。
- **文档数字自相矛盾且部分过时**：工具数 23/41/53（实测 63）、驱动「3 native」实为 8、端点 76 vs 140+、版本 0.6.9 vs README banner 0.5.10、License README 称 MIT 实为 Apache OR MIT 双授权、SECURITY.md 还写「支持 0.3.x」。营销腔重，需读者自行交叉验证。
- **pre-1.0 不稳定**：自称 feature-complete 但 minor 版间可能 breaking；上手摩擦明显（最高热度 issue 是配置 bug）。
- **可持续性**：组织年轻（0.8 年）、核心作者贡献近半，社区虽已参与但仍高度依赖单一核心。

## 行动建议

- **如果你要用它**：适合需要「自托管 + 可审计 + 常驻自治」的团队，尤其重视安全合规、或要接国内企业 IM 的场景。要嵌进既有 Python 数据/ML 流水线选 CrewAI/LangGraph；要极限轻量嵌入式选 ZeroClaw；要从 OpenClaw 迁移则它的内置迁移器成本极低。注意当前 pre-1.0，生产部署前自测配置链路。
- **如果你要学它**：重点读 `crates/openfang-runtime/src/`（agent_loop.rs 的 loop 防护与畸形调用恢复、sandbox 的双计量）、`crates/openfang-kernel/src/`（调度/能力/RBAC）、`crates/openfang-types/src/`（taint/签名/能力枚举）。这三处是「OS 思维套 Agent」的精华。
- **如果你要 fork 它**：最该改的是把 god-file 按职责拆分、对齐文档与代码的真实数字、补充供应商抽象层（早期 #116/#40 暴露的灵活性缺口）。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/RightNow-AI/openfang（已收录） |
| Zread.ai | 探测返回 403，未能确认收录 |
| 关联论文 | 无（arXiv 无匹配） |
| 在线 Demo | 官网 https://www.openfang.sh/ + Product Hunt 收录；无公开 playground |
