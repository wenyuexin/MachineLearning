# 强化学习 (Reinforcement Learning)

## 目录结构

```
reinforce-learning/
├── 01-fundamentals/                  # 基础理论
│   ├── markov-decision-processes/
│   ├── value-functions-and-bellman/
│   └── exploration-vs-exploitation/
│
├── 02-model-free-rl/                 # 无模型强化学习
│   ├── monte-carlo-methods/
│   ├── temporal-difference-learning/
│   │   ├── sarsa/
│   │   └── q-learning/
│   └── deep-q-networks/
│       ├── dqn-and-variants/
│       └── rainbow/
│
├── 03-policy-based-and-actor-critic/ # 基于策略与Actor-Critic
│   ├── policy-gradient/
│   │   ├── reinforce/
│   │   └── ppo/
│   ├── actor-critic-methods/
│   │   ├── a2c-a3c/
│   │   └── sac/
│   └── deterministic-policy-gradient/
│
├── 04-model-based-rl/                # 基于模型的强化学习
│   ├── world-models/
│   │   ├── dreamer/
│   │   └── muzero/
│   └── planning-and-tree-search/
│
├── 05-advanced-and-applied-rl/       # 进阶与应用
│   ├── hierarchical-rl/
│   ├── multi-agent-rl/
│   ├── inverse-rl/
│   └── rl-in-llm-alignment/          # RLHF、GRPO
│
└── 06-evaluation-and-tools/          # 评估与工具
    ├── gym-and-environments/
    └── benchmark-and-metrics/
```

## 学习路径

**基础阶段**
- `01-fundamentals/` — MDP、价值函数、探索与利用

**核心阶段**
- `02-model-free-rl/` — 蒙特卡洛、时序差分、DQN
- `03-policy-based-and-actor-critic/` — 策略梯度、Actor-Critic、PPO

**进阶阶段**
- `04-model-based-rl/` — 世界模型、规划与树搜索
- `05-advanced-and-applied-rl/` — 分层RL、多智能体、逆RL、LLM对齐

## 详细学习路线

参见 [roadmap.md](roadmap.md) — 包含数学基础、编程工具、核心算法、进阶主题的完整规划

## 与仓库其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| PPO/TRPO基础 | [../llm/03-training/alignment/rlhf/](../llm/03-training/alignment/rlhf/) | LLM的RLHF使用PPO |
| 策略梯度 | [../llm/03-training/alignment/dpo/](../llm/03-training/alignment/dpo/) | DPO是偏好优化的替代方案 |
| MBRL | [../world-models/02-methods-and-architectures/](../world-models/02-methods-and-architectures/) | 基于模型的强化学习 |
| 多智能体 | [../agentic/03-agent-architectures/multi-agent-systems/](../agentic/03-agent-architectures/multi-agent-systems/) | 多智能体系统中的RL |

---

*最后更新: 2026-05-02*
