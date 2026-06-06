# 23K stars 的 "Git for Data"：Dolt 如何用 Prolly Tree 把 MySQL 变成可分支可合并的数据库

> GitHub: <https://github.com/dolthub/dolt>

## 一句话总结

Dolt 是 Dolthub 公司商业主推、Apache 2.0 全开源的 **MySQL 兼容 SQL 数据库**，把 Git 的 fork/clone/branch/merge/diff/blame 完整移植到行级数据上，是当下唯一同时满足"可写 + SQL + Git 范式"三件套的开源产品。

## 值得关注的理由

1. **稀缺三角交集**：在「可写 SQL 引擎 + Git-like 版本控制 + MySQL 协议兼容」三个属性的交集里，Dolt 几乎没有直接对手，护城河来自底层自研的 Prolly Tree（概率 B-tree）+ NBS（Nomad Block Store）内容寻址存储。
2. **工程化深度第一梯队**：40+ GitHub Actions workflow、200+ BATS 集成测试、14 种语言 MySQL 客户端跨语言测试、4 种 ORM 兼容测试——商业公司的资源投入远超普通开源数据库。
3. **AI agent memory 押注成功**：2025-2026 期间日均 ~138 stars（爆发型增长），topics 中 5/20 是 agent 相关，已被 Beads、Gas Town 等多 agent 框架选作持久化记忆层，是 LLM 时代少有的"数据版本控制"可商用方案。

## 项目展示

![Dolt Logo](https://raw.githubusercontent.com/dolthub/dolt/main/images/Dolt-Logo@3x.svg) — 类型: hero

[📺 Dolt 官方介绍视频](https://www.youtube.com/watch?v=H2iZy0Cme10) — 类型: video（缩略图：https://img.youtube.com/vi/H2iZy0Cme10/maxresdefault.jpg）

![DeepWiki 4 层架构](https://deepwiki.com/dolthub/dolt) — 类型: 架构图（页面可访问，未收录静态图）

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | <https://github.com/dolthub/dolt> |
| Star / Fork | 23,238 / 794 |
| 代码行数 | 369,316（Go 92.2% / SQL 3.2% / YAML 1.8% / 其他 2.8%） |
| 项目年龄 | 11 年（首 commit 2015-06-02，GitHub 仓库 2019-07-24 创建） |
| 开发阶段 | 密集开发（v2.1.4 持续迭代中，30 天 349 commits） |
| 贡献模式 | 商业公司核心团队（7-10 人主力）+ 185 人社区增量 |
| 热度定位 | 大众热门（24h 采样 138 stars/天） |
| 质量评级 | 代码 9/10 \| 文档 8/10 \| 测试 9/10 \| CI 10/10 |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Dolt 由 **Dolthub Inc.**（Santa Monica, CA，2018 年成立）开发，旗舰产品，由 CTO **Zach Musgrave**（贡献 3,448 commits，14% 占比）作为主程。其技术血脉来自 Liquidata 时代的 **Noms** 项目——一个 Go 写的版本化数据原语库。Dolthub 把 Noms 的存储内核产品化，套上 MySQL 兼容 SQL 引擎形成 Dolt。Top 10 贡献者中还有前微软 V8/TypeScript 团队的 **Erik Arvidsson**（754 commits），侧面印证 Prolly Tree 自定义 B-tree 的技术深度。

### 问题判断

**传统数据版本控制工具的痛点**：
- **DVC/lakeFS/Iceberg** 等是"表格式层"或"文件版本层"，不替代数据库本身，下游要 `dvc get` 取出后才能用；
- **MySQL/MariaDB/TiDB** 等 OLTP 数据库虽然能 `INSERT/UPDATE`，但没有 commit/branch/merge/diff/blame 的概念——schema migration 永远是单向前进；
- **Git** 处理行级数据很顺，但 SQL 客户端和 ORM 工具链接入成本高。

Dolt 团队看到的机会窗口是：**把 Git 范式完整搬到"行级结构化数据"上，并保持 MySQL 协议兼容**——这意味着任何 MySQL 客户端、ORM、BI 工具零修改可用。

**时机为什么是现在**：
- 2015-2017 Noms 时代先做底层原语，2017-2018 沉寂 14 个月（Liquidata → Dolthub 商业化转型期），2019 拿到融资重启；
- 2022-06 v1.0 GA 赶上数据团队"协作 + 审计"需求爆发；
- 2025-2026 AI agent 多机协作场景给"行级版本控制"找到新杀手级应用（agent memory）。

### 解法哲学

**明确选择做什么**：
- **MySQL 兼容**（不发明新 SQL 方言）—— 复用 go-mysql-server 作为 SQL 引擎，零客户端改造；
- **Git 范式当一等公民**（不是补丁式 migration）—— `CALL dolt_commit()`、`SELECT * FROM dolt_log` 都是核心 API；
- **自研 Prolly Tree**（不基于 PostgreSQL/MySQL 二次开发）—— 因为 B+ tree 的 page 内部变更会丢失行级 lineage；
- **NBS 内容寻址存储**（不依赖 LSM 树或 B+ 树）—— 让"修改一行"只哈希链路上的祖先节点，未变化子树天然 dedup。

**明确不做什么**：
- 不做分布式事务/水平扩展（Hosted Dolt 是 SaaS，单机为主）；
- 不做 HTAP / 列存分析（写吞吐本身已让位给 lineage，OLAP 不是目标）；
- 不发明新 SQL 语法（`DOLT_*` 用 stored procedure 而非新关键字——保证 MySQL 客户端零修改）；
- 不跟进 PostgreSQL 高级特性（交给 Doltgres）。

### 战略意图

Dolthub Inc. 三条商业线：
- **DoltHub**（公共托管，类似 GitHub for databases）；
- **DoltLab**（自托管企业版）；
- **Hosted Dolt**（托管 Dolt 服务）。

Dolt 是开源引流 + 商业服务的核心引擎。**同公司产品矩阵**：Dolt (MySQL) + Doltgres (PG) + DoltLite (SQLite) + Dumbo (Mongo) 共用同一颗 Prolly Tree + NBS 内核，是"版本化 SQL"产品家族。

## 核心价值提炼

### 创新之处

按新颖度×实用性排序：

1. **Prolly Tree（概率 B-tree）** — 新颖度 4/5，实用性 5/5，可迁移性 4/5
   - 节点不是固定 page size，而是自适应到目标块大小（4KB），天然能映射到内容寻址 chunk
   - 行级 lineage、跨版本/跨分支 diff/merge 变一阶操作
   - 任何"对树状数据集做时间旅行+分支合并"场景都可借鉴

2. **DOLT_\* 存储过程 + 系统表桥** — 新颖度 4/5，实用性 5/5，可迁移性 4/5
   - 把 Git 命令翻译成 SQL stored procedure，把 Git 数据投影成可 SELECT 的系统表
   - 任何 MySQL 客户端（5.7+）零修改可用——TablePlus、MySQL Workbench、各语言 ORM
   - 是 Dolt 商业落地的关键护城河

3. **3-way merge for SQL data** — 新颖度 5/5，实用性 5/5，可迁移性 3/5
   - 把文本三路 merge 算法搬到 Prolly Tree 上
   - cell-wise 冲突解决——多人在同表不同分支改同一行不会丢数据
   - 依赖 Prolly Tree 抽象，迁移成本高

4. **NBS（Nomad Block Store）** — 新颖度 3/5，实用性 5/5，可迁移性 5/5
   - 内容寻址 chunk store + manifest CAS 乐观锁
   - 纯工程模式，移植到任何"只追加"系统都可

5. **自适应 Tuple 编码（Adaptive Tuple Encoding）** — 新颖度 3/5，实用性 4/5，可迁移性 3/5
   - `go/store/val/` 的 `TupleDesc` 可对每列指定不同编码
   - 列存项目的常规做法，参考 ClickHouse/DuckDB

### 可复用的模式与技巧

1. **Merkle DAG + 内容寻址是处理可版本化数据的通用模式**——Git、IPFS、Cassandra SSTable 都是同源思想，Dolt 把这套思想下沉到行级。
2. **go-mysql-server 适配模式**——用接口断言（`var _ sql.StoredProcedureDatabase = Database{}`）把"业务能力"挂到"通用引擎"上，比自己写解析器/优化器高 ROI 10 倍。
3. **stored procedure + 系统表桥接**——想给已有协议/工具加新概念时，**先想怎么映射到已有协议**，而不是发明新协议。
4. **测试矩阵化**——Dolt 把 14 种语言 MySQL 客户端 + 4 种 ORM + 5 个 OS 都做成 CI 矩阵，是"产品承诺=测试用例"的典范。
5. **feature_version 字段**——RootValue 根上带 `DoltFeatureVersion = 7`，新格式 vs 旧格式数据共存时按版本号分支处理，规避"老二进制读新数据崩溃"。

### 关键设计决策

```
决策: 用 go-mysql-server 做 SQL 前端，自己只做"Git 包装"
问题: 重写 SQL 解析器/优化器成本巨大
方案: 实现 sql.Database / sql.Table / sql.StoredProcedureDatabase 等接口，把版本控制"叠"在 SQL 之上
Trade-off: ✅ 继承 go-mysql-server 全部 SQL 兼容性、修复、安全补丁 ❌ 紧跟其 API 演化（同组织项目，方便但耦合）
可迁移性: 高（任何想用 go-mysql-server 的人都能用这套模式）
```

```
决策: Prolly Tree 作为表数据的"行级版本化"载体
问题: B+ tree 的 page 内部变更会丢失行级 lineage
方案: 自适应节点大小（4KB）+ 内容寻址哈希 + Flatbuffers 编码
Trade-off: ✅ 行级 diff/merge/blame 一阶操作 ❌ 写吞吐比 InnoDB 慢一个量级
可迁移性: 中（任何"对树状数据集做版本控制"的项目可借鉴）
```

```
决策: DOLT_* 用 stored procedure 而非新 SQL 语法
问题: MySQL 客户端不会发新关键字（ORM 还会解析失败）
方案: CALL dolt_commit('-m', 'msg', '-a') + 系统表 dolt_log/dolt_status/dolt_diff_<tab>
Trade-off: ✅ 任何 MySQL 客户端零修改可用 ❌ 过程调用语法笨拙
可迁移性: 高（任何想给已有协议加新能力的项目都可用此模式）
```

```
决策: RootValue = 一棵 Prolly Tree（数据库级别的"working tree"）
问题: 怎么把"Git 不可变性"映射到"数据库"
方案: 所有不可变操作（PutTable/RemoveTables/...）都返回新的 RootValue
Trade-off: ✅ commit/diff/merge/cherry-pick/revert 都成了一阶操作 ❌ 任何 schema 变更都要重写整个 root 节点
可迁移性: 高（"不可变树"模式可推广到任何文档/对象存储）
```

```
决策: NBS（Nomad Block Store）— 内容寻址 chunk store + manifest
问题: 怎么支持大量小写不丢 lineage
方案: 只追加（无 update/delete）+ manifest CAS + table file mmap
Trade-off: ✅ 节点级 dedup + 跨版本字节级共享 + 多进程乐观锁无锁读 ❌ 随机写效率比 LSM 差
可迁移性: 高（纯工程模式，移植到任何"只追加"系统都可）
```

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Dolt | DVC | lakeFS | TiDB |
|------|------|-----|--------|------|
| 数据所在 | Dolt 数据库内 | 外部存储 + .dvc 元文件 | 架在 S3 之上 | TiDB 集群内 |
| 版本单位 | 整库/表/行/cell | 文件 | 对象（key 级） | 整库（schema migration） |
| 查询语言 | SQL（MySQL 完整兼容） | 无（要 dvc get 取出） | 配合 Spark/Trino | SQL（MySQL 完整兼容） |
| 行级 diff/merge | ✅ 一阶操作 | ❌ 只支持文件 diff | ❌ 只支持 key 级 | ❌ 无 lineage 概念 |
| 随机写吞吐 | 中（commit 瓶颈） | 高 | 高 | 高（LSM + Raft） |
| 分布式 | 单机为主（Hosted Dolt 是 SaaS） | 不适用 | 强（多组件） | 强（水平扩展，TiKV） |
| 运维成本 | 极低（一个二进制） | 低 | 高（S3+DB+lakeFS 集群） | 高（PD/TiKV/TiDB） |
| 学习曲线 | 低（会 MySQL 就会） | 中 | 中 | 中（需理解 Raft/Region） |

### 差异化护城河

**技术护城河**：Prolly Tree + NBS 是 Dolthub 的独家实现，复制需要 5+ 年的工程积累。
**生态护城河**：与 go-mysql-server 同组织协同，MySQL 兼容性迭代速度无人能及。
**信任护城河**：Apache 2.0 全开源 + 商业公司背书 + 6 年生产案例。

### 竞争风险

- **最可能被替代的场景**：纯 SQL 兼容性需求（无版本控制）会被 TiDB/CockroachDB 抢走；纯大数据版本控制（TB-PB 级）会被 lakeFS/DVC 抢走。
- **核心风险点**：单一公司控制，路线图与商业 DoltHub 强绑定——若 Dolthub 商业化失败，开源版本可能进入"维护期"。

### 生态定位

```
            写吞吐 ↑
                     │
                     │     TiDB
                     │   lakeFS
                     │   DVC
                     │
                     │                       Dolt
                     └────────────────────────────────→ 行级版本化
                          弱                                 强
```

Dolt 在"行级版本化"轴上独占头部位置，代价是写吞吐（落在右下角）。填补了"可写 SQL + Git 范式 + MySQL 兼容"三角交集的空白——这是任何"传统数据库 + 版本控制"叠加方案都做不到的。

## 套利机会分析

- **信息差**：Dolt 不是"被低估的暗仓库"——23K stars、138/天爆发式增长、媒体曝光充分。**真正的信息差**在于「为什么行级版本控制这么难」（Prolly Tree 的工程深度）和「如何在 AI agent 场景落地」（agent memory 模式）。
- **技术借鉴**：
  - 学 Prolly Tree 的自适应块大小设计——可移植到任何需要"树状数据时间旅行"的场景（文档版本、KV 存储元数据、向量索引元数据）；
  - 学 stored procedure + 系统表桥接模式——给已有协议加新能力时，最高 ROI 的方式；
  - 学 go-mysql-server 适配模式——任何想基于成熟 SQL 引擎做垂直创新的项目都可参考。
- **生态位**：填补"行级版本化 SQL"空白，是 Git 范式在结构化数据上的最终归宿之一。
- **趋势判断**：
  - **2025-2026 增长趋势** ✅：AI agent memory 叙事精准命中，日均 138 stars 是同体量项目罕见速度；
  - **符合技术趋势** ✅：Merkle DAG + 内容寻址是分布式系统主流范式，Dolt 在 OLTP 场景做了产品化；
  - **后发优势** ❌：先发优势强，11 年历史 + 商业公司护城河难以追赶。

## 风险与不足

### 技术短板
1. **写吞吐瓶颈**：每次 commit 都要重新哈希 Prolly Tree 链路上的祖先节点，写吞吐比 InnoDB 慢一个量级（公开承认）；
2. **历史包袱**：旧 Noms-style `types.Value` 接口（`go/store/types/`，2,328 commits）与新 `prolly.Map` 并存，新人上手需学两套；
3. **单测覆盖率不透明**：无 `cover.out` 提交，可读覆盖率只能依赖 Go 工具本地跑；
4. **`dprocedures/init.go` 单文件膨胀**：30+ 个 `dolt_*` 过程集中在一个文件里——可读性 OK，但维护时小心冲突。

### 生态风险
1. **单点商业依赖**：路线图与商业 DoltHub 强绑定，存在供应商风险；
2. **fork 率偏低**：stars/forks ≈ 29.3，说明主要是"看 / 用 SaaS"而非"二次开发"——社区护城河弱；
3. **无顶级学术背书**：没有顶会论文，工程实现上的创新点主要在内部文档里。

### 选型场景
- ✅ **推荐场景**：中小数据（GB 级）+ 频繁 SQL 协作 + 数据审计 / lineage 需求 + AI agent 持久化记忆；
- ❌ **不推荐场景**：高 QPS OLTP（< 10K TPS）、TB-PB 级大数据、需要 PG 高级特性（交给 Doltgres）。

## 行动建议

### 如果你要用它
- **数据规模 ≤ 100GB、QPS ≤ 1K、需要 lineage/审计/AI agent memory** → 选 Dolt
- **数据规模 > 1TB、需要分布式水平扩展** → 选 TiDB 或 lakeFS
- **AI agent 持久化记忆** → Dolt 已是 Beads、Gas Town 等多 agent 框架的默认选择，证据充分

### 如果你要学它
按学习 ROI 排序：
1. **`go/store/prolly/tree/`** — Prolly Tree 节点定义、merge 算法、map/tuple 实现（核心创新）
2. **`go/libraries/doltcore/sqle/database.go`** — 接口断言模式（`var _ sql.XxxDatabase = Database{}`）看 Dolt 怎么把 Git 能力挂到 go-mysql-server
3. **`go/libraries/doltcore/sqle/dprocedures/init.go`** — 30+ `dolt_*` 存储过程注册表
4. **`go/store/nbs/`** — NBS 内容寻址存储 + manifest CAS
5. **`go/libraries/doltcore/doltdb/root_val.go`** — RootValue 接口定义（数据库级 working tree）
6. **`integration-tests/bats/`** — 200+ BATS 端到端测试看真实使用模式

### 如果你要 fork 它
可改进方向：
1. **补齐 PG 高级特性**：交给 Doltgres，自己可以专注 MySQL 优化
2. **优化写吞吐**：把 commit 链路上的祖先节点重哈希做 batch / async 化
3. **支持 Iceberg/Delta 表导出**：让 Dolt 写入的数据可被 Spark/Trino 读取
4. **Agent memory 框架集成**：提供 LLM-friendly 的 high-level SDK（`dolt_agent_memory` 之类）
5. **清理历史包袱**：把 `go/store/types/` 的 Noms 旧代码彻底迁到 prolly

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | <https://deepwiki.com/dolthub/dolt> |
| Zread.ai | <https://zread.ai/dolthub/dolt> |
| 关联论文 | 无（工程产品，无对应学术论文） |
| 在线 Demo | <https://www.dolthub.com/>（Hosted Dolt 试用） |
| 官方文档 | <https://docs.dolthub.com/> |
| 官方博客 | <https://www.dolthub.com/blog>（含 Prolly Tree、adaptive encoding、merge 算法深度文章） |
