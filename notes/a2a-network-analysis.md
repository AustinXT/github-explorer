# A2A (Agent-to-Agent Protocol) — 网络分析

> 分析时间：2026-03-22 | 仓库：[a2aproject/A2A](https://github.com/a2aproject/A2A)

---

## 仓库基本数据

| 指标 | 数值 |
|------|------|
| Stars | 22,712 |
| Forks | 2,307 |
| Watchers | 227 |
| Issues (总计) | 188 |
| Pull Requests (总计) | 24 |
| 磁盘占用 | 27.8 MB |
| 主语言 | Shell（协议定义为主，非代码项目） |
| 许可证 | Apache License 2.0 |
| 创建时间 | 2025-03-25 |
| 最近推送 | 2026-03-16 |
| 最近更新 | 2026-03-21 |
| 默认分支 | main |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 官网 | https://a2a-protocol.org |
| Topics | a2a, a2a-mcp, a2a-protocol, a2a-server, agents, generative-ai, linux-foundation |

**版本发布历程：**
| 版本 | 发布时间 | 说明 |
|------|---------|------|
| v1.0.0 | 2026-03-12 | 正式发布 1.0 稳定版，里程碑版本 |
| v0.3.0 | 2025-07-30 | |
| v0.2.6 | 2025-07-17 | |
| v0.2.5 | 2025-06-30 | |
| v0.2.4 | 2025-06-30 | |

**核心特征：** 这不是一个传统的代码仓库，而是一个**协议规范仓库**。主语言标记为 Shell 是因为仓库内以协议文档（Protobuf 定义、Markdown 规范）和构建脚本为主。真正的 SDK 实现分布在组织下的独立仓库中。

---

## 作者画像

### 组织：a2aproject

| 属性 | 值 |
|------|-----|
| 名称 | Agent2Agent (A2A) Project |
| 简介 | Donated to the Linux Foundation by Google |
| 官网 | https://a2a-protocol.org |
| 公开仓库 | 10 |
| 关注者 | 1,273 |
| 创建时间 | 2025-06-20 |

**背景：** A2A 最初由 Google 发起，后捐赠给 Linux Foundation 运营。组织从 Google 名下（`google/A2A`）迁移到独立的 `a2aproject` 组织，表明项目已走向社区化治理。

### 核心贡献者

| 贡献者 | 提交数 | 身份 |
|--------|--------|------|
| **holtskinner** | 174 | Google Cloud AI Developer Advocate，位于 Austin TX，995 followers。项目实际推动者 |
| kthota-g | 27 | Google 相关 |
| amye | 22 | Linux Foundation 社区管理 |
| dependabot[bot] | 13 | 自动依赖更新 |
| madankumarpichamuthu | 13 | |
| pstephengoogle | 13 | Google 工程师 |
| didier-durand | 12 | 社区贡献者 |
| zeroasterisk | 12 | 社区贡献者 |
| darrelmiller | 12 | |
| herczyn | 11 | |

**贡献者结构分析：** 项目高度依赖 holtskinner（174 次提交，占总量的约 40%），其余贡献者提交量断崖式下降。这是典型的"企业主导+社区辅助"模式。Google 员工占据核心位置，Linux Foundation 提供治理支持。

---

## 社区热度

### Star 增长轨迹

| 时间节点 | Stars 约数 | 事件 |
|----------|-----------|------|
| 2025-04-09 | ~100 | 最早期（首批 100 stars 的时间戳） |
| 2025-04-11 | ~5,000 | 发布约 2 周，爆发式增长 |
| 2025-04-15 | ~10,000 | 发布 3 周，破万 |
| 2025-05-15 | ~15,000 | 持续增长 |
| 2025-10 | ~20,000 | 稳定增长 |
| 2026-03-21 | 22,712 | 当前值 |

**增长模式分析：**
- **爆发期（2025-04）：** 发布后 3 周内从 0 涨到约 10,000 stars，日均增长 400+，这是 Google 品牌效应 + AI Agent 赛道热度叠加的结果
- **快速增长期（2025-04 ~ 2025-10）：** 半年内从 10K 增长到 20K，月均增长约 1,600
- **平稳期（2025-10 ~ 2026-03）：** 5 个月增长约 2,700，月均增长约 540，增速显著放缓
- **最近活跃：** 2026-03-21 仍有新 star，v1.0.0 发布（2026-03-12）可能带来小幅回升

### 开发活跃度

- 近 4 周总提交：28 次（owner: 0，全部来自社区/bot）
- 近 12 周总提交：90 次
- 社区健康度评分：87/100（GitHub Community Profile）
- 有 CODE_OF_CONDUCT、CONTRIBUTING.md、LICENSE
- 缺少 Issue Template 和 PR Template

---

## 生态网络

### 官方 SDK 矩阵

| SDK | 语言 | Stars | 安装方式 |
|-----|------|-------|---------|
| [a2a-python](https://github.com/a2aproject/a2a-python) | Python | 1,761 | `pip install a2a-sdk` |
| [a2a-js](https://github.com/a2aproject/a2a-js) | TypeScript | 495 | `npm install @a2a-js/sdk` |
| [a2a-java](https://github.com/a2aproject/a2a-java) | Java | 365 | Maven |
| [a2a-go](https://github.com/a2aproject/a2a-go) | Go | 299 | `go get github.com/a2aproject/a2a-go` |
| [a2a-dotnet](https://github.com/a2aproject/a2a-dotnet) | C# | 209 | `dotnet add package A2A` |
| [a2a-inspector](https://github.com/a2aproject/a2a-inspector) | TypeScript | 376 | A2A Agent 验证工具 |
| [a2a-samples](https://github.com/a2aproject/a2a-samples) | Jupyter | 1,424 | 示例集合 |
| [a2a-tck](https://github.com/a2aproject/a2a-tck) | Python | 31 | 协议兼容性测试 |

**SDK 生态星级总计：** ~4,960 stars（不含主仓库）

### 社区讨论动态（最新）

- **a2a-rust：** 社区自发的 Rust SDK 实现
- **jamjet-a2a：** 另一个独立 Rust SDK
- **QHermes 26：** 后量子加密授权内核提案
- **awesome-a2a：** 社区资源汇总项目（26 条回复的讨论热度很高）

### 合作伙伴生态

官方文档声称 **170+ 合作伙伴组织**，横跨科技巨头、咨询公司和 AI 平台。

### 教育生态

- **DeepLearning.AI 短课程：** 与 Google Cloud 和 IBM Research 合作，由 Holt Skinner 等讲授
- 涵盖 Google ADK、LangGraph、BeeAI 等框架集成

---

## 官方文档洞察

### 文档站点：https://a2a-protocol.org

**核心结构：**
- **What is A2A / Key Concepts** — 入门介绍
- **Agent Discovery** — Agent Card 发现机制
- **Life of a Task** — 任务生命周期
- **Streaming / Asynchronous Operations** — 流式和异步操作
- **Enterprise Features** — 企业级特性
- **Extensions** — 扩展机制
- **Protocol Specification (v1.0)** — 完整协议规范

**技术架构要点：**
- 基于 **JSON-RPC 2.0 over HTTP(S)** 的标准化通信
- 通过 **Agent Card** 进行能力发现（类似服务发现）
- 支持三种交互模式：同步请求/响应、SSE 流式、异步推送通知
- Protocol Buffers 定义规范数据模型
- 三种传输绑定：JSON-RPC 2.0 over HTTP/SSE、gRPC over HTTP/2、HTTP/REST

**文档质量：** 高质量，结构清晰，有 Python Quickstart 8 步教程，版本化文档系统（MkDocs 构建）。

---

## 竞品清单

| 协议/项目 | 发起方 | 定位 | 区别 |
|-----------|--------|------|------|
| **MCP (Model Context Protocol)** | Anthropic | Agent-to-Tool | 解决 Agent 访问工具/数据源的标准化问题，与 A2A 互补而非竞争 |
| **OpenAI Agents SDK** | OpenAI | Agent 开发框架 | 偏向 OpenAI 生态的 Agent 构建工具，非开放互操作协议 |
| **LangGraph** | LangChain | Agent 编排框架 | 构建 Agent 工作流的框架，A2A 可与其集成 |
| **CrewAI** | CrewAI | 多 Agent 协作框架 | 预设角色的多 Agent 框架，A2A 提供更底层的通信标准 |
| **AutoGen** | Microsoft | 多 Agent 对话框架 | 侧重 Agent 间对话，A2A 更侧重互操作协议 |
| **BeeAI** | IBM | Agent 运行平台 | 已与 A2A 集成的 Agent 平台 |

**关键定位差异：** A2A 不是框架或工具，而是**协议标准**。它定义的是 Agent 之间"如何对话"的规范，而非"如何构建 Agent"。这使得它与上述框架更多是互补关系——各框架可以通过实现 A2A 协议来实现跨框架互操作。

**A2A vs MCP 关系：** 官方明确将 A2A 定位为 MCP 的补充。MCP 解决的是 Agent 如何发现和调用工具（Agent-to-Tool），A2A 解决的是 Agent 之间如何协作（Agent-to-Agent）。两者可以共存于同一系统中。

---

## 关键 Issue 信号

### 最高讨论热度（已关闭）

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| #1206 | feat(spec): Add last update time to Task | 58 | closed | 任务管理细节的高度关注 |
| #1259 | fix(spec): Clarify versioning strategy | 47 | closed | 版本策略是核心争议点 |
| #1306 | feat(spec)!: support arrays/primitives in DataPart | 41 | closed | 数据模型扩展需求强烈 |
| #1298 | feat(spec): add file_with_text field to FilePart | 41 | closed | 文件处理能力完善 |
| #1309 | fix(spec): Clarify contextId behavior | 37 | closed | 上下文管理复杂性 |
| #831 | feat(spec): Add tasks/list method | 35 | closed | 任务列表和分页需求 |
| #1160 | docs(spec): Large refactor of specification | 27 | closed | 规范重构（传输层分离） |

### 最高讨论热度（开放中）

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| #642 | feat(schema): support open agent discovery via API Catalog | 17 | open | Agent 发现机制仍在演进 |
| #1077 | [Proposal]: Versioning & Release Strategy | 16 | open | 版本策略仍未完全确定 |
| #1029 | [Feat]: Support publish/subscribe for async communications | 15 | open | pub/sub 模式需求强烈 |
| #1079 | feat: Unique identifier for an agent in Agent Card | 13 | open | Agent 身份标识尚未统一 |
| #1455 | feat: Agent-Mesh Trust Layer - Cryptographic Identity | 15 | closed | 安全信任层提案 |
| #1549 | feat!: Proposal for bidirectional streaming over gRPC | 2 | open | gRPC 双向流式提案 |

**Issue 信号解读：**
1. **版本策略争议大** — #1259（47评论）和 #1077（16评论，仍开放），说明社区对协议演进节奏存在分歧
2. **数据模型扩展活跃** — DataPart、FilePart 的扩展讨论激烈，说明实际使用中遇到了表达力不足的问题
3. **安全/身份是下一个焦点** — Agent 身份验证（#1079）、加密信任层（#1455）、授权审计（#1583）等安全相关提案密集出现
4. **传输层多样化** — gRPC 双向流（#1549）、pub/sub（#1029）说明 HTTP/SSE 不能满足所有场景

---

## 知识入口

| 来源 | 链接 | 说明 |
|------|------|------|
| 官方文档 | https://a2a-protocol.org | 最权威的协议文档、教程和规范 |
| DeepWiki | https://deepwiki.com/a2aproject/A2A | AI 生成的全面技术解读，涵盖协议架构、SDK、基础设施 |
| GitHub Discussions | https://github.com/a2aproject/A2A/discussions | 社区提案和 RFC 讨论 |
| DeepLearning.AI 课程 | https://goo.gle/dlai-a2a | 与 Google Cloud / IBM Research 合作的短期课程 |
| Code Wiki (Google) | https://codewiki.google/github.com/a2aproject/a2a | Google 的代码百科入口 |
| 协议规范 | https://a2a-protocol.org/latest/specification/ | 完整技术规范 |
| 多语言 README | openaitx.github.io 支持 20+ 语言翻译 | 国际化覆盖面广 |

---

## 项目展示素材

### 一句话定位
> Agent2Agent (A2A) Protocol — 由 Google 发起、Linux Foundation 托管的开放协议，让不同框架构建的 AI Agent 能够互相发现、协商和协作，无需暴露内部状态。

### 核心卖点（来自 README）
1. **发现能力** — Agent 通过 Agent Card 互相发现对方的能力
2. **协商交互** — 支持文本、表单、多媒体等多种交互模态协商
3. **安全协作** — 支持长时间运行任务的安全协作
4. **保持不透明** — Agent 无需暴露内部状态、记忆或工具

### 技术标签
`JSON-RPC 2.0` | `HTTP(S)` | `SSE` | `gRPC` | `Agent Card` | `Protocol Buffers` | `Apache 2.0`

### 数据亮点
- 22,700+ Stars，2,300+ Forks
- 5 个官方 SDK（Python/JS/Java/Go/.NET）+ 社区 Rust SDK
- 170+ 合作伙伴组织
- v1.0.0 于 2026-03-12 正式发布
- DeepLearning.AI 官方合作课程

---

## 快速判断

### 综合评级：A（行业标准级协议）

| 维度 | 评分 | 说明 |
|------|------|------|
| 影响力 | ★★★★★ | 22K+ stars，Google 背书 + Linux Foundation 托管，行业认可度极高 |
| 活跃度 | ★★★★☆ | v1.0.0 刚发布，近期提交以文档和规范维护为主，节奏稳定但非高频 |
| 生态完整度 | ★★★★★ | 5 语言官方 SDK + 社区 SDK + 示例 + 验证工具 + 教育课程，生态非常完整 |
| 社区健康度 | ★★★★☆ | 87/100 社区评分，讨论活跃，但核心贡献者高度集中于 Google 员工 |
| 技术成熟度 | ★★★★☆ | v1.0.0 标志着协议稳定，但安全/身份/高级传输仍在演进中 |
| 商业潜力 | ★★★★★ | 作为 Agent 互操作的事实标准候选，企业采纳潜力巨大 |

### 关键洞察

1. **协议而非产品：** A2A 的价值不在代码量，而在于它定义的标准。类似于 HTTP 或 gRPC 的定位——协议本身轻量，但影响力巨大。

2. **Google 主导风险：** 虽然已捐赠给 Linux Foundation，但核心贡献者仍以 Google 员工为主（holtskinner 占 40% 提交）。这既是优势（大厂推动力强），也是风险（如果 Google 战略调整，项目活力可能受影响）。

3. **v1.0 是关键节点：** 2026-03-12 发布 v1.0.0，标志着协议从"提案"进入"标准"阶段。后续关注点将转向：安全增强（身份/授权）、传输层扩展（gRPC 双向流）、Agent 发现进化。

4. **与 MCP 的关系是最大叙事：** 社区高度关注 A2A 与 MCP 的关系。官方明确"互补不竞争"的定位——MCP 是 Agent-to-Tool，A2A 是 Agent-to-Agent。`a2a-mcp` topic 的存在也说明两者在实践中需要桥接。

5. **Star 增长放缓但稳定：** 初期爆发后增速放缓是正常现象，v1.0 发布可能带来第二波增长。22K stars 对于协议规范类项目而言已经非常优秀。

6. **适用场景：** 需要构建多 Agent 协作系统、跨框架 Agent 互操作、企业级 Agent 编排的开发者/团队。
