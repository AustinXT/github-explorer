## 动机与定位

PowerToys 延续了 Windows 95 时代同名工具集的精神 -- 为高级用户提供操作系统级的效率工具，弥补 Windows 内置功能的空白。项目定位有三个层次：

1. **微软的社区试验场**：作为开源项目，PowerToys 充当微软测试新 Windows 功能的前哨站。被广泛采用的功能（如 FancyZones 的窗口布局理念）可能最终被纳入 Windows 本体
2. **企业级工具合规性**：通过 GPO（组策略）实现企业级管控，IT 管理员可以逐模块禁用/启用，这是个人工具集很少考虑的维度
3. **开发者生态入口**：PowerToys Run 和 Command Palette 的插件系统，本质上是微软在构建 Windows 平台的"Spotlight / Alfred"生态

核心解决的问题：Windows 作为通用操作系统，其默认交互在窗口管理、快捷键定制、文件批处理等领域存在明显效率瓶颈。PowerToys 以官方背书 + 开源方式，提供了一组可信赖的增强工具。

## 作者视角

### 对作者团队的价值
- **技术试验平台**：团队可以在 PowerToys 中快速验证新 Windows API（如 Windows 11 Snap Layouts 的前身 FancyZones），降低将功能集成到 OS 的风险
- **社区关系建设**：130K Star 项目是微软开源战略的标杆案例，PM Lead Clint Rutkas 同时负责 Terminal/WSL/Sudo，PowerToys 成为连接微软与 Windows 开发者社区的桥梁
- **模块淘汰机制**：项目敢于下线低价值模块（如 Video Conference Mute Legacy 化），说明团队将可维护性优先于功能数量

### 对使用者的价值
- **零成本获取**：25+ 工具免费开源，替代同类商业工具（如 Sizer、DisplayFusion）的多个付费功能
- **单安装包**：一次安装、统一设置界面、统一更新机制，避免了安装十几个独立小工具的碎片化体验
- **企业安全背书**：微软签名 + GPO 管控 + 遥测数据透明化，让 IT 部门放心在企业环境部署

## 架构与设计决策

### 目录结构概览

```
PowerToys/
├── src/
│   ├── runner/              # 核心启动器（C++），负责模块加载和生命周期管理
│   ├── settings-ui/         # WinUI 3 设置界面（C#），含 MVVM 架构
│   │   ├── Settings.UI/         # 前端 XAML Views + ViewModels
│   │   ├── Settings.UI.Library/ # 设置数据模型（每模块独立 Settings 类）
│   │   └── QuickAccess.UI/     # 快捷访问面板
│   ├── modules/             # 30 个功能模块，每个模块独立子目录
│   │   ├── interface/           # PowertoyModuleIface 抽象接口（C++）
│   │   ├── fancyzones/          # 典型复杂模块：Lib + Editor + CLI + Tests
│   │   ├── cmdpal/              # 最新核心模块：扩展 SDK + 19 个内置扩展
│   │   ├── launcher/            # PowerToys Run：Wox 分支 + 32 个插件
│   │   └── ...                  # 其他模块按独立目录组织
│   ├── common/              # 28 个共享库
│   │   ├── interop/             # C++/C# 跨语言通信（命名管道 IPC）
│   │   ├── SettingsAPI/         # 设置读写统一 API
│   │   ├── GPOWrapper/          # 组策略封装
│   │   ├── Telemetry/           # ETW 遥测
│   │   ├── logger/              # spdlog 封装
│   │   ├── Themes/              # 主题系统
│   │   ├── hooks/               # 全局键盘/鼠标钩子
│   │   ├── LanguageModelProvider/ # AI/LLM 集成抽象层
│   │   └── ...
│   ├── dsc/                 # PowerShell DSC v3 资源（声明式配置）
│   └── ActionRunner/        # 提权操作执行器
├── installer/               # WiX v5 安装包（MSI + MSIX）
├── tools/
│   ├── build/               # 构建脚本（PowerShell）
│   ├── project_template/    # 新模块脚手架模板
│   └── mcp/                 # MCP GitHub Artifacts 工具
└── doc/devdocs/             # 开发者文档
```

### 关键设计决策

#### 1. DLL 插件架构（Runner ←→ Module 契约）

这是整个项目最核心的设计决策。Runner 通过 C++ 虚函数接口 `PowertoyModuleIface` 定义了模块契约：

- **加载方式**：Runner 维护一个硬编码的 DLL 列表（约 30 个），逐一调用 `LoadLibrary` + `powertoy_create()` 工厂函数
- **生命周期**：`enable()` → 运行中可 `get_config()/set_config()` → `disable()` → `destroy()`
- **热键系统**：`get_hotkeys()` + `on_hotkey()` 统一注册到 `CentralizedKeyboardHook`
- **GPO 管控**：每个模块通过 `gpo_policy_enabled_configuration()` 支持组策略开关

**设计权衡**：硬编码 DLL 列表而非动态扫描，牺牲了灵活性但换来了可控性和安全性。每新增模块需修改 `main.cpp` 中的列表。

#### 2. 四种模块类型的分层设计

架构文档明确定义了四种模块类型，体现了务实的技术选型：

| 类型 | 代表模块 | 特点 |
|------|---------|------|
| Simple Module | FindMyMouse, MouseHighlighter | 纯 C++ DLL 内实现，无外部进程 |
| External App Launcher | ColorPicker, FancyZones | C++ DLL + 独立 C#/WPF/WinUI 进程，命名管道 IPC |
| Context Handler | PowerRename, FileLocksmith | Shell 扩展，集成文件资源管理器右键菜单 |
| Registry-based | File Explorer Preview | 注册预览处理程序和缩略图提供程序 |

**洞察**：这种分层让团队可以为每个工具选择最适合的实现方式 -- 简单工具用纯 C++ 获得极低开销，复杂 UI 工具用 C#/WinUI 获得现代化开发体验。

#### 3. 集中化键盘钩子系统

`CentralizedKeyboardHook` 和 `CentralizedHotkeys` 是一个精妙的设计：

- **单一全局钩子**：只安装一个底层键盘钩子（`WH_KEYBOARD_LL`），避免多模块各自安装钩子导致的性能问题
- **冲突检测**：`HotkeyConflictDetector` 负责检测多模块间的快捷键冲突
- **模块化路由**：每个模块通过 `SetHotkeyAction()` 注册回调，钩子按模块名分组管理

#### 4. 设置系统的双重架构

设置系统横跨 C++ 和 C# 两个世界：

- **C++ 侧**（`src/common/SettingsAPI/`）：JSON 文件读写，`PTSettingsHelper` 负责通用设置路径管理
- **C# 侧**（`src/settings-ui/Settings.UI.Library/`）：`BasePTModuleSettings` 基类 + 每模块独立 Settings 类（如 `FancyZonesSettings.cs`）
- **跨语言通信**：Runner(C++) 和 Settings UI(C#) 之间通过 `TwoWayPipeMessageIPC`（命名管道）传递 JSON 消息
- **AOT 兼容**：`BasePTModuleSettings.ToJsonString()` 使用 `SettingsSerializationContext` 实现 Native AOT 兼容的序列化

`EnabledModules` 类是设置系统的枢纽，为每个模块维护启用/禁用状态，带有变更通知和遥测上报。

#### 5. GPO 企业管控层

完整的组策略支持是这个项目与个人工具的核心差异：

- 每个模块在注册表 `SOFTWARE\Policies\PowerToys` 下有独立的策略键
- `GPOWrapper` 提供 C# 投影层，让 Settings UI 可以读取策略配置
- 支持机器级（HKLM）和用户级（HKCU）两种作用域
- 策略可以强制启用/禁用模块，覆盖用户设置

#### 6. 双插件生态系统

项目维护了两套并行的插件体系：

**PowerToys Run（Wox 分支）**：
- 32 个内置插件（Calculator, WindowWalker, WebSearch, OneNote 等）
- `IPlugin` 接口：`Init()` + `Query()` 两个核心方法
- 继承自 Wox 启动器的插件架构

**Command Palette（全新设计）**：
- 19 个内置扩展 + WinGet 扩展
- WinRT IDL 定义的 `IExtension` + `ICommand` 接口体系
- 支持丰富的交互模式：命令列表、表单、确认对话框、Toast 通知
- COM 激活模型，支持进程外扩展

Command Palette 是 PowerToys Run 的"精神继承者"，但采用了更现代的架构（WinRT IDL 而非 .NET 接口），暗示了未来的技术方向。

## 创新点

### 1. AI 能力检测的延迟异步模式
Runner 启动时通过 `DetectAiCapabilitiesAsync()` 在后台线程启动 ImageResizer 的 `--detect-ai` 模式，将检测结果缓存到文件。这是一个巧妙的模式：主进程不阻塞，子模块在首次使用时读取缓存结果。仅在 Windows 11+ 执行，体现了渐进增强策略。

### 2. LLM Provider 抽象层
`src/common/LanguageModelProvider/` 定义了 `ILanguageModelProvider` 接口，对接 `Microsoft.Extensions.AI` 生态。结合 GPO 策略支持（可配置 OpenAI、Azure AI、Mistral、Google、Ollama、FoundryLocal 等），企业 IT 可以控制员工使用哪些 AI 后端。这是将 AI 集成与企业合规结合的前瞻设计。

### 3. PowerShell DSC v3 集成
`src/dsc/` 提供声明式系统配置（Desired State Configuration），IT 管理员可以用 YAML/JSON 声明"PowerToys 应处于什么状态"，DSC 引擎自动修正偏差。这将 PowerToys 从"个人工具"提升到"可管理的企业基础设施组件"。

### 4. Debug 模式容错加载
Runner 在 Debug 模式下加载模块失败时仅记录警告而非弹窗报错，让开发者可以只编译自己修改的模块就能调试，无需编译全部 30 个模块。这显著降低了新贡献者的上手门槛。

### 5. 模块模板脚手架
`tools/project_template/ModuleTemplate/` 提供完整的新模块脚手架（包含 `dllmain.cpp`、`PowertoyModuleIface` 实现模板、设置读写示例），新模块开发者可以直接复制并填充业务逻辑。

### 6. MCP 工具集成
`tools/mcp/github-artifacts/` 包含 MCP（Model Context Protocol）服务器实现，用于 AI 辅助开发。结合 `AGENTS.md` 的 AI 贡献者指南，项目积极拥抱 AI 辅助开发工作流。

## 可复用模式

### 1. DLL 插件宿主模式（Runner Pattern）
**适用场景**：需要在单一宿主进程中管理多个可独立开关的功能模块的桌面应用。

核心要素：
- 纯虚函数接口定义模块契约（`get_key()`, `enable()`, `disable()`, `destroy()`）
- 工厂函数 `powertoy_create()` 作为 DLL 入口点
- 智能指针 + 自定义 Deleter 管理模块生命周期（`PowertoyModuleDeleter`）
- 模块注册表（`std::map<std::wstring, PowertoyModule>`）统一管理所有加载的模块

### 2. 集中化键盘钩子模式
**适用场景**：多模块需要监听全局快捷键但又不能各自安装钩子的场景。

核心要素：
- 单一 `WH_KEYBOARD_LL` 钩子 + 模块化路由表
- 按模块名隔离的快捷键注册/清理（`SetHotkeyAction` / `ClearModuleHotkeys`）
- 内置冲突检测机制

### 3. C++/C# 跨语言 IPC 模式
**适用场景**：高性能 C++ 核心 + C# 现代 UI 的混合语言桌面应用。

核心要素：
- `TwoWayPipeMessageIPC` 命名管道封装双向通信
- JSON 作为跨语言数据交换格式
- `settings_objects.h` (C++) 和 `BasePTModuleSettings.cs` (C#) 分别在两侧解析同一份 JSON

### 4. GPO 策略层模式
**适用场景**：需要企业级集中管控的桌面工具。

核心要素：
- 注册表路径约定（`SOFTWARE\Policies\{AppName}`）
- 枚举类型定义策略状态（not_configured / enabled / disabled / unavailable）
- C++ 策略读取层 + WinRT 投影层供 C# UI 使用
- 策略优先于用户配置的覆盖逻辑

### 5. 模块化设置基类模式
**适用场景**：多模块应用中每个模块有独立配置的场景。

核心要素：
- `BasePTModuleSettings` 抽象基类提供 `Name`, `Version`, `ToJsonString()` 公共行为
- 每个模块继承并添加自己的属性（如 `FancyZonesSettings`）
- `EnabledModules` 作为中央启停开关，带变更通知回调
- Native AOT 兼容的 JSON 序列化注册机制

### 6. OOBE/SCOOBE 引导流程模式
**适用场景**：需要区分首次安装引导（OOBE）和版本更新引导（SCOOBE - Second Chance Out of Box Experience）的应用。

## 竞品交叉分析

| 维度 | PowerToys | Flow Launcher | AutoHotkey | Everything |
|------|-----------|---------------|------------|------------|
| **定位** | 官方系统工具集 | 社区启动器 | 脚本自动化 | 极速文件搜索 |
| **覆盖面** | 25+ 工具全覆盖 | 仅启动器 | 仅自动化 | 仅搜索 |
| **企业管控** | GPO + DSC 全面支持 | 无 | 无 | 无 |
| **插件生态** | PowerToys Run 32 + CmdPal 19 | 丰富的社区插件 | 庞大脚本库 | 有限 |
| **性能开销** | 30 个 DLL 常驻内存 | 较轻 | 按需启动 | 极低 |
| **更新频率** | 4-6 周一个大版本 | 社区驱动 | 低频 | 低频 |
| **AI 集成** | LLM Provider + AI 超分 | 无 | 无 | 无 |

**关键差异**：PowerToys 的核心竞争力不在于单个工具的深度（Flow Launcher 作为启动器可能更强），而在于：
1. 微软官方背书带来的信任度和 Windows API 的深度集成
2. 企业管控能力（GPO/DSC）是个人工具无法企及的
3. 统一的安装、设置和更新体验减少了碎片化
4. AI 能力整合（AdvancedPaste、ImageResizer 的 AI 超分辨率）是独有的方向

**潜在弱点**：常驻 30 个 DLL 的内存开销、模块质量参差不齐（有些模块默认关闭暗示成熟度不足）、双插件体系（Run vs CmdPal）可能造成生态分裂。

## 代码质量

### 架构层面
- **模块化良好**：30 个模块通过统一接口解耦，新增/移除模块的影响面可控
- **关注点分离**：Runner（C++ 核心）、Settings UI（C# 前端）、Module DLL 三层分明
- **共享库丰富**：`src/common/` 下 28 个共享库覆盖日志、IPC、设置、遥测、主题等横切关注点
- **文档完善**：`AGENTS.md` 针对 AI 贡献者的详细指南、`doc/devdocs/core/architecture.md` 的架构文档、模块模板脚手架

### 工程实践
- **测试覆盖**：24 个单元测试项目 + 10+ UI 自动化测试 + 4 个模糊测试项目
- **构建系统**：集中化包版本管理（`Directory.Packages.props`）、自动化构建脚本、详细的构建失败日志
- **CI/CD**：GitHub Actions 工作流（Issue 去重、Store 提交、拼写检查）
- **安全性**：SHA256 校验和、证书签名流程、GPO 策略

### 需注意的技术债
- 硬编码的模块 DLL 列表（新增模块需修改 `main.cpp`），可考虑基于配置文件的动态发现
- PowerToys Run（Wox 分支）和 Command Palette 并行两套插件生态，长期可能需要统一
- `EnabledModules.cs` 每新增模块需手动添加属性（约 30 个重复的 getter/setter），可考虑代码生成
- 部分模块默认关闭（Keyboard Manager, MouseJump, PowerAccent 等），暗示这些模块的成熟度或适用场景有限

### 质量检查清单

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 单元测试 | 良好 | 24 个测试项目，主要模块有覆盖 |
| UI 自动化测试 | 良好 | 10+ 模块有 UI 测试，使用 WinAppDriver |
| 模糊测试 | 部分 | 4 个模块（FancyZones, AdvancedPaste, RegistryPreview, Hosts） |
| 静态分析 | 启用 | `Microsoft.CodeAnalysis.NetAnalyzers 9.0.0` |
| 文档 | 优秀 | AGENTS.md + 架构文档 + 模块模板 + BUILD 指南 |
| 错误处理 | 良好 | 模块加载异常不阻塞 Runner，各模块独立崩溃隔离 |
| 日志系统 | 良好 | spdlog (C++) + Logger (C#) 统一封装 |
| 遥测 | 完善 | ETW Trace + 模块级遥测事件 |
| 可访问性 | 未深入评估 | - |
| 国际化 | 良好 | .resx / .resw 资源文件，内部 l10n 团队负责 |
| 安全审计 | 良好 | GPO 支持、SHA256 校验、提权操作隔离（ActionRunner） |
| 依赖管理 | 良好 | 集中版本管理，固定易受攻击的传递依赖版本 |
| 代码风格 | 规范 | 有 XamlStyler 配置、C++/C# 编码规范文档 |
