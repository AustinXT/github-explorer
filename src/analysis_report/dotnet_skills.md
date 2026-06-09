# 微软给 .NET 写了 98 个官方技能：实测旗舰却没让 Opus 更强

> GitHub: https://github.com/dotnet/skills

## 一句话总结
微软 .NET 团队亲自下场、给 AI 编码代理写的 98 个官方 Agent Skills 合集——工程化程度堪称业界标杆（近 1:1 评测覆盖 + C# 校验器），但实测旗舰技能对强模型的行为增益约等于零，真正值得抄的是它那套「技能即被测代码」的评测基建。

## 值得关注的理由
1. **唯一的官方 first-party .NET 技能集**：不是技术人转策展，而是「同一拨造 .NET 平台的工程师，把内部生产已验证的工作流固化成 agent 可发现的 skill」，对一堆社区 .NET skill 形成权威碾压
2. **业界罕见的评测工程化**：98 个技能配 95 份 `eval.yaml`（近 1:1 断言覆盖）+ 独立 C# `skill-validator` + 覆盖率脚本 + 5 条专用 CI——把「技能」当「需要回归测试的代码」来管，这是真正稀缺的可复用资产
3. **一个诚实的反差实测**：旗舰技能 `migrate-nullable-references` 客观结构分 61/100、写得很完整，但 `with_skill` vs `without_skill` 的行为 **delta ≈ 0**——Opus 本就会 nullable 迁移，这类「mastery 象限」技能对前沿模型边际收益有限

## 项目展示

```
dotnet/skills/                       # 官方 plugin marketplace（.claude-plugin/marketplace.json，13 plugin）
├── plugins/
│   ├── dotnet-test/skills/          # 25 个技能（最大）
│   ├── dotnet-msbuild/skills/       # 18
│   ├── dotnet-blazor/skills/        # 9
│   ├── dotnet-maui/skills/          # 8
│   ├── dotnet-upgrade/skills/       #  6 ← 旗舰 migrate-nullable-references 所在
│   └── …（dotnet-diag/ai/aspnet/data/nuget…）
├── tests/                           # 95 份 eval.yaml，与 plugins/ 镜像，逐技能断言
├── eng/skill-validator/             # 独立 C# 项目：SKILL.md 合规校验
├── eng/skill-coverage/              # PowerShell：技能覆盖率
└── .github/workflows/               # 30 个 workflow，含 evaluation/skill-check/skill-validator
```

*这个仓库的「主语言」被 GitHub 标成 C# 96.4%，但那是 `skill-validator` + 评测脚手架；技能本体是 98 份以 prose 为主的 SKILL.md。*

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/dotnet/skills |
| Star / Fork | 3,306 / 245 |
| 代码行数 | 98 个技能（13 plugin）/ 32 带 reference·4 带 scripts / 实测旗舰 1 个 |
| 项目年龄 | 4 个月（2026-02 ~ 2026-06） |
| 开发阶段 | 活跃高频建设期（近 30 天 50 commits，工作日为主，weekend 0%） |
| 贡献模式 | 核心少数 + 社区（微软 .NET 团队，Top2 约 70%，含 bot） |
| 热度定位 | 中等热度（官方背书的 4 个月新仓） |
| 质量评级 | 质量[中] 旗舰实测 delta[≈0] 裁决[weak] 象限[mastery] |
| 许可证 | MIT |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
维护者是 GitHub 组织 `dotnet`（**微软官方 .NET 平台团队，非个人**）：22,675 followers，top 仓库全是 .NET 顶级项目（maui 23k / roslyn 20k / runtime 18k）。这不是「技术人转内容策展」，而是**框架作者亲自写 AI 用知识包**。贡献分布是典型微软团队制——Amaury Levé 42%、Jan Krivanek 28%，加 dependabot/Copilot bot 与多名 .NET 团队成员，由 Tim Heuer 在 .NET 官博正式发布。

### 问题判断
AI 编码代理（Claude Code / Copilot / Cursor）写 .NET 代码时，常给出**过时或非地道**的写法。微软判断：与其等模型自己学会，不如把「官方生产已验证」的工作流喂给代理，确保 .NET 在 AI-coding 时代不被边缘化。

### 解法哲学
- **官方权威 + 精选**，对标社区的「数量 + 众包」（如 VoltAgent 那种上千条聚合）
- **按 .NET 工作负载切 plugin**（test / msbuild / blazor / maui / diag / upgrade…），13 个 plugin 即 13 条产品线
- **技能即被测代码**：每个技能配 `eval.yaml` 断言，随 CI 回归——这是把内部工程纪律搬到了技能治理上
- **跨代理**：声称构建于 agentskills.io 开放标准，在 Claude Code / Copilot CLI / VS 2026 / Cursor 通用

### 战略意图
这是微软「让 AI 编码代理吃官方领域知识」统一战略簇的一员（与 `microsoft/win-dev-skills`、`microsoft/skills`、`power-platform-skills` 并列）。意图是 **AI 编码生态卡位 + 平台护城河**，非商业导流——用官方指导守住 .NET 在代理时代的开发者心智。

## 技能清单总览
98 个真实技能（排除 2 个 fixture/template），归入 13 个 plugin + 另含 17 个 agent。结构成熟度：**32/98（33%）带 `references/` 深度资料，仅 4/98（4%）带可执行 `scripts/`，65% 为纯 SKILL.md 单文件**；正文中位 10.6KB、区间 2.7–39.4KB，没有占位式短技能，策展密度高。导航不靠 README（仅 5.1KB 无 TOC），靠 `marketplace.json` + 目录结构。旗舰 = `migrate-nullable-references`（dotnet-upgrade，35.9KB，唯一同时带 reference + scripts），备选 `coverage-analysis`（dotnet-test，29.1KB）。

## 抽样精读：旗舰技能实测（migrate-nullable-references）

按「每篇报告固定只对 1 个最有代表性的技能真跑 eval」的规则，对旗舰跑了一遍 `with_skill` vs `without_skill` 的行为对比（3 个用例，含 1 个边界用例）。

- **2×2 象限**：`mastery`（模型能力强 93 + 人类经验好 91，confidence 0.92）——即「这是个把强模型已具备的能力写成规范」的技能。
- **客观结构分**：61/100。亮点 content 25/25（内容详尽），短板 examples 6/25、trust 5/15（缺可跑示例与权威背书标注）。
- **行为 delta（核心）**：**with 1.0 vs without 1.0 → delta ≈ 0.00**。三个用例（启用 NRT 并修 CS8618/CS8602、标注公共 API 可空契约、对「已迁移项目」的边界处理）里，**装不装这个技能，Opus 的输出都满足全部断言**——5 条 expectation 全部 `always-pass`，无一条体现出技能独有贡献。
- **裁决：`weak`**。诚实说：旗舰技能写得规范，但对 Opus 这种前沿模型几乎没让它做得更好——因为 nullable 迁移、可空注解这些正是强模型的基本功。
- **诚实补注**：本次只跑 3 个用例、断言由分析方设定，「全 always-pass」也可能意味着用例区分度不够；但「强模型已达标」这一信号与 mastery 分类一致，方向可信。对**较弱的模型 / 不熟 .NET 的团队**，这类技能的价值会显著更高——它是一致性保险，不是给满血模型的能力增量。

## 核心价值提炼

### 创新之处
1. **「技能即被测代码」的评测基建**（新颖度 5/5 × 实用性 5/5）：95 份 `eval.yaml` 对 98 技能近 1:1 断言覆盖 + 独立 C# `skill-validator` + 覆盖率脚本 + 5 条专用 CI（evaluation / skill-check / skill-coverage / skill-validator / nightly）。绝大多数 skills 合集是「写完即终」，这里把技能当需要回归测试的工程资产管——**这才是整个仓库最稀缺、最该抄的东西**。
2. **agentic 运营自动化**（新颖度 4/5 × 实用性 3/5）：30 个 workflow 含大量 gh-aw 智能体流（issue-triage / pr-triage / devops-health / 恶意 PR 扫描），治理由 agent 驱动。
3. **按工作负载分 plugin 的领域切分**（新颖度 3/5 × 实用性 4/5）：13 个 plugin 对应 13 条 .NET 产品线，用户按需装。

### 可复用的模式与技巧
- **技能配套 eval.yaml + CI 校验器**：给自己写的每个 skill 配一份断言评测随仓回归，杜绝「技能腐烂」——可整套搬走
- **marketplace 分 plugin 而非平铺**：按领域切 plugin，控制单次安装的上下文体积
- **结构成熟度自检**：用「带 reference / 带 scripts 占比」量化合集深度

### 关键设计决策
- **官方精选 vs 社区众包**：用权威 + 评测背书换规模（98 vs 竞品上千），代价是覆盖窄
- **mastery 象限技能的取舍**：明知强模型已会，仍把规范固化下来——赌的是「弱模型 + 一致性 + 跨团队」的长期价值，而非给前沿模型加 buff

## 竞品格局与定位

| 维度 | dotnet/skills（本） | anthropics/skills | obra/superpowers | VoltAgent/awesome-agent-skills | addyosmani/agent-skills |
|------|------|------|------|------|------|
| Star | 3,306 | 8 万–14.7 万 | ~40.9k | 聚合型 | 23 技能 |
| 定位 | 官方垂直 .NET 领域 | 官方母仓·全域黄金标准 | 方法论/SDLC 工作流框架 | 社区 awesome 聚合 mega-list | 个人通用工程实践 |
| 规模 | 98 精选 | 全域精选 | 大而方法论 | 上千众包 | 小而专 |
| 评测背书 | **近 1:1 eval + 校验器** | 部分 | 弱 | 无 | 无 |
| 差异化 | first-party 权威 + 评测纪律 | 范式标准制定者 | 链式工作流编排 | 数量 + 多代理兼容 | 全生命周期通用 |

### 差异化护城河
**「唯一官方 first-party .NET + 评测工程化」**。社区也有 `managedcode/dotnet-skills`、`Aaronontheweb/dotnet-skills` 等，但官方权威 + 95 份回归断言是它们难复制的双壁垒。

### 竞争风险
① 模型持续变强 → mastery 类技能的边际价值随之衰减（本次实测 delta≈0 即预兆）；② anthropics/skills 若下沉到语言垂直领域会正面竞争；③ 上千条社区聚合在「广度」上碾压。

### 生态定位
.NET 在 AI-coding 时代的**官方知识接口**——不是给模型加能力，而是保证模型产出「地道、官方推荐」的 .NET 代码。

## 套利机会分析
- **信息差**：多数人盯着「有哪些技能」，真正被低估的是它的**评测基建**（eval.yaml + skill-validator）——这套「技能即被测代码」的纪律值千金，技能本身反而可被强模型平替
- **技术借鉴**（最大价值）：把每个自研 skill 配 eval.yaml + CI 校验的做法整套搬到你自己的技能库
- **生态位**：官方 .NET 代理知识入口，社区 .NET skill 的权威上位替代
- **趋势判断**：随模型变强，「codify 已知能力」型技能贬值，「评测 + 治理基建」保值——抄基建，别囤技能

## 风险与不足
1. **旗舰实测增益≈0**：对前沿模型，多数 mastery 类技能是一致性保险而非能力增量；合集价值高度依赖「使用方模型多强」
2. **技能随模型/版本双重贬值**：模型变强削弱必要性；.NET 版本迭代（如 dotnetX→X+1 迁移技能）带来持续时效维护负担
3. **新仓 + 团队集中**：仅 4 个月、Top2 贡献者约 70%，治理与收录标准仍在成形（open PR 37 积压）
4. **examples / trust 维度偏弱**：旗舰客观分在「可跑示例」「权威标注」上失分，合集普遍偏 prose
5. **广度受限**：98 精选对上社区上千聚合，长尾覆盖不足

## 行动建议
- **如果你要用它**：用强模型（如 Opus）时，价值有限、按需装垂直 plugin 即可；用较弱模型或团队不熟 .NET 时，装上能稳住产出一致性
- **如果你要学着写 skill**：**重点抄它的评测基建**——给每个 skill 配 `eval.yaml` 断言 + CI 校验器，让技能像代码一样回归；别只学它写技能正文
- **如果你要 fork / 贡献它**：补强 examples（可跑示例）与跨模型 delta 实测，把「对弱模型有效」这一价值点量化出来

### 知识入口

| 资源 | 链接 |
|------|------|
| 官方发布博客 | [.NET Blog — Extend your coding agent with .NET Skills](https://devblogs.microsoft.com/dotnet/extend-your-coding-agent-with-dotnet-skills/) |
| DeepWiki | [deepwiki.com/dotnet/skills](https://deepwiki.com/dotnet/skills)（待核） |
| Agent Skills 规范 | https://agentskills.io |
| 同类对照 | [anthropics/skills](https://github.com/anthropics/skills) / [obra/superpowers](https://github.com/obra/superpowers) |
| 在线 Demo | 无（交付物即 marketplace 安装） |
