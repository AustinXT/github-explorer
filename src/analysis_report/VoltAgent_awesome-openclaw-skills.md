# awesome-openclaw-skills 深度分析报告

> GitHub: https://github.com/VoltAgent/awesome-openclaw-skills

## 一句话总结

VoltAgent 运营的 OpenClaw 技能精选列表，从官方 Registry 的 13K+ 条目中系统性筛选出 5,200+ 个 skill，是 OpenClaw 生态中最大的第三方发现入口，也是一个教科书级别的 awesome-list 增长运营案例。

## 值得关注的理由

1. **awesome-list 运营方法论标杆**：VoltAgent 围绕 AI Agent 生态构建了 5+ 个 awesome-list 矩阵（合计 80K+ stars），「内容包围产品」的增长策略值得所有开源项目创始人学习
2. **规模化策展的参考实现**：从 13K 条目中用「排除法」筛选到 5.2K 的方法论公开透明——垃圾过滤、去重、质量门槛、垂直过滤、安全过滤五层排除，38% 通过率
3. **OpenClaw 生态安全信号**：项目揭示了 OpenClaw skill 生态的安全隐患——ClawHavoc 攻击事件、13.4% 的 ClawHub skill 存在安全问题、373 个已知恶意 skill

## 项目展示

![social banner](https://github.com/user-attachments/assets/a6f310af-8fed-4766-9649-b190575b399d)

VoltAgent awesome-openclaw-skills 项目封面——索引 5,200+ 个经过筛选的 OpenClaw 技能

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/VoltAgent/awesome-openclaw-skills |
| Star / Fork | 44,394 / 4,288 |
| 内容规模 | 6,596 行 Markdown，35 个文件，30 个分类目录 |
| 项目年龄 | 约 2.3 个月（2026-01-25 创建） |
| 开发阶段 | 快速成长期（328 次 commit，日均 4.7 次） |
| 贡献模式 | 单核心维护者 + 社区贡献（necatiozmen 65%，50+ 社区贡献者 35%） |
| 热度定位 | 大众热门（70 天内从 0 到 44K stars） |
| 质量评级 | 策展[良好] 分类[一般] 安全[优秀] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

VoltAgent 是一个 AI Agent Engineering Platform 公司，核心维护者 Necati Ozmen（@necatiozmen）是 VoltAgent 联合创始人、前 Refine.js 增长负责人，深谙「awesome-list 作为增长引擎」的开源运营套路。他在 Refine.js 时期就验证过「策展型内容 → SEO 流量 → 品牌认知 → 产品转化」的漏斗模型。

VoltAgent 组织同时运营 awesome-openclaw-skills（44.4K）、awesome-claude-code-subagents（16.3K）、awesome-agent-skills（14.2K）、awesome-design-md（13.1K）、awesome-codex-subagents（3.5K）等 5+ 个 awesome-list，合计超过 80K stars——这是一套系统性的开源营销基础设施。

### 问题判断

OpenClaw 官方 Skills Registry（ClawHub）虽然托管了 13,729 个社区 skill，但存在严重的信噪比问题：4,065 个疑似垃圾条目、1,040 个重复 skill、851 个低质量描述、886 个加密货币类条目、373 个恶意 skill。用户发现高质量 skill 的成本极高。VoltAgent 识别到这个「策展层缺失」的生态机会，在 OpenClaw 爆发增长初期迅速占位。

### 解法哲学

采用「排除法」而非「选择法」——不是从 13K 中挑「最好的」，而是系统性排除已知的低质量类别。五层排除规则（垃圾/去重/质量/垂直/安全）总计排除 7,215 个，保留 5,211 个。规则公开透明，可复现，易于社区理解。

内容组织上采用「双层结构」：README 作为索引层（每个分类预览前 20 条），30 个独立分类文件作为详情层。解决了超大列表的浏览体验问题。

### 战略意图

awesome-list 矩阵是 VoltAgent 的「内容包围产品」战略。每个 awesome-list 是一个「内容锚点」，将 VoltAgent 品牌与 AI Agent 生态紧密绑定。当开发者搜索 OpenClaw skills、Agent skills 等话题时，VoltAgent 的列表大概率出现在搜索结果第一位。README 中设有赞助位（Composio 等），声称 +1M monthly views，兼具品牌营销和商业变现。

## 核心价值提炼

### 创新之处

1. **规模化排除法策展**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）：对 13K 条目全量采用五层系统性排除，公开排除标准和数量，是目前已知最大规模的 awesome-list 策展实践之一

2. **配套发现平台 clawskills.sh**（新颖度 4/5 | 实用性 4/5 | 可迁移性 3/5）：GitHub 作为「可信数据源」，clawskills.sh 作为「体验层」，双轨运营。声称索引 5,147 个 skill 并获得 +1M monthly views

3. **awesome-list 矩阵策略**（新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5）：系统性地围绕 AI Agent 生态创建 5+ 个 awesome-list，每个 README 顶部交叉推广其他列表，形成流量飞轮

4. **安全筛选层集成**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）：在策展中加入安全维度，排除 373 个恶意 skill，推荐 Snyk 扫描工具，在 awesome-list 领域是少见的安全意识

### 可复用的模式与技巧

| 模式 | 描述 | 适用场景 |
|------|------|----------|
| 排除法策展框架 | 定义明确排除规则批量过滤，而非逐一评审 | 任何大规模策展项目 |
| 双层内容结构 | README 索引层 + 独立文件详情层 | 超过 500 条目的 awesome-list |
| awesome-list 流量飞轮 | 选对生态 → 策展列表 → SEO/Star → 交叉推广 → 品牌增长 | 开源项目增长运营 |
| PR 自动化守门人 | GitHub Actions 验证 PR 格式合规性 | 接受社区 PR 的策展项目 |
| 安全过滤即差异化 | 在策展中加入安全审计维度 | 工具/插件/扩展推荐列表 |

### 关键设计决策

| 决策 | Trade-off |
|------|-----------|
| 排除法而非精选法 | 牺牲了精细度（仍有漏网之鱼），换来了规模和可执行性 |
| 整体排除加密货币类 | 引发部分社区争议，但与主流开发者需求匹配 |
| 极简条目格式（名称+链接+描述） | 缺少 star 数等元数据，但降低了维护成本 |
| README 预览 + 分类文件完整列表 | 增加同步维护成本，但大幅改善浏览体验 |
| 赞助位商业化 | 可能影响策展独立性感知，但为持续维护提供经济基础 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | VoltAgent 版（本项目） | clawdbot-ai 中文版 | sundial-org 版 | libukai 版 |
|------|----------------------|-------------------|---------------|-----------|
| Stars | 44,394 | 3,807 | 553 | 3,862 |
| 语言 | 英文 | 中文 | 英文 | 中文 |
| 收录数量 | 5,200+ | 未知 | 较少 | 跨平台 |
| 独立网站 | clawskills.sh | 无 | 无 | 无 |
| 安全筛选 | 有 | 未知 | 未知 | 未知 |
| 矩阵效应 | 5+ 列表互导 | 单一 | 单一 | 单一 |

### 差异化护城河

三重壁垒：(1) 规模壁垒——5,200+ 条目 + 30 分类，后来者难以追赶；(2) 网络效应——44.4K stars 的 SEO 优势使其成为搜索「OpenClaw skills」的默认入口；(3) 矩阵协同——5+ 个 awesome-list 的交叉推广网络，整体壁垒远大于单个列表。

### 竞争风险

- OpenClaw 官方若改进 Skills Registry 的搜索和分类功能，第三方策展列表的价值会下降
- 竞品（尤其中文版）在特定语言社区可能蚕食份额
- awesome-list 的护城河本质上是「策展权」，可被更好的策展工具或社区驱动平台替代

### 生态定位

OpenClaw 生态中最大的第三方 skill 发现入口——典型的「策展权即话语权」案例。掌握了生态的推荐入口，就拥有了品牌影响力和商业变现的基础。

## 套利机会分析

- **信息差**: 项目本身已充分曝光。但其运营方法论（awesome-list 矩阵、排除法策展、双层结构）有显著的信息差——可以写一篇「如何用 awesome-list 矩阵做开源增长」的分析文章
- **技术借鉴**: 排除法策展框架可直接用于任何插件/扩展/工具的精选列表；PR 自动化守门人模式可用于社区驱动项目
- **生态位**: 揭示了 OpenClaw 生态的安全信号——13.4% 的 skill 存在安全问题，ClawHavoc 攻击事件等。这个方向有独立文章价值
- **趋势判断**: OpenClaw 生态仍在高速增长期，策展需求真实存在。但 awesome-list 的竞争窗口已关闭（先发者 44K stars），后来者需要差异化定位（如细分领域、特定语言社区）

## 风险与不足

1. **分类准确性问题**：「Transportation」分类包含大量非交通条目（会计、法律、商业计划），最大类「Coding Agents」占 22.8% 缺乏子分类
2. **排除法执行不完全**：声明排除加密货币类，但仍有 20+ 条含 crypto/blockchain 关键词的条目漏过
3. **条目元数据单薄**：仅有名称、链接和一句话描述，缺少 star 数、作者、更新时间、安全评分等关键维度
4. **README TOC 数字不同步**：声明数字与实际条目数存在偏差，频繁迭代导致同步延迟
5. **11 个 skill 跨分类重复**：如 agent-browser、hackathon-manager 等出现在多个分类
6. **商业动机透明度**：作为 VoltAgent 增长矩阵的一部分，赞助位和交叉推广的商业性质需要读者知悉
7. **单人维护风险**：necatiozmen 占 65% 提交量，项目持续性依赖个人投入

## 行动建议

- **如果你要用它**: 作为发现 OpenClaw skill 的起点很好，但不要完全信赖其筛选——注意安全声明中的「curated, not audited」，对关键 skill 仍需自行安全审查。配合 clawskills.sh 网站浏览更高效
- **如果你要学它**: 重点不在内容本身，而在运营方法论——研究 README 结构设计（双层+折叠）、排除法筛选标准表格、PR 自动化检查（.github/workflows/pr-check.yml）、以及 VoltAgent 的矩阵策略
- **如果你要 fork 它**: 值得做的方向：(1) 为条目添加元数据（star 数、安全评分、最后更新）；(2) 修复分类准确性问题（尤其 Transportation）；(3) 针对特定垂直领域（如 DevOps、Data Science）做深度子列表；(4) 中文社区有真实需求（参考 clawdbot-ai 的 3.8K stars）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/VoltAgent/awesome-openclaw-skills](https://deepwiki.com/VoltAgent/awesome-openclaw-skills) |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| 在线平台 | [clawskills.sh](https://clawskills.sh/) — 独立 skill 发现网站 |
