# RenderCV 内容分析

## 架构概览

```
用户 YAML → Pydantic验证 → Jinja2模板 → Typst源码 → PDF/PNG
                                       → Markdown → HTML
```

三层架构:
1. **Schema层** (`schema/`): 数据建模和验证
2. **Renderer层** (`renderer/`): 模板渲染和编译
3. **CLI层** (`cli/`): 命令行界面

## 核心设计决策

### 1. YAML作为简历的唯一数据源

简历内容定义为结构化YAML,而非LaTeX/Word等混合格式。这使得:
- 版本控制 (git diff有意义)
- 内容与设计完全分离
- 多格式输出 (PDF/HTML/MD/PNG)
- AI Agent可直接读写

### 2. 从LaTeX到Typst的迁移

v2.0的关键决策:放弃LaTeX,选择Typst。原因:
- Typst编译速度极快 (毫秒级)
- Typst有Python绑定 (typst-py),无需外部安装
- Typst语法更现代,模板更易维护
- 消除了TeX发行版安装的痛点

### 3. Pydantic驱动的主题变体生成

`variant_pydantic_model_generator.py` 是最精妙的设计:
- 一个 `BuiltInDesign` 基类定义所有设计选项
- 每个主题是一个YAML文件定义默认值差异
- 运行时动态生成 Pydantic 模型变体
- JSON Schema自动反映每个主题的默认值
- IDE自动补全精确到主题级别

### 4. Jinja2模板的双层覆盖机制

模板查找顺序:
1. 用户输入文件同目录下的 `{theme_name}/` 文件夹
2. 内置的 `templates/{file_type}/` 文件夹

这允许用户覆盖任何模板而不修改源码。

### 5. 捆绑Typst包的离线编译

`pdf_png.py` 中的 `get_package_path()`:
- 将rendercv和fontawesome的Typst包打包在Python包内
- 运行时复制到临时目录,模拟Typst包管理器的目录结构
- 无需联网下载Typst包即可编译
- `@functools.lru_cache` 确保只初始化一次

### 6. 九种条目类型的类型推断

用户不需要声明条目类型,系统根据字段自动推断:
- ExperienceEntry: company + position
- EducationEntry: institution + area + degree
- PublicationEntry: title + authors + journal
- NormalEntry: 有highlights但无特定字段
- OneLineEntry: label + details
- BulletEntry: 纯文本列表
- NumberedEntry / ReversedNumberedEntry
- TextEntry: 纯文本段落

### 7. AI Skill系统 (llms.txt + Jinja2模板)

`scripts/rendercv_skill/` 目录:
- 从Pydantic模型自动生成 `docs/llms.txt`
- 包含完整的模型schema、可用主题、locale列表
- 让AI Agent能精确生成有效的RenderCV YAML
- 附带评估脚本 (`evals/`) 测试AI生成质量

### 8. ATS兼容性验证管线

`scripts/ats_proof/` 目录:
- 4个测试用例 × 5个主题 = 20个PDF
- 双层验证: 文本提取 + 商业解析器
- 自动化生成兼容性报告
- 数据驱动地证明ATS友好性

## 关键文件

| 文件 | 行数 | 职责 |
|------|------|------|
| `renderer/rendercv_typst/lib.typ` | 764 | Typst排版核心库 |
| `schema/variant_pydantic_model_generator.py` | 458 | 主题变体动态生成 |
| `renderer/templater/entry_templates_from_input.py` | ~550 | 条目类型推断和渲染 |
| `schema/models/cv/cv.py` | 250 | CV数据模型 |
| `cli/render_command/render_command.py` | 238 | render命令实现 |
| `renderer/templater/templater.py` | 215 | 模板渲染编排 |

## 创新亮点

1. **YAML字段顺序保留**: `capture_input_order` wrap validator捕获用户定义的字段顺序,header按用户期望的顺序渲染
2. **CLI字段覆盖**: `--cv.name "Jane Doe"` 风格的深层字段覆盖
3. **stale-while-revalidate版本检查**: 后台线程+磁盘缓存,永不阻塞CLI
4. **Pyodide兼容**: 可在浏览器WASM环境中运行,为Web版本铺路
5. **22种语言本地化**: 月份名、短语翻译,全部通过YAML配置
6. **自定义主题热加载**: 用户在YAML同目录放置主题文件夹,动态导入`__init__.py`

## 代码质量

- 每个函数都有Why注释,解释设计原因
- Pydantic模型全面使用Field描述和examples
- 类型注解覆盖全面 (Python 3.12+ 语法)
- 清晰的关注点分离 (schema/renderer/cli)
