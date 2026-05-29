# KaijuEngine/kaiju — Phase 1 网络分析

## 1. 仓库基本数据

| 指标 | 值 |
|------|-----|
| 名称 | kaiju |
| 全名 | KaijuEngine/kaiju |
| 描述 | General purpose 3D and 2D game engine using Go (golang) and Vulkan with built in editor |
| URL | https://github.com/KaijuEngine/kaiju |
| 主页 | https://kaijuengine.com/ |
| Stars | 4,252 |
| Forks | 177 |
| Watchers | 39 |
| Open Issues | 30 |
| Open PRs | 9 |
| Total Issues | 61 |
| Total PRs | 9 |
| 许可证 | Other（自定义许可） |
| 主语言 | Go（5.9MB） |
| 其他语言 | C（1.8MB）、C++（1.5MB）、HTML（63KB）、GLSL（57KB）、Lua（46KB）、Objective-C（40KB）、MATLAB（32KB）、Assembly（19KB）、CSS（7KB）、CMake（2KB）、Java（1KB） |
| 仓库大小 | 73.4 MB |
| 创建时间 | 2023-11-17 |
| 最后推送 | 2026-04-06（今天） |
| 默认分支 | master |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| Topics | game-engine, game-engine-2d, game-engine-3d, game-engine-development, game-engine-framework, gameengine, go, golang |
| Discussions | 7 个 |
| Wiki | 无（使用 mkdocs） |

## 2. 作者画像

### 组织账号：KaijuEngine
- 创建于 2023-11-17，与仓库同日创建
- 公开仓库 10 个，关注者 68
- 位于美国
- 主页：https://kaijuengine.com/

### 核心开发者：Brent Farris（@BrentFarris）
- **职位**：interim Lead Engine Programmer @ Tripwire Interactive（知名游戏工作室，代表作 Killing Floor 系列）
- **GitHub 注册**：2011-08-24，资深开发者
- **技术栈**：C, Go, Assembly, C++, C#
- **自述**：「We do science, because we expect design in nature.」
- **关注者**：179
- **公开仓库**：71 个
- **社交**：Twitter/X @ShieldCrush，个人博客 https://retroscience.net/
- **历史项目**：
  - Forge Networking Remastered — Unity 开源多人游戏网络库（Bearded Man Studios 出品）
  - Farris.js — HTML5 JavaScript 2D 游戏框架
  - ForgeAlloy — C# 网络库
  - go-vulkan — Go 的 Vulkan API 绑定
  - casio-fx-991cw — Casio 计算器 QR 码解析（Go）
- **核心贡献**：在 kaiju 仓库贡献 2,925 次提交，占项目绝对主导地位（>95%）
- **最新提交**：2026-04-06 `[#658] Clean up global uniforms when swap chain is remade`

### KaijuEngine 组织其他仓库
| 仓库 | 语言 | Stars | 说明 |
|------|------|-------|------|
| kaiju | Go | 4,252 | 主引擎仓库 |
| Sudoku | GLSL | 2 | Shader 写的数独（技术展示） |
| kaiju_prebuilts | JavaScript | 2 | 预编译依赖库 |
| kaiju_media_files | — | 0 | 媒体资源文件 |
| kaiju_binary_tools | — | 1 | 二进制工具 |
| kaiju_templates | — | 1 | 项目模板 |

### 其他活跃贡献者
| 用户 | 提交数 | 说明 |
|------|--------|------|
| BrentFarris | 2,925 | 创始人/主力 |
| pato98115 | 31 | 第二活跃 |
| mikenye | 18 | — |
| qwertyuu | 18 | — |
| Crazy8ball | 17 | — |
| relaxgameing | 15 | — |
| DAShoe1 | 11 | — |
| bshore | 10 | — |
| pierrec | 9 | — |
| struckchure | 8 | — |

共 21 位贡献者，但 BrentFarris 占比约 95%，属于典型的「独立开发者 + 少量社区贡献」模式。

## 3. 社区热度与增长趋势

### Star 增长时间线（月度）

| 时间段 | 新增 Stars | 说明 |
|--------|-----------|------|
| 2023-12 | 3 | 项目初期 |
| 2024-01 ~ 2024-06 | 42 | 缓慢积累期 |
| 2024-07 ~ 2024-12 | 52 | 稳定增长 |
| 2025-01 ~ 2025-10 | 32 | 低速期 |
| **2025-11** | **47** | 开始加速 |
| **2025-12** | **3,704** | 爆发式增长（HN 首页效应） |
| 2026-01 | 218 | 热度回落但仍较高 |
| 2026-02 | 81 | 趋于稳定 |
| 2026-03 | 67 | 持续稳定 |
| 2026-04 (截至4/5) | 13 | 本月进行中 |

**关键事件**：2025 年 12 月 22 日左右登上 Hacker News 首页（[HN 帖子](https://news.ycombinator.com/item?id=46205519)），单月暴增 3,704 stars，从约 160 stars 一夜跃升至 3,800+。当前累计 4,252 stars。

### 增长曲线特征
- **典型的「HN 效应」**：90%+ 的 stars 来自 2025-12 的一次 HN 首页曝光
- **后 HN 期保持健康**：月均 80-120 新 star，说明项目本身有持续吸引力
- **每日活跃开发**：主创连续推送代码至今天（2026-04-06），nightly release 每天自动发布

### Nightly Release 机制
项目使用自动化每日构建，最近 5 个 nightly 发布：
- 26.04.05.1-nightly (2026-04-05)
- 26.04.04.1-nightly (2026-04-04)
- 26.04.03.1-nightly (2026-04-03)
- 26.04.02.1-nightly (2026-04-02)
- 26.04.01.1-nightly (2026-04-01)

## 4. 生态网络

### Go 游戏引擎赛道排名

| 排名 | 项目 | Stars | 说明 |
|------|------|-------|------|
| 1 | hajimehoshi/ebiten | 13,073 | 2D 引擎，Go 游戏开发事实标准 |
| 2 | OpenDiablo2/OpenDiablo2 | 11,008 | 暗黑破坏神2开源重制（已停更） |
| 3 | faiface/pixel | 4,528 | 2D 游戏库（较不活跃） |
| **4** | **KaijuEngine/kaiju** | **4,252** | **唯一的 Go + Vulkan 3D 引擎** |
| 5 | g3n/engine | 3,072 | 3D 引擎（OpenGL，活跃度低） |

**差异化定位**：Kaiju 是 Go 生态中唯一同时支持 2D/3D 且使用 Vulkan 渲染后端的游戏引擎，也是唯一提供内置编辑器的 Go 游戏引擎。

### 依赖生态
- **Vulkan** — 现代图形 API
- **SoLoud** — C++ 音频引擎（通过 CGO 绑定）
- **Bullet3** — C++ 物理引擎（通过 CGO 绑定）
- **GLSL** — 着色器语言
- **Lua** — 脚本/Mod 支持（规划中）

## 5. 官方文档与外部洞察

### 官网 (kaijuengine.com)
- 自称「An extremely fast, open source game engine and editor, written in Go backed by Vulkan」
- 强调开发速度和构建速度优势
- 提供编辑器和纯代码两种使用方式
- 文档系统使用 mkdocs + mkdocs-material

### 社区渠道
- **Discord**：https://discord.gg/8rFPEu8U52
- **邮件列表**：https://www.freelists.org/list/kaijuengine（推荐用于详细更新）
- **X/Twitter**：@ShieldCrush
- **GitHub Sponsors**：https://github.com/sponsors/BrentFarris

### 性能声明
- Unity 空场景+立方体：~1,600 FPS
- Kaiju 同场景：~5,400 FPS（约 3.4 倍）
- 完整游戏场景（PBR、阴影、UI、音频等）debug 模式：2,712 FPS
- [作者 Twitter 截图佐证](https://x.com/ShieldCrush/status/1943516032674537958)

### DeepWiki 架构洞察
DeepWiki 对该项目有详细分析，核心架构要点：
- **Host Mediator 模式**：Host 结构体作为中心协调点，消除单例和服务定位器
- **实体-变换层次结构**：场景图采用逻辑关系和空间变换双重层次，使用脏标记延迟计算
- **三阶段渲染管线**：资产定义（JSON）-> 编译（Vulkan 对象创建）-> 执行（命令录制）
- **Cache-Then-Create 模式**：资产缓存队列化 GPU 资源创建，实现线程安全加载
- **双构建模式**：同一代码通过 build tags 编译为编辑器或游戏运行时
- **零堆分配设计**：运行时接近零新堆分配（net-0 heap allocation）

## 6. 竞品清单

| 竞品 | 语言 | 特点 | Stars | 与 Kaiju 的差异 |
|------|------|------|-------|-----------------|
| Ebitengine | Go | 2D 专精，跨平台极佳 | 13K | 无 3D，无编辑器，2D 生态更成熟 |
| g3n/engine | Go | 3D 引擎，OpenGL | 3K | OpenGL 而非 Vulkan，活跃度低 |
| faiface/pixel | Go | 2D 库 | 4.5K | 仅 2D，已较不活跃 |
| Godot | GDScript/C# | 全功能开源引擎 | 95K+ | 全面但非 Go，更重量级 |
| Bevy | Rust | ECS 架构，Vulkan | 38K+ | Rust 生态，ECS 优先，社区更大 |
| Raylib | C | 轻量级游戏库 | 25K+ | C 语言，无内置编辑器 |

**Kaiju 独特卖点**：Go + Vulkan + 内置编辑器的唯一组合，在 Go 游戏引擎赛道中是最接近「全功能引擎」的选择。

## 7. 关键 Issue 信号

| # | 标题 | 评论数 | 状态 | 标签 | 信号 |
|---|------|--------|------|------|------|
| [#489](https://github.com/KaijuEngine/kaiju/pull/489) | feat(mac-os): build and run successfully | 17 | closed | — | macOS 支持是社区高需求 |
| [#542](https://github.com/KaijuEngine/kaiju/pull/542) | chore: Added Taskfile | 13 | closed | — | 构建流程改进 |
| [#504](https://github.com/KaijuEngine/kaiju/issues/504) | Deleting/Undoing objects causes editor to crash | 12 | closed | editor | 编辑器稳定性问题 |
| [#613](https://github.com/KaijuEngine/kaiju/pull/613) | feat: Copy and Paste entity attributes | 9 | closed | — | 编辑器功能完善 |
| [#499](https://github.com/KaijuEngine/kaiju/issues/499) | Editor not rendering correctly in splash screen | 8 | closed | engine runtime, linux, amd | Linux AMD 兼容性 |
| [#621](https://github.com/KaijuEngine/kaiju/pull/621) | fix: Tag state stable btw content and stage | 6 | closed | — | 编辑器状态管理 |
| [#620](https://github.com/KaijuEngine/kaiju/pull/620) | Fix: content preview scroll reset after filter | 6 | closed | — | 编辑器 UX 修复 |
| [#655](https://github.com/KaijuEngine/kaiju/pull/655) | Feat/add texture cache to improve render performance | 2 | closed | — | 性能优化 |
| [#481](https://github.com/KaijuEngine/kaiju/pull/481) | Add CI/CD Pipeline with Vulkan config Matrix | 0 | closed | — | CI/CD 基础设施 |

**信号解读**：Issue 活动集中在编辑器功能和稳定性，说明编辑器是当前开发重心。macOS 支持的高讨论量反映跨平台需求强烈。总体 Issue 数量较少（61），与项目的「重开发」阶段一致。

## 8. 知识入口

| 来源 | 链接 | 状态 |
|------|------|------|
| DeepWiki | https://deepwiki.com/KaijuEngine/kaiju | 有详细架构分析 |
| Hacker News | https://news.ycombinator.com/item?id=46205519 | 2025-12 首页讨论 |
| HelloGitHub | https://hellogithub.com/en/repository/KaijuEngine/kaiju | 有收录 |
| daily.dev | https://app.daily.dev/posts/kaijuengine-kaiju-... | 有收录 |
| nixCraft Facebook | https://www.facebook.com/nixcraft/posts/... | nixCraft 推荐 |
| YouTube | https://www.youtube.com/watch?v=cmjX_M6lEZE | 编辑器介绍视频 |
| 官方文档 | https://kaijuengine.com/ / mkdocs | 本地可构建 |
| arxiv | — | 无相关论文 |
| Zread.ai | — | 待验证 |

## 9. 项目展示素材

### Logo
![kaiju-engine-logo](https://raw.githubusercontent.com/KaijuEngine/kaiju_media_files/master/docs/index.md/kaiju_engine_text_wide_logo.png)

### 视频素材（GitHub 托管）
| 功能 | 视频链接 |
|------|----------|
| 编辑器总览 | https://github.com/user-attachments/assets/d45511a2-2e22-4f47-a738-4affdd1cfc45 |
| 2D 模式 | https://github.com/user-attachments/assets/a3b1b53f-43ce-47bc-b1a7-1aa43c25e1a0 |
| 3D 渲染 | https://github.com/user-attachments/assets/7b5b1eb3-06ba-4827-8399-525b40d1cf09 |
| 粒子系统 | https://github.com/user-attachments/assets/09331b78-f426-47c1-ba62-b1b896f5259a |
| 骨骼动画 | https://github.com/user-attachments/assets/4e9bb101-cb09-40c3-bb03-f2a1207a04f9 |
| UI 系统 | https://github.com/user-attachments/assets/468b64c9-fb30-4b8a-83cf-1c7feee1a119 |
| 物理模拟 | https://github.com/user-attachments/assets/3bd43af8-169e-405b-bd6a-44fbfc939afd |
| 实时 Shader | https://github.com/user-attachments/assets/4b715014-ccc7-49f4-9740-d717a820665b |
| 开发速度对比 | https://github.com/user-attachments/assets/36bd06e8-dbe0-40ae-ab6a-8e8515949942 |
| 编辑器插件 | https://github.com/user-attachments/assets/4c7b7c65-f77b-47de-8d45-175dcb421afa |

### 图片素材
| 内容 | 链接 |
|------|------|
| 跨平台展示 | https://github.com/user-attachments/assets/75e56325-54aa-4133-8902-f1fd987c44f3 |
| Star 历史图 | https://api.star-history.com/svg?repos=KaijuEngine/kaiju&type=Date |

### YouTube 视频
- [Kaiju Engine Editor Introduction](https://www.youtube.com/watch?v=cmjX_M6lEZE)

## 10. 快速判断

### 亮点
1. **独特定位**：Go 生态唯一的 Vulkan 3D 游戏引擎 + 内置编辑器，填补明确空白
2. **专业背景**：创始人 Brent Farris 是 Tripwire Interactive 首席引擎程序员（Killing Floor 3），具备 AAA 级引擎开发经验
3. **极致性能**：通过精心设计实现 Go 语言下的高性能渲染，打破「GC 语言不适合游戏引擎」的偏见
4. **活跃开发**：每日推送代码 + 每日 nightly 构建，开发节奏极快
5. **全面功能**：2D/3D 渲染、物理、音频、粒子、动画、UI（HTML/CSS）、跨平台、编辑器——功能覆盖面完整
6. **爆发增长**：HN 首页后从 160 星暴增至 4,252 星，且后续增长保持健康

### 风险
1. **单人项目风险**：95%+ 代码由 BrentFarris 一人贡献，公交车因子极低
2. **编辑器未完成**：官方明确标注「编辑器仍在开发中」，engine production-ready 但 editor 不是
3. **自定义许可证**：非标准开源许可，可能影响采用
4. **社区规模小**：21 位贡献者、39 位 watchers、7 个 discussions，社区尚在萌芽
5. **Go 游戏生态薄弱**：Go 在游戏开发领域仍属小众，周边工具和资源远不如 C++/C#/Rust 生态

### 写作角度建议
- **核心叙事**：一个 AAA 引擎程序员的「周末项目」如何用 Go 重新定义游戏引擎的可能性
- **技术亮点**：Go + Vulkan 的性能突破、Host Mediator 架构、零堆分配设计
- **人物故事**：Tripwire 首席引擎师白天做 Killing Floor 3，业余时间用 Go 写出了比 Unity 快 3 倍的引擎
- **行业视角**：Go 游戏引擎赛道格局，以及 Kaiju 的「全功能引擎」差异化
