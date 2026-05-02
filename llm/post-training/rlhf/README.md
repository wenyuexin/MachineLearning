# RLHF (基于人类反馈的强化学习)

## 前置要求

学习 RLHF 之前，建议先掌握强化学习基础：

- [reinforce-learning/policy-optimization/](../../../reinforce-learning/policy-optimization/)
  - `01-AC架构.md` — Actor-Critic 架构
  - `02-优势函数.md` — GAE、优势估计
  - `04-PPO.md` — PPO 核心算法（重点）

## 目录结构

```
rlhf/
├── papers/                  # RLHF 相关论文
│   # InstructGPT、RLAIF、Constitutional AI 等
├── reward-modeling/         # 奖励模型训练
│   # 偏好数据构建、Reward Model 架构与训练技巧
├── training/                # RLHF 训练实践
│   # PPO 在 LLM 中的特殊用法
└── README.md
```

## RLHF 核心流程

```
偏好数据收集 → 训练 Reward Model → PPO 优化策略模型
                      ↑
              人工标注 / AI 标注 (RLAIF)
```

## 与 DPO 的关系

| 方法 | 是否需要显式奖励模型 | 是否需要 RL 算法 | 训练复杂度 |
|------|-------------------|---------------|-----------|
| **RLHF (PPO)** | 是 | 是（PPO） | 高 |
| **DPO** | 否 | 否 | 低 |

DPO 是 RLHF 的简化替代方案，不需要显式训练奖励模型和使用 PPO。详见 [../dpo/](../dpo/)。

## 相关资源

- [DPO (直接偏好优化)](../dpo/) — RLHF 的替代方案
- [reinforce-learning/policy-optimization/](../../../reinforce-learning/policy-optimization/) — PPO 基础理论

---

*最后更新: 2026-05-02*
