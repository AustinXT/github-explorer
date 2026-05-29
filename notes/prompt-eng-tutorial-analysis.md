# anthropics/prompt-eng-interactive-tutorial 仓库分析报告

> 分析日期：2026-03-22
> 仓库地址：https://github.com/anthropics/prompt-eng-interactive-tutorial

---

## 一、项目概览

| 属性 | 值 |
|------|-----|
| 名称 | prompt-eng-interactive-tutorial |
| 描述 | Anthropic's Interactive Prompt Engineering Tutorial |
| 主语言 | Jupyter Notebook (98.1%)，Python (1.9%) |
| 许可证 | 无（仅 AmazonBedrock 子目录含 MIT LICENSE） |
| 创建时间 | 2024-04-02 |
| 最后推送 | 2026-03-01 |
| 默认分支 | master |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 磁盘占用 | 5.6 MB |

### 核心指标

| 指标 | 数值 |
|------|------|
| Star | 33,904 |
| Fork | 3,497 |
| Watcher | 304 |
| Issue（总计） | 32 |
| Pull Request（总计） | 26 |
| Star/Fork 比 | 9.7:1 |

**定位**：这是 Anthropic 官方出品的提示工程交互式教程，以 Jupyter Notebook 为载体，面向零基础到中高级用户，系统讲解 Claude 模型的提示工程技巧。项目同时提供 Google Sheets 版本，降低使用门槛。

---

## 二、所有者分析

| 属性 | 值 |
|------|-----|
| 账号 | anthropics |
| 名称 | Anthropic |
| 类型 | 组织（AI 安全公司） |
| 关注者 | 38,346 |
| 公开仓库数 | 77 |
| 注册时间 | 2020-12-19 |

Anthropic 是 Claude 系列大语言模型的开发商，本项目是其官方教育资源的核心组成部分。组织在 GitHub 上拥有 77 个公开仓库，涵盖 SDK、课程、评估基准等，在 AI 领域具有极高的品牌影响力。

---

## 三、项目结构与内容分析

### 3.1 目录结构

```
├── README.md                      # 课程总览与目录
├── .gitignore
├── Anthropic 1P/                  # Anthropic 官方 API 版本（13 个 notebook + hints.py）
│   ├── 00_Tutorial_How-To.ipynb
│   ├── 01_Basic_Prompt_Structure.ipynb
│   ├── 02_Being_Clear_and_Direct.ipynb
│   ├── 03_Assigning_Roles_Role_Prompting.ipynb
│   ├── 04_Separating_Data_and_Instructions.ipynb
│   ├── 05_Formatting_Output_and_Speaking_for_Claude.ipynb
│   ├── 06_Precognition_Thinking_Step_by_Step.ipynb
│   ├── 07_Using_Examples_Few-Shot_Prompting.ipynb
│   ├── 08_Avoiding_Hallucinations.ipynb
│   ├── 09_Complex_Prompts_from_Scratch.ipynb
│   ├── 10.1_Appendix_Chaining Prompts.ipynb
│   ├── 10.2_Appendix_Tool Use.ipynb
│   ├── 10.3_Appendix_Search & Retrieval.ipynb
│   └── hints.py
└── AmazonBedrock/                 # Amazon Bedrock 适配版本
    ├── anthropic/                 # 使用 anthropic SDK（14 个 notebook）
    ├── boto3/                     # 使用 boto3 SDK（14 个 notebook）
    ├── cloudformation/            # AWS CloudFormation 部署模板
    ├── utils/                     # 辅助工具（hints.py 等）
    ├── requirements.txt
    ├── README.md
    ├── CONTRIBUTING.md
    └── LICENSE (MIT)
```

### 3.2 代码统计

| 类型 | 文件数 | 代码行 | 注释行 | 空行 |
|------|--------|--------|--------|------|
| Jupyter Notebook | 41 | 1,125 | 610 | 388 |
| Python | 3 | 452 | 0 | 40 |
| Markdown | 3 | 0 | 111 | 63 |
| YAML | 1 | 61 | 0 | 6 |
| **合计** | **49** | **2,763** | **1,336** | **885** |

Notebook 中嵌入的 Markdown 教学文本约 491 行，Python 代码约 1,632 行。项目整体代码量精简，以教学内容为核心。

### 3.3 课程体系

课程分为三个层级共 9 章 + 附录：

**初级（Chapter 1-3）**
- 基本提示结构
- 清晰直接的表达
- 角色分配（Role Prompting）

**中级（Chapter 4-7）**
- 数据与指令分离
- 输出格式化 & 代替 Claude 说话
- 预认知（逐步思考，Chain-of-Thought）
- 使用示例（Few-Shot Prompting）

**高级（Chapter 8-9）**
- 避免幻觉
- 从零构建复杂提示（行业用例：聊天机器人、法律、金融、编程）

**附录（Chapter 10）**
- 提示链（Chaining Prompts）
- 工具使用（Tool Use）
- 搜索与检索（Search & Retrieval）
- 经验性能评估（AmazonBedrock 版独有）

### 3.4 技术实现

- **模型**：默认使用 Claude 3 Haiku (`claude-3-haiku-20240307`)，temperature=0
- **SDK**：`anthropic` Python SDK，通过 Messages API 交互
- **辅助函数**：`get_completion()` 封装 API 调用，贯穿全部 notebook
- **API Key 管理**：通过 IPython `%store` 魔法命令跨 notebook 共享变量
- **依赖**（AmazonBedrock 版）：`awscli==1.32.74`, `boto3==1.34.74`, `anthropic==0.21.3`

---

## 四、开发历史与维护状况

### 4.1 提交统计

| 指标 | 值 |
|------|-----|
| 总提交数 | 9 |
| 首次提交 | 2024-04-02（initial commit） |
| 最后提交 | 2024-04-07（添加 Google Sheets 链接） |
| 活跃月份 | 仅 2024 年 4 月（9 次提交） |

### 4.2 提交作者

| 作者 | 提交数 |
|------|--------|
| Jawhny Cooke | 6 |
| Maggie Vo | 3 |

### 4.3 高频修改文件

| 修改次数 | 文件 |
|----------|------|
| 3 | README.md |
| 2 | AmazonBedrock 下 .DS_Store 相关文件 |
| 其余 | 各 notebook 文件均仅 1 次提交 |

### 4.4 维护评估

- **开发模式**：一次性发布型（burst release）。全部 9 次提交集中在 2024 年 4 月 2-7 日的 5 天内，之后主分支无新提交
- **社区健康度**：25/100（GitHub Community Profile 评分），缺少 CODE_OF_CONDUCT、CONTRIBUTING（根目录）、Issue/PR 模板
- **依赖更新**：`anthropic==0.21.3` 已严重过时（当前最新版本约 0.78.x），AmazonBedrock 版的 awscli/boto3 同样过时
- **PR 积压**：26 个 PR 中多数为社区贡献的修复和改进，大部分处于 open 状态未合并，显示维护者响应度低
- **活跃度判断**：项目处于**低维护状态**，内容发布后基本未更新，但社区仍有持续的贡献尝试

---

## 五、社区与影响力分析

### 5.1 Star 增长趋势

基于 Star 时间戳采样分析：
- 2024-04-03 至 2024-04-15：早期快速增长（发布首周即获得大量关注）
- 2024-04 至 2024-05：持续稳定增长
- 截至 2026-03-22：累计 33,904 Star

项目凭借 Anthropic 品牌效应和实用的教学内容，在发布后迅速获得大量关注，并持续保持稳定的 Star 增长。

### 5.2 Issue 讨论热点

| # | 标题 | 评论数 | 状态 |
|---|------|--------|------|
| 43 | 404 on how-to-use-system-prompts Link | 4 | open |
| 46 | How to start? | 3 | open |
| 60 | Fix incorrect response description in Chapter 4 | 2 | open |
| 16 | Unknown function: 'claudeMessages' | 2 | closed |
| 6 | XML tags missing in 04_Separating_Data | 2 | open |
| 74 | How do you start it? | 1 | open |
| 48 | Chapter 8: Hallucination example conflates techniques | 1 | open |
| 41 | LLMS.txt | 1 | open |

**Issue 特征**：
- 多数 Issue 来自初学者的使用疑问（"How to start?"）
- 少量内容错误报告（XML 标签缺失、描述不准确）
- 链接失效问题（system prompts 链接 404）
- 整体 Issue 量很少（32 个），反映项目的独立教程性质

### 5.3 Pull Request 情况

最近 PR 动态：
- 社区持续提交修复 PR（typo 修复、链接修复、依赖更新、兼容性修复）
- 2026 年仍有新 PR 提交，但合并率极低
- Dependabot 提交了 awscli 依赖升级 PR

### 5.4 Fork 生态

| Fork 仓库 | Star | 最后更新 |
|-----------|------|----------|
| InflixOP/prompt-eng-interactive-tutorial | 6 | 2025-10 |
| jawhnycooke/prompt-eng-interactive-tutorial | 4 | 2026-03 |
| kevin801221/prompt-eng-interactive-tutorial | 2 | 2025-04 |
| qingshanyuluo/prompt-eng-interactive-tutorial-cn | 2 | 2025-10 |

3,497 个 Fork 中多数为个人学习用途，少数 Fork 进行了翻译或改编（如中文版）。衍生项目 `ivanfioravanti/prompt-eng-ollama-interactive-tutorial`（267 Star）将教程适配到 Ollama 本地模型。

---

## 六、竞品与生态位分析

### 6.1 提示工程领域竞品

| 仓库 | Star | 定位 |
|------|------|------|
| dair-ai/Prompt-Engineering-Guide | 72,043 | 综合性提示工程指南（多模型） |
| **anthropics/prompt-eng-interactive-tutorial** | **33,904** | **Claude 专属交互式教程** |
| brexhq/prompt-engineering | 9,507 | LLM 使用技巧集（通用） |
| davidkimai/Context-Engineering | 8,583 | 上下文工程手册 |
| BoundaryML/baml | 7,813 | 提示工程框架（工具） |
| NirDiamant/Prompt_Engineering | 7,292 | 提示工程技术实现集 |
| microsoft/promptbase | 5,742 | 微软提示工程资源 |

### 6.2 竞争优势

1. **官方权威性**：Anthropic 官方出品，对 Claude 模型特性有最准确的理解
2. **交互式体验**：Jupyter Notebook 允许用户即时实验，区别于纯文档类教程
3. **体系化设计**：从基础到高级渐进式课程设计，包含练习和答案
4. **双平台支持**：同时支持 Anthropic API 和 Amazon Bedrock
5. **配套 Google Sheets 版本**：降低非编程用户的使用门槛

### 6.3 竞争劣势

1. **模型版本陈旧**：默认使用 Claude 3 Haiku，未更新到 Claude 3.5/4 系列
2. **依赖过时**：`anthropic==0.21.3` 严重落后
3. **缺少高级主题**：未涵盖 System Prompt、多轮对话优化、结构化输出、Computer Use 等新特性
4. **维护停滞**：内容自发布后未有实质性更新
5. **无许可证**（根目录）：可能影响企业培训场景的采用

---

## 七、知识入口与外部链接

| 资源 | URL |
|------|-----|
| 仓库主页 | https://github.com/anthropics/prompt-eng-interactive-tutorial |
| Google Sheets 版教程 | https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8 |
| 答案速查表 | https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E |
| Anthropic Console（API Key 申请） | https://console.anthropic.com/ |
| Anthropic Python SDK 文档 | https://docs.anthropic.com/claude/reference/client-sdks |
| Messages API 文档 | https://docs.anthropic.com/claude/reference/messages_post |
| 模型概览 | https://docs.anthropic.com/claude/docs/models-overview |

---

## 八、综合评价

### 8.1 项目价值

**高价值教育资源**。作为 Anthropic 官方教程，它是学习 Claude 提示工程的最权威入门材料。33,900+ Star 和 3,500+ Fork 证明了其在开发者社区中的广泛认可。课程设计科学，从基础概念到复杂应用逐步递进，每章配有练习和实验空间。

### 8.2 主要问题

1. **内容老化严重**：项目发布于 2024 年 4 月，此后几乎零更新。Claude 模型在这两年内经历了多次重大升级（Claude 3.5 Sonnet、Claude 4 系列等），教程内容与当前最佳实践存在显著差距
2. **维护缺失**：社区贡献的 PR 长期未被审查合并，Issue 回复不及时
3. **技术债务**：SDK 版本过时可能导致新用户运行代码时遇到兼容性问题

### 8.3 适用场景

- 学习提示工程的基础概念和通用方法论（仍然有效）
- 了解 Claude API 的基本使用方式
- 作为企业内部培训的参考框架（需配合最新文档更新内容）

### 8.4 不适用场景

- 需要学习 Claude 最新功能（System Prompt、Vision、Computer Use、Tool Use 新 API 等）
- 生产环境的提示工程最佳实践（SDK 版本过旧）
- 需要多模型对比的提示工程学习

### 8.5 发展趋势预测

项目大概率将保持当前的低维护状态。Anthropic 的文档和教育重心已转向官方文档站点（docs.anthropic.com）和 Anthropic Cookbook。该教程更多作为历史性的入门参考存在，其核心方法论仍具教学价值，但实操部分需要用户自行适配最新 API。

---

## 九、关键数据摘要

```
Star: 33,904 | Fork: 3,497 | Issue: 32 | PR: 26
语言: Jupyter Notebook 98% + Python 2%
总提交: 9（全部集中在 2024-04-02 至 2024-04-07）
贡献者: 2 人（Jawhny Cooke 6次, Maggie Vo 3次）
文件: 49（41 个 Notebook, 3 个 Python, 3 个 Markdown, 1 YAML, 1 TXT）
课程: 9 章 + 4 个附录，覆盖基础到高级提示工程技术
```
