# Memos 网络分析笔记

## 仓库基本信息

- **名称**: usememos/memos
- **描述**: Open-source, self-hosted note-taking tool built for quick capture. Markdown-native, lightweight, and fully yours.
- **URL**: https://github.com/usememos/memos
- **Stars**: 58,100 | **Forks**: 4,205 | **Watchers**: 185
- **创建时间**: 2021-12-08
- **最近推送**: 2026-03-21
- **许可证**: MIT
- **主语言**: Go (1.2M LOC), TypeScript (958K)
- **磁盘占用**: 36MB
- **Topics**: react, go, sqlite, markdown, self-hosted, note-taking, memo, docker, microblog, social-network, notecard, foss, own-your-data
- **官网**: https://usememos.com
- **默认分支**: main
- **未归档/非Fork**

## 组织信息

- **Organization**: usememos (Memos)
- **公开仓库数**: 8
- **关注者**: 737
- **官网**: https://usememos.com
- **创建时间**: 2021-12-08

## 贡献者分布

| 贡献者 | 提交数 |
|--------|--------|
| boojack (Steven) | 2,459 (核心维护者/创始人) |
| johnnyjoygh (Johnny) | 523 |
| dependabot[bot] | 253 |
| athurg | 117 |
| Zeng1998 | 98 |
| hyoban | 45 |
| memoclaw | 35 |
| taosin | 30 |
| CorrectRoadH | 29 |
| lincolnthalles | 27 |

典型的"单核心创始人"模式，boojack 贡献了约 56% 的总提交。

## 热门 Issue

1. #3655 "Could we use MINIO as database?" (41 评论) - 用户请求对象存储支持
2. #2463 "迁移数据到MySQL失败" (37 评论) - 数据库迁移问题
3. #105 "feat: personal memos page" (13 评论)
4. #1900 "feat: add memo comment api" (5 评论)
5. #5111 "feat(web): add accessible ConfirmDialog" (4 评论)

## 最近版本

- v0.26.2 (2026-02-23)
- v0.26.1 (2026-02-08)
- v0.26.0 (2026-01-31)
- v0.25.3 (2025-11-25)
- v0.25.2 (2025-10-24)

发版节奏：约每月一个小版本。

## 竞品分析

### 直接竞品

1. **Joplin** - 跨平台笔记应用，端到端加密，支持插件
2. **SiYuan** - 块级引用、双向链接，面向知识工作者
3. **Notesnook** - 隐私优先，加密笔记
4. **Blinko** - 类似 Memos 的 AI 增强笔记工具
5. **Logseq** - 大纲式双向链接笔记

### 差异化定位

Memos 的核心差异：
- **极简部署**：单 Go 二进制 + ~20MB Docker 镜像，一条命令即可运行
- **Timeline-first UI**：类 Twitter 微博式界面，而非传统文件夹式
- **Markdown 原生**：原生 Markdown 支持，数据可移植
- **多数据库支持**：SQLite/MySQL/PostgreSQL
- **隐私优先**：完全自托管，零遥测
