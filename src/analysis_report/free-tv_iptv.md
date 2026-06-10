# 把「看电视」做成开源：free-tv/iptv 的 162 行 Python 策展术

> GitHub: https://github.com/free-tv/iptv

## 一句话总结

一个用 Git-as-CMS 模式运营的全球免费电视 M3U 播放列表公益仓库：90 份 Markdown 国家频道表 + 1 段 162 行 Python 编译器 + GitHub Actions 自动出 playlist，0 服务器成本喂饱 16K stars 的剪线族。

## 值得关注的理由

- **「数据即代码」的极端样本**：仓库主体是 90 份人类可编辑的 `.md` 频道表，真实工程代码只有 162 行 Python + 17 行 Shell——证明「内容策展」才是项目，工程只是脚手架。
- **「机器代理 commit」治理范式**：PlaylistBot 用独立身份 + 静默 + 硬 push 模式吃掉 32.7% 的 commit 历史，让「CI 自动重生成产物」与「人类 PR 评审」在 git log 里视觉分离——可复用到任何「数据=代码」项目。
- **「三原则硬约束」护城河**：在 iptv-org/iptv（118k stars，走「全量自动化」）之外，用「仅免费 / 仅主流 / 仅质量」的人工策展路线，挖出 niche 生存空间，是「open-core 之外的开源策展」范本。

## 项目展示

> 本仓库无架构图、截图、Demo 视频。README 主要内容是 Markdown 频道表 + 国旗 SVG，下方为代表性国别国旗（按"美/英/日/中/意"覆盖度排列）：

1. ![USA flag](https://hatscripts.github.io/circle-flags/flags/us.svg) — 美国频道（共 ~700+ 条流，主流免费电视最大单国集合）
2. ![UK flag](https://hatscripts.github.io/circle-flags/flags/gb.svg) — 英国频道（BBC/ITV/Channel 4/5 全套，公共电视执照费频道被 README 第 183 行明确豁免）
3. ![Japan flag](https://hatscripts.github.io/circle-flags/flags/jp.svg) — 日本频道（NHK 主流 + 各地方局）
4. ![China flag](https://hatscripts.github.io/circle-flags/flags/cn.svg) — 中国大陆/港澳/台湾频道（覆盖粤语、闽南语等方言台）
5. ![Italy flag](https://hatscripts.github.io/circle-flags/flags/it.svg) — 意大利频道（社区最活跃分支，131 次修改位列 `lists/` 第一）

> 注：所有国旗均为外链（hatscripts 第三方 SVG 服务），下游使用请重新校验。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/free-tv/iptv |
| Star / Fork | 16,636 / 2,500 |
| Watcher | 623 |
| Open Issues / PRs | 171 / 40 |
| 代码行数 | 164 行（Python 89.6% / Shell 10.4%） |
| 注释/数据行 | 3,414（Code/Comment 比 1:20.8） |
| 文件数量 | 95（其中 90 份 `lists/*.md` + 1 份 `make_playlist.py` + 1 份 `make_flags.sh` + 3 份 README/flag_order/epglist） |
| 项目年龄 | 62 个月（2021-04-13 首次提交） |
| 总 commit | 1,550（PlaylistBot 32.7% + infid0 16.1% + KAMI911 10.8% + freetv332 7.6%） |
| 近 30 / 90 / 365 天 commit | 0 / 9 / 103 |
| 开发阶段 | 低维护（近 30 天 0 commit，进入平台期） |
| 开发模式 | 职业项目（自动 bot 驱动）+ 业余社区维护（周末 30.1%、深夜 21.0%） |
| 贡献模式 | 社区驱动（109 贡献者，PlaylistBot + 3 个核心人类 + 长尾志愿者） |
| 热度定位 | 大众热门（最近 9 天 136 star，6 月单月 130 star，但 star 来自消费端订阅播放器而非开发端） |
| 质量评级 | 代码[良好] 文档[优秀] 测试[基本] CI[完善] 错误处理[较差] |
| License | 无（无显著 LICENSE 文件，属隐式许可状态） |
| Tag / Release | 0 / 0（数据仓库，无版本概念） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

`Free-TV` 是 GitHub Organization，背后是个人维护者 `freetv332`（5.2 年账号龄，2,249 followers，仅 1 个公开仓库），核心人类贡献者含意大利人 `KAMI911`（167 commit）与匈牙利背景 `TVKaista`、英语圈主导者 `infid0`（250 commit）。这种「组织化品牌 + 个人实控 + 多语种分片维护」的混合体非常适合数据治理型项目，既避免单点失活又保持策展中立性。

### 问题判断

作者看到的是：剪线族（cord-cutters）/ 海外侨民 / Kodi-VLC-TiviMate 用户要拼凑一份「全球 + 主流 + 合法 + 免费 + 带 EPG」的电视清单，必须在两个极端之间选其一——要么接受 iptv-org/iptv 的「全量自动化」（10 倍规模但失效多、来源可疑、含灰色内容），要么忍受「付费机顶盒 + 灰色 IPTV reseller」。作者选择走中道：**「三原则硬约束」**（Quality over quantity / Only free channels / Only mainstream channels）把灰色资源站排除在外，把 iptv-org 的「广而杂」过滤成「少而精」。

时机也恰到好处：2018 年后 Pluto TV、Plex TV、Samsung TV Plus、Rakuten TV 这一波 FAST（Free Ad-Supported Streaming TV）兴起，「合法免费电视」的供给侧爆发——免费主流频道的素材来源问题被 FAST 平台解决了，剩下的是「策展与组织」。

### 解法哲学

- **「数据即代码」**：频道存为人类可编辑的 Markdown 表格（`[>]` 标记有效链接），`make_playlist.py` 解析为 M3U8，GitHub Actions 触发再生成。这种「Git-as-CMS」让 PR 直接变成贡献入口——任何普通贡献者打开 `lists/italy.md` 都能立即参与。
- **最小自动化**：唯一的自动化工件是 162 行无第三方依赖的 Python（仅 `os` + `re`）；所有「自动化检测」（失效链接、EPG 匹配、geo 标注）都交给**人类 + PR 工作流**完成——这与 iptv-org 的「Actions 抓取 + 自动验证」路线形成鲜明对比。
- **「通过否定来定义」**：`README.md` 第 103-126 行用醒目排版列出三原则，同时给出**显式反例**（无 +1、无替代 feed、无区域变体；公共电视执照费不算私有订阅；无成人 / 无宗教 / 无政党 / 无跨境政府频道）——把边界划在引战区的对面。

### 战略意图

项目是**核心产品本身**，不是某条产品线的子集；没有母公司 / 商业版 / SaaS——纯社区策展、纯 Git-as-CMS。所有频道元数据、EPG 桥接、生成产物全部公开，没有 open-core、没有 pro 分支。PlaylistBot（454 commit, ~32.7%）作为自动化代理人履行「rebuild playlist + commit + push」职责，所有人类 PR 必须通过它的编译步骤才能被消费——这把「PR 合规检查」成本从人工转移到机器，但保留人类对频道内容的主观裁量。

## 核心价值提炼

### 创新之处

1. **`[>]` 作为编译开关的 Git-as-CMS 模式**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）：在 markdown 表格的 Link 列里用 `[>]` / `[x]` 前缀表示「是否纳入播放列表」。`make_playlist.py` 第 153-154 行只识别带 `[>]` 的行——等价于「在 markdown 里手写 `.gitignore`」。

2. **`zz_` 前缀做主题集合的虚拟目录 hack**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）：`lists/zz_news_ar.md` / `zz_news_en.md` / `zz_news_es.md` / `zz_documentaries_ar.md` / `zz_documentaries_en.md` / `zz_movies.md` / `zz_vod_it.md` 7 个文件按 ASCII 排序天然落到各国之后——在 `make_playlist.py` 第 138 行 `sorted(os.listdir(lists_dir))` 下输出 `group-title="VOD Italy"` 等主题组，**用文件名排序隐式实现目录树**。

3. **PlaylistBot「机器代理 commit」治理范式**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）：传统 CI 是「verify → pass/fail」，这里 CI 是「rebuild → auto commit → push」；PlaylistBot 用硬 push（`git push -f`）+ 专用 `playlistbot@users.noreply.github.com` 身份 + 静默 commit（`--quiet`），让 git log 里机器噪声与人类信号视觉分离。

4. **多源外部 EPG fallback via `x-tvg-url` 头注入**（新颖度 3/5 | 实用性 4/5 | 可迁移性 3/5）：`epglist.txt` 收录 100+ 个 XMLTV 源 URL，`make_playlist.py` 第 131-134 行把它们用 `", "` 拼到 m3u8 头部作为 `x-tvg-url="URL1, URL2, ..."`，让 IPTV 播放器自动按 `tvg-id` 在多个 EPG 源里检索节目数据。

5. **`flag_order.txt` 注释驱动「人文地理顺序」国家列表**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）：136 行纯 ASCII 注释 + 国家名，按 Anglo → Asia → Europe sub-region (Nordics/Baltics/Benelux/DACH/Visegrád/Romanian/ex-Yugoslavia/Albanian/Greek/Microstates) → Middle East → Americas → Africa 分 12 组——比字母序更贴合「剪线族看家乡台」的心智模型。

6. **双产物 pipeline：全球聚合 + 单国分片**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）：`make_playlist.py` 第 138-158 行遍历 `lists/*.md` 每处理一个国家就同时写「全球版 `playlist.m3u8`」和「国家版 `playlists/playlist_<country>.m3u8`」两份产物；单国用户节省 90%+ 流量，编辑一份 md 同时影响 2 份产物。

### 可复用的模式与技巧

| 模式 | 简述 | 适用场景 |
|------|------|----------|
| **Git-as-CMS for content curation** | `lists/*.md` 是源、commit 是审计、PR 是评审、`.py` 是编译器、`.m3u8` 是发布物 | 频道清单、商品目录、地址簿、食谱库、术语表、书单 |
| **机器代理 commit（CI auto-commit with bot identity）** | 独立邮箱 + 静默 + 硬 push，与人类 commit 视觉分离 | 所有「产出物与源数据自动同步」的静态站 / 文档项目 |
| **`[>]` / `[x]` 前缀作为 PR 编译开关** | 在 markdown 表格里手写 `.gitignore` 风格的二态注释 | 所有「PR 进入主分支前需要 review、review 通过后自动进入产出」的策展型项目 |
| **多源外部数据 fallback via header injection** | `x-tvg-url` 把 100+ 第三方 EPG 源聚合到一个 m3u8 头部 | 依赖多个独立数据源的「索引 + 检索」协议（OpenSearch、RSS aggregator 等） |
| **借力外部「代码表 + 资源库」** | `Hypnotix countries.list`（ISO 映射） + `circle-flags`（SVG 资源） | 需要「ISO/标准码 + 视觉资源」的项目 |
| **`zz_` 前缀做主题集合排序 hack** | 用 ASCII 排序约定替代显式目录结构 | 少量特殊分组夹杂在大量相似条目中的列表项目 |
| **unicode 字符做状态注释** | `Ⓖ` / `Ⓢ` / `Ⓨ` 后缀表达 geo-blocked / SD / YouTube live | markdown 表格里需要附加语义但语法受限的场景 |

### 关键设计决策

**1. Markdown 而非 YAML/JSON/CSV 作为频道源数据格式**
- 问题：需要让非程序员志愿者能直接参与；同时要支持按国家、按子组（DVB-T / DVB-S / Pluto）层级化组织；并允许每行附加注释（SD/HD/GeoIP/YouTube）而无需扩展 schema。
- 方案：`lists/<country>.md` 文件，`<h1>` 作组标题，`<h2>` 作子组，`<table>` 行包含 `# / Channel / Link / Logo / EPG id` 五列；`[>]` / `[x]` 前缀作为「是否纳入播放列表」编译开关；末尾的 unicode 字符做语义注释。
- Trade-off：牺牲了机器可解析性（要写正则才能解析 markdown 表格）换来**人类可编辑性 + GitHub 渲染 + PR diff 可读**；`Channel.__init__` 第 99-105 行的 `parts = md_line.split("|")` 是脆弱的——只要 URL 列包含 `|` 就崩，但 m3u8 URL 几乎都不含 `|`，脆弱性可接受。
- 可迁移性：高。

**2. PlaylistBot 自动 commit 重建 playlist（机器代理 commit 范式）**
- 问题：人工直接 commit `playlist.m3u8` 容易出现「数据 vs 产物不一致」（Issue #211 提到的「贡献者改 md 但忘了同步 m3u」）。
- 方案：`update_playlist.yml` 第 14-21 行让 PlaylistBot 自动 commit 重建后的 playlist（`git diff --staged --quiet || git commit ...`）；`test_playlist.yml` 第 21-50 行用 `m3u-linter` 校验格式 + `iptv-checker`（基于 ffmpeg 实测）检查 100 条流的可用性，`-p100 -t120000` 表示并发 100、超时 120 秒。
- Trade-off：PlaylistBot 占用 32.7% 的 commit（约 454 次）——commit 历史被机器噪声稀释；换来的是**数据/产物强一致 + 失效链接的早期发现**。
- 可迁移性：高。

**3. EPG 桥接完全外置到 `epglist.txt` + `x-tvg-url` 头**
- 问题：EPG 维护是 IPTV 生态里最重的负担——一个国家可能就有几十个频道、每天的节目数据高达几百 MB；自建 EPG 不现实。
- 方案：`make_playlist.py` 第 131-134 行读 `epglist.txt` 把 100+ URL 拼到 m3u8 头部；同时每个频道的 `tvg-id`（如 `Rai1.it`）由人工在 markdown 第 5 列直接给出。
- Trade-off：依赖外部 EPG 提供者（主要是 `epgshare01.online`），但通过**多 URL fallback** 降低单点失效风险；要求每个贡献者懂「EPG id 命名约定」（参考 Issue #69 的讨论）。
- 可迁移性：中（原理通用，但 M3U8/EPG 是 IPTV 专用）。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | free-tv/iptv（本项目） | iptv-org/iptv | iptv-org/database + epg | TiviMate / IPTV Pro | 各国本地 fork |
|------|----------------------|---------------|------------------------|--------------------|----------------|
| **Stars** | 16,636 | 118,000+ | 数千 | N/A（闭源） | 几十~几百 |
| **策展模式** | 人工 PR 评审 | 自动化聚合 | 自动化 + 结构化 JSON | 商业客户端 | 人工 / 半自动 |
| **频道数** | ~5,000（90 国） | 50,000+ | 100,000+ | N/A | 几十~几千 |
| **失效链接率** | 低（三原则过滤） | 高（自动化未过滤） | N/A（数据底座） | N/A | 中 |
| **是否含 EPG** | 是（聚合 100+ XMLTV 源） | 是（独立 epg 仓库） | 是（独立 epg 仓库） | 是（客户端渲染） | 视 fork 而定 |
| **机器可消费** | 弱（要解析 markdown） | 强（独立 JSON + API） | 极强（JSON） | N/A | 弱 |
| **是否需付费** | 免费 | 免费 | 免费 | $5-10/月 | 免费 |
| **覆盖主流免费** | 强（核心定位） | 中（含可疑来源） | 强（数据完整） | 强（任何源） | 强（单国） |
| **EPG id 治理** | 人工精确给定 | 散落多仓库 | 散落多仓库 | N/A | 弱 |
| **生态位** | 「少而精」剪线族首选 | 「全量」事实标准 | 元数据底座 | 商业播放器 | 单国补充 |

### 差异化护城河

- **信任护城河**（核心）：三原则硬约束 + 人工 PR 评审 = 失效链接少。这是 iptv-org 自动化路线很难快速复制的——「人审」成本是免费的，但「人」的时间是稀缺的。
- **生态护城河**：与 iptv-org 形成「全量 vs 策展」分工而非正面冲突——Plex / Jellyfin 默认引用 iptv-org，TiviMate 用户把 free-tv URL 填进去即用。
- **双产物护城河**：`playlist_<country>.m3u8` 单国分片让单国用户节省 90%+ 流量——iptv-org 至今只有一份聚合产物。

### 竞争风险

- 最可能被**某个大平台的官方 playlist + 官方 EPG** 替代（如 Plex 已经把 iptv-org 作为默认源）。若 Samsung TV Plus / Pluto TV 官方推出「导出 M3U8」功能，free-tv 的存在基础会被削弱。
- iptv-org 若未来引入「verified topic」分支（类似 GitHub 的 verified topic）做策展，free-tv 的 niche 会被进一步挤压。
- 闭源商业播放器如果捆绑免费 channel aggregator，free-tv 的导流价值会下降。

### 生态定位

在 IPTV 生态里，free-tv 扮演**「开源社区策展的免费电视指南」**角色——介于「完全无策展（iptv-org 全量）」和「完全商业化（TiviMate 订阅）」之间，是开源剪线文化的核心基础设施之一。它不生产内容（频道流由官方广播商 / FAST 平台提供），不消费内容（不提供客户端），只做**「从碎片化到一份可信 M3U8」的策展与生成**。

## 套利机会分析

- **信息差**：未在「代码仓库」语境下被低估——16K stars + 2.5K forks 已是剪线族圈子的「国民级」资源；但在「Git-as-CMS 治理范式」语境下，**对工程读者群被严重低估**——这是少有的、可以拆解出可迁移设计模式的内容策展仓库（PlaylistBot 模式、`[>]` 编译开关、zz_ 排序 hack、epglist 多源 fallback），公众号技术向读者有学习价值。
- **技术借鉴**：
  - 「机器代理 commit」模式 → 适用于任何「代码=数据」项目（API doc 自动重建、翻译记忆库同步、Schema-as-code 项目的导出物）
  - `epglist.txt` + `x-tvg-url` 多源 fallback → 适用于依赖多个独立数据源的「索引 + 检索」协议
  - `flag_order.txt` 注释驱动人文地理顺序 → 适用于「分类 + 排序」被产品文化强约束的列表项目
- **生态位**：在 iptv-org（118k stars，全量自动化）旁边挖出「少而精」 niche，是「open-core 之外的开源策展」范本——可作为任何「高质量小众项目」定位的参考（不与大而全的项目正面竞争，挖垂直需求）。
- **趋势判断**：已无明显增长（近 30 天 0 commit、2024 下半年起进入低维护平台期）。star 仍快速增长（130/月）但全部来自消费端订阅播放器用户，与开发活跃度脱钩——这是「内容仓库」的典型命运：**消费曲线长，开发曲线短**。**没有后发优势**——作为内容仓库，其价值与 GitHub 平台绑定度低（任何人都可以 fork 一份继续策展），护城河是社区而非代码。

## 风险与不足

- **代码脆性**：`Channel.__init__` 第 99-105 行的 `parts = md_line.split("|")` 无任何异常捕获——若 markdown 表格行格式偏差（URL 列含 `|` 或 Logo 列缺 `src="..."`），会 `IndexError` 崩溃。`make_flags.sh` 第 14-15 行对缺失 country code 做 `exit 1`（合理），但未捕获 curl 失败（如果 Hypnotix 仓库暂时不可达，curl 静默成功但返回空）。
- **工程化薄弱**：无单元测试、无 CHANGELOG、无 LICENSE、无 linter/formatter 配置、无 CONTRIBUTING.md（靠 README 内嵌 PR 流程说明替代）。无 refactor / docs / test commit 印证——这是「数据托管」项目而非「软件项目」的典型代价。
- **架构性脆弱性**：很多频道共用第三方服务器（如 `185.189.225.150:85`），单点故障会让 4-5 个主流频道同时下线（Issue #749 「西班牙频道大量失效」即典型案例）。仓库本质是「目录」而非「内容」——可靠性结构上不归项目控制。
- **维护模型不可持续**：URL 频繁失效，维护者精力有限，需要持续志愿者补位（Issue #211 「Looking for contributors」41 条评论是社区活跃度的真实信号）。PlaylistBot 32.7% commit 占比 + 近 30 天 0 commit = 仓库正在进入「bot 维护但人不再写代码」的失能征兆。
- **「三原则」边界争议**：用户对「主流」边界的理解与维护者不一致（Issue #239 「pls add iran channel」即典型冲突），可能引发社区治理争议。
- **隐式许可状态**：无 LICENSE 文件意味着法律上「all rights reserved」——5 年持续运营、109 贡献者参与却无明确开源许可证，对商业 fork 和二创形成实际法律阻碍。

## 行动建议

- **如果你要用它**：作为 Kodi / VLC / TiviMate / IPTV Simple Client 的订阅源直接用——`https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8` 是主入口，`playlists/playlist_<country>.m3u8` 是单国入口。对比 iptv-org 选它的理由是「失效链接少 + 不含灰色内容 + 单国分片节省流量」；不选它的理由是「频道数小一个数量级 + 部分国家覆盖深度不足」。

- **如果你要学它**：重点关注以下文件/模块——
  - `make_playlist.py`（162 行，零依赖，单文件可读——30 分钟读完，能学会「数据即代码」的最简实现）
  - `.github/workflows/update_playlist.yml`（PlaylistBot 机器代理 commit 的完整配置——学习 CI auto-commit 的最佳实践）
  - `.github/workflows/test_playlist.yml`（`m3u-linter` + `iptv-checker` 的双层校验——学习数据质量门禁）
  - `lists/italy.md`（社区最活跃的国家分支——学习 markdown 频道表的标准格式）
  - `flag_order.txt`（注释驱动的人文地理分类——学习「可读性 > IDE 高亮」的配置文件设计）
  - `README.md` 第 103-126 行（「三原则硬约束 + 显式反例」的写作范式——学习如何通过否定来定义边界）

- **如果你要 fork 它**：可改进的方向——
  - **许可证缺失**：补 LICENSE（推荐 MIT / CC-BY-SA）以解决 5 年社区贡献的合法化问题
  - **错误处理**：在 `Channel.__init__` 加 try/except + 给出有意义的错误位置（行号 + 文件名）
  - **单元测试**：为 `Channel.__init__` 的 `split("|")` 解析逻辑写 5-10 个回归测试
  - **失效链接自动检测**：用 `iptv-checker` 的结果驱动自动 issue（链接失效 → 自动开 issue + 标记 `help wanted`）
  - **EPG id 一致性检查**：在 CI 里加一道 `tvg-id` 唯一性 + 命名约定校验
  - **机器可消费**：把 `lists/*.md` 同步导出成 `database.json`（参考 iptv-org 的 database 仓库），让程序消费

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录（403 Forbidden） |
| 关联论文 | 无（内容策展型仓库，无学术产出） |
| 在线 Demo | 无（产品即仓库本身：`https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8` 可直接作为 IPTV 播放器订阅 URL） |
