# sqlite-vec 内容分析

## 动机与定位

sqlite-vec 的核心动机是为 SQLite 生态提供一个**零依赖、纯 C、全平台**的向量搜索扩展。它是作者 Alex Garcia 此前项目 sqlite-vss（基于 Faiss）的精简继任者。sqlite-vss 虽然功能更强（支持 ANN 索引），但引入了 C++ 依赖和复杂的构建链，导致在 WASM、嵌入式、移动端等场景下无法使用。

sqlite-vec 做了一个大胆的取舍：**放弃 ANN 索引，换取极致的可移植性和零依赖**。整个项目是单文件 C 实现（`sqlite-vec.c`，约 10,193 行），仅依赖标准 C 库和 SQLite 扩展 API，可编译到 Linux/macOS/Windows/Android/iOS/WASM/Cosmopolitan 全平台。

定位是：**嵌入式场景下的向量搜索基础设施**——不追求最高性能，而是追求最广的兼容性和最低的集成成本。

## 作者视角

Alex Garcia 被社区称为"SQLite 扩展之王"，拥有 27 个 SQLite 扩展项目。他的设计哲学清晰一致：

1. **SQLite 原生体验**：所有功能通过标准 SQL 接口暴露，不发明新的查询语言或 API
2. **单文件分发**：遵循 SQLite 的 amalgamation 传统，一个 `.c` 文件包含全部实现
3. **零依赖极端主义**：宁可性能受限（暴力扫描），也不引入外部依赖
4. **渐进式功能开发**：从 TODO 文件可见，大量功能（partition UPDATE、NULL 处理、字典编码）处于"later"状态，说明作者优先保证核心路径的稳定

从代码注释和 Issue 引用可以看到，作者对 SQLite 虚拟表 API 的掌握极为深入，能精确利用 `sqlite3_vtab_in()`、`sqlite3_blob_open()` 等底层接口。

## 架构与设计决策

### 目录结构概览

```
sqlite-vec/
├── sqlite-vec.c          # 核心实现（10,193 行，单文件 C）
├── sqlite-vec.h.tmpl     # 头文件模板（构建时生成版本信息）
├── Makefile              # 构建系统（支持 loadable/static/cli 三种目标）
├── ARCHITECTURE.md       # 内部架构文档（Shadow Tables + idxStr 协议）
├── reference.yaml        # API 参考定义
├── bindings/             # 多语言绑定
│   ├── python/           # Python 绑定
│   ├── go/               # Go 绑定（含 ncruces WASM 方案）
│   └── rust/             # Rust 绑定
├── tests/                # 测试套件（4,118 行 Python + C + Rust + WASM）
│   ├── test-loadable.py  # 主测试（2,577 行，覆盖全部 SQL 函数和虚拟表）
│   ├── test-metadata.py  # 元数据列测试
│   ├── test-partition-keys.py
│   ├── test-insert-delete.py
│   ├── test-unit.c       # C 单元测试
│   ├── unittest.rs       # Rust 单元测试
│   └── test-wasm.mjs     # WASM 测试
├── examples/             # 16 种语言/平台示例
│   ├── simple-python/    simple-node/    simple-rust/
│   ├── simple-go-cgo/    simple-go-ncruces/
│   ├── simple-bun/       simple-deno/    simple-ruby/
│   └── simple-wasm/      simple-c/       simple-sqlite/
├── benchmarks/           # 性能基准测试
├── site/                 # 文档站（VitePress）
└── .github/workflows/    # CI（test/release/fuzz/site 四条流水线）
```

### 关键设计决策

**1. Chunk-based 列式存储**

vec0 虚拟表使用分块列式存储，每个 chunk 包含固定数量的向量（默认 chunk_size 可配置）。数据分散在多个 Shadow Tables 中：
- `_chunks`：chunk 元信息（大小、有效位图、rowid 列表）
- `_rowids`：rowid 到 chunk_id/chunk_offset 的映射
- `_vector_chunksNN`：实际向量数据（BLOB 存储）
- `_metadatachunksNN`：元数据列（支持 boolean/int/float/text 四种类型）
- `_auxiliary`：辅助列数据

这种设计使得 KNN 查询可以按 chunk 流式扫描，内存占用可控。

**2. 暴力扫描 KNN + 分块 Top-K 归并**

KNN 查询的核心算法是：逐 chunk 计算所有向量的距离，使用 `min_idx()` 选出 chunk 内 Top-K，然后通过 `merge_sorted_lists()` 归并全局 Top-K。这是一个纯暴力扫描方案，时间复杂度 O(n)，但实现极简且正确性有保障。

**3. Bitmap 过滤管线**

KNN 查询中的过滤采用 bitmap 管线设计：先用 validity bitmap 标记有效行，然后依次应用 rowid IN 过滤、metadata 过滤、距离约束过滤，每步都通过 `bitmap_and_inplace()` 原地合并。这是一个高效的列式过滤模式。

**4. idxStr 编码协议**

SQLite 虚拟表的 `xBestIndex`/`xFilter` 通过 `idxStr` 传递查询计划。sqlite-vec 设计了一套精巧的编码协议：1 字节 header（查询类型：fullscan/point/KNN）+ N 个 4 字节 block（每个 block 描述一个 argv 参数的含义）。这使得复杂的 KNN+过滤查询可以通过字符串高效传递。

**5. SIMD 条件编译分层**

距离计算函数采用三层架构：通用 C 实现 -> NEON 加速（ARM）-> AVX 加速（x86）。通过编译宏 `SQLITE_VEC_ENABLE_NEON` / `SQLITE_VEC_ENABLE_AVX` 和运行时维度检查（如 `qty > 16` 才走 NEON 路径）选择最优实现。Makefile 自动检测平台设置对应标志。

## 创新点

### 1. SQLite 虚拟表作为向量索引的范式

sqlite-vec 证明了 SQLite 虚拟表可以作为完整的向量搜索引擎：创建表 = 定义索引，INSERT = 添加向量，WHERE + ORDER BY = KNN 查询，全部通过标准 SQL 完成。这种"SQL 即接口"的设计消除了学习成本，任何了解 SQL 的开发者都可以直接使用。

### 2. 四种列类型的统一抽象

vec0 虚拟表统一了四种列类型（vector/partition/auxiliary/metadata），用 `vec0_user_column_kind` 枚举和 `user_column_idxs` 映射表实现。用户在 CREATE VIRTUAL TABLE 时自然地混合声明：

```sql
CREATE VIRTUAL TABLE movies USING vec0(
  embedding float[768],
  genre text,              -- metadata 列，可过滤
  user_id integer partition key,  -- 分区键
  title text auxiliary      -- 辅助列，仅存储
);
```

### 3. 静态 Blob 内存映射接口

`vec_static_blobs` 模块允许将外部内存（如 NumPy 数组、mmap 文件）直接注册为可查询的向量集合，无需拷贝数据进 SQLite。这是一个巧妙的零拷贝接口，适用于大规模只读向量数据。

## 可复用模式

### 1. 单文件 C + Shadow Tables 模式

整个扩展编译为单个 `.c` 文件，利用 SQLite Shadow Tables 实现持久化存储。这种模式适用于任何需要在 SQLite 上实现自定义索引/存储引擎的场景。关键点：
- 用 `#pragma region` 划分代码区域
- 所有内存管理使用 `sqlite3_malloc` / `sqlite3_free`
- Shadow Table 命名约定 `{table}_{suffix}`

### 2. 编译时平台检测 + 条件 SIMD

Makefile 通过 `uname -sm` 检测平台，自动设置 SIMD 编译标志：
```makefile
ifeq ($(shell uname -sm),Darwin arm64)
  CFLAGS += -mcpu=apple-m1 -DSQLITE_VEC_ENABLE_NEON
endif
```
代码中则通过运行时大小检查选择实现路径，确保小维度向量不会因 SIMD 对齐而受损。这种"编译期检测 + 运行期兜底"的模式在高性能 C 库中普遍适用。

### 3. idxStr 编码协议

将复杂的查询计划编码为紧凑的字符串，通过 SQLite 的 `xBestIndex` -> `xFilter` 传递。每个参数用 4 字节 block 描述类型和语义。这种协议设计在任何需要序列化查询计划的虚拟表中都可复用。

### 4. Bitmap 过滤管线

使用位图表示候选集，多个过滤条件通过 `bitmap_and_inplace` 逐步缩小候选范围。这是列式存储引擎中的经典模式，实现简单且高效。每个 chunk 的 bitmap 大小仅为 `chunk_size / 8` 字节。

## 竞品交叉分析

### vs pgvector

| 维度 | sqlite-vec | pgvector |
|------|-----------|----------|
| 数据库 | SQLite（嵌入式） | PostgreSQL（C/S 架构） |
| 索引类型 | 暴力扫描（无 ANN） | IVFFlat + HNSW |
| 依赖 | 零依赖 | 依赖 PostgreSQL |
| 适用规模 | < 100 万向量（实际受限于暴力扫描） | 数千万级 |
| 部署复杂度 | 单文件加载 | 需要 PostgreSQL 实例 |
| 生态 | Python/Node/Go/Rust/WASM | 主要 Python/Node |

**结论**：两者不在同一赛道。pgvector 面向服务端大规模向量检索，sqlite-vec 面向嵌入式/边缘/客户端场景。sqlite-vec 的价值在于"不需要服务器也能做向量搜索"。

### vs sqlite-vector (sqlite.ai)

| 维度 | sqlite-vec | sqlite-vector |
|------|-----------|---------------|
| 作者 | Alex Garcia（社区） | sqlite.ai（商业公司） |
| 开源程度 | 完全开源（Apache/MIT） | 核心开源 |
| 索引 | 暴力扫描 | DiskANN（ANN 索引） |
| 依赖 | 零依赖 | 有 C++ 依赖 |
| 成熟度 | 0.1.x alpha | 较新 |
| WASM 支持 | 完整 | 受限 |

**结论**：sqlite-vector 在性能上有 ANN 索引的优势，但 sqlite-vec 在可移植性和生态覆盖（WASM、移动端）上领先。如果 sqlite-vec 能补齐 ANN 索引（Issue #25），竞争力将大幅提升。

### vs Chroma

| 维度 | sqlite-vec | Chroma |
|------|-----------|--------|
| 定位 | SQLite 扩展 | 独立向量数据库 |
| 接口 | SQL | Python/JS SDK |
| 后端 | SQLite | SQLite + 自有索引 |
| 嵌入式 | 完全嵌入式 | 嵌入式 + C/S |
| ANN | 无 | HNSW |

**结论**：Chroma 底层也使用 SQLite 存储元数据，但有自己的 HNSW 索引层。sqlite-vec 更"原生"，直接作为 SQL 扩展使用，集成成本最低。Chroma 更适合 Python/AI 应用的快速原型。

### 综合竞争结论

sqlite-vec 占据了一个独特的生态位：**"SQLite 原生 + 零依赖 + 全平台"向量搜索**。这个定位在边缘计算、移动应用、浏览器 WASM、嵌入式设备等场景中几乎没有竞品。核心瓶颈在于缺少 ANN 索引（Issue #25），这限制了它在中大规模数据集上的实用性。一旦 ANN 索引补齐，它可能成为嵌入式 AI 场景的事实标准。

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码组织 | B+ | 单文件 10K 行，用 `#pragma region` 分区，结构清晰但文件过大 |
| 注释质量 | B | 关键结构体有 Doxygen 注释，但部分复杂算法（如 KNN 归并）缺少解释 |
| 错误处理 | A- | 全面的 `rc != SQLITE_OK` 检查，错误信息通过 `vtab_set_error` 传递给用户 |
| 内存管理 | A- | 统一使用 `sqlite3_malloc`/`sqlite3_free`，cursor 有完整的 cleanup 路径 |
| 测试覆盖 | B+ | 4,118 行测试代码，覆盖 Python/C/Rust/WASM 多平台，使用 snapshot 测试 |
| CI/CD | A | 4 条 workflow（test/release/fuzz/site），覆盖 7 个平台（含 Android/iOS/WASM） |
| 文档 | B+ | 完整的 API 参考（reference.yaml）、架构文档、16 个语言示例 |
| 安全 | B | 有 SECURITY.md，有 fuzz 测试，但暂无 `xIntegrity` 实现 |

### 质量检查清单

- [x] **测试存在**：Python (pytest) + C 单元测试 + Rust 测试 + WASM 测试
- [x] **CI 流水线**：GitHub Actions，7 平台构建 + 测试
- [x] **Fuzz 测试**：独立 fuzz workflow
- [x] **多平台构建**：Linux/macOS/Windows/Android/iOS/WASM/Cosmopolitan
- [x] **SIMD 优化**：AVX (x86) + NEON (ARM) 条件编译
- [x] **文档站**：VitePress 构建，含 API 参考和使用指南
- [x] **版本管理**：VERSION 文件 + 构建时嵌入版本/commit/日期
- [x] **双许可**：Apache-2.0 + MIT
- [ ] **ANN 索引**：核心缺失，Issue #25 尚未解决
- [ ] **xIntegrity**：代码中标注为 TODO（Issue #44）
- [ ] **xRename**：不支持重命名（Issue #43）
- [ ] **Savepoint 支持**：`xSavepoint`/`xRelease`/`xRollbackTo` 均为空实现
