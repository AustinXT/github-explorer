# 开源到芯片固件的 AI 项链 Omi：96 万行全栈，和它解决不了的「被录者没同意」

> 一句话总结：Omi（原 Friend）是一家硬件公司把「芯片固件 → BLE 协议 → 移动 app → 云后端 → 桌面看屏 agent」整条全栈 MIT 开源的 AI 可穿戴生态——挂脖项链常听、智能眼镜会看、桌面 agent 看屏，全程转写成「第二大脑」记忆。技术野心罕见、可自托管、甚至主动兼容竞品硬件;但 always-on 随身录音对「周围人未同意」这一伦理与法律根本问题，开源和自托管都解决不了。

---

## 值得关注的理由

- **罕见的「全栈开源 AI 硬件」**。从 nRF52 项链固件（C）、PCB 硬件设计，到 Flutter app、Python 转写后端、桌面 Rust agent，全部 MIT 开源，且 `backend/charts/` 提供 Deepgram-self-hosted/Parakeet/diarizer/VAD 全套 k8s chart——理论上可做到数据完全不出自有基础设施。对标被 Meta 收购的 Limitless、被 Amazon 收购的 Bee 等闭源黑盒，这是大厂难以直接收编的生态位。
- **「可穿戴 AI 操作系统」的野心**。Omi app 主动支持竞品硬件（代码里有 `limitless_connection.dart`/`bee_connection.dart`/`plaud_connection.dart`），把对手设备纳入自己生态;配 250+ 第三方 app 的「App Store」+ persona 人格克隆——它赌的是生态层，不是单一硬件。
- **一条值得抄的记忆工程范式**。它的 memory 不是把转写直接塞库，而是「抽取 → 向量召回 → LLM 裁决 skip/merge/update → 旧记忆软失效 → 建知识图谱」——这是任何长期记忆型 AI agent 都需要的去重纠错方案。
- **它把 always-on 录音的伦理债摆上了台面**。随身常听项链 + 看屏桌面 agent，触及「被录的第三方从未同意」这一深刻问题——这是整个 AI 可穿戴品类绕不开、且无法用工程手段回避的核心争议。
- **有故事性**：创始人 Nik Shevchenko（Thiel Fellow、前加密 YouTuber、病毒营销）、「两个 Friend」改名公案、$2M 融资（Tim Draper 领投）。

---

## 项目展示

README 三张官方媒体构成「多形态生态」视觉叙事：

![Omi](https://github.com/user-attachments/assets/7a658366-9e02-4057-bde5-a510e1f0217a)
![Omi 项链](https://github.com/user-attachments/assets/834d3fdb-31b5-4f22-ae35-da3d2b9a8f59)
![Omi Glass 眼镜](https://github.com/user-attachments/assets/fdad4226-e5ce-4c55-b547-9101edfa3203)

> 社交卡片兜底：`https://opengraph.githubassets.com/1/BasedHardware/omi`

---

## 项目画像

| 维度 | 数据 |
|---|---|
| 全名 | `BasedHardware/omi`（原名 Friend） |
| 定位 | 开源 AI 可穿戴生态（项链 + 眼镜 + 桌面看屏 agent） |
| Star / Fork | 12,742 ⭐ / 2,040 🍴（CSV 抓取 10,756，高速增长） |
| License | MIT（硬件 + 固件 + app + 后端全栈开源） |
| 代码规模 | 账面 137 万行 = 真实手写 ~96 万 + 固件 HEX 烧录镜像 16.6 万 + 配置/生成 22.8 万;注释比 0.085 |
| 技术栈 | Dart/Flutter（app 46万）+ Python（后端 16.8万）+ Swift（桌面 12.5万）+ C（固件 6.3万）+ Rust（桌面后端 1.8万）+ Next.js |
| 建库时间 | 2024-03（约 2.2 年，今日活跃） |
| 开发节奏 | 19,903 commit;近 90 天 7,000、近 30 天 1,236;近一年占 61%（加速） |
| 版本 | 最新 v3.0.0-Android-App;1,079 tag（多为 CI 自动构建） |
| 贡献者 | 240 人，创始人 Nik Shevchenko + 核心团队 + 印度/越南全球社区 |
| 商业 | bootstrapped + $2M 融资（Tim Draper 领投）;自称 ~$1.5M ARR |
| 设备演进 | 项链（2024 nRF52）→ omiGlass 眼镜（2025 ESP32-S3）→ 桌面看屏 agent（2026 Rust+Swift） |

---

## 作者视角

### 问题发现

创始人 Nik Shevchenko（@kodjima33，Thiel Fellow、前加密 YouTuber）从「Friend」情感陪伴吊坠起步，撞名 Avi Schiffmann 的 friend.com 后改名 Omi，并把重心从「陪伴」转向「生产力第二大脑」。他的判断：闭源消费硬件解决不了「数据归属」与「形态/模型锁定」，而开源全栈可以同时吃下「硬件销售 + 开发者平台 + 自托管信任」三块。

### 解法哲学

四个支柱：**开源全栈**（固件到云全部可读可改可自托管）+ **多形态**（项链→眼镜→桌面看屏，从「听」到「看」）+ **开发者平台**（webhook 触发的 app marketplace + persona 克隆）+ **数据自控**（per-user 加密 + 自托管 chart）。一个极具侵略性的细节：app 主动支持竞品硬件（limitless/bee/plaud/frame connection）——把自己做成「可穿戴 AI 的中台/操作系统」，赌生态层而非单一硬件。

### 背景知识迁移

团队同时驾驭：Zephyr/nRF52 嵌入式 C（PDM 麦克风 + Opus 编码 + BLE GATT）、Flutter 跨端、Python/FastAPI 流式 STT pipeline、Swift/SwiftUI + Rust 桌面原生、pyannote 说话人分离、向量检索/RAG/知识图谱、k8s/Helm 微服务。这是典型的「硬件公司被迫长成全栈软件公司」的能力栈。

### 战略图景

病毒营销（$2M 融资、改名公案制造话题）+ 开源获取开发者心智 + 硬件卖货变现 + 平台抽成。开源是获客与信任杠杆，但**始终保留中心化云作为默认路径**（默认后端用 Firestore/Firebase + Deepgram 云 STT + 服务端持密钥加密）。always-on 的隐私取舍被有意识地用「开源 + 可自托管」话术对冲，但代码层面并未触及「被录第三方未同意」这一根本问题（见隐私专节）。

---

## 核心价值提炼

### 创新点

**1. 记忆冲突消解管线（向量召回 + LLM supersede + 软失效）** — 新颖度 3/5 · 实用性 5/5 · 可迁移性 5/5

`process_conversation.py` 把长期记忆做成：抽取新 memory → `find_similar_memories(threshold=0.6)` 故意放宽阈值召回跨措辞矛盾 → 只与未失效记忆比对 → `resolve_memory_conflict` LLM 返回 skip/merge/update + supersede → 旧记忆 **invalidate（保留历史但移出检索、删向量）** 而非物理删除 → 再 `extract_knowledge_from_memory` 建知识图谱。**这是全仓最值得抄的模式**——任何长期记忆/RAG 都需要的去重纠错方案。

**2. 可穿戴 AI 中台（开源全栈 + 主动兼容竞品硬件）** — 新颖度 5/5 · 实用性 4/5 · 可迁移性 2/5

一家硬件公司把固件到云全部 MIT 开源，且 app 主动支持 Limitless/Bee/Plaud/Frame 等竞品设备（`app/lib/services/devices/` 每种硬件一个 connection），试图占据「可穿戴 AI 操作系统/App Store」生态位。

**3. nRF52 固件 BLE 音频流（PDM→Opus→GATT 分片 + SD 卡离线缓冲）** — 新颖度 3/5 · 实用性 4/5 · 可迁移性 4/5

`mic.c` PDM 双缓冲采集 → `codec.c` Opus 编码（16kHz）→ `transport.c::push_to_gatt` 按 MTU 分片、每片加 3 字节头（packet id + index）供重组/丢包检测、notify 失败重试;BLE 不可用时 `write_to_storage` 把 Opus 帧紧凑打包写 SD 卡。是可穿戴音频设备的通用骨架。

**4. 实时在线说话人聚类 + 注册声纹匹配** — 新颖度 3/5 · 实用性 4/5 · 可迁移性 4/5

对每段抽 voice embedding 与「运行均值质心」做余弦比较聚类，embedding 失败时**保留上一标签而非丢段**;叠加 speech profile 匹配标注「你 vs 他人」;离线侧用 pyannote GPU 高精度后处理。

**5. 三级 webhook + persona 的可穿戴 app 平台** — 新颖度 4/5 · 实用性 4/5 · 可迁移性 4/5

第三方 app = 声明式 capability，按 `memory_creation`/`transcript_processed`/`audio_bytes` 三档事件触发 webhook + prompt 注入;persona 走 `condense_memories` 把数百条事实压缩成 1:1 人格克隆 prompt。

**6. 桌面看屏 agent（ScreenCaptureKit OCR + ACP 桥接）** — 新颖度 4/5 · 实用性 3/5 · 可迁移性 4/5

Swift `ScreenCaptureService` 截屏 → OCR → `screen_activity` 存 OCR text + embedding 可语义检索;`acp-bridge` 经 ACP（Agent Client Protocol）让 Swift app ↔ Node bridge ↔ 外部 agent（Claude Code/Gemini）通信，把 Omi memories 作为 tool 暴露给 agent。

### 可复用模式

1. **向量召回 + LLM 冲突裁决 + 软失效**：长期记忆去重/纠错的工程化范式 — 记忆型 agent/个性化 RAG。
2. **STT provider 抽象 + 按语言路由 + BYOK**：解耦云/自托管/多语言 STT，用户可自带 key — 多语音产品。
3. **设备连接抽象层 + WAL 离线优先同步**：统一异构设备接入 + 断网不丢数据 — IoT/边缘采集 app。
4. **能力声明 + 多级事件 webhook + prompt 注入**：零侵入第三方 app 扩展 — AI app marketplace。
5. **ACP 桥接 + 私有数据封装成 agent tools**：让任意外部 agent 安全操作私有上下文 — agent 互操作。
6. **在线质心聚类 + 失败保留标签**：实时流的稳健分类容错 — 低延迟流式标注。

### 关键设计决策

- **转写 pipeline：provider 路由 + 微服务化**：`get_stt_service_for_language()` 在 Deepgram Nova-3 / 自托管 Parakeet / Modulate 间按语言路由，兜底英文 Deepgram;Listen/Pusher/VAD/Diarizer/STT 拆成独立服务各一份 Helm chart，支持 BYOK。Trade-off：可换可自托管，但 `transcribe.py` 3062 行巨型 handler 是维护噩梦，微服务多 = 部署复杂。
- **Flutter 多设备 BLE 抽象 + WAL 离线同步**：每种硬件一个 connection 实现;离线音频抽象成 WAL，`local_wal_sync`（手机）/`sdcard_wal_sync`（设备 SD）/`flash_page_wal_sync`（Limitless flash）多后端 + 限流对账;27 个 ChangeNotifier 管状态。Trade-off：抽象优雅，但 WAL 多后端对账正是离线丢数据 Issue 的根源。
- **加密为服务端持密钥 at-rest，非 E2E**：`encryption.py` 用 master secret + uid 经 HKDF 派生 per-user 密钥做 AES-GCM——密钥在服务端，服务器可解密。这是多租户隔离，不是端到端加密;默认云后端用 Firestore + Deepgram 云 STT。

---

## 竞品格局

| 竞品 | 定位 | 优势 | 劣势/现状 |
|---|---|---|---|
| **Omi（本项目）** | 开源全栈生产力 + 记忆，多形态 | 唯一硬件+软件全开源、可 DIY/自托管、开发者平台（250+ app）、跨设备（含支持竞品硬件）、$89 低价 | 转写/连接稳定性仍打磨、营销噪音大、隐私争议绕不开 |
| **Limitless**（原 Rewind） | 闭源录音吊坠 + 会议记忆 | 体验成熟、记忆叙事强 | **2025-12 被 Meta 收购** |
| **Friend**（Avi Schiffmann） | 闭源 AI 情感陪伴项链 | 话题度高、陪伴定位 | 工具性弱、争议大、不开源 |
| **Bee AI** | 闭源生活记录手环 $49 | 价格最低 | **被 Amazon 收购** |
| **Plaud（Note/NotePin）** | 闭源录音卡片 AI 转写 | **转写准确度口碑最好、商业最成功** | 单设备单任务、闭源、订阅制 |
| **Humane AI Pin / Rabbit R1** | AI 设备 | 话题度 | Humane 已倒闭、Rabbit 口碑滑坡 |

**关键对照轴**：① 开源硬件+软件全栈 vs 全员闭源消费品;② 工具型记录/记忆 vs Friend 情感陪伴;③ 多形态（项链+眼镜+桌面看屏）vs 单一设备;④ 开发者平台 vs 封闭;⑤ 可自托管、数据自控 vs 厂商云。**关键市场信号**：Limitless 被 Meta、Bee 被 Amazon 收购——闭源玩家正被巨头吸纳，而 Omi 以「开源 + 可自托管」占据了大厂难以直接收编的生态位。

**综合结论**——护城河：开源硬件全栈（固件→云→桌面可读可改可自托管）+ 多形态 + 开发者平台 + 主动做竞品中台，是闭源对手难以复制的组合。竞争风险：① 巨头持续收编闭源对手并以体验/分发碾压;② **BLE 断连重连 + 离线同步可靠性是结构性短板**（#6721/#5733/#7221 千文件堆积），直接伤害「不丢记忆」的核心承诺;③ **转写/diarization 质量落后垂直对手**（如 Plaud，#4518/#4455）;④ 免费配额限制（2h/天）+ 营销噪音稀释工程可信度;⑤ 隐私合规是悬顶之剑。生态定位：不做「最好的单一硬件」，做「可穿戴 AI 的开源操作系统 + App Store + 自托管中台」——赌生态与信任。

---

## 隐私与伦理（重点专节）

- **第三方未同意是根本缺陷**：always-on 随身录音意味着**你周围的人在毫不知情、未同意的情况下被录音**。代码层面在 app/backend/docs 中**无任何同意获取/告知机制**（仅命中本地化字符串与系统截屏授权弹窗）;设备唯一对外信号是一颗 LED，不构成有效告知。
- **法律风险**：美国各州录音同意法分裂——加州、佛州等 11+ 州要求**全体同意（two-party）**，违者属刑事窃听;多数州为一方同意。欧盟 GDPR 要求对可识别个人数据有明示合法依据，路人入音几乎不可能满足。Omi 把合规责任完全下推给佩戴者。
- **数据面持续扩大**：① app marketplace 的 `audio_bytes` 级触发把**原始音频流**交给第三方 app;② 桌面 agent 用 ScreenCaptureKit 把**屏幕全文 OCR + embedding**（含他人聊天窗口等一切可见内容）纳入记忆库;③ MCP server 把记忆读写权开放给外部 LLM。每一层都在放大攻击面。
- **加密是 at-rest 而非端到端**：密钥在服务端、服务器可解密;默认云依赖 Firestore（Google）+ Deepgram 云 STT。
- **开源/自托管能解决什么·不能解决什么**：✅ 能解决「数据存哪、谁能改、模型可换」——全套自托管 chart 理论上可做到数据不出自有基础设施。❌ **解决不了「被录的第三方从未同意」**——这是录音行为本身的伦理/法律问题，与代码是否开源、数据存哪台机器无关。**开源 ≠ 合规，自托管 ≠ 他人同意。** 这是 Omi（及整个 always-on 品类）无法用工程手段回避的核心伦理债务。

---

## 套利机会分析

- **对做记忆型 AI/RAG 的开发者**：`process_conversation.py` 的「向量召回 + LLM supersede + 软失效 + 知识图谱」是处理长期记忆去重/矛盾的成熟工程范式，可直接借鉴。
- **对做语音/会议产品的团队**：「STT provider 抽象 + 按语言路由 + BYOK」+「在线质心聚类说话人 + 失败保留标签」是可复用的稳健工程模式。
- **对做可穿戴/IoT 采集的工程师**：nRF52 BLE 音频固件（MTU 分片 + 序号头 + 离线落盘）+ Flutter「设备连接抽象 + WAL 离线优先同步」是完整参考。
- **对做 agent 互操作的人**：desktop 的 ACP 桥接 + 把私有数据封装成 agent tools，是「让外部 agent 操作私有上下文」的范式。
- **对内容创作者**：「全栈开源 AI 硬件」「两个 Friend 改名公案」「always-on 录音的隐私伦理」都是有张力的选题。

---

## 风险与不足

- **always-on 录音的第三方未同意（最严重）**：开源和自托管都解决不了「被录者没同意」的伦理与法律债务，是悬顶之剑。
- **BLE 与离线同步可靠性**：断连不自动重连（#6721）、离线同步静默丢数据/千文件堆积（#5733/#7221）——直接伤害「不丢记忆」的核心承诺。
- **转写/diarization 质量落后垂直对手**：整段转写缺失、跨段说话人分离失效（#4518/#4455），不如专注垂直的 Plaud。
- **重交付轻重构的技术债**：refactor 仅 0.5%，`transcribe.py` 3062 行等巨型文件、重复 STT socket 实现累积;注释比 0.085 偏低。
- **营销噪音 vs 工程可信度**：创始人病毒营销（融资/改名公案）的热度，与工程可靠性投入不完全匹配。
- **加密非 E2E + 默认云依赖**：默认路径数据经 Firestore/Deepgram，服务端可解密;真正数据自控需自行搭全套自托管栈（门槛高）。

---

## 行动建议

- **用它（谨慎）**：可买现成设备（~$89）或 DIY 烧固件;若重视隐私，用 `backend/charts/` 全套自托管栈让数据不出自有基础设施。**但务必了解所在地录音同意法，并主动告知/征得周围人同意**——这是工程之外你必须承担的责任。
- **学它**：精读 `backend/utils/conversations/process_conversation.py`（记忆冲突消解）+ `backend/utils/stt/streaming.py`（STT 路由 + 在线说话人聚类）+ `omi/firmware/devkit/src/`（BLE 音频固件）+ `app/lib/services/wals/`（WAL 离线同步）。
- **fork 它**：MIT，可二次开发整条全栈;开发第三方 app 走 webhook + prompt 机制（注意 `audio_bytes` 级触发的隐私放大）。
- **别忽视伦理边界**：介绍/使用该类产品时，「开源 ≠ 合规、自托管 ≠ 他人同意」是必须如实说明的底线。

---

## 知识入口

| 入口 | 链接 | 用途 |
|---|---|---|
| GitHub 仓库 | <https://github.com/BasedHardware/omi> | 全栈源码 / Issue |
| 官网 | <https://omi.me> | 产品/购买/博客（含「AI 笔记是否合法」合规讨论） |
| 文档 | <https://docs.omi.me> | Getting Started / Hardware 组装 / Firmware / App 开发 |
| App Store | <https://h.omi.me> | 250+ 第三方 app / personas |
| DeepWiki | <https://deepwiki.com/BasedHardware/omi> | AI 架构导览 |
| 核心源码切入点 | `backend/utils/conversations/` / `omi/firmware/devkit/src/` / `app/lib/services/` / `desktop/Backend-Rust/` | 架构研读起点 |
| 创始人 | X @kodjima33 / nikshevchenko.com | 项目背景 |
