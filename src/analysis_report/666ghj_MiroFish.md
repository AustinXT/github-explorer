# MiroFish 深度分析报告

> GitHub: https://github.com/666ghj/MiroFish

## 一句话总结
4 个月 38K Stars 的群体智能预测引擎——通过构建成千上万 AI 智能体的平行数字世界，模拟社交媒体交互来预测未来走向，是「社会模拟即预测」范式的首个开源产品。

## 值得关注的理由
1. **赛道独创**：在「多 Agent 社会模拟 × 预测引擎 × 开源产品」交叉领域几乎无直接竞品，38.2K Stars 远超上游引擎 OASIS（3.6K）
2. **商业背书**：北邮大四学生郭航江获盛大集团陈天桥 3000 万人民币投资，两次登顶 GitHub 全球 Trending #1
3. **范式创新**：不做「数据拟合式预测」，而是「社会模拟式预测」——将种子信息注入 LLM Agent 社会，通过群体涌现推演未来，是预测市场概念在 AI 时代的范式迁移

## 项目展示

![MiroFish Logo](https://github.com/666ghj/MiroFish/raw/main/static/image/MiroFish_logo_compressed.jpeg)

群体智能预测引擎——预测万物。

![运行截图](https://github.com/666ghj/MiroFish/raw/main/static/image/Screenshot/运行截图1.png)

五步骤线性流程：图谱构建→环境搭建→模拟运行→报告生成→深度互动。

**演示视频**：[武汉大学舆情推演预测](https://www.bilibili.com/video/BV1VYBsBHEMY/) | [红楼梦失传结局推演](https://www.bilibili.com/video/BV1cPk3BBExq)

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/666ghj/MiroFish |
| Star / Fork | 38,210 / 5,118 |
| 代码行数 | ~41,200 (Python 50%, Vue/JS 50%) |
| 项目年龄 | 4 个月（2025-11 创建） |
| 开发阶段 | 早期密集开发（v0.1.x，2025-12 月 153 次提交占 69.5%） |
| 贡献模式 | 单人主导（666ghj 219/220 次提交，Bus Factor = 1） |
| 热度定位 | 大众热门（38.2K Stars，两次登顶 GitHub Trending #1） |
| 质量评级 | 代码[一般] 文档[良好] 测试[无] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
**郭航江**（@666ghj），北京邮电大学大四学生（00 后），被媒体称为「小孩哥」。2025 年底首个项目 BettaFish 登顶 GitHub 热榜引起盛大集团创始人陈天桥关注，获 3000 万人民币投资。随后用 **Claude Code（Vibe Coding）10 天独立开发 MiroFish**。BettaFish（39.6K）+ MiroFish（38.2K）累计近 8 万 Stars，构成「采集→分析→预测」完整产品链。

### 问题判断
三个精准的交叉空白：(1) **学术工具的产品化空白**——OASIS 是强大的多 Agent 社交模拟框架但无 UI，普通用户无法使用；(2) **预测市场的方法论空白**——Polymarket/Metaculus 依赖人类群体智慧，MiroFish 用 AI Agent 群体替代人类群体；(3) **Zep Cloud 的应用场景空白**——将 Zep 用作知识图谱+Agent 长期记忆的统一存储。

### 解法哲学
**「LLM as Simulator」**——不把 LLM 当计算器，而当社会模拟器：
- **做**：种子驱动（上传文档即可）、五阶段全自动化、双平台并行模拟（Twitter+Reddit）
- **不做**：不做手动参数配置（全 LLM 自动生成）、不做数据拟合式预测
- 核心信念：**群体涌现效应能产生超越任何单一模型的预测洞察**

### 战略意图
短期开源引爆（8 万 Stars 已实现）→ 中期产品化（盛大投资 3000 万，已招聘团队 mirofish@shanda.com）→ 长期成为「群体智能引擎」基础设施。AGPLv3 许可证表明商业化意图明确。

## 核心价值提炼

### 创新之处

1. **「社会模拟即预测」范式首创**（新颖度 5/5 | 实用性 3/5 | 可迁移性 4/5）
   将 OASIS 学术引擎包装为端到端预测产品，用 AI Agent 社会模拟替代传统预测方法。开源社区首创。

2. **GraphRAG + Agent 记忆统一架构**（新颖度 4/5 | 实用性 4/5 | 可迁移性 3/5）
   通过 Zep Cloud 将知识图谱构建、Agent 实时记忆更新、语义检索统一在一个 API 下，图谱随模拟进化形成「动态世界记忆」。

3. **LLM 全自动仿真参数化**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）
   从文档上传到模拟运行，所有中间步骤（本体设计、人设生成、参数配置）由 LLM 自动完成。含中国作息时间模型（五段活跃度系数）。

4. **双平台并行模拟**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）
   Twitter（快速传播）+ Reddit（深度讨论）同时运行，捕捉不同社交媒体生态下的群体行为差异。

5. **可回溯时序记忆图谱**（新颖度 3/5 | 实用性 4/5 | 可迁移性 3/5）
   Zep 的 valid_at/invalid_at/expired_at 机制赋予关系时间维度，支持分析舆情演变过程。

### 可复用的模式与技巧

1. **子进程 + 文件 IPC 异步任务模式**：用 subprocess.Popen + 文件系统通信隔离重型 asyncio 任务，避免与 Flask 同步模型的事件循环冲突
2. **LLM 驱动的动态本体设计**：LLM 分析文档 → 设计 schema → `type()` 动态创建 Pydantic 子类 → 注入图数据库
3. **ReACT 报告生成**：规划大纲 → 每章节循环调用工具（强制最少 3 次）→ 基于检索结果写作 → 分章节流式保存
4. **中国作息时间模型**：五段活跃度系数（凌晨 0.05 → 晚间 1.5），可复用于任何中国互联网用户行为模拟
5. **OpenAI 兼容 LLM 客户端封装**：三参数通用接入 + `<think>` 标签过滤 + markdown 清理

### 关键设计决策

1. **Zep Cloud 作为统一知识层**：一个 API 承载图谱存储+Agent 记忆+语义检索。极简但形成 SaaS 单点依赖（社区已出离线版回应）。
2. **子进程隔离模拟执行**：OASIS asyncio 与 Flask 不兼容，subprocess + 文件 IPC 是务实的隔离方案。
3. **五步骤线性流程设计**：图谱构建→环境搭建→模拟运行→报告生成→深度互动，降低用户认知负担但牺牲了灵活性。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | MiroFish | camel-ai/oasis (3.6K) | MiroFish-Offline (1K) | Polymarket |
|------|---------|--------|--------|--------|
| 定位 | 端到端预测产品 | 学术模拟框架 | 离线版 | 预测市场平台 |
| 用户 | 普通用户+决策者 | AI 研究者 | 技术用户 | 交易者+研究者 |
| 预测方法 | AI Agent 社会模拟 | Agent 模拟（库级别） | 同 MiroFish（本地） | 人类群体智慧 |
| UI | Vue 3 完整 Web UI | 无（纯代码） | 有（社区维护） | 完善交易 UI |
| 记忆层 | Zep Cloud (SaaS) | 无持久化 | Neo4j+Ollama（本地） | N/A |

### 差异化护城河
1. **产品化先发优势**：唯一将 OASIS 学术引擎包装为端到端产品的项目
2. **品牌效应**：38K Stars + 陈天桥投资 + 两次 GitHub Trending #1
3. **BettaFish 生态协同**：采集→分析→预测的完整产品链

### 竞争风险
- **Zep 单点依赖**：如果 Zep 变更定价/API，整个产品受影响（离线版已是社区应对）
- **预测质量无验证**：无回测机制，与 Polymarket 的市场定价机制相比缺乏验证闭环
- **LLM 成本不可控**：每次模拟需大量 API 调用（10+ Agent × 数十轮 × 双平台）

### 生态定位
在「AI 社会模拟预测」这一全新赛道占据首发位置。与 Polymarket（人类群体智慧）的本质差异在方法论层面：MiroFish 用 AI Agent 替代真人进行预测。哪种路径更准确尚无定论——**MiroFish 的价值在于开辟了这条新路径**。

## 套利机会分析
- **信息差**: 项目热度与成熟度严重不匹配——38K Stars 但仅 v0.1.x、单人开发、无测试。了解真实状态有助于判断投资/使用时机
- **技术借鉴**: (1) LLM 动态本体设计模式（type() 动态创建 Pydantic 子类）；(2) ReACT 报告生成的「规划-检索-写作」三阶段模式；(3) 子进程 + 文件 IPC 的异步任务隔离；(4) 中国作息时间活跃度模型
- **生态位**: 填补了「开源群体智能预测产品」的空白，是学术模拟工具到终端用户产品的桥梁
- **趋势判断**: 增长势头极强（两周 +13K Stars），但项目处于「网红→产品」的关键转化窗口。3000 万投资能否转化为团队扩建和产品稳定化是决定因素

## 风险与不足

1. **单人开发 Bus Factor = 1**：219/220 次提交来自一人，社区治理健康度仅 42/100
2. **Zep SaaS 单点依赖**：知识图谱+Agent 记忆+检索全绑定 Zep Cloud，免费额度消耗快（Issue #23/#156/#56）
3. **500/504 错误频发**：Issue #64（17 comments）、#174（16 comments）、#257 反映核心流程不稳定
4. **零测试覆盖**：仅 1 个测试脚本（test_profile_format.py），无单元/集成测试
5. **预测质量无回测**：与 Polymarket 不同，无结果验证机制，「预测」的可信度无法度量
6. **安全隐患**：CORS 全开放、API 无认证、traceback 直返前端
7. **LLM 成本不可控**：每次模拟消耗大量 API 调用，README 明确提示「消耗较大」
8. **AGPLv3 许可证**：对商业二次开发有强限制
9. **热度与成熟度不匹配**：38K Stars 但仅 v0.1.x/4 个月历史/文件系统存储

## 行动建议
- **如果你要用它**: 适用于探索性预测（舆情推演、创意沙盒），不适用于生产决策。推荐 Docker 部署，准备好 Zep API Key 和 LLM API Key（阿里百炼 qwen-plus）。如果不想依赖 Zep Cloud，考虑 [MiroFish-Offline](https://github.com/nikmcfly/MiroFish-Offline)（Neo4j+Ollama 本地栈）
- **如果你要学它**: 重点关注 (1) `backend/app/services/graph_builder_service.py` — LLM 动态本体设计 + Zep 图谱构建；(2) `backend/app/services/report_agent_service.py` — ReACT 模式报告生成；(3) `backend/scripts/run_parallel_simulation.py` — OASIS 双平台并行模拟；(4) `frontend/src/components/Step4Report.vue` — 最复杂的前端组件（5,150 行）
- **如果你要 fork 它**: (1) 替换 Zep Cloud 为 Neo4j（参考 MiroFish-Offline）；(2) 添加预测回测机制；(3) 加入 pytest 测试和 API 认证；(4) 将文件系统存储升级为数据库

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [https://deepwiki.com/666ghj/MiroFish](https://deepwiki.com/666ghj/MiroFish) |
| Zread.ai | [https://zread.ai/repo/666ghj/MiroFish](https://zread.ai/repo/666ghj/MiroFish) |
| 关联论文 | [OASIS: Open Agent Social Interaction Simulations with One Million Agents](https://arxiv.org/abs/2411.11581) |
| 在线 Demo | [mirofish.ai](https://mirofish.ai) / [GitHub Pages Demo](https://666ghj.github.io/mirofish-demo/) |
| Discord | [社区](http://discord.gg/ePf5aPaHnA) |
| Bilibili | [武大舆情推演](https://www.bilibili.com/video/BV1VYBsBHEMY/) / [红楼梦结局推演](https://www.bilibili.com/video/BV1cPk3BBExq) |
