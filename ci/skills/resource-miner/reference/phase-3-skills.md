# Phase 3 — Agent Skills 仓库分析（镜头 D，detected_type=skills）

**目标**：把一个 Agent Skills 仓库讲透——它是什么技能合集、整体质量如何、**那个被实测的旗舰技能到底值不值**、读者该抄哪几个。产出判断而非罗列。
**输入变量**：LOCAL_PATH / FULL_NAME / GITHUB_URL / FACTS_JSON(`.skills` 块) / **ASSAY_RESULT**（旗舰技能的 `ASSAY-SUMMARY`，**主对话层已跑完 skill-assay**）/ Phase-1 摘要。

> **重要：本阶段不跑 eval**。旗舰技能的实测在主对话层的 Phase 2.5 已完成（skill-assay 自带子代理 fan-out，不能嵌套在本 Phase-3 子代理里）。这里只**综合** `ASSAY_RESULT` + `.skills` 清单 + 抽样阅读，不再调用 skill-assay / 42plugin eval。

**先做**：`Read FACTS_JSON` 的 `.skills`（roster / flagship / marketplace / commands_count / agents_count / root_dirs / real_skill_count），解析 ASSAY_RESULT 那行 JSON，并抽样阅读：旗舰技能的 SKILL.md（读全文，配合实测裁决）+ 2-3 个其它技能的 SKILL.md（判断家族风格与整体质量）。

## 1. 技能清单总览（从 `.skills.roster`）
- 规模与构成：`real_skill_count` 个技能；按 `root_dirs` / `group` 看分布（单一 `skills/` 还是多 plugin 分组如 dotnet 的 `dotnet-test`/`dotnet-msbuild`）。
- 结构成熟度：带 `reference`/`scripts` 的占比（脚本化=确定性下放、工程化程度高）；body 长度分布。
- 仓库形态：`single_skill`（单技能仓库）/ collection（多技能）/ marketplace（`.claude-plugin/marketplace.json` + plugins_count）/ mixed（含 `commands_count`/`agents_count`）。
- 官方 vs 社区 vs 个人：结合 Phase-1 作者画像判定（Anthropic/微软官方范本 vs 个人实验）。

## 2. 旗舰技能实测解读（把 ASSAY_RESULT 讲透）—— 报告重心
`ASSAY_RESULT` = `{"skill":..,"quadrant":..,"strategy":..,"score":0-100,"delta":Δ,"with":a,"without":b,"cases":n,"health":{...},"verdict":"keep|marginal|weak"}`。
- **象限 / 策略**：scaffolding / leverage / codification / mastery —— 说明这是哪类技能（脚手架/杠杆/知识编码/精通），决定它的价值逻辑。
- **客观结构分** `score`/100：frontmatter / 渐进式披露 / hygiene 的静态质量。
- **行为 delta**（核心）：`with a vs without b`，**delta=Δ**。这是「装上这个技能后模型到底强了多少」的实测。裁决 `keep`(Δ≥0.20，物有所值) / `marginal`(Δ小或代价高) / `weak`(Δ≈0，可砍)。
- **inverse 高亮**：若 `health.inverse>0`，**必须显著指出**——技能让模型输出更差，是反面信号。
- **expectation 健康度**：`skill_differential / always_pass / always_fail / inverse`——always_fail 多说明技能没覆盖到自己声称的能力。
- 一句话裁决：这个旗舰技能**值不值得抄**，为什么（引用 delta 与 health 具体数）。
- **降级模式**：若 ASSAY_RESULT 标 `mode:structural`（eval 后端不可用），只讲客观结构分 + 静态阅读判断，诚实写明「未做行为实测，仅结构评估」。

## 3. 「该抄哪些 / 整体质量」（结合 roster + 旗舰实测）
- 用旗舰的实测结论 + roster 的结构信号（哪些带 reference/scripts、body 充实），点名**值得装/学/抄的技能**（读者可操作）。
- 诚实规则：旗舰若 `weak` / 低 delta / 多 always_fail，直说「样板技能收益有限，多数靠模型本身也能做」，不吹。
- 整体质量评级（填项目画像 `质量评级`）：综合旗舰 delta + 结构分分布给 `质量[高/中/低]`。

## 4. 降级分支
- **single-skill 仓库**（`single_skill=true`）：报告即「这一个技能」的实测 + 结构解读，roster 总览退化为一句话，标题与正文聚焦单技能价值。
- **plugin-marketplace 无 SKILL.md**（`real_skill_count==0` 但 marketplace/plugin_json 存在）：改盘点 `commands_count` 个命令 + `agents_count` 个子代理（抽读 2-3 个 command/subagent 的 prompt），**跳过实测**，注明「本仓库是命令/插件集而非 skill 合集，无 SKILL.md 可实测」。

## 5. 共用收尾（对齐报告模板）
- **核心价值提炼**：创新之处（技能合集的运营/工程创新，如内置 eval、统一 frontmatter 规范、脚本化确定性；每个标新颖度×实用性）；可复用的模式与技巧（reference·scripts 结构、渐进式披露、eval 纪律——读者写自己的 skill 能抄的）；关键设计决策（合集的治理/规范决策 + trade-off）。
- **竞品格局与定位**：vs 其它 skills 合集 / marketplace（按 覆盖广度 + 结构质量 + 是否有实测背书 对比 3-5 维度）；差异化护城河；生态定位（标准制定者 / 工具箱 / 垂直专家）。
- **套利机会分析**：信息差（被高估/低估？）/ 技术借鉴（抄哪几个技能、抄哪套 authoring 模式）/ 生态位 / 趋势判断（模型变强后这些技能会不会贬值）。
- **风险与不足**：技能随模型变强而贬值（delta 衰减）、token 代价、未测/inverse 技能、合集只大不精、关键人依赖。
- **行动建议**：如果你要用它（装哪几个、跳过哪些）/ 如果你要学着写 skill（把哪个当范本、抄哪些 prompt 套路与 eval 纪律）/ 如果你要 fork·贡献它。
- **知识入口**：DeepWiki / Zread / Agent Skills 规范（https://agentskills.io）/ 作者博客。

## 返回格式（结构化摘要，回主对话）
```
### Phase 3 Agent Skills 分析摘要（type=skills）

**仓库形态**: collection/single/marketplace/mixed | real_skill_count=N | 带 reference·scripts 占比
**技能清单总览**: [分组/规模/成熟度 一段]
**旗舰实测**(把 ASSAY_RESULT 讲透): skill=<名> 象限=<q>/<strategy> 结构分=<score> delta=**+<Δ>** 裁决=<keep|marginal|weak>（inverse=<p>，有则高亮）—— 值不值得抄：<一句>
**该抄哪些**: 1) <技能名>：<为何> 2) ...
**核心价值/可复用模式/关键设计决策**: ...
**竞品矩阵**: [vs 其它 skills 合集，3-5 维度] | 或「无明显竞品」
**套利机会**: 信息差/技术借鉴/生态位/趋势判断
**风险**: [诚实 3-5 条，含 skill 贬值/未测/inverse]
**行动建议**: 用它/学着写 skill/fork 它
**质量评级**(填项目画像): 质量[高/中/低] 旗舰实测 delta[+X] 裁决[keep/marginal/weak] 象限[..]（降级时：实测 N/A·仅结构分）
```
