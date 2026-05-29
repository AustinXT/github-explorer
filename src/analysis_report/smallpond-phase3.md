# smallpond 内容分析（Phase 3: What & How）

## 动机与定位

smallpond 的核心定位是 **填补 DuckDB 从单机到集群的空白**。官方 README 一句话概括："A lightweight data processing framework built on DuckDB and 3FS"。

**解决的核心痛点：**
- DuckDB 单机内存上限（约几百 GB）无法处理 PB 级数据
- Spark/Flink 等重型框架的运维成本（ZooKeeper、YARN、元数据服务等长驻服务）
- 数据团队需要 SQL 能力 + Python 灵活性 + 大规模扩展的组合

**甜区定位：** 10TB ~ 1PB 的数据处理。低于 10TB 用单机 DuckDB 即可，超过 1PB 需要成熟分布式引擎（Spark）。

**关键洞察：** smallpond 不是分布式数据库，而是"分区级分布式批处理框架"。SQL 仅在单分区内执行，分区间通过文件系统交换数据。

## 作者视角

DeepSeek 做 smallpond 的动机来源于其 AI 训练管线的具体需求：

1. **与 3FS 配对**：3FS 是 DeepSeek 自研的分布式文件系统，smallpond 借助 3FS 的高吞吐 IO 实现 PB 级排序（110.5 TiB / 30 分钟）
2. **数据预处理管线**：AI 训练需要大规模数据清洗、去重、分桶，smallpond 的 partition + SQL 模式天然适配这类 ETL 场景
3. **内部工具外部化**：contrib 目录包含 `warc.py`（WARC 网页抓取格式解析），暗示其内部用于大规模网页数据预处理
4. **开源矩阵中的位置**：3FS（存储层）+ smallpond（计算层）构成完整的数据基础设施栈

## 架构与设计决策

### 整体架构

```
用户 API (DataFrame)
    → 逻辑计划 (Node DAG)
        → 优化器 (Optimizer)
            → 执行计划 (Planner → Task DAG)
                → 调度器 (Scheduler)
                    → 执行器 (Executor / Ray)
```

### 核心模块解析

#### 1. 双模式执行：Ray 模式 + 原生调度模式

**关键设计决策**：smallpond 维护了两套完全不同的执行引擎。

**Ray 模式**（`session.py`，交互式场景）：
- 通过 `smallpond.init()` 启动，自动初始化 Ray 集群
- 每个 Task 包装为 `@ray.remote` 函数，利用 Ray 的对象存储传递 DataSet 引用
- Task 通过 pickle 文件实现检查点，支持跳过已完成任务
- 适合交互式探索和中等规模作业

**原生调度模式**（`scheduler.py` + `executor.py`，生产环境）：
- 通过 `Driver` / `JobManager` 启动，自行管理分布式调度
- 基于文件系统的工作队列（`WorkQueueOnFilesystem`）进行任务分发
- Scheduler 和 Executor 通过共享文件系统通信（而非 RPC）
- Executor 用多进程（`SimplePool`）执行任务，每个 Task 隔离在独立进程中
- 支持推测执行（speculative execution）、故障容错、优雅停机

**为什么选基于文件系统的队列而不是消息队列？** 因为依赖 3FS，文件系统就是通信层，无需额外基础设施。

#### 2. 逻辑计划层（node.py，2024 行）

Node 层是所有计算的蓝图。关键节点类型：

| Node | 职责 | 对应 Task |
|------|------|-----------|
| `DataSourceNode` | 数据输入 | `DataSourceTask` |
| `SqlEngineNode` | DuckDB SQL 执行 | `SqlEngineTask` |
| `HashPartitionNode` | 哈希重分区 | `HashPartitionTask` |
| `ShuffleNode` | 按已有列分区 | 继承 `HashPartitionNode` |
| `EvenlyDistributedPartitionNode` | 均匀分区 | `EvenlyDistributedPartitionProducerTask` |
| `ArrowComputeNode` | Arrow 内存计算 | `ArrowComputeTask` |
| `ArrowStreamNode` | 流式 Arrow 处理 | `ArrowStreamTask` |
| `PythonScriptNode` | 自定义 Python | `PythonScriptTask` |
| `DataSinkNode` | 数据输出 | `DataSinkTask` |
| `ProjectionNode` | 列裁剪（零拷贝） | `ProjectionTask` |
| `ConsolidateNode` | 合并分区（逻辑操作） | `MergeDataSetsTask` |

**Node → Task 的映射**不是 1:1，而是 1:N。一个 `SqlEngineNode` 会为每个分区生成一个 `SqlEngineTask`。这是"分区级分布"的核心。

#### 3. 执行任务层（task.py，3197 行 -- 代码最重的模块）

Task 承担了执行的全部重量：

- **生命周期管理**：`initialize()` → `run()` → `finalize()` / `cleanup()`
- **DuckDB 集成**（`ExecSqlQueryMixin`）：
  - 每个 Task 创建独立的 `duckdb.connect(":memory:")`，无需并发控制
  - 通过 `CREATE VIEW` 将输入文件暴露为虚拟表，SQL 引用 `{0}`, `{1}` 占位符
  - 精细控制 DuckDB 资源：`SET threads`, `SET memory_limit`, `SET temp_directory`
  - 支持 UDF 绑定（Python UDF、DuckDB Extension、外部模块）
- **分区执行模式**（`HashPartitionTask`）：
  - DuckDB 引擎方式：用 `COPY ... TO ... (PARTITION_BY)` 实现 Hive 分区写入
  - Arrow 引擎方式：读取数据到 Arrow 表，按 hash 列计算分区 ID，逐分区写出 Parquet
- **流式处理**（`ArrowStreamTask`）：支持检查点（checkpoint），断点恢复
- **性能指标收集**：每个 Task 自动采集 wall time、CPU time、RSS、IO 时间

#### 4. 调度器（scheduler.py，1170 行）

调度器是整个系统的大脑：

- **任务调度算法**：拓扑排序 + 贪心。叶子任务先入队，完成后解锁下游
- **推测执行**：当任务执行时间超过同类型任务 P95 - P50 时，重新调度一份副本
- **Executor 探测**：周期性发送 `Probe`，超过 N 轮未响应则标记 FAIL
- **资源感知调度**：按 CPU/GPU/内存需求分配任务到 Executor，支持资源 boost（自动放大资源限制）
- **OOM 恢复**：检测 `OutOfMemory` 后自动倍增内存限制并重试
- **状态持久化**：定期将调度状态序列化到文件系统，支持调度器崩溃恢复

#### 5. DuckDB 集成方式 -- 关键设计

smallpond 对 DuckDB 的使用方式是**嵌入式、单分区、短连接**：

```python
# SqlEngineTask.run() 的核心流程（简化）
with duckdb.connect(":memory:") as conn:
    # 1. 配置 DuckDB 实例
    conn.sql(f"SET threads TO {cpu_limit}")
    conn.sql(f"SET memory_limit='{memory_limit}MB'")

    # 2. 将输入文件注册为视图
    for dataset in input_datasets:
        conn.sql(f"CREATE VIEW {view_name} AS SELECT * FROM read_parquet({paths})")

    # 3. 执行用户 SQL
    conn.sql(f"COPY ({user_query}) TO '{output_path}' (FORMAT PARQUET, PER_THREAD_OUTPUT)")
```

**设计选择的后果：**
- 无需维护 DuckDB 长连接或共享状态
- 每个 Task 的 DuckDB 实例完全隔离，天然支持并行
- 但跨分区 JOIN 需要用户手动保证分区对齐（`repartition(n, hash_by=key)`）
- 不支持跨分区的 GROUP BY 或 ORDER BY（用户需手动两阶段聚合）

#### 6. 分区策略 -- 核心创新点

分区是 smallpond 的灵魂。三种分区模式：

1. **均匀分区**（`EvenlyDistributedPartitionNode`）：按文件数或行数均匀拆分
2. **哈希分区**（`HashPartitionNode`）：按指定列的哈希值分配，保证相同 key 落入同一分区
3. **嵌套分区**（`nested=True`）：在现有分区内再细分，生成多维分区空间

分区的物理实现是 **Producer-Consumer 模式**：
- Producer 读取输入 → 计算分区 → 写出多个分区文件
- Consumer 从多个 Producer 收集属于自己的分区文件
- 支持参数 `max_card_of_producers_x_consumers = 4,096,000` 限制组合爆炸

#### 7. 优化器（optimizer.py，55 行 -- 极简）

目前唯一的优化：**连续 SqlEngineNode 融合**。

```python
# 优化前：两次 DuckDB 调用
child: "SELECT * FROM {0}"
node:  "SELECT a, b FROM {0}"

# 优化后：一次 DuckDB 调用
fused: "SELECT a, b FROM (SELECT * FROM {0})"
```

优化器设计极简，留有大量扩展空间（谓词下推、分区裁剪等均未实现）。

## 创新点

### 1. "分区级分布"而非"查询级分布"

与 Spark/Presto 将一条 SQL 分布到多个节点执行不同，smallpond 将数据分区后在每个分区上独立运行完整 SQL。这意味着：

- **无需分布式查询规划器**（DuckDB 单机规划即可）
- **无需网络 shuffle**（通过文件系统交换分区数据）
- **代价**：用户需要理解分区语义，手动管理 repartition

### 2. 基于文件系统的零基础设施通信

Scheduler 和 Executor 通过共享文件系统的目录结构通信（`WorkQueueOnFilesystem`），任务序列化为 pickle 文件：
- 无需 RPC 框架
- 无需消息队列
- 利用 3FS 的原子性保证正确性

### 3. 双引擎无缝切换

同一 API 支持 Ray 模式（交互式）和原生调度模式（生产批处理），Session 配置透明切换。

### 4. 任务级细粒度资源控制

每个 Node 可声明 `cpu_limit`, `gpu_limit`, `memory_limit`，调度器据此分配。DuckDB 实例的线程数和内存限制精确匹配声明值。支持运行时 resource boost（空闲资源自动扩容）。

## 可复用模式

1. **Producer-Consumer 分区模式**：通用的大数据集重分区方案，可移植到其他框架
2. **基于文件系统的工作队列**：零依赖的分布式任务分发机制，适合有共享存储的环境
3. **逻辑计划 → 物理计划 两阶段编译**：Node DAG → Task DAG 的设计模式，解耦计划与执行
4. **推测执行算法**：基于 P50/P95/P99 统计的尾延迟检测，自动重调度慢任务
5. **嵌入式 SQL 引擎集成模式**：独立连接 + CREATE VIEW 注入输入 + COPY TO 输出，适用于任何嵌入式 SQL 引擎
6. **检查点式流处理**：`ArrowStreamTask.RuntimeState` 记录处理进度，支持 crash recovery

## 竞品交叉分析

| 维度 | smallpond | Spark | Daft | Polars Cloud | MotherDuck |
|------|-----------|-------|------|-------------|------------|
| SQL 引擎 | DuckDB（嵌入式） | Catalyst + Tungsten | 无原生 SQL | 无原生 SQL | DuckDB（托管） |
| 分布式模型 | 分区级分布 | 查询级分布 | 查询级分布 | 工作级分布 | 云端单实例 |
| 调度依赖 | Ray 或自带 | YARN/K8s/Standalone | Ray | 自带云服务 | 无需（SaaS） |
| 长驻服务 | 无 | 需要 Master/Worker | 无 | 需要 | 需要 |
| 跨分区 JOIN | 手动 repartition | 自动 shuffle | 自动 shuffle | N/A | 自动 |
| 甜区规模 | 10TB~1PB | 1TB~10PB+ | 10GB~10TB | 10GB~1TB | 1GB~100GB |
| GPU 支持 | 有（资源声明） | 有限 | 有（原生） | 无 | 无 |
| 容错 | 推测执行+重试 | Stage 级重试 | Task 级重试 | 托管 | 托管 |
| 编程模型 | DataFrame+SQL | DataFrame+SQL | DataFrame | DataFrame | SQL |
| 核心优势 | 极简运维+DuckDB SQL 能力 | 生态成熟 | Rust 性能+GPU | 极简 API | 零运维 |

**关键差异总结：**
- **vs Spark**：smallpond 牺牲自动 shuffle 换取运维简洁性。Spark 的 Catalyst 优化器远比 smallpond 的 55 行优化器成熟，但 smallpond 的 DuckDB 单分区执行速度可能更快
- **vs Daft**：Daft 基于 Rust 有原生性能优势和 GPU 加速；smallpond 胜在 DuckDB 的 SQL 兼容性和成熟度
- **vs MotherDuck**：MotherDuck 是 SaaS，smallpond 是自部署。smallpond 能处理的数据规模远超 MotherDuck
- **vs Ray Data**：smallpond 用 Ray 但不用 Ray Data，因为 Ray Data 无法精确控制分区和 DuckDB 的资源配额

## 代码质量

### 测试
- **17 个测试文件**，2916 行测试代码
- 覆盖核心模块：`test_execution.py`（758 行）、`test_partition.py`（567 行）、`test_dataframe.py`（213 行）
- CI 跑 4 个 Python 版本（3.9~3.12），使用 `pytest-xdist` 4 路并行
- 有 benchmark 测试（`test_bench.py`）
- **不足**：测试仅在 `self-hosted` runner 上跑（依赖内部基础设施），无公共 CI 可见

### CI/CD
- 单一 `ci.yml`：格式检查（black）+ 测试 + 文档构建 + 文档部署
- 每日定时构建（`schedule: '0 0 * * *'`）
- 代码格式统一：`black --line-length=150`

### 代码组织
- **总量**：约 16,000 行 Python（含测试 2,916 行）
- **集中度高**：`task.py`（3197 行）占比 24%，承载了过多职责
- **文档**：有 Sphinx API 文档，docstring 覆盖主要公开 API
- **类型标注**：广泛使用 Python typing，但未见 mypy 检查
- **内存管理**：配置 jemalloc/mimalloc 替代系统分配器，精细控制 Arrow 和 DuckDB 内存池
- **日志**：使用 loguru，支持多级别文件日志 + Prometheus 指标 + Grafana 仪表盘 + Plotly timeline

### 待改进
- `task.py` 3197 行需要拆分（SQL 执行、Arrow 计算、流式处理应各自独立）
- 优化器仅 55 行，缺少谓词下推、分区裁剪等常见优化
- PR 合并率 10%、Issue 关闭率 15%，社区互动不足
- 无 S3/云存储原生支持（Issue #10），限制了非 3FS 环境的使用
