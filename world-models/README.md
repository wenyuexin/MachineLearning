# 世界模型 (World Models)

世界模型是环境的内部模拟器，使智能系统能够预测未来状态、理解因果关系，并在不依赖真实交互的情况下做出决策。

## 目录结构

```
world-models/
├── foundations/               # 基础理论
│
├── architectures/             # 模型架构
│   # 潜空间模型、JEPA、Transformer、扩散等架构
│
├── algorithms/                # 核心算法
│   # Dreamer、MuZero等
│
├── training/                  # 训练方法
│
├── video-generation/          # 视频生成
│   # Sora、Cosmos等
│
├── applications/              # 应用场景
│   ├── autonomous-driving/    # 自动驾驶
│   ├── game-ai/               # 游戏AI
│   ├── rl-planning/           # 强化学习规划
│   ├── robotics/              # 机器人
│   └── video-prediction/      # 视频预测
│
└── papers/                    # 论文笔记
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
- `foundations/` — 理解世界模型的基本概念
- `architectures/` — 掌握不同架构的特点和适用场景

**算法阶段**
- `algorithms/` — 学习核心算法实现
- `training/` — 掌握训练方法和技巧

**应用阶段**
- `video-generation/` — 视频生成专项
- `applications/` — 各领域的具体应用
- `papers/` — 领域核心论文

## 在具身AI中的应用

1. **规划验证** — 执行前验证计划可行性
2. **数据生成** — 合成训练数据、场景、边缘案例
3. **基于模型的强化学习** — 作为动力学模型降低样本复杂度

## 相关资源

- [具身智能](../embodied-intelligence/) — 世界模型的主要应用场景
- [强化学习](../reinforce-learning/) — MBRL基础理论
- [视频生成](applications/video-prediction/) — 世界模型的生成应用

---

*最后更新: 2026-05-02*
