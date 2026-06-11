# Kakao 工程师的 7 阶段 Agent Harness：2.5 个月拿下 6.8K stars 的 Claude Code 插件真相

> GitHub: https://github.com/revfactory/harness

## 一句话总结

`revfactory/harness` 是一个把自己定位为「L3 Meta-Factory / 团队架构工厂」的 Claude Code 插件元技能（meta-skill）：用户用自然语言说「build a harness for X」，它就按 7 阶段工作流（审计 → 领域分析 → 团队架构 → 代理定义 → 技能生成 → 集成 → 验证 → 演化）落地出 `.claude/agents/`、`.claude/skills/`、`CLAUDE.md` 指针 + 编排技能，并把分布式系统的 6 种架构模式（Pipeline / Fan-out / Expert Pool / Producer-Reviewer / Supervisor / Hierarchical）重新编码为 LLM 团队的可复用模板。

## 值得关注的理由

1. **重新定义"插件"的边界**：其他 Claude Code 插件是「单一技能」或「单一团队」，harness 是「工厂」—— 一个插件产出多个插件文件。这套元层抽象在 Anthropic 官方 plugin marketplace 生态里几乎独一份。
2. **方法论比代码更值钱**：仓库真实可执行代码只有 427 行 HTML + 819 行内嵌 JS；99% 价值在 5110 行 markdown 规范里。如果你正在设计 LLM agent 团队，QA Agent 的 7 类 boundary-mismatch 案例（`references/qa-agent-guide.md`）和 trigger 评估方法论（`references/skill-testing-guide.md`）比任何框架代码都更稀缺。
3. **作者亲自下场做 A/B**：单作者 6.8K stars 不是营销结果——同一作者还有 `harness-100`（944 stars, 1,808 个生产级 harness）作为数据集支撑，且自出版论文 `Harness: Structured Pre-Configuration for Enhancing LLM Code Agent Output Quality`，是目前少数有量化自证的 agent 框架。

## 项目展示

![Harness banner](https://raw.githubusercontent.com/revfactory/harness/main/harness_banner.png)
*项目品牌 banner：标语 "Agent Team & Skill Architect for Claude Code"。*

![Harness team diagram](https://raw.githubusercontent.com/revfactory/harness/main/harness_team.png)
*核心架构示意：7 阶段工作流 + 6 种分布式模式 + 团队拓扑。*

![Harness social card](https://raw.githubusercontent.com/revfactory/harness/main/harness_social.png)
*OpenGraph 分享卡，2.5MB，Twitter/LinkedIn 预览专用。*

![Star History Chart](https://api.star-history.com/chart?repos=revfactory/harness&type=date&legend=top-left)
*Star 增长曲线：2.5 个月冲到 6.8K，启动期与 Anthropic / Awesome Claude Code 推广节奏强相关。*

未发现 README / 官网 / 作者演讲中的视频 demo。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/revfactory/harness |
| Star / Fork / Watcher | 6,802 / 932 / 41 |
| 主语言占比 | HTML 100%（本质是 markdown 规范 + manifest 的"插件包"，可执行代码仅 427 行 HTML + 819 行内嵌 JS） |
| 项目年龄 | 2.5 个月（2026-03-26 → 2026-06-10） |
| Commits / 30 天 | 45 / 16 |
| 平均节奏 | ~5 commits/周（最近 30 天约 3.2/周） |
| 开发阶段 | 早期爆发后转入维护，54 天无新版本号（最新 1.2.1 / 2026-04-18） |
| 贡献模式 | 单作者主导（revfactory/Minho Hwang 同人 = 86.7% commits）+ 6 名外部贡献者已合 7 个 PR |
| 热度定位 | 大众热门（Awesome Claude Code 收录；首周即上榜） |
| Bus Factor | 1（86.7% 单人占比） |
| License | Apache-2.0 |
| 质量评级 | 代码 C（无 CI / 无测试 / 0 git tag）/ 文档 A（3 语 README + 6 份深度 reference）/ 治理 B+（CONTRIBUTING + 4 issue 模板 + PR 模板完整） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Minho Hwang（@revfactory）**，韩国 Kakao Corp. 工程师，GitHub 13.5 年老号，284 个公开仓库，605 followers 但 only 9 following——这是典型的「输出者」而非「社交型」账户。

他不是新入场者：同一作者在 6.8K stars 的 harness 之外，还维护着 `harness-100`（944 stars, 1,808 个生产级 harness 模板，覆盖 10 个领域 × EN/KO）、`claude-code-mastering`（774 stars, 韩文 Claude Code 教程）、`claude-code-master`（183 stars, MDX 书籍）、`claude-code-harness`（106 stars, A/B 实验基底）等 12 个 harness 变体。这说明 **harness 是个人长期品牌而非一次性产物**。

公司 bio 只写 `@kakao`，没有具体业务单元。从 issue #8 引用 NVIDIA Nemotron-Personas-Korea 数据集、PR #9/#10 Kakao 内部风格、quickstart.md 提到的"企业部署"措辞推断：他大概率在 Kakao 的 AI/Platform 组织，专注开发者生产力工具。

### 问题判断

2026 年 Q1 出现一个真实痛点：Claude Code 推出 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 标志，开放 `TeamCreate` / `SendMessage` / `TaskCreate` 三个原语后，社区有大量「怎么设计一个 agent 团队」的零散讨论，但**没有方法论**。多数教程停留在「这是 team 模式」「这是 sub-agent 模式」的概念层，不告诉用户：

- 一个具体问题应该选哪种协调拓扑？
- 团队成员怎么切分（按专业？按并行？按上下文？）？
- 怎么验证生成的团队真比单 agent 好？
- 团队上线后怎么演化？

Minho 看到了这个空白，并亲自填了一份 5110 行 markdown 的答案。

### 解法哲学

两个明确选择定义了 harness 的灵魂：

**选择 1：把 6 种分布式系统模式重新编码为 LLM 团队模板**。Pipeline / Fan-out-Fan-in / Expert Pool / Producer-Reviewer / Supervisor / Hierarchical Delegation 不是新概念，但每一项都标注「팀 모드 적합성」—— 哪种模式适合哪种场景。这是少有的把学术 taxonomy 落到工程决策树的做法。

**选择 2：CLAUDE.md 是指针，不是注册表**。v1.2.0 之后明确放弃把"agent 列表、skill 列表、目录结构、执行规则"全塞进 CLAUDE.md，只留触发规则 + 变更日志。源信息住在 `.claude/agents/` / `.claude/skills/` / 编排技能里。这是反 over-engineering 的清醒决定，但代价是单文件入口轻量。

**明确不做什么**：

- 没有内置 CI / 测试 / git tag / linter（作者亲自在 `_workspace/release/audit-2026-04-18.md` 自承 Trust Signals 3/10，但选择不立即修）
- 不内置成本控制文档（quickstart.md:99 留白）
- 不开源 A/B 复现脚本（论文数据集未随仓库）

### 战略意图

短期目标是「L3 Meta-Factory」的赛道卡位——README 里和 5 个邻居（Archon / meta-harness / ECC / wshobson / Claude Code 官方）做共存表，主动划分 L1/L2/L3 层级，是这个赛道里罕见的「边界清晰」姿态。中期目标是跨运行时复制（Codex 已有 92 stars 的 `SaehwanPark/meta-harness` 端口作为验证）。

长期看，harness-100 的 944 stars 暗示作者想把 harness 做成「harness engineering」的事实标准，类似当年 Rails 之于 web 框架。但目前 Kakao 内部采纳、官方 plugin marketplace 收录等关键信号都未公开。

## 核心价值提炼

### 创新之处

1. **「工厂」作为插件的输出物**（最高新颖度）。其他 Claude Code 插件是单 skill 或单 team，harness 是一次性产出「多文件目录布局」的元层抽象。README:32 明确"team-architecture factory"自我定位。这等于在 plugin marketplace 生态里重新发明了「framework vs library」的层级。
2. **6 模式 taxonomy + 每模式标注 team-mode 适合度**。`references/agent-design-patterns.md:83-160` 不只是列模式，每项配「정의 / 사용 시점 / 예시 팀 / 팀 모드 적합성 / 알려진 실패 모드」。这种"模式 + 决策指南"组合在 LLM 团队设计领域极少。
3. **CLAUDE.md pointer policy**（v1.2.0 设计变更）。明确放弃把 agent/skill 列表写进 CLAUDE.md，单源真相留在文件系统，是反 over-engineering 的清醒决定，并写入了文档作为可追溯的设计哲学。
4. **Phase0 审计 + Phase7 演化循环**。0 阶段读 `.claude/{agents,skills}` 和 `CLAUDE.md` 自动分流到 NEW / EXTEND / OPERATE 三种模式；7 阶段处理真实反馈并自动触发（重复 2 次即追加）。这是把"插件"从一次性产出升级为长生命周期工具的关键设计，多数框架完全没做这一层。
5. **QA Agent boundary-mismatch 七分类法**。`references/qa-agent-guide.md` 列出 7 类从 SatangSlide 生产 bug 里挖出的边界失配（API shape ↔ hook type / file path ↔ href / 状态转移 ↔ 代码等），每类带真实 JS/TS 代码示例，比任何 LLM 评测榜单都更接地气。
6. **Bilingual 触发短语内嵌到 frontmatter**。SKILL.md:3 同时写「하네스 구성해줘」+「build a harness for X」+「ハーネスを構成して」，并对韩文 tokenizer 误路由做 FAQ 防御。

### 可复用的模式与技巧

| 模式 | 文件:行 | 可迁移场景 |
|---|---|---|
| 推送型描述模板（"bad → good"对照）+ anti-trigger 反向说明 | `references/skill-writing-guide.md:36-48` | 任何写 SKILL.md 的插件作者 |
| 三层 progressive disclosure（metadata ~100 词 / SKILL.md <500 行 / references 不限，>300 行需 TOC） | SKILL.md:152-163 + skill-writing-guide.md:168-184 | 任何技能目录 |
| should / should-NOT 触发词评估法（应该触发 8-10 + 边缘不应触发 8-10） | `references/skill-testing-guide.md:237-255` | 任何技能 QA 流程 |
| Plugin/Marketplace 双 manifest 模式 + 版本号优先级文档化 | `.claude-plugin/{plugin,marketplace}.json` + `_workspace/release/audit-2026-04-18.md` | 任何用 Claude Code 插件系统的项目 |
| 7 阶段工作流（audit → analyze → arch → define → skill → integrate → validate → evolve） | SKILL.md:18-426 | 任何想搭元层技能的插件作者 |
| Orchestrator 技能包 3 模板（team / sub / hybrid）+ 数据传递协议选型表 | `references/orchestrator-template.md:11-292` | 任何需要协调多 agent 的项目 |

### 关键设计决策

**决策 1：仓库本质是 markdown 规范集，不是代码库**。
- Pros: 极低发布摩擦（45 commits 出 5 个版本），专注方法论纯度
- Cons: 与 `+60% 量化自证`叙事矛盾——读者期待看到评测脚本，看到的却是「author-measured A/B, third-party replications pending」

**决策 2：所有 agent 锁定 opus 模型**。
- Pros: 质量上限确定（SKILL.md:93, agent-design-patterns.md:213）
- Cons: 成本——quickstart.md:97-99 估算单复杂任务 50K-200K token × opus × 5+ 并行 agent；目前无成本控制文档（quickstart.md:99 留白「forthcoming」）

**决策 3：把 GTM 启动产出放进 `_workspace/` 公开仓库**。
- Pros: 透明度高，launch strategy 是可追溯的工程记录
- Cons: `_workspace/04_strategist_launch_plan.md` 详细到 KOL outreach list 与 6K+ stars trending 目标，等于把剧本公开给任何想复制的竞争者

**决策 4：单点作者 + 承诺的 SLA**。
- Pros: 设计一致性；CONTRIBUTING.md 给 72h PR / 48h issue / 24h Claude Code 重大故障响应
- Cons: 86.7% commits 来自 1 人；如果作者请假一周，SLA 立刻失约；版本节奏已 54 天未更新就印证了这点

**决策 5：跨运行时抽象，但当前 Claude Code 原语硬编码**。
- Pros: 6 种模式本身与运行时无关（Codex 已有 92 stars 端口验证）
- Cons: orchestrator-template.md:60-76 直接引用 `TeamCreate` / `SendMessage` / `TaskCreate`；移植到 Cursor/OpenCode 需要重新翻译这些原语——非零工程

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | revfactory/harness | affaan-m/ECC | coleam00/Archon | wshobson/agents | SaehwanPark/meta-harness |
|---|---|---|---|---|---|
| Stars | 6,802 | 213,243 | 22,343 | 36,628 | 92 |
| Fork | 932 | 32,700 | 3,367 | 3,968 | 少量 |
| 定位层级 | L3 Meta-Factory | L1 跨运行时算子 | L3 Runtime-Config Factory | L3 部件目录 | L3 Codex 端口 |
| 核心输出 | `.claude/agents/` + `.claude/skills/` + CLAUDE.md 指针 | 统一行为预算 + 12+ 跨运行时适配 | YAML 工作流引擎 | 84 plugins / 192 agents / 156 skills 单一 markdown 源 | Codex 版元技能 |
| 协调拓扑 taxonomy | 6 种分布式系统模式 + team-mode 适合度标注 | 单 ops 层 + instincts 体系 | 状态机 workflow | 无（catalog） | 复用 6 模式 |
| 量化自证 | +60% / 15-15 / -32% n=15 作者自测 | 无公开评测 | 无公开评测 | 无公开评测 | 沿用 harness 自证 |
| 自维护机制 | Phase7 演化循环 + 反馈触发器 | 否 | 否 | 否 | 否 |
| 跨运行时 | 是（设计层）/ 否（实现层 Claude Code 原语硬编码） | 是（12+ 运行时已实现） | 否（Claude Code 为主） | 是（多 harness 已实现） | 否（Codex） |
| 主要语言 | HTML（实为 markdown 规范） | 多 | TypeScript | Markdown | Python |

### 差异化护城河

- **唯一把"插件"重新定义为"工厂"**：其他 L3 项目要么是部件目录（wshobson），要么是工作流引擎（Archon），要么是运行时算子（ECC）。harness 占了「团队架构师」这个空白格，护城河来自方法论沉淀而非代码。
- **唯一提供量化自证 + 学术论文**：作者自出版 `Hwang, M. (2026)` 论文，公开 A/B 数据（虽然 n=15 且未独立复现），并在 README 用"同句配对"规则披露 caveat（README:259, 270-277），这个透明度在当前 agent 框架里罕见。
- **唯一做 Phase0 审计 + Phase7 演化**：把插件生命周期从"一次性产出"延长到"长期运维"，对应 Kakao 内部长生命周期工具的实操痛点。
- **唯一公开 GTM 启动剧本**：`_workspace/` 包含 auditor / scout / strategist 四角色产出，等于把"如何 launch 一个 AI 工具"作为方法论副产品公开。

### 竞争风险

1. **最大风险：Anthropic 官方 plugin marketplace 推出对等能力**。当前 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 是实验标志，Anthropic 一旦把团队设计纳入官方 skill，harness 的 L3 卡位就被吃掉。`docs/experimental-dependency.md` 已为这个场景（A 标志 GA / B Managed Agents GA / C 重大破坏变更）做了 24/48/72h SLA 承诺。
2. **次大风险：被 ECC 这类 L1 跨运行时巨头向上吞并**。ECC 213K stars、12+ 运行时适配、12 种语言支持，一旦决定加 L3 layer，harness 的设计方法论会被 5× 量级以上的用户采纳吃掉。
3. **最小风险：Codex / Cursor 等运行时团队官方做对等 plugin**。已有先兆（`SaehwanPark/meta-harness` 92 stars），但还没到"官方"层级。

### 生态定位

**L3 Meta-Factory 层的开创者**——尽管这个层级是他自己造的词，但确实填补了"agent 团队设计方法论 + 模板化生成"这片空白。`README:32-40` + `.claude-plugin/plugin.json` description 一起把定位讲清楚了。

整体生态图谱：

- **L1 跨运行时算子**：affaan-m/ECC、hkfire/cofy 等
- **L2 跨 harness 工作流**：affaan-m/ECC 的 workflow 层
- **L3 Meta-Factory**：revfactory/harness（本项目）、coleam00/Archon（runtime-config 路线）、SaehwanPark/meta-harness（Codex 端口）
- **L4 部件目录**：wshobson/agents、shanraisshan/claude-code-best-practice、ykdojo/claude-code-tips
- **L5 单领域垂直**：op7418/guizang-ppt-skill、hesreallyhim/awesome-claude-code

harness 在 L3 中的核心差异：**6 模式 taxonomy 是 IP**。ECC 没有这套、Archon 没有这套、wshobson 也没有。一旦这套 taxonomy 被社区广泛采用，作者就有了事实标准的话语权。

## 套利机会分析

- **信息差**：6.8K stars 在 agent harness 圈子算高知名度，但在更广义的 LLM engineering 圈里仍被严重低估。同时 `harness-100`（944 stars, 1,808 文件数据集）这个姊妹项目基本没人讨论。两者之间存在「主项目明星 + 数据集项目隐形」的信息差。
- **技术借鉴**：QA agent boundary-mismatch 七分类法（`references/qa-agent-guide.md`）+ should/should-NOT 触发词评估法（`references/skill-testing-guide.md`）是任何做 multi-agent 系统的项目都该复用的两件武器。
- **生态位**：填补「团队架构师」空白——大多数 agent 框架给你 agent，但没人告诉你怎么把一群 agent 组合成高效团队。如果你是 Kakao 这种大公司内部的 AI Platform 团队，可以直接 fork harness 改造成内部团队设计工具。
- **趋势判断**：Agent 团队协作是 2026 H1 的明确趋势（Claude Code experimental flag + Anthropic GA + 各家复制）。harness 的 L3 卡位如果能在 6 个月内拿到 15K stars，就能在 Anthropic 官方 L3 plugin 出现前确立事实标准。

## 风险与不足

1. **量化自证未被独立复现**。"+60% / 15-15 / -32% / n=15" 是作者自己跑出来的，且实验基底 `claude-code-harness`（106 stars）也没公开评测脚本。商业化前需独立复现。
2. **单作者风险 + 版本节奏崩塌**。86.7% commits 单人占比，CONTRIBUTING.md 承诺「every 2 weeks」biweekly，实际最新版本 1.2.1 / 2026-04-18 已 54 天没更新，且 0 git tag。下游用户无法 `pin` 到具体版本，长期可持续性存疑。
3. **运维自动化几乎为零**。0 CI / 0 测试 / 0 linter / 0 formatter。`_workspace/release/audit-2026-04-18.md` 自承发生过 README 1.0.1 / marketplace 1.1.0 / plugin 1.2.0 三方版本号漂移事故，目前 plugin.json 还停在 1.2.0 而 CHANGELOG 已写到 1.2.1——人工修复未自动化。
4. **成本控制缺位**。所有 agent 锁 opus + 5+ 并行 + 50K-200K token/任务的估算 = 单次复杂任务可能 $5-$20，下游企业用户难以做预算。quickstart.md:99 留白「cost-controls.md forthcoming」但未兑现。
5. **README 与 SKILL.md 文档轻微漂移**。对外宣传「6-phase workflow」实则 SKILL.md 定义了 7 phase（Phase0 审计 + Phase7 演化），读者数 phase 数量时会困惑。
6. **`_workspace/` 公开泄露 launch strategy**。6K+ stars trending 目标、KOL outreach list、4 角色 GTM 启动脚本全部在公开仓库，对竞争者等于免费 playbook。

## 行动建议

- **如果你要用它**：适合「需要为重复出现的领域问题设计 agent 团队」的场景——尤其是有 5+ 并行子任务、任务有清晰阶段切分、对质量上限敏感的工作流。不适合一次性脚本 / 简单 RAG / 单 agent 就能解决的轻量场景。对比 Archon 选 harness：如果你想要「agent 团队设计方法论 + 可复用模式」选 harness；如果你想要「状态机工作流 + 强可观测」选 Archon。
- **如果你要学它**：按这个顺序读 3 个文件——
  1. `references/qa-agent-guide.md`（228 行）—— 7 类 boundary-mismatch 是整个仓库信号密度最高的资产
  2. `skills/harness/SKILL.md` 的 Phase 选择矩阵（lines 29-33）+ CLAUDE.md 指针政策（lines 258-300）
  3. `references/agent-design-patterns.md` 的 6 模式 + team-mode 适合度标注（lines 83-160）
- **如果你要 fork 它**：最高杠杆的改进是 **cut version drift + ship git tags + 加 CI 自动校验 plugin.json ↔ marketplace.json ↔ CHANGELOG ↔ README badge 的版本号一致性**（约 20 行 GitHub Action + jq）。`_workspace/release/audit-2026-04-18.md` 记录了真实三方漂移事故，目前是手动修复，未来必然复发。这一个 PR 就能把 harness 的"production readiness"从 C 提到 B+。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | [Harness: Structured Pre-Configuration for Enhancing LLM Code Agent Output Quality](https://github.com/revfactory/claude-code-harness)（作者自出版 Hwang, M. 2026，未独立复现） |
| 在线 Demo | https://revfactory.github.io/harness/（landing page，无交互 demo） |
| 姊妹数据集 | https://github.com/revfactory/harness-100（944 stars, 1,808 个生产级 harness 模板） |
| 作者论文 | https://github.com/revfactory/claude-code-harness（106 stars，A/B 实验基底） |
| 跨运行时端口 | https://github.com/SaehwanPark/meta-harness（92 stars, Codex 版） |