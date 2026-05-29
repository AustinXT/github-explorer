# Win11Debloat 网络分析报告

## 仓库基本数据

| 指标 | 值 |
|------|-----|
| 仓库全名 | Raphire/Win11Debloat |
| 描述 | 轻量级 PowerShell 脚本，可移除预装应用、禁用遥测、定制 Windows 体验，支持 Win10/Win11 |
| Star 数 | 42,399 |
| Fork 数 | 1,662 |
| Watcher 数 | 199 |
| 开放 Issue | 29（总计 27 + PR 2） |
| 主语言 | PowerShell（210KB），辅以 Batchfile（1.8KB） |
| 许可证 | MIT |
| 创建时间 | 2020-10-27 |
| 最近推送 | 2026-03-20 |
| 默认分支 | master |
| 磁盘占用 | 1.8 MB |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| Topics | windows, windows-10, windows-11, powershell, debloat, bloatware-removal, privacy, cli, automated, tweaks, registry-tweaks, cleanup, optimize 等 20 个 |
| 最新版本 | 2026.03.15（发布于 2026-03-15） |
| 发布频率 | 近期非常密集：3月连续发布 3 个版本（03.07, 03.09, 03.15），2月发布 2 个版本 |

## 作者画像

| 指标 | 值 |
|------|-----|
| 用户名 | Raphire |
| 真名 | Jeffrey |
| 所在地 | 荷兰 |
| 个人主页 | ko-fi.com/raphire（接受赞助） |
| GitHub 注册时间 | 2014-11-24 |
| 公开仓库数 | 7 |
| 关注者 | 562 |
| 关注中 | 2 |

**开发者画像**：Jeffrey 是一名来自荷兰的独立开发者，Win11Debloat 是其唯一的明星项目（42.4K star），其他项目均为小型个人作品，包括 HomeESP（IoT 项目，30 star）、SusAlert（游戏辅助，21 star）、QBD-Attack-Call-outs（游戏辅助，8 star）等。技术栈覆盖 PowerShell、JavaScript、C#、C++，显示出全栈倾向。该开发者是典型的"单项目爆款"型作者。

**贡献分布**：极度集中，Raphire 本人贡献 361 次提交，占绝对主导地位。其余 21 位贡献者各贡献 1-2 次，说明该项目本质上是单人维护的项目。

## 社区热度

**Star 增长趋势分析**：

| 时间节点 | Star 里程碑 | 增速特征 |
|----------|------------|---------|
| 2020-10 ~ 2021-02 | 早期积累 | 前几个月缓慢增长 |
| 2024-08（第 10,000 颗 star 附近） | 页面 100 采样 | 一天内获得约 100 颗 star，日均增速显著 |
| 2025-05（第 20,000 颗 star 附近） | 页面 200 采样 | 2 天约 100 颗 star，持续高速增长 |
| 2025-10（第 30,000 颗 star 附近） | 页面 300 采样 | 2 天约 100 颗 star，增长稳定 |
| 2026-02（第 40,000 颗 star 附近） | 页面 400 采样 | 单日内 100 颗 star，增速加快 |
| 当前 | 42,399 star | 处于加速增长阶段 |

**增长态势**：项目在 2024 年后进入爆发期，增速显著加快。从 2024-08 到 2026-03（约 18 个月）增长了约 32,000 star，月均增长约 1,800 star。当前仍处于高速增长期，势头强劲。这与 Windows 11 持续推广及用户对隐私和臃肿软件的关注度提升密切相关。

**社区活跃度**：
- 开放 Discussions 功能，已有活跃讨论
- 社区健康评分 57%（缺少 Code of Conduct、Contributing 指南、Issue 模板等）
- 最近提交活跃（2026-03-18 连续多次提交），维护者投入度高

## 生态网络

Win11Debloat 处于 **Windows 系统优化/去臃肿化** 生态的核心位置，属于该赛道的头部项目。相关生态：

| 生态层 | 说明 |
|--------|------|
| **核心定位** | Windows 10/11 预装应用移除 + 隐私保护 + 系统定制 |
| **技术栈** | 纯 PowerShell 脚本，无需编译，无需安装额外依赖 |
| **用户群** | 普通 Windows 用户（简易 GUI）、系统管理员（CLI + Sysprep 模式）、高级用户 |
| **分发方式** | 一行 PowerShell 命令即可运行，极低门槛 |
| **上下游关系** | 依赖 Windows 内置 PowerShell、Winget；影响 Windows 系统注册表和应用管理 |

## 官方文档洞察

| 文档资源 | 状态 |
|----------|------|
| README | 详尽，包含快速安装、功能列表、使用方法，结构清晰 |
| Wiki | 已启用，包含命令行参数、应用移除列表、默认设置、高级功能、恢复指南等 |
| Contributing 指南 | 有（.github/CONTRIBUTING.md） |
| Discussions | 已启用，有活跃社区讨论 |
| 版本发布 | 规律发布，使用日期版本号（YYYY.MM.DD），有完整的 release notes |
| 官方域名 | debloat.raphi.re（用于一键安装脚本的下载地址） |

**文档亮点**：
- 提供三种安装方式（Quick / Traditional / Advanced），覆盖不同技术水平用户
- 功能按类别清晰分组（应用移除、隐私、AI 功能、系统、更新、外观、任务栏、文件管理器等）
- 明确标注所有更改均可恢复，降低用户心理门槛
- 支持 Ko-fi 赞助

## 竞品清单

| 项目 | Star 数 | 语言 | 特点 | 状态 |
|------|---------|------|------|------|
| **ChrisTitusTech/winutil** | 49,772 | PowerShell | 综合 Windows 工具（安装程序、调优、修复、更新），YouTube 大 V 加持 | 活跃 |
| **Raphire/Win11Debloat** | 42,399 | PowerShell | 专注去臃肿和隐私保护，轻量级，GUI + CLI | 活跃 |
| **Sycnex/Windows10Debloater** | 18,791 | PowerShell | 早期 Win10 去臃肿先驱 | 已停更 |
| **hellzerg/optimizer** | 18,069 | C# | 综合 Windows 优化器，GUI 界面 | 活跃 |
| **farag2/Sophia-Script-for-Windows** | 9,153 | PowerShell | 精细化 Windows 调优脚本，功能最全面 | 活跃 |
| **builtbybel/Bloatynosy** | 5,575 | C# | Win11 专用去臃肿工具，GUI 界面 | 活跃 |
| **builtbybel/bloatbox** | 1,875 | C# | Win10 去臃肿工具 | 较老 |

**竞争格局分析**：
- Win11Debloat 在去臃肿专项领域排名第一（超越已停更的 Sycnex），仅次于功能更综合的 winutil
- 核心竞争优势：纯 PowerShell 无依赖、一行命令安装、GUI + CLI 双模式、持续活跃维护
- 与 winutil 的差异：Win11Debloat 更专注去臃肿和隐私，winutil 是综合工具箱
- 与 Sophia-Script 的差异：Win11Debloat 更注重易用性，Sophia-Script 更注重精细控制

## 关键 Issue 信号

**高评论 Issue（社区关注焦点）**：

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| #361 | 运行脚本后开始菜单搜索失效 | 39 | 已关闭 | 核心功能兼容性问题，引发广泛关注 |
| #205 | 全屏应用闪烁、桌面透出 | 28 | 已关闭 | 图形兼容性问题 |
| #131 | Win10 上 Remove-AppxPackage -AllUsers 报错 | 27 | 已关闭 | Win10 兼容性 |
| #78 | Realtek 声卡不识别耳机 | 26 | 已关闭 | 驱动兼容性（可能误删组件） |
| #510 | Get-Acl 错误 | 21 | 已关闭 | 权限问题 |
| #366 | 25H2 上无法卸载 OneDrive | 20 | 已关闭 | Windows 新版本适配 |
| #432 | 添加完整 WPF GUI（PR） | 15 | 已关闭 | 社区对 GUI 的需求 |

**当前开放 Issue**：

| # | 标题 | 信号 |
|---|------|------|
| #526 | 支持多个 AppId 进行应用移除 | 功能增强需求 |
| #525 | 高亮提示禁用隐私选项会阻止 Insider 更新 | 用户体验改进 |
| #522 | 添加导出/导入设置配置功能 | 企业级需求 |
| #521 | 静默安装仍要求确认 | CLI 使用体验 |
| #500 | 防火墙、ping 和远程桌面问题 | 兼容性问题 |

**Issue 信号总结**：高评论 Issue 集中在兼容性问题（特定硬件、特定 Windows 版本），说明脚本对系统的改动较深入。维护者对 Issue 响应积极，绝大多数高热度 Issue 已关闭解决。开放 Issue 数量低（29 个），说明维护质量高。

## 知识入口

| 平台 | 状态 | 链接 |
|------|------|------|
| GitHub Wiki | 已收录，内容丰富 | https://github.com/Raphire/Win11Debloat/wiki/ |
| Zread.ai | 已收录，包含概述、快速入门、版本兼容矩阵、更新历史等 | https://zread.ai/Raphire/Win11Debloat |
| DeepWiki | 预计已收录（42K star 项目通常会被覆盖） | https://deepwiki.com/Raphire/Win11Debloat |
| 官方安装域名 | 可用 | https://debloat.raphi.re/ |
| Ko-fi 赞助页 | 可用 | https://ko-fi.com/raphire |

## 项目展示素材

**一句话介绍**：Win11Debloat 是一个轻量级 PowerShell 脚本，让你一键移除 Windows 预装臃肿软件、禁用遥测追踪、关闭 AI 功能，快速定制清爽的 Windows 体验。

**核心卖点**：
1. **极简安装**：一行 PowerShell 命令即可运行，无需下载安装任何软件
2. **全面覆盖**：应用移除、隐私保护、AI 功能禁用、界面定制、系统优化等 8 大类功能
3. **安全可逆**：所有更改均可恢复，应用可通过 Microsoft Store 重新安装
4. **双模式**：交互式 GUI 菜单 + 强大的命令行参数，适合新手和系统管理员
5. **企业级支持**：支持 Sysprep 模式、多用户操作、Windows Audit 模式

**展示图片**：仓库包含 GUI 菜单截图 `/Assets/Images/menu.png`

**安装示例**：
```powershell
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))
```

## 快速判断

| 维度 | 评分 | 说明 |
|------|------|------|
| 热度 | ★★★★★ | 42.4K star，Windows 去臃肿领域第一名，增速加快中 |
| 维护活跃度 | ★★★★★ | 最近一周仍有多次提交，密集发布新版本（2026 年已发布 5 个版本） |
| 作者可信度 | ★★★★☆ | 单人维护超 5 年，稳定投入，但缺少团队/组织背书 |
| 社区生态 | ★★★★☆ | 有 Discussions、Wiki、贡献指南，但核心贡献者过于集中（bus factor = 1） |
| 实用价值 | ★★★★★ | 直接解决 Windows 臃肿和隐私痛点，一键可用，学习成本极低 |
| 风险因素 | ★★★☆☆ | 单人项目的可持续性风险；深度修改系统存在兼容性风险；无自动化测试保障 |

**总体评价**：Win11Debloat 是 Windows 系统去臃肿/隐私保护赛道的标杆项目，凭借极低的使用门槛和全面的功能覆盖获得了爆发式增长。项目由荷兰开发者 Jeffrey 独立维护超过 5 年，展现了极高的投入度和持续性。主要风险在于单人维护的可持续性（bus factor = 1）以及深度系统修改带来的兼容性挑战。适合推荐给所有 Windows 10/11 用户，尤其是注重隐私和系统清洁度的用户。
