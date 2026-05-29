# agent-browser 网络分析报告

> 分析时间：2026-03-22
> 仓库：[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

## 仓库基本数据

| 指标 | 数值 |
|------|------|
| 名称 | agent-browser |
| 描述 | Browser automation CLI for AI agents |
| 主语言 | Rust（1,251,165 字节），辅以 TypeScript（30,024）、JavaScript（16,819）、Shell（9,524）、HTML（8,982） |
| Star 数 | **24,010** |
| Fork 数 | 1,418 |
| Watcher 数 | 61 |
| Issue 总数 | 162（开放中 ~304 含 PR） |
| PR 总数 | 142 |
| 许可证 | Apache-2.0 |
| 创建时间 | 2026-01-11 |
| 最近推送 | 2026-03-21（持续活跃） |
| 最近更新 | 2026-03-22 |
| 磁盘占用 | ~15 MB |
| 官网 | https://agent-browser.dev |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 默认分支 | main |
| 当前版本 | v0.21.4（2026-03-20 发布） |
| 社区健康度 | 37%（缺少 CODE_OF_CONDUCT、CONTRIBUTING 文件） |

**关键观察**：仓库创建仅 **2 个多月**，已获得 24K Star，增长极其迅猛。代码以 Rust 为主（占比 ~95%），体现了对性能的极致追求。

## 作者画像

### 组织：Vercel Labs

| 指标 | 数值 |
|------|------|
| 组织名 | Vercel Labs (@vercel-labs) |
| 简介 | Develop. Preview. Ship. Creators of Next.js. |
| 官网 | https://vercel.com |
| 公开仓库数 | 233 |
| 关注者 | 5,177 |
| 创建时间 | 2022-07-01 |

Vercel Labs 是 Vercel 的实验项目孵化器，Vercel 是全球领先的前端云平台和 Next.js 的创建者。Labs 定位为前沿技术探索，agent-browser 是其在 AI Agent 工具链方向的重要布局。

### 核心贡献者：Chris Tate (@ctate)

| 指标 | 数值 |
|------|------|
| 姓名 | Chris Tate |
| 身份 | Dev @Vercel, Creator @SpecUI |
| 所在地 | Austin, TX |
| 关注者 | 1,145 |
| 公开仓库 | 153 |
| 个人网站 | ctate.dev |
| 提交占比 | 262 / ~380+（约 69%） |

Chris Tate 是该项目的灵魂人物，贡献了近 70% 的 commits。他同时活跃在 X/Twitter 上发布新功能（如 Electron skill 支持）。

### 贡献者分布

| 贡献者 | 提交数 | 备注 |
|--------|--------|------|
| ctate | 262 | 核心开发者，Vercel 员工 |
| github-actions[bot] | 61 | CI/CD 自动化 |
| jin-2-kakaoent | 14 | 社区贡献者 |
| mikewong23571 | 10 | 社区贡献者 |
| hewliyang | 5 | 社区贡献者 |
| 其余 25+ 位 | 1-4 | 社区贡献者 |

**贡献者特征**：高度集中在 1 位核心开发者，社区贡献者参与广泛但贡献量较小，属于典型的"核心驱动型"开源项目。

## 社区热度

### Star 增长趋势

- **创建日（2026-01-11）**：首日即快速获取大量 Star
- 根据 API 返回的 stargazer 数据，首页（前 30 条）全部集中在 2026-01-11 当天
- 根据 X/Twitter 上 daily.dev 的报道："17k stars in hours"（数小时内 17K Star）
- **当前（2026-03-22）**：24,010 Star

**增长曲线分析**：
- 第1天（1月11日）：爆发式增长，数小时内突破 17K Star（Vercel 品牌效应 + AI Agent 赛道热度）
- 1-3月：持续增长至 24K，月均新增 ~2,300 Star
- 属于典型的"发布即引爆"模式

### npm 下载量趋势

| 时间段 | 周下载量 |
|--------|----------|
| 1月第2周（发布周） | 27,519 |
| 1月第3周 | 30,339 |
| 1月第4周 | 66,547 |
| 2月第1周 | 319,740 |
| 2月第2周 | **691,788** |
| 2月第3周 | 680,264 |
| 2月第4周 | **749,810** |
| 3月第1周 | **779,419**（峰值） |
| 3月第2周 | 361,659 |
| 3月第3周 | 113,461 |

- **总下载量（1月-3月）**：约 465 万次
- **峰值周下载量**：77.9 万次（3月第1周）
- **趋势**：2月初爆发式增长，2月-3月初维持高位（周均 60-78 万），3月中旬后回落

### 开发活跃度

| 月份 | Commits 数 |
|------|-----------|
| 1月（11日起） | 100+（API 上限） |
| 2月 | 88 |
| 3月（至21日） | 100+（API 上限） |

- 发布频率极高：近 5 天内发布了 v0.21.0 到 v0.21.4 共 5 个版本
- 最近 commit（3月21日）修复了 find flags 泄露到 fill 值的 bug
- 开发节奏非常快，几乎每天都有 commit

## 生态网络

### 集成生态

agent-browser 定位为 AI Agent 的"浏览器手臂"，已集成/兼容以下主流 AI 编码工具：

| AI Agent 工具 | 集成方式 |
|--------------|---------|
| **Claude Code** | 原生 Skill 支持（`npx skills add vercel-labs/agent-browser`） |
| **OpenAI Codex** | Bash 命令兼容 |
| **Google Gemini CLI** | Bash 命令兼容 |
| **GitHub Copilot** | Bash 命令兼容 |
| **Cursor** | Bash 命令兼容 |
| **Windsurf** | Bash 命令兼容 |
| **Goose** | Bash 命令兼容 |
| **OpenCode** | Bash 命令兼容 |

### Skills 生态

agent-browser 推出了 Skills 系统（技能扩展），已有的 Skill 包括：
- **agent-browser**（核心浏览器技能）
- **Electron** — 控制桌面应用（Discord、Figma、Notion、Spotify、VS Code）
- 可通过 `npx skills add` 安装

### 安装渠道

| 渠道 | 命令 |
|------|------|
| npm（推荐） | `npm install -g agent-browser` |
| Homebrew | `brew install agent-browser` |
| Cargo | `cargo install agent-browser` |
| 源码编译 | `pnpm build:native` |

### 技术架构

三层架构设计：
1. **Rust CLI（客户端层）**：命令解析、IPC 通信
2. **守护进程（服务层）**：管理浏览器生命周期，通过 Chrome DevTools Protocol（CDP）通信
3. **浏览器实例**：Chrome（主要）、Firefox、WebKit、Safari

五级配置优先级：内置默认 → 用户配置 → 项目配置 → 环境变量 → CLI 标志

## 官方文档洞察

### 官方网站

- **官网**：[agent-browser.dev](https://agent-browser.dev) — 提供完整的产品介绍、功能特性和使用指南
- **GitHub README**：详尽的命令参考，覆盖 50+ 命令
- **Skill 文档**：[skills/agent-browser/SKILL.md](https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/SKILL.md)
- **命令参考**：[skills/agent-browser/references/commands.md](https://github.com/vercel-labs/agent-browser/blob/main/skills/agent-browser/references/commands.md)

### 核心卖点（官方宣传）

1. **Agent-first 设计**：文本输出比 JSON 节省 82-93% 的 token（~200-400 vs ~3000-5000 tokens）
2. **Ref-based 交互模型**：通过无障碍树快照生成确定性元素引用（@e1, @e2），避免脆弱的 CSS 选择器
3. **原生 Rust 性能**：命令解析速度极快
4. **50+ 完整命令集**：导航、交互、截图、网络捕获、PDF 导出等
5. **会话管理**：多个隔离的浏览器实例并行运行
6. **跨平台**：macOS、Linux、Windows 原生二进制

### 第三方报道/博客

| 来源 | 标题/内容 | 链接 |
|------|----------|------|
| Towards AI | "Vercel Just Solved Browser Automation for AI Agents" | [链接](https://pub.towardsai.net/vercel-just-solved-browser-automation-for-ai-agents-b3414ebdb4d7) |
| Pulumi Blog | "Self-Verifying AI Agents: Vercel's Agent-Browser in the Ralph Wiggum Loop" | [链接](https://www.pulumi.com/blog/self-verifying-ai-agents-vercels-agent-browser-in-the-ralph-wiggum-loop/) |
| Medium | "Agent-Browser: AI-First Browser Automation That Saves 93% of Your Context Window" | [链接](https://medium.com/@richardhightower/agent-browser-ai-first-browser-automation-that-saves-93-of-your-context-window-7a2c52562f8c) |
| AI Base | "AI Can Finally Manipulate Things! Vercel Launches Agent Browser" | [链接](https://news.aibase.com/news/24556) |
| Apiyi Blog | "Complete Guide to agent-browser" | [链接](https://help.apiyi.com/en/agent-browser-ai-browser-automation-cli-guide-en.html) |
| NxCode | "Stagehand vs Browser Use vs Playwright: AI Browser Automation Compared" | [链接](https://www.nxcode.io/resources/news/stagehand-vs-browser-use-vs-playwright-ai-browser-automation-2026) |
| Scrapeless | "Agent Browser vs Puppeteer & Playwright: What Developers Should Know" | [链接](https://www.scrapeless.com/en/wiki/agent-browser-vs-puppeteer-playwright) |
| Bright Data | "Agent Browser vs Puppeteer & Playwright: Key Differences" | [链接](https://brightdata.com/blog/ai/agent-browser-vs-puppeteer-playwright) |

### X/Twitter 关键声音

- **@dailydotdev**："vercel just dropped agent-browser. 17k stars in hours."
- **@Shpigford**（Josh Pigford）："substantially faster than playwright and is clearly optimized for AI use"
- **@jasonzhou1993**："70% less token consumption compared with Chrome dev tool MCP"
- **@ctatedev**（作者）：持续发布新功能（Electron skill 等）
- **@kieranklaassen**："The agent browser is very good. So good that I replaced it immediately in my compound engineering plugin."

## 竞品清单

### 直接竞品对比

| 项目 | Star 数 | 语言 | 定位 | 关键差异 |
|------|---------|------|------|---------|
| **[microsoft/playwright](https://github.com/microsoft/playwright)** | 84,689 | TypeScript | 通用 Web 测试和自动化框架 | 功能全面但非 AI 优先，context 消耗大 |
| **[browser-use/browser-use](https://github.com/browser-use/browser-use)** | 81,848 | Python | 让 AI Agent 可访问网站 | Python 生态，WebVoyager 基准 89.1% 成功率 |
| **[browserbase/stagehand](https://github.com/browserbase/stagehand)** | 21,650 | TypeScript | AI 浏览器自动化框架 | 三个自然语言原语（act/extract/observe），增强 Playwright |
| **[Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern)** | 20,884 | Python | 基于 AI 的浏览器工作流自动化 | 视觉理解驱动，适合复杂工作流 |
| **[nanobrowser/nanobrowser](https://github.com/nanobrowser/nanobrowser)** | 12,500 | — | 开源 Chrome 扩展 AI 浏览器 Agent | 浏览器扩展形态，多 Agent 架构 |
| **[ntegrals/openbrowser](https://github.com/ntegrals/openbrowser)** | 9,311 | — | 自主浏览器 AI Agent 工具包 | 自主执行导向 |
| **[lavague-ai/LaVague](https://github.com/lavague-ai/LaVague)** | 6,317 | Python | 大型动作模型框架 | 学术味更重，Web Agent 框架 |

### agent-browser 的差异化定位

1. **CLI 优先**：不是 SDK/库，而是 CLI 工具 — 任何能执行 shell 命令的 AI Agent 都能使用
2. **Token 效率**：比 Playwright MCP 节省 82-93% 的 context window
3. **Rust 性能**：原生编译，启动和执行速度远超 Node.js/Python 方案
4. **Ref-based 交互**：通过无障碍树快照 + 唯一引用 ID，比 CSS 选择器更稳定
5. **零依赖运行时**：不需要 Playwright 或 Node.js（纯 Rust 守护进程）

## 关键 Issue 信号

### 热门讨论 Issue（按评论数排序）

| # | 标题 | 评论 | 状态 | 信号 |
|---|------|------|------|------|
| [#56](https://github.com/vercel-labs/agent-browser/issues/56) | Windows Daemon failed | 22 | Closed | **Windows 兼容性是主要痛点** |
| [#390](https://github.com/vercel-labs/agent-browser/issues/390) | Daemon failed to start (Windows) | 21 | Open | Windows 上 socket 问题持续存在 |
| [#953](https://github.com/vercel-labs/agent-browser/issues/953) | This thing constantly crashes on windows | — | Open | Windows 稳定性仍需改善 |
| [#954](https://github.com/vercel-labs/agent-browser/issues/954) | `upgrade` command seems not robust | — | Open | CLI 升级体验待优化 |
| [#465](https://github.com/vercel-labs/agent-browser/pull/465) | feat: file download/upload/drag-drop | 4 | Open | 文件操作功能正在开发 |
| [#467](https://github.com/vercel-labs/agent-browser/pull/467) | ARM64 Linux auto-fallback to Firefox | 4 | Open | ARM64 Linux 兼容性 |

### Issue 信号总结

1. **Windows 兼容性**是社区最大痛点（#56, #390, #953），Daemon 启动失败问题频发
2. **跨平台支持**仍在完善中（ARM64 Linux 需要回退到 Firefox）
3. **功能扩展**活跃：文件上传/下载、viewport 控制、HAR 网络捕获、批量执行等
4. **开发响应速度快**：大量 PR 在短时间内被合并（#426 一次修复 33+ 个 issue）

## 知识入口

| 平台 | 地址 | 状态 |
|------|------|------|
| **DeepWiki** | [deepwiki.com/vercel-labs/agent-browser](https://deepwiki.com/vercel-labs/agent-browser) | 已收录，提供架构解析、功能说明等深度内容 |
| **Zread.ai** | [zread.ai/vercel-labs/agent-browser](https://zread.ai/vercel-labs/agent-browser) | 已收录，提供 AI 问答、代码浏览、文档搜索 |
| **npm** | [npmjs.com/package/agent-browser](https://www.npmjs.com/package/agent-browser) | 官方包页面 |
| **skills.sh** | [skills.sh/vercel-labs/agent-browser](https://skills.sh/vercel-labs/agent-browser/agent-browser) | Skills 市场页面 |
| **官网** | [agent-browser.dev](https://agent-browser.dev) | 产品首页 |

## 项目展示素材

### 快速上手演示命令

```bash
# 安装
npm install -g agent-browser
agent-browser install

# 基本操作演示
agent-browser open example.com
agent-browser snapshot                    # 获取无障碍树（含 ref 引用）
agent-browser click @e2                   # 通过 ref 点击
agent-browser fill @e3 "test@example.com" # 通过 ref 填写
agent-browser screenshot page.png         # 截图
agent-browser close
```

### 核心亮点数据

- **24K Star**（2个月内）
- **465万+ npm 下载**（3个月内）
- **50+ CLI 命令**
- **82-93% Token 节省**（vs Playwright MCP）
- **100% Rust 原生**
- **跨平台**：macOS / Linux / Windows
- **6种安装方式**：npm / Homebrew / Cargo / 源码 / 项目依赖

### 标志性引用

> "substantially faster than playwright and is clearly optimized for AI use" — Josh Pigford (@Shpigford)

> "70% less token consumption compared with Chrome dev tool MCP" — Jason Zhou (@jasonzhou1993)

> "vercel just dropped agent-browser. 17k stars in hours." — daily.dev

## 快速判断

### 综合评分

| 维度 | 评分（/5） | 说明 |
|------|-----------|------|
| 热度 | ★★★★★ | 24K Star（2个月），465万 npm 下载，社交媒体爆火 |
| 背景 | ★★★★★ | Vercel Labs 出品，Next.js 创始团队，顶级品牌背书 |
| 活跃度 | ★★★★★ | 每天都有 commit，每周发新版本，响应迅速 |
| 创新性 | ★★★★☆ | Ref-based 交互模型、CLI-first 设计、极致 Token 优化，独树一帜 |
| 成熟度 | ★★★☆☆ | 仅 2 个月历史，Windows 兼容性欠佳，社区文档不完善（健康度 37%） |
| 竞争力 | ★★★★☆ | 在 CLI/Token 效率维度领先，但整体生态不及 browser-use（81K Star） |

### 一句话总结

**agent-browser 是 Vercel Labs 推出的 AI Agent 浏览器自动化 CLI 工具，以 Rust 原生性能和极致的 Token 效率（节省 82-93%）为核心卖点，2 个月内斩获 24K Star，是 2026 年 AI Agent 工具链赛道最受关注的新项目之一。其 CLI-first + Ref-based 的设计理念具有独创性，但 Windows 稳定性和社区文档仍需完善。**

### 适合关注的人群

- AI Agent / Coding Agent 开发者
- 浏览器自动化 / Web 测试工程师
- 关注 AI 工具链和 DevTools 生态的技术人员
- Vercel / Next.js 生态的开发者

### 风险提示

1. 核心开发者高度集中（1人贡献 69%），存在 bus factor 风险
2. 项目仅 2 个月历史，API 可能频繁变更
3. Windows 平台兼容性问题尚未完全解决
4. npm 下载量在 3 月中旬出现明显下滑，需关注后续趋势
