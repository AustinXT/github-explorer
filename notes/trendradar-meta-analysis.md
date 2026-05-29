# sansan0/TrendRadar 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 36,511（不含空行/注释） |
| 语言分布 | Python 74.6%, JavaScript 14.8%, CSS 3.7%, HTML 1.8%, YAML 1.4%, Batch 0.9%, SQL 0.5%, Shell 0.4%, Dockerfile 0.2%, TOML 0.1% |
| 代码/注释比 | 9.8:1（源代码注释 3,723 行，不含 Markdown 文档） |
| 文件数量 | 95 |
| 依赖数量 | 10（runtime，通过 pyproject.toml 管理；含 requests, pytz, PyYAML, fastmcp, websockets, boto3, feedparser, litellm, json-repair, tenacity） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 11 个月（首次提交 2025-04-28） |
| 总 commit 数 | 211 |
| 最近提交 | 2026-03-18 |
| 近 30 天 commit | 3 |
| 近 90 天 commit | 28 |
| 开发阶段 | 低维护期（近 3 个月月均 ~7 次提交，较高峰期明显下降） |
| 开发模式 | 业余 Side Project（周末占比 25.1%，深夜 22:00-06:00 占比仅 1.4%；高峰时段为 19:00 占 29.4%，属于下班后开发模式） |

### 月度 Commit 分布

| 月份 | Commit 数 | 阶段 |
|------|----------|------|
| 2025-04 | 2 | 项目启动 |
| 2025-05 | 11 | 早期开发 |
| 2025-06 | 39 | **密集开发期** |
| 2025-07 | 13 | 稳定维护 |
| 2025-08 | 19 | 稳定维护 |
| 2025-09 | 23 | 密集开发 |
| 2025-10 | 29 | 密集开发 |
| 2025-11 | 30 | **密集开发期** |
| 2025-12 | 22 | 密集开发 |
| 2026-01 | 17 | 稳定维护 |
| 2026-02 | 3 | 低维护 |
| 2026-03 | 3 | 低维护（月未结束） |

### 工作时间分析

- 最活跃时段：19:00（62 次，29.4%）> 13:00（30 次）> 21:00（20 次）
- 典型的"下班后 + 午休"开发节奏
- 周一至周五贡献 158 次（74.9%），周末贡献 53 次（25.1%）
- 贡献者几乎为单人（sansan 209 次 / 211 次 = 99.1%），另有 2 位一次性贡献者

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. readme.md — 106 次修改
2. version — 52 次修改
3. main.py — 48 次修改（后重构至 trendradar 包）
4. README-EN.md — 43 次修改
5. README.md — 41 次修改
6. config/config.yaml — 37 次修改
7. .github/workflows/crawler.yml — 20 次修改
8. docker/docker-compose.yml — 18 次修改
9. docker/.env — 18 次修改
10. trendradar/__init__.py — 17 次修改

### 热点目录

1. trendradar/ — 203 次修改（核心应用代码）
2. mcp_server/ — 92 次修改（MCP 服务端）
3. docker/ — 81 次修改（容器化部署）
4. config/ — 63 次修改（配置文件）
5. .github/ — 47 次修改（CI/CD 工作流）
6. _image/ — 35 次修改（图片资源）
7. docs/ — 11 次修改（文档站点）
8. output/ — 7 次修改（输出数据）

### Commit 类型分布（最近 200 条）

- Feature/Add: 15 (7.5%)
- Fix/Bug: 31 (15.5%)
- Refactor: 1 (0.5%)
- Docs: 53 (26.5%)
- Test: 0 (0%)
- Other: 100 (50.0%)

> 注：大量 "Other" 类型提交说明项目不严格遵循 Conventional Commits 规范，许多提交消息为中文描述性更新。文档类提交占比高（26.5%），说明作者重视项目文档维护。修复类（15.5%）多于新特性（7.5%），表明项目已进入功能稳定、以修复和维护为主的阶段。

### 版本发布

- 最新版本: v6.5.0（2026-03-12）
- 总 Tag 数: 50（含 40 个主版本 tag + 10 个 mcp-v 前缀 tag）
- 版本策略: 语义化版本（Semantic Versioning），主版本从 v1.4.1 演进至 v6.5.0；MCP 模块有独立版本线（mcp-v1.1.0 至 mcp-v4.0.0）
- 无 GitHub Release（仅使用 Git Tag）

## 项目画像卡片

```
项目: sansan0/TrendRadar
年龄: 11 个月  |  代码: 36,511 行 (Python 74.6%)
总 commits: 211  |  贡献者: 3 人（实际核心 1 人）
开发阶段: 低维护（高峰已过，从密集开发转入维护期）
开发模式: 业余 Side Project（下班后 19:00 高峰，周末占 25%）
核心文件: main.py, trendradar/__init__.py, config/config.yaml, mcp_server/server.py
Release: v6.5.0 (共 50 个 Tag，双版本线)
```
