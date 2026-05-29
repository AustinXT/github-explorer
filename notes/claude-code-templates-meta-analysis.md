# davila7/claude-code-templates 元分析报告

> 分析时间：2026-03-22 | 仓库：davila7/claude-code-templates

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 730,699 行 |
| 语言分布 | JSON 29.3%、Python 15.3%、JavaScript 6.7%、CSS 4.3%、HTML 3.5%、TeX 2.4%、Shell 1.5%、TSX 0.9%、TypeScript 0.5%、Astro 0.2%、其他 35.4%（含大量组件模板/YAML/Markdown 等） |
| 代码/注释比 | 1.3:1（代码 730,699 行 / 注释 576,914 行） |
| 文件数量 | 5,114 个 |
| 依赖数量 | 根项目 18+1、cli-tool 13+2、dashboard 15+0、docu 7+4、api 6+2（合计约 69 个，含 deps+devDeps） |

**说明**：代码行数和文件数偏大，主要因为仓库包含约 7,000+ 次修改的 `cli-tool/components` 目录——这是一个社区贡献的 CLAUDE.md 组件/模板库，内含大量 Python、Shell、SQL 等多语言模板文件，属于"数据即代码"的特殊形态。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 约 8.5 个月（2025-07-03 至今） |
| 总 commit 数 | 970 |
| 最近提交 | 2026-03-21 |
| 近 30 天 / 90 天 commit | 102 / 312 |
| 平均 commit/月 | ~114 |
| 贡献者 | 58 人（核心开发者 Dani/Daniel Avila 贡献 ~89%） |
| 开发阶段 | **活跃增长期** — 项目不到 9 个月已迭代到 v1.28.x，保持高频提交，每月平均 100+ commit |
| 开发模式 | **核心驱动 + 社区贡献型** — 单核心开发者主导（Dani），github-actions[bot] 贡献 141 次（自动化流水线），另有 50+ 社区贡献者零星参与 |

### 月度 commit 分布

| 月份 | Commit 数 | 趋势 |
|------|-----------|------|
| 2025-07 | 186 | 项目启动高峰 |
| 2025-08 | 175 | 持续高峰 |
| 2025-09 | 94 | 回落 |
| 2025-10 | 116 | 回升（密集发版） |
| 2025-11 | 49 | 低谷 |
| 2025-12 | 75 | 回暖 |
| 2026-01 | 114 | 新一轮活跃 |
| 2026-02 | 103 | 稳定 |
| 2026-03 | 58 | 月未过完，节奏正常 |

### 活跃时段
- **最活跃小时**：凌晨 03 时（138 次，可能对应 UTC 时区差异/自动化）、20 时（83 次）、17 时（62 次）
- **最活跃工作日**：周四（170 次）> 周五（153 次）> 周三（146 次）；周末活跃度也不低（周六 142、周日 117），表明开发者在业余时间也大量投入

## 演化轨迹

### 核心文件（Top 10）

| 排名 | 文件 | 修改次数 |
|------|------|----------|
| 1 | docs/components.json | 275 |
| 2 | docs/trending-data.json | 155 |
| 3 | cli-tool/package.json | 114 |
| 4 | cli-tool/src/index.js | 90 |
| 5 | docs/index.html | 78 |
| 6 | cli-tool/package-lock.json | 78 |
| 7 | README.md | 77 |
| 8 | cli-tool/bin/create-claude-config.js | 33 |
| 9 | .claude/settings.local.json | 31 |
| 10 | docs/css/styles.css | 30 |

**洞察**：`components.json` 被修改 275 次，是全仓库最热文件——它是组件注册中心索引，每次新增模板都需更新。`trending-data.json` 是自动化数据采集的产物。

### 热点目录

| 排名 | 目录 | 修改次数 |
|------|------|----------|
| 1 | cli-tool/components | 7,409 |
| 2 | cli-tool/src | 367 |
| 3 | cli-tool/templates | 160 |
| 4 | docs/blog | 139 |
| 5 | .claude/agents | 127 |
| 6 | docs/js | 122 |
| 7 | docu/docs | 116 |
| 8 | dashboard/src | 114 |
| 9 | dashboard/public | 81 |

**洞察**：`cli-tool/components` 以绝对优势领先（7,409 次），说明组件模板的增删改是项目的核心活动。`cli-tool/src` 排名第二，是 CLI 工具的主引擎代码。

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 新功能 (feat/add) | 88 | 44.0% |
| 修复 (fix/bug) | 29 | 14.5% |
| 文档 (doc) | 4 | 2.0% |
| 测试 (test) | 4 | 2.0% |
| 重构 (refactor) | 0 | 0.0% |
| 其他 | 75 | 37.5% |

**洞察**：以功能新增为主（44%），修复占 14.5%，说明项目处于功能快速扩张期。重构为 0 说明尚未进入技术债偿还阶段。

### 版本发布

| 版本 | 标题 | 日期 |
|------|------|------|
| v1.28.3 | Plugin Skills Support in Skills Manager | 2025-11-15 |
| v1.27.0 | Docker Sandbox Provider | 2025-11-02 |
| v1.26.4 | Command Usage Analytics | 2025-11-01 |
| v1.26.2 | Session Analytics (Beta) | 2025-10-31 |
| v1.25.0 | Session Sharing & UI Improvements | 2025-10-27 |
| v1.24.16 | Cloudflare Sandbox Integration | 2025-10-21 |
| v1.24.0 | Skills Integration | 2025-10-17 |
| v1.23.0 | Component Security Validation | 2025-10-16 |
| v1.22.0 | Plugin Dashboard with Monitoring | 2025-10-10 |
| v1.21.11 | Enhanced Chats Mobile Interface | 2025-09-24 |

- 总 tag 数：32 个（最新 v1.28.16，2026-02-08）
- 2025年10月为发版最密集时段（6 个 release）
- 版本号跨度大（v1.21 -> v1.28），patch 号经常跳跃（如 v1.24.0 -> v1.24.16），体现快速迭代风格

## 项目画像卡片

```
┌─────────────────────────────────────────────────────────┐
│  davila7/claude-code-templates                          │
│  Claude Code 组件模板生态工具                              │
├─────────────────────────────────────────────────────────┤
│  规模：730K 行代码 / 5,114 文件 / 69 依赖               │
│  主要语言：JSON · Python · JavaScript · TypeScript       │
│  项目年龄：8.5 个月 | 970 commits | 32 tags             │
│  贡献者：58 人（核心 1 人贡献 89%）                       │
│  开发阶段：活跃增长期（月均 114 commit）                   │
│  开发模式：核心驱动 + 社区贡献                             │
│  迭代节奏：约 3-5 天一个 release（密集期）                 │
│  代码特征：大量组件模板 + CLI 工具 + Dashboard + API      │
│  技术栈：Node.js/Astro/TypeScript + Python + Vercel     │
│  自动化：GitHub Actions 驱动 trending 数据采集            │
│  关键信号：功能新增占 44%，无重构，快速扩张期               │
└─────────────────────────────────────────────────────────┘
```
