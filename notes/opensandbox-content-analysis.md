# OpenSandbox 内容分析笔记

## 项目结构
```
OpenSandbox/
├── sdks/                    # 多语言 SDK
│   ├── sandbox/             # 基础沙箱 SDK
│   │   ├── python/
│   │   ├── kotlin/ (Java/Kotlin)
│   │   ├── javascript/ (TypeScript)
│   │   └── csharp/ (.NET)
│   ├── code-interpreter/    # 代码解释器 SDK
│   │   ├── python/
│   │   ├── kotlin/
│   │   ├── javascript/
│   │   └── csharp/
│   └── mcp/                 # MCP SDK
│       └── sandbox/
├── specs/                   # OpenAPI 规范
│   ├── sandbox-lifecycle.yml
│   ├── execd-api.yaml
│   └── egress-api.yaml
├── server/                  # Python FastAPI 生命周期服务器
│   └── src/
│       ├── main.py
│       ├── config.py
│       ├── cli.py
│       ├── api/
│       ├── middleware/
│       └── services/
│           ├── docker.py
│           ├── k8s/
│           ├── sandbox_service.py
│           ├── factory.py
│           └── ...
├── kubernetes/              # Kubernetes 运行时
│   ├── apis/                # CRD 定义
│   ├── charts/              # Helm Charts
│   ├── cmd/                 # 控制器/任务执行器
│   ├── internal/            # 内部实现
│   ├── pkg/                 # 公共包
│   └── test/                # 测试
├── components/              # 核心组件
│   ├── execd/               # Go 执行守护进程
│   ├── ingress/             # 入口代理
│   ├── egress/              # 出口控制
│   └── internal/            # 内部共享库
├── sandboxes/               # 沙箱运行时实现
│   └── code-interpreter/    # 代码解释器沙箱
├── examples/                # 20 个示例
│   ├── claude-code/         # Claude Code 集成
│   ├── gemini-cli/          # Gemini CLI 集成
│   ├── codex-cli/           # OpenAI Codex CLI
│   ├── kimi-cli/            # Kimi CLI 集成
│   ├── langgraph/           # LangGraph 工作流
│   ├── google-adk/          # Google ADK
│   ├── chrome/              # 浏览器自动化
│   ├── playwright/          # Playwright 测试
│   ├── desktop/             # 桌面环境
│   ├── vscode/              # VS Code Web
│   ├── rl-training/         # RL 训练
│   └── ...
├── oseps/                   # 增强提案 (10 个)
├── docs/                    # 文档
├── tests/                   # E2E 测试
└── scripts/                 # 脚本
```

## 架构设计（四层）
1. **SDK 层** - 多语言客户端库 (Python/Java/Kotlin/TypeScript/C#)
2. **Specs 层** - OpenAPI 规范定义协议契约
3. **Runtime 层** - FastAPI 服务器管理沙箱生命周期（Docker/Kubernetes）
4. **Sandbox 实例层** - 运行中的容器 + 注入的 execd 守护进程

## 核心技术栈
- **服务器**: Python + FastAPI + uvicorn
- **执行守护进程 (execd)**: Go + Beego 框架 + Jupyter 集成
- **Kubernetes 控制器**: Go + controller-runtime
- **入口代理**: Go
- **出口控制**: Go + nftables
- **代码解释器**: Jupyter 内核协议
- **SDK**: Python / Java / Kotlin / TypeScript / C#

## 关键设计特点
1. **协议优先**: 所有交互通过 OpenAPI 规范定义
2. **执行守护进程注入**: execd 在运行时动态注入到容器中，无需修改用户镜像
3. **多运行时**: Docker（生产就绪）和 Kubernetes（BatchSandbox CRD）
4. **安全隔离**: 支持 gVisor、Kata Containers、Firecracker
5. **网络策略**: 统一入口网关 + 按沙箱出口控制
6. **OSEP 提案机制**: 类似 PEP/KEP 的增强提案流程

## OSEP 增强提案列表
- 0001: FQDN 出口控制
- 0002: kubernetes-sigs/agent-sandbox 支持
- 0003: 卷和卷绑定支持
- 0004: 安全容器运行时
- 0005: 客户端沙箱池
- 0006: 开发者控制台
- 0007: 快速沙箱运行时支持
- 0008: 暂停/恢复/根文件系统快照
- 0009: 入口访问时自动续期沙箱
- 0010: OpenTelemetry 可观测性
