# GitHub 推荐：52K stars、3 年 0 个 tag：MediaCrawler 把「签名」做成了订阅生意

> GitHub: https://github.com/nanmicoder/mediacrawler

## 一句话总结
中文社媒爬虫的事实标准——7 平台（小红书/抖音/B 站/快手/微博/知乎/贴吧）一站采集，靠「CDP 连用户真实 Chrome + monkey-patch 修补第三方签名库」绕过风控，靠「无 tag + 微信赞赏 + 付费课 Pro」跑通商业化。

## 值得关注的理由
- **生态占位**：5.2 万 star，1.09 万 fork，是中文社媒爬虫圈无争议的 reference implementation；新爬虫工程师从这里入门。
- **反检测实战范式**：默认走 `playwright.connect_over_cdp` 连用户真实 Chrome（而非启动新 Chromium），把「navigator.webdriver=true」这个老问题用架构层方式绕开。
- **单飞副业做到职业级别**：作者程序员阿江-Relakkes 一人占 78% commit（3 个 git alias 合并），靠 B 站+公众号+赞赏+付费课四渠道变现，36 个月稳定维护。

## 项目展示

![Star History Chart](https://api.star-history.com/svg?repos=NanmiCoder/MediaCrawler&type=Date) — 热度曲线，3 年从 0 涨到 52K stars

![WebUI 界面预览](https://raw.githubusercontent.com/nanmicoder/mediacrawler/main/docs/static/images/img_8.png) — 配套 FastAPI WebUI（端口 8080），扫码登录 + 任务控制

![项目横幅](https://raw.githubusercontent.com/nanmicoder/mediacrawler/main/docs/static/images/tikhub_banner_zh.png) — README 顶部 banner，对接 TikHub 签名 API 平台

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/nanmicoder/mediacrawler |
| Star / Fork | 52,728 / 10,918 |
| 代码行数 | 25,777（Python 74.2% / JSON 15.4% / HTML 6.3% / JavaScript 2.4% / GraphQL 1.5%） |
| 文件数量 | 206（Python 160） |
| 项目年龄 | 36.6 个月（2023-06 → 2026-06） |
| 开发阶段 | 稳定维护（近 90 天 26 commit，月均 ~7，仍持续 fix 平台接口） |
| 贡献模式 | 单人主导（主作者 78.3%，第二名 28 commit） |
| 热度定位 | 大众热门（5 万 star 中文社媒爬虫圈天花板） |
| 质量评级 | 代码良好 / 文档优秀 / 测试基本（17 文件但 0 平台核心单测） |
| Release | **0 个 git tag，0 次 GitHub Release**（commit 节奏代替版本号） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
「程序员阿江-Relakkes」（GitHub: NanmiCoder），深圳，账号 7.4 年，公开仓库 39 个。垂直聚焦「反爬对抗 + 浏览器自动化」，账号字段直接写「MediaCrawler」—— 项目即人设。

### 问题判断
2023 年小红书 461 状态码、Verifytype 字段、抖音 webmsdk 升级把「裸 httpx 爬虫」挤到了死角；同期 CDP 协议 + Playwright `connect_over_cdp` 成熟，「接用户真实 Chrome」成为绕开 `navigator.webdriver` 的最优解。作者抓准这个时间窗口，把「扫码登录 + CDP 复用登录态」做成默认开箱体验。

### 解法哲学
- **配置驱动 + 教学友好 > 性能极致**：所有开关在 `config/base_config.py` 中文注释暴露，README 显式声明「仅供学习请勿商用」作合规护城河。
- **明确不做什么**：不做账号池、不做商业级分布式（`MAX_CONCURRENCY_NUM=1` 默认）、不做 UI——主动让位给 Pro 版。
- **跨域迁移**：从 web 后端的 Mixin、Singleton、Factory 模式（`ProxyRefreshMixin` / `ExcelStoreBase` / `XxxStoreFactory`）整体移植到爬虫，把「被风控追着跑」的项目做出服务端工程的体感。

### 战略图景
**Genuinely open，但 open-core 商业化**：
- 核心代码免费 NCAL 1.1
- Pro 版（断点续爬 / 多账号 / 企业架构）订阅
- 4 渠道变现：微信/支付宝/Buy Me a Coffee 打赏 + TikHub 签名 API 联运 + Atlas Cloud 云赞助 + B 站+公众号 私域引流
- 0 个 tag 是商业选择——发 tag 锁版本就断了「持续更新促打赏」的飞轮

## 核心价值提炼

### 创新之处

| 创新 | 新颖度 | 实用性 | 可迁移性 |
|------|------|------|------|
| **CDP 连用户真实 Chrome**（`playwright.connect_over_cdp("ws://localhost:9222")` 复用用户 Cookie/扩展/历史） | 4/5 | 5/5 | 5/5 |
| **monkey-patch 修补第三方签名库**（`xhshow` 的 GET a3 hash bug 启动时热修补，POST 走原生） | 4/5 | 4/5 | 3/5 |
| **ExcelStoreBase 单例流式追加**（类级 `_instances: Dict + _lock` 保证多 store 同一 workbook） | 3/5 | 5/5 | 5/5 |
| **comment 默认开、sub-comment 默认关**（分级降速 + 降低法律风险） | 3/5 | 4/5 | 4/5 |
| **CrawlerFactory 字典派发 + ABC 最小抽象**（7 平台扩展只需加 dict entry） | 2/5 | 4/5 | 4/5 |

### 可复用的模式与技巧
1. **CDP 优先于 Playwright** —— 反检测不要在 Chromium flag 上死磕，直接连用户的真实 Chrome。
2. **签名 = 上游库 + monkey-patch + 显式串构造** —— 不 fork 上游库，运行时修补 + 显式 quote/safe 规则对齐浏览器编码。
3. **8 后端存储 = ABC + Factory + 单例 Excel writer** —— ETL 数据落地直接抄。
4. **Mixin + Semaphore 长跑爬虫模板** —— `ProxyRefreshMixin._refresh_proxy_if_expired()` + `asyncio.Semaphore(MAX_CONCURRENCY_NUM)`。
5. **README 当 wiki 用** —— 50K+ star 必然导致「文档即客服」，从一开始就按 wiki 节奏维护（README 改了 204 次 / 776 commit = 26.3%）。

### 关键设计决策

1. **决策**：CrawlerFactory 字典派发 + 每个平台 `core.py` 手写
   - **问题**：7 平台 init/launch/search/store 流程要可插拔
   - **方案**：`CRAWLERS: dict` + `AbstractCrawler` 三个 ABC 最小契约
   - **Trade-off**：加平台简单（加 dict entry + 加文件），但平台间重复代码约 30%
   - **可迁移性**：高 —— 多云 SDK / 多数据库驱动 / 多 IM 协议通杀

2. **决策**：`ENABLE_CDP_MODE=True` 默认开启作反检测主防线
   - **方案**：`tools/cdp_browser.py` 535 行 + `browser_launcher.py` 291 行两层封装；CDP_CONNECT_EXISTING 复用用户浏览器，自动启动则注入 17 个反检测 flag
   - **Trade-off**：体验最像真人但需用户手动开远程调试；自动启动 flag 越多越可能被指纹库识别
   - **可迁移性**：高 —— 任何「既要登录态又要真人指纹」的爬虫/自动化项目

3. **决策**：0 个 git tag，0 次 Release
   - **方案**：让用户永远拉 main，每次升级拿最新反爬
   - **Trade-off**：放弃「语义化版本」的可预期性，换取「打赏驱动的持续更新飞轮」
   - **可迁移性**：低 —— 仅适合反爬/对抗类工具

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | MediaCrawler | TikTokDownload | weiboSpider | Douyin_TikTok_Download_API | RedNoteTools 小 fork |
|------|-------------|---------------|------------|---------------------------|--------------------|
| 平台覆盖 | **7 平台** | 2（抖音/快手） | 1（微博） | 1（抖音/TikTok） | 1（小红书） |
| 核心数据 | 内容+评论+创作者 | 视频文件下载 | 微博+关系图 | REST API | WebUI 包装 |
| 反检测 | CDP 复用真实 Chrome | 单 flag | 老牌低强度 | 弱 | 不定 |
| 存储后端 | 8（CSV/JSON/SQL/MySQL/PG/Mongo/Excel） | 文件 | CSV | API 输出 | 不定 |
| 教学 | VitePress 17 篇 + B 站视频 | 单 README | 学术文档 | 简单 | 简单 |
| 维护 | 月均 21 commit | 中 | 慢 | 中 | 难 |
| 商业化 | 赞赏+Pro 订阅+联运赞助 | 单赞助 | 无 | SaaS | SaaS |
| Stars | **52K** | 6K | 4K | 6K | 几百到几千 |

### 差异化护城河
- **生态护城河（最强）**：52.7K★ + B 站 434377496 + 公众号 + Pro 订阅 + 多个衍生 fork，构成中文社媒爬虫事实标准
- **教学护城河**：中文注释 config + 完整 VitePress 文档站 + Pro 版「看架构」营销
- **技术护城河（中）**：CDP 模式 + 多签名后端修补 + 8 存储后端

### 竞争风险
- **SaaS 化**（TikHub、Atlas Cloud）API 路线会侵蚀单平台小工具市场
- **签名持续升级**（xhs 461、抖音 webmsdk）让 monkey-patch 维护成本指数增长
- **Pro 版被 fork 魔改免费化**（issue #199/#191 的 OSS 治理难题）

### 生态定位
中文社媒爬虫的「教学型 reference implementation」——新爬虫工程师从这里入门，进阶后转向 TikHub/SaaS 或 fork 出自己的 Pro 版。**不是被低估的潜力股，而是已被广泛认可的实战教学项目**。

## 套利机会分析
- **信息差**：5 万 star 已是垂直天花板，**没有低估空间**。但作为学习样本（反爬实战、CDP 多平台适配）价值仍高。
- **技术借鉴**：
  - **CDP 连用户真实 Chrome** 模式可迁移到任何「既要登录态又要真人指纹」的自动化项目
  - **monkey-patch 修补 + 显式串构造**签名打法是反爬工程师通用工具
  - **ExcelStoreBase 单例流式追加**可直接抄到任何 ETL 流水线
- **生态位**：填补「一站式多平台采集 + 开源 + 教学驱动」三角空白
- **趋势判断**：未在增长（最近 200 star 集中在 3 天内进入，KOL 驱动型而非自然增长），但稳态后仍长期占据头部。比 SaaS 路线有「可审计 + 可修改」优势，比学术爬虫有「覆盖广度」优势。

## 风险与不足
- **单点作者风险**：78% commit 来自一人；账号年龄 7.4 年但作者若倦怠/转岗，项目可能进入半维护态
- **零自动化测试**：物理 17 个测试文件（2299 行）但 commit message 里 `test:` 几乎为 0（1/776 = 0.13%），且 **没有 CI 跑测试**，重构无保护
- **平台反爬升级**：xhs 461/Verifytype、抖音 webmsdk、B 站 wbi 持续升级，monkey-patch 维护成本指数增长
- **tieba 与 zhihu 平台热度低**（目录修改次数 74 / 54，约为 xhs 的 1/3），风控升级时响应会慢
- **NCAL 1.1 协议**（项目自定义，非 OSI 标准）+ 显式「仅供学习请勿商用」声明 = 商业使用有合规灰区
- **Linter/Formatter 缺失**：无 `.flake8` / `.ruff.toml` / `pyproject.toml [tool.ruff]`，pre-commit 声明了但没配

## 行动建议
- **如果你要用它**：
  - 适合：自媒体内容分析、研究者、做教学示例、需要「扫码登录 + 开箱即用」的非工程用户
  - 不适合：需要 SLA 的商业级数据采集、需要支持海外平台（Twitter/Reddit/YouTube）、需要真正分布式集群
  - **首选 SQLite 后端起步**，再迁 MySQL/PG
- **如果你要学它**（重点关注文件）：
  1. `tools/cdp_browser.py`（535 行）—— CDP 反检测范式核心
  2. `media_platform/xhs/playwright_sign.py`（monkey-patch 实战）
  3. `proxy/proxy_mixin.py`（Mixin + 代理自动刷新）
  4. `store/excel_store_base.py`（单例流式 Excel 写入器）
  5. `base/base_crawler.py`（三个 ABC 最小契约）
- **如果你要 fork 它**：
  - 加平台：照 `media_platform/<platform>/{core,client,login,field,help}` 模板复制 + 在 `main.py:51-67` 的 `CRAWLERS` dict 注册
  - 减维护负担：把 `launch_browser_with_cdp` 从「每平台重写」抽到 base（30% 重复代码可消解）
  - 接 CI 测试：把 `tests/` 接到 GitHub Actions（目前 0 CI）
  - 加 LLM 后处理：评论爬取后接 Claude 做情感分析/话题聚类（契合作者的 skills-agent-proto 路线）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | 无（非学术项目） |
| 在线 Demo | 无（爬虫类项目无 playground；作者提供 MediaCrawlerPro 付费 WebUI 作为商业化 Demo） |
| 官方文档站 | https://nanmicoder.github.io/MediaCrawler/ |
| 作者 B 站 | https://space.bilibili.com/434377496 |
| 架构文档 | `docs/项目架构文档.md`（含 Mermaid 流程图） |
| CDP 教程 | `docs/CDP模式使用指南.md` |
