## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 484,029（不含空行/注释） |
| 语言分布 | Rust 78.7%, JSON 16.3%, Python 1.4%, TOML 1.3%, YAML 1.2%, Markdown 0.05%, 其他 1.05% |
| 代码/注释比 | 7.6:1 |
| 文件数量 | 1,093 |
| 依赖数量 | 761（Cargo.lock 中的 package 数） |
| 工作空间 crate 数 | 68 |

**解读**：48 万行代码的 Rust 项目，规模极大。代码/注释比 7.6:1 表明项目以代码实现为主，注释相对精简，符合 Rust 社区「代码即文档」+类型系统自文档的风格。68 个内部 crate 说明项目高度模块化，架构组织成熟。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 30 个月（首次提交 2023-10-05） |
| 总 commit 数 | 8,846 |
| 最近提交 | 2026-04-05 |
| 近 30 天 commit | 234 |
| 近 90 天 commit | 767 |
| 近 365 天 commit | 2,624 |
| 开发阶段 | 密集开发（月均 295 commits） |
| 开发模式 | 职业项目（周末占比 12.8%，深夜占比 14.9%） |

**解读**：30 个月产出 8,846 次提交，月均近 300 次，这是极高强度的职业化开发。周末提交仅占 12.8%，深夜提交 14.9%，典型的全职工程团队节奏。从月度趋势看，2024 年 7-8 月达到高峰（月 500-600 commits），此后稳定在 150-285 之间，进入「高产出稳定维护」阶段，但远未放缓。

### 月度 commit 趋势

| 时期 | 月均 commit | 阶段判断 |
|------|------------|---------|
| 2023 Q4（启动期） | 165 | 密集开发 |
| 2024 H1 | 360 | 极速扩张 |
| 2024 Q3（高峰） | 514 | 巅峰开发 |
| 2024 Q4 | 359 | 密集开发 |
| 2025 H1 | 261 | 密集开发 |
| 2025 H2 | 232 | 密集开发 |
| 2026 Q1 | 258 | 密集开发 |

### 核心贡献者

| 排名 | 贡献者 | commit 数 | 占比 |
|------|--------|----------|------|
| 1 | Charlie Marsh | 3,008 | 34.0% |
| 2 | Zanie Blue | 1,899 | 21.5% |
| 3 | konsti | 1,057 | 11.9% |
| 4 | renovate[bot] | 966 | 10.9% |
| 5 | Andrew Gallant | 253 | 2.9% |
| 6 | samypr100 | 84 | 0.9% |
| 7 | Jo | 77 | 0.9% |
| 8 | Aria Desires | 71 | 0.8% |
| 9 | William Woodruff | 70 | 0.8% |
| 10 | Ibraheem Ahmed | 68 | 0.8% |

总贡献者：539 人

**解读**：Charlie Marsh（创始人/CEO）+ Zanie Blue + konsti 三人贡献 67.4% 的 commit，核心团队极为紧凑。renovate[bot] 占 10.9% 说明依赖更新自动化程度高。539 名贡献者体现了强大的社区参与度。

## 演化轨迹

### 核心文件（Top 10 最常修改，基于最近 500 commits）
1. Cargo.lock — 136 次修改
2. Cargo.toml — 39 次修改
3. .github/workflows/test.yml — 28 次修改
4. crates/uv/tests/it/lock.rs — 27 次修改
5. crates/uv/Cargo.toml — 27 次修改
6. .github/workflows/check-lint.yml — 27 次修改
7. crates/uv/tests/it/pip_install.rs — 26 次修改
8. crates/uv/src/lib.rs — 23 次修改
9. pyproject.toml — 22 次修改
10. docs/guides/integration/docker.md — 22 次修改

### 热点目录
1. crates/uv — 8,996 次修改（核心 CLI 逻辑）
2. crates/uv-resolver — 2,131 次修改（依赖解析器）
3. crates/uv-python — 1,125 次修改（Python 版本管理）
4. docs/guides — 1,119 次修改（用户文档）
5. .github/workflows — 966 次修改（CI/CD 管线）
6. crates/uv-cli — 678 次修改（命令行接口定义）
7. crates/uv-distribution — 644 次修改（包分发处理）
8. docs/concepts — 596 次修改（概念文档）
9. docs/reference — 558 次修改（参考文档）
10. crates/uv-client — 511 次修改（网络客户端）

### Commit 类型分布（最近 200 条）
- Feature/Add: 21 (10.5%)
- Fix/Bug: 11 (5.5%)
- Docs: 10 (5.0%)
- Test: 10 (5.0%)
- Refactor: 0 (0%)
- Other: 148 (74.0%)

**注**：uv 大量使用 PR 标题式 commit（如「Support X」「Update Y」「Use Z」），不遵循 Conventional Commits 规范，导致多数归入 Other 类。实际 feature 比例远高于统计值。

### 版本发布
- 最新版本: 0.11.3（2026-04-01）
- 总 Release 数: 267
- 版本策略: 语义化版本（0.x 阶段），高频发布（平均每 3-4 天一个版本）

**解读**：267 个版本在 30 个月内发布，平均 3.4 天一个版本，这是极为激进的发布节奏。仍处于 0.x 阶段意味着 API 尚未完全稳定，但从 0.10 → 0.11 的演进看，正在向 1.0 稳步迈进。

## 项目画像卡片

```
项目: astral-sh/uv
年龄: 30 个月  |  代码: 484,029 行 (Rust 78.7% / Python 1.4% / TOML 1.3%)
总 commits: 8,846  |  贡献者: 539 人
开发阶段: 密集开发（月均 ~250 commits，持续 30 个月未减速）
开发模式: 职业项目（Astral 公司全职团队，周末仅 12.8%）
核心文件: crates/uv/src/lib.rs, crates/uv-resolver/, crates/uv-python/
Release: v0.11.3 (共 267 个版本，平均 3.4 天/版本)
```
