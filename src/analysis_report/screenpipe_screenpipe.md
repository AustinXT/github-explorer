# screenpipe/screenpipe 深度分析报告

> GitHub: https://github.com/screenpipe/screenpipe

## 一句话总结

"AI 的屏幕记忆层"——通过事件驱动捕获（点击/切换应用/打字暂停触发截屏+无障碍树遍历的原子操作）+ 多后端 OCR/STT + Pipe 插件系统，将你在电脑上看到和听到的一切变成 AI Agent 可搜索/可自动化的本地知识库，21 个月 17K star。

## 值得关注的理由

1. **事件驱动捕获是核心架构创新**：不是简单定时截屏，而是基于 8 种用户行为事件（AppSwitch/WindowFocus/Click/TypingPause/ScrollStop/Clipboard/VisualChange/Idle）触发捕获。Paired Capture 模式将截图+无障碍树遍历原子配对，比纯 OCR 更精确且 CPU 节省 30-50%
2. **Pipe = Markdown 文件的极简插件系统**：AI Agent 的 prompt 和配置编码为 `pipe.md`，YAML frontmatter 定义调度/模型/权限，Markdown 正文即 prompt。支持 cron 调度和权限控制——这是将 AI Agent 变成"定时任务"的最简路径
3. **零知识可搜索加密云同步**：ChaCha20-Poly1305 本地加密 + Argon2id 密钥派生 + HMAC-based token 实现服务端搜索但服务端无法解密——在隐私保护和实用性之间找到了精妙平衡

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/screenpipe/screenpipe |
| Star / Fork | 17,375 / 1,474 |
| 代码行数 | ~200,000 核心代码 (Rust 115K, TSX 53K, TS 24K) |
| 项目年龄 | 21 个月（2024-06-19 创建） |
| 开发阶段 | 密集开发（247 个 release，每 2.5 天发版，2026Q1 月均 1000+ commits） |
| 贡献模式 | 创始人主导（louis030195 占 85%+，Bus Factor = 1） |
| 热度定位 | 大众热门（17K star，100K+ 用户） |
| 质量评级 | 代码[B+] 文档[A-] 测试[B+] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Louis Beaumont (@louis030195)，San Francisco，Mediar Inc. 创始人。175 个公开仓库，421 followers。自称"100k users"。5,978 commits（85%+），核心合作者 m13v (419 commits)。典型的"创始人驱动"型开源项目。

### 问题判断

Rewind.ai（闭源，产品方向调整中）和 Windows Recall（隐私争议大）验证了"屏幕记忆"的需求，但市场缺少一个**开源、跨平台、隐私优先、AI Agent 可消费**的方案。AI Agent（Claude Code、Cursor 等）需要理解用户"正在做什么"才能提供更好的辅助，但它们看不到屏幕——screenpipe 填补了这个"感知层"空白。

### 解法哲学

"录制一切，全部本地，AI 可用"——核心原则：
1. **本地优先**：所有数据存储在本地 SQLite，OCR/STT 可全部本地运行
2. **事件驱动**：不盲目连续录制，而是基于用户行为智能触发（5-10% CPU）
3. **多模态融合**：屏幕截图 + OCR + 无障碍树 + 音频转录 + 剪贴板，构建完整的上下文
4. **Agent 原生**：Pipe 插件系统让 AI Agent 直接消费屏幕上下文
5. **安全第一**：DRM 检测暂停录制、密码字段排除、PII 去除、零知识加密

### 战略意图

- **开源核心 + 企业版** (ee/ 目录独立许可)
- **AI Gateway** (Cloudflare Worker 路由多模型)
- **云同步** (零知识加密)
- **MCP 集成** (独立版本管理 mcp-v0.10.0)
- 目标成为 AI Agent 生态的"感知基础设施层"

## 核心价值提炼

### 创新之处

1. **事件驱动捕获 + Paired Capture**（新颖度 5/5 × 实用性 5/5）
   8 种用户行为事件触发截图+无障碍树遍历的原子操作。`FrameComparer` 先哈希早退（O(1)）再降采样直方图比较，静态场景 CPU 节省 30-50%。比定时截屏更智能，不丢失关键信息

2. **Pipe = Markdown 插件系统**（新颖度 5/5 × 实用性 5/5）
   `pipe.md` 文件 = YAML frontmatter（调度/模型/权限）+ Markdown 正文（AI prompt）。支持 cron 调度（`every 30m`/`daily`/cron 表达式）和类型化权限控制（Api/App/Window/Content）

3. **零知识可搜索加密**（新颖度 4/5 × 实用性 4/5）
   ChaCha20-Poly1305 加密 + Argon2id 密钥派生 + HMAC-SHA256 可搜索 token。服务端可执行搜索但无法解密内容

4. **会议检测 v2（无障碍树扫描）**（新颖度 4/5 × 实用性 4/5）
   不依赖应用名判断，而是扫描 Zoom/Teams/Meet/Slack 的无障碍树中的 mute/leave 按钮确认会议真正在进行中

5. **多模态 OCR 后端抽象**（新颖度 3/5 × 实用性 5/5）
   OcrEngine enum 统一 Apple Vision、Windows OCR、Tesseract、自定义 API、云端 OCR 五种后端，平台透明切换

6. **ImmediateTx SQLite 并发解决方案**（新颖度 3/5 × 实用性 4/5）
   用 Rust 信号量在应用层排队 `BEGIN IMMEDIATE` 事务，解决 WAL 模式下读者升级为写者时的 SQLITE_BUSY_SNAPSHOT 问题

### 可复用的模式与技巧

1. **事件驱动捕获 + 帧差异早退**：任何需要"智能采样"的监控/录制系统
2. **Pipe = Markdown 插件**：AI Agent 定时任务的最简设计模式
3. **Paired Capture（截图+A11y 原子配对）**：视觉数据+结构化数据的融合存储
4. **零知识可搜索加密**：任何需要云端搜索但保护隐私的系统
5. **ImmediateTx 事务排队**：高并发 SQLite 写入的标准解决方案
6. **多 OCR 后端抽象**：跨平台 OCR 集成的参考模式

### 关键设计决策

| 决策 | 牺牲了什么 | 换来了什么 |
|------|-----------|-----------|
| 事件驱动替代连续录制 | 可能漏掉纯浏览的内容 | CPU 从 30%+ 降到 5-10% |
| Pipe 用 Markdown 而非代码 | 逻辑表达受限 | 零门槛创建 AI 自动化 |
| 本地优先存储 | ~20GB/月存储 | 100% 隐私，零联网可用 |
| 多 OCR 后端 | 适配层复杂度 | 最优 OCR 质量（各平台原生 API） |
| 零知识加密云同步 | 搜索效率受限 | 服务端无法解密用户数据 |
| DRM 检测暂停录制 | 无法记录 Netflix 等内容 | 法律合规 |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | screenpipe | Rewind.ai | Windows Recall | ActivityWatch |
|------|-----------|-----------|----------------|---------------|
| 开源 | MIT | 闭源 | 闭源 | MPL-2.0 |
| 平台 | macOS/Win/Linux | 仅 macOS | 仅 Win 11+ | 全平台 |
| 屏幕捕获 | 事件驱动+OCR | 连续录制+OCR | 定时快照+AI | 无 |
| 音频捕获 | Whisper/Deepgram | Whisper | 无 | 无 |
| AI 搜索 | 多模型+向量 | 内置 | Copilot+ | 无 |
| 插件/自动化 | Pipe 系统 | 无 | 无 | 有限 |
| 加密 | ChaCha20+零知识 | 未知 | BitLocker | 无 |
| Agent 集成 | MCP + Pipe | 无 | 无 | 无 |
| Star/用户 | 17K/100K | 闭源 | 内置 | 17K |

### 差异化护城河

1. **唯一开源的全栈方案**：屏幕+音频+AI 搜索+自动化的完整管线
2. **AI Agent 感知层定位**：通过 MCP 和 Pipe 系统，让 Agent 消费屏幕上下文
3. **跨平台最广**：macOS/Windows/Linux 全覆盖
4. **零知识加密**：在隐私保护上超越所有竞品

### 竞争风险

- Apple Intelligence / Windows Recall 内置到 OS 中可能蚕食用户需求
- 20GB/月的存储需求限制长期数据留存
- 创始人主导（85%+ commits），Bus Factor = 1

### 生态定位

"AI Agent 的感知基础设施"——填补了 AI 工具链中"理解用户正在做什么"的空白。通过 MCP 和 Pipe 系统，让任何 AI Agent 都能消费屏幕上下文。

## 套利机会分析

- **信息差**: 事件驱动捕获 + Paired Capture 的架构模式在"智能监控"领域有广泛迁移价值（安全审计、UX 研究、无障碍测试）
- **技术借鉴**: (1) 事件驱动捕获 + 帧差异早退；(2) Pipe = Markdown 插件系统；(3) 零知识可搜索加密；(4) ImmediateTx SQLite 并发方案；(5) 会议检测 v2（A11y 树扫描）
- **生态位**: AI Agent 的"眼睛和耳朵"，填补感知层空白
- **趋势判断**: 2026Q1 月均 1000+ commits 爆发式增长，247 个 release，正处于最活跃的迭代期

## 风险与不足

1. **Bus Factor = 1**：创始人 louis030195 贡献 85%+，项目高度依赖单人
2. **fix 占比 57%**：快速迭代导致高回归率，窗口管理和 UI 层是高频回归区
3. **db.rs 7,164 行**：数据库层单文件过大，应拆分
4. **meeting_detector.rs 3,820 行**：硬编码大量应用的 AX 标识符，维护成本高
5. **20GB/月存储需求**：限制长期数据留存，需要更好的压缩/清理策略
6. **2025 年中 6 个月低活动期后突然爆发**：可能存在 AI 生成代码的质量一致性问题
7. **macOS 内存泄漏**（Issue #2571）和段错误（#2539）等稳定性问题

## 行动建议

- **如果你要用它**: `npx screenpipe@latest record` 即可开始。适合：需要 AI 帮你回忆"刚才看到的那个东西"、自动化日常工作流、构建个人知识库。注意：需要较好的 CPU/GPU 和 20GB/月存储空间
- **如果你要学它**: 重点关注以下模块：
  - `crates/screenpipe-engine/` — 事件驱动捕获架构核心
  - `crates/screenpipe-screen/src/capture_screenshot_by_window.rs` (1,927 行) — 多平台截屏管线
  - `crates/screenpipe-core/src/pipes/` — Pipe = Markdown 插件系统
  - `crates/screenpipe-vault/` — 零知识加密方案
  - `crates/screenpipe-db/src/db.rs` (7,164 行) — SQLite + sqlite-vec 数据层
  - `crates/screenpipe-events/src/meeting_detector.rs` (3,820 行) — A11y 树会议检测
- **如果你要 fork 它**: 可改进方向：
  - 拆分 db.rs（7K 行）和 meeting_detector.rs（3.8K 行）
  - 降低存储需求（更好的压缩/自动清理策略）
  - 将会议检测的硬编码 AX 标识符迁移到配置文件
  - 改善 macOS 内存管理

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | [deepwiki.com/screenpipe/screenpipe](https://deepwiki.com/screenpipe/screenpipe) |
| 官方文档 | [docs.screenpi.pe](https://docs.screenpi.pe) |
| 官方网站 | [screenpi.pe](https://screenpi.pe) |
| Discord | [discord.gg/screenpipe](https://discord.gg/screenpipe) |
| 关联论文 | 无 |
| 在线 Demo | 无（桌面应用需安装） |
