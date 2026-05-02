# 世界模型 (World Models)

世界模型是环境的内部模拟器，使智能系统能够预测未来状态、理解因果关系，并在不依赖真实交互的情况下做出决策。

## 目录结构

```
world-models/
├── 01-foundations/                   # 基础
│   ├── definition-and-motivation/
│   ├── predictive-models-in-rl/
│   └── learning-latent-dynamics/
│
├── 02-methods-and-architectures/     # 方法与架构
│   ├── dreamer-family/
│   │   ├── dreamerv1-v2/
│   │   └── dreamerv3/
│   ├── autoregressive-world-models/
│   ├── diffusion-world-models/
│   └── jepa-and-energy-based-models/
│
├── 03-reasoning-models/    # 推理用世界模型
│   ├── model-based-planning/
│   └── causal-world-models/
│
├── 04-large-scale-world-models/      # 大规模世界模型
│   ├── video-prediction-models/
│   ├── sora-and-video-generation/
│   └── embodied-world-models/
│
├── 05-evaluation/                    # 评估
│   ├── prediction-metrics/
│   └── downstream-task-transfer/
│
└── 06-applications/                  # 应用
    ├── robotics-simulation/
    ├── autonomous-driving/
    └── game-play-and-agi-exploration/
```

## 四大架构类别

| 类别 | 代表模型 | 优势 | 劣势 |
|------|---------|------|------|
| **潜空间模型** | DreamerV1-V3, PlaNet | 计算高效、成熟稳定 | 长时预测能力有限 |
| **JEPA** | I-JEPA | 表示学习高效 | 理论探索阶段 |
| **Transformer** | Genie, TWM | 长程依赖建模强 | 计算资源需求大 |
| **扩散模型** | Sora, Cosmos | 生成质量最高 | 推理慢，难以实时交互 |

## 学习路径

**基础阶段**
- `01-foundations/` — 理解世界模型的基本概念
- `02-methods-and-architectures/` — 掌握不同架构的特点和适用场景

**算法阶段**
- `03-reasoning-models/` — 基于模型的规划与因果推理

**应用阶段**
- `04-large-scale-world-models/` — 视频生成、大规模预训练
- `05-evaluation/` — 评估方法
- `06-applications/` — 各领域的具体应用

## 相关资源

- [具身智能](../embodied-intelligence/) — 世界模型的主要应用场景
- [强化学习](../reinforce-learning/) — MBRL基础理论
- [视频生成](06-applications/) — 世界模型的生成应用

---

*最后更新: 2026-05-02*
