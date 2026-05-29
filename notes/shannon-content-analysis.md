# Shannon 内容分析笔记

## 项目架构

### 目录结构

```
shannon/
├── src/                          # 核心源码 (TypeScript)
│   ├── ai/                       # Claude AI 集成层
│   │   ├── claude-executor.ts    # SDK 调用、消息流、进度追踪
│   │   ├── message-handlers.ts   # 消息分发与处理
│   │   ├── models.ts             # 模型选择（small/medium/large tier）
│   │   ├── output-formatters.ts  # 输出格式化
│   │   ├── progress-manager.ts   # 进度管理
│   │   ├── router-utils.ts       # 路由工具
│   │   ├── audit-logger.ts       # 审计日志
│   │   └── types.ts
│   ├── audit/                    # 审计系统
│   │   ├── audit-session.ts      # 会话管理
│   │   ├── logger.ts             # 日志记录
│   │   ├── log-stream.ts         # 日志流
│   │   ├── metrics-tracker.ts    # 指标追踪
│   │   └── workflow-logger.ts    # 工作流日志
│   ├── services/                 # 业务逻辑层（Temporal 无关）
│   │   ├── agent-execution.ts    # Agent 生命周期管理
│   │   ├── config-loader.ts      # 配置加载
│   │   ├── container.ts          # DI 容器
│   │   ├── error-handling.ts     # 错误处理（PentestError）
│   │   ├── exploitation-checker.ts # 利用检查
│   │   ├── git-manager.ts        # Git 检查点管理
│   │   ├── preflight.ts          # 预检验证
│   │   ├── prompt-manager.ts     # 提示管理
│   │   ├── queue-validation.ts   # 队列验证
│   │   └── reporting.ts          # 报告生成
│   ├── temporal/                 # Temporal 编排层
│   │   ├── workflows.ts          # 主工作流（pentestPipelineWorkflow）
│   │   ├── activities.ts         # 活动包装器
│   │   ├── worker.ts             # Worker 入口
│   │   ├── client.ts             # CLI 客户端
│   │   ├── shared.ts             # 共享类型
│   │   ├── workspaces.ts         # 工作空间管理
│   │   └── summary-mapper.ts     # 摘要映射
│   ├── types/                    # 类型定义
│   ├── utils/                    # 工具函数
│   ├── session-manager.ts        # Agent 定义注册表
│   ├── config-parser.ts          # YAML 配置解析
│   └── splash-screen.ts          # 启动画面
├── mcp-server/                   # MCP 工具服务器
│   └── src/
│       ├── tools/                # save-deliverable, generate-totp
│       ├── types/
│       └── validation/
├── prompts/                      # 提示模板
│   ├── pre-recon-code.txt        # 预侦察
│   ├── recon.txt                 # 侦察
│   ├── vuln-{injection,xss,auth,ssrf,authz}.txt  # 漏洞分析
│   ├── exploit-{injection,xss,auth,ssrf,authz}.txt # 利用
│   ├── report-executive.txt      # 报告
│   ├── shared/                   # 共享 partial
│   └── pipeline-testing/         # 测试用最小提示
├── configs/                      # 配置文件
│   ├── config-schema.json        # JSON Schema 验证
│   ├── example-config.yaml       # 示例配置
│   └── router-config.json        # 路由配置
├── sample-reports/               # 示例渗透报告
├── xben-benchmark-results/       # XBOW 基准测试结果
├── shannon                       # CLI 入口（Bash 脚本）
├── docker-compose.yml            # Docker 编排
├── Dockerfile                    # Docker 构建
└── package.json                  # Node.js 依赖
```

## 五阶段渗透测试管线

Shannon 的核心是一个五阶段管线，由 Temporal 工作流编排：

1. **Pre-Recon**（预侦察）— 源代码分析 + 外部扫描（nmap, subfinder, whatweb）
2. **Recon**（侦察）— 攻击面映射
3. **Vulnerability Analysis**（漏洞分析，5 个并行 Agent）— Injection, XSS, Auth, SSRF, Authz
4. **Exploitation**（利用，5 个并行 Agent，条件执行）— 验证可利用的漏洞
5. **Reporting**（报告）— 执行摘要和证据汇总

### Agent 定义

共 13 个 Agent，定义在 session-manager.ts 的 AGENTS 注册表中：
- pre-recon, recon（串行）
- injection-vuln, xss-vuln, auth-vuln, ssrf-vuln, authz-vuln（并行）
- injection-exploit, xss-exploit, auth-exploit, ssrf-exploit, authz-exploit（条件并行）
- report（串行）

每个 Agent 有：name, displayName, prerequisites, promptTemplate, deliverableFilename, modelTier

## 技术栈

- **运行时**: Node.js (TypeScript, ESM)
- **AI**: @anthropic-ai/claude-agent-sdk（Claude Agent SDK）
- **编排**: Temporal（持久化工作流、崩溃恢复、自动重试）
- **浏览器自动化**: Playwright MCP Server（5 个并行实例）
- **配置验证**: AJV (JSON Schema)
- **容器化**: Docker Compose（Temporal + Worker + 可选 Router）
- **CLI 工具**: zx, chalk, figlet, boxen, gradient-string

## 关键设计决策

1. **白盒设计**：需要访问源代码，而非黑盒扫描
2. **"证明即利用"**：仅报告可被实际利用的漏洞，消除误报
3. **Claude Agent SDK**：直接使用 Anthropic SDK 而非 LangChain 等框架
4. **Temporal 编排**：持久化工作流保证崩溃恢复，queryable state 支持进度查询
5. **服务边界隔离**：src/services/ 不依赖 Temporal，纯业务逻辑
6. **安全隔离**：Playwright MCP 子进程不继承 API key 等敏感环境变量
7. **Result<T,E> 模式**：使用函数式 Result 类型替代 try/catch 的错误传播
8. **Git 检查点**：每个 Agent 执行前创建 git checkpoint，失败时回滚

## 配置系统

支持 YAML 配置文件，包含：
- **认证设置**：表单登录、SSO、TOTP 2FA
- **规则**：avoid（排除路径/子域）、focus（重点测试路径）
- **管线配置**：重试预设、最大并发数

## MCP 服务器

提供两个自定义工具：
1. **save_deliverable** — 保存 Agent 产出物到 deliverables/ 目录
2. **generate-totp** — 生成 TOTP 验证码（支持 MFA 登录测试）
