# EbookFoundation/free-programming-books 元分析

## 代码规模

| 指标 | 数据 |
|------|------|
| 总行数 | 33,050 行 |
| 语言分布 | Markdown 97.5% (215 文件, 32,179 行), Python 1.8% (1 文件, 605 行), YAML 0.5% (2 文件, 153 行), HTML 0.02% (1 文件, 9 行) |
| 文件数量 | 233 个文件（tokei 统计 219 个可识别文件） |
| 代码行 / 注释行 / 空行 | 577 / 22,137 / 10,336 |

> 备注：这是一个纯文档/awesome-list 类仓库，Markdown 文件占绝对主导。tokei 将 Markdown 内容计为 "comments"（21,964 行），实际上这些都是有效的列表内容。Python 脚本（605 行）用于链接检查等自动化，YAML 用于 GitHub Actions CI 配置。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 149 个月（约 12.4 年，2013-10-10 创建） |
| 总 commit 数 | 10,055 |
| 最近提交 | 2026-03-20 |
| 近 30 天 commit | 15 |
| 近 90 天 commit | 28 |
| 贡献者总数 | 约 3,401 个独立作者 |
| 开发阶段 | 成熟维护期（长尾社区驱动更新，核心框架已稳定） |
| 开发模式 | 大规模社区协作 + Hacktoberfest 年度脉冲 |

### 活跃度趋势

项目经历了两个明显阶段：

1. **爆发建设期（2013-10 ~ 2014-05）**：项目创建首月即获 686 次提交，前 8 个月累计 ~2,000 次提交，大量初始内容涌入
2. **社区维护期（2014-06 ~ 至今）**：月均提交量降至 10-50 次，但每年 10 月出现显著峰值（Hacktoberfest 效应）

### Hacktoberfest 脉冲效应

| 年份 | 10 月提交数 | 对比该年平均月份 |
|------|------------|----------------|
| 2020 | 531 | ~15 (非10月平均) |
| 2021 | 596 | ~20 |
| 2022 | 852 | ~30 |
| 2023 | 594 | ~12 |
| 2024 | 252 | ~9 |
| 2025 | 429 | ~8 |

每年 10 月提交量暴增 20-80 倍，是该项目最显著的开发节奏特征。这是 Hacktoberfest 活动驱动的社区贡献行为。

### 时间分布

- **最活跃时段**：UTC 20:00-23:00（全球分布的贡献者，偏欧美晚间）
- **星期分布**：周一至周五较均匀（1,372-1,614），周末略少（1,226-1,281），但差异不大，说明以个人志愿者为主

### 核心维护者

| 排名 | 贡献者 | 提交数 |
|------|--------|--------|
| 1 | victor felder（含历史名 vhf） | ~1,546 |
| 2 | Mohammad Hossein Mojtahedi | 264 |
| 3 | David Ordás | 161 |
| 4 | Alexander Fefelov | 134 |
| 5 | Victor Λntonio | 131 |

Victor Felder（vhf）是项目创始人兼核心维护者，累计提交约 1,546 次（占总量 15.4%），3,401 位贡献者中绝大多数是一次性贡献者（典型的 awesome-list 贡献模式）。

## 演化轨迹

### 核心文件（Top 10 最常修改）

| 排名 | 文件 | 修改次数 |
|------|------|---------|
| 1 | courses/free-courses-en.md | 484 |
| 2 | books/free-programming-books-langs.md | 294 |
| 3 | courses/free-courses-hi.md | 286 |
| 4 | books/free-programming-books-subjects.md | 196 |
| 5 | more/free-programming-cheatsheets.md | 129 |
| 6 | courses/free-courses-bn.md | 74 |
| 7 | .github/workflows/check-urls.yml | 60 |
| 8 | courses/free-courses-pt_BR.md | 56 |
| 9 | more/free-programming-playgrounds.md | 51 |
| 10 | more/free-programming-interactive-tutorials-en.md | 50 |

> 英文课程列表和编程语言书籍列表是修改最频繁的两个文件，反映了英语内容的主导地位。印地语（hi）和孟加拉语（bn）课程列表的高排名说明南亚社区贡献活跃。

### 热点目录

| 排名 | 目录 | 修改次数 |
|------|------|---------|
| 1 | courses/free-courses-en.md | 739 |
| 2 | books/free-programming-books-langs.md | 488 |
| 3 | courses/free-courses-hi.md | 363 |
| 4 | books/free-programming-books-subjects.md | 294 |
| 5 | more/free-programming-cheatsheets.md | 195 |
| 6 | .github/workflows | 115 |
| 7 | courses/free-courses-pt_BR.md | 101 |
| 8 | courses/free-courses-bn.md | 99 |
| 9 | courses/free-courses-id.md | 94 |
| 10 | more/free-programming-interactive-tutorials-en.md | 89 |

内容按类型组织在 `books/`、`courses/`、`more/` 三个主目录下，CI/CD 工作流（`.github/workflows`）也是高频修改区域（115 次），说明链接检查等自动化机制持续被改进。

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 功能/新增 (feat/add) | 121 | 60.5% |
| 修复 (fix/bug) | 24 | 12.0% |
| 文档 (doc) | 1 | 0.5% |
| 重构 (refactor) | 0 | 0% |
| 测试 (test) | 0 | 0% |
| 其他 | 54 | 27.0% |

> 提交以"新增资源"（Add/feat）为绝对主导（60.5%），修复类主要是"修复断链"（Fix broken link），符合 awesome-list 仓库的典型贡献模式。"其他"类多为 Update（更新现有条目）和 chore（依赖升级等维护操作）。

### 版本发布

无 Git tag，无 GitHub Release。这是合理的——作为一个持续更新的资源列表，不存在传统意义上的"版本"概念。

## 项目画像卡片

```
┌─────────────────────────────────────────────────────────────┐
│  EbookFoundation/free-programming-books                     │
│  "互联网上最大的免费编程学习资源列表"                           │
├─────────────────────────────────────────────────────────────┤
│  类型: 文档/Awesome-list     语言: Markdown (97.5%)          │
│  规模: 33K 行 / 233 文件     历史: 12.4 年 / 10,055 commits  │
│  贡献者: 3,401 人            核心维护: Victor Felder          │
├─────────────────────────────────────────────────────────────┤
│  开发阶段: 成熟维护期                                         │
│  开发模式: 大规模社区协作 + Hacktoberfest 年度脉冲              │
│  更新频率: 常规月 ~10 次, Hacktoberfest 月 250-850 次          │
│  活跃度:   近 30 天 15 commits, 近 90 天 28 commits           │
├─────────────────────────────────────────────────────────────┤
│  特征:                                                       │
│  · 无版本发布，持续滚动更新                                    │
│  · 60%+ 提交为新增资源，12% 为修复断链                         │
│  · 英语内容占主导，印地语/孟加拉语/葡语/印尼语社区活跃           │
│  · 每年 10 月 Hacktoberfest 带来 20-80x 提交量脉冲             │
│  · 3,401 位贡献者中绝大多数为一次性贡献                        │
└─────────────────────────────────────────────────────────────┘
```
