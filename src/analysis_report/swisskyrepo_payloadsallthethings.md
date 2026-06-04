# 9.6 年、78K star、零代码仓库：PayloadsAllTheThings 凭什么把渗透 payload 写成「行业基础设施」

> GitHub: <https://github.com/swisskyrepo/payloadsallthethings>

## 一句话总结

PayloadsAllTheThings 是一份**用 GitHub 仓库形态维护的渗透测试 payload 百科全书**——注释:代码 = 26:1 的「反常识」文档型项目，靠「模板化贡献 + 消毒占位符 + Burp 字典绑定」三件套，把 333 位陌生人变成 9.6 年可持续的搬运工，最终跻身 Bug Bounty 实战链条上游的事实标准。

## 值得关注的理由

- **重新定义「GitHub 仓库」**：零依赖、零 runtime、零测试，2,096 行代码 / 54,442 行注释，却拿下 78K star、333 贡献者、9.6 年长生命周期——这是一个**用代码托管平台做内容工程**的样本。
- **把「贡献门槛」标准化到极致**：`CONTRIBUTING.md` + `_template_vuln/` + markdownlint CI 把外部 PR 收敛成「复制 4 个空目录 + 填 4 个固定小节 + 跑一次 lint」——任何想建设众包内容库的人都能直接抄这套。
- **事实标准位**：Bug Bounty 圈渗透人员几乎人手一份；同作者三件套（PAT / IATT / HATT）覆盖 Web / AD / 硬件三大攻击面，是单人安全研究员的「方法论可复制」罕见样本。

## 项目展示

![项目 banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png)

> 瑞士十字 + 项目名 banner，是项目唯一的官方视觉资产；项目本质是 Markdown + 文本型 payload，无 demo 视频 / 架构图。

![贡献者头像墙](https://contrib.rocks/image?repo=swisskyrepo/PayloadsAllTheThings&max=36)

> 9.6 年累积的 333 位贡献者头像墙，是「众包可持续性」最直观的证据。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | <https://github.com/swisskyrepo/payloadsallthethings> |
| Star / Fork / Watcher | 78,184 / 17,037 / 1,961 |
| 代码行数 | 2,096 行（Python 61% / ASP.NET 9% / XSL 7% / SVG 5% / 其他 14%，实为多语种 payload 载体而非 Python 项目） |
| 注释/Markdown 行数 | 54,442 行（真正资产，**代码:文档 ≈ 1:26**） |
| 文件数量 | 293 个（绝大多数为 `.md` + `.fuzz`） |
| 项目年龄 | 115.7 个月（9.6 年，首提交 2016-10-18） |
| 总 commits | 2,185（首作者 Swissky 占 ~47.5%，前 10 贡献者占 ~65%） |
| 贡献者 | 333 人 |
| Fork/Star 比 | **21.8%**（远高于普通库 5-10%，说明被大量克隆走作实战参考） |
| 依赖 / 测试 / CI | 0 / 0 / 仅 markdownlint + mkdocs 部署 |
| License | MIT |
| 最近更新 | 2026-04-22 |
| 开发阶段 | 低维护（近 30 天 0 commit，90 天 12） |
| 开发模式 | 职业项目（weekend 27.1% < 35% 阈值，作者为 Red Team Operator 职业身份） |
| 热度定位 | **大众热门**（安全/渗透测试领域 Top 5） |
| 质量评级 | 内容 A / 文档 A- / 测试 N/A / CI B+ |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

- **账号**：swisskyrepo（昵称 Swissky），2015-04 注册，**11.1 年老账号**；bio 自述 **"Red Team Operator & Bug Hunter"**——身份完全公开。
- **影响力**：10,496 followers，13 个 following（"权威但克制的专家账号"形象）。
- **公开 13 个仓库**全部围绕渗透测试，构成**「AllTheThings 家族」**：
  - **PayloadsAllTheThings**（78.2k ⭐，Web 应用层，**本文主角**）
  - **InternalAllTheThings**（2.2k ⭐，内网/AD/红队基础设施）
  - **HardwareAllTheThings**（886 ⭐，硬件/IoT 渗透）
  - **SSRFmap**（3.6k ⭐，SSRF 自动化利用）
  - **GraphQLmap**（1.7k ⭐，GraphQL 渗透）
  - **Vulny-Code-Static-Analysis**（422 ⭐）、**Wordpresscan**（653 ⭐）、**WHID_Toolkit**（119 ⭐，WiFi HID 注入）
- **可信度证据**：HackerOne/Bugcrowd 公开漏洞报告；仓库被 **OWASP**、**PortSwigger Web Security Academy** 官方文档/培训大量引用。

### 问题判断

作者看到的是一个**「知识碎片化」+「学习成本高企」**的痛点：在 2016-2017 年（项目创建期），Web 渗透 payload 分散在 Twitter 推文、漏洞 Writeup 博客、Discord 频道、CTF writeup 论坛里——新人面对"我现在需要 WAF 绕过的 XSS payload"这种问题时，要么翻 50 条推文，要么自己造轮子。Swissky 用一份"经过审阅、可引用、可复现"的中心化文档型仓库**把这一信息差打掉**。时机选择上也精准——2016-2018 年正是 Bug Bounty 平台（HackerOne、Bugcrowd）爆发期，行业急需"作战手册"。

### 解法哲学

- **「集中即服务」**：把分散在推文/博客/议题的信息，**结构化、模板化、可引用**地集中起来。Swissky 干的是**给安全社区做"Arch Wiki for Web Pentest"**的事。
- **Unix 哲学的变体**：每章是独立的"小型知识单元"（README + Intruder + Images + Files），可单独被搜索引擎抓取、被外部 Wiki 引用、被 Burp 直接打开；不存在"先看 1 才能看 2"的强制链路。
- **贡献者友好优先于完美主义**：`_template_vuln/` 把"开新章"成本压到 copy-paste；`CONTRIBUTING.md` 的 12 行硬规则保证新 PR 即便作者水平参差也不会污染主仓。
- **明确不做什么**：不做成"商业工具"（保持 MIT）、不做成"教程网站"（不写长篇原理文）、不做成"教学平台"（不给完整靶场，仅列配套 Lab 列表）。

### 战略意图

- **AllTheThings 家族矩阵**是"按攻击者接触面"垂直化分仓：Web（外部打点）→ AD/内网（内部横移）→ 硬件（物理层）。**AD Attack.md 命中 246 次后被拆分到 InternalAllTheThings**（2.2k ⭐ 的姐妹项目）就是这一战略的明证——**家族是"按领域深耕"而非"按主题堆量"**，避免单仓臃肿。
- **「文档 + 工具」双轮**：Swissky 不只做文档（PAT/IATT/HATT），还做配套工具（SSRFmap / GraphQLmap），让读者在仓库内**闭环完成「看方法 → 跑工具」**。
- **开源策略** = **genuinely open**（MIT，可 fork/可商用），非 open-core。Sponsors 名单（SerpApi / ProjectDiscovery / Vaadata）说明有可持续的赞助现金流，但**无 SaaS 化或商业版**打算。

## 核心价值提炼

### 创新之处

1. **占位符驱动的安全 PoC 系统**（`[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `id` 替代 `rm -rf`）—— 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5。占位符本身不新，但作为**强制的 PR 准入规则**写进 `CONTRIBUTING.md`，并配合 `.markdownlint` 在 CI 中执行——**这是工程化打包**，值得任何含攻击内容的项目复刻。验证：`Command Injection/README.md` 中 `chrome '--gpu-launcher="id>/tmp/foo"'` 整段没有破坏性命令；全仓 37 处 `10.10.10.x` 引用。

2. **双消费格式（`Intruder/*.fuzz` 直接喂 Burp）** —— 新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5。这是 PAT 对 SecLists 的"差异化反击"——SecLists 只有字典，PAT 给"字典 + 用法"且字典在 Burp 里**拖入即用**。例：`Server Side Template Injection/Intruder/ssti.fuzz` 39 行 payload 一行一个，`SQL Injection/Intruder/` 下 21 个 `.txt`/`.fuzz` 文件。

3. **章节模板 + 同构目录的「贡献者零门槛」**（`_template_vuln/` + `README + Intruder + Images + Files` 四元组）—— 新颖度 2/5 | 实用性 5/5 | 可迁移性 5/5。README-as-template 是社区老做法，但 PAT 把"开新章节成本压到 5 分钟"做到极致。

4. **AllTheThings 家族矩阵（按攻击面垂直化）** —— 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5。把单一超级仓拆成 3 个聚焦仓（Web / 内网 / 硬件），并通过 README 互相导流，是**「知识仓库品牌化」**的范例。

5. **CI 仅做 Markdown Lint，不做内容 Lint** —— 新颖度 2/5 | 实用性 4/5 | 可迁移性 3/5。承认"内容正确性无法被机器验证"，把 lint 收敛到格式层，专注可控质量门——是文档型项目的成熟工程取舍。

6. **MkDocs Material 作为呈现层** —— 新颖度 2/5 | 实用性 4/5 | 可迁移性 5/5。在 `swisskyrepo.github.io/PayloadsAllTheThings/` 提供"左侧 TOC 永久可见 + 代码复制按钮 + 暗色模式 + 上次更新时间"的现代化阅读体验，对 50+ 章节的仓库是数量级提升。

### 可复用的模式与技巧

1. **章节模板系统**（`_template_vuln/` + `CONTRIBUTING.md` 同步）—— 适用场景：任何 > 20 篇、贡献者 > 5 人的长篇文档项目。
2. **占位符驱动的安全 PoC** —— 适用场景：安全工具 / 攻击载荷 / 红队 runbook / CTF writeup / 任何含可执行 payload 的文档。
3. **双消费格式（人读 + 工具读）** —— 适用场景：安全字典（Burp / ffuf 友好）、CI 配置（lint 规则 + 文档示例并行）、API 示例（README + OpenAPI spec）。
4. **MkDocs Material 文档站 + GitHub Pages 部署** —— 适用场景：任何 > 50 Markdown 文件的 GitHub 项目。
5. **「PR-Driven 协作，Issues = 0」模式** —— 适用场景：长尾维护的知识仓库，避免 issue 噪声；用 PR + Discussion 替代 Issue 协作。

### 关键设计决策

| 决策 | 问题 | 方案 | Trade-off | 可迁移性 |
|------|------|------|-----------|----------|
| 目录结构即架构（每章统一 4 元组） | 60+ 章节由不同贡献者维护，如何保证"读者用一套肌肉记忆走遍全仓"？ | 硬约束 `README.md + Intruder + Images + Files` + `_template_vuln/README.md` 脚手架 | 牺牲"按漏洞族聚类"语义层次灵活性，换"零学习成本扩展" | **高** |
| PoC 安全约束（占位符系统） | 数千条可执行 RCE/SSRF/SQLi payload，一旦被复制直接打生产环境 | `CONTRIBUTING.md` 硬性规定 6 类占位符（`id`/`whoami`/`[ATTACKER.DOMAIN.TLD]`/`10.10.10.10` 等），配合 `DISCLAIMER.md` 兜底 | 少数"展示真实利用危害"的教学场景需绕开占位符，但通过 CONTRIBUTING 把"安全默认"提到 PR 阶段拦截 | **高** |
| 双消费格式 | 知识仓库最常见的死法是"作者自己看得懂，读者/工具看不懂" | `Intruder/` 目录放纯字典文件（`.txt`/`.fuzz`），直接被 Burp/ffuf/wfuzz 消费 | 需要双轨维护（README 代码块 + Intruder 文件同步） | **高** |
| 无依赖 / 无测试 / 无 CI 构建 | 项目主体是 Markdown，不存在"运行时" | CI 只跑 `markdownlint-cli2` + `mkdocs gh-deploy`，`.markdownlint.json` 只关掉 4 条规则 | 放弃"自动化质量门槛"换取"零学习成本贡献"；质量靠社区人工 review | 中（仅适合"内容型"仓库） |
| 9.6 年长尾治理 | 单人主导 47.5%，无接班人风险 | "Issues = 0" + 接受开放 PR 排队；Hacktoberfest 集中收割 | 单作者 burn out 风险高；但生态效应已形成，护城河强 | 中 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | HackTricks | OWASP CheatSheet | SecLists | PentestMonkey |
|------|---------------------|------------|------------------|----------|---------------|
| 形态 | 文档型 payload 字典 | 自托管 wiki 百科 | 防御备忘单 | 纯字典库 | 老牌备忘单 |
| 覆盖广度 | Web 应用层 60+ 章节 | 全栈（Web+AD+云+OSINT+社工） | 30+ 安全主题 | 字典全谱（密码/子域/UA） | ~6 主题（SQLi+PrivEsc） |
| 颗粒度 | 细（payload + 绕过 + 工具文件） | 中（章节讲解） | 中（防御原则） | 细（仅字典） | 中（cheat sheet） |
| 工具可消费 | **是**（`.fuzz` 拖入 Burp） | 否（仅人读） | 否 | 是（Burp/ffuf/wfuzz） | 否 |
| 防御/攻击视角 | 攻击（含检测提示） | 攻击 | **防御** | 攻击 | 攻击 |
| 维护活跃度 | 90 天 12 commits | 高 | 高 | 偶发 | **停滞**（2010s 起） |
| 社区规模 | 333 贡献者 | **>500 贡献者** | OWASP 团队 | 100+ 贡献者 | 小型 |
| License | MIT | 混合（部分非商业） | CC BY-SA | MIT | 自由 |

### 差异化护城河

1. **payload 颗粒度 + 跨语言覆盖**：同一种漏洞下提供 Python/ASP/PHP/ASP.NET/Ruby/XSLT/Node 多种服务端语言变体——对企业内网 legacy 渗透极实用。
2. **Burp Intruder 字典与漏洞章节绑定**：行业普遍把字典和知识拆开存，PAT 把两者**装在同一个目录**——这一项 HackTricks 都没做到。
3. **9.6 年沉淀的 reference 网络**：`author+title+date` 四元组 + Wayback fallback——任何新进入者很难"复制"这层。
4. **品牌矩阵 + 同作者三件套**：跨项目 reference 已落地（PAT → IATT），方法是体系化的不是单点。
5. **结构同构 + 可预测**：读者用同一套肌肉记忆走遍全仓——这点 SecLists 的"原料堆"和 OWASP 的"原则堆"都做不到。

### 竞争风险

**最可能被替代**：HackTricks 在体系化、双语、社区规模上已经反超；若 HackTricks 引入"细粒度 payload 模块 + 跨语言覆盖"，PAT 的护城河会被压缩。

**几乎不可能被替代**：PEASS-ng（仅提权单点）、PayloadBox（无方法论）、OWASP（防御视角）——这些是错位竞争，不构成直接威胁。

### 生态定位

PAT 处在 **「Bug Bounty 实战工具链」上游**：渗透人员把 PAT 当 Burp 字典 + 报告 PoC 来源——这是「工具 + 知识」型生态位，与 HackTricks「教科书」型生态位**互补不冲突**。被 OWASP、PortSwigger 官方文档引用即是明证——已经升级为"行业基础设施"。

## 套利机会分析

- **信息差**：项目本身是**严重被高估**而非被低估——78K star 中相当比例是被 Hacktoberfest 营销和"清单"型内容吸引的低信号 Star（大量安全学生 / Cert 备考者），实际"看过 / 用过 / 贡献过"的比例远低于 star 数。**但作为方法论样本被严重低估**——它示范了"内容型 GitHub 项目的可持续治理"这件事，目前中文圈几乎没有对等讨论。
- **技术借鉴**：`_template_vuln/` + `CONTRIBUTING.md` + `markdownlint CI` 这一套是**可立刻抄到任何内容型项目**的工程范式；占位符消毒字典可移植到任何带可执行 payload 的文档；PR-only 治理姿态适合法律责任敏感的知识库。
- **生态位**：填补了「渗透实战 payload 字典」这一空白——HackTricks 偏教科书、PEASS-ng 偏工具、OWASP 偏防御，PAT 占据「实战最细颗粒度 payload」这个缝隙。
- **趋势判断**：渗透测试 / Bug Bounty 行业仍在增长，PAT 不会衰退；但若 HackTricks 跟进"细粒度 payload 模块"，PAT 需要靠"模板化贡献 + 消毒占位符 + Burp 字典绑定"这套**已经形成的网络效应**继续拉差距——这是它**真正的后发优势**而非代码本身。

## 风险与不足

1. **零代码 = 零测试**：2,096 行 Python 不是生产代码，只是 SSTI/反序列化利用示例；payload 失效 / 链接 404 完全靠社区发现。
2. **目录治理债务**：XSS Injection / XSS injection 大小写并存、Upload / Upload Insecure Files 命名不一致，9.6 年累积（核心文件热力分析已识别此问题）。
3. **审核节奏慢**：17 个 open PR 持续累积，Swissky 倾向"少而精"——新 PR 排队时间长。
4. **依赖单一作者**：Swissky 一个人占 47.5% commits，若作者精力转移，PAT 维护质量会快速下降；接班人 `p0dalirius` 67 commits 远落后。
5. **法律灰带**：武器化仓库虽然在 `DISCLAIMER.md` 立了 8 条免责，但在某些司法辖区仍可能有法律风险。
6. **commit_type_distribution 失真**：`other 74.5%` 说明 74.5% 的 commit 是"加 payload 片段"而非传统 feature/fix——这是知识库型项目的元数据特征，但**也让 commit log 难以提供有意义的 changelog**。
7. **2025-2026 新议题跟进节奏放缓**：近 30 天 0 commits，新攻击类别（LLM/Agent 攻击、AI 工具链）若未及时纳入，可能被新晋竞品（如 `L1B0RTools` 类 AI 攻击字典）反超。

## 行动建议

- **如果你要用它**：Bug Bounty 实战 / CTF 现场 / 需要可直接复制的 payload → 选 PAT；入门 / 系统学习 / 需要更宽攻击面 → 选 HackTricks。**两者协同用** 而不是二选一。
- **如果你要学它**：重点关注三个文件——`CONTRIBUTING.md`（贡献治理范式）、`_template_vuln/README.md`（降低贡献门槛的模板）、`mkdocs.yml` + `.github/workflows/mkdocs-build.yml`（双入口部署）。这 4 个文件是 PAT 工程范式的精华。
- **如果你要 fork 它**：可以改进的方向——① 清理目录治理债务（XSS Injection / Upload Insecure Files 等）；② 把 17 个 open PR 排序 + 引入维护者小组；③ 加 GitHub Action 自动检测失效 reference 链接（比 Wayback fallback 更主动）；④ 把 `other 74.5%` 的 commit 重新分类为 `docs:` 语义化，改进 changelog 质量。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | [已收录](https://zread.ai/swisskyrepo/payloadsallthethings)（提供 Quick Start / Repository Navigation / XSS Injection / Pentest Methodology / Labs and Practice Platforms 五大导读页） |
| 关联论文 | 无（工程实践型知识库，无学术对应） |
| 在线 Demo | <https://swisskyrepo.github.io/PayloadsAllTheThings/>（MkDocs Material 渲染版，可视作在线 Demo） |
| 配套靶场 | `Labs and Practice Platforms` 一章列出 HackTheBox / TryHackMe / PortSwigger Web Security Academy / DVWA / bWAPP / DVIA / SQLi-Labs / Hack The Box Academy / PentesterLab |
| 同作者姊妹项目 | [InternalAllTheThings](https://github.com/swisskyrepo/InternalAllTheThings)（AD/内网） / [HardwareAllTheThings](https://github.com/swisskyrepo/HardwareAllTheThings)（硬件） |

---

**分析说明**：
- 本次分析以 `tmp/repo-facts-payloadsallthethings.json`（schema_version 2）的 `network` / `code_scale` / `dev_rhythm` / `evolution` / `contributors` 块为唯一数据底座，所有数字均来自该 JSON。
- 外部深度视角：WebSearch 不可用，仅使用 zread.ai 作为外部解读源。
- 报告生成时间：2026-06-04（基于 `code_scale.collected_at` 与 `dev_rhythm.last_commit.date` = 2026-04-22）。
