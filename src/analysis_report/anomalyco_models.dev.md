# models.dev 深度分析报告

> GitHub: https://github.com/anomalyco/models.dev

## 一句话总结
AI 领域的「Can I Use」——由 SST/opencode 团队打造的开源 AI 模型数据库，用 Git + TOML 替代传统数据库，421 位贡献者众包覆盖 105 家提供商、近 4,000 个模型定义，是 opencode 生态的基础设施组件。

## 值得关注的理由
1. **独特的数据架构**：TOML-as-Database 模式——用 Git 做版本控制、TOML 做数据定义、Zod 做编译时验证、GitHub PR 做数据准入门控，~2,145 行代码管理 3,899 个模型
2. **顶级团队出品**：SST（25K Stars, YC 孵化）和 opencode（127K Stars）的创始团队，models.dev 是 opencode 的内置模型数据源，「自己用自己的产品」确保数据质量
3. **社区众包威力**：421 位贡献者 + 693 Forks，社区 PR 驱动的数据更新速度远超任何闭源竞品

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/anomalyco/models.dev |
| Star / Fork | 3,080 / 693 |
| 代码行数 | 76,541 (TOML 92%, TypeScript 5%, 其他 3%) |
| 项目年龄 | 10 个月 |
| 开发阶段 | 快速成长期（月提交量 6 个月增长 4 倍，日均 9.4 次） |
| 贡献模式 | 核心+社区驱动（421 位贡献者，双核心维护者占 45%） |
| 热度定位 | 中等热度（3K Stars，数据型项目标杆） |
| 质量评级 | 代码[良好] 文档[良好] 测试[无] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Anomaly 团队由 Jay V、Frank Wang（fwang）、Dax Raad（thdxr）创立，2021 年通过 YC 孵化了 SST（Serverless Stack，25K Stars），2025 年发布 opencode（127K Stars，开源 AI 编码代理）。团队擅长构建开源开发者基础设施——SST 已实现盈利，opencode 超 20 万月活开发者。

### 问题判断
opencode 需要知道每个 AI 提供商支持哪些模型、定价如何、能力边界在哪——但这些信息分散在数十个官方文档中，格式不一、更新不同步。现有方案（Artificial Analysis、aimodels.dev）要么闭源、要么不提供 API、要么数据不够全。团队需要一个「开源、API 可用、社区可维护」的模型数据库。

### 解法哲学
- **数据即代码**：用 TOML 文件定义模型信息，享受 Git 的版本控制、diff 审查和 PR 工作流
- **社区驱动更新**：421 位贡献者通过 PR 添加/更新模型数据，远比公司内部维护高效
- **API 优先**：`api.json` 是核心产出，网页只是数据的可视化层
- **AI SDK 对齐**：Model ID 与 Vercel AI SDK 标识符一致，降低开发者集成成本
- **极简代码**：核心管道仅 49 行（`generate.ts`），复杂度全部推向数据层

### 战略意图
models.dev 不是独立产品，而是 SST 生态的基础设施组件。opencode 直接消费其 API 获取模型信息，形成「数据→工具」闭环。通过开源获得社区数据贡献，同时巩固 opencode 在 AI 编码工具赛道的数据优势。

## 核心价值提炼

### 创新之处

1. **TOML-as-Database 模式** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5
   用 Git + TOML 文件替代传统数据库：每个模型一个 TOML 文件，Zod Schema 做编译时验证，GitHub PR 做数据准入门控，GitHub Actions 自动校验。421 位贡献者证明了这种「众包数据库」模式的可行性。

2. **Glob-Scan-Validate 管道** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   核心生成管道仅 49 行：glob 扫描 `providers/*/` → 解析 TOML → Zod 验证 → 输出 `api.json`。极简但完备。

3. **Build-time SSR（Hono/JSX）** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5
   使用 Hono 框架的 JSX 渲染在构建时生成静态 HTML，部署到 Cloudflare Workers 边缘。零客户端 JS 依赖，首屏极快。

4. **Provider Logo Fallback 机制** — 新颖度 2/5 | 实用性 4/5 | 可迁移性 4/5
   Logo 按优先级查找：SVG → PNG → 默认占位符，支持深色/浅色主题变体。

### 可复用的模式与技巧

1. **TOML + Git 的众包数据管理**：适用于任何需要社区维护的结构化数据集（API 目录、配置注册表、标准列表等）
2. **Zod Schema 驱动的数据验证**：定义一次 schema，同时用于构建时验证和运行时类型安全
3. **GitHub Actions PR 自动校验**：每个数据 PR 自动运行 schema 验证，确保数据质量
4. **SST + Cloudflare Workers 部署**：基础设施即代码，边缘部署全球低延迟

### 关键设计决策

1. **TOML 而非 JSON/YAML**：TOML 的可读性强于 JSON，格式约束强于 YAML（不易出缩进错误），但不如 JSON 的工具生态丰富
2. **静态生成而非动态查询**：所有模型数据编译为单个 `api.json`，简单但文件体积会随模型增长线性膨胀
3. **无数据库、无后端服务**：完全静态部署，零运维成本，但无法做复杂查询或实时更新
4. **Provider 粒度的数据组织**：每个提供商一个目录，每个模型一个 TOML 文件，简单直观但跨提供商的模型版本关联（如同一模型在 OpenAI/Azure/OpenRouter 上的定价差异）需要额外处理

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | models.dev | Artificial Analysis | aimodels.dev | Countless.dev | OpenRouter |
|------|-----------|-------------------|-------------|--------------|-----------|
| 定位 | 开源模型数据库 | 性能基准+排行 | 模型对比平台 | 价格对比 | API 路由+对比 |
| 开源 | MIT | 闭源 | 闭源 | 闭源 | 部分开源 |
| API | 免费 JSON | 付费 | 无 | 无 | 有 |
| 模型数 | 3,899 | ~200 | ~500 | ~300 | ~1000 |
| 提供商数 | 105 | ~20 | ~30 | ~20 | ~50 |
| 数据更新 | 社区 PR | 人工测评 | 人工 | 人工 | 自动 |
| 独立评测 | 无 | 有 | 无 | 无 | 无 |

### 差异化护城河
1. **开源 + API 免费**：唯一完全开源且提供免费 JSON API 的 AI 模型数据库
2. **社区众包速度**：421 位贡献者的数据更新速度远超闭源方案的人工维护
3. **opencode 生态绑定**：作为 127K Stars 工具的内置数据源，有稳定的消费者和质量保障
4. **AI SDK 对齐**：与 Vercel AI SDK 的 Model ID 一致，开发者零适配成本

### 竞争风险
- Artificial Analysis 在独立评测和性能基准方面更权威，如果他们开放 API，models.dev 的定价/能力数据价值会降低
- OpenRouter 自身维护的模型列表更实时（直接从 API 自动获取），数据时效性更好
- 数据准确性完全依赖社区，没有自动化交叉验证机制

### 生态定位
models.dev 在 AI 开发生态中扮演「模型注册表」角色——不做评测、不做路由，只做结构化的模型元数据聚合和分发。类比 caniuse.com 之于 Web 标准兼容性数据的地位。

## 套利机会分析
- **信息差**: 中等——3K Stars 在 AI 领域不算高，但作为 opencode（127K Stars）的数据基座，其实际影响力被低估
- **技术借鉴**: TOML-as-Database 的众包数据管理模式可直接迁移到任何社区驱动的数据项目；Glob-Scan-Validate 管道是极简数据处理管道的典范
- **生态位**: 填补了「开源+API+社区驱动」的 AI 模型数据库空白
- **趋势判断**: 月提交量持续加速增长（6 月 133 → 2 月 529），随 opencode 用户增长自然扩张。AI 模型爆发式增长使这类聚合数据库的价值持续提升

## 风险与不足
1. **无测试套件**：核心代码无单元测试，数据验证完全依赖 Zod schema
2. **数据时效性依赖社区**：模型上下线、定价变更的更新速度取决于社区 PR 速度，无自动化爬虫
3. **无数据交叉验证**：同一模型在不同提供商的数据一致性无自动校验机制
4. **api.json 体积膨胀**：近 4,000 个模型的完整 JSON 文件会持续增长，可能需要分片或增量更新
5. **`family.ts` 代码质量问题**：存在重复枚举值，需要清理
6. **品牌认知度低**：3K Stars 相对于竞品（Artificial Analysis 有独立品牌认知）曝光不足

## 行动建议
- **如果你要用它**: 直接消费 `https://models.dev/api.json` 获取模型元数据，适合构建模型选择器、定价计算器、能力对比工具。如果需要性能评测数据，补充 Artificial Analysis
- **如果你要学它**: 重点关注 `packages/core/src/schema.ts`（Zod 数据模型设计）、`packages/core/src/generate.ts`（49 行核心管道）、`providers/openai/` 目录（TOML 数据文件结构示例）、`packages/web/src/render.tsx`（Hono/JSX SSR 渲染）
- **如果你要 fork 它**: 可改进方向——(1) 添加自动化数据爬虫（从各提供商 API 拉取最新模型信息）；(2) 实现跨提供商数据交叉验证；(3) api.json 分片或增量更新；(4) 添加基本测试套件；(5) 清理 family.ts 的重复枚举

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [已收录](https://deepwiki.com/anomalyco/models.dev) |
| Zread.ai | [已收录](https://zread.ai/anomalyco/models.dev) |
| 关联论文 | 无 |
| 在线 Demo | [models.dev](https://models.dev) |
| API | [models.dev/api.json](https://models.dev/api.json) |
| 社区 Discord | [sst.dev/discord](https://sst.dev/discord) |
