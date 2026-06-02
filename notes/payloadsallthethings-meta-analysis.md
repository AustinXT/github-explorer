# payloadsallthethings — Phase 2 元分析

> 仓库: `swisskyrepo/payloadsallthethings`
> 维度: When & How Much（量化时间维度）
> 数据源: 本地 clone `/tmp/repo-miner-payloadsallthethings`
> 分析时点: 2026-04-22（HEAD 提交时间）

---

## 代码规模

| 指标 | 数据 |
|------|------|
| 总代码行数 | 2,096 行（不含空行/注释，纯可执行代码） |
| 文档/Payload 行数 | 54,442 行（被 tokei 识别为 comments，实际是 payload/笔记/字典） |
| 空行 | 5,599 行 |
| 文件总数 | 447 个（其中 293 个被 tokei 识别为代码文件） |
| Markdown 注释行（md 内嵌 payload） | 12,089 |
| Markdown 文件总行 | 21,527（142 个文件，平均 151 行） |
| 仓库总占用（含 .git） | 14 MB（剔除 .git 约 3 MB） |
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

### Markdown 内嵌代码语言分布（tokei 统计的 md 内嵌代码）

| 内嵌语言 | 代码行 |
|----------|--------|
| PowerShell | 763 |
| XML | 539 |
| SQL | 443 |
| JavaScript | 409 |
| PHP | 334 |
| Python | 336 |
| HTML | 346 |
| Java | 117 |
| BASH | 82 |
| YAML | 75 |
| INI | 9 |
| 其他 (CSS/Erlang/Groovy/Handlebars/Ruby/TeX/Twig/SVG) | 138 |

> PowerShell 高达 763 行 — 与 AD/Windows 攻击主题一致；SQL 443 + JavaScript 409 + PHP 334 是 Web 漏洞演示主战场。

### 文档载体（不被算作"代码"但占体积巨大）

| 载体 | 文件数 | 行数 | 性质 |
|------|--------|------|------|
| Markdown | 142 | 17,385 (含内嵌) / 21,527 (含 frontmatter) | 漏洞说明 + payload 速查 |
| Plain Text | 67 | 42,231 | payload 字典 / 巨型 fuzz 字典 |

> 解释：tokei 将 `.txt` 大字典识别为 "comments"，将 `.md` 内容识别为 "comments"。本质是 **payload 集合仓库** 而非传统软件项目，"代码" 仅占 3.4%，剩下 96.6% 是文档/字典。

### 文件类型 Top 20

```
  142 .md     ← 文档主体
   67 .txt    ← Burp Intruder fuzz 字典
   33 .png    ← README 配图
   27 .jpg    ← 截图
   18 .svg    ← 矢量图
   15 .xsl    ← XSLT payload
   14 .zip    ← 样本压缩包
   14 .php    ← PHP payload
   10 .xml    ← XXE payload
   10 .py     ← 工具脚本
    4 .yml    ← mkdocs 配置
    4 .html   ← XSS 演示
    2 .phar / .phpt / .phtml / .pht / .php3-7  ← PHP 多版本扩展
    2 .swf / .avi / .mp4  ← 媒体上传测试文件
```

### 顶层攻击类别（66 个目录）

`Upload Insecure Files/` 与 `Methodology and Resources/` 是仓库中体积与活跃度的双核心：

- **Upload Insecure Files/**：3.4 MB，116 个文件，含 16 个子目录（CVE FFmpeg HLS / CVE ZIP Symbolic Link / Configuration Apache .htaccess / EICAR / Extension ASP / Extension HTML / Extension PHP / Images / Jetty RCE / Picture Compression / Picture ImageMagick / Picture Metadata / Server Side Include 等）
- **Methodology and Resources/**：172 KB，但累计被修改 941 次（最高）
- **Directory Traversal/**：2.0 MB
- **Server Side Request Forgery/**：1.1 MB
- **SQL Injection/**：1.1 MB
- **Server Side Template Injection/**：976 KB
- **XSS Injection/**：668 KB
- **API Key Leaks/**：636 KB
- **File Inclusion/**：608 KB
- **Cross-Site Request Forgery/**：428 KB

类别谱系（节选）：

```
注入类    XSS / SQL / NoSQL / LDAP / XPATH / CSV / CSS / LaTeX / CRLF / SSTI / SSI / XSLT / XXE / Prompt
协议类    SSRF / Request Smuggling / CORS / WebSocket / XS-Leak / HPP / SAML / JWT
认证类    Account Takeover / OAuth Misconfiguration / JWT / 2FA Bypass
逻辑类    Business Logic Errors / Race Condition / Mass Assignment / IDOR / Type Juggling
文件类    File Inclusion / Directory Traversal / Upload Insecure Files / Zip Slip
服务类    Denial of Service / DNS Rebinding / Reverse Proxy Misconfigurations / Virtual Hosts
反序列化  Insecure Deserialization / Java RMI / ORM Leak
云/凭据   API Key Leaks / Dependency Confusion / Insecure Source Code Management
方法论    Methodology and Resources（含 AD/Windows/Linux 提权、Reverse Shell、Pivoting、AWS Pentest）
辅助      _LEARNING_AND_SOCIALS / _template_vuln（贡献模板与教程导航）
```

### 最长的 10 个 Markdown 文件

| 文件 | 行数 |
|------|------|
| `SQL Injection/MySQL Injection.md` | 775 |
| `XXE Injection/README.md` | 688 |
| `XSS Injection/README.md` | 609 |
| `SQL Injection/README.md` | 596 |
| `XSS Injection/1 - XSS Filter Bypass.md` | 578 |
| `JSON Web Token/README.md` | 541 |
| `Server Side Template Injection/Java.md` | 525 |
| `GraphQL Injection/README.md` | 495 |
| `Command Injection/README.md` | 476 |
| `Server Side Template Injection/Python.md` | 466 |

### CI / 工程化

- `.github/workflows/check-markdown.yml`：markdownlint 自动校验
- `.github/workflows/mkdocs-build.yml`：mkdocs 部署到 GitHub Pages（构建 `PayloadsAllTheThingsWeb`）
- `mkdocs.yml` + `custom.css`：Material 主题站点配置
- `CONTRIBUTING.md`、`DISCLAIMER.md`、`LICENSE`（MIT）

---

## 开发节奏

| 指标 | 数据 |
|------|------|
| 项目年龄 | 116 个月（2016-10-18 → 2026-04-22，约 9 年 6 个月） |
| 总 commit 数 | 2,185 |
| 贡献者总数 | 333（Swissky 一人 1,341 占 61.4%） |
| 最近提交 | 2026-04-22 |
| 近 30 天 commit | 9 |
| 近 90 天 commit | 28 |
| 近 365 天 commit | 105 |
| 开发阶段 | **稳定维护**（年 commit ~100，无明显密集期，但仍在持续更新） |
| 开发模式 | **核心驱动 + 社区补充**（主作者 1 人 + 332 协作者） |

### 年度 commit 趋势

| 年份 | commits | 备注 |
|------|---------|------|
| 2016 (10-12月) | 37 | 启动 |
| 2017 | 73 | 稳态 |
| 2018 | 149 | 加速（v1.0 + v2.0 发布年） |
| 2019 | **320** | **密集期**（10 月单月 73） |
| 2020 | **402** | **密集期**（疫情年，10 月 84） |
| 2021 | 346 | 高活跃（10 月单月 125 — 历史最高） |
| 2022 | 331 | 高活跃（10 月单月 107） |
| 2023 | 227 | 稳定维护 |
| 2024 | 157 | 缓慢下行（11 月 75 异常高） |
| 2025 | 98 | 低维护但仍持续 |
| 2026 (1-4 月) | 45 | 截至 4 月 22 日 |

> **规律**：每年 10 月（Hacktoberfest）出现显著提交高峰，单月可贡献全年 1/4+ 提交。年度峰值 2020（402），近三年回归到 ~100 量级。

### 最近 12 个月逐月分布

```
2025-05  3   2025-06  0   2025-07 15   2025-08 15
2025-09  5   2025-10  9   2025-11  6   2025-12 10
2026-01 17   2026-02  7   2026-03 12   2026-04  9
```

无任何月度完全停摆（除 2025-06 紧邻月份 15 次补偿），活跃度健康。

### 周内分布

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
- 周末 (6-7): 592 = **27.1%**（高于多数开源项目，业余性质明显）
- 周三最高、周日次高、周五最低

### 24 小时分布（按提交数排序 Top 10）

| 小时 | count |
|------|-------|
| 15 | 157 |
| 16 | 154 |
| 17 | 144 |
| 11 | 133 |
| 12 | 133 |
| 10 | 131 |
| 09 | 128 |
| 14 | 123 |
| 20 | 127 |
| 21 | 113 |

- 早晨 8-12 点: 629 = 28.8%
- 下午 13-18 点: 804 = 36.8% ← **主峰**
- 晚上 19-23 点: 519 = 23.7%
- 深夜 00-07 点: 233 = 10.7%
- 凌晨 5 点仅 17 次 → 几乎不在深夜编码

> 综合判断：**典型的业余 Side Project 节奏** — 下午+晚上为主，凌晨极少，周日活跃高。不像职业项目（职业项目会集中在工作日 9-18 段且占比 60%+），但也并非纯深夜党。

### 主作者 Swissky 年度贡献

| 年份 | Swissky 提交 |
|------|--------------|
| 2017 | 65 |
| 2018 | 125 |
| 2019 | 216 |
| 2020 | 233 |
| 2021 | 148 |
| 2022 | 188 |
| 2023 | 151 |
| 2024 | 120 |
| 2025 | 63 |
| 2026 | 32 |

> 9 个完整年度连续产出，无任何年度完全沉默。

### Commit 类型分布（全部 2,185 次）

| 类型 | 数量 | 占比 |
|------|------|------|
| Feature/Add | 297 | 13.6% |
| Fix/Bug | 185 | 8.5% |
| Refactor | 9 | 0.4% |
| Docs | 25 | 1.1% |
| Test | 8 | 0.4% |
| Other（update/补 payload/不可分类/merge/lint） | 1,661 | 76.0% |

> "Other" 比例高主要因为大量提交为 `Update X.md` / `Fix markdown linting` / `Archive external reference links` / `Merge pull request #XXX` / 简短英文短语。**Feature/Add : Fix ≈ 1.6 : 1**，符合内容仓库常态。

### 最近 300 次 commit 类型分布

| 类型 | 次数 | 占比 |
|------|------|------|
| 其他 | 219 | 73.0% |
| Fixes | 43 | 14.3% |
| Features | 29 | 9.7% |
| Docs | 8 | 2.7% |
| Refactor / Test | 各 1 | 0.3% |

最近窗口 features 占比下降、fixes 上升 → 印证「成熟期维护为重」。

---

## 演化轨迹

### 核心文件（Top 14 最常修改）

| # | 文件 | 修改次数 | 性质 |
|---|------|----------|------|
| 1 | `Methodology and Resources/Active Directory Attack.md` | 246 | 内网渗透方法论（绝对核心） |
| 2 | `Methodology and Resources/Windows - Privilege Escalation.md` | 107 | Windows 提权速查 |
| 3 | `Server Side Template Injection/README.md` | 96 | SSTI payload 字典 |
| 4 | `XSS Injection/README.md` | 85 | XSS 总目录 |
| 5 | `Server Side Request Forgery/README.md` | 80 | SSRF 协议/服务绕过 |
| 6 | `README.md` | 76 | 项目入口 |
| 7 | `Methodology and Resources/Reverse Shell Cheatsheet.md` | 67 | 反向 Shell（多语言/多协议） |
| 8 | `XSS injection/README.md` | 64 | 注意大小写重复（历史遗留） |
| 9 | `Server Side Template Injection/Intruder/ssti.fuzz` | 62 | Burp Intruder fuzz 字典 |
| 10 | `Methodology and Resources/Linux - Privilege Escalation.md` | 52 | Linux 提权速查 |
| 11 | `XXE Injection/README.md` | 49 | XXE 协议/绕过 |
| 11 | `SQL Injection/README.md` | 49 | SQLi 总目录 |
| 11 | `Methodology and Resources/Windows - Using credentials.md` | 49 | 凭据复用 |

> **核心特征**：「Methodology and Resources」章节合计修改 ~941 次，是仓库的心脏；AD/Windows 提权主题累计修改次数超过 350 次，反映 2020 年后「内网渗透」是仓库主攻方向。

### 热点目录（累计修改次数）

| 目录 | 修改次数 | 主题 |
|------|----------|------|
| `Methodology and Resources/` | 941 | 渗透方法论（最大热点） |
| `Upload Insecure Files/`（含历史 `Upload insecure files` / `Upload`） | 330+265+70 = **665** | 文件上传漏洞（**三种命名并存**） |
| `SQL Injection/`（含 `SQL injection`） | 260+149 = **409** | SQL 注入 |
| `XSS Injection/`（含 `XSS injection`） | 187+128 = **315** | XSS（**大小写重名目录**） |
| `Server Side Template Injection/` | 262 | SSTI（含 fuzz 字典） |
| `Server Side Request Forgery/` | 111 | SSRF |
| `Insecure Deserialization/` | 110 | 反序列化 |
| `CVE Exploits/` | 106 | CVE 案例 |
| `File Inclusion/`（含历史 `File Inclusion - Path Traversal`） | 87+42 = **129** | 文件包含 |
| `XXE Injection/` | 58 | XXE |
| `SSRF injection/`（旧大小写） | 52 | SSRF |
| `Command Injection/` | 45 | 命令注入 |
| `Insecure Source Code Management/` | 43 | 源码泄露 |
| `API Key Leaks/` | 42 | API Key 泄露 |
| `GraphQL Injection/` | 39 | GraphQL |
| `Directory Traversal/` | 36 | 目录遍历 |
| `JSON Web Token/` | 31 | JWT |
| `Web Sockets/` | 29 | WebSocket |
| `CORS Misconfiguration/` | 28 | CORS |
| `AWS Amazon Bucket S3/` | 28 | S3 桶（已合并到 API Key Leaks） |
| `XSLT Injection/` | 27 | XSLT |
| `Cross-Site Request Forgery/` | 22 | CSRF |

> **架构债**：仓库按漏洞类型分目录，但存在目录重命名不规范问题（`XSS Injection` vs `XSS injection`、`Upload` vs `Upload Insecure Files` vs `Upload insecure files`），导致同一类目分散在 3 个目录中。属于 Wiki 类项目的可接受代价，但反映 v2 → v3 重构期的不完全迁移。

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
- 4.x 系列节奏明显加快（4.0 → 4.1 → 4.2 间隔 7-8 个月），与 Hacktoberfest 周期吻合

### 演化阶段判断

| 阶段 | 时段 | 特征 |
|------|------|------|
| **冷启动期** | 2016-Q4 - 2017 | 37+73 commit，建立基本目录骨架 |
| **稳定建设期** | 2018-2019 | 149+320 commit，v1.0 → v2.1 三大版本发布 |
| **爆发增长期** | 2020-2022 | 402+346+331 commit，Hacktoberfest 单月突破 100+ |
| **结构性重构期** | 2022-2024 | v3.0（2022-06）大规模目录整理，v4.0（2024-04）展示系统升级 |
| **质量维护期** | 2024-至今 | 提交频次降低（157 → 98 → 45），重心转向「链接归档、引用规范、markdown lint」 |

### 近期典型提交样本

```
Update reference date, fix format
Normalize commands, callbacks and references
docs: normalize dependency confusion reference dates
docs: sanitize CSV injection examples and normalize references
GraphQL update
PTH Web Archive
Python Path File
XXE zip recompression tips
Archive external reference links via Wayback Machine
SQLi Auth Bypass fix example
Fix markdown linter
SSTI: - Added Elixir/EEx payloads - Added OGNL payloads
SSTI: - Fixed NodeJS payloads
Improve clarity in 2FA bypass documentation
Add Gixy-Next link (nginx static analyzer)
Upgrade GitHub Actions
```

**趋势画像**：
1. **持续归档外部链接**（`Archive external reference links via Wayback Machine`）—— 维护者主动用 Wayback Machine 归档外部参考链接，防止链接腐烂（这是其他同类项目很少做的细致维护）
2. **AI/LLM 时代新主题**：`Prompt Injection` 目录已建立，符合 2023 年后 GenAI 安全热点
3. **新增 SSTI 语言覆盖**：Elixir/EEx、OGNL（Java）、SpEL（Spring）等长尾语言
4. **CI/工具链升级**：`Upgrade GitHub Actions`、`Fix markdown linting` 保证内容质量
5. **新章节冷启动**：`XS-Leaks`（2017 老牌但近期补完）、`CSS Injection`、`Client Side Path Traversal` 等较新章节

---

## 项目画像卡片

```
项目: swisskyrepo/payloadsallthethings
年龄: 116 个月（2016-10 → 2026-04，约 9.5 年）
代码: 2,096 行真代码 + 54,442 行 payload/字典 + 5,599 行空行
       主语言: Python (61%), 次: ASP.NET (9%), XSL (7%), SVG/XML/ASP/YAML/PHP/Ruby
       文档/字典占比 96%（内容仓库，非软件项目）
总 commits: 2,185
贡献者: 333 人（但 1,341 个 commit 来自 Swissky 本人，占 61.4%；Top 5 占 72%）
         Swissky > p0dalirius(67) > ZANNI(50) > swisskyrepo(41) > nizam0906(22)
开发阶段: 稳定维护（年 commit 从 380 降到 ~100，仍在持续更新）
开发模式: 核心驱动 + 社区补充
         - 工作日 72.9% / 周末 27.1%
         - 下午 36.8% / 早晨 28.8% / 晚上 23.7% / 深夜 10.7%
         - 周三最高 / 周日次高 / 周五最低
核心文件: AD Attack (246) / Win PrivEsc (107) / SSTI (96) / XSS (85) / SSRF (80)
          / Reverse Shell (67) / SQLi (49) / XXE (49) / Linux PrivEsc (52)
热点目录: Methodology and Resources/ (内网渗透, 941 次修改)
          + 各漏洞类型目录（XSS/SSTI/SQLi/SSRF/File Inclusion/Upload）
          + 历史目录重命名残留（XSS injection / Upload insecure files / Upload）
Release: v4.2 (2025-07-26)，共 7 个 tag
         主版本节奏: 1.0→2.0→3.0→4.0 跨度 2-3 年
         小版本: 2.1/4.1/4.2 增量补内容
依赖: 0（纯内容仓库，无运行时依赖）
工程化: mkdocs 站点 + markdownlint CI + Hacktoberfest 友好 PR 流程
```

---

## 量化结论

1. **形态**: payload 字典 + 漏洞方法论 Wiki，不是软件项目。"代码" 仅是说明性 snippet（Python/HTML/PHP 等）。
2. **节奏**: 9.5 年长跑项目，2019-2022 是密集产出期（每年 330+ commits），2023 后进入稳定维护。最近 30 天 9 commits 属于"周期性活跃"，**项目仍在持续维护**。
3. **作者**: Swissky 一人主导 61% commit，333 人社区参与，典型的"作者驱动 + 社区 PR" 模式。
4. **方向**: 内网渗透（AD Attack / PrivEsc / Network Pivoting）是 2020 年后的主攻方向，占核心文件 60%+。
5. **架构债**: 存在目录重命名不规范（XSS / Upload 三种命名并存），但属于 Wiki 类项目的可接受代价。
6. **版本**: 1.0/2.0/3.0/4.0 是 4 个重大内容版本（1.x 起步 → 2.x 加入 SSRF/RCE → 3.x 大量内网方法论 → 4.x 现代化），平均每 2-3 年一次大版本。
7. **差异化亮点**:
   - 维护者主动用 Wayback Machine 归档外部链接（防腐烂）
   - Burp Intruder fuzz 字典（67 个 .txt）内嵌可直接使用
   - 多语言 SSTI/SQLi 横向覆盖（PHP/Java/Python/Node/Elixir/OGNL/SpEL）
   - 含可直接上传验证的 WebShell/样本（.asa/.aspx/.phar 等）

---

## 给 Phase 3（Content Analysis）的提示

值得在内容分析阶段深挖的「内容资产」：

1. **Burp Intruder fuzz 字典**（67 个 .txt）—— 这是本仓库相对同类内容仓库**最被低估的资产**，可直接用于生产环境漏洞扫描
2. **`Methodology and Resources/Active Directory Attack.md`** 单文件 246 次修改、绝对热度第一 —— AD 攻防的内容沉淀极深
3. **SSTI 多语言覆盖**：Java (SpEL/OGNL/EL) / Python (Jinja2/Twig) / PHP / Node / Elixir/EEx —— 横向对比表可以做出
4. **`_template_vuln/`** 贡献模板 —— 可以分析出「一个 payload 条目」的标准结构，进而反推仓库内容质量保障体系
5. **AI 时代新增内容**：`Prompt Injection` / `XS-Leak` 是较新章节，可以分析其相对成熟章节的内容深度差距

可作为「价值展示」的高密度信息点：
- `SQL Injection/MySQL Injection.md`（775 行）—— 完整的 MySQL 注入向量目录
- `JSON Web Token/README.md`（541 行）—— JWT 攻击矩阵
- `GraphQL Injection/README.md`（495 行）—— GraphQL 漏洞面映射
- `XXE Injection/README.md`（688 行）—— XXE 协议/绕过集合

---

报告生成于 Phase 2（Meta Analysis），所有数据均来自 `git log`、`tokei`、`find`、目录结构直接测量，未经推断。
