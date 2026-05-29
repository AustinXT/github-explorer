# supervision 网络分析报告

> 分析对象：roboflow/supervision
> 分析日期：2026-04-07

---

## 仓库基本数据

| 指标 | 数值 |
|------|------|
| Stars | **37,770** |
| Forks | 3,310 |
| Watchers | 228 |
| Open Issues | 72 |
| Open PRs | 46 |
| Closed Issues | 448 |
| License | MIT |
| 主语言 | Python (100%) |
| 磁盘占用 | ~2.99 GB |
| 创建时间 | 2022-11-28 |
| 最近推送 | 2026-04-06 |
| 默认分支 | develop |
| 官网 | https://supervision.roboflow.com |
| PyPI 月下载 | **~107 万** |

**Topics**: computer-vision, image-processing, python, yolo, instance-segmentation, object-detection, tracking, video-processing, coco, pascal-voc, deep-learning, metrics, machine-learning, pytorch, tensorflow, classification, oriented-bounding-box, low-code, hacktoberfest

---

## 作者画像

### Roboflow（组织）

| 属性 | 值 |
|------|------|
| 类型 | 公司/组织 |
| 位置 | 美国 |
| 官网 | https://roboflow.com |
| 公开仓库 | 157 |
| 关注者 | 4,633 |
| 创建时间 | 2019-07-20 |

Roboflow 是一家专注于计算机视觉开发者工具的商业公司，提供从数据标注、模型训练到部署的全链路 CV 平台。supervision 是其开源生态的核心组件之一，定位为「可复用的计算机视觉工具库」。

### Roboflow 生态矩阵

| 项目 | Stars | 定位 |
|------|-------|------|
| **roboflow/supervision** | 37,770 | CV 可视化/后处理工具库 |
| roboflow/notebooks | 9,300 | 教程笔记本集合 |
| roboflow/trackers | 3,277 | 多目标跟踪算法库 |
| autodistill/autodistill | 2,658 | 基础模型自动标注→训练监督模型 |
| roboflow/maestro | 2,665 | 多模态模型微调工具 |
| roboflow/inference | 2,248 | 推理引擎 |
| roboflow/awesome-openai-vision-api-experiments | 1,685 | OpenAI Vision API 实验 |

### 核心贡献者

| 贡献者 | 提交数 | 身份 |
|--------|--------|------|
| **SkalskiP** (Piotr Skalski) | 1,339 | Roboflow OSS Lead，makesense.ai 创始人，6,739 粉丝 |
| **onuralpszr** (Onuralp SEZER) | 847 | 高级 ML/CV 工程师，现 @ultralytics，706 粉丝 |
| **pre-commit-ci[bot]** | 571 | 自动化代码质量 |
| **LinasKo** | 400 | 核心贡献者 |
| **dependabot[bot]** | 325 | 依赖管理 |
| **capjamesg** (James) | 120 | 活跃贡献者，538 粉丝 |
| **Borda** (Jirka Borovec) | 108 | Kaggle Master，CV/ML 专家，3,867 粉丝 |
| **hardikdava** | 106 | 核心贡献者 |

SkalskiP 以 1,339 次提交占据绝对主导地位（排除 bot），是项目事实上的技术灵魂。团队约 30+ 活跃贡献者，社区参与度高。

---

## 社区热度

### 增长指标

- **37,770 Stars** — 在 CV 工具库领域属于头部级别
- **3,310 Forks** — fork/star 比约 8.8%，实用导向型项目
- **月下载量约 107 万**，日均约 3.5 万次（PyPI），2026 年初呈现稳中有升趋势
- **72 个 Open Issues + 46 个 Open PR** — 社区活跃，持续有外部贡献

### 下载趋势（2025-10 至 2026-04）

| 月份 | 日均下载（估算） | 趋势 |
|------|-----------------|------|
| 2025-10 | ~30,000 | 基线 |
| 2025-11 | ~35,000 | +17% |
| 2025-12 | ~38,000 | +9% |
| 2026-01 | ~42,000 | +11% |
| 2026-02 | ~37,000 | -12%（假期效应） |
| 2026-03 | ~38,000 | 回稳 |
| 2026-04 | ~35,000 | 稳定 |

下载量自 2025 年末至 2026 年初有明显爬升，日峰值超过 5 万次（2026-01-20），项目处于成熟增长期。

### 版本发布节奏

| 版本 | 发布日期 | 间隔 |
|------|----------|------|
| 0.25.0 | 2024-11-12 | — |
| 0.26.0 | 2025-07-16 | ~8 个月 |
| 0.26.1 | 2025-07-23 | 1 周 |
| 0.27.0 | 2025-11-16 | ~4 个月 |
| 0.27.0.post2 | 2026-03-14 | ~4 个月 |

版本迭代稳定，大版本间隔约 4-8 个月，属于健康节奏。

---

## 生态网络

### 上游依赖与集成

supervision 设计为「模型无关」的工具库，已集成：

- **Ultralytics YOLO** — 最主流的目标检测框架
- **Hugging Face Transformers** — 模型生态
- **MMDetection** — OpenMMLab 检测工具箱
- **Roboflow Inference** — 自家推理引擎
- **RF-DETR** — 新兴检测模型（直接返回 sv.Detections）

### 下游应用场景

从 Issue 和讨论中提取的主要使用场景：

1. **目标检测可视化** — Box/Mask/Label/Trace 等注解器
2. **视频分析管道** — process_video、帧处理、速度估计、停留时间分析
3. **数据集管理** — COCO/YOLO/Pascal VOC 格式互转、数据集拆分/合并
4. **区域计数** — PolygonZone、LineZone（进出计数）
5. **多目标跟踪** — ByteTrack 集成、轨迹可视化
6. **模型评估** — Confusion Matrix、mAP 计算
7. **SAHI（切片辅助推理）** — InferenceSlicer 小目标检测

### 社区入口

- **Discord 社区**：活跃（badge 显示在线）
- **GitHub Discussions**：有 "Built with Supervision" 分类
- **YouTube 频道**：Roboflow 官方频道，提供视频教程
- **Colab Notebook**：提供在线 demo
- **Hugging Face Spaces**：Gradio 演示应用

---

## 官方文档洞察

### 文档体系

- **主文档站**：https://supervision.roboflow.com（基于 MkDocs/Material）
- **How-to 指南**：检测注解、跟踪、数据集处理等
- **Cookbooks**：端到端实战教程
- **Cheatsheet**：可视化速查表（独立 Svelte 项目）
- **API Reference**：按模块组织的详细 API 文档

### 博客内容

- **Roboflow Blog** (blog.roboflow.com)：定期发布 supervision 相关教程和更新文章
- 涵盖主题：速度估计、停留时间分析、车辆跟踪、行人计数等实际场景

---

## 竞品清单

| 项目 | Stars | 定位 | 与 supervision 的关系 |
|------|-------|------|----------------------|
| **ultralytics/ultralytics** | 55,482 | YOLO 系列，检测+跟踪+分割全栈 | 上游模型库，supervision 为其后处理提供可视化 |
| **facebookresearch/detectron2** | 34,284 | Facebook 目标检测/分割平台 | 上游模型，supervision 可对接其输出 |
| **open-mmlab/mmdetection** | 32,575 | OpenMMLab 检测工具箱 | 上游模型，有 from_mmdetection 接口 |
| **HumanSignal/label-studio** | 26,938 | 多类型数据标注平台 | 竞品（标注场景），但侧重点不同 |
| **cvat-ai/cvat** | 15,567 | 计算机视觉标注工具 | 竞品（标注场景），CVAT 重交互标注 |
| **voxel51/fiftyone** | 10,546 | 数据集管理和模型评估 | 最直接竞品，都做数据集管理+可视化 |

**差异化分析**：

supervision 的核心定位是**「可复用的 CV 后处理工具」**——不做模型训练，专注检测结果的可视化、过滤、追踪、统计。与 FiftyOne（数据集管理+探索）和 Label Studio/CVAT（标注工具）有场景重叠但不完全竞争。与 Ultralytics YOLO 等模型库是互补关系。这种「模型无关 + 轻量级工具」的定位在 CV 领域几乎没有完全同类的竞品，市场空白明显。

---

## 关键 Issue 信号

### Top 10 高价值 Issue（按影响力和讨论热度）

1. **#1929 — Reimplement video utils**（14 评论）— 核心架构重构，Video API 重新设计
2. **#183 — Show Progress in time consuming tasks**（29 评论，标记 good first issue）— 长期社区需求，进度条功能
3. **#1449 — PolygonZone: estimate how much of the zone is occupied**（20 评论）— 区域占用率估算，高价值功能需求
4. **#781 — [InferenceSlicer] allow batch size inference**（21 评论）— 批量推理支持，性能优化关键
5. **#2139 — Make OpenCV an optional dependency**（4 评论，Copilot 提交）— 解耦 OpenCV 依赖，支持 contrib 变体
6. **#268 — weighted_box_fusion 替代 NMS**（10 评论）— 加权框融合，检测后处理新方案
7. **#316 — DetectionDataset 懒加载**（10 评论）— 大数据集性能优化
8. **#291 — DetectionDataset 迁移 classes 字段**（15 评论）— 核心数据结构重构
9. **#2102 — process_video 死锁修复**（1 评论）— 关键 bug 修复，视频处理稳定性
10. **#2194 — EU AI Act 合规检查**（2 评论）— 新兴需求，AI 监管合规方向

### 信号解读

- **架构演进信号**：Video API 重写、数据集懒加载、OpenCV 解耦——项目正从「快速迭代的工具集」向「工程级库」转变
- **社区需求热点**：区域分析（占用率/停留时间）、跟踪增强（ReID/DeepSort）、数据集格式互转
- **监管趋势**：EU AI Act 合规检查 Issue 出现，说明 CV 领域也开始关注 AI 安全合规

---

## 知识入口

| 入口 | URL | 状态 |
|------|-----|------|
| **DeepWiki** | https://deepwiki.com/roboflow/supervision | 可访问 |
| **Zread** | https://zread.ai/roboflow/supervision | 可访问 |
| **官方文档** | https://supervision.roboflow.com | 活跃维护 |
| **Cheatsheet** | https://roboflow.github.io/cheatsheet-supervision/ | 可访问 |
| **Colab Demo** | https://colab.research.google.com/github/roboflow/supervision/blob/main/demo.ipynb | 可用 |

---

## 项目展示素材

### README 核心图片

1. **Banner 图片**
   - `https://media.roboflow.com/open-source/supervision/rf-supervision-banner.png?updatedAt=1678995927529`
   - 顶部全宽 banner，展示项目品牌

2. **注解器演示视频**
   - `https://github.com/roboflow/supervision/assets/26109316/691e219c-0565-4403-9218-ab5644f39bce`
   - 展示各种注解器的实时效果

3. **Built with Supervision 视频**
   - `https://user-images.githubusercontent.com/26109316/207858600-ee862b22-0353-440b-ad85-caa0c4777904.mp4`
   - 社区构建案例展示

4. **教程缩略图**
   - 停留时间分析：`https://github.com/SkalskiP/SkalskiP/assets/26109316/a742823d-c158-407d-b30f-063a5d11b4e1`
   - 速度估计：`https://github.com/SkalskiP/SkalskiP/assets/26109316/61a444c8-b135-48ce-b979-2a5ab47c5a91`

### Trendshift 徽章

- Trendshift 排名 #124，有动态徽章展示项目趋势排名

---

## 快速判断

### 一句话定位
**计算机视觉领域的「瑞士军刀」——模型无关的轻量级后处理与可视化工具库，填补了检测模型输出与实际应用之间的工具链空白。**

### 核心价值判断

1. **市场定位精准**：不做模型（避免与 YOLO/Detectron 竞争），专做模型输出的后处理（可视化/过滤/跟踪/统计），在 CV 生态中占据独特的「中间层」生态位。

2. **增长强劲**：3 年多时间达到 37,770 Stars，月下载量超 100 万，在 CV 工具库领域增长速度极快。SkalskiP 的个人影响力（6,739 粉丝）和 Roboflow 的商业推广能力形成双重驱动。

3. **商业化路径清晰**：Roboflow 通过 supervision 建立生态入口，用户使用 supervision 的可视化工具后，自然过渡到 Roboflow 的数据标注和推理服务。开源→引流→商业化的路径非常顺畅。

4. **技术壁垒**：相对较低——核心功能（画框、画掩码、数据集转换）在技术上是确定性的。但先发优势 + 丰富的注解器生态 + 模型集成矩阵构建了实用壁垒。

5. **风险点**：
   - 核心贡献者高度集中（SkalskiP 占绝对主导）
   - OpenCV 依赖耦合问题（#2139 仍在讨论中）
   - 版本号仍在 0.x，API 稳定性需关注

### 推荐评级
**值得深度分析**。项目在 CV 工具链领域有明确的开创性地位，社区活跃度高，商业支持稳定，增长趋势健康。适合作为「CV 工程化」主题的深度分析对象。
