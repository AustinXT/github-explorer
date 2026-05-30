# oven-sh/bun — 元分析（Phase 2）

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 285.9 万行（不含空行/注释） |
| 语言分布 | Rust 25.3%, Zig 18.6%, TypeScript 18.5%, JavaScript 13.1%, C++ 7.7%, C 7.3%, C Header 2.1%, CSS 1.9%, 其他 5.5% |
| 代码/注释比 | 4.8:1 |
| 文件数量 | ~50,000+（含测试） |
| 依赖数量 | 0 runtime / 13 devDeps |

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 62 个月（首次提交 2021-04-17） |
| 总 commit 数 | 15,607 |
| 最近提交 | 2026-05-29 |
| 近 30 天 commit | 400 |
| 近 90 天 commit | 911 |
| 开发阶段 | 密集开发 |
| 开发模式 | 职业项目（周末占比 19.6%，深夜占比 36%） |

## 演化轨迹

### 核心文件（Top 10 最常修改）
1. `src/install/install.zig` — 631 次修改
2. `Makefile` — 544 次修改
3. `src/bun.js/bindings/ZigGlobalObject.cpp` — 518 次修改
4. `src/bun.js/api/server.zig` — 469 次修改
5. `src/bun.js/bindings/bindings.zig` — 463 次修改
6. `src/cli.zig` — 458 次修改
7. `src/js_ast.zig` — 434 次修改
8. `README.md` — 421 次修改
9. `src/bun.js/javascript.zig` — 413 次修改
10. `src/bun.js/bindings/bindings.cpp` — 407 次修改

### 热点目录
1. `packages/bun-uws` — 58,688 次修改（WebSocket/uSockets 底层库）
2. `src/bun.js` — 22,705 次修改（核心 JavaScript 运行时）
3. `test/js` — 13,853 次修改（JavaScript 测试套件）
4. `src/js` — 3,052 次修改（JS 解析器相关）
5. `src/install` — 2,792 次修改（包管理安装逻辑）
6. `src/javascript` — 2,531 次修改（JavaScript 引擎绑定）
7. `src/runtime` — 2,452 次修改（运行时）
8. `test/cli` — 2,292 次修改（CLI 测试）
9. `src/jsc` — 2,001 次修改（JavaScriptCore 绑定）
10. `src/cli` — 1,908 次修改（CLI 实现）

### Commit 类型分布
- Feature/Add: 2 (1%)
- Fix/Bug: 44 (22%)
- Refactor: 0 (0%)
- Docs: 1 (0.5%)
- Test: 5 (2.5%)
- Other: 148 (74%)

### 版本发布
- 最新版本: v1.3.14（日期 2026-05-13）
- 总 Release 数: 246
- 版本策略: 语义化版本（bun-v1.x.y 格式）

## 项目画像卡片

```
项目: oven-sh/bun
年龄: 62 个月  |  代码: 285.9 万行
总 commits: 15,607  |  贡献者: 10 人（核心）
开发阶段: 密集开发
开发模式: 职业项目（周末占比 19.6%，深夜占比 36%）
核心文件: install.zig, ZigGlobalObject.cpp, server.zig, bindings.zig, cli.zig, js_ast.zig
Release: v1.3.14 (共 246 个版本)
```