# 4 个月 8305 star 的开源自进化引擎 evolver：拆开看 85% 是混淆闭源

> GitHub: https://github.com/EvoMap/evolver

## 一句话总结

evolver（EvoMap）号称「GEP 驱动的 AI agent 自进化引擎」，用 Genes/Capsules/Events 做可审计的经验进化，4 个月冲到 8305 star。但拆开看：它是一个「GPL 开源外壳 + 闭源变现核」的商业化项目——src/ 里 85% 的字节是 javascript-obfuscator 混淆的闭源内核，真正的协议还藏在仓库外的闭源 SDK 与一个未暴露的 Rust 运行时里；可审计的开源部分只有约 1MB 的 I/O 胶水。它有真实传播力和扎实的外壳工程，但「开源自进化」这个标签需要打上引号。

## 值得关注的理由

1. **「开源外壳 + 闭源内核」的典型样本**：README 自认「核心进化引擎模块以混淆形式分发以保护知识产权」。这与 GPL-3.0「分发便于修改的首选形式（源码）」的精神直接冲突——研究开源商业化边界与「伪开源」现象的好案例。
2. **外壳工程确有干货，值得借鉴**：不可信命令沙箱（node-only 白名单 + 封禁 eval flag + 引用真实 CVE）、schema 单一真相源治理（create/validate 对 + 枚举集中根治漂移）、本地邮箱 Proxy 解耦鉴权、内容寻址 + 拒绝伪造成功——这几处是真功夫。
3. **现象级增长背后的运营机制值得拆解**：8305 star/4 个月里，混合了真实病毒传播（前作 ClawHub 首发 10 分钟登顶）、与 Nous Research 的「Hermes 抄袭」公开争议营销、以及邀请码/积分/排行榜/拉新激励 + 发布机器人灌库——是「增长黑客 + 争议营销」的活教材。

## 项目展示

![Evolver Cover](https://raw.githubusercontent.com/EvoMap/evolver/main/assets/cover.png)

evolver 项目封面。可交互平台见官网 evomap.ai（含 Capsule Market、积分排行榜、Worker 池）。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/EvoMap/evolver（官网 https://evomap.ai） |
| Star / Fork | 8,305 / 794（Watcher 36、open issues 4） |
| 代码行数 | 名义 5.9 万行 JS（95.7%），**但 src/ 实测 85% 字节是 `_0x` 十六进制花指令混淆的闭核**（50 文件 5.68MB），可读外壳仅约 1MB（15%）；协议还在仓库外的闭源 npm SDK（@evomap/atp-sdk、@evomap/gep-sdk）与一个未暴露的 Rust 运行时 EvoX 里 |
| 项目年龄 | 约 1.7-4 个月（git 历史被压缩，首 commit 即「Release v1.66.0」，GitHub 建库 2026-02-01，最近提交 2026-06-08） |
| 开发阶段 | 密集开发（高频自动发布，81 tag/v1.88.4） |
| 贡献模式 | 单一核心 + 发布机器人（9 贡献者；**102 commit 中 80 个是 evolver-publish 发布机器人**，真人核心 autogame-17 仅 13） |
| 热度定位 | 现象级爆发（约 100 star/天，但含明显运营催化，非纯口碑） |
| 质量评级 | 可读层代码[良] 文档[优但过度包装] 测试[仅覆盖外壳] 开源透明度[差] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

主创张昊阳（GitHub autogame-17，知乎多篇自述确认），公司实体 EVOMAP PTE. LTD.（新加坡）。项目起家于前作 ClawHub（OpenClaw 插件生态）被封杀后「48 小时另起炉灶」——代码里留有血脉痕迹（SKILL.md frontmatter 仍带 clawdbot 元数据）。从「单 agent 技能分发」升级到「agent 之间的进化经验网络」。叙事能力极强，深谙中文 AI 社区传播。

### 问题判断

要解决的问题是：把 AI agent 运行中习得的经验（修过的 bug、优化套路）从一次性 prompt 微调，沉淀为可复用、可继承、可审计的结构化资产。作者论点（援引自家 arXiv 论文）是——面向文档的 Skill 包控制信号「稀疏且不稳定」，紧凑的 Gene 表示是更好的经验载体。所以不做「更长的 SKILL.md」而做 Gene 协议。

### 解法哲学

三个核心决策都服务于商业化而非纯开源：
- **GPL 外壳 + 混淆闭核**：README 直接写明核心引擎以混淆形式分发保护 IP——开源是获客漏斗，真正的智能（选择/生成/蒸馏/记忆/变异）混淆保护。
- **prompt 生成器而非代码改写器**：刻意保留 human-in-the-loop（`--review`），只产 GEP prompt + 资产、不自动改源码——既是安全卖点，也规避了自动改码的责任风险。
- **Freemium 网络 + 积分经济**：核心离线免费，Hub（技能市场/Worker 池/Validator 共识/ATP 任务交易）联网才解锁，靠 credits/reputation/leaderboard 形成飞轮。

### 战略意图

抢占「agent 自进化 / 经验继承网络」的叙事卡位。把 Hermes Agent（Nous Research）抄袭争议同时用作两件事：营销话题 + 「转向 source-available」的正当化理由。商业意图明确：**开源是冷启动与信任背书，闭源混淆 + 外部 SDK + 积分经济才是变现内核**。还把生物学隐喻（Genome/Gene/Capsule/Mutation）与区块链叙事（去中心化 validator/共识/credits/内容寻址）系统性迁移过来。

## 核心价值提炼

> 诚实分层：真功夫在可读外壳的几处工程实践；GEP schema 设计扎实；但「自进化」名不副实（实为结构化经验复用 + prompt 资产化，非模型层进化），核心智能混淆闭源不可审计。

### 创新之处

1. **GEP 可审计进化协议（Gene/Capsule/Event 三件套）** — Gene = 可复用策略模板（signals_match + strategy 步骤 + constraints + validation），Capsule = 带 outcome/confidence/blast_radius 的验证过技能包，Event = append-only 审计流。schema 设计扎实可读。**真创新**，但「自进化」名不副实。新颖度 4/5、实用性 4/5、可迁移性 3/5。
2. **不可信命令沙箱（全仓库最值得借鉴的真功夫）** — `sandboxExecutor.js` 硬白名单仅 `node`，封禁 `-e/--eval/-r/--require/--loader/--import` 等 eval 化 flag，拒绝 shell 元字符，fresh temp dir + 凭据剥离 env + 超时，明确引用真实安全公告 GHSA-jxh8-jh77-xh6g（曾把 npm/npx 移出白名单防供应链 RCE）。新颖度 3/5、实用性 5/5、可迁移性 5/5。
3. **prompt 生成器而非代码改写器** — 只产 GEP prompt + 资产，host runtime（Claude Code/Cursor/Codex/Kiro/opencode/OpenClaw 六家 hook）决定是否执行。真实且诚实的设计取舍（安全 + 责任规避兼得）。新颖度 3/5、实用性 4/5、可迁移性 4/5。
4. **skill2gep 反向蒸馏（SKILL.md + 真实执行 → Gene+Capsule）** — 把任意 procedural skill 逆向成 GEP 资产；难得的是**代码注释比 README 诚实**，反复标注论文结论仅适用「45 个科学代码场景/特定模型」、泛化是「假设而非已证明结果」。新颖度 4/5、实用性 3/5、可迁移性 3/5。
5. **「自进化引擎」叙事 + 自引用 arXiv 论文** — **主要是包装**：所谓 self-evolution 实为结构化经验复用 + prompt 资产化（非模型层进化），arXiv 论文是自家发表用于背书，README 高调引用「CritPt 9.1%→18.57%」而代码内部却 hedging。新颖度 2/5、实用性 1/5、可迁移性 1/5。

### 可复用的模式与技巧

1. **Schema 单一真相源 + create/validate 对**：`createGene()`（合并默认+规范化，幂等、数组深拷贝防污染）+ `validateGene()`（发布前抛错）+ `protocol.js` 统一所有「既在校验代码又在 LLM prompt 模板里」的枚举，根治枚举漂移——任何 LLM prompt schema 与运行时校验需保持一致的项目。
2. **不可信命令沙箱**：node-only 白名单 + 封禁 eval flag + 拒绝 shell 元字符 + fresh tmp + 凭据剥离 env + 超时——执行外部/LLM 下发命令的任何场景。
3. **本地邮箱 Proxy 解耦鉴权**：agent 只读写本地 JSONL（127.0.0.1），鉴权/重试/同步交给本地常驻 Proxy——需把第三方 SDK 鉴权与业务隔离、且要审计留痕的集成。
4. **内容寻址 + 「无真实 trace 不发成功」**：SHA-256 资产寻址 + Capsule 只能由真实 execution_trace 且非零 blast_radius 产出——需溯源/防刷的经验或结果库。
5. **多 harness 适配器骨架**：`adapters/{claudeCode,cursor,codex,kiro,opencode}.js` 统一 install/uninstall + marker 包裹注入 CLAUDE.md，可幂等卸载——要同时挂多个 agent runtime hook 的工具。

### 关键设计决策

- **核心混淆 + 外部闭源 SDK + 影子 Rust 运行时**：javascript-obfuscator 把「脑」（selector/prompt/memoryGraph/mutation/a2aProtocol 等）混淆，协议抽到闭源 npm SDK（@evomap/atp-sdk、@evomap/gep-sdk，不在仓库），更深的核在未暴露的 Rust crate「EvoX」（schema 注释引用 `crates/evox-*`）。得到「开源」标签与传播力，但可审计性归零、与 GPL 精神冲突、社区无法贡献核心。
- **Gene 携带成本路由提示**：Gene 带 `routing_hint{tier, reasoning_level}` 和 `tool_policy`，把成本治理下沉到资产层（消费端在闭源 router 不可见）。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | evolver | Letta(MemGPT) | ECC | Hermes Agent | Mem0 |
|------|---------|---------------|-----|--------------|------|
| 定位 | 进化资产网络 | agent 记忆平台 | Claude Code harness | 通用自进化 agent | 记忆 SDK |
| 开源透明度 | **混淆闭核** | 全开源 | **全开源** | 开放 | 开源 |
| 核心机制 | Gene/Capsule 协议 | 长期记忆 | instinct→skill | 自进化 | 记忆存取 |
| 网络效应 | 积分经济+市场 | 无 | 无 | 社区 | 无 |
| 学术背书 | 自引用论文 | MemGPT 论文 | 实战 | Nous 研究 | 流行 |

### 差异化护城河

① GEP 协议 + 资产 schema 这套「叙事 + 工程」组合先发卡位；② 混淆闭核 + 外部 SDK + Rust 运行时筑起**反向护城河**（别人抄不到「脑」）；③ 六家 harness 覆盖 + 积分/Worker/Validator 网络效应。但护城河多建立在**不透明**之上，而非可验证的技术领先。

### 竞争风险

① **开源透明度是致命短板**——ECC/Letta/Mem0 全开源，evolver 混淆闭核；② GPL + 混淆的法理张力；③ 增长靠激励催化不可持续；④ Hermes 抄袭叙事可能反噬；⑤「自进化」过度包装一旦被技术读者识破会损信任（已有 #540「README 宣称支持 Codex 但仅接了 hooks」等能力与宣传落差）。

### 生态定位

有真实传播力和一定工程实质（沙箱/schema/适配器/蒸馏确有干货）的**商业化 agent 经验网络**——开源是获客与背书层，变现在闭源内核与积分经济。与 ECC 形成鲜明对照：ECC 全开源透明（instinct→skill 链路可读可改），evolver 则是 GPL 外壳下的闭源变现核。

## 套利机会分析

- **信息差**：这是当下「AI agent 自进化/经验继承」最热的话题级项目，但**纯吹增长会严重踩坑**。真正有信息增量的角度是**拆穿「开源自进化引擎」的真相**——85% 混淆闭核、协议在外部 SDK、增长被积分经济与机器人放大、自进化实为 prompt 资产化。这种「揭露式」深度拆解对技术读者（尤其本站 Claude Code/agent 受众）价值极高，且区别于满屏软文。
- **技术借鉴**：可借鉴的是它**可读外壳**里的真功夫——「不可信命令沙箱」「schema 单一真相源治枚举漂移」「本地邮箱 Proxy 解耦」「内容寻址 + 拒绝伪造成功」「多 harness 适配器骨架」五项，与本类 agent 工具开发高度相关。
- **生态位**：填补「agent 经验协议化 + 网络」的叙事空白，但实质护城河建立在不透明上。
- **趋势判断**：踩在 agent 自进化风口，但开源透明度短板、增长可持续性、叙事被识破风险都是变量。

## 风险与不足

- **开源透明度差（核心问题）**：src/ 85% 字节混淆 + 协议在外部闭源 SDK + 影子 Rust 运行时零暴露；GPL「首选修改形式」要求与混淆分发冲突，社区无法真正审计或贡献核心。
- **质量门控薄弱易刷分**：`outcome.score`/`status` 为自声明，防刷/鉴权/去中心化承诺薄弱，验收最终落在不可见的 Hub（社区已提案 #213 补质量门控，反证当前薄弱）。
- **增长不可当纯口碑**：git 历史被压缩（首 commit 即 v1.66.0、81 tag 高频自动发布）；80/102 commit 是发布机器人；邀请码/积分/排行榜/拉新激励 + auto-issue 默认开显著放大增长。
- **宣传与能力落差**：「self-evolution」叙事 + 论文背书 vs 实为 prompt 资产化；#540 README 宣称支持 Codex 但实际未打通 review 上下文。
- **测试只覆盖外壳**：159 个测试文件量很足，但占 85% 字节的混淆核无法被任何测试覆盖。
- **总线因子 + 身份**：真人核心高度集中（autogame-17 + 极少数），团队身份仅部分公开、未披露融资。

## 行动建议

- **如果你要用它**：想把 agent 经验沉淀为结构化资产、且能接受核心闭源 + 联网积分经济——可试用（核心离线免费）。但要清楚你能审计的只有 15% 的外壳，关键智能不可见、验收落在不可控的 Hub。想要全开源透明的同类选 ECC（everything-claude-code）；要 agent 长期记忆选 Letta；要轻量记忆 SDK 选 Mem0。
- **如果你要学它**：跳过混淆核，直接读可读外壳的真功夫——`src/gep/validator/sandboxExecutor.js`（沙箱白名单，最值得抄）、`src/gep/schemas/{gene,capsule,protocol}.js`（schema 单一真相源治枚举漂移）、`src/gep/skill2gep.js`（蒸馏 + 诚实注释）、`src/adapters/claudeCode.js`（hook 集成）、`src/proxy/`（本地邮箱解耦）。
- **如果你要 fork 它**：几乎无法真正 fork——核心混淆、协议在外部 SDK、更深的核在未公开的 Rust 运行时，GPL 外壳下你拿不到「脑」。可借鉴的是外壳的几个设计模式，而非整个引擎。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/EvoMap/evolver（已收录，含 Core Engine/GEP Protocol/Asset Management/Hub Integration 模块划分） |
| 官网/平台 | https://evomap.ai（Capsule Market + 积分经济 + 进化排行榜的可交互平台） |
| 抄袭争议视角 | [硅谷明星项目被指抄袭中国团队 EvoMap（36kr）](https://eu.36kr.com/en/p/3767967755371011)（含反方「未发现代码级抄袭」证据，宜两面看） |
| 关联研究（同赛道） | MemEvolve、EvoSkills、Darwin Gödel Machine（学术自进化原型，比 evolver 严谨可引用） |
