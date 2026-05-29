# suitenumerique/docs 内容分析报告（Phase 3）

> 分析日期：2026-03-22 | 仓库：https://github.com/suitenumerique/docs

## 动机与定位

- **要解决的问题**：欧洲政府机构依赖 Google Docs / Notion 等美国商业平台进行日常协作文档编辑，面临数据主权丧失、供应商锁定和合规风险。法国政府需要一款自主可控的实时协作文档平台，同时满足公共部门对无障碍（Accessibility）、多语言和安全审计的严苛要求。
- **为什么现有方案不够**：（1）Google Docs / Notion 数据存储在美国，不符合欧洲 GDPR 及各国数据本地化政策；（2）Outline 定位为团队知识库（Wiki），缺乏富文本实时协作和离线编辑；（3）HedgeDoc 只支持 Markdown，不适合非技术用户；（4）现有开源方案均缺乏政府级 OIDC 认证集成和精细化的 RBAC 权限体系。
- **目标用户**：首要用户是法国、德国、荷兰等欧洲政府公务员；次要用户是关注数据主权的企业和开源社区。核心场景：跨部门协作文档编辑、政策草案实时审阅、内部知识管理。

## 作者视角

### 问题发现

DINUM（法国政府数字化部门）在推动"La Suite"（政府数字工具套件）过程中发现，协作文档是公务员最高频使用场景之一。团队从内部项目代号 "impress" 起步（代码中 DB 表名、包名均保留 `impress` 前缀），逐步演化为独立产品 "Docs"。这种"自己先用"的模式确保了需求的真实性。

### 解法哲学

Docs 的架构决策体现三个核心价值观：

1. **数据主权优先**：文档内容存储在 S3 兼容对象存储而非数据库中，支持完全自托管，MIT 许可允许任意部署。同时特意将 BlockNote XL 的 GPL 功能（如 PDF 导出）设为可选项，通过 `PUBLISH_AS_MIT=true` 构建纯 MIT 镜像。
2. **渐进式安全**：OIDC 认证 + RBAC 五级角色（Reader/Commenter/Editor/Admin/Owner）+ 文档链接三级可达性（Restricted/Authenticated/Public），加上附件恶意文件检测（`lasuite.malware_detection`）和不安全 MIME 类型黑名单。
3. **微服务可组合**：后端 Django API、前端 Next.js 应用、Y-Provider 协作服务器三个独立部署单元，通过标准 HTTP/WebSocket 通信。Helm Chart 支持 Kubernetes 原生部署。

### 背景知识迁移

DINUM 团队从政府 IT 运维中带来了独特洞察：

- **行政工作流** → 精细化权限体系：五级角色 + 团队授权 + 祖先文档权限继承（基于 Materialized Path 树结构），完美映射了政府组织的层级结构。
- **多 IdP 环境** → OIDC Resource Server：支持多个 OIDC 提供商的 Token 内省，允许不同部委使用各自的身份服务器。
- **法规合规** → 附件安全：恶意文件检测回调、不安全 MIME 类型黑名单（55+ 类型）、文档审计日志。

## 架构与设计决策

### 整体架构（三服务微服务）

```
[前端 Next.js App]  ←→  [Django REST API]  ←→  [PostgreSQL + S3]
        ↕                        ↕
[Y-Provider Server]  ←→  [Redis (Celery/Session)]
   (HocusPocus + Express)
```

**后端（Django，约 48,500 行 Python）**：
- 核心模型（`models.py`，2,031 行）：Document 使用 `django-treebeard` 的 Materialized Path 实现树状子页面结构（`MP_Node`）；文档内容不存在数据库中，而是通过 S3 对象存储按版本管理，支持版本回溯和删除。
- API 层（`viewsets.py`，2,857 行 + `serializers.py`，1,017 行）：12+ 个 ViewSet 覆盖文档 CRUD、访问控制、邀请、评论、版本、AI 代理等。
- 外部 API（`external_api/`）：OIDC Resource Server 模式，允许其他 La Suite 服务通过 Token 内省访问文档 API，实现跨服务集成。

**前端（Next.js + React，约 44,800 行 TS/TSX）**：
- Monorepo 结构（Yarn Workspaces）：主应用 `app-impress`、E2E 测试 `app-e2e`、i18n 包、ESLint 插件、Y-Provider 协作服务器。
- 功能模块化：`features/docs/` 下按关注点拆分为 `doc-editor`、`doc-export`、`doc-share`、`doc-versioning`、`doc-tree` 等 10 个子模块。
- 编辑器基于 BlockNote.js（ProseMirror + Yjs），支持自定义 Block 类型（Callout、PDF 嵌入、图片访问控制、上传加载器）。

**协作服务器（Y-Provider，Node.js + Express + HocusPocus）**：
- 使用 HocusPocus Server 封装 Yjs CRDT 协作引擎。
- `onConnect` 钩子验证用户权限：通过 Cookie 提取 session，调用 Django API 检查文档读写权限，设置 `readOnly` 模式。
- 提供格式转换 HTTP API（Markdown/HTML/DOCX → Yjs 二进制格式）。

### CRDT/Yjs 实时协作集成

- **前端**：BlockNote.js 内建 Yjs 支持，通过 HocusPocus Provider 连接到 Y-Provider 服务器。
- **后端**：使用 `pycrdt`（Python CRDT 库）在服务端操作 Yjs 文档（如 demo 数据生成）。
- **格式转换管道**：DOCX → DocSpec API → BlockNote JSON → YdocConverter → Yjs 二进制，实现 Word 文档导入。
- **WebSocket 权限**：通过 Cookie-based session 实现匿名用户和认证用户的差异化处理。
- **连接管理**：`CollaborationService` 支持强制重连（权限变更后踢出用户）和连接状态查询。

### AI 能力集成（pydantic-ai）

AI 集成是一个精心设计的代理层，而非简单的 API 包装：

- **双模式 AI**：（1）Legacy 模式——简单文本变换（纠错、改写、摘要、美化、翻译），通过 OpenAI SDK 直连；（2）BlockNote 模式——使用 `pydantic-ai` Agent + `VercelAIAdapter` 实现流式 SSE 输出，支持前端工具调用（`ExternalToolset` + `DeferredToolRequests`），AI 可以直接操作文档 Block 结构。
- **安全控制**：`AI_ALLOW_REACH_FROM` 三级策略控制谁能使用 AI 功能；独立的速率限制（用户级 3/min、文档级 5/min）；`SaveRawBodyMiddleware` 专门为 AI 代理请求保存原始 body。
- **可观测性**：集成 Langfuse 进行 LLM 调用追踪和成本监控。
- **前端代理模式**：前端通过 `fetchAPI(documents/${docId}/ai-proxy/)` 发起请求，后端作为反向代理将请求转发到 AI 服务，避免在前端暴露 API Key。

### 认证和多租户设计

- **OIDC 全栈集成**：`mozilla-django-oidc` + `django-lasuite` 封装，支持 Authorization Code Flow + PKCE、Token 内省、可配置的 ID Provider 端点。
- **多 IdP 支持**：通过 OIDC Resource Server 模式，不同的 Service Provider（如 La Suite 生态中的其他应用）可以携带自己的 Token 访问 Docs API。
- **用户调和**：独特的 `UserReconciliation` 模型支持合并重复用户账号——在多 IdP 环境中，同一公务员可能在不同 IdP 下创建了不同账号。系统支持通过邮件双方确认后自动迁移文档权限、收藏、评论等所有关联数据。
- **Feature Flags**：集成 `django-waffle` 实现功能灰度发布。
- **Session 管理**：`ForceSessionMiddleware` 为未认证用户强制创建 session，确保匿名协作场景下的 WebSocket 连接可识别。

## 创新点识别

### 1. 文档内容存储架构（S3 + 版本化）
将文档内容存储在 S3 对象存储而非数据库中，利用 S3 原生版本控制实现文档版本历史。每次保存通过 MD5 哈希比对避免无变化的重复写入。这种设计解耦了元数据（PostgreSQL）和内容（S3），使得大文档不会成为数据库瓶颈，同时免费获得版本回溯能力。

### 2. Materialized Path 树形文档结构
使用 `django-treebeard` 的 Materialized Path 实现文档层级，`steplen=7` 支持最多 3.5 万亿个同级节点。权限通过路径前缀匹配从祖先继承（`document__path=Left(OuterRef("path"), Length("document__path"))`），一次查询获取整个继承链——这比传统的递归 CTE 查询高效得多。

### 3. 软删除 + 回收站的事务性实现
`soft_delete()` 和 `restore()` 使用 `@transaction.atomic` 确保原子性，通过 `deleted_at` / `ancestors_deleted_at` 双时间戳区分"自身删除"和"祖先删除"，并带有 `TRASHBIN_CUTOFF_DAYS`（默认 30 天）的保留策略。还通过 CheckConstraint 在数据库层面强制一致性。

### 4. AI 工具调用的"硬化"机制
`_harden_messages()` 方法在检测到前端传来 `applyDocumentOperations` 工具定义时，注入一条严格的系统提示（`BLOCKNOTE_TOOL_STRICT_PROMPT`），强制 LLM 只通过工具调用修改文档。这种"提示硬化"技术在 Agent 安全领域是前沿实践。

### 5. 用户账号调和系统
针对政府多 IdP 环境下用户账号碎片化问题设计的 `UserReconciliation` 系统：支持双向邮件确认、事务性数据迁移（文档权限取最高角色、收藏去重、评论/反应归属转移），以及 CSV 批量导入。这是 B2G（Business-to-Government）场景下的独特解法。

## 竞品交叉分析

| 维度 | Docs | Notion | Google Docs | Outline | HedgeDoc |
|------|------|--------|-------------|---------|----------|
| **数据主权** | 完全自托管，MIT 许可 | 美国服务器，闭源 | Google 云，闭源 | 自托管，BSL 许可 | 自托管，AGPL |
| **实时协作** | Yjs CRDT，低延迟 | 私有协议 | OT 算法 | WebSocket | WebSocket |
| **离线编辑** | 支持（Yjs 本地状态） | 有限支持 | 需连线 | 不支持 | 不支持 |
| **认证集成** | OIDC + Resource Server + 多 IdP | SAML/SCIM | Google Workspace | SAML/OIDC | LDAP/SAML |
| **权限粒度** | 5 级角色 + 树状继承 | 页面级 | 文件级 | 页面级 | 文档级 |
| **AI 集成** | OpenAI 兼容代理 + 文档操作 | 内建 AI | 内建 Gemini | 无 | 无 |
| **格式互操作** | DOCX/ODT/PDF/Markdown | 有限导出 | Google 格式 | Markdown | Markdown |
| **政府合规** | DPGA 认证，15 部委生产使用 | 无 | 无 | 无 | 无 |
| **许可协议风险** | MIT 核心，GPL 可选功能明确标注 | N/A | N/A | BSL→Apache | AGPL |

**关键差异化**：Docs 的核心护城河不是技术（Yjs、BlockNote 是开源通用组件），而是**政府级合规认证 + 实际政府生产使用 + MIT 许可** 的组合。在技术层面，Materialized Path 权限继承和 S3 版本化存储是独特的架构选择。

## 代码质量评估

### 测试覆盖

- **后端测试**：88 个测试文件，1,004 个测试函数，覆盖文档 CRUD、权限校验、迁移兼容性、认证流程、外部 API 等。使用 `pytest` + `pytest-xdist`（并行执行，`-n 2`）+ `pytest-cov`（覆盖率报告）+ `factory_boy`（测试数据工厂）。
- **前端测试**：67 个单元/集成测试文件（Vitest），覆盖编辑器、认证、文档管理等功能模块。
- **E2E 测试**：28 个 Playwright 端到端测试文件。
- **协作服务器**：Y-Provider 使用 Vitest + vitest-mock-extended 测试。

### CI/CD 管道

`.github/workflows/impress.yml` 定义了完整的 CI 管道：
- **代码质量**：gitlint（提交消息规范）、codespell（拼写检查）、ruff format + ruff check（Python 格式化和 lint）、pylint、ESLint（前端）。
- **测试**：后端 pytest 运行于 PostgreSQL 16 + MinIO 环境；前端 Vitest 单元测试。
- **安全**：CHANGELOG 变更检查、`print()` 语句检测、fixup commit 检测。
- **部署**：Helmfile linter、Docker Hub / GHCR 镜像发布、Crowdin 翻译同步。

### 代码规范

- **Python**：使用 ruff（line-length=88）替代 black + isort + flake8，配置了 13 个 lint 规则集。自定义 import 排序（django / third-party / impress / first-party）。
- **TypeScript**：自建 `eslint-plugin-docs` 包，统一前端代码规范。
- **代码组织**：后端遵循 Django 标准分层（models / serializers / viewsets / services / tasks）；前端按功能领域（features/）组织，每个功能包含 api / components / hooks / types。

### 技术债务信号

- `models.py` 2,031 行、`viewsets.py` 2,857 行——单文件过大，已标注 `# pylint: disable=too-many-lines`。
- 历史包名 `impress` 在 DB 表名、配置模块、Docker 镜像中大量残留，与公开品牌 "Docs" 不一致（与 Issue #726 品牌命名争议相关）。
- `pyproject.toml` 中 `keywords = ["Django", "Contacts", "Templates", "RBAC"]` 包含遗留关键词（"Contacts"、"Templates"）。

## 可提取的技术价值

### 对开发者的实用价值

1. **S3 版本化文档存储模式**：可直接复用于任何需要版本历史的内容管理系统，避免在数据库中存储大文本。
2. **Materialized Path 权限继承**：通过路径前缀匹配实现 O(1) 祖先查询的权限体系，比递归 CTE 高效。
3. **pydantic-ai + VercelAIAdapter 的流式 AI 代理实现**：展示了如何用 Python 后端代理 AI 请求并支持前端工具调用回传。
4. **HocusPocus + Django 的协作权限桥接**：Y-Provider 中 `onConnect` 的权限验证模式可复用于任何 WebSocket + REST API 混合架构。
5. **OIDC Resource Server 的跨服务集成模式**：External API 的 ViewSet 继承 + Token 内省 + 动作白名单机制，是微服务认证的参考实现。

### 可学习的设计模式

- **双时间戳软删除**：`deleted_at` + `ancestors_deleted_at` 解决了树状结构中软删除的级联和恢复问题。
- **能力矩阵（Abilities）**：`get_abilities()` 返回 30+ 项布尔权限字典，前端根据能力矩阵动态控制 UI，比传统的角色硬编码灵活得多。
- **Feature Flag 驱动的 AI 功能分级**：`AI_FEATURE_ENABLED` / `AI_FEATURE_BLOCKNOTE_ENABLED` / `AI_FEATURE_LEGACY_ENABLED` 三层开关控制 AI 功能的渐进式启用。
