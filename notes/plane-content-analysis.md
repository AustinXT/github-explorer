# Plane 内容分析（Phase 3 — Content Analysis）

> 仓库：makeplane/plane | 分支：preview | 分析日期：2026-04-07

---

## 1. 动机与定位

### 1.1 它解决什么问题

Plane 定位为「开源的 Jira/Linear 替代品」，核心解决项目管理工具市场中三个长期未被满足的痛点：

1. **SaaS 锁定之痛**：Jira 和 Linear 都是闭源 SaaS，企业数据、工作流和自定义能力被供应商绑架。Plane 以 AGPL-3.0 开源，允许自托管（self-hosted），用户拥有完整的数据主权。
2. **复杂度的两极分化**：Jira 过度复杂（配置一个项目可能需要数天），Linear 过度简化（缺乏企业级的多层级结构）。Plane 试图在两者之间找到平衡——比 Jira 简单一个数量级，比 Linear 功能丰富一个维度。
3. **协作体验的断裂**：传统工具将「项目管理」「文档协作」「实时编辑」割裂为独立产品。Plane 将这些能力内聚到一个平台中——Issue 管理与 Page 文档共享同一套编辑器和实时协作引擎。

### 1.2 为什么现有方案不够

| 竞品 | 核心不足 |
|------|----------|
| Jira | 过度工程化，UI/UX 陈旧，定价昂贵（Data Center 版年费可达数十万美元） |
| Linear | 闭源 SaaS，无自托管选项，API 能力受限，不支持 Pages 级文档协作 |
| Redmine | Ruby on Rails 老旧技术栈，UI 仍停留在 2010 年代，移动端体验差 |
| Taiga | 功能覆盖不全（缺 Module、Page），社区活跃度下降，近年更新缓慢 |
| OpenProject | 面向传统瀑布流项目管理，对敏捷团队的支持不够原生 |

### 1.3 目标用户

Plane 的目标用户分层清晰：

- **核心用户**：中小型技术团队（5-200 人），需要一个可自托管、功能完整的项目管理工具
- **扩展用户**：成长中的初创公司，希望从 Linear/Jira 迁出，保留数据所有权
- **企业用户**：需要合规性（GDPR、数据驻留）的大型组织，通过 Plane 的 Enterprise Edition（`apps/web/ce` vs 核心路径暗示了 CE/EE 分层）获取高级功能

---

## 2. 作者视角

### 2.1 问题发现

从代码结构和提交历史可以看出，Plane 的创始团队（印度初创公司 Makeplane Software Inc.）对项目管理工具有着一线使用经验：

- **Issue 模型极其丰富**：`apps/api/plane/db/models/issue.py`（812 行）定义了 priority、state、assignees、labels、estimate_point、start_date、target_date、sequence_id 等十余个维度，这不是理论设计能做出的——只有亲身经历过 Jira 的「字段地狱」和 Linear 的「字段匮乏」之后，才会精确地选择这些字段。
- **Three-tier workspace 结构**：`Workspace > Project > Issue` 三级模型（见 `workspace.py`、`project.py`、`issue.py`），既不像 Jira 那样有 `Epic > Story > Task > Sub-task` 四层嵌套的混乱，也不像 Linear 那样只有 `Team > Issue` 两层扁平结构。这是一个「刚刚好」的设计。
- **内置 Cycle 和 Module**：Cycle（迭代）和 Module（功能模块）作为一等公民存在（见 `cycle.py`、`module.py`），说明作者同时理解 Scrum（Cycle）和 Kanban（Module）两种工作模式。

### 2.2 解决方案哲学

Plane 的架构决策体现了鲜明的工程哲学：

1. **Monorepo All-in**：6 个 apps + 15 个 packages，用 pnpm workspace + Turborepo 统一管理。这不是渐进式重构的结果，而是一开始就决定将前后端共享类型、UI 组件、服务层全部放在一个仓库中。这意味着极高的内聚性，但也意味着贡献者的上手门槛较高。
2. **前后端类型同步**：`packages/types` 作为独立的 TypeScript 类型包，被前端（`apps/web`、`apps/space`、`apps/admin`）和后端的 Live 协作服务（`apps/live`）同时引用。这种类型即契约（types-as-contract）的模式在开源项目管理工具中是罕见的。
3. **CE/EE 分层设计**：`apps/web/ce` 目录（280 个文件）包含社区版特有的组件、hooks 和 store，而核心路径则包含完整功能。这是一种「Open Core」商业模式在代码层面的体现。

### 2.3 战略画面

Plane 的战略意图从 `docker-compose.yml` 的 10 个服务容器中清晰可见：

```
web (用户主界面) + admin (管理后台) + space (公开门户)
    ↓
api (Django REST) + live (Hocuspocus 实时协作)
    ↓
worker (Celery 异步任务) + beat-worker (定时任务) + migrator (数据库迁移)
    ↓
plane-db (PostgreSQL) + plane-redis (Valkey) + plane-mq (RabbitMQ) + plane-minio (MinIO S3)
```

这是一个面向生产部署的全栈架构——不是「MVP 先跑起来」，而是「从第一天就考虑了 10 人到 10000 人规模的可扩展性」。

---

## 3. 架构与设计决策

### 3.1 目录结构全景

```
plane/
├── apps/
│   ├── web/          # 用户主界面 (React Router v7, Vite)
│   ├── admin/        # 管理后台 (/god-mode 入口)
│   ├── space/        # 公开门户 (Issue 公开页面)
│   ├── api/          # Django REST API 后端
│   │   └── plane/
│   │       ├── db/models/    # 数据模型层
│   │       ├── api/views/    # v1 API (OpenAPI 规范)
│   │       ├── app/views/    # 内部 API
│   │       ├── space/        # Space 专用 API
│   │       ├── bgtasks/      # Celery 异步任务
│   │       ├── authentication/ # 认证系统 (OAuth + Session)
│   │       ├── license/      # 许可证管理
│   │       └── settings/     # Django 配置 (common/local/production/test)
│   ├── live/         # 实时协作服务 (Hocuspocus + Express)
│   └── proxy/        # Nginx 反向代理
├── packages/
│   ├── propel/       # 组件库 (50+ 组件，Storybook 驱动)
│   ├── ui/           # 业务组件 (集成 drag-drop、charts)
│   ├── editor/       # Tiptap 富文本编辑器 (core + ce + ee)
│   ├── services/     # API 客户端层 (axios 封装，15+ 领域服务)
│   ├── shared-state/ # MobX 状态管理 (filter store, workspace store)
│   ├── hooks/        # React Hooks
│   ├── i18n/         # 国际化 (20 种语言)
│   ├── types/        # 共享 TypeScript 类型
│   ├── constants/    # 常量定义
│   ├── decorators/   # Express 路由装饰器
│   ├── logger/       # Winston 日志
│   ├── utils/        # 工具函数
│   ├── codemods/     # 数据迁移脚本
│   ├── tailwind-config/   # Tailwind 共享配置
│   └── typescript-config/ # TypeScript 共享配置
└── turbo.json        # Turborepo 构建编排
```

### 3.2 关键设计决策

#### 决策 1：三层前端应用分离（web / admin / space）

**问题**：不同角色（团队成员、系统管理员、外部访客）需要不同的 UI，但共享同一套 API 和数据模型。

**方案**：拆分为三个独立的 React 应用：
- `apps/web`：团队成员日常使用，路由最多（40+ 路由，见 `app/routes/core.ts`）
- `apps/admin`：实例管理员（`/god-mode/` 入口），专注于用户管理、实例配置
- `apps/space`：面向外部用户的公开门户（如 Issue 反馈、客户查看进度）

**权衡**：三个应用共享 `packages/propel`、`packages/ui`、`packages/services` 等包，减少了代码重复，但增加了构建复杂度。三个独立的 Docker 镜像意味着三倍的 CI 时间。

**可迁移性**：★★★★★ — 多应用共享包的 monorepo 模式在企业级产品中极其常见，Plane 的实现是教科书级的。

#### 决策 2：Hocuspocus 实时协作架构

**问题**：Page 文档和 Issue 描述需要多人实时协作编辑，类似 Google Docs 的体验。

**方案**：独立的 `apps/live` 服务，基于 Hocuspocus（Yjs 的服务端实现）：
- `apps/live/src/hocuspocus.ts`：单例模式管理 HocusPocus 服务器
- `apps/live/src/extensions/database.ts`：将 Yjs 文档状态持久化到 PostgreSQL
- `apps/live/src/lib/auth.ts`：通过 Django Session Cookie 验证 WebSocket 连接
- `apps/live/src/controllers/collaboration.controller.ts`：WebSocket 控制器
- 支持 PDF 导出（`controllers/pdf-export.controller.ts`）

**权衡**：引入了独立的服务和 Redis 依赖，增加了运维复杂度，但获得了真正的实时协作能力（OT/CRDT）。使用二进制格式存储文档（`description_binary` 字段），空间效率高但调试困难。

**可迁移性**：★★★★☆ — Hocuspocus + Redis + PostgreSQL 的实时协作架构可直接迁移到任何需要富文本协作的场景。

#### 决策 3：装饰器驱动的路由系统

**问题**：`apps/live` 是 Express 应用，手动注册路由容易遗漏且不易维护。

**方案**：自建装饰器框架（`packages/decorators`）：
- `@Controller("/base")` 类装饰器定义基础路径
- `@Get("/path")`、`@Post("/path")` 方法装饰器注册路由
- `@Middleware(fn)` 注入中间件
- 支持 REST 和 WebSocket 双模式（通过 `registerController` 自动检测）
- 使用 `reflect-metadata` 存储元数据

```typescript
// packages/decorators/src/controller.ts — 核心路由注册逻辑
export function registerController(router, Controller, dependencies = []) {
  const instance = new Controller(...dependencies);
  const isWebsocket = Object.getOwnPropertyNames(Controller.prototype)
    .some(name => Reflect.getMetadata("method", instance, name) === "ws");
  // 自动选择 REST 或 WebSocket 注册模式
}
```

**权衡**：增加了学习曲线（需要理解 TypeScript 装饰器和 reflect-metadata），但换来了声明式的路由定义和自动依赖注入。

**可迁移性**：★★★★★ — 装饰器路由模式可直接复用于任何 Express/Fastify 项目。

#### 决策 4：多版本 API 并存策略

**问题**：API 需要持续演进，同时保持向后兼容。

**方案**：三套 API 路径并存（见 `apps/api/plane/urls.py`）：
- `/api/` → `plane.app.urls`（内部 API，Session 认证）
- `/api/public/` → `plane.space.urls`（公开 API，Space 门户用）
- `/api/v1/` → `plane.api.urls`（公开 REST API，API Key 认证，带 OpenAPI 文档）

v1 API 使用 `drf-spectacular` 自动生成 OpenAPI 规范，支持 Swagger UI。旧的 URL 模式被标记为 deprecated 但仍保留。

**可迁移性**：★★★★☆ — API 版本化是通用最佳实践，Plane 的三层分离模式值得借鉴。

#### 决策 5：PostgreSQL Advisory Lock 实现分布式序列号

**问题**：Issue 的 `sequence_id`（如 `PROJ-42`）需要在分布式环境下保持连续且无冲突。

**方案**：在 `Issue.save()` 方法中使用 PostgreSQL 的 `pg_advisory_xact_lock`：

```python
# apps/api/plane/db/models/issue.py:204-233
if self._state.adding:
    with transaction.atomic():
        lock_key = convert_uuid_to_integer(self.project.id)
        with connection.cursor() as cursor:
            cursor.execute("SELECT pg_advisory_xact_lock(%s)", [lock_key])
        last_sequence = IssueSequence.objects.filter(
            project=self.project
        ).aggregate(largest=models.Max("sequence"))["largest"]
        self.sequence_id = last_sequence + 1 if last_sequence else 1
```

**权衡**：事务级 Advisory Lock 在高并发下可能成为瓶颈（同一项目的 Issue 创建会串行化），但保证了序列号的连续性。对于大多数团队（每分钟创建 < 100 个 Issue）完全足够。

**可迁移性**：★★★★★ — Advisory Lock 模式可用于任何需要分布式序列号的场景。

#### 决策 6：MobX 响应式过滤系统

**问题**：Issue 列表需要支持多维度、嵌套、可组合的过滤条件，且过滤状态需要跨组件共享。

**方案**：基于 MobX 的分层过滤架构（`packages/shared-state`）：
- `WorkItemFilterStore`：管理所有过滤实例的 Map
- `FilterInstance`：单个过滤实例，支持表达式树
- `RichFilterStore`：高级过滤配置（group_by、order_by、layout 等）
- 使用 `computedFn` 实现高效的计算属性缓存
- 过滤表达式支持逻辑运算符（AND/OR/NOT）

**可迁移性**：★★★★☆ — MobX 响应式过滤模式可迁移到任何需要复杂过滤 UI 的应用。

---

## 4. 创新点

### 4.1 创新点矩阵

| # | 创新点 | 新颖性 | 实用性 | 可迁移性 | 总分 |
|---|--------|--------|--------|----------|------|
| 1 | 三应用分离架构（web/admin/space） | 3 | 5 | 5 | 75 |
| 2 | 装饰器驱动的 Express + WebSocket 路由 | 4 | 4 | 5 | 80 |
| 3 | Tiptap 富文本 + Hocuspocus 实时协作 | 3 | 5 | 4 | 60 |
| 4 | MobX 表达式树过滤系统 | 4 | 4 | 4 | 64 |
| 5 | PostgreSQL Advisory Lock 分布式序列号 | 4 | 5 | 5 | 100 |
| 6 | CE/EE 代码级分层（ce/ 目录模式） | 3 | 4 | 4 | 48 |
| 7 | 二进制文档格式 + HTML/JSON 多格式同步存储 | 4 | 4 | 3 | 48 |
| 8 | 类型即契约（shared types package） | 3 | 5 | 5 | 75 |
| 9 | Turborepo + pnpm catalog 统一依赖版本 | 3 | 5 | 5 | 75 |
| 10 | Celery 定时清理体系（10+ 清理任务） | 2 | 5 | 4 | 40 |

### 4.2 亮点详解

**最高分项：PostgreSQL Advisory Lock 分布式序列号（100 分）**

这是整个代码库中技术含量最高的单项设计。在 `apps/api/plane/db/models/issue.py:204-233` 中，作者没有使用常见的 UUID 或全局自增 ID，而是选择了「项目级连续序列号 + Advisory Lock」的方案。这意味着：
- 用户看到的是人类友好的 `PROJ-42`，而不是 `550e8400-e29b-41d4-a716-446655440000`
- 序列号在项目范围内严格连续（无空洞）
- 在分布式部署中，同一项目的并发 Issue 创建通过 Advisory Lock 串行化
- `convert_uuid_to_integer` 将 project UUID 转为整数作为 lock key，避免 UUID 冲突

**最具迁移价值：装饰器路由框架（80 分）**

`packages/decorators` 是一个精巧的实现——仅三个文件（`controller.ts`、`rest.ts`、`websocket.ts`），约 150 行代码，就实现了：
- 声明式路由定义
- REST 和 WebSocket 的统一注册
- 中间件注入
- 依赖注入（通过 `registerController` 的 `dependencies` 参数）

这个模式可以零修改地复制到任何 Express 项目中。

---

## 5. 可复用模式

### 5.1 Django 软删除 + 审计追踪 Mixin

**路径**：`apps/api/plane/db/mixins.py`

```
TimeAuditModel → created_at, updated_at（自动时间戳）
UserAuditModel → created_by, updated_by（当前用户追踪，通过 crum 中间件）
SoftDeleteModel → deleted_at（软删除 + 级联软删除 via Celery）
BaseModel = TimeAuditModel + UserAuditModel + SoftDeleteModel + UUID primary key
```

**复用场景**：任何需要软删除和审计追踪的 Django 项目。`soft_delete_related_objects` 通过 Celery 异步级联删除关联对象，避免同步删除的性能问题。

### 5.2 权限装饰器模式

**路径**：`apps/api/plane/app/permissions/base.py`

```python
@allow_permission([ROLE.ADMIN, ROLE.MEMBER], level="WORKSPACE")
def some_view(self, request, *args, **kwargs):
    ...
```

支持 Workspace 和 Project 两级权限，支持 `creator=True` 判断（只有创建者可以操作），支持 Workspace Admin 越权。这是一个比 Django Guardian 更轻量、比 DRF 自带权限更具体的 RBAC 实现。

### 5.3 S3 预签名 URL 上传模式

**路径**：`apps/api/plane/settings/storage.py`

完整实现了：
- `generate_presigned_post`：客户端直传 S3（避免文件经过 Django 服务器）
- `generate_presigned_url`：带 Content-Disposition 的下载链接
- MinIO 兼容模式（`USE_MINIO=1` 时自动切换）
- 文件元数据获取、复制、删除、直接上传

### 5.4 前端服务层模式

**路径**：`packages/services/src/api.service.ts` + `packages/services/src/*/`

所有前端 API 调用都继承自 `APIService` 基类，按领域拆分：
- `issue/`、`cycle/`、`module/`、`project/`、`workspace/`
- `auth/`、`file/`、`ai/`、`dashboard/`
- `developer/`（API Token、Webhook 管理）

每个领域服务独立封装，但共享同一个 axios 实例（带 Cookie 凭证）。

### 5.5 Turborepo + pnpm Catalog 版本管理

**路径**：`pnpm-workspace.yaml` 的 `catalog:` 字段 + `package.json` 的 `overrides`

```yaml
catalog:
  react: "18.3.1"
  typescript: "5.8.3"
  vite: "7.3.1"
```

所有 workspace 包通过 `catalog:` 引用统一版本，避免不同包使用不同版本的 React/TypeScript。`package.json` 中的 `overrides` 处理第三方依赖的传递性版本冲突。这是一个值得任何 monorepo 项目学习的模式。

---

## 6. 竞品交叉分析

### 6.1 功能矩阵

| 功能维度 | Plane | Linear | Jira | Redmine | Taiga |
|----------|-------|--------|------|---------|-------|
| **开源** | ✅ AGPL-3.0 | ❌ 闭源 | ❌ 闭源 | ✅ GPL | ✅ MPL-2.0 |
| **自托管** | ✅ Docker Compose | ❌ | ✅ Data Center | ✅ | ✅ |
| **Issue 管理** | ★★★★★ | ★★★★ | ★★★★★ | ★★★ | ★★★ |
| **看板视图** | ✅ | ✅ | ✅ | ❌ 需插件 | ✅ |
| **甘特图** | ✅ | ✅ | ✅ 需插件 | ❌ | ❌ |
| **Cycle/Sprint** | ✅ Cycle | ✅ Cycle | ✅ Sprint | ❌ | ✅ Sprint |
| **Module/Epic** | ✅ Module | ❌ | ✅ Epic | ❌ | ✅ Epic |
| **Page 文档** | ✅ 实时协作 | ✅ 静态 | ❌ Confluence | ❌ Wiki | ❌ |
| **实时协作编辑** | ✅ Hocuspocus | ❌ | ❌ | ❌ | ❌ |
| **公开门户** | ✅ Space | ❌ | ✅ JSM | ❌ | ❌ |
| **富文本编辑器** | ✅ Tiptap | ✅ ProseMirror | ❌ Wiki Markup | ❌ Textile | ❌ Markdown |
| **OpenAPI 文档** | ✅ v1 API | ✅ | ✅ | ❌ | ✅ |
| **国际化** | ✅ 20 种语言 | ❌ 仅英文 | ✅ | ✅ | ✅ |
| **GitHub 集成** | ✅ | ✅ | ✅ | ✅ 插件 | ✅ |
| **Slack 集成** | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Webhook** | ✅ | ✅ | ✅ | ❌ | ❌ |
| **移动端** | ❌ 响应式 Web | ✅ 原生 | ✅ 原生 | ❌ | ❌ |
| **AI 功能** | ✅ AI Assistant | ✅ | ✅ | ❌ | ❌ |

### 6.2 架构对比

| 技术维度 | Plane | Linear | Jira | Redmine | Taiga |
|----------|-------|--------|------|---------|-------|
| **后端** | Django + DRF | Node.js | Spring/Java | Rails | Django |
| **前端** | React + Vite | React | React/Atlassian | ERB | Angular |
| **数据库** | PostgreSQL | ? | 多种 | MySQL/PG | PostgreSQL |
| **实时** | Hocuspocus/Yjs | 自研 | ? | 无 | 无 |
| **异步任务** | Celery + RabbitMQ | ? | 内置 | 无 | Celery |
| **缓存** | Redis/Valkey | ? | Ehcache | 无 | 无 |
| **存储** | MinIO/S3 | ? | S3 | 本地 | 本地 |
| **Monorepo** | ✅ Turborepo | ? | ❌ | ❌ | ❌ |
| **容器化** | ✅ 10 个服务 | ❌ | ✅ | ❌ | ❌ |

---

## 7. 代码质量评估

### 7.1 代码质量（7.5/10）

**优点**：
- 全仓库统一使用 `oxfmt` + `oxlint`，格式和风格高度一致
- TypeScript 严格模式，类型覆盖率极高
- Django 后端使用 `drf-spectacular` 自动生成 OpenAPI 规范
- 自建 `@plane/decorators` 装饰器框架，路由定义简洁优雅
- 每个 view 文件顶部都有版权声明（AGPL-3.0）

**不足**：
- `apps/api/plane/api/views/issue.py` 达 2484 行，单个 view 文件过于庞大
- 部分 Python 代码有 `# noqa: E501` 注释，行过长
- `Issue.save()` 方法中混合了状态推断、序列号生成、排序逻辑，职责过多

### 7.2 文档（7/10）

**优点**：
- `CONTRIBUTING.md` 详尽，包含环境搭建、架构说明、编码规范、国际化指南
- `AGENTS.md` 为 AI 辅助开发提供快速参考
- OpenAPI 文档自动生成，可交互（Swagger UI）
- 代码注释密度适中，关键逻辑有解释

**不足**：
- 缺少独立的架构设计文档（ADR）
- `packages/` 下的包缺少 README
- 没有数据模型 ER 图或关系文档

### 7.3 测试（4/10）

**不足明显**：
- 后端测试集中在 `apps/api/plane/tests/`，分为 `unit/`、`contract/`、`smoke/` 三层
- 但测试文件数量极少（仅约 15 个），与 400K 行代码库体量严重不匹配
- Issue 核心模型只有 `test_issue_comment_modal.py` 一个测试
- `apps/live` 有独立的 test 命令但测试覆盖率未知
- 前端几乎没有可观察到的测试文件
- 这在 47K star 的开源项目中是一个显著的短板

### 7.4 CI/CD（6/10）

**GitHub Actions 工作流**：
- `pull-request-build-lint-web-apps.yml`：PR 触发的 lint + format + build 检查
- `pull-request-build-lint-api.yml`：后端 API 的 PR 检查
- `build-branch.yml`：分支构建（410 行，最复杂的工作流）
- `feature-deployment.yml`：功能分支部署
- `codeql.yml`：安全扫描
- `copyright-check.yml`：版权声明检查
- `check-version.yml`：版本号检查

**优点**：PR 级别的构建和 lint 检查完善，使用 Turborepo 的增量构建能力。使用 `concurrency` 控制避免重复构建。

**不足**：没有自动化测试在 CI 中运行（可能因为测试本身太少），没有看到 E2E 测试流水线。

### 7.5 错误处理（7/10）

**前端**：
- `apps/web/app/error/` 目录提供错误边界
- `apps/live/src/lib/errors.ts` 自定义 AppError 类，带 context 和 code
- API 服务层统一 axios 异常处理

**后端**：
- `plane.utils.exception_logger.log_exception` 统一异常日志
- REST Framework 自定义异常处理器（`EXCEPTION_HANDLER` 指向 `authentication.adapter.exception.auth_exception_handler`）
- Celery 任务使用 JSON 格式日志
- S3 操作使用 try-catch + `log_exception` + 返回 None 的防御式模式

**亮点**：Live 服务的错误处理设计精良——当文档获取失败时，会通过 `broadcastError` 通知前端用户，而不是静默失败。

---

## 总结

Plane 是一个野心勃勃的项目——它试图在「开源 + 自托管 + 功能完整 + 现代体验」四个维度上同时做到优秀。从架构来看，它确实在大多数维度上做到了：

- **架构成熟度**：三层前端 + Django REST + Hocuspocus 实时协作 + Celery 异步任务 + MinIO/S3 存储，这是一个面向生产级部署的全栈架构。
- **代码工程化**：Turborepo monorepo、装饰器路由、共享类型包、20 种语言国际化——这些都是大型产品才需要考虑的工程实践。
- **创新亮点**：PostgreSQL Advisory Lock 分布式序列号、装饰器驱动的 REST/WebSocket 路由、二进制文档 + 多格式同步存储、MobX 表达式树过滤。

**最大的风险点**是测试覆盖率严重不足——400K 行代码只有约 15 个测试文件，这在快速迭代中可能积累大量回归问题。47K star 的社区热度是否可持续，取决于团队能否在功能迭代的同时补齐技术债务。
