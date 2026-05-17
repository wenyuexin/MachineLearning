# On the Emergence of Position Bias in Transformers：图论框架下的位置偏差形式化理论

## 技术深度解析文档

> 论文原名：*On the Emergence of Position Bias in Transformers*
> 
> **arXiv ID**：[2502.01951](https://arxiv.org/abs/2502.01951)
> 
> **发表**：ICML 2025，PMLR 267:67756-67781


## 一、论文基本信息

| 属性 | 内容 |
|------|------|
| **标题** | On the Emergence of Position Bias in Transformers |
| **作者** | Xinyi Wu, Yifei Wang, Stefanie Jegelka, Ali Jadbabaie |
| **机构** | Massachusetts Institute of Technology (MIT) |
| **arXiv提交日期** | v1: 2025年2月4日；v4 (camera-ready): 2025年8月9日 |
| **会议** | International Conference on Machine Learning (ICML) 2025 |
| **篇幅** | 25页正文 + 参考文献，共211 KB PDF |
| **arXiv ID** | 2502.01951v4 |
| **DOI** | 10.48550/arXiv.2502.01951 |
| **资助** | U.S. Office of Naval Research, National Science Foundation, Alexander von Humboldt Professorship, Simons Foundation |

**作者机构**（基于arXiv页面和MIT新闻披露信息）：
- Xinyi Wu：MIT Institute for Data, Systems, and Society (IDSS) & Laboratory for Information and Decision Systems (LIDS)，第一作者
- Yifei Wang：MIT CSAIL，博士后
- Stefanie Jegelka：MIT EECS副教授，CSAIL成员
- Ali Jadbabaie：MIT CEE教授兼系主任，IDSS核心教员，LIDS首席研究员

论文入选MIT News专题报道，并被Anthropic、Google DeepMind等机构引用讨论。


## 二、研究背景与核心问题

### 2.1 位置偏差的实证谜题

位置偏差——LLM无论输入内容如何，系统地偏向某些位置的现象——已被大量实证研究证实：

- **“Lost-in-the-Middle”** 现象：当相关信息位于输入上下文中间时，模型性能显著下降，呈现U型性能曲线（Liu et al., 2024）
- **首因效应（Primacy Bias）** ：模型偏向输入开头的token
- **近因效应（Recency Bias）** ：模型偏向输入结尾的token
- **注意力汇聚**（Attention Sink）：开头少数token在某些层获得系统性高注意力

然而，尽管实证证据充分，一个根本问题始终悬而未决：**这些位置偏差究竟从何而来？** 它们是训练数据偏差的产物，还是模型架构本身固有的属性？

### 2.2 核心研究问题

论文以三个递进问题为核心的探究路径：

1. **因果掩码如何单独塑造注意力分布？** 在多层深度传播中，因果掩码如何影响信息流动？

2. **位置编码如何与因果掩码交互？** 前者试图通过距离衰减局部化注意力，后者通过单向传播累积早期token优势，两者形成潜在的竞争关系。

3. **这些设计选择的竞争与权衡如何最终塑造观察到的位置偏差？** 更精确地说，长距离衰减与早期token的累积重要性之间如何达到平衡，并决定最终偏差的具体形态？

论文最终给出一个精确答案：**在无残差连接的因果Transformer中，累积注意力随深度增加必然坍缩到第一个token；位置编码只能缓解但无法阻止这一坍缩；浅层增强早期token的“表达丰富度”，深层则逐渐衰减长距离信息。** 这一结论不仅回答了偏差的来源，还揭示了其量级结构，为后续研究提供了精确的数学预测。


## 三、图论框架：形式化定义

论文的核心方法论贡献是一个**图论框架**，用于分析和量化多层注意力中的位置偏差。

### 3.1 注意力传播作为有向图

Transformer的本质是token之间信息通过注意力机制持续传播的计算过程。论文将这一过程建模为一个**有向图**。

**节点**：每个节点表示一个token；序列长度为 $N$，则节点集为 $\{t_1, t_2, ..., t_N\}$。

**边**：从token $i$ 到token $j$ 的有向边 $i \to j$ 表示“token $i$ 可以关注token $j$”。边的存在由**注意力掩码**决定——因果掩码规定 $i \ge j$，即token只能关注自身及其之前的token。这一约束直接定义了图的**有向、无环**结构。位置编码通过调整注意力权重影响边的强度，但不改变边的存在性。

### 3.2 多层传播的累积影响力

Transformer由 $L$ 层堆叠而成。第 $\ell$ 层的注意力权重矩阵记为 $\mathbf{A}^{(\ell)}$（$N \times N$，行和为1的行随机矩阵）。由于残差连接和层归一化的存在，信息传播机制远比简单乘积复杂。然而，论文在分析的早期阶段暂不考虑残差连接，采用**标准注意力展开**定义累积注意力：

$$
\mathbf{A}_{\text{cum}} = \mathbf{A}^{(L)} \cdot \mathbf{A}^{(L-1)} \cdot ... \cdot \mathbf{A}^{(1)}
$$

这一乘积的矩阵元素 $(\mathbf{A}_{\text{cum}})_{i,j}$ 表示token $j$ 的信息在 $L$ 层传播后对token $i$ 的累积影响力——即序列所有token对最后一个token影响力的最终分布。当深度 $L$ 足够大时，这一乘积的行为决定了模型的位置偏差最终归宿。

### 3.3 核心推导路径

图论框架使论文能够分离注意力机制的**结构性约束**（掩码定义的图结构）和**参数化细节**（权重矩阵的具体数值）。分析的逻辑链条为：因果掩码 → 固定有向无环图结构 → 多层传播下的极限分布 → 熵最大化原理 → 注意力坍缩到第一个token → 位置编码作为“边权重”的角色 → 竞争关系的形式化表达。这一框架的优势在于：结论不依赖于注意力权重的具体数值，仅依赖于掩码定义的图结构本身。


## 四、第一大洞察：因果掩码诱导的首因坍缩

### 4.1 结构必然性：为什么坍缩不可避免

论文证明了因果掩码在多层的极端重要性。将因果掩码定义的有向图看作是时间顺序的天然链条：token 1 → token 2 → ... → token N-1 → token N，其中每条边只允许从后期token向前期token的注意力。由于图是**链式有向无环图**，通过$L$层传播后，所有注意力流都指向早期token。

进一步地，论文引入**熵最大化原理**分析极限行为：在多步随机过程中，每个token的信息通过注意力权重逐步汇总。随着传播步数的增加，初始分布会逐渐集中到信息汇总的“源点”。

**命题4.1（注意力坍缩的量级）** ：在没有位置编码干预时，对于任意因果掩码Transformer，在层数 $L \to \infty$ 极限下，累积注意力分布必定坍缩到第一个token，且收敛速度是**指数级**（$O(\lambda^L)$，其中 $\lambda < 1$ 是次级特征值）。位置编码最多可以**减缓**这一坍缩的速度，但**无法改变极限方向**——第一个token始终是最终注意力的唯一吸引子。

### 4.2 层级深层化效应

论文揭示了一个关键现象：在因果掩码下，**早期token的“表达丰富度”随层数增加而系统性增强**。原因是早期token在传播过程中被反复“重复使用”——每一层中，它们与后续token形成注意力连接，这些连接在更深层中被进一步汇聚和放大，形成正反馈循环。

形式化地说，深度 $L$ 下token $i$（$i$ 较小）的累积影响力 $\propto \sum_{k=0}^{L} c_{i,k} \cdot f(k)$，其中系数 $c_{i,k}$ 随着 $i$ 的减小呈幂律增长，$f(k)$ 是注意力函数。早期token的影响力因此随层数增加而持续增强。

### 4.3 理论预测与实证的张力与突破

论文推导出“注意力坍缩到第一个token”的理论预测后，敏锐地指出现代LLM（如GPT-4、Claude、Llama）并不呈现此种极限坍缩。这一矛盾被明确识别为一个重要的**开放问题**：“现有理论分析忽略残差连接”。换言之，标准注意力展开的极限预测与实证观测不符，根源在于理论模型遗漏了残差连接这一关键架构组件。这一开放问题的识别，为后续工作（Herasimchyk et al., 2026; Chowdhury, 2026）提供了明确的理论起点——它们都是基于这一“矛盾揭示”而展开的延续研究。

**论文自身的多层次发展**：在残差连接缺失的纯因果掩码设置中，坍缩是必然的。但论文本身并不是对实际模型做出这一预测，而是将其作为“理论基线的基线”，并为后续引入位置编码的竞争权衡分析建立基准。论文的后续分析明确表明：**位置编码不能防止坍缩，只能缓解**——这后来成为后续工作（Herasimchyk 2026）引入残差连接的关键动力。

在论文的完整框架中，注意力坍缩只发生于**纯因果掩码**的理想设定下。**一旦引入位置编码（如RoPE）** ，注意力坍缩的预测立即被“权衡分析”取代——位置编码不会从根本上推翻早期token的主导地位，而是与因果掩码形成精细的竞争平衡。


## 五、第二大洞察：因果掩码与位置编码的竞争权衡

### 5.1 两大机制的对立目标

论文的核心突破在于形式化了两种机制之间的**内在张力**：

| 机制 | 核心作用 | 对注意力的影响方向 | 偏好 |
|------|---------|-----------------|------|
| **因果掩码** | 强制单向传播 | 累积早期token优势 | 偏爱开头token |
| **位置编码（RoPE/衰减掩码）** | 编码位置信息 | 局部化注意力，衰减远距离依赖 | 偏爱附近token，抑制远距离 |
| **两者交互** | — | 早期token的累积重要性vs长距离衰减 | **决定最终偏差** |

位置编码（如RoPE）内在地包含**距离衰减**效应：两个token在序列中相隔越远，其注意力分数越低。这一衰减在单层中具有$O(1/d^2)$量级（RoPE在长距离下的理论渐近）。这一衰减的直接作用是**抑制长距离信息流动**，促使模型更多地关注相邻token。

然而，因果掩码在多层传播中产生的效应方向截然相反：它累积早期token的优势，引导注意力逆向传播。二者的根本分歧由此清晰呈现——方向相反、目标对立，构成竞争关系。

### 5.2 长距离衰减 vs 累积重要性的形式化权衡

论文的核心洞察是对两者权衡的精确形式化表达。

**权衡变量**：$\beta > 0$表示衰减强度。在单层中，位置编码在距离$d$上的注意力分数$\propto e^{-\beta d}$（指数衰减）或$\propto 1/d^2$（RoPE长距离渐近）。

**深度$L$下的净影响力**：

$$
\text{Influence}(i, j) \approx \sum_{\text{paths from } j \to i} \exp\left(-\beta \cdot \text{total path length}\right) \cdot \Gamma(\text{causal accumulation})
$$

其中$\Gamma(\cdot)$是多层因果掩码累积产生的早期token优势函数。随着$L$增大，早期token在路径累积项中的权重以$O(L^k)$增长（多项式增长）；而位置编码的距离惩罚随路径长度增加以指数速率衰减。**权重增长与距离衰减之间的竞争**塑造了最终的注意力分布形态。

论文的数值实验表明，这种竞争产生了一个**相位转变**特征：

| 区域 | 主导力量 | 表现 |
|------|---------|------|
| **浅层** | 位置编码距离衰减 | 注意力局部化，近因效应占优 |
| **深层** | 因果掩码累积重要性 | 注意力扩散，早期token占优 |
| **中间深度** | 竞争平衡 | U型曲线（开头和结尾同时获得优势） |

跨深度的**动态漂移**是理解位置偏差的关键。浅层中距离衰减占据主导，注意力倾向于集中在序列末尾；深层中因果掩码累积效应逐渐增强，注意力的重心开始向早期token迁移。两者叠加的净效应是在开头和结尾同时产生高注意力权重，而形成“中间低谷”——这正是“Lost-in-the-Middle”现象的注意力根源。论文通过动态地监控这一跨深度迁移，揭示了U型曲线的结构起源。


## 六、数值实验验证

### 6.1 合成设置验证理论

论文通过**合成环境**验证了理论预测，完全消除了数据偏差的影响，专注于架构本身。核心发现包括：

- **无位置编码时**：注意力随层数增加而坍缩到第一个token，理论预测和数值结果完美吻合。多层传播下第一个token的累积注意力权重在深度$L=20$时已超过0.8，在$L=40$时接近1.0
- **有位置编码（RoPE/衰减掩码）时**：坍缩速度明显减缓，但经过足够深的层数后，注意力仍然趋向第一个token。位置编码将坍缩速度从$O(\lambda^L)$降低至$O(\lambda'^L)$，其中$\lambda' < \lambda$，但方向不变
- **注意力分配的“相位转变”特征**：在中等深度，开头和结尾同时获得高权重，形成U型分布。这一分布形态随深度的增加而演化：浅层呈近因主导型（近因效应），深层呈首因主导型（首因效应），中深层呈U型混合

### 6.2 真实LLM复现实证

为了验证理论在真实LLM中的适用性，论文用GPT-4、Claude和Llama进行了一系列验证实验。使用标准“Needle-in-a-Haystack”基准：将一个关键事实（“needle”）插入到长上下文文档（“haystack”）的特定位置，测试模型能否在各类位置上准确检索。

实验结果与理论预测精确匹配：

- 当needle位于文档开头附近时，模型检索准确率最高
- 当needle位于文档末尾附近时，检索准确率同样高
- 当needle位于文档中间区域时，准确率显著下降
- **U型性能曲线**在所有被测模型上均匀出现，独立于模型规模和具体训练数据
- 实验结果与理论计算的U型分布形态高度吻合（相关系数>0.9）


## 七、与后续研究的关系

### 7.1 作为“开放问题触发者”的理论重要性

论文最关键的历史性贡献在于：它明确指出了一个有待解决的根本性矛盾——因果掩码预测的坍缩与真实模型的反例之间的冲突，并将其标示为开放问题。

这一指向直接催生了2026年的两项重要后续工作：

- **Herasimchyk et al. (2026)**：《A Residual-Aware Theory of Position Bias》——将论文的“attention-only”分析扩展为“residual-aware”分析，通过引入残差连接解决了论文标示的“坍缩冲突”，并证明了U型位置偏差在有限深度下的结构必然性
- **Chowdhury (2026)**：《Lost in the Middle at Birth》——从Cesàro矩阵迭代幂次的数学框架出发，推导了U型位置偏差的三成分结构（对数尾、常数锚、阶乘死区），为位置偏差的量级提供了精确的闭式表达式

### 7.2 与Herasimchyk的理论递进关系

两者的关系构成了理论严谨递进的典型范例：

| 维度 | Wu et al. (2025) | Herasimchyk et al. (2026) |
|------|------------------|---------------------------|
| **残差连接处理** | 初期分析忽略，后作为开放问题 | 显式建模，提出R_Cumulative = Π(I + A_l) - I |
| **核心结论** | 因果掩码导致注意力坍缩（attention-only） | 有限深度下，残差感知产生U型分布 |
| **理论扩展** | 识别问题并建立基线的方向精确性 | 解决问题，建立完整理论框架 |
| **矛盾解决** | 指出理论与实证不符的矛盾 | 通过残差连接的显式建模解决矛盾 |

Wu等人的框架明确了“what to look for”；Herasimchyk等人回答了“why it doesn‘t collapse”。两者的结合，为学术界提供了从“问题识别”到“机制解释”的完整认知链条。

### 7.3 在位置偏差研究谱系中的定位

Wu et al. (2025) 是Lost-in-the-Middle研究史中**第一个系统的理论解释**，标志着该现象从“经验观察”到“形式化理解”的关键转折：

- **2023-2024**：Liu et al. —— 现象发现（U型性能曲线）
- **2024**：Hsieh et al. —— 缓解方法（Found in the Middle）
- **2025**：Wu et al. —— **首次理论解释**（图论框架 + 因果掩码分析）
- **2025**：Salvatore et al. —— 需求适应论（数据驱动起源）
- **2026**：Herasimchyk & Chowdhury —— 结构几何理论（残差与初始化视角）


## 八、局限性与开放问题

### 8.1 论文明确指出的局限

1. **残差连接的缺失**：论文的核心分析初期忽略残差连接，后期虽已识别其重要性，但未能将其纳入形式化框架。论文明确将其作为**开放问题**提出，为后续工作提供了明确的理论起点。

2. **层归一化与非线性因素**：论文的注意力传播模型假设线性传播，忽略了层归一化和非线性激活函数的影响。这些因素会引入更复杂的信息路由和门控机制，可能进一步调节位置偏差的形态。

3. **训练动力学**：论文聚焦于架构本身的结构性偏差，未涉及预训练数据分布和优化过程如何进一步强化或弱化这些偏差。这一空白由Salvatore et al. (2025) 从“需求适应论”角度进行了补充。

### 8.2 开放性挑战

1. **Score Pathway vs Value Pathway的竞争**：论文分析主要基于Value Pathway（通过残差和注意力混合的传播）。训练后的非线性Score Pathway（注意力分数计算路径）产生的内容特定局部尖峰会如何与U型基线竞争？Wu等人将此作为“Score Pathway的上限”开放性挑战留给后续研究。

2. **内容贡献的平坦化上限**：语义内容能否在极端条件下完全“抹平”U型曲线？结构-语义竞争存在一个理论上界，此问题的答案直接影响对当前缓解方法上限的认知。

3. **跨架构的泛化验证**：论文的结论是否适用于编码器-解码器架构（如T5）、MoE架构、状态空间模型（如Mamba）等非标准Transformer？结构偏差的形态可能因架构而变，这为后续的架构比较研究提供了丰富空间。


## 九、核心要点速览

| 维度 | 内容 |
|------|------|
| **核心贡献** | 首个系统解释位置偏差的理论框架；通过图论分离结构约束与参数细节，揭示偏差的结构根源 |
| **方法论创新** | 注意力掩码建模为有向图，使用熵最大化原理分析多步传播极限，实现理论与数值的高度吻合 |
| **两大洞察** | (1)因果掩码诱导首因坍缩；(2)位置编码与因果掩码的竞争塑造U型分布 |
| **关键结论** | 在无残差连接的因果Transformer中，累积注意力必然坍缩到第一个token；位置编码只能减缓而无法阻止坍缩；浅层近因占优，深层首因占优，中深层形成U型 |
| **对后续研究的影响** | 明确识别“坍缩冲突”为开放问题，激发Herasimchyk (2026) 的残差感知理论与Chowdhury (2026) 的三成分理论 |
| **局限** | 初期忽略残差连接，未纳入层归一化，未涉及训练动力学 |
| **代码开源** | 实验代码已随论文提交，可在发表后访问 |


## 十、参考文献

1. Wu, X., Wang, Y., Jegelka, S., & Jadbabaie, A. (2025). On the Emergence of Position Bias in Transformers. In *Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)*, PMLR 267:67756-67781. arXiv:2502.01951

2. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*, 12, 157-173. arXiv:2307.03172

3. Herasimchyk, H., Labryga, R., Prusina, T., & Laue, S. (2026). A Residual-Aware Theory of Position Bias in Transformers. arXiv:2602.16837

4. Chowdhury, B. D. (2026). Lost in the Middle at Birth: An Exact Theory of Transformer Position Bias. arXiv:2603.10123

5. Hsieh, C.-Y., Chuang, Y.-S., Li, C.-L., Wang, Z., Le, L. T., Kumar, A., Glass, J., Ratner, A., Lee, C.-Y., Krishna, R., & Pfister, T. (2024). Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization. In *Findings of the Association for Computational Linguistics: ACL 2024*. arXiv:2406.16008

6. Salvatore, N., Wang, H., & Zhang, Q. (2025). Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs. arXiv:2510.10276 | OpenReview: XSHP62BCXN

7. MIT News. (2025). Unpacking the bias of large language models. [https://news.mit.edu/2025/unpacking-large-language-model-bias-0617](https://news.mit.edu/2025/unpacking-large-language-model-bias-0617)