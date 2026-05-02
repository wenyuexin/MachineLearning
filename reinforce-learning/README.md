# 强化学习 (Reinforcement Learning)

## 目录结构

```
reinforce-learning/
├── fundation/                 # 基础理论
│   ├── 00-基本概念.md          # RL基本概念
│   ├── 01-马尔可夫决策.md      # MDP、状态、动作、奖励
│   ├── 价值与回报.md           # 价值函数、回报、折扣因子
│   ├── 基于价值的算法.md       # 价值迭代、策略迭代
│   ├── 基于策略的方法.md       # 策略梯度、REINFORCE
│   ├── 蒙特卡洛方法.md         # MC估计
│   └── 时序差分.md             # TD、SARSA、Q-Learning
│
└── policy-optimization/       # 策略优化
    ├── 01-AC架构.md           # Actor-Critic架构
    ├── 02-优势函数.md          # 优势函数、GAE
    ├── 03-TRPO与重要性采样.md   # TRPO、重要性采样
    ├── 04-PPO.md              # PPO算法
    └── paper/                 # 相关论文
```

## 学习路径

**基础阶段**
- `fundation/` 按编号顺序阅读：
  1. `00-基本概念.md` — RL基本框架
  2. `01-马尔可夫决策.md` — MDP形式化
  3. `价值与回报.md` — 价值函数定义
  4. `基于价值的算法.md` — 动态规划方法
  5. `基于策略的方法.md` — 策略梯度基础
  6. `蒙特卡洛方法.md` / `时序差分.md` — 无模型方法

**进阶阶段**
- `policy-optimization/` 按编号顺序：
  1. `01-AC架构.md` — Actor-Critic
  2. `02-优势函数.md` — 方差缩减
  3. `03-TRPO与重要性采样.md` — 信任域方法
  4. `04-PPO.md` — 近端策略优化

## 详细学习路线

参见 [roadmap.md](roadmap.md) — 包含数学基础、编程工具、核心算法、进阶主题的完整规划

## 与仓库其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| PPO/TRPO基础 | [../llm/post-training/rlhf/](../llm/post-training/rlhf/) | LLM的RLHF使用PPO |
| 策略梯度 | [../llm/post-training/dpo/](../llm/post-training/dpo/) | DPO是偏好优化的替代方案 |
| MBRL | [../world-models/algorithms/](../world-models/algorithms/) | 基于模型的强化学习 |
| 多智能体 | [../agentic/05-multi-agent/](../agentic/05-multi-agent/) | 多智能体系统中的RL |

---

*最后更新: 2026-05-02*
