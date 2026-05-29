# WiFi-DensePose 元分析笔记

## 代码统计 (tokei)
- **总文件数**: 1,078
- **总行数**: 771,099
- **代码行数**: 619,874
- **注释行数**: 91,080
- **空行**: 60,145

### 语言分布
| 语言 | 代码行数 | 文件数 |
|------|---------|--------|
| Rust | 108,522 (+ Markdown内嵌代码) | 385 |
| JSON | 395,033 | 27 |
| Python | 36,607 | 134 |
| JavaScript | 20,230 | 62 |
| Markdown | 53,647 (注释) | 204 |
| TSX | 10,502 | 63 |
| C | 5,408 | 21 |
| CSS | 4,605 | 5 |
| Shell | 3,531 | 14 |
| TypeScript | 3,142 | 59 |

## Git 提交历史
- **总提交数**: 316
- **首次提交**: 2025-06-07 "Initial commit"
- **最后提交**: 2026-03-20 "docs: add README for happiness-vector example"
- **项目生命周期**: ~9.5个月

### 提交频率（按月）
| 月份 | 提交数 |
|------|--------|
| 2025-06 | 17 |
| 2026-01 | 13 |
| 2026-02 | 78 |
| 2026-03 | 208 |

### 提交者统计
| 提交者 | 次数 |
|--------|------|
| ruv | 248 |
| Claude (AI) | 90 |
| rUv | 69 |
| github-actions[bot] | 61 |
| Reuven | 17 |
| fr4iser | 6 |
| Yossi Elkrief | 4 |
| Tuan Tran | 2 |

### 活跃时段
- 最活跃日: 2026-02-28 (78 commits)、2026-03-01 (68 commits)
- 最活跃时间段: 上午10-16时 (美东时区 -0400)
- 2月底到3月初有爆发式开发 (可能为 Rust 重写 & 功能冲刺)

## CI/CD
- 8个 GitHub Actions workflow:
  - ci.yml, cd.yml
  - desktop-release.yml
  - firmware-ci.yml, firmware-qemu.yml
  - security-scan.yml
  - update-submodules.yml
  - verify-pipeline.yml

## 版本历史
- v0.5.0-esp32 (2026-03-15): mmWave 传感器融合
- v0.4.3-esp32 (2026-03-15): 跌倒检测修复
- Python v1.2.0 (pyproject.toml)
- Rust workspace v0.3.0

## 依赖 / 子模块
- vendor/midstream
- vendor/ruvector (核心信号处理)
- vendor/sublinear-time-solver

## Claude Flow v3 集成
- 使用 @claude-flow/cli MCP 工具
- 配置了层级网格拓扑、最多15个agent
- Claude 是第二大贡献者（90次提交）
