# remotion-dev/remotion 元分析报告

> 分析日期：2026-03-22

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 837,842（不含空行/注释） |
| 语言分布 | TypeScript 68.1%, TSX 17.3%, JavaScript 9.6%, JSON 3.3%, Rust 0.5%, CSS 0.3%, PHP 0.3%, Python 0.2%, 其他 0.4% |
| 代码/注释比 | 9.3:1 |
| 文件数量 | 8,389 |
| 包数量 | 115（monorepo） |
| 文档页面 | 856 个 MDX/MD 文件（118MB docs 包） |

### 语言详情（Top 10）

| 语言 | 文件数 | 代码行数 | 占比 |
|------|--------|----------|------|
| TypeScript | 4,836 | 570,536 | 68.1% |
| TSX | 1,840 | 144,614 | 17.3% |
| JavaScript | 229 | 80,138 | 9.6% |
| JSON | 240 | 27,374 | 3.3% |
| Rust | 25 | 3,834 | 0.5% |
| CSS | 74 | 2,773 | 0.3% |
| PHP | 12 | 2,384 | 0.3% |
| Python | 16 | 1,780 | 0.2% |
| Go | 8 | 586 | 0.1% |
| Ruby | 12 | 391 | <0.1% |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 69 个月（首次提交 2020-06-23） |
| 近 15 个月 commit 数 | 8,630（2025-01-01 起） |
| 近 27 个月 commit 数 | 14,557（2024-01-01 起） |
| 最近提交 | 2026-03-20 |
| 开发阶段 | 高度活跃（每日平均 19+ commits） |
| 开发模式 | 全职商业项目（工作日集中，欧洲时区） |

### 月度 Commit 分布（2025-01 至 2026-03）

| 月份 | Commits | 活跃度 |
|------|---------|--------|
| 2025-01 | 662 | ████████ |
| 2025-02 | 429 | █████ |
| 2025-03 | 537 | ██████ |
| 2025-04 | 504 | ██████ |
| 2025-05 | 413 | █████ |
| 2025-06 | 416 | █████ |
| 2025-07 | 229 | ██ |
| 2025-08 | 336 | ████ |
| 2025-09 | 407 | █████ |
| 2025-10 | 767 | █████████ |
| 2025-11 | 487 | ██████ |
| 2025-12 | 809 | ██████████ |
| 2026-01 | 929 | ███████████ |
| 2026-02 | 1,241 | ███████████████ |
| 2026-03 | 464（截至3/20）| █████ |

趋势：2025下半年起开发节奏明显加速，2026-02 达到峰值（1,241 commits），项目处于快速迭代阶段。

### 工作时间模式

- **高频时段**：09:00-17:00（欧洲CET时区），峰值在 11:00（938 commits）
- **工作日占比**：85.2%（周一至周五 7,337 commits）
- **周末占比**：14.8%（周六 570 + 周日 723 = 1,293 commits）
- **深夜开发（22:00-06:00）**：约 2.9%（246 commits），极低
- **模式判断**：典型的全职商业开发团队模式，工作日密集、周末少量维护

### 星期分布

| 星期 | Commits |
|------|---------|
| 周一 | 1,461 |
| 周二 | 1,659（峰值） |
| 周三 | 1,464 |
| 周四 | 1,403 |
| 周五 | 1,350 |
| 周六 | 570 |
| 周日 | 723 |

## 贡献者分析

| 指标 | 数据 |
|------|------|
| 近 15 个月活跃贡献者 | 87 人 |
| 引用 PR 数 | 1,428 个独立 PR |

### 核心贡献者（非 merge commits，2025-01 起）

| 排名 | 贡献者 | Commits | 角色判断 |
|------|--------|---------|----------|
| 1 | Jonny Burger | 3,910 | 创始人/核心维护者 |
| 2 | JonnyBurger | 1,437 | 同一人（不同 Git 配置） |
| 3 | Igor Samokhovets | 489 | 核心团队成员 |
| 4 | copilot-swe-agent[bot] | 170 | AI 辅助开发 |
| 5 | ASchwad | 113 | 活跃贡献者 |
| 6 | Hunain Ahmed | 81 | 活跃贡献者 |
| 7 | Vlad M | 71 | 活跃贡献者 |
| 8 | pullfrog[bot] | 67 | 自动化工具 |
| 9 | Pramod | 57 | 贡献者 |
| 10 | MehmetAdemi | 44 | 贡献者 |

> Jonny Burger（合并两个账户）贡献了 5,347/6,719 非 merge commits（79.6%），属于典型的**创始人主导型**项目。
> 值得注意的是 AI 辅助开发（copilot-swe-agent、Cursor Agent、claude[bot]）合计 198 commits，占比约 3%，体现了 AI 辅助编码的趋势。

## 演化轨迹

### 热点文件（Top 15 最常修改，2025-01 起）

| 文件 | 修改次数 | 说明 |
|------|----------|------|
| bun.lock | 270 | 依赖锁文件（版本更新频繁） |
| packages/web-renderer/src/render-media-on-web.tsx | 101 | Web 渲染核心 |
| packages/web-renderer/package.json | 97 | Web 渲染器包配置 |
| packages/docs/package.json | 93 | 文档包配置 |
| packages/media/package.json | 86 | 媒体处理包配置 |
| packages/example/package.json | 83 | 示例项目配置 |
| packages/lambda/package.json | 78 | Lambda 部署包 |
| packages/it-tests/package.json | 78 | 集成测试包 |
| packages/design/package.json | 78 | 设计系统包 |
| packages/bundler/package.json | 78 | 打包器包 |
| packages/studio/package.json | 76 | Studio IDE 包 |
| packages/renderer/package.json | 76 | 渲染器包 |
| packages/mcp/package.json | 76 | MCP 集成包 |
| packages/docs/sidebars.ts | 75 | 文档侧边栏（频繁新增页面） |
| packages/google-fonts/scripts/incompatible-fonts.ts | 74 | 字体兼容性脚本 |

> 大量 package.json 高频修改反映了 monorepo 版本同步发布模式：每次 release 更新所有包版本号。

### 热点目录（非 merge commits，2025-01 起）

| 目录 | 修改次数 | 领域 |
|------|----------|------|
| packages/web-renderer/src | 422 | Web 端渲染引擎（最活跃开发区） |
| packages/web-renderer/src/test | 390 | Web 渲染测试 |
| packages/cli/src | 319 | CLI 工具 |
| packages/core/src | 313 | 核心运行时 |
| packages/web-renderer/src/drawing | 252 | 绘制引擎 |
| packages/docs | 251 | 文档 |
| packages/docs/docs | 247 | 文档内容 |
| packages/lambda-php | 235 | PHP Lambda SDK |
| packages/media/src | 223 | 媒体处理 |
| packages/lambda-go | 177 | Go Lambda SDK |

### 最活跃包（按 commit message 统计）

| 包名 | Commits | 领域 |
|------|---------|------|
| @remotion/media | 109 | 媒体处理 |
| @remotion/media-parser | 99 | 媒体解析 |
| @remotion/web-renderer | 76 | Web 渲染引擎（新模块） |
| @remotion/renderer | 69 | 服务端渲染 |
| @remotion/studio | 67 | 可视化 Studio IDE |
| @remotion/lambda | 37 | AWS Lambda 部署 |
| @remotion/webcodecs | 27 | WebCodecs API 集成 |
| @remotion/cli | 20 | 命令行工具 |
| @remotion/vercel | 18 | Vercel 部署 |
| @remotion/media-utils | 16 | 媒体工具函数 |

> 2025-2026 年开发重心明显集中在：(1) **@remotion/web-renderer** — 全新的 Web 端渲染引擎，(2) **@remotion/media & media-parser** — 媒体处理能力强化，(3) **多平台 Lambda SDK**（PHP、Go、Ruby）— 生态拓展。

### Commit 类型分布（2025-01 起，基于关键词分析）

| 类型 | 数量 | 占比 |
|------|------|------|
| Merge | 1,911 | 22.1% |
| Update/Upgrade | 1,524 | 17.7% |
| Feature/Add/Support | 911 | 10.6% |
| Fix/Bug | 584 | 6.8% |
| Test | 511 | 5.9% |
| Docs | 473 | 5.5% |
| Release（版本号） | 213 | 2.5% |
| Remove/Delete/Deprecate | 240 | 2.8% |
| Refactor/Clean | 212 | 2.5% |
| CI/CD | 209 | 2.4% |
| Performance | 131 | 1.5% |
| Revert | 68 | 0.8% |

> 项目以持续更新和功能添加为主，Fix 占比仅 6.8%，说明代码质量较高。高 merge 比（22.1%）反映了严格的 PR Review 流程。

## 版本发布

| 指标 | 数据 |
|------|------|
| 最新版本 | v4.0.438 |
| 最早版本 | v1.0.0-alpha.2 |
| 总 Tag 数 | 833 |
| v4.x Tag 数 | 441（v4.0.0 ~ v4.0.438） |
| v3.x Tag 数 | 194 |
| 版本策略 | 高频 patch 发布（v4.0.x，几乎每 1-3 天一个版本） |

### 近期发布频率（2026-03 示例）

| 版本 | 日期 | 间隔 |
|------|------|------|
| v4.0.438 | 2026-03-19 | 3 天 |
| v4.0.437 | 2026-03-19 | 同日 |
| v4.0.436 | 2026-03-16 | 4 天 |
| v4.0.435 | 2026-03-12 | 7 天 |
| v4.0.434 | 2026-03-05 | 同日 |
| v4.0.433 | 2026-03-05 | 2 天 |
| v4.0.432 | 2026-03-03 | — |

> 极高的发布频率（平均 1-3 天/版本），采用持续交付策略，所有 v4.x 使用 patch 版本号递增（无 minor/major 跳跃），当前已发布 438 个 patch 版本。

## Monorepo 包分类

### 核心包
- `core` — React 运行时核心
- `renderer` — 服务端渲染引擎
- `web-renderer` — Web 端渲染引擎（新）
- `bundler` — Webpack 打包器
- `cli` — 命令行工具
- `player` — React 播放器组件

### 云部署
- `lambda` / `lambda-client` — AWS Lambda 部署
- `cloudrun` — Google Cloud Run
- `vercel` — Vercel 部署
- 多语言 SDK：`lambda-go`、`lambda-php`、`lambda-python`、`lambda-ruby`

### 媒体处理
- `media` — 统一媒体 API
- `media-parser` — 媒体格式解析
- `media-utils` — 媒体工具函数
- `webcodecs` — WebCodecs API
- `captions` — 字幕处理
- `convert` — 格式转换
- `gif` — GIF 支持
- `lottie` — Lottie 动画

### 创作工具
- `studio` / `studio-server` / `studio-shared` — 可视化 Studio IDE
- `mcp` — MCP (Model Context Protocol) 集成
- `transitions` — 转场效果
- `animation-utils` / `motion-blur` / `noise` — 动画效果
- `three` — Three.js 3D 集成

### 其他
- `docs` — Docusaurus 文档站点
- `eslint-plugin` / `eslint-config` — 代码规范
- `google-fonts` / `fonts` — 字体支持
- 20+ 个 `template-*` 模板项目
- `licensing` — 许可证管理
- `design` / `brand` — 设计系统

## 项目画像卡片

```
项目: remotion-dev/remotion
年龄: 69 个月 (2020-06 起)  |  代码: 837,842 行 (TypeScript/TSX/JS)
总 tags: 833  |  当前版本: v4.0.438
近 15 月 commits: 8,630  |  活跃贡献者: 87 人
Monorepo 包数: 115  |  文档页面: 856
开发阶段: 高度活跃（持续加速中）
开发模式: 全职商业团队（创始人主导 79.6%，欧洲CET时区）
发布策略: 持续交付（平均 1-3 天/版本）
核心热点: web-renderer（新引擎）、media/media-parser（媒体栈）、多语言 Lambda SDK
AI 辅助: copilot + cursor + claude 合计约 3% commits
里程碑: 40K+ stars, 1.4M+ 下载, 8000+ Discord 成员
```
