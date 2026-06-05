# 9 年 78K stars: 一位红队的 payload 字典怎么成安全圈事实标准

> GitHub: https://github.com/swisskyrepo/PayloadsAllTheThings

## 一句话总结
Swissky 用 9 年时间把「渗透测试时的 payload + 绕过笔记」沉淀成 web 应用安全领域的事实标准 cheatsheet，凭借 65 个标准化漏洞章节和可立即灌入 Burp Intruder 的 fuzz 字典，成为红队 / 漏洞赏金猎人的案头必查资源。

## 值得关注的理由
1. **渗透测试领域的「OWASP 之外」事实标准**：78,214 stars、17,049 forks，10.5K 关注者的 Swissky 把零散在博客与推特里的 payload 系统化整理，9 年沉淀成 65 个漏洞 chapter，被无数 OSCP 备考指南与 CTF 资料直接引用。
2. **可立刻复用的工程资产**：不同于「读读就好」的 wiki，仓库自带 Burp Intruder 字典（35% 的章节含 `Intruder*` 子目录）、样本 payload 文件和参考资料，是少有的「打开就能在渗透中直接用」的公共知识库。
3. **教科书级的开源治理设计**：`_template_vuln` 模板 + 占位符脱敏标准 + Wayback 引文规范 + 增量 markdownlint CI 这套组合，让非工程师贡献者也能持续输出高质量内容，是内容型开源项目最值得复用的治理范式。

## 项目展示

![banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png) — 仓库主视觉横幅，由 Material for MkDocs 渲染到 https://swisskyrepo.github.io/PayloadsAllTheThings/

![sponsors-list](https://contrib.rocks/image?repo=swisskyrepo/PayloadsAllTheThings&max=36) — contrib.rocks 生成的社区贡献者墙，112 位贡献者中 Swissky 主导 79.3% 的提交，第二名 p0dalirius 仅 81 次

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/PayloadsAllTheThings |
| Star / Fork | 78,214 / 17,049 |
| Watcher | 1,962 |
| License | MIT |
| 创建时间 | 2016-10-18（9 年 8 个月）|
| 最近推送 | 2026-04-22 |
| 主语言 | Python 76.2%（payload 脚本）、ASP.NET 8.7%、XSLT 5.9%、Classic ASP 3.2%、PHP 3.1% |
| 文档量 | 142 个 .md 文件，约 21,500 行 |
| 漏洞章节 | 65 个标准化 chapter（含 `_template_vuln`） |
| 项目年龄 | 约 116 个月 |
| 开发阶段 | 低维护（近 30 天 0 commit，近 90 天 12 commit，进入内容维护期） |
| 贡献模式 | 单人主导（Swissky 1,290 commits 占 79.3%，112 位贡献者） |
| 热度定位 | 大众热门（pentest 知识库领域标杆） |
| 质量评级 | 内容 A / 文档 A / 治理 A / CI B+ |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Swissky 本人公开身份是 **Red Team Operator & Bug Hunter**，账号 11.1 年历史，10,500 关注者，13 个公开仓库中此项目是绝对的「主舞台」——78K+ stars 远超第二名 InternalAllTheThings 的 2,243 stars。他长期运营「AllTheThings」矩阵：PayloadsAllTheThings（Web 应用）/ InternalAllTheThings（AD & 内网）/ HardwareAllTheThings（硬件 IoT），用统一的目录树模式把 red team 的脑回路（Recon → Initial Access → Foothold → Lateral Movement → Exfil）抽象成可命名的攻防 phase，再在每个领域实例化成具体 payload。

### 问题判断
作者看到的不是「找不到 SQL 注入语句」这种表层痛点，而是渗透任务中**反复发生的三件事**：
1. 找到一个可绕过 WAF 的 payload 变体
2. 在 Burp Intruder 里直接灌一坨 fuzz 字典
3. 写报告时需要可引用的参考文献与截图证据

过去这三件事要在多个浏览器 tab、Twint 推文、Notion 笔记里来回切换才能完成。HackTricks 偏「思路与流程」而非可立即消费的 payload；OWASP CheatSheetSeries 是**防御侧** cheatsheet，对 attacker 没有开箱即用价值；nixawk/pentest-wiki 偏静态规模小；FuzzDB / SecLists 类的字典是裸文本，缺背景说明。市场缺一个「长得像 cheatsheet、跑起来像 payload 库、读起来像 wiki」的混合体——这就是 PATT 的存在理由。

### 解法哲学
- **目录树 + 标准化 chapter**，而不是单一 wiki 单文件 / 自动化构建管线 / 内部数据库。一个 5 万行的单文件 PR 几乎不可能被精细评审；目录树把 PR 体积拆到「一个漏洞类别」的尺度，让 review 保持原子性。
- **可拷贝最小骨架**（`_template_vuln`）+ 文字规范（CONTRIBUTING.md），而不是 JSON / YAML schema 强制结构。这是为**非工程师贡献者**做的妥协——「在 GitHub Web 上点 Upload 就能贡献」的门槛对开源友好度是压倒性优势。
- **核心哲学**：用最低门槛（Markdown + GitHub Web）最大化贡献者数量；用最低规范成本（标题、Summary、Tools、Methodology、Labs、References）保证下游消费可预期。

### 战略意图
「AllTheThings」矩阵布局至少承载四层战略意图：
1. **内容品牌化**——「AllTheThings」是 Swissky 个人 IP 的核心载体。
2. **个人 IP 飞轮**——3 个矩阵项目互相导流，每新增一个 chapter 都在强化「Swissky = 攻击侧权威参考」的认知。
3. **商业化路径**——FUNDING.yml 同时挂了 GitHub Sponsors / Ko-fi / Buy Me a Coffee，README 与 CONTRIBUTING 末段都加了 sponsor 链接，并显式列出 3 个企业 sponsor（SerpApi、ProjectDiscovery、VAADATA），是典型独立开发者的「开源作品 + 多渠道赞助」模式。
4. **教育变现伏笔**——`_LEARNING_AND_SOCIALS/` 下挂了 BOOKS.md / YOUTUBE.md / TWITTER.md 三个外链文件，把「读者」二次转化为「学员/订阅者」的引导入口，后续可接付费课程、Discord 社区、咨询等延伸变现。

## 核心价值提炼

### 创新之处

1. **标准化四件套 + 可拷贝最小骨架的 chapter schema**
   - 一个漏洞一个顶级目录，固定包含 README.md / Intruder(s)/ / Images/ / Files/ 四个子结构；README 强制 5 个 H2 区段（Tools / Methodology / Labs / References），Summary 强制 anchor 目录。
   - 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
2. **payload 脱敏标准（占位符统一化）**
   - `id` / `whoami` 用于 RCE PoC、`[ATTACKER.DOMAIN.TLD]` 占位域、`10.10.10.10/11` 占位 IP、`P@ssw0rd` 等占位密码——既保留「可立即复制再替换」的便利，又消除「成品可立即滥用」的风险面。这是开源 offensive security 仓库能长期存活在 GitHub 上的必要代价。
   - 新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5
3. **Wayback 必填 + 四元组引文规范**
   - 引用强制 author/title/link/date 四元组；死链必须用 `web.archive.org` 包裹。contributor 多花 30 秒套格式，5 年后这个项目里 80% 的链接仍能点开。
   - 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
4. **AllTheThings 矩阵 + 跨项目反引**
   - 在 `Methodology and Resources/` 顶部明确声明「Content of this page has been moved to InternalAllTheThings/cloud/aws」——一种「集中化主索引 + 跨矩阵反向引用」的内容工程做法。
   - 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
5. **CI 增量 markdownlint（按 changed-files 跑 lint）**
   - PR 触发时只 lint 改动文件，避免大仓 markdownlint 跑崩。`mkdocs-build.yml` 推 master → 自动 `mkdocs build --force` gh-deploy 到 GitHub Pages。
   - 新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5

### 可复用的模式与技巧
- **目录树即内容 schema**：一个一级目录 = 一个内容单元，URL 与 GitHub 仓库目录 1:1 映射，PR 体积受控
- **可拷贝最小骨架**：`_template_*/README.md` 是为非工程师设计的约束方案
- **占位符标准化**：让 payload 在「可演示」与「不可滥用」之间取得平衡
- **Wayback 必填引文规范**：所有长寿命参考集合项目都应引入
- **增量 lint workflow**：用 changed-files 跑 lint 解决大仓 lint 性能问题
- **跨项目内容矩阵 + 反向外链占位**：让多个 repo 形成统一品牌叙事
- **MkDocs Material + 自定义 overrides 注入第三方分析**（Umami）+ AddToAny 分享按钮
- **三轨赞助**：GitHub Sponsors / Ko-fi / Buy Me a Coffee
- **章节「已迁移」软提示**：在文档顶部加 `:warning:` 提示比硬删除 + 404 更优雅

### 关键设计决策

1. **chapter 物理目录化**（一个漏洞一个文件夹）
   - 问题：60+ 个漏洞类别如果塞进一个 README，单文件会膨胀到无法 PR review
   - 方案：每个漏洞一个顶级目录，目录名即 slug；URL 与 GitHub 仓库目录 1:1 映射
   - Trade-off：顶级目录多到 65 个，`ls` 略乱；换来 URL 永久稳定、PR 体积受控——**以可发现性换可贡献性**

2. **`Methodology and Resources/` 作为「软迁移」过渡索引**
   - 方案：不直接删旧文件，而是在文件顶部加 `:warning: Content of this page has been moved to ...` 并把本地 Summary 改成外链列表
   - Trade-off：本地仓库保留了一些「已不维护」的 `.md`；好处是**降低历史读者断链率**

3. **MkDocs Material + `git-revision-date-localized` + `mkdocs build --force` gh-deploy**
   - 方案：推 master 时自动 pip install + gh-deploy
   - Trade-off：依赖 pin 到 `latest`（不锁版本），未来 mkdocs 重大版本升级可能 break deploy

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | HackTricks | OWASP CheatSheetSeries | nixawk/pentest-wiki |
|------|---------------------|-----------|----------------------|-------------------|
| Star | 78K | ~11.5K | ~30K | 3.7K |
| 视角 | 攻击侧 | 攻击侧 | 防御侧 | 攻击侧 |
| 核心价值 | 可立即使用的 payload 字典 | 攻击流程与思路 | 防御规范 | 综合渗透知识 |
| 结构 | 目录树 + 标准化 chapter | mdbook wiki | 单文件 cheatsheet | 静态 wiki |
| 字典/样本 | Burp Intruder 字典 | 无 | 无 | 无 |
| 多语言 | 英语 + 部分翻译 | 17 种语言 | 英语 | 英语 |
| 维护模式 | 单人主导 + 社区 PR | 多人协作 | 官方组织 | 单人 |
| 沉淀年限 | 9 年 | 6 年 | 持续更新 | 8 年 |

### 差异化护城河
- **可立即消费的 payload 字典**——别家给思路，PATT 给「打开就能在 Burp 里灌」的具体字符串
- **标准化 chapter schema** 带来的认知一致性——读 SQLi 章节和读 SSTI 章节是同一种心智模型
- **9 年沉淀 + 78K stars 形成的「事实标准」地位**——后来者要挑战的不仅是内容质量，还要挑战已成型的社区认知
- **社区规模 → 更新速度 → 持续覆盖新型漏洞**——飞轮效应，OWASP CSS 这种官方项目都难以复制

### 竞争风险
- **AI 辅助渗透工具的崛起**：BurpGPT / PentestGPT 等把「查 wiki」自动化，「打开 PATT 复制 payload」的步骤被工具直接吃掉
- **PortSwigger Web Security Academy**：免费、官方背书、互动式实验室，正在替代「读 + 手动试」的渗透学习路径
- **单一作者依赖**：贡献集中度 79.3%，若 Swissky 离开，红队侧的事实标准地位可能被 HackTricks 或新矩阵接管

### 生态定位
攻击侧知识资产领域处于**事实标准位置**；防御侧象限不占位（留给 OWASP）；在攻防一体化平台里属于**互补内容源**——任何做漏洞扫描器、WAF、自动化渗透平台的项目都可以把 PATT 当作上游 payload 字典来源。

## 套利机会分析
- **信息差**：不构成 star 增长套利（已 9 年成熟、78K stars 沉淀），但构成**「内容工程化」方法论套利**——它的治理设计（_template + 脱敏 + 引文规范 + 增量 lint）可以原样迁移到任何「多贡献者长寿命内容仓库」项目
- **技术借鉴**：标准化 chapter schema、可拷贝最小骨架、Wayback 必填、占位符脱敏——这 4 套范式对所有内容型开源项目（书单、Paper Reading List、CVE 数据库、教学材料）都直接可用
- **生态位**：在 AI 自动化渗透工具挤压「查 wiki」场景的今天，**「可立即使用的 payload 字典」**这个生态位反而更稀缺——AI 生成 payload 时需要 ground truth 训练数据，PATT 是天然语料库
- **趋势判断**：增长已停滞（处于「低维护」阶段），但仍是 pentest 圈默认起点；中短期不会被取代，长期（5 年+）可能被 AI 工具链消化

## 风险与不足
- **测试覆盖 N/A**：文档型项目无单元测试概念，markdownlint 增量 CI 是软性守门
- **子目录命名不一致**：`Intruder/` vs `CONTRIBUTINGIntruders/`、`Files/` vs `files/` 存在 3 处不一致（9 年演化遗留技术债）
- **依赖未锁版本**：mkdocs.yml 用 `latest` pip 包，未来升级可能 break deploy
- **缺少 PR/Issue 模板**：`.github/PULL_REQUEST_TEMPLATE.md` 与 `ISSUE_TEMPLATE/` 都未发现，仅靠 CONTRIBUTING.md 文字规范引导——对超大 PR 量（18 个 open PR）的项目是个治理短板
- **法律风险敞口**：作为 offensive security 仓库，payload 脱敏和 DISCLAIMER 是必要护城河，但 GitHub DMCA / 政策风险始终存在

## 行动建议
- **如果你要用它**：渗透任务前打开对应 chapter，把 Intruder 字典直接喂给 Burp；写报告时直接引用四元组参考文献；建议同步阅读 HackTricks（互补）以补全攻击流程叙事
- **如果你要学它**：重点看 `_template_vuln/README.md`（最小骨架）、`CONTRIBUTING.md`（8 条脱敏规则 + 4 元组引文）、`.github/workflows/check-markdown.yml`（增量 lint）、`Methodology and Resources/`（软迁移索引）——这是内容型开源项目最值得复用的 4 个文件
- **如果你要 fork 它**：可以改进的方向是 (1) 加 PR/Issue 模板降低贡献摩擦；(2) 锁 mkdocs 依赖版本；(3) 规范化子目录命名（`Intruder` 单数 + `Files` 首字母大写）；(4) 增加跨章节索引（按 OWASP Top 10 / CVE 分类的二级目录）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/swisskyrepo/PayloadsAllTheThings |
| Zread.ai | 未收录 |
| 关联论文 | 无（项目是知识整理型，非学术产出） |
| 在线 Demo | https://swisskyrepo.github.io/PayloadsAllTheThings/ （Material for MkDocs 渲染的站点） |
| AllTheThings 矩阵 | [InternalAllTheThings](https://swisskyrepo.github.io/InternalAllTheThings/) / [HardwareAllTheThings](https://swisskyrepo.github.io/HardwareAllTheThings/) |
