# 9.6 年 78K stars：一个人撑起的 Web 渗透 Payload 字典

> GitHub: https://github.com/swisskyrepo/payloadsallthethings

## 一句话总结

一个红队操作员用 9 年时间，把「每个 Web 漏洞章节 = README + Burp 字典 + 截图 + 附件」的同构范式做成 78K stars 的事实标准——PayloadsAllTheThings 是「GitHub 形态 + 广度 + 社区贡献」三者结合下，渗透测试人员人手一份的 Web 漏洞字典。

## 值得关注的理由

- **真·事实标准**：78,168 stars / 17,036 forks / 1,961 watchers / 333 贡献者，是渗透测试 / Payload 字典垂直领域全球第一，超过 SecLists（~60k）、OWASP CheatSheet Series（~30k）等同类项目。
- **Payload 卫生标准可被任何敏感知识库复用**：CONTRIBUTING.md 强制 `id` / `whoami` / `[ATTACKER.DOMAIN.TLD]` / `10.10.10.10` / `P@ssw0rd` 等占位符，让敏感内容既能公开托管又不被滥用——这种「把伦理/法律边界做成工程约束」的思路，远超普通 README 写一句「仅供教育用途」，也是项目能存活 9.6 年而不被 GitHub 下架的根本原因。
- **家族化个人品牌策略值得独立开发者学习**：同一作者的 `PayloadsAllTheThings`（Web）/ `InternalAllTheThings`（AD 内网）/ `HardwareAllTheThings`（IoT 物理）三件套互相 backlink，把「企业攻击面三轴」拆成可独立成长的子品牌。

## 项目展示

![PayloadsAllTheThings 官方 banner](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/.github/banner.png)

> 项目是 Markdown 内容仓库，没有架构图、Demo GIF、演示视频。README 头部仅一张 banner.png + 三个赞助商 logo（SerpApi / ProjectDiscovery / VAADATA），所有架构/技术内容都通过 Markdown 目录结构传达。**站点版**：[swisskyrepo.github.io/PayloadsAllTheThings](https://swisskyrepo.github.io/PayloadsAllTheThings/)

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/swisskyrepo/payloadsallthethings |
| Star / Fork | 78,168 / 17,036 |
| Watcher | 1,961 |
| 代码规模 | ~2,096 行可执行/标记语言 + 54,442 行 Markdown（文档:代码 ≈ 26:1） |
| 语言分布 | Python 76.2%（payload PoC）、ASP.NET 8.7%、XSLT 5.9%、Classic ASP 3.2%、PHP 3.1%、Ruby 1.2%、Jupyter 0.6% |
| 项目年龄 | 9.6 年（2016-10-18 首次提交） |
| 总 commit | 2,185 |
| 贡献者 | 333 人（主作者 Swissky 1,290 commits 占比 47.5%，第 2 名 p0dalirius 81，第 3 名 noraj 50） |
| Open Issue / PR | 0 / 17（issues 主动保持空白） |
| License | MIT |
| Release | v4.2（共 7 个 tag，5 个 release，语义化版本） |
| 开发阶段 | 低维护（近 30 天 0 commit，近 90 天 13 个，近一年 105 个，仍在持续小更新） |
| 开发模式 | 职业项目（周末 27.1% / 深夜 18.2%，Hacktoberfest 季节性爆发） |
| 热度定位 | 大众热门（heat_level = 大众热门） |
| 质量评级 | 内容[优秀] 文档[优秀] 模板一致性[良好] CI/CD[优秀] 贡献引导[优秀] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Swissky（@swisskyrepo）自述 "Red Team Operator & Bug Hunter"，11.1 年账号、10,492 followers、following 仅 13，是典型的「高影响力低维护」账号画像。公开仓库矩阵显示他已围绕「AllTheThings」形成家族品牌：

- `PayloadsAllTheThings`（78K，2026-04 仍 push）— 旗舰，Web 渗透
- `InternalAllTheThings`（2.2K，2026-04 push）— 蓝队 / AD 攻击
- `HardwareAllTheThings`（886，2025-11 push）— 物联网
- `SSRFmap`（3.6K，2025-09 push）— SSRF 工具
- `Vulny-Code-Static-Analysis`（422，2025-02 push）— PHP 静态分析
- `GraphQLmap`（1.7K，2024-03 停滞）— 旧工具

核心合作者 p0dalirius（81 commits，知名 Linux/AD 贡献者）、noraj（50 commits，OSCP 教材作者）、lanjelot（17 commits，patator 作者）—— 不少是圈内有头有脸的安全研究者，间接为项目质量背书。

### 问题判断

Swissky 在 9 年红队实战中发现：**每个渗透测试工程师都在造重复的轮子**——把同一组 payload 拷来拷去，但又怕在公开仓库里直接放可执行代码会触犯法律 / 被滥用 / 触发 GitHub 风控下架。他的洞察是**把「卫生标准」（占位符）工程化**，让敏感内容既可公开托管又不被滥用——这是项目能存在 9.6 年而不被下架的根本原因，也是 2016-2018 恰逢 Burp Suite + Intruder 在企业渗透中普及期的精准时机选择。

### 解法哲学

- **GitHub 维基 > 个人博客**：赌「单一作者写不完所有漏洞」，PR 通道是规模化路径（333 贡献者，9.6 年沉淀）。
- **结构一致性 > 内容深度**：70+ 章节统一为 `Tools` / `Methodology` / `Labs` / `References` 四段式（`## Summary` 软四件套渗透率 100%），让用户形成稳定心智模型。
- **原子化交付 > 一站式工具**：不打包自家扫描器，而是给 Burp / ffuf / HopLa 已知工具直接喂文件——复用用户既有工具链。
- **明确不做什么**：不做漏洞扫描器（那是 Nuclei 的事）、不做付费课程、不做实时通讯（连 Discord 都没有）。
- **PR-only 治理**：Open Issues 长期保持 0，所有协作走 PR 通道，让 GitHub Contributor 图谱直接充当贡献者荣誉墙。

### 战略意图

商业化路径很克制——仅依赖 ① GitHub Sponsors（SerpApi / ProjectDiscovery / VAADATA 三家精准流量反向赞助）② 个人品牌溢出（咨询/演讲）。没有 SaaS 化、没有付费墙、没有 open-core，「AllTheThings」家族化品牌本身就是商业护城河。

## 核心价值提炼

### 创新之处

| # | 创新点 | 新颖度 | 实用性 | 可迁移性 |
|---|--------|-------|-------|---------|
| 1 | **Payload 卫生标准 + 占位符工程化**：把医学研究「去标识化」思路移植到安全研究，让敏感内容既能公开托管又不被滥用 | 4/5 | 5/5 | 5/5 |
| 2 | **机器可读转接视图（`hopla_config.json`，87KB / 285 项分类）**：在面向人阅读的 README 之外维护结构化 JSON 把 XSS/SQLi/SSRF/SSTI 喂给 Burp HopLa 扩展，实现「文档 ↔ 工具」无缝 | 4/5 | 4/5 | 4/5 |
| 3 | **章节即子模块的目录范式**：`_template_vuln/` + 64 个同构目录实现「一个仓库 = 多个可独立阅读的子项目」，把 monorepo 的「边界即目录」理念移植到文档 | 3/5 | 5/5 | 5/5 |
| 4 | **家族化个人品牌策略**：用「AllTheThings 家族」分别覆盖企业攻击面三轴（外部 Web / 内网 AD / 物理 IoT），互相 backlink，共建品牌 | 3/5 | 4/5 | 3/5 |
| 5 | **PR-only 治理 + Hacktoberfest 季节性引流**：Open Issues 长期保持 0，所有协作走 PR 通道；Hacktoberfest 10 月提交脉冲做季节性刷新（2021-10 单月 125 commits、2022-10 107 commits、2020-10 84 commits） | 2/5 | 4/5 | 4/5 |

### 可复用的模式与技巧

1. **`_template_xxx/` 模板子目录** — onboarding 文档做成可 fork 的目录，贡献者直接 copy-paste 开始，门槛接近零。
2. **同构骨架 + markdownlint 兜底** — 4-5 段固定骨架，CI 强制格式统一（`.markdownlint.json` + `.github/workflows/check-markdown.yml`）。
3. **双轨 CI（按需 lint + 全量 build）** — PR 阶段用 `tj-actions/changed-files` 过滤后 lint 变更文件，master push 才做全量 mkdocs 构建，PR 反馈 < 30 秒。
4. **双视图（GitHub 原生 + mkdocs 站点）** — 同一份 Markdown 既在 GitHub 原生渲染，又由 mkdocs-material + 自定义 `custom.css` + `overrides/main.html`（AddToAny 分享 + Umami 统计）渲染成独立站。
5. **占位符卫生标准** — 把法律/伦理边界做成工程约束，让敏感内容既能公开托管又不被滥用。

### 关键设计决策

| 决策 | 问题 | 方案 | Trade-off | 可迁移性 |
|------|------|------|----------|---------|
| 章节四件套同构（README + Intruder + Images + Files） | 333 位贡献者对「一个漏洞章节应含什么」理解不一 | 硬性指定 + `_template_vuln/` 可 fork + `check-markdown.yml` 兜底 | 牺牲按需扩展自由度（新型漏洞如 Mass Assignment / Prototype Pollution 只有 README），换跨章节等价性 | 高 |
| Payload 卫生标准（占位符强制） | 公开仓库托管攻击 payload 触法/被滥用/触发 GitHub 风控 | CONTRIBUTING.md 强制 `id` / `whoami` / `Administrator` / `[ATTACKER.DOMAIN.TLD]` 等不可执行占位符 | 牺牲「直接复制粘贴」便利，换项目可公开托管 9.6 年 | 高 |
| 跨工具转接 JSON（`hopla_config.json`） | 知识库与工具链有「复制粘贴」损耗 | 把 XSS/SQLi/SSRF/SSTI 核心 payload 维护成结构化 JSON 喂给 Burp HopLa 扩展 | 多一份数据需双轨同步，换「打开 Burp 就能挑 payload」 | 高 |
| 目录命名历史遗留 | 64 章节有 4 处目录命名不一致（`Intruder` vs `Intruders`），`Upload Insecure Files/` 完全偏离四件套 | 有意识松弛的渐进式治理——`mkdocs.yml` 部署 + `markdownlint` 兜底**仅作用于文本层**，目录结构允许历史遗留 | 内部链接有大小写敏感破坏风险（GitHub 仍兼容） | 中（只适合「内容 > 工程严谨」型项目） |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PayloadsAllTheThings | SecLists | HackTricks | OWASP CheatSheet | PayloadBox |
|------|---------------------|----------|------------|------------------|------------|
| Stars | 78K | ~60K | ~10K+ | ~30K | ~10K+ |
| 形态 | 场景化字典 + Burp 脚本 | 裸字典 / wordlist | 叙事化 Wiki | 防御侧最佳实践 | 单文件合集 |
| 是否带说明 | ✅ 强 | ❌ 无 | ✅ 强 | ✅ 强 | ❌ 弱 |
| 工具链集成 | Burp Intruder + HopLa JSON | ffuf / wfuzz | 弱 | 弱 | 弱 |
| 多语言支持 | 英文单一语种（拒绝翻译 PR） | 英文 | 西/英双语 | 多语言 | 英文 |
| 维护活跃度 | 低维护（年 105 commit） | 活跃 | 活跃 | 活跃 | 停滞 |
| 适合「检索 payload」 | ✅ 极强 | ⚠️ 需自配 | ⚠️ 需翻章节 | ❌ 防御侧 | ✅ 强 |
| 适合「学习路径」 | ⚠️ 中 | ❌ 弱 | ✅ 强 | ✅ 强 | ❌ 弱 |

### 差异化护城河

1. **生态护城河（数据飞轮）**：70+ 章节 + 333 贡献者 + 9.6 年沉淀，新来者很难用「一次性爆款」追赶。
2. **品牌/信任护城河**：78K stars + 9.6 年持续更新 + Swissky 个人品牌（10K followers）+ 三大安全厂商（SerpApi / ProjectDiscovery / VAADATA）赞助背书。
3. **可移植性护城河**：纯 Markdown + 开放 repo + 双视图（GitHub 原生 + mkdocs 站点），任何「能读 GitHub 的人」都能消费；中文社区有多个 Gitee 镜像、第三方 Web 客户端。
4. **工具链闭环护城河**：`hopla_config.json` 让文档 ↔ Burp 工具无缝衔接，AI 工具按主题生成 payload 难以复制这种「内容-工具闭环」。

### 竞争风险

- **HackTricks 覆盖面更广**（Windows / Linux / 网络全攻击面），若在「场景化」上持续投入，会形成压力。
- **AI 工具威胁**（如 ChatGPT / Cursor 按主题生成 payload）——但**卫生标准 + 工具链集成形成的内容-工具闭环**仍是 AI 难以复制的护城河。
- **SecLists 跨界**到「带 metadata 的字典」则形成二合一挑战。

### 生态定位

在渗透测试技术栈中扮演「**执行参考层**」——介于「方法论（OWASP WSTG）」和「工具（Nuclei / Burp）」之间，把「该用什么 payload 测这个漏洞」做成行业默认：

- 为 **SecLists** 提供「带说明的字典」
- 为 **Burp** 提供「带工作流的字典」
- 为 **WAF / SAST 厂商** 提供「真值参考」

## 套利机会分析

- **信息差**：78K stars 级别项目被搜索/转载/镜像无数次，「新项目速递」角度失效；但「**纵向深度解读**」+「**中文区教程化整理**」+「**对比/趋势类横向定位**」+「**Swissky 个人品牌故事**」仍有公众号选题张力。
- **技术借鉴**：Payload 卫生标准、章节四件套同构范式、双轨 CI、双视图（GitHub + mkdocs）、家族化品牌策略——五个模式都直接可迁移到企业内部 cookbook / 案例库 / 合同模板库 / 安全培训材料。
- **生态位**：填补「GitHub 形态 + 广度 + 社区贡献」三者结合下的 Web 渗透 Payload 字典空白，是中文安全社区的「必备字典」项目。
- **趋势判断**：78K stars + 17K forks + 333 贡献者，仍在稳定流入（年 105 commit），无衰退迹象；2024-11 是最近一次大动作窗口（75 commits）后进入低维护期，但「长期维护、季节性爆发」的开源字典项目模式已被验证可行。

## 风险与不足

- **维护者精力瓶颈**：Swissky 主力是渗透测试职业工作，PayloadsAllTheThings 是「晚上/周末项目」，17 个 open PR 的合并压力大，PR review 速度是当前最大瓶颈。
- **目录结构历史遗留**：`XSS Injection` vs `XSS injection`、`Upload` vs `Upload Insecure Files` 等命名不一致，4 处 `Intruder` vs `Intruders` 混用，`Upload Insecure Files/` 完全偏离四件套——内部链接有大小写敏感破坏风险。
- **国际化缺失**：曾有大量 PR 请求中文/西班牙文/法文翻译，但被统一拒绝（"保持英文单一语种以降低维护成本"），改为引导到外部翻译项目——对中文区不友好。
- **Open Issues = 0** 的治理模式对新手不友好：issue 列表被刻意保持空白以降低噪音，新用户遇到问题找不到反馈入口。
- **未工程化**：无单元测试、无 CI lint 之外的构建流程、无依赖管理、无锁文件——这些对内容仓库是合理选择，但若未来要做「工具化」扩展会受制于基础设施。
- **伦理/法律争议**：长期存在 "是否应包含可直接利用的 Active Exploit" 争论，项目选择保留并加免责声明，体现「知识自由」立场，但 GitHub 风控政策变化始终是悬顶之剑。

## 行动建议

- **如果你要用它**：作为渗透测试 / Bug Bounty 任务的**首选 payload 参考**，按「漏洞章节 → Tools → Methodology → Labs → References」四段式快速定位；推荐搭配 Burp Suite + HopLa 扩展加载 `hopla_config.json`，可直接在 Burp 中调用。
- **如果你要学它**：重点关注 5 个文件 / 目录：
  1. `CONTRIBUTING.md` — 占位符卫生标准的范本
  2. `_template_vuln/README.md` — 模板子目录范式
  3. `.github/workflows/check-markdown.yml` + `mkdocs-build.yml` — 双轨 CI 范本
  4. `.github/hopla_config.json` — 文档 ↔ 工具转接范本
  5. `Methodology and Resources/Active Directory Attack.md`（246 次修改，绝对热点）— 内容维护活跃度的最佳样本
- **如果你要 fork 它**：可改进的方向：
  1. **目录命名统一化**（重命名 `XSS injection` → `XSS Injection`，合并 `Upload` 与 `Upload Insecure Files`）—— 工程上不复杂但维护成本高
  2. **添加 CI 链接检查**（`lycheeverse/lychee-action` 兜底 markdownlint 之外的死链）—— 78K stars 项目死链率不容忽视
  3. **结构化 Intruder 文件的 schema 校验**（用 `hopla_config.json` 的同款 JSON Schema 兜底 fuzz 字典）—— 避免贡献者格式漂移
  4. **多语言版本**（fork 走中文/西语/法语分支，主仓保持英文单一语种）—— 已被项目明确拒绝，所以这是 fork 的天然切入点
  5. **AI 辅助检索**（加 embeddings + 站内搜索）—— 章节数膨胀到 70+ 后，原生 GitHub 搜索已力不从心

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录（页面提示 "Loading... Index your code with Devin"） |
| Zread.ai | 无法访问（HTTP 403） |
| 关联论文 | 无（字典/工具类项目一般无学术论文） |
| 在线 Demo | 无（内容仓库，无可运行 Demo） |
| 站点版 | https://swisskyrepo.github.io/PayloadsAllTheThings/ |
| 学习平台收录 | TryHackMe / HackTheBox / PortSwigger Web Security Academy / OSCP 备考圈 |
| 第三方镜像 | 多个 GitHub 镜像 + Gitee 镜像（中文社区） |
| 第三方 Web 客户端 | PayloadsAllTheThingsWeb（社区维护的更友好浏览 UI） |
| Issue 替代渠道 | GitHub Discussions（实际承担 Q&A 角色） |
