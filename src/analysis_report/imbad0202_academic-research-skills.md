# 3 个月 30K stars：把「AI 写论文」做成可被同行审计的流水线协议栈

> GitHub: https://github.com/imbad0202/academic-research-skills

## 一句话总结

academic-research-skills 是一套为 Claude Code 量身打造的「严肃学术写作 + 同行评审」Agent Skills 集合 —— **价值不在「让 AI 替你写论文」**,而在把"诚实"做成结构性属性:Material Passport 跨阶段追踪每条引用的可信态,Stage 2.5/4.5 完整性闸门强制人类把关,7-mode AI Research Failure Mode Checklist 把幻觉/越权/造假做成可被 lint 校验的工程问题。

## 值得关注的理由

1. **赛道事实标准已经形成**：3 个月从 0 到 29.6K stars / 2.45K forks / 31 个 minor release，第二名是作者自家 Codex 兄弟版（3.5K stars，差距 8.5×），Claude Code 官方 `/plugin marketplace` 一键安装入口 —— 在「Claude Code + 反幻觉优先 + 非商业 + human-in-the-loop 学术写作」这个象限已占据参考实现位置。
2. **「护栏工程化」是 2026 年 LLM 应用的真正难题**:作者没有陷入「更强 prompt / 更大模型」的军备竞赛,而是把 Material Passport、Sprint Contract、Active Conductor 等护栏机制用 PreToolUse 钩子 + manifest-driven 写范围守卫 + CI spec-consistency lint 固化为结构性属性 —— **这种"用宿主平台能力做护栏"的可复用资产在 Agent Skills 生态里极为稀缺**。
3. **拒绝机制 + 边界契约公开化是稀缺信号**:POSITIONING.md 显式把 Kong 2026 提出的 5 类自主机制(端到端 / idea-gen / Paper2X / 自主实验 / 湿实验 API)逐条写进 "Rejected mechanisms",Issue #3 显式拒绝 humanizer —— **这种"立场可被同行评审"的工程化方式,是其他 AI 论文生成器项目做不到的**。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/imbad0202/academic-research-skills |
| Star / Fork | 29,632 / 2,452 |
| 代码行数 | 75,810 行（Markdown-as-Python 78.4% / JSON 14.3% / YAML 4.0% / HTML 1.9% / Shell 1.0%） |
| 项目年龄 | 3.4 个月（首次提交 2026-02-26） |
| 开发阶段 | 密集开发（近 90 天 486 次 commit，月均 150+） |
| 贡献模式 | 独立开发（Top 贡献者 62.8%，实质单人 GitHub + Codex 双线协作） |
| 热度定位 | 大众热门（赛道事实标准） |
| 质量评级 | 代码 A · 文档 A · 测试 A · CI/CD A |
| License | CC BY-NC 4.0（**非 OSI 开源，禁止商用**） |
| 最新版本 | v3.12.0（共 31 个 tag / 29 个 release，平均不到 2 周一个 minor） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Edward Cheng-I Wu（吳政宜）/ Imbad0202，账号年龄 3.1 年，13 个公开仓库，474 粉丝。中文学术背景的独立开发者，README 显式引用 AIS Senior Scholars' Basket of 11、PRISMA、ICMJE、Nature/IEEE/AAAI 等学术规范。自述「While using ARS to write a reflection article about AI in higher education」—— 本人是高校研究者，对 AI 在高教/学术写作中的角色有切身反思，这从根本上塑造了项目「Assistive, not deceptive」的立场。

### 问题判断

作者把问题定位在学术写作链路里"研究 → 写稿 → 同行评审 → 修订"四阶段被人为拆成多个工具（Zotero 读文献、Semantic Scholar 查引用、LLM 起草、Word/LaTeX 排版、邮件处理 R&R），每一步都可能引入**幻觉、引用漂移、格式错位、范式越权**（agent 越界主张、跑实验、做决策）。而市面上的"AI 论文生成器"又以**全自动**为卖点，把责任完全推给模型 —— 现有方案是"全自动骗审稿人"和"分散工具栈无统一闸门"两个极端。

### 解法哲学

POSITIONING.md 四条哲学逐条对应到具体机制：

- **「Assistive, not deceptive」** → Style Calibration + Writing Quality Check + Disclosure Mode
- **「Human-in-the-loop, always」** → FULL/SLIM/MANDATORY 三态 Checkpoint（不可跳过的 2.5/4.5 完整性闸）
- **「Failure modes are made visible, not hidden」** → 7-mode AI Research Failure Mode Checklist + v3.7.3/v3.8 L3 claim-faithfulness gate
- **「Boundaries are recorded, not improvised」** → Co-Scientist L1–L4 + Kong L1–L2 六个 design-lesson 文档显式归档

### 战略意图

把"独立 vs 平台绑定"做成可治理的扩展点（CONTRIBUTING.md § Platform ports 显式支持 Claude Code / Codex / Cowork / claude.ai 跨平台 sibling distribution），License 用 CC BY-NC 4.0 **主动排除 SaaS / 商业 API 包装 / 付费部署**，避免被转售；这与"被 SaaS 包装"路线是反向选择。

## 核心价值提炼

### 创新之处

| 创新点 | 新颖度 | 实用性 | 可迁移性 |
|---|---|---|---|
| **Material Passport + 单向 promotion + reset boundary ledger**：跨阶段状态做 append-only ledger + JSON Canonical Form hash，可被 `resume_from_passport=<hash>` 跨 session 接管 | 4/5 | 4/5 | 5/5 |
| **Sprint Contract + paper-blind Phase 1 协议**：让评审 agent 先承诺评分计划再看 paper，从机制上避免 reward hacking | 4/5 | 4/5 | 4/5 |
| **Cite-Time Provenance Finalizer 5-cell matrix**：把"引用是否可信"分解为 `source_acquired` × `source_verified_against_original` × `human_read_source` × `anchor_present` × k-of-N indexes-unmatched 五个独立维度 | 5/5 | 4/5 | 3/5 |
| **Active Conductor + PreToolUse 写范围守卫（#134）**：用 Claude Code 原生 PreToolUse 钩子 + manifest-driven 路径白名单，把"子 agent 越权写文件"从哲学问题转成结构性问题 | 4/5 | 5/5 | 5/5 |
| **7-mode AI Research Failure Mode Checklist + Stage 2.5/4.5 完整性闸**：7 个失败模式按 canonical order 在两个完整性闸上独立复检 | 3/5 | 5/5 | 4/5 |
| **corpus-first literature search + 4 Iron Rules**：用户可在 stage 1 之前用本地 Zotero/Obsidian 文件夹作为 corpus 输入，4 Iron Rules 保证 corpus 不可被 agent 改写 | 3/5 | 5/5 | 4/5 |

### 可复用的模式与技巧

1. **POSITIONING.md + Rejected mechanisms 显式立场文档**：把"我们不做什么"和"为什么不做"写成 first-party 文档，并绑定到具体 issue/spec —— 任何有伦理边界的 OSS 都应借鉴
2. **3-layer 心智模型 + `data_access_level` frontmatter 注解 + CI lint**：用 SKILL.md frontmatter 显式声明数据层级，靠 CI 强制而非运行时拦截 —— 任何 LLM-as-judge 场景都应借鉴
3. **design-lesson 三段结构（why reject / review test / known contrary evidence）**：把竞品吸收决策做成可被同行评审的设计资产
4. **Manifest-driven PreToolUse 写范围守卫**：用宿主平台的钩子做"agent 越权拦截"，比 prompt-level "do not write to X" 更可靠
5. **Adaptive Checkpoint（FULL / SLIM / MANDATORY）+ observer at non-mandatory only**：把"用户疲劳"和"完整性不可降级"做成可治理的张力
6. **CI spec-consistency lint（`check_spec_consistency.py`）**：在 30+ 个 minor release 里用脚本把"文档/CHANGELOG/SKILL.md/插件清单"锁步

### 关键设计决策

1. **Material Passport 作为跨阶段唯一可信状态载体**
   - 问题：多 agent 流水线中"哪个 agent 看过什么、引用谁、版本几"会随上下文窗口漂移
   - 方案：把 `origin_skill` / `origin_mode` / `verification_status` / `version_label` / `slr_lineage` / `terminal_policies` / `reset_boundary[]` / `literature_corpus[]` / `claim_audit_results[]` 等所有跨阶段信号**集中**到 `passport.yaml`，强制"promotion only"（Layer 1 → 2 → 3 单向）
   - Trade-off：schema 演化复杂度高（已迭代到 Schema 13.1 + 19 个子 schema）
   - 可迁移性：高

2. **Active Conductor + Deterministic Write-Scope Guard（#134）**
   - 问题：多 agent 流水线中"子 agent 帮下游阶段写文件"会让 phase 边界崩溃
   - 方案：`scripts/ars_write_scope_guard.py` 在 `Write|Edit|MultiEdit|Bash` 上挂 PreToolUse 钩子，按 `scripts/ars_phase_scope_manifest.json` 校验 23 个 Bucket A single-phase subagent 的写路径是否落在自己声明的 scope 内 —— **Bash 对 Bucket A 全拒**
   - Trade-off：牺牲了"agent 用 Bash 做 read-only 操作"的灵活性
   - 可迁移性：高

3. **L1–L4 / L1–L2 design-lesson 文档化竞品吸收决策**
   - 问题：全自动 AI 研究系统（Co-Scientist、Kong Auto-Research）提出的 capability 从机制上看似可借鉴，吸收时若不显式记录边界，未来 contributor 会无意越界
   - 方案：把竞品能力逐条做成"为什么拒收 + 审核测试 + 已知相反证据"三段结构
   - 可迁移性：高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | academic-research-skills | aipoch/medical-research-skills (1.09K) | lishix520/academic-paper-skills (856) | QJHWC/PaperForge (568) |
|---|---|---|---|---|
| 定位 | 全流水线（research → write → review → revise → finalize） | 医学垂直（protocol/数据/证据/写作） | 单技能论文写作 | 端到端 AI 写论文（思路→实验→LaTeX） |
| 哲学立场 | 「AI is your copilot, not the pilot」显式拒全自动 | 通用助手定位 | 通用助手定位 | **「全自动最少干预」** 与 ARS 立场正相反 |
| 反幻觉机制 | Material Passport + 5-cell matrix + cross-index triangulation + claim-audit gate | 学科内规则 | 提示工程级 | SSH 训练 / 反 AI 检测 |
| 完整性闸 | Stage 2.5/4.5 MANDATORY 不可跳过 | 无显式 | 写作关卡 | 无 |
| 平台依赖 | Claude Code 原生 plugin manifest | Claude Code | Claude Code | 通用 |
| License | CC BY-NC 4.0（禁商用） | 未明确 | 未明确 | 未明确 |

### 差异化护城河

- **哲学立场的显式化**：POSITIONING.md rejected mechanisms 把"立场"升级为可被同行评审的设计资产
- **完整性闸作为不可降级 first-class 机制**：Stage 2.5/4.5 MANDATORY 跳过 observer 避免稀释
- **CI spec-consistency 自检**：51 个 lint + 94 个 pytest 在 30+ minor release 里锁步
- **outcome-gradable eval**：`evals/gold/citation_extraction/manifest.yaml` 带 thresholds 0.90/0.85，ranking-lift < -0.05 必须 `[ranking-regression-acknowledged]` ack
- **plugin manifest 兼容性**：`.claude-plugin/` 原生 Claude Code 生态

### 竞争风险

- (1) OpenAI Codex 生态"codex 版"被人视作"哥哥版" —— Claude Code 版需持续证明"参考实现价值大于生态价值"
- (2) 30+ minor release 速度快但**任何一次 spec 漂移**都会污染所有下游 lint 链
- (3) 完整流水线跑完单次成本 $4–6 + 2–4 小时（README 自承），与"全自动 AI 论文生成器"在用户获取成本上有数量级差距
- (4) **单作者主导**（62.8% 集中度 + 兄弟账号 97%）的 bus factor 风险 —— 核心 spec 决策的连续性高度依赖作者本人

### 生态定位

"严肃学术写作 + Anthropic Claude Code 生态"垂直深耕。不追求"全自动最少干预"市场（让给 PaperForge / AI Scientist），不追求"协议级"市场（让给 research-claw / MCP 类项目），不追求"垂直学科"市场（让给 aipoch / medical-research-skills）。**目标是"如果你要在 Claude Code 上写一篇像样的学术论文，ARS 是默认选择"**。

## 套利机会分析

- **信息差**：已被充分定价 —— 29.6K stars + 2.45K forks + 持续 4 月内 30+ 次发版 + Claude Code 官方 `/plugin marketplace` 收录入口，估值已反映其枢纽地位
- **技术借鉴**：
  - `scripts/ars_write_scope_guard.py` 的 PreToolUse 钩子模式 —— 任何 Claude Code plugin 都可直接复制
  - Sprint Contract + paper-blind Phase 1 —— 可推广到代码评审、招聘筛选、新闻 fact-check
  - Material Passport 跨阶段 ledger —— 可推广到 CI 多 step 编排、AI 教学辅导
  - 5-cell resolution matrix + 三角测量 + policy_hash stamp —— 可推广到法律 brief、医学循证
- **生态位**：在"Claude Code 平台 + 反幻觉优先 + 非商业 + human-in-the-loop 学术写作"象限占据参考实现位置
- **趋势判断**：赛道仍在增长但已收敛 —— 第二名与第一名差距 8.5×，护城河已经从"功能齐全"转移到"哲学立场 + 工艺沉淀"；新进入者除非有更强哲学立场或更密集评测，否则很难撼动 ARS

## 风险与不足

1. **单作者主导风险**：Top 贡献者占 62.8%，加兄弟账号实质 97% 单人；核心 spec 决策连续性高度依赖作者
2. **Spec 漂移风险**：v3.7.3 codex round-7 仍有 F2/F16 closure（lint 不能一次性发现所有漂移，必须靠多轮 review 抓）
3. **License 风险**：CC BY-NC 4.0 排除商业用途 —— 对想要 SaaS 包装 / 商业 API 集成的团队来说是硬门槛
4. **完整流程成本**：单次论文跑完 $4–6 + 2–4 小时（README 自承），对"只想拿一篇草稿"的用户有数量级摩擦
5. **生态绑定**：强依赖 Claude Code 平台（PreToolUse 钩子、plugin manifest、slash command），跨平台时只能降级到"普通 Skills 集合"

## 行动建议

### 如果你要用它

适合**非商业学术研究者**,特别是有完整研究问题但苦于"找文献 / 核引用 / 查数据一致性 / 查逻辑一致性"的研究者。对比 PaperForge:**如果你能接受「半自动 + 强制完整性闸 + 强制人类把关」,ARS 是更好的选择**;如果你只想"一键拿草稿",请直接用 PaperForge。对比 aipoch/medical-research-skills:ARS 跨领域通用,aipoch 医学深 —— **做医学研究优先 aipoch,做跨学科 / 高教 / 政策研究优先 ARS**。

### 如果你要学它

重点关注以下文件/模块：

| 学习目标 | 关键文件 |
|---|---|
| 护栏工程化 | `scripts/ars_write_scope_guard.py` + `scripts/ars_phase_scope_manifest.json` |
| 跨阶段状态 | `shared/contracts/passport/*.yaml` + `scripts/_passport_yaml.py` |
| 反幻觉机制 | `shared/ground_truth_isolation_pattern.md` + `evals/gold/citation_extraction/` |
| 评审防 reward hacking | `shared/contracts/reviewer/{full,methodology_focus}.json` |
| 哲学立场文档化 | `POSITIONING.md` + `docs/design/<date>-<version>-<feature>-*.md` |
| CI 锁步 | `scripts/check_spec_consistency.py` + `scripts/check_version_consistency.py` |
| Eval 门 | `scripts/run_evals.py` + `scripts/check_ranking_lift.py` + `evals/gold/*/manifest.yaml` |

### 如果你要 fork 它

可以改进的方向：

- **跨平台解耦**：把 PreToolUse 钩子抽象成"platform adapter"，让 Codex / Cowork / 自托管平台都能复用护栏
- **垂直学科模块化**：参考 aipoch 的"先做深一个领域"路线，做一个高教品保 / 政策研究 / 法学研究的 vertical module
- **白皮书 harness**（Issue #142）：用户显式请求，目前通过 @copilot / @claude 拼装 —— 可以做成 first-class skill
- **多人协作版本**：当前模型假设单人使用，可以扩展到 lab / research group 场景
- **跨语言输出增强**：4 个语言 README 已经做到对齐，但学术论文的 LaTeX / Word 模板目前较弱

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [链接](https://deepwiki.com/Imbad0202/academic-research-skills) — 已收录 |
| Zread.ai | 未收录（403 Cloudflare 拦截） |
| 关联论文 | [Lu et al. 2026 *Nature* 651:914-919 — The AI Scientist](https://www.nature.com/articles/s41586-2026-0914-0) · [Zhao et al. 2026-05 arXiv:2605.07723 — 1.11 亿引用审计 / 14.7 万条幻觉引用](https://arxiv.org/abs/2605.07723) · [Song et al. 2026 arXiv:2604.05018 — PaperOrchestra](https://arxiv.org/abs/2604.05018) · [Kong et al. 2026 arXiv:2605.18661 — AI for Auto-Research: Roadmap & User Guide](https://arxiv.org/abs/2605.18661) |
| 外部深度视角 | [Academic Writing Shouldn't Be a Solo Act (Substack EN)](https://open.substack.com/pub/edwardwu223235/p/academic-writing-shouldnt-be-a-solo?r=4dczl&utm_medium=ios) · [學術寫作不該是一個人的事 (Substack 繁中)](https://open.substack.com/pub/edwardwu223235/p/ai?r=4dczl&utm_medium=ios) |
| 在线 Demo | 无独立 web demo；`examples/showcase/` 提供 8 份真实管线产物 PDF（含 EN/zh 两版 final paper、3 份 review report、3 份 integrity report、post-publication audit） |
