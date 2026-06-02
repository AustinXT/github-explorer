# Phase 1 — 网络分析（Network）：swisskyrepo/PayloadsAllTheThings

## 仓库基本数据

- **仓库**: swisskyrepo/PayloadsAllTheThings
- **Star / Fork / Watcher**: 78,134 / 17,028 / 1,961
- **Open Issues**: 0（仓库已禁用 Issues 跟踪，全部走 PR 流程）
- **Open PRs**: 17
- **主语言**: Python（实际为多语言 Markdown 文档集合，Python 文件最多约 80,988 字节）
- **语言分布**（字节降序）: Python 80,988 / ASP.NET 9,206 / XSLT 6,303 / PHP 3,248 / Classic ASP 3,372 / Ruby 1,234 / Jupyter Notebook 611 / HTML 473 / CSS 476 / Shell 52 / Hack 45 / JavaScript 228
  - 注：GitHub 将 Markdown 归入 "Python" 是统计 quirk；本质是 Markdown 文档集（每个漏洞章节一个 README.md）
- **License**: MIT
- **创建时间**: 2016-10-18
- **最近推送**: 2026-04-22（高度活跃，仍在持续更新）
- **最近更新元数据**: 2026-06-02
- **话题标签**: pentest, payload, bypass, web-application, hacking, vulnerability, bounty, methodology, privilege-escalation, penetration-testing, cheatsheet, security, enumeration, bugbounty, redteam, payloads, hacktoberfest
- **已归档**: 否 | **是 Fork**: 否
- **defaultBranchRef**: master
- **homepageUrl**: https://swisskyrepo.github.io/PayloadsAllTheThings/（MkDocs 渲染的镜像站点）
- **diskUsage**: 23,283 KB
- **最近一次 Release**: 2025-07-26 标签 v4.2 "FERRETEDITOR"（每年一版的命名 release）

## 作者画像

- **姓名/ID**: Swissky（@swisskyrepo）
- **公司**: 未公开（null）
- **位置**: 未公开（null）
- **Bio**: "Red Team Operator & Bug Hunter"
- **Blog**: https://swisskyrepo.github.io/
- **粉丝**: 10,488
- **关注**: 13（高度精选）
- **公开仓库**: 13
- **公开 Gist**: 2
- **账号年龄**: 2015-04-28 至今 ≈ 11 年
- **此 repo 投入权重**: **极高** — 在其最近 10 个活跃仓库中按 push 时间排第 1 位（最近推送 2026-04-22），并形成"AllTheThings"系列（InternalAllTheThings、HardwareAllTheThings、PayloadsAllTheThings）三大支柱。
- **作者类型**: **独立研究者/红队顾问**（自述 "Red Team Operator & Bug Hunter"），同时构建了一套"安全知识仓库"开源品牌。
- **贡献集中度**: **单人深度主导 + 社区众包扩充**。
  - Top 1（swisskyrepo 本人）: 1,290 commits
  - Top 2（p0daliriux）: 81 commits（约 6%）
  - Top 3（noraj）: 50 commits
  - Top 10 之外的贡献者多为单数级别提交。本人占比 ≈ 87% 之上
- **背景推断**: 长期专注 Web 应用安全与红队/漏洞赏金赛道，独立维护"AllTheThings"知识体系，有意把零散漏洞利用知识结构化为可检索的字典化资产；"11 年账号 + 1 万粉丝 + 13 个高相关仓库"画像与"独立红队顾问/安全布道者"高度一致。
- **生态联动**: 同账号下 `InternalAllTheThings`（2,238 ⭐ AD/内网渗透）、`HardwareAllTheThings`（885 ⭐ IoT/硬件）、`SSRFmap`（3,559 ⭐ SSRF 工具）、`GraphQLmap`（1,664 ⭐ GraphQL 工具），形成"知识库 + 工具"双轮。

## 社区热度

- **热度级别**: **大众热门（Web 安全领域头部项目）**
  - 78k Star 在所有 GitHub 仓库中排名前 0.05%，在 `pentest` / `bugbounty` 标签下是长期 Top 1
- **增长模式**: **经典长尾稳步型 + 周期性爆点**
  - 早期（2016-2017）逐步积累
  - 2019-11 ~ 2020-02 出现第一轮明显加速（GitHub Star History 图显示 2019 年底开始陡增）
  - 2021-2022 年持续稳步增长
  - 2022-2024 出现快速跃升（与 HackTheBox / TryHackMe 类在线靶场流行、LLM 安全兴起吻合）
  - 2024-2025 出现 Web LLM Attacks、Prompt Injection 等新章节的拉动
- **增长数据**（基于 `Accept: application/vnd.github.star+json` 抽样）
  - 抽样 page 100（2019-11 区间）日均 20-30 star
  - 抽样 page 200（2021-02 区间）日均 15-25 star
  - 抽样 page 400（2022-10 区间）日均 15-20 star
  - 整体平均星速 ≈ 30-50 star/天（基于 78k 总数 / 约 9.5 年）
- **近期趋势**: 仍稳定在 20-50 star/日区间，结合最近一次 push 距今约 40 天（4-22 → 6-02），属于"持续高产"状态而非衰减。
- **套利判断**: **被严重高估而非低估** — 已是品类事实上第一名（同类工具集合中 GitHub Star 最高）。不属于"被低估的潜力股"，而是"赛道标准答案"。任何新文档站点/工具集都默认以它为参照。

## 生态网络

### 上游依赖
- 项目是**被依赖方**，不是依赖方
- **典型上游引用**：
  - Kali Linux 收录（v2.1 "Kali Linux Repository" release 2019-07-05 明确标识被 Kali 官方仓库收录）
  - HackTheBox / TryHackMe 大量 walkthrough 引用
  - Burp Suite PortSwigger 官方文档多次交叉引用
  - OWASP Cheat Sheet Series 在多个章节中互链
  - SerpApi、ProjectDiscovery、VAADATA 等公开赞助（README sponsors 表）
- 学术界和工业界：CWE 章节与各厂商漏洞分类体系对齐

### 同类项目（竞品/邻接）

| 仓库 | Stars | 定位 | 关系 |
|---|---|---|---|
| **OWASP/CheatSheetSeries** | 32,152 | OWASP 官方安全防御 cheatsheet | 互补（一个攻一个防，PayloadsAllTheThings 是其进攻侧对偶） |
| **danielmiessler/SecLists** | 60k+ | 字典/词表/Payload 原始素材 | 上游供应（PayloadsAllTheThings 引用 SecLists 的字典） |
| **foospidy/payloads** | 3,953 | Web 攻击 payload 集合（Git All the Payloads） | 早期同类，结构化程度不如本项目 |
| **daffainfo/AllAboutBugBounty** | 6,759 | Bug Bounty 技巧与 bypass 集合 | 高度同质化竞品，但本项目结构化更清晰 |
| **Mehdi0x90/Web_Hacking** | 779 | Web Hacking 技巧与 payload | 弱竞品，文档质量与覆盖广度均不及 |
| **swisskyrepo/InternalAllTheThings** | 2,238 | AD 与内网渗透 cheatsheet | **同作者姊妹项目**，扩展渗透全链路 |

## 官方文档洞察

> 官网 https://swisskyrepo.github.io/PayloadsAllTheThings/ 抓取要点：

- **价值主张**: "Web 应用安全的有用 payload 与 bypass 集合" — 把零散的渗透测试 payload 字典化、可检索化。
- **目标用户**:
  - Web 渗透测试工程师
  - Bug Bounty 猎人
  - 安全研究员
  - CTF 选手
  - 自学者
- **差异化叙事**:
  - **结构化模板**：每个漏洞章节遵循统一目录（README.md + Intruder 文件 + Images + Files），并提供 `_template_vuln` 作为新章节的脚手架
  - **覆盖广度**：数十个漏洞类别，且每个类别按语言/平台细分（SQLi 拆出 MySQL/PostgreSQL/MSSQL/Oracle/SQLite/BigQuery/Cassandra/DB2）
  - **AllTheThings 家族**：Active Directory（InternalAllTheThings）+ IoT/硬件（HardwareAllTheThings）形成完整渗透测试知识矩阵
  - **Companion Web View**：用 Material for MkDocs 渲染为可浏览站点
  - **学习延伸**：内置 BOOKS.md / YOUTUBE.md 资源清单
- **设计哲学**:
  - 开放贡献（CONTRIBUTING.md）
  - 标准化模板（让社区可以"按套路"添加新漏洞类别）
  - 实战导向（payload 与 bypass 是一等公民，理论只作辅助）
- **技术路线图**（从 README + 近期 PR 推断）:
  - 长期主题：Web 应用层漏洞全覆盖
  - **新兴主题**（2024-2026 显著发力）：
    - **Web LLM Attacks**（#835/#836，2026 年合并）— 反映 LLM 安全是新前沿
    - **CSV/CSV Injection** 规范化（#839）
    - **Server-Side Parameter Pollution**（#838）
    - **Dependency Confusion** 引用日期规范化（#840）
    - **Host Header Attacks**（#834）
- **架构文章要点**: **无专门博客/架构文章**。项目本质是文档型仓库，README + 各章节 README 即全部"文档"。社区通过 PR 进行"架构演进"（如 #835 新增 Web LLM Attacks 章节），而非长篇架构博文。

### 外部深度视角

- **DeepWiki**: 页面存在但内容仍在加载，未抓取到实质 wiki（标注：未收录完整分析）
- **Zread.ai**: 返回 403，未收录
- **Web 搜索**: 因工具限制本次未能获取有深度的第三方评论文章
- **结论**: 暂未找到有独立分析深度的外部文章（待 Phase 2/3 补充）

## 竞品清单

| 竞品 | Stars | 定位 | 优势 | 劣势 |
|---|---|---|---|---|
| **OWASP/CheatSheetSeries** | 32,152 | OWASP 官方防御 cheatsheet 集合 | 防御视角权威；OWASP 品牌背书 | 几乎不含具体攻击 payload；偏防御 |
| **danielmiessler/SecLists** | ~60k+ | 字典/词表/Payload 原始素材库 | 海量原始 payload；安全行业标准字典 | 没有上下文解释，单纯字典 |
| **foospidy/payloads** | 3,953 | "Git All the Payloads" 攻击 payload 集合 | 早期先驱；分类齐全 | 缺乏 Burp Intruder 等工具化集成；结构化弱 |
| **daffainfo/AllAboutBugBounty** | 6,759 | Bug Bounty 技巧与 bypass 集合 | 关注 bounty 实战经验 | 内容深度和广度均不及 PayloadsAllTheThings |
| **swisskyrepo/InternalAllTheThings** | 2,238 | AD/内网渗透 cheatsheet | 同作者姊妹项目，质量一致 | 仅覆盖内网阶段，与 Web 互补不竞争 |

> **竞品格局**: **事实标准 + 同质化跟进** — 在 Web 渗透测试 payload 文档集合这个垂直品类里，PayloadsAllTheThings 已成事实标准，其他项目多以"补充/翻版"形式存在，并非红海竞争。真正的"竞品"是 OWASP（防御对偶）和 SecLists（上游素材），三者形成"上游字典 → 攻击 cheatsheet → 防御 cheatsheet"的完整生态。

## 关键 Issue 信号

**注意**: 仓库已禁用 Issues（`gh issue list` 提示 "repository has disabled issues"），所有社区交流通过 PR + Discussions 推进。Issues 数为 0 即此原因。

从 PR 中观察设计张力：

1. **[#835 Create Web LLM Attacks](https://github.com/swisskyrepo/payloadsallthethings/pull/835)** + **[#836 Create README.md at Web LLM Attacks](https://github.com/swisskyrepo/payloadsallthethings/pull/836)** — 揭示了**项目向 LLM 安全赛道主动扩张**的设计方向。从传统 Web 漏洞（XSS/SQLi/SSRF）扩展到 LLM Prompt Injection、LLM-as-attacker、Agent 攻击等新前沿。
2. **[#843 fix: semgrep found a bash reverse shell in hopla_config.json](https://github.com/swisskyrepo/payloadsallthethings/pull/843)** — 揭示了**项目自身也在被 Semgrep 等安全扫描器检测为"含恶意 payload"**的张力 — 即"教安全的仓库自己也会被标记为可疑"，这是双刃剑。
3. **[#831 + #829 fix: pin 2 unpinned action(s)](https://github.com/swisskyrepo/payloadsallthethings/pull/831)** — 揭示了**安全仓库自身也需要供应链安全治理**，对 GitHub Actions pinning 的关注。
4. **[#828 Add PayloadsAllTheThings Integration Tool (patt.py)](https://github.com/swisskyrepo/payloadsallthethings/pull/828)** + **[#841 Added AI Agents for Offensive Security to the books](https://github.com/swisskyrepo/payloadsallthethings/pull/841)** — 揭示了**社区正在围绕此项目构建工具化（patt.py）和 AI 化（AI Agents for Offensive Security）衍生品**，项目开始从"静态文档"向"动态工具平台"演化的早期信号。

> **对理解项目设计的意义**: 仓库定位不是"一个 markdown 集合"，而是"渗透测试知识与工具生态的入口"。

## 知识入口

- **DeepWiki**: 页面存在（https://deepwiki.com/swisskyrepo/payloadsallthethings）但未抓取到实质内容（页面 loading）；标注"未收录完整分析"
- **Zread.ai**: 返回 403，标注"未收录"
- **关联论文**: 未检索到 arXiv 等学术文献直接引用（标注"无"）
- **在线 Demo**: 无（项目是文档型仓库，无可运行 Demo）
- **第三方学习资源**:
  - Material for MkDocs 渲染站点: https://swisskyrepo.github.io/PayloadsAllTheThings/
  - 内置 `_LEARNING_AND_SOCIALS/BOOKS.md` 与 `_LEARNING_AND_SOCIALS/YOUTUBE.md` 推荐书单和频道
  - 官方 Twitter/X: @pentest_swissky
  - 姊妹站点 InternalAllTheThings / HardwareAllTheThings

## 项目展示素材

### README 媒体

1. ![banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png) — 类型: **hero**（README 顶部、`<p align="center">` 包裹的官方 banner，已通过 `gh api .../contents/.github/banner.png` 验证存在，size=829,829 bytes）

### 官网媒体

无（官网仅渲染 README 文本 + Material for MkDocs 装饰图标，**无独立 hero/banner/screenshot 媒体**）。

### 筛选说明

- 总共发现 1 个核心媒体元素（README 顶部 banner.png）
- 排除了 7+ 个 badge/CI 状态图标：`shields.io/static/v1?label=Sponsor`、`shields.io/twitter/url`、GitHub contributors 墙 `contrib.rocks/image?repo=`、赞助方头像（`avatars.githubusercontent.com/u/34724717` SerpApi、`u/50994705` ProjectDiscovery、`u/48131541` VAADATA）、Tweet 分享按钮等
- 保留 1 个最核心的 hero 横幅图

## 快速判断

- **是否值得深入**: **是**（条件：你是 Web 安全/红队/漏洞赏金从业者或研究者；纯应用开发者收益有限）
- **初步定位**: **大众热门 — 垂直赛道的"事实标准"**（属于"必须收藏/参考"的级别，但已是显学，不属于被低估的潜力股）
- **作者可信度**: **高**
  - 理由：账号年龄 11 年、粉丝 1 万+、同作者 "AllTheThings" 家族多项目互相支撑、持续更新（最近 push 2026-04-22）、被 Kali Linux 官方仓库收录、有 SerpApi/ProjectDiscovery/VAADATA 等商业赞助背书
- **竞品格局**: **细分市场 + 事实标准**（不是红海，因为垂直细分；不是蓝海，因为已被该项目占据心智）
- **核心信号**:
  - 项目处于"成熟稳态"而非衰退期（最近 release v4.2 = 2025-07-26，最近 push 2026-04-22）
  - 正在向 **LLM 安全** 新前沿扩张（#835/#836 Web LLM Attacks）
  - 社区开始围绕其构建工具（patt.py）与 AI 衍生（AI Agents for Offensive Security）— 演化方向值得持续观察
  - 项目自身在被 Semgrep 等扫描器误报 — 揭示了"安全教学仓库"的身份悖论
