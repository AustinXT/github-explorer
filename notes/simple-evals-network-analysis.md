# openai/simple-evals 网络分析

## 仓库基本数据

| 指标 | 值 |
|------|-----|
| 名称 | openai/simple-evals |
| URL | https://github.com/openai/simple-evals |
| 描述 | （无官方描述） |
| 主语言 | Python（148.5 KB），Jupyter Notebook（101.8 KB） |
| 许可证 | MIT License |
| 创建时间 | 2024-04-11 |
| 最后推送 | 2025-07-31（已添加弃用通知后停止更新） |
| Stars | 4,406 |
| Forks | 481 |
| Watchers | 48 |
| Issues | 33（开放约10个） |
| PRs | 21 |
| 磁盘占用 | 95 KB |
| 是否归档 | 否（但已声明弃用） |
| 是否Fork | 否 |
| 发布版本 | 无 |
| Topics | 无 |

## 作者画像

### 组织：OpenAI

| 指标 | 值 |
|------|-----|
| 登录名 | openai |
| 名称 | OpenAI |
| 官网 | https://openai.com/ |
| 公开仓库数 | 234 |
| 关注者 | 115,871 |
| 创建时间 | 2015-10-03 |

OpenAI 是全球最知名的 AI 研究公司之一，GPT 系列模型、ChatGPT、DALL-E 等产品的创造者。作为组织账号拥有超过11.5万关注者，是 GitHub 上影响力最大的 AI 组织之一。

### 核心贡献者

| 贡献者 | 提交数 | 备注 |
|--------|--------|------|
| etr2460 | 15 | 最多贡献 |
| jmcgraph-oai | 12 | OpenAI 内部员工 |
| mgl-openai | 11 | OpenAI 内部员工 |
| kzl-openai | 10 | OpenAI 内部员工 |
| karina-openai | 7 | OpenAI 内部员工 |
| Edward-Sun | 5 | - |
| rahul-openai | 5 | OpenAI 内部员工，HealthBench 负责人 |
| shanth-openai | 4 | OpenAI 内部员工 |
| yuchenhe07 | 4 | - |
| karans-openai | 3 | OpenAI 内部员工，弃用通知作者 |

**特征**：绝大多数贡献者带有 `-openai` 后缀，说明这是一个典型的企业内部项目开源，社区外部参与极少（仅 eltociear 贡献了2次 typo 修复）。

## 社区热度

### Star 增长曲线

通过分页采样（每页100个 star），还原增长轨迹：

| 时间段 | Star 范围 | 说明 |
|--------|-----------|------|
| 2024-04-11 ~ 2024-04-12 | 1 ~ 100 | 发布首日即获100+ stars |
| 2024-04-12 ~ 2024-05-14 | 100 ~ 1,000 | 首月高速增长 |
| 2024-05-14 ~ 2024-12-13 | 1,000 ~ 2,000 | 平稳增长（约7个月） |
| 2024-12-13 ~ 2025-05-14 | 2,000 ~ 3,000 | 5个月增长1000（HealthBench 发布带动） |
| 2025-05-14 ~ 2025-09-11 | 3,000 ~ 4,000 | 4个月增长1000 |
| 2025-09-11 ~ 2026-03-17 | 4,000 ~ 4,406 | 6个月仅增400+，增速明显放缓 |

**趋势判断**：项目在2025年7月宣布弃用后，star 增速显著放缓。当前仍有稳定但缓慢的 star 增长（约每天1-2个），主要来自引用和搜索流量，而非活跃推广。

### 最近 star 活动（2026年3月）

近30天仍有持续的 star 增加，最新一次为 2026-03-17，说明项目作为参考资料仍有持续关注度。

### 代码活跃度

- **最近12周提交数**：全部为0
- **最后一次提交**：2025-07-09（添加弃用通知）
- **状态**：项目代码已冻结，不再接受新功能

## 生态网络

### 依赖关系

- **上游依赖**：`openai`、`anthropic` Python SDK
- **下游被依赖**：GraphQL 查询显示 0 个依赖方（项目未发布为 pip 包，以源码形式使用）
- **Fork 生态**：481个 fork，但最高星 fork 仅2颗星，说明未产生有影响力的衍生项目

### 包含的评测基准

| 基准 | 领域 | 来源 |
|------|------|------|
| MMLU | 多任务语言理解 | Hendrycks et al. |
| MATH / MATH-500 | 数学推理 | Hendrycks et al. |
| GPQA | 研究生级QA | Rein et al. |
| DROP | 阅读理解（离散推理） | Allen AI |
| MGSM | 多语言数学 | Google Research |
| HumanEval | 代码生成 | OpenAI |
| SimpleQA | 短形式事实性 | OpenAI（原创） |
| BrowseComp | 浏览代理评估 | OpenAI（原创） |
| HealthBench | 医疗健康LLM评估 | OpenAI（原创） |

### 支持的模型采样器

- OpenAI API（GPT-4系列、o系列）
- Anthropic API（Claude系列）

## 官方文档洞察

### README 关键信息

1. **定位声明**："lightweight library for evaluating language models"——轻量级评测库，不是全面评测框架
2. **设计哲学**：强调零样本、思维链（zero-shot, chain-of-thought）提示方式，认为这比少样本或角色扮演提示更能反映模型真实水平
3. **弃用通知**（2025年7月）：不再为新模型更新评测结果，仅维护 HealthBench、BrowseComp、SimpleQA 三个原创基准的参考实现
4. **与 openai/evals 的关系**：明确表示本仓库不是 openai/evals 的替代品，后者是"comprehensive collection"
5. **维护态度**："We will not be actively maintaining this repository"——不主动维护，但可能接受 bug 修复和新模型适配器

### 基准结果表

README 中包含详细的模型评测对比表，覆盖：
- OpenAI 全系列（o3、o4-mini、o3-mini、o1、GPT-4.1、GPT-4o、GPT-4.5-preview、GPT-4 Turbo）
- 第三方报告值（Claude 3.5 Sonnet、Claude 3 Opus、Llama 3.1、Grok 2、Gemini）

这是此仓库最核心的价值——**官方基准数据的透明公布**。

## 竞品清单

| 项目 | 定位 | 差异点 |
|------|------|--------|
| [openai/evals](https://github.com/openai/evals) | OpenAI 综合评测框架 | 更全面、更复杂，支持社区贡献评测，simple-evals 明确表示不替代它 |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 社区标准 LLM 评测框架 | 支持400+任务、多后端、更活跃维护，是学术界最广泛使用的评测工具 |
| [huggingface/lighteval](https://github.com/huggingface/lighteval) | HuggingFace 轻量评测 | 与 HF 生态深度集成，支持更多模型 |
| [explodinggradients/ragas](https://github.com/explodinggradients/ragas) | RAG 评估框架 | 专注 RAG 管道评估，与 simple-evals 定位不同 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | LLM 应用评测 | 更面向应用层评估（幻觉、毒性等），商业化方向 |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | ML 生命周期管理 | 评测仅为其功能子集，更偏实验管理 |

**simple-evals 的独特定位**：不追求全面性，而是提供 OpenAI 模型官方评测数据的透明参考实现。其最大价值不在工具本身，而在于作为 OpenAI 公布的基准分数的可复现验证。

## 关键 Issue 信号

### 高讨论度 Issue

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| [#3](https://github.com/openai/simple-evals/pull/3) | Fix types overriding the stdlib module "types" | 5 | 已关闭 | 早期代码质量问题 |
| [#77](https://github.com/openai/simple-evals/issues/77) | Incorrect scores in HealthBench? | 4 | 开放 | 评测结果准确性质疑 |
| [#1](https://github.com/openai/simple-evals/issues/1) | Demo does not run - azure credentials | 4 | 已关闭 | 开箱体验差 |
| [#28](https://github.com/openai/simple-evals/issues/28) | How do we run this code? | 3 | 开放 | 文档不足，使用门槛高 |
| [#97](https://github.com/openai/simple-evals/issues/97) | What to do now that simple-evals won't be updated? | 2 | 开放 | 社区对弃用的困惑 |
| [#76](https://github.com/openai/simple-evals/issues/76) | Access to HealthBench Dataset? | 2 | 开放 | 数据集获取问题 |
| [#96](https://github.com/openai/simple-evals/issues/96) | healthbench_eval can not reproduced 0.67 on the gpt-5 | 1 | 开放 | 可复现性问题 |
| [#35](https://github.com/openai/simple-evals/issues/35) | Release SimpleQA on Hugging Face | 2 | 开放 | 数据分发诉求 |

### Issue 模式分析

1. **使用门槛高**：#1、#28、#80 都反映"如何运行"的困惑，说明文档严重不足
2. **可复现性质疑**：#77、#96 质疑评测分数的正确性，对于评测框架来说这是核心信任问题
3. **弃用焦虑**：#97 直接发问"弃用后怎么办"，社区缺乏后续方向指引
4. **官方回应少**：Issue 回复率低，符合 README 声明的"不主动维护"

## 知识入口

| 平台 | 链接 | 状态 |
|------|------|------|
| DeepWiki | https://deepwiki.com/openai/simple-evals | 可用，最后索引 2025-11-07，包含架构分析、类型系统、扩展指南等完整文档 |
| GitHub README | https://github.com/openai/simple-evals | 主要信息源，包含基准结果表和使用说明 |
| OpenAI 官方博客 | SimpleQA / BrowseComp / HealthBench 各有单独介绍页面 | 基准介绍和方法论 |

## 项目展示素材

### 核心亮点数据

- **OpenAI 官方出品**的 LLM 评测库，背书力强
- 涵盖 **9 大主流基准**（MMLU、MATH、GPQA、DROP、MGSM、HumanEval、SimpleQA、BrowseComp、HealthBench）
- 其中 **SimpleQA、BrowseComp、HealthBench 为 OpenAI 原创基准**
- 4,400+ Stars，MIT 许可证
- **零样本、思维链**评测哲学——更贴近真实使用场景

### README 中的评测表格

README 包含一个详尽的模型对比表，覆盖 OpenAI 全系列模型（从 GPT-4 到 o3/o4-mini）在各基准上的得分，以及 Claude、Llama、Grok、Gemini 等竞品数据。这是该仓库最具传播力的素材。

### 代码结构（极简设计）

```
simple-evals/
├── simple_evals.py          # 主运行入口
├── common.py                # 公共工具
├── types.py                 # 类型定义
├── sampler/                 # 模型采样器（OpenAI / Anthropic）
├── mmlu_eval.py             # MMLU 评测
├── math_eval.py             # MATH 评测
├── gpqa_eval.py             # GPQA 评测
├── drop_eval.py             # DROP 评测
├── mgsm_eval.py             # MGSM 评测
├── humaneval_eval.py        # HumanEval 评测
├── simpleqa_eval.py         # SimpleQA 评测
├── browsecomp_eval.py       # BrowseComp 评测
├── healthbench_eval.py      # HealthBench 评测
└── healthbench_scripts/     # HealthBench 辅助脚本
```

## 快速判断

### 一句话定位

OpenAI 官方发布的轻量 LLM 评测参考实现，核心价值在于模型评测数据的透明公布，而非评测工具本身。

### 适用场景

- 需要验证/复现 OpenAI 官方公布的模型评测分数
- 对 SimpleQA / BrowseComp / HealthBench 三个 OpenAI 原创基准感兴趣
- 需要一个极简的零样本评测参考实现

### 风险点

| 维度 | 评估 |
|------|------|
| 维护状态 | **已弃用**（2025年7月），不再更新新模型结果 |
| 代码活跃度 | 最近12周提交数为0 |
| 社区参与度 | 极低，几乎全部由 OpenAI 内部员工维护 |
| 文档质量 | 偏弱，多个 Issue 反馈使用困难 |
| 可复现性 | 存在争议（#77、#96） |
| 扩展性 | 有限，不接受新评测基准 |

### 综合评价

⭐⭐⭐ (3/5)

**价值**：该项目的核心价值不在于代码工具本身（代码量仅95KB，结构极简），而在于 OpenAI 官方背书的评测数据透明性。它是了解 OpenAI 如何评测自家模型的"参考窗口"。SimpleQA、BrowseComp、HealthBench 三个原创基准本身具有独立价值，在评测领域有一定影响力。

**局限**：已明确弃用，社区参与度极低，文档不完善，作为实际评测工具远不如 lm-evaluation-harness 等社区框架实用。更适合作为学术参考而非生产工具。
