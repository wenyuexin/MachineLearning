# 具身智能 (Embodied Intelligence)

具身智能：物理世界中的感知、控制、规划与交互，以及大模型驱动的机器人智能。

## 分类依据

Embodied Intelligence 目录按"基础 → 感知 → 控制与策略 → 规划与导航 → 操作与交互 → 大模型驱动 → 评估"组织：

- **01（基础）**：具身假设、传感器与执行器、仿真环境
- **02（感知）**：目标检测与跟踪、3D 场景理解、触觉与多模态感知
- **03（运动控制与策略）**：模仿学习、机器人 RL、Sim-to-Real 迁移
- **04（规划与导航）**：路径规划、任务与运动规划、LLM 驱动规划
- **05（操作与交互）**：抓取、灵巧操作、人机交互
- **06（大模型驱动）**：VLA 模型、机器人基础模型、语言条件策略
- **07（评估与基准）**：标准化任务、鲁棒评估

## 边界说明

| 内容 | 适合放 Embodied Intelligence | 不适合放 Embodied Intelligence |
|------|---------------------------|------------------------------|
| 具身假设、传感器、仿真环境 | 01-foundations | — |
| 机器人视觉感知（场景理解、目标跟踪） | 02-perception | 通用视觉方法放 `cv/` |
| 模仿学习、Sim-to-Real | 03-motor-control-and-policies | 模仿学习的通用 RL 理论放 `reinforce-learning/` |
| 路径规划、任务规划 | 04-planning-and-navigation | LLM 规划（CoT、ToT）放 `agentic/02-single-agent/planning/` |
| 人机交互（物理） | 05-manipulation/human-robot-interaction | 数字人机交互放 `agentic/04-human-agent-interaction/` |
| VLA 模型、机器人基础模型 | 06-foundation-models | 通用多模态 LLM 放 `llm/07-multimodal/` |
| 具身世界模型 | 06-foundation-models | 世界模型原理放 `world-models/` |

## 目录结构

```
embodied-intelligence/
├── 01-foundations/                    # 基础
│   ├── embodiment-hypothesis/         # 具身假设
│   ├── sensors-and-actuators/         # 传感器与执行器
│   └── simulation-environments/       # 仿真环境
│
├── 02-perception/                     # 感知闭环
│   ├── object-detection-and-tracking/ # 目标检测与跟踪
│   ├── 3d-scene-understanding/        # 3D场景理解
│   └── tactile-and-multimodal-sensing/ # 触觉与多模态感知
│
├── 03-motor-control-and-policies/     # 运动控制与策略
│   ├── imitation-learning/            # 模仿学习
│   ├── reinforcement-learning-for-robotics/ # 机器人强化学习
│   └── sim-to-real-transfer/          # Sim-to-Real迁移
│
├── 04-planning-and-navigation/        # 规划与导航
│   ├── path-planning/                 # 路径规划
│   ├── task-and-motion-planning/      # 任务与运动规划
│   └── llm-based-planning/            # LLM驱动规划
│
├── 05-manipulation/                   # 操作与交互
│   ├── grasping/                      # 抓取
│   ├── dexterous-manipulation/        # 灵巧操作
│   └── human-robot-interaction/       # 人机交互
│
├── 06-foundation-models/              # 大模型驱动具身
│   ├── vision-language-action-models/ # VLA模型
│   ├── foundation-models-for-robotics/ # 机器人基础模型
│   └── language-conditioned-policies/  # 语言条件策略
│
└── 07-evaluation-and-benchmarks/      # 评估与基准
    ├── standardized-tasks/            # 标准化任务
    └── robust-evaluation/             # 鲁棒评估
```

## 学习路径

**基础阶段**
- `01-foundations/` — 具身假设、传感器、仿真环境
- `02-perception/` — 感知闭环

**核心阶段**
- `03-motor-control-and-policies/` — 运动控制与策略
- `04-planning-and-navigation/` — 规划与导航
- `05-manipulation/` — 操作与交互

**大模型驱动**
- `06-foundation-models/` — VLA 模型、基础模型

**评估与实践**
- `07-evaluation-and-benchmarks/` — 标准化任务、鲁棒评估

## 快速导航

- **技术总结**: [`overview.md`](./overview.md)

## 与其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| 机器人视觉感知 | [../cv/](../cv/) | CV 提供通用视觉方法，本目录聚焦机器人场景 |
| 机器人 RL | [../reinforce-learning/](../reinforce-learning/) | RL 提供算法原理，本目录聚焦机器人控制应用 |
| LLM 驱动规划 | [../agentic/02-single-agent/planning/](../agentic/02-single-agent/planning/) | Agent 规划是数字层面，具身规划需要物理约束 |
| 物理人机交互 | [../agentic/04-human-agent-interaction/](../agentic/04-human-agent-interaction/) | 数字人机交互在 agentic，物理人机交互在本目录 |
| VLA/机器人基础模型 | [../llm/07-multimodal/](../llm/07-multimodal/) | 通用多模态 LLM 在 llm，具身专用模型在本目录 |
| 具身世界模型 | [../world-models/04-large-scale-world-models/embodied-world-models/](../world-models/04-large-scale-world-models/embodied-world-models/) | 世界模型原理在 world-models |
| 具身假设与哲学 | [../interdisciplinarity/03-philosophy-of-mind/](../interdisciplinarity/03-philosophy-of-mind/) | 具身认知的哲学基础 |

---

*最后更新: 2026-05-11*
