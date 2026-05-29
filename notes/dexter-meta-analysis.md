# Dexter 元分析笔记

## 代码统计

- TypeScript 文件数：155
- TypeScript 总行数：16,782
- 测试文件：6 个（cache.test.ts, utils.test.ts, store.test.ts, resolve-route.test.ts, access-control.test.ts, reconnect.test.ts）
- 总提交数：392
- 首次提交：2025-10-14 (Initial commit)
- 最新提交：2026-03-21 (Fix heartbeat)
- 项目年龄：约 5 个月

## 月度提交分布

| 月份 | 提交数 |
|------|--------|
| 2025-10 | 24 |
| 2025-11 | 25 |
| 2025-12 | 61 |
| 2026-01 | 125 |
| 2026-02 | 115 |
| 2026-03 | 42（截至21日） |

峰值在 2026 年 1-2 月，显示了项目从初期探索到快速成长的过程。

## 提交作者分布

- virattt / Virat Singh：350 次（89.3%）
- mkdev11：10 次
- Harsh Gupta：6 次
- bittoby / 7. Sun：各 5 次
- 其他贡献者均 < 5 次

## 最大文件 Top 10

| 文件 | 行数 |
|------|------|
| src/agent/scratchpad.ts | 465 |
| src/tools/browser/browser.ts | 429 |
| src/tools/fetch/web-fetch.ts | 420 |
| src/cli.ts | 403 |
| src/evals/run.ts | 360 |
| src/tools/search/x-search.ts | 344 |
| src/memory/database.ts | 342 |
| src/gateway/channels/whatsapp/inbound.ts | 326 |
| src/tools/finance/read-filings.ts | 321 |
| src/agent/prompts.ts | 298 |

## 目录结构概要

```
src/
├── agent/          # 核心 agent 循环、提示词、scratchpad、工具执行器
├── cli.ts          # CLI 入口（使用 pi-tui 库）
├── components/     # TUI 组件（聊天日志、工作指示器等）
├── controllers/    # 控制器（agent 运行、模型选择、输入历史）
├── evals/          # 评估套件（LangSmith 评估）
├── gateway/        # WhatsApp 网关集成
│   ├── channels/whatsapp/   # WhatsApp 通道实现
│   ├── group/       # 群组聊天支持
│   ├── heartbeat/   # 心跳机制
│   ├── routing/     # 路由解析
│   └── sessions/    # 会话管理
├── memory/         # 持久记忆系统（SQLite + 向量搜索 + 关键词搜索）
├── model/          # LLM 抽象层（多 provider 支持）
├── providers.ts    # Provider 注册中心
├── skills/         # 技能系统（DCF 估值、X 研究）
├── tools/          # 工具注册与实现
│   ├── browser/     # Playwright 浏览器
│   ├── fetch/       # 网页抓取
│   ├── filesystem/  # 文件读写
│   ├── finance/     # 金融数据工具集
│   ├── heartbeat/   # 心跳工具
│   ├── memory/      # 记忆读写工具
│   └── search/      # 搜索工具（Exa/Perplexity/Tavily/X）
└── utils/          # 工具函数
```

## 依赖分析

核心依赖：
- LangChain 全家桶（@langchain/core, openai, anthropic, google-genai, ollama, exa, tavily）
- @mariozechner/pi-tui — 终端 UI 框架
- Playwright — 浏览器自动化
- better-sqlite3 — 本地 SQLite（用于记忆系统）
- zod — 输入验证
- @whiskeysockets/baileys — WhatsApp Web API
- langsmith — 评估追踪

运行时：Bun
