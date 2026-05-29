# Union — 零知识证明驱动的跨链互操作性协议

> GitHub: https://github.com/unionlabs/union
> 官网: https://union.build
> 分析时间: 2026-04-06

---

## 项目概览

Union 是一个**零知识证明驱动的跨链互操作性协议**，采用独特的「共识验证」（Consensus Verification）技术路线，通过 zk-SNARKs 实现无需第三方信任的跨链消息传递。

- **Star**: 74,168 | **Fork**: 3,871 | **Watcher**: 1,606
- **License**: Apache-2.0
- **创建**: 2023-05-16 | **最近更新**: 2026-04-01

---

## 核心创新

Union 的核心创新在于将 **BLS 签名聚合** 与 **零知识证明** 结合，创造出一种新型的跨链验证机制：

```
传统跨链桥: 多签 / MPC / Oracle → 信任假设
Union: ZK 证明验证 BLS 聚合签名 → 密码学保证
```

**关键差异化**:
- 无需信任第三方、预言机、多签或 MPC
- 纯密码学安全保证
- 常数时间验证 (无论验证者数量)

---

## 技术架构

### 组件矩阵

| 组件 | 语言 | 用途 |
|------|------|------|
| **uniond** | Go | 区块链节点 (Cosmos SDK + CometBLS) |
| **galoisd** | Go + Gnark | ZK 证明器 (Groth16 + BN254) |
| **voyager** | Rust | 跨链中继器 (FSM + PostgreSQL) |
| **cosmwasm** | Rust | CosmWasm 智能合约栈 |
| **evm** | Solidity | EVM 智能合约栈 |
| **ts-sdk** | TypeScript | 开发者 SDK |

### 代码规模

- **总计**: ~745K 行 (含注释和空行)，~648K 行纯代码
- **Rust**: 52.8% (406,923 行) — 核心协议、轻客户端、中继器
- **TypeScript**: 7.5% (57,647 行) — SDK、前端应用、网站
- **Solidity**: 3.4% (25,968 行) — EVM 智能合约
- **Go**: 1.9% (14,683 行) — 区块链节点
- **其他**: Cairo、Svelte、Nix 等

---

## 密码学设计

### CometBLS 共识机制

Union 扩展了 Tendermint 共识，增加 BLS 签名聚合和 ZK 证明验证：

```
区块产生 → 验证者 BLS 签名 → 签名聚合 → ZK 证明生成 → 区块头构造 → ZK 验证
```

**验证流程**:
1. 检查区块头高度和时间戳
2. 验证 Groth16 ZK 证明 (配对检查)
3. 验证 BLS 承诺
4. 更新共识状态

### 轻客户端实现

Union 实现了 **20+ 个轻客户端**，支持多条区块链:

| 客户端类型 | 代表实现 |
|-----------|---------|
| Cosmos 生态 | CometBLS、Tendermint |
| EVM 链 | Ethereum、Arbitrum、Base、Berachain |
| Alt VM | StarkNet (Cairo)、Sui (Move)、Aptos (Move) |
| 证明透镜 | State-lens-ics23 (MPT/SMT)、Proof-lens |

---

## Voyager 中继器

Voyager 是 Union 的跨链中继器，采用独特的**无状态状态机**设计:

**核心特性**:
- **有限状态机** (voyager-vm) — 所有操作建模为状态转换
- **事务性队列** (pg-queue) — PostgreSQL 保证原子性
- **无状态设计** — 崩溃后秒级恢复

**解决的中继器三大问题**:
1. **速度**: 并行处理多个消息
2. **数据完整性**: 事务保证不丢包
3. **快速启动**: 状态完全存储在 DB

---

## 支持的区块链

**主网**: Ethereum、Arbitrum、Base、Berachain、BSC、Osmosis、Sei、Union、Xion

**测试网**: Sepolia、Arbitrum Sepolia、Berachain、Bob、Corn、Osmosis、Sui、Xion

---

## 开发者体验

### 构建系统

Union 使用 **Nix Flake** 实现可重现构建:

```bash
# 构建任意组件
nix build .#uniond
nix build .#voyager
nix build .#galoisd

# 进入开发环境
nix develop

# 预提交检查
nix run .#pre-commit
```

### TypeScript SDK

`@unionlabs/sdk` 提供:
- 跨链交易创建
- 批处理支持
- 多链 ABI 管理
- EIP-1193 提供者集成

---

## 竞争格局

### 技术路线对比

| 项目 | 技术路线 | 信任假设 | 优势 | 劣势 |
|------|---------|---------|------|------|
| **Union** | ZK + Consensus | 最小 | 密码学保证 | 复杂度高 |
| **Succinct/SP1** | 通用 ZK | 最小 | 通用性强 | 性能开销 |
| **LayerZero** | Light Client + Oracle | 中等 | 简单 | 依赖 Oracle |
| **Wormhole** | Guardian 多签 | 高 | 简单 | 19/19 多签风险 |
| **Polymer** | IBC 扩展 | 最小 | Cosmos 兼容 | 仅 IBC |

### 差异化优势

1. **ZK + IBC**: 唯一同时支持两者的协议
2. **Subsecond Messaging**: 声称首个亚秒级跨链消息
3. **全链支持**: EVM/SVM/altVM 原生支持

---

## 团队与社区

- **组织**: Union Labs (美国)
- **开发模式**: 小团队协作 — Top 7 贡献者合计 ~14,289 次提交
- **GitHub 粉丝**: 5,411
- **公开仓库**: 57

**核心贡献者**:
- `cor`: 3,355 次贡献
- `benluelo`: 2,625 次贡献
- `hussein-aitlahcen`: 2,003 次贡献

---

## 项目成熟度

### 生命周期阶段

**判断**: 成长期 → 稳定期过渡

- ✅ 代码库规模大，功能完整
- ✅ 多语言实现显示生态野心
- ⚠️ 近期提交频率下降 (2025 年多周为 0)
- ✅ 有完善的文档和 SDK
- ✅ 支持多条主网和测试网

### 企业化程度

- ✅ Nix 可重现构建
- ✅ 独立的 `audits/` 仓库
- ✅ 专业的前端/后端分离
- ✅ TypeScript SDK

---

## 潜在风险

### 技术风险

1. **ZK 电路安全** — Groth16 电路漏洞风险、可信设置依赖
2. **系统复杂度** — 8+ 语言增加攻击面
3. **经济安全** — PoA 阶段中心化风险，PoS 迁移未完成

### 竞争风险

1. **Succinct/SP1**: $55M 融资，通用 ZK 基础设施
2. **Polymer**: Cosmos 生态深度整合
3. **Lagrange**: 与 Polymer 合作，ZK + IBC

---

## 应用场景

- **DeFi 协议**: 跨链流动性、借贷、交易
- **MEV 搜索者**: 需要运行 galoisd 获取优势
- **IBC Relayers**: 使用 voyager 提高效率
- **跨链 DApp**: 通过 TypeScript SDK 集成

---

## 快速判断

### 技术价值
- **创新性**: ⭐⭐⭐⭐⭐ (Consensus Verification 独特路线)
- **完整性**: ⭐⭐⭐⭐⭐ (端到端解决方案)
- **工程化**: ⭐⭐⭐⭐ (Nix 构建，多语言分离)
- **安全性**: ⭐⭐⭐⭐ (密码学保证，但审计报告未公开)

### 商业价值
- **市场需求**: ⭐⭐⭐⭐⭐ (跨链是 DeFi 核心痛点)
- **竞争地位**: ⭐⭐⭐⭐ (第一梯队，差异化明显)
- **可持续性**: ⭐⭐⭐ (依赖融资和 PoS 迁移)

---

## 知识入口

- **官方文档**: https://docs.union.build
- **Zread.ai**: 有详细的架构文档 (CometBLS、Galoisd、Voyager 等)
- **Discord**: https://discord.union.build

---

**总结**: Union 是技术密度极高的跨链基础设施项目，采用独特的 ZK + Consensus Verification 路线，在众多跨链桥方案中差异化明显。虽然面临激烈竞争和技术复杂度挑战，但其密码学保证和全链支持使其成为值得关注的重要玩家。
