# AFFiNE 深度分析报告

> GitHub: https://github.com/toeverything/AFFiNE

## 一句话总结

新加坡团队 Toeverything 打造的开源知识操作系统，通过自研 BlockSuite 编辑器框架将文档、白板和数据库"超融合"为一体，以本地优先 + CRDT 实时协作的技术路线挑战 Notion 和 Miro 的市场地位。

## 值得关注的理由

1. **开源 Notion 替代品中 Star 最高**：66.4K Stars、4,636 Forks，在 Notion 替代品赛道中领跑，已融资 $18M，是该领域最被关注的开源项目
2. **自研编辑器框架 BlockSuite 具有独立价值**：70+ 子包的 block 编辑器框架，支持文档和白板无缝切换，基于 Web Components (Lit)，架构可迁移性极高，任何需要构建富编辑器的项目都可借鉴
3. **Local-first + CRDT 技术路线代表性**：自研 y-octo（Rust 实现的 Yjs 兼容 CRDT）实现本地优先数据所有权，技术路线对数据主权意识日益增强的用户群体具有强吸引力

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/toeverything/AFFiNE |
| Star / Fork | 66,408 / 4,636 |
| 代码行数 | ~94 万行代码（TypeScript 57 万 + TSX 12 万 + Rust 3 万 + Swift 2.3 万） |
| 项目年龄 | 3.7 年（2022-07-22 首次提交） |
| 总提交数 | 11,143 |
| 开发阶段 | 成熟开发（v0.26.3 稳定版 + canary 日更，但 2025 Q3 后活跃度显著下降） |
| 贡献模式 | 公司驱动（15+ 核心开发者，均为 Toeverything 团队成员） |
| 热度定位 | GitHub 大众热门（知识管理赛道 Top 3 开源项目） |
| 许可证 | 混合许可（前端 MIT / 后端 Enterprise Edition License） |
| 质量评级 | 代码[优秀] 文档[良好] 测试[全面·7 平台 E2E] |

## 作者视角：为什么存在这个项目

### 创始人背景

Toeverything Pte. Ltd. 是一家注册在新加坡的初创公司，创立于 2020 年，由 Jiachen He（CEO）、Yifeng Wang、Yinan Long、Chi Zhang 联合创办。团队规模约 30-50 人，核心开发者包括 DarkSky (1,107 commits)、Alex Yang/Himself65 (977)、pengx17/Peng Xiao (972)、JimmFly (674)、EYHN (589)。团队在编辑器技术、CRDT 协作和 Rust 高性能计算方面有深厚积累。

### 问题判断

创始团队观察到知识管理工具的三大碎片化痛点：

1. **功能割裂**：用 Notion 写文档、Miro 画白板、Airtable 管数据，用户在多个工具间切换，知识散落
2. **数据不自由**：Notion 等主流工具将数据锁定在云端，用户无法真正拥有自己的数据
3. **不可定制**：闭源工具无法满足个性化需求，没有 VSCode 式的插件生态

核心洞察：**这些工具的底层"building blocks"高度重叠（文本、表格、画布元素），完全可以在一个统一框架中实现**。

### 解法哲学

AFFiNE 的技术路线体现三个核心原则：

1. **超融合（Hyper-merged）**：文档、白板、数据库不是独立模块，而是同一个 block 引擎的不同视图。一个 block 可以同时出现在文档和画布中，真正做到"一切皆 block"
2. **本地优先（Local-first）**：数据默认存储在本地，云同步是可选功能。通过自研 y-octo（Rust CRDT）保证离线可用和实时协作不冲突
3. **开放内核（Open core）**：编辑器框架 BlockSuite 完全 MIT 开源，后端服务采用 EE License 商业化。允许社区自由扩展编辑器，同时保留商业化空间

明确不做的：不做轻量笔记（定位全功能工作空间），不做纯云端（坚持本地优先），不做单一平台（全平台覆盖）。

### 战略意图

- **短期**：通过 Star 增长和产品迭代建立 Notion 开源替代品的品牌认知
- **中期**：BlockSuite 作为独立框架输出，形成编辑器基础设施生态
- **长期**：AI Copilot + MCP 集成，从知识管理工具进化为"知识操作系统"
- **商业化**：Pro 订阅 + Enterprise License + 自托管企业版

## 核心价值提炼

### 创新之处

1. **BlockSuite 超融合编辑器框架** — 新颖度 5/5 · 实用性 4/5 · 可迁移性 5/5
   自研的 70+ 子包 block 编辑器框架，基于 Web Components (Lit)，同一个 block 可以在文档模式和白板模式间无缝切换。不同于 Slate/ProseMirror/TipTap 等传统编辑器框架，BlockSuite 原生支持图形渲染（GFX 层），实现了文档和白板的统一。任何需要构建复杂编辑器的项目都可以直接使用或借鉴其架构。

2. **y-octo：Rust 实现的 Yjs 兼容 CRDT** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5
   用 Rust 重写 Yjs CRDT 协议，提供与 Yjs 完全兼容的 API，但性能更高、内存占用更低。通过 NAPI-RS 桥接到 Node.js，同时可编译为 WASM 用于浏览器。对任何需要 CRDT 协作能力的应用都有参考价值。

3. **@toeverything/infra 依赖注入框架** — 新颖度 3/5 · 实用性 4/5 · 可迁移性 3/5
   自研的响应式依赖注入框架，管理整个应用的状态和生命周期。灵感来自 Angular DI 和 VSCode 的 Service Container，但针对前端 local-first 应用做了定制优化。

4. **Edgeless 白板引擎** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 3/5
   基于 Canvas 的无限画布引擎，支持形状、连接器、便签、嵌入文档等元素。通过 GFX 抽象层实现高性能渲染，支持 Metal Shading Language 加速（iOS）。

5. **nbstore 统一存储抽象** — 新颖度 3/5 · 实用性 4/5 · 可迁移性 3/5
   统一的数据存储层，支持 SQLite（本地）、IndexedDB（浏览器）、PostgreSQL（云端）多后端。配合 CRDT，实现透明的本地-云端数据同步。

### 技术栈全景

| 层 | 技术 |
|------|------|
| 编辑器 | BlockSuite (Lit Web Components, 自研) |
| 前端 | React 19 + vanilla-extract |
| 桌面 | Electron 39 |
| 移动 | Capacitor 7 (iOS Swift / Android Kotlin) |
| 后端 | NestJS 11 + GraphQL (Apollo) |
| 数据库 | PostgreSQL + Prisma ORM |
| 缓存 | Redis + BullMQ |
| CRDT | y-octo (Rust, Yjs 兼容) |
| 原生加速 | Rust via NAPI-RS |
| AI | Copilot (Gemini, 可配置) + MCP |
| 监控 | OpenTelemetry |
| 部署 | Docker + Helm + GitHub Actions |

## 竞品对比

| 维度 | AFFiNE | Notion | Obsidian | AppFlowy |
|------|--------|--------|----------|----------|
| 开源 | 是（混合许可） | 否 | 否 | 是（AGPLv3） |
| 本地优先 | 是 | 否 | 是 | 是 |
| 白板 | 原生集成 | 有限 | 无（需插件） | 无 |
| 协作 | CRDT 实时协作 | 强 | Sync 插件 | 有限 |
| AI | Copilot + MCP | Notion AI (强) | 插件生态 | 有限 |
| 自托管 | 支持 | 不支持 | N/A | 支持 |
| 移动端 | iOS + Android | 全平台 | 全平台 | Flutter |
| 生态成熟度 | 中 | 极高 | 高 | 低 |
| Star 数 | 66.4K | N/A | 56K+ (非官方) | 65K+ |

## 套利机会

### 技术套利

1. **BlockSuite 框架复用**：如果你需要构建带白板功能的编辑器应用（教育、设计、项目管理），BlockSuite 是目前唯一一个原生支持文档+白板超融合的开源编辑器框架，直接使用可节省 1-2 年开发时间
2. **y-octo CRDT 引擎**：需要本地优先协作能力的应用可以直接使用 y-octo，比纯 JS 的 Yjs 性能更高
3. **自托管部署参考**：AFFiNE 的 Docker + Helm 自托管方案是 Notion-like 应用自托管的成熟参考实现

### 内容套利

4. **Obsidian 用户迁移**：AFFiNE 已实现 Obsidian vault 导入，可以面向 Obsidian 用户推广，强调白板和协作能力的增量价值
5. **企业自托管需求**：对数据主权有要求的企业（医疗、金融、政府）是 AFFiNE 自托管版本的理想用户

### 生态套利

6. **MCP 插件开发**：AFFiNE 已支持 MCP，开发 AFFiNE-aware 的 AI Agent 工具可以切入其生态
7. **BlockSuite 插件/Block 开发**：在 BlockSuite 上构建垂直领域的 block 类型（如代码执行、数据可视化）

## 风险评估

### 项目风险

1. **活跃度下降信号**：2025 Q3 后月度提交从 600+ 骤降至 50-100，可能反映团队缩减或战略调整。需要持续观察是否为季节性波动或结构性转变
2. **商业化压力**：融资 $18M 但年收入仅 $2.37K（2023 年数据），收入与估值严重不匹配，商业化路径尚不清晰
3. **双许可摩擦**：后端 EE License 可能劝退希望完全自主可控的企业用户和社区贡献者
4. **复杂度负担**：94 万行代码 + 80+ packages 的 monorepo，新贡献者入门门槛极高

### 竞争风险

5. **Notion 的护城河**：Notion 拥有 25% 市场份额、Fortune 500 70% 采用率和完善的模板生态，AFFiNE 在产品成熟度上仍有明显差距
6. **AI 竞争升级**：Notion AI 已进化为自主 Agent（Notion 3.0），AFFiNE 的 Copilot 在能力和体验上还有差距
7. **移动端体验**：Capacitor 包装的移动端在性能和体验上难以与原生应用竞争

### 技术风险

8. **自研组件维护成本**：BlockSuite、y-octo、infra 三个核心自研框架需要持续投入，对小团队是巨大负担
9. **Electron 桌面端局限**：Electron 的内存占用和启动速度问题对知识管理工具尤为敏感

## 行动建议

### 如果你是开发者

- **优先研究 BlockSuite**：它是 AFFiNE 最有价值的独立组件，文档在 https://blocksuite.io，可以直接用于自己的项目
- **学习 CRDT 实现**：y-octo 是 Yjs 的高性能 Rust 实现，源码是学习 CRDT 的优秀教材
- **关注 MCP 集成**：AFFiNE 的 MCP 支持正在快速迭代，适合尝试构建 AI Agent 工具

### 如果你是用户

- **适合场景**：需要文档+白板一体化、重视数据所有权、愿意接受尚在成熟中的产品
- **不适合场景**：需要大规模团队协作（Notion 更成熟）、需要丰富模板生态、移动端重度使用

### 如果你是投资者/分析师

- **看多因素**：Star 增长强劲、自研技术壁垒高、本地优先符合数据主权趋势
- **看空因素**：活跃度下滑、商业化困难、与 Notion 差距仍大、团队是否能持续投入存疑

## 知识入口

| 来源 | 链接 | 说明 |
|------|------|------|
| GitHub | https://github.com/toeverything/AFFiNE | 源码仓库 |
| 官网 | https://affine.pro | 产品主页 |
| 在线体验 | https://app.affine.pro | Web 应用 |
| 文档 | https://docs.affine.pro | 用户文档 |
| BlockSuite | https://blocksuite.io | 编辑器框架文档 |
| 自托管指南 | https://docs.affine.pro/self-host-affine | 自部署文档 |
| Zread.ai | https://zread.ai/toeverything/AFFiNE | AI 生成的架构分析 |
| Discord | https://affine.pro/redirect/discord | 社区交流 |
| Crunchbase | https://www.crunchbase.com/organization/affine-2627 | 融资信息 |

---

*分析日期: 2026-03-22*
*数据快照: GitHub API + 本地仓库 (canary 分支, v0.26.3)*
