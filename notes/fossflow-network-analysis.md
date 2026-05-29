# stan-smith/FossFLOW 网络分析

## 仓库基本数据

| 指标 | 数据 |
|------|------|
| 名称 | [FossFLOW](https://github.com/stan-smith/FossFLOW) |
| 描述 | Make beautiful isometric infrastructure diagrams |
| Stars | 19,174 |
| Forks | 1,257 |
| Watchers | 93 |
| Issues（总计） | 8 |
| Pull Requests（总计） | 6 |
| 主语言 | TypeScript（81.1%），辅以 Python、Shell、CSS、JS、HTML、MDX |
| 许可证 | MIT License |
| 创建时间 | 2025-06-30 |
| 最后推送 | 2026-03-18 |
| 最后更新 | 2026-03-21 |
| 磁盘占用 | 3.6 MB |
| 默认分支 | master |
| 是否归档 | 否 |
| 是否 Fork | 否 |
| 主页 | 无（使用 GitHub Pages: https://stan-smith.github.io/FossFLOW/） |
| Topics | devops, infra, infrastructure |
| 最新版本 | v1.10.8（2026-03-01） |

## 作者画像

| 指标 | 数据 |
|------|------|
| 用户名 | [stan-smith](https://github.com/stan-smith) |
| 姓名 | Stan |
| 个人简介 | man page addict |
| 博客 | x0z.co |
| 公开仓库 | 30 |
| Followers | 258 |
| Following | 5 |
| 注册时间 | 2018-03-22 |

**作者活跃仓库（Top 5）：**

| 仓库 | 语言 | Stars | 最近推送 | Fork? |
|------|------|-------|----------|-------|
| FossFLOW | TypeScript | 19,174 | 2026-03-18 | 否 |
| noq | - | 0 | 2026-03-17 | 是 |
| SlingShot | Rust | 49 | 2026-03-08 | 否 |
| sipeed_wiki | - | 0 | 2026-03-04 | 是 |
| mppdarkgst | Rust | 0 | 2026-03-03 | 否 |

**作者特征：**
- 个人独立开发者，无公司关联，全职工作之余维护开源项目
- 技术栈跨 TypeScript（FossFLOW）和 Rust（SlingShot、dart 等），偏好系统级与前端两端
- FossFLOW 是其唯一高星项目，其余仓库星标均在 50 以下
- 活跃度较高，2026 年 3 月仍持续推送
- README 中明确表达了个人维护的时间压力，附带捐赠链接（Ko-fi、Buy Me a Coffee）

**贡献者分布：**

| 贡献者 | 提交数 | 备注 |
|--------|--------|------|
| markmanx | 494 | Isoflow 原作者，核心库贡献最多 |
| stan-smith | 136 | 仓库所有者，应用层主力 |
| semantic-release-bot | 46 | 自动发布 |
| dependabot[bot] | 22 | 依赖更新 |
| abhinav-1305 | 22 | 社区贡献者 |
| 其余 22 人 | 1-9 | 零星贡献 |

**关键发现：** markmanx（Isoflow 原作者）的提交数（494）远超仓库所有者 stan-smith（136），说明 FossFLOW 是基于 Isoflow 的封装层，核心图表引擎代码来自 markmanx。stan-smith 的角色更偏向「应用集成者」而非「核心引擎开发者」。

## 社区热度

**Star 增长趋势（按月）：**

| 月份 | 新增 Stars | 说明 |
|------|-----------|------|
| 2025-06 | 5 | 创建月（仅最后 1 天） |
| 2025-07 | 6,643 | 爆发期，可能登上 GitHub Trending |
| 2025-08 | 3,577 | 持续高热 |
| 2025-09 | 1,264 | 回落 |
| 2025-10 | 959 | 稳定期 |
| 2025-11 | 921 | 稳定期 |
| 2025-12 | 2,053 | 二次爆发 |
| 2026-01 | 1,586 | 较高 |
| 2026-02 | 1,851 | 再次上升 |
| 2026-03 | 315 | 月中数据（截至 3/14） |

**热度特征：**
- 创建后第一个月即获 6,643 星，典型的 Trending 爆发模式
- 2025-12 和 2026-02 出现两次显著回弹，说明持续获得媒体/社区推荐
- 日均增速约 72 星/天（总 19,174 星 / 约 265 天）
- Fork 比率 6.6%（1,257/19,174），属于中等水平，表明用户以直接使用为主，少量二次开发
- Watchers 仅 93，相对 Star 数偏低，说明深度关注者比例不高

## 生态网络

**上游依赖：**
- **[Isoflow](https://github.com/markmanx/isoflow)**：核心等轴测图表渲染引擎，已被 fork 并以 `fossflow` 名称发布到 NPM
- **React**：前端框架
- **Paper.js**：Canvas 图形渲染
- **i18next / react-i18next**：国际化
- **RSBuild**：应用构建工具
- **Express.js**：可选后端存储服务

**下游生态：**
- 已有 1,257 个 Fork，存在被二次封装的可能
- Docker Hub 镜像：`stnsmith/fossflow`
- GitHub Pages 在线演示版本
- SourceForge 上有镜像分发

**集成方式：**
- PWA 独立运行（浏览器内，完全离线）
- Docker Compose 一键部署（含持久化存储）
- 可选 HTTP Basic Auth 保护

## 官方文档洞察

**文档资源：**
- README 提供 10 种语言翻译版本（中、英、西、葡、法、印地、孟加拉、俄、印尼、德）
- [FOSSFLOW_ENCYCLOPEDIA.md](https://github.com/stan-smith/FossFLOW/blob/master/FOSSFLOW_ENCYCLOPEDIA.md)：代码库全面指南
- [CONTRIBUTING.md](https://github.com/stan-smith/FossFLOW/blob/master/CONTRIBUTING.md)：贡献指南
- Docker 部署文档完善（Compose、环境变量、持久化、认证均有说明）

**文档质量：**
- README 结构清晰：在线试用 → Docker 部署 → 本地开发 → 使用方法 → Monorepo 结构
- 有明确的 E2E 测试（Selenium）
- 使用 semantic-release 自动化版本发布
- 缺乏 API 文档和架构设计文档（依赖 DeepWiki 补充）

## 竞品清单

| 竞品 | 类型 | 特点 | 对比 FossFLOW |
|------|------|------|--------------|
| **[Isoflow](https://isoflow.io/)** | 开源/商业 | FossFLOW 的上游库，提供等轴测图表核心能力 | FossFLOW 是其 PWA 封装，增加了导出/导入、离线、Docker 部署等功能 |
| **[Cloudcraft](https://www.cloudcraft.co/)** | 商业 | AWS/Azure 3D 架构图，自动从云账号导入 | 商业产品，功能更强但不开源，有厂商锁定 |
| **[draw.io](https://draw.io)** | 开源 | 通用图表工具，支持多种图表类型 | 通用性强但缺乏等轴测/3D 专注度 |
| **[Excalidraw](https://excalidraw.com/)** | 开源 | 手绘风格白板，协作能力强 | 风格完全不同，偏手绘而非等轴测 |
| **[D2](https://d2lang.com/)** | 开源 | Diagram as Code，声明式图表 | 代码生成图表，与可视化拖拽是两种路径 |
| **[PlantUML](https://plantuml.com/)** | 开源 | 文本描述生成 UML 图 | 专注 UML，非等轴测基础设施图 |
| **[Terrastruct](https://terrastruct.com/)** | 商业 | 软件架构可视化 | 功能更全但商业产品 |

**竞争定位：** FossFLOW 在「开源 + 等轴测 + 基础设施图表」这个细分赛道几乎没有直接竞品，是 Isoflow 之上唯一成熟的 PWA 封装方案。

## 关键 Issue 信号

| # | 标题 | 评论数 | 状态 | 标签 |
|---|------|--------|------|------|
| [#213](https://github.com/stan-smith/FossFLOW/issues/213) | Why are my fans spinning at max speed? | 29 | Open | bug, enhancement, Priority 2 |
| [#135](https://github.com/stan-smith/FossFLOW/issues/135) | Unable to load diagrams from Server Storage | 29 | Closed | bug, Priority 1 |
| [#136](https://github.com/stan-smith/FossFLOW/issues/136) | "Add node" popup has a huge offset | 18 | Closed | bug, Priority 3 |
| [#121](https://github.com/stan-smith/FossFLOW/issues/121) | Feature: Display page on path | 14 | Closed | Priority 3, released |
| [#150](https://github.com/stan-smith/FossFLOW/issues/150) | New Icons | 12 | Open | enhancement |

**Issue 信号解读：**
- #213（风扇全速转）暗示存在性能问题，可能与 Canvas 渲染或 Paper.js 计算有关，29 条评论说明影响面较广
- #135（服务端存储加载失败）是核心功能缺陷，已修复
- #150（新图标请求）反映用户对图标库丰富度的需求
- Issue 总量极少（仅 8 个），可能是项目早期阶段或社区参与度有限
- PR 仅 6 个，社区代码贡献活跃度一般

**值得关注的 PR：**
- [#239](https://github.com/stan-smith/FossFLOW/pull/239)：AI 从 Prompt 生成图表（已关闭）
- [#240](https://github.com/stan-smith/FossFLOW/pull/240)：无图片 JSON 导出
- [#214](https://github.com/stan-smith/FossFLOW/pull/214)：Docker HTTP Basic Auth 支持
- [#98](https://github.com/stan-smith/FossFLOW/pull/98)：修复导出图片对话框的无限重渲染

## 知识入口

| 平台 | 状态 | 链接 |
|------|------|------|
| **DeepWiki** | 已收录 | [stan-smith/FossFLOW](https://deepwiki.com/stan-smith/FossFLOW) |
| **Zread.ai** | 未收录 | - |
| **AlternativeTo** | 已收录 | [FossFLOW](https://alternativeto.net/software/fossflow/) |
| **SourceForge** | 已收录（镜像） | [FossFLOW](https://sourceforge.net/projects/fossflow.mirror/) |
| **OSTechNix** | 评测文章 | [文章链接](https://ostechnix.com/fossflow-create-isometric-diagrams/) |
| **LinuxToday** | 推荐文章 | [文章链接](https://www.linuxtoday.com/blog/fossflow-create-stunning-3d-style-isometric-infrastructure-diagrams-locally-and-freely/) |
| **OSCHINA** | 已收录 | [FossFLOW](https://www.oschina.net/p/fossflow) |
| **TypeVar** | 深度文章 | [文章链接](https://typevar.dev/articles/stan-smith/FossFLOW) |
| **AIToolly** | 已收录 | [文章链接](https://aitoolly.com/ai-news/article/2026-02-23-fossflow-a-new-isometric-drawing-tool-for-beautiful-infrastructure-diagrams-hits-github-trending) |
| **Hostinger** | Docker 部署指南 | [VPS 指南](https://www.hostinger.com/vps/docker/fossflow) |
| **TrendShift** | 已收录 | 在 README 中展示徽章 |

## 项目展示素材

**在线演示：** https://stan-smith.github.io/FossFLOW/

**Docker 快速体验：**
```bash
docker compose up
# 或
docker run -p 80:80 -v $(pwd)/diagrams:/data/diagrams stnsmith/fossflow:latest
```

**README 亮点：**
- 包含项目截图（等轴测基础设施图示例）
- TrendShift 排名徽章
- 10 种语言翻译
- Ko-fi / Buy Me a Coffee 捐赠链接
- 关联项目推广（SlingShot - QUIC 视频流）

**核心卖点（可用于展示）：**
1. 完全开源（MIT）的等轴测基础设施图表工具
2. PWA 离线支持，隐私优先（数据不离开浏览器）
3. Docker 一键部署，可选服务端持久化存储
4. 基于 Isoflow 引擎，3D 等轴测视觉效果出众
5. 自动保存（每 5 秒）+ JSON 导入/导出

## 快速判断

**一句话定位：** 基于 Isoflow 引擎的开源等轴测基础设施图表 PWA，在细分赛道无直接竞品，9 个月获 19K 星。

**优势：**
- 填补了「开源等轴测基础设施图表」这一细分空白
- PWA + Docker 双模式部署，隐私友好
- MIT 许可证，商业使用无障碍
- 持续活跃开发，版本迭代频繁（v1.10.x）
- 多语言 README，国际化视野

**风险：**
- 核心引擎依赖 markmanx/Isoflow，仓库所有者并非核心引擎作者，存在上游供应链风险
- 社区参与度偏低（仅 8 个 Issue、6 个 PR、27 个贡献者）
- 个人独立维护，维护者明确表示时间有限
- 存在性能问题（#213 风扇全速转），Canvas 渲染开销可能较大
- 功能相对单一，仅支持等轴测图表，扩展性有限

**适合关注的场景：**
- DevOps/SRE 团队需要制作美观的基础设施架构图
- 技术博客/文档需要专业等轴测图示
- 需要自托管、隐私优先的图表工具
- 寻找 Cloudcraft 的免费开源替代品

Sources:
- [DeepWiki - FossFLOW](https://deepwiki.com/stan-smith/FossFLOW)
- [AlternativeTo - FossFLOW](https://alternativeto.net/software/fossflow/)
- [OSTechNix 评测](https://ostechnix.com/fossflow-create-isometric-diagrams/)
- [LinuxToday 推荐](https://www.linuxtoday.com/blog/fossflow-create-stunning-3d-style-isometric-infrastructure-diagrams-locally-and-freely/)
- [TypeVar 深度文章](https://typevar.dev/articles/stan-smith/FossFLOW)
- [AIToolly 报道](https://aitoolly.com/ai-news/article/2026-02-23-fossflow-a-new-isometric-drawing-tool-for-beautiful-infrastructure-diagrams-hits-github-trending)
- [OSCHINA](https://www.oschina.net/p/fossflow)
- [SourceForge 镜像](https://sourceforge.net/projects/fossflow.mirror/)
- [Hostinger Docker 指南](https://www.hostinger.com/vps/docker/fossflow)
