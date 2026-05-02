# 训练基础设施 (Training Infrastructure)

## 目录结构

```
training-infra/
├── distributed-training/      # 分布式训练
│   # 数据并行、模型并行、流水线并行、ZeRO
│
├── frameworks/                # 训练框架
│   # Megatron、DeepSpeed、FSDP、Colossal-AI
│
├── optimization/              # 训练优化
│   # 混合精度、梯度累积、通信优化
│
├── memory-management/         # 显存管理
│   # 激活重计算、Offloading、显存碎片
│
├── communication/             # 通信优化
│   # All-Reduce、Ring-AllReduce、NCCL
│
├── hardware/                  # 硬件相关
│   # GPU架构、互联拓扑、TPU
│
└── fault-tolerance/           # 容错机制
    # Checkpoint、故障恢复、弹性训练
```

## 核心关注点

训练基础设施解决的核心问题：**如何在有限的计算资源下高效地训练大规模模型**

### 关键挑战

| 挑战 | 解决方案 | 对应目录 |
|------|---------|---------|
| 模型太大单卡放不下 | 模型并行、流水线并行 | `distributed-training/` |
| 训练速度太慢 | 数据并行、通信优化 | `distributed-training/`, `communication/` |
| 显存不足 | ZeRO、激活重计算、Offloading | `memory-management/` |
| 训练不稳定 | 混合精度、梯度裁剪 | `optimization/` |
| 硬件故障 | Checkpoint、弹性训练 | `fault-tolerance/` |

## 学习路径

**基础阶段**
- `hardware/` — 了解GPU架构和互联方式
- `frameworks/` — 掌握主流训练框架

**进阶阶段**
- `distributed-training/` — 学习各种并行策略
- `optimization/` — 训练加速技巧
- `communication/` — 通信优化原理

**深入阶段**
- `memory-management/` — 显存优化技术
- `fault-tolerance/` — 大规模训练的稳定性保障

## 相关资源

- [LLM训练](../llm/pre-training/) — 预训练实践
- [LLM后训练](../llm/post-training/) — SFT和RLHF训练
- [强化学习](../reinforce-learning/) — RL训练基础设施

---

*最后更新: 2026-05-02*
