# 强化学习 (Reinforcement Learning)

强化学习的理论基础、核心算法、进阶主题与工具：从 MDP 到策略优化、从无模型到基于模型、从单智能体到多智能体。

## 分类依据

Reinforce Learning 目录按"基础 → 核心算法范式 → 进阶主题 → 评估"组织：

- **01（基础）**：MDP、价值函数与 Bellman 方程、探索与利用
- **02（无模型 RL）**：蒙特卡洛、时序差分、DQN 及变体
- **03（策略方法）**：策略梯度（REINFORCE、PPO）、Actor-Critic（A2C/A3C、SAC）、确定性策略梯度
- **04（基于模型的 RL）**：世界模型（Dreamer、MuZero）、规划与树搜索
- **05（进阶主题）**：分层 RL、多智能体 RL、逆 RL、LLM 对齐中的 RL
- **06（评估与工具）**：环境、基准与评估指标

## 边界说明

| 内容 | 适合放 RL | 不适合放 RL |
|------|----------|------------|
| MDP、价值函数、探索与利用 | 01-foundations | — |
| Q-Learning、SARSA、DQN | 02-model-free-rl | — |
| PPO、SAC、策略梯度原理 | 03-policy-methods | RLHF 的 LLM 应用放 `llm/03-training/alignment/` |
| Dreamer、MuZero、MBRL 原理 | 04-model-based-rl | 视频生成/预测放 `world-models/` |
| 多智能体 RL 算法 | 05-advanced-topics/multi-agent-rl | Agent 架构/协作模式放 `agentic/03-multi-agent/` |
| RLHF/GRPO 的 RL 原理 | 05-advanced-topics/rl-in-llm-alignment | RLHF 的 LLM 工程实现放 `llm/03-training/alignment/rlhf/` |
| 逆强化学习 | 05-advanced-topics/inverse-rl | — |
| Gym 环境、基准指标 | 06-evaluation-and-tools | — |

## 目录结构

```
reinforce-learning/
├── 01-foundations/                  # 基础理论
│   ├── markov-decision-processes/    # 马尔可夫决策过程
│   ├── value-functions-and-bellman/  # 价值函数与Bellman方程
│   └── exploration-vs-exploitation/  # 探索与利用
│
├── 02-model-free-rl/                 # 无模型强化学习
│   ├── monte-carlo-methods/          # 蒙特卡洛方法
│   ├── temporal-difference-learning/ # 时序差分学习
│   │   ├── sarsa/                    # SARSA
│   │   └── q-learning/              # Q-Learning
│   └── deep-q-networks/             # 深度Q网络
│       ├── dqn-and-variants/        # DQN及变体
│       └── rainbow/                 # Rainbow
│
├── 03-policy-methods/                # 基于策略与Actor-Critic
│   ├── policy-gradient/             # 策略梯度
│   │   ├── reinforce/               # REINFORCE
│   │   └── ppo/                     # PPO
│   ├── actor-critic-methods/        # Actor-Critic方法
│   │   ├── a2c-a3c/                 # A2C/A3C
│   │   └── sac/                     # SAC
│   └── deterministic-policy-gradient/ # 确定性策略梯度
│
├── 04-model-based-rl/               # 基于模型的强化学习
│   ├── world-models/                # 世界模型
│   │   ├── dreamer/                 # Dreamer
│   │   └── muzero/                  # MuZero
│   └── planning-and-tree-search/    # 规划与树搜索
│
├── 05-advanced-topics/              # 进阶与应用
│   ├── hierarchical-rl/            # 分层强化学习
│   ├── multi-agent-rl/             # 多智能体RL
│   ├── inverse-rl/                 # 逆强化学习
│   └── rl-in-llm-alignment/        # LLM对齐中的RL（RLHF、GRPO）
│
└── 06-evaluation-and-tools/         # 评估与工具
    ├── gym-and-environments/        # 环境与Gym
    └── benchmark-and-metrics/       # 基准与指标
```

## 学习路径

**基础阶段**
- `01-foundations/` — MDP、价值函数、探索与利用

**核心阶段**
- `02-model-free-rl/` — 蒙特卡洛、时序差分、DQN
- `03-policy-methods/` — 策略梯度、Actor-Critic、PPO

**进阶阶段**
- `04-model-based-rl/` — 世界模型、规划与树搜索
- `05-advanced-topics/` — 分层 RL、多智能体、逆 RL、LLM 对齐

**详细学习路线**

参见 [roadmap.md](roadmap.md) — 包含数学基础、编程工具、核心算法、进阶主题的完整规划

## 与其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| PPO/TRPO 原理 | [../llm/03-training/alignment/rlhf/](../llm/03-training/alignment/rlhf/) | LLM 的 RLHF 使用 PPO |
| 策略梯度 | [../llm/03-training/alignment/dpo/](../llm/03-training/alignment/dpo/) | DPO 是偏好优化的替代方案 |
| MBRL 世界模型 | [../world-models/02-methods-and-architectures/](../world-models/02-methods-and-architectures/) | 基于模型的强化学习 |
| 多智能体 RL | [../agentic/03-multi-agent/](../agentic/03-multi-agent/) | Agent 协作中的 RL 算法 |
| 强化学习基础 | [../agentic/01-foundations/](../agentic/01-foundations/) | Agent 的核心学习范式 |

---

*最后更新: 2026-05-11*
