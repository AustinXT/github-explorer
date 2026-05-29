# pathwaycom/pathway 元分析报告

> 分析日期：2026-03-22

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 231,879（不含空行/注释） |
| 语言分布 | Rust 37.1%, Python 50.8%, Markdown 嵌入代码, JSON 6.6%, TSX/TS 3.7%, 其他 1.8% |
| 代码/注释比 | 7.6:1 |
| 文件数量 | 1,253 |
| 仓库体积 | ~322 MB |
| 主要依赖数 | 42+（runtime，pyproject.toml），另有多组可选依赖（pyfilesystem/sql/xpack-llm 等） |

### 语言结构解读

项目采用 **Rust + Python 双语言架构**，通过 maturin 构建系统桥接：

- **Rust**（86,104 行代码，425 文件）：核心计算引擎、数据流执行、connector 底层实现。占据底层运行时的绝对主力
- **Python**（117,739 行代码，445 文件）：用户 API 层、connector 上层封装、xpacks（LLM/RAG 扩展）、测试与示例
- **Jupyter Notebooks**（49 个）：教程和示例，作为文档的重要组成部分
- **Markdown**（192 个文件，含大量嵌入代码示例）：丰富的开发者文档

### 依赖特征

核心依赖覆盖完整的数据处理生态链：
- **数据处理**：numpy, pandas, pyarrow, scikit-learn
- **异步/网络**：aiohttp, fastapi, uvicorn
- **云服务**：boto3, google-api-python-client, google-cloud-pubsub, google-cloud-bigquery
- **存储**：sqlalchemy, sqlmodel, deltalake
- **可观测性**：opentelemetry-api/sdk/exporter
- **可选 LLM 扩展**：openai, litellm, cohere, tiktoken, langchain, llama-index, instructor, fastmcp

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 32 个月（首次提交 2023-07-21，开源版本起算） |
| 总 commit 数 | 1,873 |
| 最近提交 | 2026-03-21 |
| 近 30 天 commit | ~32（截至 2026-03-22） |
| 近 6 个月 commit | 337（2025-09 至 2026-03） |
| 月均 commit | ~58（全周期） |
| 发布版本数 | 85 个 tag（v0.2.0 ~ v0.29.1） |
| 开发阶段 | 活跃成长期 |
| 开发模式 | 商业团队驱动（工作日集中，正常工作时段为主） |

### 月度 Commit 趋势分析

项目经历了清晰的增长曲线：

1. **起步期（2023-07 ~ 2023-12）**：月均 ~5 commits，开源初期铺垫
2. **爆发增长期（2024-01 ~ 2024-07）**：月均 ~85 commits，核心功能快速扩展，峰值 111 commits（2024-06）
3. **稳定高产期（2024-08 ~ 2025-06）**：月均 ~67 commits，保持高频迭代
4. **稳定成熟期（2025-07 ~ 2026-03）**：月均 ~51 commits，节奏稍缓但仍然活跃

项目从未出现"断档"，持续保持每月至少 32 次提交，表明有稳定的全职开发团队支撑。

### 工作时间模式

- **高频时段**：06:00 为绝对峰值（583 commits，占 31.1%），推测为 CI/CD 自动提交或定时任务
- **人工活跃时段**：09:00-18:00（欧洲工作时间），集中在 10:00-17:00
- **周末占比**：10.9%（周六 108 + 周日 96 = 204 / 1873），远低于自然分布 28.6%，典型商业团队节奏
- **工作日分布**：周一至周五均衡（304~360），周四略高（360）
- 整体模式：**典型欧洲时区商业团队**，06:00 峰值为自动化流水线特征

### 核心贡献者

| 排名 | 贡献者 | Commit 数 | 占比 |
|------|--------|-----------|------|
| 1 | Pathway-Dev（Bot/CI） | 672 | 35.9% |
| 2 | Sergey Kulik | 270 | 14.4% |
| 3 | Pawel Podhajski | 127 | 6.8% |
| 4 | Olivier Ruas | 118 | 6.3% |
| 5 | Szymon Dudycz | 113 | 6.0% |
| 6 | Kamil Piechowiak | 112 | 6.0% |
| 7 | berkecanrizai | 92 | 4.9% |
| 8 | Jakub Kowalski | 68 | 3.6% |
| 9 | foxCode (Sebastian) | 47 | 2.5% |
| 10 | Michal Bartoszkiewicz | 43 | 2.3% |

- **自动化占比高**：Pathway-Dev（Bot）占 35.9%，加上 dependabot（37 commits），自动化提交合计近 38%
- **核心人类开发者 5 人**：Sergey、Pawel、Olivier、Szymon、Kamil 贡献了人工 commit 的绝大部分
- **团队规模**：约 10-12 名活跃开发者，属中型团队
- **团队特征**：波兰/欧洲团队（从姓名和时区推断）

## 演化轨迹

### 版本发布节奏

| 阶段 | 版本范围 | 特征 |
|------|---------|------|
| 早期快速迭代 | v0.2.0 ~ v0.4.1 | 基础功能搭建 |
| 密集发布 | v0.5 ~ v0.21.x | 高频版本迭代，小版本修复多 |
| 稳定发布 | v0.22 ~ v0.29.1 | 大约每月一个小版本，含 BREAKING CHANGES |

近期发布频率：
- v0.27.0：2025-11-13
- v0.27.1：2025-12-08
- v0.28.0：2026-01-08
- v0.29.0：2026-01-22
- v0.29.1：2026-02-16

发布间隔约 **3~5 周**，属于快节奏但有章法的发布模式。

### 核心文件（Top 10 最常修改）

| 文件 | 修改次数 | 解读 |
|------|---------|------|
| examples/notebooks/tutorials/asynctransformer.ipynb | 537 | 示例笔记本（高频自动更新） |
| examples/notebooks/tutorials/consistency.ipynb | 400 | 教程笔记本 |
| examples/notebooks/tutorials/udf.ipynb | 258 | UDF 教程 |
| CHANGELOG.md | 230 | 变更记录 |
| src/python_api.rs | 91 | Rust-Python 桥接层核心 |
| Cargo.toml | 80 | Rust 依赖管理 |
| Cargo.lock | 79 | Rust 依赖锁文件 |
| python/pathway/tests/test_io.py | 62 | IO 测试 |
| examples/notebooks/tutorials/fs_connector.ipynb | 59 | 文件系统 connector 教程 |
| src/connectors/data_storage.rs | 53 | Rust 数据存储 connector |

**解读**：Notebook 示例文件修改次数极高（537/400/258次），是 Pathway-Dev Bot 每日自动刷新的结果。真正的核心代码热点集中在 `src/python_api.rs`（Rust-Python 桥接）和 `src/connectors/` 目录。

### 核心目录（Top 10 最常修改）

| 目录 | 修改次数 | 定位 |
|------|---------|------|
| examples/notebooks | 4,528 | 示例教程（大量自动化更新） |
| python/pathway | 3,607 | Python API 核心 |
| docs/2.developers | 1,625 | 开发者文档 |
| src/engine | 477 | Rust 引擎核心 |
| examples/projects | 423 | 项目示例 |
| src/connectors | 407 | Rust connector 层 |
| tests/integration | 275 | 集成测试 |
| external/differential-dataflow | 253 | 外部依赖（差分数据流） |
| external/timely-dataflow | 220 | 外部依赖（时序数据流） |
| src/persistence | 192 | 持久化模块 |

### 近 200 次提交类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| Features/Add | 11 | 5.5% |
| Fix/Bug | 22 | 11.0% |
| Refactor | 1 | 0.5% |
| Docs | 6 | 3.0% |
| Tests | 4 | 2.0% |
| Other | 156 | 78.0% |

"Other" 占比极高（78%），因为大量 commit 来自自动化流水线（"Daily Pathway examples refresh"等），未使用标准 conventional commits 格式。人工 commit 中 fix 与 feature 比约为 2:1，处于功能完善+修复并重阶段。

### 关键演化里程碑（从 CHANGELOG 提取）

| 版本 | 日期 | 重要特性 |
|------|------|---------|
| v0.27.0 | 2025-11 | NATS JetStream、Iceberg Glue catalog、行级更新时间戳 |
| v0.27.1 | 2025-12 | 遗忘结果过滤、Kafka key 列 |
| v0.28.0 | 2026-01 | Connector Group（空闲检测、优先级、多进程）、窗口函数优化 |
| v0.29.0 | 2026-01 | **Web Dashboard**、Kafka Headers、AWS Bedrock 原生集成 |
| v0.29.1 | 2026-02 | Kafka OAUTHBEARER、MongoDB snapshot 模式、**Worker 自动伸缩** |
| Unreleased | — | PostgreSQL WAL 读取、pyfilesystem 拆分为可选依赖 |

演化方向：从基础数据流引擎 → 丰富 connector 生态 → LLM/RAG 扩展 → 可观测性（Dashboard）→ 弹性伸缩。

## 项目画像卡片

```
┌─────────────────────────────────────────────────────┐
│  pathwaycom/pathway                                 │
│  ─────────────────────────────────────────────────  │
│  📦 定位：实时数据处理框架（Streaming + AI）           │
│  🏗️ 架构：Rust 引擎 + Python API（maturin 桥接）     │
│  📊 规模：231K 行代码 · 1,253 文件 · 322 MB          │
│  🔤 语言：Python 50.8% · Rust 37.1% · 其他 12.1%    │
│  📅 年龄：32 个月（2023-07 开源）                     │
│  🔄 活跃度：1,873 commits · 85 tags · 月均 58 次提交  │
│  👥 团队：~12 名活跃开发者（欧洲/波兰团队）             │
│  🏢 模式：商业公司驱动 · 高度自动化（38% 自动提交）     │
│  📈 阶段：活跃成长期 → 稳定成熟过渡                    │
│  🚀 发布：v0.29.1 · 每 3-5 周一个版本                │
│  🧩 依赖：42 核心 + 多组可选（LLM/SQL/PyFS）          │
│  🎯 演化：数据流引擎 → Connector 生态 → LLM/RAG →    │
│          Dashboard → 弹性伸缩                        │
│  ⚡ 特征：双语言高性能架构 · 丰富 connector ·           │
│          LLM-ready · 企业级可观测性                    │
└─────────────────────────────────────────────────────┘
```
