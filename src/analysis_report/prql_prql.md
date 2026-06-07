# 10K stars 的 SQL 替代品：PRQL 如何用 5 层 IR 编译到 12 种方言

> GitHub: https://github.com/prql/prql

## 一句话总结

PRQL 是一个用 Rust 自研的「管道式关系查询语言」编译器,先把 PRQL 降到自有 RQ（关系代数）中间表示,再通过回溯锚定拆分成原子 SELECT,最终编译到 12 种 SQL 方言——核心是「让查询的阅读顺序 = 执行顺序 = 数据流向」,并把标准库用 PRQL 自己写出来（自举式 stdlib）。

## 值得关注的理由

- **真正的语言层创新,不是方言变体**:绝大多数 SQL 替代品停留在「换个语法糖」,PRQL 设计了一套完整的 `PRQL → PR → PL → RQ → PQ → SQL` 多遍 IR,加新方言只动 `sql/dialect.rs`,不动语义层——这是教科书级的编译器分层。
- **回溯锚定拆分(reverse-walk pipeline → atomic SELECT)** 是其最具技术含量的设计:从输出列反推,贪心装入单条 SELECT,装不下就回退一格拆 CTE——生成的 SQL 接近人手写,远好于 ORM 自动拼出的废 SQL。
- **Wes McKinney（Pandas 之父）+ Jeremiah Lowin（Prefect 创始人）公开站台**,Apache-2.0、RQ 中间表示公开 JSON 化、7+ 语言绑定、9 个编辑器语法——这是一个「中立、开源、被数据圈头部人物背书」的工程化项目,而不是某个公司的 side project。

## 项目展示

README 和官网均无展示性图片/视频——README 主体以代码示例和文字为主,无架构图/demo 视频;官网首页的核心「演示」是实时可编辑的 Playground 代码块(Join invoices + customers → 计算 income → 排名),但这是文本代码块而非图片/GIF,无法作为媒体素材收录。

> 推荐直接访问官方 Playground 看效果:[prql-lang.org/playground](https://prql-lang.org/playground/)

```prql
# PRQL 官方示例:对 invoices 表做 join + 收入计算 + 排名
from invoices
join c = customers on ==customer_id
derive {
  transaction_fee = 0.8,
  income = c.revenue - amount * transaction_fee,
}
filter c.country == 「USA」
sort {-income, +amount}
take 51..100
```

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/prql/prql |
| Star / Fork / Watcher | 10,856 / 256 / 42 |
| Open Issue / PR | 235 / 25 |
| 代码行数 | 4.8 万 (Rust 73.7%, JSON 9.5%, JS 2.9%, YAML 2.1%, CSS 1.8%, HTML 1.4%, 其他 6.6%) |
| 代码/注释比 | 3.4:1（注释占 22.9%） |
| 文件数量 | 418 |
| 依赖数量 | Cargo workspace 多 crate(根 + 5+ 子 crate) |
| 项目年龄 | 53.2 个月（2022-01-18 首个 commit,2026-06-07 最近 push） |
| 开发阶段 | 密集开发（近 30 天 92 commit、近 90 天 208 commit） |
| 贡献模式 | 社区协作 + BDFL 单核（95 人贡献,Top 1 占 48.8%,Top 3 合计 ~78%） |
| 热度定位 | 大众热门（万 star 级别,稳态增长,月均 30+ star） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] CI/CD[完善] |
| License | Apache-2.0（无商业版、无 SaaS） |

## 项目速览（不是模板描述,是观察）

53 个月的开发里,前两年是「快速立项 + 0.5/0.6 初期版本冲刺」,2023 年中 0.7/0.8 又是发布 crunch;2024 年中段是「重构月 + `prql-compiler → prqlc` 大搬迁」,月度 commit 跌到 50 上下;2024 末-2025 中半年低位消化期;2025-09 之后 0.13 系列迭代重新加速。这是「预 1.0 收尾 + 文档打磨 + 错误处理精修」期的典型节奏——feature 已收敛,fix/docs 为主,核心作者仍在主推。

## 作者视角:为什么存在这个项目

### 创始人/作者背景

**Maximilian Roos (max-sixty)** 是 PRQL 的发起人和主要维护者,个人投入 ~50% commits（2,136 / 4,268）。从 30+ 行业真实 SQL 项目的工程沉淀出发,切身体会到 SQL 在写稍微复杂一点的业务管道时被迫「绕弯子」,Jinja 这种字符串模板只是在伤口上贴创可贴——真正的可组合、可静态分析的语言路径缺位。这个痛点不是纯学术研究,也不是突然拍脑袋,而是 dogfooding 出来的真实需求。

PRQL 组织旗下还托管 **pyprql（106 stars）/ dbt-prql（108 stars）/ prqlc-r（58 stars）/ prql-vscode（30 stars）/ prqlc-c / prqlc-py / prqlc-js / prqlc-java / prqlc-elixir / prqlc-php** 等绑定/集成包,形成完整生态——BDFL + 组织化扩展是 PRQL 的治理特征。

### 问题判断

SQL 是数据查询事实标准,但作者认为「声明式 + 子句顺序写死 + 难以抽象」对数据流水线场景是历史包袱。具体来说:
- **dbt**:仍以 SQL + Jinja 模板为内核,Jinja 字符串拼接并不真正解决复用,模板里塞业务规则后期极难维护。
- **Malloy**:同样编译到 SQL,但语义更像 BI DSL,绑定 BI 场景,语法不通用;现已并入 MotherDuck,生态独立性下降。
- **sqlglot**:是 SQL 解析/转译库,适合做方言转换,并不提供新的查询表达层。
- **Polars SQL / DuckDB SQL**:数据库/DataFrame 自己的 SQL 接口,绑死单后端,无法跨方言。
- **Jinja + 共享 CTE 模板**:不可组合、调试噩梦、无法静态分析。

### 解法哲学

官方五原则即解法哲学的纲领化表达:

- **Pipelined**:语法即数据流向,`from a | filter … | join b` 与执行顺序一致;改写顺序即改写语义,无歧义。
- **Simple**:一套管道变换(`from / filter / derive / aggregate / sort / take / join / group / loop`)覆盖 90% 用例;没有 `WHERE` vs `HAVING` 这种分类负担(`filter` 统一两者)。
- **Open**:Apache-2.0,语言规范/语法树可 JSON 化,中间表示 RQ 公开——任何人可以写新后端或新方言。
- **Extensible**:std 库(.prql 文件)+ `s「…」` s-string 逃生口 + 函数定义;做不到的,直接嵌入方言原生 SQL。
- **Analytical**:类型系统导向分析查询的列式算子,而不是 OLTP CRUD;明确不做 DDL/INSERT/血缘追踪(交给 dbt)。

**明确不做的清单本身就是哲学的一部分:dbt 解决 lineage,SQL engine 解决执行,PRQL 只解决「写」**。这一定位让项目保持精瘦,不被「我要不要做一整套数据平台」拖垮。

### 战略意图

- **编译器是内核,不是数据库**。PRQL 不做存储、不做执行、不做 lineage、不做 BI 渲染,只做 SQL 之前的「写作层」——这是 1 个项目想做完整数据平台时最容易被反噬的位置;PRQL 主动放弃,换取「所有人都可以用」的中立性。
- **生态化绑定**:`pyprql` / `dbt-prql` / `prql-vscode` / `prqlc-r` / QStudio 集成 / Jupyter magic / DuckDB 直连,通过 7+ 语言绑定把内核塞进各语言生态,绑定包本身是另一个 org(PRQL org)。
- **没有商业化**:`LICENSE` Apache-2.0,无 SaaS/企业版/hosted,纯开源/纯社区。
- **战略合作信号**:Wes McKinney(Pandas 之父):「I'm also really excited about efforts to create entire new query languages that compile to SQL, like Malloy and PRQL.」 Jeremiah Lowin(Prefect 创始人)公开称赞——说明上层数据工具圈对「SQL 替代品」有真实需求,这是项目最大的战略资产。

## 核心价值提炼

### 创新之处

1. **RQ(Relational Query)中间表示** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5
   - 把 PL 与 SQL 之间加一层「关系代数层」,`from/filter/derive/join/aggregate/...` 全部降级为 `Transform::From/Compute/Select/Filter/Aggregate/Sort/Take/Join/Append/Loop` 枚举 + `Expr` + 严格类型。任何「用户语言 → 多 SQL 方言」的编译器都能用这个 IR 拆层。

2. **回溯锚定拆分(reverse-walk pipeline → atomic SELECT)** — 新颖度 5/5 | 实用性 4/5 | 可迁移性 4/5
   - `pq/anchor.rs::split_off_back` 从输出列开始反推,贪心装入单条 SELECT;装不下就回退一格拆 CTE,直到全部 `inputs_required` 能在该 SELECT 内物化。配套 `CidRedirector` + `positional_mapping` 完成列名重定向与位置对齐。生成的 SQL 通常接近人手写,远好于 ORM。Pandas-style API→SQL、Kotlin Coroutines→Rx、Reactive Streams→SQL 等「线性管道→嵌套表达式」翻译器都可借鉴。

3. **`s「…」` s-string 逃生口 + 注解驱动方言行为** — 新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5
   - `s「LEFT({col:0})」` 让用户(以及 std 库本身)直接写方言 SQL,但通过 `{col:0}` 的位置化插值 + `@{window_frame=true, coalesce=「0」}` 注解控制方言语义。`std.sql.prql` 的全部 12 方言算子都是用这个机制写的。GraphQL→SQL、Prisma SQL 模板、任何「有 80% 公共部分 + 20% 方言差异」的项目都能用。

4. **自举式 std 库(std 库用 PRQL 自己写)** — 新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5
   - `std.prql`(关系算子 + 运算符,251 行)和 `std.sql.prql`(12 方言的 SQL 实现,454 行)全部用 PRQL 自身表达;`internal std.add` 这种「body 由编译器内部实现」标记让 std 既可读又可执行。Elixir stdlib in Elixir、Pharo Smalltalk 风格的自举式语言项目都能借鉴。

5. **`type relation = [{..}]` + frame 推断** — 新颖度 4/5 | 实用性 4/5 | 可迁移性 3/5
   - 把「列集合」作为类型,编译器在语义阶段对每个 transform 计算出入/出 frame,从源到输出追踪每列的来源、生死、别名,为 0.x 之后加入 LSP/列级 lineage/类型补全做准备。DataFrame API 类型系统、查询 IDE、SQL 静态分析都能用。

6. **零成本 FFI(`prqlc-c` + cbindgen)** — 新颖度 3/5 | 实用性 5/5 | 可迁移性 5/5
   - `prqlc-c` crate 通过 cbindgen 自动生成 `prqlc.h`/`prqlc.hpp`,Java/JS/Elixir/PHP/.NET 全部用这套 C ABI 包出各自语言绑定;`.NET` 还修了 64 位 `size_t` 映射、Span 指针解引用等 FFI 经典坑(0.13.12 changelog 详列)。

### 可复用的模式与技巧

1. **三段式 IR(用户语言 / 关系代数 / 方言 AST)** — 任何想一次写多后端的编译器(GraphQL→多数据库、IaC→多云、policy→多执行引擎)。
2. **s-string escape hatch + 注解驱动方言行为** — 任何「大部分公共 + 少量方言差异」的多目标 codegen(打印机、字体子集化、邮件模板多 ISP)。
3. **insta snapshot + mdBook 文档测试一体化** — 任何「文本输出 + 大量样本」的工具(formatter、codegen、template engine)。
4. **`Dialect` enum + `Box<dyn DialectHandler>` + `Any/TypeId` 差异化** — 数据库 driver、打印/字体子集化、protocol 多实现。
5. **`SourceTree` 单文件/项目二合一抽象** — CLI 同时需要 stdin/单文件/项目三种输入模式。
6. **`OnceLock` + 三级 version fallback(env/git/manifest)** — 任何发布期/测试期/构建期需要 version 一致性的 CLI。
7. **`Test-DBs` feature flag + Docker 集成测试** — 需要连真实数据库做集成测试的 ORM、migration、SQL 工具。

### 关键设计决策

1. **决策**:三层 AST 多遍编译 `PRQL → PR → PL → RQ → PQ → sqlparser::ast → SQL`
   - **问题**:SQL 方言多,若 PRQL → SQL 一遍式写,每个方言都得重写一整套语义层,无法复用作用域解析、类型推断、frame 推断。
   - **方案**:把语义层(PL)、关系代数层(RQ)、优化/分区层(PQ)、目标 AST(sqlparser)四层分离开;PL 关心「用户写了什么」,RQ 关心「这是什么样的关系查询」,PQ 关心「管道如何拆分到单条 SELECT」,最后才到方言。
   - **Trade-off**:多一遍 IR = 多一份学习成本 + 多一份维护;换来的是「加一个新方言只动 sql/dialect.rs + 一些 PQ 边角」,而不用动 PL/semantic。
   - **可迁移性**:高。几乎所有「编译到多后端 DSL」类项目(MySQL 方言、Jinja 替代、GraphQL→SQL 等)都能用这套 IR 拆分套路。

2. **决策**:标准库用 PRQL 自己写(`std.prql` 251 行,`std.sql.prql` 454 行),而不是 Rust 硬编码
   - **问题**:把 std 写在 Rust 里,用户想覆盖 `average` 换成自己公司的 `AVG` 表达需要改代码;而且 Rust 里写「`@2021-01-01` 解析」很别扭。
   - **方案**:把所有 transform / 算子 / 运算符 / 字符串函数都用 PRQL 自身写;s-string `s「MIN({column:0})」` 是 SQL 模板,`internal` 是「这个函数体由编译器内部实现」,让 std 既可被用户看、也能复用、还能用 PRQL 自身的类型推断。`@{}` 注解控制 window frame、coalesce 默认值等方言行为。
   - **Trade-off**:std 改一个语义错误要修两层(PRQL 文本 + 内部实现);运行时要先把 std 注入到 root module,占用一些启动开销。
   - **可迁移性**:高。任何带「std 库」的语言编译器都能用这个模式(Elixir stdlib in Elixir、Pharo Smalltalk 风格)。

3. **决策**:管道按「原子 SELECT」回溯拆分(`pq/anchor.rs::extract_atomic`)
   - **问题**:一条 PRQL 管道可能产生多个相互依赖的中间结果(`filter` 后再 `derive` 再 `group` 再 `filter`),如果全部塞进一个 SELECT,会出现「在 WHERE 中引用 SELECT 后的列」的非法 SQL;但粗暴地全拆 CTE 又会生成臃肿的 `WITH` 链。
   - **方案**:反向遍历管道,记录每个 transform 的「输入要求」(`inputs_required`);遇到无法在该位置物化的列(如窗口函数在 WHERE、聚合后未 GROUP BY 的列)就回退一格拆出一个 CTE,直到剩余管道可以装进一个原子 SELECT。`anchor_split` + `CidRedirector` + `positional_mapping` 三件套完成「在哪个 CTE 里计算、列名如何重定向」的全部工作。
   - **Trade-off**:拆得对不对全靠启发式规则 + 边角修正函数(184 个 snapshot 测试撑住正确性);但生成的 SQL 通常接近人手写,远好于 ORM。
   - **可迁移性**:高。任何「管道式 → 嵌套块式」转换都可借鉴这个反向锚定思想(尤其 ORM、查询构建器、ReactiveX→SQL 翻译器)。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | PRQL | dbt | Malloy | sqlglot | Polars SQL |
|------|------|-----|--------|---------|-----------|
| 形态 | 编译到 SQL 的语言 | SQL + Jinja 框架 | 编译到 SQL 的 BI DSL | SQL 解析/转译库 | DataFrame 上的 SQL 接口 |
| Stars | 10.8k | 10k+ | 1.7k+ | 7k+ | 内置于 Polars |
| 跨方言 | ✅ 12 方言 | ❌ 单方言 | ❌ 单方言 | ✅ 多方言 | ❌ 单后端 |
| 管道语法 | ✅ 原生 | ❌ Jinja 模拟 | ✅ BI 风管道 | ❌ | ❌ |
| Lineage | ⚠️ 工具链级别(待 dbt 集成) | ✅ 完整 | ⚠️ 部分 | ❌ | ❌ |
| 商业化 | 无(纯开源) | dbt Cloud | 已并入 MotherDuck | 无 | Polars Cloud |
| 生态入口 | 7+ 语言绑定 + 9 编辑器语法 | dbt 项目/包生态 | Notebook + BI | Python 库 | Polars 生态 |
| 目标用户 | 数据工程师/分析师 | 数据团队 | BI 分析师 | Python 工具作者 | DataFrame 用户 |

### 差异化护城河

- **技术护城河**:RQ 中间表示 + 回溯锚定拆分 + s-string escape hatch 这三件套,让 PRQL 能在「语言表达力 + 多方言输出」同时拉满,同行很难直接复制。
- **生态护城河**:7+ 语言绑定 + 9 个编辑器语法 + VSCode / Jupyter / QStudio / dbt-prql 集成,即使是小众语言,接入门槛也极低。
- **信任护城河**:Wes McKinney / Jeremiah Lowin 站台 + Apache-2.0 + 公开 JSON AST + PRQL org 治理结构,中立性是个人/单一公司项目无法相比的。

### 竞争风险

- **DuckDB 自带 SQL 持续变强**:如果 DuckDB 把管道语法、CTE 模板做进官方 SQL,PRQL 的「表达力优势」会被蚕食;但 PRQL 的多方言 + 类型系统 + 抽象层仍是 DuckDB 不会碰的。
- **dbt 收编上游抽象层**:dbt 可以用 Jinja macros 模拟管道语义;若 dbt 推「Jinja macros + Python models」,PRQL 的「替代 Jinja」空间会缩小。
- **项目节奏放缓风险**:README 自陈「development has slowed」,核心作者 (max-sixty) 单核瓶颈未解,新 resolver 没合入前 1.0 难产。

### 生态定位

**SQL 的写作层 / 关系型查询的 DSL / 函数式 + 关系代数的交叉产品**。不做存储、不做执行、不做 lineage、不做 BI;是「数据工具链最上面那一层」,所有人都能放进来用。整个生态位:PRQL 处于「数据团队从 raw SQL 走向工程化」的入口——dbt 在它下游(项目管理/lineage/CI),DuckDB/Postgres 在它再下游(执行),Malloy 在它的 BI 邻接位(已被 MotherDuck 收编)。

## 套利机会分析

- **信息差**:PRQL 万 star 级别但增速放缓(从月均 100+ 跌到 20-40,2025-09 后才回升),不是被低估的潜力股——是已被广泛认知的「小众但成熟」项目。**真正被低估的是它的「三段式 IR + s-string + 自举式 std」这套技术组合本身**——博客/会议 talk 里讲得不多,中文圈几乎没有深度分析。
- **技术借鉴**:回溯锚定拆分(任何链式 API→SQL 的项目都该学)、s-string escape hatch(任何编译到多方言的项目都该学)、自举式 std(任何想加 std 的语言编译器都该学)、insta snapshot + mdBook 文档测试一体化(任何 codegen/formatter 项目都该学)。
- **生态位**:填补「SQL 写作层」的空白——`dbt-prql` 适配器已经存在,意味着你可以「dbt 项目里直接用 PRQL 写模型,编译到 SQL 跑」,不需要替换整个 dbt 栈。
- **趋势判断**:2024 末-2025 中半年低谷后,2025-09 之后 0.13 系列重新加速(2026-04/05 跳到 73/92 commit),配合 Playground/文档大量改动——是「再启动期」而非「停滞期」。比 Malloy 强在「社区独立 + 通用语言」,比 sqlglot 强在「是语言不是工具库」,比 dbt 强在「真正的语言抽象 vs 字符串模板」。

## 风险与不足

- **BDFL 单核风险**:Top 1 贡献者占 48.8%,Top 3 合计 ~78%——核心作者 (max-sixty) 是单点故障,README 自陈「development has slowed」。
- **预 1.0 收尾期 + 关键功能缺口**:Issue #407(`WITH RECURSIVE` 递归/迭代查询没有正交表达,1.0 前关键阻塞)、#2857(深递归查询下栈溢出,新 resolver 计划未合入)、#725(标准化集成 vs 深度集成的方向争论)都直接影响 1.0 进度。
- **跨方言转义鲁棒性**:Issue #2155(列名 `timestamp` 转义失败)揭示了「多方言编译」叙事的现实摩擦——每个方言的引号/标识符规则都不同,12 个方言 = 12 套边角。
- **生态分散度**:7+ 语言绑定 + 9 编辑器语法 + 多个独立 repo,任何一个维护者疲劳都会拖垮整条线。
- **官方定位保守**:PRQL 官网自陈「ready to use by the intrepid」——对生产环境不友好,文档教程里有大量「请谨慎使用」「这个功能还在演进」的免责说明。

## 行动建议

- **如果你要用它**:最适合的场景是「DuckDB + Jupyter/Pandas」的探索式分析——`pyprql` 走 DuckDB 后端体验最佳,IDE 支持现代化(Playground + VSCode 扩展 + LSP)。**不建议**直接上生产:1.0 未发,关键功能(递归 CTE)缺失,项目自陈「development has slowed」。如果已经在用 dbt,优先用 `dbt-prql` 适配器,不要整体替换。
- **如果你要学它**:
  - **架构层面**:重点读 `prqlc/prqlc/ARCHITECTURE.md`(顶层 ASCII 图 + 每个 stage 子步骤)和 `prqlc/prqlc/src/lib.rs` 顶层入口,理解五层 IR 的拆分逻辑。
  - **创新层面**:重点读 `prqlc/prqlc/src/sql/pq/anchor.rs`(回溯锚定拆分)和 `prqlc/prqlc/src/sql/std.sql.prql`(12 方言 std 如何用 s-string + 注解写)。
  - **工程层面**:重点读 `prqlc/prqlc-parser/`(chumsky 0.12 解析器独立 crate)和 `.github/workflows/`(25+ workflow,Claude 驱动的 tend bot 已接入 PR review / issue triage / CI fix)。
- **如果你要 fork 它**:最值得改进的方向是
  1. **新 resolver 计划**(Issue #2857 提到的「在深递归查询下解决栈溢出」,目前还没合入,谁能搞定谁就是下一阶段的关键贡献者);
  2. **类型系统支持 LSP 补全**(路线图明列,还没开始);
  3. **SQL→PRQL 自动转译**(路线图明列,可以用 sqlglot 作为逆向前端);
  4. **代数类型系统**(路线图明列);
  5. **Substrait 编译**(路线图明列,RQ 中间表示的天然下游)。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/prql/prql （页面已建立,索引存在,待完整渲染） |
| Zread.ai | 未收录（HTTP 403） |
| 关联论文 | 无（PRQL 是开源语言项目,未发表学术论文） |
| 纲领性博客 | [A functional approach to relational queries](https://prql-lang.org/functional-relations/) — PRQL 设计哲学的纲领文章,从函数式编程视角重新审视关系查询 |
| 官方教程 | [prql-lang.org/book](https://prql-lang.org/book/) — mdBook 教程,内嵌 PRQL 文档测试 |
| 在线 Demo | [prql-lang.org/playground](https://prql-lang.org/playground/) — 官方 Playground,浏览器内可编辑并查看编译后的 SQL |
| 标准库源码 | `prqlc/prqlc/src/semantic/std.prql` (251 行) + `prqlc/prqlc/src/sql/std.sql.prql` (454 行) |
| 架构文档 | `prqlc/prqlc/ARCHITECTURE.md`（仓库内）— 顶层 ASCII 图 + 每个 stage 子步骤 |
