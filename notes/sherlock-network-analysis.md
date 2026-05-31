# sherlock-project/sherlock — Phase 1: Network Analysis

## 仓库基本数据
- **Star / Fork / Watcher**: 84,286 / 9,832 / 1,313
- **语言**: Python (主语言, ~98%), Dockerfile (1.7%), Shell (0.3%)
- **License**: MIT License
- **创建时间**: 2018-12-24 | **最近推送**: 2026-05-31
- **话题标签**: osint, reconnaissance, linux, cli, sherlock, python3, redteam, tools, information-gathering, hacktoberfest, python, cybersecurity, cti, forensics, infosec, pentesting
- **已归档**: 否 | **是Fork**: 否
- **最新版本**: v0.16.0 (2025-09-16, 发布于约8个月前)

## 作者画像
- **姓名/ID**: Sherlock (@sherlock-project) | **公司**: 无 | **位置**: 未公开
- **粉丝**: 2,602 | **公开仓库**: 4 | **账号年龄**: 约7年 (2019-03-06创建)
- **此 repo 投入权重**: 极高 (4个仓库中仅 sherlock 是主项目)
- **作者类型**: 开源组织 (非公司，但有组织结构)
- **贡献集中度**: 社区协作型 (top3贡献者: sdushantha 873次, hoadlck 467次, ppfeister 417次 —— 前三人占贡献主力，其余140+人少量参与)
- **背景推断**: 发源于独立开发者 sdushantha (冰岛) 的个人项目，经 Hacktoberfest 扩张后形成多元社区，ppfeister 自 v0.15.0 主导发布；主要维护者位于欧洲，多为网络安全/OSINT 爱好者

## 社区热度
- **热度级别**: 大众热门 (84k+ stars, OSINT 领域 top1)
- **增长模式**: 稳步持续型 (2018年底创建，7年间持续增长，未见明显爆发后回落)
- **近期趋势**: 2026年5月仍有活跃提交（vuln fix, false-positive修复），发布节奏约每14个月一个大版本
- **套利判断**: **被明显低估**。84k stars 在 OSINT 工具中遥遥领先同类竞品（maigret 31k, GHunt 19k），且持续维护中，但主流安全媒体提及度偏低，属于"闷声增长"型项目

## 生态网络
- **上游依赖**: 被多个安全工具间接依赖（如其他 OSINT 工具可调用 sherlock 作为子模块）；被 Kali Linux、BlackArch、ParrotOS 收录；Docker Hub 官方镜像
- **同类项目**:
  1. **soxoj/maigret** | Stars: 31,145 | 定位: 更激进的 username OSINT，覆盖 3000+ 站点 | 优势: 更多站点 | 劣势: 误报率高
  2. **mxrch/GHunt** | Stars: 18,995 | 定位: Google 框架 OSINT | 优势: Google 系深度 | 劣势: 仅限 Google 生态
  3. **smicallef/spiderfoot** | Stars: 17,999 | 定位: 全自动 OSINT 平台 | 优势: 端到端自动化 | 劣势: 重量级、配置复杂
  4. **twintproject/twint** | Stars: 16,376 | 定位: Twitter 专用爬虫 | 优势: Twitter 数据采集 | 劣势: 已不再积极维护
  5. **sherlock-project/sherlock** | Stars: 84,286 | 定位: 通用 username 跨平台搜索 | 优势: 简单易用、社区大、持续维护 | 劣势: 误报问题长期存在

## 官方文档洞察
*(官网 sherlockproject.xyz 需认证访问，以下基于 GitHub README + Zread.ai + Release Notes 综合)*

- **价值主张**: "Hunt down social media accounts by username across 400+ social networks" — 简单、直接、实用
- **目标用户**: 安全研究员、网络安全从业者、渗透测试人员、调查记者、社交媒体品牌管理者
- **差异化叙事**: 不依赖 API（避免速率限制）、支持 Tor/SOCKS 代理、多格式输出（txt/csv/xlsx/json）、支持批量用户名和通配符模式
- **设计哲学**: 极简 CLI 优先 → Python 包双模；社区驱动的站点 manifest（data.json）；持续治理 false-positive 问题（v0.16.0 重点）
- **技术路线图**: v0.15.0 引入 Poetry 重构、schema 验证；v0.16.0 引入自动 false-positive 过滤；未来方向：exe 构建 (issue #2006)、PyPI 官方包 (已完成)、多平台打包
- **架构文章要点**: 中心化 data.json 站点定义 + SherlockFuturesSession 并发请求 + QueryNotify 进度系统 + jsonschema 验证
- **外部深度视角**: Zread.ai 收录分析显示目标用户 = 安全研究员/调查员；技术栈 = requests/requests-futures + pandas + PySocks；部署 = pip/docker/Linux发行版

## 竞品清单

- **竞品1: soxoj/maigret** | Stars: 31,145 | 定位: 深度 username OSINT | 优势: 站点覆盖量更大 (3000+) | 劣势: 误报率更高，社区规模小
- **竞品2: mxrch/GHunt** | Stars: 18,995 | 定位: Google 生态系统 OSINT | 优势: Google ID/Email 交叉分析能力强 | 劣势: 仅限 Google，服务单一
- **竞品3: smicallef/spiderfoot** | Stars: 17,999 | 定位: 全自动威胁情报 OSINT | 优势: 自动化程度高、可视化界面 | 劣势: 重量级、不适合快速单点查询
- **竞品4: twintproject/twint** | Stars: 16,376 | 定位: Twitter 专用抓取 | 优势: 不需 Twitter API | 劣势: 已被 Elon Musk 封禁风险，维护停滞
- **竞品5: whobet.py / Sherlock-Project/api** | Stars: 82 | 定位: Sherlock REST API 封装 | 优势: 可编程调用 | 劣势: 非官方、用户少

**市场格局**: 蓝海向红海过渡中。通用 username 搜索已有 sherlock 主导，但 maigret 以更多站点占据细分，GHunt/spiderfoot 覆盖不同场景，尚未形成一家独大

## 关键 Issue 信号

1. [[#2006] Release .exe executable build](https://github.com/sherlock-project/sherlock/issues/2006) — 111条评论揭示了**跨平台分发的强烈需求**，用户希望 Windows 用户无需安装 Python 即可使用
2. [[#541] False positives](https://github.com/sherlock-project/sherlock/issues/541) — 31条评论暴露了**核心产品痛点**：误报率问题长期困扰用户，是 sherlock 最老牌的 issue 之一
3. [[#264] New logo wanted](https://github.com/sherlock-project/sherlock/issues/264) — 20条评论，**唯一 open 的高参与度 issue**，反映品牌建设需求
4. [[#647] Bug: False positive for 3 websites](https://github.com/sherlock-project/sherlock/issues/647) — 18条评论，false-positive bug 持续存在
5. [[#2122] Do we really need to package Sherlock for various platforms?](https://github.com/sherlock-project/sherlock/issues/2122) — 17条评论，社区围绕**多平台打包策略**存在分歧（官方支持 vs 社区维护）
6. [[#2011] I am new to GitHub and lots to say](https://github.com/sherlock-project/sherlock/issues/2011) — 29条评论，新用户大量涌入提建议，说明**用户增长快但文档不足**
7. [[#462] ModuleNotFoundError: requests_futures](https://github.com/sherlock-project/sherlock/issues/462) — 23条评论，**依赖安装问题是入门最大障碍**

## 知识入口
- **DeepWiki**: 未收录 (deepwiki.com/sherlock-project/sherlock 访问被拒绝)
- **Zread.ai**: 已收录 (https://zread.ai/sherlock-project/sherlock — 有详细架构分析)
- **关联论文**: 无直接关联学术论文
- **在线 Demo**: 无官方在线 Demo（CLI 工具属性决定）

## 项目展示素材

### README 媒体
1. `images/sherlock-logo.png` — 类型: hero/logo — 品牌标识，GitHub 页面展示
2. `images/demo.png` — 类型: screenshot/demo — 命令行运行截图，展示搜索结果
3. `images/banner.jpg` — 类型: banner/sponsor — OSINT Industries 赞助商横幅

### 筛选说明
- 总共发现 3 个媒体元素，筛选后保留 3 个
- README 无 badge/CI 图标（仅赞助横幅），展示性良好
- 项目以 CLI 工具为主，无视频演示

## 快速判断
- **是否值得深入**: **是**（有条件）
- **初步定位**: **被低估的大众热门 + 细分市场王者**
  - OSINT username 搜索领域实际垄断者（84k stars 远超竞品）
  - 误报问题是产品成熟度天花板，也是持续改进空间
  - v0.16.0 已在系统性解决 false-positive，方向正确
- **作者可信度**: **高**，理由: 7年持续维护，v0.15.0 成功完成 Poetry 重构，v0.16.0 引入自动化测试治理 false-positive，维护团队专业且多元
- **竞品格局**: **蓝海向红海过渡**，通用方案 sherlock 主导，细分方向各有竞争者，尚未出现整合型垄断平台