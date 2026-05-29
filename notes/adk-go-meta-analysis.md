## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 53,847（不含空行/注释） |
| 语言分布 | Go 91.3%, JavaScript 8.5%, Shell/Dockerfile/其他 0.2% |
| 代码/注释比 | 7.5:1 |
| 文件数量 | 299 |
| 依赖数量 | 88（runtime: 32, indirect: 56） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 10 个月（首次提交 2025-05-19） |
| 总 commit 数 | 373 |
| 最近提交 | 2026-03-20 |
| 近 30 天 commit | 54 |
| 近 90 天 commit | 114 |
| 开发阶段 | 密集开发 |
| 开发模式 | 职业项目（周末占比 0.3%，深夜占比 8.3%） |

## 演化轨迹

### 核心文件（Top 10 最常修改）
1. go.mod — 21 次修改
2. internal/llminternal/base_flow.go — 20 次修改
3. go.sum — 19 次修改
4. agent/remoteagent/a2a_agent_test.go — 18 次修改
5. agent/remoteagent/a2a_agent.go — 17 次修改
6. server/adka2a/executor.go — 13 次修改
7. server/adka2a/processor.go — 12 次修改
8. cmd/launcher/web/api/api.go — 12 次修改
9. cmd/launcher/console/console.go — 12 次修改
10. server/adkrest/handler.go — 11 次修改

### 热点目录
1. cmd/launcher — 193 次修改
2. internal/llminternal — 176 次修改
3. server/adka2a — 95 次修改
4. cmd/restapi — 89 次修改
5. agent/remoteagent — 82 次修改
6. server/adkrest — 81 次修改
7. agent/llmagent — 69 次修改
8. tool/mcptoolset — 68 次修改
9. agent/workflowagents — 55 次修改
10. examples/workflowagents — 50 次修改

### Commit 类型分布
- Feature/Add: 67 (33.5%)
- Fix/Bug: 62 (31.0%)
- Refactor: 5 (2.5%)
- Docs: 6 (3.0%)
- Test: 5 (2.5%)
- Other: 55 (27.5%)

### 版本发布
- 最新版本: v0.6.0（2026-03-06）
- 总 Release 数: 6
- 版本策略: 语义化版本（约每月发布一次，节奏稳定）

## 项目画像卡片

项目: google/adk-go
年龄: 10 个月  |  代码: 53,847 行 (Go)
总 commits: 373  |  贡献者: 47 人
开发阶段: 密集开发
开发模式: 职业项目
核心文件: base_flow.go, a2a_agent.go, executor.go, processor.go, handler.go
Release: v0.6.0 (共 6 个版本)
