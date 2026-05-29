## 动机与定位
- 要解决的问题: 应用部署和数据库管理对中小团队和独立开发者来说过于复杂且成本高昂。云平台（Vercel、Netlify、Heroku）存在厂商锁定和高额费用，而现有自托管方案要么 UI 粗糙（Coolify）、要么无 Web 界面（Dokku、Kamal）、要么更新停滞（CapRover）。
- 为什么现有方案不够: Coolify 资源占用高（idle CPU 6%+ vs Dokploy 0.8%）且 PHP 技术栈难以吸引现代前端开发者；Dokku 和 Kamal 纯 CLI 操作门槛高，不适合非运维角色使用；CapRover 维护力度下降。市场缺少一个**轻量、现代技术栈、UI 简洁且原生支持 Docker Swarm 集群**的 PaaS。
- 目标用户: 不愿受厂商锁定的独立开发者和中小技术团队，尤其是拥有自己 VPS 但不想手动管理部署流程的全栈开发者。

## 作者视角
### 问题发现
Siumauricio 作为独立开发者，在个人项目部署中频繁与 Docker、Traefik、SSL 证书等基础设施打交道。他发现现有 PaaS 替代品（Coolify、CapRover）要么过重、要么缺乏现代感。2024 年初正值「脱云」（de-cloud）运动兴起，self-hosted 赛道热度攀升，时机窗口精准。

### 解法哲学
**简洁优先 + Docker-native**。Dokploy 不重新发明轮子，而是做 Docker 生态的「友好外壳」：
1. **构建策略多样但统一入口** — 支持 Nixpacks、Heroku Buildpacks、Paketo、Railpack、Dockerfile、静态部署六种构建方式，通过统一的 `getBuildCommand` 调度器屏蔽复杂性
2. **Swarm 而非 Kubernetes** — 选择 Docker Swarm 作为编排层，牺牲了 K8s 生态的丰富性，换来了极低的运维复杂度和资源开销
3. **端到端类型安全** — TypeScript + tRPC + Drizzle ORM + Zod 验证，从数据库到前端全链路类型推导

### 背景知识迁移
- **前端工程化经验** → PaaS UI 设计感强，操作流畅（Next.js + Radix UI + Tailwind）
- **Docker 深度使用经验** → 对 Docker Service API（非 Container API）的深刻理解，`mechanizeDockerContainer` 函数直接操作 Swarm Service 的创建/更新
- **DevOps 自动化思维** → 将 Traefik 配置生成为 YAML 动态文件，免去手动反向代理配置

### 战略图景
**Open-core 商业模式**，代码中已明确体现：
- 核心功能 Apache 2.0 开源
- `/proprietary` 目录下的企业功能（SSO、审计日志、白标、自定义角色）采用 Dokploy Source Available License（DSAL），需商业许可
- `Dockerfile.cloud` 和 Stripe 集成表明已有云托管版本 `app.dokploy.com`
- License Key 验证系统（`/utils/crons/enterprise.ts`）每 3 天校验一次
- AI 辅助部署功能（多 LLM 提供商支持）作为差异化卖点

## 架构与设计决策
### 目录结构概览
```
dokploy/
├── apps/
│   ├── dokploy/          # 主应用 — Next.js 前端 + 自定义 Node 服务器
│   │   ├── pages/        # Next.js Pages Router
│   │   ├── components/   # React UI 组件（dashboard/shared/proprietary/ui）
│   │   ├── server/       # tRPC 路由 + BullMQ 队列 + WebSocket 服务器
│   │   ├── drizzle/      # 167 个数据库迁移文件
│   │   └── __test__/     # 48 个测试文件（Vitest）
│   ├── api/              # Hono + Inngest 部署服务（云版本用）
│   ├── monitoring/       # Go (Fiber) 监控代理，收集系统指标
│   └── schedules/        # BullMQ 定时任务调度器（备份/清理/自定义计划）
├── packages/
│   └── server/           # @dokploy/server — 核心业务逻辑包
│       └── src/
│           ├── services/   # 40+ 服务模块（application/compose/database/...）
│           ├── utils/      # 构建器/Docker/Traefik/通知/备份/集群
│           ├── db/schema/  # 45+ Drizzle ORM 表定义
│           ├── setup/      # 服务器初始化（Swarm/网络/Traefik/监控）
│           └── auth/       # Better-Auth 认证
```
**总计**: 397 个 TypeScript 文件，~78,290 行 TS 代码 + 1,267 行 Go 代码

### 关键设计决策

1. **决策**: Docker Swarm Service API（而非 Container API）作为核心编排层
   - 问题: 需要支持零停机部署、滚动更新、多节点扩展
   - 方案: 所有应用以 Docker Service 运行，通过 `mechanizeDockerContainer` 函数统一管理创建/更新，利用 Swarm 内置的服务发现和负载均衡
   - Trade-off: 放弃了 Kubernetes 的生态和大规模集群能力，但获得了极简的运维成本（单节点 Swarm 即可运行）
   - 可迁移性: **高** — 任何需要零停机更新的 Docker 项目都可借鉴此模式

2. **决策**: pnpm Monorepo + `@dokploy/server` 独立包
   - 问题: 前端和后端逻辑强耦合，服务端代码需被多个 app 复用
   - 方案: 将核心业务逻辑抽取到 `packages/server`，通过 workspace 协议 (`workspace:*`) 引用，前端 app 通过 `@dokploy/server` 导入
   - Trade-off: 增加了构建复杂度（需先构建 server 包），但实现了 API 服务和调度器共享同一套数据访问和业务逻辑
   - 可迁移性: **高** — 标准 monorepo 最佳实践

3. **决策**: tRPC + Drizzle ORM + Zod 端到端类型安全
   - 问题: REST API 在前后端之间缺乏类型保证，Schema 变更容易引入运行时错误
   - 方案: tRPC 路由直接暴露 Zod schema 验证，Drizzle ORM 的 `createInsertSchema` 从数据库定义生成 Zod 类型，前端通过 `@trpc/react-query` 获得完整类型推导
   - Trade-off: 紧耦合了前后端技术栈，不利于非 TypeScript 客户端集成（因此额外提供了 OpenAPI 文档生成）
   - 可迁移性: **高** — T3 Stack 的标准模式，适用于任何全栈 TypeScript 项目

4. **决策**: BullMQ 单队列串行部署 + Redis 作为队列后端
   - 问题: 部署操作是长耗时且资源密集型的，需要有序调度
   - 方案: 所有部署任务进入单一 BullMQ 队列 `deployments`，Worker 串行消费
   - Trade-off: 串行执行避免了资源竞争，但成为高并发场景瓶颈（Issue #2127 反映了此问题）。云版本已迁移至 Inngest（`apps/api`）实现基于 serverId 的并发控制
   - 可迁移性: **中** — BullMQ 模式通用，但串行策略特定于资源受限场景

5. **决策**: Traefik YAML 动态配置文件（而非 Docker Labels）
   - 问题: Traefik 的 Docker Labels 配置方式在 Swarm 模式下有局限，且难以持久化
   - 方案: 为每个应用生成独立的 YAML 配置文件到 `/etc/dokploy/traefik/dynamic/`，通过 Traefik 的 File Provider 动态加载
   - Trade-off: 需要维护文件系统状态，但获得了更灵活的路由控制（支持中间件、重定向、安全策略的精细配置）
   - 可迁移性: **高** — 适用于任何需要程序化管理 Traefik 配置的场景

6. **决策**: 6 个 WebSocket 端点（日志/终端/监控）
   - 问题: 部署日志、容器终端、实时监控需要低延迟双向通信
   - 方案: 在同一 HTTP 服务器上挂载 6 个独立的 WebSocket 服务器，通过路径区分（drawer-logs、listen-deployment、docker-container-logs、docker-container-terminal、terminal、docker-stats）
   - Trade-off: 服务器资源开销增加，但用户体验显著提升（实时构建日志、浏览器内 SSH 终端）
   - 可迁移性: **中** — 适用于需要实时交互的运维/DevOps 工具

7. **决策**: 远程服务器通过 SSH over Dockerode 管理
   - 问题: 需要管理多台远程服务器上的 Docker 资源
   - 方案: `getRemoteDocker` 函数通过 SSH 协议创建远程 Dockerode 实例，所有 Docker 操作透明地路由到远程或本地
   - Trade-off: SSH 连接稳定性依赖网络质量，但避免了在远程服务器上安装额外代理
   - 可迁移性: **高** — 任何 multi-server Docker 管理场景可复用

## 创新点

1. **Compose 文件随机化引擎** — 通过 `randomizeComposeFile` 为 Docker Compose 的所有属性（服务名、卷、网络、配置、密钥）添加随机后缀，实现同一 Compose 模板的多实例隔离部署。
   - 新颖度: 3/5 — 思路不复杂但实现完整
   - 实用性: 5/5 — 解决了多租户/多实例 Compose 部署的核心隔离问题
   - 可迁移性: 4/5 — 任何 Compose 编排平台可复用
   - 适用场景: SaaS 平台为每个客户部署独立实例

2. **Watch Paths 智能部署** — 使用 micromatch glob 模式匹配，仅当指定路径下的文件变更时触发部署，避免无关提交触发重新构建。
   - 新颖度: 2/5 — 借鉴了 Turborepo/Nx 的思路
   - 实用性: 5/5 — monorepo 场景下的刚需
   - 可迁移性: 5/5 — 10 行代码即可复用
   - 适用场景: 任何 CI/CD 系统的选择性触发

3. **统一构建器调度器** — `getBuildCommand` 通过策略模式将 6 种构建方式（Nixpacks/Heroku/Paketo/Railpack/Dockerfile/Static）统一到同一接口，每种构建器返回 shell 命令字符串，由外层统一执行。
   - 新颖度: 3/5 — 策略模式本身不新，但将构建抽象为「生成 shell 命令」的设计巧妙
   - 实用性: 5/5 — 极大简化了多构建工具支持
   - 可迁移性: 4/5 — 适用于任何需要支持多种构建方式的 CI/CD 系统
   - 适用场景: 平台工程团队构建统一的构建抽象层

4. **AI 辅助 Compose 生成** — 集成 10+ LLM 提供商（OpenAI、Anthropic、Azure、Gemini、Ollama 等），用户描述需求后自动生成 docker-compose.yml + 环境变量 + 域名配置 + 配置文件。
   - 新颖度: 4/5 — PaaS 领域较早集成 AI 生成部署配置
   - 实用性: 4/5 — 降低了 Compose 编写门槛
   - 可迁移性: 4/5 — `selectAIProvider` 的多 provider 适配模式通用
   - 适用场景: 任何需要 AI 辅助配置生成的 DevOps 工具

5. **ZIP Drop 部署 + 路径遍历防御** — 支持直接上传 ZIP 文件部署，内置 symlink/设备节点检测和路径遍历防御（`isDangerousNode` + `readValidDirectory`）。
   - 新颖度: 3/5 — 安全防护完善
   - 实用性: 4/5 — 适合无 Git 环境的快速部署
   - 可迁移性: 5/5 — ZIP 解压安全模式可直接复用
   - 适用场景: 文件上传类功能的安全防护

## 可复用模式

1. **Remote Docker 透明代理模式**: `getRemoteDocker(serverId)` — 根据 serverId 是否为空，返回本地 Docker 实例或通过 SSH 创建远程 Docker 实例，调用方代码无需区分本地/远程。
   - 适用场景: 多服务器管理、混合云部署

2. **Shell 命令构建器模式**: 各构建器（nixpacks/heroku/static 等）不直接执行操作，而是生成 shell 命令字符串，由上层统一调度执行并流式输出日志。
   - 适用场景: CI/CD pipeline 构建、批处理任务编排

3. **Swarm Service Upsert 模式**: `mechanizeDockerContainer` 先尝试 `service.update()`，失败则 `docker.createService()`，实现幂等的服务部署。
   - 适用场景: 任何需要声明式管理 Docker Service 的场景

4. **动态 Traefik 配置生成**: 为每个应用生成独立 YAML 文件到动态目录，Traefik File Provider 自动加载，实现无重启路由更新。
   - 适用场景: 需要程序化管理反向代理的平台

5. **Open-core 目录隔离模式**: `/proprietary` 目录使用不同许可证，通过 `hasValidLicense` 函数在运行时做功能门控，代码结构清晰分离。
   - 适用场景: 开源项目的商业化路径设计

6. **多 Provider AI 适配器**: `selectAIProvider` 通过 URL 模式匹配自动选择 SDK，统一返回 AI SDK 兼容的 provider 实例。
   - 适用场景: 需要支持多 LLM 供应商的 AI 功能

## 竞品交叉分析

### vs Coolify
- **Dokploy 更好**: UI 更简洁现代、资源占用更低（idle CPU 0.8% vs 6%+）、TypeScript 全栈类型安全、原生 Docker Swarm 集群支持
- **Coolify 更好**: 社区更大（52.6k stars）、功能更全面（内置数据库管理 UI 更丰富）、更成熟稳定
- **不同目标**: Coolify 追求功能完整性，Dokploy 追求轻量和现代感
- **迁移成本**: 中等 — 两者都是 Docker-based，应用迁移主要是配置重建

### vs Dokku
- **Dokploy 更好**: 完整的 Web UI、多节点集群、团队协作（组织/角色）、实时监控仪表板
- **Dokku 更好**: 极致轻量（Shell/Go）、Heroku 兼容的 `git push` 工作流、更长的历史和稳定性
- **不同目标**: Dokku 面向单人/单服务器的极简部署，Dokploy 面向需要可视化管理的团队
- **迁移成本**: 低 — Dokku 的 buildpacks 应用可无缝迁移

### vs CapRover
- **Dokploy 更好**: 活跃维护、现代技术栈、Docker Swarm 原生集群、AI 辅助部署
- **CapRover 更好**: 模板生态更丰富（One-Click Apps）、文档更完善
- **不同目标**: CapRover 偏向模板驱动的快速部署，Dokploy 偏向灵活的自定义部署
- **迁移成本**: 低 — Docker Compose 应用可直接迁移

### vs Kamal
- **Dokploy 更好**: Web UI、多应用管理、数据库管理、自动 SSL、Traefik 集成
- **Kamal 更好**: 37signals（Basecamp）团队背书、零依赖（直接 SSH + Docker）、适合 Rails 生态
- **不同目标**: Kamal 是 CLI 工具，面向 Rails 开发者的极简部署；Dokploy 是完整 PaaS 平台
- **迁移成本**: 低 — Docker 镜像可直接使用

### 综合竞争结论
Dokploy 的**差异化护城河**在于：① TypeScript 全栈现代技术栈吸引前端/全栈开发者贡献；② 原生 Docker Swarm 集群支持（Coolify 也在追赶）；③ Open-core 模式下的企业功能（SSO、审计日志、白标）为商业化铺路。**主要竞争风险**来自 Coolify 的社区规模优势和 Kamal 的 Rails 生态绑定。**生态定位**为中型团队的「轻量 PaaS」，介于个人用 Dokku 和重型 Kubernetes 平台之间。

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 测试覆盖 | ⭐⭐⭐ | 48 个测试文件，覆盖 Compose 解析、部署流程、权限系统、Traefik 配置等核心路径，但缺少集成测试和 E2E 测试 |
| 文档质量 | ⭐⭐⭐ | CONTRIBUTING.md 详尽、SECURITY.md 完备，但代码内注释偏少，核心架构缺少设计文档 |
| CI/CD | ⭐⭐⭐⭐ | 8 个 GitHub Actions workflow（Docker 构建/推送、PR 质量检查、格式化、OpenAPI 同步）、Canary 分支策略 |
| 错误处理 | ⭐⭐⭐ | 使用 tRPC 的 TRPCError 统一错误码、自定义 ExecError 封装命令执行失败信息、WebSocket 有 try-catch 保护 |
| Linter/Formatter | ⭐⭐⭐⭐ | Biome 2.1（替代 ESLint+Prettier）、lint-staged 预提交检查、严格的 import 排序和未使用变量检测 |
| 类型安全 | ⭐⭐⭐⭐⭐ | tRPC + Drizzle + Zod 全链路类型推导，`InferResultType` 泛型实现关联查询的类型推导 |
| 安全性 | ⭐⭐⭐⭐ | X-Frame-Options/CSP 安全头、ZIP 路径遍历防御、SSH 密钥管理、shell-quote 防注入 |
| 许可证 | ⭐⭐⭐⭐ | Apache 2.0 + 企业功能专属许可（DSAL），边界清晰 |

### 质量检查清单
- [x] LICENSE — Apache 2.0 + DSAL (proprietary)
- [x] CONTRIBUTING.md — 完整的开发设置、提交规范、PR 流程
- [x] SECURITY.md — 漏洞报告流程
- [x] CI/CD — 8 个 GitHub Actions workflows
- [x] Linter — Biome 2.1 + lint-staged
- [x] Lock file — pnpm-lock.yaml 存在
- [x] .gitignore — 完善
- [x] 测试 — Vitest，48 个测试文件
- [ ] CHANGELOG — 未发现独立的 CHANGELOG 文件（通过 GitHub Releases 管理）
- [ ] Examples — 无独立示例目录（模板系统通过外部仓库 Dokploy/templates 管理）
- [x] Docker — 多阶段构建、健康检查、生产优化
- [x] 安全头 — CSP、X-Frame-Options、nosniff
- [x] 环境变量 — .env.example 提供、敏感信息不入库
