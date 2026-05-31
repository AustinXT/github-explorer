# sherlock-project/sherlock — Phase 3: Content Analysis

## 动机与定位
- **要解决的问题**: 通过用户名在 400+ 社交平台上快速确认目标是否存在，解决渗透测试/安全研究中信息收集效率低下的问题
- **为什么现有方案不够**: 手动逐站搜索效率低下；依赖 API 的方案需要注册和维护 key，且受速率限制
- **目标用户**: 安全研究员、网络安全从业者、渗透测试人员、调查记者、社交媒体品牌管理者

## 作者视角

### 问题发现
- 起源：独立开发者 Siddharth Dushantha（冰岛）2018年创建
- 时机：2018年社交媒体爆发期，没有统一的 username OSINT 工具
- 痛点：渗透测试/安全研究中需要快速确认目标在各平台的存在性
- 现有方案不足：手动逐站搜索效率低下，无 API 方案依赖性太强

### 解法哲学
- **声明式 > 命令式**：站点定义全部在 JSON Manifest 中，核心代码只负责"检测逻辑"
- **社区驱动数据**：400+ 站点不靠团队维护，靠贡献者 PR 更新，代码和数据分离
- **简单 CLI 优先**：不追求 GUI 复杂功能，单一工具做精做透
- **明确不做**：不依赖 API key，不做需要注册的服务

### 背景知识迁移
- 从网络安全社区带来 HTTP 检测的专业知识（WAF 识别、响应分析）
- 融合并发编程模式（requests-futures）解决性能问题
- 借鉴配置驱动的设计哲学，降低社区贡献门槛

### 战略图景
- **非商业化**：纯开源 MIT，无 SaaS 化意图
- **生态定位**：成为 OSINT 工具链中的"信息收集"环节，不是终点
- **社区健康**：通过 CI 自动化降低贡献门槛，保证数据质量

## 架构与设计决策

### 目录结构概览
```
sherlock_project/
├── __init__.py          # 版本管理 + 包元数据
├── __main__.py          # 入口：Python版本检查 + 路由
├── sherlock.py          # 核心：并发检测逻辑 + CLI参数
├── sites.py             # 站点信息加载 + exclusions机制
├── notify.py            # 通知系统：QueryNotify抽象类
├── result.py            # 结果类型：QueryStatus枚举 + QueryResult
└── resources/
    ├── data.json        # 400+站点定义（核心数据资产）
    └── data.schema.json # JSON Schema验证

.github/workflows/       # CI/CD（数据验证 + 回归测试）
tests/                   # 单元测试（manifest/probes/ux）
devel/                   # 开发工具（站点列表生成器）
```

**分层逻辑**：
- **数据层**：data.json（站点定义，外部可编辑）
- **逻辑层**：sherlock.py（检测算法，与数据解耦）
- **接口层**：notify.py（输出抽象，支持多种格式）
- **工具层**：sites.py（数据加载 + 过滤规则）

### 关键设计决策

**决策1: JSON Manifest 站点定义系统**
- 问题: 如何让非开发者也能贡献新站点？
- 方案: 将站点配置抽离为 data.json，包含 url/errorType/errorMsg 等字段
- Trade-off: 牺牲了复杂检测逻辑的灵活性，换取了极低的贡献门槛
- 可迁移性: 高（任何需要"配置驱动行为"的工具都适用）

**决策2: 异步并发检测引擎（requests-futures）**
- 问题: 400+ 站点的串行检测太慢
- 方案: SherlockFuturesSession 扩展 requests-futures，20个 worker 并发
- Trade-off: 引入 HTTP 错误处理复杂性，换取了 10-20x 性能提升
- 可迁移性: 高（批量 API 调用场景均可复用）

**决策3: 多模式错误检测**
- 问题: 不同站点的"用户不存在"信号各异
- 方案: 三种检测模式——status_code（状态码）/ message（错误文本）/ response_url（重定向 URL）
- Trade-off: 每个站点需要独立配置，换取高准确率
- 可迁移性: 中（需配合领域知识）

**决策4: False Positive 排除系统**
- 问题: 检测误报（站点变更但代码未更新）
- 方案:
  - 远程 exclusions 文件（https://data.sherlockproject.xyz/exclusions）
  - CI 自动化验证 PR 修改的站点
  - WAF 指纹黑名单（Cloudflare/PerimeterX 等）
- Trade-off: 维护成本增加，换取结果可信度
- 可迁移性: 高（任何依赖外部数据的工具都适用）

**决策5: 进度通知抽象（QueryNotify）**
- 问题: 如何支持多种输出格式（终端/Debug/API）？
- 方案: 基类 QueryNotify + 子类 QueryNotifyPrint，start/update/finish 三阶段
- Trade-off: 接口略微复杂，换取极强扩展性
- 可迁移性: 高（CLI 工具的通用模式）

## 创新点

1. **WAF 指纹检测**
   - 描述: 内置 WAF（Cloudflare/PerimeterX/AWS）特征识别，检测被拦截的请求
   - 新颖度: 3/5 | 实用性: 4/5 | 可迁移性: 4/5
   - 适用场景: 反爬虫/安全检测工具的规避识别

2. **远程 Manifest + Exclusion 机制**
   - 描述: 数据与代码分离，支持热更新站点列表而不发版
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 5/5
   - 适用场景: 需要持续更新数据源的工具（威胁情报/OSINT）

3. **多用户名变体检测**
   - 描述: 支持 {?} 占位符，自动生成 username_{-.} 三种变体
   - 新颖度: 2/5 | 实用性: 4/5 | 可迁移性: 3/5
   - 适用场景: 社会工程学用户名猜测

4. **CI 驱动的站点贡献质量保证**
   - 描述: PR 修改 data.json 时自动运行验证测试，评论结果到 Issue
   - 新颖度: 3/5 | 实用性: 5/5 | 可迁移性: 4/5
   - 适用场景: 数据密集型开源项目的贡献质量管理

## 可复用模式

1. **并发 HTTP 客户端封装**: `SherlockFuturesSession` 扩展模式 — 适用场景: 批量 API 调用、爬虫、性能敏感的 HTTP 客户端
2. **声明式配置驱动**: JSON Schema + 动态加载 — 适用场景: 插件系统、规则引擎、配置即代码
3. **三阶段通知系统**: start/update/finish 抽象 — 适用场景: 长时间运行任务的进度展示
4. **False Positive 排除链**: 远程规则 + 本地覆盖 + WAF 指纹 — 适用场景: 数据质量要求高的检测工具
5. **PR 自动化测试**: 变更检测 + 针对性测试 + 结果汇总 — 适用场景: 大型配置文件的协同维护

## 竞品交叉分析

### vs soxoj/maigret

- **我们更好**:
  - False Positive 处理更成熟（WAF 指纹 + exclusions）
  - 社区更活跃，维护响应快
  - 架构更清晰，代码量适中易维护
- **竞品更好**:
  - 站点覆盖量更大（3000+ vs 400+）
  - 社区贡献数据更丰富
- **不同目标**:
  - Sherlock: 精确度优先，轻量级
  - maigret: 覆盖度优先，适合深度 OSINT
- **用户迁移成本**: 中等（CLI 参数兼容但数据源不同）

### vs mxrch/GHunt

- **我们更好**:
  - 覆盖所有社交平台，不限 Google 生态
  - 独立于平台 API（无需 key）
- **竞品更好**:
  - Google 生态内的检测更准确（利用 Google 服务）
  - GHunt 专注于 Gmail/YouTube 等 Google 资产
- **不同目标**:
  - Sherlock: 通用跨平台搜索
  - GHunt: Google 特定资产分析
- **用户迁移成本**: 高（功能定位不同）

### 综合竞争结论

- **差异化护城河**: 站点定义系统的易用性 + False Positive 处理成熟度
- **竞争风险**: maigret 的覆盖度优势可能在深度 OSINT 场景中替代 Sherlock
- **生态定位**: OSINT 工具链的"快速扫描"环节，与专业深度工具互补

## 代码质量

| 维度 | 评级 | 说明 |
|------|------|------|
| 代码质量 | 优秀 | 清晰的模块划分，类型提示完整，错误处理规范 |
| 文档质量 | 良好 | README 完整，docs/ 有贡献指南，但缺架构文档 |
| 测试覆盖 | 充分 | CI 三平台测试（Linux/Windows/macOS），pytest 套件 |
| CI/CD | 完善 | lint + 回归测试 + Docker 构建 + 数据验证 |
| 错误处理 | 规范 | 异常分类清晰（HTTP/Proxy/Timeout），上下文丰富 |

### 质量检查清单

- [x] 有测试（pytest 套件）
- [x] 有 CI/CD 配置（GitHub Actions）
- [x] 有文档（README + docs/）
- [x] 错误处理规范（requests 异常分类）
- [x] 有 linter 配置（tox）
- [x] 有 CHANGELOG（releases）
- [x] 有 LICENSE（MIT）
- [x] 有示例代码（README Usage）
- [x] 依赖版本锁定（pyproject.toml）