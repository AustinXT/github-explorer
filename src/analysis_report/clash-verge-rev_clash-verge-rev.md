# Clash Verge Rev 深度分析报告

> GitHub: https://github.com/clash-verge-rev/clash-verge-rev

## 一句话总结

已停更 Clash Verge 的社区复活版本，基于 Tauri 2 + Rust + React 构建的跨平台代理管理 GUI 客户端，以 107K+ Stars、单版本近百万下载量和 13 种语言支持，成为 Clash 生态系统中用户量最大的桌面客户端，填补了 Clash for Windows 停更后的生态空白。

## 值得关注的理由

1. **开源社区「火种传递」的典型案例**：原 Clash Verge 作者 zzzgydi 于 2023 年停止维护，rev 团队在一个月内 fork 并接力开发，从 v1.3.8 迭代到 v2.4.7，Star 数从零增长到 107K+，验证了开源生态中「不可或缺」的工具一旦停更社区会迅速填位的规律
2. **Tauri 2 框架的大规模生产级标杆**：98K 行代码（19.6K 行 Rust + 42.7K 行 TypeScript/TSX），使用 Tauri 2 + Rust 后端 + React 前端的全技术栈，对研究「如何用 Tauri 构建需要深度系统集成的桌面应用」极有参考价值
3. **系统级代理管理的工程复杂度**：同时处理 TUN 虚拟网卡、系统代理守护、服务模式/Sidecar 模式切换、多平台权限提升、DNS 配置注入等复杂系统集成问题，且需要在 Windows/macOS/Linux 三平台上保持一致体验

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/clash-verge-rev/clash-verge-rev |
| Star / Fork | 107,982 / 7,850 |
| 代码行数 | 98,413 行总计（Rust 19,611 行 + TSX 29,946 行 + TypeScript 12,834 行 + YAML 8,189 行 + JavaScript 3,762 行） |
| 项目年龄 | 2.4 年（2023-11-21 创建，fork 自 zzzgydi/clash-verge） |
| 开发阶段 | 成熟活跃（dev 分支 50 次提交，最新提交 2026-04-06，v2.4.7 发布于 2026-03-21） |
| 贡献模式 | 社区驱动 + 核心团队（zzzgydi 原作者 1,022 次贡献，Tunglies 709 次，MystiPanda 429 次，wonfen 402 次，huzibaca 360 次，Slinetrac 308 次） |
| 许可证 | GPL-3.0 |
| 热度定位 | 超级热门（GitHub 全站 Top 100 级别，v2.4.7 单版本下载量 99.9 万次） |
| 质量评级 | 代码[优秀] 文档[良好·多语言 README] 测试[基础·少量单元测试] |

## 作者视角：为什么存在这个项目

### 创始人/核心团队背景

原 Clash Verge 由 **zzzgydi**（1,022 次贡献）创建，bio 为「Coding for fun」，2017 年注册 GitHub，拥有 1,229 followers。zzzgydi 是一位低调的开发者，在 2023 年 11 月前后停止了对 Clash Verge 的维护。

Clash Verge Rev 的核心维护者团队在几乎同一时间（2023-11-30）组建了 clash-verge-rev 组织，迅速接手项目：

- **Tunglies**（709 次贡献）：位于中国，bio「Box::new(dyn Me::Code())」，当前最活跃的核心维护者
- **MystiPanda**（429 次贡献）：与 rev 组织同一天注册 GitHub（2023-11-30），专门为此项目创建的账号
- **wonfen**（402 次贡献）：早期核心贡献者
- **huzibaca**（360 次贡献）：持续活跃贡献者
- **Slinetrac**（308 次贡献）：重要贡献者

组织层面：clash-verge-rev 拥有 5,468 followers、18 个公开仓库，官网 [clashverge.dev](https://www.clashverge.dev)，TG 频道 @clash_verge_rev。

### 问题判断

2023 年下半年，中国互联网「翻墙工具」领域发生了一场系统性停更潮：

1. **Clash for Windows 停更**（2023-11-02）：用户量最大的 Clash GUI 客户端突然删库
2. **Clash 原始内核停更**（2023-11-02）：Dreamacro 的 Clash 核心删库
3. **Clash Verge 停更**（2023 年底）：zzzgydi 停止维护

这场连锁停更创造了巨大的用户真空。数十万用户需要一个仍在维护的跨平台 Clash GUI 客户端。Clash Verge Rev 精准地填补了这一空白，同时 MetaCubeX/mihomo 接手了内核的维护工作。

### 解法哲学

Clash Verge Rev 的设计理念体现在以下维度：

1. **延续而非颠覆**：保持了原 Clash Verge 的核心 UX 范式和代码架构，降低用户迁移成本，rev 名称本身就暗示「revived（复活）」
2. **性能优先**：选择 Tauri 2（Rust + WebView）而非 Electron，应用体积仅约 10MB（Electron 方案通常 100MB+），内存占用显著更低
3. **双模式运行**：支持 Service 模式（系统服务，TUN 所需）和 Sidecar 模式（直接启动核心进程），兼顾安全性和易用性
4. **配置增强系统**：通过 Merge（YAML 合并）+ Script（Boa JS 引擎执行脚本）+ SeqMap（有序编辑 rules/proxies/groups）的三层增强机制，让用户无需手动修改原始配置文件即可定制代理规则

明确不做的：不做自有内核（完全依赖 mihomo），不做移动端（专注桌面三平台），不做商业化（GPL-3.0 + 接受 sponsor 捐赠）。

### 战略意图

- 成为 Clash 生态系统中**标准桌面 GUI 客户端**
- 保持与 mihomo 内核的紧密集成和快速跟进
- 通过社区贡献和多语言支持建立全球用户基础

## 架构与设计决策

### 整体架构：Tauri 2 双进程模型

```
┌─────────────────────────────────────────────────────┐
│                   前端 (WebView)                      │
│  React + MUI + TanStack Query + Monaco Editor        │
│  src/pages/   → 8 个主页面                            │
│  src/components/ → 模块化 UI 组件                     │
│  src/services/  → API 通信 + 状态管理                 │
├─────────────────────────────────────────────────────┤
│              Tauri IPC Bridge (命令层)                 │
│  src-tauri/src/cmd/ → 70+ 个 Tauri 命令               │
├─────────────────────────────────────────────────────┤
│                 后端 (Rust)                            │
│  core/    → 核心管理器、服务、系统代理、热键、托盘      │
│  config/  → 配置层（Clash/Verge/Profiles）            │
│  enhance/ → 配置增强引擎（Merge + Script + Seq）      │
│  feat/    → 功能实现（代理、备份、窗口管理）            │
│  module/  → 轻量模式、自动备份                        │
│  utils/   → 系统工具（DNS、窗口、单例、服务端）        │
├─────────────────────────────────────────────────────┤
│             Crates（功能模块库）                       │
│  clash-verge-signal   → 跨平台信号处理                │
│  clash-verge-logging  → 结构化日志                    │
│  clash-verge-i18n     → 国际化（编译时类型安全）       │
│  clash-verge-limiter  → 速率限制                      │
│  clash-verge-draft    → 草稿系统                      │
│  tauri-plugin-sysinfo → 系统信息插件                  │
├─────────────────────────────────────────────────────┤
│          Clash Core (mihomo 外部进程)                  │
│  通过 IPC (Unix Socket / Named Pipe) 通信             │
│  支持 Service 模式 / Sidecar 模式                     │
└─────────────────────────────────────────────────────┘
```

### 关键设计决策

**1. 核心管理双模式（Service vs Sidecar）**

`CoreManager` 通过 `RunningMode` 状态机管理 mihomo 核心进程的生命周期：
- **Service 模式**：通过 `clash-verge-service` 系统服务管理核心进程，支持 TUN 模式（需要管理员权限）。使用 IPC（Unix Socket）通信，具备自动重连和版本检查机制
- **Sidecar 模式**：直接通过 Tauri Shell 插件启动核心进程，无需安装服务，但不支持 TUN

权限提升策略针对各平台定制：Windows 使用 `runas` UAC 提升，macOS 使用 `osascript` AppleScript 弹窗，Linux 优先 `pkexec` 并回退到 `sudo`。

**2. 配置增强引擎（enhance 模块）**

这是项目最具创新性的架构设计。用户的代理配置经过六层处理管线：

```
原始订阅配置 → Global Merge → Global Script → Profile Rules/Proxies/Groups
→ Profile Merge → Profile Script → Builtin Scripts → TUN 注入
→ DNS 设置 → 最终运行时配置
```

Script 引擎使用 **Boa**（Rust 实现的 ECMAScript 引擎）执行用户自定义 JavaScript，并设有安全限制（最大 1000 条日志输出、单条 1MB、JSON 总大小 10MB）。这让用户可以用 JavaScript 编写复杂的配置转换逻辑而不需要修改源码。

**3. 轻量模式（Lightweight Mode）**

独特的内存优化机制：在用户关闭窗口后启动计时器，超时后**销毁 WebView**（而非仅隐藏），释放前端所有内存，仅保留 Rust 后端和系统托盘运行。用户再次点击托盘时重新创建 WebView。使用原子操作（`AtomicU8`）实现状态机（Normal → In → Exiting），保证线程安全的状态转换。

**4. 系统代理守护（Sysopt）**

通过 `sysproxy-rs`（自维护的系统代理设置库）管理 OS 级代理配置，支持：
- 全局 HTTP/SOCKS5 代理设置
- PAC（自动配置脚本）模式
- 代理守护（Guard）：定期检查并修复被其他程序篡改的系统代理设置
- 各平台定制的 bypass 列表

**5. 前端技术选型迁移**

最近的 dev 分支正在进行重要的技术栈迁移：
- SWR → TanStack Query v5（更强大的缓存和状态管理）
- react-virtuoso → @tanstack/react-virtual（虚拟滚动）
- 修复了 Monaco Editor 内存泄漏问题

### 项目模块拆解

| 模块 | 文件变更频率排名 | 功能 |
|------|---------|------|
| `src/locales` | #1 (153次) | 13 种语言的国际化翻译 |
| `src/components` | #2 (135次) | React UI 组件库 |
| `src-tauri/src` | #3 (130次) | Rust 后端核心逻辑 |
| `src/hooks` | #4 (49次) | React 自定义 Hooks |
| `crates/clash-verge-i18n` | #5 (41次) | Rust 侧国际化支持 |
| `src/pages` | #6 (37次) | 8 个主页面组件 |

## 创新点

### 1. Boa JS 引擎驱动的配置脚本系统

在桌面代理客户端中首创使用 Rust 原生 JavaScript 引擎（Boa）来执行用户配置脚本。相比 Node.js 子进程或内嵌 V8，Boa 体积极小、启动即时、天然沙箱化，是安全执行用户代码的优雅方案。

### 2. WebView 销毁式轻量模式

不同于常规的窗口隐藏或最小化到托盘，Clash Verge Rev 在轻量模式下**完全销毁 WebView 进程**，将内存占用从前端运行时的 100-200MB 降低到仅 Rust 后端的 10-20MB。这对需要 24 小时后台运行的代理工具至关重要。

### 3. 代理链可视化编辑

`proxy-chain.tsx` 组件提供了代理链（Proxy Chain）的可视化拖拽编辑，使用 `@dnd-kit/sortable` 实现，让用户可以直观地组合多层代理。

### 4. 流媒体解锁检测

内置了对 Netflix、YouTube Premium、Disney+、Spotify、ChatGPT、Claude、Gemini、Bilibili、TikTok 等 12 个主流服务的解锁状态检测（Rust 原生实现），帮助用户快速验证节点可用性。

### 5. WebDAV 配置同步

支持通过 WebDAV 协议将配置文件备份到私有云存储，实现多设备间的配置同步，使用 `reqwest_dav` 库实现。

## 可复用模式

### 1. Tauri 2 系统级桌面应用架构模式

**适用场景**：需要深度系统集成的跨平台桌面应用

关键模式：
- 系统服务 + Sidecar 双模式核心管理
- `ArcSwap` 实现无锁状态共享
- `once_cell::Lazy` + `Mutex` 管理全局单例
- 平台条件编译（`#[cfg(target_os)]`）处理差异

### 2. 配置增强管线模式

**适用场景**：任何需要用户自定义配置转换的应用

模式：原始配置 → Merge 层（YAML 合并）→ Script 层（JS 脚本转换）→ Builtin 规则 → 最终配置。每层独立、可跳过、有日志追踪。

### 3. WebView 生命周期管理模式

**适用场景**：需要长时间后台运行的 Tauri/Electron 应用

模式：Window Close → Timer Start → Timer Fire → WebView Destroy → Tray Click → WebView Recreate，配合 AtomicU8 状态机保证并发安全。

## 竞品交叉分析

| 维度 | Clash Verge Rev | Clash Nyanpasu | v2rayN | Hiddify |
|------|----------------|----------------|--------|---------|
| Stars | 107,982 | 12,905 | 100,847 | 28,267 |
| 框架 | Tauri 2 (Rust) | Tauri (Rust) | .NET WPF | Flutter |
| 内核 | mihomo 专用 | mihomo + 传统 Clash + Rust 内核 | Xray/V2Ray/Sing-box | Sing-box |
| 平台 | Win/Mac/Linux | Win/Mac/Linux | Windows 为主 | Win/Mac/Linux/iOS/Android |
| 体积 | ~10MB | ~15MB | ~30MB | ~50MB |
| 定位 | Clash 生态标准 GUI | Clash 生态多核心支持 | V2Ray 生态老牌客户端 | 通用全平台客户端 |
| 配置增强 | Merge + Script + Seq | Profile 增强 | 内置路由规则 | 内置策略 |
| 特色功能 | 轻量模式、流媒体检测、WebDAV 同步 | 多内核切换、Clash 字段设置 | V2Ray 全协议支持 | 一键连接、自动选节点 |

**竞争格局分析**：

Clash Verge Rev 在 Clash 生态中占据**绝对领先地位**——其 Star 数是第二名 Clash Nyanpasu 的 8.4 倍。两者都 fork 自 zzzgydi/clash-verge，但 Rev 的策略是「聚焦 mihomo + 精致体验」，Nyanpasu 则走「多核心兼容」路线。从下载量看，Rev 单版本近百万下载碾压同类。

在更广泛的代理客户端领域，v2rayN（100K Stars）专注 V2Ray/Xray 生态且以 Windows 为主，Hiddify（28K Stars）走全平台路线但使用 Sing-box 内核。Clash Verge Rev 的差异化在于：**面向 Clash/mihomo 生态的最佳桌面体验**。

## 代码质量

### 优势
- **Rust 后端架构清晰**：模块划分合理（core/config/enhance/feat/module），职责单一
- **类型安全**：前端 TypeScript 严格模式，后端 Rust 强类型 + 编译时 i18n 键检查
- **并发安全**：使用 `ArcSwap`、`parking_lot::RwLock`、`AtomicU8` 等无锁/低锁原语
- **错误处理**：大量使用 `anyhow::Result` + `context()` 提供有意义的错误链

### 不足
- **测试覆盖不足**：仅在 `enhance/mod.rs` 中发现少量单元测试，缺少集成测试和 E2E 测试
- **commit 规范**：近 50 次提交中 fix 占 42%（21/50），暗示快速迭代中 bug 引入率较高
- **部分中文日志/注释**：日志系统混合使用中英文，对国际贡献者不够友好

## 社区热度

### Star 增长趋势

项目创建后一天内（2023-11-22）即获得大量 Star，反映了 Clash 生态用户群体对替代品的强烈需求。第一页 100 个 Star 在 2023-11-22 至 2023-11-23 两天内完成，增长极为陡峭。

### 下载量（v2.4.7 单版本，2026-03-21 发布）

| 平台 | 下载量 |
|------|--------|
| Windows x64 安装包 | 378,678 |
| macOS Apple Silicon | 400,145 + 36,021 (tar.gz) |
| macOS Intel | 53,977 + 12,708 (tar.gz) |
| Linux amd64 deb | 47,349 |
| 其他（ARM、RPM 等） | 70,134 |
| **总计** | **~999,012** |

macOS Apple Silicon 下载量（40 万+）超过 Windows x64（37.8 万），反映了用户群体中 Mac 用户占比极高——这与代理工具用户画像（开发者、技术从业者）高度吻合。

### 关键 Issue 信号

| Issue | 讨论量 | 信号 |
|-------|--------|------|
| [#5702](https://github.com/clash-verge-rev/clash-verge-rev/issues/5702) 核心会随机挂掉 | 99 条评论 | 最热门的 open issue，涉及上游 mihomo 内核稳定性 |
| [#550](https://github.com/clash-verge-rev/clash-verge-rev/issues/550) 拨号上网 TUN 模式失败 | 82 条评论 | 中国特色网络环境下的兼容性问题 |
| [#1311](https://github.com/clash-verge-rev/clash-verge-rev/issues/1311) 多订阅用户扩展配置不友好 | 57 条评论 | 配置管理的核心痛点 |
| [#5382](https://github.com/clash-verge-rev/clash-verge-rev/issues/5382) v2.4.3 导致无法访问网络 | 51 条评论 | 版本升级的稳定性问题 |
| [#3428](https://github.com/clash-verge-rev/clash-verge-rev/issues/3428) 存在提权漏洞 | 47 条评论 | 安全性问题——服务模式的权限管理挑战 |

### 发版节奏

| 版本 | 发布日期 | 间隔 |
|------|---------|------|
| v2.4.7 | 2026-03-21 | 30 天 |
| v2.4.6 | 2026-02-19 | 25 天 |
| v2.4.5 | 2026-01-25 | 37 天 |
| v2.4.4 | 2025-12-19 | 41 天 |
| v2.4.3 | 2025-11-08 | 62 天 |
| v2.4.2 | 2025-09-07 | — |

平均约每 5-6 周发布一个稳定版本，期间穿插 RC 预发布版本。节奏稳健。

## 知识入口

- **官方文档**：[clash-verge-rev.github.io](https://clash-verge-rev.github.io/)
- **FAQ**：[常见问题页面](https://clash-verge-rev.github.io/faq/windows.html)
- **Telegram 频道**：[@clash_verge_rev](https://t.me/clash_verge_re)
- **贡献指南**：[CONTRIBUTING.md](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/CONTRIBUTING.md)
- **内核文档**：[mihomo Wiki](https://wiki.metacubex.one/)

## 快速判断

**谁应该关注这个项目？**

- **代理工具用户**：目前 Clash 生态中最成熟、下载量最大的桌面 GUI 客户端
- **Tauri 2 开发者**：学习如何用 Tauri 2 构建需要系统服务、权限提升、TUN 虚拟网卡等深度系统集成的桌面应用
- **Rust 桌面应用开发者**：配置增强引擎（Boa JS + YAML merge + SeqMap）、WebView 生命周期管理、跨平台服务管理等模式极具参考价值
- **开源项目运营者**：从用户需求空白到 107K Stars 的社区运营案例值得研究

**风险提示**

- 项目依赖 mihomo 内核，内核层面的问题（如 #5702「核心随机挂掉」）非 GUI 层面可控
- GPL-3.0 许可证限制了商业衍生使用
- 代理工具在某些法律辖区存在合规风险
- 服务模式涉及系统权限提升，安全性需持续关注（曾有 #3428 提权漏洞报告）
