# GitHub 推荐：2.5 个月 17K stars：Google Labs 用 DESIGN.md 把设计 token 时代翻篇

> GitHub: https://github.com/google-labs-code/design.md

## 一句话总结

DESIGN.md 是 Google Labs 给 AI 编码 agent 写的「设计说明书」格式——用 YAML token + 自然语言 prose 的双层结构，让 agent 像读 README 一样读懂你的设计系统，是 design token 标准化 7 年来第一次「范式跳跃」。

## 值得关注的理由

1. **范式跳跃**：「Prose, not Tokens」是 spec 的第一公民——把 design spec 从「token 表」翻成「设计叙事」，在 W3C DTCG / Style Dictionary 内卷的赛道里撕出新维度。
2. **Google 黄金三角**：David East（Firebase 圈 DevRel 传奇）+ Matt Van Horn + Dion Almaer 三人组——把十年 DevRel 经验（讲清楚复杂技术）直接应用在 spec 设计上，**这是 Google 官方下场做 agent 时代规范的卡位战**。
3. **工程化达到 v1.0 水平**：0.3.0 alpha 阶段就有 Result pattern / 严格 TS / spec-config 单源真相 / CI 跑 Windows npm 冒烟、5 步流水线——比 90% 的 1.0 项目都严谨。
4. **完整生态闭环**：CLI + linter + 9 条 lint 规则 + Tailwind v3/v4 / DTCG 导出 + 3 个示例项目 + `.agents/` 自嵌 4 个 skill = 「不是 demo 是产品」。

## 项目展示

> 项目早期阶段不依赖视觉素材，纯靠 CLI JSON 输出 + 设计叙事文件展示价值。下方三组「代码即素材」是 design.md 最能传达自身定位的形式。

```yaml
# 示例 1：完整的 DESIGN.md（来自 README，Heritage 主题）
---
name: Heritage
colors:
  primary: "#1A1C1E"      # Deep ink for headlines
  secondary: "#6C7278"    # Sophisticated slate
  tertiary: "#B8422E"     # "Boston Clay" — sole driver for interaction
  neutral: "#F7F5F2"      # Warm limestone foundation
typography:
  h1:        { fontFamily: Public Sans, fontSize: 3rem }
  body-md:   { fontFamily: Public Sans, fontSize: 1rem }
  label-caps: { fontFamily: Space Grotesk, fontSize: 0.75rem }
rounded: { sm: 4px, md: 8px }
spacing: { sm: 8px, md: 16px }
---

## Overview
Architectural Minimalism meets Journalistic Gravitas. The UI evokes a
premium matte finish — a high-end broadsheet or contemporary gallery.
```

```jsonc
// 示例 2：lint 命令输出（agent DX-first，JSON 是默认）
$ npx @google/design.md lint DESIGN.md
{
  "findings": [
    {
      "severity": "warning",
      "path": "components.button-primary",
      "message": "textColor (#ffffff) on backgroundColor (#1A1C1E) has contrast ratio 15.42:1 — passes WCAG AA."
    }
  ],
  "summary": { "errors": 0, "warnings": 1, "info": 1 }
}
```

```text
// 示例 3：PHILOSOPHY.md 的核心反例对比（这是项目最深的叙事素材）

❌ 形容词清单（携带信息量低）：
"The design should feel modern, clean, trustworthy, and premium."

✅ 具体参考（携带信息量大）：
"A 1970s graduate lecture handout in the tradition of an old
 and established university."

// 一句"1970s lecture handout"就同时传递了：不要渐变、不要 italic、
// 不要圆角、要衬线字体、要留白——10 个 Don't 清单 1 句话搞定。
```

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/google-labs-code/design.md |
| Star / Fork | 17,225 / 1,563（fork 转化率 9.1%，高于一般设计 token 库 5%） |
| 代码行数 | 9,415（TypeScript 64.2% / JSON 30.3% / JS 4.2% / YAML 1.3%），113 文件 |
| 项目年龄 | 2.5 个月（2026-04-10 首发） |
| 开发阶段 | 稳定维护（40 commits，近 30 天 13 commits） |
| 贡献模式 | 核心少数 + 社区（18 人，主作者 David East 占 42.5%） |
| 热度定位 | 大众热门（2.5 个月破万星，设计系统赛道近 5 年最热） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] CI/CD[完善] |
| License | Apache 2.0 |
| 当前版本 | v0.3.0（4 个 tag，平均 19 天一个 release，预期未来有 v1.0 毕业） |
| Runtime 依赖 | **0**（自实现 oklch/lab/hwb/color-mix 解析） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

项目挂在 `google-labs-code` Organization 名下，账号 2.3 年、2,546 粉丝、8 个公开仓库，组织内核心项目按 stars：design.md 17,225 / stitch-skills 6,149 / jules-awesome-list 3,089 / stitch-sdk 1,723。

**核心贡献者三人组**——这是 Google 内部一支前 Firebase / Web 平台明星 DevRel 团队的二次创业产物：

- **David East（17 commits，42.5%）**：项目灵魂人物。Firebase 圈 DevRel 传奇，曾任 Firebase 团队 Lead / DevRel、polymer / firebase-js-sdk 早期贡献者、YouTube 「Firecasts」 系列讲师。近期主导 Stitch / design.md 对外布道。
- **Matt Van Horn（3 commits）**：前 Google Developers / Web.Fundamentals 团队成员，知名 PWA / Polymer 推广 DevRel。
- **Dion Almaer（1 commit）**：Google 工程总监、PWA / Web 平台老兵，与 Matt Van Horn 长期合作布道 Web Platform。

其他贡献者多为 Google 内部员工（tejas100、tototofu123、vikks、chelseayerong 等）。

**关键判断**：这不是「工程师主导」的项目，而是「开发者关系+产品经理」主导——核心技能是把复杂技术讲清楚的人。

### 问题判断

设计 token 标准化（W3C DTCG）已经走过 7 年，Style Dictionary 等工具链成熟，但 Google 内部 Stitch 团队在 2024–2025 年发现的事实是：把 DTCG JSON 直接喂给编码 agent，**生成质量并不比裸 prompt 好多少**——因为 agent 仍然没有「这套设计的精神」信息。

更深的痛点是：旧 token 工作流是**单向「设计→代码」**，而 agent 时代是**多向「prompt↔设计」循环**，需要 spec 本身能被人/agent 双向读写。

**时机为什么是现在**？2025 年中到 2026 年，AI Coding Agent 真正进入主流——Jules、Claude Code、Cursor 把「agent 持续读上下文」做成产品形态。AGENTS.md 模式被验证可行，但行业里没有任何**垂直领域版本**。design.md 是 Google Labs 给「design 这一类垂直知识」做的示范。

### 解法哲学

> 「Prose, not Tokens, is the focus of the specification」——design.md 哲学宣言第一句

**5 条设计哲学**（来自仓库内 `PHILOSOPHY.md`）：

1. **Prose is the spec**：token 是给 prose 服务的上下文，不是渲染指令
2. **具体参考 > 形容词清单**：「A 1970s graduate lecture handout」胜过「modern, clean, trustworthy, premium」
3. **Negative constraints come free**：说清楚「是什么」，「不是什么」自动被识别；显式列 Don't 清单是补充
4. **Consumer-tolerant**：未知 section / 未知 color name 直接保留，不让 agent 在新内容上失败（forward-compatible）
5. **Tokens ≠ rendering**：token 值是「context」，不是「instructions」——避免与 W3C DTCG 正面竞争

**「不做什么」清单**（核心防御）：
- 不做 design-as-code（避开 shadcn 路线）
- 不做 design-to-code Figma 同步
- 不正面替换 DTCG（做上游，不做竞品）
- 不做 prose 生成器（不替用户写设计参考）

### 战略意图

**Stitch 入口格式**：design.md 是 Google Labs 的 AI UI 设计工具 Stitch 向外公开的「设计描述标准」——Stitch 内部生成设计用的就是 prose+token 混合格式，现在把它开放成 spec，等于把 Stitch 的输入接口变成行业标准。

**Google Labs agent 矩阵**的一员：与 `Jules`（AI coding agent）、`jules-awesome-list`、`stitch-sdk` 一起构成 Google Labs 在 agent 时代的工具链矩阵。design.md 是矩阵里的「design layer」——agent 写代码时需要的「设计上下文」，与 AGENTS.md（通用上下文）互补。

**生态卡位策略**：
- **不与 DTCG 竞争，做上游**：`design.md export --format dtcg` 一行转换
- **不与 Style Dictionary 竞争，做上游**：通过 export 把 design.md 翻译为 Tailwind v3/v4 theme 配置
- **不与 Figma 竞争，做平行的纯文本格式**：design.md 是「在仓库里」的设计真相，Git diffable、可 PR review

**开源策略**：genuinely open（CLA 必签但代码 Apache 2.0），无 open-core，无 SaaS 版本——Google Labs 争夺「agent 上下文标准」话语权的工具，战略价值高于商业化价值。

## 核心价值提炼

### 创新之处

1. **Prose-first 规范范式**（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）：把 design spec 的第一公民从结构化数据翻成自然语言叙述，token 退为 prose 引用的「具名常量」。这是 W3C DTCG 7 年范式的根本性切割。

2. **`preEvaluate()` 把 finding 按 severity 分级为「fixes / improvements / suggestions」**（4/5 | 5/5 | 5/5）：同一规则两种 grouping，扁平 findings 给人/agent 看，分级 edit menu 直接喂给「AI 自动修复」 workflow。

3. **`.agents/` 自嵌入 4 个 skill（dogfooding）**（5/5 | 5/5 | 3/5）：仓库根目录的 `.agents/skills/` 放了 tdd / ink / agent-dx-cli-scale / typed-service-contracts 四个 skill——**design.md 用自己发布的 agent skill 指导自己的开发**。

4. **`spec-config.yaml` 单源真相驱动全栈**（3/5 | 5/5 | 5/5）：YAML 一份 → linter / docs / 多个 export 器共享。CI 强制 `bun run spec:gen --check` 验证生成结果与 docs 匹配——spec 永远不会与实现脱节。

5. **自实现 CSS 颜色解析（oklch/lab/hwb/color-mix）**（3/5 | 5/5 | 5/5）：纯 TS 自实现 CSS Color Module Level 4 全套颜色空间 + WCAG relative luminance 计算，**0 runtime 依赖**——任何需要 WCAG 对比度或色域转换的前端工具都受益。

6. **Agent DX-first CLI 标准**（3/5 | 5/5 | 5/5）：默认 JSON + stdin 接受（`-` 输入）+ exit code 语义（errors>0 返 1）+ 自评 `agent-dx-cli-scale` skill。2025+ 所有面向 agent 工作流的 CLI 的事实标准。

7. **`token-like-ignored` rule 的启发式**：用纯 TS 启发式（hex 正则 + dimension 正则 + 5 个 typography key）判断「未知 key 值是不是设计 token map」——是的话提示用户「export 会丢这个 key」。

### 可复用的模式与技巧

1. **「Spec & Handler」 Vertical Slice 模式**：每个子系统有 `spec.ts`（Zod schema + Result type + Interface）+ `handler.ts`（实现 class，不抛异常）+ `*.test.ts` 同行测试。**所有严格契约、强测试覆盖的 TypeScript 服务都适用**。

2. **Pipeline 编排（Parser → Model → Validator → Emitter）**：长处理路径分 4 个独立 handler，每个可 mock 可测。**所有「配置解析 + lint + codegen」工具的通用骨架**。

3. **Pure functional rule runner + RuleDescriptor 双形态**：`LintRule = (state) => Finding[]` 纯函数 + `RuleDescriptor = { name, severity, description, run }` 元数据壳子。`runLinter` 同时接受两种输入（`isDescriptorArray` 适配）。**所有可插拔 lint/validation 工具**。

4. **CI 包含 `npm-registry-smoke-windows`**：在 windows-latest 上真实从公网 `npm install @google/design.md@latest` 跑一遍。**所有公开 npm 包的发布后冒烟测试**。

5. **跨平台 bin 命名 hack**：`bin: { 「design.md」: ..., 「designmd」: ... }` 双名注册同一份 `./dist/index.js`，因为 Windows 上 `.md` 后缀与 PowerShell 关联冲突。**所有跨平台 CLI**。

6. **MDX 代码生成 spec 文档**：手写 `spec.mdx` 模板 + renderer 从 SPEC_CONFIG 注入示例，CI `--check` 模式强制对齐。**所有 spec-driven 工具（编译器、linter、formatter）的「代码即文档」**。

### 关键设计决策

1. **决策：单源真相 `spec-config.yaml` 驱动全栈**
   - **问题**：spec 同时驱动 linter 规则、Tailwind 导出、DTCG 导出、docs/spec.md 文档，任何一个常量被改三遍，spec 就会漂移
   - **方案**：YAML → Zod 校验 → 缓存 lazy singleton → 同时被 linter / spec-gen / rules 引用
   - **Trade-off**：引入一层代码生成 + CI check；好处是 spec 永远不会与实现脱节
   - **可迁移性：高**

2. **决策：Consumer-tolerant 哲学在 model 层落地为「保留未知键」**
   - **问题**：design system 在演进（motion / icons / audio），spec 不能每加一个就等下一版
   - **方案**：parser 保留 `rawValues`，model 保留 `unknownKeys` + `unknownKeyValues`，linter 用 Levenshtein ≤ 2 提示拼写错误、> 2 静默 + `token-like-ignored` 提示 export 会丢
   - **Trade-off**：用户写错 key 时 spec 不强制拒绝——把「spec 严格性」换成「agent 提示性」
   - **可迁移性：高**（所有「渐进式 schema 演进」项目）

3. **决策：Symbol Table + 链式引用解析 + 循环检测**
   - **问题**：YAML 里 `{colors.primary}` 跨段引用，需要两遍解析 + 防环
   - **方案**：ModelHandler.execute 分 3 phase：phase 1 解析 primitive + 把 reference 暂存 symbolTable；phase 2 走所有 reference 做链式 resolve（`resolveReference(symbolTable, path, visited, depth)` 用 visited Set 防环 + `MAX_REFERENCE_DEPTH=10` 防深链）；phase 3 构建 component map
   - **Trade-off**：两遍扫描的复杂度换「任意方向的引用」
   - **可迁移性：高**（style dictionary、kustomize 等「配置语言支持跨段引用」工具）

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | DESIGN.md | W3C DTCG | Style Dictionary | Figma MCP | Tokens Studio | AGENTS.md |
|------|-----------|----------|------------------|-----------|---------------|-----------|
| **核心定位** | 设计叙事 spec | Token schema | Token 编译工具 | 画板 → agent 桥 | Figma 内 token UI | 通用 agent 上下文 |
| **prose 上下文** | ✅ 核心 | ❌ | ❌ | ❌ | ❌ | ✅ 全部 prose |
| **结构化 token** | ✅ YAML | ✅ JSON | ✅ JSON | ✅ 节点树 | ✅ JSON | ❌ |
| **行业标准地位** | alpha | W3C 工作组 | 事实标准 | Figma 官方 | Figma 生态成熟 | 多 agent 内置 |
| **CI 可校验** | ✅ 9 条 rule | ❌ 需自建 | ❌ | ❌ | ❌ | ❌ |
| **导出到 Tailwind** | ✅ v3/v4 | 需 SD 转换 | ✅ 直接 | ❌ | ✅ | ❌ |
| **多主题/模式** | ❌（Issue #13） | ✅ | ✅ 透传 | ✅ Figma 本身 | ✅ 3+ 年领先 | N/A |
| **Git diff 友好** | ✅ prose | ⚠️ JSON 噪声 | ⚠️ | ❌ 版本号 | ⚠️ 早期不存 | ✅ |
| **agent 友好** | ✅ JSON 默认 + stdin | ⚠️ | ⚠️ Node 库 | ✅ | ⚠️ | ✅ 通用 |

### 差异化护城河

1. **范式护城河**：「Prose > Tokens」是 design.md 的根本命题，竞争对手都还在「tokens 标准化」维度上内卷
2. **agent 时代卡位**：Google Labs 把 design.md 与 Jules/Stitch 工具链捆绑，是目前唯一一个「既出 agent、又出 spec」的组织
3. **生态互补**：与 DTCG（下游）/ Style Dictionary（下游）/ Figma（平行）全部是上游或平行关系，不替代
4. **工程化护城河**：alpha 阶段就达到 v1.0 水平（严格 TS + Result pattern + Windows CI 冒烟），追赶难度高

### 竞争风险

1. **Issue #13「多主题/模式」**——这是 design.md 最大的不确定性，**2 个月无官方回复**。Tokens Studio 在该维度领先 3+ 年。如果 Stitch 团队年内不解决，会被用户抛下
2. **Figma 内部推进**——Figma 官方如果加一个「design description」 prose layer，design.md 失去差异点
3. **AGENTS.md 演化**——如果扩展出「AGENTS.design.md」子规范，可能直接吃掉 design.md 的 agent 上下文卡位
4. **W3C DTCG 截胡**——DTCG 同期也在做「AI-friendly token format」，标准组织有可能碾压 Google Labs 单方规范
5. **Jules/Stitch 商业化**——如果 Stitch 收费，design.md 可能被绑到 Stitch SaaS 内失去 open 性质

### 生态定位

- **垂直层**：「设计」领域的 spec 描述格式
- **生态位**：与 AGENTS.md（通用）平行；与 DTCG（schema）/ Style Dictionary（编译）/ Figma（GUI）形成互补矩阵
- **角色**：「prose layer」——位于「设计意图」和「代码生成」之间，是 LLM 时代的中间语言

## 套利机会分析

- **信息差**：**高**——2.5 个月 17K stars，但国内技术社区对 design.md 的认知度仍低，知道「Prose over Tokens」哲学的人更少。这是公众号会爆款的方向。
- **技术借鉴**：
  - **Spec & Handler 模式** + **Result pattern 零 throw** → 任何 TypeScript 服务可照搬
  - **`spec-config.yaml` 单源真相** + **MDX 代码生成文档** + **CI `--check` 强制** → 任何 spec-driven 工具的「代码即文档」最佳实践
  - **Pure functional rule runner + RuleDescriptor** + **`preEvaluate()` 分级** → 任何可插拔 lint 工具的标杆架构
  - **自实现 oklch/lab/hwb/color-mix 解析** → 任何需要 WCAG 对比度或色域转换的前端工具
  - **Agent DX-first CLI 标准** → 2025+ 所有面向 agent 工作流的 CLI 的事实标准
- **生态位**：填补「AI 时代设计 spec」这个空白——DTCG / Style Dictionary 在「token 怎么流转」上做了 7 年，但「设计意图怎么表达给 agent」没人做
- **趋势判断**：**强增长**——2.5 个月 17K stars，爆发型增长；fork 转化率 9.1%（高于一般设计 token 库），说明开发者动手改造意图强；与 AI Coding Agent 主线趋势完全对齐

## 风险与不足

1. **关键 Issue 长期 open**：#13「多主题/模式」2 个月无官方回复是最大不确定性。Tokens Studio 在该维度领先 3+ 年。
2. **alpha 阶段 + Owner 是 Organization**：未来若 Google 战略调整，组织仓库可能停摆（类似 Polymer 的命运）。
3. **viral star ≠ production 落地**：需要观察是否有大厂 / 框架实际采用（截至目前没有 shadcn / Tailwind / Vercel 等生态接纳信号）。
4. **生态窗口期**：W3C DTCG 同期也在做「AI-friendly token format」，存在被标准组织截胡的可能。
5. **CHANGELOG 缺失**：仓库无 CHANGELOG.md / HISTORY.md，仅靠 git history + 0.3.0 版本号。
6. **Test commit type 占比 0%**：测试文件高频维护（`handler.test.ts` 改了 9 次），但 commit message 不打 `test:` 标签——对 release-note 工具是挑战。
7. **规范哲学与工程现实的张力**：Issue #63「单仓多文件策略」未定，monorepo 团队会立刻遇到。

## 行动建议

- **如果你要用它**：直接用——0 runtime 依赖 + Apache 2.0 + 跨平台 + agent DX-first。**先等 v1.0 解决多主题再生产采用**（#13 是 blocker），alpha 阶段适合个人/小团队探索。
- **如果你要学它**：重点关注这些文件
  - `PHILOSOPHY.md`（5 条设计哲学必读）
  - `packages/cli/src/linter/model/handler.ts`（linter 核心）
  - `packages/cli/src/linter/model/spec.ts`（schema 定义）
  - `packages/cli/src/linter/linter/rules/index.ts`（规则集）
  - `packages/cli/src/linter/spec-config.yaml`（单源真相）
  - `examples/atmospheric-glass/DESIGN.md`（最佳实践示范）
- **如果你要 fork 它**：可以改进的方向
  - 实现 Issue #13 多主题/模式（最大缺口）
  - 加 OKLCH 之外的支持（display-p3 等更广色域）
  - 实现 Storybook addon（让 design.md 变 living styleguide）
  - 加 Motion / Iconography / Accessibility token 支持
  - VS Code 插件（实时 lint 高亮）

### 知识入口

| 资源 | 链接 |
|------|------|
| GitHub README | https://github.com/google-labs-code/design.md |
| PHILOSOPHY.md（仓库内） | https://github.com/google-labs-code/design.md/blob/main/PHILOSOPHY.md |
| 完整规范 | https://github.com/google-labs-code/design.md/blob/main/docs/spec.md |
| DeepWiki | 未收录（403 拒绝） |
| Zread.ai | https://zread.ai/google-labs-code/design.md |
| 官方 spec 站 | https://stitch.withgoogle.com/docs/design-md/specification |
| 关联论文 | 无（工程实践，无学术论文） |
| 在线 Demo | `npx @google/design.md lint <DESIGN.md>`（CLI 即 demo） |
