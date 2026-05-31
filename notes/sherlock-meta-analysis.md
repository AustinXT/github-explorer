# sherlock-project/sherlock — Phase 2: Meta Analysis

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 6,371 行（不含空行/注释） |
| 语言分布 | Python 27%, JSON 54%, Markdown 13%, 其他 6% |
| 代码/注释比 | 6.3:1 |
| 文件数量 | 27 个（17 Python, 2 JSON, 4 Markdown, 2 INI, 1 TOML, 1 Dockerfile） |
| 依赖数量 | 16 个（runtime 11 + dev 4 + ci 1） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 89 个月（首次提交 2018-12-24） |
| 总 commit 数 | 2,919 |
| 最近提交 | 2026-05-09 |
| 近 30 天 commit | 1 |
| 近 90 天 commit | 1 |
| 开发阶段 | 稳定维护 |
| 开发模式 | 业余 Side Project（深夜提交 18%） |

## 演化轨迹

### 核心文件（Top 10 最常修改）
1. `sherlock/resources/data.json` — 561 次修改
2. `data.json` — 492 次修改
3. `sherlock_project/resources/data.json` — 222 次修改
4. `sherlock.py` — 194 次修改
5. `removed_sites.md` — 191 次修改
6. `sites.md` — 188 次修改
7. `README.md` — 172 次修改
8. `sherlock/sherlock.py` — 138 次修改
9. `removed_sites.json` — 120 次修改
10. `data_bad_site.json` — 45 次修改

### 热点目录
1. `sherlock/resources` — 576 次修改
2. `sherlock_project/resources` — 224 次修改
3. `sherlock/sherlock.py` — 138 次修改
4. `.github/workflows` — 79 次修改
5. `.github/ISSUE_TEMPLATE` — 39 次修改
6. `sherlock/tests` — 36 次修改

### Commit 类型分布
- Feature/Add: 76 (38%)
- Fix/Bug: 53 (26.5%)
- Refactor: 0 (0%)
- Docs: 0 (0%)
- Test: 1 (0.5%)
- Other: 70 (35%)

### 版本发布
- 最新版本: v0.16.0（2025-09-16）
- 总 Release 数: 3
- 版本策略: 语义化版本（SemVer）

## 项目画像卡片

项目: sherlock-project/sherlock
年龄: 89 个月  |  代码: 6,371 行 (Python/JSON)
总 commits: 2,919  |  贡献者: 330 人
开发阶段: 稳定维护
开发模式: 业余 Side Project
核心文件: sherlock.py, resources/data.json
Release: v0.16.0 (共 3 个版本)