# Zie619/n8n-workflows 网络分析报告

## 仓库基本数据
- Star / Fork / Watcher: 53,105 / 6,876 / 842
- 语言: Python (47.7%), HTML (26.0%), PLpgSQL (9.4%), JavaScript (6.3%), Shell (5.7%), TypeScript (2.3%), PowerShell (1.4%), Dockerfile (0.8%)
- License: MIT License
- 创建时间: 2025-05-14 | 最近推送: 2026-02-11
- 话题标签: 无（repositoryTopics 为 null）
- 已归档: 否 | 是Fork: 否
- 主页: https://zie619.github.io/n8n-workflows（GitHub Pages 在线搜索界面）
- 磁盘占用: ~45 MB

## 作者画像
- 姓名/ID: Eliad Shahar / Zie619 | 公司: 无（独立） | 位置: 未公开
- 粉丝: 3,837 | 公开仓库: 19 | 账号年龄: ~6.5 年（2019-08 创建）
- 此 repo 投入权重: **高**（在最近活跃仓库中排第 1，Star 数远超其他项目总和）
- 作者类型: 独立开发者（AI 和自动化工程师，有机械工程-机器人编程学位背景）
- 贡献集中度: 单人主导（Zie619 占 55% commits / 72 次，第二贡献者仅 10 次）
- 背景推断: 拥有机械工程-机器人编程学位，曾做 2 年控制算法工程师，现转型为 AI 与自动化工程师。个人博客为 Trusera.dev（目前 404），同时推广关联项目 AI-BOM（n8n 工作流安全扫描工具）。其他项目涵盖 n8n 聊天机器人、WhatsApp MCP、自动化技术栈等，深耕 n8n 生态。

## 社区热度
- 热度级别: **大众热门**（53K+ stars，n8n 生态中最大的第三方工作流集合）
- 增长模式: **爆发型 + 持续增长**
  - 2025-05-14 创建，前两周内获得首批约 100 stars
  - 2025-05-28 首次爆发（单日大量 star）
  - 2025-06 至 2025-11 月持续高速增长：约每月 5,000-10,000 stars
    - Page 1 (stars 1-100): 2025-05-14 ~ 2025-05-28
    - Page 50 (stars ~5,000): 2025-06-14
    - Page 100 (stars ~10,000): 2025-06-29
    - Page 200 (stars ~20,000): 2025-07-31
    - Page 300 (stars ~30,000): 2025-09-16
    - Page 400 (stars ~40,000): 2025-11-14
  - 从创建到 53K stars 仅用约 10 个月，增速极快
- 近期趋势: 2025-11 至 2026-03 约增长 13K stars（月均约 3K），增速有所放缓但仍保持高位
- 套利判断: **否，已充分曝光**。53K stars 意味着该项目已被广泛发现，不存在信息差套利机会。但对于 n8n 用户而言，其内容价值仍然很高。

## 生态网络
- 上游依赖: n8n 自动化平台（该仓库是 n8n 官方工作流模板的超集+社区采集）
- 关联项目:
  - [AI-BOM](https://github.com/Trusera/ai-bom) — 作者关联公司 Trusera 的 n8n 工作流安全扫描工具，在 README 中大力推广
  - [automation-stack](https://github.com/Zie619/automation-stack) — 作者的 n8n + Agent Zero + ComfyUI 自动化技术栈（128 stars）
  - [whatsapp-mcp-n8n](https://github.com/Zie619/whatsapp-mcp-n8n) — 作者的 WhatsApp MCP 与 n8n 集成（109 stars）
- 同类项目:
  1. **enescingoz/awesome-n8n-templates** | Stars: 20,392 | 280+ 模板，定位"最大开源 n8n 模板集合"
  2. **wassupjay/n8n-free-templates** | Stars: 5,584 | 200+ 即插即用工作流，融合 AI 技术栈
  3. **Marvomatic/n8n-templates** | Stars: 1,464 | 面向 SEO 和内容优化的 n8n 模板
  4. **lucaswalter/n8n-ai-automations** | Stars: 1,396 | YouTube 频道配套的 AI 自动化工作流
  5. **n8n.io/workflows** | 官方模板库: 8,800+ 模板 | n8n 官方维护

## 官方文档洞察
- 价值主张: "The Ultimate Collection of n8n Automation Workflows" — 4,343 个生产就绪的工作流，覆盖 365+ 集成，一站式解决 n8n 用户寻找自动化模板的需求
- 目标用户: n8n 自动化开发者、DevOps 工程师、希望快速部署自动化方案的企业用户
- 差异化叙事:
  1. 规模最大（4,343 工作流 vs 竞品的 200-280 个）
  2. 高性能搜索（SQLite FTS5，<100ms 响应）
  3. 多种部署方式（在线浏览、Docker、本地安装）
  4. 集成安全扫描（AI-BOM）
- 设计哲学: 追求全面收录（"all of the workflows of n8n I could find"），强调开箱即用和高性能搜索体验
- 技术路线图: 未明确公开路线图，但从更新日志看，持续优化安全性、Docker 支持和 UI
- 架构文章要点: README 中包含 Mermaid 架构图，三层架构：用户 -> Web 界面 -> FastAPI 服务 -> SQLite FTS5 数据库。后端支持 Python FastAPI 或 Node.js Express 双实现
- 外部深度视角:
  - [Templacity 分析文章](https://templacity.com/github-zie619-n8n-workflows/) — 提供了对项目的外部概述
  - [BlackHatWorld 讨论](https://www.blackhatworld.com/seo/2000-n8n-workflows-collection.1723692/) — 社区用户讨论使用场景
  - 未找到有深度独立分析的外部文章（多数为 README 复述）

## 竞品清单
| 竞品 | Stars | 定位 | 优势 | 劣势 |
|------|-------|------|------|------|
| **enescingoz/awesome-n8n-templates** | 20,392 | 精选 n8n 模板集合 | 自称"最大开源集合"，分类清晰 | 数量仅 280+，远少于 Zie619 |
| **wassupjay/n8n-free-templates** | 5,584 | AI 技术栈融合的 n8n 工作流 | 融合向量数据库、嵌入、LLM 等现代 AI 栈 | 200+ 模板，规模较小 |
| **n8n.io/workflows（官方）** | N/A | n8n 官方模板库 | 官方维护，质量有保证，8,800+ 模板 | 搜索体验一般，无本地部署选项 |
| **Marvomatic/n8n-templates** | 1,464 | SEO 和内容优化 n8n 模板 | 垂直领域专注 | 仅覆盖 SEO 场景 |
| **lucaswalter/n8n-ai-automations** | 1,396 | YouTube 频道配套 AI 自动化 | 有视频教程配合 | 数量有限，更新依赖频道节奏 |

## 关键 Issue 信号
1. [#85 Repository History Rewritten Due to DMCA Compliance](https://github.com/Zie619/n8n-workflows/issues/85) — 11 评论。因 DMCA 合规强制重写仓库历史，删除了 8 个工作流文件。揭示了**版权风险**：大规模采集 n8n 官方和社区工作流可能触及版权问题，这是该项目最大的法律隐患。
2. [#136 Docker Hub command](https://github.com/Zie619/n8n-workflows/issues/136) — 11 评论。用户对 Docker 部署方式的咨询，说明社区对本地部署的需求强烈。
3. [#138 Website popup for workflow detail](https://github.com/Zie619/n8n-workflows/issues/138) — 5 评论。用户对 Web 界面体验的反馈，说明在线浏览是核心使用场景。
4. [#123 property "connections": {}](https://github.com/Zie619/n8n-workflows/issues/123) — 5 评论。工作流 JSON 结构问题，揭示部分采集的工作流可能存在**数据质量问题**。
5. [#82 create_categories.py not working](https://github.com/Zie619/n8n-workflows/issues/82) — 5 评论。脚本兼容性问题，说明开发者工具链的维护存在一定滞后。

## 知识入口
- DeepWiki: [https://deepwiki.com/Zie619/n8n-workflows](https://deepwiki.com/Zie619/n8n-workflows) — 已收录，内容详尽
- Zread.ai: [https://zread.ai/Zie619/n8n-workflows](https://zread.ai/Zie619/n8n-workflows) — 已收录，内容详尽
- 关联论文:
  - [Evaluating Workflow Automation Efficiency Using n8n](https://arxiv.org/abs/2602.01311) — n8n 工作流自动化效率评估（非直接引用此仓库，但高度相关）
  - [ReusStdFlow: Standardized Reusability Framework](https://arxiv.org/abs/2602.14922) — 使用 n8n 工作流数据集的可复用框架研究
- 在线 Demo: [https://zie619.github.io/n8n-workflows](https://zie619.github.io/n8n-workflows) — GitHub Pages 托管的在线搜索界面

## 项目展示素材

### README 媒体
README 中未包含有价值的展示性图片或视频。所有图片均为：
- Badge/Shield 图标（n8n-Workflows、Workflows 4343+、Integrations 365+ 等）
- Buy Me a Coffee 按钮
- AI-BOM Logo 和 Mascot（关联项目推广素材，非本项目展示）
- GitHub 社交统计图标

### 筛选说明
- 总共发现 15+ 个媒体元素，筛选后保留 0 个
- 全部为 badge/CI 状态图标或外部项目推广素材，无 hero 图、架构图、Demo GIF 或功能截图
- 注：README 中的 Mermaid 架构图以代码形式存在，不是图片资源

## 快速判断
- 是否值得深入: **有条件**。如果你是 n8n 用户，这是目前最大的第三方工作流集合，有实用价值。但需注意 DMCA 风险和工作流质量参差不齐的问题。如果只是技术学习，项目本身的 FastAPI + SQLite FTS5 搜索架构也值得参考。
- 初步定位: **大众热门** — 10 个月内达到 53K stars，是 n8n 生态中增长最快的第三方项目
- 作者可信度: **中**，理由: 作者有工程背景且深耕 n8n 生态，但 README 中大量篇幅用于推广关联商业项目 AI-BOM（Trusera 公司），存在利用高流量仓库做商业推广的意图。DMCA 事件也说明早期采集方式存在合规风险。
- 竞品格局: **红海** — n8n 模板/工作流集合领域竞争激烈，已有多个万星级项目（enescingoz 20K+），n8n 官方也维护 8,800+ 模板库。但 Zie619 凭借规模优势（4,343 个工作流）和搜索体验在赛道中领先。
