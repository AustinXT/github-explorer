# NVIDIA SkillSpector：5K+ stars 的 MCP Skill 装前扫描器，把 AI Agent 安全做成可机检规则集

> GitHub: https://github.com/nvidia/skillspector

## 一句话总结

NVIDIA 在 AI Agent 安全赛道押注的「装前体检「工具——用 **16 类 64 条规则** + **两阶段静态/LLM 流水线**，把 Claude Code / Codex CLI / Gemini CLI 等的 SKILL.md 插件当作「待扫描的二进制「，在装机前发现提示词注入、工具投毒、MCP 最小特权越权等风险。

## 值得关注的理由

1. **MCP 协议层安全的事实标准**：业内第一套把「工具描述里藏指令「（TP1-4）和「声明 vs 实际 capability 不一致「（LP1-4）做成可机检规则的实现，5.3K stars + LangGraph 编排 + Pydantic 结构化输出，工程化范例完整。
2. **NVIDIA Agent 战略的安全护城河**：与 `nvidia/skills`（1.26k stars）、`NemoClaw`（21k stars）形成「平台 / skill 市场 / 安全审计「三角，下一家要做 MCP 市场的玩家很难绕过它的规则集。
3. **CI 友好的可机读输出**：SARIF 2.1.0 + JSON + Markdown + Terminal 四种格式，`risk_score > 50 → exit code 1` 直接断在 PR pipeline；多 LLM provider（OpenAI / Anthropic / NVIDIA build.nvidia.com / Ollama）一行 env 切换。

## 项目展示

README 与 docs 中**没有嵌入任何图片、视频或架构图**（连 badge 也只是 shields.io 的 Python/License 标识，不算展示素材）。`homepage_url` 为空、官网无素材、DeepWiki/Zread.ai 也未实质收录——这个项目**完全靠代码 + docs/ + README 「How It Works「 文本**传达信息。

> 若需公众号首图，建议走 Unsplash 兜底（关键词建议：「cyber security「, 「AI code scan「, 「lock + neural network「），不寄希望于仓库自带图。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/nvidia/skillspector |
| Star / Fork | 5,345 / 408 |
| Watcher | 28 |
| Open Issues / PRs | 26 / 24 |
| 代码行数 | 14,979（Python 98.5%, 141 文件, 注释比 28.9%） |
| 依赖 | 89（runtime, 来自 pyproject.toml） |
| 项目年龄 | 2.8 个月（首次提交 2026-03-21） |
| 开发阶段 | 稳定维护（OSS 发布冲刺后期，近 30 天 19 commits，占总量 83%） |
| 贡献模式 | 小团队核心主导 + 社区点缀（Top1 占 29.0%，前 4 人占 78%；8 位贡献者） |
| 热度定位 | 大众热门 + 爆发期（近 24h 内 +145 stars） |
| License | Apache License 2.0 |
| Release | **0 tag / 0 release**（首次 release 预计在 oss-release 冲刺后落地） |
| 质量评级 | 代码 优秀 \| 文档 优秀 \| 测试 充分 |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
NVIDIA Corporation（Organization 账号），Santa Clara, CA，14.1 年账号，26,725 粉丝，749 公开仓库。核心贡献者是 NVIDIA 内部 3-4 人小团队：`nraghavan`（9 commits）、`Nir Paz`（6）、`keshavp`（6）、`keshprad`（4），外加一个 `nv-automation` 机器人。少量外部 PR 来自 `jcchavezs` / `Lucas Recknagel` / `Werner Kasselman`。NVIDIA 正在推自家 Agent 生态（`nvidia/skills` 1.26k stars、`NemoClaw` 21k stars），SkillSpector 与它们**同源**——本质是 NVIDIA 推 Agent 平台时**配套的「上岗前体检「工具**。

### 问题判断
AI Agent 生态里「装上 SKILL.md 就能跑 shell「这种隐式信任是个未爆弹。2026 年 Liu 等人基于 42,447 个 skill 的实证研究发现 **26.1% 含漏洞、5.2% 含明显恶意意图**——这是一个**问题已被量化、但工业级扫描器缺位**的窗口。传统 Semgrep/Snyk 不识 prompt injection / system-prompt 泄漏 / 工具投毒 / memory poisoning 这一整套 Agent-原生威胁模型；通用 LLM 红队工具只给「红队评估「，不输出可在 CI 拦截的 SARIF 报告；OSV/NVD 没有直接对接「skill 声明的依赖文件「的现成路径；更没有项目把「MCP 最小特权「做成可机检规则。SkillSpector 同时填补了所有这四个空白。

### 解法哲学
**「pre-install gate, 不是 post-hoc audit「**——README 反复强调「DO NOT INSTALL「作为输出动作。技术栈选择贯彻这一思路：
- **静态扫描优先**：11 个 analyzer 在零 LLM 零网络下就能跑出 64 模式，保证「零依赖就能拦下大头「；
- **LLM 只做语义层补刀**：3 个 `semantic_*` + `meta_analyzer` filter 把精度从 ~70% 提到 ~87%，但**不是必备路径**；
- **可机读输出优先于人话**：SARIF → CI 拦截、JSON → 自动审计、Markdown/terminal → 人读，把「返回结构化报告「当作一等公民。

### 战略意图
**NVIDIA Agent 战略的基础设施件**，不是给 NVIDIA 创收的产品，而是给自家 Agent 生态做的「安全护城河「，让其他 Agent 平台在合规压力下也难以绕过。**Apache 2.0 真正开源**（不是 open-core），无 SaaS 版、无 enterprise 版、无 SaaS 控制点。与 `nvidia/skills`、`NemoClaw` 形成「**平台 / skill 市场 / 安全审计**「三角。如果它能跟着 NVIDIA 自家 agent 平台成为默认 install gate，就从「工具「升级为「标准「。

> 官方文档：仓库无独立官方文档站（homepage_url null），NVIDIA 开发者博客也未提及该项目。但 README 写得很充分（约 20k tokens），docs/ 下还有 5 篇深度设计文档（B.3.1 mcp-least-privilege / B.3.2 mcp-tool-poisoning / SC4-osv-live-vulnerability-lookups / LLM_ANALYZER_BASE_GUIDE / EVAL_DATASETS）+ DEVELOPMENT.md；外部深度分析文章**未找到**（DeepWiki 未实质收录，Zread.ai 403）。

## 核心价值提炼

### 创新之处
按新颖度 × 实用性 × 可迁移性 排序：

1. **MCP 协议层语义攻击的可机检规则集（LP1-4 + TP1-4）**——新颖度 5/5 | 实用性 5/5 | 可迁移性 4/5
   把「工具描述里藏指令「这种语义攻击拆成 4 条可机检规则（HTML/Markdown 注释、zero-width 字符、base64 解码成功、data URI），把「声明 vs 实际 capability「做成 RBAC 风格对账（LP1-4 含 wildcard / missing / underdeclared / overdeclared 4 种不对称）。**MCP 最小特权是全行业首套**。

2. **自写 AST 数据流分析（TT1-5）+ 类型推断**——新颖度 4/5 | 实用性 4/5 | 可迁移性 3/5
   用 `build_type_map` 先把 `p = Path(x)` 这种局部 var 映射到 `pathlib.Path`，再让 `p.read_text()` 解析成 `pathlib.Path.read_text`，解决「为什么 `from pathlib import Path` 后所有 `p.read_text()` 不被误识为 file_read sink「的痛点。零外部依赖、可解释、可控。

3. **「声明/实际「对账框架（declared vs actual capabilities）**——新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5
   把 skill manifest 的 `permissions[]` 视作「声明「、代码视作「实际「，用「差集的方向 + 大小「分四类问题。和 K8s RBAC drift / IaC compliance 完全同构，**通用适用**。

4. **LangGraph + Pydantic structured output + `operator.add` reducer 做「多 analyzer 聚合「**——新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   把「扫描工具的多 analyzer 多源输出「建模成图节点 + reducer，LLM 输出直接吃 Pydantic schema 校验；适合 SIEM、multi-linter、eval harness 等多源情报聚合场景。

5. **SC4 live CVE lookup 的「OSV.dev batch + in-memory cache + 静态 fallback「三段式**——新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   API 不可达时不「硬失败「也不「沉默降级「，而是降级到一份手写 fallback；cache 用 monotonic time 不污染业务时间。**任何「实时数据 + 离线兜底「服务对接都该这么设计**。

6. **YARA rules 用户可注入 + 编译降级**——新颖度 2/5 | 实用性 5/5 | 可迁移性 4/5
   `--yara-rules-dir` 让企业把自家 IOC 灌进扫描流水线；编译失败时不挂掉而是 `logger.warning` + 累加 skipped。代价是**用户的恶意 yara 也会被加载并执行**（YARA 本身有安全 CVE 史）——这是个值得注意的攻击面。

### 可复用的模式与技巧

1. **「Provider + Protocol + 每包 YAML「模式**：每个 LLM provider 自带一份 `model_registry.yaml` 描述 token 预算；`SKILLSPECTOR_MODEL_REGISTRY` 可整体覆盖。「能力即数据「模型胜过用 ABC 强绑定。
2. **`LLMAnalyzerBase.get_batches()` 自动 chunk**：按 token 预算切文件 + 50 行 overlap；`arun_batches()` 用 `asyncio.gather` + Semaphore 并发。任何「LLM 处理长文件「场景通用。
3. **风险评分公式**：CRITICAL=50, HIGH=25, MEDIUM=10, LOW=5；`has_executable_scripts` 1.3× 乘数。简单可解释，适合任何「严重度 → 分 → 门槛「的扫描工具。
4. **SARIF 通过 Pydantic `populate_by_name` + `alias` 做 camelCase 兼容**：标准协议契约的标准做法；下次 SARIF spec 改只需跟改一处。
5. **Granular → Coarse 三层 fallback key**：`meta_analyzer.apply_filter` 用 exact `(file, rule_id, start_line, end_line)` → `start_line-only` → `coarse (file, rule_id)` 的降级链，行级回填精度可控。
6. **`is_available()` 探活 + 失败 fallback**：OSV.dev 客户端对每个新依赖库都该有；不假设网络随时可达。

### 关键设计决策

1. **用 LangGraph 而非裸 asyncio.gather 编排 20 个 analyzer**
   - **问题**：analyzer 数量多，依赖共享 state（findings 要 reducer 聚合），要支持 Studio 可视化调试。
   - **方案**：每个 analyzer 都是一个图节点，`findings: Annotated[list[Finding], operator.add]` 让 LangGraph 的 reducer 自动合并多源输出。
   - **Trade-off**：换来声明式编排 + Studio 可调试 + REST 复用（`graph.py` 顶部 TODO 明确写了 `Implement skillspector serve (FastAPI): POST /scan`），代价是 LangGraph 学习曲线和一层抽象。
   - **可迁移性**：高。

2. **MCP 最小特权（LP1-4）用「regex 反查代码能力 vs 声明权限「实现，非语义比对**
   - **方案**：6 类 capability（shell/network/file_read/file_write/env/mcp）各有 ~7 条 regex；扫 `file_cache` 全文聚合 `actual_caps`；把 `permissions` 列表按 word-boundary 映射到 cap 名聚合 `declared_caps`；四个差集（实际未声明、声明但 wildcard、声明但无代码、未声明但有代码）→ LP1-4。
   - **Trade-off**：纯静态、毫秒级、可解释；代价是 `subprocess` 这种 regex 会同时命中 shell+env，且**测试文件不豁免**（`_is_test_file` 写了但没在 `node()` 里调用，正是 #14 「False Report「 的根因）。
   - **可迁移性**：高。任何「声明/实际「对账场景（IaC drift、IAM policy audit、package manifest vs import）都能套用。

3. **报告 schema 用 Pydantic 全手写（SARIF、Finding、MetaAnalyzerResult）**
   - **方案**：`sarif_models.py` 完整建模 SarifLog / Run / Tool / Driver / Result / Location / Region / ArtifactLocation（带 `populate_by_name` 做 camelCase 兼容）；`MetaAnalyzerResult` 用 Pydantic Field + `field_validator` 兜「LLM 把 nested 对象 stringify「边界 case。
   - **Trade-off**：换来 LLM 输出自动 schema 校验（`with_structured_output` 直接吃 model），代价是 SARIF 全套模型手工维护。
   - **可迁移性**：高。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | SkillSpector | AI-Infra-Guard | Semia | skill-sentinel | SkillScan |
|------|------|------|------|------|------|
| Stars | 5.3k | 3.9k | 512 | 13 | 3 |
| 规则集 | 16 类 64 模式 | ~12 类 ~30 模式 | 较少 | <10 条 | 较少 |
| MCP 协议层 | LP1-4 + TP1-4 (独家) | 无 | 无 | 无 | 无 |
| LLM 阶段 | Stage 2 可关 (~87% 精度) | 有 | 无 | 无 | 有 |
| 多 LLM provider | OpenAI / Anthropic / NVIDIA / Ollama | 单一 | 单一 | 无 | 单一 |
| 输出格式 | JSON / MD / SARIF / Terminal | HTML dashboard | JSON | JSON | JSON |
| 编排 | LangGraph + Studio | Flask web | 裸 Python | 裸 Python | 裸 Python |
| 动态执行 | ❌（明确无） | ❌ | ❌ | ❌ | ✅ Docker 沙箱 |
| 定位 | CI 友好 pre-install gate | 红队评估控制台 | pre-install 轻量替代 | 极简对照 | 动态行为预测 |

### 差异化护城河
- **技术护城河**：MCP 协议层规则集（LP/TP 全行业首套），LangGraph + Pydantic structured output 的「工程化范例「，SARIF 2.1.0 完整建模。
- **生态护城河**：NVIDIA 品牌 + 与自家 `nvidia/skills` / `NemoClaw` 的协同（其他竞品无类似「自家平台背书「）。
- **信任护城河**：Apache 2.0 + 内部 NVIDIA 团队 + 5K+ stars / 早期快速积累 + 8 位贡献者 + 28 watchers。

### 竞争风险
- **最大风险**：Tencent/AI-Infra-Guard 哪天把 MCP 规则集补齐 + 加 LangGraph 编排 → 直接吃差异化（其 3.9k stars 社区底盘很稳）。
- **次大风险**：Semgrep 推出 `semgrep agent-skills` 规则集（Semgrep 是行业默认 SAST，背书效应强）。
- **细分风险**：半年内冒出 19 个同名/类名仓库（topic `skill-scanner` 下），仅 1 个腾讯先发者，其余都是个位-百位 star 尾随者——**长尾可能内卷**。

### 生态定位
「**CI 友好的 skill pre-install gate**「——与「红队评估平台「（AI-Infra-Guard）、「动态沙箱「（SkillScan）形成**三层互补**。在 AI Agent 安全这个 2026 年才成型的细分赛道里，SkillSpector 以 NVIDIA 出品 + 5.3K stars + 64 模式规则 + MCP 协议层专属规则占据事实头部；接下来 6-12 个月的看点是它能不能跟着 NVIDIA 自家 agent 平台成为默认 install gate——若成功，会从「工具「升级为「标准「。

## 套利机会分析

- **信息差**：**不再小众**。5K+ stars + 近 24h +145 stars = 已被发现 + 还在爆发，没有早期红利可套。价值在于「跟住它「看 NVIDIA 接下来把它接到 `nvidia/skills` 哪个 agent 框架上。
- **技术借鉴**：可复用的设计模式密度极高——LangGraph + reducer 聚合、Provider + Protocol + YAML、SC4 三段式 fallback、Pydantic structured output 校验、Granular → Coarse 三层 key 降级链。**任何一个做多 analyzer / 多 provider / 实时情报对接的项目都能直接借鉴**。
- **生态位**：MCP 协议层安全目前是它独家占据的；一旦 MCP 市场成形（NVIDIA、Anthropic、OpenAI 三家都在推），这会是默认 install gate 标准的有力候选。
- **趋势判断**：AI Agent 装机量持续暴涨（Claude Code / Codex / Gemini CLI 装机基数都在百万级）+ Liu et al. 2026 数据证明 **26.1% skill 含漏洞** = 装机前扫描是结构性需求。**SkillSpector 处于「标准成型前夜「**，比 Tencent/AI-Infra-Guard 早一步在 MCP 协议层 + CI 友好定位上卡位。

## 风险与不足

1. **0 release / 0 tag / 0 refactor 三连缺位**：仓库还在 v0 公开窗口，**不建议生产环境直接锁版本**——等首次 release tag 出来再切。
2. **测试驱动是真文化，但 fix 阶段仍有反例**：Issue #9 揭示 `meta_analyzer` 异常吞掉 + exit 0 是真问题，**对跑大批量 skill 的 CI 场景是个埋雷**。Issue #10 揭示 LLM 调用无 retry/backoff 且默认并发 10 硬编码。
3. **规则-语境割裂导致 FP**：Issue #14 揭示它报的是 capability 不是 blast radius，隔离沙箱里跑也会被报「高严重度「，对内部 agent / CI 跑 skill 的用户会产生大量「不可操作「的告警。
4. **规则集「出向偏置「盲点**：Issue #61 揭示 64 条规则盯着「把数据发出去「和「exec/subprocess「两类 sink，对 SSRF（169.254.169.254 等内网/元数据目标）直到 #61 才补。
5. **正在从 CLI 演化成 agent 内部组件，但接口契约没跟上**：Issue #33 揭示用户已经在用 `graph.invoke({...})` 把扫描器当库嵌进自家 skill，但 `--no-llm` 与 LLM 模式输出差异、静态 FP 都没文档化。
6. **YARA 用户注入是双刃剑**：`--yara-rules-dir` 让企业内化自家 IOC，但**用户的恶意 yara 也会被加载并执行**（YARA 本身有 CVE 史），需要文档警示。
7. **小众早期项目的「开源疲劳「风险**：核心团队 3-4 人 + 1 个 bot 主导，社区贡献（jcchavezs / Lucas Recknagel / Werner Kasselman）只 1 commit，**外部生态尚未成型**——若 NVIDIA 战略转向，OSS 维护可能放缓。

## 行动建议

- **如果你要用它**：
  - **CI gate**（推荐）：用 `--no-llm` 跑 Stage 1 静态、`--format sarif` 输出 + `--risk-threshold 50` 拦 CRITICAL，零 API key 成本；Stage 2 LLM 留给「评审「环节人读。
  - **Agent 平台市场方**：把 `from skillspector import graph` 嵌入上架审核流水线，PR 时跑一遍、CI 不通过不让合并。
  - **个人开发者**：在装 Claude Code / Codex / Gemini CLI 第三方 skill 之前**先扫一遍**，把「DO NOT INSTALL「 当硬门槛。
  - **观望 vs 立刻上**：生产环境**等首次 release tag 出来再锁版本**；个人/实验项目**可以现在就用**。

- **如果你要学它**：
  - **LangGraph 编排 + Pydantic structured output**：`src/skillspector/graph.py`（44 行）、`llm_analyzer_base.py`、`sarif_models.py` 是教科书级别的范例。
  - **MCP 协议层规则集**：`nodes/analyzers/mcp_tool_poisoning.py` + `nodes/analyzers/mcp_least_privilege.py` 是行业首套实现。
  - **OSV.dev 三段式 fallback**：`nodes/analyzers/osv_client.py` 的 batch + cache + static fallback 是所有「实时情报对接「场景的样板。
  - **Provider 抽象**：`providers/{base.py,registry.py,openai/,anthropic/,nv_build/}` 的 Protocol + 子包 + 每包 YAML 模式胜过 ABC 强绑定。

- **如果你要 fork 它**：
  - **加动态执行层**：和 NMitchem/SkillScan 互补——SkillSpector 静态过、CRITICAL 标红直接拒；标黄/标绿再走动态验证。这是 NVIDIA 完全能做的双层。
  - **补 LangGraph conditional_edge**：把现在的「每节点自己查 use_llm「改成图条件路由，让 fallback 路径可被观测（issue #9 / #10 揭示的反例）。
  - **加 SSRF 入向规则**：扩展 OSV.dev + taint 跟踪到内网/元数据目标（issue #61 已开了口子）。
  - **加 CHANGELOG / examples 目录**：当前 0 release 的状态不利于外部采纳，CHANGELOG + 一个 5 行 `examples/scan_one_skill.py` 就能把门槛从「读完 README「降到「复制粘贴「。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未实质收录（页面处于加载态） |
| Zread.ai | 未收录（HTTP 403） |
| 关联论文 | 「Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale「（Liu et al., 2026）——README 引用为 26.1% 含漏洞 / 5.2% 可能恶意 / 42,447 skills 数据集，arXiv 链接未直接核验 |
| 在线 Demo | 无（仓库未提供 hosted playground；Docker 镜像可本地一键起） |
| 关键 Issue | [#9 两阶段流水线静默退化](https://github.com/NVIDIA/SkillSpector/issues/9) / [#14 False Report](https://github.com/NVIDIA/SkillSpector/issues/14) / [#61 SSRF 检测](https://github.com/NVIDIA/SkillSpector/issues/61) |
| 设计文档 | [B.3.1 mcp-least-privilege](https://github.com/NVIDIA/SkillSpector/blob/main/docs/B.3.1-mcp-least-privilege.md) / [B.3.2 mcp-tool-poisoning](https://github.com/NVIDIA/SkillSpector/blob/main/docs/B.3.2-mcp-tool-poisoning.md) / [SC4 OSV live lookup](https://github.com/NVIDIA/SkillSpector/blob/main/docs/SC4-osv-live-vulnerability-lookups.md) |
