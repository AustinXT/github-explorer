# sandbox-runtime 深度分析报告

> GitHub: https://github.com/anthropic-experimental/sandbox-runtime

## 一句话总结

Anthropic 为 Claude Code 打造的 OS 级轻量进程沙箱——用 macOS Seatbelt + Linux bubblewrap/seccomp 而非容器实现文件系统和网络双重隔离，将权限提示减少 84%，是 AI Agent 安全领域的范式创新。

## 值得关注的理由

1. **完全不同的沙箱范式**：唯一不依赖 Docker/VM 的主流 AI 沙箱方案，用 OS 原语（Seatbelt/bwrap/seccomp-BPF）实现零延迟进程包装，代码继续在用户本地文件系统上直接操作
2. **安全工程的教科书**：3,675 行源码 + 6,362 行测试（1.87:1 测试比），域名通配符验证、symlink 边界检查、文件移动攻击防护、两阶段 seccomp 应用——每个细节都从攻击者视角思考
3. **Anthropic 官方 AI 安全基础设施**：Claude Code 的内置安全层，npm 月下载 19 万，吸引了 Bun 创始人和 Electron 维护者贡献，代表了 AI Agent 安全的最佳实践方向

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | https://github.com/anthropic-experimental/sandbox-runtime |
| Star / Fork | 3,492 / 225 |
| 代码行数 | 15,686 行（TypeScript，源码 3,675 行 + 测试 6,362 行 + C 195 行） |
| 项目年龄 | 5 个月（创建 2025-10-20） |
| 开发阶段 | 早期活跃（v0.0.42，Beta Research Preview，1.5 commit/天） |
| 贡献模式 | 双核心驱动（ollie-anthropic 42% + ddworken 37%，23 位贡献者） |
| 热度定位 | 中等热度 / 快速增长（3.5K stars，月均增长 300-400） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[优秀] |

## 作者视角：为什么存在这个项目

### 创始人/作者背景

Anthropic 官方实验性项目组织（anthropic-experimental），仅 3 个公开仓库。核心开发者 ollie-anthropic（92 commits）和 ddworken（David Dworken，82 commits）为 Anthropic 员工。项目已吸引 Bun 创始人 Jarred-Sumner、Electron 维护者 MarshallOfSound 等知名开源开发者贡献，说明在基础设施社区有技术影响力。

### 问题判断

Anthropic 团队在构建 Claude Code 时面临一个实际悖论：AI Agent 需要执行 shell 命令才有用，但每个命令都可能读取 `~/.ssh/id_rsa` 或向外部泄露数据。传统「每次提示用户确认」方案导致交互疲劳（审批疲劳），用户习惯性点「允许」，安全形同虚设。

关键洞察：**文件系统和网络隔离必须同时存在**——仅有文件隔离，恶意代码可通过网络传出；仅有网络隔离，可读密钥等待日后泄露。

### 解法哲学

**「OS 原语而非容器化」**——三层实现：
- macOS：`sandbox-exec` + 动态生成 Seatbelt 配置（借鉴 Chrome 沙箱策略）
- Linux：`bubblewrap` 命名空间隔离 + `seccomp-BPF` 系统调用过滤
- 网络：HTTP/SOCKS5 代理在应用层做域名白名单过滤（比 iptables 更灵活）

核心理念：**「命令包装」而非「环境隔离」**——`srt 「npm install」` 和直接 `npm install` 在同一文件系统上操作，用户工作流完全透明。

### 战略意图

srt 是 Claude Code 商业化的关键基础设施。开源目的多重：信任建设（让用户看到安全实现）、生态杠杆（MCP 服务器沙箱标准化）、安全研究贡献（Research Preview 邀请社区改进）。

## 核心价值提炼

### 创新之处

1. **OS 原语沙箱在 AI Agent 场景的首次系统化应用**（新颖度 5/5 | 实用性 5/5 | 可迁移性 3/5）
   将浏览器沙箱技术（Seatbelt、seccomp-BPF）移植到 AI Agent 安全领域。零延迟进程包装，代码直接操作本地文件系统，与容器方案的体验差距是本质性的。

2. **两阶段 seccomp 应用**（新颖度 5/5 | 实用性 4/5 | 可迁移性 3/5）
   Linux 网络隔离需要 socat 使用 Unix socket，但用户命令不应有此能力。解决方案：先启动 socat，再通过 `apply-seccomp` C 程序施加 BPF 过滤器后 exec 用户命令。不到 100 行 C 代码实现的精巧工程取舍。

3. **代理驱动的域名级网络过滤**（新颖度 4/5 | 实用性 5/5 | 可迁移性 4/5）
   不用 iptables IP 级过滤，而是 HTTP/SOCKS5 代理做域名白名单。策略写成 `allowedDomains: [「github.com」, 「*.npmjs.org」]` 而非 IP 列表。

4. **文件移动攻击防护**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）
   `generateMoveBlockingRules()` 不仅阻止直接写入受保护文件，还阻止通过 `mv`/`rename` 移动祖先目录来间接绕过保护。

5. **`control-fd` 动态配置更新协议**（新颖度 4/5 | 实用性 4/5 | 可迁移性 4/5）
   通过文件描述符接收 JSON Lines 格式的运行时配置更新，让 Claude Code 可以动态调整沙箱策略（如用户授权新域名），无需重启。

### 可复用的模式与技巧

1. **Zod Schema 驱动的安全配置验证**：域名通配符验证器拒绝 `*.com` 等过宽模式，将安全策略编码到类型系统
2. **平台适配器模式**：SandboxManager 通过 `getPlatform()` 分发到 macOS/Linux 独立实现，接口一致但内部完全不同
3. **代理环境变量全覆盖列表**：HTTP_PROXY、GIT_SSH_COMMAND、DOCKER_*_PROXY、GRPC_PROXY 等 20+ 工具的代理配置——宝贵的经验总结
4. **环形缓冲区违规存储**：64 行实现，保留最近 100 条违规事件 + 订阅通知
5. **Symlink 边界检查**：`isSymlinkOutsideBoundary` 防止符号链接扩大沙箱边界，特别处理 macOS `/tmp` → `/private/tmp`
6. **不对称文件系统权限模型**：读取 deny-then-allow（方便「禁止全部但放行工作目录」），写入 allow-only + denyWrite 覆盖（方便「允许写但保护 .env」）

### 关键设计决策

1. **OS 原语 vs 容器**：零延迟 + 直接文件系统访问 vs 更薄的安全边界。对本地 IDE/CLI Agent 场景是唯一可行方案。
2. **Mandatory Deny Paths 不可取消**：`.bashrc`、`.gitconfig`、`.git/hooks`、`.mcp.json` 等永远不可写——纵深防御，防止持久化攻击。
3. **SandboxManager 模块级单例**：整个进程只有一个沙箱上下文，代理服务器持续运行服务多个子命令，`updateConfig()` 动态更新策略。
4. **动态生成 Seatbelt 配置**：每次命令执行根据当前策略生成完整的 macOS 沙箱配置，含唯一 logTag 用于违规追踪。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | srt | Daytona | E2B | OpenSandbox |
|------|-----|---------|-----|-------------|
| 隔离技术 | OS 原语 | Docker | Firecracker microVM | Docker/K8s |
| 部署位置 | 本地 | 云端 | 云端 SaaS | 私有云 |
| 启动延迟 | ~0ms | 秒级 | 毫秒级 | 秒级 |
| 文件系统 | 直接本地访问 | 复制到容器 | 复制到 VM | 复制到容器 |
| 网络控制 | 域名级白名单 | 容器网络策略 | VM 网络策略 | K8s NetworkPolicy |
| 离线可用 | 完全 | 需云连接 | 需云连接 | 需集群 |
| Stars | 3.5K | 69K | 11K | 9K |

### 差异化护城河

- **架构范式不同**：不是「更轻的容器」而是「完全不同的隔离方式」——OS 原语的零延迟和本地文件系统直接访问是容器方案无法复制的
- **跨平台安全策略**：macOS Seatbelt 配置生成 893 行 + Linux bwrap 构建 1,190 行，覆盖了 Mach IPC/IOKit/sysctl 等多个子系统的精确白名单
- **Claude Code 深度集成**：作为官方内置组件，有最大的分发渠道和用户反馈回路

### 竞争风险

srt 与 Daytona/E2B 不在同一竞争维度——前者解决「本地 Agent 安全」，后者解决「云端代码执行安全」，互为补充。真正的风险是 OS 原语的安全边界比容器/VM 更薄——macOS `sandbox-exec` 的未来行为变化可能影响稳定性。

### 生态定位

填补了「本地开发环境下的轻量 AI Agent 进程沙箱」的市场空白。随着 Claude Code 用户增长和 MCP 生态扩展，有潜力成为本地 AI Agent 安全的事实标准。

## 套利机会分析

- **信息差**: 中等。3.5K stars 但 npm 月下载 19 万（因 Claude Code 捆绑），实际使用量远超 star 体现。OS 原语沙箱的技术路线在 AI 安全社区中被低估。
- **技术借鉴**: 两阶段 seccomp 应用、动态 Seatbelt 配置生成、代理驱动域名过滤、文件移动攻击防护——这些安全工程模式可迁移到任何需要进程级安全边界的项目。
- **生态位**: 「本地 AI Agent 安全」是一个新兴且快速增长的需求。随着更多 AI IDE 和 Agent 工具出现，srt 的架构范式可能被广泛采纳。
- **趋势判断**: AI Agent 安全是刚需。srt 的「Research Preview」标签意味着 Anthropic 可能会推出正式版和付费企业方案。

## 风险与不足

1. **仍为 Beta（v0.0.42）**：API 和配置格式可能频繁变化，不建议在关键生产系统中独立依赖
2. **dotfile 泄漏安全缺陷**（#139，18 评论，仍 open）：进程被 SIGKILL 时泄漏 dotfiles
3. **macOS sandbox-exec 未来不确定性**：Apple 已标记 `sandbox-exec` 为非公开 API，未来 macOS 版本可能改变行为
4. **Linux 代理依赖 HTTP_PROXY 环境变量**：不遵循该变量的程序会绕过网络过滤（已知限制）
5. **社区健康度 37%**：缺少 CONTRIBUTING、CODE_OF_CONDUCT，PR 积压明显（29 个 open PR）
6. **OS 安全边界比容器薄**：OS 原语可能存在未知漏洞，提供的隔离保证弱于容器/VM

## 行动建议

- **如果你要用它**: 最佳使用方式是通过 Claude Code 自动启用（已内置）。独立使用时 `npm i -g @anthropic-ai/sandbox-runtime && srt 「your-command」` 即可。特别适合包裹 MCP 服务器限制其权限。注意仍是 Beta，安全边界有已知限制。
- **如果你要学它**: 重点关注 `src/sandbox/sandbox-manager.ts`（1,014 行，核心调度）、`src/sandbox/macos-sandbox-utils.ts`（893 行，Seatbelt 配置生成——借鉴 Chrome 沙箱策略的精彩实现）、`vendor/seccomp-src/`（195 行 C，两阶段 seccomp 的极简实现）。配合 Anthropic 工程博客一起阅读效果最佳。
- **如果你要 fork 它**: (1) 修复 #139 dotfile 泄漏问题；(2) 添加 Windows 原生支持（当前仅 WSL2）；(3) 实现 TTY 交互式终端支持（#77）；(4) 探索替代 macOS sandbox-exec 的方案（如 EndpointSecurity 框架）。

### 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | https://deepwiki.com/anthropic-experimental/sandbox-runtime |
| Zread.ai | 未收录 |
| 关联论文 | 无 |
| Anthropic 工程博客 | [Beyond Permission Prompts: Making Claude Code More Secure](https://www.anthropic.com/engineering/claude-code-sandboxing) |
