# sqlite-vec 网络分析报告

> 分析时间：2026-03-22 | 仓库：[asg017/sqlite-vec](https://github.com/asg017/sqlite-vec)

---

## 仓库基本数据

| 指标 | 数值 |
|------|------|
| 名称 | sqlite-vec |
| 描述 | A vector search SQLite extension that runs anywhere! |
| 主语言 | C（370KB），辅以 Python（176KB）、Makefile、Rust、TypeScript 等 |
| Star | **7,248** |
| Fork | 294 |
| Watch | 63 |
| Issues | 143（含已关闭） |
| PR | 33 |
| 许可证 | Apache-2.0 |
| 磁盘占用 | 894 KB |
| 创建时间 | 2024-04-20 |
| 最近推送 | 2026-03-21 |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| Topics | `sqlite`, `sqlite-extension` |
| 默认分支 | main |
| 官方文档 | https://alexgarcia.xyz/sqlite-vec/ |

**核心定位**：一个极小、零依赖、纯 C 编写的 SQLite 向量搜索扩展，可运行在任何 SQLite 支持的平台上（Linux/macOS/Windows/WASM/Raspberry Pi 等）。是 `sqlite-vss`（基于 Faiss）的精简继任者。

---

## 作者画像

| 属性 | 值 |
|------|------|
| 姓名 | Alex Garcia |
| GitHub ID | asg017 |
| 身份 | 自由职业软件工程师 |
| 所在地 | 洛杉矶，加利福尼亚 |
| 个人网站 | https://alexgarcia.xyz/ |
| 公开仓库 | 167 个 |
| 粉丝 | 736 |
| 注册时间 | 2015-10-18 |

**作者特征**：Alex Garcia 是 **SQLite 扩展领域最活跃的独立开发者之一**，几乎所有公开仓库都围绕 SQLite 扩展生态构建。其作品矩阵：

| 项目 | Stars | 语言 | 定位 |
|------|-------|------|------|
| **sqlite-vec** | 7,248 | C | 向量搜索（当前主力项目） |
| sqlite-vss | 1,984 | C++ | 向量搜索（已废弃，基于 Faiss） |
| sqlite-lines | 403 | C | 按行读取文件 |
| sqlite-loadable-rs | 401 | Rust | Rust 编写 SQLite 扩展的框架 |
| sqlite-html | 397 | Go | HTML 解析 |
| sqlite-ecosystem | 286 | TS | SQLite 扩展生态汇总 |
| sqlite-http | 261 | Go | HTTP 请求 |
| sqlite-lembed | 255 | C | 本地文本嵌入（GGUF 格式） |
| sqlite-rembed | 153 | Rust | 远程 API 嵌入（OpenAI/Ollama） |
| sqlite-regex | 202 | Rust | 正则表达式 |

**判断**：作者是「SQLite 扩展之王」级别的专注开发者，拥有完整的 SQLite 工具链思维。sqlite-vec 是其旗舰项目。

### 贡献者分布

| 贡献者 | 提交数 |
|--------|--------|
| asg017（作者本人） | 394 |
| dleviminzi | 5 |
| otoolep | 2 |
| sheldonrobinson | 2 |
| 其他 12 位 | 各 1 |

**典型的单人核心项目**，总共 16 位贡献者，作者贡献占比 > 95%。社区 PR 参与有限。

---

## 社区热度

### Star 增长曲线

通过采样不同时间段的 star 数据，构建增长轨迹：

| 时间节点 | 累计 Star 约值 | 阶段特征 |
|----------|---------------|----------|
| 2024-04 创建 | 0 → ~1,500 | 首月爆发（HN 效应） |
| 2024-08 | ~1,500 → ~3,000 | 稳定增长期，Mozilla 赞助公布 |
| 2024-12～2025-01 | ~4,500 | 持续中速增长 |
| 2025-08 | ~6,000 | AI/RAG 热度带动 |
| 2026-03 | ~7,248 | 仍在增长，v0.1.7 发布带来关注 |

**增长节奏**：从 2024-04 创建至今（约 23 个月）积累 7,248 star，平均月增 ~315 star。增长主要由 Hacker News 首发、Mozilla Builders 赞助公布、AI/RAG 浪潮三波驱动。2026 年 3 月最新一周仍有稳定的 star 流入。

### 包下载量（极为亮眼）

| 平台 | 最近一个月下载量 |
|------|----------------|
| **PyPI** | **2,359,518**（日均 ~107K） |
| **npm** | **4,929,009**（月均近 500 万） |

**分析**：月下载量合计超 **700 万次**，远超其 7K star 所暗示的受众规模。说明 sqlite-vec 已被大量自动化流水线、CI/CD、框架（如 LangChain）集成，属于**基础设施级别**的采用规模。

### 最新版本

| 版本 | 发布时间 | 说明 |
|------|---------|------|
| v0.1.8-alpha.1 | 2026-03-21 | 最新预发布 |
| **v0.1.7** | **2026-03-17** | 正式回归版本，标题为 "sqlite-vec is back" |
| v0.1.7-alpha.11~13 | 2026-03-17 | 密集预发布 |

v0.1.7 的发布标题"sqlite-vec is back"表明项目经历了一段维护沉寂期后重新活跃。

---

## 生态网络

### 赞助商（重量级）

| 赞助商 | 类型 |
|--------|------|
| **Mozilla Builders** | 主赞助商 |
| Fly.io | 云平台 |
| Turso | SQLite 云服务商（libSQL 背后公司） |
| SQLite Cloud | SQLite 托管服务 |
| Shinkai | AI 产品 |

获得 **Mozilla** 主赞助是极高的行业认可信号。

### 多语言绑定与集成

sqlite-vec 提供了极广泛的语言/平台支持：

- **Python**: `pip install sqlite-vec` — PyPI 月下载 236 万
- **Node.js**: `npm install sqlite-vec` — npm 月下载 493 万
- **Ruby**: `gem install sqlite-vec`
- **Go**: `go get github.com/asg017/sqlite-vec/bindings/go`
- **Rust**: `cargo add sqlite-vec`
- **Datasette**: `datasette install datasette-sqlite-vec`
- **rqlite**: 原生支持
- **sqlite-utils**: 插件
- **Elixir**: 社区请求中（Issue #151）
- **Dart/Flutter**: PR 进行中（PR #119）
- **.NET**: 社区请求中（Issue #193）

### 框架集成

- **LangChain**: 内置 SQLiteVec 向量存储集成
- **Drupal AI**: SQLite VDB Provider 模块
- **Simon Willison 的工具链**: sqlite-utils / Datasette 原生支持

### 配套项目

- **sqlite-lembed**: 本地生成文本嵌入（GGUF 模型）
- **sqlite-rembed**: 通过远程 API（OpenAI/Nomic/Ollama）生成嵌入
- **sqlite-ecosystem**: 作者的 SQLite 扩展总览

---

## 官方文档洞察

| 文档资源 | URL | 状态 |
|----------|-----|------|
| 官方文档站 | https://alexgarcia.xyz/sqlite-vec/ | 进行中（WIP） |
| 安装指南 | https://alexgarcia.xyz/sqlite-vec/installation.html | 可用 |
| Python 指南 | https://alexgarcia.xyz/sqlite-vec/python.html | 可用 |
| Node.js 指南 | https://alexgarcia.xyz/sqlite-vec/js.html | 可用 |
| Go/Rust/Ruby 指南 | 各语言独立页面 | 可用 |
| GitHub README | 含完整 SQL 示例 | 质量良好 |

**文档质量评价**：README 提供了清晰的安装和使用示例，官方文档站覆盖多语言入门，但标注为 WIP，深度内容（如性能调优、ANN 索引）尚不完善。

---

## 竞品清单

| 产品 | 类型 | 核心差异 |
|------|------|----------|
| **sqlite-vector**（sqlite.ai） | SQLite 扩展 | 更新的竞争者，声称插入快 50%，查询快 16%，量化后快 3-17 倍；仅 30MB 内存 |
| **pgvector** | PostgreSQL 扩展 | 服务端向量搜索，高并发性能优异，但需要 PostgreSQL |
| **Chroma** | 独立向量数据库 | 嵌入式优先设计，快速原型，但高并发下性能不稳 |
| **libSQL / Turso** | SQLite Fork | 内建向量搜索，无需扩展，自动索引更新 |
| **Vectorlite** | SQLite 扩展 | 类似 sqlite-vss，使用外部向量索引库 |
| **Milvus** | 专用向量数据库 | 企业级，分布式，规模化场景 |
| **Pinecone/Weaviate** | 云向量数据库 | 托管服务，无需自建 |

**sqlite-vec 的差异化优势**：
1. **零依赖纯 C**：不依赖 Faiss 等重型库，编译简单
2. **全平台覆盖**：从服务器到浏览器 WASM 到树莓派
3. **SQLite 原生 SQL 接口**：使用标准 SQL 操作向量
4. **嵌入式优先**：无需服务端，适合本地/边缘场景

**sqlite-vec 的不足**：
1. 目前仅支持暴力搜索（brute-force），ANN 索引仍在开发中（Issue #25）
2. 大数据集性能不如 sqlite-vector 和 pgvector
3. 项目曾有维护沉寂期，引发社区担忧

---

## 关键 Issue 信号

### 高讨论度 Issue（按评论数排序）

| # | 标题 | 评论 | 状态 | 信号 |
|---|------|------|------|------|
| #13 | Windows Python 扩展加载失败 | 22 | Open | 跨平台兼容性痛点 |
| **#226** | **项目半年未更新，是否弃坑？** | **19** | **Open** | **维护信任危机**（v0.1.7 回归后缓解） |
| #187 | SELECT WITH IN 语法问题 | 17 | Closed | SQL 兼容性 bug |
| **#25** | **ANN 近似最近邻索引跟踪** | **17** | **Open** | **核心功能缺失的长期跟踪** |
| #119 | Dart/Flutter 绑定 | 13 | Open | 移动端需求 |
| #45 | Windows 11 扩展加载失败 | 13 | Closed | Windows 兼容性 |
| #193 | .NET 支持 | 11 | Open | 生态需求 |
| #148 | ARM64 Linux 包缺失 | 10 | Open | 平台覆盖 |
| #96 | JOIN + LIMIT 不兼容 | 9 | Open | SQL 兼容性 |
| #127 | Upsert 支持 | 8 | Open | 功能需求 |

### 关键信号解读

1. **维护信任问题**（#226）：社区对项目维护连续性有疑虑，v0.1.7 的回归是重要信号
2. **ANN 索引是核心期待**（#25）：暴力搜索在大数据集上性能受限，社区强烈期待 ANN 支持
3. **跨平台问题突出**：Windows（#13, #45）和 ARM64 Linux（#148）是主要痛点
4. **SQL 兼容性**：虚拟表与标准 SQL 的交互边界是反复出现的问题

---

## 知识入口

| 入口 | URL | 价值 |
|------|-----|------|
| 官方文档 | https://alexgarcia.xyz/sqlite-vec/ | 安装与多语言入门 |
| DeepWiki | https://deepwiki.com 搜索 sqlite-vec | 有第三方集成架构文档 |
| LangChain 集成文档 | https://docs.langchain.com/oss/python/integrations/vectorstores/sqlitevec | Python RAG 集成 |
| Simon Willison TIL | https://til.simonwillison.net/sqlite/sqlite-vec | 混合搜索实践 |
| Mozilla 公告 | https://hacks.mozilla.org/2024/06/sponsoring-sqlite-vec-to-enable-more-powerful-local-ai-applications/ | 项目背景与愿景 |
| Hacker News 发布帖 | https://news.ycombinator.com/item?id=40243168 | 社区初始讨论 |
| Medium 教程 | https://medium.com/@stephenc211/how-sqlite-vec-works-for-storing-and-querying-vector-embeddings-165adeeeceea | 嵌入存储实践 |
| DEV.to 深度文章 | https://dev.to/aairom/embedded-intelligence-how-sqlite-vec-delivers-fast-local-vector-search-for-ai-3dpb | 架构分析 |
| 竞品对比 Issue | https://github.com/asg017/sqlite-vec/issues/94 | 官方对比讨论 |
| 向量搜索现状分析 | https://marcobambini.substack.com/p/the-state-of-vector-search-in-sqlite | 行业视角 |
| arxiv 相关论文 | https://arxiv.org/abs/2310.14021 | 向量数据库管理系统综述（无 sqlite-vec 专属论文） |

---

## 项目展示素材

### 一句话介绍
> 一个极小的、零依赖的向量搜索 SQLite 扩展，用纯 C 编写，可运行在任何 SQLite 支持的地方 -- 是 sqlite-vss 的精简继任者。

### 核心代码示例
```sql
-- 创建向量虚拟表
create virtual table vec_examples using vec0(
  sample_embedding float[8]
);

-- 插入向量数据（支持 JSON 或二进制格式）
insert into vec_examples(rowid, sample_embedding)
  values
    (1, '[-0.200, 0.250, 0.341, -0.211, 0.645, 0.935, -0.316, -0.924]'),
    (2, '[0.443, -0.501, 0.355, -0.771, 0.707, -0.708, -0.185, 0.362]');

-- KNN 查询
select rowid, distance
from vec_examples
where sample_embedding match '[0.890, 0.544, 0.825, 0.961, 0.358, 0.0196, 0.521, 0.175]'
order by distance
limit 2;
```

### 特色亮点
- 支持 float、int8、binary 三种向量类型
- 支持元数据列、辅助列、分区键列
- 向量可用 JSON 或紧凑二进制格式传入
- 跨 8 种语言/平台可用（Python/Node/Ruby/Go/Rust/Datasette/rqlite/sqlite-utils）
- Mozilla Builders 主赞助

---

## 快速判断

| 维度 | 评分 | 说明 |
|------|------|------|
| 技术质量 | ★★★★☆ | 零依赖纯 C 设计精巧，但缺 ANN 索引限制了大规模使用 |
| 社区活跃度 | ★★★☆☆ | Star 增长稳定但单人核心，曾有维护空窗期 |
| 实际采用 | ★★★★★ | npm + PyPI 月下载合计超 700 万，已是基础设施级别 |
| 生态整合 | ★★★★★ | Mozilla 赞助、LangChain 集成、8 种语言绑定 |
| 发展潜力 | ★★★★☆ | AI/RAG 持续驱动需求，ANN 索引落地将是关键转折点 |
| 维护可持续性 | ★★★☆☆ | 单人核心是风险点，但赞助支持 + 2026 年活跃回归是正面信号 |

### 总结判断

**sqlite-vec 是 SQLite 向量搜索领域事实上的标准扩展**，拥有 Mozilla 背书和月下载 700 万的惊人采用量。其零依赖、纯 C、全平台的设计哲学完美契合了 AI 时代「本地优先」的趋势。

**主要风险**：(1) 单人维护的 bus factor；(2) ANN 索引长期缺失使其在大数据集上竞争力不足；(3) 新竞争者 sqlite-vector 在性能上有明显优势。

**建议关注**：ANN 索引（Issue #25）的进展将决定项目能否从"够用的轻量方案"升级为"全面的向量搜索引擎"。v0.1.7 的回归和密集的 alpha 发布表明作者正在积极推进。

---

Sources:
- [Mozilla Builders 赞助公告](https://hacks.mozilla.org/2024/06/sponsoring-sqlite-vec-to-enable-more-powerful-local-ai-applications/)
- [sqlite-vec 官方文档](https://alexgarcia.xyz/sqlite-vec/)
- [LangChain SQLiteVec 集成](https://docs.langchain.com/oss/python/integrations/vectorstores/sqlitevec)
- [Simon Willison: 混合全文与向量搜索](https://simonwillison.net/2024/Oct/4/hybrid-full-text-search-and-vector-search-with-sqlite/)
- [The State of Vector Search in SQLite](https://marcobambini.substack.com/p/the-state-of-vector-search-in-sqlite)
- [sqlite-vector 竞品](https://www.sqlite.ai/sqlite-vector)
- [DEV.to: Embedded Intelligence](https://dev.to/aairom/embedded-intelligence-how-sqlite-vec-delivers-fast-local-vector-search-for-ai-3dpb)
- [Hacker News 讨论](https://news.ycombinator.com/item?id=40243168)
- [竞品对比 Issue #94](https://github.com/asg017/sqlite-vec/issues/94)
