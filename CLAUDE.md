# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

**GitHub 仓库探索技能**（repo-miner）：一个 Agent Skill，通过三阶段分析流程深度挖掘 GitHub 仓库的价值信息，产出结构化分析报告，用于公众号发布。

## 核心工作流

### 三阶段分析流程

每个仓库的分析分三个阶段，中间产物存放在 `notes/`（命名为 `{repo}-{phase}-analysis.md`）：

1. **Phase 1 — 网络分析（Network）**：作者背景、社区活跃度、增长趋势
2. **Phase 2 — 元分析（Meta）**：代码统计、提交历史、开发节奏
3. **Phase 3 — 内容分析（Content）**：架构解读、创新点、技术价值

最终合并为 `src/analysis_report/{username}_{repo_name}.md`。

### 常用命令

```bash
# 使用 repo-miner 技能分析单个仓库
/repo-miner <github_url>

# 批量并发分析（从仓库列表文件）
./batch_analyze.sh [repos_file] [start_line] [end_line] [concurrency]
# 例：./batch_analyze.sh docs/analysis_report/repos.md 1 0 8

# 解析 GitHub Trending 归档数据（需先克隆 github-trending-archive 到 /tmp）
python3 src/trending_repo/parse_trending.py

# 发布分析报告为公众号文章
/md2wechat <report_path>
```

## 项目结构

- **src/analysis_report/** — 最终分析报告（222+ 篇），命名 `{username}_{repo_name}.md`，部分有 `.html` 发布版
- **src/publish.md** — 公众号发布记录与待发布队列
- **src/starred_repo/** — GitHub 用户 Star 仓库分析
- **src/trending_repo/** — GitHub Trending 数据（daily/weekly/monthly JSON + 去重汇总）
- **notes/** — 分析过程中间产物（`{repo}-network-analysis.md`、`-meta-analysis.md`、`-content-analysis.md`）
- **notes/prompts/** — 提示词模板
- **tmp/** — 临时文件（已 gitignore）
- **batch_analyze.sh** — 批量分析脚本，使用信号量控制并发

## 规则

- 文档使用中文，文件名使用英文
- 不自动提交，除非用户明确要求
- 敏感信息存 `.env.local`，不入 Git
- 分析报告中使用直角引号「」而非""
