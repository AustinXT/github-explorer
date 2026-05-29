# OpenClaw 仓库深度分析

> **仓库**: https://github.com/openclaw/openclaw
> **分析日期**: 2026-03-19
> **当前版本**: v2026.3.13-1 (2026-03-14)

---

## 1. 项目概述

**定位**: 开源的个人 AI Agent 助手，部署在用户自己的设备上，通过 25+ 消息平台（WhatsApp、Telegram、Slack、Discord、Signal、iMessage、微信等）统一交互，能执行浏览器操作、文件管理、定时任务等实际工作。

**口号**: "EXFOLIATE! EXFOLIATE!" 🦞

| 指标 | 数值 |
|------|------|
| Stars | 322,770 |
| Forks | 62,147 |
| Watchers | 1,580 |
| Open Issues | 8,512 |
| Open PRs | 6,136 |
| 磁盘占用 | ~309 MB |
| 创建时间 | 2025-11-24 |
| 最后推送 | 2026-03-18 |
| 许可证 | MIT |
| 官网 | https://openclaw.ai |
| 文档 | https://docs.openclaw.ai |
| Discord | https://discord.gg/clawd |

**现象级数据**: 仅 4 个月即达 322K Stars，打破 GitHub 历史纪录。

---

## 2. 语言与技术栈

### 语言分布

| 语言 | 代码量 (bytes) | 占比 |
|------|---------------|------|
| TypeScript | 41,503,955 | 87.9% |
| Swift | 3,604,234 | 7.6% |
| Kotlin | 831,052 | 1.8% |
| Shell | 514,068 | 1.1% |
| JavaScript | 384,864 | 0.8% |
| CSS | 214,605 | 0.5% |
| Go | 65,653 | 0.1% |
| Python | 61,664 | 0.1% |
| HTML | 35,727 | <0.1% |
| Dockerfile | 18,653 | <0.1% |
| PowerShell | 11,321 | <0.1% |
| Ruby | 9,865 | <0.1% |

### 工具链

| 类别 | 工具 |
|------|------|
| 运行时 | Node.js ≥22 |
| 包管理 | pnpm (monorepo workspaces) |
| 构建 | tsdown (esbuild)、Vite (UI) |
| 测试 | Vitest（9 套独立配置） |
| Lint | oxlint + ESLint + Prettier + ShellCheck + SwiftLint |
| 安全 | detect-secrets、pre-commit、zizmor (GHA 审计) |
| 重复检测 | jscpd |
| 死代码检测 | knip |
| 容器 | Docker + Docker Compose + Podman |
| CI/CD | GitHub Actions |
| 部署 | Fly.io、Render、Docker、Nix |

### TypeScript 配置

- `strict: true` — 严格模式
- `target: ES2023` — 现代 JS 特性
- `module: NodeNext` — ESM 原生模块
- `noEmitOnError: true` — 类型错误阻断编译

---

## 3. 仓库结构

### Monorepo Workspace 布局

```yaml
# pnpm-workspace.yaml
packages:
  - .              # 主包 (openclaw)
  - ui             # Control UI 前端
  - packages/*     # 独立 npm 包
  - extensions/*   # 70+ 渠道/功能扩展
```

### 目录全景

```
openclaw/
├── src/                        # 核心源码 (TypeScript)
│   ├── gateway/                # Gateway 控制平面（200+ 文件）
│   │   ├── server.ts           # WebSocket 服务器主入口
│   │   ├── server-methods.ts   # RPC 方法注册
│   │   ├── server-http.ts      # HTTP API 层
│   │   ├── server-channels.ts  # 渠道管理
│   │   ├── server-chat.ts      # 聊天会话处理
│   │   ├── server-cron.ts      # 定时任务
│   │   ├── server-plugins.ts   # 插件加载
│   │   ├── auth*.ts            # 认证/授权（15+ 文件）
│   │   ├── control-ui*.ts      # Control UI 服务
│   │   ├── openai-http.ts      # OpenAI 兼容 API
│   │   ├── hooks*.ts           # 钩子系统
│   │   └── origin-check.ts     # CSRF 防护
│   ├── agents/                 # Agent 运行时（500+ 文件）
│   │   ├── pi-embedded-runner.ts    # Pi Agent 嵌入式运行器
│   │   ├── pi-embedded-subscribe.ts # 流式订阅处理
│   │   ├── pi-tools.ts              # Agent 工具注册
│   │   ├── model-*.ts               # 模型管理（30+ 文件）
│   │   ├── auth-profiles*.ts        # 认证 profile 轮换
│   │   ├── subagent-*.ts            # 子 Agent 系统（30+ 文件）
│   │   ├── sandbox*.ts              # 沙箱隔离
│   │   ├── skills*.ts               # Skills 加载/安装
│   │   ├── compaction.ts            # 上下文压缩
│   │   ├── bash-tools*.ts           # Bash 执行工具
│   │   └── workspace*.ts            # 工作空间管理
│   ├── channels/               # 渠道抽象层
│   │   ├── registry.ts         # 渠道注册表
│   │   ├── session.ts          # 会话管理
│   │   ├── routing/            # 消息路由
│   │   ├── transport/          # 传输层
│   │   └── plugins/            # 渠道插件接口
│   ├── providers/              # 模型 Provider 适配
│   ├── cli/                    # CLI 命令
│   ├── config/                 # 配置管理
│   ├── plugin-sdk/             # 插件 SDK（60+ subpath exports）
│   ├── browser/                # 浏览器自动化
│   ├── canvas-host/            # Canvas 渲染
│   ├── memory/                 # 记忆系统
│   ├── tts/                    # 语音合成
│   ├── web-search/             # 网页搜索
│   ├── security/               # 安全模块
│   ├── cron/                   # 定时任务引擎
│   ├── hooks/                  # 钩子系统
│   ├── sessions/               # 会话持久化
│   ├── pairing/                # DM 配对
│   ├── wizard/                 # 安装向导
│   ├── i18n/                   # 国际化
│   ├── acp/                    # ACP 协议支持
│   ├── image-generation/       # 图像生成
│   ├── link-understanding/     # 链接理解
│   ├── media-understanding/    # 媒体理解
│   ├── media/                  # 媒体处理管线
│   ├── context-engine/         # 上下文引擎
│   ├── daemon/                 # 守护进程
│   ├── interactive/            # 交互式终端
│   ├── logging/                # 日志系统
│   ├── terminal/               # 终端 UI
│   ├── tui/                    # 文本用户界面
│   └── utils/                  # 工具函数
├── apps/                       # 原生客户端应用
│   ├── macos/                  # macOS 菜单栏应用 (Swift)
│   ├── ios/                    # iOS 应用 (Swift)
│   ├── android/                # Android 应用 (Kotlin)
│   └── shared/                 # 跨平台共享协议
├── extensions/                 # 70+ 扩展包
│   ├── [消息渠道]               # whatsapp, telegram, discord, slack, signal, ...
│   ├── [模型 Provider]          # anthropic, openai, google, ollama, ...
│   ├── [功能扩展]               # elevenlabs, memory-core, memory-lancedb, ...
│   └── shared/                 # 扩展共享代码
├── packages/                   # 独立 npm 包
│   ├── clawdbot/               # 历史兼容包
│   └── moltbot/                # 历史兼容包
├── skills/                     # 60+ 内置 Skills
├── ui/                         # Control UI (Vite + React)
│   ├── src/                    # 前端源码
│   ├── public/                 # 静态资源
│   └── vite.config.ts          # Vite 配置
├── docs/                       # 文档
├── test/                       # 集成/E2E 测试
├── test-fixtures/              # 测试固件
├── vendor/                     # 第三方代码
├── scripts/                    # 构建/部署脚本
├── patches/                    # pnpm patch 补丁
├── git-hooks/                  # Git 钩子
├── assets/                     # 静态资源/Logo
├── .github/                    # GitHub Actions CI
├── .agents/                    # AI Agent 配置
├── .agent/                     # Agent 工作目录
├── .pi/                        # Pi Agent 配置
├── Dockerfile                  # 主镜像
├── Dockerfile.sandbox          # 沙箱镜像
├── Dockerfile.sandbox-browser  # 浏览器沙箱镜像
├── Dockerfile.sandbox-common   # 沙箱基础镜像
├── docker-compose.yml          # Docker Compose 编排
├── fly.toml                    # Fly.io 部署配置
├── render.yaml                 # Render 部署配置
├── pnpm-workspace.yaml         # Monorepo workspace
├── tsconfig.json               # TypeScript 配置
├── tsdown.config.ts            # 构建配置
├── knip.config.ts              # 死代码检测
├── CLAUDE.md                   # Claude Code 指导文件
├── AGENTS.md                   # Agent 配置文档
├── VISION.md                   # 项目愿景
├── CONTRIBUTING.md             # 贡献指南
├── SECURITY.md                 # 安全策略
├── CHANGELOG.md                # 变更日志
└── package.json                # 主包配置 (v2026.3.14)
```

---

## 4. 架构分析

### 核心架构：Gateway 控制平面

```
消息平台 (25+ 渠道)
  WhatsApp / Telegram / Slack / Discord / Signal / iMessage / ...
               │
               ▼
┌─────────────────────────────────────┐
│          Gateway (控制平面)            │
│        ws://127.0.0.1:18789         │
│                                     │
│  ┌──────────┐  ┌─────────────────┐  │
│  │ HTTP API │  │  WebSocket API  │  │
│  │(REST/OpenAI│ │   (实时通信)     │  │
│  │ compat)  │  │                 │  │
│  └────┬─────┘  └───────┬─────────┘  │
│       │                │            │
│  ┌────▼────────────────▼─────────┐  │
│  │      Channel Router           │  │
│  │  (8 级匹配: peer→...→default)  │  │
│  └────────────┬──────────────────┘  │
│               │                     │
│  ┌────────────▼──────────────────┐  │
│  │    Session Manager            │  │
│  │  (main / group / subagent)    │  │
│  └────────────┬──────────────────┘  │
│               │                     │
│  ┌────────────▼──────────────────┐  │
│  │    Pi Agent Runtime (RPC)     │  │
│  │  - Tool streaming             │  │
│  │  - Block streaming            │  │
│  │  - Compaction                 │  │
│  │  - Model failover             │  │
│  └────────────┬──────────────────┘  │
│               │                     │
│  ┌────────────▼──────────────────┐  │
│  │  Tools / Skills / Extensions  │  │
│  │  Bash | Browser | Canvas |    │  │
│  │  Cron | Webhook | ...         │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌───────────────────────────────┐  │
│  │   Plugin SDK (60+ exports)    │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
         │           │           │
    ┌────▼───┐  ┌────▼───┐  ┌───▼────┐
    │ macOS  │  │  iOS   │  │Android │
    │  App   │  │ Node   │  │ Node   │
    │(Swift) │  │(Swift) │  │(Kotlin)│
    └────────┘  └────────┘  └────────┘
```

### 架构模式

| 模式 | 说明 |
|------|------|
| Gateway Pattern | 单一控制平面管理所有渠道和会话 |
| Plugin Architecture | 核心精简，能力通过 extensions/plugins/skills 三层扩展 |
| Multi-Agent Routing | 不同渠道/用户可路由到隔离的 Agent 工作空间 |
| Event-Driven | WebSocket 实时通信，事件驱动消息处理 |
| Monorepo Workspaces | pnpm workspace 管理多包 |
| Sandbox Isolation | Docker/Podman/SSH 多后端沙箱执行 |

### 关键设计决策

1. **Agent Runtime 内嵌 Gateway**: Pi Agent 以 RPC 模式嵌入 Gateway 进程，非独立微服务——对"个人助手"场景，简化胜过水平扩展
2. **渠道即扩展**: 每个消息平台作为独立 workspace 包（`extensions/`），可按需启用，渠道 A 的 bug 不影响渠道 B
3. **模型抽象统一**: 30+ provider 的统一接口，支持 failover chain + profile rotation + cooldown
4. **Session Key 8 级路由**: peer → parent → guild+roles → guild → team → account → channel → default，一个 Gateway 可运行多人格 Agent
5. **Lane-based 命令队列**: Main/Cron/Subagent/Nested 四个 lane，独立队列和可配置并发

---

## 5. 扩展生态全景

### 消息渠道扩展 (25+)

| 类别 | 渠道 |
|------|------|
| 即时通讯 | WhatsApp (Baileys)、Telegram (grammY)、Signal (signal-cli)、iMessage (BlueBubbles/legacy)、LINE、Zalo |
| 企业协作 | Slack (Bolt)、Discord (discord.js)、Microsoft Teams、Google Chat、Feishu (飞书)、Mattermost、Matrix |
| 其他 | IRC、Nostr、Synology Chat、Tlon、Twitch、Nextcloud Talk、WebChat |

### 模型 Provider 扩展 (30+)

| 类别 | Provider |
|------|----------|
| 主流 | Anthropic、OpenAI、Google (Gemini)、GitHub Copilot |
| 本地 | Ollama、vLLM、sglang |
| 云平台 | Amazon Bedrock、Azure (Microsoft)、NVIDIA |
| 聚合 | OpenRouter、Together、Chutes、Cloudflare AI Gateway、Vercel AI Gateway |
| 中国厂商 | Volcengine (火山引擎)、BytePlus、MiniMax、Moonshot、Qianfan (千帆)、Qwen Portal、ModelStudio、Xiaomi |
| 其他 | xAI、Venice、Mistral、Hugging Face、Perplexity、Kimi Coding |

### 内置 Skills (60+)

1password、Apple Notes、Apple Reminders、Bear Notes、BlogWatcher、BlueBubbles、Canvas、ClawHub、Coding Agent、Discord、GitHub、GitHub Issues、Gemini、GifGrep、GoPlaces、HealthCheck、Himalaya (Email)、iMessage、McPorter (MCP)、Model Usage、Nano PDF、Node Connect、Notion、Obsidian、OpenAI Image Gen、OpenAI Whisper、OpenHue、Oracle、Peekaboo、Session Logs、Sherpa ONNX TTS、Skill Creator、Slack、Spotify Player、Summarize、Things (macOS)、Tmux、Trello、Video Frames、Voice Call、Weather、xURL 等

---

## 6. 测试基础设施

### 9 套独立 Vitest 配置

| 配置 | 用途 |
|------|------|
| `vitest.unit.config.ts` | 单元测试 |
| `vitest.e2e.config.ts` | 端到端测试 |
| `vitest.channels.config.ts` | 渠道集成测试 |
| `vitest.gateway.config.ts` | Gateway 服务器测试 |
| `vitest.extensions.config.ts` | 扩展包测试 |
| `vitest.scoped-config.ts` | 作用域隔离测试 |
| `vitest.live.config.ts` | 在线 API 真实调用测试 |
| `vitest.config.ts` | 默认/全量测试 |
| `ui/vitest.config.ts` | Control UI 前端测试 |

### 测试密度

- `src/agents/` — 500+ 文件中约一半是 `.test.ts`，覆盖模型 failover、沙箱隔离、子 Agent 生命周期、Skills 安装等
- `src/gateway/` — 200+ 文件，大量 `server.*.test.ts` 覆盖认证、渠道、钩子、CSRF、角色策略等
- 命名规范严格：`*.test.ts` (单元)、`*.e2e.test.ts` (端到端)、`*.live.test.ts` (在线 API)、`*.contract.test.ts` (合约)

---

## 7. Docker 部署架构

### docker-compose.yml

```yaml
services:
  openclaw-gateway:
    image: ${OPENCLAW_IMAGE:-openclaw:local}
    ports:
      - "${OPENCLAW_GATEWAY_PORT:-18789}:18789"   # Gateway API
      - "${OPENCLAW_BRIDGE_PORT:-18790}:18790"     # Bridge
    volumes:
      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw
      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace
    restart: unless-stopped
    healthcheck:
      test: fetch('http://127.0.0.1:18789/healthz')
      interval: 30s
```

### 多 Dockerfile 策略

| Dockerfile | 用途 |
|-----------|------|
| `Dockerfile` | 主 Gateway 镜像 |
| `Dockerfile.sandbox` | Agent 代码执行沙箱 |
| `Dockerfile.sandbox-browser` | 浏览器自动化沙箱 |
| `Dockerfile.sandbox-common` | 沙箱基础层 |

---

## 8. 团队与治理

### 创始人

**Peter Steinberger** ([@steipete](https://github.com/steipete)) — PSPDFKit 创始人，iOS 生态知名人物，42K+ GitHub 粉丝。2026 年 2 月宣布加入 OpenAI，项目将移交开源基金会。

### 核心维护者 (16 人)

| 维护者 | GitHub | 负责领域 |
|--------|--------|---------|
| Peter Steinberger | @steipete | 核心架构、总决策 |
| Shadow | @thewilloftheshadow | Discord、社区管理、ClawHub |
| Vignesh | @vignesh07 | Memory (QMD)、TUI、IRC、Lobster |
| Jos | @joshp123 | Telegram、API、Nix |
| Ayaan Zaidi | @obviyus | Telegram、Android 应用 |
| Tyler Yust | @tyler6204 | Agents/subagents、cron、BlueBubbles、macOS |
| Mariano Belinky | @mbelinky | iOS 应用、安全 |
| Nimrod Gutman | @ngutman | iOS/macOS 应用 |
| Vincent Koc | @vincentkoc | Agents、遥测、Hooks、安全 |
| Val Alexander | @BunsDev | UI/UX、文档、Agent DevX |
| Seb Slight | @sebslight | 文档、Agent 可靠性、运行时加固 |
| Christoph Nakazawa | @cpojer | JS 基础设施 (前 Meta/Jest) |
| Gustavo Madeira | @gumadeiras | Multi-agents、CLI、性能、Plugins、Matrix |
| Onur Solmaz | @osolmaz | Agents、ACP、MS Teams |
| Josh Avant | @joshavant | Core、CLI、Gateway、安全 |
| Jonathan Taylor | @visionik | ACP、Gateway |

### Top 贡献者 (GitHub API)

steipete、vincentkoc、obviyus、vignesh07、gumadeiras、thewilloftheshadow、sebslight、Takhoffman、cpojer、shakkernerd、tyler6204、joshavant、mbelinky 等

### 赞助商

OpenAI、Vercel、Blacksmith、Convex

### 社区健康度

| 项 | 状态 |
|----|------|
| README | ✅ |
| License (MIT) | ✅ |
| Contributing Guide | ✅ |
| PR Template | ✅ |
| Code of Conduct | ❌ 缺失 |
| Issue Template | ❌ 缺失 |
| 健康评分 | 75/100 |

---

## 9. 近期活跃度

### 最新 10 次提交 (2026-03-18)

| SHA | 内容 |
|-----|------|
| `91d37cc` | fix(auth): lazy-load provider oauth helpers |
| `6ebcd85` | fix(plugin-sdk): isolate provider entry surfaces |
| `b526098` | docs: restore original Credits heading |
| `c749957` | docs: fix duplicate Credits heading |
| `e5a1185` | docs: add extensions section to docs hubs |
| `be3f4a7` | docs: add Building Extensions guide |
| `198de10` | docs: add missing H1 headings and fix HEARTBEAT template |
| `63e09f8` | chore(changelog): remove fragment workflow drift |
| `2797ae1` | docs: add missing voice-call CLI commands |
| `cc5bd57` | docs: add missing provider pages (google, modelstudio, perplexity, volcengine) |

### 近期版本

| 版本 | 日期 | 类型 |
|------|------|------|
| v2026.3.13-1 | 2026-03-14 | stable |
| v2026.3.13-beta.1 | 2026-03-14 | beta |
| v2026.3.12 | 2026-03-13 | stable |
| v2026.3.11 | 2026-03-12 | stable |
| v2026.3.11-beta.1 | 2026-03-12 | beta |

**发布频率**: 几乎每日一版，CalVer 日期版本 (`vYYYY.M.DD`)

### 热门 Open Issues

| # | Issue | 评论 | 主题 |
|---|-------|------|------|
| #29793 | 并发工作空间锁 | 119 | 多 Agent 共享工作空间互斥 |
| #38161 | postHookActions 机制 | 54 | Hook 系统增强 |
| #39207 | before_response_emit hook | 47 | 输出策略/人类监督 |
| #30185 | 自适应模型路由 | 17 | 按任务自动选择最优模型 |
| #43961 | SIGKILL 僵尸进程 | 10 | 优雅关闭超时后强制终止 |
| #43497 | 子 Agent 恢复 | 6 | Gateway 重启后恢复 subagent |

---

## 10. 安全设计

### 安全默认值

| 机制 | 说明 |
|------|------|
| DM Pairing | 未知发送者需配对码验证 |
| Origin Check | WebSocket CSRF 防护 (GHSA-5wcw-8jjv-m286) |
| Sandbox | Docker/Podman 沙箱隔离代码执行 |
| Token Auth | Gateway 支持 token + 密码认证 |
| Rate Limiting | 控制平面速率限制 |
| Secrets Detection | detect-secrets + pre-commit |
| GHA Audit | zizmor GitHub Actions 安全审计 |

### 已知风险

- Cisco 研究发现 26% 社区 Skills 含漏洞（数据窃取、提示注入）
- 连接真实消息平台时配置错误可暴露敏感数据
- 建议运行 `openclaw doctor` 检查安全配置

---

## 11. 项目演进时间线

```
2025-11   Warelay (原型阶段)
    ↓
2025-12   Clawdbot (首次公开)
    ↓
2026-01   Moltbot (改名，突破 100K Stars)
    ↓
2026-02   OpenClaw (最终定名，突破 250K Stars)
           - OpenAI/Meta 据传有收购意向
           - steipete 宣布加入 OpenAI
    ↓
2026-03   322K Stars，v2026.3.13-1 (当前)
           - 日均发布，16 名核心维护者
```

---

## 12. 竞品对比

| 特性 | OpenClaw | Claude Code | Perplexity Computer | Eigent | Agno |
|------|----------|-------------|-------------------|--------|------|
| 定位 | 全渠道 AI Agent | 代码终端助手 | 桌面 Agent | 多 Agent 桌面 AI | 轻量 Agent 框架 |
| 开源 | ✅ MIT | ❌ | ❌ | ❌ | ✅ |
| 消息渠道 | 25+ | 无 | 无 | 无 | 无 |
| 模型支持 | 30+ providers | Claude only | 多模型 | 多模型 | 多模型 |
| 配置复杂度 | 极高 | 低 | 低 | 中 | 低 |
| 隐私 | 本地优先 | 云端 | 云端 | 本地 | 本地 |
| 语音/Canvas | ✅ | ❌ | ❌ | 部分 | ❌ |
| 移动应用 | iOS + Android | ❌ | ❌ | ❌ | ❌ |
| 目标用户 | 技术极客 | 开发者 | 普通用户 | 普通用户 | 开发者 |

---

## 13. 社区声量

### 国际

- **Lex Fridman Podcast** — 与创始人 Peter Steinberger 深度对谈
- **OpenAI、Vercel** 等知名公司赞助
- Hacker News 多次登顶

### 中文社区

- [虎嗅: 第一批玩OpenClaw的人，已经开始清醒了](https://m.huxiu.com/article/4839363.html) — 部署困难、API 月费数百美元
- [知乎: 国内办公场景实测体验](https://zhuanlan.zhihu.com/p/2014739266169758476) — "开发者的乐高积木盒"
- [腾讯云: "数字员工"能值多少钱](https://cloud.tencent.com/developer/article/2640500) — AI 可交付 43.5% 高价值任务
- 中文社区 29 个微信群，电商安装服务 198-566 元

### 知识平台

| 平台 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/openclaw/openclaw](https://deepwiki.com/openclaw/openclaw) |
| Zread.ai | [zread.ai/openclaw/openclaw](https://zread.ai/openclaw/openclaw) |
| 官方文档 | [docs.openclaw.ai](https://docs.openclaw.ai) |

---

## 14. 总结评价

### 优势

- **生态覆盖无人能及**: 25+ 消息渠道、30+ 模型 provider、60+ skills、70+ extensions
- **架构成熟**: Gateway 控制平面 + Plugin SDK 设计优雅，Session 8 级路由灵活强大
- **工程质量高**: TypeScript strict、9 套 Vitest 配置、多层 lint/安全工具链
- **社区强大**: 322K Stars、16 名核心维护者、OpenAI/Vercel 赞助
- **隐私优先**: 全部本地运行，无云端数据依赖
- **迭代极快**: 几乎每日发布

### 劣势

- **部署门槛极高**: Node ≥22 + 多步配置，新手 30 分钟起步
- **代码量庞大**: 41.5 MB TypeScript，维护理解成本高
- **API 成本**: 深度使用月费 $300-750
- **Issue 积压**: 8,512 open issues + 6,136 open PRs
- **创始人风险**: steipete 加入 OpenAI 后的治理延续性
- **品牌混乱**: 经历三次改名
- **缺少 Code of Conduct 和 Issue Template**

### 适用人群

| 推荐 | 不推荐 |
|------|--------|
| Node.js/TypeScript 开发者 | 非技术用户 |
| 隐私优先的技术用户 | 预算敏感者 |
| AI Agent 架构研究者 | 需要稳定生产环境的企业 |
| 全渠道 AI 助手极客 | 只需代码助手的开发者 (用 Claude Code) |

### 建议

1. 先在本地 Docker 中试玩，连接 Telegram 或 Discord 感受基本能力
2. 不要一上来就连接 WhatsApp/iMessage 等高隐私渠道
3. 关注安全配置，运行 `openclaw doctor` 检查策略
4. 学习其架构模式: Gateway 控制平面、Plugin SDK subpath exports、Model failover chain、Lane-based 并发
5. 关注 Skills 生态的早期机会 (ClawHub)
