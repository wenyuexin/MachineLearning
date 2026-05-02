# 深度学习基础 (Deep Learning)

## 目录结构

```
deep-learning/
├── 01-neural-network-fundamentals/  # 神经网络基础
│   ├── perceptron-and-mlp/
│   ├── activation-functions/
│   └── loss-functions/
│
├── 02-training-and-optimization/    # 训练与优化
│   ├── backpropagation/
│   ├── gradient-descent-variants/
│   │   ├── sgd/
│   │   ├── adam/
│   │   └── learning-rate-schedules/
│   ├── regularization/
│   │   ├── l1-l2/
│   │   ├── dropout/
│   │   └── batch-normalization/
│   └── initialization-methods/
│
├── 03-architectures-by-domain/      # 按领域划分的架构
│   ├── cnns/                        # 卷积神经网络
│   ├── rnns-and-sequence-models/    # 循环神经网络与序列模型
│   ├── transformers/                # Transformer
│   └── generative-models/           # 生成模型
│       ├── gans/
│       ├── vaes/
│       └── diffusion-models/
│
├── 04-advanced-topics/              # 进阶主题
│   ├── self-supervised-learning/
│   ├── meta-learning/
│   ├── neural-architecture-search/
│   └── continual-learning/
│
└── 05-deep-learning-infra/          # 深度学习基础设施
    ├── gpu-computing/
    ├── distributed-training/
    └── framework-comparison/
```

## 学习路径

**基础阶段**
- `01-neural-network-fundamentals/` — 感知机、激活函数、损失函数
- `02-training-and-optimization/` — 反向传播、优化器、正则化

**进阶阶段**
- `03-architectures-by-domain/` — CNN、RNN、Transformer、生成模型

**深入阶段**
- `04-advanced-topics/` — 自监督学习、元学习、NAS、持续学习
- `05-deep-learning-infra/` — GPU计算、分布式训练、框架对比

## 与仓库其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| Transformer架构 | [../llm/01-foundations/transformer-architecture/](../llm/01-foundations/transformer-architecture/) | LLM基于Transformer扩展 |
| CNN/RNN | [../cv/02-image-classification/classic-backbones/](../cv/02-image-classification/classic-backbones/) | CV中的深度学习方法 |
| 训练技巧 | [../training-infra/](../training-infra/) | 分布式训练、显存优化 |
| Diffusion | [../cv/05-generative-and-multimodal/image-generation/](../cv/05-generative-and-multimodal/image-generation/) | 图像生成应用 |
| 生成模型 | [../world-models/04-large-scale-world-models/sora-and-video-generation/](../world-models/04-large-scale-world-models/sora-and-video-generation/) | 视频生成 |

---

*最后更新: 2026-05-02*
