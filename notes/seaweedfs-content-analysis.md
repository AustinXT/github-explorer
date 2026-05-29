# SeaweedFS 内容分析笔记

## 项目架构

### 核心组件 (weed/ 目录)
SeaweedFS 是一个单二进制程序(`weed`)，通过子命令启动不同角色：

1. **Master Server** (`weed/server/master_server.go`, `weed/topology/`)
   - 管理 Volume 分配和拓扑
   - 使用 Raft 协议实现高可用
   - 维护 volume -> server 映射

2. **Volume Server** (`weed/storage/`, `weed/server/volume_server.go`)
   - 实际存储 blob 数据
   - 每个 Volume 32GB，包含大量 needle（blob）
   - 元数据仅 16 字节/文件，可全内存
   - 支持压缩、TTL、复制

3. **Filer** (`weed/filer/`, `weed/server/filer_server.go`)
   - 提供目录/文件层级结构
   - 无状态，线性可扩展
   - 支持 20+ 元数据后端（MySQL, Postgres, Redis, Cassandra, MongoDB, etc.）

4. **S3 API** (`weed/s3api/`)
   - Amazon S3 兼容 API
   - IAM、Bucket Policy、版本控制
   - 最近新增嵌入式 IAM 系统

5. **FUSE Mount** (`weed/mount/`)
   - POSIX 文件系统挂载
   - 跨平台支持（Linux, macOS, FreeBSD）

6. **Message Queue** (`weed/mq/`)
   - 内置消息队列（SeaweedMQ）
   - 支持 Kafka Gateway
   - SQL 查询能力

7. **Admin UI** (`weed/admin/`)
   - Web 管理界面（使用 templ 模板）
   - 插件系统管理
   - 最近开发最活跃的模块

8. **Plugin/Worker** (`weed/plugin/`, `weed/worker/`)
   - 可扩展任务系统
   - volume_balance, vacuum, erasure_coding, iceberg 等 handler

### 存储引擎结构 (weed/storage/)
- `store.go` - 存储主入口
- `volume.go` - Volume 管理
- `needle/` - Needle（blob）读写
- `needle_map/` - Needle 索引（内存/LevelDB/排序文件）
- `erasure_coding/` - 纠删码实现 (10.4 EC)
- `super_block/` - 超级块管理
- `backend/` - 存储后端抽象
- `idx/` - 索引文件格式

### 网络通信
- HTTP REST API（客户端访问）
- gRPC（内部通信，proto 文件在 weed/pb/）
- 支持 mTLS 安全通信

### 新兴功能（2025-2026 开发重点）
1. **Iceberg Tables** - Apache Iceberg 集成，支持 S3 Tables
2. **Admin UI + Plugin System** - Web 管理界面和任务调度
3. **RDMA Sidecar** - RDMA 网络加速（Rust 实现）
4. **Telemetry** - 遥测系统（Prometheus + Grafana）
5. **Helm Charts** - Kubernetes 部署增强
6. **结构化日志** - JSON 格式日志、gzip 压缩旋转

## 依赖分析 (go.mod)
### 核心依赖
- **gRPC**: google.golang.org/grpc v1.79.3
- **Protobuf**: google.golang.org/protobuf v1.36.11
- **Raft**: github.com/hashicorp/raft v1.7.3
- **S3 SDK**: github.com/aws/aws-sdk-go-v2
- **Iceberg**: github.com/apache/iceberg-go v0.5.0
- **FUSE**: github.com/seaweedfs/go-fuse/v2

### 元数据存储后端
- MySQL, PostgreSQL, SQLite
- Redis, MongoDB, Cassandra
- Elasticsearch, LevelDB, RocksDB
- etcd, TiKV, YDB
- HBase, FoundationDB, ArangoDB, Tarantool

### 云存储集成
- Google Cloud Storage, AWS S3
- Azure (via gocloud.dev)
- Backblaze B2 (via blazer)

### Go 版本
- go 1.25.0

## 设计理念
- 受 Facebook Haystack 论文启发
- O(1) 磁盘读取（每文件仅 40 字节开销）
- Master 只管 Volume（非文件），减轻中心节点压力
- 热数据本地 + 冷数据云端的分层存储
- 追加写入（append-only），对 SSD 友好
