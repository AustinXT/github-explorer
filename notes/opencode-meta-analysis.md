# anomalyco/opencode 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 436,532 行（含注释 162,297 行，空行 89,549 行，总计 688,378 行） |
| 语言分布 | TypeScript 157,982 行（36.2%）、TSX 75,805 行（17.4%）、CSS 19,473 行（4.5%）、SVG 16,223 行（3.7%）、Rust 2,508 行（0.6%）、Astro 1,115 行、JavaScript 622 行、BASH 490 行、SQL 385 行、Nix 312 行 |
| 代码/注释比 | 2.69:1（注释大量来自 MDX 文档 148,950 行） |
| 文件数量 | 3,769 个源文件 |
| 依赖数量 | 核心包 opencode: 84 deps + 29 devDeps；app: 32+12；ui: 27+11；web: 21+4；desktop-electron: 14+9；enterprise: 14+7；desktop: 19+6；根: 5+10 |

### 语言分布详情

| 语言 | 代码行数 | 文件数 | 占比 |
|------|----------|--------|------|
| JSON | 160,591 | 213 | 36.8% |
| TypeScript | 157,982 | 957 | 36.2% |
| TSX | 75,805 | 355 | 17.4% |
| CSS | 19,473 | 122 | 4.5% |
| SVG | 16,223 | 1,242 | 3.7% |
| Rust | 2,508 | 14 | 0.6% |
| Astro | 1,115 | 7 | 0.3% |
| JavaScript | 622 | 8 | 0.1% |
| BASH | 490 | 6 | 0.1% |
| SQL | 385 | 67 | 0.1% |

> 剔除 JSON 和 MDX 文档后，核心业务代码约 275,000 行，以 TypeScript + TSX 为绝对主力（约 85%），辅以 Rust（Tauri 桌面端）。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 约 12 个月（2025-03-21 至 2026-03-21） |
| 总 commit 数 | 10,447 |
| 平均 commit/天 | ~28.6 次/天 |
| 最近提交 | 2026-03-21（分析当天） |
| 近 30 天 commit | 884 |
| 近 90 天 commit | 4,456 |
| 开发阶段 | **高速增长期**——commit 从 2025-03 的 8 次迅猛增长至 2026-01 的 2,083 次，12 个月内超万次提交 |
| 开发模式 | 多人协作密集型，工作日驱动但周末也有 ~17% 的提交量（周六 898 + 周日 884 / 总 10,447） |

### 月度 Commit 趋势

```
2025-03 ▏      8
2025-04 ▊    152
2025-05 █▌   301
2025-06 ███▎  654
2025-07 ███▎  650
2025-08 ███   614
2025-09 ██▌   518
2025-10 ███▌  709
2025-11 █████▎ 1049
2025-12 █████████▍ 1877
2026-01 ██████████▍ 2083  ← 峰值
2026-02 █████▊ 1165
2026-03 ███▎   667 (进行中)
```

### 活跃时段

- 高峰时段：UTC 10:00-17:00（每小时 500-765 次），12:00 为最高峰（765 次）
- 次高峰：UTC 19:00-01:00（400-537 次），说明有跨时区贡献者
- 低谷时段：UTC 02:00-08:00（163-311 次）

### 核心贡献者 Top 10

| 排名 | 贡献者 | Commits |
|------|--------|---------|
| 1 | Dax Raad | 1,784 |
| 2 | Adam | 1,230 |
| 3 | Aiden Cline | 1,051 |
| 4 | GitHub Action (bot) | 839 |
| 5 | Frank | 606 |
| 6 | David Hill | 557 |
| 7 | opencode (bot) | 460 |
| 8 | Jay V | 336 |
| 9 | adamdottv | 330 |
| 10 | opencode-agent[bot] | 269 |

> 前三名人类贡献者（Dax、Adam、Aiden）合计 4,065 次 commit，占 39%。Bot 自动提交（GitHub Action + opencode + opencode-agent）合计约 1,568 次（15%）。项目自身 bot 参与度高，体现了 AI-native 的开发模式。

## 演化轨迹

### 版本里程碑

| 版本 | 发布日期 | 意义 |
|------|----------|------|
| v0.0.1 | 2025-04-21 | 首个可用版本，项目启动一个月后 |
| v0.1.0 | 2025-06-12 | 首个功能里程碑 |
| v1.0.0 | 2025-10-31 | 正式版发布，项目启动 7 个月后 |
| v1.2.0 | 2026-02-14 | 当前主版本线起点 |
| v1.2.27 | 2026-03-16 | 最新版本（Latest） |
| vscode-v0.0.13 | — | VSCode 扩展最新版 |

### 版本发布

| 指标 | 数据 |
|------|------|
| 总版本标签 | 904+ 个（含 v* 核心标签 + vscode-v* 扩展标签） |
| 当前版本 | v1.2.27（2026-03-16） |
| 版本范围 | v0.0.0-* → v0.x → v1.0 → v1.1.x → v1.2.x |
| 发布频率 | 极高，平均每天 ~2.5 个版本 |
| 最近 10 个版本 | v1.2.18 ~ v1.2.27 密集在 2026-03-05 ~ 2026-03-16 间发布（12 天 10 个版本） |
| VSCode 扩展 | 独立版本线 vscode-v0.0.1 ~ v0.0.13 |

### 核心热点文件 Top 15

| 修改次数 | 文件 |
|----------|------|
| 286 | packages/opencode/src/config/config.ts |
| 280 | packages/opencode/src/session/index.ts |
| 269 | packages/extensions/zed/extension.toml |
| 265 | packages/app/src/pages/layout.tsx |
| 262 | packages/opencode/src/provider/provider.ts |
| 253 | packages/app/src/pages/session.tsx |
| 226 | packages/opencode/src/session/prompt.ts |
| 218 | packages/opencode/src/server/server.ts |
| 192 | packages/app/src/components/prompt-input.tsx |
| 188 | packages/opencode/src/cli/cmd/tui/routes/session/index.tsx |
| 168 | packages/opencode/src/provider/transform.ts |
| 158 | packages/tui/internal/tui/tui.go |
| 146 | packages/sdk/js/src/gen/types.gen.ts |
| 145 | packages/sdk/js/src/v2/gen/types.gen.ts |

### 热点目录 Top 10

| 修改次数 | 目录 |
|----------|------|
| 8,791 | packages/opencode |
| 5,768 | packages/ui |
| 5,329 | packages/app |
| 5,298 | packages/web |
| 4,454 | packages/console |
| 2,967 | packages/desktop |
| 2,787 | packages/sdk |
| 2,049 | packages/tui |
| 772 | packages/plugin |
| 676 | internal/tui |

### Commit 类型分析（最近 200 次）

| 类型 | 数量 | 占比 |
|------|------|------|
| fix（修复） | 72 | 36.0% |
| other（杂项/chore/tweak/wip） | 88 | 44.0% |
| feat/add（新功能） | 20 | 10.0% |
| refactor（重构） | 14 | 7.0% |
| docs（文档） | 4 | 2.0% |
| test（测试） | 2 | 1.0% |

按 conventional commit 前缀细分：

| 前缀 | 数量 |
|------|------|
| fix | 63 |
| chore | 45 |
| refactor | 15 |
| feat | 9 |
| zen | 9 |
| tweak | 8 |
| app | 8 |
| docs | 7 |
| wip | 5 |
| tui | 3 |
| effectify | 3 |
| test | 2 |

> 修复占绝对主导（36%），说明项目正处于快速迭代+持续打磨阶段。chore 占比高（22.5%）反映了大量自动化构建/依赖更新。重构 7% 表明团队在持续优化架构。值得注意的是新出现的 "effectify" 前缀（3 次），表明正在进行 Effect 库的架构迁移。

## 项目画像卡片

```
┌──────────────────────────────────────────────────────┐
│  anomalyco/opencode                                  │
│  AI-native 编码助手 — Terminal + Desktop + Web       │
├──────────────────────────────────────────────────────┤
│  规模：436K 代码行 / 3,769 文件 / 904+ 版本          │
│  架构：Monorepo (14+ packages)                       │
│     核心: TypeScript (85%) + Rust (Tauri)            │
│     前端: SolidJS (TSX) + CSS + Astro                │
│     工具链: Bun + Nix + Turbo                        │
├──────────────────────────────────────────────────────┤
│  节奏：12 个月 / 10,447 commits / ~29/天             │
│     近 30 天: 884 commits                            │
│     近 90 天: 4,456 commits                          │
│     发布频率: ~2.5 版本/天                            │
├──────────────────────────────────────────────────────┤
│  团队：24+ 贡献者 + 3 Bot                            │
│     核心三人: Dax Raad / Adam / Aiden Cline          │
│     Bot 参与度: 15% (AI-native 开发)                 │
├──────────────────────────────────────────────────────┤
│  阶段：高速增长期                                     │
│     - Commit 月增长率 260 倍 (8→2,083)               │
│     - Fix 主导 (36%) = 快速迭代+品质打磨              │
│     - 版本号 v1.2.x = 产品已进入稳定迭代期           │
│     - 热点集中在 opencode/app/ui = 核心功能活跃       │
├──────────────────────────────────────────────────────┤
│  特征：                                              │
│     - 超高发布频率，CI/CD 高度自动化                  │
│     - Monorepo 多产品线并行(TUI/桌面/Web/控制台/SDK)  │
│     - 自身 Bot 参与提交，dogfooding AI 编码           │
│     - 跨时区团队，全天候开发                          │
│     - 正在进行 Effect 库架构迁移 (effectify)          │
└──────────────────────────────────────────────────────┘
```
