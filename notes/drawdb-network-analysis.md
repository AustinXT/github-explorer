## 仓库基本数据
- Star / Fork / Watcher: 37,022 / 2,974 / 132
- 语言: JavaScript (99.0%), CSS (0.8%), HTML (0.1%), Dockerfile (0.0%)
- License: AGPL-3.0（GNU Affero General Public License v3.0）— 强 copyleft，商业使用需开源衍生代码
- 创建时间: 2023-07-16 | 最近推送: 2026-04-04
- 话题标签: database-schema, editor, mariadb, postgresql, sql, sql-server, sqlite, svg, react, indexeddb, tailwindcss, javascript, diagram-editor, erd, erdiagram, oracle-database, oracle-db
- 已归档: 否 | 是Fork: 否

## 作者画像
- 组织/ID: drawdb-io（GitHub Organization）| 公司: 无 | 位置: 未知
- 粉丝: 461 | 公开仓库: 5 | 账号创建: 2023-07-16（约 2.7 年）
- 核心创始人: **1ilit** — 个人开发者，bio 为「i make stuff | founder of @drawdb-io」，就职于 @krispai，GitHub 账号创建于 2021-12，粉丝 163，公开仓库 9 个
  - 个人仓库包括 oracle-sql-parser（PEG.js）、Desktop-Cat（Python, 81 star）、advent-of-code（C++）等，技术栈广泛
- 此 repo 投入权重: **极高**（drawdb 是 drawdb-io 组织下唯一核心项目，37k star 远超其余所有仓库）
- 作者类型: 独立开发者（个人创建组织托管项目，目前就职于 KrispAI）
- 贡献集中度: **单人主导**（1ilit 贡献 816 次提交，占总提交的 81.0%；Top 3 贡献者占 86.5%）
- 背景推断: 1ilit 是一位全栈开发者，对数据库工具和解析器有深入研究（oracle-sql-parser），在 KrispAI 工作的同时独立维护 drawDB。项目从个人 side-project 成长为 37k star 的热门开源工具，属于「独立开发者的意外爆款」

## 社区热度
- 热度级别: **大众热门**（37k+ star，远超同类工具）
- 增长模式: **爆发型 + 稳步增长**
  - 2024-04-06 首次出现大量 star（HN Show HN 爆发期），单日密集增长
  - page 1 → page 100（~10,000 star）: 2024-04-06 ~ 2024-05-10（约 1 个月内首轮爆发）
  - page 200（~20,000 star）: 2024-10-23（6 个月后稳步达到）
  - page 300（~30,000 star）: 2025-06-04（再过 7 个月）
  - page 370（~37,000 star）: 2026-03-22（又过 9 个月）
  - 增速从爆发期后逐渐放缓，但保持长尾稳定增长
- 近期趋势: 2026 年仍有持续 star 增长，项目最近推送在 2026-04-04，Discord 社区 1000+ 人，支持 37 种语言
- 套利判断: 无明显 star 刷量痕迹，增长曲线与 HN 曝光事件吻合，社区互动真实

## 生态网络
- 上游依赖: React、Dexie.js（IndexedDB）、TailwindCSS、SVG 渲染
- 同类项目:
  - **chartdb/chartdb** — 21.7k star，AI 驱动的 DDL 导出，支持 NoSQL
  - **dineug/erd-editor** — 1.6k star，ER 图编辑器
  - **azimutt/azimutt** — 1.9k star，企业级数据库探索工具
  - **liam-erd** — 4k star，零配置 ERD 生成（Rails/Prisma）
- drawdb-io 组织内部生态:
  - **drawdb-server** — 160 star，后端服务（支持分享功能）
  - **docs** — 3 star，文档站
  - **gh-analytics** — 2 star，GitHub 分析工具

## 官方文档洞察
- 官网: https://drawdb.app/（SPA 应用，JS 渲染，WebFetch 无法完整抓取）
- 核心定位: 「Free, simple, and intuitive online database diagram editor and SQL generator」
- 关键卖点（来自外部评测）:
  - **零门槛**: 无需注册账号、无需安装、完全免费
  - **隐私优先**: 所有处理在客户端完成，数据库 schema 不离开浏览器
  - **多数据库支持**: MySQL、PostgreSQL、SQLite、SQL Server、MariaDB、Oracle
  - **双向操作**: 可视化设计导出 SQL，也可导入 SQL 反向生成 ER 图
  - **导出格式**: SQL、PNG、JSON
  - **可自托管**: Docker 部署支持
- 局限性: 大型 schema（100+ 表）性能下降；基础版无实时协作（需部署 server）

## 竞品清单
| 项目 | Star | 定位 | 差异化 |
|------|------|------|--------|
| **drawDB** | 37k | 浏览器端免费 ERD 编辑器 | 零账号、隐私优先、最直观 |
| **chartdb/chartdb** | 21.7k | AI 驱动的 DB schema 可视化 | AI DDL 导出、支持 NoSQL |
| **Azimutt** | 1.9k | 企业级数据库探索 | 高级搜索、关系图谱、适合大型项目 |
| **Liam ERD** | 4k | 零配置 ERD 生成器 | 自动从 Rails/Prisma schema 生成 |
| **dineug/erd-editor** | 1.6k | 轻量 ER 图编辑器 | VS Code / IntelliJ 插件生态 |
| **dbdiagram.io**（商业） | — | 在线 ERD 工具 | DBML 语法、团队协作（付费） |

## 关键 Issue 信号
- **#115** (35 评论, closed): 多语言翻译支持 — 已实现 37 种语言，社区参与度高
- **#148** (16 评论, closed): 触控屏支持与坐标管理重写 — 体现移动端适配需求
- **#561** (15 评论, open): URL 构造失败 bug — 活跃讨论中的技术问题
- **#188** (11 评论, open): 可调整表格大小 — 用户呼声较高的 UX 改进
- **#58** (9 评论, open): 实时协作功能 — 长期需求，尚未实现
- **#87** (8 评论, open): ORM 导出支持 — 向开发者工具链更深层集成
- **#334** (4 评论, open): Crow's Foot / IDEF1X 表示法 — ERD 专业功能扩展
- **#17** (7 评论, open): 从已有数据库自动生成 ER 图 — 逆向工程需求

**信号解读**: 社区活跃度中等偏高，需求方向集中在「协作」「更多数据库方言」「专业 ERD 表示法」和「开发工具链集成」。核心维护者（1ilit）持续响应。

## 知识入口
- DeepWiki: [https://deepwiki.com/drawdb-io/drawdb](https://deepwiki.com/drawdb-io/drawdb) — 已收录，包含完整架构文档、状态管理、数据模型等技术参考
- Zread.ai: 未收录（403 拒绝访问）
- 关联论文: 无
- 在线 Demo: [https://drawdb.app/](https://drawdb.app/)（即为产品本身，浏览器直接使用）
- Discord 社区: [https://discord.gg/BrjZgNrmR6](https://discord.gg/BrjZgNrmR6)（1000+ 成员）
- X/Twitter: [@drawDB_](https://x.com/drawDB_)

## 项目展示素材
- 主截图: `https://raw.githubusercontent.com/drawdb-io/drawdb/main/drawdb.png` — 编辑器界面全貌截图
- Logo: `https://raw.githubusercontent.com/drawdb-io/drawdb/main/src/assets/icon-dark.png` — 深色版 Logo
- 赞助商 Banner: Warp（AI 终端）赞助图片（非项目素材，跳过）

## 快速判断
- 是否值得深入: **是** — 37k star 的成熟项目，独立开发者的标杆案例，技术架构（纯前端 + IndexedDB）有分析价值
- 初步定位: **大众热门** — 数据库 ERD 编辑器赛道中 star 数第一，远超竞品
- 作者可信度: **高** — 1ilit 持续维护近 3 年，提交稳定，从 side-project 成长为行业标杆，有 Warp 赞助背书
- 竞品格局: **细分市场偏蓝海** — 虽有 chartdb 等竞品，但「零账号 + 纯浏览器端 + 开源免费」的定位仍具独特性，各竞品在不同子场景（AI 辅助、企业级、框架集成）差异化明显
