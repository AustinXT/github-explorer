# 9.5 年 78k stars：Web 渗透 payload 字典如何做成赛道事实标准

> GitHub: https://github.com/swisskyrepo/payloadsallthethings

## 一句话总结

PayloadsAllTheThings 是一个用 GitHub 当 CMS、由独立红队 Swissky 主导 9.5 年的 Web 渗透测试 payload 速查手册——78k stars、70+ 漏洞章节、5.4 万行 payload 字典，是 Burp 生态的事实标准**带语境的字典**，而非裸字典。

## 值得关注的理由

- **品类事实标准**：在 Web 渗透测试 payload 文档这个垂直赛道里，它是 78k stars 的 No.1，被 Kali Linux、OWASP Cheat Sheet Series、PortSwigger 官方文档交叉引用，是新人入行绕不开的参考手册。
- **"文档即工具" 的范本**：每个漏洞章节采用统一的"四件套"（README + Intruder 字典 + Images 截图 + Files 样本），payload 可以直接喂给 Burp Suite 执行——这是把"知识库"和"工具链"焊死在一起的设计。
- **AllTheThings 家族矩阵的母项目**：同作者还维护 InternalAllTheThings（AD/内网渗透）、HardwareAllTheThings（IoT）、SSRFmap、GraphQLmap——一个独立研究者用统一后缀命名 + 互相引用 + 共享学习资源，建立渗透测试社区的个人品牌资产。

## 项目展示

![banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png)

> 官方 banner 图（829KB，master 分支已验证存在）。项目其他媒体主要是各漏洞章节内的 Intruder 字典片段与流程截图，分布在 70+ 章节的 `Images/` 子目录中。

**在线浏览版本**：<https://swisskyrepo.github.io/PayloadsAllTheThings/>（Material for MkDocs 渲染的镜像站点，带全文搜索和夜间模式）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/payloadsallthethings |
| Star / Fork | 78,134 / 17,028 |
| Watcher | 1,961 |
| Open Issues | 0（仓库已禁用 Issues 跟踪） |
| Open PRs | 17 |
| 代码行数 | 2,096 行真代码 + 54,442 行 payload/字典（96% 是文档内容） |
| 语言分布 | Python 61% (实质是 Markdown 文档) / ASP.NET 9% / XSLT 7% / 其他 ~23% |
| 文件数量 | 447 个（其中 140+ 个 Markdown 章节） |
| 依赖数量 | 0（纯内容仓库） |
| 项目年龄 | 116 个月（2016-10 → 2026-04，约 9.5 年） |
| 总 Commit | 2,185 |
| 贡献者 | 334 人（Swissky 本人占 61.4%，Top 5 占 72%） |
| License | MIT |
| 最近 Release | v4.2 "FERRETEDITOR"（2025-07-26），共 7 个 Tag |
| 开发阶段 | 稳定维护 → 缓慢下行（年 commit 从 380 降至 ~100） |
| 贡献模式 | 单人深度主导 + 社区众包扩充 |
| 热度定位 | 大众热门 + 垂直赛道事实标准（GitHub Top 0.05%） |
| 质量评级 | 内容[优秀] 文档[优秀] 治理[优秀] 工程化[完善] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Swissky（@swisskyrepo）**，自述 "Red Team Operator & Bug Hunter"，账号创建于 2015-04-28，至今约 11 年。公开仓库仅 13 个，但每个都是"渗透测试相关"——形成清晰的"AllTheThings"品牌矩阵：

- **PayloadsAllTheThings**（78k ⭐）— Web 应用层
- **InternalAllTheThings**（2,238 ⭐）— AD/内网渗透
- **HardwareAllTheThings**（885 ⭐）— IoT/硬件安全
- **SSRFmap**（3,559 ⭐）— SSRF 工具
- **GraphQLmap**（1,664 ⭐）— GraphQL 工具

粉丝 1 万+，关注仅 13（高度精选）。被 SerpApi、ProjectDiscovery、VAADATA 三家商业公司公开赞助。**典型画像：独立红队顾问 + 安全布道者**。

### 问题判断

2016 年启动时的具体痛点：

- 渗透测试工程师每次做新目标的 SQLi/XSS/SSTI 都要去翻推特、博客、过去自己的笔记找 payload——重复劳动、低效、易遗漏
- **SecLists**（60k+ ⭐）虽大但只是"裸字典"——没有方法论、没有工具调用样例、没有图示
- **OWASP CheatSheetSeries**（32k ⭐）走"防御侧"叙述，不是"利用侧"

时机选择（2016 启动）正逢：
- Burp Suite Pro 在行业全面普及
- HackerOne/Bugcrowd 等 bug bounty 平台爆发
- Material for MkDocs、GitHub Pages 三件套成熟让"GitHub 当 CMS"变得可行

### 解法哲学

Swissky 选择了"内容广度优先 + 模板一致性"，明确**不做什么**：

- 不做 SaaS 漏洞扫描器（那是 Nuclei/sqlmap/Burp 的活）
- 不做漏洞情报聚合/时序跟踪（那是 nuclei-templates/Exploit-DB 的活）
- 不教"零基础"（README 第一句就假定读者懂 Web 漏洞基础）
- **价值主张清晰**："我给你的是带语境的字典，而不是字典"——每个 payload 旁边配工具调用、检测方法、WAF 绕过条件

### 战略意图

在 Swissky 的开源战略中，PATT 是**旗舰项目**（最近推送排第 1 位），在 AllTheThings 家族矩阵中承担"Web 应用层"这一面。

**商业化策略**：无 SaaS、无 Pro 版、无课程订阅。商业化靠**间接路径**——GitHub Sponsors + 三家公开赞助商 + 个人咨询声望。"声量 → 咨询/演讲机会"比 SaaS 更契合单人独立研究者身份。

**开源策略**：genuinely open（MIT + 公开贡献规则），但**实质依赖 Swissky 本人长期 editorial**（所有 PR 默认被审核，commit 占比 >60%）——更像是"以 Swissky 主编为中心的维基"，而非"治理民主化"的开源。

> 无专门博客或架构文章——项目本质是文档型仓库，README + 各章节 README 即全部"文档"。社区通过 PR 进行"架构演进"。

## 核心价值提炼

### 创新之处

按新颖度×实用性排序：

1. **占位符 sanitization 协议**（新颖 4/5，实 5/5）：在 CONTRIBUTING.md 强制使用 `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` 等占位符——是双用途内容项目的法律护盾，也是 PATT 真正的护城河之一。
2. **"内容仓库做品牌" 的版本**（新颖 4/5，实 4/5）：主动选择"不开发自动扫描器"，让影响力来自**知识整理 + 引用信誉**，而不是产品——是 2024+ 越来越多人走的路。
3. **"四件套" 漏洞章节标准模板**（新颖 3/5，实 5/5）：每个漏洞章节统一 `README + Intruder + Images + Files`——业界最早用"结构化目录"承载"漏洞方法论 + 可执行 payload + 工具消费 + 可视化"的项目。
4. **跨方言/平台细分的母-子章节**（新颖 3/5，实 5/5）：SQLi 拆出 MySQL/PostgreSQL/MSSQL/Oracle/SQLite/BigQuery/Cassandra/DB2 八个 DBMS——解决"单章节不可读"的顽疾。
5. **AllTheThings 家族矩阵**（新颖 3/5，实 4/5）：单一维护者用统一后缀命名 + 互相引用 + 共享 `_LEARNING_AND_SOCIALS` 资源。
6. **GitHub-as-CMS + Material MkDocs 渲染管线** + 增量 lint（新颖 2/5，实 5/5）：用 `tj-actions/changed-files` 增量 lint，master 自动构建——大型 markdown 仓库的工程化范本。
7. **新兴主题"Web LLM Attacks" 的快速接入**（新颖 3/5，实 4/5）：2024-2026 几周内接入 LLM 安全新章节，与传统 Web 漏洞并列——首个把 LLM 安全纳入"Web AllTheThings"框架的项目。
8. **社区衍生品反哺**（新颖 3/5，实 3/5）：社区已自发出现 `patt.py` 集成工具、"AI Agents for Offensive Security" 衍生——知识库正在从内容走向生态。

### 可复用的模式与技巧

可直接迁移到其他项目的高价值设计模式：

1. **"四件套" 目录结构**（README + 工具消费文件 + 配图 + 样本文件）——适用：任何"领域知识 + 工具链"项目（威胁情报库 + MISP 导出、SOC playbook + Splunk SPL、CTF write-up）
2. **`_template_vuln` 脚手架**——CONTRIBUTING 中放一个最小可复制模板胜过千行说明。适用：所有"接受外部贡献"的大型内容仓库
3. **占位符 sanitization 协议**——强制 `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `id` / `P@ssw0rd`。适用：任何含"双用途/攻击性"内容的开源项目（exploit-db、payloads、nuclei-templates）
4. **跨方言/平台细分的母-子章节**——SQLi 拆 8 个 DBMS 解决"单章节太胖"。适用：协议实现、CI 系统、漏洞类型、框架适配
5. **Material MkDocs + 增量 markdownlint**——`tj-actions/changed-files` + PR 时增量 lint。适用：>50 .md 的开源文档项目
6. **家族矩阵 + 互相引用 + 共享学习资源**——AllTheThings 模式。适用：独立研究者的开源作品集
7. **PR 主导 / Issues 禁用**——防止 issues 洪水，让所有"补充 payload"通过 PR 走 markdownlint + review。适用：高 star + 单维护者的成熟知识库
8. **内容仓库做品牌**——不做 SaaS，靠"内容深度 + 引用信誉"积累影响力。适用：任何"信息差大、工具竞争白热化"领域

### 关键设计决策

**决策 1：每个漏洞章节用统一的"四件套"结构 `README + Intruder + Images + Files`**
- **问题**：渗透测试是"工具调用密集型"任务，纯文本 payload 没用，必须**可被工具直接消费**
- **方案**：章节强制包含可被 Burp Intruder 消费的 .txt 字典、可被 README 引用的 .xml/.gif/.php 样本、说明流程的截图
- **Trade-off**：牺牲了"纯文档纯粹性"——仓库膨胀（每个章节 3-5 个子文件），但**获得了"文档即工具"的高实战价值**
- **可迁移性**：高

**决策 2：跨方言/平台细分（SQL Injection 拆出 8 个 DBMS 文件）**
- **问题**："SQL Injection" 概念覆盖太广，MySQL 跟 BigQuery 的 payload 几乎不通用
- **方案**：母章节作入口（"概览" + Summary TOC 链接），子文件按平台/语言/引擎细分
- **Trade-off**：增加了认知跳跃（用户必须懂自己面对的 DB 才能选对文件），但**避免了"10000 行的 SQLi 章节不可读"**
- **可迁移性**：高

**决策 3：Intruder 字典的命名约定 `FUZZDB_<DBMS>_<Technique>.txt`**
- **问题**：Burp Intruder 是行处理工具，字典名 = 用户记忆负担
- **方案**：自描述文件名（`FUZZDB_MSSQL-WHERE_Time.txt` = "FUZZDB 项目里的 MSSQL WHERE 子句时间盲注字典"）
- **Trade-off**：牺牲了"简短命名"，但**字典可独立分发/复用**——`FUZZDB` 前缀还让外部合并（从 SecLists 借鉴时）一望即知出处
- **可迁移性**：高

**决策 4：CONTRIBUTING.md 强制 sanitization（占位符协议）**
- **问题**：一个 PR 里写 `curl evil.com/x` 就有真实危害；payload 字典如果包含真实 exploit 链接是法律雷区
- **方案**：强制使用 `id` / `whoami` / `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `P@ssw0rd` 等占位符
- **Trade-off**：牺牲"真实感"（payload 看着不如真实 exploit 那样"活"），换来**法律与伦理安全** + CI 自动化校验可行性
- **可迁移性**：高

**决策 5：用 `Methodology and Resources/` 把跨主题 cheatsheet 集中 + 外迁到 InternalAllTheThings**
- **问题**：Reverse Shell / AD Attack / Cloud / Linux Priv Esc 是"工具型 cheatsheet"而非"漏洞型 payload 字典"——放顶层会让目录膨胀且与漏洞章节混淆
- **方案**：单独建一个 `Methodology and Resources/` 目录收纳，同时把部分内容（如 AD）**外迁**到 `InternalAllTheThings`（用引用而非重复）
- **Trade-off**：牺牲了"一站式搜索"——用户需要在 PATT 与 IATT 之间跳转，但**避免了内容腐烂**（一份资料只在一个地方维护）
- **可迁移性**：高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | OWASP CheatSheetSeries | SecLists | foospidy/payloads | AllAboutBugBounty |
|------|---------|--------|--------|--------|--------|
| Stars | 78,134 | 32,152 | ~60k+ | 3,953 | 6,759 |
| 视角 | **利用侧（攻击）** | 防御侧 | 原材料（裸字典） | 利用侧（早期） | 案例集（bounty 报告） |
| 覆盖广度 | 70+ 漏洞类别 | 80+ 防御主题 | 海量字典/词表 | XSS/SQLi/CMD 为主 | bounty 实战技巧 |
| Payload 可执行性 | **Burp Intruder 字典直接可用** | 叙述性 prose | 裸 .txt | 几乎裸 .txt | 几乎无字典 |
| 结构化程度 | 四件套模板 + 跨方言细分 | 长文 PDF/HTML | 文件名分类 | 弱 | 个人笔记风格 |
| 实战性 | 高（payload 实战可用） | 低（理论） | 中（需自行构造语境） | 中 | 高（真实 case） |
| 贡献活跃度 | 周更，年 ~100 commit | 一年一版 | 持续 | 多年未更新 | 中等 |
| 品牌矩阵 | AllTheThings 家族 | OWASP 官方 | 单项目 | 单项目 | 单项目 |
| License | MIT | CC BY-SA 4.0 | MIT | MIT | MIT |

### 差异化护城河

- **生态护城河（最高）**：家族矩阵 + 跨工具（SSRFmap、GraphQLmap）+ 9.5 年 commit 沉淀 + 1000+ 贡献者社区——**没法用钱/时间快速复制**
- **品牌护城河（高）**：Swissky 在 bug bounty 圈的"Swissky 说到 PATT"是"SecLists 之于字典"的等价物
- **网络效应护城河（中）**：PR 主导的众包内容扩充——贡献者越多，权威性越强，吸引更多贡献者
- **技术护城河（低）**：单一 MkDocs 渲染 + 模板化文件结构，技术上不复杂

### 竞争风险

- **最可能替代**：**被"AI 驱动的智能 payload 生成器"取代**——例如 AI Agent 输入"目标 URL + 漏洞类型"自动生成定制 payload（PR #841 显示社区已经在往这个方向走）。如果 PATT 不主动集成 AI 化，5 年后可能被类似工具抢用户。
- **次要风险**：**被 nuclei-templates 这类"结构化 YAML 化"项目冲击**——nuclei-templates 把"漏洞利用"做成机器可执行，且与 ProjectDiscovery 工具链深度集成（ProjectDiscovery 已是 PATT 赞助商，**这是双刃剑**）。

### 生态定位

- 位于**"漏洞类型 → 方法论" 这一中间层**——比 CVE 抽象层低，比工具命令行高
- 与 sqlmap/Nuclei/Burp 是**互补关系**（PATT 教思路，工具做执行）
- 与 SecLists 是**"语境补强"关系**（SecLists 是字典，PATT 是字典的"使用说明"）
- 与 OWASP CheatSheetSeries 是**攻防对偶关系**（PATT 攻，OWASP 防）

> PATT **不是替代品，而是速查手册的范本**。OWASP、SecLists、foospidy、AllAboutBugBounty 都不是真正的"竞品"——而是**不同维度的互补/上游/案例**关系。

## 套利机会分析

- **信息差**：**被严重高估而非低估**——已是品类事实上第一名（同类工具集合中 GitHub Star 最高）。任何新文档站点/工具集都默认以它为参照。**不适合作为"被低估的潜力股"入场**，但适合作为**学习/借鉴的对象**。
- **技术借鉴**: 八个可迁移模式（见"可复用的模式与技巧"小节）几乎都适合其他项目——特别是"四件套目录结构"和"占位符 sanitization 协议"可以原样套用到威胁情报库、CTF write-up、exploit-db 等任何"双用途内容"项目。
- **生态位**: 在 Web 安全知识图谱中填补了"漏洞类型 → 方法论"中间层的空白，且通过家族矩阵把"Web → 内网 → 硬件"打通成端到端的渗透测试知识体系。
- **趋势判断**: 仍稳定在 20-50 star/日，最近 push 距今约 40 天（2026-04-22）——属于"持续高产"状态而非衰减。但年 commit 从 380 降至 ~100，**已进入稳定维护阶段**。社区正在向 AI 化（PR #841）、工具化（PR #828 patt.py）方向演化。

## 风险与不足

- **维护者单点风险**：Swissky 一人占 61.4% commit，无 Co-maintainer 机制——若作者停更，整个项目面临实质衰退
- **增量 lint 不会自动整改旧章节**：`_template_vuln` 之后新章节规范，旧章节仍可能不符合标准
- **无 CHANGELOG / 无 GitHub Releases**：大版本变更难以追踪（仅靠 git tag 推断）
- **目录命名不一致**：`XSS Injection` vs `XSS injection`、`Upload` vs `Upload Insecure Files` vs `Upload insecure files`——同一类目分散在多个目录中
- **"安全教学仓库"的身份悖论**：项目自身会被 Semgrep 等扫描器检测为"含恶意 payload"（PR #843），用 DISCLAIMER + 占位符规范缓解但无法根治
- **References 链接腐烂风险**：尽管已用 Wayback Machine 兜底，70+ 章节的外部引用仍有失效风险

## 行动建议

- **如果你要用它**：
  - Web 渗透测试工程师 / Bug Bounty 猎人：直接当**速查手册**用，结合 Burp Suite 工作流（Intruder 字典直接喂）
  - 蓝队 / WAF 规则设计者：反向阅读，理解攻击者字典以增强检测规则
  - 安全培训讲师：作为"渗透测试方法论"教学参考
  - 与 SecLists 配合使用（SecLists 是字典，PATT 是"字典使用说明"）

- **如果你要学它**：
  - 重点学习 **CONTRIBUTING.md**——它教"如何规范化接受社区贡献"是开源治理的范本
  - 重点学习 **`_template_vuln/`**——脚手架胜过千行说明
  - 重点学习 **`.github/workflows/`**——增量 lint + 自动部署的工程化做法
  - 重点学习 **`.markdownlint.json` + `mkdocs.yml`**——大型 markdown 仓库的配置范本

- **如果你要 fork 它**：
  - 可以改进的方向：
    1. 加一个 quarterly workflow 跑全量 lint 并开 issue
    2. 补充 CHANGELOG.md 与 GitHub Releases 模板
    3. 整理目录命名一致性（XSS / Upload 等多版本合并）
    4. 增加 AI 化衍生（PR #828 patt.py、#841 的方向）
    5. 增加更多新兴主题（Serverless 安全、eBPF 安全、API 安全、GraphQL 安全——GraphQLmap 工具已存在可联动）
  - 不要重新发明——而是成为 AllTheThings 家族矩阵的"行业垂直子项目"（如 CloudAllTheThings、MobileAllTheThings）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 页面存在但未收录完整分析（https://deepwiki.com/swisskyrepo/payloadsallthethings） |
| Zread.ai | 未收录（403） |
| 关联论文 | 无（无 arXiv 学术文献直接引用） |
| 在线 Demo | 无（项目是文档型仓库，无可运行 Demo） |
| 官方渲染站点 | https://swisskyrepo.github.io/PayloadsAllTheThings/（Material for MkDocs） |
| 内置学习资源 | `_LEARNING_AND_SOCIALS/BOOKS.md` + `YOUTUBE.md`（书单和 YouTube 频道推荐） |
| 姊妹项目 | InternalAllTheThings / HardwareAllTheThings / SSRFmap / GraphQLmap |
