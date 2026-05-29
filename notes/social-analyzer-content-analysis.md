# Phase 3：内容分析 - qeeqbox/social-analyzer

## 3.1 动机与定位

**项目一句话描述**：跨 1000+ 社交媒体网站的用户名侦查与分析工具，提供 API、CLI 和 Web App 三种使用方式。

**README 传达的核心叙事**：
- 定位为 OSINT（开源情报）工具，用于发现和分析可疑/恶意活动相关的社交媒体档案
- 强调被"部分资源有限国家的执法机构"使用（增加权威感，但无法验证）
- 宣称检测数据库"不同于共享版本"，暗示有更完整的私有版本

**实际功能矩阵**：
| 功能 | 状态 | 实现质量 |
|------|------|----------|
| 用户名快速扫描（HTTP） | 核心功能 | 可用 |
| 用户名慢速扫描（Selenium） | 已实现 | 可用但依赖重 |
| 特殊检测（Facebook/Gmail/Google） | 已实现 | 脆弱，依赖页面结构 |
| 字符串分析（拆词/数字/符号） | 已实现 | 基础实现 |
| 姓名来源识别 | 已实现 | 基于静态字典 |
| 年龄猜测 | 已实现 | 极简启发式 |
| 元数据提取 | 已实现 | HTML meta 标签 |
| 力导向图可视化 | 已实现 | 依赖 ixora 库 |
| OCR 检测 | 已实现 | 使用 tesseract.js |
| Google API 搜索 | 已实现 | 需要 API Key |

---

## 3.2 作者视角价值分析

**对作者的价值**：
- **安全工具集品牌建设**：QeeqBox 有 93 个公开仓库，social-analyzer 是其安全工具矩阵中的旗舰项目（Stars 最高），用于建立"安全工具开发者"的个人品牌
- **技能展示**：展示了全栈能力（Node.js + Python + Web前端 + Docker + Selenium）
- **AGPL-3.0 策略**：故意选择限制性许可证，可能为商业咨询/私有版本保留空间
- **"执法机构使用"声明**：增加项目可信度的营销策略

**Star 数与实际使用量的巨大落差分析**（22K Stars vs 129 npm 下载/月）：
- 项目定位为"安全/OSINT"，这类工具天然吸引 Star 但实际使用频率低
- AGPL 许可证阻止了商业集成
- 依赖过重（需要 Firefox、Tesseract OCR）降低了实际部署意愿
- sites.json 中的检测规则容易过时，维护不跟上则工具逐渐失效

---

## 3.3 架构与设计决策

### 整体架构

```
┌─────────────────────────────────────────────┐
│              入口层                           │
│  app.js (Node CLI/Web)  │  app.py (Python CLI) │
├─────────────────────────────────────────────┤
│              模块层（仅 Node.js）              │
│  fast-scan  │ slow-scan │ special-scan       │
│  engine     │ helper    │ extraction         │
│  string-analysis │ name-analysis │ stats     │
│  external-apis   │ visualize                 │
├─────────────────────────────────────────────┤
│              数据层                           │
│  sites.json (999 站点, 22K 行)               │
│  names.json │ dict.json │ languages.json     │
└─────────────────────────────────────────────┘
```

### 关键设计决策

**1. 双语言实现（Node.js + Python）**
- Node.js 版本是"完整版"：Web UI + CLI + 全部功能模块
- Python 版本是"精简版"：仅 CLI + 快速扫描，单文件 912 行
- 两套代码共享 `data/sites.json`，但检测逻辑各自独立实现
- **问题**：维护两套几乎相同的逻辑是典型的技术债务

**2. 数据驱动的检测引擎**
- 核心思想：将"如何检测用户是否存在于某网站"抽象为 JSON 配置
- `sites.json` 每条记录包含：URL 模板、检测规则、站点元数据
- 检测类型分层：`normal`（字符串匹配 HTML 源码）、`advanced`（纯文本匹配）、`ocr`（截图 OCR）、`shared`（共享检测规则）、`special`（自定义 Selenium 脚本）
- **这是该项目最有价值的设计**：将领域知识（各网站的检测特征）与执行逻辑分离

**3. 评分系统**
- 基于检测规则命中率计算 0-100% 评分
- 分为 good(100%) / maybe(50-99%) / bad(<50%) 三档
- 有 `detection_level` 配置（extreme/high），控制需要命中多少条规则才算"发现"
- **实际效果**：减少误报但设计简陋，无权重概念

**4. 三种扫描模式的分层**
- Fast Scan：HTTP GET + 字符串匹配（轻量，默认 15 并发）
- Slow Scan：Selenium 无头浏览器 + 截图 + OCR（重量级，8 并发）
- Special Scan：针对特定平台的定制脚本（Facebook 密码恢复、Gmail 注册检查等）
- **设计合理**：分层解决了"反爬"问题，但 slow/special 模式对环境依赖极重

**5. 重试机制**
- Fast Scan 自带 3 轮重试：`find_username_normal_wrapper` 被调用 3 次
- 失败的站点进入下一轮重试队列
- 3 轮后仍失败的标记为 `failed`
- **简单有效**的容错设计

### 代码规模

| 文件 | 行数 | 职责 |
|------|------|------|
| app.js | 841 | Node 入口，Express 路由 + CLI 逻辑 |
| app.py | 912 | Python 独立实现 |
| helper.js | 364 | 工具函数集（HTTP、日志、解析） |
| string-analysis.js | 284 | 用户名字符串分析 |
| fast-scan.js | 215 | HTTP 快速扫描 |
| slow-scan.js | 199 | Selenium 慢速扫描 |
| special-scan.js | 192 | 平台特定检测 |
| external-apis.js | 152 | Google/DuckDuckGo API |
| engine.js | 132 | 检测引擎核心 |
| stats.js | 113 | 统计分析 |
| extraction.js | 92 | 元数据/模式提取 |
| visualize.js | 88 | 力导向图 |
| name-analysis.js | 79 | 姓名来源分析 |
| **data/sites.json** | **22,760** | **站点检测数据库** |
| **总计** | **~3,663 (代码) + 22,760 (数据)** | |

**结论**：这是一个"数据重、代码轻"的项目。sites.json 占据了项目的绝大部分体量和核心价值。

---

## 3.4 创新点识别

### 值得借鉴的设计

**1. 检测规则数据库模式（核心创新，价值 ★★★★）**

将网站检测逻辑抽象为声明式 JSON 配置：

```json
{
  "url": "https://7cups.com/@{username}",
  "detections": [
    {"return": "false", "string": "Not Found", "type": "normal"},
    {"return": "true", "string": "com/@{username}", "type": "normal"},
    {"return": "true", "string": "Profile - 7 Cups", "type": "normal"}
  ],
  "type": "Health > Mental Health",
  "global_rank": 64188,
  "country": "United States"
}
```

正向检测（`return: "true"` — 页面包含此字符串则+1分）和反向检测（`return: "false"` — 页面不包含此字符串则+1分）的组合设计非常巧妙，能有效区分"用户存在"和"404 页面"。

**2. 共享检测规则（shared detections）**

多个使用同一平台（如 MediaWiki）的站点可以共享一套检测规则，减少重复配置。sites.json 中 999 个站点里有 389 条使用了 shared 类型。

**3. 用户名字符串分析管线（价值 ★★★）**

从用户名中提取结构化信息的流水线设计：
- 大小写拆分 → 字母数字拆分 → 符号识别 → 数字识别
- 数字转字母（leetspeak: 4→a, 3→e, 0→o 等）
- 字典拆词（WordsNinja）
- 姓名数据库匹配 + 来源国识别
- 年龄猜测（从数字中推断出生年份）
- 常见词语言分布分析

这套管线本身就是一个有价值的小工具。

**4. WAF/反爬检测过滤**

自动过滤被 Cloudflare、CAPTCHA 等拦截的结果，通过正则检测 title 和 body 中的特征字符串。Python 版本还检查 HTTP 响应头中的 `cf-ray` 和 `server: cloudflare`。

### 局限性

**1. 无状态码检测**：只做字符串匹配，不检查 HTTP 状态码（200/404/301），这是 Sherlock 的核心检测方式之一
**2. 无 API 检测**：不利用社交平台公开 API 做验证
**3. 检测规则维护困难**：999 个站点的检测规则需要持续更新，一人维护不可持续

---

## 3.5 竞品交叉分析

| 维度 | social-analyzer | Sherlock (74K Stars) | Maigret (19K Stars) |
|------|----------------|---------------------|---------------------|
| **语言** | Node.js + Python | Python | Python |
| **站点数** | 999 | 400+ | 3000+ |
| **检测方式** | 字符串匹配+OCR+Selenium | 状态码+字符串匹配+响应URL | 状态码+字符串+响应URL+JSON解析 |
| **使用界面** | API+CLI+Web | CLI | CLI+Web报告 |
| **分析能力** | 有（字符串分析、姓名来源、元数据、评分） | 无 | 有（标签提取） |
| **可视化** | 力导向图 | 无 | 有 |
| **许可证** | AGPL-3.0 | MIT | MIT |
| **维护状态** | 极低频 | 活跃 | 活跃 |
| **误报控制** | 评分系统 | 依赖社区维护 | 更精细的检测规则 |

**social-analyzer 的差异化价值**：
1. **Web UI**：开箱即用的 Web 界面是 Sherlock/Maigret 没有的
2. **字符串分析**：从用户名提取情报的附加分析能力是独有的
3. **评分系统**：量化检测置信度而非简单的"存在/不存在"二元判断
4. **力导向图**：跨平台元数据关联可视化

**social-analyzer 的劣势**：
1. **MIT vs AGPL**：竞品使用更宽松的许可证，更利于社区和商业采用
2. **维护活跃度**：竞品社区活跃，检测规则持续更新
3. **站点覆盖**：Maigret 3000+ 站点远超 social-analyzer 的 999
4. **依赖重量**：需要 Firefox + Tesseract OCR，而 Sherlock 只需 requests 库

---

## 3.6 代码质量评估

### 测试

- **测试文件**：仅一个 `test/test.sh`（5 行），只检查 Python CLI 能否加载配置文件
- **无单元测试、无集成测试**
- `package.json` 中的 test 脚本是 `echo "Error: no test specified" && exit 1`
- **评分：0/10** — 实质上没有测试

### CI/CD

- GitHub Actions 仅用于自动提交（由机器人 `qb-auto` 推送），不是真正的 CI
- 下载外部脚本 `auto-checking.sh` 执行检测规则更新，而非运行测试
- **评分：1/10** — 有流水线但不做质量保证

### 代码风格

- 有 ESLint 配置（devDependencies），但代码风格不统一
- 混用 `async/await` 和 `Promise`，多处 `await forEach` 是反模式（不会等待异步完成）
- 大量 `suppress(Exception)` / 空 `catch` 吞掉异常
- 变量命名不规范：`temp_`, `_temp`, 拼写错误（`pendding`、`recoveqr`、`resutls`、`tecert`）
- app.js 单文件 841 行，`analyze_string` 路由处理函数超过 200 行
- **评分：3/10** — 可运行但维护困难

### 安全问题

- `req.body.uuid` 虽有正则过滤，但 Express 路由无认证保护
- 直接使用 `fs.readFileSync` 处理用户输入路径（UUID 构造文件名）
- 特殊扫描中的 Selenium 脚本操作 Facebook 登录页面 — 在某些司法管辖区可能违规
- 依赖版本锁定不严格（如 `cheerio: "^1.0.0-rc.11"`）

### 架构问题

- Node.js 和 Python 两套实现共享数据但不共享逻辑，改一边忘记改另一边
- `app.js` 既是 Express 服务器又是 CLI 入口，职责不清
- 全局可变状态：`helper.websites_entries` 被多处修改（设置 selected 状态）
- `setup.py` 中版本号 `0.45` 与 `package.json` 中 `2.0.32` 不一致
- `countries_json_path` 指向 `names.json` 而非 `countries.json`（复制粘贴错误）

---

## 综合评估

### 项目价值分级

| 维度 | 评分 | 说明 |
|------|------|------|
| 创意与差异化 | ★★★★☆ | 评分系统+字符串分析+Web UI 的组合在 OSINT 工具中独特 |
| 代码质量 | ★★☆☆☆ | 可运行但充满反模式和技术债务 |
| 可维护性 | ★☆☆☆☆ | 无测试、双语言冗余、单人维护已停滞 |
| 实用性 | ★★★☆☆ | 功能丰富但部署复杂、检测规则过时 |
| 学习价值 | ★★★☆☆ | 数据驱动检测引擎的设计模式值得学习 |

### 核心洞察

1. **这是一个"数据产品"而非"代码产品"**：项目 90% 的价值在 `sites.json`（22K 行检测规则数据库），代码只是执行引擎。一旦数据停止更新，项目就失去核心价值。

2. **22K Star 是"安全工具光环效应"**：OSINT/安全类工具天然吸引关注，但从 npm 月下载量（129）看，实际用户极少。大量 Star 来自"收藏以备不时之需"的安全从业者。

3. **双语言实现是战略性的**：Python 版本作为 pip 包发布方便集成到现有 OSINT 工具链，Node.js 版本提供 Web UI 和 Express API。但维护成本翻倍，已经出现两边不一致的情况。

4. **项目的实际衰退已开始**：检测规则依赖人工维护，而贡献者基本只有作者一人。随着网站改版，越来越多的检测规则会失效。CI 中的"自动检测更新"脚本可能是作者试图自动化这个过程的尝试。

### 可提取的技术模式

1. **声明式检测引擎**：将领域知识（网站特征）抽象为 JSON 配置，检测逻辑通用化 — 适用于任何需要"对大量目标执行模式匹配"的场景
2. **多层检测策略**：fast→slow→special 的渐进式检测，先用轻量方式筛选，再用重量级方式确认
3. **置信度评分**：用命中率百分比替代二元判断，配合阈值过滤减少误报
4. **用户名情报分析**：从字符串结构中推断用户画像（年龄、姓名、性别、国籍）的方法论
