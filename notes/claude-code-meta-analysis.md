# anthropics/claude-code 元分析报告

> 分析日期：2026-03-22 | 数据来源：本地克隆仓库 git 历史

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 3,182（不含空行/注释，纯代码文件） |
| 语言分布 | Shell 42.4%, Python 28.7%, TypeScript 18.8%, JSON 7.1%, PowerShell 3.1% |
| 代码/注释比 | 7.9:1（纯代码文件；项目含大量 Markdown 文档 13,849 行） |
| 文件数量 | 143（其中 Markdown 97 个，代码文件 46 个） |
| 依赖数量 | 0（无 package.json/requirements.txt 等依赖清单文件） |

**说明**：该项目本质上是一个以 Markdown 文档为核心的「插件/技能集合」项目，代码主要为 Shell 脚本、Python 脚本和 TypeScript 工具脚本，并非传统意义上的软件工程项目。Markdown 文档（插件定义、命令模板、工作流配置等）是项目的核心产出。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 13 个月（首次提交 2025-02-22） |
| 总 commit 数 | 563 |
| 最近提交 | 2026-03-20 |
| 近 30 天 commit | 51 |
| 近 90 天 commit | 158 |
| 近 365 天 commit | 561 |
| 开发阶段 | 密集开发（月均 ~43 次提交，近期持续高频更新） |
| 开发模式 | 职业项目（周末占比 8.7%，深夜 22:00-06:00 占比 33.4%） |

### 月度 commit 分布

```
2025-02:   1    ▏
2025-03:   1    ▏
2025-04:  15    ██
2025-05:  31    ████
2025-06:  26    ███▌
2025-07:  57    ████████
2025-08:  77    ██████████▌  ← 峰值
2025-09:  45    ██████
2025-10:  58    ████████
2025-11:  56    ███████▌
2025-12:  38    █████
2026-01:  66    █████████
2026-02:  70    █████████▌
2026-03:  22    ███ (截至 3/20)
```

**开发节奏分析**：
- 2025-02/03 为项目初始化阶段（极少提交）
- 2025-04 开始进入正式开发，2025-07/08 达到首个高峰
- 2025-09 之后维持在每月 38-70 次的高频开发状态
- 2026-01/02 出现第二个开发高峰（月均 68 次），表明项目仍在积极演进
- 该项目没有明显的停滞期，属于持续活跃项目

### 贡献者构成（Top 10）

| 贡献者 | Commit 数 |
|--------|----------|
| GitHub Actions | 266 |
| Boris Cherny | 88 |
| Claude | 52 |
| Ashwin Bhat | 34 |
| ant-kurt | 21 |
| Franklin Volcic | 20 |
| Chris Lloyd | 13 |
| Octavian Guzu | 13 |
| Kurt Carpenter | 10 |
| bogini | 9 |

**注意**：GitHub Actions（自动化）占总提交的 47.2%，说明项目高度依赖 CI/CD 自动化流程（如自动更新 CHANGELOG、自动发布等）。排除自动化后，人工提交约 297 次。此外 Claude（AI）贡献了 52 次提交。总贡献者 64 人。

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. CHANGELOG.md — 270 次修改
2. plugins/code-review/commands/code-review.md — 23 次修改
3. README.md — 16 次修改
4. .github/workflows/claude-issue-triage.yml — 16 次修改
5. .github/workflows/claude-dedupe-issues.yml — 14 次修改
6. .claude-plugin/marketplace.json — 13 次修改
7. .github/workflows/oncall-triage.yml — 11 次修改
8. scripts/auto-close-duplicates.ts — 9 次修改
9. .github/workflows/auto-close-duplicates.yml — 9 次修改
10. .devcontainer/init-firewall.sh — 9 次修改

**洞察**：CHANGELOG.md 修改 270 次（几乎每次发版自动更新），是 GitHub Actions 自动提交的主要目标。真正反映人工开发重心的是 code-review 插件和 GitHub Actions 工作流配置。

### 热点目录

1. .github/workflows — 89 次修改
2. plugins/plugin-dev — 58 次修改
3. plugins/code-review — 26 次修改
4. plugins/hookify — 24 次修改
5. .claude/commands — 15 次修改
6. plugins/ralph-wiggum — 12 次修改
7. plugins/agent-sdk-dev — 11 次修改
8. plugins/pr-review-toolkit — 9 次修改
9. plugins/feature-dev — 9 次修改
10. .devcontainer — 9 次修改

**洞察**：`.github/workflows` 是绝对热点，说明项目在 CI/CD 和 Issue 自动化治理上投入大量精力。`plugins/` 目录下的各个插件是核心业务代码，其中 `plugin-dev`（插件开发指南）和 `code-review`（代码审查）是最活跃的两个插件。

### Commit 类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| Feature/Add | 64 | 11.4% |
| Fix/Bug | 49 | 8.7% |
| Refactor | 2 | 0.4% |
| Docs | 14 | 2.5% |
| Test | 3 | 0.5% |
| Other | 431 | 76.6% |

**说明**：Other 占比极高（76.6%），因为大量提交使用 `chore:` 前缀（如 `chore: Update CHANGELOG.md`，由 GitHub Actions 自动生成）以及其他非标准前缀。实际功能性提交中，Feature 和 Fix 比例大致为 1.3:1，说明项目仍以新功能开发为主，同时保持适度的问题修复。

### 版本发布

- 最新版本：v2.1.81（2026-03-20）
- 最早版本：v2.0.73（2025-12-19）
- 总 Release 数：66
- 总 Tag 数：67
- 版本策略：语义化版本（Semantic Versioning），从 v2.0.73 到 v2.1.81，主版本稳定在 2.x，次版本从 0 升至 1，补丁版本频繁递增。发布节奏极高，近期几乎每天一个版本。

## 项目画像卡片

```
项目: anthropics/claude-code
年龄: 13 个月  |  代码: 3,182 行 (Shell/Python/TypeScript) + 13,849 行文档
总 commits: 563  |  贡献者: 64 人（含 GitHub Actions 自动化 266 次）
开发阶段: 密集开发（月均 43 次提交，无停滞期）
开发模式: 职业项目（周末仅 8.7%，深夜 33.4% — 全球分布式团队的时区特征）
核心文件: CHANGELOG.md, plugins/code-review/*, .github/workflows/*
Release: v2.1.81 (共 66 个版本，语义化版本，近期日更节奏)
```

**总体判断**：这是 Anthropic 官方维护的 Claude Code 插件生态项目，本质上是一个「文档驱动」的插件/技能集合仓库。项目处于高速发展期，以 Markdown 定义的插件、命令模板和 GitHub Actions 工作流为核心，辅以少量脚本工具。高频发布（日更级别）、大量自动化提交、全球分布式团队协作是其显著特征。
