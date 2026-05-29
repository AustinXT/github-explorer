# GitHub Trending 数据获取方案研究报告

## 1. GitHub 官方 Trending API -- 不存在

GitHub **没有提供官方的 Trending API 端点**。这一点已在 GitHub 社区讨论中得到确认（[Discussion #161519](https://github.com/orgs/community/discussions/161519)）。

GitHub 有意将 trending 和 explore 设计为 **仅限 UI 访问** 的视图，原因包括：
- 防止滥用和刷排名
- 保持动态排名逻辑的灵活性（算法不公开）
- CDN 优化考虑

GitHub REST API 文档（https://docs.github.com/en/rest）中没有任何 trending 相关端点。

### GitHub Trending 算法（已知信息）

GitHub 未公开具体算法，但社区分析推测考虑以下因素：
- **Star 增速**（最核心）：不是绝对数量，而是相对于历史平均值的增速
- **参与度指标**：Forks、Issues、PRs、Comments 等活跃度
- **时间权重**：星标获取时间可能有不同权重
- **语言归一化**：热门语言（如 JavaScript）需要更高阈值

---

## 2. 第三方解决方案

### 2.1 JavaScript/Node.js 生态

| 项目 | 方式 | 状态 | 备注 |
|------|------|------|------|
| **[@huchenme/github-trending-api](https://github.com/huchenme/github-trending-api)** | Cheerio 抓取 HTML | 已归档（archived） | 曾最流行；提供 `/repositories`、`/developers`、`/languages` 端点；API 曾托管在 ghapi.huchen.dev |
| **[trending-github](https://www.npmjs.com/package/github-trending)** | npm 包 | 不维护（最后更新 9 年前） | v1.0.3 |
| **[node-github-trend](https://github.com/rhysd/node-github-trend)** | 抓取 + GitHub API | 不维护（2018 年停更） | TypeScript 实现，可结合 API 获取增强数据 |
| **[GiTrends](https://github.com/maulikshetty/GiTrends)** | Node.js 后端 + Next.js 前端 | 较新 | 实时抓取 trending 页面 |

### 2.2 Python 生态

| 项目 | 方式 | 状态 | 备注 |
|------|------|------|------|
| **[gtrending](https://github.com/hedyhli/gtrending)** | BeautifulSoup 抓取 | 维护中（最后 release 2023-06） | 最成熟的 Python 方案；支持 repos/developers/languages |
| **[github-trending (PyPI)](https://pypi.org/project/github-trending/)** | 抓取 | 待确认 | PyPI 上可安装 |
| **[git-trend](https://github.com/manojkarthick/git-trend)** | CLI 工具 | 可用 | 支持 daily/weekly/monthly，JSON 输出 |

### 2.3 托管 API 服务

| 服务 | URL | 特点 |
|------|-----|------|
| **OSS Insight API** | `GET https://api.ossinsight.io/v1/trends/repos/?period=past_24_hours&language=All` | 免费；TiDB 支持；可选 period 和 language 参数 |
| **Apify GitHub Trending Scraper** | apify.com/plantane/github-trending-scraper | 商业平台上的托管抓取器 |
| **Trendshift** | trendshift.io | 第三方 trending 可视化平台 |

### 2.4 自建方案

**[OhNiceRepo](https://github.com/behnamazimi/ohnicerepo)** -- 使用 GitHub Search API 模拟 trending 的开源项目：
- React + TypeScript + Vite 前端
- Fastify + Cloudflare Workers 后端
- 使用多个 GitHub Personal Access Token 轮换
- Upstash Redis 做请求频率控制
- 核心思路：根据用户参数（日期范围 + 最低星标数 + 语言）构建 Search API 查询

---

## 3. 抓取 github.com/trending 页面

### 3.1 HTML 结构（2026年3月实测）

trending 页面是**服务端渲染的静态 HTML**，不需要 JavaScript 执行即可抓取。每个仓库包裹在 `<article class="Box-row">` 中。

关键 HTML 结构：

```
<article class="Box-row">
  ├── <h2 class="h3 lh-condensed">
  │     └── <a>
  │           ├── <span class="text-normal">{owner} /</span>
  │           └── {repo_name}
  │
  ├── <p class="col-9 color-fg-muted my-1 tmp-pr-4">
  │     └── {description}
  │
  └── <div class="f6 color-fg-muted mt-2">
        ├── <span class="repo-language-color" style="background-color: #xxx">
        ├── <span itemprop="programmingLanguage">{language}</span>
        ├── <a href="/{owner}/{repo}/stargazers">{total_stars}</a>
        ├── <a href="/{owner}/{repo}/forks">{total_forks}</a>
        ├── Built by {contributor_avatars}
        └── <span class="d-inline-block float-sm-right">
              {N} stars today/this week/this month
            </span>
</article>
```

### 3.2 每条记录暴露的数据字段

| 字段 | 示例 |
|------|------|
| 仓库全名 | `FujiwaraChoki/MoneyPrinterV2` |
| 描述 | `Automate the process of making money online.` |
| 编程语言 | `Python` |
| 语言颜色 | `#3572A5` |
| 总星标数 | `17,223` |
| 总 Fork 数 | `1,835` |
| 周期内新增星标 | `379 stars today` |
| 主要贡献者 | 头像 + 用户名链接 |
| Sponsor 链接 | 如果仓库作者可赞助 |

### 3.3 抓取注意事项

- **优势**：页面是 SSR（服务端渲染），无需 headless browser，普通 HTTP 请求 + HTML 解析即可
- **URL 模式**：`https://github.com/trending/{language}?since={daily|weekly|monthly}&spoken_language_code={code}`
- **风险**：HTML 结构可能随时变更（过去几年已有多次变更，导致抓取库失效）
- **反爬**：大量请求可能被 GitHub 限制；建议缓存结果（trending 页面更新频率约每小时一次）
- **推荐工具**：
  - Python: `requests` + `BeautifulSoup`
  - Node.js: `cheerio`（无需 Puppeteer）

---

## 4. GitHub Search API 模拟 Trending

### 4.1 核心方法

使用 `GET /search/repositories` 端点，通过 `created:` 日期范围 + `sort=stars` 排序模拟 trending 效果。

### 4.2 实用查询示例

```bash
# 过去 7 天内创建的、星标超过 50 的仓库，按星标排序
GET /search/repositories?q=created:>2026-03-15+stars:>50&sort=stars&order=desc&per_page=30

# 过去 14 天内的 Python 仓库，按星标排序
GET /search/repositories?q=created:>2026-03-08+language:python+stars:>100&sort=stars&order=desc

# 模拟 "本周热门"：过去 7 天创建 + 按星标降序
GET /search/repositories?q=created:>2026-03-15&sort=stars&order=desc&per_page=100

# 发现新兴仓库：最近 30 天创建 + 至少 10 星
GET /search/repositories?q=created:>2026-02-20+stars:>10&sort=stars&order=desc
```

### 4.3 可用查询限定符

| 限定符 | 说明 | 示例 |
|--------|------|------|
| `created:>YYYY-MM-DD` | 创建日期之后 | `created:>2026-03-15` |
| `pushed:>YYYY-MM-DD` | 最后推送之后 | `pushed:>2026-03-20` |
| `stars:>N` | 最低星标数 | `stars:>100` |
| `stars:N..M` | 星标范围 | `stars:50..500` |
| `forks:>N` | 最低 fork 数 | `forks:>10` |
| `language:X` | 编程语言 | `language:rust` |
| `topic:X` | 主题标签 | `topic:machine-learning` |

### 4.4 排序选项

| sort 参数 | 说明 |
|-----------|------|
| `stars` | 按星标数（最常用于模拟 trending） |
| `forks` | 按 fork 数 |
| `updated` | 按更新时间 |
| `help-wanted-issues` | 按需要帮助的 issue 数 |
| 不传 sort | 按 best match（GitHub 内部相关性算法） |

### 4.5 Search API 与真实 Trending 的差异

| 维度 | Search API 模拟 | 真实 Trending |
|------|-----------------|---------------|
| 排序依据 | 绝对星标数 | 星标增速（velocity） |
| 新仓库发现 | 可通过 `created:` 控制 | 自动包含各年龄段仓库 |
| 已有热门仓库 | 总是排在前面 | 只在有新增活跃度时出现 |
| 语言筛选 | 支持 | 支持 |
| 时间窗口 | 灵活自定义 | 仅 daily/weekly/monthly |
| 精确度 | 粗略近似 | GitHub 专有算法 |

### 4.6 实测结果

查询 `created:>2026-03-15+stars:>50&sort=stars&order=desc` 返回 243 条结果，例如：
- `HKUDS/ClawTeam` -- 2398 stars（2026-03-17 创建）
- `VoltAgent/awesome-codex-subagents` -- 1955 stars（2026-03-17 创建）

查询 `created:>2026-03-08+stars:>100&sort=stars&order=desc` 返回 436 条结果，例如：
- `garrytan/gstack` -- 34564 stars（2026-03-11 创建）

---

## 5. 速率限制

### 5.1 Search API 限制（最关键）

| 类型 | 限制 |
|------|------|
| **未认证请求** | **10 次/分钟**（实测确认） |
| **认证请求** | **30 次/分钟** |
| **结果上限** | 每次查询最多返回 **1,000 条**记录 |
| **每页上限** | `per_page` 最大 **100** |
| **查询长度** | 不超过 **256 字符**（不含操作符） |
| **布尔操作符** | 每次查询最多 **5 个** AND/OR/NOT |

### 5.2 通用 REST API 限制

| 类型 | 限制 |
|------|------|
| 未认证请求 | 60 次/小时 |
| 认证请求（Personal Access Token） | 5,000 次/小时 |
| GitHub Enterprise Cloud | 15,000 次/小时 |

### 5.3 二级速率限制（Secondary Rate Limits）

即使未超过主要限制，以下情况也会触发 403/429 错误：
- 并发请求不超过 **100 个**
- REST 端点不超过 **900 点/分钟**
- CPU 时间不超过 **90 秒/60 秒实际时间**
- 内容生成请求不超过 **80 次/分钟**

### 5.4 响应头

```
x-ratelimit-limit: 10          # 当前窗口允许的最大请求数
x-ratelimit-remaining: 7       # 剩余请求数
x-ratelimit-used: 3            # 已使用请求数
x-ratelimit-resource: search   # 所属限制类别
x-ratelimit-reset: 1774112170  # 重置时间（Unix 时间戳）
```

### 5.5 应对策略

1. **使用认证 Token**：从 10 次/分钟提升到 30 次/分钟
2. **Token 轮换**：像 OhNiceRepo 一样使用多个 PAT 轮换
3. **缓存结果**：trending 数据不需要实时更新，建议至少缓存 1 小时
4. **合并请求**：用 `per_page=100` 减少请求次数
5. **条件请求**：使用 `If-None-Match` / `If-Modified-Since` 头，304 响应不计入限制

---

## 6. 推荐方案对比

| 方案 | 优势 | 劣势 | 适用场景 |
|------|------|------|----------|
| **抓取 trending 页面** | 获取真实 trending 数据；包含 star velocity | HTML 结构可能变更；需维护解析器 | 需要与 GitHub trending 完全一致的数据 |
| **GitHub Search API** | 官方支持；稳定可靠；灵活的查询参数 | 只能近似 trending（按绝对星标排序，非增速）；30 次/分钟限制 | 自定义 trending 逻辑；不需要与官方 trending 完全一致 |
| **OSS Insight API** | 免费；专门为 trending 设计；无需管理 Token | 第三方依赖；可能下线 | 快速集成；对可靠性要求不极高 |
| **gtrending (Python)** | 开箱即用；维护较好 | 依赖 HTML 结构不变 | Python 项目快速集成 |
| **自建抓取 + Search API 混合** | 最灵活；可自定义权重和算法 | 开发维护成本高 | 需要深度定制的 trending 算法 |

---

## 7. 针对本项目的建议

对于 "GitHub 仓库探索技能" 项目，推荐 **混合方案**：

1. **主要数据源**：使用 **GitHub Search API** 模拟 trending
   - 构建灵活的查询：`created:>日期 + stars:>阈值 + language:语言`
   - 使用 `sort=stars` 排序
   - 好处：官方 API，稳定，不怕 HTML 变更

2. **补充数据源**：可选抓取 `github.com/trending`
   - 获取真实的 "stars today/this week" 增速数据
   - 使用简单的 HTTP + HTML 解析（无需 headless browser）

3. **缓存策略**：
   - trending 数据缓存 1-2 小时
   - 使用认证 Token，每分钟 30 次搜索请求足够覆盖多语言查询

4. **OSS Insight API** 作为备选，当 GitHub API 限流时可切换
