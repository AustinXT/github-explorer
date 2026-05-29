# clockworklabs/SpacetimeDB 元分析报告

> 分析日期：2026-03-22

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 590,455（不含空行/注释） |
| 语言分布 | Rust 35.8%, JSON 14.6%, Markdown 13.3%, C Header 9.1%, TypeScript 8.5%, YAML 8.1%, C# 7.7%, C++ 4.8%, TSX 3.6%, 其他 |
| 代码/注释比 | 4.4:1 |
| 文件数量 | 4,622 |
| Rust crate 数量 | 41 |
| SDK 数量 | 4（Rust, C#, TypeScript, Unreal C++） |

### 核心 Crate 规模（Rust 代码行数 Top 10）

| Crate | 代码行数 |
|-------|---------|
| core | 43,437 |
| table | 18,068 |
| cli | 17,539 |
| schema | 14,843 |
| datastore | 14,209 |
| sats | 14,098 |
| codegen | 12,156 |
| smoketests | 10,953 |
| commitlog | 8,622 |
| client-api | 5,962 |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 40 个月（首次提交 2022-11-01） |
| 总 commit 数 | 3,202 |
| 最近提交 | 2026-03-21 |
| 近 30 天 commit | 173 |
| 近 90 天 commit | 448 |
| 近 365 天 commit | 1,237 |
| 贡献者总数 | 109 人 |
| 远程分支数 | 1,810 |
| 开发阶段 | 高速迭代期（v2.0 刚发布，快速修补中） |
| 开发模式 | 商业公司全职团队（周末仅 4.1%，工作时间集中 9:00-19:00） |

### 月度 Commit 密集期分析

项目活跃度持续攀升，呈现几个阶段：

1. **2022-11 ~ 2023-02**（21 commits）：项目初始化，代码框架搭建
2. **2023-06 ~ 2023-12**（657 commits）：Beta 开发期，v0.6-v0.8 密集迭代
3. **2024-01 ~ 2024-12**（921 commits）：Beta 完善期，v0.8-v0.12 系列发布
4. **2025-01 ~ 2025-12**（1,143 commits）：1.0 正式版发布，快速迭代至 v1.11
5. **2026-01 ~ 2026-03**（439 commits，3 个月）：v2.0 大版本发布，月均 146 commits 为历史最高

2026-02 达到 217 commits 的历史单月峰值，对应 v2.0 发布周期。

### 工作时间模式

- 高频时段：09:00-19:00（工作日标准时间），峰值在 13:00（292 commits）
- 深夜开发（22:00-06:00）占 13.1%，可能与多时区贡献者有关
- 周末占比仅 4.1%（远低于自然分布 28.6%），典型商业团队开发模式
- 每周分布：周二（671）与周三（682）最活跃，周日最低（32）

## 演化轨迹

### 热点文件（Top 15 最高变更量）

| 文件 | 总变更行数 | 说明 |
|------|-----------|------|
| `sdks/rust/tests/test-client/src/main.rs` | 4,827 | Rust SDK 测试入口 |
| `crates/vm/src/expr.rs` | 2,666 | 虚拟机表达式求值 |
| `crates/table/src/table_index/mod.rs` | 1,910 | 表索引实现 |
| `crates/codegen/src/unrealcpp.rs` | 1,709 | Unreal C++ 代码生成 |
| `crates/core/src/subscription/query.rs` | 1,402 | 订阅查询核心 |
| `crates/core/src/sql/ast.rs` | 1,140 | SQL AST 定义 |
| `sdks/rust/tests/view-pk-client/src/main.rs` | 1,130 | View PK 测试客户端 |
| `crates/core/src/sql/compiler.rs` | 999 | SQL 编译器 |
| `crates/core/src/host/v8/mod.rs` | 992 | V8 宿主运行时 |
| `crates/core/src/vm.rs` | 919 | 虚拟机主模块 |

### 高频修改文件（Top 10 commit 次数最多）

| 文件 | Commit 次数 | 说明 |
|------|------------|------|
| `sdks/rust/tests/test.rs` | 34 | Rust SDK 主测试文件 |
| `sdks/rust/tests/test-client/src/main.rs` | 34 | 测试客户端 |
| `crates/cli/src/subcommands/dev.rs` | 30 | CLI dev 子命令 |
| `sdks/rust/tests/view-pk-client/src/main.rs` | 22 | View PK 测试 |
| `crates/client-api/src/routes/database.rs` | 21 | 数据库 API 路由 |
| `crates/cli/src/spacetime_config.rs` | 21 | CLI 配置管理 |
| `sdks/rust/tests/view-client/src/main.rs` | 20 | View 测试客户端 |
| `crates/cli/src/subcommands/init.rs` | 17 | CLI init 子命令 |
| `crates/core/src/db/relational_db.rs` | 16 | 关系数据库核心 |

### 热点目录

| 目录 | 总变更行数 | 说明 |
|------|-----------|------|
| `docs/` | 52,739 | 文档（含网站） |
| `sdks/unreal/` | 20,478 | Unreal Engine SDK |
| `sdks/rust/` | 17,897 | Rust SDK |
| `templates/` | 17,444 | 项目模板 |
| `crates/core/` | 11,497 | 数据库核心引擎 |
| `crates/bindings-typescript/` | 8,424 | TypeScript 绑定 |
| `crates/bindings-cpp/` | 7,895 | C++ 绑定 |
| `skills/` | 6,717 | Agent Skills |
| `tools/` | 5,696 | 工具脚本 |
| `crates/smoketests/` | 4,418 | 冒烟测试 |

### Commit 类型分布（2025-01 至今，1,552 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 其他（无规范前缀） | 811 | 52.3% |
| Feature/Add | 216 | 13.9% |
| Fix/Bug | 205 | 13.2% |
| Chore/Update/Release | 149 | 9.6% |
| CI/Build | 88 | 5.7% |
| Docs | 33 | 2.1% |
| Refactor | 31 | 2.0% |
| Revert | 9 | 0.6% |
| Perf | 5 | 0.3% |
| Test | 3 | 0.2% |

> 注：约半数 commit 消息使用 PR 标题风格（如 "Keynote-2 sqlite fixes (#4678)"），未严格遵循 Conventional Commits 规范，因此"其他"占比较高。feat 和 fix 合计 27.1%，显示项目正处于功能密集开发+快速修复阶段。

### 版本发布

| 指标 | 数据 |
|------|------|
| 最新版本 | v2.0.5（2026-03-13） |
| 总 Tag 数 | 50+（含 SDK 分组 tag） |
| 版本策略 | 语义化版本，Beta 阶段 v0.6-v0.12，正式版 v1.0-v2.0 |

#### 版本演化里程碑

| 阶段 | 时间段 | 版本范围 | 说明 |
|------|--------|---------|------|
| Beta | 2023-08 ~ 2024-10 | v0.6.0-beta ~ v0.12.0-beta | 14 个月，13 个 beta 版本 |
| GA 1.x | 2025-02 ~ 2026-02 | v1.0.0 ~ v1.12.0 | 12 个月，20+ 个 1.x 版本 |
| GA 2.x | 2026-02 ~ 至今 | v2.0.0-rc1 ~ v2.0.5 | 1 个月，快速修补中 |

#### 发布节奏

- Beta 期间：约每月 1 个版本
- v1.x 期间（2025-02 ~ 2026-02）：约每 2-3 周一个版本，2025 年下半年加速至每周级别
- v2.x 期间（2026-02 ~ 至今）：一个月内 5 个补丁版本，极高频修补

### 核心贡献者

| 贡献者 | 总 Commits | 2026 年 Commits | 角色推测 |
|--------|-----------|----------------|---------|
| Zeke Foppa | 367 | 53 | 核心开发者/架构师 |
| Mazdak Farrokhzad | 304 | 32 | 核心开发者 |
| joshua-spacetime | 296 | 31 | 核心开发者 |
| Kim Altintop | 224 | 18 | 核心开发者 |
| Tyler Cloutier | 222 | 20 | 核心开发者/创始人 |
| John Detter | 220 | 25 | 核心开发者 |
| Noa | 219 | 39 | 核心开发者 |
| Phoebe Goldman | 206 | 16 | 核心开发者 |
| Ingvar Stepanyan | 189 | — | 核心开发者（近期减少） |
| Piotr Sarnacki | 110 | 12 | 核心开发者 |

> 前 10 位贡献者占总 commit 的 73%，团队核心约 10 人，符合商业公司研发团队规模。2026 年出现新活跃贡献者（Ryan: 31, bradleyshep: 20, clockwork-labs-bot: 35），团队在扩展中。

## 项目画像卡片

```
项目: clockworklabs/SpacetimeDB
年龄: 40 个月  |  代码: 590,455 行 (Rust/TS/C#/C++)
总 commits: 3,202  |  贡献者: 109 人
开发阶段: 高速迭代期（v2.0 刚发布，快速修补中）
开发模式: 商业公司全职团队（周末 4.1%，工作日 9-19 时集中）
核心模块: core(43K LOC), table(18K), cli(18K), schema(15K), datastore(14K)
SDK覆盖: Rust, C#, TypeScript, Unreal C++
Release: v2.0.5 (共 50+ 版本, v0.6-beta → v2.0)
发布节奏: v1.x 每 2-3 周, v2.x 近每 3 天一个补丁
```
