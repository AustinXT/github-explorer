## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 15,686（不含空行/注释） |
| 语言分布 | TypeScript 64.0%, JSON 32.3%, Shell 1.0%, JavaScript 0.9%, C 0.7%, Markdown 1.1% |
| 代码/注释比 | 6.7:1 |
| 文件数量 | 48 |
| 依赖数量 | 22（runtime: 6, dev: 16） |

**规模评价**：中小型项目。去除 JSON（主要是 package-lock.json 的 4,941 行），实际业务代码约 10,618 行，以 TypeScript 为绝对主力（10,037 行，占实际代码 94.5%）。代码/注释比 6.7:1 表明注释覆盖尚可，关键模块有解释性注释。C 代码（108 行）来自 vendor 目录的 seccomp 安全过滤器，Shell 脚本（154 行）用于构建 seccomp 二进制。

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 5 个月（首次提交 2025-10-20） |
| 总 commit 数 | 221 |
| 最近提交 | 2026-03-12 |
| 近 30 天 commit | 15 |
| 近 90 天 commit | 79 |
| 近 365 天 commit | 221（即全部提交） |
| 开发阶段 | 密集开发 → 稳定维护过渡期 |
| 开发模式 | 职业项目（周末占比 8.1%，深夜占比 13.1%） |

**节奏分析**：

- **月度分布**：2025-10 和 2025-11 各 54 次提交是密集开发期，2025-12 降至 34 次，2026-01 回升至 40 次，2026-02 降至 31 次，2026-03（截至12日）仅 8 次。整体呈逐步放缓趋势，从高速迭代进入稳定维护阶段。
- **时间分布**：提交集中在 13:00-20:00（太平洋时间工作时段），高峰在 15:00-17:00，典型的美国西海岸职业开发团队模式。
- **工作日偏好**：周四（55 次）和周五（42 次）提交最多，周六仅 3 次，符合职业项目特征。
- **贡献者结构**：21 位贡献者，David Dworken（60 次）和 ollie-anthropic（54 次）为核心维护者，两人合计占总提交的 51.6%，其余贡献者每人 1-5 次。

## 演化轨迹

### 核心文件（Top 10 最常修改）

1. `package.json` — 46 次修改
2. `package-lock.json` — 43 次修改
3. `src/sandbox/sandbox-manager.ts` — 36 次修改
4. `src/sandbox/linux-sandbox-utils.ts` — 34 次修改
5. `src/sandbox/macos-sandbox-utils.ts` — 29 次修改
6. `src/sandbox/sandbox-config.ts` — 17 次修改
7. `src/cli.ts` — 16 次修改
8. `src/sandbox/sandbox-utils.ts` — 15 次修改
9. `src/sandbox/generate-seccomp-filter.ts` — 15 次修改
10. `README.md` — 14 次修改

**解读**：排除包管理文件后，`sandbox-manager.ts`、`linux-sandbox-utils.ts`、`macos-sandbox-utils.ts` 是项目的三大核心文件，分别对应沙箱管理逻辑、Linux 沙箱实现和 macOS 沙箱实现。项目显然是一个跨平台的进程沙箱化工具。

### 热点目录

1. `src/sandbox` — 155 次修改
2. `test/sandbox` — 52 次修改
3. `src/utils` — 17 次修改
4. `src/cli.ts` — 16 次修改（顶层文件）
5. `.github/workflows` — 10 次修改
6. `src/index.ts` — 9 次修改
7. `vendor/seccomp-src` — 4 次修改
8. `vendor/seccomp` — 4 次修改
9. `test/utils` — 4 次修改
10. `test/config-validation.test.ts` — 4 次修改

**解读**：`src/sandbox` 以 155 次修改占绝对主导（占全部目录级修改的 ~55%），配合 `test/sandbox` 的 52 次修改，说明沙箱核心逻辑是持续迭代的重点，且有良好的测试覆盖意识。

### Commit 类型分布

- Feature/Add: 41 (18.6%)
- Fix/Bug: 38 (17.2%)
- Refactor: 0 (0%)
- Docs: 2 (0.9%)
- Test: 6 (2.7%)
- Other: 134 (60.6%)

**说明**："Other" 中大量是 Merge PR 提交（约 40+）、版本 bump（chore）、安全加固（security）、性能优化（perf）和 CI 相关提交。Feature 和 Fix 数量接近（41 vs 38），说明项目在快速添加功能的同时也在积极修复问题，符合早期快速迭代的特征。项目使用 Conventional Commits 约定（`feat:`, `fix:`, `chore:`, `ci:`, `security:`, `perf:` 等前缀），但不完全严格——部分提交未加前缀。

### 版本发布

- 最新版本: v0.0.42（2026-03-12）
- 总 Release 数: 5（GitHub Releases 上仅保留 v0.0.38-v0.0.42）
- 总 Tag 数: 5
- 版本策略: 语义化版本（0.0.x 补丁级递进），仍处于 0.x 阶段表示 API 尚未稳定

**说明**：从 commit 历史可以看到更早的版本（如 0.0.29、0.0.34、0.0.36、0.0.37），但仅有 v0.0.38 起才创建了 Git tag 和 GitHub Release。发布频率约每 1-2 周一个版本，节奏较快。

## 项目画像卡片

```
项目: anthropic-experimental/sandbox-runtime
年龄: 5 个月  |  代码: 10,037 行 (TypeScript)
总 commits: 221  |  贡献者: 21 人
开发阶段: 密集开发 → 稳定维护过渡期
开发模式: 职业项目（Anthropic 内部工具，周末 8.1%，深夜 13.1%）
核心文件: sandbox-manager.ts, linux-sandbox-utils.ts, macos-sandbox-utils.ts
Release: v0.0.42 (共 5 个正式版本)
```
