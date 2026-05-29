# supermemoryai/supermemory 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总行数 | 130,033 |
| 代码行数 | 79,822 |
| 注释行数 | 33,672 |
| 空行数 | 16,539 |
| 文件总数 | 709 |
| 主要语言 | TSX (37,597 行, 47.1%) / TypeScript (26,595 行, 33.3%) |
| 次要语言 | Python (4,727 行, 5.9%) / JSON (4,787 行) / CSS (714 行) |
| 文档内容 | MDX 145 文件 (26,995 行注释内容) |
| Monorepo 包数 | 15 个 package.json |
| 根依赖 | 33 deps + 8 devDeps |
| 最大子包 (apps/web) | 92 deps + 11 devDeps |
| 总依赖规模 (估算) | ~222 dependencies + ~70 devDependencies |

### 语言分布

| 语言 | 代码行数 | 占比 |
|------|---------|------|
| TSX | 37,597 | 47.1% |
| TypeScript | 26,595 | 33.3% |
| Python | 4,727 | 5.9% |
| JSON | 4,787 | 6.0% |
| SVG | 2,425 | 3.0% |
| CSS | 714 | 0.9% |
| 其他 (TOML/HTML/JS) | 339 | 0.4% |

### 子包依赖概览

| 包名 | 类型 | deps | devDeps |
|------|------|------|---------|
| @repo/web | app | 92 | 11 |
| supermemory (root) | monorepo | 33 | 8 |
| @repo/ui | package | 32 | 0 |
| @repo/lib | package | 13 | 0 |
| @supermemory/memory-graph | package | 9 | 7 |
| docs-test | package | 9 | 0 |
| supermemory-mcp | app | 8 | 7 |
| supermemory-browser-extension | app | 7 | 7 |
| @supermemory/tools | package | 7 | 9 |
| @supermemory/ai-sdk | package | 5 | 5 |
| memory-graph-playground | app | 4 | 7 |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 首次提交 | 2024-02-21 (initialised monorepo with auth and extension communication) |
| 最新提交 | 2026-03-21 (Implement MCP connection status polling #788) |
| 项目年龄 | ~25 个月 |
| 总 Commit 数 | 1,470 |
| 活跃月份数 | 21 个月 |
| 不活跃空窗期 | 2024-10 ~ 2024-12 (3个月), 2025-05 ~ 2025-07 (3个月) |
| 平均 Commit/月 | 70.0 |
| 峰值月份 | 2024-07 (268), 2024-04 (232), 2024-06 (195) |
| 贡献者总数 | 85 人 |

### 月度活跃度

| 月份 | Commits | 活跃度 |
|------|---------|--------|
| 2024-02 | 10 | ▎ |
| 2024-03 | 66 | ████ |
| 2024-04 | 232 | ████████████████ |
| 2024-05 | 25 | █▌ |
| 2024-06 | 195 | █████████████ |
| 2024-07 | 268 | ██████████████████ |
| 2024-08 | 136 | █████████ |
| 2024-09 | 16 | █ |
| 2025-01 | 25 | █▌ |
| 2025-02 | 24 | █▌ |
| 2025-03 | 24 | █▌ |
| 2025-04 | 11 | ▋ |
| 2025-05 | 3 | ▏ |
| 2025-08 | 52 | ███ |
| 2025-09 | 50 | ███ |
| 2025-10 | 100 | ██████▌ |
| 2025-11 | 34 | ██ |
| 2025-12 | 46 | ███ |
| 2026-01 | 70 | ████▌ |
| 2026-02 | 46 | ███ |
| 2026-03 | 37 | ██▌ |

### Top 贡献者

| 排名 | 贡献者 | Commits | 占比 |
|------|--------|---------|------|
| 1 | Dhravya Shah / Dhravya | 783 | 53.3% |
| 2 | MaheshtheDev / Mahesh Sanikommu | 200 | 13.6% |
| 3 | Yash | 74 | 5.0% |
| 4 | codetorso / CodeTorso | 101 | 6.9% |
| 5 | Kinfe123 | 42 | 2.9% |
| 6 | yxshv | 38 | 2.6% |
| 7 | Saatvik Arya | 27 | 1.8% |
| 8 | Prasanna721 | 18 | 1.2% |
| 9 | nexxeln | 16 | 1.1% |
| 10 | Kush Thaker | 15 | 1.0% |

### 星期分布

| 星期 | Commits | 活跃度 |
|------|---------|--------|
| 周一 | 217 | ████████████████ |
| 周二 | 249 | ██████████████████▌ |
| 周三 | 174 | ████████████▌ |
| 周四 | 201 | ██████████████▌ |
| 周五 | 182 | █████████████▌ |
| 周六 | 253 | ██████████████████▌ |
| 周日 | 194 | ██████████████ |

> 开发活跃度在工作日和周末分布较均匀，周二和周六略高，说明这是一个混合了业余时间和工作时间的开源项目。

## 演化轨迹

### 核心文件（Top 10 最常修改）

| 排名 | 文件路径 | 修改次数 |
|------|---------|---------|
| 1 | bun.lock | 56 |
| 2 | apps/docs/docs.json | 42 |
| 3 | packages/tools/package.json | 30 |
| 4 | apps/web/package.json | 21 |
| 5 | packages/tools/src/vercel/middleware.ts | 18 |
| 6 | packages/tools/README.md | 17 |
| 7 | apps/web/components/views/chat/chat-messages.tsx | 16 |
| 8 | apps/web/components/new/header.tsx | 16 |
| 9 | apps/web/components/new/chat/index.tsx | 15 |
| 10 | apps/web/components/header.tsx | 14 |

### 热点目录

| 排名 | 目录 | 修改次数 | 说明 |
|------|------|---------|------|
| 1 | apps/web | 4,747 | 核心 Web 应用，绝对热点 |
| 2 | apps/docs | 727 | 文档站点 |
| 3 | packages/ui | 637 | UI 组件库 |
| 4 | apps/extension | 340 | 旧版浏览器扩展 |
| 5 | apps/backend | 279 | 后端服务 |
| 6 | apps/cf-ai-backend | 240 | Cloudflare AI 后端 |
| 7 | packages/tools | 233 | 工具包 (SDK) |
| 8 | apps/browser-extension | 178 | 新版浏览器扩展 |
| 9 | packages/memory-graph | 128 | 记忆图谱核心 |
| 10 | apps/web-v2 | 113 | Web 应用 v2 |

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| Features/Add | 53 | 26.5% |
| Fixes/Bug | 68 | 34.0% |
| Refactor | 1 | 0.5% |
| Docs | 12 | 6.0% |
| Tests | 1 | 0.5% |
| Other | 65 | 32.5% |
| **合计** | **200** | **100%** |

> 修复类提交占比最高(34%)，其次是功能开发(26.5%)和其他类型(32.5%)。重构和测试类提交极少，说明项目处于快速迭代阶段，技术债务积累风险较高。

### 版本发布

| 指标 | 数据 |
|------|------|
| Git Tags | 无 |
| GitHub Releases | 无 |

> 项目没有正式的版本标签和发布记录，属于持续部署模式（Continuous Deployment），通过主分支持续交付。

## 项目画像卡片

```
┌──────────────────────────────────────────────────────┐
│  supermemoryai/supermemory                            │
│  "AI 记忆层 - 个人知识管理与记忆增强平台"              │
├──────────────────────────────────────────────────────┤
│  类型: Monorepo 全栈应用 (Web + 扩展 + MCP + SDK)     │
│  技术栈: TypeScript/TSX 80.4% | Python 5.9%          │
│  架构: Turborepo Monorepo (15 packages)               │
│  规模: 79,822 行代码 / 709 文件                       │
├──────────────────────────────────────────────────────┤
│  年龄: 25 个月 (2024-02 ~ 2026-03)                   │
│  总 Commits: 1,470                                    │
│  贡献者: 85 人                                        │
│  核心维护者: Dhravya Shah (53.3% commits)             │
│  平均月产出: 70 commits/月                             │
├──────────────────────────────────────────────────────┤
│  发展阶段: 快速迭代期（有两段3个月空窗）                │
│  发布模式: 持续部署 (无版本标签)                       │
│  活跃周期: 早期爆发(2024 Q2-Q3) → 休整 → 稳定回暖     │
│  代码质量信号: 测试/重构 commit 极少，修复占比 34%      │
│  热点: apps/web 占 64.5% 修改量                       │
└──────────────────────────────────────────────────────┘
```
