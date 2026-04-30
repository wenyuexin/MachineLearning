# Sparse Autoencoders Find Highly Interpretable Features in Language Models

**会议**: ICLR 2024

**论文链接**: OpenReview (iclr.cc)

**arXiv**: 相关预印本

---

## 基本信息

| 属性 | 内容 |
|------|------|
| **研究目标** | 系统性验证 SAE 在语言模型中提取可解释特征的能力 |
| **模型范围** | Pythia 模型系列 (70M - 6.9B 参数) |
| **对比方法** | PCA, ICA, 其他基线 |

---

## 核心贡献

### 1. 系统性验证

在多个规模的 Pythia 模型上训练 SAE：
- 验证了 SAE 方法的可扩展性
- 特征质量随模型规模提升

### 2. 方法对比

| 方法 | 可解释性 | 重建质量 |
|------|----------|----------|
| SAE | **高** | 良好 |
| PCA | 低 | 高 |
| ICA | 中 | 中 |

### 3. 自动评估

开发了特征可解释性的自动评估方法：
- 使用大模型自动标注特征
- 量化特征的一致性和特异性

---

## 与 Anthropic 工作的关系

| 工作 | 关系 |
|------|------|
| **Towards Monosemanticity** | 本工作扩展验证至开源模型 |
| **Scaling Monosemanticity** | 后续更大规模的工作 |

---

## 关键引用

```bibtex
@inproceedings{huben2024sparse,
  title={Sparse Autoencoders Find Highly Interpretable Features in Language Models},
  author={Huben, Robert and Cunningham, Hoagy and Smith, Logan Riggs and Ewart, Aidan and Sharkey, Lee},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2024}
}
```

---

*文档创建: 2026-04-30*
