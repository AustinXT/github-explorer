# GitHub推荐：21 个月 5,327 个 commit：一个人把 Vite 塞进微信小程序，还顺手做了个 MCP

> GitHub: https://github.com/weapp-vite/weapp-vite

## 一句话总结

weapp-vite 是把 Vite + Rolldown + Vue SFC + TypeScript + MCP 这套现代 web 工具链整套「塞」进微信原生小程序的构建器，自带自研的 Wevu 响应式运行时和快照 diff setData 优化，定位「不替换运行时只升级工程化层」——和 Taro / uni-app 的「换框架换运行时」路线正面错开。

## 值得关注的理由

1. **「不替换运行时」的路线本身是稀缺解**：Taro/uni-app 都是「用 React/Vue 渲染到 DSL 再编译回 WXML」，代价是丢掉原生 Page/Component 全部运行时语义，平台新能力要等框架跟进。weapp-vite 显式选择保留原生，只升级工程化层，让存量项目可以渐进接入。
2. **5,327 个 commit、1,370 个 tag、100+ Release、完整 monorepo + Turbo + Changesets 的工程化强度，对应只有 348 个 star——是中文前端圈被显著低估的项目**。同作者的另一项目 `weapp-tailwindcss` 已 1.8k stars，证明他「做出来的东西真有人用」。
3. **AI 协作是 1 等公民**：仓库根有 295 行的 `AGENTS.md` + 6 段强制 guard，独立 `packages/mcp` 暴露 stdio / streamable-http / Runtime REST 三层 transport，让 Claude/Codex 能在「真实小程序运行时」里截图、读 DevTools 日志、跑构建——这在小程序工具链里基本是独一份。

## 项目展示

![Star History Chart](https://api.star-history.com/svg?repos=weapp-vite/weapp-vite&type=Date) — 类型：hero（增长曲线）

![weapp-vite logo](https://raw.githubusercontent.com/weapp-vite/weapp-vite/main/website/public/logo.png) — 类型：logo / brand

![weapp-vite 官网 logo](https://vite.icebreaker.top/logo.svg) — 类型：hero logo（官网 header / 主视觉）

> 筛选说明：总共发现 9 个候选媒体元素，筛选后保留 3 个（Star History 曲线 + README logo + 官网 logo SVG）。**素材缺口**：项目 README 缺少架构图与 Demo GIF，官网无产品截图与教学视频——作者应该补 ① 整体 monorepo 架构图；② 一次 `pnpm create weapp-vite` 启动全流程的 GIF；③ IDE 内 HMR 效果对比。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/weapp-vite/weapp-vite |
| Star / Fork / Watcher | 348 / 22 / 3 |
| 代码行数 | 626,619（TS 70.9% / JSON 13.6% / JS 9.4% / YAML 4.0% / Vue 1.2%） |
| 文件数量 | 6,967 |
| 依赖数量 | 111 dev（pnpm monorepo，根 package.json runtime = 0） |
| 项目年龄 | 21 个月（首次提交 2024-09-19） |
| 开发阶段 | 密集开发（近 30 天 354 commits，2026 Q1 大爆发后已收敛到日均 ~12） |
| 开发模式 | 职业项目（周末 27.0%，深夜 34.3%；自动化 changeset + turbo + 100+ Release） |
| 贡献模式 | 单人主导（Top1 `sonofmagic` 占比 93.5%；外部贡献者累计 < 1%，bus factor = 1） |
| 热度定位 | 小众精品（348 stars 显著低估，5,327 commits 远超同 stars 量级项目） |
| 质量评级 | 代码：优秀 \| 文档：优秀 \| 测试：充分（836 .test.ts）\| CI/CD：完善 \| 错误处理：规范 |
| Monorepo | pnpm 11 + Turbo 2 + Changesets（pnpm-lock.yaml 854 次变更印证上游 Vite 同步密度） |
| 最新版本 | wevu@6.17.0（共 1,370 个 tag，双轨 semver） |
| 关键转折期 | 2026-01 ~ 2026-04（4 个月 3,541 commit，wevu 语义对齐 + 编译器拆分的关键窗口） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

主开发者 `sonofmagic`（组织 `weapp-vite` + 提交别名 `ice breaker`），独立开发者，bio 写「致力于提供更好的小程序开发体验」。账号年龄 1.7 年，组织 4 个仓库里本项目是唯一非 fork、非 0 star 的核心。同作者另一项目 `weapp-tailwindcss` 已 1.8k stars，是「把 Tailwind 接进小程序」的事实标准——这条产品线踩过的「文件类型编译产物和原生运行时对不上」的所有坑，本质上都是「小程序没有现代构建器」在每个新需求里重复触发。把工程化层抽出来作为独立产品，是从同赛道 star 数最多的两个项目经验里合成的判断。

### 问题判断

作者看到的问题是「小程序工程化整体落后于 web 一个时代」：没有 HMR、TypeScript、ESM、Vue SFC、PostCSS/Sass/Less、Tailwind、自动路由、自动组件导入、JSONC、路径别名——而 web 生态早在 2020 年就普及了。Taro/uni-app 试图用「换框架」补这个缺口，但代价是「写 React/Vue 经过编译还原」，团队从原生切过去要重写业务、调试要双层链路、平台 patch 要等框架跟进。作者判断「保留原生 + 升级工程化层」是被市场反复验证过、但没人做透的细分位。

### 解法哲学

- **「不替换运行时只升级工程化层」**——保留原生 Page/Component/wxml/wxss/wxs/json，不强行套 VDOM、不抢平台生命周期。
- **Vue 3 心智 + 小程序数据层**——Wevu 运行时保留 Vue 3 API 形态（ref/computed/watch/scope/effect/batch），但渲染目标不是 VDOM 而是「响应式 → 快照 → diff → setData」，性能优于 VDOM 方案。
- **AI 协作是 1 等公民**——AGENTS.md 显式把 AI 协作的工程纪律（monorepo 路由、dist sync、跨平台 CI、E2E 串行、隐私路径、变更集规则）写进仓库级一等公民。
- **现代 monorepo 工程范式全套迁移**——pnpm + Turbo + Changesets + fixed group + catalog + 6 道 publish 前 check。

### 战略意图

- 与 `weapp-tailwindcss` 形成「底层构建器 + 垂直适配器」的组合，定位不重叠。
- 多平台（微信/支付宝/抖音）通过「平台无关 plugin + 平台特定 rewrite」做扩展，证明这是一套为「多小程序平台」设计的工具链，而非单平台 hack。
- 暂无明确商业化路径，但 `packages/mcp` 暴露 REST endpoint 给非 MCP 客户端调用、`rolldown-require` 单独发布 npm 包给社区——能看到「从自家需求反哺社区」的产品思路。

## 核心价值提炼

### 创新之处

1. **快照 diff setData（patchScheduler + payload + snapshot + scheduler 4 模块联动）** — 响应式数据变化 → 收集 dirty path → 浅/深相等比较 → 路径化 patch → payload 大小阈值控制 → fallback 全量 snapshot，配合 51 行的微任务调度器做批量更新。**新颖度 4/5，实用性 5/5，可迁移性 4/5**。
2. **保留原生的渐进升级路线** — 与 Taro/uni-app 「换框架」路线相反，weapp-vite 让团队可以「用原生 + Vite 跑通 → 在新页面引入 Vue SFC + Wevu → 老页面不动」。**新颖度 4/5，实用性 5/5，可迁移性 3/5**。
3. **MCP server 三层 transport（stdio + streamable-http + Runtime REST）** — 单包同时支持嵌入 IDE、独立服务、REST 端点三套协议，把「静态工作区能力 / 命令执行能力 / 运行时 session 能力」三档区分。**新颖度 4/5，实用性 4/5，可迁移性 5/5**。
4. **AGENTS.md 作为仓库级一等公民 + 6 段强制 guard** — 把 AI agent 协作的工程纪律（monorepo 路由、dist sync、跨平台 CI、E2E 串行、隐私路径、变更集规则）显式写进 295 行的 AGENTS.md，并和 `.vscode/settings.json` 排除规则、Changesets 规则、scripts 钩子耦合。**新颖度 5/5，实用性 5/5，可迁移性 5/5**（这是该项目最具差异化、最值得其他项目借鉴的部分）。
5. **Vue 3 风格运行时但跑在小程序数据层（非 VDOM）** — 保留 Vue 3 API 形态，渲染目标是「响应式 → 快照 → diff → setData」。**新颖度 4/5，实用性 5/5，可迁移性 3/5**。
6. **oxc-parser 替代 Babel parser + 公开 benchmark 文档** — Rust 写的 OXC parser 替换 Babel，并在 `docs/architecture/weapp-vite-oxc-parser-vs-babel-parser.md` 公开实测数据（大文件 7%、中等文件 2x）。**新颖度 2/5，实用性 4/5，可迁移性 5/5**。
7. **自研 rolldown-require（独立 npm 包）** — 把 rolldown-vite 项目里「加载用户 TS/ESM 配置」的需求反向抽成独立 npm 包，README 诚实标注「bundle-require 是 esbuild 版，我们是 rolldown 版」。**新颖度 3/5，实用性 4/5，可迁移性 4/5**。
8. **共享 chunk 策略作为一等配置（hoist/duplicate/common × forceDuplicateTester × sharedMode × resolveSharedPath）** — 微信主包 2MB 体积限制下，把 chunk 拆分策略升级为一等配置 + 设计文档 + 复杂 fixture。**新颖度 3/5，实用性 5/5，可迁移性 3/5**。
9. **runtime marker 单一来源（@weapp-core/constants + 3 道自动 check）** — 跨包共享的常量收敛到一个包 + 3 道 CI check 脚本强制守住。**新颖度 3/5，实用性 4/5，可迁移性 5/5**。
10. **GitHub issue 1:1 e2e fixture + worktree 隔离修复流程** — 仓库里 `e2e-apps/github-issues` 子目录每个 issue 对应一个最小复现 app，加 AGENTS.md 强制规定 issue 修复流程。**新颖度 4/5，实用性 5/5，可迁移性 5/5**。

### 可复用的模式与技巧

1. **「保留原生 + 升级工程化层」路线**：与「替换运行时」路线相对——保留目标平台的所有原生语义，只升级构建器/工具链/类型工具。适用场景：所有「平台有完整原生能力 + 工程化陈旧」组合（小程序 / React Native / Flutter / Cordova 等老牌跨端方案）。
2. **响应式 → 快照 diff → patch + 大小阈值回退（4 模块联动）**：用「先比相等再走 patch，size 超阈值 fallback 全量」的协议骨架，把响应式桥接到任意受限的更新目标。适用场景：小程序/Worker/低带宽协议/嵌入式。
3. **MCP 三层 transport + 资源/工具/会话/提示词分层**：把 AI agent 与真实运行时的桥接分成「静态资源 + 命令执行 + 运行时 session + prompts」四档，并用 stdio/streamable-http/REST 三种 transport 覆盖不同客户端。适用场景：所有 AI agent 协作工具。
4. **AGENTS.md + 6 段强制 guard + .vscode/settings.json 排除规则**：把 AI agent 的工程纪律写进仓库级一等公民，并和 lint-staged/husky/skills:link 联动。适用场景：所有 AI 协作密集的仓库。
5. **Changesets fixed group + 6 道 publish 前 check**：30+ 包 monorepo 的发布纪律，包括 catalog 同步、changeset 校验、依赖范围校验、版本校验、rolldown 版本校验、ci:release 跑通。适用场景：所有 monorepo。
6. **oxc-parser 优先 + Babel fallback + 公开 benchmark 文档**：JS 解析热点场景的迁移套路。适用场景：bundler/linter/codemod/IDE 后端。
7. **runtime marker 单一来源 + 3 道 check 脚本**：跨包共享常量收敛。适用场景：所有 monorepo。
8. **GitHub issue 1:1 e2e fixture + worktree 隔离修复流程**：issue 多的长期维护仓库。适用场景：所有用户基数大、issue 多的项目。

### 关键设计决策

#### 决策 1：Vite 8 + Rolldown 1.1.2 底座 + 自研 rolldown-require
- **问题**：小程序工程想要 HMR、ESM、原生 ESM 生态、Vue SFC、Volar 类型工具链协同。
- **方案**：底座 Vite 8（catalog 锁定）+ Rolldown 1.1.2；自研 `rolldown-require` 处理配置预捆绑；为 Vite 钩子链扩展「小程序特有文件类型」：wxml → 字符串管道，wxss → sass/postcss 管道后输出 `.wxss`，wxs/sjs → 编译到 ES5/CommonJS 写入 mini-program 期望位置，json → 通过 `comment-json` 支持 JSONC + 宏展开。
- **Trade-off**：放弃 webpack 生态的成熟 loader 链（通过自定义 plugin 链补齐）；Rolldown 与 Babel 的兼容性边界需要自己盯（CHANGELOG 中多次出现 rolldown 升级带来的 bundle 修复）。
- **可迁移性**：高。

#### 决策 2：自研 Wevu 运行时（Vue 3 风格，但跑在小程序数据层而非 VDOM）
- **问题**：Taro/MPX/Remax 都靠 VDOM + reconciler 抽象，对小程序平台 patch 反应慢、Hello World 体积大、复杂页面递归 diff 卡顿。
- **方案**：`packages-runtime/wevu` 自写响应式核心（与 Vue 3 同形：`effect`/`reactive`/`ref`/`computed`/`watch`/`scope`/`batch`，282 行 `core.ts`），但渲染目标不是 VDOM，而是「响应式 → 快照 → diff → setData」（`runtime/app/setData/` 目录下 4 个文件合计 1238 行）。保留 Vue 3 reactive 的 `toRaw`/`unref`/`markRaw`/`shallowRef`/`readonly` 全部语义。
- **Trade-off**：自写响应式意味着「Vue 上游优化」要自己 backport；需要单独维护一份 `@vue/language-core` 类型增强（`volar.ts` 包）；provide/inject 在小程序 Page 上下文里语义有差异（见 `provide.test.ts` 的特殊处理）。
- **可迁移性**：中。

#### 决策 3：MCP server 三层 transport（stdio + streamable-http + Runtime REST）
- **问题**：开发者要让 Claude/Codex 在「真实小程序运行时」里操作，而不是只读代码。
- **方案**：`packages/mcp` 同时支持嵌入 IDE（stdio）和独立服务（streamable-http on 127.0.0.1:3088）两种 transport，再叠一层 REST endpoint（`DEFAULT_RUNTIME_REST_ENDPOINT`）给非 MCP 客户端调用。资源/能力分 4 类：① 静态工作区能力（`workspace_catalog` / `list_source_files` / `read_source_file` / `search_source_code`）；② 命令执行能力（`run_pnpm_script` / `run_weapp_vite_cli_tool`）；③ 运行时能力（`RuntimeSessionManager` + `registerRuntimeTools`：截图/截图对比/日志桥接/预览/上传）；④ Prompts/Resources。
- **Trade-off**：三种 transport 的协议不同，要写三套协议适配层（`runtime.ts` 214 行 + `server/runtime/rest/*`）；MCP server 需要绑定到具体 workspace，启动前 `process.chdir` 要正确处理；与 IDE DevTools 通信受沙箱限制。
- **可迁移性**：高。

#### 决策 4：AGENTS.md 作为仓库级一等公民
- **问题**：AI agent 协作（Claude Code / Codex）缺乏统一的工程纪律——容易踩到 monorepo 跨包改动、dist stale、跨平台 CI 陷阱、E2E 串行约束、隐私路径泄漏等坑。
- **方案**：仓库根 `AGENTS.md`（295 行）覆盖 7 大主题——monorepo 路由、fast-path 命令、dist sync guard（强制先 `pnpm --filter <pkg> build` 再下游验证）、cross-platform guard（Windows 路径/换行/spawn/execa）、编码规范（TypeScript ESM 2-space 缩进、AGENTS 文档中文化、文件超 300 行需评估拆分）、test/e2e 规则（E2E 全局串行、`pnpm e2e:ide` 必须 caffeinate 保活）、commit/changeset 规则、`.vscode/settings.json` 排除规则。
- **Trade-off**：AGENTS.md 写得过细维护成本高；过度自动化（如 dist sync 强制 rebuild）会让本地迭代变慢。
- **可迁移性**：极高。

#### 决策 5：monorepo 单仓多包 + Changesets fixed group 发布
- **问题**：发布节奏需要稳定，但 30+ 包中 `weapp-vite`、`@weapp-vite/ast`、`@weapp-vite/dashboard`、`wevu`、`@wevu/compiler` 必须一起升级版本；部分包如 `@weapp-vite/mcp` 可以独立迭代。
- **方案**：`.changeset/config.json` 里把核心 5 个包放进 fixed 数组强绑定版本；用 catalog（pnpm 9+ 特性）+ turbo cache 控制 CI 时间；`pnpm publish-packages` 一次性脚本串行执行 catalog 同步、changeset 版本、自动校验、`turbo run test`、`changeset publish`。
- **Trade-off**：fixed group 的隐式耦合需要严格治理（脚本里有 `check:publishable-workspace-changeset` 等 6 个独立 check 脚本把关）；CI 校验矩阵 3 平台 × 多 Node 版本（22/24），耗时成本客观存在（CI Ubuntu 25min、macOS 25min、Windows 40min）。
- **可迁移性**：高。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | weapp-vite | Taro | uni-app | 微信官方脚手架 | MPX |
|------|-----------|------|---------|--------------|-----|
| 定位 | 单平台深度现代化构建器 | 跨端跨框架 | 跨端大一统 IDE 体系 | 兜底起点 | 增强原生语法 |
| Stars | 348 | 37.6k | 41.6k | 官方 | ~1.7k |
| 渲染策略 | 不替换运行时 + 可选 Vue SFC | React/Vue 渲染到 DSL | uts/Vue 渲染到 DSL | 原生 | 增强原生模板 |
| 构建器 | Vite 8 + Rolldown 1.1 | webpack 主 | webpack / Vue CLI | gulp 模板 | 自研 |
| 运行时 | 自研 Wevu（响应式 + 快照 diff setData） | VDOM + reconciler | VDOM + uts runtime | 无 | 自研 |
| 跨端能力 | 微信主，插件扩展多端 | 微信/支付宝/百度/字节/QQ/京东/钉钉/淘宝 | App/小程序/H5/快应用 | 仅微信 | 微信 |
| HMR | 有（且 MCP/截图对比） | 有 | 有 | 无 | 有限 |
| AI 协作 | MCP + AGENTS.md + 7 skills + Runtime REST | 弱 | 弱 | 无 | 弱 |
| 体积 | 小（无 VDOM） | 中（VDOM 运行时） | 中 | 最小 | 小 |
| TypeScript | 一等公民 | 需配置 | 需 IDE 插件 | 弱 | 需配置 |
| 平台 patch 速度 | 极快（保留原生） | 慢（等框架） | 慢（等框架） | 极快（官方） | 快（接近原生） |
| 单作者风险 | 极高（93.5%/93.9% 占比） | 中（京东背书） | 低（DCloud 团队） | 无 | 中 |

### 差异化护城河

1. **「不替换运行时」的路线选择**——在平台 patch 速度、体积、调试体验上有结构性优势。
2. **Wevu 自研响应式 + 快照 diff setData**——性能优于 VDOM 方案。
3. **MCP + AGENTS.md + Skills 工程化**——AI 协作维度领先同赛道所有竞品。
4. **Changesets + Turbo + pnpm catalog + 6 道 publish check**——发布工程化领先。
5. **Issue 1:1 e2e fixture 制度**——质量保证可观察可复现。
6. **从自家需求反哺社区**（`rolldown-require` 独立 npm 包、`@weapp-core/constants` 跨包共享）——产品思路领先。

### 竞争风险

- **最可能被微信官方工具链升级替代**——如果官方原生支持 Vite/HMR，本项目核心价值会被压缩。但短期内微信官方的工程化节奏明显落后，威胁等级低。
- **跨端 story 不如 Taro/uni-app 完整**——单平台深耕的代价是「一码多端」场景被竞品切走。
- **单人主导（93.5%/93.9%）的关键人员风险**——bus factor = 1 是最大隐性风险。
- **社区规模小**——star 数与体量大的竞品差距明显。
- **Rolldown/Vite 上游版本升级带来的持续适配成本**——CHANGELOG 多次出现 rolldown 适配记录。

### 生态定位

「现代 web 工具链向小程序的完整移植 + AI 协作一等公民 + 不替换运行时」。在「单平台深度」与「跨平台广度」之间选前者，在「替换运行时」与「升级工程化」之间选后者，在「传统 DX」与「AI-native DX」之间领先一个身位。在 Taro（跨端跨框架）和官方脚手架（兜底起点）之间找到的精准细分位。

## 套利机会分析

- **信息差**：显著低估。证据链：① 5,327 commits + 1,370 tag + 100 release 的开发强度，定位为「职业项目」；② 自带 VSCode 扩展、MCP server、Volar 插件、5 套示例 app、完整 monorepo + Turbo + Changesets 工程化，几乎是「一个人的小程序工具链公司」；③ 与同作者 `weapp-tailwindcss` 1.8k stars 对照，此项目解决的是更上游的「构建器」问题，按理应有更高量级。中文前端圈对小众工程化工具的评测滞后，加上项目营销与文档外宣缺位（README 缺架构图和 Demo GIF、官网基本是纯文本），都是 star 数被低估的原因。
- **技术借鉴**：本项目最有借鉴价值的不是 Vite 集成本身（这个社区已有不少尝试），而是 ① AGENTS.md + 6 段强制 guard 的 AI 协作工程纪律；② MCP 三层 transport + 资源/工具/会话/提示词分层；③ GitHub issue 1:1 e2e fixture + worktree 隔离修复流程；④ 响应式 → 快照 diff → patch + 大小阈值回退的协议骨架。
- **生态位**：「原生小程序 + 现代 web 工程化」的细分位，与 Taro/uni-app 是互补而非正面竞争。
- **趋势判断**：AI 协作维度领先一个身位——MCP 生态正在爆发，AGENTS.md 的工程化模式会越来越重要，本项目的「AI 协作是 1 等公民」定位踩在趋势上。比 Taro/uni-app 有后发优势，因为它们是「跨端跨框架」时代的产物，而 weapp-vite 是「AI-native DX」时代的产物。

## 风险与不足

1. **单人主导（93.5%/93.9%）**——bus factor = 1 是最大隐性风险。如果作者精力分散到其他项目（`weapp-tailwindcss` 等），本项目的迭代速度会立刻下降。
2. **跨端 story 不如 Taro/uni-app 完整**——虽然通过「平台无关 plugin + 平台特定 rewrite」做扩展，但微信以外的平台成熟度未知。
3. **上游版本升级带来的持续适配成本**——Rolldown/Vite 升级在 CHANGELOG 中多次出现，2026-03-16 还出现过 `rolldown-plugin-dts-lexical-environment-bug`。
4. **关键 Issue 仍 open**——issue 446（template ref 类型问题）仍 open，issue 510（Vue 3 provide/inject 深层作用域语义对齐）刚合入——功能边界还在持续扩张，未进入「稳定维护」。
5. **修复占比 40% + 重构仅 2.5%**——项目处于「功能密集上线 + 边修边稳」阶段，未到收敛期。
6. **可视化资产空缺**——README 缺架构图与 Demo GIF，官网无产品截图与教学视频，对传播不利。
7. **Vue 3 语义对齐开放**——provide/inject 在小程序 Page 上下文里语义有差异（`provide.test.ts` 的特殊处理），快照 diff setData 在响应式数据 vs 平台 setData 边界处的语义陷阱（issue 312）——自研运行时的核心难点未完全解决。
8. **小程序平台限制 vs 现代模块系统的根本张力**——issue 120（Worker 隔离、ESM/CJS 互操作）是所有「web 工具链 → 小程序」项目的天花板。

## 行动建议

- **如果你要用它**：如果你正在维护微信原生小程序、希望渐进升级到 TypeScript / Vite / Vue SFC / HMR，weapp-vite 是当前最合适的方案。可以从 `wv init` 渐进接入，老页面不动，新页面直接上 Vue SFC + Wevu。优先评估 monorepo 工程化能力（Turbo / Changesets）是否符合团队节奏——本项目的工程化纪律是「准职业级」的，团队需要能跟得上。
- **如果你要学它**：重点关注 ① `packages-runtime/wevu/src/reactivity`（自研响应式核心 282+286+149+71+261 行，复用 Vue 3 API 形态但不直接依赖其内部）；② `packages/weapp-vite/src/runtime/advancedChunks.ts` + `chunkStrategy/` 目录（分包共享 chunk 策略一等配置，68 行核心 + 复杂 fixture + 设计文档）；③ `packages/mcp`（MCP 三层 transport）；④ 仓库根 `AGENTS.md`（295 行 + 6 段强制 guard）；⑤ `packages/rolldown-require`（从自家需求反哺社区的产品思路）。
- **如果你要 fork 它**：可以改进的方向有 ① 补齐可视化资产（架构图、Demo GIF、教学视频）；② 拆分多端 story（mpcore 已铺路但成熟度未知）；③ 引入更多外部贡献者（当前外部贡献者累计 < 1%）；④ 与 DCloud 团队合作的可能性（uni-app 用户的 Vite 升级需求）；⑤ 把 rolldown-require 的预捆绑思路推广到其他 bundler（Webpack/Vite 的非 rolldown 分支）。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [weapp-vite/weapp-vite](https://deepwiki.com/weapp-vite/weapp-vite)（已收录，DeepWiki 给出三大支柱总结：构建编排 `weapp-vite` v6.16.27、响应式运行时 `wevu`、平台抽象 `@wevu/api`） |
| Zread.ai | 未收录（站点反爬/认证拦截，无法确认） |
| 关联论文 | 无（工程化项目，无学术论文对应） |
| 在线 Demo | 无公开 Playground（项目提供 5 套 `apps/` 本地示例 app，但无在线 sandbox；用户需本地 `pnpm create weapp-vite` + 微信开发者工具走完链路） |
| 官网 | https://vite.icebreaker.top/ |
| 同作者项目 | https://github.com/sonofmagic/weapp-tailwindcss（1.8k stars，「底层构建器 + 垂直适配器」组合） |
