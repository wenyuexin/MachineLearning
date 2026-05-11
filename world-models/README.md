# 世界模型 (World Models)

环境的内部模拟器：使智能系统能够预测未来状态、理解因果关系，并在不依赖真实交互的情况下做出决策。

## 分类依据

World Models 目录按"基础 → 方法架构 → 推理 → 大规模模型 → 评估 → 应用"组织：

- **01（基础）**：世界模型的定义与动机、RL 中的预测模型、潜动态学习
- **02（方法与架构）**：Dreamer 系列、自回归/扩散世界模型、JEPA 与能量模型
- **03（推理用世界模型）**：基于模型的规划、因果世界模型
- **04（大规模世界模型）**：视频预测、Sora 与视频生成、具身世界模型
- **05（评估）**：预测指标、下游任务迁移
- **06（应用）**：机器人仿真、自动驾驶、游戏与 AGI 探索

## 边界说明

| 内容 | 适合放 World Models | 不适合放 World Models |
|------|-------------------|----------------------|
| 潜动态模型、Dreamer 架构 | 02-methods-and-architectures | Dreamer 的 RL 训练细节放 `reinforce-learning/04-model-based-rl/` |
| 视频预测与生成（Sora 等） | 04-large-scale-world-models | 视频理解（动作识别等）放 `cv/04-video-and-3d-vision/` |
| 基于模型的规划 | 03-reasoning-models | LLM 推理/CoT 放 `llm/` |
| 因果世界模型 | 03-reasoning-models | 通用因果推理放 `interdisciplinarity/` |
| 机器人仿真 | 06-applications/robotics-simulation | 机器人感知与控制放 `embodied-intelligence/` |
| 图像生成（SD、DALL-E） | — | 放 `cv/05-generative-and-multimodal/` |
| 扩散模型原理 | — | 放 `deep-learning/03-architectures/generative-models/` |

## 目录结构

```
world-models/
├── 01-foundations/                   # 基础
│   ├── definition-and-motivation/    # 定义与动机
│   ├── predictive-models-in-rl/      # RL中的预测模型
│   └── learning-latent-dynamics/     # 潜动态学习
│
├── 02-methods-and-architectures/     # 方法与架构
│   ├── dreamer-family/               # Dreamer系列
│   │   ├── dreamerv1-v2/             # DreamerV1/V2
│   │   └── dreamerv3/                # DreamerV3
│   ├── autoregressive-world-models/  # 自回归世界模型
│   ├── diffusion-world-models/       # 扩散世界模型
│   └── jepa-and-energy-based-models/ # JEPA与能量模型
│
├── 03-reasoning-models/              # 推理用世界模型
│   ├── model-based-planning/         # 基于模型的规划
│   └── causal-world-models/          # 因果世界模型
│
├── 04-large-scale-world-models/      # 大规模世界模型
│   ├── video-prediction-models/      # 视频预测模型
│   ├── sora-and-video-generation/    # Sora与视频生成
│   └── embodied-world-models/        # 具身世界模型
│
├── 05-evaluation/                    # 评估
│   ├── prediction-metrics/           # 预测指标
│   └── downstream-task-transfer/     # 下游任务迁移
│
└── 06-applications/                  # 应用
    ├── robotics-simulation/          # 机器人仿真
    ├── autonomous-driving/           # 自动驾驶
    └── game-play-and-agi-exploration/ # 游戏与AGI探索
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

## 与其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| Dreamer/MBRL 架构 | [../reinforce-learning/04-model-based-rl/](../reinforce-learning/04-model-based-rl/) | RL 侧的训练与应用细节 |
| 视频预测与生成 | [../cv/04-video-and-3d-vision/](../cv/04-video-and-3d-vision/) | CV 侧重视频理解，WM 侧重视频预测/生成 |
| 扩散模型原理 | [../deep-learning/03-architectures/generative-models/](../deep-learning/03-architectures/generative-models/) | 扩散模型的通用架构原理 |
| 具身世界模型 | [../embodied-intelligence/06-foundation-models/](../embodied-intelligence/06-foundation-models/) | 具身智能中的世界模型应用 |
| 因果推理 | [../interdisciplinarity/](../interdisciplinarity/) | 因果推断的跨学科视角 |

---

*最后更新: 2026-05-11*
