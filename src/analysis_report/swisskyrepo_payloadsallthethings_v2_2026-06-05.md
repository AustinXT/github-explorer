# 78K stars、9 年长青：渗透测试界的「新华字典」PayloadsAllTheThings 怎么炼成

> GitHub: https://github.com/swisskyrepo/payloadsallthethings
>
> **版本说明**：本报告由 `/repo-miner` 于 2026-06-05 重新生成，与同目录 `swisskyrepo_payloadsallthethings.md`（旧版）并存，仅供版本对照。若需发布请用主文件。

## 一句话总结
PayloadsAllTheThings 是一个把 Web/内网/硬件安全测试所需的所有漏洞利用 payload 与绕过技巧「按漏洞类型结构化归档、可被 Burp 等工具直接消费」的社区驱动知识库，是渗透测试研究员的「键盘+Google」替代品。

## 值得关注的理由
- **结构化到极致**：每个漏洞一个目录，统一 `README + Intruder + Images + Files + _template_vuln` 五件套，贡献者门槛低，整库可被工具链批量处理
- **安全卫生做到教科书级**：RCE 用 `id/whoami`、IP 用保留段 10.10.10.10、回调用占位域 `[ATTACKER.DOMAIN.TLD]`、失效链接统一走 Wayback——可被企业安全报告与论文直接引用
- **10 年社区驱动**：333 位贡献者，Top 作者占 47.5%；每年 10 月靠 Hacktoberfest 集中收稿，已形成可持续的「集体维护+主理人审核」治理模式

## 项目展示

![PayloadsAllTheThings Banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png)

> 上方为仓库官方 banner；项目无 Demo 视频与架构示意图，「展示」靠结构化目录与 Burp Intruder 字典文件体现。

![Contributors](https://contrib.rocks/image?repo=swisskyrepo/PayloadsAllTheThings&max=36)

> 333 位社区贡献者头像矩阵——证明它是一个真正集体维护的项目，而非作者独角戏。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/payloadsallthethings |
| Star / Fork | 78,209 / 17,045 |
| Watcher | 1,962 |
| 代码行数 | 2,096 行（注释/说明 54,442 行，1:26 悬殊比） |
| 语言分布 | Python 61.1% / ASP.NET 9.0% / XSL 7.0% / ASP 3.5% / PHP 3.0% / 多语言混杂 |
| 项目年龄 | 9.6 年（2016-10 首次提交） |
| 开发阶段 | 低维护（近 365 天 105 commit，Hacktoberfest 集中收稿模式） |
| 贡献模式 | 社区驱动 + 主理人审核（Top 作者 swisskyrepo 占 47.5%，前 10 名合占 80%+） |
| 热度定位 | 大众热门（security topic 头部项目） |
| 质量评级 | 文档 [优秀] / 代码 [N/A] / 测试 [N/A] |
| License | MIT |
| 最新版本 | v4.2（共 7 个 tag，5 个 Release，2024-11 后无新 tag） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
**Swissky（@pentest_swissky）**：法语圈出身的资深红队/漏洞赏金猎人，2015-04 注册 GitHub，至今 11.1 年。账号 10,500 粉丝、13 个公开仓库，主营「AllTheThings」三件套（Payloads/Internal/Hardware）以及 SSRFmap、GraphQLmap 等被广泛引用的同源工具。10+ 年红队一线经验，Twitter @pentest_swissky 持续公开活动。

### 问题判断
在 2016 年项目启动时，安全研究员要找一个 SSTI payload 或 XXE 绕过方式，主要靠 Google + Twitter + 个人博客；这带来三个问题：
1. **散落**：研究结果写在别人博客里，搜索不到、复现不了
2. **污染**：Bug Bounty 报告里的 payload 经常带作者专属 callback 域，复制时把工作环境污染甚至误触发安全告警
3. **碎片化**：OWASP Cheat Sheet 偏防御、没 payload；HackTricks 类方法论笔记偏「流水账」，缺少按漏洞类型归档的颗粒度

Swissky 看到了「按漏洞类型结构化、可被工具消费」这个中段空白——既不是单纯防御文档，也不是工程师笔记本，而是「payload 字典」。

### 解法哲学
- **实用主义 payload 优先**：选 `id`/`whoami` 而非炫技反弹 shell；占位 IP 用 10.10.10.10、占位账号 `Administrator`、占位密码 `P@ssw0rd`——**安全卫生是核心价值观**
- **模板化 + 工具链消费**：`_template_vuln` 四件套刻意让内容可被脚本批处理；`.github/hopla_config.json` 把 payload 抽出来作为结构化 JSON，Hackvertor/HopLa Burp 扩展可直接消费
- **PR-only 治理**：open_issues = 0、open_prs = 17——把开放讨论收回到 PR 通道，markdownlint CI 兜底格式
- **明确的「不做什么」**：不做工具（与 Nuclei/Snallygaster 错位）、不做企业版、不开 SaaS、不做付费课程——保持纯 Wiki 形态

### 战略意图
这是 Swissky 个人品牌的三件套之一（Web/Internal/Hardware 矩阵），是 Bug Bounty 简历的「标志性资产」。商业化意图极弱——Sponsors 仅 SerpApi/ProjectDiscovery/VAADATA 三家小 logo，README 中 GitHub Sponsors 入口是仅有的变现渠道；**没有任何 SaaS / 培训 / 企业版信号**。MIT 协议下保持 **genuinely open** 而非 open-core。

## 核心价值提炼

### 创新之处
按新颖度×实用性排序：

1. **强模板 + 占位符协议**（新颖度 4/5 / 实用性 5/5 / 可迁移性 5/5）
   把「安全占位符」提到 CONTRIBUTING 规范层，统一 5 条占位规则；任何「内容会被直接复制运行」的知识库（PoC 仓库、IaC 模板、CTF writeup）都该学

2. **「Wiki 即 Burp 资源」双向桥接**（新颖度 4/5 / 实用性 4/5 / 可迁移性 3/5）
   不只把 payload 写在 Markdown，还把 `Intruder/` 文件夹、Burp 占位语法（`§HOST§`/`§IP§`/`§PORT§`）、`hopla_config.json` 做成「工具可消费层」

3. **PR-only 治理 + markdownlint 守卫**（新颖度 3/5 / 实用性 5/5 / 可迁移性 5/5）
   「1 个 PR = 1 段内容」让贡献可追溯、变更可审计；任何高贡献量、低门槛的「集体维护型」项目（chinese-poetry、awesome-*、free-programming-books）都适用

4. **AllTheThings 家族的内容路由升级**（新颖度 3/5 / 实用性 4/5 / 可迁移性 4/5）
   AD 攻击等内容从 Web 仓迁到 Internal 仓时，**原章节不删除，整页变成新仓链接目录**——保持 SEO 与外部引用不破

5. **Wayback Machine 作为引用防腐层**（新颖度 2/5 / 实用性 5/5 / 可迁移性 5/5）
   CONTRIBUTING.md **明文要求**所有失效链接改用 Wayback URL——让一份文档十年可读

### 可复用的模式与技巧
1. **「安全占位符协议」**：在 CONTRIBUTING 中**显式列出**命令/IP/域/账号/密码的统一占位字符串
2. **「目录即路由」**：老章节整页变成新仓链接目录，保留 anchor
3. **「双层结构化」**：同一份知识既以人类可读 Markdown 写，又以机器可消费 JSON 写（README + hopla_config.json）
4. **「PR-only + lint 守卫」**：Issue 关闭提交，PR 是唯一编辑通道，CI 跑 markdownlint
5. **「分支=站点源」**：主仓=内容源，gh-pages=构建产物，单 workflow 闭环

### 关键设计决策
1. **每个漏洞章节强制五件套（README/Intruder/Images/Files/_template_vuln）**：牺牲作者自由表达，换来**整库结构一致性与可被爬虫/工具批处理**
2. **失效链接统一走 Wayback**：牺牲直链新鲜度，换来**链接十年可读**（被多份企业安全报告、论文长年引用）
3. **markdownlint 作为唯一 CI 守卫（无 CI 测试）**：项目没有可编译代码，CI 跑测试无意义——但格式不统一会拖垮可读性
4. **`hopla_config.json` 双写**：维护成本翻倍（同一份 payload 在 README 和 JSON 各写一遍），换**生态可扩展性**

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | HackTricks | The Hacker Recipes | OWASP Cheat Sheet |
|------|---------|--------|--------|--------|
| 形态 | 分类索引 + payload 字典 | 工程师笔记本 | 故事化方法论 | 官方防御建议 |
| 漏洞类型覆盖 | 60+ 章节（全栈） | 100+（侧重内网/云） | 偏 AD/HTB | 主流 Web 漏洞 |
| Payload 可复制性 | ⭐⭐⭐⭐⭐（Intruder 字表） | ⭐⭐（命令参考） | ⭐⭐（叙述） | ❌（无 payload） |
| 工具链消费 | HopLa/Burp/Intruder 直读 | 弱 | 弱 | 弱 |
| 社区活跃度（近 1 年） | 中（年度 Hacktoberfest 集中） | 高（持续投稿） | 中 | 中 |
| 权威性 | 中（个人品牌） | 中（个人品牌） | 中（个人品牌） | 高（OWASP 基金会） |
| 防御视角 | 弱 | 弱 | 弱 | ⭐⭐⭐⭐⭐ |

### 差异化护城河
- **结构护城河**：强模板 + 占位符协议 + Intruder 资源——模仿者要重建的不是内容，而是 9 年沉淀的「五段式 README × 60 章节」一致性
- **生态护城河**：被 Burp/Hackvertor 工具链二次引用 + 企业安全报告/学术论文长年引用——新仓库拿不走「先发优势」沉淀的引用网络
- **品牌护城河**：Swissky + AllTheThings 家族心智——「Swissky 风格」已成渗透测试圈黑话

### 竞争风险
最可能威胁来自两个方向：
1. **HackTricks 在 Web 漏洞侧的「工具化」演进**：HackTricks 已开始做 fuzz JSON/字典；如果其工具链消费做得更好，可能蚕食 PATT 的差异化
2. **AI 辅助的 payload 生成**：未来模型直接吐出绕过 payload，削弱「现成字典」价值——这是 PATT 长期最大的范式风险

### 生态定位
**Web 应用安全 payload 知识库的「基础设施层」**——上层是工具（Nuclei/Burp）、下层是漏洞报告（漏洞赏金平台）、同层有 HackTricks 形成双寡头。PATT 处于「你要找 payload → 来 PATT 搜；你要理解方法论 → 去 HackTricks 看；你要写防御建议 → 引 OWASP」这个不可替代的中间位置。

## 套利机会分析
- **信息差**：❌ 严重高估（78K stars 已是事实标准），任何「被低估」指标对它都无效
- **技术借鉴**：✅ 极强——「安全占位符协议」「PR-only 治理 + lint 守卫」「双层结构化」三种模式可直接迁移到任何高贡献量知识库
- **生态位**：✅ 稳固——「按漏洞类型结构化的 payload 字典」这一垂直生态位，PATT 是定义者
- **趋势判断**：⚠️ 风险信号——近 30 天 0 commit、版本号 14 个月未升；但**仓库价值已从「靠更新拉粉」转为「被引用」**，增长稳态化是正常衰退而非项目死亡

## 风险与不足
- **版本号已退化为里程碑**：2024-11 后无新 tag，但代码层面每月仍持续 commit——**信号是混乱的**，可能让外部贡献者困惑
- **重复目录残留**：`XSS Injection/` 与 `XSS injection/` 并存（大小写不一致），`Upload insecure files/JPG Resize` 与 `Upload/JPG Resize` 重复——9 年沉淀的结构债务
- **AI 范式风险**：未来 2-3 年若 LLM 直接吐出高质量 payload+绕过，PATT 的「现成字典」价值会显著下降
- **个人依赖**：Swissky 一人占 47.5% 贡献，333 人是「广而不深」社区——若主理人失能，项目将快速陷入维护停滞
- **速度落后**：HackTricks 2020 年后增速反超，社区活跃度优势已被追平

## 行动建议

### 如果你要用它
**渗透测试工作中**：把 PATT 当「payload 检索起点」而非「学习教材」。具体场景——做 SSTI 测试时直接来搜引擎、复制 `Intruder/*.fuzz` 到 Burp、用占位符协议确保不污染客户环境。

**Bug Bounty 报告写作**：PATT 的占位符协议 + Wayback 引用格式是「可被企业接受」的标准——你的报告如果照 PATT 格式写，安全团队更易消化。

### 如果你要学它
重点关注**5 个文件**就够：
1. `README.md` — 看「安全卫生」与「模板」的顶层定义
2. `CONTRIBUTING.md` — 5 条占位符规则、Wayback 引用规范
3. `_template_vuln/README.md` — 五段式模板的宪法
4. `.github/hopla_config.json` — 双层结构化的机器消费层
5. `Methodology and Resources/Active Directory Attack.md` — 看 246 次修改后沉淀下来的「成熟章节」长什么样

### 如果你要 fork 它
**值得改进的方向**：
1. **目录去重**：合并 `XSS Injection` / `XSS injection` 与两个 `JPG Resize` 副本
2. **AI 时代护城河**：增加「模型生成 payload 的 prompt 模板」章节，把 PATT 从「字典」升级为「字典+配方」
3. **本地化版本**：参考 HackTricks 的 `hacktricks-translate` 模式，启动 PATT 多语言版本
4. **结构化抽取自动化**：写脚本从 Markdown 自动生成 `hopla_config.json`，消除双写成本
5. **贡献者梯度**：从「全开放 PR」改为「核心贡献者 Triage 制度」，让 333 人深度参与而非 47.5%+ 广度参与

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [已收录](https://deepwiki.com/swisskyrepo/payloadsallthethings) — 覆盖 40+ 漏洞主题与方法论分类 |
| Zread.ai | [已收录](https://zread.ai/swisskyrepo/payloadsallthethings) — 提供架构视角与「AllTheThings 家族」联动解读 |
| 关联论文 | 无（仓库本身是工程化知识库，非论文项目） |
| 在线 Demo | [官方导航站](https://swisskyrepo.github.io/PayloadsAllTheThings/)（MkDocs Material 渲染，配套 Burp Intruder `.fuzz` 文件下载） |

---

## 附：与同目录旧版报告的差异说明

旧版 `swisskyrepo_payloadsallthethings.md`（未日期戳）有以下差异：
- 旧版强调「双消费格式」（人读 + Burp 直读）；新版拆出更细的「Wiki 即 Burp 资源」双向桥接（README + `.fuzz` + `hopla_config.json`）
- 旧版竞品矩阵 4 列（含 foospidy/payloads），新版替换为 The Hacker Recipes（更相关）
- 旧版以"文档型 GitHub 项目"为定位；新版以"Web 应用安全 payload 知识库的基础设施层"为定位
- 旧版仅 5 个可复用模式；新版归类为 5 个，命名为更易传播（安全占位符协议、目录即路由、双层结构化、PR-only 守卫、分支=站点源）

两份报告**都成立**——选择哪份发布取决于发布渠道风格偏好。
