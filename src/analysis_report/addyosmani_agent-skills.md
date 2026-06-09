# Google 工程总监的 23 份 SKILL：3.7 个月把 49.7K Star 拉爆的"工程纪律即 prompt"

> GitHub: https://github.com/addyosmani/agent-skills

## 一句话总结

把 Google Chrome 团队 16 年沉淀的工程纪律（spec → plan → build → verify → review → ship）打包成 23 份 `SKILL.md`，让 Claude Code / Cursor / Gemini CLI 等 8 个 Agent harness 强制遵循——**本质是「给 AI 写 SOP，而不是给 AI 喂资料」**。

## 值得关注的理由

- **品牌 × 内容 × 生态三重背书**：Addy Osmani（Google 工程总监，《Learning JavaScript Design Patterns》作者）+ 23 个 skill 覆盖完整 SDLC + 同时支持 8 个 IDE/harness——是迄今最完整的跨 vendor Agent skill 套件。
- **49.7K stars 但只有 277KB**：纯 markdown 知识资产，无 npm 依赖、无运行时，每个 commit 平均带动 ~235 stars——单位 commit 含金量极高。
- **Anti-Rationalization Table 首创**：每个 skill 都有一节专门反驳"agent 想偷懒的借口"，把流程型 prompt 的偷工问题结构化解决——这套模式可迁移到任何 prompt 工程场景。

## 项目展示

![Addy's Agent Skills](https://addyosmani.com/assets/images/addys-agent-skills.jpg)

*README 顶部 banner，作者本人品牌色。仓库本身是 markdown 知识库，**没有 demo GIF、没有架构图**——SKILL.md 类内容仓库的固有形态，价值在文本而非图。*

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/addyosmani/agent-skills |
| Star / Fork | 49,710 / 5,553 |
| Watcher | 330 |
| 代码行数 | 808（Shell 76.6% / JS 21.7% / JSON 1.7%） |
| 文档行数 | 6564 行 Markdown（23 SKILL.md + 5 reference + 7 docs + 3 agent） |
| 项目年龄 | 3.7 个月（2026-02-15 首 commit） |
| 开发阶段 | 密集开发（近 90 天 177 commit，4 月单月 88 commit 为爆发期） |
| 贡献模式 | 明星项目早期（Addy 本人 55.4%，32 名贡献者，Federico Bartoli 14 commit 是核心 #2） |
| 热度定位 | 大众热门 × 小众精品内核（49.7k stars / 277KB / 211 commits） |
| 质量评级 | 内容[优秀] 文档[优秀] 测试[充分] CI/CD[完善] |
| 版本 | v0.6.1（3 个 tag，SemVer 0.x 阶段） |
| 仓库体积 | 277KB（与 4.97 万 stars 极不匹配，强证内容型定位） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Addy Osmani——Google 工程总监，Chrome 团队出身，16.9 年 GitHub 资历，公开身份 "Director at Google working on Gemini and Google Cloud"。著有《Learning JavaScript Design Patterns》《Image Optimization》，是 Web 性能领域的顶级布道者。近一年明显转向 AI 工程化方向：同期维护 web-quality-skills（Lighthouse/CWV 技能集，2202 stars）、agent-engineer、agentic-seo、oust 等姐妹仓。这次把 Chrome 团队长期打磨的工程纪律（Hyrum's Law、Beyonce Rule、Chesterton's Fence、~100-line PR、trunk-based dev）打包成 SKILL.md，**本质是把"Google 工程文化"作为知识资产开源化**。

### 问题判断

作者在《Long-running Agents》一文中明确："shortcuts become archaeology after 30h"——当 AI agent session 持续 30 小时，第 5 小时跳过的 spec、跳过的 test 会在第 25 小时变成要考古的技术债。这是他**自己做长跑任务时被自己绊倒**的痛点，也是当前所有 agentic coding 工具的通病：模型默认走"最短路径到 done"，跳过 spec、跳过 test、跳过 review、跳过 performance verification，导致 prototype-quality 而不是 production-quality 输出。

### 解法哲学

- **Process over prose**：SKILL 是 workflow 不是 reference doc，每个 skill 都有 steps / checkpoints / exit criteria。
- **Anti-Rationalization Tables**：把 agent 想偷懒的借口显式列出并反驳——这是被作者点名为「最独特的设计选择」。
- **Verification as non-negotiable exit criterion**：每个 skill 的「完成」必须有可验证证据，不是"我看了就行"。
- **Progressive Disclosure**：meta-skill 只把相关 skill 拉进 ~5K token context，而不是 startup-eager-load 全部 23 份。
- **Scope Discipline**：「touch only what you're asked to touch」——禁止 agent 借机重构"顺手"代码。

### 战略意图

在作者更大的图景中，`agent-skills` 是**通用生命周期层**（横向），`web-quality-skills` 是**领域纵深**（前端质量），`agentic-seo` / `oust` / `agent-engineer` 是其他领域——形成**矩阵布局而非单点产品**。MIT 协议、纯开源、**无 SaaS / 托管版 / 企业版**；商业价值靠作者个人品牌（Google Director + Head of Chrome DX）放大，而非仓库本身变现。

## 核心价值提炼

### 创新之处

| # | 创新点 | 新颖度 | 实用性 | 可迁移性 |
|---|--------|--------|--------|----------|
| 1 | **Anti-Rationalization Table** | 4/5 | 5/5 | 5/5 |
| 2 | **Three-Layer Orchestration**（skills + personas + slash commands 分层） | 4/5 | 4/5 | 5/5 |
| 3 | **Validator-Owned Exemption**（被校验文件不能自己声明豁免） | 3/5 | 5/5 | 5/5 |
| 4 | **HTTP 304-Driven Cache**（用服务器验证代替 TTL） | 3/5 | 4/5 | 5/5 |
| 5 | **Block-Level Simplify-Ignore**（注释 + hash 占位的代码保护） | 4/5 | 4/5 | 4/5 |
| 6 | **Parallel Fan-Out + Merge**（多 persona 并行评审，主 agent 合并） | 3/5 | 4/5 | 4/5 |
| 7 | **DAMP Over DRY**（test 里的反 DRY 原则） | 2/5 | 5/5 | 5/5 |

最值得借鉴的是 **Anti-Rationalization Table**——**把"agent 会偷懒的借口"显式枚举并反驳**，比"提醒它别偷懒"有效得多。例（test-driven-development）：借口"tests slow me down"，反驳"15 min of tests saves 15 hours of debugging"。

### 可复用的模式与技巧

1. **Skill Anatomy**：每个 prompt skill 必有 `name` + `description` + Overview/When to Use/Process/Rationalizations/Red Flags/Verification 五段。
2. **Meta-Skill Routing**：用 ASCII 决策树把"任务 → skill"映射画出来，作为 session-start hook 的注入内容。
3. **Cross-IDE Command Adaptation**：同一命令用不同 frontmatter（`.claude/commands/spec.md` YAML frontmatter vs `.gemini/commands/spec.toml` TOML）指向同一 skill。
4. **Section-Budget Hard Cap**：SKILL.md ≤ 500 行是硬约束不是建议——token 经济性做成硬约束。
5. **Quality Bar 四条**：Specific / Verifiable / Battle-tested / Minimal——4 个形容词 + 一句话解释。
6. **Validator-Owned Exemption Policy**：豁免权只能 validator 自己授予，不能由被校验对象声明。
7. **HTTP 304 Cache in Agent Tool Hook**：跨 session 的文档缓存只信任服务器 `304 Not Modified`，没有 validator 一律不缓存。
8. **Skill-Override Precedence**：用户级别覆盖 plugin 级别——把 Claude Code 的 scope priority 用规则化语言写进文档。

### 关键设计决策

| 决策 | Trade-off | 适用场景 |
|------|-----------|----------|
| **Markdown-only 跨 harness 复用** | 放弃自动化执行能力，换 8 个 harness 零修改复用 | 任何"声明式 prompt pack"项目 |
| **session-start Hook 自动注入 meta-skill** | 每次新 session 额外注入 ~2k tokens，换 agent 第一个 prompt 就知道路由表 | 所有 Claude Code plugin |
| **sdd-cache hook 用 HTTP 304 而不是 TTL** | 每次 cache miss 多一次 HEAD roundtrip，换"服务器说没变就用"的语义干净性 | 所有需要"既要缓存又不能 stale"的 agent 系统 |
| **progressive disclosure + 500-line hard cap** | 偶尔需要 agent 主动加载附件，换 23 skill 共用不到 2000 token description 预算 | 任何"系统提示 + 知识库"系统 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | addyosmani/agent-skills | obra/superpowers | anthropics/skills | wondelai/skills | awslabs/agent-plugins |
|------|-------------------------|-------------------|-------------------|------------------|------------------------|
| Skill 数量 | **23**（完整 SDLC） | ~15（集中 TDD/Review/Plan） | 较少（spec + 几个 demo） | ~5~10 | ~10（AWS 主题） |
| Star | 49.7K | ~116K（数据待核） | N/A（官方） | 1.2K | N/A |
| 跨 IDE 支持 | **8 个 harness** | 仅 Claude Code | Claude 生态 | Claude + agentskills.io | Claude + AWS |
| 核心差异化 | **Anti-Rationalization + Google 工程实践** | 协议先驱 / 社区共建 | Spec 权威 | 协议胶水 | AWS 工具箱 |
| 工程纪律出处 | SWE-book + eng-practices 可追溯 | 社区共识 | Anthropic 内部 | 通用 | AWS 架构 |
| Validator | 自研 `validate-skills.js` + CI 三 job | 较轻 | 官方 SDK | 无显著 | AWS 内部 |
| 作者 | Google Director | 社区 | Anthropic 官方 | 个人 | AWS Labs |

### 差异化护城河

不是技术护城河（协议开放、markdown 开放），而是三重：

- **品牌护城河**（最强）：Addy Osmani 个人 IP + Google 工程文化背书；
- **内容护城河**：anti-rationalization table + section anatomy + 23 skill 完整度；
- **生态护城河**：8 个 IDE/harness 同时支持。

### 竞争风险

最可能被 **anthropics/skills 演化**替代——若 Anthropic 把官方 skill 库扩展到同等规模，agent-skills 的"23 skill 完整度"优势会被磨平；护城河只剩品牌。次风险是 obra/superpowers 继续扩张社区共识。

### 生态定位

处于三层架构的中间层：① Anthropic spec（底层协议）→ ② Addy agent-skills（通用生命周期）→ ③ 领域 skills（web-quality-skills / agentic-seo / oust / agent-engineer，作者姐妹仓纵向）。和 obra/superpowers 是横向竞品，但定位更"产品化"。

## 套利机会分析

- **信息差**：不算被低估（已是大众热门量级），但作为"知识资产型"仓库，**49.7k stars / 277KB / 211 commits**的密度说明单位 star 含金量高——仍有"小众精品内核 + 大众传播外衣"的组合优势。
- **技术借鉴**：Anti-Rationalization Table、Three-Layer Orchestration、Validator-Owned Exemption、HTTP 304 Cache in Hook——这四个模式可直接迁移到任何 prompt 工程、multi-agent 系统、linter 工具。
- **生态位**：填补了"通用工程流程层"的空白——既不是 spec 定义者（Anthropic），也不是领域专题（web-quality-skills），而是**横向全生命周期**。
- **趋势判断**：**强烈增长**——4 个月 49.7K stars，单日 ~200 stars 的爆发曲线说明仍在加速；8 harness 适配矩阵和 v0.6.1 节奏说明产品成熟度还在提升。**比 superpowers 有后发优势**（更完整 + 更跨平台）。

## 风险与不足

1. **协议依赖风险**：完全依赖 Anthropic Agent Skills 协议的稳定性。若协议改版（frontmatter schema、description 长度限制、progressive disclosure 模型），全部 23 个 skill 需同步修订——这是"协议红利"的反面。
2. **作者集中度**：Addy 55-67% commits 是真实投入也是单点风险——若 Google 工作变化或个人兴趣转移，节奏可能断档。Issue 矩阵里多处提到 Addy 个人 review bot 化的可能。
3. **Hook 兼容性脆弱**：Issue #110 揭示 SessionStart hook 在 Claude Code 上 silently fail 是已知问题——把 hook 当作 enforcement layer 使用的策略与上游 harness 的稳定性耦合。
4. **版本号不一致**：`.claude-plugin/plugin.json` 写 `1.0.0` 而 git tag 是 `0.6.0`（Issue #145 已 close），但仍是未来隐患。
5. **零测试代码**：Test commit 仅 0.5%（1 次），验证手段靠 frontmatter 校验 + 人工 review，不是单元测试——对"流程型 prompt"而言可接受，但与生产代码项目标准差距大。
6. **markdown-only 张力**：Issue #136 揭示部分 skill 提到 scripts 目录却没有脚本——刻意拒绝做成"可执行代码项目"的代价是一些 skill 的"可执行"承诺无法兑现。

## 行动建议

- **如果你要用它**：直接通过 `/plugin marketplace add addyosmani/agent-skills` 装 Claude Code，或参考 `docs/` 下对应 IDE setup；推荐先用 `/ship` 跑一个真实 PR 体验三层 orchestration，再逐步启用 `test-driven-development` + `code-review-and-quality` + `security-and-hardening` 三个核心 skill。**不建议装完全部 23 个**——按团队痛点选 3-5 个试用，渐进引入。
- **如果你要学它**：优先读 4 份文件——`skills/using-agent-skills/SKILL.md`（meta-skill 路由决策树）、`docs/skill-anatomy.md`（skill 写作规范）、`references/orchestration-patterns.md`（5 种 endorsed + 5 种 anti-pattern 模式）、`scripts/validate-skills.js`（豁免权管理）。这四份覆盖了**怎么写 skill、怎么路由、怎么编排、怎么校验**的完整闭环。
- **如果你要 fork 它**：可改进方向——① 给 `validate-skills.js` 加 custom rule 插件机制，让下游 fork 可以扩展规则集；② 把 `simplify-ignore` 的 block-level 保护做成语言无关（当前依赖 JS/TS 注释语法）；③ 补一个 `scripts/run-eval.js`——把每个 skill 的"能否让 agent 实际遵循"做成可度量的 eval（不只是 frontmatter 合规）；④ 把 `sdd-cache` 的 HTTP 304 缓存做成可插拔 backend（目前用本地 JSON，未来可支持 Redis / SQLite）。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/addyosmani/agent-skills |
| Zread.ai | https://zread.ai/addyosmani/agent-skills |
| 关联论文 | 无（仓库本质是工程实践集，非研究产物） |
| 在线 Demo | 无（每个 skill 设计为在 Claude Code/Cursor 中实际执行，隐式 demo） |
| 作者博客 | [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/) · [Long-running Agents](https://addyosmani.com/blog/long-running-agents/) |