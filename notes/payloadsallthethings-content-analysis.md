## 动机与定位

- 要解决的问题:
  - 渗透测试 / Bug Bounty 场景下，**payload 与 bypass 知识碎片化**于个人笔记、推特、博客、Discord 频道，难以快速检索复用；新手难以系统性掌握 Web 漏洞利用与绕过的"成体系字典"。
  - 把"如何构造 payload、为什么能 bypass、怎么 fuzz、用什么工具复现"压缩为**章节化的可执行参考手册**，覆盖"漏洞介绍 → 工具 → 方法论 → 实验 → 引用"的完整闭环。
  - 提供**与 Burp Suite（业界渗透测试事实标准）紧耦合的 Intruder 字典**，让文档能直接驱动工具执行，而不只是描述。

- 为什么现有方案不够:
  - **OWASP CheatSheetSeries** (32k ⭐) 走"防御侧"叙述（如何防护），不是"利用侧"。
  - **SecLists** (~60k ⭐) 是"原材料"，一堆 .txt，没有方法论、没有工具调用样例、没有图示。
  - **foospidy/payloads** (3.9k ⭐) 与 **daffainfo/AllAboutBugBounty** (6.7k ⭐) 覆盖广度或深度不如 PATT；前者项目节奏已放缓，后者偏"个人报告集合"风格。
  - 没有任何既有项目同时做到 **"结构化模板 + 跨 DBMS 细分 + Intruder 字典 + 配图 + 实验平台引用 + MkDocs 美化"** 这六位一体。

- 目标用户:
  - Web 渗透测试工程师（红队 / 顾问 / 内部安全）
  - Bug Bounty 猎人（自学或复现他人报告）
  - 安全研究员与 CTF 选手
  - 安全自学者与培训讲师
  - 蓝队也可以反向用——读懂攻击者的字典以增强 WAF/SAST 规则

- 项目本质定性:
  - **不是软件项目**，而是**"GitHub-as-CMS 的内容仓库"**——以 Markdown 为内容、以 Pull Request 为编辑流、以 GitHub Pages + Material for MkDocs 为发布面。
  - 治理难度不亚于代码项目：140+ .md 章节需要一致性、PR 需要 lint、链接/引用需要追踪。

---

## 作者视角

### 问题发现

- **直接源自 dogfooding（自身痛点）**：Swissky 是 Bug Hunter 出身，每次做新目标的 SQLi/XSS/SSTI 测试都要去翻推特、博客、过去自己的笔记找 payload——重复劳动、低效、易遗漏。
- **工程实践沉淀**而非学术研究延伸：作者没有把它包装成"通用安全本体"或"漏洞分类法"论文，而是用最朴素的"按漏洞类型建文件夹 + README 模板"形式沉淀。
- **时机选择（2016 启动）**:
  - 2015-2016 是 Burp Suite Pro 在渗透测试行业全面普及、bug bounty 平台（HackerOne/Bugcrowd）开始爆发的关键节点。
  - OWASP Top 10 已经稳态多年、漏洞类型已经收敛（Top 10 + 各种新兴绕过），可以开始"系统性整理"而不是"追新"。
  - SecLists 虽早但以 .txt 为主，缺乏语境化文档；MkDocs 等静态站点工具成熟，让"GitHub 当 CMS"变得可行。
  - 早期 **markdownlint、Material for MkDocs、GitHub Pages** 三件套在 2016-2018 完成流行化，提供了低成本"专业外观"。

### 解法哲学

- **简单 vs 功能完整**：选了"**内容广度优先 + 模板一致性**"——不追求单点深度做到研究论文级（如 SSTI 没有自成一篇研究综述），但所有漏洞类型都"有目录、有字典、有图、有实验"，让用户 30 秒内能判断"我该不该深入"。
- **开放 vs 封闭**：选**真正开放**（genuinely open, 不是 open-core）——
  - CONTRIBUTING.md 明确写出 sanitization 规则（如用 `[ATTACKER.DOMAIN.TLD]`、`10.10.10.10` 这类占位符）——既接受贡献又防止"恶意 PR 在 README 里塞真的 exploit URL"。
  - 三大公开赞助商（SerpApi、ProjectDiscovery、VAADATA）出现在 README 但不阻挡贡献。
  - 没有"Pro 版"、没有 SaaS 入口、没有付费内容。
- **明确不做什么**（克制）:
  - 不做 SaaS 漏洞扫描器（那是 Nuclei / sqlmap / Burp 的活）
  - 不做漏洞情报聚合/时序跟踪（那是 nuclei-templates / Exploit-DB 的活）
  - 不做"学习路径"（用 _LEARNING_AND_SOCIALS 列书与 YouTube，**链接出去而不是内化**）
  - 不教"零基础"（README 第一句就假定读者懂 Web 漏洞基础）
- **价值主张清晰**：**"我给你的是带语境的字典，而不是字典"**——每个 payload 旁边配工具调用、检测方法、WAF 绕过条件。

### 背景知识迁移

- **从 Bug Bounty 实战中来的"语境感知"**：作者理解"同样的 SQLi payload 在 MySQL 8.0 + 严格 WAF 下还需要 Unicode 替换"，所以才有 `Encoding Transformations` 独立章节 + `FUZZDB_*` 字典 + `Generic_WAFBypass` 章节。
- **从 Burp Suite 生态来的"工具链绑定"**：每章都有 Intruder 目录——说明作者深谙"研究员的工作流是 Burp + Repeater + Intruder + Decoder"，所以**字典命名直接对应 Intruder 位置**（如 `FUZZDB_MySQL-WHERE_Time.txt`）。
- **从红队运营中来的"占位符规范"**：CONTRIBUTING.md 里的占位符规则（`id` / `whoami` / `[ATTACKER.DOMAIN.TLD]` / `DC01` / `P@ssw0rd`）——是红队真实作战时为避免"payload 误触发"和"报告截图脱敏"总结的实务经验，不是教科书能教出来的。
- **从材料工程(Materials Science)社区来的"标准模板思维"**：README 章节结构 `Tools / Methodology / Labs / References` 几乎是"科学论文结构"的非正式版本。

### 战略图景

- **核心位置**（不是基础设施）：PATT 是 Swissky 个人 IP 的**旗舰项目**——10k+ 关注、10k+ star、最近推送排第 1。
- **基础设施位置**：在 **AllTheThings 家族战略**中承担 **"Web 应用层"** 这一面：
  - PATT = Web 应用安全
  - InternalAllTheThings (2,238 ⭐) = AD/内网渗透
  - HardwareAllTheThings (885 ⭐) = IoT/硬件安全
  - SSRFmap (3,559 ⭐)、GraphQLmap (1,664 ⭐) = 衍生工具
- **品牌化策略**："AllTheThings" 已经是 Swissky 在渗透测试社区的**个人品牌**——所有项目都带这个后缀，形成可识别的家族矩阵。
- **商业化意图**：
  - **直接商业化：无**（无 SaaS、无 Pro 版、无课程订阅）
  - **间接商业化**：GitHub Sponsors + 三家公开赞助商 + 个人咨询声望
  - 这种"声量 → 咨询/演讲机会"的路径，比 SaaS 更契合单人独立研究者身份。
- **开源策略**：
  - **genuinely open**（MIT License + 公开贡献规则 + 无歧视）
  - 但**实际上依赖 Swissky 本人长期 editorial**：所有 PR 默认被 Swissky 审核（commit 占比 >60%），开放性 ≠ 治理民主化，更像是"以 Swissky 主编为中心的维基"。

---

## 架构与设计决策

### 目录结构概览

**顶层组织**：每个 Web 漏洞类型 = 一个顶层文件夹（70+ 个），文件夹名即"漏洞类别"（如 `SQL Injection/`、`Server Side Request Forgery/`、`CORS Misconfiguration/`），**目录名即 URL 路径即 SEO 关键词**。

**次层组织**（按漏洞可选）：
- `README.md` — 必选，主入口与方法论
- `Intruder/` — Burp 字典
- `Images/` — 配图（PNG/PNG 占位）
- `Files/` — 引用到的样本文件（如 XXE 的 .xml 样本）
- 跨方言/平台细分文件（如 `SQL Injection/MySQL Injection.md`）
- 特殊子目录（如 `Upload Insecure Files/CVE FFmpeg HLS/`）— 一漏洞多 PoC 时的拆分

**辅助顶层**：
- `_template_vuln/` — 章节脚手架（README.md 模板）
- `_LEARNING_AND_SOCIALS/` — 外部学习资源（BOOKS / TWITTER / YOUTUBE）
- `Methodology and Resources/` — 跨主题 cheatsheet（30+ .md：AD/Cloud/Container/Windows）
- `.github/workflows/` — CI（markdownlint + mkdocs build）
- `.github/overrides/` — MkDocs theme overrides
- `mkdocs.yml` — 站点生成配置

**命名约定**：
- 空格允许出现在目录名（`Server Side Template Injection/`）— GitHub URL 会编码为 `%20`
- Intruder 字典用 `FUZZDB_` 前缀或下划线分隔的 `Type_DBMS_Technique` 命名法
- 配图命名 `wildcard_underscore.jpg`、`Unicode_SQL_injection.png`（描述性 + 主题）

### 关键设计决策

1. **决策**: 每个漏洞章节用统一的"四件套"结构 `README + Intruder + Images + Files`
   - 问题: 渗透测试是"工具调用密集型"任务，纯文本 payload 没用，必须**可被工具直接消费**
   - 方案: 章节强制包含可被 Burp Intruder 消费的 .txt 字典、可被 README 引用的 .xml/.gif/.php 样本、说明流程的截图
   - Trade-off: 牺牲了"纯文档纯粹性"——仓库膨胀（每个章节 3-5 个子文件），但**获得了"文档即工具"的高实战价值**
   - 可迁移性: **高**——任何"领域知识 + 工具链"项目都可套用（如威胁情报库 + MISP 导出、SOC playbook + Splunk SPL）

2. **决策**: 设立 `_template_vuln/` 作为脚手架
   - 问题: 70+ 章节需要一致性，纯靠人盯 PR 不可持续
   - 方案: 提供一个最小可复制的 README 模板，规定 `Tools / Methodology / Labs / References` 四段式 + Summary TOC
   - Trade-off: 模板可能束缚**新类型漏洞**的叙述（如 Serverless / LLM 的章节可能不天然匹配）
   - 可迁移性: **高**——是"内容仓库贡献标准化"的范本，胜过"读我整个 CONTRIBUTING.md 几百行字"

3. **决策**: 跨方言/平台细分（如 SQL Injection 拆出 8 个 DBMS 文件）
   - 问题: "SQL Injection" 概念覆盖太广，MySQL 跟 BigQuery 的 payload 几乎不通用
   - 方案: 母章节作入口（"概览" + Summary TOC 链接），子文件按平台/语言/引擎细分（`MySQL Injection.md`、`PostgreSQL Injection.md`、`SQLmap.md`）
   - Trade-off: 增加了认知跳跃（用户必须懂自己面对的 DB 才能选对文件），但**避免了"10000 行的 SQLi 章节不可读"**
   - 可迁移性: **中**——适用于任何"广概念 + 多实现"领域（如 Protocol Buffers 各语言实现、CI 系统各平台、Linux 各发行版）

4. **决策**: Intruder 字典的命名约定 `FUZZDB_<DBMS>_<Technique>.txt`
   - 问题: Burp Intruder 是行处理工具，字典名 = 用户记忆负担
   - 方案: 自描述文件名（`FUZZDB_MSSQL-WHERE_Time.txt` = "FUZZDB 项目里的 MSSQL WHERE 子句时间盲注字典"）
   - Trade-off: 牺牲了"简短命名"，但**字典可独立分发/复用**——`FUZZDB` 前缀还让外部合并（从 SecLists 借鉴时）一望即知出处
   - 可迁移性: **高**——所有"以文件名携带语义"的工具/数据集项目都应这样

5. **决策**: CONTRIBUTING.md 强制 sanitization（占位符协议）
   - 问题: 一个 PR 里写 `curl evil.com/x` 就有真实危害；payload 字典如果包含真实 exploit 链接是法律雷区
   - 方案: 强制使用 `id` / `whoami` / `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `P@ssw0rd` 等占位符
   - Trade-off: 牺牲"真实感"（payload 看着不如真实 exploit 那样"活"），换来**法律与伦理安全** + CI 自动化校验可行性
   - 可迁移性: **高**——任何"涉及攻击/越权 payload 的开源知识库"都该采用类似的占位符规范

6. **决策**: 用 `Methodology and Resources/` 把跨主题 cheatsheet 集中
   - 问题: Reverse Shell / AD Attack / Cloud / Linux Priv Esc 是"工具型 cheatsheet"而非"漏洞型 payload 字典"——放顶层会让目录膨胀且与漏洞章节混淆
   - 方案: 单独建一个 `Methodology and Resources/` 目录收纳，同时把部分内容（如 AD）**外迁**到 `InternalAllTheThings`（用引用而非重复）
   - Trade-off: 牺牲了"一站式搜索"——用户需要在 PATT 与 IATT 之间跳转，但**避免了内容腐烂**（一份资料只在一个地方维护）
   - 可迁移性: **高**——是"知识库家族"的真正做法（中心化维护，分发用引用）

7. **决策**: CI 包含两个 workflow：`check-markdown.yml`（PR 时 lint）+ `mkdocs-build.yml`（master push 时构建）
   - 问题: 70+ 章节的 markdown 仓库，没有 lint 必然格式腐烂
   - 方案: PR 时只 lint **改动的文件**（`tj-actions/changed-files` + 增量 lint）——既保证一致性又控制 CI 时间
   - Trade-off: 旧章节不会被自动 lint 整改；需要志愿者手动跑全量
   - 可迁移性: **高**——大型 markdown 仓库的标准做法

8. **决策**: 用 Material for MkDocs 渲染、`custom_dir: overrides`、加 `umami` 统计
   - 问题: GitHub README 直出阅读体验差（无搜索/无侧栏 TOC/无夜间模式）
   - 方案: MkDocs + Material theme + 自定义 overrides（注入 addtoany 分享、umami 统计）+ light/dark palette 自动切换
   - Trade-off: 维护一个 `mkdocs.yml` 配置文件、依赖 docs submodule、每次 master push 跑一次 build——成本不低
   - 可迁移性: **中**——任何"严肃的 markdown 仓库"都该上 MkDocs，但**注意 submodule 复用的复杂度**

9. **决策**: README 顶部用 `intruder` 风格的"safe payload"占位符
   - 问题: 仓库本身被 Semgrep 等安全扫描器**误报为"含恶意 payload"**（PR #843 揭露）
   - 方案: 在 CONTRIBUTING.md 写明占位符规范、README 顶部加 sponsor 链接和免责声明（DISCLAIMER.md）——用文档 + 社区规范解决工具误报
   - Trade-off: 不可能 100% 解决——Semgrep 等扫描器仍会报警；这是"安全知识库"的结构性张力
   - 可迁移性: **高**——任何含"双用途"内容（payload、漏洞利用、绕过）的项目都该有 DISCLAIMER.md + 严格的占位符规则

10. **决策**: PR 主导 / Issues 禁用（社区众包扩充通过 PR）
    - 问题: Issues 会被大量"如何利用"的低质问题淹没
    - 方案: 直接关闭 issues，让所有"补充 payload"通过 PR 走 markdownlint + review
    - Trade-off: 牺牲了"提问者作为新贡献者入口"的常见漏斗
    - 可迁移性: **中**——对"成熟、维护者精力有限"的知识库项目适用，新项目不应照搬

---

## 创新点

1. **"四件套" 漏洞章节标准模板**（README + Intruder + Images + Files）
   - 描述: 业界最早用"结构化目录"承载"漏洞方法论 + 可执行 payload + 工具消费 + 可视化"的项目
   - 新颖度: 3/5（不原创，但**首个规模化**做到这个组合的）
   - 实用性: 5/5（直接驱动 Burp 工作流）
   - 可迁移性: 4/5（任何"知识 + 工具"型项目可借鉴）
   - 适用场景: 领域知识库、CTF write-up 仓库、SOC playbook 库

2. **跨方言/平台细分的母-子章节模式**（SQLi 拆 8 个 DBMS）
   - 描述: 解决"单章节太胖"的可读性问题
   - 新颖度: 3/5（教科书早就这么干，但**实战 cheat sheet 圈层内不算常见**）
   - 实用性: 5/5
   - 可迁移性: 5/5（任何"广概念 + 多实现"领域都适用）
   - 适用场景: 协议实现库（HTTP/2 各浏览器）、CI 系统（GitHub Actions / GitLab CI / Jenkins）、CVE PoC 集合

3. **GitHub-as-CMS + Material MkDocs 渲染管线** + 增量 lint
   - 描述: 70+ 章节的 markdown 仓库用 `tj-actions/changed-files` 增量 lint、master 自动构建
   - 新颖度: 2/5（这是 MkDocs 官方推荐做法）
   - 实用性: 5/5（解决"大型 markdown 仓库格式腐烂"顽疾）
   - 可迁移性: 4/5
   - 适用场景: 任何 >50 .md 的开源文档项目

4. **占位符 sanitization 协议**（强制 `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10`）
   - 描述: 在 CONTRIBUTING.md 明确"payload 必须脱敏"的占位符字典
   - 新颖度: 4/5（**这是 PATT 真正的护城河之一**）
   - 实用性: 5/5
   - 可迁移性: 4/5
   - 适用场景: 任何含"双用途/攻击性"内容的开源项目（exploit-db、payloads、nuclei-templates）

5. **AllTheThings 家族矩阵**（Web + Internal + Hardware + 工具 = 个人品牌）
   - 描述: 单一维护者用统一后缀命名 + 互相引用 + 共享 `_LEARNING_AND_SOCIALS` 资源
   - 新颖度: 3/5
   - 实用性: 4/5（让个人 IP 资产组合化）
   - 可迁移性: 4/5
   - 适用场景: 独立研究者的开源作品集（任何"个人知识矩阵"）

6. **"内容仓库做安全研究品牌" 的版本**（与工具化产品对立）
   - 描述: 主动选择"不开发自动扫描器"，让影响力来自**知识整理 + 引用信誉**，而不是产品
   - 新颖度: 4/5（这是 2024+ 越来越多人走的路：知识 > 工具）
   - 实用性: 4/5
   - 可迁移性: 5/5（任何"信息差大、工具竞争白热化"领域都该考虑）
   - 适用场景: 威胁情报、漏洞复现、CVE 解读、CTF write-up

7. **新兴主题"Web LLM Attacks" 的快速接入**（PR #835/#836）
   - 描述: 当 2024 年 LLM 安全成为焦点时，PATT 用同样模板新建章节，与传统 Web 漏洞并列
   - 新颖度: 3/5（不是第一个做 LLM 安全的，但**是首个把它纳入"Web AllTheThings"框架**的）
   - 实用性: 4/5
   - 可迁移性: 5/5（任何"主题收敛型知识库"该有"新主题快速接入"流程）
   - 适用场景: AI 安全、Serverless 安全、eBPF 安全

8. **社区衍生品反哺**（`patt.py` 集成工具、PR #841 "AI Agents for Offensive Security" 书籍）
   - 描述: 围绕 PATT 已经自发出现工具化、AI 化衍生品，说明**知识库正在从内容走向生态**
   - 新颖度: 3/5
   - 实用性: 3/5（依赖社区自组织）
   - 可迁移性: 3/5
   - 适用场景: 任何"用户量大、覆盖广"的知识库

---

## 可复用模式

1. **"四件套"目录结构**: `README + Intruder + Images + Files` — 适用场景: 领域知识 + 工具链深度结合的项目（威胁情报库、SOC playbook、CTF write-up）
2. **跨方言/平台细分的母-子章节**: 解决"单章节不可读" — 适用场景: 协议实现、CI 系统、漏洞类型、框架适配
3. **占位符 sanitization 协议**: 强制 `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` — 适用场景: 任何含"双用途"内容的知识库（exploit、payload、nuclei-templates）
4. **`_template_vuln` 脚手架**: CONTRIBUTING 中放一个最小可复制模板胜过千行说明 — 适用场景: 所有"接受外部贡献"的大型内容仓库
5. **Material MkDocs + 增量 markdownlint**: 大型 markdown 仓库的标准工程化 — 适用场景: >50 .md 的文档项目
6. **家族矩阵 + 互相引用 + 共享学习资源**: AllTheThings 模式 — 适用场景: 独立研究者的开源作品集
7. **PR 主导 / Issues 禁用**: 成熟项目防止 issues 洪水 — 适用场景: 高 star + 单维护者的知识库
8. **内容仓库做品牌**: 不做 SaaS，靠"内容深度 + 引用信誉"积累影响力 — 适用场景: 任何"信息差大、工具竞争白热化"领域

---

## 竞品交叉分析

**关键维度（按用户决策权重排序）**：
1. **覆盖广度**（漏洞类型齐全度）
2. **Payload 可执行性**（能否直接喂给工具）
3. **结构化程度**（章节是否一致、可检索）
4. **实战性**（payload 是否经真实 bounty 验证）
5. **贡献活跃度**（PR 速度、commits）

### vs OWASP/CheatSheetSeries (32,152 ⭐)

- 我们更好:
  - **"利用侧"视角 vs 防御侧**——PATT 教"怎么打"，OWASP 教"怎么防"
  - **Payload 可执行性**——PATT 的 Intruder 字典直接喂 Burp；OWASP 是叙述性 prose
  - **新兴主题更新速度**——PATT 几周内接入 Web LLM Attacks，OWASP 一年一次 stable
  - 视觉化（流程图）+ 实战（Labs 链接）——OWASP 是 PDF/HTML 长文
- 竞品更好:
  - **权威性 / 引用率**——OWASP 是行业标准，PATT 是"个人维基"
  - **防御代码示例**（如"如何写安全的 ORM 查询"）——PATT 只有"如何利用"，没有"如何修"
  - **国际化翻译**（多语言版本）——PATT 仅英文
- 不同目标:
  - **OWASP 给"蓝队 + 培训 + 审计"**；**PATT 给"红队 + bounty + 自学"**
  - 错位竞争，互不替代
- 用户迁移成本: 极低——大多数安全工程师两边都用

### vs danielmiessler/SecLists (~60k+ ⭐)

- 我们更好:
  - **结构化程度**——PATT 每个 payload 有"为什么 + 怎么用 + 图示 + 实验"，SecLists 是"裸 .txt"
  - **可检索性**——MkDocs 全文搜索，SecLists 全靠文件名
  - **跨方言细分**——PATT 的 SQLi 按 DBMS 拆 8 个文件，SecLists 也有但**没有叙述语境**
- 竞品更好:
  - **原始覆盖度**（字典/词表/用户名/密码/UA 等）——SecLists 远超 PATT（PATT 只覆盖 Web 漏洞 payload）
  - **社区规模**（60k+ ⭐，是渗透测试"原材料"事实标准）
  - **下载/集成工具链友好**（如 ffuf / gobuster 默认引用 SecLists）
- 不同目标:
  - **SecLists 是"原材料"**（wordlist / payload list）
  - **PATT 是"加工后的知识"**（带语境的 cheat sheet）
  - **互为补充**：PATT 引用 SecLists 的 `FUZZDB_*` 文件作为字典
- 用户迁移成本: 不需要迁移——一般用户两者都用（SecLists 喂工具，PATT 查方法）

### vs foospidy/payloads (3,953 ⭐)

- 我们更好:
  - **覆盖广度**（PATT 70+ 类别 vs foospidy 主打 XSS/SQLi/CMD）
  - **结构化模板**（PATT 四件套 vs foospidy 几乎裸 .txt）
  - **维护活跃度**（PATT 几乎周更 vs foospidy 多年未更新）
  - **家族矩阵 + MkDocs** vs foospidy 仅 GitHub 浏览
- 竞品更好:
  - **历史地位**（foospidy 2014 立项，是"payloads all the things"概念的鼻祖之一）
  - **极简风格**（无叙述负担，纯 payload）
- 不同目标: foospidy 适合"我要直接 copy payload"，PATT 适合"我想理解为什么这样 payload"
- 用户迁移成本: 低——foospidy 用户转 PATT 几乎无学习成本

### vs daffainfo/AllAboutBugBounty (6,759 ⭐)

- 我们更好:
  - **结构化 + 模板**（PATT 是知识库，AllAboutBugBounty 是"个人 bounty 报告合集"）
  - **Payload 字典**（PATT 强项 vs AllAboutBugBounty 几乎没有）
  - **维护活跃度 + 品牌矩阵** vs AllAboutBugBounty 单一项目
- 竞品更好:
  - **真实 bounty 报告**（AllAboutBugBounty 收录具体被披露的漏洞 case，含金额/平台/状态）
  - **学习路径指引**（面向 bounty 新手的"如何开始"内容更丰富）
- 不同目标:
  - AllAboutBugBounty = "案例集 / 经验分享"
  - PATT = "工具书 / 速查手册"
- 用户迁移成本: 低——大多数 bounty 玩家两者都用

### vs swisskyrepo/InternalAllTheThings (2,238 ⭐) — 同作者姊妹项目

- 我们更好:
  - **Web 层覆盖**（PATT 独占 Web 漏洞场景）
  - **跨社区贡献者**（PATT >1000 contributor vs IATT 较少）
- 竞品更好:
  - **AD/内网/Windows**（IATT 的"方法论深度"远超 PATT 里的 `Methodology and Resources/`，因为后者已外迁到 IATT）
- 不同目标: **垂直分工**——PATT = Web，IATT = 内网
- 用户迁移成本: 几乎零（同一作者、同一风格、互相引用）
- 战略含义: **协同护城河**——两个 repo 互相倒流，"用户粘性"显著高于单项目

### 综合竞争结论

- **差异化护城河**:
  - **生态护城河**（最高）：家族矩阵 + 跨工具（SSRFmap、GraphQLmap）+ 6+ 年 commit 沉淀 + 1000+ 贡献者社区——这些**没法用钱/时间快速复制**
  - **品牌护城河**（高）：Swissky 在 bug bounty 圈的"Swissky 说到 PATT"是"SecLists 之于字典"的等价物
  - **网络效应护城河**（中）：PR 主导的众包内容扩充——贡献者越多，权威性越强，吸引更多贡献者
  - **技术护城河**（低）：单一 MkDocs 渲染 + 模板化文件结构，技术上不复杂
- **竞争风险**:
  - **最可能替代**：**被"AI 驱动的智能 payload 生成器"取代**——例如 AI Agent 输入"目标 URL + 漏洞类型"自动生成定制 payload（PR #841 显示社区已经在往这个方向走）。如果 PATT 不主动集成 AI 化，5 年后可能被类似工具抢用户。
  - **次要风险**：**被 nuclei-templates 这类"结构化 YAML 化"项目冲击**——nuclei-templates 把"漏洞利用"做成机器可执行，且与 ProjectDiscovery 工具链深度集成（ProjectDiscovery 已是 PATT 赞助商）
- **生态定位**:
  - PATT 是**"渗透测试人员的速查手册 + Burp 字典的标准化源"**——位于"知识层"，而非"工具层"
  - 与 sqlmap/Nuclei/Burp 是**互补关系**（PATT 教思路，工具做执行）
  - 与 SecLists 是**"语境补强"关系**（SecLists 是字典，PATT 是字典的"使用说明"）
  - 在 Web 安全知识图谱中的位置：**"漏洞类型 → 方法论" 这一中间层**——比 CVE 抽象层低，比工具命令行高

---

## 代码质量

**说明：这是内容仓库，质量评估调整为「内容质量 + 治理质量 + 工程化」三个维度。**

### 质量检查清单

- [x] **统一的章节模板（`_template_vuln`）**: 存在并明确在 README + CONTRIBUTING.md 引用
- [x] **CI/CD 配置**: `check-markdown.yml`（增量 lint）+ `mkdocs-build.yml`（自动部署）
- [x] **markdown lint / 格式校验**: `.markdownlint.json` 配置 + PR 时自动跑
- [x] **CONTRIBUTING.md 贡献指南**: 详尽，含 sanitization 规则、模板说明、Docker 验证命令
- [x] **`_LEARNING_AND_SOCIALS` 资源索引**: BOOKS + TWITTER + YOUTUBE 三个 .md
- [x] **Sister Projects 引用**: InternalAllTheThings + HardwareAllTheThings 在 README 显式列出
- [x] **示例 / 演示（图片、Intruder 字典、Files 样本）**: 70+ 章节多数配套
- [x] **LICENSE**: MIT（Copyright Swissky, 2019）
- [x] **DISCLAIMER.md**: 明确"仅供教育研究、用户自负其责"——重要的法律护盾
- [x] **FUNDING.yml**: GitHub Sponsors 配置
- [ ] **测试覆盖**: N/A（内容仓库）
- [x] **`.gitignore`**: 简洁（`BuildPDF/`、`.vscode`、`.todo`）
- [x] **变更历史 / CHANGELOG.md**: 不存在，但通过 GitHub Releases / PR 历史可追踪
- [x] **Issue 模板**: 不存在（Issues 禁用）
- [x] **PR 模板**: 不显式存在（CONTRIBUTING.md 充当）

### 维度评分

| 维度 | 评级 | 说明 |
|------|------|------|
| **内容质量** | **优秀** | 70+ 漏洞章节覆盖广、深度均衡、payload 实战可用；引用（References）格式严格（author/title/link/date + Wayback 兜底）；跨方言细分（SQLi 8 个 DBMS、SSTI 多种引擎）体现深度。 |
| **文档质量** | **优秀** | README 简洁、CONTRIBUTING.md 详尽、DISCLAIMER.md 必备；统一四件套结构；140+ .md 累计 21,527 行——大型 markdown 仓库的中上水平。 |
| **治理质量** | **优秀** | CONTRIBUTING.md 规范、PR 主导流、增量 lint、占位符 sanitization、赞助商披露、DISCLAIMER——内容仓库治理的范本。 |
| **工程化（CI/lint/模板）** | **完善** | 两个 GitHub Actions workflow + `.markdownlint.json` + `_template_vuln` + `mkdocs.yml` 完整配置；Material theme overrides 注入统计 + 分享。 |
| **错误处理（不适用）** | N/A | 内容仓库无运行时错误处理。 |
| **品牌/家族策略** | **优秀** | AllTheThings 矩阵 + 个人品牌沉淀，是"独立研究者"开源策略的典范。 |
| **法律/伦理安全** | **优秀** | MIT + DISCLAIMER + 占位符规范——双用途内容项目的必做项全部到位。 |

### 综合结论

- **整体评级：内容质量、治理质量、工程化均达到"优秀"水平**
- **领先项**：
  - 跨方言细分的母-子章节模式是渗透测试圈层的范本
  - 占位符 sanitization 协议是双用途内容项目的护盾
  - 家族矩阵 + 互相引用是个人研究者的品牌资产
- **可改进项**（按重要性）：
  1. 增量 lint 不会自动整改旧章节——可以加一个 quarterly workflow 跑全量 lint 并开 issue
  2. 无 CHANGELOG / 无 Releases——大版本变更难以追踪
  3. References 链接腐烂风险——Wayback Machine 兜底已做但仍可考虑
  4. `Methodology and Resources/` 与 `InternalAllTheThings` 的边界需要更明确（已有外迁，但仍有重复）
- **最终判断**：PATT 是**"内容型安全知识库"的天花板项目之一**——治理完善、品牌扎实、社区活跃、可持续性强。对任何想搭建"领域知识 + 工具链"开源项目的人来说，是**学习模板**。
