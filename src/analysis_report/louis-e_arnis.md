# 4 个月从 0 到 16K stars：20 岁 BMW 工程师用 Rust 把地球搬进 Minecraft

> GitHub: https://github.com/louis-e/arnis

## 一句话总结

Arnis 是一款 Rust 写的开源工具，把 OpenStreetMap + AWS Terrain Tiles + ESA WorldCover 卫星分类实时拼装成可玩的 Minecraft 世界，同时支持 Java / Bedrock / Luanti 三种世界格式输出，4 个月从 Python 原型重写后 star 突破 1.6 万。

## 值得关注的理由

- **垂直赛道近乎垄断的工程实现**：开源世界把『OSM → MC 世界』做成产品级工具，Terra 1-to-1 (1800 stars) 已停更、BuildTheEarth 是人工 1:1 体力活、OSM2World/blosm 不直接出 MC 世界——Arnis 几乎没有同量级对手。
- **真实的工程取舍案例**：Minecraft Y=384 硬高度限制 vs 真实世界任意 bbox 海拔差，用『归一化 + bundled datapack 拉到 4064』双层化解，是少有的『游戏引擎 vs 真实世界』边界处理范例。
- **学术 + 行业 + 玩家三圈层背书**：AWS Public Sector 博客、Hackaday、Tom's Hardware、XDA 持续报道；K-12 教育论文（Floodcraft）作平台引用；Discord 1.3 万成员。

## 项目展示

![Banner](https://raw.githubusercontent.com/louis-e/arnis/main/assets/git/banner.png)

![Minecraft Preview](https://raw.githubusercontent.com/louis-e/arnis/main/assets/git/preview.jpg)
<i>海德堡老城 1:1 还原——你能在自己长大的地方玩 Minecraft。</i>

![GUI](https://raw.githubusercontent.com/louis-e/arnis/main/assets/git/gui.png)
<i>Tauri 2.0 桌面客户端，矩形工具选区域，点 Start Generation 即可。</i>

![Documentation](https://raw.githubusercontent.com/louis-e/arnis/main/assets/git/documentation.png)
<i>完整 Wiki 覆盖技术原理、FAQ、贡献指南、Roadmap。</i>

> 背景演示视频：[backgroundvid.webm](https://github.com/user-attachments/assets/420acc19-a850-418e-8397-1a45b05582ab)

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/louis-e/arnis |
| Star / Fork | 15,949 / 1,316 |
| 代码行数 | 76,603（Rust 53.2% / JavaScript 36.0% / JSON 4.6% / CSS 4.5%，纯 Rust 50,593 行） |
| 项目年龄 | 44.9 个月（2022-09-10 至今） |
| 开发阶段 | 密集开发（近 30 天 155 commit，近 90 天 568 commit） |
| 贡献模式 | 独立开发为主（louis-e 81.2% commit）+ 多国社区 PR 补位（53 贡献者） |
| 热度定位 | 大众热门（2024-12 破圈后稳定在 15K+ stars） |
| 质量评级 | 代码 [优秀] 文档 [优秀] 测试 [基本] CI/CD [完善] 错误处理 [规范] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Louis Erbkamm (louis-e)，20 岁，BMW 集团 Android/AOSP 平台工程师（巴伐利亚/慕尼黑），bio: "🌌 space & science fanatic // 20 y/o"。GitHub 7.6 年，主业负责蓝牙/Wi-Fi/Neue Klasse 平台层，2024 年转正。早期经历 freelance web → TV1 GmbH 3D 直播 → BMW 学徒——把『3D 直播渲染经验 + AOSP 平台层抽象（feature gate / stub module） + Rust 高性能』三件套用在 Minecraft 上。

> 公开博客：louisdev.de

### 问题判断

作者看到的是**『OSM 数据丰富 + Minecraft 玩家基础大 + 自动化 1:1 地图工具稀缺』**的三方错位。Terra 1-to-1 等老牌工具停留在 Python+Tkinter、只支持 Java、不做高程。BuildTheEarth 是全球社区人工体力活。OSM2World/blosm 面向通用 3D 引擎不直接出 MC 世界——**没有人在维护『开源、自动、跨版本、能真实还原地形』这条产品线**。

时机：2024-12 月 AWS Terrain Tiles 等开放 DEM 数据成熟、OSM Overpass API 稳定、Tauri 2.0 解决跨平台桌面应用打包。三件事凑齐，作者顺势把 Python 原型重写为 Rust。

### 解法哲学

**拒绝单一完美方案，转向多源自适应 + 多格式输出 + 模块化替换**——这跟 ML 圈『一个模型压全场』的趋势相反，更接近 Unix 哲学 + 微内核 + 平台工程的现代合流：

- **不追求『1:1 真实海拔』**：承认 Minecraft 384 块硬约束是 game-engine 与 real-world 的本质 gap，默认做归一化、玩家可启用扩展 datapack
- **不押注单一数据源**：6 个 elevation provider（AWS Terrain Tiles / Overture Maps / USGS 3DEP / IGN France / IGN Spain / SRTM）自适应 fallback
- **不做 AI 推演**：纯规则算法（OSM tag → 块类型映射），确定性、可复现、零幻觉
- **不强制 GUI**：同一二进制默认 GUI，`--no-default-features` 编 headless CLI 跑 Docker / CI
- **不锁定 Minecraft 版本**：Java 1.17+ / Bedrock / Luanti 三套世界格式共用内存数据模型

### 战略意图

主仓保持 Apache-2.0 + 强烈 open-core 倾向。**MapSmith**（README 提到的浏览器 SaaS 化补充）可能是商业化试水——『开源是开发者入口，浏览器 SaaS 是大众入口』的经典双轨。最大 250 km² 的浏览器生成服务，可能走『免费额度 + 付费扩大 + 商业 API』路径。

> AWS Public Sector 博客背书说明已进入『学者 + 行业 + 玩家』三圈层。

## 核心价值提炼

### 创新之处

按新颖度×实用性排序：

1. **Land-cover-aware elevation repair**（histogram mode 水面 + Gaussian σ=30m 平滑建成区 + 25m 海岸线 BFS 内插）—— 一次性解决 DEM+DSM 城市区域『看起来像被啃了』的伪影，可迁移到任何『栅格地形 + 卫星分类 mask』pipeline
2. **Y=384 hard cap 倒逼的『归一化 + bundled datapack』双层设计**—— 不与引擎硬约束抗争，先 scale_to_minecraft 压缩、必要时 bundled datapack 把 min_y 拉到 -2032 / height 4064；通过运行时改写 level.dat 注入 file/arnis_tall 来『装载时扩界』
3. **Overture Maps GeoParquet 远程 row-group 过滤**—— HTTP Range 读 footer → ParquetMetaData → bbox-overlap 过滤 row group → 只下载相关 row group 的列数据，避免下载 TB 级文件；OSM ID 高位加 0x8000_0000_0000_0000 避免冲突
4. **Cloud-Optimized GeoTIFF HTTP Range 读 + ESA WorldCover land cover 流水线**—— ESA WorldCover 10m 分辨率 ~500MB/tile，用 HTTP Range 读 COG 内部 tile 而不下载整文件；通用 COG 处理模式，可直接 copy 到 S2 / Sentinel / NAIP
5. **预计算 floodfill + 1-bit 坐标位图 + Arc<Shared> 缓存**—— 24 个 element 子模块都要 flood fill 同样的 OSM way，主循环前 rayon 并行预计算；Arc<Vec<(i32, i32)>> 共享（refcount bump 代替 deep clone）；1-bit 位图（5000×5000 = 3MB）替代 HashSet（1.2GB）做 footprint 集合

### 可复用的模式与技巧

- **Feature-gate 双入口 + stub module**：`Cargo.toml` 的 `default = ["gui"]` 让 `cargo run` 起 GUI，`cargo run --no-default-features` 编 headless CLI；`#[cfg(feature = "gui")]` 隔离 progress/telemetry 依赖。任何『GUI 可选 / 跨多个 headless 入口』的 Rust 项目都可借鉴
- **Provider 链 + bbox overlap + 自适应 fallback**：按分辨率倒序选择 → bbox overlap 检测 → 失败时 fallback → 区域空数据率 >50% 时再次 fallback → NaN ratio 自检；任何『多源异构数据 + 自动选最佳源 + 失败降级』的 pipeline 都适用
- **Precompute + Arc<Shared> + empty sentinel**：主循环前并行预计算 → Arc 共享 → `OnceLock` 静态空集零分配；『内存敏感 + 并行热点 + 多 consumer』场景的通用模式
- **Datapack/runtime pack 注入扩界**：游戏引擎硬约束（build height / 物件数）需要用户态『临时加 mod』绕过的工程模式
- **HTTP Range 读 COG/Parquet 远程 footer**：TB 级地理数据在云上，做 bbox 局部切片又不下载全文件的标准做法

### 关键设计决策

- **OSM 北向上 vs MC 玩家朝北向小 Z 的冲突**：用 lat → -z 翻转一次性解决，**拒绝 Issue #97 的任意角度旋转请求**——反映对浮点误差 + 性能的硬约束。代价：玩家必须接受「北向上」作为约束
- **land cover 修正 elevation 而非反过来**：`elevation/postprocess.rs:151-211` 后处理流水线做 MAD 异常修复 → IQR 双向过滤 → NaN 邻域填 → land-cover-aware repair；承认数据噪声不可避免，用分类 mask 当先验
- **多源 elevation provider 链**：6 个 provider（AWS Terrain Tiles 30m 兜底 / Overture Maps / USGS 3DEP 1m / IGN France / IGN Spain / SRTM），按地区自动选最佳
- **三套 world format 抽象 + 共用 WorldToModify 内存模型**：Java Anvil（fastanvil + NBT gzip）/ Bedrock（LevelDB + zip mcworld）/ Luanti（sqlite map.sqlite），写时统一修改内存 `WorldToModify`，save 时三个后端各自序列化
- **Claude Issue Bot 自动回复**：2026-05 上线，claude-code-action 驱动 Sonnet，给新 issue 自动找最多 3 个重复 + 高置信 grounded 解决提示；prompt 要求『只输出 grounded 证据（PR 号 / 合并的修复 / 版本）』，禁止泛化排错和臆造

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Arnis | Terra 1-to-1 | BuildTheEarth | OSM2World/blosm | 国家地理院项目 (minecraft.ign.fr) |
|------|-------|--------------|---------------|-----------------|----------------------------------|
| Stars | 15,949 | ~1,800 | ~1,000 | 数百~千 | N/A |
| 维护状态 | 密集开发 | 已停更 | 社区活跃 | 中等活跃 | 一次性 |
| 自动化程度 | 完全自动 | 完全自动 | 全人工 | 完全自动 | 半自动 |
| 跨版本 | Java 1.17+ / Bedrock / Luanti | 仅 Java | 任意 | 不产 MC | 不产 MC |
| 跨平台 | Win/macOS/Linux + 云端 | 桌面 | 任意 | 任意 | 不可下载 |
| 高程数据 | 6 个 provider + land cover 修正 | 无 | N/A | 无 | 专业级 |
| 输出 | 直接可玩 MC 世界 | MC 世界 | MC 世界 | OBJ/Blender | 不可下载 |
| 3D 模型 | 3DMR + Wikimedia glTF | 无 | N/A | 通用 mesh | N/A |
| GUI | Tauri 2 桌面 | Tkinter | 无 | 桌面 | 不可下载 |
| 学术引用 | ✅ K-12 论文 | ❌ | ❌ | ❌ | 有限 |
| 商业模式 | 开源 + MapSmith SaaS | 无 | 众筹 | 无 | 官方项目 |

### 差异化护城河

- **技术栈** = 6 个 provider 自适应 + 三 world format 共用内存模型 + 3DMR 嵌入 + Land-cover-aware elevation repair——**这套管线竞品几乎无法快速复制**，因为它需要同时懂 OSM 数据生态、MC 世界格式反向工程、地理数据科学
- **生态** = Discord 1.3 万成员、AWS Public Sector 博客、Hackaday / Tom's Hardware / XDA 持续报道、3 篇学术论文引用、Floodcraft K-12 教育落地
- **数据飞轮** = 贡献者按 OSM 区域聚集（Oleg4260 拉脱维亚、TheComputerGuy96 立陶宛、HelleBenjamin 爱沙尼亚、krvstek 波兰、XianlinSheng 中文），『按真实城市生成』设计天然吸引本地 OSM 贡献者

### 竞争风险

- **最大风险** = MapSmith（自家 SaaS）一旦成熟可能把开源版边缘化；但作者明确表示主仓保持 Apache-2.0 + 强烈 open-core
- **次要风险** = Minecraft 协议变更（Bedrock 区块结构、Java datapack 格式）需要持续跟进——louis-e 2025-01 社区 PR 爆发说明这是个『单人核心 + 社区补位』的良性循环
- **长尾风险** = 国家地理院项目若出大众版（法国/荷兰已存在），可能蚕食教育市场；但 Arnis 的『任意 bbox』优势仍在

### 生态定位

在整个『MC + 开放地理数据』的交叉点，Arnis 是**明显头部项目**，填补了『自动化 + MC 原生世界格式 + 多源高程 + 卫星 land cover + 跨版本』五件事的空白。

## 套利机会分析

- **信息差**: 已大众曝光（AWS / Hackaday / Tom's Hardware），不是被低估潜力股；但**垂直赛道近乎垄断位置稳固**，长期持有价值高
- **技术借鉴**: 
  - **HTTP Range 读 COG/Parquet 远程 footer** 模式可迁移到任何 TB 级地理数据 ETL
  - **Feature-gate 双入口** 模式适用于任何 CLI + GUI 双形态的 Rust 项目
  - **Land-cover-aware elevation repair** 适用于城市规划可视化、洪水模拟、地形数据预处理
  - **Datapack 注入扩界** 适用于任何『游戏引擎硬约束 vs 真实数据』场景（UE / Unity / Roblox）
- **生态位**: 填补了『MC + 开放地理数据』交叉点的空白；与 K-12 教育（防洪 / 城市规划）、OSM 社区可视化、独立游戏 modpack 三个方向都有合作空间
- **趋势判断**: 
  - ✅ **在增长**（4 年累计 15.9K stars，2024-12 破圈后稳定流入）
  - ✅ **符合技术趋势**（开放数据 / 数字孪生 / 地理可视化 / 游戏化学习）
  - ✅ **后发优势**（Rust 重写后 4 个月 commit 量比 Python 时代 1 年还多，吞吐量提升约 5-6 倍）

## 风险与不足

- **测试覆盖偏弱**：184 个 `#[test]` 函数覆盖坐标变换、provider 选择、postprocess、cache 清理、JSON 解析等纯逻辑；**缺端到端测试**（生成结果的视觉/结构正确性靠人工），无 fixture 完整世界
- **没有 CHANGELOG.md**：用 git log + GitHub Releases 代替，对 changelog-driven 工具链（如 release-please）不友好
- **Issue #97 旋转地图至今未做**：核心玩家诉求未满足（OSM 默认地理北向上 vs MC 玩家习惯出生点为南），**暴露当前轴系约束仍未解决**——`CoordinateTransformer` 的 lat→-z 翻转是一次性设计
- **Minecraft 协议强耦合**：fastanvil / fastnbt / bedrockrs_level / nbtx 全部 git pin 在 rev 上，**Mojang / Bedrock 协议变更时需要 4 个上游同步更新**
- **国际化是社区驱动**：俄 / 乌 / 瑞 / 韩 / 西 / 土 / 阿多语种 PR 涌入，作者只做框架与合并；**单点故障风险**：louis-e 一人占 81% commit
- **macOS 构建历史问题**：`test-macos-build.yml.disabled` 备而不用，说明 macOS 构建曾有问题
- **OOM / TIFF / cache 修复是反复话题**：2026-04 月 276 commit 大部分是修多源高程管线的 OOM、TIFF 损坏、cache 失效——**地理数据管线的稳定性是持续投入项**

## 行动建议

### 如果你要用它

- **普通玩家**：直接下载 [Release](https://github.com/louis-e/arnis/releases) GUI 版本，矩形选区域 → Start Generation。Java 1.17+ / Bedrock 都可
- **模组服主 / 大型生成**：CLI 版本（`cargo run --no-default-features`）+ `--bbox` 参数，可跑 Docker / CI 批量生成
- **教育场景**：K-12 防洪教学参考 [Floodcraft 论文](https://www.researchgate.net/publication/384644535)
- **移动端 / 不想装**：用 [MapSmith](https://arnismc.com/mapsmith/) 浏览器版，最大 250 km²

### 如果你要学它

重点关注以下文件/模块（按 learning value 排序）：

| 文件 | 改动次数 | 学习价值 |
|------|---------|---------|
| `src/elevation/postprocess.rs` | - | Land-cover-aware elevation repair（histogram mode + Gaussian + BFS） |
| `src/elevation/selector.rs:26-50` | - | 多源 provider 链 + bbox overlap + 自适应 fallback |
| `src/floodfill_cache.rs` | - | Precompute + Arc<Shared> + 1-bit 位图 + empty sentinel |
| `src/coordinate_system/` | - | LLBBox/XZBBox/CoordTransformer 隔离 lat/lng 地理坐标与 XZ 局部笛卡尔 |
| `src/element_processing/buildings.rs` | 175 | OSM tag → Minecraft 块映射的建筑核心（门窗/屋顶/楼层） |
| `src/world_editor/` | 134 | 三套世界格式（Java/Bedrock/Luanti）+ 共用内存模型 |
| `src/main.rs:362-381` | 126 | CLI/GUI 双入口分发 + `#[cfg(feature = "gui")]` 隔离 |
| `src/models_3d/` | - | 3DMR / Wikimedia glTF → dda-voxelize → 替换方块（保留 magenta sentinel 做 GLASS） |
| `src/overture.rs` | - | Overture Maps GeoParquet 远程 row-group 过滤 |

### 如果你要 fork 它

可以改进的方向：

- **E2E 测试**：用黄金截图 + 区块结构 diff 验证生成结果（参考 [Minecraft 快照测试框架](https://github.com/llasram/mc-world-rs)）
- **Issue #97 旋转地图**：CoordinateTransformer 引入 quaternion 旋转 + bbox 重投影（代价：浮点误差 + 性能，**这是个 trade-off 学习机会**）
- **更多 world format**：Hytale / Vintage Story / Vintage Story 的 [C# 实现](https://github.com/ancientmultitudes-org/vintage-story-essentials) 可参考
- **WebAssembly 编译**：Tauri 2 + Rust → WASM 可以在浏览器本地生成（与 MapSmith SaaS 互补）
- **更精细的建筑语义**：从 OSM Multipolygon → 房间分割 / 门窗放置（参考 [osm2streets](https://github.com/a-b-street/osm2streets) 街道语义）
- **生成结果可视化**：Tauri 窗口内嵌 3D 预览（用 [three.js](https://threejs.org/) 加载区块）—— 这是从『生成工具』升级到『设计工具』的关键

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/louis-e/arnis |
| Zread.ai | https://zread.ai/louis-e/arnis |
| 关联论文 | [Floodcraft: Game-based Interactive Learning Environment using Minecraft for Flood Mitigation](https://www.researchgate.net/publication/384644535) |
| AWS 案例研究 | [Building realistic Minecraft worlds with Open Data on AWS](https://aws.amazon.com/de/blogs/publicsector/building-realistic-minecraft-worlds-with-open-data-on-aws-how-arnis-uses-elevation-datasets-at-scale/) |
| 媒体评测 | [Hackaday](https://hackaday.com/2024/12/30/bringing-openstreetmap-data-into-minecraft/) / [Tom's Hardware](https://www.tomshardware.com/video-games/pc-gaming/minecraft-tool-lets-you-create-scale-replicas-of-real-world-locations-arnis-uses-geospatial-data-from-openstreetmap-to-generate-minecraft-maps) / [XDA Developers](https://www.xda-developers.com/hometown-minecraft-map-arnis/) |
| 在线 Demo | [MapSmith 浏览器版](https://arnismc.com/mapsmith/)（最大 250 km²） |
| 官方 Wiki | https://github.com/louis-e/arnis/wiki/ |
| 作者博客 | https://louisdev.de |
