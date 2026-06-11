# 3 个月 15K Star：把 PM 方法论编码成 Claude Skill 集，pm-skills 凭什么破圈？

> GitHub: https://github.com/phuryn/pm-skills

## 一句话总结

把 Teresa Torres、Marty Cagan、Ash Maurya 等产品界主流方法学封装成 **68 个 Skill + 42 条 Command + 9 个 Plugin**，让 Claude / Codex / Cursor / Gemini / OpenCode / Kiro 一次性加载——一个用「三层抽象 + 跨工具分发」重新定义 AI 时代 PM 工作流的**文档型产品**。

## 值得关注的理由

1. **现象级增长**：3 个月从 0 冲到 **15,313 Star**，是同期 AI 工具圈罕见的「破圈」案例，验证了「PM × Agent Skills」是一个真实的用户痛点赛道。
2. **可复用的协议范式**：`Skill(名词) × Command(动词) × Plugin(领域)` 三层抽象 + 自研 `validate_plugins.py` 校验器，构成一份**「AI 时代知识仓库」的参考实现**。
3. **原创的审查方法论**：`intended-vs-implemented`（以意图为锚）和 `strategy-red-team`（cheapest-test 排序）是把软件审计与产品决策领域的方法学落地到 LLM 工作流的**原创贡献**，不是简单包装现有方法。

## 项目展示

![PM Skills marketplace: skills, commands, and all 9 plugins at a glance](https://raw.githubusercontent.com/phuryn/pm-skills/main/.docs/images/plugins.png) — hero：9 个 plugin 的全局视图

![Example prompts: a skill and two commands (/write-prd, /ship-check) in action](https://raw.githubusercontent.com/phuryn/pm-skills/main/.docs/images/examples.png) — screenshot：命令用法示例

![Installing PM Skills in Claude Cowork](https://raw.githubusercontent.com/phuryn/pm-skills/main/.docs/images/pm-skills-install.gif) — demo：安装动图

![PM Brain composes with PM Skills](https://raw.githubusercontent.com/phuryn/pm-skills/main/.docs/images/pm-brain-pm-skills.webp) — screenshot：与 PM Brain 组合示意

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/phuryn/pm-skills |
| Star / Fork | 15,313 / 1,645 |
| Watcher | 141 |
| 代码行数 | 353 行 Python（仅为辅助脚本）；123 个 Markdown 文件构成实际产品（注释/代码比 1:24.2，文档即代码） |
| 项目年龄 | 3.3 个月（首次提交 2026-03-02） |
| 开发阶段 | 密集开发 → 稳定维护（v2.0 引爆回流） |
| 贡献模式 | 单人主导（Pawel Huryn 占 96.2%，另有 2 位贡献者各 1 commit） |
| 热度定位 | 大众热门（细分赛道事实头部） |
| License | MIT |
| 最新版本 | v2.0.0（共 1 个 tag，版本号 lockstep 同步） |
| 质量评级 | 文档[优秀] 校验[优秀] 跨工具分发[优秀] CI/CD[无] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Pawel Huryn**（phuryn），12 年 GitHub 账号（2014-06 注册），公开仓库 28 个，但其中 27 个只有 0-21 星（仅 `claude-usage` 1,776 星、`pm-brain` 342 星有量级）。他同时是：

- **The Product Compass Newsletter** 创始人，自报 400K+ 关注
- **AI PM 教练**（对外身份）
- **前 CPO**（背景经历）

12 年账号但只把 `pm-skills` 一个仓库做成「15K Star 旗舰」——这不是代码能力问题，而是「内容资产 + 品牌权威 + 时机把握」三件套同时成立的稀缺组合。

### 问题判断

**作者看到了什么别人没看到的问题？**

> 「AI does not fix weak product judgment. It scales it. PM Skills is where the judgment lives.」

AI 写文档的瓶颈不在「语言能力」而在「方法论」——Claude 写出来的 PRD 没有 non-goals、discovery doc 没有 OST、launch plan 没有 risk category。**痛点不是 AI 不够聪明，而是 AI 没人教它产品方法论。**

**时机为什么是现在？**

2024-2025 Anthropic 推出 Skills / Plugins / Marketplaces 协议后，**第一次让「给 Claude 装方法论」成为可能**（`marketplace.json`、`plugin.json`、`SKILL.md` frontmatter）。Cursor / Gemini CLI / Codex CLI 同期跟进，让 SKILL.md 格式成了事实标准。作者顺势把多年 newsletter 内容（被 400K+ PM 验证过的方法）**一次结构化释放**。

### 解法哲学

**明确选择**：

1. **极简 + 可组合**：Skill（名词 = 领域知识）+ Command（动词 = 链式工作流）+ Plugin（领域容器），每层独立可装。`CLAUDE.md` 明文规定「No cross-plugin references」——commands 用自然语言建议下一步，绝不硬跨插件引用。
2. **文档即代码**：整个项目不是 .py/.ts，而是 markdown + YAML frontmatter + JSON manifest。「代码质量」≈「文档质量 + skill 一致性 + frontmatter 合规」。
3. **慢深而非快广**：v1.x 累积 28+ skills，v2.0 跳到 68 skills + 42 commands，是方法论的「字典式」封装——把 PM 实务每个动作都对应一个 skill，而不是为流行趋势做单点功能。
4. **跨工具抗单点**：同一份 SKILL.md 可被 Claude / Codex / Gemini / Cursor / OpenCode / Kiro 6 家加载，README 提供 4 套 shell 片段做「降级到 skills-only 安装」。

**明确不做什么**：

- 不做 SaaS 封装（与 Productboard / Airfocus 类互补）
- 不做多模态（不接图像/语音/OCR）
- 不做自动化运行时（不部署 agent、不调度 LLM、不接管 git）
- 不为制造怀疑而怀疑（`strategy-red-team` 明文要求「What's Well-Reasoned」节——必须 explicit 列出没问题的假设）

### 战略意图

pm-skills 在作者商业矩阵中的位置：

```plain
内容（The Product Compass Newsletter, 付费）
        ↓ 导流
工具（pm-skills, 免费 15K Star）
        ↓ 配套
生态（pm-brain, second-brain CLI, 342 Star）
```

是**「免费钩子 + 付费漏斗顶」的典型 open-core 模型**。每个 SKILL.md 末尾的「Further Reading」链接到 productcompass.pm 文章——免费 SKILL 引流到付费文章，付费文章反哺免费 SKILL 准确性。

**开源自建协议示范意图**：`validate_plugins.py` 明确参考 `agentskills.io` 与 Claude Code plugin 规范，作者希望别人 fork 模板做自己领域的 skill 集（legal-skills、design-skills、finance-skills）。他本人也有意把仓库做成「skill 协议示范」（Issue #12 pm-governance 提案 + 主动兼容 6 家工具）。

## 核心价值提炼

### 创新之处

1. **三层抽象：Skill × Command × Plugin（noun × verb × domain）**
   - 切分 LLM 内容交付物为**三个正交层级**；manifest 协议（marketplace.json / plugin.json / SKILL.md frontmatter / commands/*.md frontmatter）形成 4 层文件树，每层都有自己的校验规则
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

2. **Intended vs Implemented 审计方法**
   - 以代码意图（documentation/*.md）为锚而非以代码本身为锚的审查方法。审查者必须 cite 双方（doc 说 X、code 做 Y），并 explicit name attacker + victim + concrete fix
   - **新颖度 5/5** | 实用性 5/5 | 可迁移性 5/5

3. **Cheapest-Test-First 风险排序**
   - `strategy-red-team` 不输出 20 条风险列表，而是按 `impact × likelihood × cheapness-to-test` 排序后只输出 top 3-5 条「本周可验证」的 kill-assumption，每条配 evidence / kill criterion / cheapest test
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

4. **Core + Conditional 文档模式**
   - `shipping-artifacts` 把审查文档分成 5 个 always-on core + 4 个 conditional；conditional 缺失时只写一行「No scheduled work — no `cron.md`」作为「we don't do X」的诚实声明
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

5. **跨工具 marketplace（一份内容覆盖 6 家 AI 工具）**
   - SKILL.md 遵循 agentskills.io 通用协议，可被 Claude / Codex / Gemini / Cursor / OpenCode / Kiro 加载；README 提供 4 套 shell 片段做「降级到 skills-only 安装」
   - 新颖度 4/5 | 实用性 4/5 | 可迁移性 5/5

6. **Steelman-then-attack 而非直接 strawman**
   - `strategy-red-team` 明文规定「attack the steelman or don't attack」——攻击前必须先写出最强版本；output 必须含「What's Well-Reasoned」节
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5

### 可复用的模式与技巧

1. **Frontmatter 双层协议**：Skill（name + description + trigger 短语）vs Command（description + argument-hint）——区分「自动加载 vs 显式触发」。所有 Claude-based 知识仓库都应采用 noun/verb 切分。

2. **No-cross-plugin-references 自然语言桥接**：plugin 内可硬引 skill（同装必现），跨 plugin 必须用自然语言「Want me to design growth loops?」。适合任何可拆分打包的多 plugin marketplace。

3. **Version lockstep + 单一信源**：marketplace.json 与所有 plugin.json 同步版本号（当前全 2.0.0）。适合紧密耦合的微内核集合。

4. **Self-validating 仓库**：`validate_plugins.py`（507 行）把「内容质量」转成「可 CI 跑的检查」——errors / warnings / info 三层分级 + 彩色 ANSI + Windows UTF-8 兜底。适合所有需要 lint 自己的内容仓库。

5. **Tiered severity + cite-both-sides 报告格式**：`/security-audit-static` 输出 Critical/High/Medium/Low 四档 + 每条 finding 必须含 Attack Scenario + Impact + Solution + 引用 file:line。

6. **Progressive disclosure 设计**：frontmatter 始终加载（cheap）；body 仅在触发时加载（expensive）；README 仅 GitHub 展示（不进入运行时）。所有 token-cost-sensitive 的 LLM 内容设计都应如此。

7. **Honest-map over polished-template**：明确允许「一行声明不存在」而非「为不存在的功能编空文档」。`shipping-artifacts` 中「No scheduled work — no `cron.md`」是核心模式。

8. **Cheapness-to-test as primary axis**：风险/假设排序用 impact × likelihood × cheapness-to-test——把「本周可验证」作为优先级维度。

### 关键设计决策

**决策 1: Skill = 名词 vs Command = 动词**
- 问题：LLM 自动加载 vs 用户显式触发的两类能力如何共存？
- 方案：YAML frontmatter 的 `description` 与 `argument-hint` 区分——skill 必须含「Use when / Triggers」短语；command 必须含 `argument-hint`（如 `<PRD, roadmap, strategy>`）。
- Trade-off：牺牲了「skill 也能传参」的对称性，换来了「skill 在对话中无缝漂浮」的可用性。
- 可迁移性：高

**决策 2: No cross-plugin references**
- 问题：plugin 必须可独立安装。command A 写「先跑 plugin-B 的 /foo」，用户没装 plugin-B 时静默失败。
- 方案：`CLAUDE.md` 与 `CONTRIBUTING.md` 双重明文禁止；`validate_plugins.py` 校验 command 内的 `**skill-name** skill` 引用必须在同 plugin 存在。
- Trade-off：放弃「插件组合形成图」的可能性，换来了「每个 plugin 真独立可装」的强保证。
- 可迁移性：高

**决策 3: 版本全 lockstep**
- 问题：插件独立可装时如何协调版本？
- 方案：CLAUDE.md 明文规定「There is no independent per-plugin versioning. Bump any `plugin.json` → also bump `marketplace.json`, and vice-versa」。
- Trade-off：牺牲 plugin 级独立迭代，换来了「marketplace 单一版本号即一切」的极简心智模型。
- 可迁移性：中

**决策 4: 自研 `validate_plugins.py` 而非依赖外部 lint**
- 问题：Claude plugin 协议没有官方 lint 工具；社区 plugin 普遍 frontmatter 不全、name 不匹配目录、cross-refs 断裂。
- 方案：507 行 Python 自写校验器——检查 plugin.json 必填字段、semver、author、keywords；skill frontmatter `name == directory name`；command frontmatter 含 `description` + `argument-hint`；cross-refs；README 子串。
- Trade-off：放弃「用现成 YAML/JSON linter」的零代码（507 行自研需维护），换来了「对 plugin 协议完整建模」的能力。
- 可迁移性：高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | phuryn/pm-skills | Product Faculty PM-Copilot | cafe3310/public-agent-skills | inngest/inngest-skills |
|------|-----------------|---------------------------|------------------------------|-------------------------|
| Star 数 | 15,313 | 41 | 214 | 23 |
| Skill 数 | 68 | 65+ | 通用集 | Inngest 专属 |
| Command 数 | 42 | 17 | 仅 skills | 平台专属 |
| 覆盖域 | PM 全栈（9 plugin） | 12 域 | 通用 | Inngest workflow |
| 跨工具分发 | 6 个 AI 工具 | 仅 Claude | 通用 | 仅 Inngest |
| Sub-agents | 无（skill+command 双层） | 8 个 | 无 | 无 |
| 配套生态 | newsletter + pm-brain | 单一项目 | 无 | Inngest 平台 |

### 差异化护城河

1. **生态护城河（最关键）**：**9 个 plugin × 68 skill × 42 command × 6 个 AI 工具的覆盖矩阵**是单纯 fork 无法追赶的；作者 12 年账号 + 400K+ 关注 newsletter 形成的「产品方法论权威」品牌。
2. **协议护城河**：`validate_plugins.py` 把 agentskills.io 协议工程化，提供完整 lint + manifest 校验 + cross-ref 检查；其他竞品没有同等工具。
3. **方法论护城河**：Teresa Torres / Marty Cagan / Alberto Savoia / Ash Maurya 等方法被高质量编码成可执行 skill，单人 96.2% 主导保证一致性。

### 竞争风险

1. **Anthropic 官方 Skills 库**：如果 Anthropic 推出官方 PM skill bundle（社区已多次提议），pm-skills 的护城河会受冲击。Issue #26（Claude 4 月更新后个人 skills filter 失效）证明上游协议变化是真实风险。
2. **GitHub Copilot Workspace / Devin**：如果 AI IDE 原生集成 PM agent，pm-skills 可能被部分替代。
3. **作者单点风险**：96.2% 单人贡献意味着作者若长期缺席，仓库活跃度会快速衰减。

### 生态定位

「PM 领域的 Skills 协议示范 + 方法论事实标准」。在 Anthropic Skills 生态中扮演「垂直深度参考实现」角色，在 PM 教育生态中扮演「AI-native 教学材料」角色。

## 套利机会分析

- **信息差**：★☆☆☆☆（已破圈，15K Star 不再被低估）；但 PM × Agent Skills 细分赛道仍处于早期，整体市场认知度低于工具型项目
- **技术借鉴**：★★★★☆（三层抽象协议、`validate_plugins.py` 校验器、Intended vs Implemented 审计方法、Cheapest-Test-First 排序都是高价值可迁移资产）
- **生态位**：★★★★★（「PM × Agent Skills」是 Anthropic 协议下的稀缺垂直深度，短时间内难以被复制）
- **趋势判断**：★★★★☆（Anthropic Skills 协议仍在演进，跨工具分发策略有抗单点优势；v2.0 引爆 + Red Team / Shipping Kit 等真实 PM 痛点能力验证产品方向）

## 风险与不足

1. **上游耦合风险**：Issue #26 证明**产品可用性被 Anthropic 产品节奏直接绑架**；4 月 Claude 客户端一次更新就破坏原有教程。
2. **安装链路脆弱**：Issue #7 反映用户从 Cowork 插件 UI 添加 GitHub Marketplace 时报错——新手最大摩擦点在 marketplace 元数据 + 安装链路工程细节。
3. **作者单点风险**：96.2% 单人贡献，10 个其他活跃仓库 0-21 星的现状说明作者若精力分散，pm-skills 会快速衰减。
4. **架构边界争议**：Issue #12 提案新增 pm-governance plugin——揭示「按阶段 + 按能力」两种切法的张力（横向 governance 层该不该独立成第 10 个插件）。
5. **CHANGELOG 缺失**：版本号 lockstep 但用户看不到升级内容，需读 commit 历史。
6. **无 CI/CD**：README 未提到 GitHub Actions；`validate_plugins.py` 是 CI-ready 工具但未启用，依赖作者纪律。

## 行动建议

### 如果你要用它

- **强推荐场景**：需要写 PRD/roadmap 并在上会前做压力测试的 PM；AI 生成代码需要人工 sign-off 的 founder / 技术 PM；Claude Cowork / Code 用户想要插件化 PM 工作流。
- **不建议场景**：需要多 agent 协作模拟（选 Product Faculty PM-Copilot）；PM 通用方法论之外的领域工作（选 public-agent-skills）；需要平台深度集成（选 inngest-skills）。

### 如果你要学它

重点关注：
- `CLAUDE.md` —— 109 行的 single source of truth，定义了所有协议约束
- `.claude-plugin/marketplace.json` 与各 `plugin.json` —— manifest 协议范本
- `pm-execution/skills/shipping-artifacts/SKILL.md` 与 `pm-execution/skills/intended-vs-implemented/SKILL.md` —— 两个最有方法论原创性的 skill
- `validate_plugins.py` —— 507 行内容仓库 test suite 实现

### 如果你要 fork 它

可以改进的方向：
- 新增横向 plugin（如 pm-governance，Issue #12 已提案）
- 翻译为中文版本（当前 README 全英文，但方法论本身无语言依赖）
- 适配更多 AI 工具（目前覆盖 6 家，可继续扩展）
- 为 validator 增加单元测试（dogfooding 盲区）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | [链接](https://zread.ai/phuryn/pm-skills) |
| 关联论文 | 无（非研究类项目） |
| 在线 Demo | 无（仅 README 内嵌的安装 GIF） |
| 官方文档 | [productcompass.pm/p/pm-skills-2-red-team-ship](https://www.productcompass.pm/p/pm-skills-2-red-team-ship)（付费 newsletter） |