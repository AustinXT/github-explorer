# 0 代码 9.5K Star：一位 Atlassian 设计总监如何用一份 SKILL.md 撬动 AI 写作反 slop 赛道

> GitHub: https://github.com/hardikpandya/stop-slop

## 一句话总结

一个零依赖、零代码、零构建的 Agent Skill，把「AI 写作痕迹」（slop）编码成 5 维评分 + 35/50 阈值，让 Claude/Cursor 在写完散文后自我审计并改写，5 个月爆 9.5K Star。

## 值得关注的理由

- **形态创新**: 整个仓库只有 332 行 Markdown，把"linter"从 npm install 压缩到 copy-paste 一份文件——这是 Agent Skill 时代的"超轻量工具"标本。
- **可复用骨架**: 三段式 prompt 模板（Rule + Quick Check + Scoring）+ Blacklist 配 Instead-routing，对任何"反 X 风格"任务都能直接 fork。
- **现象级爆款**: 12 个 commit、**2.7 个月未更新、Star 仍每天涌入**——典型的"规则骨架对了，星会自己长"案例。

## 项目展示

![Stop Slop hero banner](https://github.com/user-attachments/assets/902afc15-1f40-4a9d-af24-8cd67afb8ebf)

> 标题装饰性 banner，仓库本身无 demo 视频/GIF，README 文本密度高、视觉资产稀缺。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/hardikpandya/stop-slop |
| Star / Fork | 9,555 / 673 |
| 代码行数 | 0（332 行 Markdown 规则文档） |
| 项目年龄 | 4.9 个月（2026-01-11 至今） |
| 开发阶段 | 低维护（最近提交 2026-03-18，已停更 ~2.7 个月） |
| 贡献模式 | 单人主导（Hardik Pandya 占 83.3%，社区贡献者 1 人） |
| 热度定位 | 大众热门（爆发型增长，155 个新 Star 全部落在 0 天窗口） |
| 质量评级 | 文档[优秀] 规则自洽性[一般] 测试[无] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Hardik Pandya，Atlassian Head of Design，15 年 GitHub 账号，189 粉、12 个公开仓库。其个人博客 hvpandya.com 与 solari-split-flap、vibe-slack 等作品，体现「美学 + 工具」的复合兴趣——他既会写工程化的视觉项目（solari-split-flap 是拆 flap 显示牌），也会做 Slack 客户端替代品（vibe-slack），长期关注「写作/内容工艺」与 LLM 协作体验。这份 stop-slop 是他职业训练延伸到 AI 写作审美的产物。

### 问题判断

LLM 写散文时有一组可被命名的「AI 写作痕迹」（"here's the thing"、"Not X, but Y"、"a complaint becomes a fix"……），这些不是语法错误，而是词法、短语、句法、节奏层面的统计偏好。他把"AI 写出来读着像 AI"这件事从个人审美不满，提炼成了一个独立工具：把零散的反感编码成可复用的结构化清单。

### 解法哲学

"Restriction prompting → positive routing"——先以禁词/禁结构建立底线（"Don't write this"），再逐步补充"write this instead"。所有禁条都附 Instead 行（phrases.md 的 Business Jargon 用对偶表，structures.md 每节结尾都有 Instead 段落），是典型的从 blacklist → guided rewriting 演化路径。社区在 issue #10 推动的设计改进方向，作者本人持开放态度。

### 战略意图

以「SKILL.md 形态」卡位 Agent Skill 生态：纯文本 + 零依赖 + 5 min 集成 = **低阻力扩散**。停更 2.7 个月但 Star 仍在涌入，说明**该形态本身已是产品**——Star 反映「被加进我的项目清单」，而非「还在迭代」。近 90 天 3 commits 表明作者把维护成本压到极低，赌的是「规则骨架对了，社区会驱动扩展」。

> 个人博客未把本 repo 单列深度文章，「官方文档洞察」仅基于 README/SKILL.md/CHANGELOG 解读。

## 核心价值提炼

### 创新之处

1. **三段式 prompt 结构（rule + checklist + rubric）作为反风格护栏**（新颖度 3/5，实用性 4/5，可迁移性 5/5）
   - 把"理解 / 执行 / 评分"分到三层 rubric，LLM 在改写前先自评 5 维 1-10 分，低于 35/50 触发重写。这把"修辞质量"从感觉判断变成可被 prompt 引导的自循环。

2. **SKILL.md 形态的「零部署 linter」**（新颖度 4/5，实用性 5/5，可迁移性 5/5）
   - 整个项目 0 代码 0 依赖，「安装」=「把 SKILL.md 放进上下文」，「运行」=「让 LLM 写完散文后过一遍规则」。这在社区层面相当稀缺。

3. **「False Agency」作为独立规则类型**（新颖度 4/5，实用性 4/5，可迁移性 4/5）
   - structures.md 把"complaint becomes a fix"、"bet lives or dies"、"data tells us"等「无生命主语 + 人类动词」单列一节，配 7 个具体例子——这是**对 LLM 特有偏好的命名**（人类写作不容易犯这种错，**因为人有具身经验**）。

4. **Blacklist 配 Instead-routing 对偶表**（新颖度 2/5，实用性 5/5，可迁移性 5/5）
   - 同一份文件同时承担"禁词库"和"替代词库"两本字典，避免 LLM 矫枉过正。

5. **5 维评分（Directness/Rhythm/Trust/Authenticity/Density）而非 1 维**（新颖度 3/5，实用性 4/5，可迁移性 4/5）
   - 五个正交维度避免模型在单一「流畅度」上走捷径，把"AI 风"从模糊气质拆成可分别打分的子能力。

### 可复用的模式与技巧

- **「Rule + Quick Check + Scoring」三段式 prompt 模板**：让 LLM 先理解、再执行、最后量化——适用任何需要"自我审计"的 agent 任务。
- **「Blacklist with Instead-routing」模式**：每个禁条都配正向示例，避免 LLM 矫枉过正——适用反风格指南、tone-of-voice 守门员。
- **「分粒度 reference 文件」模式**：系统提示放抽象规则，references/ 放具体词典；上下文预算友好——适用任何给 LLM 长期挂载的领域知识包。
- **「SKILL.md 形态的纯规则资产」模式**：零代码仓库承担完整工具职责，发布门槛 = 复制文件——适用一切 LLM 协作类的低频工具。
- **「1 issue = 1 规则增量」的低维护节奏**：作者用 issue 收集社区信号（#10 taxonomy 改进、#9 句法树、#33 交互模式），让维护 = review issue——最大化 star-to-effort 比。

### 关键设计决策

1. **用 LLM 上下文做"linter"而不是用代码做 linter**
   - 问题: 散文 slop 在 token 流里，不在 AST 里；任何代码方案都需要额外运行时
   - 方案: 把规则编码为 LLM 自然语言可读的 markdown，靠模型自检
   - Trade-off: 检出率取决于模型能力 / 上下文长度 / 规则位置，但部署成本 = 一份文件，且天然跨模型
   - 可迁移性: **高**

2. **三层规则粒度（rule / quick check / 评分 rubric）**
   - 问题: 单一粒度的规则要么太抽象（"be specific"）模型抓不住，要么太具体（白名单 500 词）超过上下文预算
   - 方案: SKILL.md 给 8 条抽象 rule + 12 条 imperative quick check + 5 维 1-10 评分三层
   - Trade-off: 三层之间有重叠（如"no adverbs"出现在 rule #1 与 quick check #1），需要读者心智合并
   - 可迁移性: **高**

3. **评分阈值 35/50（70% 分位）作为 rewrite 触发线**
   - 问题: LLM 在没有可验证目标时倾向于"礼貌地改一点"
   - 方案: 用 5×10 rubric 量化，给定 70% 阈值，把"需要重写"从感觉判断转成**确定性判定**
   - Trade-off: 维度仍偏主观，可能让模型"优化到 rubric"而非"优化到人话"（**Goodhart 风险**）
   - 可迁移性: **中**

4. **拒绝"代码层 schema"——纯 markdown，不引入 YAML/插件机制**
   - 问题: 加 schema 看似严谨，但每加一个 meta 就把"会写 markdown 的人"过滤掉
   - 方案: 仅 SKILL.md frontmatter 是必需结构，其余内容自由文本
   - Trade-off: 失去结构化校验，但获得了"看一遍就能 fork 改一份"
   - 可迁移性: **高**

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | stop-slop（9.5K★） | vale-ai-tells（24★） | slopbuster（16★） | anti-slop（693★） |
|------|------|------|------|------|
| 形态 | SKILL.md 纯文本 | Vale 规则包 | humanizer 工具 | GitHub Action |
| 焦点 | 散文 slop | 散文 slop | 散文/代码/学术 | 代码 PR slop |
| 部署成本 | copy-paste 1 文件 | 装 Vale | 跑脚本 | 接 Action |
| 评分机制 | 5 维 1-10 + 35 阈值 | 无 | 无 | 二元 |
| 自审能力 | 是（in-loop） | 否 | 否 | 否 |
| 跨 LLM 通用 | 是 | 是 | N/A | N/A |

### 差异化护城河

形态本身（SKILL.md 零部署） + 评分 rubric 量化「AI 风」 + 规则三层粒度。这三者结合让任何「反 X 风格」都能 fork 一份。

### 竞争风险

- **最可能被替代**: Anthropic/OpenAI 官方把「反 slop」做进 base model 行为，stop-slop 价值归零
- **替代条件**: 官方 model spec 把"no AI tells"写进 system prompt，是最大下行风险
- **社区风险**: issue #10 暗示的「positive-only」分流可能催生 fork，吞噬原版

### 生态定位

散文 slop 工具的「v0」位置——竞品稀少（直接对位只有 vale-ai-tells），但下游会出现大量「反 X 风格」fork。stop-slop 占据的是「规则工程 + 评分 rubric」这个交叉点。

## 套利机会分析

- **信息差**: 低（已被 9.5K Star 充分定价，且最近 155 个 Star 全部在 0 天窗口涌入，处于爆发高峰）——但作为「AI 写作工艺赛道的现象级 skill」仍有内容拆解价值。
- **技术借鉴**: 三段式 prompt 模板（Rule + Quick Check + Scoring）+ Instead-routing 对偶表 + 分粒度 reference 文件——这三条直接可套到自己项目的 agent prompt 里。
- **生态位**: 「反 X 风格」是 2025-2026 才浮现的微细分，stop-slop 用 SKILL.md 形态暂时领跑散文方向。
- **趋势判断**: 比代码方向（anti-slop/aislop）的 700+ Star 路线更轻、更易 fork；若 Anthropic 未来把 slop 防护内建，stop-slop 的「人工规则」价值会受冲击，但「可定制、可白名单」的差异化仍有空间。

## 风险与不足

- **规则自洽性风险**: issue #14 揭示 README 里的示例文本曾违反自身规则（如"X that isn't Y"在 structures.md 出现，README 又有"X that isn't Y"做反例），没有自动化校验意味着这类自反性 bug 会持续
- **停更风险**: 2.7 个月无新 commit，若社区驱动减速，star 增长将放缓
- **Goodhart 风险**: 5 维评分可能让模型"优化到 rubric"而非"优化到人话"
- **覆盖度缺口**: 漏了「段落首句使用同义词变化」（AI 偏好"另外 / 而且 / 更重要的是"这种段落连接词）、「过度对仗」（每段都是 a-b-a-b 节奏）等更细粒度的偏好
- **平台依赖**: 强依赖 LLM 行为，Claude/GPT 模型升级若改变对禁词的反应，整套规则可能需要重调

## 行动建议

- **如果你要用它**: 适合用 Claude Code / Cursor 写 README、博客、公号文案时作为 Skill 挂载；不适合纯学术说明文（会与 passive voice 规则冲突）
- **如果你要学它**: 重点关注 SKILL.md 的「Rule + Quick Check + Scoring」三段式结构与 phrases.md 的对偶表设计——这是可移植到任何 LLM 协作 prompt 的模板
- **如果你要 fork 它**: 可以改进的方向——
  1. 加一个"LLM 自审 example.md 是否自洽"的 CI 任务
  2. 把"positive routing"做成可选开关（issue #10 方向）
  3. 补段落级规则（连接词、节奏模板）
  4. 引入 Wikipedia 24 Signs 的句法树检测（issue #9 方向）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录（403） |
| Zread.ai | [链接](https://zread.ai/hardikpandya/stop-slop) |
| 关联论文 | 无（启发式规则工程，非学术输出） |
| 在线 Demo | 无（无运行态 UI） |
