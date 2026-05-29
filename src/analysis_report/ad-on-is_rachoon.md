# Rachoon 深度分析报告

> GitHub: https://github.com/ad-on-is/rachoon

## 一句话总结
面向自由职业者的自托管发票管理平台，采用 AdonisJS + Nuxt 3 全栈 TypeScript monorepo 架构，以极简部署和聚焦发票为核心卖点。

## 值得关注的理由
- **架构设计精良**：共享领域模型（`@repo/common`）、声明式查询（BaseAppModel）、全局 HashID 中间件等模式可直接迁移到其他项目
- **极简自托管体验**：单 Docker 容器运行全栈（Caddy + Nuxt + AdonisJS + cron），一条命令部署
- **多租户架构就绪**：子域名/Header/参数三通道组织识别，为 SaaS 化预留了基础设施

## 项目展示

![Dashboard](https://raw.githubusercontent.com/ad-on-is/rachoon/main/.github/screenshots/dashboard.png)

Rachoon 仪表盘界面

![创建发票](https://raw.githubusercontent.com/ad-on-is/rachoon/main/.github/screenshots/create-invoice.png)

发票创建表单，支持实时金额计算

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/ad-on-is/rachoon |
| Star / Fork | 926 / 71 |
| 代码行数 | 30,533 行（TypeScript 主，Vue 次之） |
| 项目年龄 | 22 个月（首次提交 2024-05-08） |
| 开发阶段 | 低活跃维护期（近 90 天 3 commit） |
| 贡献模式 | 单人主导（Adis Durakovic 92% commits） |
| 热度定位 | 小众精品（926 stars，80% 来自单次爆发事件） |
| 质量评级 | 架构[A-] 代码[B+] 文档[B] 测试[D] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Adis Durakovic，维也纳 DYNAMIC 公司全栈开发者，技术栈覆盖 Node.js / Flutter / Go。此前在 AdonisJS 生态有知名贡献——adonis-autoswagger（194 Star），对 AdonisJS 的 IoC 容器、Lucid ORM、middleware/provider 系统非常熟练。项目名「rachoon」来自波斯尼亚语「račun」（发票）+ raccoon（浣熊）。

### 问题判断
高度疑似 dogfooding 项目——作为自由职业全栈开发者，开票是刚需。Invoice Ninja 等竞品功能臃肿像完整会计系统，Crater 已不活跃且 Laravel 栈对 JS 全栈开发者不友好。作者需要的只是：创建发票 → 导出 PDF → 追踪付款状态。

### 解法哲学
- **选 AdonisJS 而非 Laravel**：TypeScript 全栈意味着前后端类型共享，`@repo/common` 包统一领域模型
- **极简部署**：违反「一容器一进程」最佳实践，但换来了 `docker compose up` 一条命令启动的极低门槛
- **选择不做什么**：不做会计、不做支付、不做移动端——只聚焦发票/报价/催款

### 战略意图
代码中已预留商业化基础：`CLOUD` 环境变量区分自托管/SaaS 模式、子域名多租户（`rachoon.work`）、`premium` 模板字段。但无 LICENSE 文件、无支付集成，处于早期 MVP 阶段，更像是开源社区建设先于商业化。

## 核心价值提炼

### 创新之处

1. **全局 HashID 中间件自动编解码**（新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5）
   基于 `*Id`/`id` 命名约定自动编解码所有 ID 字段，零侵入实现 API 层 ID 混淆。开发模式直返原始 ID 便于调试。

2. **声明式查询能力模型 (BaseAppModel)**（新颖度 2/5 | 实用性 4/5 | 可迁移性 5/5）
   模型只需声明 `searchFields`/`sortFields`/`filterFields` 静态数组，自动获得排序、搜索、过滤、分页查询能力，controller 几乎无需写查询逻辑。

3. **共享领域计算模型 (Document.rebuild)**（新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5）
   `@repo/common` 中纯 TS 类封装发票金额计算（折扣→税费→净值→总额），前端实时计算 + 后端 `beforeSave` 二次校验，确保财务数据多端一致性。

4. **前端 composable-store 混合架构**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）
   `_base.ts` 定义通用 CRUD store，`useDocument`/`useClient` 继承后快速获得完整的表单和列表管理能力。

5. **三通道多租户识别**（新颖度 2/5 | 实用性 5/5 | 可迁移性 5/5）
   子域名/Header/参数三通道优雅降级，非 CLOUD 模式自动回退单组织。

### 可复用的模式与技巧

- **BaseAppModel 声明式查询**：静态属性声明 + scope 自动生成 — 适用任何 CRUD 后端
- **HashIdParser 全局中间件**：命名约定驱动的零侵入 ID 混淆 — 适用任何 REST API
- **共享领域模型前后端一致性**：纯 TS 类前后端共用，前端实时 + 后端校验 — 适用多端数据一致性需求
- **单容器全栈 entrypoint**：Dockerfile + entrypoint.sh 多进程 — 适用简单自托管应用
- **Nunjucks + Gotenberg 文档生成**：HTML 模板 + 微服务转 PDF + PDFium 预览 — 适用 PDF 导出场景

### 关键设计决策

1. **Monorepo 共享领域模型**：确保发票金额计算前后端一致，避免 REST API 前后逻辑不一致
2. **单容器全栈部署**：降低自托管门槛，牺牲了独立扩展能力
3. **Gotenberg 而非 Puppeteer**：独立微服务更适合 Docker 化，但引入了额外容器依赖（Issue #45）

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Rachoon | Invoice Ninja | Crater | Akaunting |
|------|---------|---------------|--------|-----------|
| 技术栈 | TS 全栈 (AdonisJS+Nuxt) | Laravel+Flutter | Laravel+Vue 2 | Laravel |
| 功能范围 | 发票/报价/催款 | 全功能（发票+支付+会计+库存） | 发票+费用 | 完整会计 |
| 部署复杂度 | 极低（单容器） | 中等 | 中等 | 中等 |
| 支付集成 | 无 | Stripe/PayPal/等 | 有限 | 有限 |
| 多租户 | 内建 | 内建 | 无 | 内建 |
| 活跃度 | 低活跃 | 活跃 | 停滞 | 活跃 |
| Stars | 926 | ~8k | ~7k | ~8k |

### 差异化护城河
**「极简自托管 + 现代技术栈 + 聚焦发票」**的定位在竞品中有一定空白——Invoice Ninja 功能太全太重，Crater 已停滞，市场需要轻量级替代。但差异化主要在实现层面（TypeScript vs PHP），功能层面无明显创新。

### 竞争风险
- 缺少支付集成（Stripe/PayPal）是致命短板，这是竞品标配功能
- 单人维护模式可持续性风险高（92% commits 来自一人）
- 自然增长弱（926 Star 中 ~80% 来自单次爆发事件，之后 5 个月仅增 117）

### 生态定位
在自托管发票管理赛道的「轻量级」细分市场中寻找位置，但尚未建立足够的功能或社区护城河。

## 套利机会分析
- **信息差**: 项目架构设计质量远超其 Star 数所反映的知名度。BaseAppModel、HashID 中间件、共享领域模型等模式值得更多人学习
- **技术借鉴**: 声明式查询模型、全局 ID 混淆中间件、前后端共享领域逻辑可直接迁移到其他 TS 全栈项目
- **生态位**: AdonisJS 生态中缺少成熟的发票/支付解决方案，Rachoon 有填补空白的潜力
- **趋势判断**: 自托管需求持续增长，但竞争激烈（红海赛道），且项目当前低活跃

## 风险与不足
- **无 License**：README 提及 LICENSE 但实际缺失，法律风险不明
- **测试几乎为零**：仅 2 个占位测试文件，CONTRIBUTING 声称 70% 目标但远未达到
- **CI 形同虚设**：lint 和 test 阶段都设了 `continue-on-error: true`
- **无支付集成**：对于发票工具来说是核心功能缺失
- **错误处理薄弱**：前端 `catch` 块直接返回空对象，吞掉错误
- **单人维护风险**：92% commits 来自一人，近 90 天仅 3 commit

## 行动建议
- **如果你要用它**: 适合只需开票+导出 PDF 的自由职业者，生产使用前务必补充测试。如需支付集成或完整会计，选 Invoice Ninja 或 Akaunting
- **如果你要学它**: 重点关注 `apps/backend/app/Models/BaseAppModel.ts`（声明式查询）、`apps/backend/app/Middleware/HashIdParser.ts`（全局 ID 混淆）、`packages/common/Document.ts`（共享领域模型）、`entrypoint.sh`（单容器全栈部署）
- **如果你要 fork 它**: 补充 Stripe/PayPal 支付集成、添加实际测试覆盖、修复 CI `continue-on-error`、添加 LICENSE

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/ad-on-is/rachoon](https://deepwiki.com/ad-on-is/rachoon)（20+ 章节极高质量） |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| 在线 Demo | 无 |
