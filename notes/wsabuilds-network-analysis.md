# WSABuilds 网络分析报告

## 仓库基本数据
- Star / Fork / Watcher: 16,467 / 2,244 / 153
- 语言: Python (44.7%), Shell (39.4%), PowerShell (15.5%), Batchfile (0.4%), HTML (0.1%)
- License: GNU AGPL v3.0（强 copyleft，商业使用需开源衍生代码）
- 创建时间: 2022-12-30 | 最近推送: 2026-01-16
- 话题标签: windows, windows-10, windows-11, magisk, google-apps, android, subsystem, android-emulator, kernelsu, windowssubsystemforandroid, magiskonwsa, wsapatch, wsa, wsa-root, wsa-with-gapps-and-magisk
- 已归档: 否 | 是Fork: 否
- 磁盘用量: ~157 MB
- 官网: 无（homepageUrl 为空）
- 社区入口: [Discord](https://discord.gg/2thee7zzHZ) | [XDA Forums](https://xdaforums.com/t/wsabuilds-latest-windows-subsystem-for-android-wsa-builds-for-windows-10-and-11-with-magisk-and-google-play-store.4545087/)

## 作者画像
- 姓名/ID: MustardChef | 公司: 未公开 | 位置: 未公开
- 粉丝: 1,004 | 公开仓库: 19 | 账号年龄: ~5.7 年（2020-07 创建）
- Bio: 未填写 | Blog: 无
- 此 repo 投入权重: **高** — WSABuilds 占其全部 star 数的 95%+，是绝对核心项目；另有 WSAPackages (243 star)、GPGPCToolkit (201 star) 等相关项目，形成 WSA 生态矩阵
- 作者类型: **独立开发者** — 无公司标注，不隶属任何组织，个人身份信息极少
- 贡献集中度: **单人主导** — MustardChef 贡献 912 次 (63%)，第二名 Howard20181 仅 166 次 (12%)，第三名 PeterNjeim 160 次 (11%)。核心开发由作者一人驱动
- 背景推断: 专注于 Windows + Android 生态的技术爱好者，具有 Magisk/root、GApps 集成、PowerShell/Shell 自动化构建方面的深厚经验。从 XDA 社区起步，逐步成为 WSA 社区中最活跃的预构建分发者。匿名度较高，几乎无个人信息公开

## 社区热度
- 热度级别: **大众热门** — 16.4K star，在 WSA 生态中排名第一
- 增长模式: **持续增长 + 事件驱动爆发**
  - 早期（2023-01 ~ 2023-05）：稳定增长，月均 ~190 star
  - 成长期（2023-06 ~ 2024-03）：加速增长，月均 ~420 star，2024-02 达到 583
  - 平台期（2024-04 ~ 2025-09）：稳定在月均 ~300 star
  - **爆发期（2025-10 ~ 2025-12）**：2025-11 月单月 2,037 star（历史峰值），这与微软正式终止 WSA 支持（2025-03）后用户大量涌入寻找替代方案直接相关
  - 回落期（2026-01 至今）：月均 ~430 star，仍远高于历史平均水平
- 近期趋势: 2025 年底出现井喷式增长后逐步回落，但仍保持较高热度。项目已进入 LTS 维护阶段，最近一次推送在 2026-01-16
- 套利判断: **事件驱动型热度** — 微软宣布终止 WSA 支持是增长的核心推动力。项目在"后 WSA 时代"承担了社区维护的关键角色，具有较强的不可替代性。但长期来看，随着 WSA 底层技术逐渐过时（Windows 更新可能持续破坏兼容性），增长将逐步放缓

## 生态网络
- 上游依赖:
  - **LSPosed/MagiskOnWSALocal** (10.5K star) — 核心构建脚本来源，WSABuilds 基于此进行预构建和分发
  - **Microsoft WSA** — 底层 Windows Subsystem for Android 运行时（已停止官方支持）
  - **Magisk / KernelSU** — Root 方案
  - **MindTheGapps** — Google Play 服务集成方案
  - **cinit/WSAPatch** — Windows 10 兼容补丁
- 同类项目:
  - **LSPosed/MagiskOnWSALocal** (10,469 star) — "自己动手构建"方案，WSABuilds 的上游
  - **YT-Advanced/WSA-Script** (1,028 star) — 基于 GitHub Actions 的 WSA 构建脚本
  - **Lyxot/WSAOnWin10** (452 star) — 专注 Win10 的 WSA 方案
  - **MustardChef/WSAMagiskDelta** (304 star) — 作者自己的 Magisk Delta 变体

## 官方文档洞察
- homepageUrl 为空，无独立官网
- README 即为主文档，内容极其详尽：包含版本兼容矩阵、系统要求、下载链接、已知问题、虚拟化配置指南
- 文档结构化程度高：使用折叠面板、表格、emoji 状态标识，面向终端用户设计
- XDA Forums 有专属帖子，是另一个重要社区互动渠道
- Discord 服务器作为实时支持渠道
- 作者视角要素：
  - 项目定位明确 —"让普通用户无需折腾 Linux/WSL 即可获得带 Google Play 和 Root 的 WSA"
  - 强调 LTS 长期支持承诺，即使微软已停止 WSA 支持
  - 透明的版本状态追踪（项目看板）
  - 提供 OneDrive 镜像下载，应对 GitHub Release 下载限速

## 竞品清单

| 项目 | Star | 定位 | 差异点 |
|------|------|------|--------|
| LSPosed/MagiskOnWSALocal | 10,469 | 本地构建 WSA + Magisk + GApps | 需要 Linux 环境自行构建，面向高级用户 |
| YT-Advanced/WSA-Script | 1,028 | GitHub Actions 在线构建 | 用户 fork 后通过 CI 自动构建，无需本地环境 |
| Lyxot/WSAOnWin10 | 452 | Win10 专用 WSA 方案 | 专注 Windows 10 兼容性 |
| BlueStacks / NoxPlayer / LDPlayer | N/A (闭源) | 传统 Android 模拟器 | 闭源商业产品，性能和兼容性路线不同 |
| Waydroid | 10K+ | Linux 原生 Android 容器 | 仅限 Linux，非 Windows 方案 |

- **WSABuilds 的独特优势**: 唯一提供"开箱即用预构建包"的方案，用户无需任何技术背景即可安装。同时支持 Win10/Win11、x64/arm64、多种 Root 方案组合，版本矩阵最全
- **竞品格局**: 在 WSA 细分领域中占据绝对主导地位；在更广泛的"Windows 上运行 Android"市场中，面临 BlueStacks 等商业模拟器的竞争，但定位差异化明显（WSA 原生集成 vs 模拟器）

## 关键 Issue 信号

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| #593 | Windows 更新后大量应用闪退（2025年7月后） | 236 | Open | **最高优先级问题** — Windows 更新持续破坏 WSA 兼容性，作者正在修复中 |
| #329 | WebGL 不支持 (DOFUS Touch) | 85 | Closed/Solved | GPU/图形兼容性问题 |
| #106 | WSA 加载后直接关闭 | 85 | Closed | 早期稳定性问题 |
| #325 | 无法在 Copilot+ PC 和 ARM64 设备运行 | 67 | Open | **ARM64 兼容性** — 新一代 Windows 设备的支持挑战 |
| #154 | Magisk 模块重启后消失 | 52 | Closed/Solved | Root 方案集成的技术难点 |
| #565 | WSA 不工作 | 43 | Open | 通用可用性问题 |
| #330 | 微软停止支持后的延续请求 | 26 | Open (Enhancement) | 社区对项目持续维护的强烈诉求 |

**Issue 信号总结**: 核心挑战是 Windows 系统更新频繁破坏 WSA 运行环境，这是项目面临的系统性风险。ARM64/Copilot+ PC 兼容性是第二大挑战。作者对问题响应积极，使用标签系统管理得当

## 知识入口
- DeepWiki: [https://deepwiki.com/MustardChef/WSABuilds](https://deepwiki.com/MustardChef/WSABuilds) — 已收录，索引至 2025-12-13
- Zread.ai: [https://zread.ai/repo/MustardChef/WSABuilds](https://zread.ai/repo/MustardChef/WSABuilds) — 已收录
- 关联论文: 无
- 在线 Demo: 无（桌面软件，需本地安装）
- 外部资源:
  - [XDA Forums 专题帖](https://xdaforums.com/t/wsabuilds-latest-windows-subsystem-for-android-wsa-builds-for-windows-10-and-11-with-magisk-and-google-play-store.4545087/)
  - [AlternativeTo 页面](https://alternativeto.net/software/wsabuilds/about/)
  - [Internet Archive 存档](https://archive.org/details/github.com-MustardChef-WSABuilds_-_2023-08-13_16-11-46)

## 项目展示素材

1. **项目 Logo**
   - ![WSABuilds Logo](https://github.com/MustardChef/WSABuilds/assets/68516357/35cd1d5d-e464-4eb8-a676-b451341f65ad)
   - 用途: 项目标识

2. **赞助商横幅**
   - ![Sponsor Banner](https://github.com/user-attachments/assets/5bf3e8f6-2b92-448c-b90f-4d3210900bab)
   - 用途: 展示项目有赞助支持

3. **Discord 社区邀请卡**
   - ![Discord Widget](https://invidget.switchblade.xyz/2thee7zzHZ)
   - 用途: 展示活跃社区

4. **下载统计**
   - 最近5个 Release 下载量合计: ~901,219 次
   - 最高单个 Release: Windows_11_2407.40000.4.0_v2 — 504,244 次下载
   - 用途: 证明实际使用量远超 star 数

> 注: README 中大量使用 shields.io badge 和 icons8 图标用于装饰 UI，非展示素材。项目本身为系统工具类，无产品截图或演示视频。

## 快速判断
- 是否值得深入: **有条件** — 如果你的目标是在 Windows 上运行 Android 应用（特别是需要 Google Play 和 Root），这是目前最佳方案。但需注意：(1) 微软已终止 WSA 官方支持，长期前景不确定；(2) Windows 更新可能随时破坏兼容性；(3) AGPL v3 协议限制商业衍生
- 初步定位: "后 WSA 时代"的社区维护预构建分发中心，在微软放弃 WSA 后成为该技术的实际标准维护者。属于**系统工具/Android 模拟**细分领域
- 作者可信度: **中高** — 超过 3 年的持续维护记录，912 次提交，活跃的 Issue 响应，Discord + XDA 多渠道支持，有赞助商。但匿名度极高（无真名、无公司、无位置），降低了部分信任分
- 竞品格局: **细分市场领导者** — 在"WSA 预构建包"这个精确细分中几乎没有直接竞品；在更广泛的"Windows 运行 Android"市场中，与 BlueStacks 等商业模拟器形成差异化竞争（原生 WSA vs 模拟器）
