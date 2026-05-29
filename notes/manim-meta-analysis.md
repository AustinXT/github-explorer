# 3b1b/manim 元分析报告

> 分析日期：2026-03-22

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 23,288（不含空行/注释） |
| 语言分布 | Python 84.3%, ReStructuredText 8.1%, YAML 3.7%, GLSL 3.4%, 其他 0.5% |
| 代码/注释比 | 19.3:1 |
| 文件数量 | 153 |
| 依赖数量 | 32（runtime，requirements.txt） |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 132 个月（首次提交 2015-03-22） |
| 总 commit 数 | 6,366 |
| 最近提交 | 2026-03-14 |
| 近 30 天 commit | 3 |
| 近 90 天 commit | 21 |
| 近 365 天 commit | 38 |
| 开发阶段 | 低维护（偶有集中突发开发，但整体节奏放缓） |
| 开发模式 | 业余 Side Project（周末占比 18.8%，深夜占比 11.1%） |

### 月度 Commit 密集期分析

项目经历了几个明显的密集开发期：

1. **2018-01 ~ 2018-05**（1,058 commits）：最密集的开发阶段，大规模重构和功能完善
2. **2019-01 ~ 2019-06**（661 commits）：持续高强度开发
3. **2021-01 ~ 2021-02**（454 commits）：ManimGL 重写期间
4. **2022-12 ~ 2023-01**（796 commits）：又一波集中开发
5. **2024-08 ~ 2024-12**（389 commits）：最近的活跃期

2025 年后 commit 频率显著降低，进入低维护状态。

### 工作时间模式

- 高频时段：10:00-17:00（工作时间集中），峰值在 11:00（549 commits）
- 深夜开发（22:00-06:00）占 11.1%，说明有一定比例的夜间编码习惯
- 周末占比 18.8%（略低于自然分布 28.6%），偏向工作日开发
- 整体模式：偏业余创作者/独立开发者模式，以工作时间段为主但无严格考勤

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. `manimlib/mobject/types/vectorized_mobject.py` — 439 次修改
2. `manimlib/mobject/mobject.py` — 419 次修改
3. `manimlib/scene/scene.py` — 273 次修改
4. `mobject/mobject.py` — 201 次修改（旧路径）
5. `scene/scene.py` — 178 次修改（旧路径）
6. `manimlib/camera/camera.py` — 169 次修改
7. `manimlib/mobject/svg/text_mobject.py` — 148 次修改
8. `manimlib/config.py` — 144 次修改
9. `manimlib/mobject/geometry.py` — 143 次修改
10. `manimlib/mobject/svg/svg_mobject.py` — 137 次修改

### 热点目录

1. `manimlib/mobject` — 2,439 次修改
2. `manimlib/shaders` — 636 次修改
3. `manimlib/scene` — 502 次修改
4. `manimlib/utils` — 477 次修改
5. `manimlib/animation` — 435 次修改
6. `from_3b1b/old` — 416 次修改
7. `active_projects/eop` — 347 次修改
8. `docs/source` — 339 次修改
9. `old_projects/eola` — 324 次修改
10. `old_projects/eoc` — 238 次修改

### Commit 类型分布（最近 200 条）

- Feature/Add: 22 (11.0%)
- Fix/Bug: 29 (14.5%)
- Refactor: 3 (1.5%)
- Doc: 1 (0.5%)
- Test: 0 (0.0%)
- 其他: 145 (72.5%)
- **总计**: 200

> 注：大量 commit 消息未遵循 conventional commit 规范，属于自由描述风格，因此"其他"类别占比较高。这与个人项目的开发习惯一致。

### 版本发布

- 最新版本: v1.7.2（2024-12-13）
- 总 Release 数: 13
- 总 Tag 数: 21
- 版本策略: 语义化版本（从 v0.1.x 到 v1.7.x，从 v1.0.0 起严格语义化）

## 项目画像卡片

```
项目: 3b1b/manim
年龄: 132 个月  |  代码: 23,288 行 (Python/GLSL)
总 commits: 6,366  |  贡献者: 207 人
开发阶段: 低维护（偶有突发活跃）
开发模式: 业余 Side Project（周末占比 18.8%，深夜占比 11.1%）
核心文件: vectorized_mobject.py, mobject.py, scene.py, camera.py
Release: v1.7.2 (共 13 个版本)
```
