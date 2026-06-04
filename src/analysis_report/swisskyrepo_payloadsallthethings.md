# 9.6 年、78K star、零代码仓库：PayloadsAllTheThings 凭什么把渗透 payload 写成「行业基础设施」

> GitHub: <https://github.com/swisskyrepo/payloadsallthethings>

## 一句话总结

PayloadsAllTheThings 是一份**用 GitHub 仓库形态维护的渗透测试 payload 百科全书**——注释:代码 ≈ 26:1 的「反常识」文档型项目，靠「模板化贡献 + 消毒占位符 + Burp 字典绑定」三件套，把 333 位陌生人变成 9.6 年可持续的搬运工，最终跻身 Bug Bounty 实战链条上游的事实标准。

## 值得关注的理由

- **「文档即产品」的天花板案例**：单仓 54,442 行 Markdown + 2,096 行代码，9.6 年长尾 333 位贡献者，开源安全知识基础设施的样板
- **跨域移植的工程化创新**：把 Arch Wiki 范式（分章节 + 可预测导航）+ SecLists 范式（字典即资产）+ 开源项目 `_template/` 脚手架三者合璧，做出"贡献者零门槛"的内容生态
- **行业护城河已成型**：被 OWASP、PortSwigger 官方文档引用，成为 Burp Intruder 字典的事实来源，竞品难以快速复制 9.6 年沉淀的 reference 网络

## 项目展示

1. ![banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png) — 类型: hero（项目主视觉 banner）
2. ![sponsors-list](https://contrib.rocks/image?repo=swisskyrepo/PayloadsAllTheThings&max=36) — 类型: 社区贡献者墙（自动生成，9.6 年沉淀的可视化）

> 在线文档站：[swisskyrepo.github.io/PayloadsAllTheThings](https://swisskyrepo.github.io/PayloadsAllTheThings/)（MkDocs Material 主题，左侧 TOC + 代码复制 + 暗色模式）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | <https://github.com/swisskyrepo/payloadsallthethings> |
| Star / Fork | 78,186 / 17,039（Watchers 1,961） |
| 代码行数 | 2,096 行 Python 61% + ASP.NET 9% + XSL 7% + 多语种（实际主体是 54,442 行 Markdown） |
| 项目年龄 | 115.7 个月（约 9.6 年，2016-10-18 首次提交） |
| 开发阶段 | 稳定维护（季节性脉冲，10 月 Hacktoberfest 集中爆发，2026-04 仍有更新） |
| 贡献模式 | 单人主导 + 社区协作（Swissky 占 47.5%，Top3 占 ~60%，333 位贡献者） |
| 热度定位 | 大众热门（安全/Pentest 主题头部，事实标准） |
| 质量评级 | 文档 优秀 / 工程 良好 / 测试 N/A（内容型） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Swissky（swisskyrepo），独立 **Red Team Operator & Bug Hunter**，账号 11.1 年（2015-04 注册），10,496 粉丝，13 个公开仓库。bio 自述为红队/漏洞众测领域研究者，配套开源 SSRFmap、GraphQLmap、Wordpresscan、InternalAllTheThings、HardwareAllTheThings 等多个独立工具，是欧洲安全圈（法语区）较有影响力的红队/漏洞研究者。**作者本身既是内容生产者（payload 沉淀），也是工具开发者（红队工具），更是知识消费者（自家仓库的读者）**——典型的"dogfooding 驱动型"创作者。

### 问题判断

2016-2018 年 Web 渗透 payload 高度碎片化，散落在 Twitter 推文、漏洞 Writeup 博客、Discord 频道、CTF writeup 论坛里。新人面对"我现在需要 WAF 绕过的 XSS payload"这种问题时，要么翻 50 条推文，要么自己造轮子，**信息差巨大**。叠加 Bug Bounty 平台（HackerOne、Bugcrowd）爆发期带来的"作战手册"刚需，作者认定需要"集中、可引用、可复现"的内容型基础设施。

### 解法哲学

- **「集中即服务」**：把分散在推文/博客/议题的信息，结构化、模板化、可引用地集中起来，干的是「给安全社区做 Arch Wiki for Web Pentest」的事
- **Unix 哲学的变体**：每章是独立的"小型知识单元"（README + Intruder + Images + Files），可单独被搜索引擎抓取、被外部 Wiki 引用、被 Burp 直接打开；不存在"先看 1 才能看 2"的强制链路
- **贡献者友好优先于完美主义**：`_template_vuln/` 把"开新章"成本压到 copy-paste 5 分钟级；`CONTRIBUTING.md` 的 12 行硬规则保证新 PR 即便作者水平参差也不会污染主仓
- **明确不做什么**：不做成"商业工具"（保持 MIT）、不做成"教程网站"（不写长篇原理文）、不做成"教学平台"（不给完整靶场，仅列配套 Lab 列表）

### 战略意图

**AllTheThings 家族矩阵**：按攻击者接触面垂直化分仓：Web（外部打点）→ AD/内网（内部横移）→ 硬件（物理层）。`Active Directory Attack.md` 单文件命中 246 次修改后被拆分到 `InternalAllTheThings`（2.2k ⭐），即"按领域深耕"而非"按主题堆量"的明证。**「文档 + 工具」双轮**：不只做文档（PAT/IATT/HATT），还做配套工具（SSRFmap / GraphQLmap），让读者在仓库内闭环完成「看方法 → 跑工具」。**开源策略** = genuinely open（MIT，可 fork/可商用），非 open-core；Sponsors（SerpApi / ProjectDiscovery / Vaadata）说明有可持续赞助现金流但无 SaaS 化或商业版打算。

## 核心价值提炼

### 创新之处

1. **占位符驱动的安全 PoC 系统** — `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `id` 替代 `rm -rf` 等破坏性命令；占位符本身不新，但作为强制的 PR 准入规则写进 `CONTRIBUTING.md` 并配合 `.markdownlint` 在 CI 中执行——这是工程化打包。**新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5**
2. **双消费格式（`Intruder/*.fuzz` 直接喂 Burp）** — 对 SecLists 的"差异化反击"——SecLists 只有字典，PAT 给"字典 + 用法"且字典在 Burp 里拖入即用。**新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5**
3. **章节模板 + 同构目录的「贡献者零门槛」** — `_template_vuln/` + `README + Intruder + Images + Files` 四元组；README-as-template 是社区老做法，但 PAT 把"开新章节成本压到 5 分钟"做到极致。**新颖度 2/5 | 实用性 5/5 | 可迁移性 5/5**
4. **AllTheThings 家族矩阵（按攻击面垂直化分仓）** — 把单一超级仓拆成 3 个聚焦仓（PayloadsAllTheThings / InternalAllTheThings / HardwareAllTheThings），并通过 README 互相导流，是「知识仓库品牌化」的范例。**新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5**
5. **CI 仅做 Markdown Lint，不做内容 Lint** — 承认"内容正确性无法被机器验证"，把 lint 收敛到格式层，专注可控质量门——是文档型项目的成熟工程取舍。**新颖度 2/5 | 实用性 4/5 | 可迁移性 3/5**

### 可复用的模式与技巧

- **章节模板系统**（`_template_vuln/` + `CONTRIBUTING.md` 同步）— 适用场景: 任何 > 20 篇、贡献者 > 5 人的长篇文档项目
- **占位符驱动的安全 PoC**（强制 PR 准入规则 + 配套 CI lint）— 适用场景: 安全工具/攻击载荷/红队 runbook/CTF writeup
- **双消费格式（人读 + 工具读）**（`Intruder/` 字典与 README 代码块同目录绑定）— 适用场景: 安全字典（Burp/ffuf 友好）、CI 配置（lint 规则 + 文档示例并行）、API 示例（README + OpenAPI spec）
- **MkDocs Material 文档站 + GitHub Pages 部署**（`mkdocs.yml` + `.github/workflows/mkdocs-build.yml`）— 适用场景: 任何 > 50 Markdown 文件的 GitHub 项目
- **「PR-Driven 协作，Issues = 0」模式**（用 PR + Discussion 替代 Issue 协作）— 适用场景: 长尾维护的知识仓库，避免 issue 噪声；法律责任敏感的知识库

### 关键设计决策

1. **目录结构即架构**：60+ 章节由不同贡献者维护，硬约束 `README.md + Intruder + Images + Files` 同构布局保证"读者用一套肌肉记忆走遍全仓"。**Trade-off**: 牺牲"按漏洞族聚类"语义层次灵活性，换"零学习成本扩展"。**可迁移性: 高**
2. **占位符消毒系统**：`CONTRIBUTING.md` 硬性规定 6 类占位符（`id`/`whoami`/`[ATTACKER.DOMAIN.TLD]`/`10.10.10.10` 等），配合 `DISCLAIMER.md` 兜底。**Trade-off**: 少数"展示真实利用危害"的教学场景需绕开占位符，但通过 CONTRIBUTING 把"安全默认"提到 PR 阶段拦截。**可迁移性: 高**
3. **9.6 年长尾治理**："Issues = 0" + 接受开放 PR 排队；Hacktoberfest 集中收割（2019-10 73 / 2020-10 84 / 2021-10 125 / 2022-10 107 / 2024-11 75 单月 commit）。**Trade-off**: 单作者 burn out 风险高（Swissky 占 47.5%，`p0dalirius` 67 commits 远落后），但生态效应已形成、护城河强。**可迁移性: 中**

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | HackTricks | SecLists | OWASP WSTG | PentestMonkey |
|------|---------|--------|--------|--------|--------|
| 定位 | 实战 payload + 工具可消费字典 | 教科书式体系化百科 | 原料字典库 | 防御方法论 | 老牌 cheatsheet |
| Stars | 78K | ~10w+ | ~62k | ~7k | ~3k |
| 广度 | 60+ 漏洞类目 | 全栈（Web+AD+云+OSINT+社工） | 全谱（密码/子域/UA） | 30+ 主题 | ~6 主题 |
| 工具可消费 | ★★★★★（Burp `.fuzz` 拖入即用） | ★★ | ★★★★★ | ★ | ★★ |
| 维护活跃度 | ★★★★（9.6 年长尾） | ★★★★★ | ★★★★ | ★★★ | ★（停滞） |
| 贡献者规模 | 333 | >500 | 100+ | 50+ | 小型 |

### 差异化护城河

1. **payload 颗粒度 + 跨语言覆盖**：每漏洞下提供 Python/ASP/PHP/ASP.NET/Ruby/XSLT/Node 多语言变体，对内网 legacy 渗透极实用
2. **Burp Intruder 字典与漏洞章节同目录绑定**：行业普遍把字典和知识拆开存，PAT 装在同一个目录
3. **9.6 年沉淀的 reference 网络**：任何新进入者很难"复制"这层（author+title+date 四元组 + Wayback fallback）
4. **AllTheThings 家族矩阵 + 同作者三件套**（PayloadsAllTheThings / InternalAllTheThings / HardwareAllTheThings）：跨项目 reference 已落地
5. **结构同构 + 可预测的读者肌肉记忆**：60+ 章节用同一套目录布局，读者上手成本接近零

### 竞争风险

**最可能被 HackTricks 替代**——HackTricks 在体系化程度、多语言本地化（中/西/葡）、社区规模（>500 vs 333）上已经反超；若 HackTricks 引入"细粒度 payload 模块 + 跨语言覆盖"，PAT 的护城河会被压缩。**2025-2026 新议题跟进节奏放缓**（近 30 天 0 commits），新攻击类别（LLM/Agent 攻击、AI 工具链）若未及时纳入，可能被新晋竞品反超。

### 生态定位

处在「Bug Bounty 实战工具链」上游，渗透人员把 PAT 当 Burp 字典 + 报告 PoC 来源——这是「工具 + 知识」型生态位，与 HackTricks「教科书」型生态位互补不冲突；被 OWASP、PortSwigger 官方文档引用，已升级为"行业基础设施"。

## 套利机会分析

- **信息差**: ❌ **无套利空间**——78K stars + 9.6 年沉淀 + 行业基础设施定位，已是事实标准（de-facto cheatsheet），在 Pentest 圈接近"开荒者必备"，不是被低估标的
- **技术借鉴**: ✅ **借鉴价值极高**——章节模板系统、占位符消毒系统、双消费格式、MkDocs Material 部署模式、PR-Driven 协作模式 5 个可迁移模式可直接用于自己的文档/工具/安全项目
- **生态位**: ✅ **生态位明确**——填补"Web App 渗透 payload + 工具可消费字典"细分领域的空白，与 HackTricks「教科书」型生态位错位互补
- **趋势判断**: ⚠️ **增长放缓但护城河深**——近 30 天 0 commits 进入静默期；安全 AI Agent 自动化"查 payload"可能压缩 PAT 的"信息载体"价值，但 9.6 年沉淀的 reference 网络 + 行业基础设施定位难以被快速颠覆

## 风险与不足

- **单作者依赖风险高**：Swissky 占 47.5% commits，第二名 `p0dalirius` 仅 67 commits（远落后），存在显著的"作者 burn out → 仓库衰落"风险
- **新议题跟进节奏放缓**：近 30 天 0 commits、2025-2026 对 LLM/Agent 攻击、AI 工具链等新类别跟进慢，可能被新晋竞品反超
- **目录治理债务**：存在历史命名不一致（`XSS Injection/` vs `XSS injection/`，`Upload/` vs `Upload insecure files/`），说明分叉后未做归并
- **17 个 Open PR 排队处理**：协作流通率不高，新贡献者 PR 反馈周期可能较长
- **commit 语义化覆盖率低**：74.5% commit message 归入 "Other"，未来做 changelog 自动生成会很难
- **Payload 时效性**：部分 payload 基于旧版本框架/语言，新版本可能已被官方修复
- **合规/法律风险**：尽管有 `DISCLAIMER.md` 兜底，但敏感地区/平台对其内容仍可能有合规疑虑

## 行动建议

- **如果你要用它**: 渗透测试/红队/Bug Bounty 工作者必备字典源；`Intruder/*.fuzz` 可直接拖入 Burp 起步；建议结合 HackTricks 读"怎么打"、用 PAT 取"打什么"。**对比竞品**：要体系化教学用 HackTricks，要字典规模用 SecLists，要行业背书用 OWASP WSTG；要"实战细颗粒度 payload + 工具可消费字典"用 PAT。
- **如果你要学它**: 重点看 4 个文件——`_template_vuln/README.md`（贡献模板设计）、`CONTRIBUTING.md`（12 行硬规则）、`mkdocs.yml`（站点配置）、`.github/workflows/check-markdown.yml`（CI lint）；再扫一遍 `Methodology and Resources/Active Directory Attack.md`（246 次修改的核心资产）理解"高频迭代"是怎么发生的
- **如果你要 fork 它**: 三个改进方向——① 在 CI 加入 reference 链接失效检测（Wayback fallback 是被动，主动 Action 才能根治）；② 归并历史目录命名债务（XSS/Upload 重名问题）；③ 引入"新攻击类别追踪"流程（LLM/Agent 攻击、AI 工具链），避免被新晋竞品反超

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [https://deepwiki.com/swisskyrepo/PayloadsAllTheThings](https://deepwiki.com/swisskyrepo/PayloadsAllTheThings) |
| Zread.ai | 未收录 |
| 关联论文 | 无（Cheatsheet 类项目无学术论文关联） |
| 在线 Demo | [https://swisskyrepo.github.io/PayloadsAllTheThings/](https://swisskyrepo.github.io/PayloadsAllTheThings/)（GitHub Pages 文档版，MkDocs Material） |
