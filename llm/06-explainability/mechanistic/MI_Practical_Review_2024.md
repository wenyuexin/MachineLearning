# A Practical Review of Mechanistic Interpretability for Transformer-based Language Models

**论文链接**: arXiv:2407.02646

**发布日期**: 2024年7月

**研究机构**: 马里兰大学等

---

## 基本信息

| 属性 | 内容 |
|------|------|
| **类型** | 综述论文 |
| **目标读者** | 希望进入 MI 领域的研究人员 |
| **覆盖范围** | Transformer MI 的核心方法和工具 |

---

## 主要内容

### 1. 方法论综述

| 方法 | 描述 | 工具 |
|------|------|------|
| Activation Patching | 激活修补 | TransformerLens |
| Attribution Patching | 归因修补 | TransformerLens |
| Gradient-based Attribution | 梯度归因 | Captum, Ecco |
| SAE-based Analysis | 基于 SAE 的分析 | SAELens |
| Probing | 探针分析 | 自定义实现 |

### 2. 工具生态系统

| 工具 | 用途 |
|------|------|
| TransformerLens | 激活修补、电路分析 |
| SAELens | SAE 训练与分析 |
| Neuronpedia | 特征可视化 |
| nnsight | 通用干预框架 |

### 3. 挑战与未来方向

- 规模扩展：大型模型的 MI 分析
- 自动化：减少人工解释依赖
- 因果性：从相关性到因果性
- 标准化：评估指标的统一

---

## 关键引用

```bibtex
@article{rai2024practical,
  title={A Practical Review of Mechanistic Interpretability for Transformer-based Language Models},
  author={Rai, Daking and Zhou, Yilun and Feng, Shi and Saparov, Abulhair and Yao, Ziyu},
  journal={arXiv preprint arXiv:2407.02646},
  year={2024}
}
```

---

*文档创建: 2026-04-30*
