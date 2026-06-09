# 3 个月 15K stars：柏林独立开发者把 754 个网络安全 SOP 编码成 AI Agent 可直接调用的「Skills 库」

> GitHub: https://github.com/mukul975/anthropic-cybersecurity-skills

## 一句话总结

Mahipal（mukul975）用「YAML frontmatter progressive disclosure + MITRE ATT&CK/NIST CSF/ATLAS/D3FEND/AI RMF 五框架映射 + agentskills.io 开放分发」三件套，把资深安全分析师脑中的 754 个 SOP 沉淀为 Claude Code / Cursor / Copilot 等 26+ AI 平台可一键调用的结构化技能库——这是「AI Agent 时代知识库工程化」的范本。

## 值得关注的理由

1. **赛道头部 + 蓝海**：3.4 个月达成 15K stars / 1.8K forks，Apache-2.0 + Anthropic plugin marketplace 分发加持；在「AI Agent × Cybersecurity 垂直 skills」极窄子赛道基本没有直接对手，ComposioHQ/awesome-claude-skills（63.9K★）只是聚合目录而非内容层
2. **五框架映射独家护城河**：唯一一个同时把 MITRE ATT&CK（攻击）/ NIST CSF 2.0（治理）/ MITRE ATLAS（AI 安全）/ D3FEND（防御）/ NIST AI RMF（AI 治理）五套异构分类体系同时打到每个 skill 上的开源库——「一鱼五吃」叙事在合规行业是硬通货
3. **工程哲学高度成熟**：754 个 skill 仅靠 <300 行 stdlib Python 校验脚本 + 3 个 CI workflow + 严格 frontmatter 契约维护；「结构承载规模，元数据承载信任，token 效率优先」是核心信条，可直接迁移到任何「LLM 消费的知识库」场景

## 项目展示

### README 媒体
1. ![Anthropic Cybersecurity Skills banner](https://raw.githubusercontent.com/mukul975/anthropic-cybersecurity-skills/main/assets/banner.png) — 类型: hero（仓库主横幅）
2. ![Star History Chart](https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date) — 类型: screenshot（外部 star-history 动态图）

### 官网媒体
- 官网为纯文字布局（WebFetch 403 / JINA reader 均无 img/video），无可补充项

### 筛选说明
- 总共发现 2 个媒体元素（1 README hero + 1 Star History 动态图），筛选后保留 2 个
- 排除了 13 个 badge / CI 状态图标 / 占位 svg

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/mukul975/anthropic-cybersecurity-skills |
| Star / Fork | 15,042 / 1,787 |
| Watcher | 111 |
| 代码行数 | 203,954 行（Python 97.9% / JSON 1.8% / PowerShell 0.3%） |
| 文件数量 | 3,420 个（含 ~756 个 SKILL.md + index.json 等元数据） |
| 项目年龄 | 3.4 个月（2026-02-25 创建） |
| 开发阶段 | 密集开发 → 稳定维护（90 天 143 commit，30 天仅 7 commit） |
| 开发模式 | 职业项目（系统判定；实际为柏林安全研究者的强内驱晚间 OSS） |
| 贡献模式 | 单人主导（mukul975 75.4%，第二别名 Mahipal 14.5%，MAGI / juliosuas 各 ~5%） |
| 热度定位 | 大众热门（3.4 个月达成 15K，爆发型增长） |
| 质量评级 | 代码[A] 文档[A+] 测试[C] CI[A] |
| License | Apache-2.0 |
| 最新版本 | v1.2.0（共 3 个 tag：v1.0.0 / v1.1.0 / v1.2.0） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Mahipal（GitHub: mukul975），常驻 Berlin，MSc 学历，账号注册于 2018-08（7.8 年），bio 自标「Cybersecurity · Dev · Research & AI Security」。30 个公开仓库中 TOP3 全部围绕「AI Agent × Security」主题：

- `cve-mcp-server`（990★）— CVE 检索 MCP server
- `mcp-windows-automation`（36★）— Windows 自动化代理
- `claude-team-dashboard`（51★）— Claude 团队协作面板

近期还启动 GARS-2026 全球学术调查（SRH Berlin 监管）和 Casky.ai Playground Saa化尝试。**作者本质是「AI-native cybersecurity company」愿景的全栈构建者**——本仓库（skills 内容层）+ cve-mcp-server（工具层）+ Casky（产品层）构成三层栈。

### 问题判断

Mahipal 在构建 `cve-mcp-server` 和 `mcp-windows-automation` 的实战中发现：**MCP 提供「手」，但 AI 代理缺「脑」**——当代理面对一个取证镜像，它需要的不是「能调用 vol」，而是「为什么先跑 windows.info、跑完 pslist 后为什么还要 psscan 做交叉视图、什么时候该怀疑进程注入」。这是「工具调用」到「操作流程」的鸿沟，2026 年 AI Agent 大爆发恰好让这个鸿沟变得不可忍受——任何接触过 Claude Code 的安全工程师都会立刻意识到这个缺口。

### 解法哲学

「**结构承载规模，元数据承载信任**」——754 个 skill 能稳定运行的关键不是 skill 数量本身，而是：

1. **YAML frontmatter 让代理在 ~30 tokens 内就能扫描并匹配**（progressive disclosure）——README 写明「Discovery ~40 tokens」，把 context window 效率当 first-class concern
2. **统一 markdown body 段落结构**（When to Use / Prerequisites / Workflow / Verification）——让模型零样本理解新 skill 的形态
3. **严格 kebab-case + 动词-技术-工具命名规范**（`analyzing-memory-dump-with-volatility3`、`performing-nist-csf-maturity-assessment`）——LLM 见到 `detecting-` 开头就知道是检测类，见到 `with-volatility3` 后缀就知道工具栈

**明确不做的事**：不做领域封闭（必须遵循 agentskills.io 开放标准而非 Claude 私有格式）、不做形式主义校验（仅校验 frontmatter 字段，不做语义验证）、不做内容硬约束（接受贡献者 PR 但保持 48 小时 review 承诺）。

### 战略意图

三个信号揭示战略图景：

- **Issue #59 `multi-agent-prompt-injection-defense`**：下一个扩张方向——「AI Security 自防御」，作者已把 AI 代理自身安全纳入主线（2025-2026 才浮现的垂直）
- **Issue #23 `[good first issue + new-skill]`**：把社区共建当产能放大器，3 个月扩到 754 个 skill 的核心机制
- **GARS-2026 学术调查 + Casky.ai Playground + Hermes Agent 兼容徽章**：用学术研究建立权威性 + 用 Playground 把 skill 转化为 SaaS + 用多平台兼容扩大分发面——三者形成「学术 × 产品 × 分发」的三位一体飞轮

本仓库在作者更大的规划中是**内容层基础设施**，上游对接 AI 平台分发，下游对接自家 cve-mcp-server 工具层和未来的 Casky 产品层。

## 核心价值提炼

### 创新之处

#### 1. Progressive Disclosure Skill 元数据（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）

通过 ~30 tokens 的 YAML frontmatter 让 LLM 在单次扫描中评估 754 个 skill 的相关性，仅在选中后加载完整 500-2000 tokens 的 workflow。这是把「RAG 的 chunking 思想」应用到「AI Agent tool discovery」的工程化实践——**Anthropic 推广的 progressive disclosure 模式在这个项目里被工程化到极致**。

#### 2. 五框架合规映射矩阵（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）

把 MITRE ATT&CK（攻击）+ NIST CSF 2.0（治理）+ MITRE ATLAS（AI 安全）+ D3FEND（防御）+ NIST AI RMF（AI 治理）五套异构分类体系同时打到每一个 skill 上。README 给出范例：`analyzing-network-traffic-of-malware → T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6`——一个 skill 同时被五套分类体系承认。**「一鱼五吃」叙事在合规行业是硬通货**，金融 PCI、医疗 HIPAA、汽车 ISO/SAE 21434 都会买账。

#### 3. agentskills.io 开放分发协议（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）

不绑定单一 AI 平台（不像 GitHub Copilot 的私有 prompt 仓库），而是输出符合 `agentskills.io` 标准的目录结构 + `marketplace.json` + `npx skills add` 安装协议，让同一份内容触达 26+ AI 平台（Claude Code / Copilot / Cursor / Windsurf / Cline / Codex / Gemini / Hermes Agent / MCP-compatible agents）。这是 ComposioHQ/awesome-claude-skills 没有的护城河——**「聚合目录 vs 内容即产品」的差别**。

#### 4. 「动词-技术-工具」语义命名空间（新颖度 3/5 | 实用性 4/5 | 可迁移性 5/5）

与 LangChain Tool 的「抽象 name/description」不同，强制把语义压进 skill 名字本身（`analyzing-memory-dump-with-volatility3`），让 LLM **零样本**就能从名字预测能力边界。这是把「命令式 API 设计」思想应用到 LLM 消费场景。**「命名即 API」** 模式值得在任何大规模 function/tool 集合上推广。

#### 5. 学术调查 × 开源产品的飞轮（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）

通过 GARS-2026 全球学术调查（SRH Berlin 监管）反向建立权威性，把用户变成数据点；用 Casky.ai Playground 把 skill 转化为 SaaS（50 token 激励填写）；调查产出 CC-BY 4.0 论文——「**用户填调查 → 项目获得权威性数据 → 数据发表论文 → 论文为项目背书 → 更多用户填调查**」的飞轮。这种「学术 + 产品」双轮模式在开源基础设施项目中罕见且有效。

#### 6. MITRE ATT&CK Navigator 自动导出（新颖度 3/5 | 实用性 5/5 | 可迁移性 4/5）

通过扫描所有 SKILL.md 中的 `T1XXX(.XXX)` 模式 + 计数，自动生成可视化的 Navigator layer JSON（`attack-navigator-layer.json`），让用户能在 MITRE 官方 Navigator 上看到 218 个 technique 的覆盖深度（蓝渐变）。这是「合规覆盖可视化」的现成范式——任何「测试用例 × OWASP Top 10」「设备配置 × CIS Benchmark」都能套用。

### 可复用的模式与技巧

1. **Frontmatter 渐进披露**：YAML 头（~30 tokens）+ Markdown 体（按需加载）+ `references/` 子目录（深度按需）。适用于一切 LLM 消费的知识库——医学、法律、金融合规、企业 runbook 全场景可迁移
2. **一行 `npx skills add` + 多平台分发**：遵循开放标准 + `marketplace.json` 清单 + CLI 入口，让一份内容触达多平台。适用于所有想做「AI 内容产品」的项目
3. **轻量 stdlib 校验脚本 + CI 自动跑**：290 行 Python 完成全部 frontmatter 校验，无任何依赖。适用于社区协作项目的质量底线——「故意写得简单」降低 contributor 心智负担
4. **Alias 兼容 schema 演进**：在 `validate-skill.py` 里维护 `_SUBDOMAIN_ALIASES` dict（30+ 历史名 → 规范名），新 skill 用规范名、老 skill 用 alias 名（接受但打印 WARN）。任何长期演进的 schema 都应该建别名层
5. **自动重建索引 + CI 同步 marketplace 版本**：`update-index.yml` 在 push 时重建 `index.json`；`sync-marketplace-version.yml` 在 release 时同步版本号。适用于一切「机器可读元数据 + 人类可读内容」共存的仓库
6. **「命名即 API」**：kebab-case `动词-技术-工具` 让 LLM 零样本推断能力。适用于大规模 function/tool 命名空间

### 关键设计决策

1. **决策**：YAML frontmatter + Markdown body 双层结构，每个 skill 自包含一个目录
   - **问题**：754 个 skill 怎么让 LLM 既能秒级扫（匹配相关 skill）又能深度读（执行 workflow），且不爆 context？
   - **方案**：frontmatter 含 `name`/`description`/`tags`/`mitre_attack`/`nist_csf`/`atlas_techniques`/`d3fend_techniques`/`nist_ai_rmf` 给 agent 做 discovery；body 含可执行 workflow 在被选中后才加载
   - **Trade-off**：牺牲了自由表达（必须套固定段落结构），换来了 754 skill 可在单次 prompt 内全部扫描而不爆 context
   - **可迁移性**：高。任何「知识库 + LLM 消费」的场景都能用

2. **决策**：`index.json` 用极简 schema（仅 `name`/`description`/`domain`/`path`）作为发现层
   - **问题**：怎么让 Agent 在不扫描整个 git 仓库的前提下找到所有 754 个 skill？
   - **方案**：CI workflow `update-index.yml` 在 push 到 main 时自动扫描 `skills/` 目录并重写 `index.json`（~170KB）。Agent 加载这一个文件就能枚举全部 skill
   - **可迁移性**：高。「预生成索引 + 增量 CI 重建」是知识库的标配模式

3. **决策**：`.claude-plugin/marketplace.json` 标准化分发协议 + `npx skills add` 一行安装
   - **问题**：怎么让 754 个 skill 触达 26+ AI 平台？
   - **方案**：遵循 Anthropic 推出的 `agentskills.io` 开放标准，提供 `marketplace.json` 作为插件清单；`sync-marketplace-version.yml` 在 GitHub Release 时自动同步版本号
   - **Trade-off**：依赖 `agentskills.io` 标准生态的成熟度；换来了「单仓库分发到 26+ 平台」的网络效应
   - **可迁移性**：极高。任何做「内容即产品」的开源项目都可以借这套 marketplace 协议分发给所有 AI 平台

4. **决策**：`tools/validate-skill.py` 用 stdlib-only Python 写准入闸门（必需字段 + kebab-case + 长度 + 50 字符最小描述）
   - **问题**：社区贡献 754 个 skill 时，怎么保证质量底线而不被 PR 海啸击垮？
   - **方案**：三层质量闸——① 编写规范（CONTRIBUTING.md）、② 本地脚本验证（validate-skill.py，零依赖）、③ CI 自动验证（`.github/workflows/validate-skills.yml`）+ `update-index.yml` 自动重建索引
   - **可迁移性**：高。任何大型社区协作的知识库项目都能套这套「轻量校验脚本 + CI 自动跑」模式

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | 本项目 | awesome-claude-skills (63.9K★) | deer-flow (70.8K★) | langchain (138.9K★) | cve-mcp-server (990★) |
|------|--------|-------------------------------|-------------------|-------------------|---------------------|
| 类型 | 垂直内容库 | 聚合目录 | 通用 Agent harness | 通用 Agent 框架 | 工具 MCP server |
| 垂直深度 | ★★★★★ | ★★（聚合） | ★（通用） | ★（通用） | ★（单一 CVE） |
| 广度 | ★（单 Security 域） | ★★★★★（跨域 1000+） | ★★★ | ★★★★★ | ★ |
| 分发面 | ★★★★★（26+ 平台） | ★★★★（Claude 生态） | ★★（自用为主） | ★★★★★ | ★★（MCP 客户端） |
| 五框架合规映射 | ★★★★★（独家） | × | × | × | × |
| 决策流程层 | ★★★★★ | × | ★★★（通用） | ★★（抽象） | ×（数据查询） |
| 商业化路径 | Casky SaaS | × | 字节内部 | LangSmith SaaS | × |

### 差异化护城河

- **技术护城河**：五框架映射（ATT&CK + CSF + ATLAS + D3FEND + AI RMF）独家——ComposioHQ / LangChain / Deer Flow 都做不到「一鱼五吃」
- **生态护城河**：26+ 平台分发（agentskills.io + marketplace.json）——单仓库触达 Claude Code / Copilot / Cursor / Windsurf / Cline / Codex / Gemini / Hermes Agent 的网络效应
- **信任护城河**：GARS-2026 学术调查（SRH Berlin 监管）+ CITATION.cff + 学术论文——把开源项目升格为「可引用的学术资源」

### 竞争风险

- **Anthropic 官方若推出 cybersecurity skill 官方集**，依赖度会被削弱（但项目已声明「独立社区项目，与 Anthropic PBC 无关」做了品牌隔离）
- **agentskills.io 标准若被淘汰**，分发优势消失（但 `npx skills add` + `marketplace.json` 已是事实标准）
- **内容同质化**：其他研究者可以快速复制 skill 结构（但五框架映射的维护成本 + 26 平台分发网络 + 学术飞轮三者绑定的复利是单点难以追平的）

### 生态定位

定位为「**AI × Cybersecurity 赛道的内容基础设施**」，是作者 Casky.ai Playground（产品层）和 cve-mcp-server（工具层）之上的「知识层」。三层组合形成难以复制的全栈优势——在「AI Agent × Cybersecurity」这个 2026 年最热的赛道上，作者既是规则的制定者，也是最大的受益者。

## 套利机会分析

- **信息差**：✅ 已被市场充分定价（15K stars / 20 个精确行业话题标签 / Apache 2.0），但作为「Claude Code 生态在 Security 垂直的事实标准」具备极强的引用价值。短期内没有「早期套利」空间
- **技术借鉴**：✅ Progressive Disclosure + Frontmatter 元数据模式可直接复用到任何「LLM 消费的知识库」场景（医学教科书、法律条文、企业内部 runbook）；五框架映射模式可复用到受强监管行业（金融 PCI / 医疗 HIPAA / 汽车 ISO/SAE 21434）；agentskills.io 分发协议是「AI 时代内容产品」的标配
- **生态位**：✅ 填补「AI Agent 时代 + 安全合规垂直」交叉的空白——未来一年内 GRC SaaS / SOC 平台 / 安全咨询公司都需要类似的内容资产
- **趋势判断**：✅ 强增长。MITRE ATT&CK v19 即将于 2026-04-28 上线（Defense Evasion 拆分为 Stealth / Impair Defenses），作者已规划迁移；Issue #59 揭示「multi-agent-prompt-injection-defense」方向预示赛道向「AI Security 自防御」延展——比通用 Agent 框架有后发优势

## 风险与不足

- **i18n 严重不足**：仅 6/754 个 skill 有西班牙语版本（SKILL.es.md），其他 11+ 主流语言未覆盖——对中文/日文/法语等大市场需求为零
- **MITRE ATT&CK v19 迁移风险**：README 已注明 v19 即将上线会拆 Defense Evasion，但作者尚未给出迁移路线图——若 4 月底未及时迁移，218 个 technique 映射会失准
- **真实痛点：防御性安全工具会误报**：Issue #33/#24 多次出现「ESET Smart Security / Windows Defender 把 skill 内容当恶意软件」的 bug 报告——这是「用 AI 自动化做攻防」赛道的典型摩擦，对企业级采用是潜在阻碍
- **集成稳定性问题**：Issue #56（phishing skills tab 渲染失败）+ #65（NPX 安装失败）揭示「前端分类 UI」与「分发链 NPX」是当前最易出问题的两个集成点——前端工程化滞后于内容扩张
- **技能内容正确性无自动化验证**：仅做形式校验（frontmatter 字段存在性、kebab-case、长度），无 skill 工作流步骤正确性的自动化测试——这对企业级采用是潜在风险信号
- **缺乏单元测试 / 集成测试**：validate-skill.py 是形式校验而非功能验证，754 个 skill 的工作流步骤全靠人工 review——3 个月从 0 扩到 754 的速度意味着人工 review 必然存在遗漏
- **单人主导风险**：75.4% commit 来自单一作者（虽然有 2 个别名账号 + 5 个外部贡献者），若作者精力转向 Casky 商业化或学术研究，仓库维护可能放缓

## 行动建议

### 如果你要用它
- **首选场景**：你的团队正在用 Claude Code / Cursor / Copilot 做 IR / 取证 / 威胁狩猎 / 红蓝队 / 合规审计，希望 AI 副驾能按 playbook 工作——直接 `npx skills add mukul975/anthropic-cybersecurity-skills` 一键安装
- **次选场景**：你的 SOC 平台 / 安全产品想以「技能包」形式快速给产品赋能——用 `marketplace.json` 协议集成
- **不推荐场景**：你需要企业级 SLA + 测试覆盖 + 多语言支持的合规库——目前 754 skill 仅 6 个有西语版本，测试覆盖为 0
- **对比说明**：vs ComposioHQ/awesome-claude-skills（聚合目录，本仓库是结构化内容）；vs LangChain（通用框架，本仓库是 Security 垂直内容）；vs cve-mcp-server（工具调用，本仓库是决策流程）——四者组合使用效果最佳

### 如果你要学它
- **重点关注文件**：
  - `tools/validate-skill.py`（290 行 stdlib Python）— 极简形式校验的工程范本
  - `skills/<单个 skill>/SKILL.md` — frontmatter + 标准化段落结构（When to Use / Prerequisites / Workflow / Verification）的范本
  - `mappings/ATTACK_COVERAGE.md`（55KB）— 五框架映射的呈现范本
  - `index.json`（170KB）— 机器可读元数据缓存的 schema
  - `.claude-plugin/marketplace.json` — plugin 分发协议的标准格式
  - `.github/workflows/validate-skills.yml` + `update-index.yml` + `sync-marketplace-version.yml` — CI/CD 三件套
- **重点关注模式**：Frontmatter 渐进披露 / 一行 npx 安装 + 多平台分发 / 轻量 stdlib 校验脚本 / Alias 兼容 schema 演进 / 自动重建索引 / 命名即 API

### 如果你要 fork 它
- **可改进方向**：
  - **i18n 全覆盖**：从西语扩到中/日/法/德/俄/阿，覆盖非英语安全从业者市场
  - **内容正确性验证**：建立「skill × 真实 CVE / 真实告警」回放测试集，用 SIEM / EDR 验证 skill 工作流的有效性
  - **ATT&CK v19 提前迁移**：在 2026-04-28 前完成 Defense Evasion 拆分（Stealth / Impair Defenses）映射更新
  - **CLI 工具**：基于 754 skill 构建 `cybersec-cli`，让没有 AI 平台的传统 SOC 也能用 skill 工作流
  - **行业垂直裁剪**：抽出金融 PCI、医疗 HIPAA、汽车 ISO/SAE 21434 的合规子集，做强监管行业专用版
  - **ATT&CK 双向桥接**：建立「skill → ATT&CK technique」之外的反向桥接「ATT&CK technique → 推荐 skill」，让告警能直接触发 skill 调用
  - **Agent 自评估**：让 skill 包含「成功标准」字段，AI 代理执行完工作流后自动评估是否达成，反向校准 skill 质量

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | GARS-2026 学术调查（SRH Berlin 监管，CC-BY 4.0，待发表） |
| 在线 Demo | Casky.ai Playground（作者 SaaS 化尝试，50 token 激励） |
| 关联 MCP | [Mahipal/cve-mcp-server](https://github.com/Mahipal/cve-mcp-server)（同作者 CVE 检索 MCP，990★） |
| 学术引用 | [CITATION.cff](https://github.com/mukul975/anthropic-cybersecurity-skills/blob/main/CITATION.cff)（含 BibTeX） |
| 同作者其他 OSS | mcp-windows-automation（36★） / claude-team-dashboard（51★） |