# Suite numérique Docs 深度分析报告

> GitHub: https://github.com/suitenumerique/docs

## 一句话总结

法德两国政府联合打造的开源协作文档平台——基于 Django + React + CRDT(Yjs) 实现实时协作编辑，已在法国 15 个部委生产环境使用，是 Notion/Google Docs 的数据主权替代品。

## 值得关注的理由

1. **政府级验证的开源协作平台**：不是又一个「Google Docs 开源克隆」，而是已在法国 15 个部委（数百万公务员）生产环境运行、德国和荷兰正在接入的真实主权方案
2. **架构设计精巧**：S3 版本化文档存储 + MD5 去重、Materialized Path 树形权限继承、双时间戳软删除、AI 提示硬化——每个设计决策都解决了协作文档的真实痛点
3. **数据主权趋势的标杆项目**：通过 Digital Public Goods 认证，MIT 许可，欧洲数字主权运动的旗舰产品，对关注数据合规的组织有直接参考价值

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/suitenumerique/docs |
| Star / Fork | 16,287 / 560 |
| 代码行数 | ~100,000 行（Python 39%, TypeScript/TSX 38%, 其余 23%） |
| 项目年龄 | 27 个月（2024-01 创建） |
| 开发阶段 | 密集开发（v4.8.2，月均 60-130 commits，每 1-2 周发版） |
| 贡献模式 | 小团队核心（AntoLC 55%，~6 人团队，96% 工作日提交） |
| 热度定位 | 大众热门（16K+ stars，政府开源文档赛道领先） |
| 质量评级 | 代码[A-] 文档[B+] 测试[A-] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

La Suite numérique 是法国数字化部门 DINUM（Direction interministérielle du numérique）旗下的开源软件套件，目标是为法国和欧洲政府机构提供「数字主权」的生产力工具替代品。Docs 是该套件的旗舰项目。核心开发者 AntoLC 领导一个约 6 人的全职团队，96% 的提交集中在欧洲工作时间，是典型的政府资助开源项目。

### 问题判断

欧洲政府面临一个紧迫的数字主权问题：**公务员的日常协作严重依赖美国科技公司的 SaaS 产品（Google Docs、Notion、Microsoft 365），敏感政府文档存储在美国服务器上**。GDPR 合规压力、Schrems II 裁决（限制向美国传输数据）和地缘政治风险使得自主可控的协作工具成为刚需。现有开源方案（Outline、HedgeDoc）要么功能不足，要么缺乏政府级的认证/权限/无障碍合规。

### 解法哲学

**「政府级合规 + 现代编辑体验」**：
- **做什么**：BlockNote.js 富文本编辑（块编辑器体验接近 Notion）、CRDT 实时多人协作、离线编辑、AI 辅助（摘要/翻译/格式化）、OIDC 多 IdP 认证、细粒度权限、PDF 导出
- **不做什么**：不做数据库/项目管理（Notion 的全家桶路线）、不做自托管市场推广（优先保障政府部署）
- **核心信条**：数据主权和无障碍合规是不可妥协的底线

### 战略意图

Docs 是法国数字主权战略的关键组件，是 La Suite numérique 套件（含邮件、视频会议、即时通讯等）的核心入口。MIT 许可 + Digital Public Goods 认证表明目标是成为欧洲政府协作的开放标准。商业化不是目标——由政府预算直接资助开发。

## 核心价值提炼

### 创新之处

| 创新点 | 新颖度 | 实用性 | 可迁移性 | 说明 |
|--------|--------|--------|----------|------|
| S3 版本化文档存储 + MD5 去重 | 4/5 | 5/5 | 5/5 | 文档内容不在数据库，S3 按版本管理，写入前 MD5 校验去重 |
| Materialized Path 树形权限继承 | 4/5 | 5/5 | 4/5 | 文档树用路径前缀匹配实现权限从祖先继承，查询效率高 |
| 双时间戳软删除 | 3/5 | 5/5 | 5/5 | `deleted_at` + `ancestors_deleted_at` 事务性标记，支持恢复整个子树 |
| AI 提示硬化 | 4/5 | 4/5 | 4/5 | `_harden_messages()` 强制 LLM 通过工具调用操作文档，防止越界行为 |
| 政府多 IdP 用户调和 | 3/5 | 4/5 | 3/5 | `UserReconciliation` 处理同一用户从不同 IdP 登录的身份合并 |

### 可复用的模式与技巧

1. **S3 版本化文档存储**：文档内容存 S3 对象存储（而非数据库 BLOB），按版本管理，写入前 MD5 校验避免重复写入。适用于任何需要版本化大对象存储的系统。

2. **Materialized Path 树形权限**：文档树结构用 materialized path 表示，权限查询通过路径前缀匹配从祖先继承。比递归查询高效，适用于层级化资源的权限管理。

3. **双时间戳软删除**：`deleted_at` 标记直接删除，`ancestors_deleted_at` 标记因祖先删除而级联软删除，恢复时可区分处理。适用于树形数据的软删除场景。

4. **AI 提示硬化（Prompt Hardening）**：在系统提示中强制 AI 只能通过工具调用操作文档，用户消息和 AI 回复都经过消毒处理。适用于任何需要限制 AI 行为边界的产品。

5. **HocusPocus + Yjs 协作服务器**：独立的 Y-Provider 服务处理 CRDT 同步，通过 webhook 回调 Django 后端做权限检查和持久化。适用于需要实时协作的 Web 应用。

### 关键设计决策

1. **三服务微服务架构**：Django API + Next.js 前端 + Y-Provider 协作服务器分离部署。Trade-off：增加了部署复杂度，但获得了独立扩缩能力（协作服务器是 WebSocket 有状态的，需要独立扩展）。

2. **BlockNote.js 而非 ProseMirror/Slate**：选择 BlockNote 的块编辑器（类 Notion 体验）而非底层编辑器框架。Trade-off：上层封装减少了定制灵活性，但大幅降低了编辑器开发成本。

3. **S3 存储而非数据库 BLOB**：文档内容存 S3 而非 PostgreSQL。Trade-off：增加了基础设施依赖（需要 S3 兼容存储），但获得了无限扩展性和版本管理能力。

4. **Django 而非 FastAPI/Express**：选择 Django 全栈框架而非更轻量的选择。Trade-off：Django 在 AI/实时场景下不如 async 框架灵活，但其 ORM、admin、认证等企业级功能降低了政府级应用的开发成本。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Docs | Notion | Google Docs | Outline | HedgeDoc |
|------|------|--------|-------------|---------|----------|
| 开源 | MIT | 闭源 | 闭源 | BSL | AGPL |
| 数据主权 | 完全自托管 | 美国服务器 | Google 云 | 自托管 | 自托管 |
| 政府认证 | DINUM + DPG | 无 | FedRAMP | 无 | 无 |
| 实时协作 | CRDT (Yjs) | 私有协议 | 私有 OT | 无 | 基本 |
| 离线编辑 | 支持 | 部分 | 需 Chrome | 否 | 否 |
| AI 集成 | 内置（多模型） | 内置 | 内置 | 无 | 无 |
| 块编辑器 | BlockNote | 自研 | 传统富文本 | ProseMirror | Markdown |
| 无障碍 | RGAA 合规 | 部分 | 部分 | 有限 | 有限 |

### 差异化护城河

1. **政府背书 + 生产验证**：法国 15 个部委生产环境使用、Digital Public Goods 认证、法德两国政府联合推进——这不是任何开源项目能轻易复制的信任资产
2. **主权合规深度**：OIDC 多 IdP 认证、RGAA 无障碍合规、双时间戳软删除（审计需求）、AI 提示硬化——每个设计都指向政府级合规需求
3. **欧洲数字主权运动加持**：项目受益于欧洲 GDPR/Schrems II 的监管趋势，政治意愿驱动的采纳比市场驱动更可持续

### 竞争风险

- **Notion/Google 添加欧洲数据驻留**：如果大厂在欧洲设立合规数据中心，部分政府用户的迁移动力会减弱
- **Outline 追赶**：Outline 功能更成熟、社区更大，如果改为 MIT 许可并添加 CRDT 协作，会成为直接竞品
- **功能差距**：相比 Notion 的全功能套件，Docs 仅覆盖文档编辑，功能丰富度有明显差距

### 生态定位

Docs 是 **欧洲数字主权运动在协作文档领域的旗舰实现**。它不是要在消费市场与 Notion 竞争，而是为政府和受监管行业提供「必须自托管、必须开源、必须合规」的唯一可行选择。

## 套利机会分析

- **信息差**: 显著存在——16K stars 但在中文开发者社区几乎无人知晓。政府级 CRDT 协作文档平台的架构模式（S3 版本化存储、Materialized Path 权限、AI 提示硬化）对企业级应用开发有很高的参考价值
- **技术借鉴**: (1) S3 版本化文档存储 + MD5 去重是协作应用的优雅方案；(2) Materialized Path 树形权限继承适用于任何层级化资源管理；(3) AI 提示硬化模式对限制 AI 行为边界有直接参考价值；(4) HocusPocus + Yjs 协作架构是 CRDT 实时协作的参考实现
- **生态位**: 欧洲政府协作文档的事实标准，填补了「政府级开源 Google Docs 替代品」的空白
- **趋势判断**: 稳定增长。数据主权是欧洲长期政策趋势（GDPR/AI Act/Data Act），政府预算资助确保开发持续性

## 风险与不足

1. **核心开发者集中**：AntoLC 贡献 55%+（1,069 commits），单点风险明显。政府项目的人员稳定性通常好于创业公司，但仍需关注。
2. **功能丰富度差距**：与 Notion 的全功能套件相比，Docs 仅覆盖文档编辑，缺少数据库视图、看板、时间线等高级功能。
3. **品牌命名问题**：项目名 「docs」 过于通用，SEO 困难，社区正在讨论重新命名（Issue #726）。代码中仍残留旧名 「impress」。
4. **部署复杂度**：三服务架构（Django + Next.js + Y-Provider）+ S3 + PostgreSQL + Redis + Celery，自托管门槛较高。
5. **国际化有限**：虽然支持多语言，但核心用户群集中在法语区，英语文档和社区互动仍需改善。
6. **单文件过大**：核心模块 `api.py`（1000+ 行 DRF ViewSet）需要拆分。

## 行动建议

- **如果你要用它**: 当你的组织（政府、银行、医疗等受监管行业）需要自托管协作文档且 Notion/Google Docs 不满足数据合规要求时选它。部署建议使用官方 Docker Compose 配置。注意功能不及 Notion 丰富，但核心编辑 + 协作体验可用。
- **如果你要学它**: 重点关注 (1) `src/backend/core/models.py` — Materialized Path 树形文档结构和双时间戳软删除设计；(2) `src/backend/core/services/ai_services.py` — AI 提示硬化和双模式 AI 集成；(3) `src/backend/core/services/collaboration_services.py` — CRDT 协作持久化和 S3 版本管理；(4) `src/backend/core/authentication/` — 多 IdP 用户调和系统。
- **如果你要 fork 它**: (1) 添加 Notion 风格的数据库视图/看板功能扩展文档编辑之外的场景；(2) 简化部署（All-in-one Docker 镜像）；(3) 改善英语文档和国际化支持；(4) 拆分过大的单文件（api.py 等）。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/suitenumerique/docs](https://deepwiki.com/suitenumerique/docs) |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| 在线 Demo | [docs.numerique.gouv.fr](https://docs.numerique.gouv.fr) |
