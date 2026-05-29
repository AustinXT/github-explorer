# 网络分析：basecamp/omarchy

## 仓库基本数据

| 指标 | 值 |
|------|------|
| 全名 | basecamp/omarchy |
| 描述 | Beautiful, Modern & Opinionated Linux |
| URL | https://github.com/basecamp/omarchy |
| 主页 | https://omarchy.org |
| 主语言 | Shell（336KB），辅以 Lua、CSS、Go Template、QML、JavaScript |
| 许可证 | MIT License |
| 默认分支 | dev |
| Stars | 21,323 |
| Forks | 2,133 |
| Watchers | 122 |
| Issues（总计） | 262 |
| Pull Requests（总计） | 181 |
| 磁盘占用 | 75 MB |
| 创建时间 | 2025-06-01 |
| 最近推送 | 2026-03-20 |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 当前版本 | v3.4.2 |

## 作者画像

### 组织：basecamp（37signals）

| 指标 | 值 |
|------|------|
| 登录名 | basecamp |
| 显示名 | 37signals |
| 简介 | HEY! It's in Basecamp! |
| 位置 | Chicago, IL |
| 博客 | https://37signals.com/ |
| 公开仓库 | 232 |
| 关注者 | 2,615 |
| 创建时间 | 2008-06-09 |

37signals 是全球知名的软件公司，由 Jason Fried 和 David Heinemeier Hansson（DHH）联合创办。DHH 同时是 Ruby on Rails 的创造者。公司产品包括 Basecamp（项目管理）和 HEY（邮件服务）。近期活跃仓库涵盖 basecamp-sdk（Go）、basecamp-cli（Go）、activerecord-tenanted（Ruby, 568 stars）等。

### 核心贡献者

| 排名 | 用户 | 提交数 | 角色推断 |
|------|------|--------|----------|
| 1 | **dhh** | 2,738 | 项目创始人、核心维护者（占总提交量 ~85%） |
| 2 | ryanrhughes | 302 | 核心协作者 |
| 3 | tahayvr | 18 | 活跃贡献者 |
| 4 | pomartel | 15 | 社区贡献者 |
| 5 | sgruendel | 15 | 社区贡献者 |
| 6 | alansikora | 12 | 社区贡献者 |

**特征**：DHH 亲力亲为的"独裁仁王"式项目，个人风格强烈。第二贡献者 ryanrhughes 贡献量仅为 DHH 的 ~11%。社区贡献呈长尾分布，约 30 位贡献者参与。

## 社区热度

### Star 增长曲线

| 里程碑 | 日期 | 用时 |
|--------|------|------|
| 第 1 颗 star | 2025-06-25 | — |
| 1,000 stars | 2025-07-07 | 12 天 |
| 3,000 stars | 2025-08-07 | 43 天 |
| 5,000 stars | 2025-08-26 | 62 天 |
| 8,000 stars | 2025-09-17 | 84 天 |
| 10,000 stars | 2025-09-26 | 93 天（~3 个月破万） |
| 12,000 stars | 2025-10-06 | 103 天 |
| 15,000 stars | 2025-10-24 | 121 天（~4 个月） |
| 18,000 stars | 2025-12-16 | 174 天 |
| 20,000 stars | 2026-02-17 | 237 天（~8 个月破 2 万） |
| 21,000 stars | 2026-03-10 | 258 天 |
| 21,323 stars | 2026-03-22（当前） | 270 天 |

**增长分析**：
- **爆发期**（2025-06 ~ 2025-10）：前 4 个月获得 ~15,000 stars，日均 ~125 stars。DHH 的个人影响力 + Hacker News 效应 + Linux 桌面话题性驱动。
- **稳定期**（2025-10 ~ 2026-03）：后 5 个月获得 ~6,300 stars，日均 ~42 stars。增速下降但仍保持可观的日均水平。
- **当前热度**：近 30 天获得 ~1,300 stars（日均 ~43），说明项目仍具持续吸引力。

### 发版节奏

| 版本 | 发布日期 |
|------|----------|
| v3.4.2 | 2026-03-08 |
| v3.4.1 | 2026-02-28 |
| v3.4.0 | 2026-02-26 |
| v3.3.3 | 2026-01-08 |
| v3.3.2 | 2026-01-08 |

从 2025-06 发布至今已迭代到 v3.4.2，版本号从 1.x 快速演进到 3.x，发版频率高，维护活跃。

## 生态网络

### 上游依赖
- **Arch Linux**：底层 Linux 发行版
- **Hyprland**：Wayland 合成器/平铺式窗口管理器
- **Waybar**：状态栏
- **Walker**：GTK4 Wayland 原生启动器
- **Alacritty / Kitty / Ghostty**：终端模拟器
- **Btrfs + Snapper**：文件系统快照与恢复
- **SDDM**：显示管理器
- **Mako**：通知守护进程
- **pacman / yay**：包管理器

### 兄弟项目
- **Omakub**（basecamp/omakub）：DHH 的 Ubuntu 版 "opinionated" 开发环境配置工具，面向初学者，使用 GNOME 桌面。Omarchy 是其"进阶版"。
- **Omacom**（learn.omacom.io）：Omarchy 的官方学习平台/手册。

### 生态组件
- **Elephant Desktop Components**：Omarchy 自研的应用启动器和桌面集成层，作为 Walker 的数据提供者。
- **Voxtype**：语音听写守护进程（从 PR #5082 可见正在集成）。
- **omarchy-online.iso**：官方安装镜像，通过 iso.omarchy.org 分发。

### 硬件生态
- 支持 Intel、Apple T2、Microsoft Surface 等硬件配置
- 被推荐为"$499 Mac Killer"——搭配迷你 PC 使用

## 官方文档洞察

### 主站（omarchy.org）
- 简洁的着陆页，展示当前版本 v3.4
- 提供 ISO 下载链接
- 链接到 Discord 社区、GitHub 源码、Omacom 手册
- Cloudflare 赞助托管

### 学习平台（learn.omacom.io）
- 完整的 Omarchy 手册，覆盖：
  - 安装指南（在线/本地两种方式）
  - 系统架构说明（7 层架构）
  - 主题系统（原子切换、15+ 应用联动）
  - 包管理策略（声明式包清单，148+ 基础包）
  - 迁移系统（幂等迁移脚本）
  - 桌面组件（Elephant 系统）

### DHH 博客文章
- [Omarchy is out](https://world.hey.com/dhh/omarchy-is-out-4666dd31)（2025-06 发布公告）
- [Omarchy 2.0](https://world.hey.com/dhh/omarchy-2-0-16fefc15)（2025-08 版本发布）
- 核心理念："You could setup this, not change a thing, and you'll have exactly what I run every day."

## 竞品清单

| 竞品 | 定位 | 与 Omarchy 差异 |
|------|------|-----------------|
| **Omakub**（DHH） | Ubuntu + GNOME 开发环境 | 同一作者的"入门版"，更易上手，但自由度较低 |
| **Arch Linux（原版）** | 极简 DIY 发行版 | 需要大量手动配置，Omarchy 提供开箱即用体验 |
| **EndeavourOS** | 友好化的 Arch | 更通用，不针对开发者，无统一设计哲学 |
| **Manjaro** | 预配置的 Arch 衍生版 | 更面向普通用户，桌面选择多但不"opinionated" |
| **NixOS** | 声明式 Linux 发行版 | 可复现性更强但学习曲线极陡 |
| **Fedora Workstation** | 企业级桌面 Linux | 更稳定保守，不追求极致定制 |
| **Linux Mint** | 新手友好桌面 Linux | 完全不同的目标用户群 |
| **Ubuntu Desktop** | 最流行的桌面 Linux | 通用性强但缺乏个性化 |

**差异化定位**：Omarchy 是唯一一个由知名开发者（DHH）亲自维护的"作者品味驱动型"Linux 发行版，强调美学与开发体验的统一，不追求通用性。

## 关键 Issue 信号

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| [#1414](https://github.com/basecamp/omarchy/issues/1414) | Use NetworkManager instead of systemd-networkd | 97 | open | **架构决策争论**：社区强烈要求切换网络管理方案 |
| [#3891](https://github.com/basecamp/omarchy/issues/3891) | Videos not playing after recent update (v3.2.3) | 90 | open | **回归 bug**：更新导致视频播放中断，用户影响面大 |
| [#3899](https://github.com/basecamp/omarchy/issues/3899) | Chromium GPU/Ozone errors after update to 3.2.3 | 83 | closed | **GPU 兼容性**：已修复，反映 Wayland 下浏览器兼容挑战 |
| [#1897](https://github.com/basecamp/omarchy/pull/1897) | Add aarch64 support for Omarchy 3.x | 82 | open | **ARM 架构支持**：高需求功能，社区期待 |
| [#688](https://github.com/basecamp/omarchy/issues/688) | Hyprland doesn't start after upgrade to 1.13 | 73 | closed | **早期升级问题**：已解决，说明快速迭代的阵痛 |
| [#26](https://github.com/basecamp/omarchy/issues/26) | System Freeze on Wake-up | 56 | closed | **电源管理**：早期核心问题，已修复 |
| [#1417](https://github.com/basecamp/omarchy/pull/1417) | Add hibernation support | 57 | closed | **电源管理增强**：社区贡献 |
| [#2909](https://github.com/basecamp/omarchy/pull/2909) | Switch to NetworkManager | 36 | open | **执行中**：对应 #1414 的实际实现 PR |
| [#4525](https://github.com/basecamp/omarchy/pull/4525) | Omarchy 3.4.0 | 25 | closed | **版本发布 PR**：社区反馈活跃 |

**Issue 信号总结**：
- 网络管理（NetworkManager vs systemd-networkd）是当前最大的架构争论
- GPU/视频兼容性是 Wayland 生态的典型痛点
- ARM（aarch64）支持呼声高，说明用户群有硬件多样性诉求
- 社区活跃度高，Issue 讨论深入且参与人数多

## 知识入口

| 平台 | 链接 | 内容质量 |
|------|------|----------|
| **DeepWiki** | https://deepwiki.com/basecamp/omarchy | 高质量架构文档，涵盖 7 层架构、安装管线、主题系统、包管理策略等 |
| **Zread.ai** | https://zread.ai/basecamp/omarchy | 可搜索的文档系统，涵盖安装先决条件、桌面组件、包管理等 |
| **Omacom** | https://learn.omacom.io/2/the-omarchy-manual | 官方学习手册 |
| **GitHub** | https://github.com/basecamp/omarchy | 源码 + Issues + PRs |
| **Grokipedia** | https://grokipedia.com/page/omarchy | 百科式摘要 |
| **omarchy.org** | https://omarchy.org | 官方着陆页 + ISO 下载 |

## 项目展示素材

### README 概述
README 极其简洁（仅 3 行有效内容）：
> Omarchy is a beautiful, modern & opinionated Linux distribution by DHH.
> Read more at omarchy.org.

无截图、无功能列表、无安装指南——全部外链到官网和 Omacom。这符合 DHH 的风格：简洁到极致。

### 目录结构亮点
```
├── boot.sh          # 引导安装脚本
├── install.sh       # 主安装脚本
├── install/         # 安装模块（模块化管线）
├── config/          # Hyprland、Waybar 等配置
├── themes/          # 主题系统（原子切换）
├── migrations/      # 幂等迁移脚本
├── applications/    # 应用配置
├── bin/             # 工具脚本
├── default/         # 默认配置
└── version          # 当前版本号（3.4.2）
```

### 展示要点
- 37signals 宣布全公司将在三年内迁移到 Omarchy
- DHH 引用语："You could setup this, not change a thing, and you'll have exactly what I run every day."
- 被媒体称为"$499 Mac Killer"——搭配迷你 PC 即可获得高质量开发体验
- 版本演进速度：9 个月内从 v1.0 迭代到 v3.4.2

## 快速判断

| 维度 | 评分 | 说明 |
|------|------|------|
| **影响力** | ★★★★★ | 21K+ stars，DHH 个人品牌加持，主流科技媒体（The New Stack、TechForward 等）深度报道 |
| **活跃度** | ★★★★★ | DHH 本人每日提交，最近推送 2026-03-20，发版频率高（v3.4.2），PR 和 Issue 持续流入 |
| **成熟度** | ★★★★☆ | 9 个月内迭代到 v3.x，功能基本完整，但仍有 NetworkManager、ARM 支持等重要功能待完善 |
| **社区** | ★★★★☆ | Discord 活跃（3,500+ 早期用户），Issue 讨论深入，但贡献集中在 DHH 个人（85% 提交量） |
| **可持续性** | ★★★★☆ | 37signals 企业背书 + DHH 强个人投入，但高度依赖单人维护存在"巴士因子"风险 |
| **创新性** | ★★★★☆ | 将"opinionated"理念从 Web 框架（Rails）带入 Linux 桌面，7 层架构设计、原子主题切换、幂等迁移系统在 Linux 发行版中罕见 |

### 一句话总结
Omarchy 是 DHH 将 Ruby on Rails 的"Convention over Configuration"哲学移植到 Linux 桌面的野心之作——基于 Arch + Hyprland，面向开发者，9 个月 21K stars，37signals 全公司背书，是当前最具话题性的个人品味驱动型 Linux 发行版。
