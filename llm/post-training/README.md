# LLM 后训练 (Post-Training)

后训练是大型语言模型开发的关键阶段，在预训练之后，通过监督微调和对齐技术使模型具备遵循指令和符合人类偏好的能力。

## 阶段流程

```
预训练模型 → SFT → 偏好对齐
                      ├── DPO
                      ├── RLHF (PPO)
                      └── 其他方法 (KTO, IPO, SimPO...)
```

## 目录结构

| 目录 | 内容 |
|------|------|
| [sft/](./sft/) | 监督微调：指令数据构建、SFT原理与技巧 |
| [dpo/](./dpo/) | 直接偏好优化：DPO原理、变体、数据构建 |
| [rlhf/](./rlhf/) | 基于人类反馈的强化学习：PPO、Reward Modeling |

## 基础理论

通用强化学习算法参见 [reinforce-learning/policy-optimization/](../../reinforce-learning/policy-optimization/)

---

*最后更新: 2026-05-02*
