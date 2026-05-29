# Phase 2：元分析 — paperclipai/paperclip

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 209,996（不含空行/注释，排除 JSON 数据文件） |
| 语言分布 | TypeScript 64.1%, TSX 27.7%, YAML 4.9%, Shell 1.5%, SQL 0.8%, JavaScript 0.6%, CSS 0.3%, Dockerfile 0.05% |
| 代码/注释比 | 21:1（总代码 209,996 行 / 注释 9,994 行，注释率偏低） |
| 文件数量 | 1,344（含 86 个 JSON 数据文件、165 个 Markdown 文档） |
| 依赖数量 | server: 32 runtime + 14 dev; ui: 31 runtime + 9 dev; cli: 17 runtime + 3 dev（monorepo 架构，另含 adapter-utils/adapters/db/plugins/shared 5 个内部包） |

**规模判断**：~21 万行有效代码，属于**中大型项目**。TypeScript + TSX 占比超 91%，是典型的全栈 TypeScript monorepo。代码/注释比 21:1 说明文档化程度较低，以快速迭代为主而非文档驱动开发。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | ~1.6 个月（首次提交 2026-02-16，最近提交 2026-04-04） |
| 总 commit 数 | 1,879 |
| 最近提交 | 2026-04-04 |
| 近 30 天 commit | 1,364 |
| 近 90 天 commit | 1,879（项目本身不满 90 天） |
| 开发阶段 | **密集开发期**（1.6 个月内 1,879 次提交，日均约 39 次） |
| 开发模式 | **职业项目**（周末占比 17.9%，深夜 22:00-05:00 占比仅 3.6%，工作时间高度集中在 06:00-17:00） |

### 月度 Commit 分布

| 月份 | Commit 数 | 说明 |
|------|-----------|------|
| 2026-02 | 231 | 项目启动（2月16日起，仅半个月） |
| 2026-03 | 1,544 | **爆发式开发**，日均 ~50 次提交 |
| 2026-04 | 104 | 前 4 天，日均 ~26 次（节奏略有放缓） |

### 每日时间分布（作者本地时间 CST/CDT）

高频时段：16:00（188次）、08:00（154次）、09:00（153次）、14:00（146次）、15:00（145次）
— 典型的**美国工作日节奏**，上午 + 下午双高峰。

### 贡献者分布

| 排名 | 贡献者 | Commit 数 |
|------|--------|-----------|
| 1 | Dotta（含 dotta） | 1,560（83%） |
| 2 | Devin Foley | 56 |
| 3 | Matt Van Horn | 27 |
| 4 | zvictor | 24 |
| 5 | HenkDz | 24 |
| 6 | gsxdsm | 17 |
| 7 | Aaron | 17 |

总贡献者：**71 人**（但核心开发高度集中在 Dotta 一人，占 83% 的 commit）

**节奏判断**：日均 39 次 commit 的频率极其惊人，即使考虑到 CI/bot 贡献，这也是一个**极度活跃的初创项目**。Dotta 作为主力开发者几乎独自驱动了整个项目，属于典型的创始人驱动模式。

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. `ui/src/pages/Inbox.tsx` — 21 次修改
2. `server/src/services/heartbeat.ts` — 13 次修改
3. `server/src/__tests__/workspace-runtime.test.ts` — 12 次修改
4. `packages/shared/src/index.ts` — 12 次修改
5. `ui/src/pages/AdapterManager.tsx` — 11 次修改
6. `server/src/services/workspace-runtime.ts` — 11 次修改
7. `ui/src/components/CommentThread.tsx` — 10 次修改
8. `server/src/routes/issues.ts` — 10 次修改
9. `server/src/routes/agents.ts` — 10 次修改
10. `ui/src/pages/ProjectDetail.tsx` — 9 次修改

**核心文件解读**：Inbox、Agent、Adapter、Issue、Workspace 是产品核心领域，heartbeat 和 workspace-runtime 是后端关键基础设施。

### 热点目录

1. `ui/src` — 567 次修改（前端 UI 层）
2. `server/src` — 474 次修改（后端服务层）
3. `packages/shared` — 130 次修改（共享逻辑层）
4. `cli/src` — 117 次修改（CLI 工具）
5. `packages/adapters` — 88 次修改（适配器系统）
6. `packages/db` — 82 次修改（数据库层）
7. `skills/paperclip` — 17 次修改（技能系统）
8. `packages/plugins` — 16 次修改（插件系统）
9. `packages/adapter-utils` — 15 次修改（适配器工具）
10. `.github/workflows` — 11 次修改（CI/CD）

**架构焦点**：前端 UI（567 次）与后端 Server（474 次）修改最密集，前后端齐头并进。packages/ 下的共享层、适配器、数据库也频繁变更，说明基础架构仍在快速演化。

### Commit 类型分布（全部 1,579 个非合并 commit）

| 类型 | 数量 | 占比 |
|------|------|------|
| Feature/Add | 449 | 28.4% |
| Fix/Bug | 547 | 34.6% |
| Refactor | 14 | 0.9% |
| Docs | 48 | 3.0% |
| Test | 17 | 1.1% |
| Other | 504 | 31.9% |

**Commit 模式解读**：Fix 占比最高（34.6%），Feature 紧随其后（28.4%），这是典型的**快速迭代 + 持续修复**模式。Refactor 极少（0.9%）说明项目处于功能优先阶段，尚未进入架构优化期。测试 commit 仅占 1.1%，文档仅 3.0%，进一步印证了「速度优先」的开发策略。

### 版本发布

| 指标 | 数据 |
|------|------|
| 最新版本 | v2026.403.0（2026-04-04） |
| 总 Release 数 | 5 个正式 Release |
| 总 Tag 数 | 216 个（含 72 个 canary 预发布、130 个稳定版 tag、8 个 npm 包 tag） |
| 版本策略 | **混合版本策略** — 早期使用语义化版本（v0.2.x → v0.3.x），3 月中旬后切换为**日期版本**（v2026.MMDD.patch），同时维护 canary 预发布通道 |

**发布节奏**：216 个 tag 在 1.6 个月内产生，意味着**几乎每天都有多次发布**。canary 通道的存在说明采用了渐进式发布策略（canary → stable），这是成熟的 SaaS 发版实践。从语义化版本切换到日期版本，暗示项目从「版本驱动」转向「持续交付」模式。

## 项目画像卡片

```
项目: paperclipai/paperclip
年龄: 1.6 个月  |  代码: 209,996 行 (TypeScript/TSX 91%)
总 commits: 1,879  |  贡献者: 71 人（核心 1 人占 83%）
开发阶段: 密集开发（日均 39 次 commit）
开发模式: 职业项目（周末 17.9%，深夜 3.6%，美国工作时间节奏）
核心文件: Inbox.tsx, heartbeat.ts, workspace-runtime.ts, shared/index.ts
Release: v2026.403.0 (共 216 个 tag, 5 个正式 Release)
版本策略: 日期版本 + canary 预发布通道
Monorepo: ui / server / cli / packages(5) / skills
```
