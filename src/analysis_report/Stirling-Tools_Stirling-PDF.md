# Stirling-PDF 深度分析报告

> GitHub: https://github.com/Stirling-Tools/Stirling-PDF

## 一句话总结

GitHub Star 数最高的 PDF 工具（76K+），从 Docker 一键部署的个人项目成长为覆盖 50+ 工具的三端平台（Web/桌面/SaaS），正在经历从纯开源向 Open-Core 商业化的关键转型。

## 值得关注的理由

1. **Open-Core 转型教科书**：从纯 MIT 开源走向 common/core/proprietary 三模块架构，Spring Profile + classpath 检测实现开源/商业边界，是观察「开源项目如何商业化」的活案例
2. **Pipeline 自举式自动化**：50+ REST API 端点通过内部 HTTP 调用自身实现流水线编排，实现了「API = 自动化接口」的架构目标
3. **AI Agent PDF 编辑**：Python Engine 使用 pydantic-ai 构建多 Agent 系统，工具参数模型从前端 TypeScript 自动生成，实现「自然语言 → PDF 操作」的闭环

## 项目展示

![Stirling PDF Dashboard](https://raw.githubusercontent.com/Stirling-Tools/Stirling-PDF/main/images/home-light.png)

Stirling-PDF 主界面，展示 50+ PDF 工具的首页入口，涵盖合并、拆分、转换、签名、编辑、OCR 等全生命周期操作。

![自定义首页深色模式](https://raw.githubusercontent.com/Stirling-Tools/Stirling-PDF/main/images/custom-home-dark.png)

深色主题自定义首页，用户可按需配置常用工具。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/Stirling-Tools/Stirling-PDF |
| Star / Fork | 76,337 / 6,552 |
| 代码行数 | 781,760 行（Java 15.4%, TSX 13.5%, JS 13.1%, TS 7.4%） |
| 项目年龄 | 38 个月（2023-01 创建） |
| 开发阶段 | 成熟活跃期（月均 130 commits，2026 年平均 4.3 天/版本） |
| 贡献模式 | BDFL + 社区驱动（创始人 Frooodle 53%，301 位贡献者） |
| 热度定位 | S 级超级明星（GitHub PDF 类目第一） |
| 质量评级 | 代码[优秀] 文档[良好] 测试[一般] CI/CD[卓越] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Anthony Stirling（Frooodle）是英国全栈开发者，Java/Spring Boot 企业级开发背景。2023 年初以个人工具发布到 Docker Hub，社区迅速验证需求（一年内破 10K stars）。已成立 Stirling PDF Inc.，采用 Open-Core 模式商业化。

### 问题判断

PDF 处理存在三大痛点：隐私风险（商业工具要求上传文档到第三方）、工具碎片化（50+ 操作散落不同工具）、企业缺失（自托管方案缺乏 SSO/审计/工作流能力）。Stirling-PDF 填补了「自托管、全功能、可编程」的空白。

### 解法哲学

1. **组合优于自研**：不重造轮子，封装 Apache PDFBox、OCRmyPDF、LibreOffice、Ghostscript、WeasyPrint、Tesseract 等成熟工具链，Stirling-PDF 是「PDF 工具链的统一编排层」
2. **API-first**：每个 UI 操作都有对应的 REST API，Pipeline 系统通过内部 HTTP 调用自身 API 实现自举式自动化
3. **渐进式复杂度**：Docker 单命令启动即可获得完整功能，企业特性通过环境变量/许可密钥按需启用
4. **Open-Core 商业化**：核心 MIT 许可覆盖基础功能，企业特性（proprietary 目录）通过商业许可保护

### 战略意图

Frooodle 正在执行明确的 Open-Core 战略转型：v2.0 完成 React SPA 重写 + Tauri 桌面端；AI/Agent Engine（Python + pydantic-ai）探索自然语言操作 PDF；Workflow 系统对标 DocuSign 的多参与方签名工作流。

## 核心价值提炼

### 创新之处

1. **Pipeline 自举式自动化**（新颖度 4/5 | 实用性 5/5）
   PipelineProcessor 通过内部 HTTP 调用自身 REST API 编排多步操作。每个 PDF 工具是独立 API 端点，Pipeline 只是编排层，零耦合。

2. **AI Agent 工具参数自动生成**（新颖度 5/5 | 实用性 5/5）
   从前端 TypeScript 源码自动生成 Python Pydantic 模型，确保 AI Agent 生成的参数与 API 契约完全一致。OrchestratorAgent → PdfEditAgent 的意图路由实现自然语言到 PDF 操作的闭环。

3. **Type3 字体签名识别引擎**（新颖度 5/5 | 实用性 4/5）
   从零构建 Type3 字体→字形提取→签名计算→字体库匹配→自动替换的完整链路。Apache PDFBox 社区都没有提供完整解决方案。

4. **AutoJob AOP + 虚拟线程执行框架**（新颖度 3/5 | 实用性 5/5）
   @AutoJobPostMapping 注解 + AOP 切面统一 50+ 操作的异步执行、超时、重试、进度追踪、资源限流。Java 21 虚拟线程 + ResourceMonitor 水位控制。

### 可复用的模式与技巧

1. **Open-Core 模块分离**：common/core/proprietary 三模块 + Spring Profile 条件加载 + classpath 检测——适用于任何开源项目商业化
2. **API 自举自动化**：每个操作暴露为 REST API，Pipeline 通过内部 HTTP 调用编排——适用于任何工具平台
3. **外部进程信号量池**：按工具类型维护独立 ProcessExecutor + Semaphore 限流——适用于任何编排外部进程的系统
4. **AI Agent 工具参数自动生成**：TypeScript → Python Pydantic 模型自动同步——适用于 LLM Agent 集成 REST API
5. **SSRF 三级防护模型**：OFF / MEDIUM / MAX + 内网 IP 检测——适用于任何处理用户 URL 的服务

### 关键设计决策

1. **Gradle 三模块架构**：common/core/proprietary 实现清晰的开源/商业边界，proprietary 可在构建时完全排除
2. **Pipeline API 自举**：内部 HTTP 调用引入网络开销，但换来了零耦合的架构——每个操作都是独立 API
3. **Python Engine（AI）+ Java 后端**：引入 Python 运行时增加部署复杂度，但 Python AI 生态远比 Java 成熟
4. **三种 Docker 镜像策略**：ultra-lite (~200MB) / standard (~400MB) / fat (~1GB) 按需选择，平衡功能与体积

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Stirling-PDF | OCRmyPDF | PDF Arranger | PDF24 | PDFgear |
|------|-------------|----------|-------------|-------|---------|
| Star | 76K | 33K | 5.3K | N/A | N/A |
| 自托管 | ✅ Docker/桌面/SaaS | CLI only | GNOME only | ❌ | ❌ |
| REST API | 50+ 端点 | 无 | 无 | 部分 | 无 |
| 自动化 | Pipeline + Workflow | CLI 脚本 | 无 | 无 | 无 |
| AI/Agent | 实验性 | 无 | 无 | 无 | 有 |
| 企业特性 | SSO/SAML/MFA/审计 | 无 | 无 | 无 | 无 |
| 开源 | MIT + 商业 | MPL-2.0 | GPL-3.0 | 闭源 | 闭源 |

### 差异化护城河

1. **唯一的全栈自托管 PDF 平台**：从个人 Docker 到企业集群，覆盖部署形态最广
2. **API-first + Pipeline 自动化**：竞品中唯一将每个操作暴露为 REST API 并提供流水线编排
3. **AI Agent 前沿探索**：竞品中最早将 LLM Agent 集成进 PDF 工作流
4. **多形态许可隔离**：一套代码库支撑开源、桌面、企业、SaaS 四种商业模式

### 竞争风险

- **PDF24 品牌壁垒**：Windows 桌面市场有深厚用户基础，功能全面且免费
- **PDFgear 用户体验**：桌面端 UX 更精致，AI 功能已上线
- **Open-Core 争议**：社区贡献者可能对「贡献的代码是否被纳入商业版」产生顾虑
- **功能广度 vs 深度**：50+ 工具但单个工具的深度可能不如专用工具

### 生态定位

自托管 PDF 基础设施平台——不是某个专用工具的替代品，而是将所有 PDF 工具统一到可编程、可自动化、可审计的平台下。类比「PDF 领域的 n8n」。

## 套利机会分析

- **信息差**：无——已是大众共识超级明星项目
- **技术借鉴**：Open-Core 三模块分离、Pipeline API 自举、外部进程信号量池等模式可直接迁移
- **生态位**：填补了「自托管全功能 PDF 平台」的空白，在 Docker 生态和 Homelab 社区中地位稳固
- **趋势判断**：Open-Core 转型是关键变量。成功（如 GitLab）则持续领先；社区分裂则给竞品机会

## 风险与不足

1. **测试覆盖率偏低**：JaCoCo 门槛仅 13-14%，对于 76K Star 的项目来说偏低
2. **单人主导风险**：Frooodle 贡献 53%，长期可持续性依赖社区化程度
3. **Open-Core 社区争议**：部分用户因商业化转向替代品（如 Bento PDF）
4. **功能广度 vs 深度**：单个工具的深度可能不如专用工具（如 OCRmyPDF 的 OCR 质量）
5. **桌面端兼容性**：Tauri 桌面端在不同 Windows 环境下仍有兼容性挑战

## 行动建议

- **如果你要用它**：自托管 PDF 处理的首选，Docker 一行命令部署。企业场景通过商业许可获得 SSO/审计/工作流能力。注意 Open-Core 模式下部分高级功能需要许可密钥
- **如果你要学它**：重点看 `app/core/src/main/java/.../controller/api/pipeline/`（Pipeline 自举架构）、`engine/src/stirling/agents/`（AI Agent 系统）、`app/proprietary/`（Open-Core 边界划分）
- **如果你要 fork 它**：测试覆盖率提升（目标 40%+）或为单个工具（如 OCR、签名）做深度优化是最高价值方向

### 知识入口

| 资源 | 链接 |
|------|------|
| 官方文档 | https://docs.stirlingpdf.com |
| API 文档 | https://registry.scalar.com/@stirlingpdf/apis/stirling-pdf-processing-api/ |
| DeepWiki | [deepwiki.com/Stirling-Tools/Stirling-PDF](https://deepwiki.com/Stirling-Tools/Stirling-PDF) |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| 在线 Demo | `docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf` |
| Discord | [discord.gg/HYmhKj45pU](https://discord.gg/HYmhKj45pU) |
