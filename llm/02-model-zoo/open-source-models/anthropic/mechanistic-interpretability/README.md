# 机制可解释性 (Mechanistic Interpretability) 论文索引

**主题**: Transformer 语言模型的机制可解释性与稀疏自编码器 (SAE)

**创建日期**: 2026-04-30

---

## 概述

机制可解释性（Mechanistic Interpretability, MI）致力于逆向工程神经网络的内部计算机制，理解模型如何从输入表示逐步转换为输出预测。Anthropic 在该领域做出了奠基性贡献，特别是通过**稀疏自编码器 (Sparse Autoencoders, SAE)** 提取可解释的"单语义"特征 (monosemantic features)，突破了传统"多语义神经元" (polysemantic neurons) 的可解释性障碍。

---

## 论文列表

### 奠基性论文 (Anthropic Transformer Circuits)

| 论文 | 文档 | 来源 | 核心贡献 | 重要性 |
| --- | --- | --- | --- | --- |
| Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet | [`Scaling_Monosemanticity_Claude3_2024`](./Scaling_Monosemanticity_Claude3_2024.md) | Anthropic (2024) | 在大型语言模型 (Claude 3) 中提取数百万可解释特征 | ⭐⭐⭐ 里程碑 |
| Towards Monosemanticity: Decomposing Language Models With Dictionary Learning | [`Towards_Monosemanticity_2023`](./Towards_Monosemanticity_2023.md) | Anthropic (2023) | 提出字典学习方法分解模型，提取单语义特征 | ⭐⭐⭐ 必读 |
| Toy Models of Superposition | [`Toy_Models_Superposition_2022`](./Toy_Models_Superposition_2022.md) | arXiv:2209.10652 | 理论解释"叠加" (superposition) 现象：为什么神经元是多语义的 | ⭐⭐⭐ 理论基础 |
| A Mathematical Framework for Transformer Circuits | [`Mathematical_Framework_Transformer_Circuits_2021`](./Mathematical_Framework_Transformer_Circuits_2021.md) | Anthropic (2021) | Transformer 电路的数学框架，QK/OV 电路分解 | ⭐⭐⭐ 理论奠基 |
| Quantifying Tuning Effects in Language Models | [`Quantifying_Tuning_Effects_2024`](./Quantifying_Tuning_Effects_2024.md) | Anthropic (2024) | 量化微调对模型内部特征的影响 | ⭐⭐ 值得关注 |

### 稀疏自编码器 (SAE) 方法学

| 论文 | 文档 | 来源 | 核心方法 |
| --- | --- | --- | --- |
| Sparse Autoencoders Find Highly Interpretable Features in Language Models | [`SAE_Interpretable_Features_ICLR2024`](./SAE_Interpretable_Features_ICLR2024.md) | ICLR 2024 | SAE 提取可解释特征的系统性验证 |
| Gated Sparse Autoencoders | [`Gated_SAE_2024`](./Gated_SAE_2024.md) | arXiv:2404.16014 | 门控机制改进 SAE 训练，减少活性坍塌 |
| Improving Dictionary Learning with Gated Sparse Autoencoders | 待创建 | ICML 2024 | 门控 SAE 的改进版本 |
| Efficient Dictionary Learning with Switch Sparse Autoencoders | 待创建 | arXiv:2410.08201 | Switch SAE 提升效率 |

### 电路追踪与归因方法

| 论文 | 文档 | 来源 | 核心内容 |
| --- | --- | --- | --- |
| Circuit Tracing: Revealing Computational Graphs in Language Models | [`Circuit_Tracing_2025`](./Circuit_Tracing_2025.md) | Anthropic (2025) | 归因图方法追踪模型计算图 |
| Attribution Patching: Layer-Specific Interventions | 待创建 | Anthropic | 层级归因干预方法 |
| Activation Patching: A Unified View | 待创建 | Anthropic | 激活修补的统一视角 |

### 特征解释性与可视化

| 论文 | 文档 | 来源 | 核心内容 |
| --- | --- | --- | --- |
| Golden Gate Claude | [`Golden_Gate_Claude`](./Golden_Gate_Claude.md) | Anthropic Blog | 具体案例：激活 Golden Gate Bridge 特征 |
| Softmax Linear Units (SoLU) | [`SoLU_2022`](./SoLU_2022.md) | Anthropic (2022) | SoLU 激活函数提升特征可解释性 |
| Eliciting Latent Predictions from Transformers with the Tuned Lens | [`Tuned_Lens_2022`](./Tuned_Lens_2022.md) | arXiv:2303.08112 | 调整透镜读取中间层预测 |

### 其他重要工作

| 论文 | 文档 | 来源 | 核心内容 |
| --- | --- | --- | --- |
| Progress Measures for Grokking via Mechanistic Interpretability | [`Grokking_Measures_2023`](./Grokking_Measures_2023.md) | ICML 2023 | 用 MI 方法研究 grokking 现象 |
| Locating and Editing Factual Associations in GPT | [`ROME_2022`](./ROME_2022.md) | NeurIPS 2022 | 知识编辑的因果干预方法 |
| A Practical Review of Mechanistic Interpretability | [`MI_Practical_Review_2024`](./MI_Practical_Review_2024.md) | arXiv:2407.02646 | MI 领域实用综述 |

---

## 核心概念与术语

### 关键概念

| 术语 | 解释 |
|------|------|
| **Superposition (叠加)** | 神经网络将比维度更多的特征压缩存储在同一向量空间中的现象 |
| **Polysemanticity (多语义性)** | 单个神经元对多个不相关概念都有响应的特性 |
| **Monosemanticity (单语义性)** | 每个特征对应单一可解释概念的属性 |
| **Sparse Autoencoder (SAE)** | 稀疏自编码器，用于分解激活、提取可解释特征 |
| **Dictionary Learning** | 字典学习方法，将激活分解为稀疏线性组合 |
| **Circuit** | 模型中执行特定功能的子网络或计算路径 |
| **Activation Patching** | 干预方法：将一个输入的激活替换到另一个输入 |
| **Attribution Graph** | 归因图，显示特征间的计算依赖关系 |
| **Residual Stream** | Transformer 中的残差流，信息传递的主通道 |
| **QK Circuit / OV Circuit** | Query-Key 电路和 Output-Value 电路，注意力机制的分解 |

---

## 主题分类

### 按研究方向

```
Mechanistic Interpretability
├── 特征提取方法
│   ├── Sparse Autoencoders (SAE): Anthropic 主导方法
│   ├── Dictionary Learning: 数学基础
│   ├── PCA/ICA baselines: 对比基线
│   └── Gated SAE: 改进训练稳定性
│
├── 理论基础
│   ├── Superposition Theory: 为什么需要特征提取
│   ├── Toy Models: 简化模型中的理论分析
│   └── Computational Framework: Transformer 电路数学
│
├── 解释性分析方法
│   ├── Activation Patching: 因果干预
│   ├── Attribution Patching: 层级归因
│   ├── Circuit Tracing: 电路追踪
│   └── Logit Lens / Tuned Lens: 读取内部表示
│
└── 应用场景
    ├── Hallucination Detection: 幻觉检测
    ├── Jailbreak Analysis: 越狱攻击分析
    ├── Knowledge Editing: 知识编辑
    └── Steering: 模型行为引导
```

### 按阅读路线

```
入门路线
├── 1. Toy Models of Superposition (2022)
│      └── 理解"叠加"现象的理论基础
├── 2. A Mathematical Framework for Transformer Circuits (2021)
│      └── Transformer 电路的数学分解
└── 3. Towards Monosemanticity (2023)
       └── SAE 方法提取单语义特征

进阶路线
├── 4. Scaling Monosemanticity (2024)
│      └── 在 Claude 3 上的大规模验证
├── 5. Gated Sparse Autoencoders (2024)
│      └── SAE 训练技术改进
└── 6. Circuit Tracing (2025)
       └── 归因图与电路追踪方法

实践路线
├── 7. TransformerLens: 代码实现
├── 8. Neuronpedia: 特征可视化工具
└── 9. 复现 SAE 训练实验
```

---

## 工具与框架

| 工具 | 说明 | 链接 |
|------|------|------|
| **TransformerLens** | 机制可解释性分析库，支持激活修补、归因分析 | [GitHub](https://github.com/neelnanda-io/TransformerLens) |
| **SAELens** | 稀疏自编码器训练与分析工具 | [GitHub](https://github.com/jbloomAus/SAELens) |
| **Neuronpedia** | 可解释特征的可视化与搜索平台 | [neuronpedia.org](https://neuronpedia.org) |
| **Anthropic SAE** | Anthropic 开源的 Claude SAE 权重 | [GitHub](https://github.com/anthropics/anthropic-sae) |
| **nnsight** | 神经网络干预与解释库 | [GitHub](https://github.com/ndif-team/nnsight) |
| **pyvene** | 因果干预工具库 | [GitHub](https://github.com/stanfordnlp/pyvene) |

---

## 相关资源

### 官方资源

- **Transformer Circuits Thread**: https://transformer-circuits.pub/
- **Anthropic Research Blog**: https://www.anthropic.com/research
- **Neel Nanda's Mech Interp Guide**: https://neelnanda-io.github.io/

### arXiv 搜索

- Mechanistic Interpretability: https://arxiv.org/search/?query=mechanistic+interpretability
- Sparse Autoencoders: https://arxiv.org/search/?query=sparse+autoencoder+language+model
- Transformer Circuits: https://arxiv.org/search/?query=transformer+circuits

### 相关主题

- [LLM 校准与不确定性](../../evaluation/calibration/papers/) - 模型置信度评估
- [Anthropic Claude 概述](../Anthropic_Claude_Overview.md) - Claude 模型家族

---

## 更新日志

- 2026-04-30: 创建论文索引与目录结构
  - 添加 15+ 篇核心论文分类
  - 建立研究路线与工具索引
- 待添加: 核心论文详细文档
  - Scaling Monosemanticity
  - Towards Monosemanticity
  - Toy Models of Superposition
  - Mathematical Framework
  - Circuit Tracing

---

*最后更新: 2026-04-30*
