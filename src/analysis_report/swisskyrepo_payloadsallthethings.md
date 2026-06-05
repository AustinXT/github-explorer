# 78K stars、9 年沉淀：红队 Swissky 怎么把渗透字典变成 GitHub「事实标准」

> GitHub: https://github.com/swisskyrepo/payloadsallthethings

## 一句话总结
一份按漏洞类型组织的「真实可粘贴」Web 渗透 payload 字典与 WAF 绕过合集，作者 Swissky 用 Git 当版本化个人记事本、用 Hacktoberfest 当季节流量，硬生生把一个资源库做成了渗透测试领域的**「社区基础设施」**。

## 值得关注的理由
- **学一个仓库，胜读十本 Cheat Sheet**：70+ 漏洞章节、246 次改动的 AD 攻击篇、107 次改动的 Windows 提权篇、333 位贡献者、17k+ Fork，覆盖 XSS/SQLi/SSRF/SSTI/RCE/AD 等所有 Web+内网高频攻击面。
- **Git 当 CMS、目录当模板的内容工程范本**：4 件套子目录（README+Intruder+Images+Files）、4 段式模板（Tools/Methodology/Labs/References）、Wayback 兜底引用、占位符卫生化、markdownlint CI 门禁——这套「内容仓库治理」可被任何 long-tail 参考型项目复用。
- **品牌化、系列化、可商业化**：Swissky 围绕 PATT 沉淀出姐妹仓 InternalAllTheThings / HardwareAllTheThings + GitHub Sponsors（SerpApi、ProjectDiscovery、VAADATA），是「个人知识库→企业赞助基础设施」的样板路径。

## 项目展示

### README 媒体
1. ![banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png) — 类型: hero
2. ![sponsors-list](https://contrib.rocks/image?repo=swisskyrepo/PayloadsAllTheThings&max=36) — 类型: screenshot（社区贡献者墙）
3. ![sponsor-serpapi](https://avatars.githubusercontent.com/u/34724717?s=40&v=4) — 类型: sponsor logo
4. ![sponsor-projectdiscovery](https://avatars.githubusercontent.com/u/50994705?s=40&v=4) — 类型: sponsor logo
5. ![sponsor-vaadata](https://avatars.githubusercontent.com/u/48131541?s=40&v=4) — 类型: sponsor logo

### 筛选说明
- 总共发现 7 个媒体元素（README 候选 7 个，官方无增量），筛选后保留 5 个：1 个 hero banner + 1 个社区贡献者墙 + 3 个主要赞助商 logo。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/payloadsallthethings |
| Star / Fork | 78,211 / 17,047 |
| Watcher | 1,962 |
| 代码行数 | 2,096 行有效代码 + 54,442 行 payload/文档（Python 61% / ASP.NET 9% / XSLT 7% / SVG 4.5% / XML 3.9%） |
| 项目年龄 | 115.7 个月（≈ 9.6 年），首提交 2016-10-18，最近推送 2026-04-22 |
| 开发阶段 | 低维护（近 30 天 0 commit、近 90 天 12 commit、近 1 年 105 commit） |
| 贡献模式 | 单人主持+社区共建（Top 贡献者 Swissky 占 79.3%，但社区 333 位贡献者） |
| 热度定位 | 大众热门（GitHub 前 0.1% 顶级资源，渗透测试领域事实标准） |
| 质量评级 | 文档[优秀] 测试[无] CI/CD[完善]（markdownlint + mkdocs gh-deploy） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Swissky（@pentest_swissky）账号注册于 2015-04-28，Bio 自述「Red Team Operator & Bug Hunter」，粉丝 10,500、公开仓库 13 个。PATT 在其仓库中 Star 数 78k+ 一骑绝尘（第二名 InternalAllTheThings 仅 2.2k），是绝对旗舰项目。围绕 PATT 他还衍生了 InternalAllTheThings（内网/AD/Cloud）、HardwareAllTheThings（IoT/硬件）两个 sister repo，并配套贡献了 SSRFmap、GraphQLmap 等实战工具——是典型的「单点深耕→系列化」作者路径。

### 问题判断
一线红队/Bug Hunter 在每次 Web 任务里都要重复「翻博客→猜 IP→改 payload」这套动作。Swissky 从 2016 年起把个人复盘记在 GitHub 上，当同一段 payload 在第 11 次被复用时，他意识到这已是一类可被工具化的「知识工作」。他看到的关键空白是：**没有现成项目把「payload + 绕过 + 配套 Intruder 字典 + 截图 + 配套 PHP 接收脚本」作为单一「漏洞章节单元」标准化沉淀**。OWASP 只讲防御、HackTricks 偏方法论、SecLists 是纯字典（无解释）、个人博客离散且链接腐烂——四条线都没有覆盖到他真正需要的「可立即复制粘贴」这一格。

### 解法哲学
- **字典型 cheat sheet 而非教科书**：每个漏洞章节固定「概念 2 段 + payload 列表 + 工具列表 + 绕过变体 + 截图 + Intruder 字典」，不写大段防御理论。
- **目录即模板、字段即契约**：每个漏洞章节复用 4 件套子目录；每个 README 强制 4 段式（Tools/Methodology/Labs/References），`_template_vuln/` 给贡献者「填空式」入口。
- **Pull Request 即版本管理**：用 Git 流程代替 CMS/DB/后台，mkdocs gh-deploy 编译成静态站点。
- **占位符卫生化**：RCE 用 `id`/`whoami`、回调域用 `[ATTACKER.DOMAIN.TLD]`、IP 用 `10.10.10.10`、密码用 `P@ssw0rd`——既不触发蜜罐，也不泄露客户凭据。
- **Wayback Machine 兜底引用**：所有 References 强制走 `web.archive.org/...`，10 年后这个仓库仍可读。

### 战略意图
PATT 是 Swissky「进攻性安全百科」中的「Web 入口层」——姊妹仓覆盖内网/AD/Cloud 与硬件/IoT，三者共同构成 Swissky 品牌。商业化路径清晰：GitHub Sponsors + SerpApi/ProjectDiscovery/VAADATA 显式赞助商，把「个人知识库」沉淀为「可持续维护的公共基础设施」。开源策略是 genuinely open（MIT License），非 open-core。

## 核心价值提炼

### 创新之处

| # | 创新点 | 新颖度 | 实用性 | 可迁移性 |
|---|--------|--------|--------|----------|
| 1 | **「目录即章节模板」强约束内容工程**：4 件套子目录 + 4 段固定模板，配套 `_template_vuln/` 复制即用 | 3/5 | 5/5 | 5/5 |
| 2 | **「占位符 + 卫生化」payload 贡献约定**：`[ATTACKER.DOMAIN.TLD]`/`P@ssw0rd`/固定 IP 让 PoC 既可读又安全 | 4/5 | 5/5 | 5/5 |
| 3 | **「References 必走 Wayback 兜底」长期可读性策略**：强制 `web.archive.org/...` 包裹，10 年后仍可用 | 3/5 | 5/5 | 5/5 |
| 4 | **「Burp Intruder 字典作为一等公民」内嵌到文档**：每个漏洞章节自带 `Intruder/` 目录，命名带原作者 handle（如 `BRUTELOGIC-XSS-JS.txt`、`0xcela_event_handlers.txt`） | 4/5 | 5/5 | 4/5 |
| 5 | **「Pull Request 即 Issue Track + Hacktoberfest 季节流量」双轨治理**：不开 issue 跟踪，所有工作收敛到 PR；每年 10 月 PR 集中涌入（2022-10 出现 107 commit 峰值） | 3/5 | 5/5 | 4/5 |
| 6 | **「sister repo + redirect stub」分库治理**：内网/AD/Cloud 内容迁到 InternalAllTheThings，PATT 保留「标题+warning+链接」薄壳 | 4/5 | 4/5 | 4/5 |
| 7 | **「lint 即内容门禁」Markdown CI 标准化**：`tj-actions/changed-files` 增量检查 + `markdownlint-cli2-action`，把**格式问题**前移到 CI，配合 `MD013: false`/`MD033: false` 规则 | 3/5 | 5/5 | 4/5 |

### 可复用的模式与技巧

1. **「目录即模板」模式** — 用固定子目录让多作者产出可预测。适用场景：知识库/cookbook/playbook/培训手册。
2. **「字段级模板」模式** — 在 README 模板里显式列字段，给贡献者「填空式」写作入口。适用场景：长尾覆盖的参考文档。
3. **「占位符卫生」模式** — 用统一占位符代替真实值（IP/域名/凭据）。适用场景：公开 PoC/sample/exploit 仓库。
4. **「Wayback 兜底引用」模式** — 所有外部链接走 archive.org。适用场景：长期维护的 wiki/research note。
5. **「lint 即内容门禁」模式** — PR 阶段用 markdownlint 把「格式问题」前移到 CI。适用场景：大型 markdown 仓库。
6. **「sister repo + redirect stub」模式** — 主仓保留薄壳，内容沉到子仓。适用场景：单作者主导的、多主题但分主题深耕的知识库。
7. **「致谢嵌入文件名」模式** — `BRUTELOGIC-XSS-JS.txt` 让署名随文件永久可追溯。适用场景：字典/语料库/数据集。
8. **「工具消费嵌入式资产」模式** — 把 Burp/ffuf/sqlmap 等工具可直接 Load 的字典放在仓库里。适用场景：安全工具链配套内容。

### 关键设计决策

**决策 1：用 Git 承载 payload 字典，不引入 DB/CMS/wiki 引擎**
- 问题：payload 集合需要版本可追溯、可 diff、可回滚
- 方案：每个 payload 章节都是普通 markdown；变更通过 PR 触发 markdownlint CI；`mkdocs gh-deploy` 发布为静态站点
- Trade-off：失去「全文搜索/标签/分类」等结构化查询能力 → 换取「不承担 DB 运维成本 + 内容变更天然带 blame/历史」
- 可迁移性：极高

**决策 2：4 件套目录模板（README+Intruder+Images+Files）**
- 问题：多作者协作时章节结构各自为政，读者无法形成稳定心智模型
- 方案：在 README/CONTRIBUTING/_template_vuln 三处显式声明模板
- Trade-off：`Intruder/` vs `Intruders/` 命名未统一 → 换取「读者上手成本趋近于零 + 新贡献者可无脑复制骨架」
- 可迁移性：极高

**决策 3：4 大标准段落（Tools/Methodology/Labs/References）**
- 问题：渗透类内容易写成「自由散文」，重要信息散落各处
- 方案：模板直接列字段，且 References 强制 `Title - Author (@handle) - Month Day, Year` 格式 + Wayback 包裹
- Trade-off：非标章节需写 redirect stub → 换取「任意章节被独立翻译/检索/引用」的便利
- 可迁移性：高

**决策 4：占位符卫生约定（`[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `P@ssw0rd`）**
- 问题：公开仓库放真实值会被滥用 + 触发蓝队蜜罐 + 泄露客户凭据
- 方案：CONTRIBUTING.md 硬约束占位符集合
- Trade-off：用户须自己替换占位符 → 换取「DNS/IP 不会真实指向攻击者」「不会误触发蜜罐」「不构成数据泄露」
- 可迁移性：极高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | OWASP Cheat Sheet | HackTricks | SecLists | ippsec/0xdf |
|------|---------------------|-------------------|------------|----------|-------------|
| Stars | 78K | ~30K | ~8K | ~60K | N/A |
| 视角 | 进攻（payload） | 防御（规约） | 通用方法论 | 纯字典 | 实战 walkthrough |
| 配套资产 | Burp Intruder 字典 + 截图 + Files | 无 | 工具链接 | 字典 | 视频 |
| 覆盖深度 | 单点 payload 极细 | 行业标准广 | 内网/AD/Cloud 更深 | 字典数量最多 | 真实环境演示 |
| 章节结构 | 强模板（4 件套+4 段式） | 自由 | 自由 | 无章节 | 单点视频 |
| 长期可读性 | Wayback 兜底 | 官方维护 | 官方维护 | 官方维护 | 频道存活即用 |

### 差异化护城河
「字典型 cheat sheet + 配套 Burp 字典 + 占位符卫生 + Wayback 引用 + 10 年长尾维护」五位一体的组合，是其他项目都难以同时满足的。**LLM 时代的新护城河反而是「半成品资产」——LLM 无法直接生成可被 Burp Suite 0 摩擦消费的 .fuzz 字典**，这让 Intruder/ 目录的工程价值在 AI 时代不降反升。

### 竞争风险
- LLM/AI 助手正在让「实时检索+改写」成本降低，对「手工整理的字典」依赖下降——但 PATT 的「配套 Intruder 字典」是 LLM 无法直接生成的「半成品」。
- HackTricks 持续高频更新可能蚕食「方法论」侧优势。
- SecLists 在字典数量上仍领先，且与 ffuzz/wfuzz 生态绑定更深。

### 生态定位
PATT 处于「内容型参考库」赛道，是「Web 渗透」主题下**事实上的 community cheatsheet standard**。OWASP（防御规约）/HackTricks（方法论）/SecLists（纯字典）/PATT（payload+字典+绕过）四者形成清晰的「内容分工」生态。

## 套利机会分析
- **信息差**：78K Star 已严重被市场充分定价，「被低估的潜力股」窗口早已关闭；但作为基础设施型资源库仍具备长期不可替代性。
- **技术借鉴**：上面 8 个「可复用模式与技巧」是核心套利点——任何一个「长期维护的 markdown 知识库」项目都可以照搬其「目录模板+字段模板+占位符卫生+Wayback 兜底+markdownlint CI」五件套，把内容治理水平从「自由生长」提到「工程化」。
- **生态位**：填补了「可立即复制粘贴的渗透 payload + 配套 Burp 字典」这个细分空白，与 OWASP（防御）/HackTricks（方法论）/SecLists（纯字典）形成四分天下。
- **趋势判断**：10 年长尾维护 + 333 贡献者 + 企业赞助 + 系列化 sister repo，处于「成熟期+稳定护城河」阶段；增量主要在「新攻击类别」（Prompt Injection / Dependency Confusion / Cloud SSRF / Container Pentest 等）。

## 风险与不足
- **近 30 天 0 commit**：已进入「低维护」阶段，社区 PR 合并节奏放缓，对「最新 CVE 出现即收录」的时效性诉求需要依赖读者自补。
- **无 Issue 跟踪**：所有工作收敛到 PR 流程，新人遇到内容问题反馈路径不清晰。
- **目录命名历史债**：`XSS Injection/` vs `XSS injection/`、`Upload insecure files/JPG Resize` vs `Upload/JPG Resize`、`Intruder/` vs `Intruders/`——大小写/复数未规范化，影响站内搜索与新贡献者 PR 体验。
- **质量保证无自动化**：payload 正确性依赖社区 review，没有自动化 fuzz/校验；与「AI 改写 payload 引入错误」的风险面没有 CI 防护。
- **法律/伦理双刃剑**：仓库本身可被滥用为「一键攻击工具书」，DISCLAIMER.md 的「教学/研究/有授权」三红线对恶意使用者无强制力。

## 行动建议

### 如果你要用它
- **首选场景**：Web 渗透测试的「payload 速查 + 绕过变体 + Burp 字典消费」三位一体需求；Bug Bounty 提交前的「最后一遍绕过验证」；CTF/HTB 机器中遇到某类漏洞时直接定位章节。
- **建议用法**：先看 README 顶层目录定位漏洞类型 → 进章节看 Tools/Methodology 段 → 加载 Intruder/ 字典到 Burp → 用 Labs 段在 RootMe/PortSwigger 上练手 → 实战前必看 DISCLAIMER.md。

### 如果你要学它
- **重点关注**：
  - `_template_vuln/README.md` — 4 段式模板的字段定义
  - `CONTRIBUTING.md` — 占位符卫生约定 + 4 件套目录说明
  - `.github/workflows/check-markdown.yml` — 增量 markdownlint 门禁
  - `mkdocs.yml` + `.github/overrides/main.html` — 静态站点编译与主题定制
  - `XSS Injection/README.md` 完整 4 件套（README + 15 个 Intruders/.txt + Files/）作为「满分章节范例」

### 如果你要 fork 它
- **可改进方向**：
  - 解决 `Intruder/` vs `Intruders/` 命名异构，做一次 PR 重命名统一化
  - 补「AI 改写 payload 的 CI 防呆」：用 markdownlint 之外加一个简单的 `regex: alert(1)\b` 替换提醒
  - 把 `active_directory_attack.md` 等顶级热点章节用 mkdocs 的 `nav:` 提到第一屏
  - 加一个 `FINDABILITY.md`：把「如何高效搜索本仓库」写成新人 onboarding 文档
  - 引入「CVE 编号 + 章节名」索引表，让「今年新出的 CVE 被哪个章节覆盖」一键可查

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | 无（项目为工程化资源集合，未发表论文） |
| 在线 Demo | https://swisskyrepo.github.io/PayloadsAllTheThings/（README 渲染版静态站点，提供可搜索展示层） |
| Sister repos | https://github.com/swisskyrepo/InternalAllTheThings（内网/AD/Cloud）<br>https://github.com/swisskyrepo/HardwareAllTheThings（IoT/硬件）<br>https://github.com/swisskyrepo/SSRFmap（作者配套工具） |
| 官方 CI | https://github.com/swisskyrepo/PayloadsAllTheThings/actions |
| 作者推特 | @pentest_swissky（基于 bio 「Red Team Operator & Bug Hunter」） |
