# Skyvern 网络分析报告

> 分析时间：2026-03-22
> 仓库：[Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)

## 仓库基本数据

| 指标 | 值 |
|------|-----|
| 名称 | skyvern |
| 描述 | Automate browser based workflows with AI |
| Stars | 20,883 |
| Forks | 1,858 |
| Watchers | 101 |
| Open Issues/PRs | 58 issues / 85 PRs |
| 许可证 | AGPL-3.0 (GNU AGPLv3) |
| 主语言 | Python (7.7MB)，TypeScript (3.3MB) 为辅 |
| 其他语言 | Jinja, JavaScript, MDX, Shell, HTML, CSS, Mako, Dockerfile |
| 仓库大小 | ~506 MB |
| 创建时间 | 2024-02-28 |
| 最后推送 | 2026-03-21（分析前1天） |
| 是否归档 | 否 |
| 是否Fork | 否 |
| 官网 | https://www.skyvern.com |
| 默认分支 | main |
| 当前版本 | v1.0.24（2026-03-13 发布） |
| Topics | api, automation, browser, computer, gpt, llm, playwright, python, rpa, vision, workflow, browser-automation, ai, powerautomate, puppeteer, selenium |

**项目定位**：基于 LLM 和计算机视觉的浏览器自动化工具。与传统依赖 DOM 解析和 XPath 的方案不同，Skyvern 使用视觉大语言模型动态理解和交互网页，无需为每个网站编写定制脚本。提供 Playwright 兼容 SDK + 无代码工作流构建器。

## 作者画像

### 组织概况 (Skyvern-AI)

| 属性 | 值 |
|------|-----|
| 类型 | 组织账号 |
| 简介 | Skyvern helps companies automate browser based workflows with AI |
| 位置 | United States of America |
| 官网 | https://www.skyvern.com/ |
| 关注者 | 401 |
| 公开仓库数 | 6 |
| 创建时间 | 2023-08-04 |

**组织旗下仓库**：
1. **skyvern** (20,883 stars) - 核心产品，Python，持续活跃
2. **n8n-nodes-skyvern** (17 stars) - N8N 集成节点，TypeScript
3. **wyvern** (77 stars) - 前身/关联项目，Python，2023年停更
4. **wyvern-docs** / **wyvern-starter** - wyvern 配套文档和入门项目，均已停更
5. **repo-file-sync-action** (3 stars) - Fork 项目

**判断**：Skyvern-AI 是一家专注于 AI 浏览器自动化的初创公司。Wyvern 系列（推荐/排序引擎）是其早期探索方向，后来完全转向浏览器自动化赛道。

### 核心贡献者

| 排名 | 贡献者 | 提交数 | 身份 |
|------|--------|--------|------|
| 1 | **wintonzheng** (Shuchang Zheng) | 1,767 | Skyvern 公司成员，旧金山，创始人级别 |
| 2 | **LawyZheng** | 587 | 核心开发者 |
| 3 | **ykeremy** (Kerem Yilmaz) | 400 | 旧金山，核心开发者 |
| 4 | **jomido** | 259 | 核心开发者 |
| 5 | **suchintan** | 215 | 核心开发者 |
| 6 | **pedrohsdb** | 168 | 活跃贡献者 |
| 7 | **stanislaw89** | 167 | 活跃贡献者 |
| 8 | **celalzamanoglu** | 147 | 活跃贡献者 |
| 9 | **marcmuon** | 116 | 活跃贡献者 |
| 10 | **Prakashmaheshwaran** | 63 | 贡献者 |

**贡献分布分析**：wintonzheng 一人贡献了 1,767 次提交，占绝对主导地位（约47%）。前5名贡献者合计超过 3,200 次提交，说明这是一个有稳定核心团队的商业公司项目，社区外部贡献相对较少。

## 社区热度

### Star 增长趋势

- **起步期**（2024-02-28 ~ 2024-03）：项目创建后几天内即获得大量关注，早期 star 密集增长
- **最近活跃度**（2026-03-19 ~ 2026-03-21）：每天持续新增 star，3天内约 30 个新 star，说明项目保持稳定的曝光度和吸引力
- **总量**：20,883 stars，对于一个 2024 年 2 月创建的项目来说增长迅猛

### 发布节奏

| 版本 | 发布时间 |
|------|---------|
| v1.0.24 | 2026-03-13 |
| v1.0.23 | 2026-03-02 |
| v1.0.22 | 2026-02-26 |
| v1.0.21 | 2026-02-24 |
| v1.0.20 | 2026-02-21 |

**发布频率**：近一个月内发布了 5 个版本，平均每 4-5 天一个版本，开发节奏极快。

### 最近提交活动

最近的提交（2026-03-20/21）包括 API 规范更新、安全漏洞修复（Minerva 定时攻击）、脚本审查功能、存储安全限制、登录测试增强等，显示项目在安全性和功能完善方面持续投入。

### 社区基础设施

- Discord 社区：活跃（有官方 Discord 链接）
- 社区健康度：75%（GitHub community profile）
- 有 CODE_OF_CONDUCT.md 和 CONTRIBUTING.md
- 缺少 Issue 模板和 PR 模板

## 生态网络

### 集成生态

Skyvern 构建了丰富的集成生态：

- **工作流平台**：Zapier、Make.com、N8N（有专门的 n8n-nodes-skyvern 包）
- **密码管理器**：Bitwarden 集成（已完成），1Password（开发中）
- **MCP 协议**：支持 Model Context Protocol，可与任何支持 MCP 的 LLM 集成
- **SDK**：Python SDK (`pip install skyvern`) + TypeScript SDK (`npm install @skyvern/client`)
- **浏览器引擎**：基于 Playwright，支持 CDP 连接本地 Chrome

### 技术生态位

Skyvern 处于 "AI 浏览器自动化" 赛道，连接了以下技术领域：
- **RPA（机器人流程自动化）**：替代传统 Selenium/Puppeteer 方案
- **LLM Agent**：受 BabyAGI 和 AutoGPT 启发的任务驱动自主代理
- **计算机视觉**：使用 Vision LLM 理解网页
- **多模型支持**：OpenAI、Anthropic、Gemini、UI-TARS 等

## 官方文档洞察

### 官网 (skyvern.com)

- 定位为 "AI 驱动的浏览器自动化工具"
- 提供 Skyvern Cloud 托管服务（app.skyvern.com）
- 有完整的产品文档站（skyvern.com/docs）
- 官方博客活跃，发布竞品对比文章（Browser Use vs Skyvern, Browserbase vs Skyvern 等）

### 核心功能亮点

1. **四大 AI 页面命令**：`page.act()`, `page.extract()`, `page.validate()`, `page.prompt()`
2. **三种交互模式**：传统 Playwright 选择器 / AI 自然语言 / AI 降级兜底
3. **工作流系统**：支持循环、条件分支、HTTP 请求、自定义代码等块类型
4. **实时流媒体**：可实时查看浏览器操作过程
5. **认证支持**：2FA (TOTP)、密码管理器集成
6. **脚本缓存**：重复工作流执行速度提升 10-100 倍

### 部署方式

- **Skyvern Cloud**：托管服务，内置反机器人检测、代理网络、验证码解决
- **本地部署**：pip install + quickstart 或 Docker Compose
- **嵌入式模式**：作为 SDK 嵌入到现有应用中

### 性能基准

- WebBench 基准测试：64.4% 准确率（SOTA）
- 在 WRITE 任务（表单填写、登录、文件下载等）上表现最优
- WebVoyager 评估：85.8%（根据技术报告）

## 竞品清单

| 竞品 | Stars | 定位 | 与 Skyvern 的差异 |
|------|-------|------|-------------------|
| **browser-use** | 81,796 | 让 AI 代理可访问网站，自动化在线任务 | Star 数约为 Skyvern 的 4 倍，社区更大；WebVoyager 得分 89%；更轻量的 Python 库 |
| **UI-TARS-desktop** (字节跳动) | 28,976 | 多模态 AI 代理栈 | 字节跳动出品，侧重多模态桌面代理 |
| **Browserbase** | 商业 | 托管无头浏览器实例集群 | 2025 年 B 轮融资 $40M；侧重基础设施层而非 AI 代理层 |
| **Hyperbrowser AI** | 商业 | AI 代理的互联网基础设施 | 内置验证码解决和代理管理；亚秒级启动 |
| **Steel** | 开源 | 为 AI 代理设计的浏览器 API | 开源，专注于云端浏览器舰队管理 |
| **Lightpanda** | 开源 | 为 ML 和自动化设计的浏览器引擎 | 性能是 Chrome 的 11 倍，内存降低 9 倍；侧重底层引擎 |
| **Browser Operator** | 开源 | 隐私优先的 AI 浏览器 | 强调隐私和企业合规 |
| **Claude Computer Use** | Anthropic | 视觉方式控制计算机 | Anthropic 原生能力，非独立产品 |
| **OpenAI Operator** | OpenAI | 视觉方式控制浏览器 | OpenAI 原生能力 |

**竞争态势**：browser-use 是最大的开源竞争对手，社区规模约为 Skyvern 的 4 倍。但 Skyvern 在企业级功能（工作流系统、认证管理、集成生态）和 WRITE 任务性能上有优势。Browserbase 和 Hyperbrowser 则更侧重基础设施层。

## 关键 Issue 信号

### 活跃 PR（按讨论热度排序）

| 编号 | 标题 | 评论数 | 状态 | 信号 |
|------|------|--------|------|------|
| #4904 | CDP screencast 流媒体与交互式输入（本地模式） | 12 | Open | 社区对本地模式的实时可视化需求强烈 |
| #4681 | 将流媒体集成为 Linux/WSL 上的 Skyvern 服务 | 7 | Open | 跨平台流媒体是持续需求 |
| #3841 | 文件夹、持久化导入进度追踪与 UX 增强 | 5 | Closed | 工作流管理和用户体验改善 |
| #3769 | Webhook 回放测试 URL | 5 | Closed | 开发者调试体验提升 |
| #4716 | 浏览器配置文件组件 | 5 | Open | 浏览器会话持久化是重要特性 |
| #4483 | 保留并显示下载文件的原始文件名 | 3 | Open | 细节体验优化 |
| #4393 | 完整多会话 VNC 支持 | 1 | Open | 远程浏览器控制能力 |
| #3349 | 改善移动端响应式和 UI | 4 | Open | UI 跨设备兼容需求 |

**Issue 信号总结**：
- 社区最关注的方向是 **实时可视化**（流媒体/VNC）和 **浏览器会话管理**（配置文件持久化）
- 项目以 PR 为主要工作方式，独立 issue 相对较少（58个），说明核心团队内部管理为主
- 没有积压大量未解决的 bug issue，项目维护状况良好

## 知识入口

| 平台 | 状态 | 链接 |
|------|------|------|
| DeepWiki | 已收录 | [deepwiki.com/Skyvern-AI/skyvern](https://deepwiki.com/Skyvern-AI/skyvern) |
| Zread.ai | 已收录 | [zread.ai/Skyvern-AI/skyvern](https://zread.ai/Skyvern-AI/skyvern) |
| 官方文档 | 完整 | [skyvern.com/docs](https://www.skyvern.com/docs/) |
| 官方博客 | 活跃 | [skyvern.com/blog](https://www.skyvern.com/blog/) |
| Discord | 活跃 | [discord.gg/fG2XXEuQX3](https://discord.gg/fG2XXEuQX3) |
| Twitter | 有账号 | [@skyvernai](https://twitter.com/skyvernai) |
| LinkedIn | 有页面 | [Skyvern LinkedIn](https://www.linkedin.com/company/95726232) |
| Product Hunt | 已上线 | [producthunt.com/products/skyvern](https://www.producthunt.com/products/skyvern) |

**DeepWiki 概要**：提供了完整的 6 层架构解析（用户界面层 -> API 层 -> 执行引擎层 -> 浏览器自动化层 -> AI/LLM 层 -> 数据持久化层），详细说明了 ForgeAgent 执行循环和工作流系统设计。

**Zread.ai 概要**：提供了 7 层架构视图，强调了三种执行模式（Task V1 步进式、Task V2 深度思考、Script 缓存执行），以及多 LLM 引擎支持（Skyvern V1/V2、OpenAI、Anthropic、UI-TARS）。

## 项目展示素材

### 核心演示场景

README 中展示了以下真实应用场景的 GIF 动画：

1. **保险报价获取**：自动在 GEICO、BCI Seguros 等保险网站获取报价（支持多语言）
2. **发票下载**：自动从多个不同网站批量下载发票
3. **求职申请**：自动化填写和提交工作申请
4. **制造业采购**：自动在零件供应商网站搜索和采购材料
5. **政府网站**：自动注册账号和填写政府表单
6. **联系表单**：自动填写各类"联系我们"表单

### 技术展示亮点

- **Skyvern 2.0 系统架构图**：展示多代理协同工作的系统设计
- **SDK 代码示例**：三种交互模式（传统选择器/AI 自然语言/AI 降级兜底）的对比演示
- **性能基准图表**：WebBench 整体得分和 WRITE 任务得分对比图

### 品牌资产

- 龙形 Logo（明暗主题双版本）
- 标语："Automate Browser-based workflows using LLMs and Computer Vision"
- 配色和设计风格：专业的技术产品风格

## 快速判断

### 综合评分

| 维度 | 评分 | 说明 |
|------|------|------|
| 热度 | ⭐⭐⭐⭐ | 20,883 stars，AI 浏览器自动化领域第二名 |
| 活跃度 | ⭐⭐⭐⭐⭐ | 每 4-5 天发一个版本，每天有提交，极度活跃 |
| 团队 | ⭐⭐⭐⭐ | 商业公司支撑，核心团队约 8-10 人，旧金山 |
| 社区 | ⭐⭐⭐ | Discord 活跃，但外部贡献者相对少，以内部开发为主 |
| 生态 | ⭐⭐⭐⭐ | Zapier/Make/N8N 集成，Python/TypeScript SDK，MCP 支持 |
| 竞争力 | ⭐⭐⭐⭐ | WRITE 任务 SOTA，WebBench 64.4%，WebVoyager 85.8% |

### 关键判断

1. **商业驱动的开源项目**：Skyvern 是一家 VC 支持的初创公司的核心产品，AGPL-3.0 许可证意味着商业使用需要注意合规。有 Skyvern Cloud 托管服务作为商业化路径。

2. **赛道头部选手**：在 AI 浏览器自动化赛道中，Star 数仅次于 browser-use（81,796），但在企业级功能和 WRITE 任务性能上具有差异化优势。

3. **快速迭代期**：当前处于 v1.0.x 版本快速迭代阶段，从版本号看已经走过了 0.x 的早期验证期，进入产品成熟化阶段。

4. **技术特色鲜明**：三种交互模式（传统/AI/降级）的设计非常务实，脚本缓存带来 10-100 倍性能提升是实用的工程优化。

5. **潜在风险**：核心贡献高度集中于 wintonzheng 一人（47% 提交），存在一定的"总线因子"风险。AGPL 许可证可能限制部分企业的采用。

### 适合关注的人群

- 需要自动化复杂网页工作流（表单填写、数据提取、文件下载）的企业
- 对传统 Selenium/Puppeteer 方案的脆弱性感到不满的开发者
- 构建 AI Agent 系统、需要浏览器交互能力的开发者
- 关注 RPA 赛道 AI 化趋势的技术决策者
