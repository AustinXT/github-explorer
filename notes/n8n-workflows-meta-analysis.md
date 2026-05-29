# Zie619/n8n-workflows 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 1,156,391（不含空行/注释） |
| 语言分布 | JSON 98.6%, Python 0.52%, JavaScript 0.27%, SQL 0.09%, YAML 0.07%, 其他 0.45% |
| 代码/注释比 | 196:1 |
| 文件数量 | 2,157 |
| 依赖数量 | 11（runtime，Python pip） |

**说明：** 代码量极高（超百万行），但绝大部分是 JSON 工作流定义文件（2,075 个 JSON 文件，占 98.6%）。实际手写代码（Python 6,056 行 + JavaScript 1,458 行 + Shell 681 行等）约 1.1 万行。注释极少（5,884 行），代码/注释比高达 196:1，说明文档化程度很低，但考虑到 JSON 文件无法注释，这是合理的。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 9 个月（首次提交 2025-05-14） |
| 总 commit 数 | 151 |
| 最近提交 | 2026-02-11 |
| 近 30 天 commit | 0 |
| 近 90 天 commit | 18 |
| 近 365 天 commit | 151（全部） |
| 开发阶段 | 低维护（最近 30 天无 commit，上次活跃在 2 月中旬） |
| 开发模式 | 业余 Side Project（周末占比 25.2%，深夜占比 19.9%） |

### 月度 Commit 分布

| 月份 | Commit 数 | 活跃度 |
|------|-----------|--------|
| 2025-05 | 5 | 项目启动 |
| 2025-06 | 38 | **密集开发期** |
| 2025-07 | 10 | 放缓 |
| 2025-08 | 21 | 中等活跃 |
| 2025-09 | 20 | 中等活跃 |
| 2025-10 | 1 | 几乎停滞 |
| 2025-11 | 36 | **第二波密集开发** |
| 2025-12 | 2 | 低活跃 |
| 2026-01 | 15 | 中等活跃 |
| 2026-02 | 3 | 低活跃 |

**分析：** 项目呈波浪式开发节奏，有两次密集开发期（2025-06 和 2025-11），中间穿插低活跃期。目前处于低维护状态，最近一个月无新提交。

### 每周 Commit 分布

| 星期 | Commit 数 |
|------|-----------|
| 周一 | 52（**最活跃**） |
| 周二 | 16 |
| 周三 | 27 |
| 周四 | 6 |
| 周五 | 12 |
| 周六 | 19 |
| 周日 | 19 |

**分析：** 周一提交量异常高（占 34.4%），可能是周末积累的工作在周一集中 push。周末合计 25.2%，深夜（22:00-06:00）占比 19.9%，整体呈业余 Side Project 模式，但有一定的工作日开发习惯。

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. README.md — 22 次修改
2. workflow_db.py — 10 次修改
3. .github/workflows/ci-cd.yml — 10 次修改
4. Dockerfile — 9 次修改
5. .gitignore — 9 次修改
6. static/index.html — 8 次修改
7. generate_documentation.py — 8 次修改
8. context/search_categories.json — 8 次修改
9. api_server.py — 8 次修改
10. requirements.txt — 7 次修改

### 热点目录

1. Documentation/Manual — 3,128 次变更
2. workflows/Manual — 1,877 次变更
3. Documentation/Splitout — 1,552 次变更
4. Documentation/Code — 1,464 次变更
5. Documentation/Http — 1,408 次变更
6. workflows_backup/Manual — 1,169 次变更
7. Documentation/Telegram — 952 次变更
8. workflows/Splitout — 938 次变更
9. workflows/Code — 874 次变更
10. Documentation/Wait — 832 次变更

**分析：** 热点集中在 Documentation/ 和 workflows/ 目录，说明项目核心活动是不断整理、分类和文档化 n8n 工作流。Manual 类别变更最频繁，是最大的工作流集合。

### Commit 类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| Feature/Add | 53 | 35.1% |
| Fix/Bug | 43 | 28.5% |
| Refactor | 4 | 2.6% |
| Docs | 3 | 2.0% |
| Test | 1 | 0.7% |
| Other | 47 | 31.1% |

**分析：** Feature 和 Fix 占比较高（63.6%），说明项目处于积极功能开发和问题修复阶段。测试提交极少（仅 1 次），测试覆盖可能不足。"Other" 类别偏高（31.1%），提交消息规范性一般。

### 版本发布

- 最新版本：dmca-compliance-2025-08-14（2025-08-14）
- 总 Release 数：1
- 版本策略：无规律（仅有 1 个 DMCA 合规相关 release，非常规版本发布）

**说明：** 唯一的 release 是"Repository History Rewrite - DMCA Compliance"，这是一次因 DMCA 合规要求进行的仓库历史重写操作，并非功能版本发布。该项目不采用传统的版本发布策略。

### 贡献者

| 排名 | 贡献者 | Commit 数 |
|------|--------|-----------|
| 1 | Eliad Shahar | 50 |
| 2 | zie619 | 26 |
| 3 | Praveen Mudalgeri | 8 |
| 4 | root | 8 |
| 5 | Claude（AI） | 3 |
| 其他 | 36 位贡献者 | 合计 56 |

**分析：** 总贡献者 41 人，但核心开发者仅 2 人（Eliad Shahar 和 zie619），合计贡献 50.3%。其余大量贡献者每人仅 1-3 次提交，可能是社区贡献或自动化提交。值得注意的是有 AI 辅助开发（Claude 3 次提交）。

## 项目画像卡片

```
项目: Zie619/n8n-workflows
年龄: 9 个月  |  代码: 1,156,391 行 (JSON 98.6%, Python 0.5%)
总 commits: 151  |  贡献者: 41 人
开发阶段: 低维护（近 30 天无 commit）
开发模式: 业余 Side Project（周末占比 25.2%，深夜占比 19.9%）
核心文件: README.md, workflow_db.py, ci-cd.yml, Dockerfile, api_server.py
Release: dmca-compliance-2025-08-14 (共 1 个版本，非常规发布)
特征: n8n 工作流集合库，含 2,075 个 JSON 工作流文件 + Python API 服务
```
