# DeerFlow 内容分析笔记

## 项目定位
DeerFlow (Deep Exploration and Efficient Research Flow) 是字节跳动开源的"超级 Agent 系统框架"（Super Agent Harness），从最初的深度研究框架 (Deep Research) 进化而来，能够编排子 Agent、记忆和沙箱来完成几乎所有任务。

## 架构概览

### 整体结构
```
deer-flow/
├── backend/           # Python 后端
│   ├── app/           # FastAPI 应用
│   │   ├── channels/  # IM 通道（Telegram, Slack, Feishu）
│   │   └── gateway/   # HTTP Gateway API（REST 路由）
│   ├── packages/
│   │   └── harness/   # 核心引擎包 (deerflow-harness)
│   │       └── deerflow/
│   │           ├── agents/        # Agent 系统
│   │           ├── community/     # 社区集成
│   │           ├── config/        # 配置管理
│   │           ├── mcp/           # MCP 协议支持
│   │           ├── models/        # 模型工厂
│   │           ├── reflection/    # 反思机制
│   │           ├── sandbox/       # 沙箱执行
│   │           ├── skills/        # 技能系统
│   │           ├── subagents/     # 子 Agent
│   │           ├── tools/         # 工具系统
│   │           └── utils/         # 工具函数
│   └── tests/         # 45+ 测试文件
├── frontend/          # Next.js 前端
│   └── src/
│       ├── app/       # 页面路由
│       ├── components/# UI 组件
│       ├── core/      # 核心逻辑
│       └── hooks/     # React Hooks
├── skills/            # 技能模块
│   └── public/        # 内置技能
├── docker/            # Docker 配置
└── scripts/           # 启动/部署脚本
```

### 技术栈
**后端**：
- Python 3.12+, FastAPI, LangGraph, LangChain
- 沙箱执行（Docker / Kubernetes）
- uv 包管理
- 支持多种 LLM API（OpenAI 兼容）

**前端**：
- Node.js 22+, Next.js, TypeScript, React
- Tailwind CSS, CodeMirror
- pnpm 包管理

## 核心特性

### 1. Skills 技能系统
- 技能是 Markdown 文件定义的结构化能力模块
- 按需加载（progressive loading），节省 context window
- 支持自定义技能和 .skill 归档安装
- 内置技能：
  - deep-research（深度研究）
  - chart-visualization（图表可视化，支持 30+ 图表类型）
  - podcast-generation（播客生成）
  - ppt-generation（PPT 生成）
  - image-generation（图片生成）
  - video-generation（视频生成）
  - data-analysis（数据分析）
  - frontend-design（前端设计）
  - consulting-analysis（咨询分析）
  - skill-creator（技能创建器）
  - claude-to-deerflow（Claude Code 集成）
  - github-deep-research（GitHub 深度研究）
  - find-skills（技能发现和安装）
  - bootstrap（初始化引导）

### 2. Agent 架构
- Lead Agent：主控 Agent，负责任务分析和调度
- Sub-Agents：子 Agent，并行执行分解后的任务
  - bash_agent（命令执行）
  - general_purpose（通用任务）
- Middlewares 中间件：
  - SummarizationMiddleware（上下文摘要）
  - MemoryMiddleware（记忆管理）
  - LoopDetectionMiddleware（循环检测）
  - ClarificationMiddleware（澄清确认）
  - TitleMiddleware（标题生成）
  - TodoMiddleware（待办管理）
  - ViewImageMiddleware（图片查看）
  - SubagentLimitMiddleware（子 Agent 限制）
  - ToolErrorHandlingMiddleware（工具错误处理）
  - DeferredToolFilterMiddleware（延迟工具过滤）

### 3. 沙箱系统
- 三种模式：本地执行、Docker 容器、Kubernetes Pod
- 隔离的文件系统：uploads/workspace/outputs
- 技能脚本在沙箱内执行

### 4. 长期记忆
- 跨会话持久化记忆
- 用户画像、偏好、知识积累
- 去重机制防止重复条目

### 5. 上下文工程
- 子 Agent 上下文隔离
- 完成子任务自动摘要
- 中间结果卸载到文件系统

### 6. MCP 协议支持
- 可配置 MCP 服务器
- 支持 HTTP/SSE 传输
- OAuth 令牌流支持

### 7. IM 通道集成
- Telegram（长轮询）
- Slack（Socket Mode）
- 飞书 / Lark（WebSocket）

### 8. Gateway API
完整的 REST API 路由：
- agents（Agent 管理）
- artifacts（工件管理）
- channels（通道管理）
- mcp（MCP 服务管理）
- memory（记忆管理）
- models（模型管理）
- skills（技能管理）
- suggestions（建议生成）
- uploads（文件上传）

### 9. 嵌入式 Python 客户端
- DeerFlowClient 提供编程接口
- 支持同步 chat 和流式 stream
- 无需启动 HTTP 服务

## 工程质量
- 45+ 测试文件覆盖各模块
- Makefile 统一开发工作流
- Docker 支持开发和生产部署
- 配置模板和自动配置升级
- CONTRIBUTING.md 贡献指南
- SECURITY.md 安全政策
- 多语言 README（英文、中文、日文）

## 代码风格
- Python 使用 Pydantic 做配置验证
- TypeScript 前端组件化架构
- 模块化设计，各功能独立包
