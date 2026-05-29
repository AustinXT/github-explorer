## 仓库基本数据
- Star / Fork / Watcher: 25,018 / 1,893 / 111
- 语言: TypeScript (99.2%), CSS (0.3%), JavaScript (0.3%), PLpgSQL (0.2%)
- License: Apache License 2.0（商业友好）
- 创建时间: 2024-06-25 | 最近推送: 2026-03-27
- 话题标签: react, typescript, tailwindcss, nextjs, low-code, design, frontend, ui, figma, cursor, ide, cursor-ai, design-to-code, editor, vibe-coding, drizzle, supabase, ai, vibecoding
- 已归档: 否 | 是Fork: 否
- 官网: https://onlook.com
- 文档: https://docs.onlook.com
- 磁盘占用: ~80 MB

## 作者画像
- 组织名: Onlook (onlook-dev) | Bio: "Somewhere between dev and design"
- 创始人: Daniel Farrell (CEO, 设计师背景, 10+ 年经验, 前 DIMO Growth 负责人, Bird 前 100 号员工) & Kiet Ho (@Kitenite, 工程师, 前 Amazon/ServiceNow SWE)
- 主力开发者 @Kitenite: 粉丝 482 | 公开仓库 66 | 账号创建于 2017 年（~9 年）| 现已创立新公司 Superset (superset.sh)，bio 标注 "prev cofounder onlook"
- YC 批次: W25 (Y Combinator Winter 2025) | 团队规模: 3 人 | 总部: San Francisco
- 此 repo 投入权重: **高**（onlook 是该组织唯一核心项目，25K+ stars，其余仓库均为辅助模板/fork）
- 作者类型: **YC 初创公司**（已获 YC 投资，正在招募 Founding Engineer，薪资 $130K-$200K + 1-4% 股权）
- 贡献集中度: **单人主导 + 小团队**
  - Kitenite: 1,035 commits（占绝对主导）
  - spartan-vutrannguyen: 102 commits
  - drfarrell (CEO Daniel Farrell): 88 commits
  - devin-ai-integration[bot]: 67 commits（使用 AI 辅助开发）
  - 其余贡献者均 < 35 commits，呈明显长尾分布
- 背景推断: 典型的 YC 初创双人组合——设计师 CEO + 工程师 CTO。Daniel Farrell 有增长运营背景（Bird/DIMO），Kiet Ho 有大厂工程经验（Amazon/ServiceNow）。值得注意的是 Kiet 的 GitHub bio 已标注 "prev cofounder"，当前在 Superset 工作，这可能意味着核心技术创始人已转移重心。

## 社区热度
- 热度级别: **大众热门**（25,018 stars）
- 增长模式: **多波爆发型**
  - 2024-07 创建，早期缓慢积累
  - 2025-01 下旬达到 ~5,000 stars（首次爆发，可能与 HN #1 和 YC Demo Day 相关）
  - 2025-06 初快速从 ~10,000 飙升至 ~15,000（5 天内增长 5,000 stars，第二次大爆发，GitHub Trending #1）
  - 2025-07 初达到 ~20,000
  - 2026-01 底~02 初达到 ~24,500
  - 2026-04 初达到 25,018（近期增长明显放缓）
- 近期趋势: 2026 年以来增长速率下降，从高峰期每月数千 stars 降至每月数百。最近 100 个 star 在 2026-04-02 至 2026-04-03 间获得，日均 ~50 stars。
- 套利判断: **不适用**。项目已充分曝光（HN #1、GitHub Trending #1、YC 背书），不存在信息差。但需关注：核心技术创始人 @Kitenite 已离开（bio 标注 prev cofounder），最近推送停在 2026-03-27，这些信号值得在后续阶段深入验证。

## 生态网络
- 上游依赖/技术栈:
  - 前端: Next.js 16.0.7 + React 19.2.0 + TailwindCSS
  - 后端: tRPC + Supabase (Auth/DB/Storage) + Drizzle ORM
  - AI: AI SDK (Vercel) + OpenRouter (LLM 路由) + Morph Fast Apply + Relace (快速应用模型)
  - 沙箱: CodeSandbox SDK（云端运行用户项目）
  - 部署: Freestyle (托管服务)
  - 运行时: Bun 1.3.1（monorepo 管理 + 运行时 + 打包）+ Docker
  - 编辑器: CodeMirror + xterm (终端) + Penpal (iframe 通信)
  - 状态管理: MobX
- 同类项目:
  - DouyinFE/semi-design (9,805 stars) — 抖音前端团队的设计系统，含 Design-to-Code 功能
  - Lona/Lona (7,558 stars) — 跨平台设计系统定义工具（已归档）

## 官方文档洞察
- 价值主张: 「The fastest way for anyone to build, deploy, and iterate on websites and web apps」——面向设计师的 Cursor，代码即设计的真实来源（source of truth）
- 目标用户:
  1. 想要直接编辑代码但不懂代码的设计师
  2. 希望统一设计-开发工作流的团队
  3. 构建 Next.js + TailwindCSS 网站的快速原型需求
- 差异化叙事: 「Developers have historically been second-rate citizens in the design process」——传统设计工具产出的是「设计稿」而非真正的代码，Onlook 让设计变更直接反映在 .tsx/.css 文件中，保留 Git 工作流，避免厂商锁定
- 设计哲学:
  1. Code as source of truth——所有视觉编辑都直接修改源代码
  2. 双向实时同步——视觉编辑器 <-> 代码编辑器
  3. 开源透明——给开发者对工具的完全控制权
  4. AI-first——AI 读取整个仓库上下文，理解命名规范和设计 token
- 技术路线图（来自 README 清单）:
  - 待完成: Figma 导入、GitHub 仓库导入/PR、拖拽组件面板、评论协作、MCP 集成、非 Next.js/非 Tailwind 项目支持、图片作为 AI 参考
  - 已完成: 分支实验、检查点恢复、CLI 命令、应用市场、自定义域名、实时协作编辑
- 架构要点: Web 容器架构——代码加载到 Web 容器 → 容器运行并 serve → 编辑器通过 iFrame 显示预览 → 代码注入 instrumentation 实现元素到代码的映射 → 编辑时先改 iFrame DOM 再改源码。理论上可扩展到任何声明式渲染 DOM 的语言/框架。
- 外部深度视角:
  1. [BrightCoding 深度评测](https://www.blog.brightcoding.dev/2025/09/05/onlook-the-open-source-cursor-for-designers-that-lets-you-visually-build-style-and-edit-react-apps-with-ai/) — 指出 Onlook 占据独特象限：唯一同时具备「真实 React 代码输出 + 开源 + 实时视觉-代码双向同步」的工具。诚实承认局限：Alpha 成熟度不足、仅限桌面、框架锁定 Next.js+Tailwind、无离线模式。
  2. [LogRocket 技术评测](https://blog.logrocket.com/onlook-react-visual-editor/) — 指出初始视觉编辑会将所有代码生成到单个 page.tsx 中，需手动重构为组件架构；对复杂状态管理（Redux/Zustand）的支持边界不明确；更准确的定位是「React 的视觉 IDE 增强」而非设计协作工具的替代品。

## 竞品清单
| 竞品 | Stars | 定位 | 与 Onlook 对比 |
|------|-------|------|----------------|
| stackblitz/bolt.new | 16,307 | AI 全栈 Web 应用生成器 | Bolt 侧重 prompt-to-app 的一次性生成，Onlook 侧重持续可视化编辑；Bolt 不保留本地代码控制 |
| BuilderIO/builder | 8,655 | 可视化开发 + Headless CMS | Builder 支持多框架（React/Vue/Svelte/Qwik），功能更成熟，但偏向 CMS 场景，非纯设计工具 |
| webstudio-is/webstudio | 8,405 | 开源 Webflow 替代品 | Webstudio 更接近传统 Webflow 模型（拖拽建站），不深度集成 React 组件逻辑 |
| plasmicapp/plasmic | 6,702 | 可视化构建器 + 代码集成 | Plasmic 支持 React/Next.js/Gatsby，组件集成能力强，但非完全开源（有商业版） |
| appsmithorg/appsmith | 39,539 | 内部工具/管理面板构建器 | 定位不同——Appsmith 面向内部工具和管理后台，非面向消费者的 Web 设计 |
| V0 (Vercel) | 非开源 | AI 代码生成器 | V0 是 prompt-to-code 单次生成，无持续可视化编辑能力，无开源 |
| Lovable | 非开源 | AI 全栈应用构建器 | 与 Bolt 类似定位，但 Onlook 的差异在于代码可控性和开源 |

## 关键 Issue 信号
1. [#2229 Add alternate sandbox provider](https://github.com/onlook-dev/onlook/issues/2229) — 揭示了对 CodeSandbox SDK 的单一依赖风险，社区要求支持 E2B 等替代沙箱方案，反映架构灵活性需求
2. [#2242 Need help setting up Onlook project locally](https://github.com/onlook-dev/onlook/issues/2242) — 揭示了本地开发环境搭建的复杂度问题，对贡献者友好度有改善空间
3. [#2763 (PR) feat: add branching](https://github.com/onlook-dev/onlook/pull/2763) — 84 条评论的大型 PR，揭示了「分支实验」功能的架构复杂性，这是 Onlook 的核心差异化能力之一
4. [#2924 (PR) feat: integrate sync eng](https://github.com/onlook-dev/onlook/pull/2924) — 34 条评论，揭示了代码同步引擎的重大架构整合，是双向同步能力的关键基础设施
5. [#2966 (PR) Fix all cyclical dependencies](https://github.com/onlook-dev/onlook/pull/2966) — 揭示了 monorepo 中存在循环依赖和类型检查问题，技术债务需要系统性清理

## 知识入口
- DeepWiki: https://deepwiki.com/onlook-dev/onlook — **已收录**，包含完整项目概述、技术架构、核心功能文档
- Zread.ai: https://zread.ai/onlook-dev/onlook — **无法访问**（403）
- 关联论文: **无**（arxiv.org 无相关论文）
- 在线 Demo: https://onlook.com — 官网提供 hosted app，Free 计划允许 5 个项目 + 每天 5 条 AI 消息 / 每月 50 条
- Product Hunt: https://www.producthunt.com/products/onlook-2
- Y Combinator: https://www.ycombinator.com/companies/onlook
- YouTube Demo: https://youtu.be/RSX_3EaO5eU

## 项目展示素材

1. **Web 预览主图** (产品界面全貌)
![web-preview](https://raw.githubusercontent.com/onlook-dev/onlook/main/assets/web-preview.png)

2. **产品使用示例** (AI 聊天 + 可视化编辑)
![Onlook-GitHub-Example](https://github.com/user-attachments/assets/642de37a-72cc-4056-8eb7-8eb42714cdc4)

3. **架构图** (系统工作原理)
![architecture](https://raw.githubusercontent.com/onlook-dev/onlook/main/assets/architecture.png)

## 快速判断
- 是否值得深入: **有条件的是**。产品定位独特（可视化 React 编辑器 + AI + 开源），YC 背书，25K stars 证明市场需求。但需在后续阶段重点验证：(1) 核心技术创始人 @Kitenite 已离开对项目的影响；(2) 最近推送停在 3 月底，团队是否仍在积极开发；(3) 从桌面版到 Web 版的迁移是否顺利完成。
- 初步定位: 「设计师的 Cursor」——面向设计师和前端团队的 AI 可视化代码编辑器，专注 Next.js + TailwindCSS 生态，处于「AI 代码生成」和「可视化设计工具」的交叉地带
- 作者可信度: **中高**。YC W25 背书，创始人背景扎实（大厂工程 + 增长运营），但核心工程创始人已转向新项目是重大风险信号。当前正在招聘 Founding Engineer 填补空缺。
- 竞品格局: 赛道拥挤但 Onlook 有差异化——唯一同时满足「开源 + 真实 React 代码输出 + 实时双向同步 + AI 辅助」的工具。直接竞争者多为商业化产品（V0/Lovable/Bolt.new），开源竞品（Builder/Plasmic/Webstudio）定位偏 CMS 或传统建站。核心风险在于 Next.js+Tailwind 的框架锁定限制了受众面。
