# shadcn-ui/ui 元分析报告（Phase 2: When & How Much）

> 分析时间: 2026-03-22
> 仓库: shadcn-ui/ui
> 本地路径: /tmp/repo-miner-ui

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 537,132（不含空行/注释） |
| 语言分布 | TSX 49.2%, JSON 29.2%, TypeScript 13.2%, YAML 6.9%, CSS 1.3%, 其他 0.2% |
| 代码/注释比 | 18.6:1（代码 537,132 行 vs 注释 28,936 行） |
| 文件数量 | 6,647 |
| 依赖数量 | 35（runtime 29 + dev 6，根 package.json） |

**说明：**
- 实际业务代码（TSX + TypeScript）约 334,929 行，占总代码的 62.4%，是项目的核心
- JSON 占比高（29.2%）主要来自 registry 配置文件和 pnpm-lock.yaml
- 注释极少（代码注释比 18.6:1），项目依赖 TypeScript 类型系统和组件命名自文档化，而非内联注释
- MDX 文件（204个）承载了大量文档内容（24,218 行注释/文本），文档化程度实际较高

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 38 个月（首次提交 2023-01-24） |
| 总 commit 数 | 1,877 |
| 最近提交 | 2026-03-20 |
| 近 30 天 commit | 353 |
| 近 90 天 commit | 673 |
| 近 365 天 commit | 1,142 |
| 开发阶段 | **密集开发**（近期 commit 量大幅飙升，v4 重大版本发布中） |
| 开发模式 | **职业项目**（周末占比 18.4%，深夜占比 18.6%） |

**开发节奏详解：**

- **2023年（孵化期）**：月均 28 commits，稳定的持续开发，以 v0.x 到 v1.x 迭代为主
- **2024年初（低谷期）**：2024-02 仅 1 次提交，2024-04~06 明显放缓，可能在规划/重构
- **2024年下半年（回暖期）**：2024-10 达 60 次，恢复活跃
- **2025年（加速期）**：2025-02 起持续上升，2025-10 达 145 次
- **2026年初（爆发期）**：2026-02 达 310 次，2026-03（截至20日）已 264 次 — 这是 v4.0 大版本发布带来的密集开发

**工作时间分布：**
- 高峰时段：11-17 时（工作时间，占比最大），符合职业开发者模式
- 周一至周三 commit 最密集（Mon 357, Tue 326, Wed 331），周末较少（Sat 147, Sun 198）
- 深夜（22-06时）占比 18.6%，说明偶尔有加班但非主要模式

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. `apps/v4/public/r/registries.json` — 151 次修改
2. `apps/v4/registry/directory.json` — 142 次修改
3. `pnpm-lock.yaml` — 66 次修改
4. `apps/v4/package.json` — 56 次修改
5. `packages/shadcn/src/commands/init.ts` — 50 次修改
6. `packages/shadcn/package.json` — 35 次修改
7. `packages/shadcn/CHANGELOG.md` — 27 次修改
8. `apps/v4/app/(create)/components/project-form.tsx` — 25 次修改
9. `apps/v4/public/r/styles/*/registry.json` — 各 24 次修改（10个样式变体）
10. `apps/v4/app/(create)/create/page.tsx` — 23 次修改

**洞察：** registry 相关配置文件和 CLI init 命令是变更热点，说明组件注册/发现机制和项目初始化流程是核心关注点。

### 热点目录

1. `apps/v4` — 19,182 次修改（主应用，v4 版本）
2. `apps/www` — 11,851 次修改（旧版官网）
3. `deprecated/www` — 6,597 次修改（已废弃的旧版本）
4. `packages/shadcn` — 1,507 次修改（CLI 工具包）
5. `packages/cli` — 502 次修改（旧 CLI）
6. `templates/next-template` — 221 次修改
7. `examples/playground` — 202 次修改
8. `packages/tests` — 133 次修改
9. `templates/monorepo-next` — 102 次修改
10. `.github/workflows` — 76 次修改

**洞察：** 从 `apps/www` → `deprecated/www` → `apps/v4` 的迁移轨迹清晰可见，项目经历了至少两次重大架构演进。

### Commit 类型分布（基于最近 500 条 commit 采样）

| 类型 | 数量 | 占比 |
|------|------|------|
| Fix/Bug | 202 | 40.4% |
| Feature/Add | 122 | 24.4% |
| Other | 160 | 32.0% |
| Docs | 8 | 1.6% |
| Refactor | 6 | 1.2% |
| Test | 2 | 0.4% |

**洞察：** Fix 占比最高（40.4%），说明项目处于快速迭代中，bug 修复频繁。Feature 占 24.4% 表明新功能持续增加。Refactor 和 Test 占比极低，暗示项目更偏重功能交付而非工程化重构。

### 版本发布

- **最新版本**: shadcn@4.1.0（2026-03-19）
- **总 Release 数**: 86 个 tag
- **版本策略**: 语义化版本（Semantic Versioning）
- **命名演化**: `@shadcn/ui@0.0.4` → `shadcn-ui@0.1.x` → `shadcn@3.x` → `shadcn@4.x`
- **v4.0 发布密度**: 2026-03-06 发布 4.0.0 后，14 天内连发 9 个补丁/小版本（4.0.0 → 4.1.0），迭代极为密集

### 贡献者

| 排名 | 贡献者 | Commits |
|------|--------|---------|
| 1 | shadcn | 1,065（56.7%） |
| 2 | github-actions[bot] | 83 |
| 3 | dependabot[bot] | 23 |
| 4 | KapishDima | 12 |
| 5 | Jaem | 10 |

- **总贡献者**: 508 人
- **核心维护者**: shadcn（独立开发者 shadcn 贡献了超过半数 commit）
- **特征**: 典型的个人主导开源项目，社区贡献者众多但贡献分散

## 项目画像卡片

```
项目: shadcn-ui/ui
年龄: 38 个月  |  代码: 537,132 行 (TSX/TypeScript 为主)
总 commits: 1,877  |  贡献者: 508 人
开发阶段: 密集开发（v4 大版本发布，近期爆发式增长）
开发模式: 职业项目（周末占比 18.4%，深夜占比 18.6%）
核心文件: registries.json, directory.json, init.ts
Release: shadcn@4.1.0 (共 86 个版本)
关键特征: 个人主导 + 大规模社区贡献，正经历 v3→v4 重大版本迁移
```
