# abhigyanpatwari/GitNexus 元分析报告

## 代码规模

| 指标 | 数值 |
|------|------|
| 总文件数 | 1,478 |
| 总行数 | 135,397 |
| 代码行数 | 104,479 |
| 注释行数 | 15,350 |
| 空行数 | 15,568 |
| 语言数量 | 24 |
| 注释率 | 12.8% |

### 语言分布（按代码行数 Top 10）

| 语言 | 代码行 | 占比 |
|------|--------|------|
| TypeScript | 70,021 | 67.0% |
| TSX | 6,521 | 6.2% |
| JSON | 16,569 | 15.9% |
| Python | 2,066 | 2.0% |
| JavaScript | 1,787 | 1.7% |
| C# | 1,080 | 1.0% |
| PHP | 975 | 0.9% |
| Rust | 915 | 0.9% |
| Java | 776 | 0.7% |
| Kotlin | 672 | 0.6% |

> **主导语言**：TypeScript 占绝对主导（67%），项目是一个 TypeScript 为核心的代码分析工具。多语言文件（C/C++/C#/Go/Java/Kotlin/PHP/Python/Ruby/Rust/Swift）主要存在于 test fixtures 中，用于测试代码解析能力。

## 开发节奏

| 指标 | 数值 |
|------|------|
| 首次提交 | 2026-01-03（标记为 "GitNexus V2 - Complete refactor"） |
| 最近提交 | 2026-03-21 |
| 项目跨度 | 77 天（11 周） |
| 总 Commit 数 | 389 |
| 活跃天数 | 60 天 |
| 平均每活跃日 Commit | 6.4 |

### 月度提交分布

| 月份 | Commit 数 | 占比 |
|------|-----------|------|
| 2026-01 | 100 | 25.7% |
| 2026-02 | 156 | 40.1% |
| 2026-03 | 133 | 34.2% |

> 2 月是开发高峰期，3 月（截至 21 日）仍保持高强度。项目整体呈加速趋势。

### 星期提交分布

| 星期 | Commit 数 | 活跃度 |
|------|-----------|--------|
| 周一 | 39 | ▓▓▓░░ |
| 周二 | 49 | ▓▓▓▓░ |
| 周三 | 57 | ▓▓▓▓░ |
| 周四 | 63 | ▓▓▓▓▓ |
| 周五 | 68 | ▓▓▓▓▓ |
| 周六 | 50 | ▓▓▓▓░ |
| 周日 | 63 | ▓▓▓▓▓ |

> 全周均有提交，周四/周五/周日最活跃。典型的高强度开源项目模式，开发者在工作日和周末均投入。

### 贡献者分布

| 贡献者 | Commit 数 |
|--------|-----------|
| abhigyanpatwari | 216 (合并两个身份) |
| Gergo Magyar / Gary Magyar | 76 |
| Paul Robello | 17 |
| Güneş Bizim | 14 |
| Zander Raycraft | 12 |
| Linus Beckhaus | 8 |
| jandyx | 7 |
| 其他 (6人) | 39 |

> 核心维护者 abhigyanpatwari 贡献了约 55% 的 commit，Gergo/Gary Magyar 贡献约 20%。项目有约 15 位贡献者，是一个有活跃社区参与的小型团队项目。

## 演化轨迹

### 版本发布

| 版本 | 日期 | 说明 |
|------|------|------|
| v1.4.7 (Latest) | 2026-03-19 | CI 修复 |
| v1.4.6 | 2026-03-18 | - |
| v1.4.5 | 2026-03-17 | - |
| v1.4.0 | 2026-03-13 | 主要版本升级 |
| v1.3.11 | 2026-03-08 | - |
| v1.3.10 | 2026-03-07 | - |
| v1.2.8 | 更早 | - |

> 7 个版本标签，6 个正式 Release。3 月中旬进入快速迭代期（v1.4.0 → v1.4.7，一周内 4 个版本）。

### 核心文件（变更最频繁 Top 10）

| 文件 | 变更次数 |
|------|----------|
| README.md | 46 |
| gitnexus/package.json | 46 |
| gitnexus/src/core/ingestion/workers/parse-worker.ts | 37 |
| gitnexus/src/core/ingestion/call-processor.ts | 37 |
| gitnexus/src/core/ingestion/parsing-processor.ts | 32 |
| CLAUDE.md | 30 |
| AGENTS.md | 30 |
| gitnexus/package-lock.json | 29 |
| gitnexus/src/core/ingestion/pipeline.ts | 28 |
| gitnexus/src/core/ingestion/import-processor.ts | 28 |

> 核心热点集中在 `gitnexus/src/core/ingestion/` 目录下的解析和处理管线，这是项目的引擎核心。`CLAUDE.md` 和 `AGENTS.md` 的高频变更表明项目深度使用 AI 辅助开发。

### 热点目录（变更最频繁 Top 10）

| 目录 | 变更次数 |
|------|----------|
| gitnexus/test | 1,521 |
| gitnexus/src | 945 |
| gitnexus-web/src | 185 |
| src/core | 107 |
| gitnexus-cli/src | 80 |
| .github/workflows | 58 |
| src/components | 54 |
| gitnexus/skills | 53 |
| gitnexus-mcp/src | 52 |
| gitnexus/package.json | 46 |

> 测试代码变更量（1,521）远超源码（945），说明项目高度重视测试质量。多个子项目（gitnexus-web、gitnexus-cli、gitnexus-mcp）表明这是一个 monorepo 结构。

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| Fix/Bug | 90 | 45.0% |
| Feature/Add | 71 | 35.5% |
| Test | 5 | 2.5% |
| Refactor | 3 | 1.5% |
| Docs | 2 | 1.0% |
| Other | 29 | 14.5% |

> Fix 类提交（45%）略多于 Feature（35.5%），项目处于快速迭代阶段——大量新功能开发伴随着频繁的缺陷修复，符合高速成长期项目的典型模式。

## 项目画像卡片

```
┌─────────────────────────────────────────────────────────────┐
│  abhigyanpatwari/GitNexus                                   │
│  代码仓库静态分析引擎 + MCP Server                            │
├─────────────────────────────────────────────────────────────┤
│  规模: 104K 代码行 / 1,478 文件 / 24 语言                     │
│  核心: TypeScript (67%) + 多语言测试 fixtures                 │
│  架构: Monorepo (gitnexus / gitnexus-web / cli / mcp)        │
├─────────────────────────────────────────────────────────────┤
│  节奏: 389 commits / 77 天 / 5.1 commits/天                  │
│  版本: 7 tags, v1.2.8 → v1.4.7 (快速迭代)                    │
│  团队: ~15 贡献者, 核心 2 人 (75% commits)                    │
├─────────────────────────────────────────────────────────────┤
│  引擎核心: ingestion pipeline (parse → call → import)        │
│  测试文件变更数 1.6x 于源码，测试驱动开发                       │
│  AI 辅助开发 (CLAUDE.md/AGENTS.md 高频变更)                   │
├─────────────────────────────────────────────────────────────┤
│  阶段: 快速成长期 (v2 重构后密集迭代)                          │
│  特征: Fix 45% > Feature 36%, 高密度缺陷修复                  │
│  趋势: 月均 130 commits, 1 月加速, 3 月持续                   │
└─────────────────────────────────────────────────────────────┘
```
