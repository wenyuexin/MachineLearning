# 具身智能 (Embodied Intelligence)

本目录存放具身智能 (Embodied AI) 的研究笔记、论文精读和知识整理。

---

## 目录结构

```
embodied_intelligence/
├── papers/              # 论文精读笔记
│   ├── VLA_Models_Survey_2508.15201.md
│   ├── Robot_Manipulation_Foundation_Models_2512.22983.md
│   └── LM_Empowered_Embodied_AI_2508.10399.md
├── models/              # 模型架构整理
├── datasets/            # 数据集资源
├── learning_methods/    # 学习方法与训练范式
├── applications/        # 应用场景与实践
└── topics/              # 专题研究
    └── egocentric/      # Egocentric2Embodiment 论文集
```

---

## 核心概念速查

| 概念 | 定义 |
|------|------|
| **具身智能** | 具有物理形态的智能系统，通过与环境交互获得智能 |
| **VLA** | Vision-Language-Action，视觉-语言-动作模型 |
| **世界模型** | 环境的内部模拟器，用于预测和规划 |
| **模仿学习** | 从专家演示中学习策略 |
| **Sim-to-Real** | 仿真到真实的迁移 |

---

## 大模型分类

### 1. 大语言模型 (LLM)
- **代表**: GPT系列、LLaMA、Deepseek-R1
- **作用**: 高层任务规划、代码生成、知识推理

### 2. 多模态大语言模型 (MLLM/VLM)
- **代表**: GPT-4o、Gemini-1.5、Qwen-VL、CLIP
- **作用**: 跨模态理解，桥接视觉和语言

### 3. 视觉-语言-动作模型 (VLA)
- **代表**: RT-2、OpenVLA、Octo、π0、GR00T N1
- **作用**: 端到端从视觉语言输入直接输出机器人动作

### 4. 世界模型 (World Model)
- **代表**: DreamerV3、Sora、Cosmos
- **作用**: 预测未来状态，支持规划和学习

---

## 决策制定范式

### 分层决策 (Hierarchical)
```
感知层 → 高层规划(LLM/MLLM) → 底层执行(策略网络)
```
- **优势**: 模块化、可解释性强
- **代表**: Inner Monologue、Progprompt、VoxPoser

### 端到端决策 (End-to-End)
```
视觉+语言 → VLA模型 → 动作
```
- **优势**: 整体优化、部署简单
- **代表**: RT-2、OpenVLA、Octo、π0

---

## 学习方法

| 方法 | 核心思想 | 适用场景 |
|------|----------|----------|
| **模仿学习** | 从专家演示学习 | 数据充足、任务固定 |
| **强化学习** | 通过试错优化 | 动态环境、有明确目标 |
| **迁移学习** | 跨域知识迁移 | 有相关任务经验可复用 |
| **元学习** | 学会如何学习 | 需要快速适应新任务 |

---

## 数据金字塔

| 层级 | 数据类型 | 代表数据集 | 规模 |
|------|----------|-----------|------|
| L1 | 互联网图文 | WebLI | 10B |
| L2 | 视频数据 | Ego4D | 3670小时 |
| L3 | 仿真数据 | RLBench | 100任务 |
| L4 | 真实机器人 | OXE | 1M+轨迹 |

---

## 当前研究热点

### 1. Egocentric2Embodiment (2024-2026)
将人类第一人称视角视频转换为机器人训练数据

| 里程碑 | 论文 | 核心贡献 |
|--------|------|----------|
| 分层学习 | MimicPlay (CoRL 2023) | 人类视频学规划，机器人数据学执行 |
| 联合训练 | EgoMimic (2024) | 人类+机器人数据统一训练 |
| 零样本 | Phantom (CoRL 2025) | 零机器人数据训练 |
| 缩放定律 | EgoScale (2026) | 20K+小时验证对数线性缩放 (R²=0.9983) |
| 统一空间 | Being-H0.5 (ICLR 2026) | Human-Centric + 30形态统一动作空间 |
| 零样本迁移 | LAP (2026) | 语言-动作表示跨形态迁移 |

### 2. VLA模型发展

| 阶段 | 时间 | 核心问题 | 代表模型 |
|------|------|----------|----------|
| 萌芽期 | 2023.7前 | 如何让机器人听懂人话 | RT-1, CLIPort |
| 探索期 | 2023.7-2024 | 如何让机器人具备常识 | RT-2, Octo, OpenVLA |
| 发展期 | 2024至今 | 如何既聪明又快 | π0, GR00T, Hume |

---

## 当前挑战

1. **数据瓶颈**: 机器人数据量远小于互联网数据
2. **泛化能力**: 新场景、新任务适应困难
3. **实时性**: 大模型推理延迟
4. **安全性**: 真实环境交互风险
5. **Sim-to-Real**: 仿真到真实的迁移差距

---

## 未来方向

1. **数据飞轮**: 自主数据收集与优化
2. **多模态融合**: 触觉、力觉等信息整合
3. **分层架构**: 平衡泛化与实时性
4. **世界模型**: 更精确的环境模拟
5. **Human-Centric**: 以人为中心的训练范式

---

## 学习路径建议

```
阶段1: 基础知识
├── 深度学习基础
├── 强化学习基础
└── 机器人学基础

阶段2: 核心论文
├── RT-1, RT-2 (VLA基础)
├── Diffusion Policy (策略学习)
├── Dreamer系列 (世界模型)
└── MimicPlay, EgoMimic (Egocentric)

阶段3: 实践
├── 仿真环境实验 (RLBench/CALVIN)
├── 开源模型复现 (OpenVLA/Octo)
└── 真实机器人部署

阶段4: 研究
├── 特定问题深入
└── 创新方法探索
```

---

## 快速导航

- **论文精读**: [`papers/`](./papers/)
- **模型架构**: [`models/README.md`](./models/README.md)
- **数据集**: [`datasets/README.md`](./datasets/README.md)
- **学习方法**: [`learning_methods/README.md`](./learning_methods/README.md)
- **应用场景**: [`applications/README.md`](./applications/README.md)
- **Egocentric专题**: [`topics/egocentric/README.md`](./topics/egocentric/README.md)

---

*最后更新: 2026-04-22*
