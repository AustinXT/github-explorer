# playcanvas/engine 元分析报告

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 232,953（不含空行/注释） |
| 语言分布 | JavaScript 89.3%, JSON 9.5%, GLSL 0.5%, CSS 0.4%, WGSL 0.1%, 其他 0.2% |
| 代码/注释比 | 3.2:1 |
| 文件数量 | 1,864 |
| 依赖数量 | 29（runtime: 2, dev: 27） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 173 个月 / ~14.4 年（首次提交 2011-10-24） |
| 总 commit 数 | 12,804 |
| 最近提交 | 2026-03-20 |
| 近 30 天 commit | 69 |
| 近 90 天 commit | 185 |
| 开发阶段 | 密集开发（近 3 个月月均 ~62 commit，持续 14 年的活跃项目） |
| 开发模式 | 职业项目（周末占比 7.2%，深夜占比 10.0%，工作时间高度集中在 10:00-18:00） |

## 演化轨迹

### 核心文件（Top 10 最常修改）

| 排名 | 文件 | 修改次数 |
|------|------|----------|
| 1 | src/scene/gsplat-unified/gsplat-manager.js | 56 |
| 2 | package.json | 42 |
| 3 | src/framework/components/gsplat/component.js | 39 |
| 4 | package-lock.json | 38 |
| 5 | src/scene/shader-lib/chunks-wgsl/chunks-wgsl.js | 36 |
| 6 | src/scene/gsplat/gsplat-resource-base.js | 31 |
| 7 | src/index.js | 29 |
| 8 | src/scene/shader-lib/wgsl/chunks/gsplat/frag/gsplatCopyToWorkbuffer.js | 28 |
| 9 | src/scene/gsplat/gsplat-sogs-data.js | 28 |
| 10 | src/scene/gsplat-unified/gsplat-octree-instance.js | 28 |

> 注：由于仓库使用了 partial clone，统计结果反映的是本地可达的 commit 历史范围内的修改频次。Gaussian Splatting（GSplat）相关文件占据热点，反映当前最活跃的开发方向。

### 热点目录

| 排名 | 目录 | 修改次数 |
|------|------|----------|
| 1 | src/scene | 1,351 |
| 2 | examples/assets | 831 |
| 3 | examples/src | 700 |
| 4 | src/extras | 224 |
| 5 | src/framework | 214 |
| 6 | src/platform | 184 |
| 7 | examples/thumbnails | 120 |
| 8 | scripts/esm | 87 |
| 9 | src/core | 55 |
| 10 | .github/workflows | 55 |

### Commit 类型分布（近 200 条）

| 类型 | 数量 | 占比 |
|------|------|------|
| 功能新增 (feat/add) | 39 | 19.5% |
| 缺陷修复 (fix/bug) | 65 | 32.5% |
| 重构 (refactor) | 7 | 3.5% |
| 文档 (doc) | 6 | 3.0% |
| 测试 (test) | 1 | 0.5% |
| 其他 | 82 | 41.0% |

> Fix 类 commit 占比最高（32.5%），说明项目处于功能完善与质量提升并重阶段。

### 版本发布

| 版本 | 发布日期 | 类型 |
|------|----------|------|
| v2.17.2 | 2026-03-19 | Latest |
| v2.17.1 | 2026-03-16 | Patch |
| v2.17.0 | 2026-03-06 | Minor |
| v2.16.2 | 2026-02-24 | Patch |
| v2.16.1 | 2026-02-04 | Patch |
| v2.16.0 | 2026-02-03 | Minor |
| v2.15.3 | 2026-01-28 | Patch |
| v2.15.2 | 2026-01-26 | Patch |
| v2.15.1 | 2026-01-12 | Patch |
| v2.15.0 | 2026-01-12 | Minor |

> 发布节奏：近 3 个月 10 次发布，约每周一次。Minor 版本约每月一次，Patch 版本频繁跟进。采用语义化版本管理，同时有 preview 预发布机制。

## 项目画像卡片

```
┌─────────────────────────────────────────────────────┐
│  playcanvas/engine                                  │
│  开源 WebGL/WebGPU 3D 游戏引擎                       │
├─────────────────────────────────────────────────────┤
│  📐 规模: 23 万行代码 | 1,864 文件 | 29 依赖         │
│  🗓️ 历史: 14.4 年 | 12,804 commits                  │
│  ⚡ 节奏: ~62 commits/月 | 每周发布                   │
│  🏢 模式: 职业项目（周末 7.2%，深夜 10.0%）           │
│  🔥 热点: Gaussian Splatting / 场景渲染 / 示例       │
│  📦 版本: v2.17.2（2026-03-19）                      │
│  🏷️ 阶段: 密集开发                                   │
│  🧬 语言: JavaScript 89.3% + GLSL/WGSL 着色器       │
└─────────────────────────────────────────────────────┘
```
