# Skyvern-AI/skyvern 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总文件数 | 2,151 |
| 总代码行数 | 318,258 行 |
| 主语言 | Python（164,505 行，51.7%） |
| 第二语言 | TSX（53,412 行，16.8%） |
| 第三语言 | TypeScript（32,096 行，10.1%） |
| 其他主要语言 | JSON（56,076 行）、MDX（27,045 行注释/文档）、JavaScript（3,159 行） |
| 注释行数 | 43,768 行（注释率 13.7%） |
| 空行数 | 42,743 行 |
| 核心依赖数 | 60+（pyproject.toml 中列出） |
| Python 版本要求 | >=3.11, <3.14 |
| 关键依赖 | FastAPI、Playwright、LiteLLM、OpenAI SDK、SQLAlchemy、Anthropic SDK、FastMCP |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 首次提交 | 2024-02-28（Initial commit） |
| 最新提交 | 2026-03-20 |
| 项目年龄 | ~25 个月 |
| 总提交数 | 4,234 |
| 月均提交 | ~169 次 |
| 最活跃月份 | 2026-02（254 次）、2025-10（251 次）、2025-05（234 次） |
| 活跃工作日 | 周三（829）和周四（869）最活跃，周末明显减少（周六 243，周日 235） |
| 活跃时段 | 11:00-16:00 为高峰（每小时 240-283 次），凌晨 3:00-6:00 最低 |
| 核心贡献者 | Shuchang Zheng（1,767 次，41.7%）、LawyZheng（587 次）、Kerem Yilmaz（400 次） |
| 贡献者数（Top 15） | 15 位主要贡献者（含 dependabot） |

## 演化轨迹

### 核心文件（变更最频繁）

| 排名 | 文件 | 变更次数 |
|------|------|---------|
| 1 | `skyvern/forge/sdk/workflow/service.py` | 67 |
| 2 | `skyvern/forge/sdk/db/agent_db.py` | 56 |
| 3 | `skyvern/forge/sdk/workflow/models/block.py` | 47 |
| 4 | `uv.lock` | 40 |
| 5 | `pyproject.toml` | 39 |
| 6 | `skyvern/config.py` | 34 |
| 7 | `skyvern-frontend/src/routes/workflows/editor/Workspace.tsx` | 28 |
| 8 | `fern/openapi/skyvern_openapi.json` | 28 |
| 9 | `skyvern/forge/sdk/routes/agent_protocol.py` | 26 |
| 10 | `skyvern/forge/agent.py` | 25 |

### 热点目录

| 排名 | 目录 | 变更次数 |
|------|------|---------|
| 1 | `skyvern/forge` | 1,341 |
| 2 | `skyvern-frontend/src` | 1,149 |
| 3 | `skyvern-ts/client` | 759 |
| 4 | `skyvern/client` | 686 |
| 5 | `skyvern/webeye` | 243 |
| 6 | `docs/images` | 219 |
| 7 | `skyvern/cli` | 215 |
| 8 | `tests/unit` | 189 |
| 9 | `skyvern/core` | 149 |
| 10 | `skyvern/services` | 142 |

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| Fix/Bug | 98 | 49.0% |
| Feature/Add | 57 | 28.5% |
| Refactor | 2 | 1.0% |
| Docs | 4 | 2.0% |
| Test | 2 | 1.0% |
| Other | 37 | 18.5% |

### 版本发布

| 指标 | 数据 |
|------|------|
| 总标签数 | 128 个 |
| 版本范围 | 0.1.1 → v1.0.24 |
| 最早标签 | 0.1.1（2024-03-16） |
| 最新版本 | v1.0.24（2026-03-13） |
| 近期发布频率 | 平均每 2.6 天一次（最近 10 个版本） |
| 发布节奏特征 | 密集迭代型，v1.0.15 至 v1.0.19 在 2 天内连续发布 5 个版本 |

## 项目画像卡片

```
┌─────────────────────────────────────────────────────────────┐
│  Skyvern-AI/skyvern                                         │
│  AI 驱动的浏览器自动化平台                                      │
├─────────────────────────────────────────────────────────────┤
│  规模：318K 行代码 │ 2,151 文件 │ 4,234 commits             │
│  语言：Python 51.7% │ TSX 16.8% │ TypeScript 10.1%         │
│  架构：后端(Python/FastAPI) + 前端(React/TSX) + TS SDK       │
│  年龄：25 个月（2024.02 ~ 至今）                              │
│  节奏：月均 169 次提交，工作日驱动，周三/周四高峰                  │
│  版本：128 个标签，当前 v1.0.24，近期每 2.6 天发版              │
│  核心：workflow 引擎 + DB 层 + 浏览器代理（Playwright）         │
│  团队：1 位核心主力 + 2 位高活跃 + 12 位活跃贡献者               │
│  特征：Fix 占比 49%（稳定性优先），Feature 占 28.5%（持续迭代）   │
│  依赖：LiteLLM 多模型接入、FastMCP 工具协议、Fern API 生成       │
│  趋势：提交量稳步上升，2025 年下半年起进入密集发版阶段              │
└─────────────────────────────────────────────────────────────┘
```
