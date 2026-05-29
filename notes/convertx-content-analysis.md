# ConvertX 内容分析笔记

## 技术栈
- 运行时: Bun (v1.2.2)
- Web 框架: Elysia (v1.4.22)
- 前端: TSX (服务端渲染) + TailwindCSS v4 + @kitajs/html
- 数据库: SQLite (bun:sqlite)
- 认证: JWT (@elysiajs/jwt), 7天过期
- 容器: Debian testing-slim, 多阶段构建
- 包管理: Bun
- 代码质量: ESLint + Prettier + Biome + Knip

## 架构设计
### 入口 (src/index.tsx)
- Elysia 应用，插件式路由注册
- 无限制请求体大小 (Number.MAX_SAFE_INTEGER)
- 定时清理过期任务 (AUTO_DELETE_EVERY_N_HOURS)
- 开发模式下动态生成 TailwindCSS

### 转换引擎 (src/converters/)
20 个转换器模块，通过统一的 properties 接口注册：
1. Inkscape - 矢量图像
2. libjxl - JPEG XL
3. resvg - SVG
4. Vips - 通用图像
5. libheif - HEIF
6. XeLaTeX - LaTeX
7. Calibre - 电子书
8. Dasel - 数据文件
9. LibreOffice - 文档
10. Pandoc - 文档
11. msgconvert - Outlook
12. dvisvgm - 矢量图像
13. ImageMagick - 图像
14. GraphicsMagick - 图像
15. Assimp - 3D 资产
16. FFmpeg - 音视频 (~472入~199出)
17. Potrace - 光栅转矢量
18. VTracer - 光栅转矢量
19. VCF - 联系人
20. Markitdown - 文档转 Markdown

### 转换器架构
- 每个转换器导出 properties (from/to 映射) 和 convert 函数
- main.ts 中注册所有转换器，按优先级匹配
- 支持并发转换控制 (MAX_CONVERT_PROCESS)
- 通过 execFile 调用外部命令行工具

### 数据库 (src/db/)
- 3 张表: users, jobs, file_names
- WAL 模式
- 版本迁移机制 (PRAGMA user_version)

### 页面路由 (src/pages/)
- root - 主页/上传界面
- upload - 文件上传
- convert - 转换触发
- results - 结果查看
- download - 文件下载
- history - 历史记录
- user - 用户管理(注册/登录/账户)
- healthcheck - 健康检查
- chooseConverter - 转换器选择
- deleteFile/deleteJob - 删除操作
- listConverters - 转换器列表

### Docker 配置
- 多阶段构建 (base → install → prerelease → release)
- 安装 20+ 个系统级转换工具
- 支持 amd64 和 arm64
- VTracer 通过二进制下载安装
- pipx 安装 markitdown

### 安全设计
- 文件名清理 (sanitize-filename)
- JWT 认证，httpOnly + secure cookie
- 支持密码保护和多账户
- HTTP_ALLOWED 标志控制安全 cookie
- ALLOW_UNAUTHENTICATED 模式
- 首次运行强制创建账户

### 环境变量
JWT_SECRET, ACCOUNT_REGISTRATION, HTTP_ALLOWED, ALLOW_UNAUTHENTICATED,
AUTO_DELETE_EVERY_N_HOURS, WEBROOT, FFMPEG_ARGS, FFMPEG_OUTPUT_ARGS,
HIDE_HISTORY, LANGUAGE, UNAUTHENTICATED_USER_SHARING, MAX_CONVERT_PROCESS

## 亮点
1. 极简代码量 (~7000 行代码) 支持 1000+ 格式转换
2. 通过统一接口聚合 20 个专业转换工具
3. 低耦合转换器设计，容易添加新转换器
4. 开发者体验好，bun dev 即可启动
5. 完整的 CI/CD 自动化

## 不足
1. 无 API 文档，缺少 REST API 供外部调用
2. 转换选项有限（如 FFmpeg 无法自定义编解码参数）
3. 无队列系统，大量并发转换可能压垮服务
4. 无文件大小限制（MAX_SAFE_INTEGER）
5. SQL 注入风险低但存在动态 SQL 拼接
6. 用户管理功能不完善（无管理员角色）
