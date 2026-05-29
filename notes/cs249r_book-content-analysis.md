## 动机与定位
- 要解决的问题: AI/ML 行业"重使用、轻工程"——人人会调用 `model.fit()`，但极少人理解底层系统如何将算法映射到硅片、如何在万卡集群上协调训练、如何在毫瓦级设备上实时推理。这不是知识缺失，而是整个"AI 工程"学科的缺失。
- 为什么现有方案不够: (1) Pete Warden 的《TinyML》聚焦嵌入式推理但缺乏系统性架构视角；(2) openmlsys 是中文 ML 系统教科书但缺少配套实践平台；(3) Karpathy 的 micrograd / Cornell 的 MiniTorch 只覆盖 autograd，不涉及优化、量化、分布式和硬件部署。现有方案要么只讲理论，要么只做一个小 demo，没有人做"从理论到代码到硬件到面试"的全链路闭环。
- 目标用户: (1) 高校 CS/AI 方向本科生和研究生——作为哈佛 CS249r 课程的核心教材；(2) 想转型 ML 系统工程师的从业者——通过 Interview Playbook 和 TinyTorch 补齐系统思维；(3) 全球教育者——通过 Instructor Hub 可直接采用两学期课程大纲。

## 作者视角
### 问题发现
Vijay Janapa Reddi 在哈佛教 CS249r 多年，观察到一个根本性矛盾："The world is rushing to build AI systems. It is not engineering them." 学生能写出 PyTorch 训练脚本，却无法解释 `loss.backward()` 背后发生了什么，更无法诊断 KV-cache 碎片化导致的推理延迟飙升。他同时担任 MLCommons 联合创始人，对行业级基准测试（MLPerf）有深刻理解，知道"不可度量则不可改进"的道理。

### 解法哲学
核心理念可以用他自己的话概括："The repository is the curriculum." 这不是一本书加几个代码示例，而是**7 个深度耦合的组件构成的教学操作系统**：

1. **教科书**（book/）提供心智模型和定量推理——"READ"
2. **Co-Labs**（labs/）用交互式 Marimo 笔记本探索权衡——"EXPLORE"
3. **TinyTorch**（tinytorch/）从零构建 ML 框架——"BUILD"
4. **硬件套件**（kits/）在真实嵌入式设备上部署——"DEPLOY"
5. **MLSys·im**（mlsysim/）用物理模型模拟你租不起的基础设施
6. **Interview Playbook**（interviews/）用 1,063 道系统设计题验证理解——"PROVE"
7. **Instructor Hub**（instructors/）为教育者提供完整的两学期课程方案

这种"READ -> BUILD -> DEPLOY -> EXPLORE -> PROVE"的循环体现了建构主义学习理论：学生不只是被动接收知识，而是通过动手构建来内化概念。

### 背景知识迁移
Reddi 将多个领域的经验融合进这个项目：
- **计算机体系结构教学法**: 教科书明确采用 Hennessy & Patterson 的双卷册模式（Vol I: 单机系统 / Vol II: 分布式系统），这是向经典计算机体系结构教科书致敬并迁移其验证过的教学结构。
- **MLCommons 基准测试经验**: TinyTorch 的第 19-20 模块直接对标 MLPerf，从个人项目升级到行业级基准测试。
- **Bloom 认知层次理论**: Interview Playbook 的 5 级掌握体系（L1-L6+）严格映射到 Bloom 分类法：回忆 -> 定义 -> 应用 -> 分析 -> 综合推导。
- **物理第一原则**: MLSys·im 使用 `pint` 单位库强制维度一致性，所有硬件常量可追溯到数据手册，这是工程模拟的金标准做法。

### 战略图景
这不仅是一个课程项目，而是一个**学科建设运动**：
- **出版路径**: MIT Press 2026 年夏季出版硬拷贝，赋予学术正当性
- **规模目标**: "Help 100,000 learners master ML Systems this year, and reach 1 million by 2030"
- **开源社区**: CC-BY-NC-ND 许可证保护内容完整性，MIT 许可证开放代码复用
- **生态系统品牌**: mlsysbook.ai（主站）+ mlsysbook.org（生态系统），形成从教材到工具到社区的完整闭环
- **国际化**: README 已有英/中/日/韩四语版本，面向全球教育市场

## 架构与设计决策
### 目录结构概览
```
cs249r_book/                          # 单仓库（monorepo）——"仓库即课程"
├── book/                             # 教科书（Quarto 构建）
│   ├── quarto/contents/vol1/         # 卷一：16 章（单机 ML 系统）
│   ├── quarto/contents/vol2/         # 卷二：16+ 章（分布式 ML 系统）
│   ├── cli/                          # Binder CLI（构建工具）
│   ├── socratiQ/                     # AI 学习伴侣（即将开源）
│   └── vscode-ext/                   # VS Code 扩展
├── tinytorch/                        # 从零构建 ML 框架
│   ├── src/ (20 模块)                # 源代码（开发者编辑）
│   ├── modules/                      # 生成的 Jupyter 笔记本（学生使用）
│   ├── tinytorch/                    # 生成的 Python 包
│   ├── milestones/ (6 个历史里程碑)   # 从 1958 感知机到 2018 MLPerf
│   ├── tito/                         # CLI 工具（23 个命令）
│   └── tests/ (600+ 测试)            # 综合测试套件
├── labs/                             # 33 个交互式 Marimo 实验室
│   ├── vol1/ (17 labs)               # 基础篇
│   └── vol2/ (16 labs)               # 规模篇
├── mlsysim/                          # ML 系统分析模拟器
│   ├── core/                         # 5 层分析引擎（物理约束求解器）
│   ├── hardware/                     # 硬件规格注册表
│   ├── models/                       # 工作负载模型（Llama, ResNet 等）
│   ├── infra/                        # 数据中心基础设施
│   └── cli/                          # Agent-ready CLI（JSON schema 输出）
├── kits/                             # 嵌入式硬件实验
│   ├── contents/arduino/             # Arduino Nicla Vision
│   ├── contents/seeed/               # Seeed XIAO ESP32S3
│   └── contents/raspi/               # Raspberry Pi
├── slides/                           # Beamer 幻灯片（26 套）
│   ├── vol1/ (17 decks)
│   └── vol2/ (9+ decks)
├── interviews/                       # 面试题库（1,063 题）
│   ├── cloud/ (296 题)
│   ├── edge/ (268 题)
│   ├── mobile/ (261 题)
│   └── tinyml/ (238 题)
├── instructors/                      # 教育者资源站
├── shared/                           # 跨组件共享资源
└── .github/workflows/ (45 个)        # CI/CD 管道
```

### 关键设计决策

**决策 1: Monorepo 而非多仓库**
- 选择: 7 个组件全部放在一个仓库
- 理由: "I designed this as a single integrated curriculum, not a collection of independent projects." 教科书引用 TinyTorch 的 API，Labs 调用 MLSys·im 的求解器，Interview 题目引用 mlsysim 的常量——跨组件引用是设计的核心而非偶然
- 代价: 仓库庞大（184K+ 行 Python、123K+ 行 Quarto、45 个 CI 工作流），贡献门槛高
- 支撑: 每个组件有独立的 CI 验证工作流，互不阻塞

**决策 2: TinyTorch 采用"src -> notebook -> package"三阶段管道**
- 工作流: `src/*.py`（Jupytext 格式）-> `modules/*.ipynb`（学生用笔记本）-> `tinytorch/*.py`（可导入包）
- 理由: 开发者在 `.py` 文件中编辑（版本控制友好），学生在笔记本中交互学习，最终框架可像真实包一样被 import
- 创新: 使用 `tito` CLI 工具管理这个三阶段流水线，提供 23 个命令覆盖模块管理、测试、构建等

**决策 3: MLSys·im 基于物理第一原则而非经验拟合**
- 5 层分析栈: Workload -> Hardware -> Infrastructure -> Systems -> Solver
- 使用 `pint` 库强制单位一致性（如 TFLOPs/second、GB/second），所有常量可追溯到数据手册
- 求解器分三级: Models（分析模型）-> Solvers（物理约束求解）-> Optimizers（设计空间搜索）
- 关键文件: `core/solver.py`（1,915 行，核心求解器）、`core/constants.py`（472 行，硬件规格）

**决策 4: Labs 采用 Marimo + WebAssembly 架构**
- 选择 Marimo 而非 Jupyter，因为 Marimo 笔记本可在浏览器中通过 WebAssembly 零安装运行
- "Design Ledger" 概念: 每个 Lab 的预测和设计决策存储在浏览器 localStorage 中，后续 Lab 读取之前的决策，形成累积式学习路径
- 每个 Lab 遵循统一结构: Briefing -> Parts A-E (含预测锁) -> Synthesis

**决策 5: Interview Playbook 采用四轨道 × 五级别矩阵**
- 四轨道: Cloud / Edge / Mobile / TinyML——按部署场景划分，物理约束完全不同
- 五级别: L1(Intern) -> L3(New Grad) -> L4(Practitioner) -> L5(Senior) -> L6+(Staff)，映射 Bloom 分类法
- 关键创新: 提供 LLM Mock Interview Prompts，可用任何 LLM 模拟 Staff 级面试官

## 创新点

1. **"仓库即课程"范式**: 这是教育技术中一个罕见的设计——不是"教材 + 配套代码"的松散耦合，而是一个深度集成的教学操作系统。书中的公式、Lab 中的交互、TinyTorch 中的代码、硬件套件中的约束，全部来自 MLSys·im 的"Single Source of Truth"。

2. **历史里程碑教学法**: TinyTorch 不仅教你构建框架，还让你用自己构建的框架重现 ML 史上的里程碑（1958 感知机 -> 1969 XOR -> 1986 反向传播 -> 1998 CNN -> 2017 Transformer -> 2018 MLPerf），将技术学习嵌入历史叙事中。

3. **MLSys·im 作为"基础设施即代码编译器"**: 将 ML 系统设计问题形式化为可求解的物理约束优化问题。支持 YAML 声明式场景定义 + CI/CD 集成 + JSON schema 验证，使其可被 AI Agent 直接调用。Exit Code 3 表示 SLA 约束违反——这是面向自动化的设计。

4. **预测-发现-解释学习循环**: Labs 要求学生先做预测（结构化输入，非自由文本），再交互探索，最后用"预测与现实之间的差距"作为学习时刻。这不是普通的交互笔记本，而是有意识地利用认知失调驱动学习。

5. **SocratiQ AI 学习伴侣**: 集成在教科书中的 AI 助手，提供实时测验、概念解释和进度追踪，有配套研究论文（arXiv:2502.00341），代表了生成式 AI 在教育中的前沿实验。

## 可复用模式

1. **Monorepo 教育生态系统模式**: 将教材、代码、实验、工具链放在一个仓库中，用 CI 验证跨组件一致性。适用于任何想构建完整课程体系的教育项目。关键是每个组件有独立的 validate 工作流，但共享常量和类型定义。

2. **"Jupytext + CLI + Package"三阶段代码管道**: `src/*.py`（Jupytext percent 格式）作为源码，自动生成笔记本和包。这比直接用 `.ipynb` 做版本控制好得多（JSON diff 不可读），同时保持了学生的笔记本交互体验。

3. **物理常量注册表模式**: `mlsysim/core/constants.py` 将所有硬件规格集中管理，每个常量标注数据手册来源，使用 `pint` 强制单位检查。任何需要量化推理的项目都可以复用这个模式。

4. **面试题库四维矩阵**: 按"部署场景 x 认知层次"组织问题，每题标注 Bloom 层次和工程范围。可推广到任何需要分层评估的教育或面试系统。

5. **Design Ledger 渐进式学习持久化**: 用浏览器 localStorage 跨 Lab 累积学生的预测和决策，后续 Lab 引用之前的数据。这是一种低成本但有效的学习连续性机制。

## 竞品交叉分析

| 维度 | cs249r_book | openmlsys (4,784 star) | Pete Warden《TinyML》| micrograd / MiniTorch |
|------|-------------|----------------------|---------------------|----------------------|
| **范围** | 全栈（Cloud -> Edge -> TinyML） | ML 系统理论 | TinyML 推理 | 仅 autograd |
| **配套代码** | TinyTorch（20 模块，43K 行）+ MLSys·im（14K 行） | 少量示例 | 示例代码 | ~200 行 |
| **硬件实践** | Arduino + Seeed + Raspberry Pi | 无 | Arduino | 无 |
| **交互实验** | 33 个 Marimo Labs | 无 | 无 | 无 |
| **模拟器** | MLSys·im（5 层物理分析） | 无 | 无 | 无 |
| **面试/评估** | 1,063 题 + Mock Interview LLM Prompts | 无 | 无 | 无 |
| **教师支持** | 两学期大纲 + 评估量规 + TA 手册 | 无 | 无 | 无 |
| **出版物** | MIT Press 2026 + IEEE 论文 | 电子书 | O'Reilly 出版 | 博客/视频 |
| **语言** | 英/中/日/韩 | 中文 | 英文 | 英文 |

**核心差异化**: cs249r_book 的护城河不是任何单个组件，而是**7 个组件之间的深度耦合**。竞品可以复制教科书，可以复制框架构建，但复制这种"常量从 mlsysim 流向教科书流向 Lab 流向面试题"的全链路一致性极其困难。

**劣势**: (1) Monorepo 复杂度高，新贡献者入门门槛大；(2) 多个组件标记为"Under Active Development"，可能给用户不完整的印象；(3) CC-BY-NC-ND 许可证限制了商业化和衍生创作的可能性。

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 架构设计 | A | 7 组件 monorepo 设计高度内聚，跨组件共享常量和类型系统；MLSys·im 的 5 层分析栈设计精巧 |
| 代码规模 | A | Python 184K+ 行、Quarto 123K+ 行、45 个 CI 工作流——体现了持续投入的专业级项目 |
| 测试覆盖 | A- | TinyTorch 600+ 测试（25K 行测试代码），但 mlsysim 和 labs 的测试相对较少 |
| 工程实践 | A | pyproject.toml 配置了 black/isort/mypy/pylint/bandit；pre-commit 钩子；Vale 文本检查 |
| 文档质量 | A+ | 每个组件有独立的 README/CONTRIBUTING；教科书本身就是文档——123K 行 Quarto 内容 |
| CI/CD | A | 45 个 GitHub Actions 工作流覆盖每个组件的验证、构建、发布；甚至有 Windows 容器和链接检查 |
| 依赖管理 | B+ | pyproject.toml 规范但可选依赖分组（dev/ai/build）可进一步细化；部分组件有独立的 requirements.txt |
| 代码风格 | A- | 统一使用 black（100 字符行宽）、isort；TinyTorch 源码使用 Jupytext percent 格式一致性好 |
| 安全性 | B+ | bandit 安全扫描配置完备；但 .env.local 策略未在仓库中显式文档化 |
| 可维护性 | B+ | monorepo 规模大（45 个 workflow），长期维护依赖核心作者的持续投入；学生贡献者流动性高 |

### 质量检查清单
- [x] 有 LICENSE 文件（CC-BY-NC-ND 4.0 + MIT）
- [x] 有 CITATION.bib（IEEE 2024）
- [x] 有 CONTRIBUTING.md（TinyTorch 有完整贡献指南）
- [x] 有 PR 模板（.github/PULL_REQUEST_TEMPLATE.md）
- [x] CI/CD 管道完备（45 个 GitHub Actions 工作流）
- [x] 代码格式化工具（black, isort）
- [x] 类型检查（mypy，strict 模式）
- [x] 安全扫描（bandit）
- [x] 文本质量检查（Vale）
- [x] pre-commit 钩子
- [x] VS Code 配置共享（.vscode/settings.json + 多个 vscode-ext）
- [x] 多格式输出（HTML 网站 + PDF + EPUB）
- [x] 多语言 README（英/中/日/韩）
- [ ] CHANGELOG 文件（未找到独立的 CHANGELOG，但 Quarto 中有 backmatter/changelog）
- [ ] 社区行为准则 CODE_OF_CONDUCT.md（未发现，社区健康度 50% 的根因之一）
- [ ] Issue 模板（PR 模板有，但 Issue 模板未发现）
