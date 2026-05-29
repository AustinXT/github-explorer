# GitHub Trending 历史数据源研究报告

研究目标：获取过去 6 个月（2025年9月 ~ 2026年3月）GitHub trending 历史数据的可行数据源。

---

## 核心发现

GitHub 官方 trending 页面 (`https://github.com/trending`) **仅支持 daily / weekly / monthly 三个视图**，没有任何历史回溯功能，也没有公开 API。但社区中有多个项目通过 GitHub Actions 每日自动抓取并提交快照，形成了完整的历史归档。

---

## 第一梯队：推荐数据源（活跃维护 + 覆盖目标时间段）

### 1. duzhuoshanwai/github-trending-archive ★★★★★ 数据最丰富

- **URL**: https://github.com/duzhuoshanwai/github-trending-archive
- **数据时间范围**: 2024-07 ~ 2026-03（持续更新中）
- **格式**: Markdown（按日存储），但每条记录包含丰富的结构化字段
- **每条记录的字段**:
  - 仓库名 (owner/repo)
  - GitHub URL
  - 编程语言
  - **Star 数量**（绝对值）
  - **Fork 数量**（绝对值）
  - 描述
- **目录结构**: `data/YYYY-MM/YYYY-MM-DD.md`
- **维护状态**: 活跃（pushed_at: 2026-03-21），652 commits
- **覆盖完整度**: 覆盖目标时间段（2024-07 起）,但 2026-03 只到 03-03
- **优势**: 是唯一同时包含 stars/forks 数值和描述的 Markdown 归档
- **Stars**: 2

### 2. larsbijl/trending_archive ★★★★★ 历史最悠久

- **URL**: https://github.com/larsbijl/trending_archive
- **数据时间范围**: **2014年8月** ~ 2026年3月（超过11年！）
- **格式**: Markdown（按日存储）
- **每条记录的字段**:
  - 仓库名 (owner/repo)
  - GitHub URL
  - 描述
  - 按语言分类（python, go, c++, javascript, coffeescript）
- **目录结构**: `YYYY-MM/YYYY-MM-DD.md` + `YYYY-MM/YYYY-MM-DD_short.md`
- **维护状态**: 活跃（pushed_at: 2026-03-20），4,196 commits
- **覆盖完整度**: 完整覆盖目标时间段，且有十年以上历史
- **缺点**: 只覆盖 5 种语言；没有 stars/forks 数值
- **Stars**: 346

### 3. antonkomarev/github-trending-archive ★★★★☆ JSON格式 + 语言最全

- **URL**: https://github.com/antonkomarev/github-trending-archive
- **数据时间范围**: 2021 ~ 2026年3月
- **格式**: **JSON**（最适合程序化处理）
- **每条记录的字段**:
  - 日期
  - 语言
  - 仓库名列表（仅 owner/repo 列表，无 stars/forks/描述）
- **目录结构**: `archive/repository/YYYY/YYYY-MM-DD/{language}.json`
- **覆盖语言**: **31种**（C, C#, C++, Dart, Go, Haskell, Java, JavaScript, Kotlin, Lua, PHP, Python, R, Ruby, Rust, Scala, Shell, Swift, TypeScript, CSS, HTML, Markdown, Svelte, Vue, HCL, Makefile, WebAssembly 等）
- **同时归档 developer trending**: `archive/developer/YYYY/YYYY-MM-DD/{language}.json`
- **维护状态**: 活跃（pushed_at: 2026-03-21）
- **覆盖完整度**: 完整覆盖目标时间段
- **缺点**: JSON 中只有 repo 名列表，没有 stars/forks/description 等元数据
- **Stars**: 31

### 4. yangwenmai/github-trending-backup ★★★★☆ 中文社区最流行

- **URL**: https://github.com/yangwenmai/github-trending-backup
- **数据时间范围**: **2017** ~ 2026年3月
- **格式**: Markdown（按日存储）
- **每条记录的字段**:
  - 排名编号
  - 仓库名 (owner/repo)
  - GitHub URL
  - Stars/Forks 标注（格式 `(0s/0f)` -- 实测显示为0，可能是采集问题）
  - 描述
  - 按语言分类
- **目录结构**: `YYYY/MM/YYYY-MM-DD.md`（历史）或 `YYYY-MM-DD.md`（近期直接在根目录）
- **覆盖语言**: 21种（Go, Rust, Python, Ruby, C++, C, Java, Shell, Makefile, Swift, Objective-C, Kotlin, Jupyter-Notebook, HTML, JavaScript, TypeScript, CSS, Vue, TeX, Markdown）
- **维护状态**: 活跃（pushed_at: 2026-03-19），2,801 commits
- **覆盖完整度**: 完整覆盖目标时间段
- **缺点**: Stars/Forks 值似乎都是0，实际数值未被正确采集
- **Stars**: 437

### 5. bonfy/github-trending ★★★★☆

- **URL**: https://github.com/bonfy/github-trending
- **数据时间范围**: **2015** ~ 2026年3月
- **格式**: Markdown
- **每条记录的字段**:
  - 仓库名 (owner/repo)
  - GitHub URL
  - 描述
  - 按语言分类（Python, Swift, JavaScript, Go 等）
- **目录结构**: `YYYY/MM/YYYY-MM-DD.md` (历史) 或 `YYYY-MM-DD.md`（近期）
- **维护状态**: 活跃（pushed_at: 2026-03-21）
- **覆盖完整度**: 完整覆盖目标时间段
- **Stars**: 831

---

## 第二梯队：补充数据源

### 6. aneasystone/github-trending ★★★☆☆ 独特的月度汇总

- **URL**: https://github.com/aneasystone/github-trending
- **数据时间范围**: 2022-08 ~ 2025-10（archived 目录中按月汇总）
- **格式**: Markdown -- 按月汇总，记录每天新出现在 trending 的仓库
- **每条记录的字段**: 日期 + 仓库名 + URL + 描述
- **目录结构**: `archived/YYYY-MM.md`
- **特点**: 不是每日完整快照，而是只记录"新出现"的仓库（去重后的增量）
- **维护状态**: 活跃（pushed_at: 2026-03-21），1,291 commits
- **覆盖完整度**: 覆盖 2025-09 ~ 2025-10，但之后没有 archived 数据（最新数据在 README 中）
- **Stars**: 193

### 7. frodeaa/github_trending_archive ★★★☆☆

- **URL**: https://github.com/frodeaa/github_trending_archive
- **数据时间范围**: **2016-11** ~ 2026-03（近10年）
- **格式**: Markdown
- **每条记录的字段**: 仓库名 + URL + 描述，按语言分类
- **覆盖语言**: 5种（Go, Rust, Java, JavaScript, Python）
- **目录结构**: `archive/YYYY-MM/YYYY-MM-DD.md`
- **维护状态**: 活跃（pushed_at: 2026-03-20），3,444 commits
- **特点**: 同时提供 HTTP 访问（archive.faabli.com）
- **Stars**: 17

### 8. lxw15337674/github-trending-history ★★★☆☆

- **URL**: https://github.com/lxw15337674/github-trending-history
- **数据时间范围**: 2025-12 ~ 2026-03
- **格式**: TypeScript 项目 + Vercel 部署，带 API 端点
- **特点**: 不是纯数据归档，而是带 Web UI 和 API 的应用；使用 AI 生成摘要
- **维护状态**: 活跃（pushed_at: 2026-03-20）
- **Stars**: 5

---

## 第三梯队：API 和聚合平台

### 9. OSSInsight API ★★★☆☆

- **URL**: https://api.ossinsight.io/v1/trends/repos/
- **可用 period 参数**: `past_24_hours`, `past_week`, `past_month`, `past_3_months`（不支持 `past_6_months` 或 `past_year`）
- **返回字段**: repo_id, repo_name, primary_language, description, stars, forks, pull_requests, pushes, total_score, contributor_logins, collection_names
- **每次返回**: 100 条记录
- **特点**: 免费 API，数据丰富（包含 score 计算），但最长只支持 3 个月窗口
- **文档**: https://ossinsight.io/docs/api/list-trending-repos
- **底层**: 基于 GH Archive 事件数据 + TiDB 计算
- **缺点**: 无法获取3个月以前的快照；不是每日归档，而是当前滑动窗口

### 10. GH Archive + BigQuery ★★★★☆ 最强大但需要自行计算

- **URL**: https://www.gharchive.org/
- **BigQuery 公开数据集**: `githubarchive.day.YYYYMMDD`
- **数据时间范围**: 2011年至今
- **格式**: JSON（每小时一个 gzip 文件），也可通过 BigQuery SQL 查询
- **特点**:
  - 不直接记录 trending，但记录了所有 GitHub 事件（WatchEvent = star, ForkEvent, PushEvent 等）
  - 可以通过 SQL 查询重建"trending"：统计任意时间窗口内的 WatchEvent 增量
  - Google BigQuery 每月免费 1TB 查询额度
- **示例查询**:
  ```sql
  SELECT repo.name, COUNT(*) as stars
  FROM `githubarchive.day.2025*`
  WHERE type = 'WatchEvent'
    AND _TABLE_SUFFIX BETWEEN '0901' AND '0930'
  GROUP BY repo.name
  ORDER BY stars DESC
  LIMIT 100
  ```
- **优势**: 可自定义任意时间窗口和计算逻辑，数据最完整
- **缺点**: 需要写 SQL，需要 Google Cloud 账户，大规模查询可能产生费用

### 11. daily-stars-explorer ★★★☆☆ 单仓库深度分析

- **URL**: https://emanuelef.github.io/daily-stars-explorer/
- **GitHub**: https://github.com/emanuelef/daily-stars-explorer
- **特点**: Web 应用，可查看任意仓库的每日 star 增长历史
- **用途**: 不是 trending 归档，而是查看特定仓库的 star 趋势曲线
- **数据**: 通过 GitHub GraphQL API 实时查询
- **Stars**: 334

---

## 第四梯队：Kaggle 数据集

### 12. GitHub Daily Trending Repos (Kaggle)

- **URL**: https://www.kaggle.com/datasets/satoshiss/github-daily-trending-repos
- **格式**: CSV（ZIP 压缩，约 2.2MB）
- **最后更新**: 2025-10-02
- **许可证**: CC0 Public Domain
- **字段**: 包含 stars, forks, descriptions, 编程语言等
- **版本号**: 335（暗示 335 次更新，约每日一次）
- **缺点**: 2025年10月后不再更新，无法覆盖 2025-11 ~ 2026-03

### 13. GitHub Trending Repositories Dataset (2025) (Kaggle)

- **URL**: https://www.kaggle.com/datasets/mihikaajayjadhav/github-trending-repositories-dataset-2025
- **格式**: CSV（ZIP，约 94KB）
- **记录数**: 1,500+ 仓库
- **字段**: owner, repo_name, full_name, description, language, stars, forks, stars_period, contributors_count, url, search_language, timeframe, scraped_at
- **数据采集时间**: 2024年12月（一次性快照）
- **最后更新**: 2025-12-03
- **覆盖**: 30+ 编程语言，daily/weekly/monthly 三个维度
- **缺点**: 单次快照而非持续归档

---

## 已停更/不推荐的数据源

| 项目 | 原因 |
|------|------|
| `xiaobaiha/github-trending-history` | 2024-07 停更 |
| `anptgen/github-trending` | 2023-12 停更 |
| `mrcrypster/github-stars-stats` | 2023-04 归档，不再更新 |
| `ifyour/github-trending-archive` | 2022-11 停更 |
| `Leko/github-trending-archive` | 2025-02 停更 |
| `TommyZihao/Awesome` | 2023-08 停更 |
| `kujian/githubTrending` | 2025-02 停更 |

---

## github.com/trending 本身的历史能力

**结论：无历史回溯功能。**

- `https://github.com/trending` 只支持 `?since=daily|weekly|monthly` 参数
- 没有日期选择器，没有 `?date=2025-09-01` 这样的参数
- 页面仅展示当前时间点的 trending 快照
- 没有 RSS/Atom feed（但有第三方 RSS 生成器如 `mshibanami/GitHubTrendingRSS`）

---

## 推荐组合方案

针对"获取 2025年9月 ~ 2026年3月 完整 trending 历史数据"的目标：

### 方案 A：最快速（纯 Git 归档）

1. **首选**: `larsbijl/trending_archive` -- 覆盖全时间段，格式统一，11年数据
2. **补充**: `antonkomarev/github-trending-archive` -- JSON 格式 + 31种语言覆盖
3. **元数据补充**: 用归档中的 repo 名，通过 GitHub API 批量查询 stars/forks/description

### 方案 B：数据最丰富

1. **首选**: `duzhuoshanwai/github-trending-archive` -- 包含 stars/forks/description
2. **补充**: `yangwenmai/github-trending-backup` -- 21种语言覆盖
3. **对照**: `bonfy/github-trending` -- 作为数据校验源

### 方案 C：可编程查询（最灵活）

1. **GH Archive + BigQuery** -- 任意 SQL 查询任意时间窗口的 star 增量
2. **OSSInsight API** -- 免费 API 获取最近 3 个月的 trending 数据
3. **Git 归档** 补充 3 个月以前的数据

### 推荐实施策略

```
Step 1: Clone larsbijl/trending_archive 和 antonkomarev/github-trending-archive
Step 2: 解析 2025-09 到 2026-03 的每日文件
Step 3: 合并去重，得到时间段内所有曾登上 trending 的仓库列表
Step 4: 通过 GitHub API 批量补充元数据（stars, forks, topics, license 等）
Step 5: 可选：用 OSSInsight API 补充最近 3 个月的 score 数据
```

---

## 数据源完整对比

| 数据源 | 时间跨度 | 格式 | 含Stars | 含描述 | 语言覆盖 | 活跃 | 推荐度 |
|--------|---------|------|---------|--------|---------|------|--------|
| larsbijl/trending_archive | 2014~ | MD | - | 有 | 5种 | 是 | ★★★★★ |
| antonkomarev/github-trending-archive | 2021~ | JSON | - | - | 31种 | 是 | ★★★★☆ |
| duzhuoshanwai/github-trending-archive | 2024-07~ | MD | 有 | 有 | 多种 | 是 | ★★★★★ |
| yangwenmai/github-trending-backup | 2017~ | MD | (0) | 有 | 21种 | 是 | ★★★★☆ |
| bonfy/github-trending | 2015~ | MD | - | 有 | 多种 | 是 | ★★★★☆ |
| frodeaa/github_trending_archive | 2016~ | MD | - | 有 | 5种 | 是 | ★★★☆☆ |
| GH Archive + BigQuery | 2011~ | JSON/SQL | 可算 | - | 全部 | 是 | ★★★★☆ |
| OSSInsight API | ~3个月 | JSON API | 有 | 有 | 全部 | 是 | ★★★☆☆ |
| Kaggle (satoshiss) | ~2025-10 | CSV | 有 | 有 | 多种 | 否 | ★★☆☆☆ |
