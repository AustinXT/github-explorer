# Shannon 深度分析报告

> GitHub: https://github.com/KeygraphHQ/shannon

## 一句话总结

Keygraph 团队打造的自治式白盒 AI 渗透测试框架，通过 Claude Agent SDK + Temporal 工作流编排实现五阶段渗透管线，以"无法利用就不报告"的严格标准消除误报，在 XBOW 基准测试中以 96.15% 成功率刷新纪录。

## 值得关注的理由

1. **"证明即利用"的安全哲学**：区别于传统 SAST/DAST 工具的"可能有风险"式报告，Shannon 只报告带有可复制 PoC 的已验证漏洞——这一设计哲学从根本上解决了安全工具的误报问题，具有行业变革意义
2. **AI Agent 多阶段编排的工程范例**：13 个 AI Agent 通过 Temporal 持久化工作流协调，5 路并行管线、条件执行、崩溃恢复、Git 检查点回滚——这是目前开源社区中最成熟的 AI Agent 工作流编排实现之一
3. **极致的成本效率颠覆**：将传统 $10,000+、数周的人工渗透测试压缩到 ~$16 API 成本、1.5 小时自动完成，且覆盖率不输人工，这是 AI 在安全领域实现 100x 成本改进的实证

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/KeygraphHQ/shannon |
| Star / Fork | 34,176 / 3,446 |
| 代码行数 | 6,755 行 TypeScript 核心代码（总 78,911 含 Markdown 基准结果） |
| 项目年龄 | 5.5 个月（2025-10-03 至今） |
| 开发阶段 | 活跃开发（月均 35+ 提交，2 月达峰值 54 次） |
| 贡献模式 | 团队驱动（6 名核心贡献者，均为 Keygraph 员工） |
| 热度定位 | 爆款项目（5 个月 34k stars，安全类开源项目中增速罕见） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[基准测试] |

## 作者视角：为什么存在这个项目

### 创始团队背景

Keygraph 是一家美国安全与合规平台公司，2024 年 9 月在 GitHub 注册。核心贡献者 ajmallesh（Arjun Malleswaran）贡献了约 59% 的提交。团队成员均以 `-keygraph` 后缀命名 GitHub 账号，表明这是一个公司驱动的有组织开发。6 个公开仓库，319 个 GitHub 粉丝——这是一个将开源作为商业策略核心的初创公司。

### 问题判断

Keygraph 团队识别到了应用安全领域的一个结构性矛盾：**现代团队每天部署代码，但渗透测试每年只做一两次**。这创造了一个 364 天的安全盲区。现有解决方案的不足在于：

- **传统渗透测试**：昂贵（$10,000+）、缓慢（数周排期）、低频（年度）
- **SAST/DAST 工具**：误报率高，开发者疲于应对警报而非真实威胁
- **黑盒 AI 安全工具**：不理解代码逻辑，无法发现业务逻辑漏洞

Shannon 选择了白盒路线（需要源代码访问），这是一个有意的权衡——放弃黑盒场景的通用性，换取对代码逻辑的深度理解能力。

### 解法哲学

Shannon 的核心设计选择体现了清晰的工程价值观：

- **可利用性 > 可能性**：只有成功执行了 exploit 的漏洞才会出现在报告中——消除误报
- **深度分析 > 广度扫描**：通过源代码分析引导动态测试，而非盲扫
- **自治性 > 交互性**：单条命令启动，全程无需人工干预（包括 2FA/TOTP 登录）
- **可恢复性 > 一次性**：Temporal 持久化工作流保证崩溃后自动恢复
- **安全隔离**：Playwright 子进程不继承 API key，环境变量使用显式白名单

他们明确**不做**的事：黑盒扫描、不可利用漏洞的报告、与传统 SAST 工具竞争（Shannon Pro 会做这些）。

### 战略意图

Shannon Lite（本仓库）是 Keygraph 商业战略的开源入口。其商业版 Shannon Pro 在开源版基础上增加了：

- **SAST 层**：Code Property Graph、数据流分析、SCA 可达性分析、密钥检测
- **静态-动态关联**：静态发现的漏洞自动流入动态利用管线验证
- **CI/CD 集成**和自托管部署模型

这是经典的 "Open Core" 商业模式：开源版建立社区信任和技术品牌，商业版满足企业需求。AGPL-3.0 许可证的选择也印证了这一策略——它阻止竞争对手将代码闭源使用，同时不影响终端用户。

## 核心价值提炼

### 创新之处

1. **五阶段并行渗透管线** — 新颖度 5/5 | 实用性 5/5 | 可迁移性 4/5
   13 个 AI Agent 组成的五阶段管线：Pre-Recon → Recon → 5 路并行漏洞分析 → 5 路条件并行利用 → 报告。每一对 vuln/exploit Agent 构成独立管线，exploit 在自己的 vuln 完成后立即启动，无需等待其他漏洞类型。这种 "pipelined parallel" 架构将端到端时间压缩到最小，同时保持逻辑依赖的正确性。

2. **Temporal 持久化 Agent 编排** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5
   利用 Temporal 的持久化工作流机制实现 AI Agent 的崩溃恢复、自动重试（含 spending cap 检测和计费恢复）、可查询进度状态、命名工作空间恢复。生产环境支持最多 50 次重试、5-30 分钟退避间隔。这是 Temporal 在 AI Agent 编排中的最佳实践范例。

3. **Git 检查点回滚机制** — 新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5
   每个 Agent 执行前创建 git checkpoint，失败时通过 `rollbackGitWorkspace` 回滚到干净状态。成功时 `commitGitSuccess` 保存交付物。这确保了并行 Agent 之间的文件系统隔离——每个 Agent 读写同一 repo 但互不干扰。

4. **Playwright MCP 安全隔离** — 新颖度 4/5 | 实用性 4/5 | 可迁移性 3/5
   5 个 Playwright MCP Server 实例分别分配给不同 Agent，每个使用独立的 user-data-dir。关键设计：Playwright 子进程不继承父进程的环境变量，使用显式白名单（PATH, HOME 等），防止 API key 泄露到浏览器进程。

5. **Spending Cap 防御性检测** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   多层防御检测 API 配额耗尽：SDK 层检测、Agent 完成后检测（低 turn count + 零成本 + 结果模式匹配）、Temporal 活动层分类。这是使用商业 LLM API 构建生产系统时的必备模式。

6. **Result<T,E> 函数式错误传播** — 新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5
   使用 Rust 风格的 Result 类型替代 try/catch，结合 ErrorCode 枚举和 PentestError 分类（可重试/不可重试）。Temporal 活动层通过 `executeOrThrow` 方法转换为异常，保持服务层和编排层的边界清晰。

### 可复用的模式与技巧

1. **Agent 注册表模式**（session-manager.ts）：所有 Agent 的元数据（名称、前置条件、提示模板、交付物文件名、模型等级）集中声明在一个 `Record<AgentName, AgentDefinition>` 中。新增 Agent 只需在注册表中添加条目，工作流自动适配。

2. **服务层/编排层分离**：`src/services/` 包含纯业务逻辑，不导入任何 Temporal 类型；`src/temporal/activities.ts` 是薄包装层，只做心跳和错误分类。这使得核心逻辑可独立测试，不依赖 Temporal 基础设施。

3. **提示模板系统**（prompt-manager.ts）：使用变量替换（`{{TARGET_URL}}`、`{{CONFIG_CONTEXT}}`）和共享 partial（`prompts/shared/`），支持生产提示和测试最小提示的双轨切换。

4. **条件执行管线**：每对 vuln/exploit Agent 之间有 `checkExploitationQueue` 检查——如果漏洞分析未发现可利用项，直接跳过 exploit 阶段，节省 API 成本。

5. **DI 容器 + 审计会话分离**：`container.ts` 提供每工作流的 DI，但 AuditSession 故意排除在外——因为并行 Agent 需要各自独立的审计上下文，共享会导致状态混乱。

## 架构深度解析

### 核心数据流

```
用户命令
  → shannon CLI (Bash)
    → Docker Compose (Temporal + Worker)
      → Temporal Client (client.ts)
        → pentestPipelineWorkflow (workflows.ts)
          → AgentExecutionService.execute (services/)
            → runClaudePrompt (ai/claude-executor.ts)
              → Claude Agent SDK (query API)
                → MCP Servers: shannon-helper + playwright-agent
                  → 浏览器自动化 / 工具调用
```

### Agent 执行生命周期

AgentExecutionService.execute 方法包含 9 个步骤：
1. 加载配置（可选 YAML）
2. 加载提示模板（变量替换、partial 注入）
3. 创建 Git 检查点
4. 启动审计日志
5. 调用 Claude SDK（maxTurns: 10,000, bypassPermissions）
6. Spending cap 检查
7. 处理执行失败（回滚 + 审计）
8. 验证输出（检查交付物文件是否存在）
9. 成功时 git commit + 记录指标

### 模型配置

支持三层模型配置（small/medium/large），可通过环境变量覆盖：
- Pre-Recon 使用 large tier（深度代码分析）
- Report 使用 small tier（文本汇总）
- 其他 Agent 使用 medium tier（默认）

支持 Anthropic 直接 API、Bedrock、Vertex AI、自定义 Base URL、OAuth Token 多种认证方式。

### Docker 架构

```
┌─────────────┐  ┌───────────────┐  ┌──────────────┐
│  Temporal    │  │  Worker       │  │  Router      │
│  (编排引擎)  │←→│  (Agent执行)   │  │  (可选,多模型)│
│  Port 7233  │  │  + Playwright  │  │  Port 3456   │
│  Web UI     │  │  MCP Servers   │  │              │
│  Port 8233  │  │  shm: 2GB     │  │              │
└─────────────┘  └───────────────┘  └──────────────┘
```

## 项目健康度评估

### 优势

- **高代码质量**：TypeScript 严格模式（exactOptionalPropertyTypes），清晰的分层架构，详尽的 CLAUDE.md 开发指南
- **优秀的文档**：README 35K+ 字，CLAUDE.md 覆盖架构/模式/故障排查，COVERAGE.md 提供 WSTG 测试清单对照
- **活跃开发**：5.5 个月 212 次提交，月均 38 次，无明显停滞期
- **基准验证**：XBOW 96.15% 成功率，3 份示例渗透报告（Juice Shop, Capital API, crAPI）

### 风险因素

- **项目年龄极短**：仅 5.5 个月历史，长期稳定性未经验证
- **纯公司团队**：6 名贡献者全部是 Keygraph 员工，无外部社区贡献
- **无正式发布**：没有 Git 标签或 GitHub Release，版本管理不明确
- **强依赖单一 AI 提供商**：核心依赖 Anthropic Claude Agent SDK，虽然通过 Router 支持多模型，但 SDK 绑定较深
- **AGPL 限制**：AGPL-3.0 许可证可能阻碍某些商业集成场景

### 社区信号

- **Stars 增长异常快**：5.5 个月 34k+ stars，这在安全工具类项目中极为罕见
- **Issue 活跃度适中**：10 个历史 issue，23 个开放中，评论密度表明团队响应积极
- **媒体关注度高**：Medium 多篇技术分析、CyberSecurityNews/GBHackers 报道、教程文章
- **Discord 社区**：有 Discord 频道，表明在建设社区

## 关键洞察

### 1. AI Agent 编排的最佳实践教材

Shannon 的代码库是目前开源社区中最完整的 AI Agent 工作流编排实现之一。其 Temporal 集成展示了如何解决 AI Agent 系统的核心工程挑战：崩溃恢复、并行执行、条件分支、成本控制、进度可观测性。任何构建多 Agent 系统的工程师都应研究其 `workflows.ts` 和 `agent-execution.ts`。

### 2. "Open Core" 安全产品的标准样本

Shannon Lite (AGPL) → Shannon Pro (商业) 的分层策略执行清晰：开源版足够强大以建立技术信誉（96% XBOW 成功率），但缺少企业级功能（SAST、CI/CD 集成、合规报告），自然引导企业客户升级。AGPL 许可证确保竞争对手无法闭源使用。

### 3. Anthropic 生态系统的深度押注

Shannon 是 Claude Agent SDK 的重度用户——`maxTurns: 10,000`、`bypassPermissions` 模式、Playwright MCP 集成。这使其成为 Anthropic Agent 生态的标杆案例，但也意味着深度绑定。Router 机制（支持 OpenAI/OpenRouter）只是补充路径，核心能力仍依赖 Claude 的代码分析和工具使用能力。

### 4. 安全行业的"AI 颠覆时刻"

$10,000 → $16 的成本压缩是典型的 AI 颠覆叙事，但 Shannon 用 XBOW 基准数据做了实证。96.15% 的白盒成功率 vs 传统黑盒 ~85% 表明，AI + 源代码访问的组合可能优于人工黑盒测试。这对年收入数十亿美元的渗透测试行业构成直接挑战。
