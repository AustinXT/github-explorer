# OpenAI Codex 插件集开仓 3 个月：2.6K★、173 个插件、零测试的策展型仓库怎么治理

> GitHub: https://github.com/openai/plugins

## 一句话总结

OpenAI 官方维护的 **Codex 插件示例集与 Marketplace 事实源**——173 个自包含 plugin 子目录、174 条 marketplace 注册表项，承载 ChatGPT plugins 遗产并迁移到 Codex + MCP 协议，**正在定义 AI 插件生态的 form-factor**。

## 值得关注的理由

- **AI 插件 form-factor 定义者**：`interface`块 12 字段、marketplace 双状态机、`plugin.lock.json` 版本锁定——正在定义行业标准。
- **3 个月 2.6K★ 的官方背书**：开仓即爆发，star/fork ≈8.5（远高于行业基准 4-6），是策展型仓库的典型信号。
- **零测试、零重构的工程化反思**：553 个 markdown +174 个 manifest 怎么保证质量？这是个值得思考的反例。

## 项目画像

|维度 | 数据 |
|------|------|
| GitHub | https://github.com/openai/plugins |
| Star / Fork |2,589 /305（star/fork ≈8.5，策展型高围观低 fork）|
| 代码行数 |223,579 行（JS58.9% / Python32.8% / Standard ML2.0% / Shell1.4%）|
| 文件数 |4,248（含 561 个 YAML manifest、148 个 SVG 图标）|
| 项目年龄 |3.2 个月（首提交 2026-03-04）|
| 开发阶段 |密集开发（近 90 天 257 commits，月度 106→73→48→39 缓降）|
|贡献模式 | openai 组织主导，60 位贡献者，Ashwin Mathews 占 17.8% |
|热度定位 | 中等热度（2.6K★，官方背书 +爆发型增长）|
|质量评级 | 代码 N/A（无业务代码）/文档优秀 / 测试 无（合理缺位）|

## 项目展示

> 仓库 README 与官网均未嵌入展示性图片/视频，跳过此节。
>官方媒体入口：https://openai.com/index/chatgpt-plugins/（ChatGPT plugins 范式官方公告）+ https://platform.openai.com/docs/guides/codex/plugins（Codex 插件平台开发者文档）+ https://chatgpt.com/plugins（用户端入口与分类导航）。

## 作者视角：为什么存在这个项目

### 创始人/作者背景

仓库主是 openai **组织**而非个人——10.7 年历史、123K followers、255 个公开仓库。旗下头部项目矩阵清晰：codex（89.9K★，Rust 写的 CLI 运行时）/ openai-cookbook（74.1K★，示例与最佳实践）/ openai-agents-python（27K★，Agents SDK）/ symphony（25.2K★，Elixir 写的 Symphony）/ gpt-oss（20.1K★），plugins 以 2.6K★ 位列第 6。

核心维护者 60 人，头部 10 人占 60%+，是「核心少数 +社区」结构。Ashwin Mathews（17.8%占比）是头号贡献者，最近一次提交是 `[catalyst] use canonical plugin category #327`——直接揭示了当前路线图主线：**规范化 plugin 分类**。

### 问题判断

ChatGPT plugins 是 OpenAI2023-03 推出、2024-04 弃用的早期插件范式。弃用的真实原因不是产品失败，而是 **生态被 Anthropic 的 MCP（Model Context Protocol）协议重新定义**——MCP 用更标准的 JSON-RPC over stdio 把「模型 ↔工具」解耦成通用协议，OpenAI 不能不跟。

但 plugins 范式留下了三个不可丢弃的遗产：
1. **manifest as source of truth**（plugin.json 即合约）
2. **marketplace 中央注册**（UI/CLI/Gateway 共用）
3. **「Code 实体 ↔ NL 接口」的桥梁**（displayName、shortDescription、defaultPrompt 把工具描述给 LLM）

openai/plugins 这个仓就是承接遗产、并向 Codex + MCP 迁移的「过渡容器」——内部已经全面用 `.codex-plugin/plugin.json`命名空间，外部仓库命名仍是 `openai/plugins`保留可发现性。这是 **品牌迁移过渡期的产物**。

### 解法哲学

OpenAI 明确选择了：**让仓库承担「生态样板 + Marketplace 事实源」双重角色**，而不是只做 SDK 包装。

具体选择与不选择：
- ✅ **选择**：自包含 plugin 目录约定（manifest + skills + agents + assets +各自 LICENSE）——任何人都能直接 `cp -r` 一个 plugin 出来作为新仓库起点
- ✅ **选择**：marketplace.json 中央注册表（85 次改动 Top1，承担「事实唯一源」）——而非让 UI 层各自维护
- ✅ **选择**：plugin.lock.json 版本锁定（figma 示范，类似 Cargo.lock，锁定 vendored skill 的 git ref + sha256）
- ❌ **不选择**：单仓库 SDK +插件混杂（每个 plugin 测试仍在各自 SDK 仓）
- ❌ **不选择**：协议层独立（manifest schema 即协议）

### 战略意图

这个仓库是 OpenAI **「Codex 平台 → plugin 生态 → agent 应用」**链路里的 **生态样板层**——上游是 codex（89.9K★）作为运行时，下游是 agent 应用开发者作为消费者，本仓提供「参考实现 + Marketplace 事实源」。

商业化路径：不直接商业化，而是 **以生态主导权换商业护城河**——谁定义 plugin form-factor，谁就掌握 agent 应用迁移的「默认目标」。这与 Anthropic 押注 MCP 协议是同一种打法：**抢标准而非抢产品**。

> 官方文档说明：本仓库 homepage 为空（指向 openai.com），文档入口在 platform.openai.com。已通过 DeepWiki 完成架构补全。

## 核心价值提炼

### 创新之处

1. **`.codex-plugin/plugin.json` schema 作为 AI 插件 form-factor 定义**
 - `interface`块 12 字段（displayName、shortDescription、longDescription、developerName、category、capabilities、法务三件套、defaultPrompt、brandColor、composerIcon、logo、screenshots）是「把 Code 实体描述给 LLM」的标准方式
 - 新颖度 4/5 |实用性 4/5 | 可迁移性 5/5

2. **marketplace.json 双状态机设计**（installation × authentication 笛卡尔积）
 - AVAILABLE / INSTALLED_BY_DEFAULT × ON_INSTALL / ON_USE
-158 条 AVAILABLE/ON_INSTALL 为绝对主流（适合稳定插件）
-2 条 AVAILABLE/ON_USE 用于 sandbox 插件（延迟到首次使用时认证，避免 OAuth 风险）
-15 条加 `products:["CODEX"]` 白名单（限平台）
 - 新颖度 3/5 |实用性 5/5 | 可迁移性 4/5

3. **`plugin.lock.json` 版本锁定**（figma 示范）
 - 类似 Cargo.lock：vendored skill 的 git ref + sha256 锁定
 -解决了「skill 在 marketplace 里被升级导致行为漂移」的隐患
 - 新颖度 4/5 |实用性 4/5 | 可迁移性 5/5

4. **`evaluations/`目录**（notion 示范）的评测驱动开发范式
-评测用例 JSON schema（query + expected_behavior + success_criteria）
 - 把 prompt engineering 从「手工调」变成「跑评测看分数」
 - 新颖度 3/5 |实用性 4/5 | 可迁移性 5/5

5. **四层 prompt routing**（plugin.json → agents/openai.yaml → SKILL.md → references/）
 - 从粗粒度（plugin identity）到细粒度（reference data），分层描述工具
 - figma-use 用大写关键词 `MANDATORY` / `NEVER`强制 LLM 行为约束
 - 新颖度 3/5 |实用性 5/5 | 可迁移性 5/5

### 可复用的模式与技巧

1. **自包含 plugin 目录约定**——每个 plugin 都有 `agents/openai.yaml` + `skills/<name>/SKILL.md` + `commands/` + `assets/` + `README.md` + `LICENSE`，**任何人能直接 `cp -r` 一个 plugin 作为新仓起点**。适用场景：任何需要「多个独立组件共同注册到一个中心」的体系。

2. **plugin.lock.json 模式**——锁定 vendored 依赖的精确版本（git ref + sha256），避免 marketplace 升级导致插件行为漂移。适用场景：多 plugin 共用 skill 库的场景。

3. **evaluations/评测驱动开发**——把 LLM 行为的「期望」显式写成可验证的成功标准，而不是埋在 SKILL.md 散文里。适用场景：所有 prompt engineering 工作。

4. **mandatory/never 强制关键词**——用大写关键词在 SKILL.md 里强制 LLM 行为，比写「请不要」有效得多（LLM 对大写指令敏感度高）。适用场景：所有 prompt engineering 工作。

5. **脚手架工具的 name validation 三件套**（`.agents/skills/plugin-creator/scripts/create_basic_plugin.py`）：
 - `normalize_plugin_name` 转 lowercase hyphen-case（保证跨文件系统可移植）
 - `validate_plugin_name`限 64 字符（防止 URL 路径爆炸）
-幂等设计（force 参数，已存在时覆盖）

### 关键设计决策

```plain
决策: marketplace.json 作为中央注册表（而非每个 plugin各自注册）
问题:173 个 plugin怎么避免 UI/CLI/Gateway 各维护一份注册信息？
方案: .agents/plugins/marketplace.json 单文件2099 行，174 条 entry
Trade-off: 单文件易冲突（85 次改动 Top1），换来「事实唯一源」+原子更新
可迁移性: 高——任何多组件体系都适用中央注册表模式
```

```plain
决策: 测试缺位（refactor0% / test0%）
问题:553 个 SKILL.md +174 个 manifest怎么保证质量？
方案: 把测试责任下沉到各 plugin 的 SDK仓 + evaluations/评测驱动开发
Trade-off:失去「单仓 CI 全验证」保护，换来仓库轻量化（173 个 plugin几乎零业务代码）
可迁移性: 中——这种下沉测试的范式适合清单/策展型仓库，但不适合 SDK仓
```

```plain
决策:173 个 plugin全部自包含（每个 plugin 自带 LICENSE / README / agents）
问题:重复内容（每个 plugin都有 README）vs共享困难
方案: 自包含优于共享——牺牲 DRY换取「任何 plugin 可单独 fork出去」
可迁移性: 高——适合「生态丰富度优先于代码复用」的场景
```

## 竞品格局与定位

### 竞品对比矩阵

|维度 | openai/plugins | Anthropic MCP 协议 | openai/openai-cookbook |
|------|--------------|---------------------|----------------------|
|形态 |173 个 plugin manifest 集合 |协议规范 + server 实现 | API 调用片段示例集 |
|数量 |174 条注册项（plugin）| MCP server 注册在各自 repo |数百个 notebook 示例 |
| 主语言 | 多语言（manifest + 各 plugin SDK）| 多语言 SDK（Python/TS/Rust）| Python / JS notebook |
|维护方 | OpenAI 官方 | Anthropic +社区 | OpenAI 官方 |
|协议层 | `.codex-plugin/plugin.json` schema | JSON-RPC over stdio | 无统一 schema |
| Marketplace | marketplace.json 中央注册 | 多源（PulseMCP 等聚合站）| 无 |
| 版本控制 | plugin.lock.json（figma 示范）|协议层固定（无 schema 演化保护）| 无 |
|评测驱动 | evaluations/（notion 示范）| 各 MCP server 自管 | 无 |

### 差异化护城河

- **生态主导权**：OpenAI 旗下 codex（89.9K★）+ agents-python（27K★）+ plugins 形成的「运行时 + SDK +插件集」三件套，是 Anthropic MCP 仅有的「server 注册」所不具备的。
- **官方策展**：openai 亲自下场打磨头部 plugin（zoom809 次改动、nvidia506 次、figma393 次、cloudflare382 次），社区贡献者只是补 plugin——保证头部质量下限。
- **evaluations/评测驱动**：把 prompt engineering 变成可验证的工程实践，比 MCP server「手工调 prompt」领先一步。

### 竞争风险

- **最可能被替代的对象**：本仓库本身——若 Anthropic MCP 成为行业事实标准（已有 PulseMCP 等聚合站），OpenAI 可能直接弃用 plugins 仓，转向「Codex ↔ MCP bridge」模式（事实上已在 `.codex-plugin/plugin.json` 的 `interface`块里埋了 `mcp`字段兼容）。
- **最可能的替代路径**：当 Codex 真正支持「任意 MCP server 一键接入」时，plugins 仓的角色会从「plugin 集合」降级为「Codex 官方精选插件集」。

### 生态定位

在整个 AI agent 生态里，openai/plugins 扮演 **「Codex 平台的官方插件集 + Marketplace 事实源」**——不是 SDK，不是协议，而是 **「应用样板的策展层」**。填补了「SDK → 应用」之间的空白：SDK 给工具，plugins 仓给「工具怎么接入 Codex」的参考实现。

> 行业竞品数量少且定位错位：本仓填补的是「官方 plugin form-factor + Marketplace 中央注册」的双重空白——MCP 只定义了协议、cookbook 只给了示例片段、agents-python 只给了 SDK。三者都未覆盖「官方策展的 plugin 集合 +评测驱动开发示范」。

## 套利机会分析

- **信息差**：star/fork ≈8.5 远高于行业基准 4-6，说明开发者来「看范例」多、改源码少——意味着 **plugin manifest schema 与 evaluations/评测范式还没被广泛理解**，提前吃透这些模式的人能拿到定义权红利。
- **技术借鉴**：
 - 自包含 plugin 目录约定 → 直接复用到任何「多组件共注册」体系
 - plugin.lock.json →任何 vendored 依赖场景都适用（甚至比 Cargo.lock 更轻）
 - evaluations/评测驱动 → 你自己的 prompt engineering 工作立刻可用
- **生态位**：本仓填补了「**SDK → 应用**」之间的「官方样板层」空白——没有它，Codex 平台只有 SDK 没有应用示范，外部开发者无从下手。
- **趋势判断**：本仓正在「向 Codex + MCP 迁移」——3.2 个月龄、96.6% commits 集中在最近一季度、月度缓降但未衰减，属于 **早期扩展期的健康状态**。比 MCP server 仓（各自为政）有更强的「中央治理」后发优势。

## 风险与不足

- **零 refactor /零 test 提交**（refactor0.0%，test0.0%）——长期可能积累技术债。`marketplace.json`85 次改动历史里，若有一次手抖改错，没有 CI 兜底。
- **License 缺失**（`license_info: null`）——每个 plugin 内部可能各自有 LICENSE，但顶层未声明，给下游 fork 留下法律不确定性。
- **依赖 openai 组织势能**——本仓热度 2.6K★几乎完全来自 openai 品牌背书（codex89.9K★、cookbook74.1K★ 的关注外溢），社区自驱动能力未经验证。
- **evaluations/ 仅 notion 示范**——评测驱动开发范式尚未扩展到全部 550 个 skill，大部分 plugin 的 prompt 质量仍依赖手工调优。
- **品牌迁移风险**——仓库名仍是 `openai/plugins`，内部已全面用 `.codex-plugin/plugin.json`命名空间；某天若 OpenAI 决定放弃 `plugins` 这个品牌（如直接并入 codex 单仓），本仓的外部可发现性会骤降。

## 行动建议

> **一句话结论**：本仓的价值不在 plugin 数量，而在「**官方 form-factor + 中央 marketplace + 评测驱动开发**」三件套——提前吃透就能拿到 AI 插件生态的定义权红利。

### 如果你要用它

- **构建 Codex plugin**：直接 `cp -r plugins/figma/` 作为新 plugin 起点，按 `.codex-plugin/plugin.json` schema 填充，提交 PR 到本仓（27 个 open PR 显示活跃合并）。
- **接入外部服务**：参考 `plugins/{zoom,nvidia,figma,cloudflare}` 的 manifest + skills + agents 组合结构。
- **评测你的 prompt**：参考 `plugins/notion/evaluations/` 的 query + expected_behavior + success_criteria schema。

### 如果你要学它

- **重点关注**：
 - `plugins/figma/`（最高频改动 + plugin.lock.json 示范）
 - `plugins/notion/`（evaluations/评测驱动开发示范）
 - `.agents/plugins/marketplace.json`（2099 行注册中心，看 schema 设计）
 - `.agents/skills/plugin-creator/scripts/create_basic_plugin.py`（脚手架工具，300 行高质量 CLI）
 - `plugins/figma/skills/figma-use/SKILL.md`（MANDATORY/NEVER 大写关键词强制技巧）
- **不学什么**：零测试的工程化基线——这在 SDK 仓不可接受。

### 如果你要 fork 它

- **可改进的方向**：
1. 添加 `plugin.schema.json`顶层 schema 文件 + JSON Schema 校验 CI（避免 marketplace.json85 次改动里偶发手抖）
2. 添加 `marketplace.json` CI 校验（entry 数量、必填字段、URL 可达性）
3. 把 evaluations/ 从 notion 示范扩展为「每个 plugin 必须有评测」的硬性要求
4. 添加顶层 LICENSE（Apache2.0 或 MIT，明确法律授权）
5. 把 plugin.lock.json 从 figma 示范升级为「全部 plugin 强制要求」

### 知识入口

|资源 |链接 |
|------|------|
| DeepWiki | https://deepwiki.com/openai/plugins（已收录，覆盖 overview/architecture/plugin anatomy/marketplace/evaluation/glossary 全章节）|
| Zread.ai | 未收录（403，可能需要登录）|
|关联论文 | 无（仓库非研究产出）|
| 在线 Demo | https://chatgpt.com/plugins（用户端入口与分类导航）+ https://platform.openai.com/docs/guides/codex/plugins（开发者文档）|
