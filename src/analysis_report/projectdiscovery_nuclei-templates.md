# 13K 模板 × 1,300 贡献者：漏洞扫描的「npm registry」怎么炼成

> GitHub: https://github.com/projectdiscovery/nuclei-templates

## 一句话总结

nuclei-templates 是漏洞扫描领域最大的「**detection-as-data 众包平台**」——用 YAML DSL 把「漏洞定义」做成可机械同步的数据文件，配合四套机器人 + 现金悬赏 + 三段式质量门，把新 CVE 从披露到全球可检测的窗口期从数天压缩到数小时。

## 值得关注的理由

- **范式领导地位**：13,324 个 YAML 模板、12.5k stars、3,521 forks，在「**应用层主动扫描**」这一格是事实标准——和 Sigma/YARA/Snort 一样是 detection-as-data 范式的标杆，但**独占了 Web 漏洞扫描格**。
- **元数据纪律罕见**：仓库元数据（cves.json 2MB、TEMPLATES-STATS.md 1.5MB、templates-checksum.txt 1.1MB）的**总规模超过 README**——把「Git 即数据库」做到极致的工程化样本。
- **机器贡献率 36.4%**：四套机器人（ghost / actions-user / MostInterestingBotInTheWorld / PDBot）协同——这是 AI 写规则的「早期部署样本」，领先业内两年。
- **Bounty-driven 众包**：明确文档化的 $50–$250 现金悬赏 + 💎 Bounty 标签 + 强制 vulnerable docker 验证——把「模板生产」变成全球可竞争市场。
- **健康 OSS-CS 路径**：商业化（PDCP 云平台）不污染开源体验，模板永远完整公开——是值得所有开源安全工具参考的**商业化范本**。

## 项目展示

README 媒体极简（仅 repobeats 提交活跃度 + contrib.rocks 贡献者墙），项目展示素材以**实操样例**和**运行截图**为主，散布在 docs.projectdiscovery.io。

- 模板签名流程: 见 .github/workflows/template-sign.yml（密码学签名 PR）
- 实际模板范本: `/http/cves/2021/CVE-2021-44228.yaml`（Log4Shell）、`/http/cves/2024/CVE-2024-0012.yaml`（PAN-OS auth bypass）

> README 和官网均无展示性 hero 图，建议读者直接看 `http/cves/2024/` 下最新模板来直观感受 YAML DSL 的精炼。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/projectdiscovery/nuclei-templates |
| Star / Fork | 12,491 / 3,521 |
| Watcher / Open Issue / Open PR | 203 / 59 / 63 |
| 代码行数 | 968,067 行（YAML 99.4% / JSON 0.6%）|
| 文件数量 | 13,324 |
| 项目年龄 | 6 年（首提交 2020-04-04）|
| 总 commit | 70,874（最近 30 天 1,004，最近 90 天 3,413）|
| 开发阶段 | 密集开发（dev_stage）|
| 贡献模式 | 核心 5 人 + 1,290 社区 + 4 机器账户（机器贡献 36.4%）|
| 热度定位 | 大众热门（heat_level）|
| 质量评级 | 代码 5/5（schema 严格） 文档 5/5（4 语言 README + 3 个指南） CI/CD 5/5（13 个 workflow）|
| License | MIT（与 nuclei 引擎同许可）|
| Tag / Release | 327 / 100（语义化版本，与 nuclei 引擎同步）|
| 月均 commit | 1,453（2025-12 峰值 3,178）|

## 作者视角：为什么存在这个项目

### 创始人/作者背景

归属 **ProjectDiscovery** 组织（2019-05 成立，11,393 粉丝），使命「Democratize Security」。创始人 Sandeep（ehsandeep）从 fuzzing/bug bounty 行业起家，把 fuzzing 行业的核心 insight——**把语料当数据，不要把 fuzzer 写成代码**——迁移到漏洞检测领域：nuclei-templates 是同一个思路在 detection 领域的应用。

公司产品矩阵：nuclei（29.1k stars，Go 引擎）+ nuclei-templates（12.5k）+ subfinder（13.8k）+ httpx（10k）+ katana/naabu/cvemap 等。**nuclei-templates 是开源漏扫 SaaS 的内容护城河**。

### 问题判断

传统漏洞扫描器（Nexpose/Nessus/OpenVAS）把 detection 写成闭源二进制插件或 NASL 脚本，bug bounty hunter 无法快速写出「今天爆出的 CVE 模板」，导致**新 CVE 出现到检测能力上线**的窗口期可能数天到数周。三个外部条件在 2020 年同时成熟：① YAML 在 DevOps 圈已普及（K8s/Ansible/Terraform）② bug bounty 平台（HackerOne/Bugcrowd）成熟带来大量 CVE POC ③ 远程办公爆发让 ASM 需求暴涨。

### 解法哲学

把 detection **抽象为数据**（YAML）而非**代码**（Python/Go 插件），让安全研究员不必是 Go 程序员也能贡献。**明确选择不做的**：① 任意控制流（无法像 Burp 插件做循环/重试/条件分支）② 复杂协议（仅 HTTP/TCP/DNS/FILE/SSL/CODE/JAVASCRIPT/HEADLESS/CLOUD/DAST 10 类）③ 商业闭源。

这种取舍换来的是：**5 分钟写一个模板 + 即刻全球共享**的扩展性。**detection-as-code** 不是新词，但**detection-as-data** 是 nuclei-templates 真正的范式创新。

### 战略意图

README 顶部直接链 `cloud.projectdiscovery.io/templates`——**开源模板库是流量入口，云平台是商业转化**。免费版每月有扫描额度天花板，超额订阅 PDCP。这与 Elastic（ES → Elastic Cloud）、GitLab（CE → EE）的开源-商业化路径一脉相承，但**商业化不污染开源体验**（没有 SaaS 锁定、没有功能阉割、模板永远完整公开）。

## 核心价值提炼

### 创新之处（按新颖度 × 实用性排序）

| 创新点 | 新颖度 | 实用性 | 可迁移性 |
|---|---|---|---|
| **CVE 编号即文件名**（id == filename == git path）| 4/5 | 5/5 | 5/5 |
| **Git 即数据库**（cves.json/TEMPLATES-STATS.md 机器 commit）| 4/5 | 5/5 | 5/5 |
| **三段式质量门**（lint→validate→runtime）+ weak-matcher 自动拒绝 | 5/5 | 5/5 | 4/5 |
| **Bounty-driven crowdsourced detection-as-code** | 4/5 | 5/5 | 4/5 |
| **多源威胁情报自动 sync**（NVD+EPSS+CISA KEV+VulnCheck KEV）| 4/5 | 5/5 | 5/5 |
| **.review-bot LLM 预审**（仓库内嵌 prompt）| 4/5 | 4/5 | 3/5 |
| **OAST 外带检测**（interactsh-url + DNS 回带）| 5/5 | 5/5 | 4/5 |
| **Honeypot 反向校验**（CI 主动跑模板打 honey.scanme.sh）| 5/5 | 4/5 | 4/5 |

### 可复用的模式与技巧

1. **「外部标识符驱动命名」**：用 CVE/CWE/CPE/ATT&CK/Bugzilla 这类权威 ID 当文件名/ID，让跨工具链的翻译成本降到 0。**任何对接外部本体的数据集都该这么干**。
2. **「Git 即数据库」**：用 Git + Actions 把「派生数据」（索引/统计/校验和/增量列表）作为 commit artifact 推到仓库——零基础设施 + PR 可审计 + 用户 `curl raw.githubusercontent.com` 即同步。**任何用 SQLite/JSON 做对外数据源的小项目都可借鉴**。
3. **「三段式可执行规范」**：把 review 标准编码成 lint→validate→runtime 三段式 CI 门，把「防误报」从口头建议变成 CI 必过门。**任何需要众包生产的项目（规则集/翻译/标注）都可参考此分层**。
4. **「AI 写规则 + 人类 review」**：`MostInterestingBotInTheWorld` AI 账号 + `.review-bot` LLM 预审 + 人类核心维护者三段式——这是**LLM 时代难得的「先有规范再上 AI」路径**。
5. **「Bounty 加速众包」**：把「写模板」明码标价作为商品，让全球社区用机会成本最低的方式填空白。**关键约束**：「MUST share vulnerable setup information」——把可复现性从软性建议变成支付前提。
6. **「机器人账号即身份层」**：四个 bot 账号（ghost/actions-user/MIBTW/PDBot）承担不同职责，让 commit history 视觉上立刻区分「机器写的」和「人写的」，**透明度可审计**。
7. **「多语言运营走 IaC」**：4 份 README 模板化（`README_CN.tmpl`）由 readme-update.yml 自动重写——把多语言运营也做成 CI 流水线。

### 关键设计决策（trade-off 分析）

#### 决策 1：YAML DSL + 四段式 schema

- **问题**：怎么让「写检测」和「运行检测」解耦，让非 Go 程序员也能贡献
- **方案**：`info` 块自描述元数据（CVE/CVSS/CWE/EPSS/CPE/tags）+ `requests` 块描述探测行为 + `matchers` 块定义命中条件 + `extractors` 块提取结构化字段
- **Trade-off**：牺牲「任意控制流」，换 PR 友好（diff 即审查）+ 引擎可预编译 + 模板签名/校验变简单
- **可迁移性**：高。任何「探测型」任务（云配置扫描、合规检查、DNS 健康度）都可套用

#### 决策 2：二维目录分类法（协议 × 用途）

- **问题**：9000+ 模板怎么组织才能让用户快速定位 + 引擎按场景批量加载
- **方案**：一级按协议（http/network/dns/file/ssl/cloud/code/javascript/headless/dast），HTTP 内部再按用途分（cves/exposed-panels/technologies/vulnerabilities/...）
- **Trade-off**：牺牲「跨协议检测同一漏洞」的表达力，换用户能用 glob 精细控制扫描范围（`-t http/cves/`）
- **可迁移性**：高。是 Unix 工具链「小工具组合」思想的现代版

#### 决策 3：CVE 编号即文件名

- **问题**：如何让 cves.json、git log、搜索引擎、外部 POC 平台都能机械同步这些模板
- **方案**：用 CVE 编号作为稳定标识符，模板 ID 字段也等于文件名
- **Trade-off**：牺牲「按产品名聚合浏览」的便利，换 ① 跨工具链 0 翻译成本 ② git log 可按 CVE 搜 ③ 第三方（VulnCheck/NVD）可反向索引
- **可迁移性**：高

#### 决策 4：Git 即数据库

- **问题**：13K+ 模板的全集索引、统计、增量变更怎么对外暴露
- **方案**：cves.json / cves.json-checksum.txt / templates-checksum.txt / TEMPLATES-STATS.md / TEMPLATES-STATS.json / .new-additions 都是机器人自动生成并 commit
- **Trade-off**：牺牲「实时查询」和「高写入吞吐」（commit 一次要等 CI），换 ① 零基础设施 ② PR 可审计 ③ 用户直接 `curl raw.githubusercontent.com` 就能拿
- **可迁移性**：高

#### 决策 5：Bounty-driven crowdsourced detection-as-code

- **问题**：关键 CVE（KEV 列表里的）需要 24h 内出检测，但维护者产能有限
- **方案**：高价值 CVE 用 💎 Bounty 标签 + $50–$250 现金悬赏 + 强制要求 PR 附带 vulnerable docker + 由 `/attempt` `/claim` 机器人评论协议认领
- **Trade-off**：牺牲「完全控制」（任何人都能提 PR，需严格 review），换 ① 产能按需扩展 ② 把「模板生产」变成全球可竞争市场
- **可迁移性**：高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | nuclei-templates | Sigma rules | YARA rules | Nmap NSE | OWASP ZAP addons | Nessus plugins |
|------|-----------------|-------------|------------|----------|------------------|----------------|
| 数据格式 | YAML | YAML | YARA DSL | Lua | XML/JS/Java | NASL（闭源）|
| 引擎解耦 | 完全解耦 | 完全解耦 | 完全解耦 | 半耦合 | 半耦合 | 完全闭源 |
| 规则规模 | 13K | 3K+ | 20K+ | 600+ | 1K+ | 100K+ |
| 社区贡献 | 1,300+ | 300+ | 500+ | 100+ | 200+ | 内部分析师 |
| 检测时机 | 主动 | 被动（SIEM）| 被动（文件）| 主动 | 主动（代理）| 主动 |
| 主要场景 | Web 漏洞/暴露面 | 日志关联 | 恶意样本 | 端口/服务发现 | 拦截代理 | 漏洞管理 |
| 弱 matcher 风险 | **有**（CI 自动拦）| 中 | 中 | 低 | 低 | 不公开 |
| 学习曲线 | 极低（YAML）| 低 | 中 | 高（Lua）| 高 | 不可学 |
| 商业化路径 | OSS → PDCP | OSS（无）| OSS（无）| OSS（无）| OSS（无）| 纯商业 |
| 元数据自动 sync | **NVD/EPSS/KEV 四源** | 无 | 无 | 无 | 无 | 内置 |
| Bounty 激励 | **$50–$250 + 标签** | 无 | 无 | 无 | 无 | 无 |

### 差异化护城河

1. **「最易贡献的格式 + 最强激励 + 最快元数据保鲜」三者叠加**：
   - YAML 4 段式让「写模板」门槛低到 5 分钟上手
   - Bounty 悬赏让「写模板」有现金回报
   - 每日 NVD/EPSS/KEV 自动 sync 让「模板保鲜」无人化
2. **Honeypot 反向校验**（CI 主动跑模板打 honey.scanme.sh）——把「防误报」从口头建议变成 CI 必过门，**这是其他规则库都没做的工程化实践**。
3. **三段式质量门 + .review-bot LLM 预审**——把「review 标准」编码成可执行规则，1300 贡献者的产能才能稳定输出。
4. **Git 即数据库**——5 个派生数据文件（cves.json / templates-checksum.txt / .new-additions / TEMPLATES-STATS.md / TOP-10.md）全部机器生成并 commit，第三方工具 `curl raw.githubusercontent.com` 即可同步。

### 竞争风险

- **最可能替代**：
  - 商业版（Tenable Nessus）——如果企业用户更看重覆盖广度而非响应速度
  - 新一代 AI 驱动扫描器（**如果**它们把 detection 抽象做得更易用，可能从下层颠覆）
- **来自 Sigma/YARA 的侧翼**——如果未来 detection 范式融合（一个 YAML 同时被 SIEM 关联 + 主动扫描使用），nuclei-templates 需要扩展协议维度

### 生态定位

**「应用层主动扫描」这一格的事实标准**。在更大的 detection-as-data 生态里：
- **Sigma** = 日志关联层（被动、事后）
- **YARA** = 文件检测层（被动、静态）
- **Snort/Suricata** = 网络 IDS 层（被动、流量）
- **nuclei-templates** = **应用层主动扫描层**（主动、Web）
- **Nessus/Qualys** = 商业综合扫描层

四者**正交而不竞争**，共同构成 detection-as-data 范式的完整生态。nuclei-templates 在它占据的格子里**没有同量级对手**。

## 套利机会分析

- **信息差**：**不存在信息差**——12.5k stars + 3,521 forks 是大众热门级，且 bug bounty/security 是热门领域。但**detection-as-data 范式可迁移到其他领域**这一点，很多项目还没意识到——这是读者的认知差。
- **技术借鉴**：
  - **「外部标识符驱动命名」** → 任何对接外部本体的数据集（CWE/CPE/ATT&CK/Bugzilla）都该这么干
  - **「Git 即数据库」** → 任何「对外数据源」的小项目都该把派生数据 commit 到仓库
  - **「三段式质量门」** → 任何需要众包生产的项目（规则集/翻译/标注）都该套用
  - **「Bounty 加速众包」** → 任何「开放式内容生产」项目都可用 bounty 加速
  - **「机器人账号即身份层」** → 任何混 AI + 人类协作的项目都该做身份分层
- **生态位**：填补了「**应用层主动扫描**」格子的开源空白，对标商业版（Nessus）的开源 + 社区 + AI 三位一体替代。
- **趋势判断**：
  - **增长中**：2025-12 单月 3,178 commit（历史峰值），对应 AI 写规则机器人的成熟
  - **符合技术趋势**：AI 写代码、detection-as-data、开源商业化、bug bounty 全都在风口
  - **比竞品后发优势**：商业版（Nessus）已经 30+ 年，但**响应新 CVE 的速度**上 nuclei-templates 已经反超（KEV 列表 1496 个全部有模板）——这是**「开源速度 > 商业广度」**的胜利

## 风险与不足

1. **过度依赖机器账户**：4 个机器账户贡献率 36.4%，若任一账户签名/权限失效，可能引发 commit 历史混乱或元数据漂移。
2. **fix 占比统计失真**：commit_type_distribution 中 `other` 77% 反映 conventional commit 未普及，**对「误报修复」类改动缺乏语义标记**，不利于工程化运营。
3. **CVE 单一类目集中**：`http/cves` 占 hot_dirs 修改 88%——若攻击面从 Web 转向移动/IoT/供应链，模板库需要重新组织目录结构（issue #15275 已经在讨论把 `http/vulnerabilities` 转 CVE 化）。
4. **.review-bot 依赖 LLM**：评论质量不可严格保证——LLM 不如专家，需要 prompt 持续维护。
5. **部分老模板（pre-2019）缺 EPSS/KEV/CPE 字段**，与新模板观感不一致——技术债。
6. **学习曲线虽低但弱 matcher 难写**：新人最容易踩坑的地方，bounty 拒稿率高。
7. **模板运行需要 vulnerable docker 验证**，新人本地调试成本高。

## 行动建议

### 如果你要用它

- **Bug bounty 工作流**：直接用 `nuclei -l urls.txt -t http/cves/`，KEV 优先
- **企业 ASM**：用 `-severity high,critical` + `-t http/exposed-panels/,http/technologies/`，低噪声高价值
- **CI/CD 集成**：用 `nuclei -sign` 验签模板（`NUCLEI_USER_CERTIFICATE`），防止供应链攻击
- **vs 商业版（Nessus）**：选 nuclei-templates 如果你需要**响应新 CVE 极快 + 开源可定制**；选 Nessus 如果你需要**覆盖广度 + 厂商支持 + 合规报告**
- **vs Sigma/YARA**：三者**正交不冲突**——nuclei-templates 主动扫 Web、Sigma 关联日志、YARA 检样本，可同时部署

### 如果你要学它

重点关注的文件/模块：
- **范式层**：`README.md` + `TEMPLATE-CREATION-GUIDE.md`（513 行 SOP）+ `TEMPLATE-REVIEW-GUIDE.md`（432 行）
- **设计层**：`http/cves/2021/CVE-2021-44228.yaml`（Log4Shell 范本）+ `http/cves/2024/CVE-2024-0012.yaml`（PAN-OS auth bypass 范本）
- **质量门**：`tests.yml`（lint→validate→weak-matcher 三段式）+ `.review-bot`（LLM 预审 prompt）
- **自动化**：`cves.json` + `templates-checksum.txt` + `.new-additions` + `TEMPLATES-STATS.md` 4 个机器生成元数据
- **Bounty 机制**：`Templates-Bounty-FAQ.md` + `PULL_REQUEST_TEMPLATE.md`
- **工程纪律**：`.yamllint` + `.pre-commit-config.yml` + `.github/workflows/autoassign.yml`（公平派单算法）

### 如果你要 fork 它

可改进的方向：
1. **修复弱 matcher 自动检测**：当前 `weak-matcher-checks.sh` 是基于 honeypot 的被动校验，可以扩展为主动 fuzzing 模板输入，发现更多边界误报
2. **LLM 评审 prompt 升级**：当前 `.review-bot` 是规则化 prompt，可接入更结构化的「先 lint 输出错误、再 diff 比对 best practice、最后给评分」流水线
3. **元数据多源化**：当前 EPSS/KEV 都是定时 sync，可以接入实时威胁情报（vulnCheck NVD++、GreyNoise）做按需增量
4. **跨范式融合**：探索一个 YAML 同时被 SIEM 关联 + 主动扫描使用的可能性（与 Sigma 合作）
5. **本地 RAG 知识库**：把 TEMPLATES-STATS.md 灌成向量库，让企业用户能用自然语言「找所有 log4j 模板」

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/projectdiscovery/nuclei-templates |
| Zread.ai | https://zread.ai/projectdiscovery/nuclei-templates |
| 关联论文 | 无（detection-as-data 范式尚无系统学术综述）|
| 在线 Demo | https://cloud.projectdiscovery.io/templates（PDCP 云平台）|
| 官方文档 | https://docs.projectdiscovery.io/templates/introduction |
| 核心元数据 | https://raw.githubusercontent.com/projectdiscovery/nuclei-templates/main/cves.json |
| Top 10 速查 | https://raw.githubusercontent.com/projectdiscovery/nuclei-templates/main/TOP-10.md |
