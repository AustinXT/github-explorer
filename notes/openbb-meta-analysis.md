# OpenBB-finance/OpenBB 元分析（When & How Much）

## 代码规模

| 语言 | 文件数 | 代码行数 | 注释 | 空行 |
|------|--------|----------|------|------|
| YAML | 323 | 1,209,620 | 0 | 0 |
| Python | 1,267 | 195,427 | 7,255 | 28,556 |
| JSON | 77 | 176,315 | 0 | 3 |
| XML | 2 | 57,727 | 0 | 0 |
| TSX | 80 | 20,850 | 931 | 1,840 |
| TypeScript | 15 | 22,093 | 34 | 88 |
| Rust | 19 | 13,602 | 821 | 1,894 |
| JavaScript | 8 | 3,334 | 163 | 561 |
| TOML | 59 | 1,303 | 11 | 225 |
| CSS | 4 | 1,120 | 32 | 176 |
| **总计** | **1,974** | **1,707,227** | **14,222** | **36,735** |

- 总行数（含注释/空行）：**175.8 万行**
- 核心代码行：**170.7 万行**（其中 YAML 占 70.8%，主要是 CI/CD 配置和数据文件）
- 主力语言为 **Python**（19.5 万行，占有效代码的 11.4%），是业务逻辑的核心
- 前端部分使用 **TSX/TypeScript**（约 4.3 万行），桌面端使用 **Rust**（约 1.4 万行）

## 开发节奏

| 维度 | 数据 |
|------|------|
| 首次提交 | 2020-12-20 |
| 最新提交 | 2026-03-19 |
| 项目年龄 | **5 年 3 个月** |
| 主分支总提交 | **6,820** |
| 全部分支提交 | **10,380** |
| 唯一贡献者 | **288** |
| 平均提交/月 | ~108 |

### 月度提交趋势

项目经历了明显的生命周期阶段：

1. **爆发增长期（2021-02 ~ 2021-04）**：月均 520+ commits，项目从终端工具快速成型
2. **稳定开发期（2021-05 ~ 2022-09）**：月均 ~80 commits，持续迭代
3. **平台重构期（2022-10 ~ 2023-02）**：月均 350+ commits，高峰达 787（2023-02），推测为 v3→v4 的 OpenBB Platform 重构
4. **成熟维护期（2023-03 ~ 2024-05）**：月均 ~90 commits，功能趋于稳定
5. **低频维护期（2024-06 ~ 至今）**：月均 ~15 commits，进入稳定维护阶段

### 星期分布

| 星期 | 提交数 | 占比 |
|------|--------|------|
| 周一 | 1,183 | 17.3% |
| 周二 | 1,163 | 17.1% |
| 周三 | 1,090 | 16.0% |
| 周四 | 1,037 | 15.2% |
| 周五 | 1,064 | 15.6% |
| 周六 | 696 | 10.2% |
| 周日 | 587 | 8.6% |

工作日提交占比 **81.2%**，周末活动占 **18.8%**，呈现典型的**专业团队开发模式**，但周末仍有可观的贡献量。

### Top 贡献者

| 贡献者 | 提交数 |
|--------|--------|
| DidierRLopes（创始人） | 735 |
| Danglewood | 718 |
| James Maslek | 545 |
| didier（同创始人） | 514 |
| Artem Veremey | 384 |
| Colin Delahunty | 345 |
| montezdesousa | 307 |
| Diogo Sousa | 255 |

创始人 Didier Lopes 合计约 1,249 次提交（两个账号），占总量 18.3%，深度参与开发。

## 演化轨迹

### 版本发布

| 版本 | 日期 | 说明 |
|------|------|------|
| v3.1.0 | 2023-06 | v3 系列起始 |
| v3.2.0 ~ v3.2.5 | 2023-07 ~ 2024-03 | v3 系列维护更新 |
| v4.2.0 | 2024-06 | v4 平台架构，跨越式升级 |
| v4.3.1 ~ v4.3.4 | 2024-08 ~ 2024-10 | v4 快速迭代 |
| v4.4.0 ~ v4.4.3 | 2025-02 ~ 2025-03 | 稳定版本 |
| v4.5.0 | 2025-10 | |
| v4.6.0 | 2026-01 | |
| v4.7.0 | 2026-03 | 最新发布 |

此外还有 **ODP（Open Data Platform）Desktop** 桌面端独立发布线：v0.9.0 ~ v1.0.1。

发布节奏：v4 系列约 **2-3 个月一个小版本**，维护节奏稳定。

### 核心文件（最常修改 Top 10）

| 修改次数 | 文件 |
|----------|------|
| 125 | openbb_platform/openbb/assets/reference.json |
| 91 | openbb_platform/extensions/equity/integration/test_equity_python.py |
| 90 | openbb_platform/extensions/equity/integration/test_equity_api.py |
| 81 | openbb_platform/openbb/package/economy.py |
| 80 | openbb_platform/pyproject.toml |
| 72 | openbb_platform/poetry.lock |
| 69 | openbb_platform/core/pyproject.toml |
| 67 | openbb_platform/core/openbb_core/app/static/package_builder.py |
| 62 | openbb_platform/providers/yfinance/poetry.lock |
| 59 | openbb_platform/core/poetry.lock |

核心文件集中在 **openbb_platform** 目录，`reference.json`（API 参考）是最活跃的文件，equity（股票）模块的测试文件变更频繁，体现了数据驱动的开发模式。

### 热点目录

| 修改次数 | 目录 |
|----------|------|
| 16,101 | website/content（文档站） |
| 9,583 | openbb_platform/providers（数据提供者） |
| 7,943 | tests/openbb_terminal（终端测试） |
| 3,508 | openbb_platform/extensions（功能扩展） |
| 2,918 | openbb_platform/core（平台核心） |
| 2,124 | openbb_terminal/stocks（股票模块） |
| 1,987 | openbb_terminal/miscellaneous（杂项） |
| 1,154 | openbb_terminal/cryptocurrency（加密货币） |
| 1,154 | openbb_terminal/core（终端核心） |
| 1,129 | openbb_platform/openbb（平台入口） |

**文档站内容**是最活跃的区域，其次是 **providers（数据提供者）**，体现了项目重视文档和数据源集成。

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| Fix / Bug | 73 | 36.5% |
| Feature / Add | 56 | 28.0% |
| Docs | 3 | 1.5% |
| Refactor | 1 | 0.5% |
| Test | 3 | 1.5% |
| Other | 64 | 32.0% |

近期提交以 **修复（36.5%）** 和 **新功能（28%）** 为主，项目处于活跃维护与功能扩展并行的阶段。

## 项目画像卡片

```
┌─────────────────────────────────────────────────────┐
│  OpenBB-finance/OpenBB                              │
├─────────────────────────────────────────────────────┤
│  定位：开源金融数据与投研分析平台                       │
│  语言：Python 为主 + TSX/TS 前端 + Rust 桌面端        │
│  规模：170.7 万行代码 │ 1,974 文件                    │
│  历史：5 年 3 个月 │ 6,820 commits │ 288 贡献者       │
│  版本：v4.7.0（2026-03） │ 20+ 个发布版本             │
│  节奏：月均 ~108 commits（历史）│ ~15 commits（近期）  │
│  阶段：成熟维护期，低频但稳定迭代                       │
│  架构演进：CLI Terminal → OpenBB Platform → ODP Desktop│
│  特征：重视文档 │ 多数据源集成 │ 模块化扩展架构         │
│  团队：创始人深度参与，核心团队 8-10 人                  │
└─────────────────────────────────────────────────────┘
```
