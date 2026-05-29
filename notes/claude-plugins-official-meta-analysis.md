# anthropics/claude-plugins-official 元分析

## 代码规模

| 语言 | 文件数 | 代码行 | 注释行 | 空行 | 总行数 |
|------|--------|--------|--------|------|--------|
| Markdown | 168 | 0 | 16,989 | 7,381 | 24,370 |
| Python | 21 | 2,761 | 237 | 503 | 3,501 |
| TypeScript | 3 | 1,579 | 157 | 162 | 1,898 |
| Shell | 16 | 1,177 | 206 | 242 | 1,625 |
| HTML | 2 | 726 | 9 | 99 | 834 |
| JSON | 12 | 241 | 0 | 1 | 242 |
| Plain Text | 1 | 0 | 169 | 33 | 202 |
| **合计** | **223** | **11,418** | **23,365** | **10,249** | **45,032** |

> Markdown 内嵌代码（BASH 1,076 行、JSON 2,094 行、TypeScript 462 行等）占比极高，含内嵌代码共 4,335 行有效代码。

**关键特征**：这是一个以 **文档/配置驱动** 为核心的插件市场仓库，纯代码行仅 11,418 行（其中近一半是 Markdown 内嵌示例代码），实际可执行代码约 6,500 行（Python + TypeScript + Shell + HTML）。仓库规模属于 **轻量级**。

## 开发节奏

| 指标 | 数值 |
|------|------|
| 首次提交 | 2025-11-20 |
| 最近提交 | 2026-03-20 |
| 项目年龄 | ~4 个月 |
| 总提交数 | 180（其中 merge 59、non-merge 121） |
| 活跃天数 | 41 天 |
| 月均提交 | ~45 次 |
| 贡献者数 | 15+ 人 |

### 月度提交分布

| 月份 | 提交数 | 趋势 |
|------|--------|------|
| 2025-11 | 7 | 项目启动 |
| 2025-12 | 11 | 缓慢增长 |
| 2026-01 | 36 | 加速开发 |
| 2026-02 | 24 | 稳步推进 |
| 2026-03 | 102 | 爆发式增长 |

> 3 月份提交量占总量的 **56.7%**，项目正处于高速迭代期。

### 工作日分布

| 星期 | 提交数 | 说明 |
|------|--------|------|
| 周一 | 8 | |
| 周二 | 31 | |
| 周三 | 23 | |
| 周四 | 48 | 高峰 |
| 周五 | 68 | **最高峰** |
| 周六 | 1 | |
| 周日 | 1 | |

> 典型的 **工作日驱动** 开发节奏，周四/周五最活跃（合计占 64.4%），周末几乎无活动，符合企业级项目特征。

### 核心贡献者

| 贡献者 | 提交数 | 角色 |
|--------|--------|------|
| Tobin South | 50 | 核心维护者（27.8%） |
| Kenneth Lien | 34 | 核心维护者（18.9%） |
| Noah Zweben | 32 | 核心维护者（17.8%） |
| Thariq Shihipar | 10 | 活跃贡献者 |
| Dickson Tsai | 8 | 贡献者 |
| Claude | 8 | AI 辅助提交 |
| Kenshiro Nakagawa | 7 | 贡献者 |
| Isabella He | 5 | 贡献者 |

> 前三名贡献者贡献了 **64.5%** 的提交。值得注意的是 **Claude（AI）** 也有 8 次提交，体现了 dogfooding 特征。

## 演化轨迹

### 版本发布

- 无标签（tags）
- 无正式 releases

> 项目尚处于早期开发阶段，未建立正式的版本发布体系。

### 高频变更文件 Top 10

| 变更次数 | 文件/目录 |
|----------|-----------|
| 57 | `.claude-plugin/marketplace.json`（插件注册表） |
| 16 | `external_plugins/telegram/server.ts` |
| 7 | `external_plugins/discord/server.ts` |
| 6 | `external_plugins/telegram/README.md` |
| 6 | `external_plugins/discord/README.md` |
| 5 | `README.md` |
| 5 | `plugins/artifact/skills/artifact/SKILL.md` |
| 5 | `.github/workflows/close-external-prs.yml` |

### 高频变更目录 Top 10

| 变更次数 | 目录 | 说明 |
|----------|------|------|
| 77 | `plugins/plugin-dev` | 插件开发工具 |
| 50 | `external_plugins/telegram` | Telegram 集成 |
| 44 | `plugins/skill-creator` | 技能创建器 |
| 41 | `external_plugins/discord` | Discord 集成 |
| 33 | `plugins/hookify` | Hook 管理 |
| 24 | `external_plugins/fakechat` | 模拟聊天 |
| 22 | `plugins/claude-code-setup` | 开发环境配置 |
| 19 | `plugins/mcp-server-dev` | MCP 服务开发 |
| 17 | `plugins/artifact` | 制品管理 |
| 15 | `plugins/math-olympiad` | 数学竞赛 |

### 提交类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 功能新增（feat/add） | 96 | 53.3% |
| 修复（fix/bug） | 15 | 8.3% |
| 文档（doc） | 4 | 2.2% |
| 测试（test） | 1 | 0.6% |
| 重构（refactor） | 0 | 0% |
| 其他 | 64 | 35.6% |

> 功能新增占提交的半数以上，修复占比仅 8.3%，说明项目处于 **快速功能扩张期**，而非稳定维护期。

### 插件生态规模

| 类别 | 数量 |
|------|------|
| 内置插件（plugins/） | 32 |
| 外部插件（external_plugins/） | 15 |
| **总计** | **47** |

## 项目画像卡片

| 维度 | 描述 |
|------|------|
| **定位** | Claude Code 官方插件市场/仓库，提供可安装的插件和技能扩展 |
| **技术栈** | Python + TypeScript + Shell + Markdown（SKILL.md 驱动） |
| **代码规模** | 轻量级（~6,500 行可执行代码），以文档/配置为核心 |
| **项目阶段** | 早期快速成长期（4 个月，无正式版本号） |
| **开发模式** | Anthropic 内部团队驱动，3 名核心维护者贡献 65% 提交 |
| **迭代速度** | 高速（月均 45 提交，3 月爆发至 102 提交） |
| **热点模块** | plugin-dev（开发工具）、telegram/discord（集成）、skill-creator（技能创建） |
| **架构特征** | 插件化、marketplace.json 中心注册、SKILL.md 技能描述范式 |
| **独特之处** | Claude AI 自身参与提交（dogfooding）；47 个插件覆盖开发工具、社交集成、教育等场景 |
| **成熟度信号** | 无 tag/release、无测试/重构提交、fix 占比低 → 典型早期原型/实验阶段 |
