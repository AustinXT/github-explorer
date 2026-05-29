# harvard-edge/cs249r_book 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 330,875（不含空行/注释） |
| 语言分布 | Python 42.8%, TeX 12.5%, JSON 8.6%, JavaScript 8.5%, SVG 12.4%, Sass 3.1%, TypeScript 2.7%, CSS 2.6%, Lua 1.6%, 其他 5.2% |
| 代码/注释比 | 3.1:1 |
| 文件数量 | 1,721 |
| 依赖数量 | ~14（主 requirements.txt）+ 13 核心依赖（pyproject.toml），另有 18 个依赖配置文件分布于子项目 |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 30 个月（2023-09 至 2026-03） |
| 总 commit 数 | 11,123 |
| 最近提交 | 2026-03-21 |
| 近 30 天 commit | 710 |
| 近 90 天 commit | 2,244 |
| 开发阶段 | 活跃成熟期——项目持续高频迭代，近期 commit 密度（月均 700+）远超早期，处于内容扩展与工具链完善阶段 |
| 开发模式 | 单核心主导 + 社区协作。主导者 Vijay Janapa Reddi 贡献 79.8% commit（8,872/11,123），其余为课程助教与学生贡献者。工作时间集中在工作日下午（13-17 时），周日略多，表明学术节奏驱动 |

## 演化轨迹

### 核心文件

| 变更次数 | 文件 |
|----------|------|
| 42 | book/quarto/contents/vol2/distributed_training/distributed_training.qmd |
| 39 | book/quarto/contents/vol2/inference/inference.qmd |
| 35 | README.md |
| 35 | book/quarto/contents/vol2/compute_infrastructure/compute_infrastructure.qmd |
| 33 | book/quarto/contents/vol2/performance_engineering/performance_engineering.qmd |
| 32 | book/quarto/contents/vol2/sustainable_ai/sustainable_ai.qmd |
| 31 | book/quarto/contents/vol2/introduction/introduction.qmd |
| 29 | book/quarto/contents/vol2/network_fabrics/network_fabrics.qmd |
| 29 | book/quarto/contents/vol1/introduction/introduction.qmd |
| 28 | book/quarto/contents/vol2/security_privacy/security_privacy.qmd |

核心文件以 Quarto (.qmd) 教材章节为主，Vol2（大规模 ML 系统）内容变更最密集，说明该卷正处于积极撰写阶段。

### 热点目录

| 变更次数 | 目录 |
|----------|------|
| 880 | book/quarto |
| 267 | slides/vol1 |
| 239 | slides/vol2 |
| 143 | labs/vol2 |
| 128 | labs/vol1 |
| 127 | .github/workflows |
| 64 | mlsysim/docs |
| 53 | labs/plans |
| 52 | mlsysim/core |
| 52 | interviews/cloud |

教材内容（book/quarto）是绝对热点，配套的课件（slides）和实验（labs）紧随其后，CI/CD 工作流也有大量迭代。

### Commit 类型分布（最近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 功能/新增 (feat/add) | 49 | 24.5% |
| 修复 (fix/bug) | 59 | 29.5% |
| 重构 (refactor) | 12 | 6.0% |
| 文档 (doc) | 11 | 5.5% |
| 测试 (test) | 0 | 0% |
| 其他 | 69 | 34.5% |

修复与功能新增占主体，反映项目处于快速迭代期。无测试类 commit 表明测试工作可能内嵌于功能开发中，或尚未形成独立测试流程。

### 版本发布

共 23 个标签，近期发布集中在 TinyTorch 子项目：

| 版本 | 日期 | 说明 |
|------|------|------|
| tinytorch-v0.1.9 | 2026-02-18 | Computed Values, VS Code Extension & Progressive Disclosure |
| tinytorch-v0.1.8 | 2026-02-08 | Content updates and improvements |
| tinytorch-v0.1.7 | 2026-01-29 | Export Reliability Fix |
| tinytorch-v0.1.6 | 2026-01-27 | Windows/Git Bash Support |
| tinytorch-v0.1.5 | 2026-01-27 | Content updates and improvements |
| tinytorch-slides-v0.1.0 | 2026-01-25 | 配套课件首版 |
| book-v0.5.1 | 较早 | 教材 v0.5.x 系列 |
| book-v0.5.0 | 较早 | 教材 v0.5 |

发布节奏表明：TinyTorch（交互式教学工具）正处于密集迭代期（2 个月 10 个版本），教材主体版本更新相对稳定。

### 月度活跃趋势

项目呈现明显的加速增长趋势：
- **初创期**（2023-09 ~ 2024-01）：月均 ~250 次 commit，项目启动与基础搭建
- **波动期**（2024-02 ~ 2024-12）：月均 ~160 次，存在学期节奏波动（暑假低谷、学期高峰）
- **爆发期**（2025-01 ~ 至今）：月均 ~530 次，2025-08 达峰值 1,145 次，2026-01 达 1,030 次

## 项目画像卡片

```
┌─────────────────────────────────────────────────┐
│  harvard-edge/cs249r_book                       │
│  "Machine Learning Systems" 开源教材            │
├─────────────────────────────────────────────────┤
│  类型：教育/教材    许可证：MIT                   │
│  主语言：Python 42.8% + TeX 12.5%              │
│  规模：330K 行代码 / 1,721 文件                  │
│  年龄：30 个月      Commits：11,123              │
│  活跃度：近 30 天 710 commits（极高）             │
│  贡献者模式：学术主导（单教授 80% + 学生社区）     │
│  发布状态：教材 v0.5 + TinyTorch v0.1.9          │
│  开发阶段：活跃成熟期（加速扩展中）               │
├─────────────────────────────────────────────────┤
│  特征标签：                                      │
│  #教材 #哈佛 #TinyML #ML系统 #Quarto            │
│  #交互式学习 #开源教育 #高活跃度                  │
└─────────────────────────────────────────────────┘
```
