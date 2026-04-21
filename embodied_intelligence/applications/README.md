# 应用场景

本目录整理具身AI的应用场景和实践案例。

## 主要应用领域

### 1. 机器人操作

最核心的应用领域。

| 任务类型 | 描述 | 挑战 |
|----------|------|------|
| 抓取与放置 | 基础操作能力 | 物体多样性、遮挡 |
| 组装任务 | 多步骤精确操作 | 精度要求高、顺序依赖 |
| 柔性物体操作 | 布料、绳索、食品 | 形变建模困难 |
| 工具使用 | 使用各种工具 | 工具种类多、使用方式复杂 |
| 双臂协作 | 双臂协同操作 | 协调控制复杂 |

### 2. 移动导航

| 任务类型 | 描述 | 代表工作 |
|----------|------|----------|
| 室内导航 | 家庭/办公环境导航 | 内心独白 |
| 户外导航 | 复杂室外环境 | - |
| 移动操作 | 导航+操作结合 | Mobile ALOHA |

### 3. 人机交互

| 场景 | 描述 |
|------|------|
| 服务机器人 | 餐厅、酒店、家庭服务 |
| 协作机器人 | 人机协作完成复杂任务 |
| 辅助机器人 | 老人护理、康复辅助 |

### 4. 工业应用

| 场景 | 描述 |
|------|------|
| 生产线装配 | 自动化装配任务 |
| 质量检测 | 视觉检测与分拣 |
| 物流仓储 | 货物搬运与分拣 |

### 5. 特殊场景

| 场景 | 描述 |
|------|------|
| 极端环境 | 太空、深海、核电站 |
| 医疗手术 | 手术机器人辅助 |
| 农业机器人 | 采摘、种植、监测 |

## 机器人平台

### 常用机械臂

| 平台 | 自由度 | 特点 |
|------|--------|------|
| Franka Emika Panda | 7 DoF | 研究常用，力控能力 |
| UR5/e系列 | 6 DoF | 工业应用广泛 |
| WidowX | 5 DoF | 低成本，教育研究 |
| Sawyer | 7 DoF | 单臂协作机器人 |
| ALOHA | 双臂 | 双臂操作研究 |

### 人形机器人

| 平台 | 特点 |
|------|------|
| Tesla Optimus | 全身人形 |
| Figure 01 | 商用人形 |
| Unitree H1 | 四足+上肢 |
| AgiBot | 多样化任务能力 |

## 基准测试

### 仿真基准

| 基准 | 任务数 | 评价维度 |
|------|--------|----------|
| RLBench | 100 | 多样化操作任务 |
| CALVIN | - | 长序列任务 |
| LIBERO | 130 | 终身学习 |
| Meta-World | 50 | 元学习 |

### 真实世界测试

| 测试场景 | 评价标准 |
|----------|----------|
| 桌面操作 | 任务成功率 |
| 厨房任务 | 长程任务完成率 |
| 真实环境泛化 | 新场景适应能力 |

## 开源项目

### VLA模型

| 项目 | 链接 | 特点 |
|------|------|------|
| OpenVLA | [github.com/openvla/openvla](https://github.com/openvla/openvla) | 开源VLA，Llama架构 |
| Octo | [github.com/octo-models/octo](https://github.com/octo-models/octo) | 开源通用策略，扩散 |

### 模仿学习

| 项目 | 链接 | 特点 |
|------|------|------|
| ACT | [github.com/MarkFzp/act-plus-plus](https://github.com/MarkFzp/act-plus-plus) | Action Chunking |
| Diffusion Policy | [github.com/real-stanford/diffusion_policy](https://github.com/real-stanford/diffusion_policy) | 扩散策略 |

### 世界模型

| 项目 | 链接 | 特点 |
|------|------|------|
| DreamerV3 | [github.com/danijar/dreamerv3](https://github.com/danijar/dreamerv3) | 通用世界模型 |
| DayDreamer | [github.com/danijar/daydreamer](https://github.com/danijar/daydreamer) | 机器人世界模型 |

### 数据集工具

| 项目 | 链接 | 特点 |
|------|------|------|
| Open X-Embodiment | [robotics-transformer-x.github.io](https://robotics-transformer-x.github.io) | 跨机器人数据 |
| BridgeData V2 | [rail-berkeley.github.io](https://rail-berkeley.github.io) | 多任务操作数据 |

## 参考资料

- 论文: `../papers/Robot_Manipulation_Foundation_Models_2512.22983.md`
- 论文: `../papers/VLA_Models_Survey_2508.15201.md`