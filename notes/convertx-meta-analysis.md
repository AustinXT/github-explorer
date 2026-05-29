# ConvertX 元分析笔记

## 代码统计
- 总行数: 8,254 (代码 6,987 / 注释 404 / 空行 863)
- TypeScript: 50 文件, 4,993 行
- TSX: 18 文件, 2,124 行
- JavaScript: 4 文件, 306 行
- CSS: 2 文件, 79 行
- Dockerfile: 1 文件, 112 行
- 总提交数: 845

## 时间线
- 首次提交: 2024-04-06 Initial commit (via bun create)
- 最新提交: 2026-03-04 chore(deps): update docker/login-action action to v4
- 项目年龄: ~24 个月

## 月度提交分布
- 2024-04~07: 爆发式开发 (4→95→85→71)
- 2024-08~12: 稳定期 (54→36→13)
- 2025-01~08: 二次增长 (25→48)
- 2025-09~至今: 维护期 (11→2)

## 版本发布
- 最新版本: v0.17.0 (2026-01-13)
- 总版本数: 17+ (v0.1.0 ~ v0.17.0)
- 发布节奏: 约每月 1 次

## 最频繁修改的文件
1. package.json (185)
2. bun.lockb (123)
3. Dockerfile (95)
4. README.md (87)
5. src/index.tsx (85)
6. src/converters/main.ts (47)
7. .github/workflows/docker-publish.yml (36)
8. CHANGELOG.md (34)
9. src/converters/ffmpeg.ts (29)

## 最频繁修改的目录
1. src/converters (282) - 核心转换逻辑
2. tests/converters (142) - 测试
3. src/pages (106) - 页面路由
4. src/index.tsx (85) - 应用入口
5. .github/workflows (83) - CI/CD

## 标签
v0.17.0, v0.16.1, v0.16.0, v0.15.1, v0.15.0, v0.14.1, v0.14.0, v0.13.0, v0.12.1, v0.12.0

## 开发模式
- 使用 conventional commits
- renovate[bot] + dependabot[bot] 自动依赖更新
- 7 个 GitHub Actions workflows
- 19 个转换器测试文件
