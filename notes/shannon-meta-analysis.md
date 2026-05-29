# Shannon 元分析笔记

## 代码统计

| 语言 | 文件数 | 代码行 | 注释行 | 空行 |
|------|--------|--------|--------|------|
| TypeScript | 63 | 6,755 | 1,840 | 1,238 |
| JSON | 524 | 16,377 | 0 | 511 |
| Markdown | 1,172 | 0 | 444,937 | 154,648 |
| Shell | 1 | 278 | 53 | 47 |
| Dockerfile | 1 | 95 | 41 | 25 |
| YAML | 3 | 115 | 11 | 12 |
| **总计** | **1,795** | **78,911** | **459,782** | **162,825** |

注：Markdown 中嵌入了大量代码（benchmark 结果、报告等），实际核心代码约 6,755 行 TypeScript。

## 关键文件行数

| 文件 | 行数 |
|------|------|
| src/temporal/workflows.ts | 495 |
| src/ai/claude-executor.ts | 433 |
| src/config-parser.ts | 562 |
| src/services/agent-execution.ts | 292 |
| src/session-manager.ts | 227 |

## 提交历史

- **总提交数**: 212
- **首次提交**: 2025-10-03 (Initial commit)
- **最近提交**: 2026-03-19 (docs: update announcement banner URL)
- **项目年龄**: ~5.5 个月

## 月度提交分布

| 月份 | 提交数 |
|------|--------|
| 2025-10 | 42 |
| 2025-11 | 32 |
| 2025-12 | 18 |
| 2026-01 | 24 |
| 2026-02 | 54 |
| 2026-03 | 42 |

## 提交者分布

| 作者 | 提交数 |
|------|--------|
| ajmallesh | 167 |
| ezl-keygraph | 73 |
| Arjun Malleswaran | 56 |
| keygraphVarun | 50 |
| Khaushik-keygraph | 20 |
| george-keygraph | 9 |
| nelliekeygraph | 1 |

注：ajmallesh 和 Arjun Malleswaran 可能是同一人（223 次提交），占总提交的 ~59%。

## 版本与发布

- 无 Git 标签
- 无正式 GitHub Release
- 最近通过 npx @keygraph/shannon 提供安装方式

## 开发节奏分析

- 项目于 2025 年 10 月开源，前两个月活跃
- 12 月放缓（假期），1 月恢复
- 2 月迎来最高峰（54 次提交），可能对应 XBOW benchmark 发布和重大功能迭代
- 3 月持续高活跃度
