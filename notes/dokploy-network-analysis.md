## 仓库基本数据
- Star / Fork / Watcher: 32,729 / 2,310 / 99
- 语言: TypeScript (99.0%), Go (0.7%), CSS (0.1%), JavaScript (<0.1%), Dockerfile (<0.1%), Shell (<0.1%)
- License: Other（非标准 OSI License，需进一步确认具体条款）
- 创建时间: 2024-04-19 | 最近推送: 2026-04-06
- 话题标签: deployment, self-hosted, vps, backend, backups, databases, devops, docker, frontend, mariadb, mongodb, mysql, nextjs, postgresql
- 已归档: 否 | 是Fork: 否

## 作者画像
- 姓名/ID: Dokploy（GitHub Organization） | 公司: 无 | 位置: 未公开
- 粉丝: 743 | 公开仓库: 16 | 账号年龄: 约 2.2 年（2024-01-17 创建）
- 核心维护者: **Siumauricio**（3,962 次提交，占总量约 80%+），为项目创始人兼唯一核心开发者，通过 GitHub Sponsors 接受赞助
- 此 repo 投入权重: **极高** — Organization 下 16 个仓库中 dokploy 是绝对核心（32.7k stars），其余仓库（website、templates、mcp、cli、examples）均为配套生态
- 作者类型: 独立开发者主导的开源组织（Dokploy Org 专为此项目而建）
- 贡献集中度: **单人主导** — Siumauricio 贡献 3,962 次，第二名 lorenzomigliorero 仅 69 次；Top 30 贡献者中扣除 bot 后社区贡献约 800+ 次
- 背景推断: Siumauricio 是一位全栈开发者，具备深厚的 Docker/DevOps 领域经验。Organization bio 直接定位为「Vercel/Netlify/Heroku 的开源替代」，说明作者对 PaaS 赛道有清晰的产品认知。生态布局完善（CLI、MCP Server、Templates、Examples），展现出成熟的开源运营思维

## 社区热度
- 热度级别: **大众热门**（32.7k stars）
- 增长模式: **爆发+稳步复合型**
  - 2024-04-26 首个 star → 2024-04-29 爆发式增长（HN/Reddit 引爆，单日数百 star）
  - 2024-05 ~ 2024-08: 4 个月内达到 5,000 stars（稳步增长）
  - 2024-08 ~ 2024-12: 4 个月 5k → 10k（加速期）
  - 2025-01 ~ 2025-05: 10k → 20k（高增长期，4 个月翻倍）
  - 2025-05 ~ 2025-10: 20k → 25k（增速放缓但依然健康）
  - 2025-10 ~ 2026-02: 25k → 30k（5 个月 5k，稳步增长）
  - 2026-02 ~ 2026-04: 30k → 32.7k（2 个月 2.7k，保持稳定）
- 近期趋势: 最近 2 天（4/2-4/4）约 100 个新 star，日均约 50 个 star，增长健康持续
- 套利判断: **非低估** — 32.7k stars 已充分反映市场认知，但项目仍在快速迭代中，持续增长可期

## 生态网络
- 上游依赖/平台生态:
  - **Dokploy Cloud**（app.dokploy.com）— 官方托管版，$4.50/月起
  - **Dokploy CLI** — 命令行管理工具（80 stars）
  - **Dokploy MCP Server** — AI 集成，支持 Claude 等 AI 直接操作部署（160 stars）
  - **Dokploy Templates** — 一键部署模板库（184 stars）
  - **Dokploy Examples** — 部署示例集（92 stars）
  - Docker Hub 下载量 6M+
- 同类项目:
  1. **Coolify**（coollabsio/coolify）— 52.6k stars，PHP，最大直接竞品，模板更多（280+），社区更大
  2. **Dokku**（dokku/dokku）— 31.9k stars，Shell/Go，Heroku 式 PaaS 鼻祖，Git-push 部署，更轻量但功能较少
  3. **CapRover**（caprover/caprover）— 15.0k stars，JavaScript，Docker+nginx，模板驱动，成熟但更新较慢
  4. **Kamal**（basecamp/kamal）— 14.0k stars，Ruby，Basecamp 出品，非 UI 驱动，侧重 SSH 部署
  5. **Portainer** — 容器管理平台，功能更广但不是纯 PaaS 定位

## 官方文档洞察
- 价值主张: 「免费、可自托管的 PaaS 平台，简化应用和数据库的部署与管理」— 强调零成本自主可控
- 目标用户: 寻求部署简便性但不愿受厂商锁定的开发者和中小团队；对 Docker 有基本了解的工程师
- 差异化叙事:
  - 相比 Coolify：UI 更简洁直观、资源占用更低（idle CPU 0.8% vs 6%+）、原生 Docker Swarm 集群支持
  - 相比 Dokku：提供完整 Web UI、多服务器管理、实时监控
  - 相比云厂商：完全自托管、无账单意外、数据完全自主
- 设计哲学: Docker-native 一切以容器为中心；端到端类型安全（TypeScript + tRPC）；自动化优先（Git webhook、API/CLI）
- 技术路线图: 网络管理系统 v1（PR #2811 进行中）、构建并发控制（PR #2127 进行中）；持续扩展模板生态
- 架构文章要点:
  - 四大核心组件：Next.js（前端+SSR）、PostgreSQL（持久化）、Redis（部署队列 via BullMQ）、Traefik（反向代理+负载均衡）
  - Monorepo 架构：pnpm workspace，三个应用（前端 port 3000、Hono API port 4000、BullMQ processor port 4001）+ 共享包 @dokploy/server
  - Better-Auth 认证系统，支持 OAuth/SSO/TOTP
- 外部深度视角:
  1. **[Self-Hosted Deployment Tools Compared (dev.to)](https://dev.to/ameistad/self-hosted-deployment-tools-compared-coolify-dokploy-kamal-dokku-and-haloy-2npd)** — 作者认为 Dokploy UI 最优雅，但指出社区规模和教育资源不如 Coolify，资源消耗对小 VPS 不友好
  2. **[Comparing Self-Hostable PaaS (kloudshift.net)](https://kloudshift.net/blog/comparing-self-hostable-paas-solutions-caprover-coolify-dokploy-reviewed/)** — 作者将 Dokploy 评为个人最爱，但指出单管理员限制、Preview 部署仅支持 GitHub App、缺乏外部日志导出、build/host 分离不成熟、缺少 robust 可观测性集成等关键缺陷

## 竞品清单
- **Coolify** | Stars: 52.6k | 定位: 自托管 PaaS 全家桶 | 优势: 社区最大、280+ 模板、功能最全面、多服务器管理 | 劣势: PHP 技术栈较重、idle 资源占用高、UI 相对粗糙
- **Dokku** | Stars: 31.9k | 定位: 轻量 Heroku 式 PaaS | 优势: 极轻量、成熟稳定（10+ 年历史）、Git-push 体验 | 劣势: 无 Web UI、单服务器限制、学习曲线
- **CapRover** | Stars: 15.0k | 定位: Docker 模板驱动 PaaS | 优势: 简单易上手、丰富的一键部署 | 劣势: 更新频率放缓、架构老旧（Node.js + nginx）、缺少多节点原生支持
- **Kamal** | Stars: 14.0k | 定位: SSH 部署工具（非 UI PaaS） | 优势: Basecamp 背书、Ruby 生态强、无 daemon 占用 | 劣势: 无 Web UI、需要 Ruby 知识、更适合 Rails 项目
- **Portainer** | Stars: 32.0k+ | 定位: 通用容器管理平台 | 优势: 功能极广、企业版成熟 | 劣势: 不是 PaaS、部署流程需自行编排、付费版贵

## 关键 Issue 信号
1. [#2811 feat!: Network Management System v1](https://github.com/Dokploy/dokploy/pull/2811)（54 评论，Open）— 揭示了 Dokploy 在网络管理方面的架构重构方向，这是从「简单 PaaS」向「生产级平台」演进的关键一步，社区讨论活跃说明此功能需求强烈
2. [#2127 feat(server): add ability to change builds concurrency](https://github.com/Dokploy/dokploy/pull/2127)（38 评论，Open）— 揭示了当前构建队列的瓶颈：Redis 单队列串行构建在多项目场景下成为性能卡点，用户对并发构建的需求迫切
3. [#4002 Upgrading to latest version broke my installation](https://github.com/Dokploy/dokploy/issues/4002)（44 评论，Closed）— 揭示了升级稳定性的核心痛点：自托管 PaaS 的升级可靠性直接关系用户信任度，频繁出现破坏性升级将动摇生产用户的信心

## 知识入口
- DeepWiki: [https://deepwiki.com/dokploy/dokploy](https://deepwiki.com/dokploy/dokploy) — 已收录，包含完整架构分析
- Zread.ai: 未收录（403 错误）
- 关联论文: 无（arxiv.org 无相关论文）
- 在线 Demo: 无公开 Playground；可通过 [Dokploy Cloud](https://app.dokploy.com) 试用托管版

## 项目展示素材
### README 媒体
1. ![Dokploy Hero Banner](.github/sponsors/logo.png) → `https://raw.githubusercontent.com/Dokploy/dokploy/canary/.github/sponsors/logo.png` — 类型: hero/banner
2. ![Video Tutorial Thumbnail](https://dokploy.com/banner.png) — 类型: demo（视频教程封面，链接至 [YouTube 教程](https://youtu.be/mznYKPvhcfw)）

### 官网媒体
- 官网（dokploy.com）首页包含产品截图和功能展示，但非静态图片 URL

### 筛选说明
- 总共发现 4 个媒体元素，筛选后保留 2 个
- 排除了 1 个 Discord widget badge 和 1 个 contrib.rocks 贡献者头像拼图（非展示性内容）

## 快速判断
- 是否值得深入: **是** — 32.7k stars 且仍在快速增长，架构现代（TypeScript monorepo + tRPC + Docker Swarm），生态完善（CLI/MCP/Templates），自托管 PaaS 赛道需求明确
- 初步定位: **大众热门 + 赛道挑战者** — 在 Coolify（52.6k）之后稳居自托管 PaaS 第二名，但增速和代码质量可能后来居上
- 作者可信度: **高** — 单人主导但投入极高（3,962 次提交），2 年内从零到 32.7k stars，商业化路径清晰（Cloud 托管版），生态布局成熟
- 竞品格局: **红海但有差异化空间** — 自托管 PaaS 赛道玩家众多（Coolify、Dokku、CapRover、Kamal），但 Dokploy 在 Docker-native 体验、UI 质量和资源效率上有明确差异化定位
