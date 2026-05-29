# google/langextract 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 24,190（不含空行/注释） |
| 语言分布 | Python 95.0%, TOML 0.6%, Shell 0.3%, INI 0.3%, 其他 0.1%（Markdown 文档 3.6% 未计入代码） |
| 代码/注释比 | 9.2:1 |
| 文件数量 | 98 |
| 核心依赖数量 | 17（另有可选依赖：openai 1, dev 8, test 2, notebook 2） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 约 8 个月（2025-07-15 至 2026-03-21） |
| 总 commit 数 | 132 |
| 首次提交 | 2025-07-15 |
| 最近提交 | 2026-03-21 |
| 近 30 天 commit | 5 |
| 近 90 天 commit | 8 |
| 开发阶段 | 成熟维护期 — 核心功能已稳定（v1.1.1），当前以 bug 修复和小幅增强为主 |
| 开发模式 | 爆发式开发 + 长尾维护 — 2025-08 月集中贡献 99 次 commit（占总量 75%），之后进入低频维护 |

### 月度 Commit 分布

| 月份 | Commit 数 |
|------|-----------|
| 2025-07 | 5 |
| 2025-08 | 99 |
| 2025-09 | 9 |
| 2025-10 | 3 |
| 2025-11 | 8 |
| 2025-12 | 3 |
| 2026-02 | 1 |
| 2026-03 | 4 |

### 星期分布

| 星期 | Commit 数 |
|------|-----------|
| 周一 | 13 |
| 周二 | 16 |
| 周三 | 23 |
| 周四 | 24 |
| 周五 | 16 |
| 周六 | 14 |
| 周日 | 26 |

### 活跃时段（UTC）

高峰时段集中在 UTC 05:00（11 次）、19:00（9 次）、15:00（9 次）、22:00（8 次）、18:00（8 次），呈双峰分布，提示可能有跨时区的贡献者。

## 演化轨迹

### 核心文件（Top 10 最常修改）

| 排名 | 文件 | 修改次数 |
|------|------|----------|
| 1 | pyproject.toml | 26 |
| 2 | README.md | 19 |
| 3 | .github/workflows/ci.yaml | 18 |
| 4 | tests/inference_test.py | 15 |
| 5 | tests/init_test.py | 14 |
| 6 | langextract/inference.py | 12 |
| 7 | langextract/extraction.py | 12 |
| 8 | langextract/__init__.py | 12 |
| 9 | langextract/annotation.py | 11 |
| 10 | langextract/resolver.py | 10 |

### 热点目录

| 排名 | 目录 | 修改次数 |
|------|------|----------|
| 1 | .github/workflows | 60 |
| 2 | langextract/providers | 55 |
| 3 | langextract/core | 24 |
| 4 | examples/ollama | 14 |
| 5 | examples/custom_provider_plugin | 14 |
| 6 | docs/examples | 14 |

### Commit 类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| 功能开发（feat/add） | 51 | 38.6% |
| 缺陷修复（fix/bug） | 37 | 28.0% |
| 文档（doc） | 7 | 5.3% |
| 重构（refactor） | 4 | 3.0% |
| 测试（test） | 1 | 0.8% |
| 其他 | 32 | 24.2% |

### 版本发布

共 12 个版本，发布历史如下：

| 版本 | 日期 | 备注 |
|------|------|------|
| v1.1.1 | 2025-11-27 | Latest |
| v1.1.0 | 2025-11-14 | — |
| v1.0.9 | 2025-08-31 | — |
| v1.0.8 | 2025-08-15 | — |
| v1.0.7 | 2025-08-14 | — |
| v1.0.6 | 2025-08-13 | Custom Model Provider Plugins & Schema System Refactor |
| v1.0.5 | 2025-08-08 | — |
| v1.0.4 | 2025-08-05 | Ollama integration and improvements |
| v1.0.3 | 2025-08-03 | OpenAI language model support |
| v1.0.2 | 2025-08-03 | Removes pylibmagic dependency |
| v1.0.1 | — | — |
| v1.0.0 | — | 首个正式版本 |

发布节奏：2025-08 月密集发布 8 个版本（v1.0.2→v1.0.9），之后放缓至 2025-11 月发布 v1.1.x 系列。

## 项目画像卡片

| 维度 | 描述 |
|------|------|
| 项目定位 | 从语言模型（LLM）中提取结构化数据的 Python 库 |
| 技术栈 | Python（95%）, setuptools 构建, pytest 测试, tox 多环境管理 |
| 项目规模 | 小型库 — 24K 行代码, 98 个文件, 17 个核心依赖 |
| 项目阶段 | 成熟维护期（v1.1.1）— 核心功能完整，进入低频维护状态 |
| 开发模式 | 典型的 Google 开源项目：集中冲刺式开发后转为社区驱动维护 |
| 开发节奏 | 初期高强度（月均 99 commit），当前低频维护（月均 1-4 commit） |
| 架构特征 | 插件化 Provider 体系（Gemini/Ollama/OpenAI），模块间有严格的 import 约束（importlinter 规则）|
| 关键依赖 | google-genai, google-cloud-storage, pydantic, pandas, numpy |
| 代码质量信号 | 代码注释比 9.2:1（注释偏少），有完善的 CI/CD（ci.yaml 修改 18 次），测试占比适中 |
| 演化趋势 | 从核心提取功能 → 多 Provider 支持 → 批处理/GCS 集成，功能逐步外扩 |
