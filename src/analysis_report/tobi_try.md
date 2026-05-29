# try 深度分析报告

> GitHub: https://github.com/tobi/try

## 一句话总结

Shopify CEO Tobias Lutke 的周末个人工具——一个零依赖 Ruby CLI，用 2,500 行代码解决「实验项目目录混乱」问题，emit-and-eval 架构精巧地绕过子进程改变父 Shell 状态的经典难题，「Built for developers with ADHD by developers with ADHD」的设计哲学真实而动人。

## 值得关注的理由

1. **emit-and-eval 架构值得深入学习**：Ruby 进程将决策结果编码为 Shell 脚本输出到 STDOUT，由父 Shell eval 执行——这个模式优雅地解决了 CLI 工具的经典难题（子进程无法修改父进程状态），适用于任何需要在父 Shell 中执行操作的工具
2. **Shopify CEO 仍然写代码的故事性**：身价数十亿的 CEO 在业余时间用最熟悉的 Ruby 写了一个 2,500 行的目录管理脚本，78% 的提交亲自完成，还用 AI Agent 工作流将其移植到 C——这是「CEO 即首席产品官」文化的鲜活注脚
3. **ADHD 友好设计哲学的范本**：零配置、即时可用、模糊搜索、时间感知排序、「毕业」机制——每个设计决策都服务于「降低启动摩擦」，不要求用户改变行为而是把混乱组织起来

## 项目展示

![try 模糊搜索演示](https://github.com/tobi/try/raw/main/assets/try-fuzzy-search-demo.gif)

try 的模糊搜索界面——输入片段即时匹配，最近使用的项目浮到顶部

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/tobi/try |
| Star / Fork | 3,553 / 137 |
| 代码行数 | 2,561 行核心 + 4,900 行测试（Shell 67%, Ruby 33%） |
| 项目年龄 | 7.5 个月（2025-08-19 创建） |
| 开发阶段 | 稳定维护期（v1.9.3，158 commits，脉冲式开发） |
| 贡献模式 | 创始人主导（tobi 78%）+ 25 位社区贡献者 |
| 热度定位 | 中等热度（名人效应驱动三波增长） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分，测试/代码比 1.9:1] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Tobias Lutke**（@tobi），Shopify 联合创始人兼 CEO。Ruby on Rails 核心团队早期成员，创建了 Liquid 模板引擎（已成行业标准）。GitHub 4,610 followers，86 个公开仓库。2025 年发布内部备忘录要求 Shopify 团队「在申请招聘前必须证明 AI 无法胜任该工作」。业余时间持续活跃——AudioPriorityBar（632 stars）、try（3,553 stars）是其影响力最大的两个个人项目。

### 问题判断

README 精准描述了痛点：开发者在 `/tmp/redis-test`、`~/Desktop/redis-actually`、`~/projects/testing-redis-again` 之间反复创建散落目录，事后无法找回凌晨 2 点写的精妙代码。「Your brain doesn't work in neat folders. You have ideas, you try things, you context-switch like a caffeinated squirrel.」

这不是在卖软件，而是在表达对「混乱中的创造力」的认同。Tobi 公开谈论过自己的 ADHD，try 是他应对注意力分散的个人工具。

### 解法哲学

**「不要求用户改变行为」的 ADHD 友好设计**：

- **零配置**：不需要 config 文件、不需要环境变量
- **即时可用**：`try redis` 要么跳到已有项目，要么直接创建新的
- **时间感知**：不需要记住项目名，最近用过的自动浮顶
- **模糊搜索**：`rds` 就能匹配 `redis-server`
- **「毕业」机制**：Ctrl-G 将实验升级为正式项目，留下符号链接保持可达

你继续像以前一样混乱地创建项目，try 帮你把混乱组织起来。

### 战略意图

纯个人工具，无商业化意图。MIT 许可，三渠道分发（RubyGems/Homebrew/Nix）。用 AI Agent 工作流将其从 Ruby 移植到 C（bouk/try-c）是对 AI 辅助编程的个人实验——AGENTS.md 作为 AI 协作契约展现了对这个方向的深入思考。

## 核心价值提炼

### 创新之处

1. **emit-and-eval Shell 集成架构**（新颖度 4/5 | 实用性 5/5 | 可迁移性 5/5）：Ruby 进程将决策编码为 Shell 脚本输出到 STDOUT，TUI 渲染到 STDERR，父 Shell 通过 eval 执行。优雅解决子进程修改父进程状态的经典难题，支持 bash/zsh/fish/PowerShell 四种 Shell

2. **Spec-driven 跨语言测试**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）：Markdown 规格文档 + Shell 测试套件的组合，同一行为规格验证 Ruby 原版和 C 移植版。Shell 测试通过 `--and-keys`/`--and-exit`/`--and-type` 隐藏标志注入键盘事件，支持 tmux 集成测试

3. **「毕业」机制**（新颖度 3/5 | 实用性 5/5 | 可迁移性 3/5）：Ctrl-G 将实验目录移动到正式项目位置 + 在 tries 目录留下符号链接，感知 Git Worktree（`.git` 是文件 vs 目录）自动选择 `git worktree move` 或 `mv`

4. **时间衰减评分融合模糊匹配**（新颖度 3/5 | 实用性 4/5 | 可迁移性 4/5）：`3.0 / sqrt(hours + 1)` 衰减函数——刚访问 3.0 分、1 小时前 2.1 分、一天前 0.6 分——与模糊匹配分数自然叠加

5. **AGENTS.md 作为 AI 协作契约**（新颖度 4/5 | 实用性 3/5 | 可迁移性 5/5）：不只是 AI 编码指南，而是完整的项目贡献契约（代码风格/测试要求/版本管理/安全注意事项），使 AI Agent 工作流从 Ruby 到 C 的移植成为可能

### 可复用的模式与技巧

| 模式 | 描述 | 适用场景 |
|------|------|----------|
| emit-and-eval | STDERR 用 TUI/日志、STDOUT 用 Shell 脚本、exit code 区分 eval/echo | 任何需在父 Shell 执行操作的 CLI |
| 领域特化模糊匹配 | 将领域知识（日期前缀、访问时间）编码为 base_score + 通用匹配分数叠加 | 有特定命名惯例的列表搜索 |
| 零依赖 TUI 框架 | Screen/Section/Line 分层 + 单次写入消除闪烁 + alternate screen buffer | 不依赖 curses 的交互式 CLI |
| 测试钩子注入 | `--and-keys` 注入键盘序列模拟用户交互 | 交互式 TUI 应用的自动化测试 |
| Spec-Documentation-Test 三角 | Markdown 规格 = 行为契约，Shell 测试 = 跨语言验证器 | 支持多语言实现的项目 |

### 关键设计决策

| 决策 | Trade-off |
|------|-----------|
| 零依赖（仅标准库） | 安装简单、运行可靠，但 TUI 需从零构建（835 行） |
| Shell 脚本输出而非直接执行 | 解决子进程改变父进程状态，但需用户正确配置 Shell 包装函数 |
| 单文件 try.rb（1,589 行） | 安装和理解简单，但文件略显臃肿 |
| 日期前缀自动命名 | 免去命名纠结 + 自然时间排序，但目录名较长 |
| Git Worktree 集成 | 支持分支隔离实验，但增加了毕业逻辑复杂度 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | try | zoxide | fzf | autojump | tmuxinator |
|------|-----|--------|-----|----------|------------|
| 核心功能 | 创建+组织+跳转+毕业 | 频率加权跳转 | 通用模糊搜索 | 学习型跳转 | tmux 会话 |
| 创建能力 | 有（日期前缀） | 无 | 无 | 无 | 无 |
| 目录生命周期 | 完整（创建→毕业→归档） | 仅跳转 | 仅搜索 | 仅跳转 | 仅会话 |
| 时间感知 | 原生（mtime 衰减） | 原生（frecency） | 无 | 原生（频率） | 无 |
| 依赖 | 零（标准 Ruby） | Rust 编译 | Go 编译 | Python | Ruby + tmux |
| TUI | 内建完整 TUI | 无 | 自带 | 无 | 无 |

### 差异化护城河

在「实验项目目录管理」这个细分场景上没有直接竞品。zoxide 解决「跳转到已有目录」，fzf 解决「在列表中搜索」，但没有工具同时解决「创建+命名+组织+搜索+毕业」这一完整工作流。竞争优势不在单一功能的优越性，而在工作流的完整性。Shopify CEO 的个人品牌也是独特的传播杠杆。

### 竞争风险

- 受众天花板有限——只对频繁创建实验项目的开发者有价值
- 名人效应驱动的 star 增长已过高峰，进入稳定期
- 如果 zoxide 等主流工具集成类似的「创建+命名」功能，try 的差异化将被蚕食

### 生态定位

开发者工具链中一个精准的「微工具」——不追求大而全，只解决一个具体痛点。衍生项目 bouk/try-c（C 移植版）展示了 AI 辅助跨语言移植的可能性。

## 套利机会分析

- **信息差**: emit-and-eval 架构模式在中文技术社区几乎没有被讨论过——可以写一篇「CLI 工具如何优雅修改父 Shell 状态」的技术解读
- **技术借鉴**: 零依赖 TUI 框架（835 行 Ruby）可作为学习 ANSI 终端编程的优秀教材；领域特化模糊匹配算法（137 行）展示了如何将业务知识编码到搜索排序中；测试钩子注入模式可用于任何 TUI 应用测试
- **生态位**: 「Shopify CEO 的个人工具」本身就是一个传播力极强的叙事角度；ADHD 友好设计哲学有独立的方法论价值
- **趋势判断**: AI 辅助编程（27% Copilot 参与 + AI Agent 移植到 C）是持续热点，try 作为真实案例有参考价值

## 风险与不足

1. **单人依赖**：78% 提交来自 tobi，如果 CEO 工作繁忙停止维护，社区接管动力不足
2. **Ruby 依赖门槛**：虽然零外部依赖，但需要安装 Ruby 运行时。C 移植版（bouk/try-c）可能解决此问题但由不同仓库维护
3. **try.rb 主文件过大**：1,589 行混合了 CLI 入口逻辑和 TrySelector 类，可拆分
4. **安装体验仍有痛点**：Issue #90（RubyGems）和 #51（Homebrew）均涉及安装问题，#87（Homebrew 版本滞后）仍未关闭
5. **受众天花板**：精准但狭窄的定位——只对频繁创建实验项目的 power user 有价值
6. **Shell 脚本拼接的安全风险**：虽有 `q()` 转义保护，但手动拼接 Shell 字符串总是存在边界情况

## 行动建议

- **如果你要用它**: 最适合频繁做小型实验、上下文切换频繁的开发者。`gem install try-cli` 或 `brew tap tobi/try && brew install try`。配合 Git Worktree 使用效果最佳——`try .` 为当前仓库创建隔离的实验分支
- **如果你要学它**: 重点关注三个核心设计——(1) emit-and-eval 架构（`try.rb` 的 `emit_script` 方法 + Shell 包装函数），(2) `lib/fuzzy.rb`（137 行领域特化模糊匹配，含预计算 sqrt 表和时间衰减），(3) `lib/tui.rb`（835 行零依赖 TUI 框架，Screen/Section/Line 分层 + 单次写入 + z-index）
- **如果你要 fork 它**: 最有价值的方向：(1) 将 try.rb 拆分为更清晰的模块结构；(2) 添加项目模板支持（`try redis --template=node`）；(3) 集成到 IDE（VS Code 扩展）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/tobi/try](https://deepwiki.com/tobi/try) |
| Zread.ai | 未收录 |
| 官网 | [pages.tobi.lutke.com/try](https://pages.tobi.lutke.com/try/) |
| RubyGems | [rubygems.org/gems/try-cli](https://rubygems.org/gems/try-cli) |
| 关联论文 | 无 |
| C 移植版 | [bouk/try-c](https://github.com/bouk/try-c) |
| 在线 Demo | [Asciinema 录屏](https://asciinema.org/a/ve8AXBaPhkKz40YbqPTlVjqgs) |
