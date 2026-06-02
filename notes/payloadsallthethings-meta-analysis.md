# payloadsallthethings — Phase 2 元分析

> 仓库: `swisskyrepo/payloadsallthethings`
> 维度: When & How Much（量化时间维度）
> 数据源: 本地 clone `/tmp/repo-miner-payloadsallthethings`

---

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 2,096 行（不含空行/注释，纯可执行代码） |
| 文档/Payload 行数 | 54,442 行（被 tokei 识别为 comments，实际是 payload/笔记/字典） |
| 空行 | 5,599 行 |
| 文件总数 | 447 个（其中 293 个被 tokei 识别为代码文件） |
| 代码 vs 注释比 | 1 : 26（注释/payload 远高于代码，符合 payload 字典型仓库特征） |
| 依赖数量 | 0（无 requirements.txt / pyproject.toml / package.json） |

### 语言分布（Top 10，按 code 行数）

| 语言 | 文件数 | Code | Comments | Blanks | 占比 |
|------|--------|------|----------|--------|------|
| Python | 10 | 1,280 | 77 | 150 | 61.1% |
| ASP.NET | 2 | 189 | 0 | 23 | 9.0% |
| XSL | 16 | 147 | 4 | 4 | 7.0% |
| SVG | 18 | 94 | 0 | 1 | 4.5% |
| XML | 10 | 81 | 0 | 1 | 3.9% |
| ASP | 2 | 74 | 78 | 14 | 3.5% |
| YAML | 2 | 73 | 10 | 8 | 3.5% |
| PHP | 14 | 63 | 4 | 17 | 3.0% |
| Ruby | 1 | 44 | 1 | 21 | 2.1% |
| CSS | 1 | 22 | 1 | 5 | 1.0% |
| HTML | 4 | 15 | 0 | 0 | 0.7% |
| **代码小计** | | **2,096** | | | |

### 文档载体（不被算作"代码"但占体积巨大）

| 载体 | 文件数 | 行数 | 性质 |
|------|--------|------|------|
| Markdown | 142 | 17,385 | 漏洞说明 + payload 速查 |
| Plain Text | 67 | 42,231 | payload 字典 / 巨型 fuzz 字典 |

> 解释：tokei 将 `.txt` 大字典识别为 "comments"，将 `.md` 内容识别为 "comments"。本质是 **payload 集合仓库** 而非传统软件项目，"代码" 仅占 3.4%，剩下 96.6% 是文档/字典。

---

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 116 个月（2016-10-18 → 2026-04-22，约 9 年 6 个月） |
| 总 commit 数 | 2,185 |
| 最近提交 | 2026-04-22 |
| 近 30 天 commit | 0（最近一次在 4 月，距今已 40+ 天） |
| 近 90 天 commit | 13 |
| 近 365 天 commit | 105 |
| 开发阶段 | **低维护/稳定维护**（年 commit ~100，无明显密集期，但仍在断续更新） |
| 开发模式 | **业余 Side Project** |

### 月度 commit 趋势（节选）

| 年份 | commits | 备注 |
|------|---------|------|
| 2016 (10-12月) | 37 | 启动 |
| 2017 | 73 | 稳态 |
| 2018 | 167 | 加速 |
| 2019 | 355 | **密集期** |
| 2020 | 380 | **密集期**（疫情年） |
| 2021 | 350 | 高活跃 |
| 2022 | 330 | 高活跃（10 月单月 107） |
| 2023 | 235 | 稳定维护 |
| 2024 | 165 | 缓慢下行 |
| 2025-2026 | 130 | 低维护，2025 全年 5+9+18+5+3+15+15+5+9+6+10 = 100 左右 |

> 规律：**每年 10 月有一个提交小高峰**（2021/10=125、2022/10=107、2024/11=75），疑似与年度安全会议（Hacktoberfest / 高校新学期）相关。

### 周中 vs 周末

| 日 | count | % |
|----|-------|---|
| 周一(1) | 344 | 15.7% |
| 周二(2) | 338 | 15.5% |
| 周三(3) | 380 | **17.4%** |
| 周四(4) | 273 | 12.5% |
| 周五(5) | 258 | 11.8% |
| 周六(6) | 255 | 11.7% |
| 周日(7) | 337 | **15.4%** |

- 工作日 (1-5): 1,593 = **72.9%**
- 周末 (6-7): 592 = **27.1%**
- 周日高于周六、接近周一 → 业余维护者（工作日 9-18 偏向高，但周日异常活跃）

### 24 小时分布（按提交数排序 Top 10）

| 小时 | count |
|------|-------|
| 11 | 160 |
| 18 | 158 |
| 12 | 148 |
| 14 | 146 |
| 23 | 145 |
| 17 | 143 |
| 22 | 140 |
| 16 | 138 |
| 09 | 136 |
| 21 | 131 |
| 10 | 131 |

- 早晨 8-12 点: 604 = 27.6%
- 下午 13-18 点: 819 = 37.5% ← **主峰**
- 晚上 19-23 点: 640 = 29.3%
- 深夜 00-07 点: 122 = 5.6%
- 凌晨 5 点仅 2 次 → 几乎不在深夜编码

> 综合判断：**典型的业余项目节奏** — 下午+晚上为主，凌晨极少，周日活跃高。**不像职业项目**（职业项目会集中在工作日 9-18 段且占比 60%+），但也并非纯深夜党。

---

## 演化轨迹

### 核心文件（Top 10 最常修改）

| # | 文件 | 修改次数 | 性质 |
|---|------|----------|------|
| 1 | `Methodology and Resources/Active Directory Attack.md` | 246 | 内网渗透方法论（核心） |
| 2 | `Methodology and Resources/Windows - Privilege Escalation.md` | 107 | Windows 提权速查 |
| 3 | `Server Side Template Injection/README.md` | 96 | SSTI payload |
| 4 | `XSS Injection/README.md` | 85 | XSS payload |
| 5 | `Server Side Request Forgery/README.md` | 80 | SSRF payload |
| 6 | `README.md` | 76 | 项目入口 |
| 7 | `Methodology and Resources/Reverse Shell Cheatsheet.md` | 67 | 反向 Shell 速查 |
| 8 | `XSS injection/README.md` | 64 | 注意大小写重复（历史遗留） |
| 9 | `Server Side Template Injection/Intruder/ssti.fuzz` | 62 | Burp fuzz 字典 |
| 10 | `Methodology and Resources/Linux - Privilege Escalation.md` | 52 | Linux 提权速查 |
| 11 | `XXE Injection/README.md` | 49 | XXE payload |
| 11 | `SQL Injection/README.md` | 49 | SQLi payload |
| 11 | `Methodology and Resources/Windows - Using credentials.md` | 49 | 凭据复用 |

### 热点目录

| 目录 | 修改次数 | 主题 |
|------|----------|------|
| `Methodology and Resources/` | 246+107+67+52+49+39+39 ≈ 700+ | 渗透方法论（最大热点） |
| `Server Side Template Injection/` | 96+62 ≈ 158+ | SSTI（含 fuzz 字典） |
| `XSS Injection/` / `XSS injection/` | 85+64 = 149 | XSS（**大小写重名目录**） |
| `Server Side Request Forgery/` | 80+ | SSRF |
| `SQL Injection/` | 49+ | SQLi |
| `Upload Insecure Files/` / `Upload insecure files/` / `Upload/` | 97+50+42 = 189 | 上传漏洞（**三个目录并存**） |
| `Methodology and Resources/Windows - Persistence.md` | 39 | Windows 持久化 |
| `Methodology and Resources/Network Pivoting Techniques.md` | 39 | 内网穿透 |

> **架构观察**：仓库按"漏洞类型"分目录，但存在目录重命名不规范问题（`XSS Injection` vs `XSS injection`，`Upload` vs `Upload Insecure Files` vs `Upload insecure files`），导致同一类目分散在 3 个目录中。

### Commit 类型分布（基于关键字匹配）

| 类型 | 数量 | 占比 |
|------|------|------|
| Feature/Add | 297 | 13.6% |
| Fix/Bug | 185 | 8.5% |
| Refactor | 9 | 0.4% |
| Docs | 25 | 1.1% |
| Test | 8 | 0.4% |
| Other（update/补 payload/不可分类） | 1,661 | 76.0% |
| **总计** | **2,185** | 100% |

> "Other" 比例异常高是因为大量提交信息为 "Update X.md" / "Added Y" / 简短英文短语不命中关键字。**Feature/Add:Fix 比例约 1.6:1**，符合内容仓库的常态（持续新增 payload > 修复）。

### 版本发布（Tag）

| Tag | 日期 | 距上次 |
|-----|------|--------|
| 1.0 | 2018-07-26 | — |
| 2.0 | 2018-11-17 | 4 个月 |
| 2.1 | 2019-07-05 | 8 个月 |
| 3.0 | 2022-06-30 | **3 年** |
| 4.0 | 2024-04-25 | 22 个月 |
| 4.1 | 2024-12-01 | 7 个月 |
| 4.2 | 2025-07-26 | 8 个月 |

- **总 Tag/Release 数**: 7（其中 v1.0 之前的 2016 commit 无 tag）
- **版本策略**: 主版本号 + 数字（**语义化版本粗略**）— 1.0 → 2.0 → 3.0 → 4.0 是大幅内容扩展，小版本 2.1/4.1/4.2 是增量补充
- 没有 GitHub Release（`gh release list` 无结果），仅 git tag
- **2026-04-22 的最近 commit 还未打新 tag**（可能 4.3 在路上，或已停止发版）

---

## 项目画像卡片

```
项目: swisskyrepo/payloadsallthethings
年龄: 116 个月（2016-10 → 2026-04，约 9.5 年）
代码: 2,096 行真代码 + 54,442 行 payload/字典 + 5,599 行空行
       主语言: Python (61%), 次: ASP.NET (9%), XSL (7%), SVG/XML/ASP/YAML/PHP/Ruby
       文档/字典占比 96%（内容仓库，非软件项目）
总 commits: 2,185
贡献者: 334 人（但 1341 个 commit 来自 Swissky 本人，占 61.4%；Top 5 占 72%）
         Swissky > p0dalirius(67) > ZANNI(50) > swisskyrepo(41) > nizam0906(22)
开发阶段: 稳定维护 → 缓慢下行（年 commit 从 380 降到 ~100，仍在更新）
开发模式: 业余 Side Project
         - 工作日 72.9% / 周末 27.1%
         - 下午 37.5% / 晚上 29.3% / 早晨 27.6% / 深夜 5.6%
         - 周日异常活跃 (15.4%)
核心文件: AD Attack / Win PrivEsc / SSTI / XSS / SSRF / Reverse Shell / SQLi
热点目录: Methodology and Resources/ (内网渗透)
          + 各漏洞类型目录（XSS/SSTI/SQLi/SSRF/File Inclusion）
Release: v4.2 (2025-07-26)，共 7 个 tag
         主版本节奏: 1.0→2.0→3.0→4.0 跨度 2-3 年
         小版本: 2.1/4.1/4.2 增量补内容
依赖: 0（纯内容仓库，无运行时依赖）
```

---

## 量化结论

1. **形态**: payload 字典 + 漏洞方法论 Wiki，不是软件项目。"代码" 仅是说明性 snippet（Python/HTML/PHP 等）。
2. **节奏**: 9.5 年长跑项目，2019-2022 是密集产出期（每年 330+ commits），2023 后进入稳定维护。最近 30 天 0 commits 属于"周期性沉寂"而非"已放弃"（历史上有 2024-02/2024-08/2025-04 等多个低活跃月份）。
3. **作者**: Swissky 一人主导 61% commit，334 人社区参与，典型的"作者驱动 + 社区 PR" 模式。
4. **方向**: 内网渗透（AD Attack / PrivEsc / Network Pivoting）是 2020 年后的主攻方向，占核心文件 60%+。
5. **架构债**: 存在目录重命名不规范（XSS / Upload 三种命名并存），但属于 Wiki 类项目的可接受代价。
6. **版本**: 1.0/2.0/3.0/4.0 是 4 个重大内容版本（1.x 起步 → 2.x 加入 SSRF/RCE → 3.x 大量内网方法论 → 4.x 现代化），平均每 2-3 年一次大版本。
