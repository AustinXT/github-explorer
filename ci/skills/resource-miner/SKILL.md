---
name: resource-miner
description: >
  Deep analysis and value mining of "resource-type" GitHub repositories — awesome
  lists, learning materials (tutorials, roadmaps, courses, books, interview prep),
  and atypical non-code projects (config specs, template/rule libraries, doc sites,
  media playlists, free-service repos). Analyzes curation quality, content scale &
  structure, update rhythm & automation signature, distribution/commercial model,
  and replicability — instead of code architecture. Use when the target repo is a
  curated collection, a study/learning resource, or a non-code project, or when the
  user asks to analyze an awesome-list / tutorial / roadmap / dataset-style repo.
  For ordinary code projects use repo-miner instead.
argument-hint: <github-url> [--type awesome|learning|atypical]
disable-model-invocation: false
model: opus
metadata:
  author: NightVoyager
  title: 资源类 Repo 深度挖掘
  description_zh: |
    对「资源类」GitHub 仓库（awesome 列表 / 教程·路线图·课程·书 / 非典型非代码项目）
    做深度价值分析，产出与 repo-miner 同骨架的中文报告（可直接进站点/公众号流水线）。
    分析镜头换成：策展质量、内容规模与结构、更新节奏与自动化签名、分发/商业模式、可迁移性，
    而非代码架构。Orchestrator-Worker 三阶段委托 subagent，主对话只留结构化摘要。
  dependencies:
    - gh
    - git
    - jq
  version: 1.0.0
  license: MIT
---

# Resource Miner — 资源类 GitHub 仓库深度挖掘

对「没有代码架构」的资源类仓库做深度价值分析。repo-miner 的三段式框架侧重代码架构 /
创新点 / 可复用代码模式，套不进 awesome 列表、教程书、数据集这类仓库（会得「近零代码行
= 已放弃」的错误结论）。本 Skill **保持报告骨架不变**（下游解析器依赖），把**分析视角 +
采集指标**换成资源视角。

**输入：** `$ARGUMENTS`（GitHub URL `https://github.com/owner/repo`，可选 `--type awesome|learning|atypical` 覆盖自动判型）

## When to Use

- awesome / 精选资源合集（`awesome-*`、cheatsheet 集、清单仓库）
- 学习资料：教程、路线图（roadmap）、课程、书、面试题、知识手册
- 非典型非代码项目：配置规范（如 toml）、模板/规则库（如 nuclei-templates）、文档站、媒体列表（IPTV/直播源）、免费服务仓库
- 评估这类仓库的策展质量、运营模式、可迁移的运营/自动化经验、信息差套利

**Don't use for:**
- 普通代码项目 / 库 / 框架 / 应用 → 用 **repo-miner**
- Agent Skills 仓库（SKILL.md 合集 / `.claude-plugin` marketplace）→ 未来由 **skills-miner** 专门处理；当前若必须分析，可临时按 `--type atypical` 降级，但不做单 skill 抽样评估
- 仅需 README 概要的简单查询

## 架构说明（Orchestrator-Worker，沿用 repo-miner 模式）

```
/resource-miner <url>（主对话 = 编排者）
│
├─ 准备：gh repo clone → 跑 collect_resource_facts.py（含 detected_type）→ 提取变量
│
├─ Phase 1 + Phase 2（并行 Agent 调用，各自 Read FACTS_JSON 所需字段）
│   ├─ Agent → 网络分析（作者/热度/增长/竞品/媒体/知识入口）
│   └─ Agent → 内容规模与策展元分析（内容规模/结构/更新节奏/自动化签名）
│
├─ Phase 3（串行 Agent，接收 Phase 1 摘要 + detected_type）
│   └─ Agent → 策展内容分析（按子类型分支）
│
└─ 主对话：基于三份摘要按 report-template.md 组装最终报告
```

**为什么这样做：** 各阶段的原始数据（gh JSON、git log、文件遍历）留在 subagent 隔离
context 里，主对话只累积三份结构化摘要（约 3000 字），context 保持干净。Phase 1/2 独立可并行。

## 前置工具检查

```bash
which gh && which git && which jq && echo "All tools ready"
```

缺失则停止并提示 `brew install gh git jq`。**不需要 tokei/onefetch**（资源仓库无需代码行统计）。

## 执行流程

### 准备阶段（主对话内执行）

从 `$ARGUMENTS` 提取 GitHub URL（支持 `https://github.com/owner/repo` 或简写 `owner/repo`）
和可选 `--type`。

```bash
# 完整 clone（需完整 commit 历史算更新节奏 + 自动化签名）；超大仓库用 --filter=blob:none
git clone <url> /tmp/resource-miner-<repo>
# 备用：git clone --filter=blob:none <url> /tmp/resource-miner-<repo>
```

**提取关键变量**：`OWNER` / `REPO` / `LOCAL_PATH`(`/tmp/resource-miner-<repo>`) /
`FULL_NAME`(`owner/repo`) / `GITHUB_URL` / `DEFAULT_BRANCH`。

```bash
DEFAULT_BRANCH=$(cd /tmp/resource-miner-<repo> && git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/origin/||' || echo "main")
```

#### 确定性数据采集（一次性，供 Phase 1 + Phase 2 共用）

```bash
# 优先用 skill 自带脚本；本仓库回退到 src/scripts
FACTS_SCRIPT="${CLAUDE_PLUGIN_ROOT}/scripts/collect_resource_facts.py"
[ -f "$FACTS_SCRIPT" ] || FACTS_SCRIPT="src/scripts/collect_resource_facts.py"
# 透传用户的 --type（若提供）
FACTS_JSON=$(python3 "$FACTS_SCRIPT" "$LOCAL_PATH" --full-name "$FULL_NAME" ${TYPE_FLAG:-})
# 脚本把 JSON 写入 tmp/resource-facts-<repo>.json 并把该路径打印到 stdout
```

脚本只把**路径**打印到 stdout（大体积原始数据落文件），主对话 context 保持干净。
读 `FACTS_JSON` 顶层的 `detected_type`（`awesome|learning|atypical`，`--type` 会覆盖），
作为 `DETECTED_TYPE` 变量传给 Phase 3。把 `FACTS_JSON`（路径）传给下面三个 Agent。

> **提前终止**：若 `detected_type` 不属于资源类、或这其实是个普通代码项目（`content_scale.main_ext`
> 是 `.py/.ts/.go/.rs` 等且有真实依赖清单），提示用户「这是代码项目，建议改用 repo-miner」并停止，
> 不硬套资源模板。

### Phase 1 + Phase 2（并行启动两个 Agent，必须同一响应内同时发起）

#### Agent 1 — 网络分析
读取 `${CLAUDE_SKILL_DIR}/reference/phase-1-network.md` 完整指令，启动 subagent，
prompt 含该指令 + 替换变量 FULL_NAME/OWNER/REPO/GITHUB_URL/LOCAL_PATH/DEFAULT_BRANCH/**FACTS_JSON**。

#### Agent 2 — 内容规模与策展元分析
读取 `${CLAUDE_SKILL_DIR}/reference/phase-2-content-scale.md` 完整指令，启动 subagent，
prompt 含该指令 + 替换变量 LOCAL_PATH/FULL_NAME/**FACTS_JSON**。

### Phase 3（串行，依赖 Phase 1 结果）

等 Phase 1/2 都返回后启动。读取 `${CLAUDE_SKILL_DIR}/reference/phase-3-curation.md` 完整指令，
启动 subagent，prompt 含该指令 + 替换变量 LOCAL_PATH/FULL_NAME/GITHUB_URL/**DETECTED_TYPE**/**FACTS_JSON**，
并**附加 Phase 1 关键结果**作为上下文：作者画像摘要、官方文档/博客、竞品清单（同主题资源）、关键 Issue 信号。

Phase 3 据 `DETECTED_TYPE` 选镜头：`awesome` / `learning` / `atypical` 三分支 + 共用收尾。

### 报告组装（主对话内执行）

收到三份摘要后，**严格按 `${CLAUDE_SKILL_DIR}/reference/report-template.md` 组装**。
该模板是**硬约束**：H1 + `> GitHub:` 行 + 固定 `##` 章节 + 项目画像表的**可解析行键白名单**
必须原样保留，否则下游 `build_reports_index.py` 解析失败、报告无法入库上站。

组装原则：
- 直接用各 Phase 的结论，不重新推理
- 某 Phase 标注「跳过」的部分（如无竞品、无官方文档），对应节注明即可
- 「项目展示」：用 Phase 1 返回的展示素材 markdown；无则**省略整节**，不留空标题
- 全文中文、用直角引号「」（不用 ""）、正文 ≥4KB、结尾不截断

## 标题创作规则（H1 = 公众号文章标题，必读）

H1 会被下游直接当文章标题。**严禁** `# {repo} 深度分析报告` / `{repo} 全方位解读` 这类泛模板
（无点击竞争力；解析器虽会剥掉尾缀「深度分析报告」，但泛标题本身没价值）。

**准则**（同 repo-miner）：
1. **长度** ≤ 32 字
2. **至少含 2 个要素**：具体数据（star/年龄/条目数/仓库体积）、差异化卖点（「GitHub 当 CDN」「时钟式自动化策展」）、读者真实关心的问题、故事性反差（「一个人周更 4 年」）
3. **格式**：主标题 +「：」+ 副标题（钩子 + 解释）
4. **避免**：感叹号、emoji、营销词（震惊/必看/绝了）

**范例**：

| 仓库 | 差（禁用） | 好（参考） |
|---|---|---|
| awesome-english-ebooks | awesome-english-ebooks 深度分析报告 | GitHub 当图书馆：14GB 英语外刊免费库怎么周更 4 年不断 |
| coding-interview-university | 面试仓库分析 | 35 万星自学路线：一个人靠 GitHub 仓库刷进谷歌的 8 个月 |
| awesome-mac | awesome-mac 解读 | 10 万星 Mac 软件清单：1300 条目怎么做到中文社区第一 |

## 注意事项

### 分析原则
1. **判断 > 描述** — 每个发现给「so what」，对读者有什么用
2. **诚实 > 好听** — 低质堆砌的清单、停滞的项目、版权灰产，直说
3. **对比 > 孤立** — 放在同主题资源的竞品语境里评价
4. **运营/策展视角 > 代码视角** — 看策展判断力、更新治理、分发与商业闭环、自动化运维，而非函数与架构
5. **可迁移 > 抽象** — 提炼读者能搬走的运营/自动化模式
6. **引用 > 概括** — 引用具体数据附来源，不用「评价很高」这类空泛词

### 异常处理
- `gh` 限流 → 等待重试或减请求；`network` 块为 null 时只用离线指标（内容规模/更新节奏/自动化签名仍可产出）
- Clone 超时 / 大仓库 → `git clone --filter=blob:none`
- 官方文档/竞品/媒体不存在 → 跳过相应节并注明
- 判型疑似错误 → 用 `--type` 覆盖重跑，或在 Phase 3 据实修正并说明

### 补充资源
- 报告模板（硬约束）：[reference/report-template.md](reference/report-template.md)
- 命令速查：[reference/commands-cheatsheet.md](reference/commands-cheatsheet.md)
- Phase 1 详细指令：[reference/phase-1-network.md](reference/phase-1-network.md)
- Phase 2 详细指令：[reference/phase-2-content-scale.md](reference/phase-2-content-scale.md)
- Phase 3 详细指令：[reference/phase-3-curation.md](reference/phase-3-curation.md)
