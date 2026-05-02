# 传统机器学习 (Traditional Machine Learning)

## 目录结构

```
traditional-ml/
├── supervised/                # 监督学习
│   ├── classification/        # 分类（SVM、决策树、随机森林等）
│   └── regression/            # 回归（线性回归、岭回归、Lasso等）
│
├── unsupervised/              # 无监督学习
│   ├── clustering/            # 聚类（K-means、DBSCAN、层次聚类等）
│   └── dimensionality-reduction/  # 降维（PCA、t-SNE、UMAP等）
│
├── semi-supervised/           # 半监督学习
│   ├── self-training/         # 自训练
│   ├── co-training/           # 协同训练
│   ├── pseudo-labeling/       # 伪标签
│   └── consistency-regularization/  # 一致性正则化
│
├── self-supervised/           # 自监督学习
│   ├── contrastive-learning/  # 对比学习
│   ├── masked-modeling/       # 掩码预测
│   └── pretext-tasks/         # 代理任务
│
├── ensemble/                  # 集成学习
│   # Bagging、Boosting、Stacking
│
├── probabilistic/             # 概率图模型
│   ├── bayesian-networks/     # 贝叶斯网络
│   ├── hmm/                   # 隐马尔可夫模型
│   ├── crf/                   # 条件随机场
│   └── gaussian-processes/    # 高斯过程
│
├── kernel-methods/            # 核方法
│   ├── kernel-trick/          # 核技巧
│   ├── kernel-pca/            # 核PCA
│   └── rkhs/                  # 再生核希尔伯特空间
│
├── feature-engineering/       # 特征工程
│   ├── feature-selection/     # 特征选择
│   ├── feature-extraction/    # 特征提取
│   └── encoding/              # 编码方法
│
├── model-selection/           # 模型选择与评估
│   ├── cross-validation/      # 交叉验证
│   ├── hyperparameter-tuning/ # 超参搜索
│   └── evaluation-metrics/    # 评估指标
│
└── time-series/               # 时间序列
    ├── arima/                 # ARIMA
    ├── exponential-smoothing/ # 指数平滑
    ├── prophet/               # Prophet
    └── anomaly-detection/     # 异常检测
```

## 学习路径

**基础阶段**
- `supervised/` — 掌握分类和回归的基本算法
- `unsupervised/` — 了解聚类和降维方法
- `feature-engineering/` — 学会处理特征

**进阶阶段**
- `ensemble/` — 集成方法提升模型性能
- `model-selection/` — 掌握评估和调参技巧
- `semi-supervised/` / `self-supervised/` — 利用未标注数据

**深入阶段**
- `probabilistic/` — 概率图模型
- `kernel-methods/` — 核方法与非线性建模
- `time-series/` — 时序分析专项

## 与深度学习的关系

传统机器学习方法是深度学习的基础，很多概念直接延续：
- 正则化（L1/L2）→ 深度学习中的 dropout、权重衰减
- 梯度下降 → 神经网络优化
- PCA → 自编码器的线性特例
- 集成学习 → 深度学习中的模型集成

---

*最后更新: 2026-05-02*
