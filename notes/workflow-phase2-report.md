# Phase 2：元分析报告 — vercel/workflow

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 175,240（不含空行/注释） |
| 语言分布 | TypeScript 46.8%, TSX 21.7%, YAML 17.8%, MDX 6.5%, Rust 4.3%, JavaScript 3.6%, CSS 1.3% |
| 代码/注释比 | 4.9:1（代码 175,240 / 注释 36,008） |
| 文件数量 | 1,382 |
| 依赖数量 | 根 monorepo: 0 runtime + 10 dev；28 子包共计约 148 runtime + 140 dev |

**规模解读**：这是一个中大型 monorepo 项目，包含 28 个子包。TypeScript/TSX 合计占比 68.5%，是绝对主力语言。YAML 占比高（17.8%）主要来自 `pnpm-lock.yaml` 等配置文件。项目还包含 Rust 代码（SWC 插件），以及 MDX 文档。代码/注释比 4.9:1 属于中等文档化程度，MDX 文档（15,390 行）和 Markdown（14,038 行）表明文档投入相当可观。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 约 5 个月（首次提交 2025-10-23） |
| 总 commit 数 | 808 |
| 最近提交 | 2026-03-18 |
| 近 30 天 commit | 172 |
| 近 90 天 commit | 434 |
| 近 365 天 commit | 808（即全部） |
| 开发阶段 | **密集开发期** |
| 开发模式 | **职业项目**（周末占比 10.1%，深夜占比 16.7%） |

### 月度 Commit 分布

| 月份 | Commit 数 | 阶段判断 |
|------|-----------|----------|
| 2025-10 | 89 | 密集开发（项目启动，8天内89个commit） |
| 2025-11 | 173 | 密集开发 |
| 2025-12 | 149 | 密集开发 |
| 2026-01 | 121 | 密集开发 |
| 2026-02 | 162 | 密集开发 |
| 2026-03 | 114 | 密集开发（截至3月18日） |

**节奏解读**：项目自 2025 年 10 月底开源以来，保持了极高的开发节奏，月均约 135 个 commit，从未低于 89。这是一个由 Vercel 团队全力推进的职业项目。工作时间集中在 09:00-18:00（占比 64.7%），深夜（22:00-06:00）仅占 16.7%，周末仅占 10.1%，典型的企业团队开发模式。

### 贡献者分布（Top 5）

| 贡献者 | Commit 数 | 占比 |
|--------|-----------|------|
| Nathan Rajlich | 219 | 27.1% |
| Peter Wielander | 153 | 18.9% |
| Pranay Prakash | 109 | 13.5% |
| Vercel Release Bot | 71 | 8.8% |
| Adrian | 65 | 8.0% |

共 66 位贡献者参与，但核心开发主要由 3 人驱动（Nathan、Peter、Pranay 合计 59.5%）。

## 演化轨迹

### 核心文件（Top 10 最常修改，排除自动生成文件）

1. `packages/core/e2e/e2e.test.ts` — 63 次修改
2. `packages/core/src/runtime.ts` — 44 次修改
3. `.github/workflows/tests.yml` — 44 次修改
4. `packages/builders/src/base-builder.ts` — 43 次修改
5. `packages/swc-plugin-workflow/transform/src/lib.rs` — 39 次修改
6. `workbench/example/workflows/99_e2e.ts` — 36 次修改
7. `packages/core/src/serialization.ts` — 30 次修改
8. `packages/core/src/workflow.ts` — 28 次修改
9. `packages/core/src/runtime/step-handler.ts` — 28 次修改
10. `packages/world-local/src/queue.ts` — 26 次修改

**核心文件解读**：`packages/core` 是项目的绝对核心，runtime、serialization、workflow 等文件是最频繁修改的逻辑所在。SWC 插件（Rust）同样是高频变更区域，说明编译时转换是项目的关键技术点。e2e 测试文件高居榜首，说明团队重视端到端测试覆盖。

### 热点目录

1. `packages/core` — 800 次修改
2. `packages/swc-plugin-workflow` — 731 次修改
3. `docs/content` — 591 次修改
4. `packages/web` — 572 次修改
5. `packages/web-shared` — 531 次修改
6. `packages/cli` — 333 次修改
7. `docs/components` — 289 次修改
8. `packages/builders` — 274 次修改
9. `packages/world-local` — 273 次修改
10. `packages/world-vercel` — 248 次修改

**目录解读**：`packages/core` 和 `packages/swc-plugin-workflow` 是双核心。docs 相关目录（content + components = 880）高频变更，说明文档与代码同步迭代。web/web-shared 共计 1,103 次，说明 Web UI（调试/追踪界面）也是重要组成部分。

### Commit 类型分布（全部 808 个 commit）

| 类型 | 数量 | 占比 |
|------|------|------|
| Feature/Add | 145 | 17.9% |
| Fix/Bug | 218 | 27.0% |
| Refactor | 20 | 2.5% |
| Docs | 44 | 5.4% |
| Test | 27 | 3.3% |
| Other | 354 | 43.8% |

**类型解读**：Fix 占比最高（27.0%），高于 Feature（17.9%），这在快速迭代的 beta 阶段是正常的 — 新功能不断添加后需要大量修复。"Other" 占比高（43.8%）主要来自 changeset/版本发布相关的自动提交（Release Bot 贡献了 71 个）以及 chore 类提交。Refactor 仅占 2.5%，说明项目仍在快速堆叠功能，尚未进入大规模重构阶段。

### 版本发布

- 最新版本: `workflow@4.2.0-beta.71`（2026-03-18）
- 总 Tag 数: 448（覆盖所有子包）
- 主包 workflow Tag 数: 72
- Release 数: 200+
- 版本策略: **语义化版本 + Beta 预发布**（当前所有发布均为 beta，尚未发布正式版）

**版本解读**：项目采用 monorepo changeset 工作流，每次发布会同时 tag 多个子包。71 个 beta 版本在 5 个月内发布，平均每 2 天发布一个新版本，迭代速度极快。从 `4.1.0-beta.x` 演进到 `4.2.0-beta.x`，主版本号为 4，暗示可能在开源前已有内部版本迭代历史。

## 项目画像卡片

```
项目: vercel/workflow
年龄: 5 个月  |  代码: 175,240 行 (TypeScript/TSX 为主，含 Rust)
总 commits: 808  |  贡献者: 66 人（核心 3 人）
开发阶段: 密集开发（月均 135 commits，全 beta 阶段）
开发模式: 职业项目（Vercel 团队，工作日+工作时间为主）
核心文件: core/runtime.ts, core/serialization.ts, builders/base-builder.ts, swc-plugin/lib.rs
Release: workflow@4.2.0-beta.71 (共 72 个主包版本, 448 个跨包 tag)
```
