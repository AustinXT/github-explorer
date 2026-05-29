# tobi/qmd 内容分析报告

## 动机与定位

QMD（Query Markup Documents）的核心动机是：**为个人知识库提供一个完全本地运行、不依赖任何云服务的混合搜索引擎**。

现有工具的痛点非常明确：
- **ripgrep/fzf**：只能做精确文本匹配，无法理解语义（"如何处理错误" 搜不到 "exception handling"）
- **Semantra**：只有向量搜索，缺乏 BM25 的精确性（搜索特定术语时召回不稳定）
- **Open Semantic Search**：企业级部署，需要 Elasticsearch/Solr，对个人用户过重
- **Obsidian 等笔记工具**：搜索功能是附属品，无法暴露给 AI Agent 调用

QMD 的定位是"个人第二大脑的搜索基础设施"，设计决策全部围绕一个人用一台 Mac 的场景：SQLite 单文件数据库、本地 GGUF 小模型、MCP Server 让 AI 助手直接查阅你的笔记。

## 作者视角

Tobias Lutke（Shopify CEO）的项目特征非常鲜明：

1. **dogfooding 驱动**：这不是学术项目或创业产品，而是作者自己每天用来搜索个人 Markdown 笔记的工具。从 `collections.ts` 的设计可以看出，他有多个知识库目录（journals、notes、docs），需要分别索引和按范围搜索。

2. **品味驱动的工程**：代码中大量出现精心调参的痕迹——RRF 融合的 k=60、强信号阈值 0.85/0.15 gap、chunk 大小 900 tokens with 15% overlap、位置感知权重（top-3 结果 RRF 权重 0.75）——这些都不是默认值，而是在实际使用中反复调优的结果。

3. **微调自有模型**：项目内含 Python finetune 脚本和自有微调模型 `tobil/qmd-query-expansion-1.7B`，说明作者对查询扩展效果不满意，亲自训练了一个专用模型。这在个人项目中非常罕见。

4. **嵌入 Claude Code Skill**：`embedded-skills.ts` 中内嵌了 Base64 编码的 `SKILL.md`，可以直接作为 Claude Code 的技能文件安装，说明作者自己就是通过 Claude Code + QMD MCP Server 来搜索笔记的。

## 架构与设计决策

### 目录结构概览

```
src/
├── store.ts          # 4,379 行 — 核心搜索引擎（索引、BM25、向量搜索、RRF、混合查询）
├── llm.ts            # 1,546 行 — LLM 抽象层（embedding、rerank、query expansion、session 管理）
├── cli/
│   ├── qmd.ts        # 3,187 行 — CLI 入口（所有子命令）
│   └── formatter.ts  #   430 行 — 输出格式化（JSON/CSV/XML/MD/CLI）
├── mcp/
│   └── server.ts     #   807 行 — MCP Server（stdio + HTTP 双传输）
├── db.ts             #    96 行 — SQLite 兼容层（Bun/Node 双运行时）
├── collections.ts    #   500 行 — YAML 配置管理
├── index.ts          #   528 行 — SDK 公开 API 入口
├── maintenance.ts    #    54 行 — 数据库维护操作
├── embedded-skills.ts #   22 行 — 内嵌 Claude Code 技能
└── bench-rerank.ts   # 性能基准测试
```

总计约 11,549 行 TypeScript 源码（不含测试），测试代码约 10,705 行，**测试代码量接近源码量**。

### 关键设计决策

**1. 单文件 SQLite 架构 + sqlite-vec 向量扩展**

将 BM25 全文索引（SQLite FTS5）和向量索引（sqlite-vec）放在同一个 SQLite 文件中。好处是零部署——没有 Elasticsearch、没有 Pinecone、没有 Redis，一个 `.sqlite` 文件就是整个搜索引擎。`db.ts` 仅 96 行，提供了 Bun 和 Node.js 的双运行时兼容。

**2. 8 步混合搜索管线**

`hybridQuery()` 是整个项目的灵魂，完整管线：
1. BM25 探测 → 强信号检测（如果 top-1 评分 >= 0.85 且与 top-2 差距 >= 0.15，跳过 LLM 扩展）
2. LLM 查询扩展 → 生成 lex/vec/hyde 三种变体
3. 类型路由：lex → FTS，vec/hyde → 向量检索
4. RRF 融合（k=60，前两个列表 2x 权重）
5. 文档切块 + 关键词最佳块选择
6. LLM 重排序（只排序最佳 chunk，非全文——避免 O(tokens) 陷阱）
7. 位置感知分数混合（top-3: 75% RRF / 25% rerank，4-10: 60/40，11+: 40/60）
8. 去重、最低分过滤、截断

**3. Smart Chunking 系统**

不是简单按字符数切割，而是实现了 Markdown 感知的智能切块：
- 10 级 Break Pattern（h1=100分 → newline=1分）
- 代码围栏保护（永不在 ``` 内部切割）
- 平方距离衰减窗口（heading 在窗口远端仍能胜过近处的低质量断点）
- 这使得每个 chunk 都是语义完整的段落单元

**4. LLM 会话管理与资源生命周期**

`llm.ts` 中实现了完整的生命周期管理：
- `LLMSession` 类支持 `maxDuration` 超时和 `AbortSignal`
- `withLLMSession()` 模式确保会话自动释放
- 5 分钟非活跃超时自动卸载 context（但保留 model 避免 VRAM 反复加载）
- 嵌入上下文池化（复用 `LlamaEmbeddingContext`）
- 并发锁防止重复加载同一模型

**5. 双传输 MCP Server**

`mcp/server.ts` 同时支持 stdio（本地 Claude Code 直接调用）和 HTTP（Streamable HTTP 传输，支持 `--daemon` 后台运行）。动态生成的 `instructions` 会根据当前索引状态告诉 LLM"你能搜什么"，避免无效调用。

## 创新点

### 1. 强信号短路 + Intent 解歧

当 BM25 已经给出高置信度结果时（top-1 >= 0.85 且领先 >= 0.15），跳过昂贵的 LLM 查询扩展。但如果用户提供了 `intent` 参数，则强制走完整管线——因为"performance"这个词在 BM25 中可能精确匹配到体育表现的文档，但用户实际想要的是 Web 性能优化。这个设计说明作者不是盲目地"全上 LLM"，而是理解了何时 LLM 是浪费、何时 BM25 会误导。

### 2. 自有微调查询扩展模型

`DEFAULT_GENERATE_MODEL` 指向 `tobil/qmd-query-expansion-1.7B`——作者基于 Qwen3-1.7B 微调了一个专门用于查询扩展的小模型。项目中还包含 LFM2（LiquidAI）的备选模型 URI 和 SFT 训练配置，说明在持续实验不同架构。这是从"使用现成模型"到"为自己的用例优化模型"的跨越。

### 3. 位置感知 RRF-Rerank 混合评分

通常 RRF 和 Reranker 的分数直接加权混合。QMD 的做法更精细：根据 RRF 排名位置动态调整权重——top-3 结果给予 RRF 75% 权重（保护检索阶段的强信号），11+ 名次的结果只给 40%（让 Reranker 有更大话语权翻盘）。这避免了"Reranker 把 BM25 精确匹配的好结果压下去"的常见问题。

## 可复用模式

### 1. SQLite 作为统一搜索后端

```
BM25 (FTS5) + 向量 (sqlite-vec) + 元数据 → 单个 .sqlite 文件
```

适用场景：任何需要混合搜索但不想部署 Elasticsearch 的本地/嵌入式应用。关键在于 `db.ts` 仅 96 行的兼容层——证明了 SQLite + 扩展可以替代重量级搜索基础设施。

### 2. Markdown 感知的智能切块算法

`scanBreakPoints()` + `findCodeFences()` + `findBestCutoff()` 三件套可以直接复用于任何 RAG 场景。核心思路：为每个断点打分（heading > 代码块边界 > 空行 > 列表项 > 换行），然后在目标窗口内用距离衰减选择最优切割点。比固定 token 数切割显著提升 chunk 语义完整性。

### 3. withLLMSession + 非活跃超时资源管理

```typescript
await withLLMSession(async (session) => {
  const expanded = await session.expandQuery(query);
  const reranked = await session.rerank(query, docs);
  return reranked;
}, { maxDuration: 10 * 60 * 1000 });
```

这种"有作用域的 LLM 会话"模式解决了本地 LLM 的核心痛点：模型加载慢但不能每次重新加载，VRAM 有限不能永远占用。5 分钟非活跃超时释放 context 但保留 model，是在"响应速度"和"资源释放"之间的最佳平衡。

### 4. MCP Server 动态 Instructions 注入

```typescript
async function buildInstructions(store: QMDStore): Promise<string> {
  const status = await store.getStatus();
  // 动态告诉 LLM：你有 N 个文档、M 个 collection、是否有向量索引...
}
```

MCP Server 在初始化时根据实际索引状态生成 instructions，让 LLM 不需要先调用 `status` 工具就知道"能搜什么、怎么搜"。这减少了一次 tool call 往返，对 Agent 的搜索效率有实际提升。

## 竞品交叉分析

### vs ripgrep

| 维度 | ripgrep | QMD |
|------|---------|-----|
| 搜索类型 | 纯正则/字面匹配 | BM25 + 向量 + LLM rerank |
| 语义理解 | 无 | 支持（"如何处理错误" → "exception handling"） |
| 启动速度 | 毫秒级 | 首次 ~3-5 秒（模型加载），后续亚秒 |
| 依赖 | 零（单二进制） | node-llama-cpp + GGUF 模型 (~3GB) |
| 适用场景 | 代码搜索、日志分析 | 笔记/文档知识库 |

**结论**：不是替代关系。ripgrep 处理"精确查找"无可匹敌，QMD 处理"我记得写过关于 X 的笔记但忘了用什么词"。作者自己的 CLI 中保留了 `search` 命令（纯 BM25）作为 ripgrep 场景的快速通道。

### vs Semantra

| 维度 | Semantra | QMD |
|------|----------|-----|
| 搜索模式 | 纯向量 | BM25 + 向量 + HyDE + RRF 融合 |
| LLM 重排序 | 无 | 有（Qwen3-Reranker-0.6B） |
| 查询扩展 | 无 | 有（自有微调模型） |
| MCP/Agent 集成 | 无 | 原生 MCP Server |
| UI | Web 界面 | CLI + SDK + MCP |
| 运行时 | Python | TypeScript (Node.js/Bun) |

**结论**：QMD 在搜索质量上明显领先——混合搜索 + reranking + query expansion 三板斧。Semantra 的优势是有 Web UI（QMD 目前纯 CLI/MCP）。但 QMD 的真正杀手锏是 MCP Server 集成——它不只是给人用的搜索工具，更是给 AI Agent 用的知识检索后端。

### 综合竞争结论

QMD 占据了一个独特的生态位：**本地运行 + 混合检索 + Agent 原生**。市面上没有其他工具同时满足这三个条件。它的竞争壁垒不在于任何单一技术（BM25/向量/rerank 都是成熟技术），而在于将它们整合到一个零部署的 CLI 工具中、并通过 MCP 让 AI 助手能直接调用。

最大风险是 **模型体验的平台碎片化**：M1 Mac 上运行流畅（Metal GPU 加速），但 WSL2 和非 Mac 设备上的问题（Issues #141, #212, #291）说明 node-llama-cpp 的跨平台能力仍有短板。

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 类型安全 | A | 全 TypeScript，丰富的接口定义和类型导出，Zod 用于运行时验证 |
| 测试覆盖 | A | 16 个测试文件、~10,705 行测试代码，覆盖 store/llm/mcp/formatter/rrf 等核心模块 |
| CI/CD | A | GitHub Actions 覆盖 Node 22/23 + Bun，macOS + Ubuntu 双平台矩阵 |
| 文档与注释 | A- | 每个核心函数都有 JSDoc 注释，`hybridQuery` 有 8 步管线文档；缺少架构图 |
| 错误处理 | B+ | LLM 操作有 graceful fallback（嵌入失败返回 null、模型不可用跳过向量搜索），但部分 catch 块是空的 |
| 模块化 | B+ | 核心逻辑集中在 store.ts（4,379 行），有些过大；但函数粒度合理，可单独调用 |
| 跨平台兼容 | B | 精心处理了 Git Bash、WSL、Windows 路径；但 node-llama-cpp 的 GPU 加速在非 Mac 上不稳定 |
| 依赖管理 | A- | 依赖精简（7 个运行时依赖），sqlite-vec 使用 optionalDependencies 按平台安装 |

### 质量检查清单

- [x] TypeScript 严格模式
- [x] CI 自动化测试（Node + Bun 双运行时）
- [x] 测试覆盖核心搜索管线（BM25、向量、RRF、结构化搜索）
- [x] 测试覆盖 MCP Server
- [x] 生产/测试模式隔离（`enableProductionMode()` 防止测试写入全局索引）
- [x] 发布脚本（`release.sh` + `publish.yml`）
- [x] 性能基准测试（`bench-rerank.ts`）
- [x] 双运行时兼容层（`db.ts` 支持 Bun/Node）
- [ ] Windows 原生支持（依赖 node-llama-cpp 的 CUDA/Vulkan 支持）
- [ ] CJK 全文搜索（Issue #291，SQLite FTS5 默认分词器不支持）
- [ ] 远程 API 后端选项（Issue #114，当前仅支持本地 GGUF 模型）
