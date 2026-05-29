# openai/skills 元分析报告（Phase 2: When & How Much）

> 分析时间: 2026-03-22
> 仓库: openai/skills
> 本地路径: /tmp/repo-miner-skills

## 代码规模

| 指标 | 数据 |
|------|------|
| 总行数 | 99,379（含所有文本文件） |
| 可执行代码行数 | 14,489（Python/JS/Shell/Swift/PowerShell） |
| 语言分布 | Markdown 80.2%, Python 10.9%, TXT(LICENSE) 7.2%, JavaScript 3.4%, YAML 0.7%, Shell 0.4%, 其他 1.2% |
| 代码/注释比 | 约 37:1（代码 12,570 行 vs 注释 342 行，仅统计可执行代码文件） |
| 文件数量 | 712 |
| 依赖数量 | 0（无 package.json / requirements.txt / pyproject.toml，各 skill 自包含） |

**说明：**
- 这是一个"技能仓库"（Skill Registry），并非传统意义上的应用程序。绝大多数内容是 Markdown 文档（501 个文件，占 80.2%），用于描述每个 skill 的定义、参考资料和 prompt 模板
- 实际可执行代码（Python 29 个文件、JS 11 个、Shell 3 个、Swift 3 个、PowerShell 1 个）仅 47 个文件共 14,489 行，占比很小
- YAML 文件（46 个）为 OpenAI Agent 的配置文件（`openai.yaml`），定义了每个 skill 的 agent 行为
- TXT 文件（41 个）几乎全是 LICENSE.txt，每个 skill 独立携带 MIT 许可证
- 项目无集中依赖管理，每个 skill 是独立的自包含单元

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 4 个月（首次提交 2025-11-24） |
| 总 commit 数 | 83 |
| 最近提交 | 2026-03-20 |
| 近 30 天 commit | 16 |
| 近 90 天 commit | 61 |
| 近 365 天 commit | 83（项目尚不满一年） |
| 开发阶段 | **密集开发**（新项目快速扩张中，4 个月内从 0 增长到 36 个 curated skills） |
| 开发模式 | **职业项目**（周末占比 25.3%，深夜占比 18.1%） |

**开发节奏详解：**

- **2025-11（启动期）**：1 次提交（初始化仓库）
- **2025-12（爆发期）**：23 次提交，大量基础 skill 密集上线（vercel-deploy, sentry, pdf, yeet 等）
- **2026-01（持续扩张）**：20 次提交，继续添加新 skill（atlas, playwright, 实验性 skill 等）
- **2026-02（活跃迭代）**：24 次提交，高密度开发，添加 slides, playwright-interactive, chatgpt-apps 等复杂技能
- **2026-03（截至20日）**：15 次提交，继续添加新 skill（frontend-skill），同时更新已有 skill

**工作时间分布：**
- 高峰时段：9-10 时、12 时、15-19 时，呈典型双峰型（上午 + 下午），符合北美职业开发者工作时间
- 周一 commit 最密集（18 次），其次为周四/五/六（各 14-15 次）
- 深夜（22-06 时）占比 18.1%，有一定的非工作时间开发，可能涉及多时区协作

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. `skills/.system/skill-creator/SKILL.md` — 6 次修改（skill 创建模板，频繁调优）
2. `skills/.curated/vercel-deploy/SKILL.md` — 5 次修改
3. `skills/.curated/vercel-deploy/agents/openai.yaml` — 5 次修改
4. `skills/.curated/figma-implement-design/SKILL.md` — 5 次修改
5. `skills/.curated/atlas/agents/openai.yaml` — 5 次修改
6. `README.md` — 5 次修改
7. `skills/.system/skill-creator/scripts/init_skill.py` — 4 次修改
8. `skills/.experimental/wrapped/SKILL.md` — 4 次修改
9. `skills/.experimental/wrapped/scripts/report.sh` — 4 次修改
10. `skills/.curated/yeet/agents/openai.yaml` — 4 次修改

**洞察：** 修改最频繁的是 skill-creator（造技能的技能）和 vercel-deploy（部署类技能），说明基础设施和部署能力是团队最关注的核心能力。每个文件修改次数均较低（最多 6 次），因为项目年轻且内容以"添加新 skill"为主，而非反复修改已有内容。

### 热点目录

1. `skills/.curated` — 856 次文件变更（主要技能目录，36 个 skill）
2. `skills/.experimental` — 110 次文件变更（实验性技能，大部分已被清理）
3. `skills/.system` — 59 次文件变更（系统级技能：skill-creator, skill-installer, openai-docs）
4. `.github/workflows` — 3 次文件变更（CI/CD）

**洞察：** `.curated` 目录承载了绝大多数变更（83.3%），是项目核心。`.experimental` 曾活跃但后来经历了一次清理（`Remove experimental skills except wrapped`），表明团队对技能质量有把控意识。

### Commit 类型分布（全部 83 条 commit）

| 类型 | 数量 | 占比 |
|------|------|------|
| Feature/Add | 37 | 44.6% |
| Other（Update/Remove/Rename 等）| 39 | 47.0% |
| Fix/Bug | 3 | 3.6% |
| Docs | 3 | 3.6% |
| Test | 1 | 1.2% |
| Refactor | 0 | 0.0% |

**洞察：** Feature/Add 占 44.6%，说明项目处于快速扩张的"内容生产"阶段，主要工作是添加新 skill。Bug 极少（3.6%），因为 skill 定义本质是声明式配置 + 文档，不容易出 bug。没有 Refactor，代码结构从一开始就比较稳定。

### 版本发布

- **无 Tag/Release**：项目没有使用 Git Tag 或 GitHub Release
- **版本策略**：无版本概念，采用持续交付模式（main 分支直接合并 PR）
- **发布节奏**：通过 PR 合并驱动，PR 编号已达 #284，说明有大量 PR 活动（含创建后关闭的）

### 贡献者

| 排名 | 贡献者 | Commits |
|------|--------|---------|
| 1 | Gav Verma | 17（20.5%） |
| 2 | Vaibhav Srivastav | 15（18.1%） |
| 3 | Dominik Kundel | 13（15.7%） |
| 4 | github-actions[bot] | 9（10.8%） |
| 5 | Ed Bayes | 7（8.4%） |
| 6 | Andrew Qu | 4 |
| 7 | Eric Traut | 4 |
| 8 | Luke | 3 |
| 9 | ae | 3 |
| 10 | Curtis 'Fjord' Hawthorne | 2 |

- **总贡献者**: 24 人（不含 bot）
- **核心维护者**: Gav Verma、Vaibhav Srivastav、Dominik Kundel 三人贡献了 54.2% 的 commit
- **特征**: 典型的小团队协作项目，由 3 位核心开发者驱动，20+ 位贡献者参与，多为 OpenAI 内部员工（从用户名可推断如 `cching-openai`、`cguo-oai`、`lukeqin-oai`、`xl-openai`、`alistair-openai`、`easong-openai` 等）

## 项目画像卡片

```
项目: openai/skills
年龄: 4 个月  |  文件: 712 个  |  总行数: 99,379（可执行代码 14,489 行）
总 commits: 83  |  贡献者: 24 人
开发阶段: 密集开发（快速扩张，4 个月内建成 36 个 curated + 3 个 system skills）
开发模式: 职业项目（OpenAI 内部团队，周末占比 25.3%，深夜 18.1%）
核心文件: skill-creator/SKILL.md, vercel-deploy, figma-implement-design
Release: 无版本发布（持续交付模式）
关键特征: 技能注册中心 — 以 Markdown+YAML 声明式定义为主，少量 Python/JS 脚本辅助
         OpenAI 内部 3 人核心团队驱动，快速构建 Agent 生态的基础设施层
```
