# 9 年 78K stars：一份「payload 字典」如何成为安全行业的基础设施

> GitHub: https://github.com/swisskyrepo/payloadsallthethings

## 一句话总结
`PayloadsAllTheThings` 把渗透测试中碎片化的 payload、bypass、cheatsheet 集中成一份「人读 + Burp 直接吃」的双消费字典，9.6 年沉淀为 333 位贡献者共建的渗透测试行业基础设施。

## 值得关注的理由
- **真正的「行业事实标准」**：78K stars、9.6 年长尾维护、333 位贡献者，被 OWASP、PortSwigger 官方文档引用，是 Bug Bounty 实战中事实上的渗透 payload 字典。
- **「双消费格式」教科书案例**：README 给人看，`Intruder/*.fuzz` 拖入 Burp Intruder 就能跑——同一份内容服务两类消费者，333 位贡献者涌入的关键设计。
- **可复用模式宝库**：占位符消毒系统、四元组 reference + Wayback 兜底、模板化贡献者零门槛、家族矩阵分仓——8 个可迁移模式可复用到任何长篇文档/知识库项目。

## 项目展示

1. ![banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png) — 类型: hero（仓库顶图，标志性 "AllTheThings" 视觉）
2. ![contributors](https://contrib.rocks/image?repo=swisskyrepo/PayloadsAllTheThings&max=36) — 类型: screenshot（自动生成的贡献者墙）

> GitHub Pages 镜像提供浏览版：https://swisskyrepo.github.io/PayloadsAllTheThings/

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/payloadsallthethings |
| Star / Fork | 78,208 / 17,044 |
| 监控 | 1,962 Watchers |
| 「代码行数」 | 2,096 行真代码 + 54,442 行 payload/注释（Python 61.1%, ASP.NET 9.0%, XSLT 7.0%） |
| 项目年龄 | 115.7 个月（约 9.6 年） |
| 总 commit | 2,185 次 |
| 贡献者 | 333 人（主作者 Swissky 占 47.5%） |
| 话题标签 | pentest, payload, bypass, web-application, hacking, vulnerability, bounty, methodology, privilege-escalation, penetration-testing, cheatsheet, security, enumeration, bugbounty, redteam, payloads, hacktoberfest |
| 开发阶段 | 低维护（近 30 天 0 commit, 90 天 12 commit） |
| 开发模式 | 职业项目（周末占比 27.1%，深夜占比 18.2%） |
| 热度定位 | 大众热门（垂直领域头部） |
| License | MIT |
| 质量评级 | 代码[中] 文档[优秀] 测试[N/A 文档型项目] |

> **关键校正**：「2,096 行代码」是误导性指标——本仓库 54,442 行「注释/Payload」才是核心资产。Python 占比最高是因 Burp Suite 扩展（.py）以及各分类目录下大量 Python 漏洞利用脚本片段；ASP.NET/ASP/PHP/Ruby 等多语言并存，每种语言都对应一类漏洞 PoC（不是项目本身依赖它们）。

## 作者视角：为什么存在这个项目

### 创始人/作者背景
- **Swissky (swisskyrepo)**，账号 11.1 年，自述「Red Team Operator & Bug Hunter」，独立开发者
- 运营多个 "AllTheThings" 知识体系仓库：**PayloadsAllTheThings**（Web/外部打点，78K ⭐）、**InternalAllTheThings**（AD/内网横移，2.2K ⭐）、**HardwareAllTheThings**（物理层，887 ⭐）——形成「AllTheThings」家族矩阵品牌
- 自研配套工具：SSRFmap / GraphQLmap / jsleak / Vulny-Code-Static-Analysis 等姊妹工具，被广泛采用
- 333 贡献者中主作者占 47.5%，前 10 名合计约 45%，**剩下 55% 由 320+ 社区贡献者分散贡献**——典型「核心驱动 + 社区投稿」模式
- Issue 面板已关闭（`open_issues: 0`），改用 PR + Discussion 模式沟通；当前有 17 个 open PR 排队

### 问题判断
Swissky 在 2016 年前后的红队/Bug Bounty 实战中，发现渗透测试 payload 存在**三重信息摩擦**：

1. **碎片化**——优质 payload 散落在推文、博客、Discord、CTF 论坛，没有集中入口
2. **不可复现**——博客中贴的 payload 经常因 WAF 升级或框架迭代而失效，但没有版本/时间戳标注
3. **不可引用**——漏洞报告里需要引用 PoC 来源时，找不到权威可引用的链接

这三重摩擦导致**新人学习曲线陡、老人重复造轮、跨团队知识传递低效**。叠加 HackerOne/Bugcrowd 平台爆发期带来的「作战手册」刚需，这个动机具有强烈的「供给侧补缺」属性。

### 解法哲学
Swissky 的解法可以概括为「**四件套**」：

- **「集中即服务」（Centralization as a Service）**：把分散信息结构化、模板化、可引用地集中起来，参考 Arch Wiki 范式（章节化 + 可预测导航 + 一致风格）
- **「模板化贡献者零门槛」（Contributor-First）**：`_template_vuln/` 把「开新章节」成本压到 copy-paste 5 分钟级
- **「双消费格式」（Human-Readable + Tool-Readable）**：README 是给人看的，`Intruder/*.fuzz` 是给 Burp 吃的——同一目录绑定两种消费者
- **「明确不做什么」（Disciplined Scope）**：不做成商业工具（保持 MIT）、不做成教程网站（不写长篇原理）、不做成教学平台（不给完整靶场，仅列配套 Lab 列表）——这种**克制**让它能 9.6 年专注一个领域

### 战略意图
Swissky 的战略图景是「**AllTheThings 家族矩阵**」：按攻击者接触面垂直化分仓，三个仓库共享同一套目录/命名/贡献规范，构成「知识仓库品牌化」的范例。

更深层的战略是「**文档 + 工具双轮**」：不只做文档（PAT/IATT/HATT），还做配套工具（SSRFmap / GraphQLmap / Vulny-Code-Static-Analysis），让读者在自家生态内闭环完成「**看方法 → 跑工具**」。Sponsors（SerpApi / ProjectDiscovery / Vaadata）说明有可持续现金流但**无 SaaS 化或商业版打算**——genuine open（MIT + Sponsors）模式，而非 open-core 模式。

## 核心价值提炼

### 创新之处

1. **占位符驱动的安全 PoC 系统（Sanitization-First Contribution）** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   把 6 类占位符（`id`/`whoami`/`[ATTACKER.DOMAIN.TLD]`/`10.10.10.10`/`Administrator`/`P@ssw0rd`/`DC01`）作为**强制 PR 准入规则**写进 `CONTRIBUTING.md`，并配合 `.markdownlint` 在 CI 中执行格式校验。占位符概念不新，但作为**制度化、工程化、CI 强制化**的 PR 准入门槛是 PAT 的创造。

2. **双消费格式：人读 + 工具读（Human-Readable + Tool-Readable）** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5
   README 是给人看的（Markdown 渲染 + TOC + 代码块），`Intruder/*.fuzz` 是给 Burp 吃的（直接拖入 Burp Intruder 当字典）。同一目录下「**人 + 工具**」两种消费者，原子化绑定。**这是对 SecLists 的「差异化反击」**——SecLists 只有字典，PAT 给「字典 + 用法」且字典在 Burp 里拖入即用。

3. **章节模板 + 同构目录的「贡献者零门槛」系统** — 新颖度 2/5 | 实用性 5/5 | 可迁移性 5/5
   `_template_vuln/` 提供「Tools/Methodology/Labs/References」四段式结构 + `Intruder/`/`Images/`/`Files/` 子目录约定。贡献者只需「**复制 `_template_vuln/` → 改名 → 填内容 → 提 PR**」即可，新章节成本压到 5 分钟级。

4. **AllTheThings 家族矩阵：按攻击面垂直化分仓** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
   把「单一超级仓」按攻击者接触面垂直化分仓——**PayloadsAllTheThings（外部 Web 打点）/ InternalAllTheThings（AD/内网横移）/ HardwareAllTheThings（物理层）**。三个仓共享目录/命名/贡献规范，通过 README 互相导流。

5. **Reference 四元组 + Wayback Machine 兜底（author + title + date + link）** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5
   每条 reference 必须有 `author`、`title`、`link`、`date` 四元组，链接失效时强制使用 Wayback Machine 兜底。9.6 年沉淀形成可搜索、可验证、长期可引用的 reference 网络。

6. **「PR-Driven 协作 + Issues = 0」模式** — 新颖度 2/5 | 实用性 4/5 | 可迁移性 3/5
   关闭 issue 入口，强制所有协作走 PR + Discussion 通道。GitHub Issues 在长尾维护项目中常被滥用（提问/吐槽/法律灰色需求），关闭 issue 入口把协作收敛到「**可审阅的代码/内容变更**」这一可管理通道。

### 可复用的模式与技巧

| # | 模式名 | 适用场景 |
|---|--------|----------|
| 1 | **「Sanitization-First Contribution」占位符消毒系统** | 安全工具、攻击载荷库、红队 playbook、CTF writeup 平台、PoC 集合 |
| 2 | **「四元组 Reference + Wayback 兜底」可引用性制度** | 知识库、文档站、教程集、学术综述、新闻聚合、案例库 |
| 3 | **「README + 同构子目录 + 模板脚手架」贡献者零门槛系统** | 长篇文档项目、知识库、API 文档、教程集合、Wiki 站点、组件库 |
| 4 | **「双消费格式：人读 + 工具读」同目录绑定** | 安全字典库、API 文档、CI 配置、UI 组件库、配置 schema 库 |
| 5 | **「MkDocs Material + GitHub Pages」文档站部署** | 任何 > 50 Markdown 文件的 GitHub 项目 |
| 6 | **「Format-Only CI + 人工内容 review」分层质量门** | 内容正确性需要人类专家判断的项目（安全知识库、医学/法律知识库） |
| 7 | **「家族矩阵 + 共享规范 + 跨仓导流」品牌化分仓** | 知识仓库品牌化、文档站分语言/分主题分仓、案例库分行业分仓 |
| 8 | **「PR-Driven + Issues = 0」长尾维护模式** | 长尾维护的知识仓库、法律责任敏感的知识库、企业内部 runbook |

### 关键设计决策

**决策 1：目录结构即架构（同构四元组 README + Intruder + Images + Files）**
- **问题**：70+ 章节由不同贡献者分散维护，如何保证「读者用一套肌肉记忆走遍全仓」？
- **方案**：硬约束每个漏洞目录必须包含 `README.md`（人读）+ `Intruder/`（Burp 字典）+ `Images/`（截图）+ `Files/`（附件）四元组，README 必须包含「Tools / Methodology / Labs / References」四段式结构
- **Trade-off**：牺牲「按漏洞族聚类」的语义层次灵活性，换取「零学习成本扩展 + 搜索引擎友好 + 工具可直接 walk 目录」的多重收益
- **可迁移性**：高

**决策 2：占位符消毒系统（Sanitization-First Contribution）**
- **问题**：渗透 payload 在 PR 阶段若被嵌入真实攻击命令，可能成为「恶意代码传播源」+「法律风险敞口」
- **方案**：`CONTRIBUTING.md` 硬性规定 6 类占位符，配合 `DISCLAIMER.md` 兜底「教育/研究用途」声明
- **Trade-off**：少数「展示真实利用危害」的教学场景需要绕开占位符，但通过把「安全默认」提到 PR 准入阶段拦截，把人工 review 压力降到最低
- **可迁移性**：高

**决策 3：CI 仅做 Markdown Lint，不做内容 Lint**
- **问题**：文档型项目如何在「自动化质量门」与「不过度限制贡献者」之间取得平衡？
- **方案**：`check-markdown.yml` 用 `DavidAnson/markdownlint-cli2-action` 仅做格式层 lint，不做内容正确性检查
- **Trade-off**：牺牲「内容质量」自动化兜底（错别字、过期 payload、错误命令无法被 CI 发现），换取「贡献者零摩擦 + 维护者精力集中在内容审核 + 承认机器无法验证攻防正确性」的工程成熟度
- **可迁移性**：中-高

**决策 4：MkDocs Material + GitHub Pages 文档站**
- **问题**：60+ Markdown 文件如何在「GitHub 在线浏览」之外提供更好的阅读体验？
- **方案**：`mkdocs.yml` 配置 Material 主题（左侧 TOC、代码复制按钮、暗色模式 toggle、navigation.tracking 锚点跟踪）+ `.github/workflows/mkdocs-build.yml` 自动部署到 `swisskyrepo.github.io/PayloadsAllTheThings`
- **Trade-off**：引入 MkDocs 工具链依赖，但获得「左导航 + 全文搜索 + 移动端友好 + 复制代码按钮 + 锚点定位」等 GitHub Web UI 缺失的能力
- **可迁移性**：高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | OWASP/CheatSheetSeries | HackTricks | foospidy/payloads |
|------|---------------------|------------------------|-----------|------------------|
| 定位 | 实战 payload + 工具可消费字典 | 防御方法论 + 编码建议 | 教科书式体系化百科 | 纯 payload 字典集合 |
| Stars | 78,188 | 30k+ | ~10w+（已反超） | 2k+ |
| 工具可消费 | ★★★★★（Burp `.fuzz` 拖入即用） | ★（纯文档） | ★★（偶尔有字典） | ★★★★（纯字典） |
| 维护活跃度 | 9.6 年持续更新 | 慢，部分 CheatSheet 数年级 | 活跃 | 数年级停滞 |
| 内容广度 | 60+ Web 漏洞类目 | 防御视角全覆盖 | Web + AD + 云 + OSINT 全栈 | 2-3 个类目 |
| 体系化程度 | ★★★（按漏洞分章节） | ★★★★ | ★★★★★（强 TOC + 攻击链） | ★（仅字符串） |
| 社区规模 | 333 贡献者 | 多公司委员会 | >500 贡献者 | N/A |
| 行业地位 | 被 Burp 官方引用 | 行业标准 | 体系化教科书 | 被替代中 |

### 差异化护城河

1. **payload 颗粒度 + 跨语言覆盖** — Python/ASP/PHP/ASP.NET/Ruby/XSLT/Node 多语言变体，对内网 legacy 渗透极实用，HackTricks/OWASP 都未做到
2. **Burp Intruder 字典与漏洞章节同目录绑定** — 行业普遍把字典和知识拆开存，PAT 装在同一个目录，工具消费零摩擦
3. **9.6 年沉淀的 reference 网络** — 「author + title + date + Wayback fallback」四元组 reference 体系，是任何新进入者用 2-3 年时间难以复制的「时间型护城河」
4. **AllTheThings 家族矩阵** — PAT / IATT / HATT 三仓共享规范 + 跨项目导流，形成「品牌即生态」效应
5. **结构同构 + 可预测的读者肌肉记忆** — 60+ 章节用同一套目录布局，读者上手成本接近零

### 竞争风险

1. **最可能被 HackTricks 替代** — HackTricks 在体系化程度、多语言本地化（中/西/葡）、社区规模（>500 vs 333）上已经反超；若 HackTricks 引入「细粒度 payload 模块 + 跨语言覆盖」，PAT 的护城河会被压缩
2. **新议题跟进节奏放缓** — 近 30 天 0 commits 进入静默期；新攻击类别（LLM/Agent 攻击、AI 工具链、GraphQL/Async API 攻击）若未及时纳入，可能被新晋竞品反超（2024-11 出现的 75 次非典型高峰暗示新一波"重型重构/方法论更新"窗口正在酝酿）
3. **单作者依赖风险** — Swissky 占 47.5% commits，第二名 `p0dalirius` 仅 67 commits（远落后），存在显著的「**作者 burn out → 仓库衰落**」风险
4. **目录治理债务** — 历史命名不一致（`XSS Injection/` vs `XSS injection/`、`Upload/` vs `Upload insecure files/`），分叉后未做归并

### 生态定位
处在「**Bug Bounty 实战工具链**」上游，渗透人员把 PAT 当 **Burp 字典 + 报告 PoC 来源**——这是「**工具 + 知识**」型生态位，与 HackTricks「**教科书**」型生态位互补不冲突；被 OWASP、PortSwigger 官方文档引用，已升级为「**行业基础设施**」。建议读者画像：「**渗透测试/红队/Bug Bounty 工作者**」 + 「**需要快速获取 Burp 可用 payload 的安全工程师**」。

## 套利机会分析
- **信息差**：不存在套利空间。78K+ stars 的事实使其已进入「被引证对象」层级，竞品难以撼动其心智占位；新进入者只能做「细分增量」（如 LLM/Agent 攻击、AI 工具链 PoC）
- **技术借鉴**：8 个可迁移模式（占位符消毒、四元组 reference、模板脚手架、双消费格式、MkDocs 部署、Format-Only CI、家族矩阵、PR-Driven 协作）可直接复用到任何长篇文档/知识库/工具集项目
- **生态位**：在「文档型 GitHub 项目」中占据「工程化文档项目的天花板」位置——9.6 年持续维护 + 333 贡献者 + 双消费格式 + 模板化贡献系统的组合，是「GitHub 知识仓库」型项目的标杆
- **趋势判断**：近 30 天 0 commits 进入静默期，新攻击类别（LLM/Agent 攻击）跟进慢，存在被 HackTricks 等新晋竞品在「细粒度 payload + 跨语言覆盖」方向反超的风险；但 9.6 年沉淀的 reference 网络仍是难以快速复制的护城河

## 风险与不足

- **单作者 burn out 风险**：Swissky 占 47.5% commits，第二名 `p0dalirius` 仅 67 commits（远落后），核心维护高度依赖单一作者
- **新议题跟进放缓**：近 30 天 0 commit，新攻击类别（LLM/Agent 攻击、AI 工具链、GraphQL/Async API 攻击）跟进慢
- **目录治理债务**：`XSS Injection/` vs `XSS injection/`、`Upload/` vs `Upload insecure files/` 历史命名不一致，分叉后未做归并
- **Open PR 排队**：17 个 Open PR 排队，协作流通率有提升空间
- **缺乏结构化 changelog**：74.5% commit message 归「Other」（"Update xxx.md"、"Add payload for xxx"），无 CHANGELOG.md 维护
- **法律责任敏感**：渗透 payload 涉及法律灰色地带，`DISCLAIMER.md` 声明「教育/研究用途」是必要但非充分的保护

## 行动建议

### 如果你要用它
**渗透测试/红队/Bug Bounty 工作者必备字典源**：
- `Intruder/*.fuzz` 可直接拖入 Burp Intruder 起步
- 建议结合 **HackTricks** 读「**怎么打**」、用 **PAT** 取「**打什么**」
- 报告 PoC 来源引用时，PAT 的四元组 reference（含 Wayback 兜底）可作为可引用来源

### 如果你要学它
重点看 4 个文件，理解「**文档型 GitHub 项目**」的工程化范式：
1. **`_template_vuln/README.md`** — 贡献模板设计，看「贡献者零门槛」怎么做
2. **`CONTRIBUTING.md`** — 12 行硬规则 + 章节格式 + PR 流程
3. **`mkdocs.yml`** — 站点配置，看「Material 主题 + 自动化部署」怎么搭
4. **`.github/workflows/check-markdown.yml`** — CI lint，看「Format-Only CI」怎么落地

再扫一遍 `Methodology and Resources/Active Directory Attack.md`（246 次修改的核心资产）理解「**高频迭代**」是怎么发生的。

### 如果你要 fork 它
三个改进方向（按优先级）：

1. **在 CI 加入 reference 链接失效检测** — Wayback fallback 是被动，主动 Action 才能根治「链接腐烂」
2. **归并历史目录命名债务** — 清理 `XSS Injection`/`XSS injection`、`Upload`/`Upload insecure files` 重复目录
3. **引入「新攻击类别追踪」流程** — LLM/Agent 攻击、AI 工具链、GraphQL/Async API 攻击等新议题，避免被新晋竞品反超

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录（项目为纯 Markdown 知识库，不适合 DeepWiki 自动抽取代码结构） |
| Zread.ai | 未收录 |
| 关联论文 | 无（纯实战工程类项目，无学术论文） |
| 在线 Demo | https://swisskyrepo.github.io/PayloadsAllTheThings/（GitHub Pages 镜像站） |
| 姊妹项目 | https://github.com/swisskyrepo/InternalAllTheThings（AD/内网） |
| 姊妹项目 | https://github.com/swisskyrepo/HardwareAllTheThings（物理层） |
| 配套工具 | https://github.com/swisskyrepo/SSRFmap |
| 配套工具 | https://github.com/swisskyrepo/GraphQLmap |
