# AstrBot 量化分析报告（Meta Analysis）

> 仓库：AstrBotDevs/AstrBot
> 分析日期：2026-04-07

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 183,820（不含空行/注释） |
| 语言分布 | Python 57.7% (106,130行), Vue 4.0% (7,377行), YAML 3.4% (6,291行), TypeScript 3.0% (5,584行), JavaScript 1.5% (2,766行), CSS 0.6% (1,149行), 其他 29.8% (含 JSON 配置 16,484行、Markdown 文档等) |
| 代码/注释比 | 8.9:1（注释 20,589 行，代码 183,820 行） |
| 文件数量 | 1,237 |
| 依赖数量 | 77 runtime + 5 dev（共 82 个，来自 pyproject.toml） |

### 语言详情（tokei）

| 语言 | 文件数 | 总行数 | 代码 | 注释 | 空行 |
|------|--------|--------|------|------|------|
| Python | 480 | 126,780 | 106,130 | 3,613 | 17,037 |
| Vue | 129 | 8,462 | 7,377 | 232 | 853 |
| YAML | 20 | 8,119 | 6,291 | 59 | 1,769 |
| TypeScript | 49 | 7,006 | 5,584 | 624 | 798 |
| JavaScript | 16 | 3,388 | 2,766 | 209 | 413 |
| JSON | 134 | 16,485 | 16,484 | 0 | 1 |
| Markdown | 369 | 19,704 | 0 | 13,338 | 6,366 |
| CSS | 2 | 1,593 | 1,149 | 116 | 328 |
| Sass | 15 | 701 | 606 | 26 | 69 |
| Shell | 4 | 509 | 400 | 37 | 72 |
| 其他 | 15 | 1,247 | 1,033 | 35 | 179 |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 40 个月（首次提交 2022-12-08） |
| 总 commit 数 | 4,442 |
| 最近提交 | 2026-04-07 |
| 近 30 天 commit | 279 |
| 近 90 天 commit | 777 |
| 近 365 天 commit | 2,522 |
| 开发阶段 | 密集开发（月均 commit 持续 > 100，2025 年月均 196） |
| 开发模式 | 职业项目（周末占比 32.0%，工作日 68.0%；下午+晚间为主，分别占 37.0% 和 34.6%） |
| 贡献者数量 | 242 人 |

### 月度 Commit 分布

```
 64  2022-12  ← 项目启动
 14  2023-01
 18  2023-02
 92  2023-03
125  2023-04  ← v3.0.0 发布
 91  2023-05
 56  2023-06
  1  2023-07  ← 低谷
 33  2023-08
 42  2023-09
 12  2023-10
 33  2023-11
 50  2023-12
 18  2024-01
 27  2024-02
 19  2024-03
  9  2024-04  ← 低谷
 41  2024-05
 11  2024-06
 30  2024-07
 57  2024-08
 40  2024-09
 17  2024-10
 16  2024-11
 65  2024-12  ← 恢复增长
148  2025-01  ← 密集开发开始
323  2025-02  ← 峰值
407  2025-03  ← 峰值（全项目最高）
292  2025-04
294  2025-05
289  2025-06
174  2025-07
 84  2025-08
134  2025-09
169  2025-10
183  2025-11
165  2025-12
130  2026-01
345  2026-02  ← 再次密集
293  2026-03
 31  2026-04  ← 进行中（截至 4/7）
```

### 每日时段分布

| 时段 | Commit 数 | 占比 |
|------|-----------|------|
| 深夜 (00-06) | 519 | 11.7% |
| 上午 (06-12) | 743 | 16.7% |
| 下午 (12-18) | 1,642 | 37.0% |
| 晚间 (18-24) | 1,538 | 34.6% |

### 星期分布

| 星期 | Commit 数 |
|------|-----------|
| 周一 | 625 |
| 周二 | 651 |
| 周三 | 578 |
| 周四 | 607 |
| 周五 | 560 |
| 周六 | 701 |
| 周日 | 720 |

## 演化轨迹

### 核心文件（Top 15 最常修改）

1. astrbot/core/config/default.py — 31 次修改
2. astrbot/core/provider/sources/openai_source.py — 19 次修改
3. dashboard/src/i18n/locales/en-US/features/config-metadata.json — 18 次修改
4. pyproject.toml — 16 次修改
5. dashboard/src/i18n/locales/zh-CN/features/config-metadata.json — 16 次修改
6. dashboard/src/i18n/locales/ru-RU/features/config-metadata.json — 10 次修改
7. dashboard/src/assets/mdi-subset/* — 10 次修改（字体资源）
8. .github/workflows/pr-checklist-check.yml — 10 次修改
9. tests/test_dashboard.py — 9 次修改
10. astrbot/cli/__init__.py — 9 次修改
11. tests/test_tool_loop_agent_runner.py — 8 次修改
12. README.md — 7 次修改
13. docs/.vitepress/config.mjs — 7 次修改
14. astrbot/core/skills/skill_manager.py — 7 次修改
15. astrbot/core/provider/sources/gemini_source.py — 7 次修改

### 热点目录

1. astrbot/core — 545 次修改
2. dashboard/src — 525 次修改
3. docs/zh — 142 次修改
4. docs/en — 116 次修改
5. astrbot/dashboard — 79 次修改
6. .github/workflows — 41 次修改
7. astrbot/cli — 31 次修改
8. tests/unit — 28 次修改
9. docs/.vitepress — 17 次修改
10. tests/fixtures — 13 次修改
11. astrbot/builtin_stars — 11 次修改
12. desktop/lib — 8 次修改

### Commit 类型分布（最近 500 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| Fix/Bug | 232 | 46.4% |
| Feature/Add | 121 | 24.2% |
| Chore | 53 | 10.6% |
| Refactor | 35 | 7.0% |
| Doc | 19 | 3.8% |
| Test | 3 | 0.6% |
| Other | 37 | 7.4% |

> 注：Fix 占比较高，反映项目处于快速迭代中，同时持续修复功能和适配多平台。

### 版本发布

- 最新版本：v4.22.3（2026-04-04）
- 总 Release 数：208 个（GitHub Releases）
- 总 Tag 数：218 个
- 版本策略：语义化版本（SemVer），从 v3.0.0 开始规范，此前使用 publish 风格命名
- 早期版本：publish（2023-01-09）→ v3.0.0（2023-04-09）→ v4.x（2025 年起）
- 发版节奏：近期高频发版，2026 年 3 月单月发布 5 个版本（v4.19.3 ~ v4.22.0）

### 核心贡献者（Top 10）

| 贡献者 | Commit 数 | 占比 |
|--------|-----------|------|
| Soulter | 3,107 | 69.9% |
| Raven95676 | 173 | 3.9% |
| 氕氙 | 143 | 3.2% |
| anka | 63 | 1.4% |
| LIghtJUNction | 54 | 1.2% |
| RC-CHN | 45 | 1.0% |
| IGCrystal | 41 | 0.9% |
| Gao Jinzhe | 32 | 0.7% |
| pre-commit-ci[bot] | 30 | 0.7% |
| Dt8333 | 27 | 0.6% |

> 项目呈现典型的「BDFL」模式，核心维护者 Soulter 贡献了近 70% 的 commit。

## 项目画像卡片

```
项目: AstrBotDevs/AstrBot
年龄: 40 个月 | 代码: 183,820 行 (Python/Vue/TypeScript)
总 commits: 4,442 | 贡献者: 242 人
开发阶段: 密集开发
开发模式: 职业项目（工作日 68%，下午/晚间占 71.6%）
核心文件: config/default.py, openai_source.py, config-metadata.json, pyproject.toml
Release: v4.22.3 (共 208 个版本)
```

## 关键发现

1. **高速迭代**：项目在 2025 年 2-3 月达到开发高峰（月均 365 commits），至今保持月均 150+ commits 的强度，处于密集开发阶段。
2. **大规模重写**：从 v3.x（2023 年初）到 v4.x 的演进，伴随代码量从零到 18 万行的爆发式增长，2025 年初的 commit 激增暗示了可能的大版本重构。
3. **多语言全栈**：Python 后端 + Vue/TypeScript 前端 Dashboard + 多平台文档（中/英），是一个完整的全栈项目。
4. **重度依赖**：77 个 runtime 依赖涵盖 LLM SDK（OpenAI、Anthropic、Google GenAI）、IM 平台 SDK（Telegram、Discord、微信、钉钉、飞书等），体现了「多平台聊天机器人框架」的定位。
5. **社区驱动**：242 位贡献者，但核心依赖 Soulter 一人（69.9% commits），存在单点维护风险。
6. **发版频繁**：208 个 release，近期几乎每周发版，说明功能迭代快但也可能暗示质量控制的挑战。
