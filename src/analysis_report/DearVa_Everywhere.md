# Everywhere 深度分析报告

> GitHub: https://github.com/DearVa/Everywhere

## 一句话总结
复旦背景开发者打造的屏幕上下文感知桌面 AI 助手，通过 OS 级 Accessibility API 获取结构化 UI 元素树（非截图 OCR），让 AI 真正「看到」并「操控」桌面——在 Electron 聊天框泛滥的赛道中以原生 C# + 系统级集成独树一帜。

## 值得关注的理由
- **屏幕感知是唯一差异化**：通过 Windows FlaUI / macOS AXUIElement / Linux AT-SPI 获取结构化 UI 树，比截图 OCR token 效率高 10 倍+，且保留语义结构
- **Token-Budget-Aware 树序列化**：专为 LLM 设计的 Best-First Search 算法，智能裁剪 UI 树到 token 预算内
- **C# 在 AI 领域的少见实践**：.NET 10 + Avalonia + Semantic Kernel，证明 C# 生态在 AI 桌面应用中的可行性

## 项目展示

![Everywhere Banner](https://raw.githubusercontent.com/DearVa/Everywhere/refs/heads/main/img/banner.webp)

「Every moment, Every place. Your AI - Everywhere」——在任何应用中按快捷键即可唤起 AI 助手。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/DearVa/Everywhere |
| Star / Fork | 5,757 / 342 |
| 代码行数 | 78,186（C# 56.8%, AXAML 7.1%, I18N 资源 32.8%） |
| 项目年龄 | 10.4 个月（2025-04-23 创建） |
| 开发阶段 | 快速迭代打磨期（v0.6.7，50 个版本，~6 天/版本） |
| 贡献模式 | 单人主导 + 小团队（DearVa 72%, 10 位贡献者） |
| 热度定位 | 中等热度（5.7K stars），Product Hunt #8 日榜 |
| 质量评级 | 代码[优秀] 文档[中等] 测试[较弱] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
DearVa（Dear.Va），复旦大学背景，Sylinko Inc. 创始人/核心开发者。深度 C# / .NET / Avalonia 开发者，fork 过 Avalonia 主仓库贡献代码，另有 LiveMarkdown.Avalonia（110 stars）项目。880/1,219 commits（72%），以深夜+周末开发为主（21:00-01:00 高峰，周末提交量远超工作日），典型的激情驱动项目。

### 问题判断
桌面 AI 助手的核心瓶颈不是模型能力，而是「输入管道」——用户必须手动把屏幕信息搬运给 AI（截图、复制、粘贴）。这是一个 **UI 自动化领域的人去做 AI 产品** 的典型路径：从 accessibility API 专长出发，看到了 LLM 缺乏的「眼睛」。

### 解法哲学
不做浏览器插件或 Electron 包装器，而是直接调用操作系统级别的 UI Automation API，将屏幕上的 UI 元素树结构化为 XML 注入 LLM prompt。这是「结构化视觉」而非「截图 OCR」的路线——token 效率更高，语义保真度更好，且能反向操控 UI 元素（Click、SetText、SendKey）。

### 战略意图
BSL-1.1 许可证 + Sylinko Inc. 公司背景 + 302.AI 赞助 + Cloud 模块（OAuthCloudClient）已就位，暗示商业化路线。50 个版本的密集迭代表明这不是业余项目。长期可能提供付费同步/托管服务或企业版。

## 核心价值提炼

### 创新之处

1. **结构化屏幕感知（IVisualElement 跨平台抽象）**（新颖度 5/5 | 实用性 5/5 | 可迁移性 3/5）
   通过 OS Accessibility API 获取 UI 元素树，转换为结构化 XML 注入 prompt。三个平台实现完全不同：Windows FlaUI（UI Automation 3.0）、macOS AXUIElement（P/Invoke）、Linux AT-SPI（D-Bus）。将 30+ 种 UI 元素类型（Label/Button/TextEdit/Document/Panel/Screen 等）统一到一个接口下，是整个项目最有技术含量的抽象。

2. **Token-Budget-Aware Best-First Search 树序列化**（新颖度 5/5 | 实用性 5/5 | 可迁移性 5/5）
   `VisualTreeBuilder` 不是简单 DFS/BFS，而是用优先级队列做智能裁剪。评分公式 `FinalScore = -(TopologyScore × IntrinsicScore)`，拓扑分考虑方向和距离，类型权重区分文本（2.0x）/容器（1.5x）/交互（1.0x）/装饰（0.5x）。5 档 token 预算（1024~无限）。超出预算的分支标记 `omitted`，LLM 可通过 `get_visual_tree` 按需展开——模拟人类「先扫一眼再仔细看」的认知模式。

3. **execute_visual_actions UI 操控自动化**（新颖度 4/5 | 实用性 5/5 | 可迁移性 2/5）
   不只是「看」还能「做」——Click、SetText、SendKey、Wait 组成动作队列，LLM 直接操控桌面 UI 实现端到端任务自动化。配合细粒度权限系统（8 级 flags），高风险操作需用户确认。

4. **Subagent 模式**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）
   `EssentialPlugin.RunSubagentAsync` 允许 AI 启动子代理处理复杂多步任务，子代理共享工具但禁止递归调用（防无限递归）。桌面级 AI 代理中少见的设计。

5. **Source Generator 驱动的配置和 I18N**（新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5）
   编译时生成 Settings UI 绑定代码和强类型 i18n key，消除运行时反射和字符串魔法。12 种语言持续更新，I18N 资源变更 1,187 次。

### 可复用的模式与技巧

1. **IVisualElement 跨平台抽象**：将三种 OS accessibility API 统一到一个接口下，适用于任何跨平台 UI 感知项目
2. **Token-Budget Tree Serialization**：给定 token 预算，用优先级队列 BFS 序列化树结构。可复用于代码 AST、DOM 树、文件系统等任何「大结构送入 LLM」的场景
3. **KernelMixin 策略 + 工厂模式**：统一 5+ LLM 提供商的适配层，Schema 枚举 + 工厂方法 + 缓存
4. **BuiltIn + MCP 双轨插件系统**：原生插件提供核心能力 + MCP 插件提供可扩展性，共享 ChatPlugin 基类
5. **Watchdog 进程管理**：独立守护进程 + Named Pipe RPC 管理外部进程生命周期

### 关键设计决策

1. **结构化 XML 而非截图 OCR**：UI 元素树的 token 效率远高于图片描述，且保留了语义结构（按钮是按钮、文本是文本）。代价是依赖 Accessibility API 的完整性——某些应用的 accessibility 支持不佳会导致感知能力下降。

2. **Avalonia 而非 Electron**：原生 .NET 运行时，内存占用和启动速度优于 Electron。代价是 Avalonia 生态不如 Web 前端丰富，需要自行修补框架缺陷（Everywhere.Patches）。

3. **BSL-1.1 许可证**：允许非商业使用，限制竞争性商业使用。保护了商业化空间，但可能抑制社区贡献意愿。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Everywhere | 5ire (5.1K) | Witsy (1.9K) | PyGPT (1.7K) | MS Copilot |
|------|-----------|-------------|--------------|-------------|------------|
| 技术栈 | .NET + Avalonia | Electron | Electron | Python | 系统内置 |
| 屏幕感知 | Accessibility API 结构化 | 无 | 无 | 截图 OCR | 系统级 |
| UI 操控 | FlaUI/AX/AT-SPI | 无 | 无 | 无 | 系统级 |
| MCP 支持 | stdio + HTTP/SSE | 有 | 无 | 无 | 无 |
| 多 LLM | 8+ 提供商 | 多家 | 多家 | 多家 | GPT-4o |
| 跨平台 | Win + Mac (Linux WIP) | 全平台 | 全平台 | 全平台 | Windows |
| 许可证 | BSL-1.1 | AGPL-3.0 | Apache-2.0 | Apache-2.0 | 商业 |

### 差异化护城河
- **技术壁垒**：三套 OS accessibility API 实现 + token-aware 树序列化算法，不是可以快速复制的特性
- **原生性能优势**：.NET + Avalonia 的内存和启动性能优于 Electron 方案
- **系统级集成深度**：不只是「对话框」，而是能看到并操控桌面 UI 的 AI 代理

### 竞争风险
- BSL-1.1 许可证可能限制社区贡献意愿
- Linux 支持仍在进行中，macOS 支持刚落地（v0.6.0）
- Microsoft Copilot / Apple Intelligence 等系统级方案如果持续进化，将压缩第三方桌面 AI 助手的生存空间

### 生态定位
在桌面 AI 助手赛道中占据「系统级 AI 代理」的独特位置——介于纯聊天工具（5ire/Witsy）和系统级方案（Copilot/Apple Intelligence）之间。对于不满足于聊天框但又需要多 LLM 选择自由的开发者和高级用户，Everywhere 是目前最佳开源选择。

## 套利机会分析
- **信息差**: 高。中国开发者作品（复旦背景），Product Hunt 有曝光但中文技术社区深度分析极少。屏幕感知的技术创新角度和 C# AI 技术栈角度都适合科普
- **技术借鉴**: (1) Token-Budget Tree Serialization 算法可用于任何「大结构送入 LLM」的场景（代码 AST、DOM 树）；(2) IVisualElement 跨平台抽象是 Accessibility API 工程化的最佳参考；(3) BuiltIn + MCP 双轨插件系统设计精巧
- **生态位**: 唯一具备结构化屏幕感知的开源桌面 AI 助手
- **趋势判断**: 爆发期已过（2025-10/11 月峰值），进入稳定增长阶段（月均 200+ stars）。长期价值取决于 macOS/Linux 支持的成熟度和商业化路径的清晰化

## 风险与不足
1. **测试覆盖极弱**：仅 4 个测试文件覆盖工具类，核心 Chat/AI/Plugin 逻辑无单元测试。对于日均 3.9 次提交的项目来说，测试债务严重
2. **单人关键依赖**：DearVa 贡献 72% commits，bus factor 极低
3. **BSL-1.1 许可证**：限制商业使用，可能抑制社区贡献和企业采用
4. **Linux 支持不完整**：X11 基础支持已有，但 Wayland 和全功能覆盖仍在进行中
5. **Accessibility API 依赖**：某些应用的 accessibility 支持不佳会导致感知能力下降（尤其是游戏、自绘 UI 的应用）
6. **40GB 虚拟内存问题**（#92）虽已修复，但暗示 .NET 运行时的内存管理仍需持续关注
7. **文档仍在开发中**：官方文档站标注 "Document is in development"

## 行动建议
- **如果你要用它**: Windows 体验最完整，macOS 刚落地（v0.6.0+），Linux 仍在开发中。从 GitHub Releases 下载安装包，配置任意 LLM 提供商的 API Key 即可开始。核心体验是在任何应用中按快捷键唤出 AI 助手
- **如果你要学它**: 重点关注 `src/Everywhere.Core/Interop/IVisualElement.cs`（跨平台屏幕感知核心抽象）、`src/Everywhere.Core/Chat/VisualTreeBuilder.cs`（Token-Budget Best-First Search 树序列化算法）、`src/Everywhere.Core/AI/KernelMixinFactory.cs`（多 LLM 适配策略模式）、`src/Everywhere.Windows/Interop/`（FlaUI UI 自动化集成）
- **如果你要 fork 它**: (1) 补充核心模块的单元测试（ChatService、VisualTreeBuilder、Plugins）；(2) 完善 Linux Wayland 支持；(3) 考虑从 BSL-1.1 转为 AGPL 以扩大社区参与

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/DearVa/Everywhere](https://deepwiki.com/DearVa/Everywhere) |
| 官方网站 | [everywhere.sylinko.com](https://everywhere.sylinko.com) |
| Product Hunt | [producthunt.com/products/everywhere](https://www.producthunt.com/products/everywhere) |
| YouTube 预告 | [youtu.be/BGujYa5hbXo](https://youtu.be/BGujYa5hbXo) |
| Discord | 社区群组（链接见 README） |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| 在线 Demo | 无（桌面应用，需本地安装） |
