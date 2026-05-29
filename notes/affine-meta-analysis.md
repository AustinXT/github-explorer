# AFFiNE 元分析

## 代码规模

| 语言 | 文件数 | 代码行数 |
|------|--------|----------|
| TypeScript | 5,609 | 569,908 |
| JSON | 584 | 175,446 |
| TSX | 1,102 | 119,725 |
| Rust | 205 | 29,664 |
| Swift | 523 | 23,108 |
| SVG | 500 | 8,134 |
| Kotlin | 35 | 5,774 |
| GraphQL | 197 | 4,449 |
| JavaScript | 29 | 3,140 |
| SQL | 104 | 1,451 |
| CSS | 7 | 605 |

**总计**: ~9,700+ 文件, 核心代码约 94 万行

## 项目历史

- **首次提交**: 2022-07-22 "init: the first public commit for AFFiNE"
- **最新提交**: 2026-03-22
- **总提交数**: 11,143
- **项目寿命**: ~3.7 年
- **平均提交**: ~8.2 commits/天

## 月度提交趋势（2025-03 至 2026-03）

| 月份 | 提交数 | 趋势 |
|------|--------|------|
| 2025-03 | 620 | 高峰 |
| 2025-04 | 603 | 高峰 |
| 2025-05 | 441 | 活跃 |
| 2025-06 | 190 | 下降 |
| 2025-07 | 283 | 回升 |
| 2025-08 | 74 | 低谷 |
| 2025-09 | 54 | 低谷 |
| 2025-10 | 42 | 低谷 |
| 2025-11 | 42 | 低谷 |
| 2025-12 | 75 | 恢复 |
| 2026-01 | 59 | 低 |
| 2026-02 | 97 | 回升 |
| 2026-03 | 74 | 稳定 |

**注意**: 2025年8月后提交量显著下降（从600+降至50-100），可能与团队重组或开发策略转变有关。

## 版本发布

### 最新版本
- **稳定版**: v0.26.3 (2026-02-25)
- **Canary**: v2026.3.20-canary.913 (2026-03-20)

### 版本命名变化
从语义化版本（v0.26.x）转向日期版本（v2026.3.x-canary），表明转向持续交付模式。

### 发布频率
Canary 版本几乎每天发布，稳定版约每月一次。

## 最近活跃目录（300次提交）

| 目录 | 变更次数 | 说明 |
|------|----------|------|
| packages/frontend | 1,289 | 前端核心 |
| packages/backend | 790 | 后端服务 |
| blocksuite/affine | 731 | 编辑器框架 |
| packages/common | 402 | 共享库 |
| blocksuite/framework | 75 | 编辑器基础框架 |
| .github/helm | 67 | Kubernetes 部署 |
| .github/workflows | 62 | CI/CD |
| tools/cli | 59 | CLI 工具 |

## 最频繁变更文件

1. yarn.lock (75) - 依赖更新频繁
2. packages/backend/server/package.json (36)
3. packages/frontend/apps/electron/package.json (18)
4. package.json (18)
5. Cargo.lock (18)
6. packages/frontend/i18n/src/resources/en.json (15) - 国际化
7. .github/workflows/build-test.yml (14)
8. packages/backend/server/schema.prisma (13) - 数据库 schema

## 顶级提交者

| 作者 | 提交数 | 身份 |
|------|--------|------|
| DarkSky (darkskygit) | 1,107 | 核心开发 |
| JimmFly | 674 | 核心开发 |
| EYHN | 589 | 核心开发 |
| Alex Yang / Himself65 | 977 (合计) | 核心开发 |
| pengx17 / Peng Xiao | 972 (合计) | 核心开发 |
| Saul-Mirone | 391 | 编辑器开发 |
| forehalo | 344 | 后端开发 |
| LongYinan / Brooooooklyn | 799 (合计) | Rust/Native |
| CatsJuice | 313 | 前端开发 |
| renovate | 424 | 自动化依赖更新 |

## 开发重心演变

从最近提交信息分析:
- **MCP 集成**: 加入 Model Context Protocol 支持（文档读写工具）
- **Copilot 重构**: 将 Copilot 模块迁移到原生实现
- **移动端**: iOS/Android 持续优化（RevenueCat 付费、代码签名）
- **编辑器性能**: edgeless 性能和内存优化
- **Gemini 集成**: 适配 Gemini 3.1 preview
- **自托管改进**: OIDC 兼容性、Docker 配置
- **国际化**: 德语等多语言更新
- **Obsidian 导入**: 支持 Obsidian vault 导入
