# axios 核心只有 7000 行，却被 17 万个项目依赖：一个基础库的设计与 2026 投毒事件

> GitHub: https://github.com/axios/axios

## 一句话总结

axios 是基于 Promise 的同构 HTTP 客户端——一套 API 同时跑浏览器和 Node.js，用拦截器、自动 JSON、超时、取消、进度等能力补齐原生 fetch/XMLHttpRequest 的 DX 缺口。它 11.8 年长青，核心库仅约 7000 行、运行时只有 4 个依赖，却被 17.7 万个 npm 包直接依赖、周下载 5000 万到 1 亿+，是基础设施级的存在。2026-03 它经历了一次震动全网的供应链投毒事件——这让它同时成为「架构教材」和「软件供应链安全活案例」。

## 值得关注的理由

1. **极致反差：7000 行核心撬动全网**：核心 lib/ 仅约 7.2k 行、运行时仅 4 个窄职责依赖，却是 npm 第 11 大被依赖包（17.7 万包直接依赖）。「靠稳定与克制而非体量取胜」的精炼基础库范本。
2. **被全网模仿的两个设计**：同构 adapter 抽象（构建期静态替换 + 运行期能力探测双层，一套核心跑浏览器/Node/RN/Deno/Bun）+ 拦截器 Promise pipeline（请求/响应钩子串成可插拔链，业务核心夹中段）——这两个是 SDK 设计的教科书模式。
3. **软件供应链安全的标志性活案例**：2026-03 维护者 npm 账号被盗、被推送植入 RAT 的投毒版本（影响 1 亿+ 周下载，3 小时响应）+ CVE-2026-40175（mergeConfig 原型污染→SSRF）。axios 的 94KB `THREATMODEL.md`、OIDC 可信发布、复现性构建等治理实践，是「基础库如何向下游证明可信」的参考实现。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/axios/axios |
| Star / Fork | 109,095 / 11,721 |
| 代码规模 | **核心库 lib/ 仅约 7.2k 行 / 65 文件**（运行时仅 4 个依赖）+ 测试约 20.4k 行（核心 3 倍）+ ESM/CJS 双份手写 TS 类型 1.5k；cloc 中 JSON 41.8% 是 package-lock + 赞助/fixtures，非业务代码 |
| 项目年龄 | 141.8 个月（约 **11.8 年**，2014-08 创建） |
| 开发阶段 | 密集开发（11 年长青仍高频，2026-04 因投毒事件爆发 119 commit 紧急加固） |
| 贡献模式 | 高度社区化（659 贡献者，top_share 仅 14.2%，无单点核心；Matt Zabriskie 创始 → 社区接棒） |
| 热度定位 | **基础设施级**（npm 周下载 5000 万-1 亿+，17.7 万包直接依赖，第 11 大被依赖包） |
| 质量评级 | 代码[优] 文档[优·94KB THREATMODEL] 测试[优] CI[优·8 workflow] 供应链安全[优] |
| License | MIT（默认分支 v1.x，latest v1.17.0，141 tags） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

最初作者 **Matt Zabriskie（mzabriskie）**——2014 年 Promise 刚成主流、fetch 尚未落地时切入「Promise + 同构 + 配置驱动」的空档（API 明显借鉴 Angular `$http` 的 config 对象风格）。他因没时间维护，没有让项目烂尾，而是发表著名的「Axios: Help Wanted」博文、把项目迁入独立 organization、公开招募接棒人。此后 **Jay/Jason Saayman（jasonsaayman）** 成首席维护者，Dmitriy Mozgovoy（DigitalBrainJS）为另一核心。这是开源界「创始人优雅退出、社区接棒延续」的典型成功案例。

### 问题判断

原生方案有明确的 DX 缺口：`XMLHttpRequest` 回调式、API 冗长、无 Node 等价物；`fetch` 虽是标准但**无拦截器、无上传进度、无统一超时/取消、404 不 reject、无自动 JSON**。axios 把这些一次补齐，并用 adapter 抽象实现「一份业务代码两端跑」。

### 解法哲学

- **同构优先**：核心逻辑（拦截器/配置合并/transform）与传输层（adapter）彻底解耦，传输层按环境可替换。
- **DX 优先**：合理默认（自动 JSON、`validateStatus` 把 2xx 之外判错），让 80% 场景零配置可用。
- **克制依赖**：运行时仅 4 个依赖（follow-redirects/form-data/https-proxy-agent/proxy-from-env），全部窄职责、成熟。
- **明确不做什么**：长期搁置 HTTP/2（结构性软肋 #1175）、不做自动重试/分页（留给 got）、不沙箱化用户钩子（THREATMODEL 明列为非目标）。

### 战略意图

axios 清醒认识到自己是「一处沦陷、全网受害」的基础设施。`THREATMODEL.md` 开宗明义把系统拆成两半建模：**运行时**（保护 `import axios` 的应用）和 **项目/SDLC**（保护「发到 npm 上的 axios 是什么」），并明说后者是更高风险的一半。这是一个被海量依赖的库对自身「责任面」的战略自觉——价值重心已从「功能领先」转向「可信度与兼容性领先」。

## 核心价值提炼

### 创新之处

1. **同构 adapter 抽象（构建期静态替换 + 运行期能力探测双层）**（新颖 4 / 实用 5 / 可迁移 5）：构建期靠 package.json 的 `browser`/`react-native` 字段把 Node 专属代码（http.js/platform/node）替换并摇树掉，浏览器包不含 http/zlib；运行期靠 `getAdapter` 按默认顺序 `['xhr','http','fetch']` 逐个 `adapter.get(config)` 能力探测，命中第一个可用的即停。用户可传字符串名或自定义函数完全替换 adapter。
2. **拦截器 Promise pipeline + 全同步链路快路径**（新颖 4 / 实用 5 / 可迁移 5）：`InterceptorManager` 是个 handlers 数组（`eject` 置 null 不 splice，避免下标错位），请求拦截器 unshift 到链首、响应拦截器 push 到链尾、中间夹 `dispatchRequest`，组成 Promise chain 两两 `.then()` 消费。亮点：若所有请求拦截器标 `synchronous:true` 走同步快路径（跳过为每个拦截器建 microtask），`runWhen(config)` 支持条件跳过。
3. **per-key 合并策略表 + 空原型防污染**（新颖 3 / 实用 5 / 可迁移 4）：`mergeConfig` 用 `mergeMap` 把每个 key 映射到专属合并函数（url/data 只取本次、headers 深合并、timeout 覆盖）；安全加固直接可见——合并结果用 `Object.create(null)`（空原型杜绝从被污染 Object.prototype 继承），遍历键时显式拦截 `__proto__/constructor/prototype`，连 hasOwnProperty 都用 null-proto descriptor 重挂。**这正是 CVE-2026-40175（原型污染→CRLF 头注入→SSRF）的修复现场**。
4. **CancelToken thenable 自研 → AbortController 标准桥接**（新颖 4 / 实用 4 / 可迁移 4）：早期 JS 无标准取消原语，自研 `CancelToken`（劫持 `this.promise.then` 让每次订阅可单独 unsubscribe 防泄漏）；标准化后新增 `toAbortSignal()` 桥接，`composeSignals` 把 signal + cancelToken + timeout 三信号合一。「自研原语 → 标准化后做适配桥」的长寿命库演进范式。
5. **威胁建模即文档资产（THREATMODEL.md 94KB）**（新颖 5 / 实用 5 / 可迁移 5）：运行时 + 供应链双系统建模，逐项标 likelihood×impact + 代码引用 + gap。这是 axios 最值得抄的「软」创新——被广泛依赖的库可用它向下游尽调直接证明可信。
6. **HTTP adapter 的纵深安全**（新颖 3 / 实用 4 / 可迁移 3）：Node 端 http.js 处理代理/重定向/解压/绝对 URL 每项都是攻击面——`isSameOriginRedirect` 用 URL().origin 比对、重定向剥离过期 Proxy-Authorization、`maxContentLength` 防解压炸弹、`sanitizeHeaderValue` 剥离 C0/DEL 控制字符防 CRLF 注入、`allowAbsoluteUrls` 闸门缓解 SSRF。

### 可复用的模式与技巧

1. **「核心 + adapter 注册表 + 能力探测」同构骨架**：`knownAdapters` 映射 + `getAdapter` 按序探测 `.get(config)`，配合 bundler `browser` 字段做死代码消除。
2. **Promise pipeline 中间件**：用户钩子数组 reduce 成 `.then()` 链，业务核心夹中段；纯同步钩子降级为顺序执行省 microtask。
3. **per-key 策略表合并**：`mergeMap[key] = strategyFn`，避免「一把梭深合并」的语义错乱与安全坑。
4. **空原型 + key 黑名单防原型污染**：`Object.create(null)`、`__proto__:null` descriptor、跳过 `__proto__/constructor/prototype`——可直接拷进任何 merge/parse 路径。
5. **自研原语 → 标准桥接**：`CancelToken.toAbortSignal()` + `composeSignals` 把历史 API 平滑收敛到 Web 标准。
6. **威胁模型驱动的供应链工程**：OIDC trusted publisher（无长效 NPM_TOKEN）+ `.npmrc ignore-scripts` + 硬件密钥 + SHA 钉死 Actions + 两遍构建复现性校验 + provenance attestation——「基础库供应链治理」参考实现。

### 关键设计决策

- **transform 体系（函数数组管线）**：`transformRequest`/`transformResponse` 都是函数数组，`transformData` 用 reduce 式链式跑；默认按数据类型分支（HTMLForm→FormData、对象→JSON.stringify 并自动设 Content-Type），响应侧受 `transitional.silentJSONParsing` 控制容错 parse。
- **ESM/CJS 双份手写 TS 类型**：index.d.ts + index.d.cts 各约 21KB 双份同步维护，给 ESM/CJS 双消费形态一等公民待遇。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | axios | 原生 fetch | undici | got | ky |
|------|-------|--------|--------|--------|--------|
| 形态 | 同构库 | 平台标准 | Node 官方底层 | Node 重型库 | 现代 fetch 封装 |
| 周下载/规模 | 5000万-1亿+ | 内置 | ~26M | 重型 | ~2M |
| 同构 | ✅ | 部分 | ❌ 仅 Node | ❌ 仅 Node | ✅ |
| 拦截器 | ✅ | ❌ | ❌ | Hooks | ✅ |
| 进度/取消 | ✅ | 部分 | 底层 | ✅ | 部分 |
| 包体 | 偏重 | 零 | 中 | 大 | ~9KB |
| 供应链风险 | 有（已治理） | 零 | 低 | 有 | 有 |

### 差异化护城河

①拦截器统一掌控请求/响应生命周期（最被模仿且最难替代）；②真·同构（一套 API 跑浏览器/Node/RN/Deno/Bun）；③11.8 年生态惯性 + 17.7 万包直接依赖的存量；④近年补齐的供应链安全治理与威胁模型，构成「可信度」护城河。

### 竞争风险

1. **被轻量化潮流两端夹击**：浏览器侧 fetch/ky 蚕食（零依赖/小体积叙事），Node 侧 undici 以性能和官方身份下沉。
2. **HTTP/2 长期未交付**是结构性短板（#1175，undici/got 差异化点）。
3. **供应链是最大风险面**：2026-03 投毒事件验证「发布权集中到极少 npm 账号」的软肋；单维护者使双人审查难强制。
4. **包体偏重**：在「零依赖」叙事下处于劣势。

### 生态定位

从「最好用的 HTTP 库」逐渐转为「最稳妥、被依赖最广、治理最透明的基础设施级 HTTP 库」——价值重心从功能领先转向可信度与兼容性领先。

## 套利机会分析

- **信息差**：axios 早是基础设施，不存在「会不会火」。内容价值在换角度——「一个被全网依赖的基础库如何设计、如何治理、出事多大」。2026 供应链投毒 + CVE 让它同时具备架构教材 + 安全活案例双重选题价值，时效性强。
- **技术借鉴**：同构 adapter 双层抽象、拦截器 Promise pipeline + 同步快路径、per-key 合并策略表 + 空原型防污染、自研原语→标准桥接——这些是 SDK/库设计的通用范式，直接可抄。
- **安全治理借鉴**（最稀缺）：THREATMODEL.md 双系统建模 + OIDC 可信发布 + ignore-scripts + 硬件密钥 + 复现性构建——这套是任何被广泛依赖的开源库都该学的供应链治理。
- **生态位**：HTTP 客户端的稳妥默认 + 供应链安全治理标杆；增长边界在 HTTP/2 与轻量化竞争。

## 风险与不足

1. **供应链发布权集中**：极少 npm 账号持发布权，2026 投毒事件验证此软肋；单维护者难强制双人审查。
2. **HTTP/2 结构性缺失**：已 import http2 但长期未作正式特性交付。
3. **包体偏重**：相对 fetch/ky 在「零依赖/小体积」叙事下劣势。
4. **大文件复杂度**：lib/adapters/http.js（1325 行）、fetch.js（552 行）单文件偏重。
5. **复现性构建尚非硬闸**：两遍构建复现性校验当前 `continue-on-error`，待消除非确定性后转硬闸。

## 行动建议

- **如果你要用它**：需要拦截器、上传/下载进度、统一超时/取消、同构（浏览器+Node 一致）、成熟 TS 类型——axios 仍是稳妥选择，但务必锁版本 + `npm audit signatures` 验 provenance + 用 lockfile（吸取投毒教训）。只要零依赖/小体积、能接受手写错误处理选原生 fetch/ky；Node 高吞吐选 undici；要自动重试/分页选 got。
- **如果你要学它**：重点读 `lib/adapters/adapters.js`（注册表+能力探测）+ `lib/adapters/http.js`/`xhr.js`/`fetch.js`（同构三适配器）、`lib/core/Axios.js` + `InterceptorManager.js`（拦截器 pipeline）、`lib/core/mergeConfig.js`（防原型污染合并，CVE 修复现场）、`lib/cancel/CancelToken.js`（自研→标准桥接）、`THREATMODEL.md`（威胁建模文档资产）。
- **如果你要 fork/借鉴它**：最值得搬走的不是代码而是治理——把 THREATMODEL.md 双系统建模 + OIDC 可信发布 + ignore-scripts + 复现性构建这套供应链工程搬到你自己被依赖的库。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/axios/axios](https://deepwiki.com/axios/axios)（大概率已收录，建议人工确认） |
| Zread.ai | 未确认（网络受限） |
| npm | [npmjs.com/package/axios（v1.17.0，周下载 5000 万-1 亿+）](https://www.npmjs.com/package/axios) |
| 官方文档 | https://axios-http.com |
| 供应链事件复盘 | [Inside the Axios supply chain compromise — Elastic Security Labs](https://www.elastic.co/security-labs/axios-one-rat-to-rule-them-all) |
| 关联论文 / 在线 Demo | 无（工程库；官网即文档站，含最小用例） |
