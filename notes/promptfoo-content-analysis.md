# promptfoo/promptfoo — 内容分析报告

## 动机与定位

Promptfoo 解决的核心问题是：**LLM 应用缺乏系统化的质量保障和安全验证手段**。在 LLM 从实验走向生产的转折点上，团队面临两类痛点——

1. **评估困境**：提示词和模型的选择依赖「直觉试错」，无法量化对比不同配置的效果差异。传统软件测试框架无法应对 LLM 输出的非确定性。
2. **安全盲区**：LLM 应用上线前缺乏自动化的红队攻击测试，安全漏洞（提示注入、PII 泄露、越狱等）只能靠人工发现。

Promptfoo 的定位是 **「LLM 应用的测试与安全一站式工具箱」**，同时覆盖评估（Evals）和红队安全测试（Red Teaming）两个维度。这在竞品中是独一无二的组合——DeepEval 只做评估，Garak 只做漏洞扫描，Promptfoo 将二者统一在同一声明式配置框架下。

项目于 2026 年 3 月被 OpenAI 收购，这是其战略价值的最高验证。收购后保持 MIT 开源，反映出 OpenAI 希望通过开源评估工具建立生态标准、推动模型评估标准化的意图。

**核心价值主张**：
- 开发者优先（CLI 驱动，YAML 声明式配置）
- 100% 本地运行（零隐私泄露风险）
- 插件式 Provider 架构（90+ LLM 提供商适配）
- 评估 + 红队安全测试一体化

---

## 作者视角

### 问题发现

Ian Webster（typpo）作为 Discord 的 LLM 工程负责人，直接面对了 2 亿用户规模的 LLM 应用质量和安全挑战。这个位置赋予了他独特的视角：

- **规模化验证困境**：在 Discord 体量下，手动评估完全不可行，必须自动化
- **安全紧迫性**：LLM 应用暴露给 C 端用户后，提示注入和有害输出的风险指数级放大
- **多模型比较需求**：Discord 需要同时对接多个 LLM Provider，横向对比成为刚需

联合创始人 Michael D'Angelo（mldangelo）贡献了 62.6% 的 commit，两人合计占 64%，构成典型的「双核创始人驱动」模式。

### 解法哲学

Promptfoo 的设计哲学可以用三个关键词概括：

1. **声明式优于命令式**：用 YAML 配置文件定义测试套件，而非编写测试代码。降低使用门槛，同时保持足够灵活性
2. **本地优先**：所有评估和测试在用户机器上运行，提示词和 API 密钥不离开本地。这解决了企业客户的隐私顾虑
3. **插件化扩展**：Provider、Assertion、Redteam Plugin 都可以通过注册机制扩展，核心框架保持稳定

### 背景知识迁移

Ian 的 Smile ID VP of Engineering 经历（ML + 工程管理）直接影响了 Promptfoo 的架构：
- ML 评估指标体系（BLEU/ROUGE/余弦相似度）被内置为 Assertion 类型
- 工程化思维体现在声明式配置、CI/CD 集成、缓存机制等基础设施
- a16z 投资和 Fortune 500 企业客户（25%）验证了产品市场匹配

### 战略图景

被 OpenAI 收购后的战略路径清晰：

- **评估标准化**：作为 OpenAI 生态的「官方」评估工具，推动行业标准统一
- **红队民主化**：让更多开发者能够进行专业级的安全测试
- **合规桥梁**：内置 OWASP/NIST/EU AI Act 等合规框架映射，成为 AI 治理的基础设施
- **模型竞争力放大器**：通过多模型横向对比，间接展示 OpenAI 模型的优势

---

## 架构与设计决策

### 目录结构概览

```
src/
├── providers/        # LLM Provider 适配层（198 文件，88 个注册条目）
├── redteam/          # 红队安全测试（201 文件）
│   ├── plugins/      #   65+ 攻击插件（每个 Plugin + Grader 配对）
│   ├── strategies/   #   31 种攻击策略（Crescendo/GOAT/Iterative 等）
│   ├── providers/    #   多轮攻击 Provider（红队专用）
│   ├── extraction/   #   目的系统意图提取
│   └── grading/      #   攻击结果评分
├── assertions/       # 55 种断言类型（contains/similarity/llm-rubric/事实性等）
├── evaluator.ts      # 核心评估引擎（2622 行）
├── matchers.ts       # 评分匹配器（2066 行，余弦相似度/LLM 评分等）
├── scheduler/        # 自适应速率限制调度器
├── prompts/          # 提示词处理（支持 10+ 格式）
├── database/         # Drizzle ORM + SQLite 持久化
├── server/           # Express Web 服务（API + WebSocket）
├── models/           # 数据模型层
├── tracing/          # OpenTelemetry 集成
├── cache.ts          # 双层缓存（磁盘/内存）
├── index.ts          # 公共 API 导出（evaluate + redteam）
└── commands/         # CLI 命令集（eval/view/redteam/init 等）
```

### 关键设计决策

1. **决策：Provider 注册表模式（test/create 工厂对）**
   - 问题：需要支持 90+ 种 LLM Provider，且持续增长
   - 方案：在 `registry.ts` 中定义 `ProviderFactory[]` 数组，每个条目包含 `test`（匹配规则）和 `create`（实例化逻辑）方法。按顺序匹配，首个命中即创建
   - Trade-off：线性匹配的 O(n) 复杂度在 88 个条目时性能可忽略，但代码量膨胀（1783 行单一文件）。更优方案是用前缀树（Trie）或 Map，但当前规模下不值得重构
   - 可迁移性：**高** — 这种「test/create 工厂链」模式适用于任何需要动态路由的插件系统

2. **决策：Plugin-Grader 配对架构**
   - 问题：红队测试需要「生成攻击」和「判定成功」两个独立逻辑
   - 方案：每个攻击类型由 `RedteamPluginBase`（生成测试用例）和 `RedteamGraderBase`（评分判定）配对实现。Plugin 产出 `TestCase[]`，Grader 对响应给出 `GradingResult`
   - Trade-off：增加了新攻击类型的实现工作量（需要写两个类），但分离关注点使测试更可靠。`graders.ts` 注册了 100+ 个 Grader 实例
   - 可迁移性：**高** — 「攻击生成 + 结果判定」的双抽象是安全测试框架的标准模式

3. **决策：声明式 YAML 配置作为主要接口**
   - 问题：降低开发者使用门槛，同时支持 CI/CD 自动化
   - 方案：通过 `promptfooconfig.yaml` 定义测试套件，支持 Nunjucks 模板、外部文件引用、变量注入。Zod schema 验证配置合法性
   - Trade-off：YAML 的表达力上限低于代码，但通过 `file://` 引用 JS/Python 脚本弥补了灵活性不足
   - 可迁移性：**中** — YAML 配置模式在 CI 工具中普遍存在，但 Promptfoo 的 schema 设计具有领域特异性

4. **决策：自适应速率限制调度器**
   - 问题：多 Provider 并发评估时，各 API 的速率限制差异巨大
   - 方案：`AdaptiveConcurrency` 类实现「学习-适应」模式 — 从响应头解析速率限制信息，动态调整并发度。被限流时减半（BACKOFF_FACTOR=0.5），连续 5 次成功后恢复（RECOVERY_FACTOR=1.5）
   - Trade-off：增加了调度层复杂度，但将用户从手动调参中解放。从最低并发恢复到初始值需要 25 次成功请求
   - 可迁移性：**高** — 自适应并发是通用模式，可独立于 Promptfoo 使用

5. **决策：本地 SQLite + Drizzle ORM 持久化**
   - 问题：评估结果需要持久化存储和查询，但不能依赖外部数据库
   - 方案：使用 `better-sqlite3` 嵌入式数据库 + Drizzle ORM，数据存储在 `~/.promptfoo/promptfoo.db`。定义了 evals/prompts/tags/datasets/traces/spans 等 10+ 张表
   - Trade-off：SQLite 的并发写入限制在多人共享场景下是瓶颈，但 100% 本地运行的设计目标优先级更高
   - 可迁移性：**中** — 嵌入式数据库模式在桌面/CLI 工具中可复用

6. **决策：合规框架映射矩阵**
   - 问题：企业客户需要按 OWASP/NIST/EU AI Act 等标准进行合规测试
   - 方案：在 `constants/frameworks.ts` 中定义了 8 大合规框架（OWASP LLM/API/Agentic Top 10、NIST AI RMF、MITRE ATLAS、EU AI Act、ISO 42001、GDPR、DoD AI Ethics）到 Plugin + Strategy 的映射矩阵
   - Trade-off：映射关系需要持续维护以跟进标准更新，但为企业客户提供了开箱即用的合规测试能力
   - 可迁移性：**高** — 合规框架到测试用例的映射矩阵是 AI 治理工具的标准需求

7. **决策：远程生成 + 本地执行混合模式**
   - 问题：红队测试用例生成需要强大的 LLM 能力，但用户可能没有 API Key 或希望保护隐私
   - 方案：`remoteGeneration.ts` 实现三级优先级 — 环境变量 > Cloud 配置 > 默认端点（api.promptfoo.app）。可通过 `PROMPTFOO_DISABLE_REMOTE_GENERATION` 完全禁用远程调用
   - Trade-off：远程生成简化了使用但引入了网络依赖；混合模式平衡了易用性和隐私
   - 可迁移性：**中** — 远程/本地混合模式在 SaaS 工具中常见

---

## 创新点

1. **评估 + 红队一体化框架**
   - 描述：将 LLM 评估和 AI 安全红队测试统一在同一声明式配置和执行引擎下。同一套 Provider 体系既用于 eval 也用于 redteam，同一套 Assertion 体系既用于评分也用于安全判定
   - 新颖度: 5/5 | 实用性: 5/5 | 可迁移性: 4/5

2. **自适应速率限制调度器**
   - 描述：`AdaptiveConcurrency` 从 LLM API 响应头自动学习速率限制，动态调整并发度。无需手动配置，零知识启动，自我优化。包含限流减半、连续成功恢复、10% 剩余预警等策略
   - 新颖度: 4/5 | 实用性: 5/5 | 可迁移性: 5/5

3. **合规框架自动映射**
   - 描述：内置 8 大 AI 安全合规标准（OWASP LLM/API/Agentic Top 10、NIST AI RMF、MITRE ATLAS、EU AI Act、ISO 42001、GDPR、DoD AI Ethics）到具体 Plugin + Strategy 的映射矩阵。用户指定 `owasp:llm` 即可自动生成对应的完整测试套件
   - 新颖度: 5/5 | 实用性: 5/5 | 可迁移性: 4/5

4. **多轮攻击策略引擎**
   - 描述：实现了 31 种攻击策略，包括学术攻击算法（Crescendo — 基于论文 arXiv:2312.02119 的渐进式对话攻击、GOAT — 目标导向自适应攻击）、编码混淆（Base64/ROT13/Leetspeak/Hex/同形字）、复合攻击（Iterative Tree/Meta/Best-of-N）等。每种策略将 Plugin 生成的测试用例包装为多轮对话 Provider
   - 新颖度: 5/5 | 实用性: 4/5 | 可迁移性: 3/5

5. **风险评分系统（riskScoring.ts）**
   - 描述：基于 Impact（影响）x Exploitability（可利用性）x Human Factor（人为因素）三维模型计算系统风险评分。结合攻击策略复杂度加权，输出 Critical/High/Medium/Low/Informational 五级风险等级和分布
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 4/5

6. **Provider 路径 DSL**
   - 描述：通过字符串路径（如 `openai:chat:gpt-4o`、`anthropic:messages:claude-3`、`bedrock:converse:claude-3`）实现 Provider 的声明式引用。路径格式既作为路由键又携带配置参数，无需额外配置文件即可指定 Provider
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 4/5

7. **系统目的自动提取（extraction/purpose.ts）**
   - 描述：通过 LLM 从目标应用的提示词模板自动推断「系统目的」（System Purpose），然后将目的信息注入所有 Plugin 的测试用例生成。这使得攻击测试具有上下文相关性，而非通用泛化
   - 新颖度: 4/5 | 实用性: 4/5 | 可迁移性: 3/5

---

## 可复用模式

### 1. test/create 工厂链（Provider 注册表）
适用场景：需要动态路由到不同实现的插件系统。按优先级顺序匹配，首个命中即创建实例。
核心代码：`src/providers/registry.ts`

### 2. Plugin-Grader 配对（安全测试框架）
适用场景：安全测试中「生成攻击」和「判定结果」分离。Plugin 生成 `TestCase[]`，Grader 输出 `GradingResult`。
核心代码：`src/redteam/plugins/base.ts` + `src/redteam/graders.ts`

### 3. 自适应并发调度
适用场景：需要调用多个有速率限制的 API 的并发场景。从响应头学习限制，动态调整并发度。
核心代码：`src/scheduler/adaptiveConcurrency.ts`

### 4. 合规框架映射矩阵
适用场景：将抽象的安全标准映射到具体测试用例。支持嵌套映射（框架 -> 风险域 -> Plugin + Strategy）。
核心代码：`src/redteam/constants/frameworks.ts`

### 5. 远程/本地混合生成
适用场景：需要强大的 LLM 能力但又要支持离线/隐私模式。三级优先级：环境变量 > Cloud 配置 > 默认端点。
核心代码：`src/redteam/remoteGeneration.ts`

---

## 竞品交叉分析

### vs DeepEval (confident-ai)
- **覆盖范围**：DeepEval 专注 Python 生态的 LLM 评估，提供 Faithfulness/Answer Relevance 等指标。Promptfoo 在评估维度上与其重叠（均支持事实性、相关性检查），但额外提供完整的红队安全测试
- **语言生态**：DeepEval 是 Python-first，Promptfoo 是 TypeScript/Node-first。二者服务不同的开发者群体
- **差异化**：Promptfoo 的声明式 YAML 配置 vs DeepEval 的代码化测试。Promptfoo 的 Provider 覆盖范围（90+）远超 DeepEval
- **红队能力**：Promptfoo 独有。DeepEval 没有任何安全测试功能

### vs Langfuse
- **定位差异**：Langfuse 是 LLM 可观测性平台（追踪、监控、日志），偏向生产环境的事后分析。Promptfoo 是预发布测试工具（评估、红队），偏向部署前的主动验证
- **互补性**：两者可以串联使用 — Promptfoo 做上线前测试，Langfuse 做上线后监控
- **数据模型**：Langfuse 基于 Traces/Spans 的实时数据流，Promptfoo 基于 Eval/TestCase 的离线评估结果

### vs RAGAS
- **聚焦度**：RAGAS 极度专注 RAG 质量指标（Faithfulness/Context Precision/Answer Relevancy）。Promptfoo 的 RAG 评估是其子集
- **深度 vs 广度**：RAGAS 在 RAG 指标上更深更专业，Promptfoo 在整体测试覆盖面上更广
- **红队**：Promptfoo 独有的 RAG 安全测试（rag-document-exfiltration、rag-source-attribution）

### vs Garak (NVIDIA)
- **方向一致，深度不同**：Garak 是 NVIDIA 出品的 LLM 漏洞扫描器，与 Promptfoo 的红队模块定位接近
- **攻击方法**：两者都覆盖了提示注入、越狱、有害内容等攻击面。Promptfoo 额外实现了多轮攻击策略（Crescendo/GOAT/Iterative Tree），Garak 更偏静态探测
- **评估能力**：Garak 缺乏评估功能，Promptfoo 的 eval 模块是其核心差异
- **生态**：Garak 是 Python 命令行工具，Promptfoo 同时提供 CLI + Node.js API + Web UI

### vs Arize AI Phoenix
- **层次差异**：Phoenix 是 ML 可观测性平台，覆盖模型训练到推理的全生命周期。Promptfoo 聚焦 LLM 应用的测试阶段
- **技术栈**：Phoenix 基于 OpenTelemetry + LlamaIndex，Promptfoo 自建评估框架 + OpenTelemetry 集成
- **目标用户**：Phoenix 面向 ML 工程师，Promptfoo 面向应用开发者

### 综合竞争结论

Promptfoo 的核心竞争力在于 **「评估 + 红队」一体化** 的独特定位。在评估维度上，它与 DeepEval/RAGAS 有功能重叠但语言生态不同；在安全测试维度上，它与 Garak 方向一致但更全面（多轮策略 + 合规映射）。没有任何单一竞品同时覆盖这两个维度。

被 OpenAI 收购后，Promptfoo 获得了不对称的竞争优势——作为 OpenAI 生态的「官方」评估工具，它可能成为 LLM 评估事实标准的制定者。其内置的合规框架映射（OWASP/NIST/EU AI Act 等）进一步巩固了在企业市场的壁垒。

---

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| **架构清晰度** | A- | 模块划分明确（providers/redteam/assertions/evaluator 四大支柱），依赖关系单向。扣分项：`registry.ts`（1783 行）和 `evaluator.ts`（2622 行）的单一文件过大 |
| **抽象层次** | A | 核心抽象设计合理：`ApiProvider`（Provider 统一接口）、`RedteamPluginBase`/`RedteamGraderBase`（攻击/评分配对）、`Assertion`（断言类型系统）。Zod schema 验证保证类型安全 |
| **扩展性** | A+ | 插件化架构贯穿全局：Provider 通过 test/create 工厂链扩展，Plugin/Grader 通过注册表扩展，Assertion 通过类型分发器扩展，Strategy 通过包装器模式扩展 |
| **测试覆盖** | A- | 654 个测试文件，29.7 万行测试代码。覆盖核心路径和边界情况。红队集成测试有独立的 `test/redteam/integration` 目录 |
| **文档质量** | A+ | 项目根目录 AGENTS.md（320 行）提供全面的 AI 代理协作指南。每个子目录有独立的 AGENTS.md。CONTRIBUTING.md 指向详细文档站。代码注释充分 |
| **类型安全** | A | 全 TypeScript，严格模式。Zod 用于运行时 schema 验证。类型导出完整（`dist/src/index.d.ts`）。唯一的 `FIXME` 注释在 `providers/index.ts` 中 |
| **依赖管理** | A | Renovate 自动管理依赖更新（运行时依赖延迟 5 天，开发依赖延迟 2 天）。`engine-strict=true` 确保 Node.js 版本兼容。Node.js 24 Alpine 基础镜像 |
| **错误处理** | B+ | 核心路径错误处理完善（Provider 加载失败、API 调用超时、远程生成不可用），但部分 Provider 实现中的错误处理不一致。`invariant` 函数用于前置条件检查 |
| **性能优化** | A | 自适应速率限制调度器、双层缓存（磁盘 + 内存，14 天 TTL）、better-sqlite3 嵌入式数据库、增量构建支持。`build:watch` 使用 8GB 内存上限 |
| **安全性** | A | 入口文件零依赖设计（先检查 Node 版本再加载模块），CSRF 保护中间件，日志自动脱敏，API Key 不入 Git，敏感信息存储在 `.env.local`。被 OpenAI 收购后安全审查标准更高 |
| **CI/CD 成熟度** | A | 多层测试策略（单元/集成/Smoke/红队集成），Biome + Prettier 双格式化，pre-commit hook 自动格式化，release-please 自动发版，409 个版本标签反映持续交付节奏 |

---

## 附录：关键数据点

- 代码规模：903 个 TypeScript 文件（src/），520 个 TSX 文件（前端）
- Provider 覆盖：88 个注册条目，198 个实现文件
- 红队插件：65 个攻击插件目录，31 种攻击策略，100+ 个 Grader 实例
- 断言类型：55 种内置断言
- 合规框架：8 大标准（OWASP LLM/API/Agentic、NIST、MITRE ATLAS、EU AI Act、ISO 42001、GDPR、DoD AI Ethics）
- 示例库：208 个示例配置目录
- 测试：654 个测试文件，29.7 万行测试代码
- 版本：v0.121.3（409 个版本标签，37 个月持续迭代）
