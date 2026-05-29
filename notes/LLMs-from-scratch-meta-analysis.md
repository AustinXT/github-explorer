# Phase 2：元分析 — rasbt/LLMs-from-scratch

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 68,892（不含空行/注释） |
| 语言分布 | Jupyter Notebooks 38.6%, Python 28.8%, JSON 22.6%, Markdown 5.9%, YAML/TOML 0.3% |
| 代码/注释比 | 3.7:1（68,892 code vs 18,644 comments） |
| 文件数量 | 287 |
| 依赖数量 | 11（requirements.txt：torch, jupyterlab, tiktoken, matplotlib, tensorflow, tqdm, numpy, pandas, psutil 等核心依赖） |

### 语言分布详情

| 语言 | 文件数 | 代码行 | 注释行 | 空行 |
|------|--------|--------|--------|------|
| Jupyter Notebooks | 62 | 15,885 | 6,360 | 4,307 |
| Python | 130 | 19,817 | 3,149 | 5,601 |
| JSON | 10 | 15,596 | 0 | 0 |
| Markdown | 67 | 0 | 2,441 | 1,693 |
| YAML | 1 | 125 | 15 | 27 |
| TOML | 2 | 102 | 3 | 15 |
| Plain Text | 15 | 0 | 215 | 37 |

> 注：Jupyter Notebooks 内嵌 Python 代码约 16,084 行、Markdown 约 5,400 行，是项目的主要载体。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 33 个月（2023-07-23 至 2026-04-05） |
| 总 commit 数 | 1,043 |
| 最近提交 | 2026-04-05 |
| 近 30 天 commit | 9 |
| 近 90 天 commit | 30 |
| 开发阶段 | 成熟维护期：核心内容完整，处于持续改进与扩展阶段 |
| 开发模式 | 单核心驱动 + 社区贡献。Sebastian Raschka 贡献 873/1043 commits（83.7%），Daniel Kleine 63 commits 为主要协作者。周末（周六周日）提交量最高（170+208），表现出个人项目/教育写作的典型模式。高峰时段集中在早晨 6-8 点（美东时区），符合晨间写作习惯。 |

### 月度 Commit 分布

| 月份 | Commits | 备注 |
|------|---------|------|
| 2023-07 | 1 | 项目创建 |
| 2023-09 ~ 2023-10 | 9 | 早期准备 |
| 2023-12 ~ 2024-01 | 63 | 书稿加速编写 |
| 2024-02 ~ 2024-03 | 164 | **第一波高峰**：核心章节密集开发 |
| 2024-04 ~ 2024-06 | 339 | **历史峰值**：书籍出版前冲刺期 |
| 2024-07 ~ 2024-10 | 166 | 出版后持续完善 |
| 2024-11 ~ 2025-01 | 34 | 低活跃期 |
| 2025-02 ~ 2025-04 | 82 | 第二波活跃：新增 bonus 内容 |
| 2025-06 ~ 2025-12 | 130 | 持续扩展（Llama、Gemma 等模型） |
| 2026-01 ~ 2026-04 | 35 | 维护更新 |

### 星期分布

| 星期 | Commits |
|------|---------|
| 周一 | 143 |
| 周二 | 146 |
| 周三 | 148 |
| 周四 | 113 |
| 周五 | 115 |
| 周六 | 170 |
| **周日** | **208** |

### 贡献者分布

| 贡献者 | Commits |
|--------|---------|
| Sebastian Raschka (rasbt) | 873（83.7%） |
| Daniel Kleine | 63（6.0%） |
| casinca | 15（1.4%） |
| Intelligence-Manifesto | 9（0.9%） |
| TITC | 7（0.7%） |
| 其他 | 76（7.3%） |

## 演化轨迹

### 核心文件（Top 10 最常修改）

| 修改次数 | 文件 |
|----------|------|
| 126 | `README.md` |
| 72 | `ch05/01_main-chapter-code/ch05.ipynb` |
| 64 | `ch02/01_main-chapter-code/ch02.ipynb` |
| 61 | `.gitignore` |
| 58 | `ch04/01_main-chapter-code/ch04.ipynb` |
| 53 | `ch06/01_main-chapter-code/ch06.ipynb` |
| 49 | `ch03/01_main-chapter-code/ch03.ipynb` |
| 47 | `ch07/01_main-chapter-code/ch07.ipynb` |
| 45 | `ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb` |
| 38 | `ch06/02_bonus_additional-experiments/README.md` |

> README.md 以 126 次修改高居榜首，反映了项目作为教育资源持续更新目录和说明。ch05（预训练）和 ch02（文本处理）是修改最频繁的章节核心代码。

### 热点目录

| 修改次数 | 目录 |
|----------|------|
| 156 | `ch05/01_main-chapter-code` — 预训练 GPT |
| 152 | `ch04/01_main-chapter-code` — 从零实现 GPT |
| 152 | `.github/workflows` — CI/CD |
| 138 | `ch02/01_main-chapter-code` — 文本数据处理 |
| 137 | `pkg/llms_from_scratch` — 可安装包 |
| 118 | `ch03/01_main-chapter-code` — 注意力机制 |
| 116 | `ch05/11_qwen3` — Qwen3 模型扩展 |
| 105 | `ch05/07_gpt_to_llama` — Llama 转换 |
| 99 | `ch07/01_main-chapter-code` — 指令微调 |
| 97 | `ch06/01_main-chapter-code` — 文本分类 |

> ch04-ch05（模型实现与预训练）是绝对热点，`.github/workflows` 高频修改说明持续维护 CI 流程。`ch05/11_qwen3` 和 `ch05/07_gpt_to_llama` 等扩展目录活跃度高，说明作者持续将新模型架构纳入教学体系。

### Commit 类型分布（近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 功能新增（feat/add） | 27 | 13.5% |
| 缺陷修复（fix/bug） | 44 | 22.0% |
| 重构 | 0 | 0% |
| 文档 | 2 | 1.0% |
| 测试 | 4 | 2.0% |
| 其他（更新、改进等） | 123 | 61.5% |

> 修复类提交占比最高（22%），体现教育项目对准确性的高要求。大量「其他」类型的提交主要是内容更新、格式调整、notebook 改进等，不符合传统 commit message 分类但属于教育项目的正常模式。

### 版本发布

无 Git tag 和 GitHub Release。项目采用持续更新模式，以书籍出版为里程碑（《Build a Large Language Model (From Scratch)》，Manning Publications, 2024），不设软件版本号。

## 项目画像卡片

```
┌─────────────────────────────────────────────┐
│  rasbt/LLMs-from-scratch                    │
│  ─────────────────────────────────────────  │
│  类型：教育类开源项目（配套书籍代码仓库）      │
│  规模：中型（287 文件 / 68.9K 代码行）        │
│  年龄：33 个月（2023.07 - 2026.04）          │
│  活跃度：持续活跃（1,043 commits）            │
│  节奏：成熟维护期，月均 ~10 commits           │
│  模式：作者主导型（83.7% 来自 Raschka）       │
│  特征：                                      │
│  · 以 Jupyter Notebooks 为核心载体            │
│  · 周末+晨间写作为主要开发时段                │
│  · 持续扩展新模型架构（Llama, Qwen, Gemma）   │
│  · 修复/精确性提交占比高，体现教育品质追求     │
│  · 无版本发布，以书籍出版为核心里程碑          │
│  · 依赖精简（11 个），专注教学而非工程化       │
└─────────────────────────────────────────────┘
```
