# SeaweedFS 网络分析笔记

## 仓库基本信息
- **名称**: seaweedfs/seaweedfs
- **URL**: https://github.com/seaweedfs/seaweedfs
- **描述**: 分布式存储系统，支持对象存储(S3)、文件系统和 Iceberg 表，设计处理数十亿文件，O(1) 磁盘访问，轻松水平扩展
- **Stars**: 31,062 | **Forks**: 2,753 | **Watchers**: 531
- **License**: Apache-2.0
- **主语言**: Go (16M+ 行代码)
- **创建时间**: 2014-07-14
- **最近推送**: 2026-03-21
- **主页**: https://seaweedfs.com
- **Topics**: distributed-storage, distributed-systems, s3, hdfs, fuse, kubernetes, replication, object-storage, erasure-coding, blob-storage, cloud-drive

## 组织信息
- **组织**: SeaweedFS, San Francisco
- **公开仓库**: 17
- **关注者**: 290
- **创建时间**: 2015-04-16

## 社区健康度
- **健康分数**: 62%
- **有**: Code of Conduct, Issue Template, PR Template, License, README
- **缺少**: CONTRIBUTING.md

## 顶级贡献者
| 贡献者 | 提交数 |
|--------|--------|
| chrislusf (Chris Lu) | 9,018 |
| dependabot[bot] | 1,389 |
| kmlebedev | 526 |
| chrisluuber | 104 |
| proton-lisandro-pin | 88 |
| hilimd | 54 |
| LazyDBA247-Anyvision | 54 |
| bingoohuang | 46 |
| shichanglin5 | 45 |
| ryanrussell | 38 |

注：chrislusf 和 chrislu 是同一人 Chris Lu，合计贡献约 10,677 次提交，占总量 80%+

## 热门 Issues
1. #8147 - feat: Add S3 Tables support for Iceberg tabular data (9 comments, closed)
2. #7160 - S3 API: Advanced IAM System (31 comments, closed)
3. #7185 - Message Queue: Add sql querying (31 comments, closed)
4. #7178 - filer store: add foundationdb (31 comments, closed)
5. #8114 - migrate IAM policies to multi-file storage (6 comments, closed)

## 竞品分析
1. **MinIO** - 最知名的 S3 兼容存储，2025年停止开源社区版
2. **Ceph** - 统一存储平台（对象/块/文件），复杂但功能全面
3. **JuiceFS** - 分离数据和元数据的分布式文件系统
4. **Garage** - Rust 实现的轻量级 S3 兼容存储
5. **RustFS** - 新兴 Rust 实现，仍在 alpha 阶段
6. **GlusterFS** - 传统分布式文件系统
7. **MooseFS** - 适合大文件的分布式文件系统

SeaweedFS 在 MinIO 停止开源后成为最成熟的开源 S3 兼容替代品。
