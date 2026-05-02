# 传统机器学习 (Traditional Machine Learning)

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

## 与深度学习的关系

传统机器学习方法是深度学习的基础，很多概念直接延续：
- 正则化（L1/L2）→ 深度学习中的 dropout、权重衰减
- 梯度下降 → 神经网络优化
- PCA → 自编码器的线性特例
- 集成学习 → 深度学习中的模型集成

---

*最后更新: 2026-05-02*
