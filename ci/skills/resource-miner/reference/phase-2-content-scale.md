# Phase 2 — 内容规模与策展元分析（替换 repo-miner 的代码元分析）

**目标**：把「这个资源仓库有多大、长什么结构、更新有多勤、是不是自动化运维」量化出来。
**关键认知**：资源仓库的 tokei 代码行接近 0 是**正常**，不是「已放弃」。真信号是**内容规模 +
更新节奏 + 自动化签名 + 贡献集中度**。

**输入变量**：LOCAL_PATH / FULL_NAME / FACTS_JSON

**先做**：`Read FACTS_JSON`，读 `content_scale` / `update_rhythm` / `evolution` / `contributors`。
确定性指标已采好，本阶段做**解读与判断**，必要时用 `commands-cheatsheet.md` 的命令补查细节。

## 2.1 内容规模（读 `content_scale`）
- `total_human`（仓库体积）/ `file_count` / `main_ext`（主体文件类型）/ `ext_histogram`（文件类型直方图）
- `top_dirs`：**顶层目录即分类** —— 资源仓库的目录结构就是它的策展分类法，逐一解读每个顶层目录代表的内容类别与规模
- `markdown_files` / `total_link_count`：markdown 文件数与全仓外链总数
- `readme`：`bytes`（README 体量）/ `heading_count` / `h2_count` / `has_toc` / `link_count` / `list_link_items`
- **产出「内容规模」一句话**（填进项目画像 `代码行数` 行）：如 `1300 条目 / 42 个 md 文件 / 1.2MB`，或 `14GB（181 epub + 154 pdf），仅 1 个 91 字节 CSS 是真代码`

## 2.2 更新节奏（读 `update_rhythm`）
- `dev_stage`（密集开发/稳定维护/低维护/已放弃 → 资源语义映射为 活跃更新/稳定运维/低维护/已停滞）
- `age_months`（项目年龄）/ `total_commits` / `commits_last_30/90/365` / `monthly_distribution`
- 判断：更新是否**规律**（每周/每月固定）？近期是否仍在更新（时效性资源停更=价值快速衰减）？

## 2.3 自动化签名（读 `update_rhythm.automation_signature`）—— 资源类核心指标
- `signature`（高/中/低）+ `top_minute_bucket`（最密集的「星期 + 时:分」）+ `top_minute_share` + `distinct_minute_buckets` + `sample`
- **解读**：提交时刻是否精确到分钟级聚集（如「经济学人永远周五 21:20」）→ 背后是 **cron-driven 自动化流水线**（采集→格式转换→git commit→push）。这是「时钟式自动化策展」的铁证，也是最值得读者偷的运营模式
- 若 `signature=低` 但更新规律 → 可能是人工但纪律性强；据 `monthly_distribution` 与 `top_minute` 综合判断，诚实给结论

## 2.4 贡献集中度（读 `contributors`）
- `count` / `top`（Top 10）/ `top_author_share_pct` / `collaboration`（单人主导/核心少数+社区）
- 资源仓库多为**关键人依赖**（单人 100%）→ Bus Factor 风险，写进「风险与不足」

## 2.5 内容结构与导航质量（读 `content_scale.readme` + cheatsheet 补查）
- README 是否承担「目录/导航」职责（`has_toc`、大量章节）？还是极简只列文件？
- （awesome）外链规模 `total_link_count` 与失效信号：用 cheatsheet 抽样几条外链状态，估失效率（覆盖度治理的关键质量轴）
- 分类逻辑是否清晰（顶层目录命名规范、按主题/年份/期号组织）

## 返回格式（结构化摘要，回主对话）

```
### Phase 2 内容规模与策展元分析摘要

**内容规模一句话**(填项目画像 代码行数 行): [N 条目/M 文件/X 体积（主体类型）]
**内容结构**: [顶层目录分类法解读 + 导航/TOC 质量]
**更新节奏**(填 开发阶段 行): [活跃更新/稳定运维/低维护/已停滞 + 规律性 + 近期是否在更]
**自动化签名**: [高/中/低 + top_minute + 是否 cron 驱动的判断]
**贡献集中度**(填 贡献模式 行): [独立运营/小团队/社区 + 主作者占比 + Bus Factor]
**覆盖与失效**(awesome 适用): [外链总数 + 抽样失效率估计]
**项目年龄**(填 项目年龄 行): X 个月（YYYY-MM ~ YYYY-MM）
```
