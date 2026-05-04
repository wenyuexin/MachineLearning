# LLM 可解释性 (Explainability)

## 通用方法论（本目录）

| 子方向 | 内容 |
|--------|------|
| [mechanistic/](./mechanistic/) | 机制可解释性：电路分析、注意力头功能、神经元解释 |
| [attribution/](./attribution/) | 归因方法：梯度归因、显著性分析、SHAP、LIME |
| [probing/](./probing/) | 探测技术：线性探测、表示几何、跨层相似性分析 |
| [counterfactual/](./counterfactual/) | 反事实解释：概念解释、TCAV、因果中介分析 |

## 应用研究（其他目录索引）

| 主题 | 位置 |
|------|------|
| CoT 忠实性 | [../inference/prompt-engineering/](../inference/prompt-engineering/) |
| 不确定性诊断 | [../evaluation/calibration/](../evaluation/calibration/) |
| SFT 后的表征变化 | [../post-training/sft/](../post-training/sft/) |
| RLHF 对齐分析 | [../post-training/rlhf/](../post-training/rlhf/) |

## 开源仓库与工具存放指南

LLM 可解释性相关的开源仓库和工具，按方法论放入对应子目录：

| 工具/仓库功能 | 放入目录 | 示例 |
|-------------|---------|------|
| 机制可解释性（电路分析、注意力头） | `mechanistic/` | TransformerLens, Anthropic Circuits |
| 归因方法（梯度、显著性） | `attribution/` | Captum, Integrated Gradients |
| 探测与表征分析 | `probing/` | Ecco, LIT (Language Interpretability Tool) |
| 反事实与因果解释 | `counterfactual/` | TCAV, Concept Activation Vectors |

---

*最后更新: 2026-05-03*
