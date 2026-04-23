# MachineLearning

机器学习与人工智能学习笔记

## 目录结构

```
MachineLearning/
├── traditional_ml/              # 传统机器学习
│   ├── supervised/              # 监督学习
│   │   ├── classification/      # 分类算法（SVM、决策树、随机森林等）
│   │   └── regression/          # 回归算法（线性回归、岭回归等）
│   ├── unsupervised/            # 无监督学习
│   │   ├── clustering/          # 聚类算法（K-means、层次聚类、DBSCAN等）
│   │   └── dimensionality_reduction/  # 降维（PCA、t-SNE等）
│   └── ensemble/                # 集成学习（Bagging、Boosting、Stacking）
│
├── deep_learning/               # 深度学习基础
│   ├── architectures/           # 基础架构（CNN、RNN、Transformer等）
│   ├── foundations/             # 训练技巧、优化方法
│   └── generative/              # 生成模型（GAN、VAE、Diffusion）
│
├── cv/                          # 计算机视觉
│   ├── traditional/             # 传统方法（SIFT、HOG、Canny等）
│   ├── deep_learning/           # 深度学习方法
│   │   ├── architectures/       # 网络架构（ResNet、ViT等）
│   │   ├── classification/      # 图像分类
│   │   ├── detection/           # 目标检测（YOLO、Faster R-CNN等）
│   │   ├── segmentation/        # 图像分割（UNet、SAM等）
│   │   ├── pose_estimation/     # 姿态估计
│   │   ├── face/                # 人脸相关
│   │   ├── ocr/                 # 文字识别
│   │   ├── tracking/            # 目标跟踪
│   │   ├── 3d_vision/           # 3D视觉（NeRF、深度估计）
│   │   ├── video/               # 视频理解
│   │   └── generative/          # 图像生成（Stable Diffusion等）
│   └── applications/            # 应用场景（自动驾驶、医学影像等）
│
├── llm/                         # 大语言模型
│   ├── architectures/           # 模型架构（GPT、LLaMA等）
│   ├── pretraining/             # 预训练
│   ├── sft/                     # 监督微调
│   ├── dpo/                     # 直接偏好优化
│   ├── rlhf/                    # 人类反馈强化学习
│   ├── prompt/                  # Prompt工程
│   └── inference/               # 推理优化
│       └── decoding/            # 解码策略
│
├── reinforce_learning/          # 强化学习
│   ├── fundation/               # 基础理论
│   └── policy_otimization/      # 策略优化（PPO、TRPO等）
│
├── agentic/                     # AI智能体
│   ├── 00-overview/             # 概述
│   ├── 01-foundations/          # 基础
│   ├── 02-core-capabilities/    # 核心能力
│   ├── 03-architectures/        # 架构
│   ├── 04-memory-and-tools/     # 记忆与工具
│   ├── 05-multi-agent/          # 多智能体
│   ├── 06-applications/         # 应用
│   ├── 07-evaluation-and-safety/# 评估与安全
│   ├── 08-projects/             # 项目实践
│   └── 09-papers/               # 论文笔记
│
├── embodied_intelligence/       # 具身智能
│   ├── applications/            # 应用场景
│   ├── datasets/                # 数据集
│   ├── learning_methods/        # 学习方法
│   ├── models/                  # 模型
│   ├── papers/                  # 论文
│   └── topics/                  # 细分主题
│
├── world_models/                # 世界模型
│
├── knowledge_graph/             # 知识图谱
│
├── training_infra/              # 训练基础设施
│
├── learning_materials/          # 学习资料
│
└── assets/                      # 资源文件
    ├── images/                  # 图片
    ├── scripts/                 # 脚本
    └── test/                    # 测试
```

## 层级关系

```
层级 1：基础模型
└── LLM：语言智能核心

层级 2：学习范式（跨领域方法）
└── Reinforce Learning：通过交互学习

层级 3：应用形态
└── Agentic：LLM驱动的自主智能体

层级 4：物理落地
└── Embodied Intelligence：智能体 + 物理身体

横向支撑：
└── World Models：环境建模与预测
```

## 学习路线

待更新...

## 声明

如需转载，请注明出处