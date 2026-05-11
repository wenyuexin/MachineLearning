# 训练基础设施 (Training Infrastructure)

大规模模型训练的硬件、分布式策略、框架、显存优化、编译、运维与调试。

## 分类依据

Training Infra 目录按"硬件底座 → 分布式策略 → 框架工具 → 显存优化 → 编译加速 → 运维 → 可观测性"组织：

- **01（硬件与网络）**：GPU 架构、AI 加速器、互联与网络
- **02（分布式训练）**：数据并行、模型并行、混合与序列并行
- **03（框架与工具）**：DeepSpeed、Megatron-LM、HF Accelerate、编排工具
- **04（内存与存储）**：梯度检查点、混合精度、Offloading、检查点与恢复
- **05（编译与内核）**：Triton、torch.compile、XLA/JIT
- **06（ML 运维）**：实验管理、数据管线、ML CI/CD
- **07（可观测性与调试）**：Profiling、训练异常检测、成本管理

## 边界说明

| 内容 | 适合放 Training Infra | 不适合放 Training Infra |
|------|----------------------|------------------------|
| GPU/TPU 架构、互联拓扑 | 01-hardware-and-networking | — |
| 数据并行、模型并行、ZeRO | 02-distributed-training | 具体模型的并行配置放 `llm/03-training/pre-training/distributed-training/` |
| DeepSpeed、Megatron-LM 使用 | 03-frameworks-and-tools | 推理框架（vLLM、TensorRT-LLM）放 `llm/04-serving/serving-frameworks/` |
| 混合精度、梯度检查点、Offloading | 04-memory-and-storage | — |
| Triton、torch.compile、XLA | 05-compilation-and-kernels | — |
| 实验管理、数据管线 | 06-ml-operations | 数据集构建放 `llm/03-training/pre-training/data-curation/` |
| Profiling、训练调试 | 07-observability-and-debugging | — |
| 训练方法（预训练/微调/对齐） | — | 放 `llm/03-training/`，本目录只关注工程层面 |

## 目录结构

```
training-infra/
├── 01-hardware-and-networking/            # 硬件与网络
│   ├── gpu-architecture/                  # GPU架构
│   ├── tpu-and-ai-accelerators/           # TPU与AI加速器
│   └── interconnects-and-networking/      # 互联与网络
│
├── 02-distributed-training/               # 分布式训练
│   ├── data-parallelism/                  # 数据并行
│   │   ├── pytorch-ddp/                   # PyTorch DDP
│   │   └── deepspeed-zeRO/                # DeepSpeed ZeRO
│   ├── model-parallelism/                 # 模型并行
│   │   ├── tensor-parallelism/            # 张量并行
│   │   └── pipeline-parallelism/          # 流水线并行
│   └── hybrid-and-sequence-parallelism/   # 混合与序列并行
│
├── 03-frameworks-and-tools/               # 训练框架与工具
│   ├── deepspeed/                         # DeepSpeed
│   ├── megatron-lm/                       # Megatron-LM
│   ├── hf-accelerate/                     # HF Accelerate
│   └── orchestration/                     # 编排工具
│
├── 04-memory-and-storage/                 # 内存与存储优化
│   ├── gradient-checkpointing/            # 梯度检查点
│   ├── mixed-precision/                   # 混合精度
│   ├── offloading-strategies/             # Offloading策略
│   └── checkpointing-and-recovery/        # 检查点与恢复
│
├── 05-compilation-and-kernels/            # 模型编译与内核
│   ├── triton-and-custom-kernels/         # Triton与自定义内核
│   ├── torch-compile/                     # torch.compile
│   └── xla-and-jit/                      # XLA与JIT
│
├── 06-ml-operations/                      # 实验追踪与运维
│   ├── experiment-management/             # 实验管理
│   ├── data-pipelines/                    # 数据管线
│   └── ci-cd-for-ml/                      # ML CI/CD
│
└── 07-observability-and-debugging/        # 可观测性与调试
    ├── profiling-tools/                   # Profiling工具
    ├── anomaly-detection-in-training/     # 训练异常检测
    └── cost-management/                   # 成本管理
```

## 核心关注点

训练基础设施解决的核心问题：**如何在有限的计算资源下高效地训练大规模模型**

### 关键挑战

| 挑战 | 解决方案 | 对应目录 |
|------|---------|---------|
| 模型太大单卡放不下 | 模型并行、流水线并行 | `02-distributed-training/` |
| 训练速度太慢 | 数据并行、通信优化 | `02-distributed-training/` |
| 显存不足 | ZeRO、激活重计算、Offloading | `04-memory-and-storage/` |
| 训练不稳定 | 混合精度、梯度裁剪 | `04-memory-and-storage/`、`05-compilation-and-kernels/` |
| 硬件故障 | Checkpoint、弹性训练 | `04-memory-and-storage/checkpointing-and-recovery/` |

## 学习路径

**基础阶段**
- `01-hardware-and-networking/` — 了解 GPU 架构和互联方式
- `03-frameworks-and-tools/` — 掌握主流训练框架

**进阶阶段**
- `02-distributed-training/` — 学习各种并行策略
- `05-compilation-and-kernels/` — 训练加速技巧

**深入阶段**
- `04-memory-and-storage/` — 显存优化技术
- `06-ml-operations/` — 实验追踪与运维
- `07-observability-and-debugging/` — 可观测性与调试

## 与其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| 分布式训练工程 | [../llm/03-training/pre-training/distributed-training/](../llm/03-training/pre-training/distributed-training/) | LLM 侧的并行配置与实践经验 |
| 训练框架 | [../llm/04-serving/serving-frameworks/](../llm/04-serving/serving-frameworks/) | 训练框架 vs 推理框架 |
| 数据构建 | [../llm/03-training/pre-training/data-curation/](../llm/03-training/pre-training/data-curation/) | 数据管线与数据集构建 |
| 深度学习基础设施 | [../deep-learning/05-infra/](../deep-learning/05-infra/) | DL 基础设施的概念介绍 |
| 强化学习训练 | [../reinforce-learning/](../reinforce-learning/) | RL 训练基础设施 |

---

*最后更新: 2026-05-11*
