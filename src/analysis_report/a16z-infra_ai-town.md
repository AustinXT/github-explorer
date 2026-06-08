# 万星小镇的 1KB 玄学：a16z × Convex 的 AI Town 凭什么让 8 个 NPC 自己聊出性格

> GitHub: https://github.com/a16z-infra/ai-town

## 一句话总结

a16z 联手 Convex 团队把 Stanford「Generative Agents」论文搬进工程化形态的 AI NPC 虚拟小镇 starter kit——10k stars、Ian Macartney 一人主导 40% commit、0 美元本地 LLM 跑通、真人可围观可下场，本质是 Convex 平台借 a16z 渠道做的一次「reactive 后端 + LLM agent 范式」的旗舰销售物料。

## 值得关注的理由

- **三层解耦是真货**：engine / game / agent 三层互不依赖，**换皮换模型换世界各取所需**——是 2024 年「如何用 reactive DB 写实时多人 AI 应用」最干净的参考实现。
- **反思型记忆系统有论文级工程实现**：importance 阈值 500 + LLM reflection 总结，NPC 行为有「回忆 / 自省 / 性格演化」能力，不是「向量 RAG 拼 prompt」那种。
- **生态护城河 0 美元 5 分钟跑通**：Convex 平台 + Pinokio 一键安装 + Fly.io 部署 + 默认 Ollama 本地推理，新人 clone 后到看到 8 个 NPC 互相聊天不超过 5 分钟——这是 99% AI agent 沙盒项目做不到的体验。

## 项目展示

![AI Town screenshot](https://github.com/a16z-infra/ai-town/assets/3489963/a4c91f17-23ed-47ec-8c4e-9f9a8505057d)

*小镇全景：8 个 AI 角色（伊索、克劳斯、玛雅等）在一个 2D 像素世界里走动、聚集、发起对话。玩家（默认 `Me`）可以走进 NPC 触发对话、点击观察 AI 之间的自发行为。*

在线 Demo: <https://www.convex.dev/ai-town>（Convex 官方部署的 live demo，无需登录即可围观）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/a16z-infra/ai-town |
| Star / Fork | 9,970 / 1,106 |
| 代码行数 | 13k 行业务代码（TypeScript / JavaScript / TSX），总 29.7k 行（含 15.7k JSON 数据） |
| 项目年龄 | GitHub 仓库 35 个月（首 commit 2018-06-04，a16z 接管 2023-07） |
| 开发阶段 | 低维护（近 30/90 天 0 commit，近 365 天 3 commit） |
| 贡献模式 | 单人主导（Ian Macartney 占 40.3%，Top 3 占 69.6%） |
| 热度定位 | 大众热门（即将破万星，月增 100+ stars） |
| 质量评级 | 代码[良好] 文档[优秀] 测试[不足] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Ian Macartney 是 Convex 早期工程师，也是这个仓库的实质主导者（Top 1 贡献者，40.3% commit）。a16z-infra 这个组织账号维护着被投公司 demo 矩阵（其他代表作：companion-app 5.9k★、ai-getting-started 4.1k★、llama2-chatbot 1.4k★）。所以 ai-town 本质是 Convex 团队借 a16z 渠道发布的「Convex 平台旗舰 demo」——Ian 是技术决策者，a16z 是流量放大器。

其他核心贡献者包括 Sujay Jayakar（Convex CTO）和 Yoko Li，三人在 2023-07/08 单月 push 了 447 commit（占仓库总 commit 39%），是典型的「按发布窗口集中发力」节奏。

### 问题判断

Ian 看到了两个叠加的机会：

1. **学术→工程的真空**：Stanford 2023 年 4 月放出的「Generative Agents: Interactive Simulacra of Human Behavior」论文引爆了「会记忆、会反思、会自发聊天的 NPC」叙事，但原作者 joonspk-research/generative_agents 用 Python + Jupyter + Berkeley 仿真器在单机跑，**离多人实时、地图可扩展、记忆可持久、模型可换的工业级 demo 还差十万八千里**。
2. **平台演示的饥渴**：a16z 投了 Convex（一个 reactive TypeScript 后端 + 向量搜索 + 事务 + scheduled functions 的 BaaS 平台），Convex 最缺一个「让投资人/开发者一打开就觉得『这就是未来』的杀手级 demo」。reactive 订阅、向量搜索、事务、scheduled functions 四个特性正好是 AI agent 范式的天然秀场：
   - reactive 订阅 → 多人围观 NPC 行为不用写一行 WebSocket
   - 向量搜索 → NPC 反思型记忆系统的天然落地点
   - 事务 + scheduled functions → 仿真引擎的 tick/step 调度天然落地点
   - 沙箱化 + dashboard → 「世界可归档、可重启、可 kick」的人机协作流

时机的选择：2023 年 8 月正值 Stanford 论文放上 arXiv 不到半年，全行业都在做 AI agent 复制，Convex 提前 6 个月把「我们能做这个」摆在 a16z 网站首页——是 a16z 给被投公司导流 + 给 LP 演示「AI + 元宇宙」叙事的双赢。

### 解法哲学

- **平台暴露而不是封装**：`convex/util/llm.ts` 顶部那行「// That's right! No imports and no dependencies 🤯」是 Convex 团队招牌式设计哲学的注解——把 LLM 调用做成「你改哪一行就走哪个 LLM」的最低门槛切换器。Ollama / OpenAI / Together.ai 全部通过环境变量 + 一个 `EMBEDDING_DIMENSION` 常量切换。
- **可读性 > 性能 > 抽象**：引擎用 60Hz tick + 1Hz step 的二级调度（`tickDuration = 16`、`stepDuration = 1000`），是不计成本换「代码好读」。换做 Erlang/Elixir 仿真框架不会用 60 这种整齐数字，但 Convex 选了整齐数字给读者看。
- **承认局限、不藏**：ARCHITECTURE.md 末尾主动列出 4 条 limitations（active game state 必须放得进内存 / 大流量 input 不适合 / 1.5s 输入延迟 / 单线程 engine 算力受限），是工程诚实，也是 starter kit 必备的「哪些别学我」声明。
- **明确不做什么**：
  - **不做 SaaS 版本**：`convex/util/llm.ts` 把 4 个 LLM 提供商全做成环境变量切换，等于主动放弃「我来做 LLM 网关」的可能性——Convex 想卖「后端」而不是「agent 网关」，让所有人都能换 LLM 反而对 Convex 有利。
  - **不做 release/tag**：仓库 0 tag、0 GitHub Release、`package.json` 不走 semver，是 demo 仓库的标志性证据。
  - **不绑 OpenAI**：默认 `chatModel = 'llama3'` + `embeddingModel = 'mxbai-embed-large'`（Ollama），完整 Docker compose 支持（连 Windows WSL2 + socat 桥接都写在 README 60 行 troubleshooting 里）。

### 战略意图

**Convex 平台的旗舰销售物料**。和 Convex 文档站首页的「vector search demo」是同一级别。

a16z 在 2023 年夏做了「明星 demo 项目」矩阵（companion-app、ai-getting-started、llama2-chatbot、ai-town），这些仓库的共同特征是：**为被投公司做导流，而不是为 a16z 自己抽税**。ai-town 是其中「AI agent 示范」那个——告诉开发者「用 Convex 写 LLM 实时应用，就是这么简单」。

**商业化路径**：无 SaaS，无 enterprise 版，无 paid support——开源策略是 genuinely open（MIT + 全代码可改可商用），不是 open-core。代价是 a16z 不能从 fork 里抽税；收益是 Convex 平台直接被宣传。

## 核心价值提炼

### 创新之处

按新颖度×实用性排序：

1. **「engine / game / agent」三层解耦的 reactive 仿真框架**（新颖度 3/5，实用性 4/5，可迁移性 4/5）
   - `convex/engine` 不知道有 NPC，`convex/aiTown` 不知道有 LLM，`convex/agent` 不知道有地图。三层各自 100% 可独立测试/复用。Stanford Smallville 没有这种解耦，所以难以做衍生品。
2. **反思型记忆 = 向量检索 + LLM 总结高阶洞察**（新颖度 3/5，实用性 5/5，可迁移性 5/5）
   - `convex/agent/memory.ts:325-397` 的 `reflectOnMemories` 拿最近 100 条记忆，sum importance，超 500 触发一次 LLM「给我 3 条高阶洞察」，JSON 输出写成新记忆条，下一次相似度检索会同时被命中。区别于「向量 RAG 拼 prompt」，这种 reflection 模拟了论文里的「心智状态」层。
3. **HistoricalObject 二进制压缩（Quantize + Delta + RLE + Varint + xxHash32）**（新颖度 4/5，实用性 4/5，可迁移性 3/5）
   - `convex/engine/historicalObject.ts` 限定最多 16 个数值字段，先 quantize 浮点→整数，再 deltaEncode（差分），再可选 runLengthEncode（匀速运动就一个 RLE 就够），再 varint（小整数用 1 字节），最后 xxHash32 配置头。**1KB 左右就能装下 1 个 NPC 1 秒的 60 帧位置轨迹**。
4. **沙箱运维命令集（stop / resume / kick / archive / wipeAllTables）+ 3 个 cron**（新颖度 3/5，实用性 5/5，可迁移性 5/5）
   - 完整覆盖「演示调试 + 长期自治」。README 单独一节「How to stop the back end」系统讲。**所有「需要 demo 给非工程人员看的 AI 应用」都该有这套**。
5. **generation number 防 race + engine 单步批处理**（新颖度 3/5，实用性 4/5，可迁移性 4/5）
   - `expectedGenerationNumber` 模式（`convex/engine/abstractGame.ts:78-84`）。每次 `runStep` 把自己看到的 `engine.generationNumber` 作为参数带进 action；引擎被 kick 时 `generationNumber += 1`，正在跑的 step 一回到 `saveStep` 就会因 generation 不匹配而立刻 fail。**完全不用考虑 race / lock / 事务冲突**，可以放心写 `Player.tick` 这种带 mutate 状态的同步函数。
6. **默认本地 Ollama + 完整 Docker 桥接文档**（新颖度 2/5，实用性 5/5，可迁移性 5/5）
   - 0 美元 0 联网跑通完整 demo，是「demo 0 门槛」的关键。
7. **`useHistoricalTime` 自适应时间同步（0.8x / 1.2x）**（新颖度 3/5，实用性 4/5，可迁移性 4/5）
   - 服务端 step 边界 → 客户端 0.8x 慢放（buffer 不够）或 1.2x 快进（buffer 太多）平滑追平。

### 可复用的模式与技巧

1. **Convex + LLM agent 三件套**：`internalAction` 异步调 LLM → `insertInput` 回写 engine → `inProgressOperation` 串行化。适用场景：任何「主循环 + 长耗时副作用」agent（游戏 NPC、客服机器人、DevOps 自动化）。
2. **反思型记忆系统**：向量存储 + importance 阈值 + LLM reflection。适用场景：长期 agent、个性化 agent、行为可解释 AI。
3. **engine / game / agent 三层解耦**：Convex 上跑「可换皮肤的实时多人仿真」。适用场景：所有 Convex 实时游戏 / 模拟器。
4. **PixiJS + React 混合前端**：@pixi/react 让 React 写游戏（`src/components/Game.tsx:50-64`），pixi-viewport 处理缩放拖动，React 状态驱动 UI 高亮。适用场景：地图类 + UI 协作类应用。
5. **historical buffer 回放**：60Hz tick + 1Hz step + 客户端 0.8x/1.2x 自适应。适用场景：所有 serverless 高频状态同步。
6. **沙箱运维命令集**：`stop / kick / resume / archive / wipe` 五件套 + crons。适用场景：所有「需要给非工程人员看 demo」的 AI 应用。
7. **多 LLM 抽象（环境变量 + 维度校验 + 退避）**：`getLLMConfig` + `EMBEDDING_DIMENSION` 常量 + `retryWithBackoff`。适用场景：所有需要支持 2+ LLM provider 的项目。
8. **HistoricalObject 数值压缩**：限定 16 字段 + Quantize + Delta + RLE + Varint。适用场景：高频数值同步（多人游戏位置、IoT 传感器流、协作白板笔迹）。

### 关键设计决策

**1. 引擎单线程 + generation number 防 race**
- **问题**：Convex scheduled function 可能多个同时跑同一个 world 的 step，怎么避免重复执行？input 来了 engine 空闲超过 1 分钟，要立即触发、然后被 idle timeout 取消，怎么不出 race？
- **方案**：`expectedGenerationNumber` 模式（`convex/engine/abstractGame.ts:78-84`），单线程 step 循环，被 kick 时 `generationNumber += 1` 让正在跑的 step 在 `saveStep` 立刻 fail。
- **Trade-off**：失去多核并行能力（README 明说「做不了几千个对象同时交互」）。换来：**完全不用考虑 race / lock / 事务冲突**，可以放心写同步函数风格的 `Player.tick`。
- **可迁移性：高**。任何「确定性仿真 + 用户输入」场景（回合制策略、RTS、棋盘、模拟经营）都能搬这套。

**2. tick / step 二级调度：60Hz 内部时间 + 1Hz 落库**
- **问题**：游戏要 60fps 流畅动画，但 Convex mutation 太贵，每秒 60 次 mutation 不可行。
- **方案**：`tickDuration = 16ms` / `stepDuration = 1000ms` / `maxTicksPerStep = 600`（`convex/aiTown/game.ts:47-50`）。`runStep` 内部跑最多 60 个 tick，但只把整个 step 的最终状态写一次 DB。客户端拿到的不是「step 末态」，而是 step 内每 tick 的历史 buffer（HistoricalObject 打包的二进制）。
- **Trade-off**：客户端需要「插值回放」才能流畅显示（`useHistoricalTime` 的 0.8x/1.2x 自适应速率）。换来：60x mutation 数量降低。
- **可迁移性：高**。任何「高频状态 + 低频落库」的实时应用（多人白板、协作 IDE、模拟器）都能用。

**3. 反思型记忆 = importance 阈值（500）+ LLM 总结高阶洞察**
- **问题**：NPC 不能只「用向量相似度取前 3 条记忆」——这种 RAG 会丢失**抽象洞察**（「我最近总跟爱抱怨的人聊天」）。
- **方案**：`reflectOnMemories`（`convex/agent/memory.ts:325-397`）拿最近 100 条记忆，sum importance，超 500 触发一次 LLM 总结，JSON 输出写成新记忆条。`MEMORY_OVERFETCH = 10` 多拉 10x 候选，再 `rankAndTouchMemories` 按「相关性 + 重要性 + 时新性」线性归一打分排序。
- **Trade-off**：reflection 是「全量 LLM 调用」，高峰期会成成本大头。JSON 解析失败直接 `console.error` 吞掉（`memory.ts:391-395`）。换来：NPC 行为有「回忆 / 自省 / 性格演化」能力。
- **可迁移性：高**。任何「长时记忆 + 性格化」的 LLM agent 都适用，重要度阈值 / 反思 prompt 都可以参数化。

**4. 沙箱运维 = 5 个 `npx convex run testing:xxx` 命令 + 3 个 cron**
- **问题**：演示 + 演示给投资人 + 自托管的人，最常做的操作是「卡了踢一下」、「世界废了归档重启」、「调试时停止」。
- **方案**：`convex/testing.ts` 集中 5 个命令（wipeAllTables / stop / resume / kick / archive）+ `convex/crons.ts` 三个定时（5 分钟无心跳停、引擎死 2 倍 action 时间踢、每天 4:20 UTC 清 2 周前的旧 inputs / memories / memoryEmbeddings）。
- **Trade-off**：命令全部以 mutation 暴露，生产环境误调很危险（README 提示「wipeAllTables 会清掉你所有数据」）。换来：开发者调试/演示 5 分钟学完。
- **可迁移性：高**。所有「长期运行的多人应用」都该有这套「按需停/踢/归档/清空」。

**5. LLM 抽象 = 环境变量 + `EMBEDDING_DIMENSION` 编译期常量 4 选 1**
- **问题**：开发者会问「我想用 Claude / Groq / 私有 LLM / Ollama」——支持 4 个写 4 份代码？支持 1 个又不够。
- **方案**：`getLLMConfig` 按 `OPENAI_API_KEY` / `TOGETHER_API_KEY` / `LLM_API_URL` / 默认 Ollama 的优先级返回 LLMConfig（`convex/util/llm.ts:46-110`）；`EMBEDDING_DIMENSION` 是编译期常量（Ollama=1024 / OpenAI=1536 / Together=768），**不一致就 throw**；`chatCompletion` / `fetchEmbeddingBatch` 内部 `retryWithBackoff` 三次退避（1s/10s/20s + 100ms jitter）。
- **Trade-off**：4 个 provider 之外的「非 OpenAI 兼容 API」必须自己写分支。embedding 模型一换就要 `wipeAllTables` 重来（README 明确警告）。换来：4 个 LLM 提供商开箱即用，**写 demo 的人不会被绑死**。
- **可迁移性：高**。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | ai-town | generative_agents (Smallville) | letta (MemGPT) | AgentVerse |
|------|---------|-------------------------------|----------------|------------|
| 学术完整 | 弱（实现多于论文） | 强（论文级 prompt 公开） | 中 | 强（多 benchmark） |
| 工程化 / 多人实时 | **强**（PixiJS + Convex reactive） | 弱（Python 单机） | 弱（无世界层） | 弱（任务求解） |
| 世界 / 地图 | **有**（Tiled 地图 + 角色 sprite） | 有（Mesa 仿真） | **无** | 无 |
| LLM 切换 | **4 provider 开箱**（Ollama/OpenAI/Together/Any OpenAI 兼容） | Python 脚本 | 多 provider | 多 provider |
| 反思型记忆 | **有**（importance 500 + reflection） | 有（论文原始） | 有（in-context + 外部工具） | 无 |
| 本地 LLM 启动 | **是**（默认 Ollama，0 美元跑通） | 否 | 否 | 否 |
| 0 门槛上手 | **5 分钟**（clone + npx convex dev） | 数小时（Python 配环境） | 30 分钟（pip install） | 30 分钟 |
| 商业化 | MIT 全开源 | Apache 2.0 | AGPL / 商业双许可 | Apache 2.0 |

### 差异化护城河

- **生态护城河**（最深）：Convex 平台背书 + a16z 品牌 + Pinokio 一键安装 + 完整 Docker compose + Fly.io 部署文档。**竞争对手很难复制「0 美元 + 5 分钟跑通」的体验**。
- **技术护城河**（中等）：engine / game / agent 三层解耦是真正的设计遗产。Stanford Smallville 没有这种解耦，所以难以做衍生品。
- **信任护城河**（中等）：MIT + 完整测试 + 552 行测试覆盖（虽然只覆盖 util 层）+ ARCHITECTURE.md 18KB（堪比一篇论文）+ 主动列 4 条 limitations 的工程诚实。

### 竞争风险

- **最可能替代它的是 Convex 自己的下一个 demo**——平台公司每 6-12 月会推一个「最新特性示范」项目（聊天/搜索/任务流），AI Town 是 2023 年那个「AI agent 示范」，2025 年如果 Convex 出「多模态 agent 示范」，AI Town 流量会自然衰减。
- **letta** 如果未来加上「世界 SDK」会直接威胁——letta 的有状态 agent 运行时是生产级，加一层世界抽象就能覆盖 AI Town 的核心场景。
- **Pinokio 分发版** 是「非竞品而是分销」，不算竞争。

### 生态定位

**「AI 虚拟世界的入门模板 + Convex 平台的旗舰 demo」**。

它不是工具，不是框架，不是 SaaS——是**标准化的「如何用 Convex 做实时多人 AI 应用」的参考实现**。在生态中扮演「教科书 / starter kit」的角色：开发者读它的代码学 Convex + LLM agent 范式，企业要搭类似系统时把 engine / game / agent 三层直接 fork 出去改。

填补的空白：「AI agent + 沙盒 + 全栈可部署」这个交集几乎无对手——Smallville 是学术、AgentVerse 是研究、letta 是运行时——AI Town 是**唯一把「可玩的虚拟世界 + LLM 推理 + 多人后端」三者打通的**。

## 套利机会分析

- **信息差**：不存在套利空间——这是现象级 demo（同类对比：comfyui、stable-diffusion-webui 量级）。价值不在「被低估」，而在「借 demo 卖平台」。
- **技术借鉴**：8 个可复用模式都能直接搬到自己的项目（见上文）。最有价值的是「反思型记忆系统 + 沙箱运维命令集」——这两个在任何长期运行的 AI agent 项目里都该有。
- **生态位**：「AI 虚拟世界入门模板 + Convex 旗舰 demo」。如果你要做的项目是「多人 + 实时 + LLM」，这套架构是几乎可以直接 fork 的起点。
- **趋势判断**：项目本身已处于低维护期（近 30/90 天 0 commit），但 Convex 平台特性在持续演进（最新向多模态、cron 增强、cron 触发 scheduled functions 等方向）。**对读者的真正价值是读代码学范式，而不是部署它**。

## 风险与不足

- **无 CI/CD、无 CHANGELOG、无 release**：没有 `.github/` 目录、没有 GitHub Actions；Docker compose + Vercel + Fly.io 部署是「手动档」；接手者需自己锁定 commit。
- **核心 engine / aiTown / agent 全无单元测试**：只有 `convex/util/` 和 `convex/engine/historicalObject.test.ts` 共 552 行测试。**这是一个 starter kit 性质的 demo 的硬伤**——读者改完代码没有 regression 保护。
- **错误处理有「demo 优先于生产」特征**：
  - `reflectOnMemories` 解析失败 `console.error` 吞掉（`memory.ts:391-395`），可能让 NPC 永久卡在「同一批记忆反复 reflection」循环
  - `stop` 失败仅 `console.log`（`testing.ts:79-82`），UI 端看不到错误
  - `EMBEDDING_DIMENSION` 编译期常量 + 向量索引维度改一个忘改另一个就会立刻 schema mismatch，**代码没强校验**
- **本地起步门槛仍高**：issue #256「No default world found」、#259「clicking 'interact' gives no response」、#263/#258/#251「ollama / 本地 LLM 接入被禁」——三个 Top issue 全是部署细节，README 没说清的隐性架构约定（Convex 部署时序、前端 vs 引擎启动顺序、Docker↔host 网络桥接）。
- **单线程 engine 算力受限**：README 明说「做不了几千个对象同时交互」，扩展性天花板明确。
- **OpenAI 绑定深**：切换 Ollama 等本地 LLM 仍痛点明显（issue #251/#258），不是「开箱即用」的程度。
- **贡献者高度集中**：Top 1 Ian Macartney 占 40.3%，Top 3 占 69.6%——社区贡献微弱，Ian 一旦离开，项目易陷入长期停滞。

## 行动建议

- **如果你要用它**：**谨慎**。无 release / 无 CI / 核心逻辑无测试，意味着你要 fork 后自己加测试和 CI，否则每次升级都是赌博。**适合做 demo / 学习材料 / 短期项目**，不适合做生产基座。
- **如果你要学它**：**重点关注 4 个文件**：
  - `ARCHITECTURE.md`（18KB，堪比论文，先读这个）
  - `convex/agent.ts`（103 次修改，最热核心，AI agent 主循环）
  - `convex/lib/memory.ts`（反思型记忆系统的工程实现）
  - `convex/engine/abstractGame.ts`（单线程 + generation number 防 race + 60Hz tick/1Hz step 二级调度）
  
  读完后看 `convex/util/llm.ts`（703 行，4 LLM 提供商适配的核心复杂度集中地）。
- **如果你要 fork 它**：**最有价值的改进方向**：
  - **加核心 engine / aiTown / agent 测试覆盖**（当前只有 util 层 552 行测试）
  - **把 `reflectOnMemories` 错误处理从 `console.error` 升级为写回状态 + 告警**
  - **用 LangSmith / Helicone 这类 LLM observability 工具接进去，reflection 调用成本可视化**
  - **补充一个真实的「世界编辑器」UI**——当前 data/characters.ts + Tiled 地图都是手改 JSON，门槛太高
  - **用 Letta 替换或对接作为 agent 运行时**——letta 的有状态 agent 运行时比当前自研更生产级，嫁接 letta 可获得「LLM agent 操作系统」能力同时保留三层解耦架构

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [https://deepwiki.com/a16z-infra/ai-town](https://deepwiki.com/a16z-infra/ai-town)（已收录，2025-04-18 indexed，含 Overview/Backend/Agent/LLM/Frontend/Testing/Deployment 七大块） |
| Zread.ai | 未确认（403 拒绝访问） |
| 关联论文 | [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/pdf/2304.03442)（Stanford 2023，ai-town 的灵感来源） |
| 在线 Demo | [https://www.convex.dev/ai-town](https://www.convex.dev/ai-town)（Convex 官方部署 live demo，无需登录即可围观） |
| ARCHITECTURE.md | [https://github.com/a16z-infra/ai-town/blob/main/ARCHITECTURE.md](https://github.com/a16z-infra/ai-town/blob/main/ARCHITECTURE.md)（18KB 论文级设计文档，**必读**） |
