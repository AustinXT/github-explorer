# UI-TARS-desktop 网络分析报告

> 分析时间：2026-03-22
> 仓库：[bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)

---

## 仓库基本数据

| 指标 | 数值 |
|------|------|
| **名称** | UI-TARS-desktop |
| **描述** | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra |
| **Stars** | 28,981 |
| **Forks** | 2,835 |
| **Watchers** | 229 |
| **Issues（总计）** | 310 |
| **Pull Requests（总计）** | 54 |
| **License** | Apache-2.0 |
| **主要语言** | TypeScript (5.77M)，辅以 MDX (540K)、JavaScript (71K)、CSS (70K) |
| **磁盘大小** | ~192 MB |
| **创建时间** | 2025-01-19 |
| **最后推送** | 2026-03-10 |
| **是否存档** | 否 |
| **是否 Fork** | 否 |
| **官网** | https://agent-tars.com |
| **默认分支** | main |
| **社区健康度** | 87% |
| **Releases 总数** | 30 |
| **最新 Release** | v0.3.0（2025-11-04） |
| **Topics** | agent, vlm, vision, computer-use, mcp, mcp-server, gui-operator, browser-use, gui-agent, multimodal, tars, ui-tars, agent-tars, cowork |

**项目包含两个子产品：**
1. **Agent TARS** — 通用多模态 AI Agent 栈，CLI + Web UI 形态，通过 `npx @agent-tars/cli` 分发
2. **UI-TARS Desktop** — 基于 Electron 的本地 GUI Agent 桌面应用，驱动模型为 UI-TARS / Seed-1.5-VL/1.6

---

## 作者画像

### 组织：bytedance（字节跳动）

| 指标 | 数值 |
|------|------|
| **GitHub 登录名** | bytedance |
| **全名** | Bytedance Inc. |
| **所在地** | Singapore |
| **官网** | https://opensource.bytedance.com |
| **公开仓库数** | 401 |
| **Followers** | 15,829 |
| **注册时间** | 2013-04-15 |

字节跳动是全球头部互联网企业，旗下产品包括 TikTok、抖音、飞书等。该仓库由字节跳动 Seed 团队主导开发，Seed 是字节跳动的大模型研究部门。

### 核心贡献者

| 排名 | 用户名 | 提交数 | 身份/背景 |
|------|--------|--------|-----------|
| 1 | **[ulivz](https://github.com/ulivz)** | 677 | ByteDance Seed，Agent 方向，此前在 Web Infra、Alipay，1,910 followers |
| 2 | **[ycjcl868](https://github.com/ycjcl868)** (Charles) | 170 | ByteDance Seed，Agent Engineer / AI Infra / MLSys，杭州，1,378 followers |
| 3 | **[ZhaoHeh](https://github.com/ZhaoHeh)** | 77 | - |
| 4 | **[cjraft](https://github.com/cjraft)** | 53 | - |
| 5 | **[skychx](https://github.com/skychx)** | 35 | - |

核心贡献高度集中：ulivz 一人贡献 677 次提交，占主导地位（约 62%），前 5 人覆盖了绝大多数提交。社区贡献者约 30 人，但多数仅 1-2 次提交。

---

## 社区热度

### Star 增长趋势

- **总 Star 数**：28,981
- **仓库年龄**：~14 个月（2025-01 至 2026-03）
- **平均增速**：~2,070 stars/月
- **首批 Star 时间**：2025-01-21（仓库创建后 2 天即获关注）
- **早期增长**：创建当天 (2025-01-21) 即获 30+ stars，说明发布即有社区曝光

### 活跃度信号

| 信号 | 状态 |
|------|------|
| 最后提交时间 | 2026-03-10（12 天前） |
| 最后更新时间 | 2026-03-21（昨天） |
| Fork 活跃度 | 最新 fork 在 2026-03-21，说明仍有持续关注 |
| npm 月下载量 | @agent-tars/cli：~1,509 次/月（2026-02~03） |
| 社区文件 | CODE_OF_CONDUCT / CONTRIBUTING / PR_TEMPLATE / LICENSE 均齐全 |

### 热度评级：**极高**

近 2.9 万星，14 个月内达成，增长曲线陡峭。作为字节跳动 Seed 团队的旗舰开源项目，获得了大量关注。但 npm 月下载量仅 ~1,500，说明**关注度远大于实际使用量**，存在典型的"Star 多用户少"的现象。

---

## 生态网络

### 技术栈依赖

| 层级 | 技术 |
|------|------|
| 语言 | TypeScript |
| 包管理 | pnpm 9.10.0（双工作区架构） |
| 构建 | Turbo（根工作区）/ rslib / pdk（multimodal 工作区） |
| 测试 | vitest 3.2.4 |
| 桌面框架 | Electron |
| 协议 | MCP (Model Context Protocol) |
| AI 模型 | UI-TARS / Seed-1.5-VL/1.6 / 支持 Anthropic Claude、OpenAI GPT-4o、火山引擎 Doubao 等 |

### 关联项目

| 项目 | 关系 |
|------|------|
| [bytedance/UI-TARS](https://github.com/bytedance/UI-TARS) | 核心模型仓库（UI-TARS 模型本身） |
| [web-infra-dev/midscene](https://github.com/web-infra-dev/midscene) | 浏览器 GUI Agent（同团队生态） |
| [agent-infra/sandbox](https://github.com/agent-infra/sandbox) | AIO Agent 沙箱（隔离执行环境） |
| [ByteDance-Seed/UI-TARS-1.5-7B](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B) | HuggingFace 模型权重 |
| [ModelScope UI-TARS 集合](https://www.modelscope.cn/collections/UI-TARS-bccb56fa1ef640) | 国内模型平台 |

### npm 包生态

核心包 `@agent-tars/cli` 通过 npm 分发，基础设施包括：
- `@agent-infra/browser` — 浏览器自动化
- `@agent-infra/mcp-client` — MCP 协议客户端
- `@agent-infra/search` — 统一搜索接口
- `@ui-tars/sdk` — GUIAgent 和 Operator 基类

---

## 官方文档洞察

### 官网：https://agent-tars.com

官网提供完整文档体系：
- **快速开始**：https://agent-tars.com/guide/get-started/quick-start.html
- **CLI 文档**：https://agent-tars.com/guide/basic/cli.html
- **Web UI 文档**：https://agent-tars.com/guide/basic/web-ui.html
- **MCP 集成**：https://agent-tars.com/guide/basic/mcp.html
- **浏览器 Agent**：https://agent-tars.com/guide/basic/browser.html
- **API 参考**：https://agent-tars.com/api/
- **博客**：https://agent-tars.com/beta（介绍 Agent TARS Beta）

### 社交媒体

| 渠道 | 链接 |
|------|------|
| Discord | https://discord.gg/HnKcSBgTVx |
| Twitter/X | [@agent_tars](https://twitter.com/agent_tars) |
| 飞书群 | 有中文交流群 |
| DeepWiki | https://deepwiki.com/bytedance/UI-TARS-desktop |

### 核心论文

1. **UI-TARS (v1)**：[arXiv:2501.12326](https://arxiv.org/abs/2501.12326)（2025-01-21）
   - 标题：*UI-TARS: Pioneering Automated GUI Interaction with Native Agents*
   - 作者：Yujia Qin 及 34 位合作者（ByteDance Seed + 清华大学）
   - 关键贡献：增强感知、统一行动建模、System-2 推理、迭代训练
   - OSWorld 得分 24.6（超越 Claude 的 22.0），AndroidWorld 得分 46.6（超越 GPT-4o 的 34.5）

2. **UI-TARS-2**：[arXiv:2509.02544](https://arxiv.org/abs/2509.02544)（2025-09-05）
   - 标题：*UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning*
   - 关键突破：多轮强化学习、数据飞轮、混合 GUI 环境
   - OSWorld 得分 47.5，AndroidWorld 得分 73.3，大幅超越前代

---

## 竞品清单

### 开源竞品

| 项目 | Stars | 简介 | 语言 |
|------|-------|------|------|
| [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) | ~6K+ | 开源 ACI 框架，Agent S3 OSWorld 得分 72.6%（超越人类） | Python |
| [OpenCUA](https://opencua.xlang.ai/) | - | OpenCUA-72B 在 OSWorld-Verified 排名第一 | Python |
| [browser-use](https://github.com/browser-use/browser-use) | ~50K+ | 浏览器自动化 Agent，任务覆盖广 | Python |
| [Skyvern](https://github.com/Skyvern-AI/skyvern) | ~10K+ | 企业级浏览器自动化，高可靠性 | Python |
| [supernalintelligence/Awesome-Gui-Agents](https://github.com/supernalintelligence/Awesome-Gui-Agents) | - | GUI Agent 生态汇总 | - |

### 商业竞品

| 产品 | 厂商 | 简介 |
|------|------|------|
| **Claude Computer Use** | Anthropic | Claude 模型原生支持桌面操控 |
| **Nova Act** | Amazon | 2025 年发布，专为浏览器任务设计 |
| **Mariner** | Google | 基于 Gemini，Google I/O 2025 发布 |
| **Operator** | OpenAI | GPT 驱动的计算机操作 Agent |

### 差异化定位

UI-TARS-desktop 的独特优势：
1. **端到端自研模型**：不依赖第三方 LLM 的 prompt engineering，模型原生理解 GUI
2. **双产品线**：既有本地桌面应用（UI-TARS Desktop），又有 CLI/Web UI（Agent TARS）
3. **MCP 原生集成**：基于 MCP 协议扩展工具能力
4. **字节跳动资源**：Seed 团队的研发投入和持续迭代

---

## 关键 Issue 信号

### 热度最高的讨论

| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| [#268](https://github.com/bytedance/UI-TARS-desktop/issues/268) | Windows 平台支持 Agent TARS | 23 | Open | 社区对 Windows 支持需求强烈 |
| [#1058](https://github.com/bytedance/UI-TARS-desktop/pull/1058) | 运行时切换模型支持 | 23 | Closed | 灵活模型切换是核心需求 |
| [#591](https://github.com/bytedance/UI-TARS-desktop/issues/591) | 点击丢失 Bug | 19 | Open | GUI 操作精准性问题 |
| [#587](https://github.com/bytedance/UI-TARS-desktop/issues/587) | UI-TARS-2B 上下文长度错误 | 16 | Open | 小模型的上下文限制问题 |
| [#580](https://github.com/bytedance/UI-TARS-desktop/pull/580) | ADB Android 设备操作支持 | 15 | Open | 移动端自动化需求 |

### 近期 Issue 信号

| 类型 | 代表性 Issue | 解读 |
|------|-------------|------|
| **平台支持** | #1808 "请支持 Ubuntu" | 用户期望跨平台覆盖 |
| **模型下架** | #1802 "1.5 模型要下架"，#1840 "火山引擎 Doubao 模型下架" | 模型生态依赖问题，用户困惑 |
| **产品集成** | #1797 "接入飞书消息" | 企业场景集成需求 |
| **成本问题** | #1783 "CLI token 用量过高" | 实际使用成本是障碍 |
| **使用困难** | #1851 "请问这个咋用" | 产品易用性仍待提升 |

---

## 知识入口

| 来源 | 链接 | 说明 |
|------|------|------|
| **DeepWiki** | https://deepwiki.com/bytedance/UI-TARS-desktop | AI 驱动的代码库百科，提供架构和模块详解 |
| **官方文档** | https://agent-tars.com | 完整的快速开始、API 参考、博客 |
| **论文 v1** | https://arxiv.org/abs/2501.12326 | UI-TARS 原始论文 |
| **论文 v2** | https://arxiv.org/abs/2509.02544 | UI-TARS-2 技术报告（多轮 RL） |
| **HuggingFace** | https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B | 模型权重下载 |
| **ModelScope** | https://www.modelscope.cn/collections/UI-TARS-bccb56fa1ef640 | 国内模型平台 |
| **GitHub Discussion** | https://github.com/bytedance/UI-TARS-desktop/discussions/873 | Agent TARS CLI 介绍帖 |
| **第三方教程** | https://aicybr.com/blog/agent-tars-complete-setup-guide | Agent TARS 完整安装指南 |
| **分析文章** | https://serenitiesai.com/articles/ui-tars-bytedance-ai-agent-27k-stars | 27K Stars 分析 |

---

## 项目展示素材

### Banner 图

- `./images/tars.png` — Agent TARS 主 Banner

### Logo

- `./apps/ui-tars/resources/icon.png` — UI-TARS Desktop 应用图标

### 演示视频

| 场景 | 视频链接 |
|------|----------|
| Agent TARS 预订酒店 | https://github.com/user-attachments/assets/c9489936-afdc-4d12-adda-d4b90d2a869d |
| UI-TARS Desktop 本地操控 | https://github.com/user-attachments/assets/e0914ce9-ad33-494b-bdec-0c25c1b01a27 |
| 预订航班（主演示） | https://github.com/user-attachments/assets/772b0eef-aef7-4ab9-8cb0-9611820539d8 |
| MCP + 图表生成 | https://github.com/user-attachments/assets/a9fd72d0-01bb-4233-aa27-ca95194bbce9 |
| 远程操控演示 | https://github.com/user-attachments/assets/01e49b69-7070-46c8-b3e3-2aaaaec71800 |
| GitHub Issue 查询 | https://github.com/user-attachments/assets/3d159f54-d24a-4268-96c0-e149607e9199 |

### CLI 截图

- https://agent-tars.com/agent-tars-cli.png — Agent TARS CLI 界面

### 徽章

- TrendShift 徽章：https://trendshift.io/api/badge/repositories/13584

---

## 快速判断

### 一句话总结

**字节跳动 Seed 团队推出的多模态 GUI Agent 开源栈，集成自研视觉语言模型，提供桌面应用 + CLI 双形态，14 个月斩获近 2.9 万 Star，是当前 GUI Agent 领域最受关注的开源项目之一。**

### SWOT 分析

| | 正面 | 负面 |
|--|------|------|
| **内部** | **S 优势**：自研端到端模型（非 prompt wrapper）；字节跳动品牌与资源；双产品线覆盖 CLI/Desktop；MCP 协议集成；丰富的文档与论文支撑 | **W 劣势**：核心开发高度集中于 1-2 人；npm 实际使用量低（~1.5K/月 vs 29K Stars）；模型生态不稳定（火山引擎模型下架）；最后一次提交距今 12 天 |
| **外部** | **O 机会**：GUI Agent 赛道高速增长；MCP 生态扩展空间大；企业自动化需求旺盛；移动端（Android ADB）扩展 | **T 威胁**：Agent S3 在 OSWorld 已超人类水平；Anthropic/OpenAI/Google 等巨头入场；开源竞品（browser-use 50K+ Stars）增长迅猛 |

### 推荐关注度：⭐⭐⭐⭐⭐（5/5）

**理由**：
1. 赛道价值极高 — GUI Agent / Computer Use 是 2025-2026 年 AI Agent 领域最热赛道之一
2. 技术护城河 — 自研 UI-TARS 模型系列，从 v1 到 v2 持续在 benchmark 上领先
3. 工程完整度 — 不仅有模型，还有完整的桌面应用、CLI 工具、MCP 集成、SDK
4. 组织背书 — 字节跳动 Seed 团队持续投入，非个人/小团队项目
5. 需注意 — 实际采用率与 Star 数存在差距，模型依赖的稳定性是隐患
