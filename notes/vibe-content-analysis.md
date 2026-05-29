# Vibe 内容分析笔记

## 项目结构
```
/tmp/repo-miner-vibe/
├── .github/workflows/release.yml  # CI/CD: 自动构建和发布
├── src/
│   ├── main.rs          # 核心实现 (~1,331 行)
│   ├── provision.sh     # VM 初始配置脚本 (85 行)
│   └── entitlements.plist  # macOS 虚拟化权限声明
├── build.rs             # 构建脚本 (注入 git SHA 和构建日期)
├── Cargo.toml           # Rust 项目配置
├── Cargo.lock           # 依赖锁定
├── LICENSE              # MIT
├── readme.md            # 详尽的项目文档
└── .gitignore           # 仅排除 /target
```

## 技术架构

### 核心依赖
- **objc2 / objc2-foundation / objc2-virtualization**: Objective-C 互操作，直接调用 Apple Virtualization Framework
- **block2 / dispatch2**: Apple GCD 和 block 机制的 Rust 绑定
- **libc**: POSIX 系统调用
- **lexopt**: 轻量 CLI 参数解析器

### 架构分层
1. **CLI 解析层** (parse_cli): 解析命令行参数，支持 --mount, --script, --send, --expect 等
2. **磁盘管理层** (ensure_base_image, ensure_default_image, ensure_instance_disk):
   - 下载 Debian nocloud ARM64 镜像
   - SHA-512 校验
   - 解压、配置 provision、创建实例副本 (COW on APFS)
3. **VM 配置层** (create_vm_configuration):
   - VZGenericPlatformConfiguration (ARM)
   - VZEFIBootLoader
   - VirtioFS 目录共享
   - Virtio 网络 (NAT)
   - 串口控制台 (hvc0 主控制台 + hvc1 resize 通道)
4. **IO 复用层** (spawn_vm_io, IoContext):
   - stdin -> VM (通过 mpsc channel + poll)
   - VM output -> stdout + OutputMonitor
   - 终端大小变化 -> VM resize 通道
   - wakeup pipe 实现优雅关闭
5. **登录动作层** (spawn_login_actions_thread):
   - Expect/Send/Script 三种动作类型
   - 自动登录 root
   - 配置终端 (stty sane, raw mode)
   - 挂载共享目录 (virtiofs + bind mount)
   - 显示 MOTD 表格

### 关键设计决策
1. **单文件实现**: 整个项目仅 main.rs 一个 Rust 文件，约 1,331 行
2. **直接使用 Apple Virtualization Framework**: 通过 objc2 crate 直接调用，避免中间层
3. **Debian nocloud 镜像**: 直接 root 登录，无 cloud-init 延迟
4. **VirtioFS 目录共享**: 比 QEMU 的 9p 快数百倍
5. **自动 codesign**: 检测并自签名虚拟化 entitlement，然后 exec 替换自身
6. **COW 磁盘**: 利用 APFS COW 特性，20GB 虚拟磁盘仅占用 ~2.5GB 实际空间
7. **tmpfs 遮罩**: 在 VM 内用 tmpfs 挂载 .git/.vibe 目录，阻止 agent 访问

### provision.sh 预装工具
- build-essential, pkg-config, libssl-dev, curl, git, ripgrep
- Rust (rustup minimal profile + rustfmt + clippy)
- mise-en-place (多语言版本管理)
- 通过 mise: uv, node, codex, claude-code, gemini-cli

### CI/CD
- GitHub Actions: main 分支推送时自动构建
- 双重发布: 日期-SHA 版本 + latest 滚动版本
- 产物: vibe-macos-arm64.zip

## 代码质量观察
- 无测试代码
- 注释少但关键位置有说明
- unsafe 块集中在 Objective-C 互操作和 libc 调用（必要的 unsafe）
- 错误处理使用 Box<dyn Error> 统一处理
- README 极为详尽，包含设计理由、替代方案比较、Roadmap
