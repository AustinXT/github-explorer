# WiFi-DensePose 内容分析笔记

## 项目架构

### 双代码库设计
1. **Python v1** (`v1/`): 原始实现，FastAPI + SQLAlchemy + PyTorch
2. **Rust 重写** (`rust-port/wifi-densepose-rs/`): 16个 crate 的 workspace，Axum REST API

### 核心组件

#### Rust Crates (16个)
- `wifi-densepose-core`: 核心类型、CSI帧原语
- `wifi-densepose-signal`: 信号处理 + RuvSense 多基站感知（14个模块）
- `wifi-densepose-nn`: 神经网络推理（ONNX/PyTorch/Candle）
- `wifi-densepose-train`: 训练管线 + RuVector 集成
- `wifi-densepose-mat`: 大规模伤亡评估工具
- `wifi-densepose-hardware`: ESP32聚合器、TDM协议
- `wifi-densepose-ruvector`: RuVector v2.0.4 跨视角融合
- `wifi-densepose-api`: REST API (Axum)
- `wifi-densepose-db`: 数据库层 (Postgres/SQLite/Redis)
- `wifi-densepose-wasm`: 浏览器 WASM 绑定
- `wifi-densepose-cli`: 命令行工具
- `wifi-densepose-sensing-server`: 轻量感知服务器
- `wifi-densepose-wifiscan`: 多BSSID WiFi扫描
- `wifi-densepose-vitals`: ESP32 生命体征提取
- `wifi-densepose-desktop`: Tauri v2 桌面应用(WIP)
- `ruv-neural`: 自定义神经网络层

#### ESP32 固件 (`firmware/`)
- C 语言编写的 ESP32-S3 固件
- 35个源文件: CSI采集、边缘处理、OTA更新、WASM运行时
- 支持 AMOLED 显示、mmWave传感器融合
- 模拟CSI模式用于QEMU测试

#### UI (`ui/`)
- Observatory: Three.js 全息仪表板（5个面板）
- Pose Fusion: 双模态融合（摄像头+WiFi CSI）
- Mobile: React Native 移动端
- 配置管理界面

### 信号处理管线
RuvSense 模块 (13个):
1. multiband - 多频段CSI融合
2. phase_align - 相位对齐
3. multistatic - 注意力加权多基站融合
4. coherence - Z-score 相干性评分
5. coherence_gate - 质量门控
6. pose_tracker - 17关键点卡尔曼跟踪
7. field_model - SVD 房间特征结构
8. tomography - RF层析成像
9. longitudinal - 长期漂移检测
10. intention - 预运动信号检测(200-500ms)
11. cross_room - 跨房间指纹
12. gesture - DTW手势分类
13. adversarial - 物理不可能信号检测

### RuVector 集成（5个模块）
- mincut: 动态人员匹配
- attn-mincut: 天线注意力
- temporal-tensor: 压缩CSI缓冲
- solver: 稀疏插值
- attention: 空间注意力

## 文档体系
- 66个ADR（架构决策记录）
- 7个DDD领域模型
- 用户指南、构建指南
- 大量内嵌文档（204个Markdown文件）

## 技术亮点
1. **性能**: Rust 实现 54K fps，比 Python 快 810x
2. **硬件适配**: ESP32-S3 (~$9) 单节点可独立运行
3. **隐私**: 全程无摄像头，仅使用WiFi信号
4. **自学习**: 对比学习CSI嵌入，无需标注数据
5. **跨环境泛化**: MERIDIAN框架，域对抗学习
6. **WASM部署**: 可在浏览器中运行推理
7. **mmWave融合**: 60GHz毫米波+WiFi CSI联合感知

## 部署方式
- Docker: `docker pull ruvnet/wifi-densepose:latest` (amd64+arm64)
- ESP32直接烧录
- WASM浏览器端
- Tauri桌面应用(WIP)

## 测试
- 声称 1300+ 测试
- Rust: 15个测试文件
- Python: 36个测试文件
- QEMU ESP32模拟测试
- Fuzz testing (3个libFuzzer目标)
