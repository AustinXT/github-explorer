# Dexter 内容分析笔记

## 架构分析

### Agent 循环（src/agent/agent.ts）

核心 Agent 类实现了迭代式工具调用循环：
1. 创建 Agent 时注册所有工具和系统提示词
2. `run()` 方法是异步生成器，yield 事件流供 UI 消费
3. 每次迭代调用 LLM，判断是否需要工具调用
4. 有工具调用则执行工具，将结果写入 Scratchpad
5. 无工具调用则输出最终答案
6. 最大迭代次数默认 10
7. 上下文溢出时采用"Anthropic 风格"管理：清除最旧的工具结果

### Scratchpad（src/agent/scratchpad.ts）

最复杂的文件（465行），核心设计：
- JSONL 格式的 append-only 日志，持久化到 `.dexter/scratchpad/`
- 工具调用限制机制（软限制，默认每工具每查询 3 次）
- Jaccard 相似度检测避免重复查询
- 上下文清理仅在内存中标记，不修改 JSONL 文件

### 元工具模式（Meta-Tool Pattern）

**这是 Dexter 最有价值的架构创新。**

`get_financials` 和 `get_market_data` 不是直接的 API 封装，而是"元工具"：
1. 接收自然语言查询
2. 内部调用 LLM 做路由决策（用 LLM 选择子工具 + 参数）
3. 并行执行多个子工具
4. 合并结果返回

这样上层 Agent 只需调用一次 `get_financials("Compare AAPL vs MSFT revenue")`，
内部会自动路由到正确的 API 并合并数据。

### Provider 注册中心（src/providers.ts）

极其简洁的设计（95 行），前缀路由：
- `claude-` → Anthropic
- `gemini-` → Google
- `grok-` → xAI
- `kimi-` → Moonshot
- `deepseek-` → DeepSeek
- `openrouter:` → OpenRouter
- `ollama:` → Ollama
- 无前缀 → OpenAI（默认）

每个 provider 定义 fast model 变种，用于轻量任务。

### 技能系统（Skills）

SKILL.md 文件 = YAML frontmatter + Markdown 指令体
Agent 通过 `skill` 工具加载技能指令，按步骤执行复杂工作流。

现有技能：
- DCF 估值（详细的 8 步工作流 checklist）
- X 研究

### 记忆系统（Memory）

完整的持久记忆实现：
- SQLite 数据库存储文本块 + 向量嵌入
- 混合搜索：向量相似度（70%权重）+ 关键词（30%权重）
- Embedding providers: OpenAI > Gemini > Ollama（自动降级）
- 长期记忆（MEMORY.md）+ 每日笔记（YYYY-MM-DD.md）
- 上下文压缩前自动 flush 重要记忆到磁盘

### WhatsApp 网关

完整的 WhatsApp 集成：
- 基于 @whiskeysockets/baileys 的 WhatsApp Web 协议
- 支持个人对话和群组（@提及激活）
- 会话管理、访问控制、群组历史缓冲
- 心跳机制定期执行检查任务

### SOUL.md — 人格系统

独特的设计：用 Markdown 文档定义 Agent 人格。
Dexter 自比"卡通里建跨维度传送门的小孩"，价值观基于 Buffett/Munger 投资哲学。
用户可在 `.dexter/SOUL.md` 覆盖默认人格。

## 工程质量评估

### 优点
- 代码简洁（16,782 行实现完整金融 Agent）
- 模块化清晰（tools/agent/memory/gateway 分离）
- 元工具模式优雅解决了工具选择复杂性
- 事件驱动架构（AsyncGenerator yield events）

### 不足
- 测试覆盖极低（6 个测试文件，集中在 gateway 和 utils）
- 无 LICENSE 文件（虽然 README 声称 MIT）
- 无错误边界/fallback 的结构化处理
- 对 Financial Datasets API 的单一数据源依赖
