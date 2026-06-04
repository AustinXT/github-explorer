# 9.6 年、78K star、零代码仓库：PayloadsAllTheThings 凭什么把渗透 payload 写成「行业基础设施」

> GitHub: <https://github.com/swisskyrepo/payloadsallthethings>

## 一句话总结

PayloadsAllTheThings 是一份**用 GitHub 仓库形态维护的渗透测试 payload 百科全书**——注释:代码 = 26:1 的"反常识"文档型项目，靠「模板化贡献 + 消毒占位符 + Burp 字典绑定」三件套，把 333 位陌生人变成 9.6 年可持续的搬运工，最终跻身 Bug Bounty 实战链条上游的事实标准。

## 值得关注的理由

- **重新定义「GitHub 仓库」**：零依赖、零 runtime、零测试，2,096 行代码 / 54,442 行注释，却拿下 78K star、333 贡献者、9.6 年长生命周期——这是一个**用代码托管平台做内容工程**的样本。
- **把「贡献门槛」标准化到极致**：CONTRIBUTING.md + `_template_vuln/` + markdownlint CI 把外部 PR 收敛成"复制 4 个空目录 + 填 4 个固定小节 + 跑一次 lint"——任何想建设众包内容库的人都能直接抄这套。
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
| Star / Fork | 78,184 / 17,037 |
| 代码行数 | 2,096 行（主语言 Python 61.1%、ASP.NET 9.0%、XSL 7.0%） |
| 注释:代码比 | 1:26（典型文档型仓库，payload 文本被 tokei 计为注释） |
| 文件数量 | 293（实际 .md / payload 文件远超此数） |
| 项目年龄 | 115.6 个月（≈ 9.6 年） |
| 总 commits | 2,185 |
| 最近推送 | 2026-04-22 |
| 开发阶段 | 稳定维护（低频 + 脉冲式，Hacktoberfest 9 月单月 75-125 commit） |
| 贡献模式 | 强单人主导（Swissky 47.5% commits / 79.3% PRs）+ 333 人长尾社区 |
| 热度定位 | 大众热门（安全知识型项目头部，事实标准位） |
| License | MIT |
| 质量评级 | 内容覆盖率 A / 模板一致性 B / payload 可复现性 A / 参考链接 A+ |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Swissky（swisskyrepo）**，独立红队 / 漏洞猎人，账号年龄 11.1 年，10,497 粉丝，公开仓库 13 个。Bio 自报"Red Team Operator & Bug Hunter"，无公司背景；行业大会演讲者，渗透圈真实身份。

整个 GitHub 资产围绕 **"AllTheThings" 品牌矩阵** 展开：PayloadsAllTheThings（Web，78K stars）、InternalAllTheThings（AD/内网，2.2K stars）、HardwareAllTheThings（硬件），再加 SSRFmap / GraphQLmap 等小型工具。同模板、同方法论、同治理风格——这是单作者"方法论可复制"的成果。

### 问题判断

渗透测试者面对"某个漏洞类型有哪些可用 payload、哪些 WAF bypass、哪些参考资料"这类高频问题时，公开知识散落在 100+ 个人 blog、Twitter 线程、工具 wiki、HackTricks 子页、PortSwigger Lab 中——**没有一份可被 PR 持续维护、payload 可直接复制、参考资料齐全的清单**。个人 blog 单点存在、无版本化、SEO 极差、404 高发。

Swissky 在 2016-10 立项，恰好处于 Bug Bounty 平台 HackerOne/Bugcrowd 在欧洲完成"白帽大众化"的窗口期（2015-2017 是 BB 行业井喷期）——这是「渗透实战需要标准化 payload 库」这个需求第一次被大众化的时间窗口。

### 解法哲学

**可复制即正义**：CONTRIBUTING.md:14-19 强制用 `id` / `whoami`（不是 `whoami && rm -rf /`）+ `[ATTACKER.DOMAIN.TLD]`（不是 `evil.com`）+ `10.10.10.10`（不是 `192.168.0.1`），意味着每个 payload 都是**可直接复制粘贴到 Burp / 终端**的形式——这是把"博客式记录"和"工具箱式记录"区分开的核心。

**不重复造轮子，只做索引**：README.md:43-53 把 333 个贡献者看作 payload **搬运工** 而不是 payload **发明者**；每条 payload 都标参考（CONTRIBUTING.md:20 强制 "References must have an author, a title, a link and a date"）。

**同模板 = 可规模化**：CONTRIBUTING.md:42 引 `_template_vuln/README.md` 作为新章节模板，**降低贡献门槛到"复制一个目录 + 填四节"**。

**明确不做什么**：不是工具、不是 SaaS、不是教科书、不是个人 blog——是**字典**。Swissky 明确划清了与 HackTricks（教科书）的边界。

### 战略意图

- **短期**（2016-2019）：从 0 到 4 万 star，证明"列表型知识库"在 Web 安全领域有自然增长
- **中期**（2019-2022）：通过 Hacktoberfest 流量放大（9 月 commit 峰值 73/84/125/107）
- **长期**：形成 "AllTheThings" 品牌矩阵 + 企业赞助（SerpAPI/ProjectDiscovery/VAADATA）+ 衍生品（books/、YouTube 列表）

商业化路径：3 家安全企业持续赞助 + 3 路个人赞助渠道（GitHub Sponsors / Ko-fi / BuyMeACoffee），是**独立安全研究员的可持续开源模式**而非 SaaS 化。

## 核心价值提炼

### 创新之处

| # | 创新点 | 新颖度 | 实用性 | 可迁移性 |
|---|---|---|---|---|
| 1 | 模板化贡献（_template_vuln/ + CONTRIBUTING.md + markdownlint CI）—— 把"提交一个 PR"标准化为"复制 4 个空目录 + 填 4 个固定小节 + 跑一次 lint" | 3/5 | 5/5 | 5/5 |
| 2 | Burp Intruder 字典与漏洞章节绑定（XSS/Intruders/、SQL Injection/Intruder/ 同目录可加载） | 4/5 | 5/5 | 4/5 |
| 3 | 同作者三件套（PAT / IATT / HATT）覆盖 Web / AD / 硬件三大攻击面 | 5/5 | 4/5 | 2/5 |
| 4 | Hacktoberfest 节日营销 + 企业赞助（SerpAPI/ProjectDiscovery/VAADATA）双引擎驱动 | 3/5 | 5/5 | 4/5 |
| 5 | 占位符消毒字典（id/whoami/[ATTACKER.DOMAIN.TLD]/10.10.10.10/P@ssw0rd/DC01） | 3/5 | 5/5 | 5/5 |
| 6 | DISCLAIMER.md 法务防火墙（8 条免责声明写到「用户行为责任」层） | 2/5 | 5/5 | 5/5 |

### 可复用的模式与技巧

1. **占位符消毒字典**：任何含可执行 payload 的知识库 / SaaS 文档 / 培训材料都该用这套——把 `evil.com` 换成 `[ATTACKER.DOMAIN.TLD]` 是把"知识"和"误用"切开的最低成本动作。
2. **章节 4 文件模板（README + Intruder + Images + Files）**：任何"知识点 + 可运行片段 + 截图 + 复现文件"的 cheat sheet 项目都能照搬。
3. **PR-only + markdownlint CI**：法律责任敏感、众包成分高的内容仓库的最佳治理姿态——既切断 issue 滥用风险，又用 CI 强制统一格式。
4. **双入口（GitHub + mkdocs-material Pages）**：SEO 重要的中长篇内容必备；mkdocs-material 自带暗/亮模式 + code copy + 搜索，比裸 GitHub 阅读体验高一个维度。
5. **Wayback Machine fallback reference 规则**：任何带外部引用的长寿知识库的"长寿保险"——5 年后 50% 的 blog 链接会 404。
6. **品牌矩阵分工（AllTheThings 三件套）**：单作者想扩张领域但不放弃质量一致性的扩张方式。

### 关键设计决策

#### 决策 1：把每条 payload 都"消毒"为可安全复制粘贴的占位符

- **问题**：真实 payload 含真实 IP/域名/账号/密码，社区维护下会被误用
- **方案**：CONTRIBUTING.md:14-19 强制 4 类占位符规则
- **Trade-off**：占位符必须替换才能用，对纯复制党友好但替换本身是隐藏心智成本
- **可迁移性**：高（任何带 payload 的知识库都该用这套消毒字典）

#### 决策 2：每章固定 4 文件结构（README + Intruder(s) + Images + Files）

- **问题**：渗透笔记容易变成"随手写的纯文本"，多年后无法机器/视觉检索
- **方案**：README.md:19-24 强制每个章节文件夹有这 4 类内容
- **Trade-off**：对"只想加一个 payload"的轻量贡献者是负担（要同时建子目录）
- **可迁移性**：高

#### 决策 3：markdownlint 强制统一格式

- **问题**：333 个贡献者众包文本，Markdown 风格碎片化
- **方案**：`.github/.markdownlint.json` + `Docker run ... davidanson/markdownlint-cli2:v0.15.0`（CONTRIBUTING.md:27-29）+ `check-markdown.yml` workflow on push/PR
- **Trade-off**：贡献者需本地装 Docker
- **可迁移性**：高

#### 决策 4：参考资料强制 author/title/link/date 四元组 + Wayback fallback

- **问题**：blog 链接 5 年后 404，知识库就死了
- **方案**：CONTRIBUTING.md:20-23 强制四元组 + Wayback Machine fallback
- **Trade-off**：写一段 reference 比写一段 payload 还累
- **可迁移性**：中（规则照搬容易，但社区自发维护 reference 文化的成本高）

#### 决策 5：GitHub Pages + mkdocs-material 双入口

- **问题**：GitHub 原生 markdown 阅读体验差（无目录滚动、无搜索框、无主题切换）
- **方案**：`mkdocs.yml:1-72` 用 mkdocs-material 主题 + `.github/workflows/mkdocs-build.yml` 自动部署
- **Trade-off**：维护两套入口（GitHub + Pages），但 Pages 版本带来 SEO + 二次传播
- **可迁移性**：高

#### 决策 6：不接受新 issue，只接受 PR

- **问题**：安全话题 issue 容易被滥用为漏洞披露/法律风险
- **方案**：0 open issues + 17 open PR（PR-only 维护）
- **Trade-off**：17 个 PR 累积说明审核慢
- **可迁移性**：中（任何带"概念性内容 + 多人贡献 + 法律责任风险"的项目都可借鉴）

### 治理债务（诚实点出）

9.6 年社区贡献累积的目录规整债务：

- `XSS Injection/` vs `XSS injection/`（大小写不一致并存）
- `Upload/` vs `Upload Insecure Files/`（命名不一致）
- `Methodology and Resources/Reverse Shell Cheatsheet.md` 整文件只剩 302 跳转 IATT（迁移后未清理的空壳）

这些不是 bug，是**长期众包仓库的真实成本**——但都是后续重构切入点。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | HackTricks | OWASP CheatSheet | PEASS-ng | PayloadBox |
|------|---------|--------|--------|--------|--------|
| 定位 | 实战 payload 字典 | 综合 Pentest 教科书 | 防御备忘录 | 提权脚本工具 | 纯 payload 集合 |
| Stars | 78K+ | ~50K+ | ~30K+ | ~17K+ | 多个万 |
| payload 颗粒度 | 细（具体 XML 标签变体） | 粗（一句话带过） | 几乎无 | 不适用（脚本） | 极细（纯字典） |
| 方法论覆盖 | 广 | 最广 | 防御视角 | 单点（提权） | 无 |
| 工具链集成 | 强（Burp Intruder 绑定） | 中（独立字典章节） | 无 | 极强（可执行） | 弱 |
| 双语支持 | 否 | 是（西/英） | 是（多语种） | 否 | 否 |
| 攻击 vs 防御 | 攻击 | 攻击+防御 | 防御 | 攻击（提权） | 攻击 |
| 社区规模 | 333 贡献者 | >500 贡献者 | OWASP 团队 | 100+ 贡献者 | 小型 |

### 差异化护城河

1. **payload 颗粒度 + 跨语言覆盖**：同一种漏洞下提供 Python/ASP/PHP/ASP.NET/Ruby/XSLT/Node 多种服务端语言变体——对企业内网 legacy 渗透极实用
2. **Burp Intruder 字典与漏洞章节绑定**：行业普遍把字典和知识拆开存，PAT 把两者**装在同一个目录**——这一项 HackTricks 都没做到
3. **9.6 年沉淀的 reference 网络**：author+title+date 四元组 + Wayback fallback——任何新进入者很难"复制"这层
4. **品牌矩阵 + 同作者三件套**：跨项目 reference 已落地（PAT → IATT），方法是体系化的不是单点

### 竞争风险

**最可能被替代**：HackTricks 在体系化、双语、社区规模上已经反超；若 HackTricks 引入"细粒度 payload 模块 + 跨语言覆盖"，PAT 的护城河会被压缩。

**几乎不可能被替代**：PEASS-ng（仅提权单点）、PayloadBox（无方法论）、OWASP（防御视角）——这些是错位竞争，不构成直接威胁。

### 生态定位

PAT 处在 **"Bug Bounty 实战工具链" 上游**：渗透人员把 PAT 当 Burp 字典 + 报告 PoC 来源——这是「工具 + 知识」型生态位，与 HackTricks「教科书」型生态位互补不冲突。

## 套利机会分析

- **信息差**：项目本身是**严重被高估**而非被低估——78K star 中相当比例是被 Hacktoberfest 营销和"清单"型内容吸引的低信号 Star（大量安全学生 / Cert 备考者），实际"看过 / 用过 / 贡献过"的比例远低于 star 数。**但作为方法论样本被严重低估**——它示范了"内容型 GitHub 项目的可持续治理"这件事，目前中文圈几乎没有对等讨论。
- **技术借鉴**：`_template_vuln/` + `CONTRIBUTING.md` + `markdownlint CI` 这一套是**可立刻抄到任何内容型项目**的工程范式；占位符消毒字典可移植到任何带可执行 payload 的文档；PR-only 治理姿态适合法律责任敏感的知识库。
- **生态位**：填补了「渗透实战 payload 字典」这一空白——HackTricks 偏教科书、PEASS-ng 偏工具、OWASP 偏防御，PAT 占据「实战最细颗粒度 payload」这个缝隙。
- **趋势判断**：渗透测试 / Bug Bounty 行业仍在增长，PAT 不会衰退；但若 HackTricks 跟进"细粒度 payload 模块"，PAT 需要靠"模板化贡献 + 消毒占位符 + Burp 字典绑定"这套**已经形成的网络效应**继续拉差距——这是它**真正的后发优势**而非代码本身。

## 风险与不足

1. **零代码 = 零测试**：2,096 行 Python 不是生产代码，只是 SSTI/反序列化利用示例；payload 失效 / 链接 404 完全靠社区发现
2. **目录治理债务**：XSS Injection / XSS injection 大小写并存、Upload / Upload Insecure Files 命名不一致，9.6 年累积
3. **审核节奏慢**：17 个 open PR 持续累积，Swissky 倾向"少而精"——新 PR 排队时间长
4. **依赖单一作者**：Swissky 一个人占 47.5% commits，若作者精力转移，PAT 维护质量会快速下降
5. **法律灰带**：武器化仓库虽然在 DISCLAIMER.md 立了 8 条免责，但在某些司法辖区仍可能有法律风险
6. **贡献集中度被 HackTricks 反超**：HackTricks 活跃贡献者 >500，PAT 333——若体系化差距继续拉大，PAT 的"教科书分流"会被加剧

## 行动建议

- **如果你要用它**：Bug Bounty 实战 / CTF 现场 / 需要可直接复制的 payload → 选 PAT；入门 / 系统学习 / 需要更宽攻击面 → 选 HackTricks。**两者协同用** 而不是二选一。
- **如果你要学它**：重点关注三个文件——`CONTRIBUTING.md`（贡献治理范式）、`_template_vuln/README.md`（降低贡献门槛的模板）、`mkdocs.yml` + `.github/workflows/mkdocs-build.yml`（双入口部署）。
- **如果你要 fork 它**：可以改进的方向——① 清理目录治理债务（XSS Injection / Upload Insecure Files 等）；② 把 17 个 open PR 排序 + 引入维护者小组；③ 加 GitHub Action 自动检测失效 reference 链接（比 Wayback fallback 更主动）。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | 无（工程实践型知识库，无学术对应） |
| 在线 Demo | <https://swisskyrepo.github.io/PayloadsAllTheThings/>（GitHub Pages 渲染版，可视作在线 Demo） |
| 同作者姊妹项目 | [InternalAllTheThings](https://github.com/swisskyrepo/InternalAllTheThings)（AD/内网） / [HardwareAllTheThings](https://github.com/swisskyrepo/HardwareAllTheThings)（硬件） |
