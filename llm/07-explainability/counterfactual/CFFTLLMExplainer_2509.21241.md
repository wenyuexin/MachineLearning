---
title: "Explaining Fine-Tuned LLMs via Counterfactuals: A Knowledge Graph-Driven Framework"
skill: paper
domain: nlp, xai, knowledge-graph
purpose: "追踪基于反事实的知识图谱解释微调LLM机制的前沿方法"
sources:
  - "arxiv/2509.21241"
tags: [counterfactual, LoRA, explainability, knowledge-graph, fine-tuning, interpretability]
created: 2026-05-04
updated: 2026-05-04
status: draft
---

# Explaining Fine-Tuned LLMs via Counterfactuals: A Knowledge Graph-Driven Framework

> **一句话总结**：本文提出 CFFTLLMExplainer，一种基于反事实的知识图谱驱动框架，通过最小结构扰动诱导最大语义分歧，揭示 LoRA 微调后 LLM 的内部结构依赖与参数偏移机制，填补了现有注意力解释方法在结构语义对齐上的空白。

## 基本信息
- **作者**：Yucheng Wang, Ziyang Chen, Md Faisal Kabir
- **机构**：Penn State Harrisburg
- **发表**：KDD 2025 Structured Knowledge for Large Language Models Workshop (non-archival)  |  arXiv: 2509.21241
- **链接**：[Paper](https://arxiv.org/abs/2509.21241)
- **领域**：XAI, NLP, Knowledge Graph, Fine-tuning Interpretability

## 1. 问题与动机
- **核心问题**：LoRA（Low-Rank Adaptation）微调后的 LLM 如何改变其结构推理和语义行为？现有方法（如梯度解释、注意力可视化）难以揭示微调后模型对输入图结构的深层依赖关系。
- **现有方法的不足**：
  1. **注意力机制的误导性**：注意力权重往往不能反映真实语义重要性（本文实验发现被移除的关键节点 Scallop 注意力权重极低，低于 0.002）。
  2. **缺乏结构感知**：现有解释方法多基于 token 级别，忽略了知识图谱的拓扑结构和关系语义。
  3. **无法解释微调机制**：LoRA 引入的低秩参数偏移如何影响模型对结构信息的利用尚不明确。
- **本文动机**：构建一个与 LLM 训练过程解耦的反事实解释框架，通过结构化输入的最小扰动，探测微调后模型的内部决策机制，并提供可验证的、与 LoRA 参数偏移对齐的解释信号。

## 2. 背景与相关工作
- **技术脉络**：
  1. **LLM 微调与 LoRA**：LoRA 通过低秩矩阵 $A \in \mathbb{R}^{d \times r}$ 和 $B \in \mathbb{R}^{r \times k}$ 近似参数更新 $W = W_0 + \alpha \cdot AB$，大幅降低了微调成本。
  2. **反事实解释（Counterfactual Explanation）**：在图神经网络中，反事实解释通过寻找最小的图结构修改来改变模型预测。本文将其扩展到生成式 LLM 的语义输出空间。
  3. **知识图谱增强 LLM**：通过 RAG 或图注入提升 LLM 的事实性和可控性，但现有方法常因图谱噪声导致幻觉或提取不准确子图。
  4. **LLM 可解释性**：梯度方法（如 Integrated Gradients）、注意力可视化、概念瓶颈层（CB-LLMs）等，但多聚焦输入-输出关联，缺乏对微调内部机制的解释。
- **与现有工作的关系**：
  | 相关工作 | 与本文的关系 |
  |----------|--------------|
  | 梯度/注意力解释方法 | 对比对象：本文证明注意力权重与结构重要性存在显著错位 |
  | GNN 反事实解释 | 思想借鉴：将图级反事实从判别任务扩展到生成式 LLM 语义空间 |
  | LoRA 微调研究 | 基础支撑：本文解释对象即为 LoRA 微调后的参数偏移 |
  | 概念瓶颈 LLM (CB-LLMs) | 对比对象：CB-LLMs 提升人类可解释性但缺乏与内部决策的对齐 |

## 3. 方法

### 3.1 核心思想（直觉解释）
- **直觉类比**：想象一个生物信息学专家（微调后的 LLM）根据实验流程图（知识图谱）推荐分析工具。CFFTLLMExplainer 就像一个"找茬游戏"的设计者——它小心翼翼地修改流程图中的某些步骤（最小结构扰动），使得专家给出的推荐方案发生根本性变化（最大语义分歧）。通过观察哪些步骤被修改后专家会"改变主意"，我们就能知道专家真正依赖的关键环节是什么。
- **关键设计动机**：
  - **为什么用反事实而不是直接分析注意力？** 因为注意力只能告诉我们模型"看了哪里"，但不能告诉我们"看了哪里才导致这个输出"。反事实通过"如果输入变了，输出是否变"来建立因果性更强的解释。
  - **为什么与 LLM 训练解耦？** 避免解释器过拟合特定模型，使框架具有跨模型泛化能力。同时降低计算成本，无需反向传播通过 LLM。
  - **为什么用软掩码 + Gumbel-softmax？** 图结构离散，直接优化不可微。Gumbel-softmax 提供连续松弛，允许梯度下降优化离散掩码决策。

### 3.2 形式化描述
- **问题定义**：
  给定异构知识图谱 $G = (V, E, \mathcal{A}, \mathcal{R}, \varphi, \psi, X^V, X^E)$，其中 $\varphi: V \rightarrow \mathcal{A}$ 为节点类型映射，$\psi: E \rightarrow \mathcal{R}$ 为边类型映射。目标是学习节点掩码 $\mathbf{m}_v \in [0,1]$ 和边掩码 $\mathbf{m}_e \in [0,1]$，生成反事实子图 $G_c$，使得：
  1. $G_c$ 与 $G$ 的语义差异最大化（通过 LLM 输出文本的 TF-IDF 余弦距离度量）
  2. $G_c$ 的结构变化最小化（稀疏性约束）
  3. $G_c$ 保持结构合理性和语义连贯性（平滑性、连通性约束）

- **核心公式**（总损失函数）：

$$
\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{structure}} + \alpha \cdot \mathcal{L}_{\text{semantic}} + \beta \cdot \mathcal{L}_{\text{entropy}} + \gamma \cdot \mathcal{L}_{\text{preserve}} + \delta \cdot \mathcal{L}_{\text{hard}} + \epsilon \cdot \mathcal{L}_{\text{smooth}}
$$

其中各分项含义：
- $\mathcal{L}_{\text{structure}} = \lambda_V \cdot \sum_{v \in V} \lambda_v \cdot m_v + \lambda_E \cdot \sum_{e \in E} \lambda_{\psi(e)} \cdot m_e$：结构稀疏性损失，鼓励移除更多节点和边
- $\mathcal{L}_{\text{semantic}} = 1 - \cos(\text{TF-IDF}(\mathcal{T}(G)), \text{TF-IDF}(\mathcal{T}(G')))$：语义分歧损失，$\mathcal{T}(\cdot)$ 为文本化函数
- $\mathcal{L}_{\text{entropy}}$：熵正则化，鼓励掩码趋近二进制（0 或 1）
- $\mathcal{L}_{\text{preserve}}$：结构保持损失，确保关键 Tool 节点至少保留一个
- $\mathcal{L}_{\text{hard}}$：硬掩码惩罚，推动软掩码越过 0.5 阈值
- $\mathcal{L}_{\text{smooth}}$：边平滑正则化，避免孤立边和节点，保持语义连贯性

- **Gumbel-softmax 采样**：

$$
\tilde{z} = \sigma\left(\frac{\log \alpha + G}{\tau}\right), \quad G = -\log(-\log(U + \varepsilon) + \varepsilon), \; U \sim \text{Uniform}(0,1)
$$

温度参数 $\tau = 0.15$ 平衡离散性与梯度稳定性。

### 3.3 架构与流程
- **整体框架**：
```
[BioToolKG 构建] → [图文本化注入 LLM] → [CFFTLLMExplainer 训练]
                                                        ↓
[反事实子图 G_c] → [对比 baseline/finetuned 输出] → [多维度解释分析]
```

- **关键组件详解**：
  - **BioToolKG**：面向生物信息学工具的异构知识图谱，包含 Tool、Input、Output、Download Source 等节点类型，以及 input/output/download_from 等关系类型。支持路径查找（Pathfinding）和管道构建（Pipeline Construction）任务。
  - **CFFTLLMExplainer**：独立训练的反事实解释器，以 TF-IDF 语义相似度为代理信号，通过 Gumbel-softmax 学习可微分的图掩码。与目标 LLM 完全解耦。
  - **文本化模板 $\mathcal{T}(\cdot)$**：将图谱按固定模板转为自然语言提示，确保图结构信息完整注入 LLM。

### 3.4 训练策略
- **数据**：BioToolKG 中的生物信息学工具链（以 RNA-seq 转录组组装管道为案例）
- **优化器与超参**：
  - $\alpha = 400.0$（语义分歧权重）
  - $\beta = 0.05$（熵正则化）
  - $\gamma = 10.0$（结构保持）
  - $\delta = 10.0$（硬掩码惩罚）
  - $\epsilon = 5.0$（Laplacian 平滑）
  - $\lambda_V = 0.1, \lambda_E = 0.5$（节点/边稀疏性权重）
  - $\tau = 0.15$（Gumbel-softmax 温度）
- **特殊技巧**：指数移动平均（EMA, decay=0.9）平滑损失曲线；prompt 相关性加权动态调整节点重要性。

## 4. 实验

### 4.1 实验设置
- **基准方法**：
  - RandomNodeMask / RandomEdgeMask / RandomNodeEdgeMask：随机掩码相同数量的节点/边
  - RandomNodeMaskAlign / RandomNodeEdgeMaskAlign：随机掩码但保持被掩节点类型与 $G_c$ 一致
  - Lowerattention / Higherattention：掩码注意力最低/最高的节点
- **评估指标**：
  - Jaccard Similarity：输出工具集合的交集/并集
  - Edit Distance（normalized）：工具序列的最小编辑距离
  - Path Overlap：最长公共前缀比例
  - Cosine Similarity：TF-IDF 向量余弦相似度
- **数据集**：BioToolKG 中的转录组组装管道（真实 RNA-seq 分析工作流）

### 4.2 主要结果

| 方法 | 模型 | Jaccard ↑ | Edit_norm ↓ | Overlap ↓ |
|------|------|-----------|-------------|-----------|
| G_base | 基线 | - | - | - |
| Gc_adapter (Ours) | 微调 | **0.10** | **高** | **低** |
| RandomNodeMask_base | 基线 | ~0.3 | 中 | 中 |
| RandomEdgeMask_base | 基线 | ~0.3 | 中 | 中 |
| Higherattention_adapter | 微调 | 0.14 | 中 | 中 |
| Lowerattention_adapter | 微调 | ~0.3 | 低 | 高 |

- **结果解读**：
  1. CFFTLLMExplainer 生成的 $G_c$ 使微调模型产生显著语义偏移（Jaccard 仅 0.10），而随机扰动几乎不改变输出（Jaccard ~0.3）。
  2. 高注意力基线虽能产生一定偏移（Jaccard 0.14），但始终劣于本文方法，且缺乏结构可解释性。
  3. 随机扰动虽引入大量结构变化（高 Edit_norm），但语义和工具链组成变化微弱，证明"结构变化 ≠ 语义变化"，也证明本文方法能建立结构与语义的因果映射。

### 4.3 进一步实验分析

#### 语义漂移分析（Semantic Drift）
- 完整图 $G$ 输出工具链：{Hisat2, Samtools, Scallop, Gffcompare}
- 反事实图 $G_c$ 输出工具链：{Ballgown, Cufflinks, StringTie, IGV, VEP, ...}
- Jaccard = 0.1018，Cosine Dissimilarity = 0.5443
- 结论：图级结构扰动有效触发了高层语义变异

#### 注意力对齐评估
- 被移除的关键节点（Scallop, Samtools, Gffcompare）注意力权重极低（（< 0.002）
- **关键发现**：注意力分布与真实语义重要性存在显著错位，验证了注意力不可靠的传统观察

#### 适配器偏移探测（Adapter Shift Probing）
| 工具 | LoRA 偏移范数 $\|\Delta\|$ | 解释 |
|------|---------------------------|------|
| Scallop | **0.0102** | 最大偏移，与微调目标（Scallop 相关工作流）一致 |
| Gffcompare | 0.0041 | 次要关键节点 |
| Samtools | 0.0031 | 辅助工具 |
- 结论：LoRA 参数偏移幅度可作为 token 级任务敏感度的可解释度量

#### 多信号三角验证
- 节点掩码（CFFTLLMExplainer）+ 注意力权重 + LoRA 偏移三者可相互对照：
  - 某些 token 注意力低但 LoRA 偏移大，表明存在"隐式任务感知结构依赖"
  - 这种跨信号差异正是单一解释方法无法捕捉的深层机制

### 4.4 实验总结
- 反事实结构掩码是一种精确且忠实的微调 LLM 解释方法
- 它能捕捉常规注意力可视化严重低估的结构元素
- 结构扰动与语义漂移的因果映射是随机扰动和注意力启发式无法复制的

## 5. 分析与讨论
- **关键洞察**：
  - 微调 LLM 的"知识"不仅存储在参数中，还体现在对输入结构的特定依赖模式上
  - LoRA 的低秩更新足以在潜在空间中编码显著的结构偏好（Scallop 的偏移最大）
  - 反事实解释与参数探测（LoRA 偏移）的结合，提供了从"输入-输出"到"内部参数"的全链条解释
- **方法的局限性**（含根因分析）：
  1. **固定结构化输入**：当前框架依赖预定义的知识图谱模板，无法直接解释自由文本输入。根因：反事实空间需要明确的结构化扰动定义，自由文本的"最小扰动"难以形式化。
  2. **TF-IDF 代理信号的局限**：用 TF-IDF 余弦距离近似语义分歧可能丢失深层语义关系。根因：与 LLM 解耦的设计必然需要代理信号，而 TF-IDF 无法捕捉上下文语义。
  3. **领域特定性**：BioToolKG 专注于生物信息学工具链，泛化到其他领域需要重新构建知识图谱。根因：异构图的节点/边类型定义具有领域语义。
  4. **计算开销**：Gumbel-softmax 采样和多次 LLM 推理成本较高。根因：需要在离散图空间和连续语义空间联合优化。
- **潜在改进方向**：
  - 引入预训练语言模型（如 Sentence-BERT）替代 TF-IDF 作为语义代理信号
  - 探索自动图谱生成（LLM-based KG construction）降低领域迁移成本
  - 设计更高效的掩码优化算法（如强化学习或进化算法）
- **对自己研究的启发**：
  - 反事实+参数探测的多信号解释范式可迁移到其他微调场景（如指令微调、领域适应）
  - LoRA 偏移作为可解释性信号的想法值得深入：能否在训练过程中主动约束偏移方向以提升可解释性？

## 6. 可以进一步探索的点
1. **动态知识图谱生成**：用 LLM 自动生成反事实解释所需的领域图谱，降低人工构建 BioToolKG 的成本（作者提及）
2. **改进语义相似度度量**：设计更符合 LLM 潜在语义空间的相似性指标，替代 TF-IDF（作者提及）
3. **形式化解释框架**：将反事实掩码与形式化验证结合，提供数学上严格的解释（作者提及）
4. **跨领域迁移**：将 CFFTLLMExplainer 应用于软件工程、医疗诊断等其他结构化推理领域
5. **实时解释接口**：开发交互式工具，允许用户实时调整掩码并观察输出变化
6. **与注意力机制的融合**：设计联合优化目标，使注意力权重与结构重要性对齐
7. **LoRA 秩选择与解释性的关系**：研究不同秩 $r$ 对 LoRA 偏移模式和可解释性的影响
8. **对抗鲁棒性分析**：检验反事实掩码是否能揭示模型对结构化对抗样本的脆弱性

## 7. 结论
- **核心贡献**：
  1. 提出首个基于反事实知识图谱的 LoRA 微调 LLM 解释框架 CFFTLLMExplainer
  2. 构建 BioToolKG，为生物信息学领域提供结构化推理基准
  3. 揭示注意力权重与结构重要性的错位，证明反事实解释能捕捉注意力遗漏的关键依赖
  4. 建立 LoRA 参数偏移与结构语义依赖的定量关联
- **为什么重要**：随着 LLM 微调在关键领域（医疗、生物信息学）的广泛应用，理解微调后模型的内部机制对于安全部署和故障排查至关重要。本文提供了一种与模型解耦、可验证、跨信号三角对齐的解释范式。
- **后续关注**：关注作者是否发布代码和 BioToolKG 数据集；跟踪该框架在 KDD Workshop 后的正式版本或扩展工作。

## 🔗 相关笔记
- [[LoRA_低秩适应]]：LoRA 微调技术的原理与应用
- [[反事实解释_图神经网络]]：GNN 领域的反事实解释方法综述
- [[LLM可解释性_注意力机制]]：注意力可视化及其局限性分析
- [[知识图谱增强LLM]]：KG+RAG 的技术路线与挑战

## 🔗 后续研究
（由系统在 L2 模式下自动补充，记录新笔记对本文的引用与矛盾）

---

*本文遵循 Ravel Agent 双语策略——主体以中文撰写，关键术语保留英文原词并首次出现时加注。公式使用原始 LaTeX 不翻译。*
