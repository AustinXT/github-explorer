# RenderCV 元分析

## 代码统计

| 语言 | 文件数 | 代码行数 |
|------|--------|----------|
| Python | 153 | 16,704 |
| Typst | 44 | 39,912 |
| YAML | 54 | 4,221 |
| HTML | 7 | 3,371 |
| Markdown | 47 | (文档) |
| JSON | 1 | 9,575 (schema) |
| **总计** | **317** | **75,302** |

## Git 历史

- 总提交数: 1,917
- 首次提交: 2023-06-11 (Initial commit)
- 最新提交: 2026-03-21
- 项目年龄: ~2年9个月
- 版本演进: v1.x → v2.8 (当前)

## 提交频率分析

高频阶段 (2024年1-7月): 每月50-269次提交,v2.0重写期
稳定阶段 (2024年8月-2025年3月): 每月6-91次
近期活跃 (2025年12月-2026年3月): 每月37-70次,v2.6-v2.8连续发布

## 核心作者

| 作者 | 提交数 |
|------|--------|
| Sina Atalay | 1,672 (87.2%) |
| dependabot[bot] | 63 (3.3%) |
| Jeffrey Goldberg | 21 (1.1%) |
| Akibur Rahman | 31 (1.6%) |

## 架构演进

### v1.x 时代 (2023-2024初)
- 基于LaTeX排版引擎
- 单一主题支持

### v2.0 重写 (2024年初)
- 从LaTeX迁移到Typst排版引擎
- Pydantic v2 数据模型
- 多主题系统
- Jinja2模板引擎

### v2.5+ (2025-2026)
- 9个内置主题 (classic, harvard, sb2nov, moderncv, engineeringresumes, engineeringclassic, ink, opal, ember)
- 22种语言locale支持
- AI Skill (llms.txt) 集成
- ATS兼容性测试
- Pyodide/WASM支持
- Docker支持
- Watch模式

## 依赖链

核心依赖 (最小安装):
- Jinja2 (模板引擎)
- Pydantic + pydantic-extra-types (数据验证)
- ruamel.yaml (YAML解析)
- markdown (Markdown→HTML)
- phonenumbers (电话号码验证)

完整安装 (full):
- typer (CLI框架)
- typst (PDF排版引擎,Python绑定)
- watchdog (文件监控)
- rendercv-fonts (字体包)
- packaging (版本检查)

## 构建系统

- 构建后端: uv_build
- Python要求: >=3.12
- 包管理: uv + uv.lock
- 开发工具: just (任务运行器)

## 测试特色

- 常规单元测试
- 生成文件对比测试
- Pyodide/WASM安装测试 (浏览器运行验证)
- 离线wheel测试
- ATS兼容性自动化测试 (商业解析器)
