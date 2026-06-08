# 零实现、零着陆页、109% 覆盖率：13.5K stars 的「不存在的编程语言」怎么让 HN 反复推爆

> GitHub: https://github.com/todepond/gulfofmexico

## 一句话总结

`todepond/gulfofmexico`（前名 DreamBerd）是一门**永远不会被实现的编程语言**：作者 Lu Wilson 把 JS/Python 痛点（4 个 `===`、null、NaN、import 关税）拉到荒诞极值，用一个 21.8KB 的 README 当作品本体，49.8 个月长出 13,542 stars 和 177 位贡献者——是 GitHub 上少见的「代码即概念艺术」实验场。

## 值得关注的理由

- **「零实现」破 13.5K stars 的反常样本** —— 没有 parser、没有解释器、没有 landing page，却同时登上 HN、Twitter、Bluesky；项目即作品，是 2020 年代程序员文化共鸣的代表案例。
- **自指性元幽默做到极致** —— `test/test/test/.../test.md` 9 层嵌套目录被 commit 反复 +1（「Increment cheat count」），84 次 commit + 109% 覆盖率徽章 + 36 个荒诞 tag（`v£.££` / `vNaN.NaN` / `vU.S.A`），每一个工程指标都成为 meme 素材。
- **可迁移的 5 个开源运营技巧** —— 「文档即规范」「Cheat count 计数器」「Bounty 慈善捐款」「接力陷阱」「CI 反讽」—— 这些玩法在内容项目、社区驱动项目、个人品牌里都能直接复用。

## 项目展示

![shapes.png](https://raw.githubusercontent.com/todepond/gulfofmexico/main/shapes.png)

*README 头图，仓库里唯一的 hero 资产，作者手工绘制的几何形态，呼应项目的「4 等号/反 export/无循环」抽象语法观。*

> 官网 `dreamberd.computer` 故意没有 landing page（「For the integrity of our open-source integrity, we don't have a landing page」），README 本身就是规范 + 教程 + 表演的混合体。

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/todepond/gulfofmexico |
| Star / Fork | 13,542 / 466（watchers 46） |
| 代码行数 | tokei 报告 32 行（SVG 56.2% + HTML 43.8%），**严重低估**——`suite/*.db`（28 个 SQLite 文件）不计入，实际数千行「代码即数据」 |
| 项目年龄 | 49.8 个月（2022-04-17 首次提交） |
| 最近推送 | 2026-01-20（近 90 天 0 commit，低维护） |
| 开发阶段 | 低维护（4 次脉冲月 + 长草期，月均 commit ≤3） |
| 贡献模式 | **个人品牌主导**（Lu Wilson 三种 author 署名占 67%，其余 30 人贡献碎片化） |
| 热度定位 | **大众热门（迷因型）**——13.5K stars 增长不是被低估，是已破圈 |
| 质量评级 | 作品完成度 **优秀** / 传播力 **优秀** / 概念深度 **优秀** |
| License | 自定条款（`LICENSE.md`，非 OSI 标准） |
| 真实入口 | https://dreamberd.computer（README = 规范） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

**Lu Wilson**（GitHub 署名变体 `Lu Wilson` / `Lu[ke] Wilson` / `Luke Wilson`，三号共享同一邮箱 `l2wilson94@gmail.com` = 同一人），现就职于 **tldraw**（白板工具），曾在 Ink and Switch 实验室工作（Cap'n Proto 母公司），伦敦创意编程圈核心成员。粉丝 2,333 / 公开仓库 133 / 账号 10.6 年。

Lu 的整体艺术实践跨四个域：① 创意编程视频（todepond.com 自述」surreal videos, talks, tools and music」）② 乐队 Pastagang ③ 现场表演（」Game of Living「）④ 概念装置（DreamBerd = 这个仓库）。`gulfofmexico` 不是他的「业余 side project「，是其**核心艺术装置**之一，与 tldraw 的工业级创意编程工作**互相喂养**：tldraw 的视觉化能力让 README 表演成立，DreamBerd 的传播力放大 tldraw 圈层势能。

### 问题判断

Lu 看到的是**程序员文化的「严肃性过剩」** —— JavaScript 用 3 个 `===` 还嫌不够，Python 的 `None` vs `null` 天天撕，C++ 的 undefined behavior 没人敢碰，TypeScript 的 `any`/`unknown`/`never` 三层抽象挡不住运行时崩溃。主流语言是」用更复杂的规则修补更复杂的问题「。

DreamBerd 反向操作：把「应该严谨」的事**严谨到荒诞**——`====` 才是恒等、`maybe` 是 boolean 的第三个值、import 收 25% 关税、变量能看 `previous`/`next`、不完整的代码会被自动 email 给作者。**夸张让痛点显形**——读者笑完才发现自己真的在乎 `===` vs `==`。

### 解法哲学

- **简单 vs 功能完整** → 选」规则极多但完全荒诞」——故意」做错每件事「，违反 Unix 哲学「做一件事做好「
- **开放 vs 封闭** → 极致开放：README 写明 「I will happily accept any PR that adds to this README」——连致敬 emoji 都 merge
- **不做什么** → **不写实现**、**不写 landing page**、**不写 changelog**、**不做严肃工程化**——主动放弃」软件」身份，把自己定位为「作品（artifact）「
- **跨域移植** → 把「概念艺术 + Hacker 文化 + tldraw 视觉语言 + 音乐表演」全部揉进一个 GitHub 仓库

### 战略意图

`gulfofmexico` 在 Lu Wilson 的更大艺术图景里**不是产品**——是**装置**，与 Pastagang / Game of Living 平行。反商业化姿态的商业化模式：

- `docs/investment/` 投资者大厅，标注「投资 £461.33 起」
- `bounty/` 慈善捐款，完成 X 任务作者转 £99 给慈善
- 主页留 Patreon / Liberapay / Bounty 入口

商业化的」反讽形式」是 **Gulf of Mexico 这个项目最深的 strategic intent**：作品性强到不能「用「 → 不能用就不会被商品化 → 不会被商品化就只能是作品 → 作品的传播力反哺作者个人品牌 → 个人品牌给 tldraw / 创意编程圈层势能。

## 核心价值提炼

### 创新之处

按 **新颖度 × 实用性** 排序的创新点列表：

1. **自指性元语言（README 自演示）** — 新颖 5/5，修改 README = 修改语言本体（README 被改 204 次）
2. **荒诞选项生成器** — 新颖 4/5，任何「X 个选项太少了」问题，加一项荒诞选项 = 完整讽刺（适用内容运营）
3. **反向 export**（`export add to 「main.gom」`）— 新颖 5/5，改写 import/export 默认方向
4. **Cheat count**（git log 作 meme 计数器）— 新颖 4/5，嵌套 9 层 `test/` 目录 + 84 次 commit + 「I swear I didn't cheat」
5. **Bounty 慈善捐款** — 新颖 4/5，完成 X 任务作者转 £99 给慈善
6. **三层接力陷阱**（Examples.md 链）— 新颖 5/5，4 层假页面，谴责读者「你跳着读了！」
7. **Vision Pro 启动页 + 8 分钟 YouTube 发布会** — 新颖 5/5，仿 Apple 发布会做 esolang 发布会
8. **VSCode 正则高亮**（`.vscode/settings.json`）— 新颖 3/5，支持 `function` 的任意前缀（`funct`、`fun`）
9. **`delete class` / `delete delete` 终极状态** — 新颖 4/5，删完删 delete = zen
10. **Cape Verdean escudo 字段访问**（`{player$name}`）— 新颖 5/5，真实非洲小国货币格式规范化进语言
11. **Star history 自更新 PNG**（`files/star-history.png`，6 次 commit）— 新颖 3/5，README 引用图本身被 commit 更新
12. **CI 反讽**（`action-which-doesnt-do-anything.yml` + 109% 徽章）— 新颖 5/5，空 workflow + 静态 SVG，注释「This exists only to show the green checkmark」

### 可复用的模式与技巧

可直接迁移到其他项目的设计模式和代码技巧：

1. **文档即规范** — 单一 README = spec + tutorial + 表演，零依赖。→ 教学项目 / 概念项目 / 个人品牌站点
2. **荒诞选项对比法** — 加 1 个荒诞选项 = 完整讽刺。→ 内容运营、博客、产品吐槽
3. **Cheat count 计数器** — 把「项目活跃度」做成可玩计数器（用嵌套目录 + 重复 commit）。→ 社区运营
4. **接力陷阱** — 4 层假页面（Examples.md → res/ → res/res/ → test/），谴责跳读的读者。→ 反碎片化阅读内容
5. **Bounty 慈善捐款** — 完成社区任务作者转给慈善（不拿钱给个人）。→ 社区驱动 / 反商业化
6. **CI 不做任何事** — 空 workflow + 注释「This exists only to show the green checkmark」 + 109% 静态徽章。→ 反讽工程 KPI
7. **改名 = 事件营销** — 2025 改名 DreamBerd → Gulf of Mexico，对位 Trump 政府更名令 + 撞击新闻周期。→ 长期项目重启传播
8. **Issue 即剧场** — `#297 rename C` / `#169 Rust` / `#83 9,999 stars` / `#844 zero-quote strings` 都是治理的公开表演。→ 围观治理 / 社区参与
9. **AI 四层递进** — AEMI（自动感叹号）→ ABI（自动括号）→ AQMI（自动引号）→ AI（自动代码 + email 作者）。→ 对位 AI 时代的产品哲学
10. **`badges/` 静态 SVG 徽章** — 109% 覆盖率 = 工程指标的」反讽性完成」。→ 任何需要「展示完成度「的项目

### 关键设计决策

12 个值得学习的架构选择和 trade-off：

| # | 决策 | 解决的问题 | 方案 | Trade-off | 可迁移性 |
|---|---|---|---|---|---|
| 1 | 文档即运行时 | 没有实现的语言如何「存在」 | README 单一文件承担 spec + tutorial + 表演 | 失去可执行性，换来作品性 | **高** |
| 2 | 零实现 + 悬赏第三方 | 不写实现怎么让语言成立 | bounty £99 + 注释里挂第三方实现（vivaansinghvi07/dreamberd-interpreter）| 项目不能跑；换得「实现本身」成为社区 meme | **中** |
| 3 | Issues 当剧场 | 语言演化如何被围观 | Issue 标题即语言治理提案（#297 rename C、#83 9,999 stars）| Issues 噪声大；换得治理公开表演 | **中** |
| 4 | Cheat count 9 层嵌套 | 大量 commit 看起来「没推进」项目 | 把 commit 本身做成 meme 计数器 | tokei 统计失真；换得项目即 meme | **高** |
| 5 | 4 层假 Examples.md 接力陷阱 | 碎片化阅读习惯 | 每个链接都是假页面，谴责读者「你跳着读了！」 | 浪费读者时间；换得反碎片化阅读姿态 | **高** |
| 6 | CI 反讽 + 109% 徽章 | 绿勾=信任=假象 | 注释「This exists only to show the green checkmark」 + 硬编码 109% 徽章 | 误导新人；换得对工程 KPI 的精准吐槽 | **中高** |
| 7 | 改名 Gulf of Mexico（2025）| 长期项目如何重启传播 | 与 Trump 政府更名令对位，撞击新闻周期 | 失去旧品牌；换得新流量峰值 | **高** |
| 8 | 4 等号 / maybe bool / negative lifetime | 工程师为什么对 TS / null / NaN 焦虑 | 任何」应该严谨」的事都「严谨到荒诞「 | 需要 JS 文化基础才笑得出来；换得程序员群体强共鸣 | **高** |
| 9 | AI 四层递进 | 2023 AI 自动补全 hype 怎么对位 | 4 种自动插入讽刺，末项「email Lu」是行为艺术 | 现实主义失败；换得对 AI 时代的精准反讽 | **中** |
| 10 | DBX 替代 JSX | 保留字冲突 | `class` → `htmlClassName`，`for` 因「no loops」被允许 | 学习曲线；换得概念一致性 | **中** |
| 11 | `delete` 关键字范式 | 多范式 vs 选择困难 | 删你不喜欢的；删完删 `delete` = zen | 不可逆；换得「删除即设计」哲学 | **中** |
| 12 | Cape Verdean escudo 字段访问 | 普通 `$` 太无聊 | `{player$name}` 真实非洲小国货币格式规范化进语言 | 学习成本；换得文化性 | **低** |

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | **Gulf of Mexico** | Brainfuck | INTERCAL | Shakespeare | Piet | Carbon / Mojo |
|------|---------|---------|---------|---------|--------|--------|
| 是否有真正实现 | ❌（零实现，悬赏第三方）| ✅ | ✅ | ✅ | ✅ | ✅ |
| 图灵完备 | 声称是（无证明）| ✅ 有证明 | ✅ | ✅ | ✅ | ✅ |
| 主要语法范式 | JS-like（C 风格 + async + signals）| 8 字符 | 60 年代 ALGOL | 莎士比亚戏剧 | 图像色块 | C++ 替代 |
| 文化定位 | 程序员文化共鸣 / 概念艺术 | 图灵机教学 | 学院派讽刺 | 文学性伪装 | 视觉伪装 | 「下一代语言」营销 |
| 传播机制 | HN/推特/视频/Issue 剧场 | 极客圈 | 学术圈 | 文学圈 | 视觉艺术圈 | 企业背书 + benchmark |
| 严肃性 | 0%（拒绝）| 中等 | 高 | 中等 | 中等 | 100% |
| 商业化 | 反商业化的商业化（投资/赏金/捐款）| 无 | 无 | 无 | 无 | 企业级 |
| 视频化发布 | ✅（Vision Pro + 8 分钟 YouTube）| ❌ | ❌ | ❌ | ❌ | ✅（企业发布会）|
| 创作者人设 | 创意编程艺术家（Lu Wilson / tldraw）| Urban Müller（编译器作者）| Don Woods / James Lyon | Karl Hasselström / Jon Åslund | David Morgan-Mar | Google / Modular |

### 差异化护城河

**文化护城河 ≫ 技术（无）≫ 生态（0）**

- 49.8 月沉积 + 63 真实贡献者 + 177 contributor 名录 = 时间维度难复制
- 改名事件营销（DreamBerd → Gulf of Mexico）撞 Trump 更名令 = 借势政治议程
- 跨媒介完整：文字 + 视频 + 音频 + 视觉 + 现场 + 音乐 = 单一作者作品集
- Lu Wilson 创意编程圈层势能 + tldraw 工业级背景 = 创作者个人 IP 难复制

**真正护城河是「时间 × 跨界 × 人设」三位一体**，不是代码或技术。

### 竞争风险

最可能被替代的情况：

- **同质新项目**：「假语言 + 真传播」新项目出现 → 难复制 49.8 月沉积 + 改名事件营销组合，但若新作者有同等创作者人设，可能分食关注度
- **平台变迁**：如果 GitHub 限缩 Issues 公共剧场功能、Pages 限缩静态站点能力，传播力下降
- **作者精力转移**：Lu Wilson 已在 tldraw 担任工业级创意工程师工作，gulfofmexico 已是」代表作」而非「主战场「（commit 频率可证）→ 新作品可能取代其作为艺术装置的位置

### 生态定位

在整个技术生态中扮演什么角色：

- **esolang 谱系**：偏」传播 / 概念艺术」端（vs Brainfuck 偏「图灵机教学「端）
- **艺术作品谱系**：偏「程序员文化共鸣」端（vs 学院派戏仿）
- **开源运营谱系**：偏「个人品牌 + 反商业化商业化」端（vs 企业级开源的 open-core）
- **填补的空白**：**没有其他 esolang 真正做到」零实现 + 大众传播」**——Brainfuck / INTERCAL / Shakespeare / Piet 都有真正实现，传播力局限在极客圈；Carbon / Mojo 严肃到没有「作品性「

**Gulf of Mexico 的不可替代定位：在」作品性」和「传播力「交叉点上独占，且这种独占是创作者 IP × 时间 × 跨媒介沉积的复合结果。**

## 套利机会分析

- **信息差**：低关注度但高质量？❌ 已是大众热门（13.5K stars）。但有信息差的是「**这套玩法可迁移到内容项目 / 社区驱动项目 / 个人品牌**」——大部分中文社区还没消化」零实现+真传播」模式，仍在用「功能列表「思路做开源
- **技术借鉴**：可借鉴的 5 件事 ① 文档即规范 ② Cheat count 计数器 ③ Bounty 慈善捐款 ④ 接力陷阱 ⑤ CI 反讽 —— 见「可复用的模式与技巧」节
- **生态位**：填补的空白 —— 中文开源世界还没有」作品型仓库」标杆案例；DreamBerd 改名 Gulf of Mexico 撞 Trump 更名令的事件，是中文创作者可对位学习的「借势改名「案例
- **趋势判断**：在增长吗？月 star 分布 41 / 92 / 9（2026-04 / 05 / 06）—— 2026-05 出现明显加速，配合改名事件持续放量。符合」程序员文化共鸣」长期趋势；后发优势在于「中文世界尚未出现对位作品「

## 风险与不足

- **零实现导致」不能 fork」** —— 想「用「这门语言的人会失望，潜在用户流失
- **License 自定条款**（非 OSI 标准）—— 企业法务无法直接采用
- **贡献者集中度 67%** —— Lu Wilson 三署名等同一人，剩 30 人贡献碎片化
- **最近 5 个月 0 commit** —— 长期低维护，被新作取代的风险上升
- **Issue 噪声大**（PR 135 / issue 353 堆积未处理）—— 治理公开表演的代价
- **改名破坏 SEO 链接** —— 旧名 `TodePond/GulfOfMexico` 的大量引用需要重定向
- **同行难复制** —— 这反而是」风险」：模仿者若无同等创作者人设，会变成「尴尬的拙劣模仿「

## 行动建议

- **如果你要用它**：不建议当生产工具用——它**不是**软件，是**作品**。如果你想」体验」 DreamBerd，建议去 `dreamberd.computer` 读 README 全文 + 8 分钟 YouTube 视频，理解其」作品「维度，而不是尝试找「实现「
- **如果你要学它**：
  - **架构 / 文档**：`README.md`（21.8KB 全文）= 范本级别的「文档即规范」案例
  - **运营 / 社区**：`docs/contributors/readme.md`（自动追加贡献者名）+ `#297 / #169 / #83 / #844` 4 个 Issue（剧场化治理范本）
  - **品牌 / 跨媒介**：`shapes.png` + `docs/wallpaper/` + `docs/not-vr/`（Vision Pro 启动页）+ `files/installation.mp3` + YouTube 发布会 = 跨媒介完整作品集
  - **反讽工程**：`action-which-doesnt-do-anything.yml` + `badges/coverage-109.svg` + 36 个荒诞 tag = 工程 KPI 反讽范本
- **如果你要 fork 它**：
  - **方向 1：中文本地化** —— 翻译 README + 增加「中文程序员痛点」专属规则（拼音关键字 / 方言注释 / 红包 import 关税）
  - **方向 2：垂直领域化** —— 选一个垂直场景（前端 / 游戏 / AI 提示词），做「垂直 esolang 作品」
  - **方向 3：跨域联动** —— 借」改名事件营销」模式，做「政治 / 文化事件对位「的季度改名
  - **方向 4：补完实现** —— 写一个真正可跑的 interpreter（`bounty/` 留了 £99 慈善捐款 + GitHub 上有第三方实现 `vivaansinghvi07/dreamberd-interpreter` 可参考）

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | 未收录 |
| Zread.ai | 未收录 |
| 关联论文 | 无（README 「too advanced for the current state of AI」 是反讽） |
| 在线 Demo | 无（README 自嘲「paste into ChatGPT」） |
| 真实入口 | https://dreamberd.computer（README = 规范本体） |
| 第三方实现 | https://github.com/vivaansinghvi07/dreamberd-interpreter |
| 作者主站 | https://todepond.com |
| 8 分钟发布会 | YouTube 搜索 「DreamBerd programming language」 |
