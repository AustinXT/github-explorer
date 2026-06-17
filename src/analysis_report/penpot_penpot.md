# GitHub 推荐：50K stars · 10 年 Clojure 全栈：Penpot 怎么用 Rust/WASM 渐进迁移挑战 Figma

> GitHub: https://github.com/penpot/penpot

## 一句话总结
西班牙 Kaleidos 公司用 Clojure 全栈 + Rust/WASM 渲染器打造的开源 UI/UX 设计协作平台,以「开放格式 + 自托管 + flat-rate 定价」三件套,锁定了 Figma 闭源 SaaS 结构性短板无法覆盖的 15-25% 企业合规市场。

## 值得关注的理由

1. **LISP 工业化活化石**——ClojureScript + Clojure/JVM 同栈在生产环境跑 10 年、`common/` 18 万行代码前后端 1:1 复用,是「数据驱动 SPA + 长生命周期」场景下小众语言栈的实战范本。
2. **Rust/WASM 渐进迁移教科书**——`render-wasm/src/render.rs` 2024-10 才引入已 314 次修改,靠带版本号的 feature flag(`render-wasm/v1` + `text-editor/v2` 硬依赖约束)在「同一份代码跑新旧两套渲染」之间优雅灰度。
3. **设计行业的「Linux」卡位**——MPL 2.0 + 开放 SVG/CSS/HTML/JSON 格式 + MCP server 把 Plugin API 暴露给 LLM,正在把「AI 驱动设计代理」入口的标准握在手里。

## 项目展示

![Penpot 产品全景](https://github.com/user-attachments/assets/da17b160-f289-436f-b140-972083a08602) — 类型: hero(README 首图,产品全景)

[产品 Demo 视频](https://www.youtube.com/watch?v=TpN0isiY-8k) — 类型: video(官方核心功能 Demo)

![Penpot Design Systems](https://github.com/user-attachments/assets/cce75ad6-f783-473f-8803-da9eb8255fef) — 类型: screenshot(组件/Design Tokens 演示)

![Penpot Hub](https://github.com/user-attachments/assets/0abc02f0-625c-45ab-ad81-4927bec7a055) — 类型: screenshot(模板与资源社区)

![Penpot 产品全景(官网)](https://penpot.app/72b71a7302cd1476867d124e9fe46817.webp) — 类型: hero(官网产品代表图,官网首页)

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/penpot/penpot |
| Star / Fork | 50,052 / 3,233 |
| 代码行数 | ≈31 万行(剔除 JSON 资源文件 38 万行后),Clojure 74% + JavaScript 7.7% + Rust 6.4% + SCSS 4.9% + TS 2.7% |
| 项目年龄 | 132 个月(2015-06 首次 commit,2017 转独立品牌 penpot) |
| 开发阶段 | 密集开发(近 30 天 511 commits、近 365 天 4,986 commits) |
| 贡献模式 | 商业公司主导 + 社区协作(Kaleidos 旗下,349 名贡献者) |
| 热度定位 | 大众热门(50K stars,设计工具赛道全球开源第一) |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] CI/CD[完善] |
| License | MPL 2.0(弱 copyleft,允许商业衍生但改过的源码须回馈) |
| 商业化 | 开源免费版 + Enterprise $950/月 flat-rate(Kaleidos 营收核心) |

## 作者视角:为什么存在这个项目

### 创始人/作者背景

Penpot 是西班牙马德里公司 **Kaleidos (Subsidiary SL)** 的核心产品。Kaleidos 2010 年成立,本身是一家 **Clojure 咨询与产品公司**——技术栈从一而终。CTO **Andrey Antukh(GitHub: niwinz)** 自 2015 年 6 月起累计 8,024 个 commit,占总量 35.5%,是 Penpot 的事实架构师;Top10 贡献者合计占 41.7%,典型「强 leader + 大社区协作」形态。Andrey 是 Clojure 圈知名 contributor,其决策决定了项目 10 年技术方向。

### 问题判断

Kaleidos 2010 年起给企业做 Clojure 咨询时,内部需要一个「设计师能和我们一起工作」的工具——市面上没有一个能让他们用 Clojure 全栈写、又能当 Figma 替代品的工具。**问题发现不是市场调研,而是 dogfooding 痛点**。Figma 在 2016 前后爆发,Adobe 在 2017 后才匆忙收购/孵化 XD,这是「浏览器原生 + 实时协作 + 设计系统」窗口被打开但还未闭源垄断的关键三年,Kaleidos 在 2017 把内部 uxbox 改名 penpot、注册组织账号开 GitHub,精准卡位。

### 解法哲学

作者明确选择了:
- **开放协议优于功能堆叠**——用 SVG/CSS/HTML/JSON 作为底层格式,Figma 的「导出 PNG/SVG」在 Penpot 反转为「我们就是 SVG/CSS/HTML,导出只是序列化」。
- **单一语言优于多语言融合**——Clojure 前端 + Clojure 后端共享 18 万行 Clojure,跨语言工程师的隐性成本被砍掉,代价是放弃「招 JS 工程师池」。
- **渐进式现代化优于重写**——`render-wasm/v1`、`text-editor/v2` 这种带版本号的 feature flag 让新旧两代用户在同份代码里共存。

明确不做的:不做移动端 App(只 PWA)、不做离线编辑(会和 CRDT 复杂度耦合)、不做免费版白板投屏、不做品牌资产管理(那是 Figma 收购 Area 之后的方向)。

### 战略意图

Penpot 在 Kaleidos 商业图景中处于**核心营收**位置(不是给别的产品当 SDK),商业模型是「开源 → SaaS + Enterprise flat-rate」,这是 **genuinely open 而非 open-core**——MPL 2.0 允许卖自托管版本但改过的源码须回馈,SaaS 分发不受污染。2025-2027 三大战略动作已落地:MCP server(独立子仓)卡位「AI 设计代理」入口;Rust/WASM 渲染器(2024-10 起 commit 量陡增)追平 Figma 流畅度;130+ release tag 工程节奏稳定,客户能算 ROI。

## 核心价值提炼

### 创新之处

1. **Clojure 三件套数据流(Potok + Okulary + Integrant + Beicon)** ——用带类型的事件流 + 派生 lens + 副作用三阶段绕开 Redux 在「每秒数十次不可变更新」下的 GC 墙;事件流天然携带 `[redo-changes undo-changes]`,undo/redo 几乎免费。新颖度 4/5 | 实用性 4/5 | 可迁移性 3/5。

2. **Layered feature flag 体系(URL > User profile > Team > Global + 硬依赖约束)** ——`features.cljs` 中 `setup-wasm-features` 用四层优先级 + `conj/disj` 表达「启用 render-wasm/v1 必须同时启用 text-editor/v2」的强约束,URL 参数临时覆盖一切用于内部 dogfooding。新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5。

3. **Pointer-Map + Objects-Map 可序列化 lazy 容器** ——`objects_map.cljc` 把对象按需加载到外部 blob 存储,`enable-objects-map/-pointer-map` 是开关,让 100MB+ 设计稿可以「内存常驻索引,blob 存储全量对象」,partial save / lazy load 几乎免费。新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5。

4. **ADT × Malli 三层封装(schema-spec + defprotocol + deftype/defrecord)** ——`abstraction-levels.md` 明确「基础数据 → ADT → file ops → changes → business events」5 层依赖规则,改内部结构不影响调用方。新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5。

5. **Changes × Undo/Redo × Webhooks × Audit 一份 ops 多份产出** ——把「一次编辑」建模为 `[redo-changes undo-changes]` 序列,同一份数据被消费 5 次:应用、同步、撤销、审计、webhook、导出。`pcb/empty-changes` 用「vector 顺序 + list 倒序 conj」把 GC 压力压到最低。新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5。

6. **WASM ↔ JS 通过 `HEAPU8/HEAPU32` 零拷贝边界** ——用 emscripten typed array 直接 subarray 切片,CLJS 端不复制字节就喂给 Rust。`mem.cljs` L9-15 用 `bit-shift-right` 把 byte offset 转 32-bit index 读取。新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5。

7. **MCP Server 把 Plugin API 暴露给 LLM(独立子仓架构)** ——`mcp/` 是独立 npm workspace,通过 WebSocket 连 Penpot 主程序的 plugin 沙箱,LLM 写一段 JavaScript plugin 代码调用 Plugin API 操作设计稿。稳定契约是 Plugin API 而非裸 RPC,避免穿透问题。新颖度 5/5 | 实用性 4/5 | 可迁移性 4/5。

8. **ShapesPool pool allocator with index-based references** ——`render-wasm/src/state/shapes_pool.rs` 用 `Vec<Shape>` 预分配 1.3x 增长,所有 map key 用 `usize` index 而非 `&Uuid` 引用,直接消掉 unsafe 生命周期管理和 `rebuild_references()`。新颖度 3/5 | 实用性 5/5 | 可迁移性 3/5。

### 可复用的模式与技巧

1. **Clojure 三件套事件流(Potok + Okulary + Beicon)**:UI 状态 = 带类型事件流 + 派生 lens + 副作用三阶段,绕开 Redux 不可变 GC 墙,自带 undo/redo 框架。适用场景:多人协作 SaaS、复杂表单/编辑器、设计工具。
2. **带版本号的 feature flag + 硬依赖约束**:不删旧实现,新旧共存,通过命名空间式 flag 表达「启用 A 必须启用 B」,URL 参数临时 dogfood。适用场景:渐进式迁移、A/B、长期兼容。
3. **Changes-as-data 协作协议**:把「一次编辑」建模为「可重放的 ops 序列」,统一支撑实时同步、撤销、审计、webhook、导出,服务端单写者事务。适用场景:Notion 风格、CRM、low-code、CMS。
4. **ADT × Schema 三层封装**:malli schema 描述形状 + protocol 定义接口 + deftype/defrecord 隐藏实现,内部可换。适用场景:复杂领域(金融、医疗、法律、设计)。
5. **MCP-as-Submodule**:用 WebSocket + Plugin 沙箱隔开 LLM 与核心 API,稳定契约是 Plugin API 而非裸 RPC。适用场景:所有想做「AI 接入」的 SaaS,尤其是设计/创意/低代码。

### 关键设计决策

1. **决策**:用 Potok 三态事件系统(`UpdateEvent/WatchEvent/EffectEvent`) + Okulary lens + Integrant 生命周期管理串起前端状态机
   - **问题**:React + Redux 在设计工具场景撞三堵墙——拖动操作高频 reducer 触发 GC 压力、多 tab 同步需要 pub/sub 抽象、异步副作用需要三阶段管理
   - **方案**:所有用户操作定义为带类型标签的事件;Okulary lens 让组件只订阅 state 子集(绕开 useSelector 全树 diff);Integrant 在后端做声明式 component 生命周期;Beicon 把事件变响应式流用 `rx/throttleTime` 背压
   - **Trade-off**:得 `common/` 横跨前后端的同栈效率与 undo/redo 几乎免费;失冷启动 5-8MB JS、Clojure 新人 + 三套心智模型学习曲线陡、re-frame 风格 `defmethod ptk/resolve` 生产打包后 trace 困难
   - **可迁移性**:中——适合「多人协作 + 大量 CRUD + 复杂数据模型」SaaS,但前提是团队愿意押 Clojure

2. **决策**:在保持 ClojureScript 渲染路径完全工作的前提下,把热路径(选中态、布尔运算、文本 shaping、shapes pool)用 Rust 重写并编译成 WASM,前端用「URL > User profile > Team > Global」四级 feature flag 灰度
   - **问题**:Figma 的「丝滑感」是闭源 + C++ 多年调优结果,Penpot 纯 ClojureScript 渲染在 1000+ 形状设计稿上帧率跌到 30fps 以下,这是企业 P2 评估时必测指标
   - **方案**:Rust 端用 `#[no_mangle] extern "C"` 暴露 100+ FFI 函数;`shapes_pool.rs` 用 `Vec<Shape>` 连续内存预分配 1.3x 增长 + `usize` index 而非 `&Uuid` 引用管理,直接砍掉 unsafe 生命周期;`features.cljs` 的 `setup-wasm-features` 表达「启用 render-wasm/v1 必须同时启用 text-editor/v2」的硬依赖约束
   - **Trade-off**:得单 tab 帧时延压到 16ms 以下、热路径可静态分析与 bench、跨平台一致;失 Skia 源码编译 3-5GB 依赖 + CI 15+ 分钟、Bug 域扩大到 JS + Rust + FFI + WASM 内存管理、`#[allow(static_mut_refs)]` 注释反映「单线程 WASM」假设不可移植
   - **可迁移性**:中——同「Skia→WASM + 渐进式灰度」架构可用于浏览器「重图形 SaaS」(在线 PS、白板、CAD、图表工具),但只对性能极敏感场景划算

3. **决策**:用「操作日志(ops)而不是 OT/CRDT」做实时协作——前端用 `changes-builder.cljc` 描述一次编辑产生 `redo-changes/undo-changes` 序列,后端用 `process-changes` 在单一权威文件上应用,通过 Redis pub/sub 把变更广播给同文件订阅者
   - **问题**:设计协作实时性比文本更难——一个文件 10000 形状、500 人协作,Figma 用 CRDT 衍生树解决;Penpot 选择更克制的路
   - **方案**:`schema:operation` 是 `[:multi {:dispatch :type}]`,`:assign/:set/:set-touched/:set-remote-synced` 四种原子操作异地可重放;`process-changes-and-validate` 在同一 DB 事务里 inc `revn` + 应用 changes + 校验,单写者模型;`msgbus` 是简单 `IMsgBus` 协议,后端 Redis pub/sub + 前端 BroadcastChannel 两层实现;`library-change-types/token-change-types/file-change-types` 三组分类广播是面向领域语义的优化,CRDT 不会做
   - **Trade-off**:得协议极简、数据可重放、服务端有完整审计、离线自然降级;失真协作语义弱于 CRDT(Penpot 不做真正并发编辑,last-writer-wins,这是与 Figma 的核心差距)
   - **可迁移性**:高——「ops-based 同步」架构适用于任何「多人围观 + 偶发冲突 + 需要审计」系统(Notion 风格文档协作、CRM 字段编辑、在线表单构建器)

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Penpot | Figma | Sketch | Adobe XD | Excalidraw |
|------|--------|-------|--------|----------|------------|
| 类型 | 开源 + 自托管 + SaaS | 闭源 SaaS | 闭源桌面 | 闭源(已停更) | 开源白板 |
| 部署 | Web PWA + Docker + Helm + air-gap | 仅云端 | macOS only | 桌面 | Web + 自托管 |
| 实时协作 | 是(ops-based,非 CRDT) | 是(CRDT) | 弱 | 弱 | 弱 |
| 文件格式 | 开放(SVG/CSS/HTML/JSON) | 闭源 .fig | 闭源 .sketch | 闭源 .xd | JSON |
| 自托管/合规 | 完整支持 | 不支持 | 不支持 | 不支持 | 支持 |
| 设计系统 | 原生(Design Tokens + Variants + Components) | Variables + Components | Symbols | States | 无 |
| 商业模式 | 开源免费 + Enterprise $950/月 flat-rate | $90/月/seat(per-seat) | $10/月 | 已停更 | 开源 |
| MCP/AI 接入 | MCP server(独立子仓) | 插件生态 + Figma AI | 无 | 无 | 无 |
| 贡献者 | 349 | 闭源 | 闭源 | 闭源 | ~100+ |

### 差异化护城河

- **信任护城河**(强):MPL 2.0 + 自托管 + 开放格式——企业买 Penpot 不是买功能,是买「不会因为某 SaaS 涨价/关停而失去设计资产」的承诺。这是 Figma 的 SaaS 估值模型结构性做不到的事。
- **生态护城河**(中):350+ 贡献者 + 24 个 GH Actions workflow + DEI 翻译社区 + MCP + Plugin API 双扩展接口——「由社区维护的开源」,不是某公司 marketing 开源。
- **同栈效率**(强):`common/` 18 万行 Clojure 横跨前后端 1:1 复用,改一处两端生效——React/Redux 生态几乎做不到。

### 竞争风险

- **Figma 推出企业自托管 + 开放格式**(概率低,Figma 估值模型建立在 SaaS 订阅上)
- **Figma 收购 Area/Maker 后的「品牌资产管理」侵蚀 Penpot 设计的核心用户**(可能性中,这是设计行业向「品牌一致性」演化方向)
- **WebGPU 让浏览器原生 2D 性能追上 Skia**——如果发生,Rust/WASM 投入回报变小(但代码已在手,影响有限)
- **真·并发编辑差距是结构差距**:Figma 多人同时编辑同一形状不会撞,Penpot 是 last-writer-wins;短期内不会追平 CRDT

### 生态定位

**「开源企业设计平台的 reference implementation」**——在 Figma 闭源和 Sketch/XD 退场格局里,Penpot 是唯一一个「被企业实际部署的开源设计工具」,通过 MCP + Design Tokens + Open format 三件套卡住了「设计行业的 Linux」位置。2025-2027 关键看 Rust/WASM 渲染器能否把性能差距补上,以及 MCP server 能否成为「AI 驱动设计」事实标准。

> 严格意义上的 UI 设计赛道,Penpot 的直接竞品只有 Figma(其 Figma 导入插件仓库也印证)。其他是相邻赛道(白板、流程图、矢量编辑),格局是「红海中的细分蓝海」——主流设计市场 Figma 不可撼动,但「受合规约束 + 大团队 + 不想 vendor lock-in」这个细分需求是稳定存在的真市场。

## 套利机会分析

- **信息差**:低——50K stars 是开源设计工具赛道头部,无人不识。但**「为什么商业可持续 + 大公司真的在用」这个故事**被低估:政府/金融/受监管行业的 EU 政企客户实际部署案例、Enterprise tier $950/月 flat-rate 的 ROI、Kaleidos 10 年 Clojure 工程化能力都是公开但少被中文技术圈盘点。
- **技术借鉴**:
  - **Clojure 三件套数据流**:任何考虑「放弃 Redux + 选 MobX/Zustand」的复杂 SaaS 团队,都应该先看一眼 Potok + Okulary 的事件流抽象能力。
  - **带版本号的 feature flag + 硬依赖约束**:适合任何在做「老接口逐步下线、新接口灰度」的中型项目(API 网关、SDK、UI 组件库)。
  - **MCP-as-Submodule**:所有想做「AI 接入」的 SaaS 的标准范式——LLM 调 Plugin API 而非裸 RPC,稳定契约 + 沙箱 + 版本管理。
  - **Changes-as-data**:任何「多人围观 + 偶发冲突 + 需要审计」系统的同步协议参考。
- **生态位**:Penpot 填补了「设计行业的 Linux」空白——这是 Figma 闭源 + Sketch/XD 退场后,唯一被企业实际部署的开源设计工具,且通过 MCP + Design Tokens + Open format 卡住了「AI 驱动设计」的事实标准入口。
- **趋势判断**:**在增长且符合技术趋势**——近 365 天 4,986 commits 屡创新高(2024-01: 471 → 2026-05: 577),三年体量翻倍;Rust/WASM + MCP server + Design Tokens 三个方向都在主流技术曲线之上;比 Figma 有「后发合规优势」——Figma 要补自托管需要重做整套 SaaS 架构,Penpot 是天然 native。

## 风险与不足

- **冷启动缓慢**:transit + closure-compiler + React + rumext 让首屏 5-8MB JS,在弱网/低端机表现差
- **招人池是 Clojure 圈的 1% sub-30%**:Potok + Okulary + Integrant + Rumext 四个心智模型叠加,新人上手周期长
- **真·并发编辑弱于 Figma**:CRDT vs ops-based 的结构差距,短期内不会追平;企业 P2 评估必测
- **生态规模 10-100× 落后于 Figma Community**:模板/插件/UI Kit 规模差距,Penpot 在补
- **Rust/WASM 构建复杂度爆炸**:Skia 源码编译 3-5GB 依赖 + CI 15+ 分钟 + emscripten 工具链 + shadow-cljs 双产物同步加载,Bug 域扩大到 JS + Rust + FFI + WASM 内存管理
- **Dev Mode / Inspect / Code Gen 仍基础**:Figma 在 2024+ 投入大量资源做开发者交付,Penpot 这块差距明显
- **`uxbox/main/...workspace.cljs` 残留**:改名未清理的技术债(288 changes 还在被改)

## 行动建议

- **如果你要用它**:
  - 企业用户(欧盟政企/金融/医疗/SaaS 大客户):自托管是天然选项,数据主权 + 合规审计一次过——`docker-compose` 或 Helm chart 5 分钟拉起全栈
  - 设计-工程融合团队:Design Tokens + MCP server + 开放格式让设计资产进 git、可 PR 评审、可被 AI 双向读写,这是 Figma 结构性做不到的
  - 个人/小团队:用 SaaS 版(<https://design.penpot.app>),免费 + 不限协作者人数,Figma 免费 tier 只有 3 个 file
  - 避开场景:需要真·多人大规模并发编辑(>20 人同时改同一文件)的创意 agency——CRDT 才是对的选择

- **如果你要学它**:
  - **Clojure 数据流**:精读 `frontend/src/app/main/data/workspace.cljs`(630 changes)+ `libraries.cljs`(340 changes)+ `common/src/app/common/types/objects_map.cljc`
  - **Rust/WASM 渐进迁移**:精读 `render-wasm/src/render.rs` + `frontend/src/app/render_wasm/api.cljs` + `features.cljs` 的 `setup-wasm-features`
  - **后端实时协作**:精读 `common/src/app/common/files/changes.cljc` + `backend/src/app/msgbus.clj` + `backend/src/app/rpc/commands/files_update.clj`
  - **架构文档**:DeepWiki <https://deepwiki.com/penpot/penpot> + 仓内 `docs/technical-guide/developer/` 12 个子系统文档 + `abstraction-levels.md` 五层依赖规则
  - **AI 接入范式**:`mcp/` 独立子仓架构 + Plugin 沙箱

- **如果你要 fork 它**:
  - **补 CRDT**:把 last-writer-wins 升级为 CRDT 真并发编辑,工程量极大但能拿到 Figma 一线用户
  - **优化冷启动**:首屏 5-8MB JS 是大问题,code-splitting + 路由级 lazy load 是立竿见影的方向
  - **清理 `uxbox/` 残留**:288 changes 的旧 namespace 改名未清理,逐步迁移并删除
  - **补 Dev Mode / Inspect / Code Gen**:对照 Figma 的开发者交付体验补齐,这是企业 P2 评估的重要打分项
  - **WebGPU 替代 Skia 路径**:长期看 Skia 二进制 3-5GB 构建依赖不可持续,WebGPU 标准成熟后切原生 2D

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | <https://deepwiki.com/penpot/penpot>(已收录,2026-03-08 索引,最系统的第三方架构梳理) |
| Zread.ai | 未收录(403 反爬,但 DeepWiki 已覆盖可替代) |
| 关联论文 | 无学术论文,工程日志角色由 `dev-diaries/` 与官方博客承担 |
| 在线 Demo | <https://penpot.app>(注册即用免费版 SaaS),自托管可用 `docker-compose` 跑全栈 |
| 官方博客 | <https://penpot.app/blog>(含 vs Figma enterprise 对比文、`dev-diaries` 系列) |