## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 32,081（不含空行/注释） |
| 语言分布 | Python 70.2%, Markdown 27.8%, Shell 1.4%, TOML 0.5%, INI 0.04% |
| 代码/注释比 | 2.9:1 |
| 文件数量 | 115 |
| 依赖数量 | 9（runtime） + 11（dev），另有 requirements.txt 列出 11 个包 |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 约 1 个月（首次提交 2025-06-25） |
| 总 commit 数 | 184 |
| 最近提交 | 2025-07-31 |
| 近 30 天 commit | 0（项目已于 2025-07 停止活跃） |
| 近 90 天 commit | 0 |
| 近 365 天 commit | 184 |
| 开发阶段 | 已放弃（最近 commit 距今超过 7 个月，且生命周期仅 36 天即停滞） |
| 开发模式 | 业余 Side Project（周末占比 18.5%，深夜占比 64.7%，高峰时段为凌晨 00-06 点） |

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. claude_indexer/indexer.py — 63 次修改
2. CLAUDE.md — 54 次修改
3. README.md — 48 次修改
4. claude_indexer/storage/qdrant.py — 43 次修改
5. claude_indexer/analysis/parser.py — 40 次修改
6. claude_indexer/cli_full.py — 34 次修改
7. claude_indexer/watcher/handler.py — 32 次修改
8. claude_indexer/main.py — 27 次修改
9. utils/qdrant_stats.py — 22 次修改
10. claude_indexer/analysis/javascript_parser.py — 20 次修改

### 热点目录

1. claude_indexer/analysis — 144 次修改
2. claude_indexer/storage — 78 次修改
3. claude_indexer/indexer.py — 63 次修改
4. docs/archive — 52 次修改
5. claude_indexer/watcher — 47 次修改
6. tests/unit — 39 次修改
7. claude_indexer/config — 39 次修改
8. claude_indexer/embeddings — 35 次修改
9. claude_indexer/cli_full.py — 34 次修改
10. claude_indexer/processing — 33 次修改

### Commit 类型分布

- Feature/Add: 79 (42.9%)
- Fix/Bug: 76 (41.3%)
- Refactor: 12 (6.5%)
- Docs: 8 (4.3%)
- Test: 1 (0.5%)
- Other: 8 (4.3%)

### 版本发布

- 最新版本: 无 Tag / 无 Release
- 总 Release 数: 0
- 版本策略: 无正式发布（pyproject.toml 中声明 version = "1.0.0"，但从未打 tag 或创建 release）

## 项目画像卡片

```
项目: Durafen/Claude-code-memory
年龄: ~1 个月（2025-06-25 → 2025-07-31）  |  代码: 32,081 行 (Python)
总 commits: 184  |  贡献者: 1 人
开发阶段: 已放弃（36 天密集开发后停滞超 7 个月）
开发模式: 业余 Side Project（深夜 64.7%，周末 18.5%，高峰 00-06 点）
核心文件: indexer.py, qdrant.py, parser.py, cli_full.py, handler.py
Release: 无正式发布（共 0 个版本）
```
