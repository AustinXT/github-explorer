# MustardChef/WSABuilds 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 8,970（不含空行/注释） |
| 语言分布 | Python 33.5%, Shell 29.2%, XML 25.5%, PowerShell 10.0%, Batch 0.2%, HTML 0.1%, Markdown（文档）6,007 行注释 |
| 代码/注释比 | 1.09:1（代码 8,970 行 vs 注释 8,250 行） |
| 文件数量 | 237 |
| 依赖数量 | 2（requests, packaging —— Python 依赖） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 51 个月（2021-10-26 至 2026-01-16） |
| 总 commit 数 | 1,458（主分支） |
| 最近提交 | 2026-01-16 |
| 近 30 天 commit | 0 |
| 近 90 天 commit | 9 |
| 开发阶段 | 维护/存档期 — 微软已于 2024 年 3 月正式停止 WSA 支持，项目转入 LTS 长期维护模式，发布频率大幅下降 |
| 开发模式 | 脉冲式开发 — 以集中发布为驱动，围绕 WSA 版本更新出现活跃高峰（2022-08/09、2023-01/04/08、2023-12），之后迅速回落；近期仅做 Hotfix 级别修复 |

### 活跃度趋势

- **爆发期**（2021-10 ~ 2023-12）：月均 ~45 次 commit，高峰月份超 100 次（2022-09: 122, 2023-04: 135, 2023-08: 116, 2023-01: 115）
- **衰减期**（2024-01 ~ 2024-07）：月均 ~12 次 commit，活跃度断崖式下降
- **静默期**（2024-08 ~ 2024-11）：完全无提交，长达 4 个月空窗
- **LTS 维护期**（2024-12 ~ 至今）：零星提交用于 LTS 构建和 Hotfix

### 开发时间偏好

- **高峰时段**：UTC 21:00（126 次）、19:00（116 次）、22:00（111 次）— 典型的业余/晚间开发者模式
- **低谷时段**：UTC 04:00-08:00 — 凌晨极少提交
- **工作日分布**：周五最活跃（253 次），周六最少（170 次），工作日与周末差异不大

## 演化轨迹

### 核心文件（Top 10 最常修改）

| 排名 | 文件 | 修改次数 |
|------|------|----------|
| 1 | README.md | 534 |
| 2 | .github/workflows/magisk.yml | 143 |
| 3 | scripts/build.sh | 72 |
| 4 | scripts/run.sh | 69 |
| 5 | .github/workflows/build.yaml | 45 |
| 6 | OldBuilds.md | 34 |
| 7 | .github/workflows/update.yml | 30 |
| 8 | .github/workflows/build.yml | 23 |
| 9 | README_CN.md | 22 |
| 10 | .github/workflows/buildarm64.yml | 21 |

**分析**：README.md 修改次数高达 534 次，占总 commit 的 37%，说明项目高度依赖文档驱动（发布说明、下载链接更新）。CI/CD 工作流文件（magisk.yml、build.yaml 等）是第二大修改热点，体现了构建自动化的持续迭代。

### 热点目录

| 排名 | 目录 | 修改次数 |
|------|------|----------|
| 1 | MagiskOnWSAOld/libhoudini | 1,185 |
| 2 | MagiskOnWSA/libhoudini | 1,185 |
| 3 | .github/workflows | 328 |
| 4 | Documentation/Usage Guides | 150 |
| 5 | Documentation/Fix Guides | 95 |
| 6 | MagiskOnWSA/DLL | 84 |
| 7 | Guides/Post-Installation Guides | 84 |
| 8 | MagiskOnWSA/scripts | 63 |
| 9 | MagiskOnWSA/cacerts | 63 |
| 10 | Documentation/WSABuilds | 52 |

**分析**：libhoudini（ARM 翻译层）目录以 1,185 次修改遥遥领先，这是项目的核心技术资产。CI/CD 工作流（328 次）和文档目录（Usage Guides 150 次 + Fix Guides 95 次）紧随其后。

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 更新/升级 (Update) | 46 | 23.0% |
| 文档 (Docs) | 33 | 16.5% |
| 合并 (Merge) | 32 | 16.0% |
| 修复 (Fix/Bug) | 24 | 12.0% |
| 新功能 (Feature/Add) | 13 | 6.5% |
| 其他 | 52 | 26.0% |

**分析**：项目以更新升级（23%）和文档维护（16.5%）为主，修复类占 12%，新功能仅 6.5%，符合成熟维护期项目的 commit 特征。大量 Merge commit 表明采用 Pull Request 协作模式。

### 版本发布

| 指标 | 数据 |
|------|------|
| 总 Tag 数 | 135 |
| 总 Release 数 | 100+ |
| 最新 Release | 2026-01-04 — WSABuilds LTS Build #7 Hotfix（Libhoudini ARM 翻译层修复） |
| 发布模式 | 多平台矩阵发布 — 每个版本同时发布 Windows 10 x64、Windows 11 x64、Windows 11 arm64 三个变体 |
| 版本命名 | Windows_{版本}_{WSA版本号}_{LTS编号/变体}_{架构} |

**近期发布时间线**：
- 2026-01-04：LTS Build #7 Hotfix（Libhoudini 修复）
- 2025-06-02：v2407.40000.4.0 v2 + LTS Build #7
- 2024-12-09：v2407.40000.4.0 首发

## 项目画像卡片

```
┌─────────────────────────────────────────────────────┐
│  MustardChef/WSABuilds                              │
│  Windows Subsystem for Android 自定义构建分发项目    │
├─────────────────────────────────────────────────────┤
│  规模：小型（8,970 行代码 / 237 文件）               │
│  语言：Python + Shell + PowerShell（构建脚本为主）    │
│  年龄：51 个月（2021-10 ~ 2026-01）                  │
│  活跃：1,458 commits / 135 tags / 100+ releases     │
│  状态：LTS 维护模式（近 90 天仅 9 次提交）           │
│  模式：文档驱动 + CI/CD 自动化构建 + 多平台分发      │
│  核心：libhoudini ARM 翻译层 + Magisk 集成脚本      │
│  节奏：从脉冲式高频开发转入低频 LTS 维护             │
│  协作：Pull Request 合并模式，社区贡献型             │
│  特征：非传统软件项目，更像"构建分发平台"            │
│        代码/注释比接近 1:1，文档占比极高              │
│        README 修改占总 commit 的 37%                 │
└─────────────────────────────────────────────────────┘
```
