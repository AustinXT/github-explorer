# 9.6 年 78K Star：一位 Red Teamer 把「渗透手册」做成 GitHub 事实标准

> GitHub: https://github.com/swisskyrepo/payloadsallthethings

## 一句话总结
一个 Red Team Operator 用了 9.6 年、2,185 次 commit、333 位贡献者共同堆出的 5.4 万行 Markdown 安全百科，把「漏洞说明 + 可直接复制的 payload + Burp 字典 + 绕过手法」打包成 Web 渗透的事实标准离线手册。

## 值得关注的理由
- **78K Star + 17K Fork，Fork/Star 比例 22%（健康值 2-3 倍）**——这不是"收藏欣赏型"仓库，而是 pentester 出门作业前的「行前必 clone 清单」。
- **「一个内容架构，N 个垂直版本」的产品化打法**：作者 Swissky 把它复用到 InternalAllTheThings（2.2K）、HardwareAllTheThings（887），并对高价值条目（SSRF/GraphQL）工具化成独立 Python 项目（SSRFmap 3.5K、GraphQLmap 1.6K）。
- **与传统软件工程指标完全脱钩**：代码只有 2,096 行（且分散在 12 种语言里做 PoC），注释/Markdown 反而是 54,442 行；这是一份「内容仓库」，传统的「代码行数 / 测试覆盖率 / refactor 比例」在这里全部失效。

## 项目展示

![PayloadsAllTheThings Banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png) — 官方 Hero Banner，项目视觉资产

> 仓库为纯 Markdown 知识库，无 Demo 视频或架构图。额外媒体（4 张赞助商头像）已转写为下方的「生态背书」表格。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/payloadsallthethings |
| Star / Fork | 78,210 / 17,045（Fork/Star = 21.8%，是普通项目的 2-3 倍） |
| Watcher / Open Issue / Open PR | 1,962 / 0 / 17 |
| 代码行数 | 2,096 行可执行代码 + 54,442 行 Markdown（注释/代码比 26:1） |
| 主语言 | Python 61%（占「代码」行数，实际是 PoC 多语言碎片），仓库「真实语言」是 Markdown |
| 项目年龄 | 115.7 个月（≈ 9.6 年，2016-10-18 首次提交） |
| 最近推送 | 2026-04-22 |
| 开发阶段 | 低维护 / 已完工成熟期（月均 commit 从历史 18.9 降至 8.75） |
| 贡献模式 | 单一权威 + 长尾社区（Swissky 47.5%，Top 10 约 50%，333 贡献者兜底） |
| 热度定位 | 大众热门（Web 渗透细分领域的事实标准） |
| License | MIT |
| 质量评级 | 文档：优秀（54K Markdown + lint 工具链）/ 代码：N/A（PoC 一次性）/ 测试：N/A（无 runtime 逻辑） |
| 协议 | MIT（武器级内容 + README 免责声明组合是该子领域标准做法） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
- **Swissky**（`swisskyrepo`），自我描述「Red Team Operator & Bug Hunter」，入站 11.1 年（2015-04）
- 10,500 粉丝、13 公开仓库——典型「广播型」账号，不互关、不运营纯关注网络
- **「5-Repo 帝国」策略**：同一套「README + Intruder/ + Images/ + Files/」四件套模板，复制到 Web（PayloadsAllTheThings 78K）、内网/AD（InternalAllTheThings 2.2K）、IoT 硬件（HardwareAllTheThings 887）三个垂直领域；并把高价值条目工具化成独立 Python 项目（SSRFmap 3.5K、GraphQLmap 1.6K）
- 这是典型的「**知识资产产品化**」路径：先在主仓沉淀知识图谱，等某个条目具备工具化价值再 fork 出可执行工具

### 问题判断
**2016 年的安全知识生态是碎片化的**：
- OWASP CheatSheet 偏 defensive / secure coding 视角，是「该怎么修」不是「该怎么打」
- SecLists 是纯字典，**没有使用说明**
- 个人博客的 payload 散落各处，无版本、难搜索、易失效

**Swissky 抓到的是「one-stop」空白位**：payload（可复制字符串）+ methodology（怎么用）+ bypass（绕过手法）+ Burp Intruder 文件（直接喂给工具）四件套，是 2016 年没人做、但每个 Burp 用户都痛过的事。

### 解法哲学
作者明确选择了：
- **做知识而不是工具**：工具市场头部已被 sqlmap / nuclei / Burp 占据，新工具只能找垂直缝（如 SSRFmap）。知识市场 OWASP 慢、SecLists 缺方法、HackTricks 2019 年才起步——「**知识聚合 + 持续更新**」这条赛道没有王
- **不写 SaaS、不出书、不做付费课程**：走「**开源 + 赞助**」路线（GitHub Sponsors + SerpApi / ProjectDiscovery / Vaadata 三家），稀有度高于同行业大多数 red teamer 的「博客 + 副业」打法
- **4 件套模板而不是自由结构**：每个漏洞必须 `README.md + Intruder/ + Images/ + Files/`，降低贡献者学习成本（≤ 5 分钟就能 PR）
- **payload 卫生强制规约**：`id` / `whoami` 代替真实命令、`[ATTACKER.DOMAIN.TLD]` 代替真实域名——把行业 de facto 标准用 CONTRIBUTING.md 写成可机器检查的约定

### 战略意图
**作者真实目标可能是**：
1. **行业话语权**——每个 SSRF/XSS 报告的 reference 列表都会出现他的名字
2. **招聘/客户线索**（赞助是次要的）
3. **技术简历资产化**——78K Star 的公开资产比 LinkedIn 上的自我描述更可信

## 核心价值提炼

### 创新之处
按「新颖度 × 实用性」排序：

1. **「漏洞即文件夹」抽象**（新颖度 6/10，实用性 10/10，可迁移性 9/10）
   - 一个漏洞 = 一个文件夹 + 4 件固定子结构。用文件系统做 taxonomy——物理隔离、Git diff 友好、find 检索方便
   - 这个模式可直接迁移到 DevOps runbook、Incident Response Cheat Sheet、Cloud Security Playbook 等任何「知识聚合」项目

2. **payload 卫生强制规约 + Intruder 字典捆绑**（新颖度 7/10，实用性 10/10）
   - OWASP 给描述不给字典，个人博客给字典但没规约——PATT 把「人类阅读 + 机器消费」两步都做对了
   - 攻击者拖一个 `.txt` 到 Burp 就能用，省掉自己拼字典的时间

3. **「无 issue、全 PR」治理模型**（新颖度 5/10，实用性 8/10）
   - 0 open issue / 17 open PR——issue 看板事实上被 PR 取代
   - 适合「单一权威 + 长尾社区」的知识库项目，但代价是「内容错误难追踪」+「维护者合并速度决定贡献者留存」

4. **5 仓帝国模板复用**（新颖度 7/10，可迁移性 8/10）
   - 不是"开源项目矩阵"的常见打法（那种是 monorepo 拆 monorepo），而是从一开始就用「同模板不同垂直」的可复用资产
   - 适合任何想做「行业知识图谱」的个人研究者

5. **MkDocs Material + 增量 lint 工具链**（新颖度 4/10，实用性 9/10）
   - 一份 Markdown 同时是 GitHub 仓库 + 静态站点
   - `check-markdown.yml` 只 lint 改过的文件，避免 54K Markdown 全量扫描的性能问题——这是大文档仓库的范式

### 可复用的模式与技巧
1. **「_template_vuln」模板目录**——任何「按主题分章节」的知识库都可以套用：提供空模板 + 「复制 → 改名 → 填 4 节」的贡献引导
2. **增量 lint 策略**——大文档仓库的 GitHub Action 模板：只扫描 PR/push 中变更的 `.md` 文件
3. **跨仓迁移 + 留 redirect**——`Methodology and Resources/Methodology and enumeration.md` 内容已迁到 InternalAllTheThings，本仓只留 redirect。这是「知识库演化」的优雅做法
4. **payload 占位符规约**——任何「可复制片段」类仓库都可以用（代码片段库的 `[USERNAME]` 风格）
5. **大版本号 = 目录体系重构**——7 个 tag（1.0/2.0/2.1/3.0/4.0/4.1/4.2）、平均 1.4 年打一个。在内容仓库里，SemVer 的 major = 目录/章节体系重构，不是 API 破坏性变更

### 关键设计决策
1. **4 件套文件夹模板（README + Intruder + Images + Files）**
   - 问题：内容型仓库如何在「降低贡献门槛」和「结构一致」之间取平衡
   - 方案：强制 4 子结构，缺哪个一目了然
   - Trade-off：短漏洞（5 行）和长漏洞（800 行 SQLi）共用模板，过/欠配置；新文件夹在 GitHub Web UI 浏览不如单文件
   - 可迁移性：**高**——任何「分主题聚合」的知识库都能用

2. **MIT + 武器级内容组合**
   - 问题：武器级内容怎么发出去
   - 方案：MIT 最大化开放 + DISCLAIMER.md 三条「用户自负责任」条款
   - Trade-off：商业 WAF 厂商（Cloudflare/Akamai）可以直接拿 payload 做防御规则；少数 payload 可能被黑产复制
   - 可迁移性：中——只适用于「内容本身可独立验证、攻击性弱、需要广泛传播」的场景

3. **「无 issue、全 PR」治理**
   - 问题：社区贡献走哪条管道
   - 方案：放弃 issue 模板、17 PR 排队合并、内容错误走 issue、新增/修字走 PR
   - Trade-off：维护者合并速度直接决定贡献者留存；17 个开放 PR 是这种打法的「成本」
   - 可迁移性：**高**——任何「单一权威 + 长尾社区」的开源项目都可以考虑

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | HackTricks | OWASP CheatSheet | SecLists |
|------|---------------------|-----------|------------------|----------|
| Star | 78,210 | ~11,500 | ~30,000 | ~60,000 |
| 定位 | Web 漏洞 payload 库 | 渗透全领域百科（含 Linux PrivEsc / Network） | Defensive / Secure Coding 视角 | 纯字典资源 |
| 时间 | 2016 起步 | 2019 起步 | OWASP 长期项目 | danielmiessler 长期项目 |
| 更新频率 | 月均 8.75（稳定） | 更激进（周级多 commit） | 慢（OWASP 流程） | 偶尔补 |
| Payload 卫生规约 | 6 条强制（id/whoami/占位符…） | 不强制 | 不适用（defensive 视角） | 不适用 |
| Intruder 字典 | 内置（`.txt` 直接喂 Burp） | 不内置 | 不内置 | **本体**就是字典 |
| MkDocs 站点 | ✅ | ✅ | ✅（独立站） | ❌（GitHub only） |
| 主要消费场景 | 复制 payload 到 Burp | 翻 methodology 找思路 | 看 secure coding 规范 | 拉字典到工具 |
| 关系 | 事实标准 | 同期双子星 | 攻/防镜像 | 上游/下游互补 |

### 差异化护城河
- **网络效应**：78K Star + 17K Fork 形成的「行前必 clone 清单」惯性，新人入行不知道 PATT 会被同行视为菜鸟——这是 HackTricks 等后来者很难追的先发优势
- **内容深度 + 即用性双重护城河**：OWASP 有体系没 payload、SecLists 有字典没方法、HackTricks 广而不够深，PATT 在「Web 漏洞 + payload + 字典」这个交集上是唯一王者
- **作者本人是 Red Teamer**：内容来自真实施工，不是学术研究——这是「实战可复制」的根本保证

### 竞争风险
- **HackTricks 在 Linux PrivEsc / Network 协议层**已建立独立心智，PATT 在这两块明显薄弱。如果 HackTricks 也补上 Web 漏洞 payload 化的「Burp 字典捆绑」能力，会形成真正的全面威胁
- **AI 自动生成 payload** 的工具（如 GPT-4 辅助构造 bypass）正在降低「人手整理 payload」的价值——但这类工具的准确率仍远不如人工整理的 cheat sheet
- **Cloud WAF 厂商**（Cloudflare / Akamai）若把 PATT payload 全部纳入自家 WAF 规则，会让 PATT 里的 payload 失效——但这是「攻防共同进步」的常态，作者只需持续更新

### 生态定位
- **上游**：SecLists（字典来源）
- **下游**：ProjectDiscovery Nuclei 模板（PoC 转 Nuclei 模板的常见起点）、SerpApi（OSINT 数据）
- **平级**：HackTricks、OWASP CheatSheet、PortSwigger Web Security Academy
- **角色**：**Web 渗透领域的「事实标准离线手册」**——填补了 OWASP「防」与个人博客「散」之间的「攻的可复制知识」空白

## 套利机会分析
- **信息差**：❌ **不高**。这是大众热门（78K Star、Hacktoberfest 官方收录），已经不是被低估项目
- **技术借鉴**：✅ **极高**。「_template_vuln」+ 4 件套文件夹 + 增量 lint + 「无 issue 全 PR」治理——这套打法可以**直接平移到任何「按主题聚合」的知识库项目**（DevOps runbook、IR 手册、Cloud Security Playbook、内部合规手册）
- **生态位**：✅ 仍在「Web 渗透 payload 化」这个空白位上。HackTricks 在广度，PATT 在深度，未见真正能挑战的后来者
- **趋势判断**：⚠️ 进入**「成熟期低维护」**，月均 commit 从历史 18.9 降至 8.75，Hacktoberfest 补血效应从 2021-10 的 125 commit/月衰减到 2024-10 的 16 commit/月。商业上仍有空间（赞助、咨询），但技术红利已过爆发期

## 风险与不足
- **作者单点故障**：Swissky 一人 47.5%（或 34.3% by git log）的核心 commit 占比。若他停更，333 贡献者兜底不会让项目崩，但节奏会断崖
- **Hacktoberfest 红利衰减**：2021-10 单月 125 commit 跌到 2024-10 单月 16，外部补血机制正在弱化
- **目录大小写不统一**：`XSS Injection/` vs 历史 `XSS injection/` 并存，Git 大小写不敏感导致改名会断链
- **缺乏 Issue 模板和 PR 模板**：与「无 issue 全 PR」治理一致，但对「内容错误」类反馈追踪能力弱
- **无 Changelog**：版本变更依赖 git log + 47.5% 集中贡献纪律，对新人不友好
- **武器级内容争议潜在性**：MIT + payload 的组合虽在该子领域是标准做法，但任何一次大 CVE 事件都可能让项目被舆论质疑

## 行动建议
- **如果你要用它**：直接 clone（**不是 Star**），用 MkDocs 站点的全局搜索（`swisskyrepo.github.io/PayloadsAllTheThings/`）+ Burp 字典导入，是当前最高效的 Web 渗透工作流
- **如果你要学它**：
  - **重点关注**：`CONTRIBUTING.md:13-19`（payload 卫生规约）、`README.md:19-24`（4 件套模板）、`mkdocs.yml`（Material 主题配置）、`.github/workflows/check-markdown.yml`（增量 lint 模板）
  - **重点关注**：`Methodology and Resources/Methodology and enumeration.md`（跨仓迁移 + redirect 范例）
  - **避免模仿**：1.7 万个 fork 这种「被当工具书」的消费方式不可强求——它是 9.6 年沉淀 + Red Team 圈子共识的结果
- **如果你要 fork 它**：
  - **可改进方向**：① 拆 4 件套为可参数化模板（解决短漏洞过配置问题）；② 加 Issue 模板追踪「内容错误」；③ 补 HackTricks 擅长的 Linux PrivEsc / Network 章节
  - **不建议**：① 改成 SaaS 收费（与社区治理冲突）；② 出付费课程（与作者开源路线冲突）；③ 拆 monorepo 拆出 5 个仓（增加维护负担）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/swisskyrepo/PayloadsAllTheThings](https://deepwiki.com/swisskyrepo/PayloadsAllTheThings)（已收录） |
| Zread.ai | 未收录（HTTP 403） |
| 关联论文 | 无独立 arXiv 论文；PATT 常被引为「公开 PoC 来源」而非研究对象 |
| 在线 Demo | [swisskyrepo.github.io/PayloadsAllTheThings](https://swisskyrepo.github.io/PayloadsAllTheThings/)（MkDocs Material 站点） |
| 作者博客 | [swisskyrepo.github.io](https://swisskyrepo.github.io/) |
| 配套工具 | [SSRFmap](https://github.com/swisskyrepo/SSRFmap)（3.5K Star）、[GraphQLmap](https://github.com/swisskyrepo/GraphQLmap)（1.6K Star） |
| 生态兄弟 | [InternalAllTheThings](https://github.com/swisskyrepo/InternalAllTheThings)（2.2K Star）、[HardwareAllTheThings](https://github.com/swisskyrepo/HardwareAllTheThings)（887 Star） |
