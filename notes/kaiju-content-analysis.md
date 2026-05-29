# KaijuEngine/kaiju — Phase 3 内容分析

## 1. 动机与定位

### 项目宗旨
Kaiju Engine 定位为「极快的开源 2D/3D 游戏引擎 + 编辑器」，技术栈为 Go + Vulkan。MIT 许可证（附基督教祝福语）。

### 核心价值主张
- **语言选择**：用 Go 取代 C/C++ 作为游戏引擎的「全栈语言」——游戏逻辑与引擎代码使用同一语言，消除脚本语言与引擎语言的割裂
- **性能证明**：空场景 5,400 FPS vs Unity 1,600 FPS（~3.4 倍），完整游戏场景含 PBR、阴影、UI、音频仍达 2,712 FPS
- **开发速度**：Go 的编译速度远快于 C++，强调「edit-build-launch」的极速迭代
- **编辑器即游戏**：编辑器本身是运行在引擎中的一个「游戏」，证明引擎的灵活性

### 目标受众
希望用现代、简洁的系统级语言做游戏开发的程序员；对 C++ 模板/宏疲劳的引擎开发者；Go 社区中对图形编程感兴趣的开发者。

---

## 2. 作者视角价值分析

### 2.1 问题发现视角：AAA 程序员为什么选 Go？

Brent Farris 在 Tripwire Interactive 做首席引擎/AI 程序员（Killing Floor 系列），日常面对的是 C/C++ 的复杂度。README 中他坦言：

> "I love C, and because I love C and found out that Ken Thompson played a part in designing Go, I gave Go a chance."

关键洞察：他的选择不是「Go 适合做游戏引擎」，而是「Go 让我能以写 C 的心态来写代码，同时去掉了 C++ 的复杂性」。Go 的 Assembly 支持让他写 SIMD 优化时感到「just works」——这是一个深度系统程序员的审美选择。

### 2.2 解法哲学：Host Mediator vs ECS vs 传统 OOP

Kaiju 的架构核心是 **Host Mediator 模式**，这是对 ECS 和传统 OOP 的第三条路：

| 维度 | 传统 OOP（Unity） | ECS（Bevy） | Host Mediator（Kaiju） |
|------|-------------------|-------------|----------------------|
| 数据组织 | 组件继承树 | 纯数据表 + 系统 | Host 结构体聚合所有子系统 |
| 访问模式 | 单例/服务定位器 | 系统查询 | 通过 Host 指针直接访问 |
| 复杂度 | 中等 | 高（学习曲线） | 低（Go 传参风格） |
| GC 友好度 | 差 | 不适用（Rust） | 优秀（结构体内嵌减少指针） |

CONTRIBUTING.md 明确要求：「Prefer composition of structures with members into a single pointer over creating multiple pointers that can be passed around. Please review `host.go` for an example.」

### 2.3 背景知识迁移：从 AAA 经验带来了什么

1. **零堆分配思维**：AAA 引擎的帧预算意识 → `WipeSlice`（39 处使用）清理切片而复用底层数组、`RemoveUnordered` 避免拷贝
2. **SIMD 手写汇编**：amd64 + arm64 双平台手写 SSE 矩阵乘法，配有 Go fallback
3. **多线程架构**：自定义线程池（`concurrent.Threads`），按 CPU 核数启动，条件变量调度
4. **脏标记 Transform**：Transform 组件使用 frameDirty + isDirty 双标记，批量延迟计算世界矩阵
5. **GPU 资源管线化**：Cache-Then-Create 模式——资源请求时放入 pending 队列，渲染帧开始时统一在主线程创建

### 2.4 战略图景

GitHub Sponsors 入口 + Steam SDK 集成目录 + 独立 kaijuengine.com 域名 → 个人热情项目为主，但保留了商业化可能。编辑器标注为「work in progress」，引擎核心标注为「production ready」——战略重心先稳固引擎核心，再打磨编辑器。

---

## 3. 架构与设计决策

### 3.1 项目结构总览

```
src/
├── bootstrap/        # 启动引导（GameInterface 抽象）
├── build/            # 构建标签系统（editor/debug/game 常量生成）
├── editor/           # 编辑器（本身是一个 GameInterface 实现）
├── engine/           # 引擎核心（Host、Entity、Updater、Camera、UI、Collision）
├── engine_entity_data/ # 实体数据组件（相机、灯光、粒子、物理、动画）
├── klib/             # 内部工具库（内存操作、切片工具、序列化）
├── matrix/           # 数学库（Vec2/3/4、Mat3/4、Quaternion、Transform）+ SIMD 汇编
├── platform/         # 平台抽象（窗口、音频、HID、并发、文件系统）
├── rendering/        # 渲染系统（Drawing、材质/纹理/Mesh 缓存、Vulkan 后端）
│   └── vulkan/       # Vulkan CGO 绑定（C 桥接层）
├── plugins/          # Lua 插件系统
├── network/          # 网络（含 master server）
└── ollama/           # AI 集成（Ollama LLM 绑定）
```

总计 998 个 Go 文件，230,270 行代码（含 C/H/S 汇编）。37 个文档文件，3,773 行文档。

### 3.2 Host Mediator 模式实现

**核心入口：`src/engine/host.go`**

`Host` 结构体是整个运行时的中心中介者，聚合了所有子系统：

```go
type Host struct {
    Window            *windowing.Window
    Cameras           hostCameras
    Drawings          rendering.Drawings
    Updater           Updater
    LateUpdater       Updater
    UIUpdater         Updater
    UILateUpdater     Updater
    // 内部缓存（非导出，通过方法访问）
    shaderCache       rendering.ShaderCache
    textureCache      rendering.TextureCache
    meshCache         rendering.MeshCache
    fontCache         rendering.FontCache
    materialCache     rendering.MaterialCache
    // 并发基础设施
    workGroup         concurrent.WorkGroup
    threads           concurrent.Threads
    updateThreads     concurrent.Threads
    uiThreads         concurrent.Threads
    // ...
}
```

关键设计：
- Host 注释明确说明其目的：「designed to remove things like service locators, singletons, and other global state」
- 所有子系统通过 Host 的方法（`ShaderCache()`, `TextureCache()` 等）访问，不存在全局单例
- 支持多 Host 实例隔离窗口和游戏状态
- `Host` 指针在整个代码库中广泛传递，作为唯一的「上下文对象」

### 3.3 Vulkan 渲染管线的 Go 封装

**三层架构**：

1. **C 桥接层** (`rendering/vulkan/vk_bridge.c/h`)：1,446 行 C 代码，为每个 Vulkan API 提供 `call*` 函数指针包装，支持动态加载（`VK_NO_PROTOTYPES`）
2. **CGO 绑定层** (`rendering/vulkan/vulkan.go`)：1,856 行，159 个 `#cgo noescape` 指令——这是 Go 1.22+ 的新特性，告诉编译器 CGO 调用不会让 Go 指针逃逸，**大幅减少 CGO 调用的性能开销**
3. **渲染抽象层** (`rendering/gpu_device*.go`)：GPUDevice → PhysicalDevice + LogicalDevice + Painter，Vulkan 实现与接口分离（`gpu_device.go` vs `gpu_device_vulkan.go`）

**Cache-Then-Create 模式**（线程安全 GPU 资源管理）：

```
任意线程请求资源 → 加入 pendingTextures/pendingMeshes → 
主线程 Render() 开始 → CreatePending() 统一创建 GPU 资源
```

`TextureCache.Texture()` 使用 mutex 保护写入 pending 队列，`CreatePending()` 在主线程无锁执行，巧妙分离了资源请求与 GPU 操作。

### 3.4 CGO 绑定策略

- **动态加载**：不直接链接 Vulkan 库，而是通过 `vk_default_loader` 动态加载函数指针（`VK_NO_PROTOTYPES`），支持不同平台的 Vulkan 实现
- **平台分离**：`vulkan_darwin.go`、`vulkan_linux.go`、`vulkan_windows.go` 等按平台编译
- **MoltenVK 支持**：macOS 通过 MoltenVK 适配 Vulkan API
- **`#cgo noescape` 批量标注**：159 个 Vulkan 调用全部标注为 noescape，这是目前 Go 生态中最大规模的 noescape 应用之一

### 3.5 编辑器与运行时的 Build Tag 分离

**双常量代码生成**（`src/build/tag_generator`）：

```go
// zeditor.go (//go:build editor)
const Editor = true

// zeditor_not.go (//go:build !editor)
const Editor = false
```

同样模式用于 `Debug` 常量。代码中通过 `build.Editor`、`build.Debug` 做编译时分支，Go 编译器会自动消除死代码。

**入口分离**：
- `main.ed.go`（`//go:build editor && !rawsrc`）：使用 `//go:embed *` 将整个 `src/` 嵌入二进制，供编辑器创建项目时导出
- `main.ed.dbg.go`（`//go:build editor && rawsrc`）：开发模式直接读源码目录，用于快速调试
- `main.go`（无 editor tag）：纯运行时入口

构建命令：
- 编辑器：`go build -tags="debug,editor"`
- 发布版：`go build`（无标签）

### 3.6 零堆分配设计实现

多层策略协作实现运行时近零堆分配：

1. **`WipeSlice` 模式**（39 处使用）：`clear(s); return s[:0]` —— 清除指针引用让 GC 回收，但保留底层数组供下帧复用
2. **`RemoveUnordered`**：交换到末尾再截断，O(1) 删除且不分配新内存
3. **结构体内嵌**：Host 内部的缓存、线程池等全部以值类型嵌入，而非指针字段
4. **固定大小池**：`pooling.Pool[T]` 使用固定 256 元素数组（`[ElementsInPool]T`），栈上分配
5. **SIMD 汇编无分配**：Mat4Multiply 等函数用 `NOSPLIT` 标记，在栈上完成全部计算
6. **Concurrent Updater 复用**：Update 函数通过 backAdd/backRemove 双缓冲避免运行时 map 修改
7. **unsafe 内存操作**：`klib.Memcpy`、`StructToByteArray`、`StructSliceToByteArray` 等直接操作内存，零拷贝序列化

---

## 4. 创新点

### 4.1 Go + Vulkan 的性能突破

- **159 个 `#cgo noescape` 指令**：这可能是 Go 生态中最系统化地利用 noescape 减少 CGO 开销的项目。每个 Vulkan API 调用都标注了 noescape，意味着 Go 运行时不需要在每次 CGO 调用时检查指针逃逸
- **手写双平台 SIMD 汇编**（amd64 SSE + arm64 NEON）：Go Plan9 汇编格式，Mat4Multiply 在 SSE 指令集下完成 4x4 矩阵乘法，完全避免函数调用开销（NOSPLIT）
- **结果**：证明 GC 语言在精心设计下可以匹敌甚至超越传统引擎的帧率

### 4.2 Host Mediator 架构模式

一种介于单例模式和 ECS 之间的架构选择。不是一个新概念，但在游戏引擎中这种「单一上下文对象」的彻底贯彻方式值得关注——所有子系统通过一个结构体传递，没有任何全局状态、没有服务定位器。特别适合 Go 的「传参优于全局」惯例。

### 4.3 HTML/CSS 游戏 UI 系统

自研的 retained-mode UI，支持 HTML/CSS 标记语言描述界面。使用 `golang.org/x/net/html` 解析 HTML，自研 CSS 解析器（含 spec_generator 自动生成属性处理代码）。编辑器本身的全部界面都通过这套 HTML/CSS 系统构建。

### 4.4 编辑器源码嵌入

通过 `//go:embed *` 将引擎全部源码嵌入编辑器二进制。用户创建项目时，编辑器将匹配的引擎源码导出到项目目录，确保引擎版本一致性。开发者可以修改导出的引擎源码，但需自行处理升级冲突。

### 4.5 构建标签常量化

将 Go build tags 转换为编译时布尔常量（`build.Editor = true/false`），允许在代码中用 `if build.Editor {}` 而非 build tags 做条件编译。编译器的死代码消除确保运行时零开销。

---

## 5. 可复用模式

| 模式 | 实现位置 | 可复用场景 |
|------|---------|-----------|
| Host Mediator | `engine/host.go` | 任何需要避免全局状态的大型 Go 应用 |
| WipeSlice 切片复用 | `klib/slice.go` | 高频创建/清空切片的热路径 |
| Cache-Then-Create | `rendering/texture_cache.go` | 多线程请求、单线程创建的 GPU/IO 资源管理 |
| Build Tag 常量化 | `build/tag_generator` | 需要在运行时代码中使用编译标签的 Go 项目 |
| #cgo noescape 批量标注 | `rendering/vulkan/vulkan.go` | 所有高频 CGO 调用的 Go 项目 |
| SIMD 汇编 + Go fallback | `matrix/matrix.simd.go` + `.s` 文件 | 需要 SIMD 加速的 Go 数学/数据处理 |
| 双缓冲 Updater | `engine/updater.go` | 运行时动态增删回调的并发安全更新系统 |
| 固定大小对象池 | `engine/pooling/pool.go` | 需要避免堆分配的高频对象创建/销毁 |

---

## 6. 竞品交叉分析

| 维度 | Kaiju (Go+Vulkan) | Ebitengine (Go) | Bevy (Rust) | Godot (GDScript/C#) |
|------|-------------------|-----------------|-------------|---------------------|
| 渲染后端 | Vulkan（动态加载） | OpenGL/Metal/WebGPU | wgpu (Vulkan/Metal/DX12) | Vulkan/OpenGL/Metal |
| 架构模式 | Host Mediator | 简单循环 | ECS (Archetype) | 场景树 + OOP |
| 编辑器 | 自研（HTML/CSS UI） | 无 | 第三方/计划中 | 全功能 |
| 3D 支持 | 完整（PBR、骨骼动画、物理） | 无 | 完整 | 完整 |
| GC 策略 | 近零堆分配 + Go GC | 标准 Go GC | 无 GC（Rust 所有权） | GDScript GC / C# GC |
| 平台 | Win/Linux/Mac/Android | Win/Linux/Mac/Web/Mobile | Win/Linux/Mac/Web | 全平台 |
| 社区规模 | ~490 Stars | ~13K Stars | ~38K Stars | ~95K Stars |
| 独特卖点 | Go 全栈 + AAA 级性能优化 | Go 2D 简单易用 | Rust 安全 + ECS | 全功能 + 易上手 |

**Kaiju 的独特生态位**：Go 语言生态中唯一的 Vulkan 3D 引擎 + 编辑器。Ebitengine 占据了 Go 2D 游戏市场，但没有 3D 和编辑器。Bevy 和 Godot 是功能上的竞品，但语言不同。Kaiju 的竞争力在于 Go 开发者无需学习 Rust/GDScript 即可制作 3D 游戏。

---

## 7. 代码质量评估

### 测试覆盖
- 16 个测试文件，分布在 matrix（Mat4）、klib（slice/memory/strings）、rendering（GLSL/OBJ loader）、CSS parser、collision、encoding、navigation 等模块
- 测试覆盖偏低，核心渲染路径和 Host 逻辑缺少单元测试

### CI/CD
- **三条 GitHub Actions 流水线**：
  - `ci-build-test.yml`：Windows（2022/2025）、macOS-15、Linux 三平台编译 + E2E 自动测试（`--autotest` 模式）
  - `nightly.yml`：夜间构建
  - `main.yml`：主流水线
- **GPU 场景矩阵测试**：使用 Lavapipe（软件 Vulkan）+ Khronos Profiles Layer 模拟 Integrated GPU、NVIDIA Discrete、AMD Discrete、Minimal Vulkan 1.0 四种 GPU 配置，含标准和扩展验证（GPU-assisted + best practices + synchronization validation）
- **Go 1.25**：使用最新的 Go tip 版本

### 文档质量
- 37 个 Markdown 文件（3,773 行），含 mkdocs 驱动的文档站
- CONTRIBUTING.md 详细到规定了指针使用策略、注释风格、接口使用原则、goroutine 标注规范
- 编辑器有独立 README

### 依赖管理
- 极度精简：仅 5 个直接依赖（uuid、CSS parser、clipboard、image、net/html），加 3 个间接依赖
- CONTRIBUTING.md 明确要求：「do not add any other 3rd party packages into the engine」
- 目标是最终替换所有第三方依赖

### 代码风格
- 每个文件有标准化的版权头（含 MIT 许可证 + 圣经引文）
- 公共函数均有 Go doc 注释
- 明确禁止 TODO/FIXME 未经审批的提交
- Assembly 代码要求提供 Go fallback + 基准测试证明
