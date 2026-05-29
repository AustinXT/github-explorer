# openai/skills 网络分析报告

> 分析时间：2026-03-22
> 仓库地址：https://github.com/openai/skills

## 仓库基本数据
- Star / Fork / Watcher: 14,835 / 865 / 91
- 语言: Python (73.1%), JavaScript (21.5%), Shell (2.3%), Jupyter Notebook (1.1%), Swift (1.0%), PowerShell (1.0%)
- License: 无统一 License（各 skill 目录内有独立 LICENSE.txt）
- 创建时间: 2025-11-25 | 最近推送: 2026-03-20
- 话题标签: 无（repositoryTopics 为 null）
- 已归档: 否 | 是Fork: 否
- 磁盘占用: ~1.9 MB
- 默认分支: main
- Open Issues: 37 | Open PRs: 112
- 项目存活时长: ~4 个月，持续活跃

## 作者画像
- 姓名/ID: OpenAI | 公司: - | 位置: -
- 官网: https://openai.com/
- 粉丝: 115,867 | 公开仓库: 234 | 账号年龄: 10.5 年
- 此 repo 投入权重: **中**（OpenAI 当前重心在 codex 主仓库 66.7k Star，skills 是其配套生态仓库）
- 作者类型: 顶级 AI 公司/开源组织
- 贡献集中度: **公司主导**（87% 贡献来自 -openai/-oai 后缀账号，23 位贡献者中前 3 人占 51%）
- 核心贡献者: gverma-openai (17), dkundel-openai (13), vb-openai (12), edward-bayes (7)
- 背景推断: OpenAI 为其 Codex 产品线（AI 编程代理）打造的官方技能目录。由 OpenAI 内部团队维护，社区贡献主要以 PR 提交实验性 skill 为主。该仓库是 Codex 生态的核心配套设施，对标 Anthropic 发起的 Agent Skills 开放标准。

## 社区热度
- 热度级别: **大众热门**（14.8k Star，4 个月内达成，增速极快）
- 增长模式: **爆发型**（因 OpenAI 品牌效应和 Codex 产品发布带来的集中关注）
- 近期趋势: 仓库 2 天前仍有推送，PR 活跃（112 个 PR，大量社区提交的 skill），持续有新 skill 加入（前端设计、Sora 视频、Playwright 交互等）
- 套利判断: **低套利空间**。Star 增长主要由 OpenAI 品牌背书驱动，属于平台生态配套仓库，非独立开源项目。关注度与 Codex 产品线命运绑定。
- 注：因 GitHub API 速率限制，未能获取完整 stargazer 时间序列

## 生态网络
- 上游依赖: OpenAI Codex（AI 编程代理平台）、Agent Skills 开放标准（agentskills.io，由 Anthropic 发起）
- 下游消费者: Codex 用户、ChatGPT 企业用户（Skills 功能已进入 ChatGPT 测试）
- 同类项目（竞品/互补）:
  | 项目 | Star | 定位 |
  |------|------|------|
  | affaan-m/everything-claude-code | 93,791 | Claude Code 性能优化系统，含 skills/instincts/memory |
  | sickn33/antigravity-awesome-skills | 26,351 | 1,304+ 跨平台 agent skills 集合 |
  | kepano/obsidian-skills | 15,403 | Obsidian 专用 agent skills |
  | coreyhaines31/marketingskills | 15,256 | 营销领域 Claude Code skills |
  | VoltAgent/awesome-agent-skills | 12,224 | 500+ 社区 agent skills 合集 |
  | refly-ai/refly | 7,042 | 开源 agent skills 构建器 |
- 标准生态: Agent Skills 开放标准已被 30+ 工具/平台采纳，包括 Claude Code、Cursor、VS Code Copilot、Gemini CLI、GitHub Copilot、JetBrains Junie、Databricks、Snowflake 等

## 官方文档洞察
- 价值主张: "Skills 让 agent 获得按需加载的过程性知识，扩展其能力边界"——一次编写、跨平台复用的 AI 代理能力包
- 目标用户: (1) 使用 Codex 的开发团队，(2) 希望标准化工作流的企业，(3) 构建可复用能力库的个人开发者
- 差异化叙事: 区别于 MCP（侧重数据/工具访问），Skills 侧重**工作流和能力**——是"怎么做"而非"用什么做"
- 设计哲学: 渐进式上下文加载（Progressive Disclosure）、偏好指令而非脚本、单一职责、符号链接支持开发便利
- 技术路线图: 无明确公开路线图，但方向信号包括：MCP 服务器集成、UI 可视化编辑器（拖拽构建 skill）、ChatGPT 内集成、API 层面支持 skills
- 外部深度视角:
  - Simon Willison 关注到 OpenAI 悄然采用 skills 标准，已进入 ChatGPT 和 Codex CLI
  - vibecoding.app 评价：35 个 curated skills 覆盖主流开发工作流，安装体验一键式，开放标准消除锁定风险
  - 媒体报道 OpenAI 内部代号 "Hazelnut"，Skills 功能可组合、可移植，支持代码片段
  - SkillsMP 市场已聚合 66,500+ agent skills，形成生态

## 竞品清单
| 竞品 | 类型 | Star | 关系 |
|------|------|------|------|
| anthropics/skills | 标准发起方 | - | Agent Skills 标准由 Anthropic 发起，OpenAI 跟进采纳 |
| everything-claude-code | 综合框架 | 93.8k | 包含 skills 但定位更广（instincts, memory, security） |
| antigravity-awesome-skills | Skills 合集 | 26.4k | 跨平台 skill 聚合库，兼容 Codex |
| obsidian-skills | 垂直领域 | 15.4k | Obsidian 专用，非通用竞品 |
| awesome-agent-skills | Skills 合集 | 12.2k | 社区驱动的 skill 目录 |
| refly-ai/refly | 构建工具 | 7.0k | skill 创建工具，互补关系 |
| Cursor Rules | 配置文件 | - | 类似机制但非标准化 skill |

## 关键 Issue 信号
| # | 标题 | 评论 | 状态 | 信号 |
|---|------|------|------|------|
| #36 | Add frontend-design skill | 15 | closed | 社区积极贡献高质量 skill，已合并 |
| #133 | "you can just build things" | 8 | closed | 展示性 skill，体现 Codex 综合能力 |
| #252 | add postman-json | 6 | closed | API 测试工具集成需求 |
| #255 | feat: add skill postman-json | 3 | closed | 同上需求的迭代 PR |
| #172 | add auto memory | 3 | closed | agent 记忆能力扩展 |
| #266 | slides: improve Windows rendering | 1 | open | 跨平台兼容性改进 |
| #243 | Add webpilot skill — CDP-free browser automation | 0 | open | 浏览器自动化需求 |
| #136 | fix(gh-address-comments) | 0 | open | 已有 skill 的 bug 修复 |

**Issue 信号解读**: PR 活跃度远高于 Issue（112 PR vs 37 Issue），说明社区参与方式以贡献新 skill 为主。高评论 PR 多为新 skill 的审核讨论，体现了策展（curation）流程。

## 知识入口
- DeepWiki: https://deepwiki.com/openai/skills — **已收录**，包含完整架构文档、skill 分层说明、安装指南、20+ 个 skill 详解
- Zread.ai: https://zread.ai/openai/skills — **已收录**，含概览、三层 skill 体系、渐进式发现机制
- 关联论文: 未发现直接关联的 arxiv 论文
- 在线 Demo: Codex 应用本身即为 skill 的运行环境（需 OpenAI 账号）；OpenAI 开发者文档提供 cookbook 示例
- 官方开发者文档: https://developers.openai.com/codex/skills
- Agent Skills 开放标准: https://agentskills.io
- OpenAI 开发者博客: https://developers.openai.com/blog/eval-skills（skill 测试与评估）

## 项目展示素材
- README 中无展示性图片（无截图、无架构图、无 badge 以外的视觉素材）
- 项目展示依赖 Codex 产品界面和官方文档站点
- 35 个 curated skills 目录本身即为展示素材：aspnet-core, chatgpt-apps, cloudflare-deploy, develop-web-game, doc, figma, figma-implement-design, frontend-skill, gh-address-comments, gh-fix-ci, imagegen, jupyter-notebook, linear, netlify-deploy, notion-* (4个), openai-docs, pdf, playwright, playwright-interactive, render-deploy, screenshot, security-* (3个), sentry, slides, sora, speech, spreadsheet, transcribe, vercel-deploy, winui-app, yeet
- 3 个 system skills：openai-docs, skill-creator, skill-installer

## 快速判断
- **是否值得深入**: **是**——作为 Agent Skills 开放标准的官方参考实现和 OpenAI Codex 的核心配套，具有行业标准定义级别的重要性
- **初步定位**: OpenAI Codex 产品线的官方技能目录，同时是 Agent Skills 开放标准的关键实现。不是独立工具，而是平台生态基础设施
- **作者可信度**: **极高**——OpenAI 是全球顶级 AI 公司，115k followers，10 年 GitHub 历史，Codex 主仓库 66.7k Star
- **竞品格局**: Agent Skills 已成为事实上的跨平台标准（30+ 工具采纳），openai/skills 是官方 catalog 之一。竞争不在仓库层面，而在标准生态的主导权层面（Anthropic 发起标准 vs OpenAI 跟进采纳并做大生态）。社区已涌现大量 awesome-skills 聚合项目（最高 93.8k Star），说明 skill 概念已突破单一平台

---

Sources:
- [Agent Skills – Codex | OpenAI Developers](https://developers.openai.com/codex/skills)
- [OpenAI Codex Skills Catalog Review](https://vibecoding.app/blog/openai-skills-review)
- [OpenAI are quietly adopting skills - Simon Willison](https://simonw.substack.com/p/openai-are-quietly-adopting-skills)
- [Agent Skills Open Standard](https://agentskills.io)
- [DeepWiki - openai/skills](https://deepwiki.com/openai/skills)
- [Zread.ai - openai/skills](https://zread.ai/openai/skills)
- [Testing Agent Skills with Evals | OpenAI Developers](https://developers.openai.com/blog/eval-skills)
- [Skills in OpenAI API - Cookbook](https://developers.openai.com/cookbook/examples/skills_in_api)
- [ChatGPT Skills Internal Testing - Legal IT Insider](https://legaltechnology.com/2026/02/12/openai-performs-early-testing-of-skills-in-chatgpt/)
- [ChatGPT Skills Launch Info](https://news.aibase.com/news/24035)
- [SkillsMP Marketplace Guide](https://smartscope.blog/en/blog/skillsmp-marketplace-guide/)
