# promptfoo 深度分析报告

> GitHub: https://github.com/promptfoo/promptfoo

## 一句话总结

被 OpenAI 收购的 LLM 评估与红队安全测试一体化工具——用声明式 YAML 配置实现 90+ LLM 提供商的自动化评估和 65+ 种安全攻击测试，填补了「评估 + 安全」交叉领域的空白。

## 值得关注的理由

1. **唯一同时覆盖评估 + 红队安全测试的开源工具**——竞品要么只做评估（DeepEval/RAGAS），要么只做漏洞扫描（Garak），promptfoo 将二者统一在同一声明式配置框架下
2. **已被 OpenAI 收购验证**——2026 年 3 月被收购，a16z 投资，Fortune 500 中 25% 企业客户，被 OpenAI 和 Anthropic 官方使用
3. **极高的工程化水准**——78 万行代码、409 个版本、37 个月持续迭代，自适应速率限制调度器和合规框架映射矩阵是可迁移的工程精华

## 项目展示

![prompt evaluation matrix - web viewer](https://raw.githubusercontent.com/promptfoo/promptfoo/main/site/static/img/claude-vs-gpt-example@2x.png)
多模型对比评估矩阵，核心使用场景

![promptfoo command line demo](https://www.promptfoo.dev/img/docs/self-grading.gif)
CLI 自动评分工作流

![gen ai red team dashboard](https://www.promptfoo.dev/img/redteam-dashboard@2x.jpg)
红队安全测试报告界面

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/promptfoo/promptfoo |
| Star / Fork | 19,575 / 1,679 |
| 代码行数 | 78 万行（TypeScript 52.6%, TSX 16.8%, JSON 8.7%） |
| 项目年龄 | 37 个月（2023-04 至今） |
| 开发阶段 | 高速成长期 — 日均 11.3 commit |
| 贡献模式 | 双核驱动（两位创始人合计 64%） + 284 位社区贡献者 |
| 热度定位 | 大众热门（被 OpenAI 收购后一周涨 5000 star） |
| 质量评级 | 代码 A- 文档 A+ 测试 A- |

## 作者视角：为什么存在这个项目

### 创始人背景

创始人 Ian Webster（typpo）曾任 Discord LLM 工程负责人，将 AI 产品扩展至 2 亿用户；更早任 Smile ID VP of Engineering & Head of ML。联合创始人 Michael D'Angelo（mldangelo）贡献 27.5% 的 commit。a16z 投资，2026 年 3 月被 OpenAI 收购，团队加入 OpenAI。

### 问题判断

Ian 在 Discord 面对 2 亿用户规模的 LLM 应用时，发现了两类核心痛点：
1. **评估困境**——提示词和模型选择依赖「直觉试错」，传统软件测试无法应对 LLM 输出的非确定性
2. **安全盲区**——LLM 应用上线前缺乏自动化红队攻击测试，安全漏洞只能靠人工发现

时机恰好：LLM 从实验走向生产的转折点（2023 年中），开发者急需系统化的质量保障工具。

### 解法哲学

1. **声明式优于命令式**——用 YAML 配置定义测试套件，而非编写测试代码，降低使用门槛
2. **本地优先**——所有评估 100% 本地运行，零隐私泄露风险，解决企业客户顾虑
3. **插件化扩展**——Provider、Assertion、Redteam Plugin 都通过注册机制扩展，核心框架保持稳定

### 战略意图

被 OpenAI 收购后的路径清晰：推动 LLM 评估标准化，红队测试民主化，通过合规框架映射（OWASP/NIST/EU AI Act）成为 AI 治理基础设施。同时作为多模型横向对比工具，间接展示模型竞争力。

## 核心价值提炼

### 创新之处

1. **评估 + 红队一体化框架**（新颖度 5/5）——同一套 Provider 和 Assertion 体系既用于评估也用于安全测试，竞品中绝无仅有
2. **合规框架自动映射**（新颖度 5/5）——内置 8 大 AI 安全标准到具体测试用例的映射矩阵，指定 `owasp:llm` 即可自动生成完整测试套件
3. **多轮攻击策略引擎**（新颖度 5/5）——31 种攻击策略，含学术算法（Crescendo/GOAT）、编码混淆（Base64/Leetspeak/Hex）、复合攻击（Iterative Tree/Meta/Best-of-N）
4. **自适应速率限制调度器**（新颖度 4/5）——从 API 响应头自动学习速率限制，动态调整并发度，限流减半、连续成功恢复

### 可复用的模式与技巧

1. **test/create 工厂链**——Provider 注册表用有序的 test/create 函数对实现动态路由，适用于任何插件系统
2. **Plugin-Grader 配对**——安全测试中「生成攻击」和「判定结果」分离，Plugin 产出 `TestCase[]`，Grader 输出 `GradingResult`
3. **自适应并发调度**——BACKOFF_FACTOR=0.5 限流减半，RECOVERY_FACTOR=1.5 连续 5 次成功后恢复，可独立使用
4. **合规框架映射矩阵**——将抽象安全标准映射到具体测试用例，支持嵌套结构（框架 → 风险域 → Plugin + Strategy）

### 关键设计决策

1. **YAML 声明式配置**——降低使用门槛，支持 Nunjucks 模板和 `file://` 引用脚本弥补灵活性不足
2. **本地 SQLite + Drizzle ORM**——嵌入式数据库保证 100% 本地运行，牺牲多人共享换取隐私
3. **远程生成 + 本地执行混合模式**——三级优先级（环境变量 > Cloud 配置 > 默认端点），可通过环境变量完全禁用远程调用

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | promptfoo | DeepEval | Garak | Langfuse |
|------|-----------|----------|-------|----------|
| 评估能力 | 55 种断言 + 自定义 | Python 生态评估指标 | 无 | 可观测性（非评估） |
| 安全测试 | 65 插件 + 31 策略 | 无 | 漏洞扫描 | 无 |
| 合规映射 | 8 大标准内置 | 无 | 无 | 无 |
| 语言生态 | TypeScript/Node | Python | Python | TypeScript |
| 部署模式 | CLI + 本地 Web UI | pytest 集成 | CLI | SaaS/自托管 |
| Provider 覆盖 | 90+ | 有限 | 有限 | 追踪为主 |

### 差异化护城河

1. **评估 + 安全双赛道垄断**——没有任何单一竞品同时覆盖这两个维度
2. **OpenAI 官方背书**——收购后成为 OpenAI 生态的「官方」评估工具，可能成为行业标准制定者
3. **合规框架映射**——8 大安全标准到测试用例的自动映射，企业客户的开箱即用能力

### 竞争风险

1. **OpenAI 生态绑定风险**——收购后可能优先支持 OpenAI 模型，其他 Provider 支持可能弱化
2. **DeepEval 在 Python 生态的深耕**——Python 开发者可能更倾向 pytest 风格的 DeepEval
3. **Langfuse 的可观测性优势**——生产环境监控是 promptfoo 不覆盖的领域

### 生态定位

AI 安全基础设施层——从 prompt 评估工具演化为 LLM 应用安全平台，覆盖评估、红队、漏洞扫描三大场景，填补了「开发阶段主动验证」的生态空白。

## 套利机会分析

- **信息差**：虽然 19K star 早已不是「被低估」，但「评估 + 安全一体化」的独特定位仍被市场低估——多数人只知其评估功能，不知其红队测试的深度
- **技术借鉴**：自适应并发调度器、Plugin-Grader 配对架构、合规框架映射矩阵可直接迁移到其他项目
- **生态位**：LLM 应用安全测试是刚需但缺乏标准工具的领域，promptfoo 正在成为这个领域的标准
- **趋势判断**：LLM 安全监管（EU AI Act、NIST AI RMF）将持续推动需求增长，promptfoo 的合规映射能力恰好踩中这个趋势

## 风险与不足

1. **过度依赖两位创始人**——核心 commit 的 64% 来自两位创始人，如果他们因 OpenAI 内部调整减少投入，项目可能放缓
2. **代码规模膨胀**——78 万行代码对 CLI 工具而言偏大，`registry.ts`（1783 行）和 `evaluator.ts`（2622 行）的单一文件过大
3. **尚未发布 1.0**——仍处于 v0.121.3，API 稳定性未正式保证
4. **注释率偏低**——TypeScript 代码注释比 15.3:1，远低于行业推荐

## 行动建议

- **如果你要用它**：适合 LLM 应用的上线前测试和安全审计。如果只需评估，DeepEval（Python）或 RAGAS（RAG 专用）可能更轻量。如果需要安全测试，promptfoo 几乎是唯一选择
- **如果你要学它**：重点关注 `src/providers/registry.ts`（Provider 路由）、`src/redteam/`（红队架构）、`src/evaluator.ts`（评估引擎）、`src/scheduler/adaptiveConcurrency.ts`（自适应调度）
- **如果你要 fork 它**：可以精简为纯评估工具或纯安全测试工具，降低复杂度；也可以扩展合规框架映射，增加中国 AI 安全标准

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/promptfoo/promptfoo](https://deepwiki.com/promptfoo/promptfoo) |
| 关联论文 | [Insights and Current Gaps in Open-Source LLM Vulnerability Scanning Tools](https://arxiv.org/html/2410.16527v2) |
| 关联论文 | [Automatic Test Generation for Language Model Prompts](https://arxiv.org/pdf/2503.05070) |
| 关联论文 | [Interactive Tool for Regression Testing Guided LLM Migration](https://arxiv.org/html/2409.03928v1) |
| 在线 Demo | https://promptfoo.dev |
| 收购公告 | [OpenAI to acquire Promptfoo](https://openai.com/index/openai-to-acquire-promptfoo/)（2026-03-09） |
