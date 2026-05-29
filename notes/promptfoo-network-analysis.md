# Promptfoo 网络分析报告

> 分析对象：[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
> 分析时间：2026-04-06

## 仓库基本数据

- Star / Fork / Watcher: 19,575 / 1,679 / 49
- 语言: TypeScript（主，22.3MB）、CSS（506KB）、Python（52KB）、JavaScript（170KB）、Go（8KB）、Shell、Ruby、MDX、Dockerfile 等
- License: MIT
- 创建时间: 2023-04-28 | 最近推送: 2026-04-06
- 话题标签: llm, prompt-engineering, prompts, llmops, prompt-testing, testing, rag, evaluation, evaluation-framework, llm-eval, llm-evaluation, ci, ci-cd, cicd, pentesting, red-teaming, vulnerability-scanners
- 已归档: 否 | 是Fork: 否
- 主页: https://promptfoo.dev
- 磁盘用量: 556MB

## 作者画像

- 姓名/ID: promptfoo（组织账号）| 公司: promptfoo Inc.（已被 OpenAI 收购）| 位置: 美国旧金山湾区
- 创始人: Ian Webster（CEO）—— 前 Discord LLM 工程负责人，曾将 AI 产品扩展至 2 亿用户；更早曾任 Smile ID VP of Engineering & Head of ML
- 联合创始人: Michael D'Angelo（mldangelo，第二大贡献者，2116 次提交）
- 粉丝: 319 | 公开仓库: 20 | 组织账号年龄: ~3 年（2023-06-27 创建）
- 此 repo 投入权重: 极高——组织 20 个仓库中 promptfoo 占绝对核心（19,575 stars），其余均为辅助项目
- 作者类型: 创业公司→被巨头收购的典型路径。从开源 CLI 工具起步，逐步构建企业级 AI 安全平台
- 贡献集中度:
  - typpo（Ian Webster）: 2809 次提交（36.5%）
  - mldangelo: 2116 次提交（27.5%）
  - 两位创始人合计占比 64%，是核心驱动
  - 社区贡献者 sklein12（321）、will-holley（204）、MrFlounder（190）、faizanminhas（181）等贡献可观
  - 机器人（renovate/dependabot/gru-agent）合计 1177 次提交
- 背景推断: 团队具备大型互联网公司 AI 工程经验（Discord）、机器学习工程（Smile ID）、安全领域背景。a16z 投资背景，2026 年 3 月被 OpenAI 收购，团队加入 OpenAI

### 组织仓库生态

| 仓库 | Stars | 说明 |
|------|-------|------|
| promptfoo | 19,575 | 核心 CLI + Web UI |
| promptfoo-action | 59 | GitHub Action 集成 |
| modelaudit | 40 | 模型安全审计工具 |
| evil-mcp-server | 28 | MCP 安全测试服务器 |
| crabcode | 18 | Shell 工具 |
| mcp-agent-provider | 5 | MCP Agent Provider |
| js-rouge | 3 | JS ROUGE 指标库 |
| example-app / demo-app | 2 | 示例应用 |
| promptfoo-python | 1 | Python 绑定 |

## 社区热度

- 热度级别: **S 级（顶流）**——近 2 万 Stars，1,679 Forks，被 OpenAI 收购
- 增长模式: **持续加速型**

| 里程碑 | 时间 | 累计 Stars | 增长速率 |
|--------|------|-----------|---------|
| 第 200 | 2023-05-15 | ~200 | 17 天（启动期爆发） |
| 第 1,000 | 2023-09-13 | ~1,000 | ~4 个月 |
| 第 2,500 | 2024-04-19 | ~2,500 | ~7 个月 |
| 第 7,500 | 2025-07-12 | ~7,500 | ~15 个月 |
| 第 12,500 | 2026-03-11 | ~12,500 | ~8 个月（收购消息推动） |
| 第 17,500 | 2026-03-18 | ~17,500 | ~1 周（收购引爆） |
| 第 19,000 | 2026-03-31 | ~19,000 | ~2 周（持续增长） |

- 近期趋势: 2026 年 3 月 OpenAI 收购公告后，一周内新增约 5,000 Stars，增长曲线出现明显「收购跳」。之后增速回归平稳
- 套利判断: **高确定性标的**——已被 OpenAI 收购验证。开源项目保持 MIT 协议，有 Fortune 500 中 25% 的企业客户基础，社区活跃度极高

## 生态网络

### 上游依赖
- **LLM API**: OpenAI SDK、Anthropic SDK、AWS SDK（Bedrock）等数十家 Provider 集成
- **Web 框架**: Express + Socket.IO（实时通信）
- **数据库**: better-sqlite3 + Drizzle ORM
- **前端**: React 18 + Vite + Zustand + MUI
- **配置/验证**: Zod、JS-YAML、AJV
- **文档**: Docusaurus

### 同类项目（LLM 评估/测试领域）

| 项目 | Stars | 语言 | 定位差异 |
|------|-------|------|---------|
| evidentlyai/evidently | 7,374 | Python/Jupyter | ML 可观测性，偏向数据监控 |
| DeepEval (confident-ai) | ~5,000+ | Python | pytest 风格 LLM 测试 |
| Langfuse | ~6,000+ | TypeScript | LLM 可观测性 + 追踪 |
| RAGAS | ~8,000+ | Python | 专注 RAG 管道评估 |
| Arize AI Phoenix | ~4,000+ | Python | ML 可观测性平台 |
| LangSmith (LangChain) | 商业产品 | - | LangChain 生态原生追踪 |

**promptfoo 的差异化**：唯一同时覆盖「评估 + 红队安全测试」的工具，且是 TypeScript/Node 生态中最成熟的选择。

## 官方文档洞察

- 价值主张: 「Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI」——一站式 LLM 评估 + AI 安全测试
- 目标用户: LLM 应用开发者、AI 安全工程师、DevOps/CI-CD 集成者、企业合规团队
- 差异化叙事:
  - **开发者优先**: 命令行驱动，支持 live reload 和缓存，无需 SDK/云依赖/登录
  - **隐私**: 评估 100% 本地运行，数据不离开用户机器
  - **实战验证**: 被 OpenAI 和 Anthropic 使用，支撑服务千万级用户的生产应用
  - **红队安全**: 超越简单评估，提供 AI 应用的渗透测试和漏洞扫描
- 设计哲学: 声明式配置（YAML）而非代码驱动，降低使用门槛；插件式 Provider 架构支持任意 LLM API
- 外部深度视角:
  - LinkedIn 用户评价：「invaluable for testing prompts across models... but UI is terrible, not production grade」——功能强但 UI 有待改进
  - 学术界在 arXiv 多篇论文引用 promptfoo，涵盖 LLM 安全、漏洞扫描、回归测试、prompt 优化等领域
  - 收购后外部评价积极，认为 OpenAI 获得了 Fortune 500 中 25% 的企业客户渠道

## 竞品清单

| 竞品 | 定位 | 与 promptfoo 差异 |
|------|------|------------------|
| **DeepEval** (confident-ai) | Python 生态 LLM 测试框架 | pytest 风格，偏评估，无红队功能 |
| **Langfuse** | LLM 可观测性 + 追踪 | 偏生产监控，非安全测试 |
| **RAGAS** | RAG 管道评估 | 专注 RAG 质量指标，不涉及安全 |
| **Arize AI Phoenix** | ML 可观测性 | 偏数据/模型监控 |
| **LangSmith** | LangChain 生态追踪 | 绑定 LangChain，闭源商业产品 |
| **Braintrust** | Prompt 评估 SaaS | 纯 SaaS，无本地 CLI |
| **MLflow** | 实验追踪 + 模型注册 | 通用 ML 平台，非 LLM 专用 |
| **Garak** (NVIDIA) | LLM 漏洞扫描 | 侧重安全审计，评估功能弱 |

**竞品格局总结**: promptfoo 在「评估 + 安全」双赛道上几乎无直接竞品。评估赛道有 DeepEval/RAGAS/Langfuse 等，安全赛道有 Garak，但两者结合的只有 promptfoo。

## 关键 Issue 信号

1. [#657 How to detect bias and fairness](https://github.com/promptfoo/promptfoo/issues/657) — 19 条评论，用户对偏见检测能力有强烈需求，反映安全测试场景的深度
2. [#1876 Google provider fails when using gemini 1.5 flash](https://github.com/promptfoo/promptfoo/issues/1876) — 19 条评论，Provider 兼容性是核心痛点
3. [#1873 Evals Page Empty v0.92.3](https://github.com/promptfoo/promptfoo/issues/1873) — 18 条评论，Web UI 稳定性问题
4. [#412 The dockerfile for sharing seems to be missing files](https://github.com/promptfoo/promptfoo/issues/412) — 17 条评论，部署/分享功能的需求
5. [#1611 Self-host at a custom subpath](https://github.com/promptfoo/promptfoo/issues/1611) — 13 条评论，Feature Request，企业自托管需求
6. [#1252 Install promptfoo on kubernetes](https://github.com/promptfoo/promptfoo/issues/1252) — 13 条评论，企业级部署需求

**Issue 特征**: 以 Provider 兼容性、部署问题、Web UI 稳定性为主，Feature Request 占比高，说明用户群体在向企业级场景扩展。

## 知识入口

- DeepWiki: [deepwiki.com/promptfoo/promptfoo](https://deepwiki.com/promptfoo/promptfoo) — 架构全景图，含 Monorepo 结构、评估引擎、Provider 系统、Red Team 系统、Web UI 等模块详解
- 关联论文:
  - [Insights and Current Gaps in Open-Source LLM Vulnerability Scanning Tools](https://arxiv.org/html/2410.16527v2) — 将 promptfoo 作为主要研究对象
  - [Automatic Test Generation for Language Model Prompts](https://arxiv.org/pdf/2503.05070) — 引用 promptfoo 的 assertion 机制
  - [Interactive Tool for Regression Testing Guided LLM Migration](https://arxiv.org/html/2409.03928v1) — 使用 promptfoo 进行 LLM 迁移回归测试
  - [Challenges in Testing Large Language Model Based Software](https://arxiv.org/html/2503.00481v2) — 学术界对 promptfoo 的分析
- 在线 Demo: https://promptfoo.dev（官网含交互式演示）
- 收购公告: [OpenAI to acquire Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/)（2026-03-09）

## 项目展示素材

### README 媒体

1. ![prompt evaluation matrix - web viewer](https://raw.githubusercontent.com/promptfoo/promptfoo/main/site/static/img/claude-vs-gpt-example@2x.png) — 类型: hero/demo — 展示多模型对比评估矩阵
2. ![promptfoo command line demo](https://www.promptfoo.dev/img/docs/self-grading.gif) — 类型: demo — CLI 自动评分工作流
3. ![gen ai red team dashboard](https://www.promptfoo.dev/img/redteam-dashboard@2x.jpg) — 类型: demo — 红队安全测试报告界面

### 筛选说明

- 总共发现 6 个媒体元素（3 张图片 + 1 个 GIF + 2 个 badge 类图标）
- 排除 2 个 badge/shield 图标（npm version、GitHub Actions status）
- 保留 3 个有展示价值的媒体

## 快速判断

- **是否值得深入**: **极高价值**——已被 OpenAI 收购的开源 AI 安全工具，技术架构成熟（TypeScript Monorepo + SQLite + React），社区活跃，学术引用丰富。适合作为 LLM 评估/安全领域的标杆项目深入研究
- **初步定位**: AI 安全基础设施层——从 prompt 评估工具演化为 LLM 应用安全平台，覆盖评估、红队、漏洞扫描三大场景
- **作者可信度**: **极高**——创始人 Ian Webster 有 Discord（200M+ 用户 AI 产品）和 Smile ID（VP Eng + ML 负责人）背景；a16z 投资；被 OpenAI 收购。项目被 OpenAI 和 Anthropic 官方使用
- **竞品格局**: promptfoo 在「评估 + 安全」交叉领域处于近乎垄断地位。评估赛道竞品多但无安全能力，安全赛道（Garak）缺乏评估功能。OpenAI 收购后生态优势进一步扩大
