# Machine Learning

机器学习与人工智能学习笔记

## 目录结构

```
machine-learning/
│
├── traditional-ml/              # 传统机器学习
│   ├── supervised/              # 监督学习
│   │   ├── classification/      # 分类（SVM、决策树等）
│   │   └── regression/          # 回归（线性回归、岭回归等）
│   ├── unsupervised/            # 无监督学习
│   │   ├── clustering/          # 聚类（K-means、DBSCAN等）
│   │   └── dimensionality-reduction/  # 降维（PCA、t-SNE等）
│   ├── semi-supervised/         # 半监督学习
│   │   ├── self-training/       # 自训练
│   │   ├── co-training/         # 协同训练
│   │   ├── pseudo-labeling/     # 伪标签
│   │   └── consistency-regularization/  # 一致性正则化
│   ├── self-supervised/         # 自监督学习
│   │   ├── contrastive-learning/  # 对比学习
│   │   ├── masked-modeling/     # 掩码预测
│   │   └── pretext-tasks/       # 代理任务
│   ├── ensemble/                # 集成学习（Bagging、Boosting、Stacking）
│   ├── probabilistic/           # 概率图模型
│   │   ├── bayesian-networks/   # 贝叶斯网络
│   │   ├── hmm/                 # 隐马尔可夫模型
│   │   ├── crf/                 # 条件随机场
│   │   └── gaussian-processes/  # 高斯过程
│   ├── kernel-methods/          # 核方法
│   │   ├── kernel-trick/        # 核技巧
│   │   ├── kernel-pca/          # 核PCA
│   │   └── rkhs/                # 再生核希尔伯特空间
│   ├── feature-engineering/     # 特征工程
│   │   ├── feature-selection/   # 特征选择
│   │   ├── feature-extraction/  # 特征提取
│   │   └── encoding/            # 编码方法
│   ├── model-selection/         # 模型选择与评估
│   │   ├── cross-validation/    # 交叉验证
│   │   ├── hyperparameter-tuning/  # 超参搜索
│   │   └── evaluation-metrics/  # 评估指标
│   └── time-series/             # 时间序列
│       ├── arima/               # ARIMA
│       ├── exponential-smoothing/  # 指数平滑
│       ├── prophet/             # Prophet
│       └── anomaly-detection/   # 异常检测
│
├── deep-learning/               # 深度学习基础
│   ├── architectures/           # 基础架构（CNN、RNN、Transformer等）
│   ├── foundations/             # 训练技巧、优化方法
│   └── generative/              # 生成模型（GAN、VAE、Diffusion）
│
├── cv/                          # 计算机视觉
│   ├── traditional/             # 传统方法（SIFT、HOG、Canny等）
│   ├── deep-learning/           # 深度学习方法
│   │   ├── architectures/       # 网络架构（ResNet、ViT等）
│   │   ├── classification/      # 图像分类
│   │   ├── detection/           # 目标检测（YOLO、Faster R-CNN等）
│   │   ├── segmentation/        # 图像分割（UNet、SAM等）
│   │   ├── pose-estimation/     # 姿态估计
│   │   ├── face/                # 人脸相关
│   │   ├── ocr/                 # 文字识别
│   │   ├── tracking/            # 目标跟踪
│   │   ├── 3d-vision/           # 3D视觉（NeRF、深度估计）
│   │   ├── video/               # 视频理解
│   │   └── generative/          # 图像生成（Stable Diffusion等）
│   └── applications/            # 应用场景（自动驾驶、医学影像等）
│
├── llm/                         # 大语言模型
│   ├── architectures/           # 基础架构（Transformer、Attention、MoE等）
│   ├── models/                  # 开源模型技术报告
│   │   ├── gpt/                 # GPT系列
│   │   ├── llama/               # LLaMA系列
│   │   ├── qwen/                # Qwen系列
│   │   ├── deepseek/            # DeepSeek系列
│   │   ├── mistral/             # Mistral系列
│   │   └── gemma/               # Gemma系列
│   ├── pre-training/            # 预训练
│   │   └── tokenization/        # 分词
│   ├── post-training/           # 后训练（SFT + 对齐）
│   │   ├── sft/                 # 监督微调
│   │   ├── dpo/                 # 直接偏好优化
│   │   └── rlhf/                # 人类反馈强化学习
│   ├── inference/               # 推理与使用
│   │   ├── prompt-engineering/  # Prompt工程
│   │   └── decoding/            # 解码策略
│   ├── explainability/          # 可解释性
│   │   ├── mechanistic/         # 机制可解释性
│   │   ├── attribution/         # 归因方法
│   │   ├── probing/             # 探测技术
│   │   └── counterfactual/      # 反事实解释
│   ├── evaluation/              # 模型评估
│   │   ├── benchmarks/          # 综合评估基准
│   │   ├── calibration/         # 校准与不确定性量化
│   │   ├── reasoning/           # 推理能力评估
│   │   ├── safety/              # 安全评估
│   │   └── generation/          # 生成质量评估
│   └── multimodal/              # 多模态大模型
│       ├── vlm/                 # 视觉语言模型
│       ├── audio/               # 音频语言模型
│       ├── video/               # 视频语言模型
│       └── any2any/             # 全模态模型
│
├── reinforce-learning/          # 强化学习
│   ├── fundation/               # 基础理论
│   └── policy-optimization/     # 策略优化（PPO、TRPO等）
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
├── embodied-intelligence/       # 具身智能
│   ├── applications/            # 应用场景
│   ├── datasets/                # 数据集
│   ├── learning-methods/        # 学习方法
│   ├── models/                  # 模型
│   ├── papers/                  # 论文
│   └── topics/                  # 细分主题
│
├── world-models/                # 世界模型
│   ├── foundations/             # 基础理论
│   ├── architectures/           # 模型架构
│   ├── algorithms/              # 核心算法（Dreamer、MuZero等）
│   ├── applications/            # 应用场景
│   ├── video-generation/        # 视频生成（Sora、Genie等）
│   ├── training/                # 训练方法
│   └── papers/                  # 论文笔记
│
├── knowledge-graph/             # 知识图谱
│   ├── foundations/             # 基础理论
│   ├── knowledge-representation/# 知识表示（RDF、OWL、属性图）
│   ├── knowledge-extraction/    # 知识抽取（NER、关系抽取）
│   ├── knowledge-fusion/        # 知识融合（实体对齐、消解）
│   ├── knowledge-storage/       # 知识存储（Neo4j、SPARQL）
│   ├── knowledge-reasoning/     # 知识推理
│   ├── knowledge-graph-construction/  # 知识图谱构建
│   ├── llm-kg-integration/      # LLM与知识图谱结合（GraphRAG）
│   ├── datasets/                # 数据集（Freebase、Wikidata）
│   ├── tools/                   # 工具与框架
│   └── papers/                  # 论文笔记
│
├── training-infra/              # 训练基础设施
│   ├── distributed-training/    # 分布式训练
│   ├── optimization/            # 训练优化
│   ├── frameworks/              # 训练框架（Megatron、DeepSpeed等）
│   ├── hardware/                # 硬件相关
│   ├── memory-management/       # 显存管理
│   ├── fault-tolerance/         # 容错机制
│   └── communication/           # 通信优化
│
├── learning-materials/          # 学习资料
│
└── assets/                     # 资源文件
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

## 声明

- 📢 如需转载，请注明出处

- 🏗️ 个人的学习仓库，目录建得很全，但是不确定什么时候填坑