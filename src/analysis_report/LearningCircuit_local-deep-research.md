# 对标 OpenAI Deep Research 的本地平替：8.4k star，研究全程不出本机、每人一把密钥加密

> GitHub: https://github.com/learningcircuit/local-deep-research

## 一句话总结

Local Deep Research（LDR）是 OpenAI Deep Research / Perplexity 的本地优先开源平替——把「提问→多轮自主检索→带引用长报告」整套能力搬到完全本地、数据自主、可审计的环境里跑。它支持任意本地/云 LLM（Ollama/llama.cpp）+ 10+ 搜索引擎（arXiv/PubMed/SearXNG）+ FAISS 私有知识库，每个用户一把 AES-256 密钥独立加密、零知识无后门，号称在 SimpleQA 上用消费级 GPU（3090 跑 27B）逼近前沿（数字有 caveat，见下）。由一位匿名开发者重度 AI 辅助、16 个月 6760 commits 打造。

## 值得关注的理由

1. **「数据主权」是真正的差异化卡位**：在 gpt-researcher（27.6k）/STORM（28k）/khoj（35k）的 deep research 红海里，LDR 是唯一把「全本地 + 每用户 SQLCipher AES-256 加密库 + 解密即认证零知识 + 可编程出网边界 + 零遥测」打包成头号卖点的项目——这套安全工程的脏活是竞品多数不愿做的，构成事实壁垒。
2. **「系统工程胜过模型规模」的赌注**：核心洞察是事实问答的准确率瓶颈不在模型大小，而在检索的广度与迭代深度——用多搜索引擎 + 多轮自主检索喂上下文，把消费级 GPU 上的小模型拉到接近前沿的表现。pipeline 迭代策略 + langgraph-agent 自主智能体双范式同接口切换，是 agentic 产品演进的范本。
3. **匿名单人 + 重度 AI 辅助的极端样本**：一位匿名开发者（占 82.4% 提交）16 个月日均 15 个 commit、产出 11.6 万行业务 + 46 万行测试（4:1）+ 17 个安全扫描器——是「AI 辅助开发能把单人产能推到什么程度」的活案例，也带出「测试很多但含金量需折算」的真实思考。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/learningcircuit/local-deep-research |
| Star / Fork | 8,401 / 727 |
| 代码规模 | 真实业务 **约 11.6 万行有效 Python**（src/，543 文件，40+ 模块）+ **约 46 万行测试**（4 倍于业务）；cloc 总 75.9 万行虚高真凶是超大测试套件（`community_benchmark_results` 仅 24KB） |
| 项目年龄 | 15.9 个月（2025-02 创建） |
| 开发阶段 | 密集开发（近 30 天 455 commits ≈ 日均 15，几乎确定重度 AI 辅助：覆盖率驱动测试 + 单人超人产出） |
| 贡献模式 | 匿名单核心主导（LearningCircuit 占 82.4%/6149 commits，63 贡献者，真名协作者 Daniel Petti/djpetti 学术背书） |
| 热度定位 | 大众热门（爆发型，HN 190+ 分、LangChain 官方推荐、r/LocalLLaMA 破圈） |
| 质量评级 | 代码[A-] 文档[A·诚实 caveat] 测试[B+·含金量存疑] CI[A·17 扫描器] 加密安全[A] |
| License | MIT（Copyright 2025 LearningCircuit） |

> ⚠️ 客观提示：README 顶部「~95% SimpleQA / 77% xbench」是**社区自报、HF ldr-benchmarks 众包小样本（n=300~500）+ LLM 评分**，README 自标 caveat（样本小/评分噪声/新基座模型 SimpleQA 训练数据污染风险），且 #4451 暴露评测管线有计数 bug。方向可信（多引擎 + 迭代 agentic 检索确能拉高本地小模型事实问答），但「95%」是营销化乐观值，不应当作与 OpenAI Deep Research 同口径的硬指标对比。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

作者 **LearningCircuit** 是匿名 User 账号（name/bio/company 全空，2024-10 注册，单人占 82.4% 提交），「项目红过作者」。可验证的真名协作者是 **Daniel Petti（djpetti）**，他写了学术 deep research 评测博客，是项目「学术研究」叙事的实际背书人。从 11.6 万行业务 + 46 万行测试 + 66 个 workflow 的体量与节奏看，几乎确定是重度 AI 辅助开发。

### 问题判断

核心洞察：**事实问答的准确率瓶颈不在模型大小，而在检索的广度与迭代深度**——用多搜索引擎 + 多轮自主检索去喂上下文，可以把消费级 GPU 上的小模型拉到接近前沿的 SimpleQA 表现。这是个「系统工程胜过模型规模」的赌注。而云端 deep research（gpt-researcher 默认云优先、STORM 偏云）把研究课题、源文档、检索轨迹全上传第三方，对记者、敏感课题研究者、法务/医疗/企业内部研究不可接受——LDR 填的正是「本地 + 加密 + 零遥测」这个空白。

### 解法哲学

①**全本地可选**（Ollama+SearXNG 全链路离线）；②**安全工程偏执**（每用户加密库 + 零知识 + 可编程 egress + 17 个安全扫描器）；③**一切可插拔**（研究策略/搜索引擎/LLM/embedding 全抽象成可替换组件）；④**知识复利**（研究产出回灌加密库、索引成向量、变成下次检索的一个引擎）；⑤**明确不做什么**（不做遥测、不做云锁定、不替用户决定模型）；⑥**反营销的坦诚**（README 直接写明「运行态密钥必在进程内存、egress 是实验性、SimpleQA 数字有 caveat」——这种诚实本身是信任策略）。

### 战略意图

匿名个人开发者在「AI deep research」风口赛道里卡「隐私/数据主权」细分。打法是用安全工程的深度（别人不愿做的脏活：SQLCipher、egress、十几个扫描器、SBOM）筑壁垒，再用消费级 GPU 基准 + 本地玩家社区做病毒传播。路线图从 pipeline 策略演进到 langgraph-agent 自主智能体，再叠 Journal Quality / News 订阅 / MCP，扩大「research OS」版图。

## 核心价值提炼

### 创新之处

1. **「解密即认证」的零知识 per-user 加密库**（新颖 5 / 实用 4 / 可迁移 5）：每用户一个独立 SQLCipher 库（AES-256），中央 `ldr_auth.db` **只存用户名、没有 password_hash 列**——认证 = 用提交的密码尝试解密该用户的 DB，解密成功即密码正确（auth 模型里根本没有可撞库的哈希目标）；每库独立随机 salt + PBKDF2；改密只 rekey；忘密码 = 数据永久不可读（真零知识，server admin 无能为力）。closure 前预派生 key 避免捕获明文密码。
2. **迭代/自主 agentic 检索拉高本地小模型**（新颖 4 / 实用 5 / 可迁移 4）：pipeline 策略 focused-iteration（8 轮 × 5 问题，BrowseComp 问题生成 + ThreadPoolExecutor 并行检索 + ProgressiveExplorer 实体覆盖追踪 + 不早筛信任 LLM 终判 + forced_answer 逼出直接答案）；langgraph-agent 自主策略（每引擎一个 tool + `research_subtopic` 派生并行子 agent，max 50 轮）。用「检索系统工程」补「模型规模」。
3. **30+ 搜索引擎两阶段统一抽象 + 白名单动态注册**（新颖 3 / 实用 5 / 可迁移 5）：`BaseSearchEngine` 强制 two-phase——先取 previews → LLM relevance filter 裁剪 → 仅对 top-k 取 full content（解耦便宜的相关性判断与昂贵的全文抓取）；引擎用布尔类属性自描述（is_scientific/is_local/is_news…）；`ENGINE_REGISTRY` 硬编码路径 + `get_safe_module_class()` 白名单加载防注入。**本地加密库 LibraryRAGSearchEngine 自身也是搜索引擎**，与 web 引擎完全同构。
4. **可编程 egress 出网边界**（新颖 5 / 实用 4 / 可迁移 3）：把「这次研究允许多少流量离开本机」做成一等设置——5 档（Adaptive/Both/Public only/Private only/Strict），统一控制哪些引擎能跑、LLM/embedding 能否走云、哪些 URL 能 fetch；Private 档强制全本地，fail-closed。对敏感课题是刚需。
5. **知识复利闭环（库即引擎）**（新颖 4 / 实用 5 / 可迁移 4）：研究 → 下载源（arxiv/pubmed/openalex…）→ 入加密库 → 切块嵌入建 FAISS 索引 → 暴露为 `LibraryRAGSearchEngine` → 下次研究检索时本地库与公网并列。「越用越聪明」的私有知识资产。
6. **pipeline ↔ 自主 agent 同接口双范式**（新颖 4 / 实用 4 / 可迁移 4）：确定性 pipeline（可预测、对小模型友好、兜底）+ 自主 agent（自决搜什么/换哪引擎/何时收、需更强模型）用同一策略接口暴露，给「小模型走 pipeline / 大模型走 agent」连续光谱。

### 可复用的模式与技巧

1. **Strategy ABC + 工厂 + settings_snapshot 注入**：agent 流程编排骨架。
2. **two-phase retrieval（preview→LLM 筛→full content）**：多源检索省 token/抓取成本。
3. **引擎自描述布尔属性 + 白名单动态注册**：可扩展且防注入的插件系统。
4. **解密即认证 + per-DB salt 零知识**：无后门的本地多用户加密。
5. **可编程 egress 策略对象（fail-closed）**：集中式数据出网治理。
6. **库即引擎的知识复利闭环**：检索产出回灌成可检索资产。
7. **forced_answer 强制答案抽取 handler**：提升小模型 QA 准确率。
8. **LLMRegistry + MCP server 双向适配**：bring-your-own-model 且 be-anyone's-tool。
9. **golden master 配置回归 + towncrier changelog.d + ADR**：大体量项目的配置/变更治理。

### 关键设计决策

- **LLM-powered Meta Search**：`MetaSearchEngine` 用 LLM 分析查询、从可用引擎选 top-N 依次尝试，带 Wikipedia 兜底（受 egress 策略 gate）——用户不该手动决定该问 arXiv 还是 Guardian。
- **带引用报告（citation_handlers）**：三实现 standard/forced_answer/precision_extraction，`forced_answer` 在模型回避时逼出直接答案（SimpleQA 拿高分的关键工程之一）。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | LDR | gpt-researcher | STORM | khoj | LangChain open_deep_research |
|------|------|--------|--------|--------|--------|
| Star | 8.4k | 27.6k | 28k | 35k | 11.6k |
| 形态 | 完整产品 | 通用研究 agent | 学术长文生成 | 自托管第二大脑 | 官方脚手架 |
| 全本地默认 | ✅ | ❌ 云优先 | ❌ 偏云 | 部分 | ❌ |
| 每用户加密/零知识 | ✅ 独一份 | ❌ | ❌ | ❌ | ❌ |
| 出网边界控制 | ✅ 5 档 | ❌ | ❌ | ❌ | ❌ |
| 知识复利库 | ✅ FAISS | 部分 | ❌ | ✅ | ❌ |
| 专精 deep research | ✅ | ✅ | ✅ 长文 | ❌ 偏助手 | ✅ 脚手架 |

### 差异化护城河

唯一把「全本地 + 每用户 AES-256 加密库 + 解密即认证零知识 + 可编程 egress + 知识复利 + 消费级 GPU 基准」打包成一等卖点的开源 deep research。安全工程的深度（17 扫描器 / SBOM / SQLCipher / egress）是竞品多数不愿做的脏活，构成事实壁垒。

### 竞争风险

1. **巴士因子 = 1**：单一匿名个人 + 重度 AI 辅助，长期维护与信任存疑。
2. **强制加密摩擦**：SQLCipher 带来的部署/性能摩擦（#4429/#4428）会劝退一部分用户。
3. **营销指标反噬风险**：「~95% SimpleQA」是自报小样本 + 评测管线有 bug（#4451），若被严谨复现质疑会反噬口碑。
4. **体量更大的竞品挤压**：gpt-researcher/khoj 若补齐「本地+加密」可正面挤压。

### 生态定位

本地 LLM 玩家社区 + 隐私敏感专业用户的「自托管 deep research OS」，上接 LangChain/LangGraph/Ollama/SearXNG/FAISS/SQLCipher，下出 MCP 给 Claude 等 agent 调用，卡位「隐私 × deep research」交叉细分。

## 套利机会分析

- **信息差**：话题（本地优先 deep research + 隐私加密）正当风口，作者匿名 + 中文社区缺系统解读，公众号选题窗口成立。但要带 caveat——别替它把「95% SimpleQA」背书成「吊打 OpenAI」。
- **技术借鉴**：解密即认证零知识加密、可编程 egress、two-phase 检索、知识复利闭环、forced_answer 强制抽取、pipeline↔agent 双范式——这些脱离 deep research 场景，对任何「local-first 隐私应用」「多源检索系统」「RAG 准确率优化」都直接可抄。
- **工程观察**（最稀缺）：匿名单人 + 重度 AI 辅助产出 11.6 万行业务 + 46 万行测试，是「AI 辅助开发产能极限」与「AI 生成测试含金量」的真实样本。
- **生态位**：填补「隐私 × 本地 × 数据主权的 deep research」空白；最大软肋是把品牌押在自报、小样本、评测管线还有 bug 的指标上。

## 风险与不足

1. **巴士因子 = 1**：匿名单人主导，重度 AI 辅助，长期可持续性存疑。
2. **营销指标待严谨复现**：SimpleQA ~95% 众包小样本 + #4451 计数 bug，不宜当硬指标。
3. **测试含金量存疑**：46 万行测试（4:1）AI 辅助/覆盖率驱动，易有「测试多但断言浅/重复样板」的水分，真实 bug 捕获力需结合线上 bug 折算。
4. **强制加密摩擦**：SQLCipher 部署/性能开销 + 忘密码即丢数据的真实风险。
5. **文档漂移**：README「20+ strategies」实际只有 6~7 个一等策略；部分策略文件过大（mcp_strategy 1860 行）。

## 行动建议

- **如果你要用它**：你是注重隐私/数据主权的研究者、记者、敏感课题企业，或本地 LLM 玩家/自托管用户——LDR 是当前最贴合「全本地 + 加密 + deep research」的开源选择，Docker/Ollama 起步。但要接受「单人维护、强制加密摩擦、准确率数字带 caveat」。要云端开箱即用的通用研究 agent 选 gpt-researcher；要学术长文选 STORM；要个人第二大脑选 khoj。
- **如果你要学它**：重点读 `database/encrypted_db.py` + `sqlcipher_utils.py` + `models/auth.py`（解密即认证零知识）、`web_search_engines/search_engine_base.py`（two-phase 抽象）、`advanced_search_system/strategies/{focused_iteration,langgraph_agent}_strategy.py`（双范式）、`security/egress/`（出网边界）、`research_library/services/`（知识复利）、`citation_handlers/forced_answer_*.py`。
- **如果你要 fork/借鉴它**：最值得搬走的是「解密即认证零知识加密」「可编程 egress」「two-phase 多源检索」这几套通用工程；以及客观看待「AI 辅助 4:1 测试」的质量含义。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [已收录（10 章：架构/安全/CI）](https://deepwiki.com/LearningCircuit/local-deep-research) |
| Zread.ai | 未确认（直连 HTTP 403） |
| PyPI | `local-deep-research`（pip 安装） |
| Docker Hub | `localdeepresearch/local-deep-research` |
| HF 数据集 | `local-deep-research/ldr-benchmarks`（众包基准，95% 数字出处，注意 caveat） |
| 关联论文 / 在线 Demo | 无独立论文（贡献者 djpetti 博客评测）；无公开托管 Demo（产品即自托管 Web UI :5000） |
