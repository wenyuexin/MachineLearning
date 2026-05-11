# 传统机器学习 (Traditional Machine Learning)

经典机器学习方法：从数学基础到监督/无监督学习、实践方法、时序分析与概率图模型。

## 分类依据

Traditional ML 目录按"基础 → 核心方法 → 实践 → 专项"组织：

- **01（数学基础）**：线性代数、概率论与统计、优化理论
- **02（监督学习）**：线性模型、树模型、SVM、KNN
- **03（无监督学习）**：聚类、降维
- **04（实践方法）**：特征工程、模型选择与调优、集成方法、不平衡学习、可解释性
- **05（时间序列）**：经典方法、机器学习方法、深度学习时序
- **06（概率图模型）**：贝叶斯网络、马尔可夫随机场

## 边界说明

| 内容 | 适合放 Traditional ML | 不适合放 Traditional ML |
|------|----------------------|------------------------|
| 数学基础（线代、概率、优化） | 01-fundamentals | 深度学习专用优化（Adam、学习率调度）放 `deep-learning/02-training-and-optimization/` |
| 线性回归、逻辑回归、树模型、SVM | 02-supervised-learning | 神经网络分类器放 `deep-learning/` |
| K-Means、PCA、t-SNE | 03-unsupervised-learning | 自编码器放 `deep-learning/03-architectures/generative-models/` |
| 特征工程、模型调优、集成方法 | 04-practical-ml | 深度学习调优（超参搜索、混合精度）放 `deep-learning/02-training-and-optimization/` |
| 经典时序方法（ARIMA、指数平滑） | 05-time-series | 纯深度学习时序模型（Transformer 时序）放 `deep-learning/` |
| 贝叶斯网络、马尔可夫随机场 | 06-probabilistic-graphical-models | 概率编程框架放 `deep-learning/04-advanced-topics/` |

## 目录结构

```
traditional-ml/
├── 01-fundamentals/             # 数学基础
│   ├── linear-algebra/          # 线性代数
│   ├── probability-and-statistics/  # 概率论与统计
│   └── optimization/            # 优化理论
│
├── 02-supervised-learning/      # 监督学习
│   ├── linear-models/           # 线性模型
│   ├── tree-based-models/       # 树模型
│   ├── svm/                     # 支持向量机
│   └── knn/                     # K近邻
│
├── 03-unsupervised-learning/    # 无监督学习
│   ├── clustering/              # 聚类算法
│   └── dimensionality-reduction/  # 降维方法
│
├── 04-practical-ml/             # 实践方法
│   ├── feature-engineering/     # 特征工程
│   ├── model-selection-and-tuning/  # 模型选择与调优
│   ├── ensemble-methods/        # 集成方法
│   ├── imbalanced-learning/     # 不平衡学习
│   └── interpretability/        # 可解释性
│
├── 05-time-series/              # 时间序列
│   ├── classical-methods/       # 经典方法
│   ├── machine-learning-approaches/  # 机器学习方法
│   └── deep-learning-for-ts/    # 深度学习时序
│
└── 06-probabilistic-graphical-models/  # 概率图模型
    ├── bayesian-networks/       # 贝叶斯网络
    └── markov-random-fields/    # 马尔可夫随机场
```

## 学习路径

**基础阶段**
- `01-fundamentals/` — 数学基础（线性代数、概率论、优化）
- `02-supervised-learning/` — 掌握分类和回归的基本算法
- `03-unsupervised-learning/` — 了解聚类和降维方法

**进阶阶段**
- `04-practical-ml/` — 特征工程、模型选择与调优、集成方法

**深入阶段**
- `05-time-series/` — 时序分析专项
- `06-probabilistic-graphical-models/` — 概率图模型

## 与其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| 正则化（L1/L2） | [../deep-learning/02-training-and-optimization/](../deep-learning/02-training-and-optimization/) | DL 中的 dropout、权重衰减是正则化的延伸 |
| 梯度下降 | [../deep-learning/02-training-and-optimization/](../deep-learning/02-training-and-optimization/) | DL 优化器的起点 |
| PCA | [../deep-learning/03-architectures/](../deep-learning/03-architectures/) | 自编码器是 PCA 的非线性推广 |
| 集成学习 | [../deep-learning/](../deep-learning/) | DL 中的模型集成、MoE 是集成思想的延续 |
| 树模型 | [../llm/02-models/](../llm/02-models/) | GBDT/XGBoost 仍广泛用于 LLM 评估的特征工程 |
| 概率图模型 | [../knowledge-graph/01-foundations/](../knowledge-graph/01-foundations/) | 贝叶斯网络是知识图谱推理的基础 |
| 时序分析 | [../deep-learning/](../deep-learning/) | 深度学习时序模型在 `05-time-series/deep-learning-for-ts/` |

---

*最后更新: 2026-05-11*
