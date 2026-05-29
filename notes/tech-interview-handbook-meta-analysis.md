# yangshun/tech-interview-handbook 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 114,494（不含空行/注释） |
| 语言分布 | JSON 59.6%, TSX 16.3%, TypeScript 11.0%, YAML 9.5%, JavaScript 1.9%, SQL 0.6%, Python 0.5%, CSS 0.3% |
| 代码/注释比 | 18.4:1 |
| 文件数量 | 496 |
| 依赖数量 | 57（runtime: 38, dev: 19，跨 monorepo 各包合计） |

**规模解读**：中等规模项目。JSON 占比最高（68,298 行）主要为配置和数据文件。实际业务代码以 TSX（18,666 行）和 TypeScript（12,636 行）为主，合计约 31,302 行，体现了典型的 React + TypeScript 前端技术栈。代码/注释比 18.4:1 偏高，说明注释极少，文档化程度较低（不过项目本身以 Markdown 内容为核心载体，73 个 Markdown 文件承载了 5,219 行注释/内容）。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 约 102 个月（首次提交 2017-09-20） |
| 总 commit 数 | 1,334 |
| 最近提交 | 2026-03-20 |
| 近 30 天 commit | 13 |
| 近 90 天 commit | 15 |
| 近 365 天 commit | 34 |
| 开发阶段 | 低维护期（近期有小幅活跃迹象） |
| 开发模式 | 混合型——以工作日为主的职业项目（周末占比 28.5%，深夜 0-5 时占比 14.3%） |

**节奏解读**：

- **密集开发期**：2022 年 10-11 月是项目的绝对峰值（413 + 186 = 599 commits），这段时间应为 Portal 应用（求职门户平台）的集中开发期。2022 年全年是最活跃的年份。
- **早期爆发**：2017 年 9-10 月（项目初创，122 commits），2019 年 7-9 月（62 commits，内容扩充期），2021 年 8-9 月（70 commits，重构/扩展期）。
- **2023 年后进入低维护**：月均不到 5 次 commit，说明项目已趋于稳定/完成。
- **2026 年 3 月突然有 13 次 commit**，表明近期有一波更新活动。
- **贡献者**：共 194 位贡献者，但主作者 Yangshun Tay 占据绝对主导（以 "Yangshun Tay"、"Yangshun"、"Tay Yang Shun" 三个身份合计 642 commits，占总数 48.1%）。前 10 名贡献者中，多数参与了 2022 年的 Portal 开发。

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. `apps/portal/src/components/offers/table/OffersTable.tsx` — 15 次修改
2. `apps/portal/src/components/global/AppShell.tsx` — 15 次修改
3. `apps/portal/src/mappers/offers-mappers.ts` — 13 次修改
4. `apps/portal/src/pages/resumes/[resumeId].tsx` — 12 次修改
5. `apps/portal/src/pages/questions/browse.tsx` — 12 次修改
6. `apps/portal/package.json` — 12 次修改
7. `apps/portal/src/pages/questions/[questionId]/[questionSlug]/index.tsx` — 11 次修改
8. `apps/portal/src/pages/offers/profile/[offerProfileId].tsx` — 11 次修改
9. `apps/portal/src/pages/offers/index.tsx` — 11 次修改
10. `apps/portal/src/components/questions/card/question/BaseQuestionCard.tsx` — 11 次修改

### 热点目录

1. `apps/portal` — 2,368 次修改
2. `apps/website` — 212 次修改
3. `packages/ui` — 64 次修改
4. `apps/storybook` — 49 次修改
5. `.github/workflows` — 8 次修改
6. `packages/tailwind-config` — 3 次修改
7. `packages/eslint-config-tih` — 3 次修改

### Commit 类型分布（最近 200 条）

- Feature/Add: 58 (29.0%)
- Fix/Bug: 73 (36.5%)
- Refactor: 5 (2.5%)
- Docs: 0 (0%)
- Test: 0 (0%)
- Other: 64 (32.0%)

**类型解读**：Fix 占比最高（36.5%），Feature 次之（29.0%），几乎没有 Refactor、Docs、Test 类别的 commit。这表明项目在后期以修复和功能调整为主，测试和文档建设薄弱。"Other" 占比 32% 较高，很多 commit 消息不遵循 conventional commits 规范（如 "Remove app.techinterviewhandbook.org mentions"、"Update ..."）。

### 版本发布

- 最新标签: `legacy`（无语义化版本）
- 总 Release 数: 0（无 GitHub Release）
- 总 Tag 数: 1
- 版本策略: 无版本管理——项目不使用语义化版本或定期发布，仅有一个 `legacy` 标签标记旧版代码

## 项目画像卡片

```
项目: yangshun/tech-interview-handbook
年龄: ~102 个月（2017-09 至今）  |  代码: 114,494 行 (TSX/TypeScript/JavaScript/JSON/Markdown...)
总 commits: 1,334  |  贡献者: 194 人
开发阶段: 低维护期（2023 年后放缓，2026-03 有小幅活跃）
开发模式: 混合型偏职业项目（周末 28.5%，深夜 14.3%）
核心文件: apps/portal 下的 OffersTable、AppShell、offers-mappers 等
Release: 无正式发布（仅 1 个 legacy 标签）
```

**综合判断**：这是一个以内容（面试指南 Markdown）+ Web 应用（Portal 求职平台）为核心的开源项目。2022 年经历了大规模的 Portal 应用开发（全栈 Next.js + Prisma），此后进入低维护状态。项目由 Yangshun Tay 主导，Portal 部分由一个小团队（约 8-10 人）在 2022 年集中开发完成。没有正式的版本管理和发布流程，更像是一个持续演化的内容 + 应用平台而非传统的软件库。
