# TypeWords 元分析（Phase 2）

> 仓库：zyronon/TypeWords
> 分析时间：2026-04-06

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 125,119（不含空行/注释） |
| 语言分布 | CSS 48.3%, YAML 11.8%, JavaScript 11.7%, JSON 12.1%, TypeScript 4.9%, Vue 2.0%, Sass 1.4%, 其他 < 1% |
| 代码/注释比 | 32:1 |
| 文件数量 | 309 |
| 依赖数量 | 80（runtime: 25, dev: 55） |

**备注：** CSS 占比高主要因为 `apps/vscode-web/src/assets/css/cursor.css` 单文件 60,367 行（疑似第三方资源文件）。Vue 组件内嵌的 JavaScript（13,955 行）和 HTML（4,815 行）未计入顶层语言统计，实际业务代码以 Vue + TypeScript 为主。去除 CSS/YAML/JSON 等非业务代码后，核心业务代码约 25,000-30,000 行。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 约 3 个月（2026-01-15 至今） |
| 总 commit 数 | 317（当前分支） |
| 最近提交 | 2026-04-05 |
| 近 30 天 commit | 130 |
| 近 90 天 commit | 317（覆盖全部历史） |
| 开发阶段 | 密集开发 |
| 开发模式 | 业余 Side Project（深夜型） |

### 开发节奏特征

- **月度分布：** 1 月 53 次、2 月 112 次、3 月 149 次、4 月 3 次（截至 4/5）— 呈持续加速趋势
- **活跃时段：** 凌晨 01:00-02:00 为峰值（92 次），00:00-03:00 占总提交 37%，典型深夜开发者模式
- **工作日分布：** 周一至周日均有提交，周一（60）最多，周五（35）最少，无明显工作日/周末差异，符合 Side Project 特征
- **贡献者：** 主力开发者 zyronon/Zyronon（892 次），另有 wysha-object（28）、王念超（15）、taochen（3）等少量协作者

## 演化轨迹

### 核心文件（Top 10 最常修改）

| 修改次数 | 文件 |
|---------|------|
| 58 | `apps/nuxt/app/pages/(words)/practice-words/[id].vue` |
| 40 | `apps/nuxt/app/pages/setting.vue` |
| 36 | `apps/nuxt/app/pages/(words)/words.vue` |
| 26 | `apps/nuxt/app/composables/useInit.ts` |
| 24 | `pnpm-lock.yaml` |
| 24 | `apps/nuxt/app/components/word/TypeWord.vue` |
| 23 | `package.json` |
| 21 | `apps/vscode/src/extension.ts` |
| 19 | `apps/nuxt/app/pages/(words)/words-test/[id].vue` |
| 18 | `apps/nuxt/i18n/locales/zh.json` |

**解读：** 练习页面（practice-words）以 58 次修改遥遥领先，说明「打字练习」是项目核心功能，经历了大量迭代。设置页面和单词列表紧随其后，反映功能逐步丰富的过程。

### 热点目录

| 修改次数 | 目录 |
|---------|------|
| 1,213 | `apps/nuxt` |
| 1,028 | `apps/vscode-web` |
| 269 | `packages/core` |
| 180 | `src/components`（旧目录） |
| 156 | `vscode-web/src`（旧目录） |
| 88 | `packages/base` |
| 55 | `packages/ui` |
| 50 | `apps/vscode` |

**解读：** 项目采用 monorepo 架构（pnpm workspace），包含 Nuxt Web 应用、VSCode Web 扩展、VSCode 桌面扩展三个端，以及 core/base/ui 三个共享包。Nuxt 端和 VSCode Web 端是开发重心。存在 `src/components` → `packages/core` 的目录迁移痕迹，说明项目在 3 个月内经历了一次架构重构。

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 功能新增（feat/add） | 28 | 14% |
| Bug 修复（fix/bug） | 55 | 27.5% |
| 重构（refactor） | 0 | 0% |
| 文档（doc） | 0 | 0% |
| 测试（test） | 0 | 0% |
| 其他 | 117 | 58.5% |

**解读：** fix 类提交占比最高（27.5%），说明项目处于功能快速迭代 + 持续修缮阶段。「其他」占比大，可能因为大量 commit message 未遵循 conventional commit 规范。无测试和文档类提交，反映了典型的个人项目开发风格。

### 版本发布

| 版本 | 日期 |
|------|------|
| v3.0.1 | 2026-02-25 |
| v3.0.0 | 2026-02-24 |

**解读：** 仅 2 个正式版本，且从 v3.0.0 起步（非 v0.x/v1.x），表明这可能是一个已有前身的项目重构版本（TypeWords v3），或者作者直接采用了较高版本号。两个版本间隔仅 1 天，v3.0.1 为快速修复版。

## 项目画像卡片

```
┌─────────────────────────────────────────────┐
│  TypeWords — 打字练习工具                      │
├─────────────────────────────────────────────┤
│  📏 规模：中型项目（~25K 行业务代码，309 文件）    │
│  ⏱  年龄：3 个月（2026-01 至今）                │
│  📊 节奏：317 commits / 3 月 ≈ 3.5 次/天       │
│  👤 团队：1 人主力 + 3 位少量贡献者              │
│  🏗  架构：Monorepo（Nuxt + VSCode + 共享包）   │
│  🔧 技术栈：Vue 3 / Nuxt / TypeScript / pnpm  │
│  📦 发布：2 个版本（v3.0.0-v3.0.1）             │
│  🔥 状态：密集开发中，日均 3+ 提交               │
│  ⏰ 开发模式：深夜型 Side Project               │
│  ⚠️ 短板：无测试、无文档、commit 规范性不足       │
└─────────────────────────────────────────────┘
```
