# 5 个月冲 21 万 star 的 Everything Claude Code：全家桶 harness，真功夫在 Rust 控制面

> GitHub: https://github.com/affaan-m/everything-claude-code

## 一句话总结

Everything Claude Code（ECC）是 affaan-m 把自己 10 个月重度使用 Claude Code 的配置沉淀产品化的「AI 编码 agent meta-harness 全家桶」——skills + instincts + memory + security + 一个 Rust 写的会话控制面，跨 Claude Code/Codex/Cursor 等 10+ 工具。它 2026-01 开源、5 个月冲到 21 万 star，是现象级爆款；但热度里有真实工程，也有赛道泡沫——真正值钱的是那个 Rust 控制面与确定性安全护栏，而非 261 个 skill 的内容堆叠。

## 值得关注的理由

1. **现象级增长 + 必须诚实看待的双面性**：2026-01-18 创建，9 天 3.2 万 star、3 月 50K→100K 仅 3 周、6 月初 21 万。作者有硬背书（用纯 Claude Code 8 小时建出 zenith.chat 拿下 Anthropic × Forum Ventures 黑客松冠军）。但同赛道集体爆款（superpowers 17.7 万、awesome-claude-code 3.7 万），社区对「过度工程」分歧明显——这是「真实需求 + 病毒式 hype 叠加放大」的产物。
2. **真正的技术实质藏在 Rust 控制面 ecc2/**：它不是又一套脚本，而是真会 spawn `claude/codex/opencode` 子进程、做 worktree 隔离编排、daemon 心跳/崩溃恢复、cron 调度、TUI kanban、SQLite 知识图谱的 agent 会话管理器——这是 ECC 区别于所有 markdown-only 竞品的实质。
3. **几个小而精的真创新值得抄**：确定性（零 LLM）工具调用风险评分护栏、项目作用域 + 置信度的 Instincts 持续学习（git-remote 哈希隔离防跨项目污染）、consolidated dispatcher + 自定位 plugin-root 的 hook 工程——对任何 Claude Code 插件作者或 agent 工具开发者都有直接借鉴价值。

## 项目展示

![ECC Hero](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/assets/hero.png)

ECC —— 面向 agentic 工作的 harness-native operator system。

![ECC 速查指南](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/assets/images/guides/shorthand-guide.png)

ECC 速查指南：skills / commands / 工作流概览。

![AgentShield 安全](https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/assets/images/security/security-guide-header.png)

Everything Agentic Security（AgentShield）：扫描 agent 配置的 prompt injection / 配置漂移。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/affaan-m/everything-claude-code（官网 https://ecc.tools） |
| Star / Fork | 210,163 / 32,227（Watcher 1,061、open issues 18、open PR 21；注：README 徽章显示 182K，与 API 口径略有出入） |
| 代码行数 | 160,727 行（JS 56.4% 但**主要是 tests 6.3 万 + scripts 4.4 万**，非业务应用；Rust 29.7% / 4.8 万行是真核心 ecc2/；Python 4.4% + Shell 2.1%；**comment 比仅 1.19%**，内容/配置堆叠型） |
| 内容资产 | 261 个 SKILL.md + 64 个 agents + 84 个 commands + 20 语言 rules + 11 语言文档（但仅约 13 个 skill 带 reference/scripts 的真 progressive disclosure，余多为扁平 prompt） |
| 项目年龄 | 2026-01-18 创建，不到 5 个月（最近提交 2026-06-07，极活跃） |
| 开发阶段 | 极密集开发 / 新项目爆发期（2054 commit、近 4 周 500、日均约 14 commit） |
| 贡献模式 | 单作者高强度主导 + 社区 PR（约 218 贡献者，affaan-m 占 ~70%/1431 commit） |
| 热度定位 | 现象级（GitHub 史上最高星之一，含明显泡沫成分） |
| 质量评级 | 代码[良，Rust 核心] 文档[优（量）/营销味] 测试[结构良/深度存疑] |

> 数据说明：本仓库 depth1 浅克隆，提交历史用 gh api 实采补正（facts 因浅克隆失真已弃用）；代码行数 tokei 实测可信。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

affaan-m（Affaan Mustafa），连续创业者（Itô 预测市场 @Ito-Markets），3.3 年 GitHub 账号、6959 followers。可信度高：2025-09 携队友在 Anthropic × Forum Ventures 黑客松（Cerebral Valley NYC，100+ 队）用纯 Claude Code 8 小时建出 zenith.chat 夺冠，赢 1.5 万美元 API credit。ECC 即其「10 个月 Claude Code 日常配置沉淀」的开源化——非空降营销号，有真实工程履历。但项目高度依赖单人（affaan-m 主导 70%、周更、多 harness 适配全压一人），巴士因子是隐忧。

### 问题判断

裸 Claude Code 在长期高强度真实工程中暴露的系统性缺陷：缺纪律（不写测试、改配置绕 lint）、缺记忆（跨会话遗忘项目知识）、缺安全（CLAUDE.md/hooks/MCP 可被 prompt injection / 配置漂移攻击）、缺编排（多 agent/worktree 并行靠手工）、缺可观测（不知道 token/成本/上下文耗尽）。ECC 把这些痛点固化成一套「harness-native operator system」。仓库里甚至有针对它自己的 inherited instincts（conventional commits、~70 字符 commit message 等），即作者把自己仓库的隐性规范也产品化了。

### 解法哲学

选择「大而全的 meta-harness」而非单点——核心论点是「agentic work 中持久的部分应集中在一个仓库，harness 只在边缘适配」。`SKILL.md` 被定为「最可移植单元」（YAML frontmatter + when-to-use + 通用示例，不嵌 secret），rules/hooks/MCP 按 harness 做薄适配层。**这与 obra/superpowers 的极简 markdown 哲学是明确对立的赌注**：ECC 赌「覆盖广度 + 系统化」，superpowers 赌「少即是多 + 官方背书」。这个赌注也正是「过度工程」争议的来源。

### 战略意图

典型 open-core：MIT 永久开源的工具层做获客与品牌，ECC Pro（$19/seat）+ GitHub App + Sponsors 变现。安全是商业切入点——AgentShield（**独立仓库** + npm 包 `ecc-agentshield`）做「扫你的 agent 配置」这个新风险面；控制面 ecc2/（ECC 2.0 alpha）把开源用户沉淀为「需要编排/可观测的重度用户」再向 SaaS 漏斗输送。需诚实指出：**关键价值（AgentShield 102 规则核心、GitHub App、SaaS）要么在仓库之外、要么还是 alpha**，开源主仓的含金量被「内容堆叠」稀释。

## 核心价值提炼

### 创新之处（诚实标注真创新 vs 包装）

1. **跨 harness agent 会话控制面 ecc2/（真创新）** — Rust 写，真正 spawn `claude/codex/opencode/gemini` 子进程（`build_agent_command()` 按 HarnessKind 编译成真实 CLI）并统一编排：worktree 隔离 + daemon 心跳/崩溃恢复 + cron 调度 + 远程派发 + TUI kanban + SQLite 状态机（16+ 表，含 entities/relations/observations 三表的上下文知识图谱 + 会话间消息总线）。新颖度 4/5、实用性 3/5（alpha、单机、巴士因子高）、可迁移性 3/5。
2. **确定性工具调用风险评分护栏（真创新，小而精）** — `observability/mod.rs::compute_risk()` 零 LLM：base tool risk + 文件敏感度（.env/.pem）+ blast radius（`rm -rf`、force-push）+ 不可逆性，clamp 到 [0,1] 后映射 Allow/Review/RequireConfirmation/Block，理由可解释、有单测。新颖度 3/5、实用性 4/5、可迁移性 5/5。
3. **项目作用域 + 置信度的 Instincts 持续学习（真创新，数据模型有想法）** — `observe.sh` 把工具调用按 git-remote 哈希分目录写 observations（先擦敏感信息），5 层 guard 防止观测自己（self-loop），节流通知后台 Haiku 把观测蒸馏成带置信度（0.3–0.9）的原子 instinct，TTL 30 天裁剪，`evolve` 聚类成 skill/`promote` 跨 2+ 项目升全局。新颖度 4/5、实用性 3/5、可迁移性 4/5。
4. **AgentShield prompt-injection / 配置漂移扫描（真创新，但核心在外部仓）** — 扫 CLAUDE.md/settings.json/mcp.json/hooks/agents，102 规则 + Opus 三 agent（红队/蓝队/审计）+ auto-fix + GitHub Action。本仓库只有 `skills/security-scan/SKILL.md` 调 `npx ecc-agentshield` 的壳。新颖度 4/5、实用性 4/5、可迁移性 2/5。
5. **consolidated dispatcher + 自定位 plugin-root hook（真工程创新但实现丑陋）** — hook 合并为单 dispatcher，每条命令内嵌 `node -e` 按候选路径探测解析 `CLAUDE_PLUGIN_ROOT`，配 `ECC_HOOK_PROFILE=minimal/standard/strict` 运行时分级；覆盖全生命周期（质量门、config 保护、GateGuard fact-force、cost/context 监控）。代价是内联 JS 复制十余处、几乎不可读。新颖度 3/5、实用性 4/5、可迁移性 4/5。

> 诚实分层：**ecc2 控制面 + 三个小护栏/学习模块是真材实料**；而 261 skills + 64 agents 的内容体系大部分是扁平 prompt 堆叠（新颖度 2/5），真价值集中在少数带 scripts/reference 的 skill。

### 可复用的模式与技巧

1. **专线 DB writer（mpsc + oneshot ack）**：单独 OS 线程独占 SQLite 连接，async 侧发命令并 await ack，规避跨 async 任务连接争用——高并发 async 写嵌入式 DB。
2. **确定性多因子风险评分**：base + 敏感度 + blast radius + 不可逆性 → clamp → 阈值分级 + 理由——任意需要可解释护栏的动作系统。
3. **自定位 plugin root bootstrap**：按候选路径探测 sentinel 文件解析安装根——被装到多种路径的 CLI 插件 hook。
4. **项目作用域哈希隔离 + global 提升**：git remote 哈希分目录、跨 2+ 项目才升全局——多项目记忆/学习防污染。
5. **5 层自激励防护**：防止观测系统观测自己——任何会被自己触发的监听/学习 hook。
6. **manifest 驱动的多目标选择性安装器**（profiles/modules/components + dry-run + state store 增量）——多平台分发的资产包。
7. **agent 输出 confidence-based filtering + pre-report gate**（>80% 才报、合并同类、跳过未改代码）——降低 LLM reviewer 噪声。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | ECC | obra/superpowers | SuperClaude | claude-flow | anthropics/skills |
|------|-----|------------------|-------------|-------------|-------------------|
| 体量 | 210K★ | ~177K★ | 中 | 中 | 官方 |
| 哲学 | 大而全 harness | 极简 markdown | persona 命令 | 多 agent 编排 | 官方基线 |
| 控制面/编排 | ✅ Rust ecc2(alpha) | ❌ | ❌ | ✅ hive-mind | ❌ |
| 安全层 | ✅ AgentShield(外部仓) | ❌ | ❌ | ❌ | ❌ |
| 官方背书 | ❌ | ✅ 入选官方插件市场 | ❌ | ❌ | ✅ 第一方 |
| 商业化 | ✅ open-core SaaS | ❌ | ❌ | 部分 | ❌ |

### 差异化护城河

唯一同时具备 (a) 真·跨 harness 可移植抽象 + (b) Rust 会话控制面 ecc2（spawn 子进程 + worktree + daemon + SQLite 知识图谱）+ (c) 确定性安全护栏与 AgentShield 安全切入 + (d) 项目作用域 instincts 学习 + (e) open-core SaaS 闭环 的全家桶。竞品各占其一，没有第二家全占。

### 竞争风险

① **单作者巴士因子**（ecc2 + 周更 + 多 harness 适配全压一人）；② **「过度工程」声誉风险**（261 skills 噪声、hook 内联 JS、安装复杂）削弱「可信精选」心智，正面撞 superpowers 的官方背书；③ **关键价值要么 alpha 要么在仓库之外**（AgentShield 在外部 repo、GitHub App/SaaS 在外、ecc2 仍 alpha），开源仓本体含金量被内容堆叠稀释；④ **harness 厂商内化风险**——官方 hooks/skills 演进会从下方蚕食这类上层增强。

### 生态定位

agent harness 增强层的「重型全家桶 + 安全/控制面商业化」一极，与 superpowers/官方 skills 的「极简可信」一极形成两端。适合愿意投入、需要编排/安全/可观测的重度 operator；不适合想要轻量可信精选的用户。

## 套利机会分析

- **信息差**：这是当下 Claude Code 增强生态最大流量入口，话题度满分，但**纯吹增长会踩坑**。真正有信息增量的角度是「拆穿 21 万 star 的虚实」——区分真材实料的 Rust 控制面/护栏/instincts 与泡沫化的内容堆叠，以及「全家桶 vs 极简」两条路线之争。这对做 Claude Code/agent 工具的读者（如本站受众）尤其有价值。
- **技术借鉴**：「专线 DB writer」「确定性风险评分护栏」「自定位 plugin-root bootstrap」「项目作用域哈希隔离学习」「5 层自激励防护」「manifest 多目标安装器」六项可直接抄进任何 agent 工具/Claude Code 插件。
- **生态位**：填补「重型 agent harness + 安全 + 控制面商业化」的空白。
- **趋势判断**：踩在 Claude Code/AI agent 工程化的风口，但要警惕赛道 hype 退潮、官方能力内化、单作者可持续性。

## 风险与不足

- **过度工程争议（中-高，诚实）**：单 `observe.sh` 499 行、hook bootstrap 复制十余遍、261 skills 含明显包装/堆叠、安装路径/profile/manifest 高复杂度。需区分「内容层堆叠」（确有泡沫）与「控制面工程」（真材实料）。
- **注释/可读性差**：comment 比 1.19%，hooks.json 每条命令内联一坨重复不可读的 node bootstrap。
- **关键价值不全在本仓库**：AgentShield 102 规则核心在外部 repo、GitHub App/SaaS 在外、ecc2 控制面仍 alpha（rc.1 才本地可编译、单机）。
- **测试深度存疑**：JS 6.3 万行测试多为脚本/校验器测试，核心 prompt 内容无法自动验证（Rust 核心有 551 个真测试函数，相对扎实）。
- **巴士因子**：单作者主导控制面 + 周更 + 多 harness 适配，长期可持续性是隐忧。

## 行动建议

- **如果你要用它**：你是重度日用 Claude Code/AI agent 的工程师、需要纪律/记忆/安全/编排——可选择性安装（`npx ecc` 按 `--profile/--skills/--without` 挑模块，别整套吞下）。想要轻量可信精选、低维护，选 obra/superpowers（有官方背书）；只要官方基线用 anthropics/skills；要多 agent 编排看 claude-flow。
- **如果你要学它**：跳过 261 个 skill，直接读 Rust 控制面——`ecc2/src/session/manager.rs`（spawn 子进程编排）、`runtime.rs`（子进程捕获 + 专线 DbWriter）、`store.rs`（SQLite 知识图谱 schema）、`observability/mod.rs`（确定性风险评分）；学习系统看 `skills/continuous-learning-v2/`（observe.sh + instinct-cli.py）；hook 工程看 `hooks/hooks.json`；跨 harness 看 `docs/architecture/cross-harness.md` + `scripts/install-apply.js`。
- **如果你要 fork 它**：最有价值的可复用件是 ecc2 的子模式（subprocess 编排 + 专线 DB writer + 风险评分护栏）和 instincts 数据模型；但要清楚 AgentShield/SaaS 是闭源/外部，fork 主仓得不到商业闭环，且要承接「过度工程 + 单作者」的维护包袱。

### 知识入口

| 资源 | 链接 |
|------|------|
| 官网/产品 | https://ecc.tools（Free 安装、Selective install builder、AgentShield audit、Skill catalog；GitHub App 一键装） |
| 外部深度视角 | [Inside the 82K-Star Agent Harness That's Dividing the Developer Community (Medium)](https://medium.com/@tentenco/everything-claude-code-inside-the-82k-star-agent-harness-thats-dividing-the-developer-community-4fe54feccbc1)（争议视角）；[ECC hits 163K stars (Augment Code)](https://www.augmentcode.com/learn/everything-claude-code-hits-163k-stars)（偏正面） |
| AgentShield | github.com/affaan-m/agentshield + npm `ecc-agentshield`（安全扫描核心，独立仓库） |
| DeepWiki / Zread.ai | 未确认收录 |
