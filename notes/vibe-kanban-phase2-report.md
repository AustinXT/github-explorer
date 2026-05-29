## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 213,305（不含空行/注释） |
| 语言分布 | Rust 40.3%, TSX 29.6%, TypeScript 12.3%, JSON 10.0%, YAML 3.2%, JavaScript 1.1%, SQL 0.9%, CSS 0.9%, 其他 1.7% |
| 代码/注释比 | 12:1 |
| 文件数量 | 1,427 |
| 依赖数量 | 21（Rust workspace dependencies）+ 8（npm devDependencies） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 9 个月（首次提交 2025-06-14） |
| 总 commit 数 | 1,989 |
| 最近提交 | 2026-03-18 |
| 近 30 天 commit | 256 |
| 近 90 天 commit | 768 |
| 近 365 天 commit | 1,989（全部） |
| 开发阶段 | 密集开发（月均 >200 commit，近期 2026-02 达 331） |
| 开发模式 | 职业项目（周末占比 10.1%，深夜 22:00-06:00 占比 10.9%） |

## 演化轨迹

### 核心文件（Top 10 最常修改）
1. shared/types.ts — 260 次修改
2. package.json — 246 次修改
3. npx-cli/package.json — 209 次修改
4. crates/server/Cargo.toml — 190 次修改
5. crates/executors/Cargo.toml — 188 次修改
6. crates/services/Cargo.toml — 179 次修改
7. crates/utils/Cargo.toml — 178 次修改
8. crates/local-deployment/Cargo.toml — 172 次修改
9. crates/db/Cargo.toml — 164 次修改
10. crates/deployment/Cargo.toml — 163 次修改

### 热点目录
1. frontend/src — 5,442 次修改
2. crates/remote — 1,163 次修改
3. crates/db — 1,141 次修改
4. crates/executors — 1,023 次修改
5. crates/server — 916 次修改
6. packages/web-core — 843 次修改
7. backend/src — 826 次修改
8. crates/services — 730 次修改
9. backend/.sqlx — 320 次修改
10. crates/local-deployment — 311 次修改

### Commit 类型分布
- Feature/Add: 41 (20.5%)
- Fix/Bug: 54 (27.0%)
- Refactor: 5 (2.5%)
- Docs: 8 (4.0%)
- Test: 1 (0.5%)
- Other: 91 (45.5%)

### 版本发布
- 最新版本: v0.1.32（2026-03-18，Latest Release）
- 总 Release 数: 264
- 总 Tag 数: 413
- 版本策略: 语义化版本 + 时间戳后缀（格式 vX.Y.Z-YYYYMMDDHHMMSS），含频繁预发布版本

## 项目画像卡片

```
项目: BloopAI/vibe-kanban
年龄: 9 个月  |  代码: 213,305 行 (Rust 40%, TSX 30%, TS 12%)
总 commits: 1,989  |  贡献者: 64 人
开发阶段: 密集开发（月均 >200 commits，无停滞迹象）
开发模式: 职业项目（工作日集中，高频 CI/CD 发布）
核心文件: shared/types.ts, package.json, Cargo.toml 系列
Release: v0.1.32 (共 264 个版本)
```

### 补充洞察

**月度开发节奏分析：**
- 2025-06（创始月）: 320 commits — 项目初始化密集开发
- 2025-07 ~ 2025-08: 203/113 — 短暂放缓
- 2025-09: 231 — 第二波密集期
- 2025-10 ~ 2025-12: 143/104/125 — 稳定维护
- 2026-01 ~ 2026-02: 298/331 — 新一轮密集开发高峰
- 2026-03（截至 18 日）: 121 — 当月仍在高速迭代

**架构特征：**
- Rust + TypeScript 全栈项目，后端 Rust workspace 包含 18+ crate
- 前端热点远高于后端（frontend/src 5,442 次 vs 最大后端模块 1,163 次）
- shared/types.ts 为最高频修改文件（260 次），是前后端类型共享的核心枢纽
- 大量 Cargo.toml 文件频繁修改，反映模块化架构中依赖管理的活跃度

**团队结构：**
- 核心开发者 3 人：Louis Knight-Webb（2,460）、anastasiya1155（860）、Alex Netsch（826）
- GitHub Action bot 贡献 516 commits（自动化发布流水线）
- 64 人总贡献者中含长尾社区贡献
