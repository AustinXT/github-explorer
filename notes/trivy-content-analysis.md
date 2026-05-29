# Trivy 内容分析（What & How）

> 仓库：[aquasecurity/trivy](https://github.com/aquasecurity/trivy)
> 分析日期：2026-03-22

## 动机与定位

Trivy 的核心动机是**解决云原生安全扫描的碎片化问题**。在 Trivy 出现之前，开发者需要为不同目标（容器镜像、文件系统、IaC 代码、K8s 集群）使用不同的扫描工具，每个工具有自己的安装流程、配置方式和输出格式。Trivy 的定位是"一站式安全扫描器"（comprehensive and versatile security scanner），用一个 CLI 二进制文件统一覆盖：

- **5 种扫描目标**：容器镜像、文件系统、Git 仓库、虚拟机镜像、Kubernetes 集群
- **5 种扫描能力**：漏洞（CVE）、IaC 错误配置、SBOM 生成、密钥泄露、许可证检查

README 中的核心命令模式清晰体现了这一哲学：`trivy <target> [--scanners <scanner1,scanner2>] <subject>`——目标和扫描器是两个正交维度，用户自由组合。

从商业角度看，Trivy 是 Aqua Security 的开源战略支柱：
1. 作为 Harbor、GitLab、Azure Defender 的默认扫描器，建立行业标准地位
2. Docker Hub 拉取量 1.08 亿次，构建了巨大的用户基础
3. 商业版 Trivy Premium 在此基础上提供客户支持、高级内容和集中管理

## 作者视角

### 问题发现

Teppei Fukuda（knqyf263）在以色列云原生安全领域工作的过程中，发现了三个关键痛点：

1. **工具碎片化**：容器扫描用 Clair，IaC 扫描用 Checkov/tfsec，密钥扫描用 truffleHog，开发者需要学习和维护多套工具链
2. **漏洞数据库管理复杂**：不同扫描器各自管理 CVE 数据库，更新频率不一、格式不一，导致结果不一致
3. **集成成本高**：每个工具有不同的 CI/CD 集成方式，安全工程师需要大量的胶水代码

### 解法哲学

Trivy 的解法哲学可以概括为 **"单二进制、多目标、插件化"**：

1. **零配置体验**：`brew install trivy && trivy image python:3.4-alpine` 即可完成首次扫描。漏洞数据库自动从 OCI 仓库（GHCR/GCR）下载，无需手动配置
2. **Analyzer 注册表模式**：所有分析器通过 `init()` 函数自注册到全局 map，运行时根据文件路径匹配自动启用，新增语言支持只需添加一个 analyzer 文件
3. **分层解耦架构**：Artifact（采集层）→ Analyzer（分析层）→ Scanner（扫描层）→ Report（输出层）四层分离，每层可独立扩展
4. **OCI-native 数据管理**：漏洞数据库以 OCI Artifact 格式分发，复用容器仓库基础设施，支持离线场景

### 背景知识迁移

- **容器运行时知识**：对 OCI 镜像规范的深度理解，使得 Trivy 能按层（layer）分析容器镜像，并缓存已分析的层，显著提升大规模扫描性能
- **包管理器生态知识**：覆盖 16+ 编程语言的依赖文件格式（从 package-lock.json 到 Cargo.lock），这是长期积累的领域知识
- **OS 发行版安全公告体系**：针对 Alpine、Debian、RHEL、Ubuntu 等 20+ 发行版实现了独立的漏洞检测器（`pkg/detector/ospkg/`），每个发行版的安全公告格式和更新节奏各不相同

### 战略图景

Trivy 的演进路线体现了清晰的战略图景：

1. **起点**（2019）：容器镜像漏洞扫描——切入最高频场景
2. **扩展目标**（2020-2021）：文件系统、Git 仓库、Kubernetes——覆盖全开发生命周期
3. **扩展能力**（2021-2022）：IaC 错误配置、密钥扫描、许可证检查、SBOM——从漏洞扫描升级为全面安全扫描
4. **生态标准**（2022-2024）：VEX 支持、Sigstore 集成、SBOM 双向能力（生成+消费）——成为安全供应链基础设施
5. **平台化**（2024-2026）：WASM 模块扩展、插件生态、通知系统——向平台演进

## 架构与设计决策

### 目录结构概览

```
trivy/
├── cmd/trivy/main.go         # 入口：极简，委托给 pkg/commands
├── pkg/
│   ├── commands/              # CLI 命令定义（cobra）
│   │   ├── app.go             # 命令注册中心：image/fs/repo/k8s/sbom/vm/...
│   │   └── artifact/run.go    # Runner 核心编排：DB初始化→WASM加载→扫描→报告
│   ├── fanal/                 # 文件分析引擎（Trivy 的核心）
│   │   ├── analyzer/          # 分析器框架 + 所有分析器实现
│   │   │   ├── analyzer.go    # 接口定义 + 全局注册表
│   │   │   ├── const.go       # 60+ 分析器类型常量
│   │   │   ├── language/      # 16 种语言的依赖分析器
│   │   │   ├── os/            # OS 发行版识别
│   │   │   ├── pkg/           # 包管理器分析（apk/dpkg/rpm）
│   │   │   ├── config/        # IaC 配置分析器
│   │   │   └── secret/        # 密钥扫描分析器
│   │   ├── artifact/          # 扫描目标抽象
│   │   │   ├── image/         # 容器镜像分析
│   │   │   ├── local/         # 本地文件系统分析
│   │   │   ├── repo/          # Git 仓库分析
│   │   │   ├── vm/            # 虚拟机镜像分析（AMI/EBS）
│   │   │   └── sbom/          # SBOM 文件分析
│   │   ├── walker/            # 文件遍历器（FS/Tar/VM）
│   │   ├── image/             # 容器镜像操作（Docker/OCI/Remote）
│   │   ├── handler/           # 后处理器（unpackaged 检测等）
│   │   ├── applier/           # 层合并器（将多层镜像合并为最终状态）
│   │   └── secret/            # 密钥扫描引擎（正则规则）
│   ├── scan/                  # 扫描服务层
│   │   ├── service.go         # 顶层服务：Artifact.Inspect() → Backend.Scan()
│   │   ├── local/service.go   # 本地扫描实现：OS包+语言包+错误配置+密钥+许可证
│   │   ├── ospkg/             # OS 包漏洞扫描
│   │   └── langpkg/           # 语言包漏洞扫描
│   ├── detector/ospkg/        # 23+ OS 发行版漏洞检测器
│   ├── db/                    # 漏洞数据库管理（OCI Artifact 下载+BoltDB 存储）
│   ├── iac/                   # IaC 扫描子系统
│   │   ├── scanners/          # Terraform/CloudFormation/Docker/Helm/K8s/Ansible/ARM 扫描器
│   │   ├── rego/              # Rego 策略引擎
│   │   └── rules/             # 内置安全规则
│   ├── sbom/                  # SBOM 生成与消费
│   │   ├── core/bom.go        # SBOM 中间表示（IR）
│   │   ├── cyclonedx/         # CycloneDX 格式
│   │   └── spdx/              # SPDX 格式
│   ├── plugin/                # 插件系统（外部二进制扩展）
│   ├── module/                # WASM 模块系统（WebAssembly 扩展）
│   ├── extension/hook.go      # Hook 框架：PreRun/PostRun/PreScan/PostScan/PreReport/PostReport
│   ├── cache/                 # 缓存层（本地FS/Redis/内存/远程）
│   ├── report/                # 输出格式（JSON/SARIF/Table/Template/CycloneDX/SPDX/GitHub）
│   ├── flag/                  # 命令行标志定义（28 个标志文件，按功能分组）
│   ├── k8s/                   # Kubernetes 集群扫描
│   ├── notification/          # 版本更新通知
│   └── result/                # 结果过滤与处理
├── internal/                  # 测试工具（cachetest/dbtest/gittest 等）
├── integration/               # 集成测试（16 个测试文件）
├── e2e/                       # 端到端测试
├── rpc/                       # gRPC 定义（client/server 模式）
├── helm/                      # Helm Chart
└── docs/                      # MkDocs 文档站
```

### 关键设计决策

**1. Analyzer 注册表模式（核心设计）**

这是 Trivy 最关键的设计模式。所有分析器通过全局注册表管理：

```go
// pkg/fanal/analyzer/analyzer.go
var analyzers = make(map[Type]analyzer)

func RegisterAnalyzer(analyzer analyzer) {
    analyzers[analyzer.Type()] = analyzer
}
```

每个分析器实现两个关键方法：
- `Required(filePath string, info os.FileInfo) bool`——基于文件路径判断是否需要分析
- `Analyze(ctx context.Context, input AnalysisInput) (*AnalysisResult, error)`——执行分析

这种设计使得新增语言/格式支持极为简单：只需创建一个新文件，在 `init()` 中调用 `RegisterAnalyzer()`，即可被自动发现。目前已注册 60+ 种分析器类型。

**2. Artifact-Backend 分离（扫描编排）**

扫描流程被分为两个正交维度：

- **Artifact**（采集）：定义"如何获取文件"——容器镜像按层遍历 tar、文件系统直接 walk、远程仓库先 clone 再 walk
- **Backend**（扫描）：定义"如何检测问题"——本地模式直接查 BoltDB 漏洞库，远程模式通过 gRPC 调用服务端

`scan.Service` 组合了两者：先调用 `artifact.Inspect()` 获取文件信息，再调用 `backend.Scan()` 执行扫描。

**3. 六层 Hook 扩展机制**

`pkg/extension/hook.go` 定义了三类 Hook，每类包含 Pre/Post 两个时机：

| Hook 类型 | 时机 | 用途 |
|-----------|------|------|
| RunHook | PreRun / PostRun | 运行前后的全局初始化/清理 |
| ScanHook | PreScan / PostScan | 扫描前后修改目标或结果 |
| ReportHook | PreReport / PostReport | 报告前后修改输出 |

WASM 模块和商业插件（trivy-plugin-aqua）通过这些 Hook 注入自定义逻辑，无需修改核心代码。

**4. OCI-native 漏洞数据库管理**

漏洞数据库以 OCI Artifact 格式存储在 GHCR（`ghcr.io/aquasecurity/trivy-db`）和 GCR 镜像（`mirror.gcr.io/aquasec/trivy-db`），双源容灾。管理逻辑：

- 首次运行自动下载，存储为本地 BoltDB
- 通过 `metadata.json` 记录 `DownloadedAt` 和 `NextUpdate` 时间
- 每次扫描前检查：若距上次下载不足 1 小时或未到更新时间，跳过更新
- 支持 `--skip-db-update` 用于离线/气隙环境
- Schema Version 机制确保 CLI 版本与 DB 版本兼容

**5. 多层缓存架构**

`pkg/cache/` 提供了 5 种缓存实现：
- `fs.go`——本地文件系统缓存（默认）
- `redis.go`——Redis 缓存（多实例共享）
- `memory.go`——内存缓存（CI 场景）
- `remote.go`——远程缓存（client/server 模式）
- `nop.go`——空缓存（禁用缓存）

容器镜像扫描时，缓存键基于层的 DiffID 计算（`pkg/cache/key.go`），相同的层只需分析一次。

**6. Client/Server 分离架构**

通过 gRPC（`rpc/` 目录）支持 client/server 模式：
- Server 端持有漏洞数据库，执行扫描
- Client 端只负责文件采集（Artifact 层），将 blob 发送给 Server
- 适用于大规模扫描场景（减少每个 CI job 的 DB 下载开销）

## 创新点

**1. 单二进制多维度扫描矩阵**

Trivy 将"扫描目标"和"扫描能力"解耦为两个正交维度，通过 `--scanners` 标志自由组合。这不是简单的命令行参数设计，而是贯穿整个架构的抽象——Artifact 层处理目标差异，Scanner 层处理能力差异，两者通过统一的 `AnalysisResult` 数据结构连接。

**2. OCI Artifact 作为数据分发机制**

将漏洞数据库打包为 OCI Artifact，复用容器镜像仓库（GHCR/GCR/ECR）的基础设施来分发安全数据。这是一个将容器生态基础设施"跨界复用"的创举——用户无需额外搭建数据服务器，任何能拉取容器镜像的环境都能自动获取最新的漏洞数据库。

**3. SBOM 中间表示（IR）+ 双向能力**

`pkg/sbom/core/bom.go` 定义了一个 SBOM 中间表示层（BOM struct），支持 CycloneDX JSON/XML 和 SPDX JSON/TV/XML 多种格式的双向转换：
- **生成方向**：扫描结果 → BOM IR → CycloneDX/SPDX 输出
- **消费方向**：CycloneDX/SPDX 输入 → BOM IR → 漏洞扫描

这使得 Trivy 既可以作为 SBOM 生产者（CI/CD 中生成 SBOM），也可以作为 SBOM 消费者（对已有 SBOM 执行漏洞扫描）。还支持 Sigstore Bundle 格式的 SBOM 证明（attestation）。

**4. WASM 模块扩展机制**

通过 WebAssembly（wazero 运行时）支持用户自定义分析器和 Hook，实现安全的沙箱化扩展。WASM 模块可以：
- 注册为自定义 Analyzer（分析新的文件格式）
- 注册为 Hook（在扫描前后注入逻辑）

模块间通过内存共享（`readMemory`/`stringToPtrSize`）进行数据交换，日志通过宿主函数注入（`logDebug`/`logInfo`/`logWarn`/`logError`）。

**5. 层级并行分析**

容器镜像按层并行分析（`pkg/fanal/artifact/image/`），使用 semaphore 控制并发度。每层内部的多个分析器也并行执行（`errgroup` + `semaphore.Weighted`）。已分析的层通过 DiffID 缓存，在同一 CI pipeline 中扫描多个共享基础镜像的镜像时，大幅减少重复分析。

## 可复用模式

**1. 全局注册表 + init() 自注册模式**

```go
// 定义接口
type analyzer interface {
    Type() Type
    Required(filePath string, info os.FileInfo) bool
    Analyze(ctx context.Context, input AnalysisInput) (*AnalysisResult, error)
}
// 全局注册
var analyzers = make(map[Type]analyzer)
func RegisterAnalyzer(a analyzer) { analyzers[a.Type()] = a }
```

适用于需要"开放扩展、文件级隔离"的场景，如日志处理器、数据解析器等。通过 `_ "path/to/all"` 批量导入触发注册。

**2. Functional Options 模式**

整个代码库大量使用 Go 的 Functional Options 模式（如 `db.Option`, `plugin.ManagerOption`, `artifact.Option`），在保持 API 向后兼容的同时支持灵活配置。

**3. OCI Artifact 数据分发模式**

将非镜像数据（数据库、策略、模块）以 OCI Artifact 格式分发，复用容器仓库基础设施。这种模式可推广到任何需要版本化分发的数据场景。

**4. 六阶段 Hook 生命周期**

`PreRun → PreScan → Scan → PostScan → PreReport → PostReport` 的生命周期设计，使得扩展可以在任意阶段介入。这种模式适用于任何需要"核心流程固定、扩展点灵活"的系统。

**5. Cache Key 基于内容哈希**

缓存键基于扫描目标的内容哈希（如容器层的 DiffID + 分析器版本），而非时间或名称。这保证了缓存的正确性，同时最大化命中率。

## 竞品交叉分析

| 维度 | Trivy | grype | osv-scanner | nuclei | Snyk |
|------|-------|-------|-------------|--------|------|
| **扫描目标** | 镜像/FS/Repo/K8s/VM | 镜像/FS | FS/Repo | URL/主机 | 镜像/FS/Repo/IaC |
| **扫描能力** | 漏洞+IaC+密钥+SBOM+许可证 | 仅漏洞 | 仅漏洞 | 漏洞模板 | 漏洞+IaC+密钥+许可证 |
| **漏洞数据源** | NVD+多OS发行版DB+GitHub Advisory | Grype DB | OSV 数据库 | 社区模板 | Snyk 私有 DB |
| **扩展机制** | WASM 模块+插件+Rego 策略 | 无 | 无 | YAML 模板 | 无 |
| **离线支持** | --skip-db-update | 支持 | 有限 | 支持 | 不支持 |
| **SBOM** | 生成+消费（双向） | 仅消费 | 无 | 无 | 仅生成 |
| **部署模式** | 单二进制/Client-Server | 单二进制 | 单二进制 | 单二进制 | SaaS+CLI |
| **语言覆盖** | 16+ 语言 | 10+ 语言 | 12+ 语言 | N/A | 10+ 语言 |
| **IaC 扫描** | Terraform/CF/Docker/Helm/K8s/Ansible/ARM | 无 | 无 | 有限 | Terraform/CF/Docker/K8s |
| **CI 集成** | GitHub Action + Operator | GitHub Action | GitHub Action | GitHub Action | 原生 CI 集成 |
| **许可证** | Apache-2.0 | Apache-2.0 | Apache-2.0 | MIT | 商业 |

### 综合竞争结论

1. **Trivy 的核心护城河是"全面性"**：在开源世界中，它是唯一同时覆盖漏洞扫描、IaC 错误配置、密钥扫描、SBOM 生成/消费和许可证检查的工具。grype 和 osv-scanner 聚焦漏洞扫描单一能力，nuclei 聚焦网络漏洞探测——它们在各自垂直领域可能更精深，但无法提供 Trivy 的一站式体验。

2. **生态嵌入度构成第二护城河**：作为 Harbor、GitLab、Azure Defender 的默认扫描器，Trivy 已经嵌入了云原生工具链的关键节点。这种嵌入式分发极难被替代。

3. **与 Snyk 的商业竞争维度不同**：Snyk 依赖私有漏洞数据库和 SaaS 模式，而 Trivy 的数据完全开放，支持离线部署。对于对数据主权敏感的企业（政府、金融、军工），Trivy 有天然优势。Snyk 的优势在于开发者体验和修复建议。

4. **WASM 模块化是差异化方向**：目前竞品中没有提供类似 WASM 沙箱化扩展的能力。这使得 Trivy 有潜力成为安全扫描的"平台"而非仅仅是"工具"。

5. **潜在风险**：Issue #3421（镜像扫描超时，111 comments）和 2026-03 trivy-action 供应链攻击事件说明，在大规模采用下，性能和安全供应链本身成为挑战。多目标支持带来的代码复杂度（128K+ 行 Go 代码）也增加了维护负担。

## 代码质量

### 质量检查清单

| 指标 | 数据 | 评价 |
|------|------|------|
| **测试文件数** | 625 个 `_test.go` 文件 | 优秀：测试覆盖面广 |
| **源码文件数** | 1,084 个非测试 Go 文件 | 测试/源码比 ≈ 0.58，说明重视测试 |
| **代码行数** | ~128,600 行 Go 代码（不含测试） | 大型项目，但结构清晰 |
| **依赖数量** | 514 行 go.mod（~779 依赖 in go.sum） | 依赖较多，但作为多目标扫描器可以接受 |
| **CI 工作流** | 22 个 GitHub Actions 工作流 | 完善：包含测试、集成测试、金丝雀构建、文档、发布等 |
| **集成测试** | 16 个集成测试文件 + e2e 目录 | 多层测试策略（单元→集成→e2e） |
| **Linter** | golangci-lint v2.10 | 严格的代码风格检查 |
| **跨平台测试** | ubuntu/windows/macos 矩阵 | 全平台覆盖 |
| **安全实践** | SECURITY.md + Private vulnerability reporting + zizmor.yml | 专业的安全响应流程 |
| **构建工具** | Mage（Go-native build tool） | 替代 Makefile，类型安全 |
| **发布流程** | release-please + goreleaser | 自动化语义版本 + 多平台二进制/Docker 发布 |
| **文档** | MkDocs 站点（trivy.dev） | 专业的在线文档 |
| **代码组织** | 清晰的 pkg/ + internal/ + cmd/ 分层 | 遵循 Go 项目标准布局 |
| **接口抽象** | analyzer/PostAnalyzer/Hook 三层接口 | 良好的抽象层次 |
| **错误处理** | xerrors.Errorf 包装 + 自定义错误类型 | 错误链完整，便于调试 |

**整体评价**：代码质量优秀。作为一个 128K+ 行的大型 Go 项目，Trivy 保持了清晰的分层架构、丰富的测试覆盖和专业的 CI/CD 流程。Analyzer 注册表模式使得代码高度模块化——624 个测试文件分布在各个 analyzer/scanner 包中，说明每个模块都有独立的测试。22 个 CI 工作流涵盖了从代码质量检查到跨平台测试到安全扫描的完整流水线。唯一的隐忧是依赖数量较多（514 行 go.mod），但这是多目标安全扫描器的固有复杂性。
