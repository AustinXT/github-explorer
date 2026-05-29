# openai/skills — Phase 3 内容分析（What & How）

> **重要更正**：该仓库实际为 **openai/skills**（非 anthropics/skills）。原始于 `github.com/anthropics/skills` 的 URL 指向的克隆内容全部为 OpenAI Codex 的 Agent Skills 仓库。git remote 为 `https://github.com/openai/skills`，所有贡献者邮箱为 `@openai.com`。

---

## 动机与定位

**核心定位**：Agent Skills 的官方参考实现和分发中心。Skills 是 AI Agent 可发现、可复用的"能力文件夹"——由指令（Markdown）、脚本（Python/Shell/JS）和资源（模板/文档）组成的自包含单元。

**战略意图**：
1. **标准化 Agent 能力扩展**：推动 agentskills.io 成为跨平台开放标准（目前 Codex 首发，Claude Code 也采纳了类似机制）
2. **建立 Codex 生态护城河**：39 个官方 Skills 覆盖文档处理、代码审查、部署运维、设计还原、安全审计等高频场景
3. **降低 Agent 专业化门槛**：将领域专家的程序性知识编码为可复用模块，让通用 Agent 秒变垂直专家

**不做什么**：Skills 不是插件系统（没有 runtime API），不是 MCP 替代品（而是与 MCP 互补），不是 RAG 知识库（而是程序性操作指南）。

---

## 作者视角

**OpenAI 做 Skills 的核心逻辑**：

1. **解决 Agent 的"最后一公里"问题**——LLM 什么都"知道"但什么都不"精通"。Skills 将 LLM 不可能完全记住的程序性知识（PDF 操作用 reportlab、DOCX 转换用 soffice、Figma MCP 的正确调用顺序）编码为可按需加载的上下文。

2. **在 Claude Code 的 CLAUDE.md 之上的差异化竞争**——Claude Code 用 `CLAUDE.md` 做项目级指令，Skills 比这更进一步：它有渐进式加载（三级上下文管理）、标准目录结构、脚本捆绑执行、MCP 依赖声明。这是一个完整的 Skill 生命周期管理方案。

3. **Codex 产品化的基础设施**——Skills 是 Codex 区别于通用聊天机器人的核心差异化特性。Codex 的 UI 层通过 `agents/openai.yaml` 渲染 Skill 卡片、触发 Skill 执行，这是产品体验闭环的关键一环。

---

## 架构与设计决策

### 1. Skill 目录结构与 SKILL.md 规范

```
skill-name/
├── SKILL.md              # 必需：YAML 元数据 + Markdown 指令
├── agents/
│   └── openai.yaml       # 推荐：UI 元数据（display_name, icon, default_prompt）
├── scripts/              # 可选：可执行脚本
├── references/           # 可选：按需加载的参考文档
├── assets/               # 可选：输出用的模板/图片等
└── LICENSE.txt           # 必需：每个 Skill 独立许可
```

**关键设计决策**：
- **SKILL.md 的 YAML frontmatter 是唯一触发机制**：`name` + `description` 是 Codex 判断何时使用 Skill 的唯一依据。Body 只在触发后加载。这意味着 description 承担了"函数签名"的角色。
- **严格的命名规范**：小写字母+数字+连字符，最长 64 字符，动词开头优先（如 `gh-fix-ci`、`security-threat-model`）。
- **每个 Skill 独立许可**：允许同一仓库内混合许可模式（实际为 Apache 2.0 居多，Notion 系列为 source-available）。

### 2. skill-creator（元技能）

skill-creator 是整个仓库最核心的设计——一个"用来创建 Skill 的 Skill"。它的 SKILL.md 长达 359 行，是整个仓库中最长的指令文件，实质是 **Skill 开发者手册**。

**核心工具链**：
| 脚本 | 功能 |
|------|------|
| `init_skill.py` | 脚手架：生成标准目录 + 模板 SKILL.md |
| `quick_validate.py` | 校验：检查 frontmatter 格式、命名规则 |
| `generate_openai_yaml.py` | UI 元数据生成 |

**六步创建流程**：理解需求 → 规划资源 → 初始化 → 编辑实现 → 校验 → 迭代。这是一个经过打磨的 Skill 工程化流程。

**设计哲学**（直接引用 SKILL.md）：
> "Context window is a public good" — 上下文窗口是公共资源，每个 Skill 都应证明自己值得那些 token。
> "Default assumption: Codex is already very smart" — 只添加模型不知道的信息。

### 3. document-skills 实现模式

文档处理类 Skills（pdf、doc、spreadsheet、slides）展示了两种截然不同的实现策略：

**纯指令模式**（pdf, doc, spreadsheet）：
- 不携带自有脚本（pdf）或仅少量脚本（doc 有 `render_docx.py`）
- 指令驱动：告诉 Agent 用哪些第三方工具（reportlab、python-docx、openpyxl）
- 核心价值是**工具选型决策**和**质量检查 checklist**

**重资源模式**（slides）：
- 携带 10 个 JS helper 文件（76KB 的 pptxgenjs_helpers/）
- 5 个 Python 辅助脚本（渲染、溢出检测、蒙太奇、字体检测）
- 指令 + 脚本 + 资产三层联动

**这揭示了一个重要设计原则**：Skill 的"自由度"与任务的脆弱性成反比。文本处理容错性高，用指令即可；幻灯片排版极易出错，需要大量确定性脚本保障。

### 4. 渐进式加载机制

三级上下文管理是 Skills 架构最大的创新：

| 级别 | 内容 | 加载时机 | 典型大小 |
|------|------|----------|----------|
| L1 | name + description | 始终在上下文中 | ~100 词 |
| L2 | SKILL.md body | Skill 被触发后 | <5K 词（建议 <500 行） |
| L3 | scripts/ + references/ + assets/ | Agent 按需加载 | 无上限 |

**L3 的巧妙之处**：脚本可以**不读入上下文直接执行**，绕过了上下文窗口限制。这让一个 Skill 理论上可以携带任意大的工具集。

**渐进式加载的三种模式**：
1. **高层指南 + 引用**：SKILL.md 是导航地图，references/ 是详细手册
2. **领域分区**：按变体拆分（如 cloudflare-deploy 的多个云服务商参考文件）
3. **条件详情**：基础功能内联，高级功能指向独立文件

### 5. 脚本执行模式

Skills 中的脚本有三种执行路径：

1. **Agent 直接调用**（最常见）：Agent 读取 SKILL.md 中的命令模板，构造参数后通过 shell 执行
   ```bash
   python3 scripts/sentry_api.py list-issues --org myorg --limit 20
   ```

2. **Wrapper 脚本模式**（playwright）：通过 shell wrapper 抽象底层工具安装差异
   ```bash
   "$PWCLI" open https://example.com  # wrapper 内部用 npx 调用
   ```

3. **辅助库模式**（slides）：Agent 将 helper 文件复制到工作目录，在生成的代码中 import

**脚本约定**：
- 优先 `uv pip install`，fallback 到 `pip`
- 系统工具用 brew（macOS）或 apt（Linux）
- 环境变量通过 `$CODEX_HOME` 定位 Skill 路径

---

## 创新点

### 1. "Skill 即文件夹"范式
与传统的插件系统（需要 runtime、API 适配器、注册表）不同，Skill 是纯文件夹——没有安装过程、没有依赖管理、没有运行时。复制粘贴即部署。这是一个**极低摩擦的能力扩展机制**。

### 2. 元技能 bootstrap
skill-creator 本身就是一个 Skill，这意味着：
- 用 Codex 创建 Skill 的体验本身就是 Skill 标准的示范
- 形成自举闭环：Skill 标准 → skill-creator Skill → 新 Skill → 标准演进

### 3. 声明式 MCP 依赖
`agents/openai.yaml` 中的 `dependencies.tools` 让 Skill 可以声明对外部 MCP 服务的依赖（如 Figma MCP、Linear MCP、Notion MCP）。这是 Skills 与 MCP 的融合点——Skill 提供工作流逻辑，MCP 提供数据通道。

### 4. evaluation 模式
Notion 系列 Skills 包含 `evaluations/` 目录，定义了 JSON 格式的测试用例：包含 `query`、`expected_behavior`（步骤序列）和 `success_criteria`。这是 Agent Skill 质量保证的早期探索，虽然按 Issue #556 反馈触发率为 0%。

### 5. 三级分发体系
`.system`（预装）→ `.curated`（官方审核）→ `.experimental`（实验性）的分级机制，平衡了标准化与开放性。

---

## 可复用模式

### 1. 渐进式上下文加载
**适用场景**：任何需要管理大量领域知识的 Agent 系统。
**核心思路**：元数据始终在上下文 → 匹配后加载指令 → 按需加载详细参考。
**实现要点**：L1 的 description 必须精准，因为它是唯一的"触发器"。

### 2. 自由度分级设计
**模式**：根据任务脆弱性选择指令密度。
- 开阔地带（多种正确路径）→ 文本指令 + 原则
- 窄桥（易出错、需要精确）→ 确定性脚本 + 严格 checklist

### 3. Wrapper 脚本抽象
**模式**：用 shell wrapper 屏蔽工具安装/版本差异，让 SKILL.md 中的命令跨环境一致。

### 4. SKILL.md 作为"函数签名"
**模式**：将 YAML frontmatter 当作 Agent 能力发现的索引，body 当作执行手册。这对设计任何 Agent 能力注册系统都有参考价值。

### 5. 视觉验证闭环
**模式**：文档类 Skills 统一采用"生成 → 渲染为图片 → 视觉检查 → 修正"的迭代闭环。这是利用多模态能力做质量保证的标准范式。

---

## 竞品交叉分析

### vs obra/superpowers（104K Stars）
| 维度 | openai/skills | superpowers |
|------|--------------|-------------|
| 本质 | Skill 内容仓库 + 分发标准 | 方法论 + prompt 库 |
| 交付物 | 可安装的 Skill 文件夹 | Markdown 方法论文档 |
| 执行方式 | Agent 自动发现并触发 | 用户手动引用 |
| 脚本支持 | 原生支持脚本/资产捆绑 | 无 |
| 平台绑定 | Codex 深度集成（UI、安装） | 平台无关 |

**关键差异**：superpowers 是"教 Agent 怎么思考"，skills 是"给 Agent 工具和流程"。前者适合通用 Agent 增强，后者适合特定任务自动化。

### vs GitHub Copilot Skills / Extensions
| 维度 | openai/skills | Copilot Extensions |
|------|--------------|-------------------|
| 运行时 | 无（纯文件） | 需要 OAuth + HTTP endpoint |
| 分发 | Git clone / skill-installer | GitHub Marketplace |
| 能力边界 | 指令 + 脚本 | 完整 API 后端 |
| 门槛 | 写 Markdown 即可 | 需要开发服务端 |

**关键差异**：Skills 选择了"零基础设施"路线——不需要服务器、不需要 OAuth、不需要注册审核。这是一个极端务实的设计选择，代价是能力边界有限（无法做实时 API 调用，除非结合 MCP）。

### vs MCP（Model Context Protocol）
Skills 和 MCP 是**互补而非竞争**关系：
- MCP 提供**数据通道**（API 调用、工具执行）
- Skills 提供**工作流逻辑**（何时调用、如何组合、质量标准）
- Figma Skill = Figma MCP 调用顺序 + 实现规范 + 验证 checklist
- 但 Issue #16 反映社区期望更深度的融合（如 Skill 自动配置 MCP server）

---

## 代码质量

### 测试覆盖
- **无统一测试框架**：仓库无 CI/CD（无 `.github/workflows/`）
- **个别 Skill 有测试**：`slides/scripts/slides_test.py`（溢出检测测试）
- **evaluation 模式**：4 个 Notion Skills 有 JSON 评测用例，但 Issue #556 报告触发率 0%
- **验证仅限格式**：`quick_validate.py` 只检查 YAML frontmatter 格式，不验证脚本可执行性或指令质量

### 代码统计
| 指标 | 数值 |
|------|------|
| 总 Skill 数 | 39 个（3 system + 36 curated） |
| Python 脚本 | 29 个 |
| Shell 脚本 | 3 个 |
| JS 文件 | 10 个（全在 slides/assets/） |
| Markdown 文件 | 499 个（绝大部分是 references） |
| 总提交数 | 99 个（2025-11 至 2026-03） |
| 贡献者 | 15 人（12+ 为 @openai.com） |

### 仓库健康度
- **活跃度高**：3 个月 99 次提交，平均每天 1+ 提交
- **许可清晰**：Apache 2.0 为主，Notion 系 Skills 为 source-available
- **代码规范中等**：无 linter/formatter 配置，无 pre-commit hooks，脚本风格因 Skill 而异
- **文档质量高**：skill-creator 的 SKILL.md 是极佳的开发者文档范例
- **experimental 已清理**：历史上存在的实验性 Skills 大部分已被移除，保持仓库整洁

### 潜在风险
1. **无 CI 意味着 PR 质量完全依赖人工 review**
2. **脚本缺少单元测试**——29 个 Python 脚本仅 slides_test.py 有测试
3. **evaluation 框架名存实亡**——定义了 JSON 用例但无自动化执行
4. **Issue #492 暴露的信任边界问题**——社区 Skill 可借用 `anthropic/` 等命名空间建立虚假信任
