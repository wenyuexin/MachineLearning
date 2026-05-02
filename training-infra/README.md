# 训练基础设施 (Training Infrastructure)

## 目录结构

```
training-infra/
├── 01-hardware-and-networking/            # 硬件与网络
│   ├── gpu-architecture/
│   ├── tpu-and-ai-accelerators/
│   └── interconnects-and-networking/
│
├── 02-distributed-training/               # 分布式训练
│   ├── data-parallelism/
│   │   ├── pytorch-ddp/
│   │   └── deepspeed-zeRO/
│   ├── model-parallelism/
│   │   ├── tensor-parallelism/
│   │   └── pipeline-parallelism/
│   └── hybrid-and-sequence-parallelism/
│
├── 03-training-frameworks-and-tools/      # 训练框架与工具
│   ├── deepspeed/
│   ├── megatron-lm/
│   ├── hf-accelerate/
│   └── orchestration/
│
├── 04-memory-and-storage-optimization/    # 内存与存储优化
│   ├── gradient-checkpointing/
│   ├── mixed-precision/
│   ├── offloading-strategies/
│   └── checkpointing-and-recovery/
│
├── 05-model-compilation-and-kernels/      # 模型编译与内核
│   ├── triton-and-custom-kernels/
│   ├── torch-compile/
│   └── xla-and-jit/
│
├── 06-experiment-tracking-and-operations/ # 实验追踪与运维
│   ├── experiment-management/
│   ├── data-pipelines/
│   └── ci-cd-for-ml/
│
└── 07-observability-and-debugging/        # 可观测性与调试
    ├── profiling-tools/
    ├── anomaly-detection-in-training/
    └── cost-management/
```

## 核心关注点

训练基础设施解决的核心问题：**如何在有限的计算资源下高效地训练大规模模型**

### 关键挑战

| 挑战 | 解决方案 | 对应目录 |
|------|---------|---------|
| 模型太大单卡放不下 | 模型并行、流水线并行 | `02-distributed-training/` |
| 训练速度太慢 | 数据并行、通信优化 | `02-distributed-training/` |
| 显存不足 | ZeRO、激活重计算、Offloading | `04-memory-and-storage-optimization/` |
| 训练不稳定 | 混合精度、梯度裁剪 | `05-model-compilation-and-kernels/` |
| 硬件故障 | Checkpoint、弹性训练 | `04-memory-and-storage-optimization/checkpointing-and-recovery/` |

## 学习路径

**基础阶段**
- `01-hardware-and-networking/` — 了解GPU架构和互联方式
- `03-training-frameworks-and-tools/` — 掌握主流训练框架

**进阶阶段**
- `02-distributed-training/` — 学习各种并行策略
- `05-model-compilation-and-kernels/` — 训练加速技巧

**深入阶段**
- `04-memory-and-storage-optimization/` — 显存优化技术
- `06-experiment-tracking-and-operations/` — 实验追踪与运维
- `07-observability-and-debugging/` — 可观测性与调试

## 相关资源

- [LLM训练](../llm/03-training/pre-training/) — 预训练实践
- [LLM后训练](../llm/03-training/fine-tuning/) — SFT和RLHF训练
- [强化学习](../reinforce-learning/) — RL训练基础设施

---

*最后更新: 2026-05-02*
