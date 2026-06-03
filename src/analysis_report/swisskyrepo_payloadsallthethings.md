# 9.6 年 78K stars：一个人撑起的 Web 渗透 Payload 字典

> GitHub: https://github.com/swisskyrepo/payloadsallthethings

## 一句话总结
一个红队操作员用 9 年时间,把「每个 Web 漏洞章节 = README + Burp 字典 + 截图 + 附件」的同构范式,做成 78K stars 的事实标准——PayloadsAllTheThings 是「GitHub 形态 + 广度 + 社区贡献」三者结合下,渗透测试人员人手一份的 Web 漏洞字典。

## 值得关注的理由
- **真·事实标准**: 78,154 stars / 17,032 forks / 1,961 watchers / 333 贡献者,行业默认「Web 渗透 payload 查这里」——它在 GitHub 生态内没有同量级对手。
- **架构上的「payload 卫生标准」可被任何敏感知识库复用**: CONTRIBUTING.md 强制 `id` / `whoami` / `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` 等占位符,让敏感内容既能公开托管又不被滥用,这种「把伦理/法律边界做成工程约束」的思路,远超普通 README 写一句「仅供教育用途」。
- **家族化品牌策略值得独立开发者学习**: 同一作者的 `PayloadsAllTheThings` (Web) / `InternalAllTheThings` (AD) / `HardwareAllTheThings` (IoT) 三件套互相 backlink,把「企业攻击面三轴」拆成可独立成长的子品牌。

## 项目展示

![banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png)
> 项目唯一视觉资产——Adobe Photoshop 制作的 1484×374 hero banner,2020-08 上线后未更换,本身就是「内容驱动、视觉无更新」这一仓库性格的缩影。

> 这是典型的「文档型仓库」——没有可演示的运行时/UI/Demo GIF,故本节仅展示 banner。仓库的「展示」在内容本身:72 个并列漏洞章节,每个章节自带 README + Burp Intruder 字典 + 截图 + 附件。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/payloadsallthethings |
| Star / Fork / Watcher | 78,154 / 17,032 / 1,961 |
| 代码行数 | 2,096 行(主语言 Python 1,280 行 = 61.1%,余为 ASP.NET / XSLT / SVG / XML / PHP / Ruby 等演示片段);**注释/代码比 25.97:1**——典型「文档为主」仓库 |
| 项目年龄 | 115.6 个月 ≈ 9.6 年(2016-10-18 首次提交) |
| 开发阶段 | 低维护(近 30 天 0 commit,近 90 天 13 commit,但 9.6 年从未停更) |
| 贡献模式 | 独立开发者主导 + 社区协作:Swissky 749 commits 占 Top 10 47.5%,全仓 333 位贡献者中 30 位有实质贡献 |
| 热度定位 | 大众热门 + 事实标准(星数远超同类一个数量级) |
| 质量评级 | 内容 [优秀] 文档 [优秀] 工程化 [优秀](markdownlint + 双轨 CI + 模板) |
| License | MIT(极宽松,鼓励衍生与商用) |
| 话题标签 | pentest, payload, bypass, web-application, hacking, vulnerability, bounty, methodology, privilege-escalation, penetration-testing, cheatsheet, security, enumeration, bugbounty, redteam, payloads, hacktoberfest |

## 作者视角:为什么存在这个项目

### 创始人/作者背景
**Swissky**(swisskyrepo),11.1 年老账号,自述「Red Team Operator & Bug Hunter」,无公司归属,blog 挂在 `swisskyrepo.github.io`。10,490 followers、13 个公开仓库,`PayloadsAllTheThings` 是唯一 78K 量级的旗舰项目,远超 #2 `InternalAllTheThings` (2,240 stars) 35 倍。账号年龄 + 自描述 + 旗下「AllTheThings 家族」(Payloads / Internal / Hardware 三件套)共同塑造了项目风格:**实战派、独立运营、用家族化策略做品牌**。

### 问题判断
Swissky 在做 red team 任务时,反复需要把同一组 payload 从旧笔记里复制出来——传统「个人博客 / Twitter 推文 / Notion / PentestMonkey 一类 HTML 静态页」检索成本高、无法直接导入工具、版本不固定。**2016-2018 年是 Burp Suite + Burp Intruder 在企业渗透中的普及期,「字典+payload 一体化」需求井喷;同时 GitHub Pages + mkdocs-material 让「免费可读可贡献的知识库」第一次变得简单**——这正是项目诞生与生长的窗口。

### 解法哲学
- **社区维基 > 个人博客**:核心赌注是「单一作者永远写不完所有漏洞」,开放 PR 是规模化路径,代价是质量参差——所以才有 `.markdownlint.json` + CI 校验做兜底。
- **结构一致性 > 内容深度**:不把每个漏洞写到博士论文级,而是保证 70+ 章节都用同一套四段式骨架(Tools / Methodology / Labs / References),让用户形成稳定心智模型。
- **原子化交付 > 一站式工具**:不把所有 payload 包成自家工具,而是给 Burp / ffuf / HopLa 等已知工具直接消费的文件——复用用户既有工具链,不教育用户迁移。
- **明确不做什么**:不做漏洞扫描器(那是 Nuclei 的活)、不做付费课程、不做实时通讯(连 Discord 都没有)。

### 战略意图
**「AllTheThings」家族 = 同一品牌下的领域化副本**——一个作者做不出整个安全领域的 wiki,但他可以做出「覆盖企业攻击面三轴(外部 Web / 内网 AD / 物理 IoT)」的家族,互相 backlink 在生态里互锁。商业化意图低,商业收益只来自:① GitHub Sponsors(三位赞助商中两家是产品公司、一家是 pentest 服务公司——都是精准流量反向赞助);② 个人品牌溢出(咨询/演讲邀请)。这是**「品牌型独立开发者」路径**,不是「产品型」。

## 核心价值提炼

### 创新之处(按新颖度×实用性排序)

1. **「Payload 卫生标准」与占位符约定** — 把医学研究的「去标识化」思路移植到安全研究内容,所有 payload 必须用 `id` / `whoami` / `Administrator` / `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `P@ssw0rd` 等不可执行占位符,让敏感内容既符合教育用途的法律边界,又能被代码扫描器白名单。**新颖度 4/5 · 实用性 5/5 · 可迁移性 5/5**。
2. **「机器可读转接视图」(`hopla_config.json`)** — 在面向人阅读的 README 之外,维护一份结构化 JSON 把 XSS/SQLi/SSRF/SSTI 等核心 payload 喂给 Burp 扩展 HopLa,实现「文档 ↔ 工具」无缝。**新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5**。
3. **「章节即子模块」目录范式** — `_template_vuln/` + 70+ 同构目录实现「一个仓库 = 多个可独立阅读的子项目」,把软件 monorepo 的「边界即目录」理念移植到文档。**新颖度 3/5 · 实用性 5/5 · 可迁移性 5/5**。
4. **「家族化个人品牌」策略** — 不追求单 repo 做大,而是用「AllTheThings 家族」分别覆盖企业攻击面三轴,互相 backlink,共建品牌。**新颖度 3/5 · 实用性 4/5 · 可迁移性 3/5**。

### 可复用的模式与技巧

- **「_template_xxx/ 模板子目录」模式**:onboarding 文档做成可 fork 的目录,贡献者直接 copy-paste 开始,门槛接近零。任何欢迎社区贡献的开源项目都适用。
- **「同构骨架 + markdownlint 兜底」模式**:4-5 段固定骨架(Tools/Methodology/Labs/References),CI 强制格式统一。适用于企业内 wiki、开源 cookbook 等多人协作文档。
- **「双轨 CI(按需 lint + 全量 build)」模式**:PR 只跑 `tj-actions/changed-files` 过滤后的变更文件 lint,master push 才做全量 mkdocs 构建与部署。任何 monorepo / 大型文档库都应内化。
- **「双视图(GitHub 原生 + mkdocs 站点)」模式**:既保留 GitHub 原生流量,又给重度读者一份「可搜索 + 左导航 + 暗色模式」的阅读体验。
- **「PR-only 治理」模式**:几乎所有协作走 PR,作者保留审阅 + 合入的唯一通道,issues 仅作有限沟通。适合「内容修改频次高 / 错误代价高 / 需要贡献者长期可见」的项目。

### 关键设计决策

| 决策 | 问题 | 方案 | Trade-off | 可迁移性 |
|------|------|------|-----------|----------|
| 72 章节四件套同构 | 多贡献者需保持视觉与操作一致 | `README + Intruder/ + Images/ + Files/` 硬性指定 + 模板 fork | 牺牲按需扩展自由度,换取跨章节等价 | 高 |
| Payload 卫生标准 | 敏感内容易被滥用/误报/下架 | CONTRIBUTING.md 强约束占位符 | 牺牲「直接复制粘贴」便利,换取项目可公开托管 | 高 |
| 四段式章节骨架 | 贡献者对「一个章节应含什么」理解不一 | `_template_vuln/` 当唯一模板,CI 兜底 | 牺牲灵活组织,换取零学习成本 | 高 |
| PR-only 治理 | issue 列表会变 wishlist 噪声 | 几乎所有协作走 PR,issues 仅作有限沟通 | 牺牲轻量反馈,换取 diff 可审计 + 归功明确 | 中 |
| 双轨 CI | 70+ 章节全量 lint 极慢 | PR 阶段按需 lint,master 阶段全量 build | 多一个 workflow,换 PR 反馈 < 30 秒 | 高 |
| 跨工具转接 JSON | 知识库与工具链有「复制粘贴」损耗 | `hopla_config.json` 喂给 Burp HopLa 扩展 | 多一份数据需同步,换「打开 Burp 就能挑 payload」 | 高 |
| AllTheThings 家族 | 单人写不完整个安全知识领域 | 三仓库覆盖 Web/AD/IoT 三轴,互相 backlink | 牺牲「一仓查全」,换子品牌互锁成长 | 中 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | PentestMonkey | OWASP WSTG | HackTricks | InternalAllTheThings |
|------|---------------------|---------------|------------|------------|----------------------|
| 形态 | GitHub repo + mkdocs 站点 | 单页 HTML | OWASP 官方 wiki | 个人维护的网页 wiki | GitHub repo(同作者) |
| Stars | 78,154 | 无 GitHub 主仓(独立网站) | N/A | 万级量级 | 2,240 |
| 覆盖广度 | Web 70+ 章节 | SQLi / Reverse Shell / Linux 提权(几个核心) | 全测试方法论(无 payload) | 全攻击面(含 AD/Windows/Linux) | 仅内网/AD |
| 社区协作 | GitHub PR,333 贡献者 | 无 | 慢(数年一版) | 有限(同团队 PR) | 跟随主仓风格 |
| 工具链集成 | Burp Intruder 字典 + HopLa JSON | 无 | 无 | 弱 | 同主仓 |
| 内容更新 | 持续(年 100+ commits) | 几乎停止 | 数年一版 | 持续 | 跟随主仓 |
| Payload 卫生 | 强约束(占位符) | 无 | 不涉及攻击 payload | 无强约束 | 同主仓 |
| 权威性 | 行业默认 | OSCP 教材引用 | 标准化/合规引用 | 社区影响大 | 圈内默认 |

### 差异化护城河
- **生态护城河(主)**: 70+ 章节 + 333 贡献者 + 9.6 年沉淀 = 数据飞轮,新贡献者冲着已有规模来,新竞争者难以从零聚集
- **品牌/信任护城河**: 78k stars + 9.6 年持续更新 = 行业默认「Web 渗透 payload 字典」
- **可移植性护城河**: markdown + 开放 repo + 双视图 = 不被任何单一平台锁定
- **技术护城河(弱)**: 没有「别人做不到」的技术,内容组织模式可被复制;真正的壁垒是**时间 + 规模**

### 竞争风险
- **最可能替代者**: HackTricks(覆盖面更广,作者 @carlospolop 在安全社区影响力相当)
- **AI 工具冲击**: 大模型对「按主题生成 payload」的能力,可能让本项目沦为「参考素材」而非「查询入口」;但**卫生标准 + 工具链集成形成的内容-工具闭环**,仍是 AI 难以复制的护城河
- **SecLists 跨界**: SecLists 是字典的字典,理论上可扩展到「带 metadata 的字典」,但目前未做;若做,会形成「本项目 + SecLists 二合一」挑战

### 生态定位
**介于「方法论(WSTG)」和「工具(Nuclei / Burp)」之间的「执行参考层」**——把「该用什么 payload 测这个漏洞」做成行业默认;为 SecLists 提供「带说明的字典」、为 Burp 提供「带工作流的字典」、为 WAF/SAST 厂商提供「真值参考」。

## 套利机会分析
- **信息差**: 不存在——这已是事实标准,无「被低估」空间,但也意味着「引用本项目为自己的内容背书」永远有效(它是渗透测试的「常识清单」,任何新工具/教程引用它都会被加分)。
- **技术借鉴**: 强烈推荐学习其「内容组织架构 + 治理机制」——payload 卫生标准、_template_vuln 模板、PR-only 流程、双轨 CI,这套范式可以套到任何「多人协作的知识库」项目(企业 cookbook、案例库、playbook、合同模板库)。
- **生态位**: 在「Web 渗透」领域已无空白可补;真正可挖的生态位是「**生成式 AI 时代的对抗性补充**」——当 LLM 可以即兴生成 payload,本项目的「去标识化卫生 + 工具链集成 + 引用溯源」三件套变成「可信参考源」的核心特征,反而强化不可替代性。
- **趋势判断**: 9.6 年从 0 增长到 78K stars,增长曲线仍在;Hacktoberfest 季节性脉冲说明社区驱动模式健康;AI 短期是威胁,但若本项目主动接入 LLM(例如把每个章节提供「可喂给 GPT-4 的 promptable 模板」),可化威胁为机会。

## 风险与不足
- **作者单点风险**: 47.5% 的 commits 来自 Swissky 本人,若其精力转移(已观察到近 90 天 13 commits 的低维护迹象),更新速度会断崖式下降;目前靠 333 位贡献者 + 17 个 Open PR 维持,但「主审稿人」只有一位。
- **小写目录不一致**(`XSS Injection` vs `XSS injection`): 路径历史遗留,内部链接存在大小写敏感的破坏风险。
- **内容时效性**: 部分 payload 在 WAF 升级后失效,需要持续打补丁(已观察到 `fix` 类型 commit 16.5%,但覆盖面有限)。
- **AI 工具替代风险**: 大模型对「生成 payload」能力提升,可能让「按主题查 payload」从「必须查表」变成「随口问 LLM」;**唯一的反制是强化卫生标准 + 工具链集成,让本项目继续担任「可信参考源」而非「查询入口」**。
- **合规边界**: 虽然有 DISCLAIMER.md + 卫生标准,但仍可能在某些司法辖区(尤其企业内网安全合规审计)被视为「攻击手册」,GitHub 仓库本身有被下架的潜在风险(目前未发生,但 Burp 字典的具体内容可能触发未来风控)。

## 行动建议

- **如果你要用它**: **直接用**——无需任何对比,这已是行业默认。把它当作「每次做 Web 渗透前的热身查阅清单」即可。建议配合 Burp Suite + ffuf + HopLa 扩展使用,把内容喂到工具链里。
- **如果你要学它**: **重点关注「_template_vuln/」+ 「CONTRIBUTING.md」+ 「.github/.markdownlint.json」+ 「.github/workflows/check-markdown.yml」** 这四件套——它们共同构成了「可被任何知识库项目复制的范式」,具体漏洞内容反而是次要的。
- **如果你要 fork 它**: 可改进方向——① 接入 LLM(每个章节提供 promptable 模板,对抗 AI 替代风险);② 改用 conventional commits 治理(目前 74.5% commit 是 freeform,难以自动化);③ 修复大小写不一致的目录命名;④ 把 AD/LINUX/WINDOWS 章节迁出主仓,瘦身主仓专注 Web(与 InternalAllTheThings 形成更清晰分工)。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未确认收录(DeepWiki 页面仅返回 「Index your code with Devin」 占位文案) |
| Zread.ai | 未收录(WebFetch 返回 403) |
| 关联论文 | 无(仓库为实操知识库,不涉及学术研究) |
| 在线 Demo | 官方 GitHub Pages 镜像 — <https://swisskyrepo.github.io/PayloadsAllTheThings/>(mkdocs-material 渲染,支持左导航 + 搜索 + 暗色模式) |
| 兄弟仓库 | InternalAllTheThings(AD/内网) · HardwareAllTheThings(IoT) · SSRFmap · GraphQLmap(同作者) |
