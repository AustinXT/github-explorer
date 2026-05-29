# modelcontextprotocol/servers 仓库分析报告

> 分析日期：2026-03-22
> 仓库地址：https://github.com/modelcontextprotocol/servers

---

## 一、项目概述

**Model Context Protocol (MCP) Servers** 是 Anthropic 发起的 Model Context Protocol 协议的官方参考服务器合集。MCP 是一个开放协议，旨在实现 LLM 应用与外部数据源和工具之间的无缝集成。该仓库包含一组**参考实现**，用于展示 MCP 的特性和 SDK 用法，同时也链接了大量社区构建的第三方服务器。

### 核心定位

- **参考实现**：非生产级方案，而是教育性示例
- **SDK 示范**：展示 TypeScript SDK 和 Python SDK 的标准用法
- **生态枢纽**：README 中收录了数百个官方和社区 MCP 服务器的链接
- **AI 基础设施**：是 AI 工具生态中连接 LLM 与外部世界的关键协议层

---

## 二、网络分析（Phase 1）

### 2.1 基础指标

| 指标 | 数值 |
|------|------|
| Star 数 | **81,714** |
| Fork 数 | **10,009** |
| Watcher 数 | 572 |
| 主语言 | TypeScript (69.4%) |
| 其他语言 | Python (19.2%), JavaScript (10.3%), Dockerfile (1.2%) |
| 创建时间 | 2024-11-19 |
| 最后推送 | 2026-03-17 |
| 磁盘大小 | 28.6 MB |
| 默认分支 | main |
| 是否归档 | 否 |
| 许可证 | MIT → Apache-2.0（过渡中） |
| 主页 | https://modelcontextprotocol.io |

### 2.2 组织信息

| 属性 | 内容 |
|------|------|
| 组织名 | Model Context Protocol |
| 登录名 | modelcontextprotocol |
| 简介 | An open protocol that enables seamless integration between LLM applications and external data sources and tools |
| 公开仓库数 | 39 |
| 关注者 | 44,709 |
| 创建时间 | 2024-09-20 |
| 官网 | https://modelcontextprotocol.io |

**组织旗下关键仓库**（39个）：
- 核心协议：`modelcontextprotocol`（规范文档）、`servers`（参考服务器）、`registry`（MCP 注册中心）
- SDK（10种语言）：TypeScript、Python、Go、Java、Kotlin、C#、Rust、Swift、Ruby、PHP
- 工具链：`inspector`（调试工具）、`create-python-server`、`create-typescript-server`（脚手架）
- 扩展/实验：`ext-auth`、`ext-apps`、多个 `experimental-ext-*` 扩展
- 工作组：`transports-wg`、`agents-wg`、`financial-services-interest-group`

### 2.3 核心贡献者

| 排名 | 贡献者 | 贡献次数 | 角色推断 |
|------|--------|----------|----------|
| 1 | **olaservo** | 522 | 核心维护者 |
| 2 | **tadasant** | 239 | 核心维护者 |
| 3 | **jspahrsummers** | 217 | 核心维护者（MCP 协议创始人之一） |
| 4 | **cliffhall** | 204 | 核心维护者（近期最活跃） |
| 5 | **dsp-ant** | 160 | Anthropic 工程师 |
| 6 | **jerome3o-anthropic** | 121 | Anthropic 工程师 |
| 7 | **maheshmurag** | 66 | 活跃贡献者 |
| 8 | **evalstate** | 62 | 活跃贡献者 |
| 9 | **baryhuang** | 47 | 社区贡献者 |
| 10 | **marcelo-ochoa** | 42 | 社区贡献者 |

总贡献者数量：**1,017 人**（独立作者），显示出极强的社区参与度。

近 3 个月（2025-12 至今）最活跃的贡献者：cliffhall (96 commits)、Ola Hungerford/olaservo (34 commits)、Koichi ITO (10 commits)。

### 2.4 Issue 与 PR 统计

| 类型 | 开放 | 已关闭/合并 | 总计 |
|------|------|-------------|------|
| Issue | 314 | 576 | 890 |
| PR（开放） | 236 | - | - |
| PR（已合并） | - | 1,189 | - |
| PR（已关闭未合并） | - | 1,302 | - |
| **PR 总计** | 236 | 2,491 | 2,727 |

**Issue 关闭率**：64.7%（576/890）
**PR 合并率**：43.6%（1,189/2,727）—— 大量社区 PR 被拒绝，体现严格的代码审查标准。

### 2.5 热门讨论（按评论数排序）

| # | 标题 | 评论数 | 状态 |
|---|------|--------|------|
| #40 | MCP servers fail to connect with `npx` on Windows | 112 | 已关闭 |
| #64 | MCP Servers Don't Work with NVM | 88 | 已关闭 |
| #522 | Clarify possible Brave Search TOS violation | 35 | 已关闭 |
| #3051 | The filesystem server stopped working with OpenAI Agent SDK | 21 | 开放 |
| #447 | filesystem MCP server doesn't support legal Windows pathnames | 21 | 开放 |
| #2812 | fix(sequential-thinking): Add input sanitization | 17 | 已关闭 |

**问题模式**：Windows 兼容性和 Node.js 环境（npx/nvm）问题是早期最大痛点；后期问题集中在与第三方 SDK（如 OpenAI Agent SDK）的互操作性。

### 2.6 Star 增长趋势

- 首个 Star 记录：2024-11-25（仓库创建后 6 天）
- 至 2026-03-22：81,714 Stars
- 约 16 个月积累 81K+ Stars，平均每月约 **5,100 Stars**
- 属于 GitHub 上增长最快的项目之一，反映了 MCP 协议在 AI 生态中的爆发式采纳

### 2.7 竞品与替代方案

**协议层竞品**：
1. **LangChain / LangGraph** — 提供 Agent 编排框架，可通过适配器与 MCP 集成，但并非直接竞争
2. **Vertex AI Agent Builder** — Google 的托管式 Agent 基础设施，封装了部署复杂度
3. **Amazon Bedrock AgentCore** — AWS 的企业级 MCP 编排服务，集成多会话记忆管理

**MCP 生态内的增强实现**：
1. **K2view** — 利用 Micro-Database 技术为生成式 AI 提供企业数据安全访问
2. **Vectara MCP Engine** — 专注 RAG 的 MCP 实现，强于语义搜索
3. **GitHub MCP Server** — 让 Agent 自主执行代码变更的 DevOps 自动化
4. **Merge MCP Server** — 添加企业级认证、加密和托管基础设施
5. **Disco.dev** — 开源个人 MCP 集线器，零配置启动

**安全考量**：据 Equixly 安全评估，43% 的 MCP 实现存在命令注入漏洞，30% 存在 SSRF 漏洞，22% 允许任意文件访问。

### 2.8 知识入口

| 资源 | 链接 |
|------|------|
| 官方文档 | https://modelcontextprotocol.io |
| MCP 注册中心 | https://registry.modelcontextprotocol.io |
| MCP 规范 | https://spec.modelcontextprotocol.io |
| MCP 博客 | https://blog.modelcontextprotocol.io |
| GitHub 组织 | https://github.com/modelcontextprotocol |

---

## 三、元分析（Phase 2）

### 3.1 代码统计

| 语言 | 文件数 | 代码行数 | 注释行 | 空白行 |
|------|--------|----------|--------|--------|
| TypeScript | 63 | 8,244 | 1,353 | 1,506 |
| Python | 14 | 2,188 | 121 | 418 |
| JSON | 11 | 4,308 | 0 | 0 |
| Dockerfile | 7 | 109 | 28 | 72 |
| TOML | 3 | 107 | 0 | 11 |
| Markdown | 19 | 0 (文档) | 3,020 | 610 |
| **总计** | **117** | **15,466** | **4,522** | **2,617** |

总行数 **22,605 行**。项目规模精炼，代码与文档比约 **3.4:1**。

### 3.2 提交历史

| 指标 | 数值 |
|------|------|
| 首次提交 | 2024-11-19 (`Initial commit`) |
| 最新提交 | 2026-03-17 (`fix(fetch): refresh uv lockfile`) |
| 总提交数 | **4,070** |
| 非合并提交 | **2,190** |
| 项目寿命 | ~16 个月 |
| 独立作者数 | **1,017** |

### 3.3 月度提交趋势

```
2024-11: ████████████ 232   （项目诞生，快速迭代）
2024-12: ██████████████████████████ 525   （第一波社区贡献涌入）
2025-01: ███████████████ 304
2025-02: █████████ 186
2025-03: ██████████████████████████████████ 677   （MCP 协议曝光度高峰）
2025-04: ████████████████████████ 483
2025-05: ██████████████████ 365
2025-06: ████████████ 249
2025-07: ██████████ 211
2025-08: ███████████ 217
2025-09: ████████ 170
2025-10: ███████ 144
2025-11: █████ 105   （大规模归档，瘦身为核心参考实现）
2025-12: ██████ 117
2026-01: ██ 47
2026-02: █ 27
2026-03: █ 11    （截至3/17）
```

**趋势解读**：
- **2024-11 ~ 2025-03**：爆发期，MCP 协议发布引起广泛关注，社区贡献大量涌入
- **2025-04 ~ 2025-09**：成熟期，提交量稳中有降，项目结构趋于稳定
- **2025-10 ~ 2026-03**：整理期，大量第三方服务器归档至 `servers-archived`，仓库回归核心参考实现定位，提交量显著降低

### 3.4 最频繁修改的文件

| 修改次数 | 文件 |
|----------|------|
| 670 | `README.md` |
| 46 | `src/everything/everything.ts` |
| 37 | `package-lock.json` |
| 26 | `src/everything/docs/architecture.md` |
| 24 | `src/everything/tools/index.ts` |
| 24 | `src/everything/package.json` |
| 23 | `src/filesystem/index.ts` |
| 21 | `src/git/src/mcp_server_git/server.py` |
| 20 | `src/filesystem/README.md` |
| 18 | `src/everything/server/index.ts` |

**分析**：README.md 修改 670 次，远超其他文件，因为大量社区提交是往 README 添加第三方服务器链接。核心代码修改集中在 `everything`（测试/参考服务器）和 `filesystem`（最常用的参考实现）。

### 3.5 最频繁修改的目录

| 修改次数 | 目录 |
|----------|------|
| 483 | `src/everything` |
| 197 | `src/filesystem` |
| 163 | `src/git` |
| 152 | `src/github`（已归档） |
| 91 | `src/sqlite`（已归档） |
| 77 | `src/fetch` |
| 71 | `src/memory` |
| 71 | `.github/workflows` |
| 58 | `src/time` |
| 53 | `src/sequentialthinking` |

### 3.6 当前参考服务器

仓库经过瘦身后，保留 **7 个核心参考服务器**：

| 服务器 | 语言 | 版本 | 功能 |
|--------|------|------|------|
| **Everything** | TypeScript | v2.0.0 | 完整参考/测试服务器，含 prompts、resources、tools |
| **Fetch** | Python | v0.6.3 | Web 内容抓取与转换，适用于 LLM 高效处理 |
| **Filesystem** | TypeScript | v0.6.3 | 安全文件操作，可配置访问控制 |
| **Git** | Python | v0.6.2 | Git 仓库读取、搜索和操作 |
| **Memory** | TypeScript | v0.6.3 | 基于知识图谱的持久化记忆系统 |
| **Sequential Thinking** | TypeScript | v0.6.2 | 结构化思维链推理工具 |
| **Time** | Python | v0.6.2 | 时间和时区转换 |

**已归档服务器**（13个，移至 `servers-archived`）：
AWS KB Retrieval、Brave Search、EverArt、GitHub、GitLab、Google Drive、Google Maps、PostgreSQL、Puppeteer、Redis、Sentry、Slack、SQLite

### 3.7 版本发布历史

| 发布 | 日期 | 备注 |
|------|------|------|
| 0.1.0 | 2024-11-19 | 初始发布 |
| 0.5.1 | 2024-11-25 | 快速迭代 |
| 2025.1.17 | 2025-01-17 | 切换到日期版本号 |
| 2025.4.24 | 2025-04-25 | |
| 2025.7.1 | 2025-07-01 | |
| 2025.8.4 | 2025-08-05 | |
| 2025.9.25 | 2025-09-25 | |
| 2025.11.25 | 2025-11-25 | MCP 一周年 |
| 2025.12.18 | 2025-12-18 | |
| 2026.1.14 | 2026-01-14 | |
| **2026.1.26** | **2026-01-27** | **最新发布** |

共发布 **40 个标签**，发布节奏从早期每周多次 → 中期每月 1-3 次 → 近期约每月 1 次。

### 3.8 项目治理

- **许可证**：MIT → Apache-2.0 过渡中（新贡献采用 Apache-2.0，文档采用 CC-BY-4.0）
- **行为准则**：Contributor Covenant
- **贡献指南**：CONTRIBUTING.md
- **PR 模板**：有
- **安全策略**：SECURITY.md（使用 GitHub Security Advisories）
- **所属组织**：Linux Foundation 旗下系列项目（"a Series of LF Projects, LLC"）

---

## 四、关键发现与洞察

### 4.1 项目演进路径

1. **爆发期**（2024-11 ~ 2025-03）：作为 MCP 协议的"全家桶"仓库诞生，快速收纳了 GitHub、Slack、PostgreSQL 等十余个参考服务器及数百个社区服务器链接。README 成为 MCP 生态的事实目录。

2. **瘦身转型**（2025-09 ~ 2025-12）：随着 MCP Registry 的推出，项目战略性地将第三方服务器列表引导至注册中心，同时将 13 个参考服务器归档至 `servers-archived`，仅保留 7 个最核心的参考实现。

3. **稳定维护期**（2026-01 至今）：提交频率大幅降低，聚焦于 bug 修复、依赖更新和跨平台兼容性改进。

### 4.2 社区特征

- **超大规模社区**：1,017 位独立作者，4,070 次提交，显示出 MCP 在 AI 开发者社区的巨大影响力
- **严格的门控**：PR 合并率仅 43.6%，大量社区 PR 为 README 添加链接而被拒绝（现已引导至 Registry）
- **Anthropic 主导**：核心维护者大多是 Anthropic 员工或关联人员
- **全球参与**：贡献者包括来自多个国家和公司的开发者

### 4.3 技术特征

- **多语言 SDK 覆盖**：官方提供 10 种语言的 SDK，生态覆盖极广
- **Monorepo 架构**：使用 npm workspaces 管理多个 TypeScript 包，Python 包使用独立的 pyproject.toml
- **轻量级代码**：总代码量仅 ~15K 行，体现参考实现的"示范"定位
- **日期版本号**：从 2025.1.14 起采用日历版本号（CalVer），反映持续交付的理念

### 4.4 生态地位

MCP servers 仓库是 AI 工具生态的关键基础设施节点：

- **81K+ Stars** 使其跻身 GitHub 最受关注的项目行列
- 作为 MCP 协议的**官方示范**，直接影响数千个第三方 MCP 实现
- MCP 注册中心已收录近 **2,000 个 MCP 服务器**，形成蓬勃生态
- 被 Claude Desktop、Cursor、OpenAI Agent SDK 等主流 AI 工具原生支持
- 安全性仍是主要挑战（43% 实现存在注入漏洞），需要持续关注

---

## 五、参考资源

- 仓库：https://github.com/modelcontextprotocol/servers
- MCP 官网：https://modelcontextprotocol.io
- MCP 注册中心：https://registry.modelcontextprotocol.io
- MCP 一周年博客：https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/
- MCP 2026 路线图：https://thenewstack.io/model-context-protocol-roadmap-2026/
- MCP 替代方案评估：https://www.merge.dev/blog/model-context-protocol-alternatives
- MCP 安全评估：https://cybersecuritynews.com/best-model-context-protocol-mcp-servers/
