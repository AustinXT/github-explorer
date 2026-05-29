# Onlook 元分析（Phase 2）

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 165,098（不含空行/注释） |
| 语言分布 | TypeScript 46.2%, TSX 34.3%, JSON 18.3%, SQL 0.5%, CSS 0.4%, JavaScript 0.3% |
| 代码/注释比 | 25:1 |
| 文件数量 | 1,578 |
| 依赖数量 | 406（runtime 246 / dev 160），Bun monorepo，22 个 workspace 包 |

**规模解读**：16.5 万行代码属于中大型项目，TypeScript + TSX 合计 80.5% 表明这是一个 React/Next.js 重度前端项目。代码/注释比 25:1 偏高，文档化程度较低——典型的快速迭代产品代码风格。406 个依赖分布在 22 个 workspace 包中，monorepo 架构组织清晰。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 21 个月（首次提交 2024-06-25） |
| 总 commit 数 | 1,636 |
| 最近提交 | 2026-02-26 |
| 近 30 天 commit | 0（截至 2026-04-06，最后提交在 2026-02-26） |
| 近 90 天 commit | 2 |
| 近 365 天 commit | 691 |
| 开发阶段 | 低维护期（曾经密集开发，近 2 个月几乎停滞） |
| 开发模式 | 职业项目（VC 支持的创业公司） |

**节奏解读**：项目在 21 个月内积累了 1,636 次 commit，月均约 78 次，属于高频开发。但从参与度数据看，近 52 周 owner commit 为 0（团队扩展后主要由团队成员提交），近 90 天仅 2 次 commit，项目活跃度大幅下降。周中 commit（周一至周四占 84 次/84%）远高于周末（13 次/13%），确认为职业开发模式。每日高峰集中在 15-19 点（美西时间），符合湾区工作时间。

**月度趋势**（浅 clone 可见范围）：

| 月份 | Commit 数 |
|------|-----------|
| 2025-09 | 31 |
| 2025-10 | 59 |
| 2025-11 | 4 |
| 2025-12 | 4 |
| 2026-01 | 1 |
| 2026-02 | 1 |

从 2025 年 10 月的高峰（59 次）急剧下降到 11 月后的个位数，暗示团队可能经历了重大调整。

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. `bun.lock` — 19 次修改（依赖频繁更新）
2. `apps/web/client/public/onlook-preload-script.js` — 16 次修改（核心预加载脚本）
3. `apps/web/client/package.json` — 11 次修改
4. `apps/web/client/src/components/store/editor/chat/context.ts` — 9 次修改（聊天上下文状态管理）
5. `packages/file-system/src/fs.ts` — 8 次修改
6. `packages/ai/src/prompt/provider.ts` — 8 次修改（AI 提示词提供者）
7. `package.json` — 8 次修改
8. `apps/web/client/src/components/store/editor/sandbox/index.ts` — 8 次修改（沙箱编辑器）
9. `apps/web/client/src/app/project/[id]/_components/right-panel/chat-tab/chat-input/index.tsx` — 8 次修改
10. `packages/ai/src/tools/toolset.ts` — 7 次修改（AI 工具集）

**热点解读**：最常修改文件集中在三个核心模块——AI 能力层（prompt/tools）、编辑器（sandbox/preload）、聊天交互（chat context/input/messages），揭示产品核心是「AI 驱动的可视化代码编辑器」。

### 热点目录

1. `apps/web` — 1,454 次修改（主 Web 应用，占绝对主导）
2. `packages/ai` — 280 次修改（AI 能力包）
3. `packages/fonts` — 195 次修改
4. `packages/parser` — 140 次修改（代码解析器）
5. `packages/ui` — 109 次修改（UI 组件库）
6. `packages/db` — 90 次修改（数据库层）
7. `packages/models` — 82 次修改（数据模型）
8. `packages/utility` — 53 次修改
9. `apps/backend` — 50 次修改
10. `packages/file-system` — 41 次修改

**架构解读**：`apps/web` 占 57% 的变更量，说明核心逻辑高度集中在前端。`packages/ai` 排第二（11%），反映 AI 功能是持续迭代重点。后端（`apps/backend`）变更量仅 50 次（2%），印证这是一个前端优先、AI 增强的产品。

### Commit 类型分布（采样 1,636 条）

- Feature/Add: 440 (27%)
- Fix/Bug: 397 (24%)
- Refactor: 63 (4%)
- Docs: 19 (1%)
- Test: 7 (0.4%)
- Chore/CI/Build: 44 (3%)
- Style/Lint: 31 (2%)
- Other: 632 (39%)

**类型解读**：Feature 与 Fix 合计 51%，项目处于「边加功能边修 Bug」的典型快速迭代阶段。Test 仅 0.4% 极为稀少，表明测试覆盖不足。39% 的 Other 来自未遵循 Conventional Commits 规范的提交（如 Merge PR 标题），说明团队 commit 规范执行不严格。

### 版本发布

- 最新版本: v0.2.32（2025-07-17）
- 总 Release 数: 148
- 总 Tag 数: 169
- 首个 Release: v0.0.2（2024-07-20）
- 版本策略: 语义化版本（0.x 阶段），高频发布（148 个 release / 21 个月 = 月均 7 个）

**发布解读**：148 个 Release 在 21 个月内发布，月均 7 次，属于极高频发布节奏。但最新 Release（v0.2.32）停留在 2025-07-17，距今已 9 个月无新发布，与 commit 活跃度下降一致。版本号仍在 0.x 阶段，产品未宣布 1.0 正式版。

## 项目画像卡片

```
项目: onlook-dev/onlook
年龄: 21 个月  |  代码: 165,098 行
总 commits: 1,636  |  贡献者: 103 人
开发阶段: 低维护期（2025-10 后活跃度骤降，近 90 天仅 2 次 commit）
开发模式: 职业项目（VC 支持创业公司，湾区工作时间节奏）
核心文件: AI prompt/tools、编辑器 sandbox/preload、聊天交互
Release: 148 个（最新 v0.2.32，2025-07-17），月均 7 次发布
技术栈: TypeScript/TSX + Next.js + Bun monorepo (22 packages)
许可证: Apache-2.0
```
