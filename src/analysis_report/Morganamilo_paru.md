# pacman 维护者亲手写的 AUR 助手，功能比 yay 全

> GitHub: https://github.com/Morganamilo/paru

## 一句话总结

paru 是 Arch Linux 上功能最全的 AUR 助手（AUR helper），用 Rust 编写。它把 pacman 体验无损延伸到 AUR（社区软件源）：一条 `paru` 命令就等于 `pacman -Syu` + AUR 全量升级，还带交互式审阅 PKGBUILD、devel/-git 包更新追踪、clean chroot 构建、显示 Arch news 等。最大的信任点是作者——**Morganamilo（Lulu）本人就是 pacman 的维护者，还写了 libalpm 的 Rust 绑定 alpm.rs，曾是 yay 的共同维护者**。「写这个 AUR 助手的人，就是写底层包管理器的人」，这在 AUR 助手品类里独一档。客观提醒：它已进入成熟低维护期（更新放缓），且与 libalpm 强耦合、pacman 更新 ABI 时会暂时受影响。

## 值得关注的理由

- **可信度独一档**：作者是 pacman 本体维护者 + alpm.rs（libalpm Rust 绑定）作者 + 前 yay 共同维护者——AUR 助手由「最懂底层包管理器的人」打造。
- **功能最全 + 默认更安全**：交互式审阅 PKGBUILD（彩色 diff，防止盲装恶意脚本）、devel/-git 包追踪、批量操作、clean chroot、PGP 验签、Arch news、查看 AUR 评论；命令语义对齐 pacman，几乎零学习成本。
- **工程范本价值**：整套 Arch 生态的 Rust 工具链（alpm/raur/aur-depends/srcinfo）都出自作者之手，paru 是其集大成上层应用——是「Rust 封装系统级 C 库做 CLI」的优质参考。

## 项目展示

[![paru 终端演示](https://asciinema.org/a/sEh1ZpZZUgXUsgqKxuDdhpdEE.svg)](https://asciinema.org/a/sEh1ZpZZUgXUsgqKxuDdhpdEE)

交互式搜索/安装/审阅流程（asciinema 录屏）。权威文档：man `paru(8)` / `paru.conf(5)` + [ArchWiki: AUR helpers](https://wiki.archlinux.org/title/AUR_helpers)。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/Morganamilo/paru |
| Star / Fork | 8775 / 311（AUR 助手品类头部梯队，稳步增长 ~120/月） |
| 代码行数 | 25827（⚠️ **PO 翻译占 59.9%/覆盖 24 语言**，真实业务码是 **Rust 39.1%≈1 万行**） |
| 项目年龄 | 68.2 个月（约 5.7 年，2020-10 起） |
| 开发阶段 | **低维护**（成熟工具的功能完整后低频维护期：近 90 天 0 commit，作者称不再发新版） |
| 贡献模式 | 单人核心（morganamilo/Lulu 占 73.8%）+ 庞大翻译者社区（145 人，多为 PO 翻译 PR） |
| 热度定位 | 大众热门里的「高可信度精品」（非被低估，而是权威背书 + 功能最全） |
| 质量评级 | 代码[优·精炼 Rust] 文档[完善·man+ArchWiki] 测试[有·testdata 夹具活跃] |
| License | **GPL-3.0**（强 copyleft，与 pacman 生态一致） |

## 作者视角：为什么存在这个项目

### 作者背景

**Lulu（@Morganamilo）**，bio「I do arch things. **pacman | alpm.rs | paru**」——这不是自夸：① 她是 **pacman 本体的维护者之一**；② 她编写维护 **alpm.rs**（pacman 核心 C 库 libalpm 的安全 Rust 绑定）；③ 曾是 **yay 的主要共同维护者**，后用 Rust 另起 paru 作为精神继任者。她的高星仓库（aur-depends/srcinfo.rs/pacmanconf.rs）全是 paru 的配套底层库，整条技术栈围绕 paru/pacman。

### 问题判断

Arch 的官方包由 pacman 管理，但 pacman 不碰 AUR（社区维护的海量软件源），需要 AUR 助手自动完成「拉 PKGBUILD → 审阅 → 构建 → 用 pacman 安装 + 处理依赖」。既有助手（如 yay/Go）已不错，但作者作为 pacman 维护者，想要一个**更安全（默认审阅 PKGBUILD）、功能更全（devel 追踪/chroot/batch）、且基于自己写的 libalpm Rust 绑定**的助手。于是用 Rust 重做，把整条 Arch 工具链 Rust 化。

### 解法哲学

- **明确选择「pacman 超集」定位**：不重造轮子，把 pacman 体验无损延伸到 AUR，命令语义对齐 pacman。
- **明确选择 Rust + 自家 libalpm 绑定**：无 GC、强类型，解析复杂 PKGBUILD 更稳；直接操作本地包数据库。
- **明确选择安全优先**：默认鼓励/高亮审阅 PKGBUILD，防盲装恶意脚本。
- **明确选择功能最全**：devel/-git 追踪、clean chroot、PGP 验签、Arch news、AUR 评论。
- **明确选择把底层抽成独立 crate**：alpm/raur/aur-depends/srcinfo 各自成库，paru 只做编排。

### 战略意图

paru 是作者「用 Rust 重建 Arch 包管理工具链」愿景的顶层应用：底层 crate 复用于整个生态，paru 把它们组装成最强 AUR 助手。它不追求商业化，而是以「pacman 维护者出品 + 功能最全 + 默认更安全」的权威叙事，成为进阶 Arch 用户的首选。功能完整后转入低频维护是其自然归宿。

## 核心价值提炼

### 创新之处

1. **整套 Arch 生态的 Rust 化**（最值得学）：alpm（libalpm 绑定）、raur（AUR RPC）、aur-depends/srcinfo（依赖/PKGBUILD 解析）、pacmanconf——作者把 C 生态逐层包成安全 Rust crate，paru 是集大成。
2. **依赖解析 + 构建编排**：`resolver.rs`/`order.rs` 构建 AUR 与官方仓库的依赖图并定构建顺序（AUR 助手最硬的算法），`install.rs` 串起拉取→审阅→构建→安装。
3. **devel/-git 包追踪**：`devel.rs` 用 commit 比对判断滚动包是否需重建——区别于普通助手的特色。
4. **安全审阅流**：彩色 diff 审阅 PKGBUILD + PGP 验签 + clean chroot 隔离构建。

### 可复用的模式与技巧

1. **C 库分层包成独立 Rust crate**：把 libalpm 等系统库抽成可复用绑定，是 Rust 封装系统工具的范本。
2. **CLI 兼容既有工具语义**：命令对齐 pacman，零学习成本——降低迁移摩擦的设计。
3. **i18n 优先**：24 语言 PO 翻译占六成「代码」，体现国际化用户基础。
4. **测试夹具数据库**：`testdata/db` 是热点第二，安装/解析逻辑用真实包数据库夹具回归。

### 关键设计决策

- **pacman 超集而非独立工具**：复用 pacman 体验是普及关键。
- **链接 libalpm**：能直接操作包数据库，代价是 ABI 耦合（见下）。
- **安全审阅默认开**：比「一键盲装」更安全，但多一步交互。

## 竞品格局与定位

### 竞品对比

| 助手 | 语言 | 定位 | 取舍 |
|------|------|------|------|
| **paru** | Rust | 功能最全、默认更安全、pacman 维护者出品 | 功能强但更新已放缓；高级特性对进阶用户价值最大 |
| **yay** | Go | 最知名、用户基数最大、够省心 | 大众默认首选；功能不如 paru 全 |
| **pikaur** | Python | 用户友好、交互式冲突解决 | Python 运行时；深度/性能不及 |
| **aurutils** | Shell | 硬核脚本化、本地 repo 工作流 | 极可组合但学习曲线陡、非交互 |
| **pamac** | GUI | Manjaro 图形化 | 偏 Manjaro 生态，CLI 能力不同维度 |

### 差异化护城河

护城河 =「**pacman 维护者出品的权威可信度 + 功能最全 + 默认更安全 + Rust 性能**」。但 AUR 助手高度同质（都基于 pacman），paru 占「功能强/可信度高」的高端位，**yay 仍是大众默认首选**。

### 竞争风险

- **「功能最全 ≠ 大众首选」**：Slant 社区投票 yay 第 1、paru 第 6——多数普通用户更偏好 yay「少打扰、够用」，paru 的强项对深度用户才有边际价值，**没有必须从 yay 迁移的紧迫性**。
- **维护放缓**：低维护期 issue 响应/新特性变慢，可能影响信心。
- **libalpm 耦合风险**：pacman 更新 ABI 时 paru 暂时不可用（见下），曾让用户临时切回 yay。

### 生态定位

它是 Arch 进阶用户的顶级 AUR 助手、yay 的现代继任者，被 EndeavourOS/CachyOS 等社区推荐。要功能最全 + 更安全 + 作者权威 → paru；要省心大众默认 → yay；要脚本化/本地 repo → aurutils；要 GUI → pamac。

## 套利机会分析

- **信息差**：它已是几乎所有 Arch 教程都推荐的工具，不存在「小众宝藏」套利。价值在「权威可信 + 功能最全」叙事，以及「成熟低维护≠死亡」的客观认知。
- **技术借鉴**：「C 库分层包成 Rust crate」「依赖图解析 + 构建编排」「CLI 兼容既有工具」对做系统级工具/包管理器极有参考。
- **生态位**：Arch（及衍生发行版）进阶用户的首选 AUR 助手；非 Arch 用户无关。
- **趋势判断**：AUR 助手是成熟稳定品类，paru 凭可信度与功能稳居高端位；libalpm 耦合的适配节奏是主要变量。

## 风险与不足

- **⚠️ 维护已明显放缓（需正视）**：近 30/90 天 0 commit、近一年仅 78 commit，最后提交 2026-01-09，作者本人表示不再发布新版本。**这不是死亡，而是功能完整后的成熟低维护**（AUR 助手不需天天加功能，主要在 pacman/libalpm 破坏性更新时跟进），但 issue 响应与新特性节奏确实变慢。
- **⚠️ 与 libalpm 强耦合**：paru 经 alpm.rs 链接 pacman 的 C 库，**pacman 更新 ABI（如 libalpm v14→v16）时 paru 可能编译/运行失败，需等 alpm.rs 跟进并重新构建**（#1454「libalpm v16」182 评论、#1468 仍 open）。这是所有链接 libalpm 的助手（含 yay）的共性结构风险，也是低维护期社区最焦虑的点——pacman 7.x 升级时一度需临时切回 yay。
- **「功能最全 ≠ 大众首选」**：yay 仍是社区票选第一，paru 的高级特性对深度用户才有边际价值。
- **Arch 专属**：仅服务 Arch 及衍生发行版用户，受众天然受限。
- **内容安全**：无敏感问题。

## 行动建议

- **如果你要用它**：你是 **Arch（或 EndeavourOS/CachyOS 等衍生版）用户**，想要功能最全、默认更安全（审阅 PKGBUILD）、devel/-git 追踪强的 AUR 助手——paru 是顶级选择（`pacman -S paru` 即可装）。客观预期：更新已放缓但成熟稳定；**pacman 大版本升级（libalpm ABI 变动）后可能需等 paru 跟进或临时用 yay**。只想省心大众默认 → yay；要脚本化本地 repo → aurutils。
- **如果你要学它**：重点读 `src/install.rs`（安装编排）、`src/resolver.rs`/`order.rs`（依赖图解析）、`src/devel.rs`（git 包追踪），以及作者的配套 crate **alpm.rs**（libalpm Rust 绑定）。这是「Rust 封装系统级 C 库 + 依赖解析 + CLI 兼容」的工程范本。
- **如果你要 fork/借鉴它**：GPL-3.0（copyleft）；最有价值的是借鉴其分层 crate 设计与依赖解析/构建编排逻辑。注意 libalpm 耦合——任何链接它的工具都要跟 pacman ABI。

### 知识入口

| 资源 | 链接 |
|------|------|
| 文档 | man `paru(8)` / `paru.conf(5)` ｜ [ArchWiki: AUR helpers](https://wiki.archlinux.org/title/AUR_helpers) |
| DeepWiki | https://deepwiki.com/Morganamilo/paru （含架构/依赖解析详解） |
| 作者生态 | [Morganamilo (Lulu)](https://github.com/Morganamilo) ｜ alpm.rs ｜ aur-depends ｜ srcinfo.rs |
| 对比 | [Yay vs Paru（linuxadictos）](https://en.linuxadictos.com/Yay-vs-Paru:-Real-differences-between-the-two-most-popular-AUR-assistants.html) ｜ [yay vs paru（Slant）](https://www.slant.co/versus/23118/40125/~yay_vs_paru) ｜ yay ｜ pikaur ｜ aurutils |
| libalpm 耦合 | [#1454 Support libalpm v16](https://github.com/Morganamilo/paru/issues/1454) ｜ [#1468 编译失败](https://github.com/Morganamilo/paru/issues/1468) |
