## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 175,182 行（含空白/注释共 207,940 行） |
| 语言分布 | Python 56.9%（99,557 行）、TSX 22.8%（39,884 行）、TypeScript 11.2%（19,530 行）、YAML 3.4%（5,910 行）、Shell 1.6%（2,794 行）、PowerShell 1.6%（2,729 行）、JSON 1.4%（2,396 行）、其他 1.1% |
| 代码/注释比 | 14.5:1（175,182 代码 / 12,089 注释） |
| 文件数量 | 796 个源码文件（270 Python + 220 TSX + 165 TypeScript + 82 YAML + 其他） |
| 依赖数量 | 核心依赖 4 个（typer, pydantic, pyyaml, nest-asyncio）+ HuggingFace 无 Torch 组 17 个 + 大量 CUDA/ROCm/Intel 版本矩阵可选依赖（150+ 组合） |
| 仓库体积 | 68.9 MB |
| 当前版本 | 2026.4.2 |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 28.2 个月（2023-11-29 创建） |
| 总 commit 数 | 4,976 |
| 最近提交 | 2026-04-06 |
| 近 30 天 commit | 675 |
| 近 90 天 commit | 1,694 |
| 近 52 周 commit | 2,884 |
| 平均 commit/月 | 176 |
| 平均 commit/周 | 40.5 |
| 贡献者总数 | 159 人 |
| 开发阶段 | **爆发加速期** — 近 30 天 675 次提交远超历史月均 176 次，增长 3.8 倍，正经历 Studio 产品化冲刺 |
| 开发模式 | **核心驱动+社区贡献型** — Daniel Han 主导提交（浅克隆中占 64%），PR 机制活跃（#4866 为最新编号），工作日高强度（周四 28 次 > 周五 15 次 > 周三 6 次），周末极少（周日仅 1 次） |

## 演化轨迹

### 核心文件（Top 10 — 近期最活跃）

| 排名 | 文件 | 变更次数 |
|------|------|----------|
| 1 | studio/setup.sh | 10 |
| 2 | studio/install_llama_prebuilt.py | 10 |
| 3 | studio/setup.ps1 | 9 |
| 4 | studio/backend/core/inference/llama_cpp.py | 9 |
| 5 | studio/backend/routes/inference.py | 6 |
| 6 | unsloth/models/loader.py | 5 |
| 7 | tests/studio/install/test_pr4562_bugfixes.py | 5 |
| 8 | studio/backend/utils/models/model_config.py | 5 |
| 9 | studio/backend/core/inference/tools.py | 5 |
| 10 | install_gemma4_mlx.sh | 5 |

### 热点目录

| 目录 | 变更次数 | 占比 |
|------|----------|------|
| studio/frontend | 505 | 52.3% |
| studio/backend | 262 | 27.1% |
| unsloth/kernels | 38 | 3.9% |
| unsloth/models | 31 | 3.2% |
| tests/saving | 24 | 2.5% |
| tests/studio | 17 | 1.8% |
| tests/utils | 16 | 1.7% |
| unsloth/registry | 9 | 0.9% |
| tests/python | 9 | 0.9% |
| unsloth_cli/commands | 5 | 0.5% |

> 近期开发重心极度集中在 **Unsloth Studio**（前端+后端占近 80%），核心训练库 unsloth/ 本身已趋于稳定。

### Commit 类型分布（近 50 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| Fix/Bug | 26 | 52% |
| Feature/Add | 9 | 18% |
| Test | 1 | 2% |
| Refactor | 0 | 0% |
| Docs | 0 | 0% |
| Other | 14 | 28% |

> 修复类提交高达 52%，表明 Studio 刚上线处于密集打磨阶段，快速迭代修复用户反馈问题。Feature 类 18% 主要围绕 Gemma 4 模型支持和 Studio 功能增强。

### 版本发布（30 个 Release，近期加速）

| 版本 | 日期 | 名称/亮点 |
|------|------|-----------|
| v0.1.35-beta | 2026-04-02 | Google Gemma 4 支持 |
| v0.1.3-beta | 2026-03-31 | +50% 工具调用准确率 |
| v0.1.25-beta | 2026-03-27 | 重要更新 |
| v0.1.2-beta | 2026-03-25 | Studio 上线后首个正式版 |
| v0.1.0-beta | 2026-03-17 | **Unsloth Studio (Beta)** 发布 |
| February-2026 | 2026-02-10 | 12x 更快 MoE 训练 + Embedding 支持 |
| December-2025 | 2025-12-18 | 3x 更快训练 |
| November-2025 | 2025-11-25 | FP8 训练 |
| October-2025 | 2025-10-27 | Docker 支持 |
| September-2025-v3 | 2025-09-26 | RL + Auto Kernel Notebook |
| September-2025-v2 | 2025-09-16 | Vision RL + 内存高效 RL |
| August-2025-v2 | 2025-08-28 | Flex Attention + 长上下文训练 |
| August-2025 | 2025-08-08 | 开源模型微调 |
| July-2025 | 2025-07-10 | 降低显存 + Bug 修复 |
| June-2025 | 2025-06-26 | Gemma 3n + TTS |

> 发布节奏从 2025 年「月度发布」演进到 2026 年 3 月起「每周多个版本」，Studio 上线后 20 天内发布 5 个 beta 版本，进入产品化快速迭代期。

## 项目画像卡片

```
┌─────────────────────────────────────────────┐
│  unslothai/unsloth                          │
│  「2-5X faster LLM fine-tuning framework」   │
├─────────────────────────────────────────────┤
│  ⏱ 28.2 个月  │  ⭐ 59,596  │  🍴 5,058     │
│  📊 4,976 commits │ 👥 159 contributors     │
│  📦 175K 代码行 │ 🐍 Python + TSX/TS        │
├─────────────────────────────────────────────┤
│  开发阶段：爆发加速期（Studio 产品化冲刺）      │
│  发布频率：近期每周多版本（v0.1.x-beta 密集）  │
│  代码特征：14.5:1 代码注释比，工程导向         │
│  架构演化：训练库 → 全栈产品（Python+React）   │
├─────────────────────────────────────────────┤
│  关键转折点：                                 │
│  • 2023-11 创建，专注 LoRA 加速微调           │
│  • 2025-H2 引入 RL、Vision、MoE 等高级功能   │
│  • 2026-03 发布 Unsloth Studio，从库到产品    │
│  • 2026-04 Gemma 4 首发支持，生态卡位         │
│  当前重心：Studio 稳定性修复 (52%) +          │
│           新模型快速适配 (18%)                │
└─────────────────────────────────────────────┘
```
