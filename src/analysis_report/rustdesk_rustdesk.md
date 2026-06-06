# 11.5 万 Star、5 年单干：RustDesk 凭什么替代 TeamViewer

> GitHub: https://github.com/rustdesk/rustdesk

## 一句话总结

开源、端到端加密、可自建中继、跨全平台——这是 5.7 年内唯一同时做到这四件事的远程桌面项目，正在用 AGPL 撬动 TeamViewer/AnyDesk 把持的商业市场。

## 值得关注的理由

- **规模与体量**：115,684 stars + 17,473 forks + 30M+ 客户端下载 + 10M+ 活跃设备 + 50+ 语种——已经跨过"爱好者玩具"门槛，进入"事实标准"区间
- **架构稀有度**：Rust 60.5% 内核 + Dart 29.4% Flutter 跨端 UI + hbbs/hbbr 中继协议分离 + NaCl 端到端加密——四层栈同时存在且各自干净的远程桌面项目几乎没有
- **商业模式清晰**：客户端 AGPL-3.0 + 服务端 Pro 双轨；新加坡 Purslane Ltd. 商业化运营 5 年+ 还能保持开源社区活跃——少见的"长期主义"开源范本

## 项目展示

![标识 + 主标语](https://user-images.githubusercontent.com/71636191/171661982-430285f0-2e12-4b1d-9957-4a58e375304d.png) — *hero：品牌标识与「开源替代 TeamViewer/AnyDesk」的主标语*

![Connection Manager 连接管理界面](https://github.com/rustdesk/rustdesk/assets/28412477/db82d4e7-c4bc-4823-8e6f-6af7eadf7651) — *主功能截图：开箱即用的连接管理界面，输入 ID/密码即可远程*

![Connected to a Windows PC 跨平台远程](https://github.com/rustdesk/rustdesk/assets/28412477/9baa91e9-3362-4d06-aa1a-7518edcbd7ea) — *核心场景：Linux 客户端远程到 Windows 桌面，体现"全平台"覆盖*

![File Transfer 文件传输](https://github.com/rustdesk/rustdesk/assets/28412477/39511ad3-aa9a-4f8c-8947-1cce286a46ad) — *扩展能力：内置文件传输/剪贴板同步，不只是远程桌面*

![TCP Tunneling TCP 隧道](https://github.com/rustdesk/rustdesk/assets/28412477/78e8708f-e87e-4570-8373-1360033ea6c5) — *架构亮点：内网穿透/TCP 隧道能力，展示技术深度*

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/rustdesk/rustdesk |
| Star / Fork | 115,684 / 17,473（fork 率 15.1%，远高于 2-5% 均值） |
| 代码行数 | 209,769（Rust 60.5% + Dart 29.4% + C/C++ 3.8% + 其他 6.3%） |
| 项目年龄 | 68 个月（5 年 8 个月，首提交 2020-09-28） |
| 开发阶段 | 密集开发（近 30 天 60 commits，近 90 天 145 commits） |
| 贡献模式 | 核心少数 + 庞大社区长尾（461 名贡献者，Top1 仅占 20.5%） |
| 热度定位 | 大众热门（11.5 万 stars 进入 GitHub 全站前 100 俱乐部） |
| 质量评级 | 代码 B+（unwrap 滥用 1093 处）/ 文档 A（24 语种 README + AGENTS.md）/ 测试 B-（54 个 #[test] 但 tests/ 几乎空） |
| License | AGPL-3.0（强 copyleft 阻挡云厂商白嫖） |
| 商业主体 | Purslane Ltd.（新加坡） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

`rustdesk` 不是个人开发者账户，而是一个**注册在新加坡的有限公司** Purslane Ltd. 的组织账户——账号 age 5.7 年，与项目几乎同步。Bio 一句话定调：「Making affordable remote desktop service for everyone」。两个关键词："affordable"（对标 TeamViewer/AnyDesk 每年数百美元订阅）、"for everyone"（去商业化 + 白标 + F-Droid/FlatHub 全渠道覆盖）。这不是"一个极客周末项目"，而是**有法律实体 + 商业路径 + 全球用户基础的开源基础设施**。

### 问题判断

作者看到了"四元难题"——远程桌面赛道悬而未决：(1) 跨平台真全端、(2) 自托管中继（不依赖中心化厂商）、(3) 端到端加密（中继服务器不可读数据）、(4) 白标可二开。**任意一件**被 TeamViewer、AnyDesk、Chrome Remote Desktop、Apache Guacamole 各自做得不错，**同时做到四件的几乎没有**。时机选择上，2020 年立项踩中三波叠加：疫情远程办公爆发 + TeamViewer 商业策略调整（涨价 + 严打个人免费） + 国产替代 + 欧洲 GDPR/数据本地化合规需求上升。

### 解法哲学

"affordable for everyone" 价值观 → 技术选型映射非常清晰：

- **affordable**（个人也能用） → Rust + 单二进制 + `panic='abort'` + `lto=true` + `strip=true` 极致瘦身
- **for everyone**（全平台） → 同一个 `librustdesk` lib 同时给 Sciter、Flutter、CLI、便携模式调用；`src/main.rs` 顶层 `#[cfg(...)] fn main()` 四象限分流
- **Self-hosted** → 协议层把 ID 服务器/中继服务器从客户端剥离，独立成 `rustdesk-server` 仓
- **数据自主** → NaCl 端到端加密 + 密钥签名化（PKI 验证 + ECDH 协商 secretbox 密钥），server 只能转发密文
- **可二开** → cargo workspace 拆 8 个独立 crate（hbb_common、scrap、enigo、clipboard 等），用 `[patch.crates-io]` 锁住自己的 fork 链

特别值得一提的是 `AGENTS.md` 的"Rust Rules"——把 unwrap 禁止、Tokio 运行时、锁/await、依赖追加、编辑粒度都写成了**硬规则**。把"为长期演进负责"内化到 onboarding 文档里，对 461 人贡献者的项目是必要的基础设施。

### 战略意图

Purslane Ltd. 操盘的"开源 + 商业双轨"是教科书级别的：

```
        开源核心（AGPL-3.0）                  商业插件（Pro）
┌────────────────────────────────────┐   ┌────────────────────┐
│ rustdesk/rustdesk   客户端 ★115k  │   │ RustDesk Server Pro│
│ rustdesk/rustdesk-server 服务端★10k│   │ （Web 控制台+鉴权） │
│ rustdesk/hbb_common 共享库         │   │ rustdesk.com 域名  │
│ rustdesk/doc 文档站                │   │ Discord/社区活跃层 │
│ F-Droid/FlatHub/MSI/AppImage/DEB   │   │ 订阅 / OEM license │
└────────────────────────────────────┘   └────────────────────┘
                ↑                                     ↑
                └────── 同一份 hbb_common ────────────┘
```

`flutter_ffi.rs` 的"replace RustDesk with app_name"逻辑把"白标"做成**代码层一等公民**——这是开源项目能否平滑商业化的关键分水岭。

## 核心价值提炼

### 创新之处

按新颖度 × 实用性排序：

1. **hwcodecs 软硬混合编码策略**（新颖度 ★★★★★ / 实用性 ★★★★★ / 可迁移性 ★★★★★）
   - `EncoderApi` trait 抽象所有编码器，`EncoderCfg` 枚举覆盖 VPX/AOM/HWRAM/VRAM
   - 运行时协商+回退链：H.264/H.265 优先走 VRAM（GPU 纹理直采）→ 退到 HWRAM（FFmpeg 封装硬编）→ 退到 VP9 软件
   - `hwcodec.rs` 把 ffmpeg_ram 编码器（NVIDIA NVENC / VAAPI / VideoToolbox / MediaCodec / AMF）抽象成统一接口
   - **可迁移性极高**：国内做录屏/会议/直播软件都有同样痛点

2. **P2P + 自建中继 + E2E 加密三层协议栈**（★★★★ / ★★★★★ / ★★★★★）
   - hbbs（rendezvous/ID server）永远不转发业务流量，只负责"客户端注册 PK、互相发现、按需转发 UDP 打洞包"
   - hbbr（relay server）打洞失败的 fallback，对 TCP 业务流**只是密文转发**（客户端用 NaCl 端到端加密，relay 拿不到明文）
   - 客户端启动后 `register_pk` → 收到 punch 请求 → `punch_udp_hole(peer_addr)` 试图直连 → 失败则 `create_symmetric_key_msg` 跟对端 ECDH 协商密钥 → 走 relay
   - **整套协议在 `src/rendezvous_mediator.rs` + `src/common.rs::secure_tcp` + `libs/hbb_common/password_security.rs` 协同实现**

3. **hbbs / hbbr 协议分离**（★★★★ / ★★★★★ / ★★★★★）
   - "协调者只做协调不碰数据" + "流量中继者只转密文"的协议切分思想
   - 让 self-hosted、Pro 商业、第三方自写 server 三方共存成为可能
   - **可原样复用到任何 P2P 通信软件**（IM、文件传输、协作编辑）

4. **Rust ↔ Flutter FFI 全桥**（★★★ / ★★★★★ / ★★★★）
   - `flutter_rust_bridge = "=1.80"` 锁版自动生成 Dart binding
   - `enum EventToUI { Event(String) | Rgba(usize) | Texture(usize, bool) }` 视频帧以 GPU 纹理 ID 直接抛给 Flutter 端
   - `src/flutter_ffi.rs` 是项目里**第二高 churn 的文件**（442 次修改，仅次于 connection.rs 的 501 次）

5. **i18n 工程化**（★★★ / ★★★★ / ★★★★）
   - 52 个语言文件在编译期 `lazy_static!` 全部加载到 HashMap——零运行时 IO 延迟
   - 占位符语法 `{}` + 「未命中回退到英文 + 仍带替换占位符」 + app_name 替换（白标适配）三件套

### 可复用的模式与技巧

- **`Stream` 枚举统一抽象多种传输**（`libs/hbb_common/src/stream.rs`）——`pub enum Stream { WebRTC(...), WebSocket(WsFramedStream), Tcp(FramedStream) }`，对 `send_bytes / next / set_key / set_raw` 等方法做手动 match 分发；关键设计：`set_key(secretbox::Key)` 把 NaCl 对称密钥塞到流上——后续所有 `send_bytes` 都自动走 secretbox 加解密。比 trait object 零开销且没有 dyn 兼容性问题
- **共享 lib + 多入口四象限 `main()`**（`src/main.rs`）——`librustdesk` 同时输出 `cdylib+staticlib+rlib`，`#[cfg(...)] fn main()` 区分 4 个入口，bin 只做参数分流。任何要打"多端同一份核心二进制"的 Rust 项目都建议照搬
- **`Config` 双层 `lazy_static`**（`CONFIG` + `CONFIG2`）——配置/状态分离 + 加密层用钠盐 + UUID 双兜底
- **`throttled_interval`**（`src/common.rs`）——自定义节流 Interval，避免 tokio 默认 Interval 在压力下抖动
- **`video_qos.rs` 自适应算法**——用 RTT + 历史延迟窗口动态调帧率/码率/分辨率，是自研 QoS 的小巧范例

### 关键设计决策

**决策 1：共享 lib + 多入口四象限 `main()`**
- 问题：同一个客户端要同时给 Flutter 桌面、移动 App、Sciter（已弃）、CLI 调试、便携模式用
- 方案：`src/main.rs` 顶层 `#[cfg(...)] fn main()` 区分 4 个入口；`src/lib.rs` 输出 `librustdesk`（cdylib + staticlib + rlib），所有业务逻辑都在 lib 里
- Trade-off：lib 边界变厚，bin 几乎只是参数 parser；但得到的好处是"同一份代码四个消费者"
- 可迁移性：高

**决策 2：`Stream` 枚举统一抽象多种传输**
- 问题：远程桌面要在 P2P 直连、TCP 中继、KCP（UDP 抗丢包）、WebSocket 之间切换
- 方案：手动 enum match + `set_key()` 灌入 secretbox 密钥
- Trade-off：新增一个传输就要改这个枚举的每个方法（编译期能拦住缺失实现）
- 可迁移性：高

**决策 3：`EncoderApi` trait + 软硬混合编解码**
- 问题：从 Intel/AMD/NVIDIA 集显到 Apple Silicon，每家硬件编码器 API 都不同；又不能假定所有机器都有硬件编码器
- 方案：trait 抽象 + 枚举配置 + 运行时协商回退链
- Trade-off：`EncoderCfg` 加新格式要改的地方多；但跨平台软硬混合**没有 trait 抽象基本活不下来**
- 可迁移性：高

**决策 4：Rust ↔ Flutter FFI 全桥**
- 问题：UI 早已 Flutter 化（移动端、桌面端统一），但视频/编解码/网络栈必须留在 Rust
- 方案：`flutter_rust_bridge` 锁版自动生成 binding + 视频帧以 GPU 纹理 ID 直接抛给 Flutter
- Trade-off：桥两端升级要严格同步（CI 用 `bridge.yml` 单独跑生成 + 校验）
- 可迁移性：高

**决策 5：rendezvous / relay 协议分离**
- 问题：客户端都在 NAT/防火墙后面，必须有"协调者"协助打洞
- 方案：hbbs（不碰数据）+ hbbr（只转密文）分离
- Trade-off：每条 P2P 路径都要跟 hbbs 至少多跳一次；但换来的是隐私与可控性的硬底线
- 可迁移性：高

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | RustDesk | TeamViewer | AnyDesk | Apache Guacamole | Parsec |
|------|---------|--------|--------|--------|--------|
| 开源/商业 | AGPL-3.0 | 闭源商业 | 闭源商业 | Apache 2.0 | 闭源商业 |
| 自托管 | 是 | 否 | 否 | 是 | 否 |
| 协议 | 自研 + NaCl | 私有 TCP | DeskRT (UDP) | HTML5 + VNC/RDP | 私有 UDP |
| 平台 | Win/Mac/Linux/iOS/Android/Web | 全（Linux 弱） | 全（含 RPi） | 浏览器 | 全（含 RPi） |
| E2E 加密 | **真 E2E** | 黑盒 | TLS+服务器可读 | 取决于后端 | TLS+服务器可读 |
| 延迟 | 中（弱网下"等待图像"问题） | 中 | **低** | 中（依赖后端） | **极低** |
| 成本 | 免费 | 订阅高 | 订阅中 | 免费 | 订阅中 |

### 差异化护城河

- **唯一同时满足「开源 + 自托管中继 + 全平台原生客户端 + 白标可二开」** 的项目
- 461 贡献者 + 5.7 年持续投入 + 30M+ 下载 + 10M+ 活跃设备 + Purslane Ltd. 商业兜底 = 同行无法短期复制
- AGPL-3.0 阻止了"拿来即卖"的 SaaS 二开，反而把"想白嫖"的用户赶向 Pro 版——这是有意为之的护城河

### 竞争风险

- **"等待图像"问题**（Issue #5609 长期未关闭）暴露了 P2P+中继在弱网下的体验短板——AnyDesk/Parsec 的 UDP+硬编组合仍是行业天花板
- **Wayland 完整支持进展缓慢**（Issue #56，134 评论已关闭但仍有遗留）会让 RustDesk 在 GNOME/KDE 新版默认桌面上失分
- **hwcodecs 在异构 GPU 上的反人性**（Issue #3434）虽已修复但仍警示：硬编自动协商复杂度高
- **Purslane Ltd. 商业化风险**：如果 Pro 营收不达预期，核心团队可能转去做 SaaS 优先，社区版降级

### 生态定位

- **个人/极客/隐私用户**：直接对标 TeamViewer/AnyDesk 闭源替代
- **企业自托管 + OEM 白牌**：避开了 TeamViewer 的"不可改"短板，是 NoMachine 等老牌自托管方案的现代化 Rust 重写版
- **商业 + 公益双轨**：Purslane Ltd. 通过 Pro 版覆盖企业需求 + F-Droid/FlatHub/MSI/AppImage 覆盖社区需求，是教科书级别的 FOSS 商业模式

## 套利机会分析

- **信息差**：低关注度但高质量？**否**——11.5 万 stars 已经是大众热门。但**国内中文社区对它的认知度远低于其真实价值**——很多人还在用向日葵/ToDesk 付费，而不知道 RustDesk 免费 + 开源 + 可自托管
- **技术借鉴**：哪些技术可以用到自己的项目？
  - **Rust↔Flutter 跨端栈**（`src/flutter_ffi.rs` 442 次修改）——直接拿它的 FFI 桥作为 Rust 跨端实战教材
  - **hwcodecs 软硬混合编码策略**（`libs/scrap/src/common/codec.rs`）——国内做录屏/会议/直播软件都有同样痛点
  - **hbbs + hbbr 协议分离思想**——可以原样复用到 P2P 文件传输、协作编辑
  - **`Stream` 枚举 + set_key 灌密钥**模式——任何要支持"多协议可插拔 + 同一条加密通道"的项目都建议这么做
  - **i18n 工程化三件套**（lazy_static HashMap + 占位符 + app_name 替换）——做 ToB 白标产品的现成范本
- **生态位**：这个项目填补了什么空白？**唯一一个既能完全自托管(数据合规)、又能 P2P 端到端加密(隐私合规)、又跨全平台、又不收钱**的远程桌面项目
- **趋势判断**：是否在增长？符合技术趋势？比竞品有没有后发优势？
  - 增长：2023 年爆发后进入"成熟维护期"（40-95 commits/月），但用户规模仍在扩张（10M+ 活跃设备）
  - 趋势：远程办公 + 数据合规 + 自托管 是 2024-2026 三大趋势，RustDesk 三者全占
  - 后发优势：**AGPL + 自托管 + E2E** 这个三角护城河是 AnyDesk/TeamViewer 无法快速复制的（他们要照顾商业订阅模式）

## 风险与不足

- **AGPL-3.0 是双刃剑**：小项目可以拿去白嫖改一改自用，大项目/商业项目必须开源自家用或付费 Pro，限制了商业二次开发
- **unwrap 滥用 1093 处**：违反自有 `AGENTS.md` 规则，FFI 边界/锁中毒/初始化路径可接受，热点路径上的 unwrap 容易出生产事故
- **巨型文件**：connection.rs 6162 行 + client.rs 4264 行，拆分粒度可优化，严重影响 PR review
- **测试覆盖不足**：`tests/` 目录只有 1 个 C 写的 RDP cliprdr 不变式测试，集成测试/e2e 测试几乎靠 nightly CI 暗跑
- **P2P/中继协议稳定性**：Issue #5609 "waiting for image" 长期未关闭，KCP 流量的 metrics 暴露缺失，弱网下诊断能力不足
- **Wayland + hwcodecs 历史包袱**：前者决定 Linux 桌面市场，后者决定异构 GPU 笔记本体验，都是规模化运维暴露的边角问题

## 行动建议

- **如果你要用它**：
  - 个人/小团队：直接下载二进制用，**替代 TeamViewer/AnyDesk 省订阅费 + 数据自主**
  - SMB IT 管理员：用 `rustdesk-server` 自建中继服务器（Docker 一行命令），**满足 GDPR/数据本地化合规**
  - OEM/集成商：用源码改 logo、改服务器、改签名（白标），**做垂直行业远程方案**
  - 暂不建议：跨国大企业（需要更稳定的中继质量 + 企业级 SLA）

- **如果你要学它**：
  - **优先看 `src/server/connection.rs`**（501 次修改，服务端连接命脉）—— 了解 P2P 打洞 + relay 切换 + ECDH 密钥协商
  - **次看 `src/flutter_ffi.rs`**（442 次修改，FFI 桥）—— 学习 Rust↔Flutter 跨端实战
  - **再看 `libs/scrap/src/common/codec.rs` + `hwcodec.rs`**（1157+763 行）—— 学习软硬混合编码抽象
  - **隐藏宝贝**：`rustdesk-server-demo` 仓（737★）—— 写自己的 rendezvous/relay server 的脚手架，比看主仓库效率高 3 倍
  - **再看 `AGENTS.md`**——把"为长期演进负责"内化到 onboarding 文档的范本

- **如果你要 fork 它**：
  - 改进方向 1：拆分 `connection.rs`（>6000 行单文件严重影响 review）
  - 改进方向 2：把 `unwrap()` 在业务路径上的出现位置导出 metrics/grep check
  - 改进方向 3：增加端到端集成测试（用 `rustdesk-server` 的 docker compose 做 e2e 套件）
  - 改进方向 4：Wayland 完整支持（pipewire / xdg-desktop-portal 整合）
  - 改进方向 5：KCP 流量的 metrics 暴露（Issue #5609 急需的诊断能力）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/rustdesk/rustdesk |
| Zread.ai | https://zread.ai/rustdesk/rustdesk |
| 官方文档站 | https://rustdesk.com/docs/ |
| 协议自述 | 项目内 `libs/hbb_common` 注释 |
| 关联论文 | 无独立论文（工程化开源路线） |
| 在线 Demo | 无（但 `rustdesk-server-demo` 仓库 737★ 提供了完整自托管教程） |
| Discord | https://discord.gg/nDceKgxnkV（50K+ 社区） |
| Reddit r/rustdesk | https://www.reddit.com/r/rustdesk |
