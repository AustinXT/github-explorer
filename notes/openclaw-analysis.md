# [OpenClaw](https://github.com/openclaw/openclaw)

**🎯 一句话定位**

开源的个人 AI Agent 助手，部署在你自己的设备上，通过 20+ 消息平台（WhatsApp、Telegram、Slack、Discord、微信等）与你交互，能执行浏览器操作、文件管理、定时任务等实际工作，而不仅仅是对话。

⠀

**⚙️ 核心机制**

OpenClaw 的架构围绕一个本地运行的 **Gateway（控制平面）** 展开，通过 WebSocket（默认端口 18789）统一管理所有会话、渠道和工具调用：

1. **消息流入**：来自 25+ 消息平台的消息进入 Gateway
2. **路由分发**：Gateway 根据 `openclaw.json` 配置将消息路由到对应的 Agent 工作空间
3. **Agent 执行**：内嵌的 Pi Agent 运行时（RPC 模式）处理请求，可调用 bash、文件操作、浏览器控制、Canvas 渲染等工具
4. **响应回流**：结果通过原渠道返回用户

关键技术栈：TypeScript（主体 41.5M 行）、Swift（macOS/iOS 应用）、Kotlin（Android 应用）、Node ≥22、pnpm monorepo、Vite+React 前端、Docker 沙箱。支持 Claude、GPT、Gemini、本地模型等多模型切换和 failover。

⠀

**📊 项目健康度**

- **Stars**: 322,757  |  **Forks**: 62,141  |  **License**: MIT
- **团队/作者**: [Peter Steinberger](https://github.com/steipete)（核心作者，13,136 commits），组织 [openclaw](https://github.com/openclaw)。顶级贡献者还包括 Vincent Koc（905 commits）、obviyus（439）、vignesh07（437）等
- **Commit 趋势**: **极度活跃 — 快速成长期**。2025 年 11 月创建，仅 4 个月即达 322K Stars（打破 React 保持 10 年的 GitHub 记录）。2026-03-18 当天就有 15+ 次提交，涵盖 plugin-sdk、文档、测试、渠道修复等多个方向
- **最近动态**:
  - `fix(plugin-sdk): isolate provider entry surfaces` (2026-03-18)
  - `docs: add Building Extensions guide` (2026-03-18)
  - 安全修复：WebSocket origin validation，关闭 CSRF 劫持路径 (GHSA-5wcw-8jjv-m286, 2026-03-12)
  - Control UI/Dashboard v2 重构 (2026-03-13)
  - OpenAI GPT-5.4 fast mode 支持 (2026-03-13)
- **最新版本**: v2026.3.13-1 (2026-03-14)

⠀

**🔥 精选 Issue**

1. [#3460 Internationalization (i18n) & Localization Support](https://github.com/openclaw/openclaw/issues/3460) — 100+ 评论，社区热烈讨论多语言支持方案，已有贡献者提交了 9 语言 274 key 的完整 i18n 实现。核心争论点：是否接受第三方 i18n PR（维护方担心安全风险）

2. [#26534 Add DingTalk as a first-install channel option](https://github.com/openclaw/openclaw/issues/26534) — 73 评论，中国用户强烈要求支持钉钉渠道，反映了 OpenClaw 在中国的巨大热度和本地化需求

3. [#32828 False 'API rate limit reached' on all models](https://github.com/openclaw/openclaw/issues/32828) — 56 评论，大量用户报告误报速率限制问题，暴露了模型 failover 机制的 bug，现已修复

4. [#75 Linux/Windows Clawdbot Apps](https://github.com/openclaw/openclaw/issues/75) — 由创始人 steipete 发起的早期 Issue，41 评论，社区持续呼吁原生桌面应用从 macOS 扩展到 Linux/Windows

5. [#8650 Switch Built-in Feishu Plugin](https://github.com/openclaw/openclaw/issues/8650) — 69 评论，飞书频道插件的替换讨论，反映企业用户对中国办公平台集成的强烈需求

⠀

**✅ 适用场景**

- **个人自动化枢纽**：将 AI Agent 接入你日常使用的所有消息平台，统一管理
- **开发者工具链**：浏览器自动化、代码执行、定时任务、Webhook 触发
- **隐私优先场景**：所有数据本地存储（Markdown 文件 + JSONL 会话），无云端依赖
- **多 Agent 路由**：为不同渠道/用户配置隔离的 Agent 工作空间
- **技术极客的 AI 玩具**：60+ 扩展、50+ 内置 Skills、Plugin SDK 提供无限可能

⠀

**⚠️ 局限**

- **部署门槛极高**：需要 Node ≥22 环境、多步配置、频繁的版本更新，故障修复常需 30 分钟以上
- **安全风险**：Cisco 研究发现 26% 的社区 Skills 含漏洞；连接真实消息平台时配置错误可暴露敏感数据
- **API 成本不可控**：深度使用时月费 $300-750（取决于模型和用量），非免费午餐
- **能力上限取决于底层模型**：复杂上下文容易崩溃，AI 幻觉可能导致自动化错误
- **无法实时中断任务**，执行过程黑盒
- **品牌混乱**：从 Clawdbot → Moltbot → OpenClaw 两次改名，早期文档和社区讨论分散

⠀

**🆚 竞品对比**

- **vs [Claude Code](https://claude.ai)** — Claude Code 专注代码编辑和终端操作，开箱即用；OpenClaw 覆盖面更广（消息平台 + 浏览器 + 语音 + Canvas），但配置复杂度高出一个数量级
- **vs [Perplexity Computer](https://www.perplexity.ai/)** — Perplexity 提供简洁的桌面 Agent 体验；OpenClaw 更强大但需要更多技术投入。X 用户 [@jspeiser](https://x.com/jspeiser/status/2032885815538254030) 评价："OpenClaw 最强但需要技术背景和大量时间"
- **vs [Eigent](https://www.eigent.ai/)** — Eigent 强调多 Agent 桌面 AI 和图形界面；OpenClaw 胜在开源和渠道覆盖
- **vs [Agno](https://github.com/agno-agi/agno)** — Agno 定位轻量级 Agent 框架，适合嫌 OpenClaw 太臃肿的开发者
- **vs 国内方案（[实在 Agent](https://www.shizhi.cn/)、[钉钉悟空](https://www.dingtalk.com/)）** — 国内方案开箱即用、无需部署，适合非技术用户；OpenClaw 是"乐高积木盒"，灵活但需要自己搭建

⠀

**🌐 知识图谱**

- **DeepWiki**: [deepwiki.com/openclaw/openclaw](https://deepwiki.com/openclaw/openclaw) — 已收录，含架构图、组件分析和部署模型详解
- **Zread.ai**: [zread.ai/openclaw/openclaw](https://zread.ai/openclaw/openclaw) — 已收录，含技术栈概览和安装指南

⠀

**🎬 Demo**

- 官方 WebChat：通过 Gateway 内置的 Control UI 即可体验
- 在线体验需自行部署，无公开 hosted demo

⠀

**📄 关联论文**

- [MetaClaw](https://x.com/bowang87/status/2031094971630235941) — 首个基于 RL 的 OpenClaw 增强研究，让 Agent 通过对话自动进化，由 Bo Wang 发布

⠀

**📰 社区声量**

**X/Twitter**

- [@lexfridman](https://x.com/lexfridman/status/2021785659644453136): Lex Fridman 与创始人 Peter Steinberger 进行了深度对谈，称之为"truly mind-blowing, inspiring, and fun conversation"，180K+ Stars 时的采访
- [@atla\_](https://x.com/atla_/status/2021836512975843785): "3+ 小时的深度技术讨论，涵盖 OpenAI 和 Meta 的收购要约、AI Agent 的未来方向"
- [@sam_starkman](https://x.com/sam_starkman/status/2023408371685065199): 声称 OpenAI 已收购 OpenClaw，自己用 $30/月的 GCP 虚拟机运行个人 Agent 管理内容管线和自动交易
- [@jspeiser](https://x.com/jspeiser/status/2032885815538254030): 横评 OpenClaw、Perplexity Computer、Claude Cowork 三款 Agent——"OpenClaw 最强但需要技术背景和大量时间"
- [@milesdeutscher](https://x.com/milesdeutscher/status/2022230772967719252): 直言找到了比 OpenClaw 更好的替代品——"更容易设置、更便宜、更安全"

⠀

**中文社区**

- [虎嗅: 第一批玩OpenClaw的人，已经开始清醒了](https://m.huxiu.com/article/4839363.html) — GitHub 突破 250K Star，但早期用户发现部署困难、API 月费数百美元、上下文崩溃等问题。电商安装服务卖到 198-566 元，中文社区 29 个微信群
- [知乎: 最近爆火的OpenClaw到底好不好用？国内办公场景实测体验](https://zhuanlan.zhihu.com/p/2014739266169758476) — 核心结论："OpenClaw 是给开发者的'乐高积木盒'，实在 Agent 是给普通用户和企业的'成品家电'"
- [腾讯云: "数字员工"OpenClaw 能值多少钱？](https://cloud.tencent.com/developer/article/2640500) — 评测显示 AI 在金融、法律、医疗等领域可稳定交付 43.5% 高价值任务，成本仅 $100 vs 专家级 $480K
- [CSDN/GitCode: OpenClaw 多模型深度测评](https://gitcode.csdn.net/69b8d1f754b52172bc61fbe7.html) — 从效果、费用与场景三个维度详细对比不同模型下的表现
- [凤凰网: OpenClaw 揭开了一场关于 AI 主权的范式革命](https://i.ifeng.com/c/8rIq6JjWihY) — 指出 OpenClaw 的三类商业机会：垂直领域 Agent（法律/医疗/教育）
- [博客园: 装完OpenClaw之后，我把它变成了办公助手](https://www.cnblogs.com/informatics/p/19679940) — 一个月实测报告，提醒"AI 会犯错且很自信，数字/人名/日期必须核实"

⠀

**💬 我的判断**

OpenClaw 是 2025-2026 年开源 AI Agent 领域的现象级项目——4 个月 322K Stars，打破 GitHub 历史记录。它的野心极大：试图成为跨所有消息平台的统一 AI 助手入口，并且确实做到了技术上的广度覆盖（25+ 渠道、60+ 扩展、语音/Canvas/浏览器控制）。

**值得投入时间的人**：有 Node.js/TypeScript 基础的开发者、想要完全掌控数据隐私的技术用户、对 AI Agent 架构感兴趣的研究者。

**不建议的人**：非技术用户（部署门槛太高）、预算敏感者（API 月费数百美元）、需要稳定生产环境的企业（版本迭代过快、安全风险仍在收敛中）。

**建议用法**：
1. 先在本地 Docker 中试玩，连接 Telegram 或 Discord 感受基本能力
2. 不要一上来就连接 WhatsApp/iMessage 等高隐私渠道
3. 关注安全配置，运行 `openclaw doctor` 检查策略
4. 如果只需要代码助手，Claude Code 性价比更高；如果需要全渠道 Agent，OpenClaw 是目前最强的开源选择
