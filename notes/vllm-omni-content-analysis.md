# vllm-omni — Phase 3 内容分析（What & How）

## 动机与定位

### 核心问题

vLLM 是 LLM 推理的事实标准（75K stars），但它只解决了 AI 推理的一半问题——**自回归文本生成**。当今前沿模型正在走向「全模态」：Qwen3-Omni 接收文本/图像/音频/视频输入，输出文本+语音；BAGEL 接收多模态输入，输出文本+图像；FLUX/Wan 通过扩散模型生成图像/视频。这些模型的推理需求与纯文本 LLM 有根本区别：

1. **架构异构**：AR（自回归）+ DiT（扩散 Transformer）+ CNN（音频合成）等不同架构组合
2. **流水线多阶段**：一个请求需要经历 Thinker(AR) -> Talker(AR) -> Code2Wav(卷积) 等多个阶段
3. **输出多模态**：不仅是文本 token，还有图像像素、音频波形、视频帧

vLLM 的 KV Cache 管理、PagedAttention 等核心优化都是为单阶段自回归设计的，无法直接处理这种异构多阶段流水线。

### 定位

vLLM-Omni 的定位是：**在 vLLM 的地基上，构建全模态推理的统一编排层**。它不是 vLLM 的竞争者，而是 vLLM 向全模态推理的官方延伸（由 vLLM 社区在 2025 年 11 月正式发布）。

论文标题「Fully Disaggregated Serving for Any-to-Any Multimodal Models」精准概括了核心创新：通过「完全解耦」的阶段执行，实现任意模态到任意模态的高效推理。

---

## 作者视角

### 问题发现：为什么 vLLM 需要一个 Omni 分支？

团队来自华为（香港/深圳），在大规模 AI 基础设施部署中最先遇到了实际痛点：当 Qwen-Omni、BAGEL 等全模态模型上线时，现有推理框架（vLLM、SGLang、TensorRT-LLM）全部失灵——它们只能处理文本输入/输出的自回归生成，无法编排 AR+DiT+TTS 的多阶段流水线。

### 解法哲学：Stage 抽象 + 完全解耦

解决方案的核心思想是 **「Stage 抽象」**——将一个全模态模型的推理分解为若干个 Stage，每个 Stage 有独立的执行后端（可以是 vLLM 的 AR 引擎，也可以是全新的 Diffusion 引擎），Stage 之间通过 OmniConnector 传递数据。

这个设计有明显的华为系统工程思维：不追求单点最优，而是追求 **可组合性**。任何新模态、新架构，只需实现一个新的 Stage 即可插入流水线。

### 背景知识迁移

从 vLLM 继承了：
- PagedAttention 和 KV Cache 管理（用于 AR 阶段）
- 调度器框架（OmniARScheduler 继承 vLLM Scheduler）
- Worker/ModelRunner 架构（GPUARWorker 继承 vLLM GPUWorker）
- 分布式通信框架（TP/PP/DP）
- OpenAI 兼容 API 层的基础架构

新增了：
- Diffusion 引擎（完全独立实现，80K+ 行代码）
- Orchestrator 编排器（多阶段流水线的核心大脑）
- OmniConnector（跨阶段数据传输抽象）
- Stage Config YAML 体系（声明式流水线定义）
- CFG Companion 机制（跨阶段 Classifier-Free Guidance）
- Async Chunk 流水线重叠执行

### 战略图景

在 AI 推理基础设施的版图中，vLLM-Omni 占据了一个独特的生态位：

```
文本推理: vLLM / SGLang / TensorRT-LLM
图像生成: Diffusers / ComfyUI
全模态推理: vLLM-Omni ← 唯一统一 LLM+Diffusion+TTS+多阶段 pipeline 的开源项目
```

这不是增量改进，而是开辟了一个新类别。

---

## 架构与设计决策

### 整体架构

```
用户请求
  ↓
Omni / AsyncOmni（入口点）
  ↓
AsyncOmniEngine（引擎代理，主线程）
  ↓ janus 队列
Orchestrator（后台线程，事件循环）
  ├─ StageEngineCoreClient[0]（AR，如 Thinker）
  ├─ StageEngineCoreClient[1]（AR，如 Talker）
  ├─ StageDiffusionClient[2]（Diffusion，如图像生成）
  └─ OmniConnector（跨阶段数据传输）
```

### 决策 1：Stage 抽象——声明式流水线配置

**问题**：不同全模态模型的流水线结构差异巨大（Qwen3-Omni 是 3 阶段 AR+AR+卷积，BAGEL 是 2 阶段 AR+Diffusion，FLUX 是纯 Diffusion）。如何用一套代码支持所有组合？

**方案**：通过 YAML Stage Config 声明式定义流水线。以 Qwen3-Omni 为例（`qwen3_omni_moe.yaml`）：

```yaml
stage_args:
  - stage_id: 0          # Thinker: 多模态理解 + 文本生成
    stage_type: llm
    runtime: { devices: "0" }
    engine_args: { model_stage: thinker, worker_type: ar, ... }

  - stage_id: 1          # Talker: 文本嵌入 → 音频编码
    stage_type: llm
    engine_input_source: [0]
    custom_process_input_func: ...thinker2talker

  - stage_id: 2          # Code2Wav: 音频编码 → 波形
    stage_type: llm
    engine_input_source: [1]
    custom_process_input_func: ...talker2code2wav
```

**Trade-off**：配置灵活性 vs 学习成本。项目提供了 30+ 个预定义 YAML（覆盖 Qwen3-Omni、BAGEL、CosyVoice3、FLUX、HunyuanVideo 等），降低了入门门槛。

**可迁移性**：这种声明式流水线配置模式可迁移到任何需要多阶段编排的推理系统。

### 决策 2：Orchestrator——集中式事件循环编排

**问题**：多阶段流水线中，如何协调阶段间的数据流、错误传播、请求生命周期？

**方案**：`Orchestrator` 在后台线程运行独立的 asyncio 事件循环，拥有所有 Stage Client 实例。核心逻辑是 `_orchestration_loop`：

1. 轮询所有阶段的输出
2. 通过 `OutputProcessor` 处理原始输出
3. `_route_output` 决定：发给用户（final_output=true）还是转发到下一阶段

关键代码路径：
```python
async def _route_output(self, stage_id, output, req_state, ...):
    if stage_client.final_output:
        await self.output_async_queue.put({...})  # 发给用户
    if finished and stage_id < req_state.final_stage_id:
        await self._forward_to_next_stage(...)     # 转发下一阶段
```

**Trade-off**：集中式编排 vs 分布式编排。集中式更易调试和理解，但 Orchestrator 是单点瓶颈。通过 asyncio + 非阻塞轮询缓解了这个问题。

**可迁移性**：Orchestrator 的「轮询-处理-路由」模式是经典的事件驱动编排范式，可迁移到任何多阶段数据处理系统。

### 决策 3：Diffusion 引擎——独立进程架构

**问题**：Diffusion 模型（DiT）的推理模式与 AR 完全不同——没有 KV Cache，没有逐 token 生成，而是多步去噪。如何与 AR 引擎共存？

**方案**：完全独立的 `DiffusionEngine`，使用多进程架构：

```
DiffusionEngine（主进程）
  ├─ pre_process_func（模型特定预处理）
  ├─ Scheduler（请求调度）
  ├─ WorkerProc[0]（GPU 0，ZMQ 通信）
  │   └─ GPUWorker → Pipeline.forward()
  ├─ WorkerProc[1]（GPU 1）
  └─ post_process_func（后处理）
```

Diffusion 引擎拥有自己的调度器（FIFO 请求调度）、Worker（spawn 进程隔离）、Pipeline 抽象。支持 27 个模型系列（FLUX、Wan、HunyuanVideo、SD3 等），每个模型有独立的 Pipeline 实现。

**Trade-off**：独立实现 vs 复用 vLLM。选择独立实现增加了代码量（80K+ 行），但获得了针对 Diffusion 特性的深度优化能力（TeaCache、CFG 并行、序列并行等）。

**可迁移性**：「按执行模式分离引擎」的策略可迁移——当系统需要支持根本不同的计算模式时，独立引擎比勉强复用更好。

### 决策 4：OmniConnector——可插拔跨阶段传输

**问题**：阶段间需要传递 KV Cache、隐藏状态、音频编码等异构数据，可能跨进程甚至跨节点。

**方案**：抽象的 `put/get` API，4 种 Connector 实现：

| 场景 | Connector | 机制 |
|------|-----------|------|
| 单机 | SharedMemoryConnector | 共享内存（自动配置） |
| 跨机（TCP） | MooncakeStoreConnector | TCP + 元数据服务器 |
| 跨机（RDMA） | MooncakeTransferEngineConnector | RDMA 直接传输 |
| 跨机（企业级） | YuanrongConnector | 袁融数据系统 + etcd |

**Trade-off**：当前 D2H2D（设备到主机到设备）模式增加了延迟，但简化了实现。路线图中规划了 D2D（设备到设备）直连。

### 决策 5：CFG Companion 机制

**问题**：Classifier-Free Guidance 需要同时运行正向和负向 prompt，但在解耦的多阶段架构中，如何跨阶段同步 CFG？

**方案**：「Companion Request」范式：

1. AR 阶段通过 `prompt_expand_func` 钩子自动生成负向 companion prompt
2. Companion 请求与主请求并行执行
3. Orchestrator 追踪 companion 完成状态（`_companion_map`/`_companion_done`）
4. 所有 companion 完成后才转发到 Diffusion 阶段
5. Diffusion 阶段通过 `cfg_kv_collect_func` 收集正/负 KV Cache

这是一个精巧的协议设计，将 CFG 的全局同步问题拆解为 Orchestrator 层面的状态追踪问题。

### 决策 6：Async Chunk 流水线重叠

**问题**：顺序执行多阶段时，后续阶段必须等前一阶段完全结束才能开始，延迟叠加严重。

**方案**：`async_chunk` 模式让阶段间以 chunk 粒度流式传输：
- Thinker -> Talker：每个 decode step 即转发（chunk_size=1）
- Talker -> Code2Wav：累积 25 帧后转发

**实测效果**（H800 GPU）：
- TTFP（首音频延迟）降低 92%：6.5s -> 0.52s
- E2E 延迟降低 6-17%
- RTF（实时因子）改善 8-16%

---

## 创新点（含评分）

### 1. Stage 抽象与声明式流水线
- **描述**：通过 YAML 配置定义任意模态组合的推理流水线，将异构执行引擎统一在一个编排框架下
- **新颖度**：4/5（此前没有开源项目以这种粒度解决全模态推理编排）
- **实用性**：5/5（直接支持 40+ 模型架构，新模型只需写 YAML + Stage Processor）
- **可迁移性**：5/5（声明式流水线配置是通用模式）

### 2. Orchestrator 集中式事件驱动编排
- **描述**：后台线程 asyncio 事件循环统一管理所有阶段的输入/输出/转发/错误处理
- **新颖度**：3/5（事件驱动编排不新，但应用于 LLM+Diffusion 多阶段场景是首创）
- **实用性**：5/5（简化了多阶段生命周期管理，支持 CFG companion 和 async chunk）
- **可迁移性**：4/5（适用于任何需要多阶段数据流编排的系统）

### 3. 独立 Diffusion 引擎与 AR 引擎共存
- **描述**：完整的 Diffusion 推理栈（Engine + Scheduler + Worker + Pipeline），与 vLLM AR 引擎平行运行
- **新颖度**：4/5（Diffusers 做推理，但没有与 LLM 引擎统一编排）
- **实用性**：5/5（覆盖 27 个模型系列，支持 TeaCache/CacheDiT/Ring Attention 等加速）
- **可迁移性**：3/5（Diffusion 引擎代码量大，但架构模式可参考）

### 4. OmniConnector 跨阶段传输抽象
- **描述**：统一 `put/get` API，支持共享内存/TCP/RDMA/企业级多种后端，自动配置
- **新颖度**：3/5（vLLM 已有 KV Transfer，但 OmniConnector 泛化到任意阶段产物）
- **实用性**：4/5（单机自动配置零门槛，跨机部署需要额外基础设施）
- **可迁移性**：5/5（可插拔传输层是经典 SOA 模式）

### 5. CFG Companion 跨阶段同步协议
- **描述**：通过 Companion Request + Orchestrator 状态追踪实现解耦架构下的 CFG 全局同步
- **新颖度**：5/5（全新协议设计，解决了解耦架构下 CFG 的固有矛盾）
- **实用性**：4/5（对 Diffusion 图像生成质量至关重要）
- **可迁移性**：3/5（特定于 CFG 场景，但「companion tracking」模式可泛化）

### 6. Async Chunk 流水线重叠
- **描述**：阶段间以 chunk 粒度流式传输，重叠计算与 IO
- **新颖度**：3/5（流式处理不新，但在 LLM+TTS 多阶段场景的工程化实现有价值）
- **实用性**：5/5（TTFP 降低 92%，对实时语音场景是质变）
- **可迁移性**：4/5（chunk-based 流式流水线可迁移到任何多阶段系统）

---

## 可复用模式

### 1. 声明式异构流水线（Stage Config Pattern）
**场景**：任何需要组合不同执行引擎的推理/数据处理系统
**核心**：用 YAML/JSON 声明 Stage 的类型、设备、引擎参数、输入来源、转换函数
**价值**：将「如何组合」与「如何执行」分离，新模型只需写配置而非改代码

### 2. 轮询-处理-路由编排器（Orchestrator Pattern）
**场景**：多阶段异步数据流编排
**核心**：后台线程事件循环 + 轮询所有阶段输出 + 统一路由（发给用户 or 转发下一阶段）
**价值**：集中式控制流，易于添加 companion tracking、metrics、错误传播等横切关注点

### 3. 继承式扩展（Inheritance over Composition for Framework Extension）
**场景**：在现有框架上扩展功能但保持兼容
**核心**：AR 模块通过继承 vLLM 的 Scheduler/Worker/ModelRunner 添加 Omni 特性（prompt_embeds overlay、hidden state exposure），最小化改动
**价值**：享受上游优化的同时添加定制功能，降低维护成本

### 4. 可插拔传输后端（Connector Abstraction Pattern）
**场景**：跨进程/跨节点数据传输需要适配不同基础设施
**核心**：抽象 `put/get` API + Backend Selector + 自动降级（无配置默认共享内存）
**价值**：从单机开发到跨机部署无需改代码

### 5. 步级执行协议（Step Execution Protocol）
**场景**：将批处理执行分解为步级控制
**核心**：`SupportsStepExecution` Protocol（prepare_encode -> denoise_step -> step_scheduler -> post_decode）
**价值**：为 Continuous Diffusion Acceleration（Issue #1217）等未来优化预留接口

---

## 竞品交叉分析

| 维度 | vLLM-Omni | vLLM | SGLang | Diffusers | ComfyUI | Triton IS |
|------|-----------|------|--------|-----------|---------|-----------|
| AR 推理 | 继承 vLLM | 原生 | 原生 | 无 | 无 | 通用 |
| Diffusion 推理 | 原生 | 无 | 有限 | 原生 | 原生 | 需手动 |
| 多阶段编排 | 原生（Stage Config） | 无 | 无 | 无 | UI 工作流 | 需手动 |
| TTS 推理 | 原生 | 无 | 无 | 无 | 插件 | 需手动 |
| 跨阶段传输 | OmniConnector | KV Transfer | 无 | 无 | 无 | 自定义 |
| 模型覆盖 | 40+ | 200+（仅文本） | 50+（仅文本） | 100+（仅扩散） | 100+（仅扩散） | 通用 |
| 生产就绪度 | Alpha（v0.18） | 稳定 | 稳定 | 稳定 | 稳定 | 企业级 |
| 多平台 | 6 平台 | CUDA 为主 | CUDA | CUDA | CUDA | 多平台 |

**核心差异化**：vLLM-Omni 是唯一将 LLM 自回归 + Diffusion + TTS + 多阶段 pipeline 统一在一个推理框架中的开源项目。其他方案要么只覆盖一种模式（vLLM/SGLang 做文本，Diffusers 做扩散），要么需要手动集成（Triton）。

**风险**：
- vLLM 母项目可能自行实现 Omni 功能，但 vLLM-Omni 已被官方认可（vllm-project 组织下），更可能被合并
- SGLang 在多模态方面进展快，但目前仍以文本为主
- 生产就绪度仍为 Alpha，但迭代速度极快（4 个月 4 个大版本）

---

## 代码质量

### 代码规模
- **核心包** `vllm_omni/`：482 个 Python 文件，160,877 行代码
- **Diffusion 模块**：208 个文件，80,088 行（占总量 50%，是最大模块）
- **测试**：214 个文件，50,800 行（测试代码比约 31.6%）
- **CI Workflows**：3 个（pre-commit、build_wheel、pr-reviewer），共 151 行

### 测试覆盖
- **178 个 test_ 前缀文件**，覆盖：
  - 分布式连接器（omni_connectors）
  - 模型特定功能（cosyvoice3、qwen3_tts、mimo_audio 等）
  - 引擎生命周期（orchestrator、output_processor）
  - 调度器（generation_scheduler）
  - E2E 测试、ComfyUI 集成测试、Diffusion 测试
- 测试比例合理（31.6%），但考虑到 Alpha 状态和快速迭代，部分新功能可能缺乏充分测试

### 代码组织
- **模块化清晰**：entrypoints / engine / worker / diffusion / distributed / model_executor 职责分明
- **继承层次合理**：OmniBase -> Omni/AsyncOmni，OmniGPUModelRunner -> GPUARModelRunner/GPUGenerationModelRunner
- **文档丰富**：`docs/design/` 下有完整的架构设计文档（architecture_overview、dit_module、ar_module、feature 设计等）
- **Stage Config 体系**：30 个预定义 YAML 配置，覆盖主流模型

### 潜在改进点
- Orchestrator 使用 1ms 轮询间隔，高并发下可能成为瓶颈
- Diffusion Scheduler 当前仅支持单请求执行（`max_num_running_reqs = 1`），限制了吞吐
- 部分 TODO 标注（如 `reset_mm_cache not yet supported`）表明某些控制面功能尚未完成
- `D2H2D` 传输模式增加延迟，D2D 直连尚在路线图中
