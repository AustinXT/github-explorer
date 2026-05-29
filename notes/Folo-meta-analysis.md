## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 269,809（不含空行/注释） |
| 语言分布 | TSX 43.5%, TypeScript 20.4%, JSON 20.0%, YAML 12.8%, Swift 1.4%, CSS 0.9%, JavaScript 0.5% |
| 代码/注释比 | 35:1 |
| 文件数量 | 3,018 |
| 依赖数量 | 34（devDeps），根仓库级别无 runtime deps（monorepo 子包各自管理） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 24 个月（首次提交 2024-04-10） |
| 总 commit 数 | 6,723 |
| 最近提交 | 2026-04-05 |
| 近 30 天 commit | 91 |
| 近 90 天 commit | 155 |
| 近 365 天 commit | 2,631 |
| 开发阶段 | 密集开发（月均 280 commit，2025 年 3-5 月达峰值 444-505/月，2026 年初转入稳定节奏 23-91/月） |
| 开发模式 | 职业项目（周末占比 15.4%，深夜占比 23.3%） |

### 月度 commit 分布

项目经历了三个明显阶段：
1. **起步期**（2024-04 ~ 2024-06）：76-199 commit/月，快速搭建基础架构
2. **爆发期**（2024-07 ~ 2025-05）：平均 370 commit/月，2024-09 达 582 峰值，这是核心功能密集开发期
3. **收敛期**（2025-06 ~ 2026-04）：逐步收敛至 20-91 commit/月，进入稳定迭代和维护阶段

### 每小时分布

最活跃时段为 15:00-18:00 和 20:00-23:00（东八区），白天+晚间双峰模式，典型的全职开发者节奏。凌晨 3:00-8:00 极少提交。

## 演化轨迹

### 核心文件（Top 10 最常修改）
1. pnpm-lock.yaml — 650 次修改
2. package.json — 394 次修改
3. locales/settings/en.json — 193 次修改
4. apps/mobile/package.json — 190 次修改
5. locales/app/en.json — 177 次修改
6. locales/settings/zh-CN.json — 150 次修改
7. locales/app/zh-CN.json — 136 次修改
8. apps/desktop/package.json — 130 次修改
9. packages/shared/src/hono.ts — 122 次修改
10. src/renderer/src/modules/entry-column/index.tsx — 94 次修改

### 热点目录
1. apps/desktop — 9,706 次修改
2. apps/mobile — 6,875 次修改
3. src/renderer — 5,641 次修改
4. apps/renderer — 4,890 次修改
5. packages/internal — 1,894 次修改
6. locales/app — 793 次修改
7. locales/settings — 752 次修改
8. apps/ssr — 690 次修改
9. icons/mgc — 443 次修改
10. .github/workflows — 398 次修改

**架构转折信号**：`src/renderer`（5,641 次）和 `apps/renderer`（4,890 次）的共存说明项目经历过一次重大架构迁移——从早期单体 renderer 拆分为 monorepo 下的 `apps/` 结构。`apps/desktop` 以 9,706 次变更高居榜首，是绝对核心；`apps/mobile` 6,875 次变更表明移动端是后期重点发力方向。

### Commit 类型分布（最近 200 条）
- Feature/Add: 39 (19.5%)
- Fix/Bug: 94 (47.0%)
- Refactor: 3 (1.5%)
- Docs: 9 (4.5%)
- Test: 1 (0.5%)
- Other: 54 (27.0%)

Fix 占比接近半数，说明项目已过「功能堆叠」阶段，当前以质量打磨和稳定性修复为主。测试相关提交极少（0.5%），测试覆盖可能偏弱。

### 版本发布
- 最新版本: Desktop v1.5.0 / Mobile v0.4.1（2026-04-03）
- 总 Tag 数: 123，总 Release 数: 100+
- 版本策略: 语义化版本（Desktop 和 Mobile 双产品线独立版本号），辅以 Nightly 自动构建

项目采用 Desktop/Mobile 双产品线发布策略。Desktop 已迭代至 v1.5.0（成熟），Mobile 处于 v0.4.1（快速追赶）。从 v0.0.1-internal.1 到 alpha、beta、nightly 再到正式版，发布流程完善且专业。

### 贡献者
- 总贡献者: 158 人
- Top 3: Innei（2,842 commits, 42.3%）、DIYgod（1,847 commits, 27.5%）、Stephen Zhou（990 commits, 14.7%）
- 前三名贡献者占总 commit 的 84.5%，核心团队驱动型项目

## 项目画像卡片

```
项目: RSSNext/Folo
年龄: 24 个月  |  代码: 269,809 行 (TSX/TypeScript)
总 commits: 6,723  |  贡献者: 158 人
开发阶段: 密集开发 → 稳定迭代（当前处于收敛维护期）
开发模式: 职业项目（周末 15.4%，深夜 23.3%）
核心文件: packages/shared/src/hono.ts, entry-column/index.tsx, entry-content/index.tsx
核心目录: apps/desktop, apps/mobile, apps/renderer
Release: Desktop v1.5.0 / Mobile v0.4.1（共 123 个 tag, 100+ release）
```
