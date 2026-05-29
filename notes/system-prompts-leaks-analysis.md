# asgeirtj/system_prompts_leaks 仓库分析报告

> 分析日期：2026-03-22
> 仓库地址：https://github.com/asgeirtj/system_prompts_leaks

## 项目类型标注

**纯文档收集类仓库（非代码项目）**。该仓库不包含任何可执行代码，完全由 Markdown/HTML/XML/TXT 格式的文档组成，内容为各大 AI 聊天机器人的系统提示词（System Prompts）泄露合集。

---

## 一、项目概览

| 指标 | 数值 |
|------|------|
| 名称 | system_prompts_leaks |
| 描述 | Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini |
| 主要语言 | HTML（GitHub 标记），实际内容以 Markdown 为主（128 个 .md 文件） |
| Star 数 | **34,785** |
| Fork 数 | **5,594** |
| Watcher 数 | 474 |
| Issue 数 | 0（已全部关闭） |
| PR 总数 | 17 |
| 许可证 | **无** |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 磁盘用量 | 1,548 KB（GitHub）/ 7.3 MB（含 .git） |
| 默认分支 | main |
| 创建时间 | 2025-05-03 |
| 最后推送 | 2026-03-15 |
| 最后更新 | 2026-03-21 |

### 仓库标签（Topics）

`ai`, `anthropic`, `chatbots`, `chatgpt`, `claude`, `gemini`, `generative-ai`, `google-deepmind`, `large-language-models`, `llm`, `openai`, `prompt-engineering`, `prompt-injection`, `prompts`

---

## 二、仓库结构

```
.
├── Anthropic/          # Claude 系列系统提示词
│   ├── old/            # 旧版本存档（claude-3.7, 4.1, 4.5）
│   ├── raw/            # 未格式化的原始提示词
│   ├── FlintK12/       # 教育产品 FlintK12 的提示词
│   ├── claude-opus-4.6.md, claude-sonnet-4.6.md  # 最新版本
│   ├── claude-code.md, claude-code2.md           # Claude Code 提示词
│   ├── claude-cowork.md, claude-desktop-code.md  # 桌面/协作版本
│   ├── claude-in-chrome.md                       # Chrome 扩展版本
│   └── claude.html                               # 可视化 HTML 版本
├── Google/             # Gemini 系列系统提示词
│   ├── gemini-2.5/3.0/3.1 系列
│   ├── jules.md        # Google Jules Agent
│   └── ai-studio-build.md
├── OpenAI/             # GPT 系列系统提示词
│   ├── GPT-4o, GPT-4.1, GPT-4.5
│   ├── gpt-5 系列（thinking, instant, codex）
│   ├── gpt-5.1 ~ gpt-5.4 系列
│   ├── o3, o4-mini     # 推理模型
│   └── tool-*.md       # 各工具系统提示词
├── Perplexity/         # Perplexity AI
├── xAI/                # Grok 系列（3, 4, 4.1, 4.2）
├── Misc/               # 其他产品
│   ├── Notion AI, Le-Chat, Kagi Assistant
│   ├── Warp 2.0, Raycast AI, t3.chat
│   └── 各类浏览器助手等
├── .github/FUNDING.yml
└── readme.md
```

### 文件统计

| 类型 | 文件数 | 说明 |
|------|--------|------|
| Markdown (.md) | 128 | 主体内容，系统提示词文档 |
| HTML (.html) | 1 | Claude 可视化页面 |
| TXT (.txt) | 1 | 早期文本格式 |
| XML (.xml) | 1 | XML 格式存档 |
| **总计** | **135** | （含配置文件） |

### 内容规模（tokei 统计）

- Markdown 总行数：**144,502 行**
- 最大文件：`Anthropic/claude-code2.md`（97,903 行，1.1MB）——Claude Code 完整系统提示词
- HTML 部分包含嵌入的 JavaScript（4,365 行）和 CSS（206 行），用于可视化展示

---

## 三、所有者分析

| 字段 | 信息 |
|------|------|
| 用户名 | asgeirtj |
| 姓名 | Ásgeir Thor Johnson |
| 所在地 | 冰岛（Iceland） |
| 简介 | Discord: asgeirtj |
| 公开仓库数 | 32 |
| 粉丝数 | 1,007 |
| 注册时间 | 2017-04-13 |

**画像**：冰岛独立开发者/安全研究者，主要活跃于 AI 提示词泄露领域。该仓库是其最具影响力的项目，贡献了仓库 92% 以上的提交。

---

## 四、贡献者分析

### 提交贡献排名

| 贡献者 | 提交数 | 角色 |
|--------|--------|------|
| Ásgeir Thor Johnson | 309（含多个账号名义） | 创建者/核心维护者 |
| awrreny | 5 | 活跃贡献者 |
| Camilo (candreszg) | 2 | 贡献者 |
| MaloneFreak | 2 | 贡献者 |
| bgauryy | 2 | 贡献者 |
| 其他 13 人 | 各 1 次 | 偶尔贡献者 |

**总贡献者**：19 人（git log 统计），GitHub API 显示 17 人

**社区特征**：
- 典型的**单人维护仓库**，所有者贡献率超过 92%
- 社区贡献以提交新发现的系统提示词为主
- PR 合并率较低（17 个 PR 中只有 7 个被合并），维护者对内容质量有一定把控
- 有一位名为 "Claude" 的贡献者（login: claude），贡献了 1 次提交

---

## 五、Star 增长与热度分析

### 核心数据

- 总 Star 数：**34,785**
- Star/Fork 比：6.2:1
- 创建至今约 10.5 个月，平均每月增长约 **3,300 星**

### 近期活跃度

从可获取的最近 50 颗 Star 来看，全部集中在 **2026-03-21** 单日内（从凌晨 05:43 到 23:04），说明仓库仍在持续获得关注。在 TrendShift 上有活跃徽章。

### 增长判断

以 3.5 万星的体量和仅 10 个月的历史来看，该仓库经历了**爆发式增长**，很可能在创建初期（2025 年 5 月）就登上了 GitHub Trending，此后持续受到 AI 社区关注。

---

## 六、提交历史分析

### 基本统计

| 指标 | 数值 |
|------|------|
| 总提交数 | 335 |
| 首次提交 | 2025-05-03 |
| 最后提交 | 2026-03-15 |
| 活跃周期 | ~10.5 个月 |
| 月均提交 | ~32 次 |

### 月度提交分布

| 月份 | 提交数 | 趋势 |
|------|--------|------|
| 2025-05 | 111 | 项目创建，大量初始内容 |
| 2025-06 | 11 | 低谷期 |
| 2025-07 | 19 | 缓慢恢复 |
| 2025-08 | 20 | 稳定 |
| 2025-09 | 14 | 低谷 |
| 2025-10 | 24 | 回升（可能 GPT-5 发布） |
| 2025-11 | 12 | 平稳 |
| 2025-12 | 15 | 平稳 |
| 2026-01 | 16 | 平稳 |
| 2026-02 | 47 | **大幅增长**（新模型密集发布期） |
| 2026-03 | 46 | **高活跃**（截至 3/15 已有 46 次） |

**趋势分析**：2026 年 2-3 月出现显著的活跃峰值，与 GPT-5 系列、Claude 4.6、Gemini 3.x 等新模型密集发布相吻合。每当有重大模型更新，仓库会迅速收录其系统提示词。

### 最频繁修改的文件

| 修改次数 | 文件 |
|----------|------|
| 14 | readme.md |
| 13 | README.md |
| 11 | claude.txt（早期格式） |
| 7 | Anthropic/claude-opus-4.6.md |
| 7 | 2.md（临时文件） |
| 6 | claude.html |
| 5 | OpenAI/gpt-5.2-thinking.md |
| 5 | claude-3.7-sonnet-2025-05-11.xml |
| 5 | Anthropic/readme.md |

README 和 Claude 系列提示词是修改最频繁的内容，反映了 Anthropic 模型更新频繁和维护者对 Claude 提示词的持续关注。

---

## 七、Issue 与 PR 分析

### Issue（总计 0 个开放）

热门话题：

| # | 标题 | 评论数 | 状态 |
|---|------|--------|------|
| #1 | Source? | 12 | closed |
| #46 | Create gpt-5.1-medium-api.md | 6 | open |
| #41 | Updates to Claude 4.5 Sonnet System Prompt | 5 | open |
| #15 | Add Claude 4.0 sonnet artifact and analysis_tool | 3 | open |
| #72 | Add GPT-5-Mini | 2 | closed |

最热 Issue #1 "Source?" 有 12 条评论，反映社区对内容来源和合法性的关注。

### Pull Requests（总计 17 个）

- 已合并：7 个
- 已关闭（未合并）：8 个
- 开放中：2 个

典型被合并的 PR 包括：添加特定产品的系统提示词（FlintK12、Gemini 3 Fast、Confer.to、Notion AI 等）。

---

## 八、内容覆盖范围

### 按厂商分类

| 厂商 | 覆盖模型/产品 | 文件数（估算） |
|------|---------------|----------------|
| **Anthropic** | Claude 3.7, 4.1, 4.5, Sonnet 4, Opus 4.5/4.6, Claude Code, Chrome 扩展, Desktop, Cowork | ~30+ |
| **OpenAI** | GPT-4o, 4.1, 4.5, 5 系列 (含 thinking/instant/codex), o3, o4-mini, 工具提示词 | ~35+ |
| **Google** | Gemini 2.0/2.5/3.0/3.1, AI Studio, Jules, NotebookLM, Workspace | ~15+ |
| **xAI** | Grok 3, 4, 4.1 beta, 4.2, API, personas | ~7 |
| **Perplexity** | comet-browser-assistant, voice-assistant | 2 |
| **其他** | Notion AI, Le-Chat, Kagi, Warp, Raycast, Sesame AI, MiniMax 等 | ~15+ |

### 历史版本追踪

仓库在 `Anthropic/old/` 目录中保存了旧版系统提示词，形成了**版本演变的历史记录**，这是该仓库的独特价值之一。

---

## 九、影响力评估

### 量化指标

| 维度 | 评分 | 说明 |
|------|------|------|
| Star 数 | ★★★★★ | 34,785 星，属于 GitHub 顶级热门项目 |
| Fork 数 | ★★★★★ | 5,594 Fork，传播极广 |
| 社区参与 | ★★☆☆☆ | 贡献者仅 19 人，主要依赖单人维护 |
| 更新频率 | ★★★★☆ | 近期月均 40+ 提交，追踪及时 |
| 文档质量 | ★★★☆☆ | README 极简，缺乏系统化索引和说明 |
| 内容深度 | ★★★★★ | 覆盖主流 AI 产品，包含完整原始提示词 |

### 定性评价

1. **行业参考价值**：该仓库是目前 GitHub 上最全面的 AI 系统提示词收集项目，对 AI 安全研究、Prompt Engineering、竞品分析等领域有重要参考意义
2. **争议性**：Issue #1 "Source?" 反映了社区对内容来源合法性的讨论；系统提示词的泄露本身涉及灰色地带
3. **无许可证**：仓库未声明任何开源许可证，这意味着内容的使用和再分发在法律上存在不确定性
4. **追踪时效性强**：维护者能在新模型发布后短时间内收录其系统提示词，保持了内容的时效性
5. **单点风险**：高度依赖单一维护者（>92% 提交），如果维护者停止更新，仓库将迅速失去价值

---

## 十、总结

`asgeirtj/system_prompts_leaks` 是一个由冰岛开发者 Ásgeir Thor Johnson 创建并维护的**纯文档收集类仓库**，专门收集和归档主流 AI 聊天机器人（ChatGPT、Claude、Gemini、Grok 等）的系统提示词泄露内容。

**核心特点**：
- 创建仅 10 个月即获得近 3.5 万 Star，增长速度极快
- 覆盖 Anthropic、OpenAI、Google、xAI 等主要 AI 厂商的最新和历史版本系统提示词
- 128 个 Markdown 文件，总计 14.5 万行内容，最大单文件近 10 万行
- 单人核心维护模式，社区贡献有限但持续
- 无许可证声明，内容使用存在法律灰色地带
- 在 AI 安全研究和 Prompt Engineering 领域具有极高的参考价值
