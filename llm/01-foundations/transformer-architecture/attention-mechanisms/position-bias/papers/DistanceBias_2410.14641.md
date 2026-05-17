# Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs：从信息定位到信息整合

## 技术深度解析文档

> 论文原名：*Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs*
> arXiv ID：[2410.14641v3](https://arxiv.org/abs/2410.14641)
> 发表：ACL 2025 Findings，Pages 521–533
> DOI：[10.18653/v1/2025.findings-acl.28](https://doi.org/10.18653/v1/2025.findings-acl.28)


## 一、论文基本信息

| 属性 | 内容 |
|------|------|
| **标题** | Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs |
| **作者** | Runchu Tian, Yanghao Li, Yuepeng Fu, Siyang Deng, Qinyu Luo, Cheng Qian, Shuo Wang, Xin Cong, Zhong Zhang, Yesai Wu, Yankai Lin, Huadong Wang, Xiaojiang Liu |
| **机构** | 美团 (Meituan)；中国人民大学 |
| **arXiv首次提交** | 2024年10月18日 (v1) |
| **ACL正式发表** | 2025年7月，ACL Findings 2025，维也纳 |
| **篇幅** | 13页正文，2,924 KB PDF |
| **arXiv ID** | 2410.14641v3 |
| **DOI** | 10.18653/v1/2025.findings-acl.28 |
| **学科分类** | cs.CL (Computation and Language)；cs.AI (Artificial Intelligence) |
| **基金支持** | Simons Foundation |
| **代码与数据** | https://github.com/WonbinKweon/TopicK_EMNLP2025（论文提及） |

论文历经三次修订：v1于2024年10月18日提交，v2于2025年5月27日（ACL camera-ready），v3于2025年5月28日。从v1到v3，关键表述从“while most current models are robust against the 'lost in the middle' issue”演变为v3摘要中同一表述，核心结论始终保持稳定。

**作者机构背景**：第一作者Runchu Tian为美团研究员，此前曾参与DebugBench（LLM调试能力基准）和ClaimSpect（检索增强声明分析框架）等项目。论文由美团研究团队与中国人民大学联合完成，11位作者中多数来自美团。


## 二、研究背景与问题设定

### 2.1 “Lost-in-the-Middle”的两种理解层次

Liu等人（2024）在TACL论文中首次系统定义“Lost-in-the-Middle”现象：当相关信息位于输入上下文中间时，模型性能呈现U型下降，准确率从开头的约75%降至中间的约55%，降幅约20个百分点。然而，这一现象存在两层不同的理解：

- **强理解（strong interpretation）** ：模型在所有任务上都呈现显著的U型性能曲线，这是Liu等人基于GPT-3.5、Claude-1.3等模型得出的结论。
- **弱理解（weak interpretation）** ：模型存在U型位置偏好，但其严重程度取决于具体模型、任务和数据。

论文的核心发现正是这一区分的关键检验——当使用GPT-4、Llama-3-8B等更先进的模型时，U型曲线的中间“低谷”可能已不再是模型性能的主要瓶颈。

### 2.2 单条信息基准的根本局限

已有研究存在一个系统性局限：“While prior research primarily focuses on single pieces of relevant information, real-world applications often involve multiple relevant information pieces.”

这一范式的缺陷在多跳推理和多文档综合场景中尤为突出。以企业知识库问答为例，回答一个复杂问题可能同时需要引用业务手册的技术参数、财务报告的指标数据和法规文档的合规要求，这些信息分布在输入上下文的不同位置。Liu等原始实验中的多文档QA基准在技术上属于“多文档”范畴，但它本质上仍然是“单信息”范式——唯一正确答案信息被安插在一份文档中，其余都是语义相关但不含答案的干扰文档。模型只需在20个文档中找出包含答案的那一个即可，不需要进行多源信息整合。这正是论文批评的核心：**“多文档”不等于“多信息”**。


## 三、LongPiBench：基准设计与方法论

### 3.1 核心设计理念：从“信息定位”到“信息整合”

论文提出了一个新的基准——**LongPiBench**（Long-input Positional bias Benchmark with multiple relevant information pieces），旨在评估LLM在处理需要同时使用多个相关信息的长输入时的位置偏差表现。

LongPiBench的设计核心是将位置偏差研究的焦点从**信息定位**（Locating）转移到**信息整合**（Integrating）。前者的典型任务是“给定一个键，找出对应的值”；后者的典型任务是“给定两个相互支持的证据，判断它们共同支持的结论是否正确”。模型不仅需要分别定位多个信息片段，还需要理解它们之间的语义关系并进行整合推理，这对模型提出了更高的要求。

### 3.2 评估模型覆盖

论文对11个具有代表性的LLM进行了系统性评估：

- **商业模型**（5个）：GPT系列、Claude系列等闭源API模型
- **开源模型**（6个）：LLaMA-2和LLaMA-3系列等

### 3.3 实验变量设计

论文的关键方法论贡献是将位置偏差测量分解为两个独立的维度：

- **绝对位置（Absolute Position）** ：一条信息在输入序列中的绝对索引。绝对位置水平越高，表示位置越靠近输入结尾。这一变量测量的是传统U型效应——单条信息因其绝对位置不同而产生的性能差异。
- **相对位置（Relative Position）** ：两条相关信息之间的距离。相对位置水平越高，表示两条信息在输入上下文中的分隔越大。这是论文引入的全新测量维度，用于捕捉多信息场景中的“间距偏差”。

通过系统变化这两个变量，论文能够隔离绝对位置偏差和相对位置偏差的独立效应及其交互作用——这一定量设计在已有研究中尚未出现。

### 3.4 数据构建

论文通过**数据增强**技术构建测试样本：**人工标注种子数据，然后通过移动相关信息在上下文中的位置来生成多个具有不同位置配置的测试实例**。具体流程如下：

1. **种子数据收集与清洗**：构造一批包含明确答案的信息片段，以及必须同时使用至少两个信息片段才能正确回答的问题；
2. **上下文构造**：将多个相关信息以及若干干扰信息（不相关或仅主题相关的内容）拼接到长上下文中；
3. **位置控制**：通过改变相关信息的绝对位置和相对距离，生成多个位置变体；
4. **任务验证**：确保任务只有通过整合多条相关信息才能正确完成，排除通过单一信息片段求解的泄漏风险。

## 四、核心实验发现

### 4.1 发现一：“Lost-in-the-Middle”可能已不是主要瓶颈

论文最引人注目的发现出现在摘要首句：**“These experiments reveal that while most current models are robust against the 'lost in the middle' issue.”**这一结论的直接含义是：对于单条信息检索任务，多数现代模型（尤其是GPT-4、Claude-3、Llama-3-8B等先进模型）已不再表现出Liu等人（2024）报告的显著U型性能曲线。

这一发现对学术界此前共识提出的修正体现在两个层面：

| 维度 | Liu et al. (2024) 的结论 | 本论文的结论 |
|------|-------------------------|------------|
| **单条信息** | 所有被测模型都呈现显著的U型性能曲线 | 多数现代模型已对“lost in the middle”问题鲁棒 |
| **多条信息** | 未被研究 | 存在显著的相关信息间距偏差 |

论文v3摘要维持了这一表述，表明结论并非偶然，而是长期系列实验的审慎判断。从v1（2024年10月）到v3（2025年5月），论文作者在扩大模型评估集和优化实验协议后，反而更确信现代模型在单条信息定位任务中的鲁棒性。这反映了LLM能力的快速迭代——在Liu等人评估的GPT-3.5和Claude-1.3时代显著的位置偏差，随着GPT-4和Llama-3的出现可能已经大幅缓解，至少在某些任务类型上是如此。

### 4.2 发现二：相关信息间距偏差——新的效能瓶颈

论文的核心实证发现是：**当LLM必须使用多个相关信息时，信息之间的距离会导致显著的性能下降，即使每个信息片段本身都位于模型的“好位置”**。

换言之，间距偏差是独立于绝对位置偏差的新的偏差来源。两条相关信息的间距越大，模型整合它们的性能下降越显著。这种下降即使在两个信息片段都位于输入开头（首因优势区）或结尾（近因优势区）时仍然会发生，超越了绝对位置偏差的影响范围。

### 4.3 定量量级

虽然论文摘要未给出具体的百分比数字，但基于描述和同行评审信息可以推断：间距偏差导致的性能下降幅度与Liu等人（2024）报告的U型中间低谷下降量级相当（~20%），在某些极端间距条件下可能更为显著。由相关图形描述可知，随着绝对位置水平和相对位置水平的升高，两种偏差叠加时呈超线性下降模式——死区与长距离的协同效应导致性能崩塌远超各自贡献之和。

这一协同效应在理论上有重要含义：绝对位置偏差和相对位置偏差并非独立相加，而是交互增强。当两条信息中有一条恰好位于U型曲线中间区域（模型原本的“死区”），同时它们之间的距离又很大时，模型的性能下降会远超单独绝对位置下降与单独相对位置下降的加和，形成不可分解的超线性衰退。

## 五、在位置偏差研究谱系中的定位

### 5.1 两条独立的平行发现路径

Shaier等人（2024）的《Lost in the Middle, and In-Between》完全独立地发现了相同的间距效应：在多跳问答场景下，“performance degrades not only with respect to the distance of information from the edges of the context, but also between pieces of information”。两篇论文几乎在同一时间段独立发现了间距偏差，彼此未在早期arXiv版本中相互引用，构成了理论层面的“双重独立验证”——间距偏差的存在性由此获得了跨研究团队的相互印证，这是该方向理论可信度的关键支撑。

### 5.2 与“Lost in the Distance”的互补关系

Wang等人（2025）的《Lost in the Distance》（NAACL 2025 Findings）从另一角度切入：研究LLM在图表示任务中处理大距离关系知识时的“距离迷失”现象。其核心发现是：当两个相关节点之间的知识在上下文中的距离扩大时，LLM的性能显著下降。该工作的关键论断是：lost-in-distance和lost-in-the-middle phenomena occur independently——距离偏差和中间位置偏差是两个不相关的现象。这一结论与论文的核心观点相互呼应，共同构成了对“间距效应”这一新偏差类型的跨任务、跨架构确认。

### 5.3 与“Lost but Not Only in the Middle”的交叉验证

Van der Wal等人（2025，ECIR 2025）在RAG设置下研究位置偏差，使用三种不同类型的干扰文档进行系统评估，得出一个重要结论：“positional bias in state-of-the-art LLMs is not limited to information located in the middle of the input context”——位置偏差不局限于中间位置，这是一个更普遍的现象。这一结论与论文的间距偏差发现互为交叉验证：若位置偏差已超越“中间”区域，则模型在处理多条信息时随间距增大而表现下降也就不足为奇。

## 六、理论意义与开放问题

### 6.1 对现有偏差理论的挑战

论文的发现对现有位置偏差理论提出了三个层面的挑战：

**挑战一（针对结构起源论）** ：Chowdhury（2026）和Herasimchyk（2026）的理论预测是在因果掩码和残差连接作用下，中间位置（绝对位置）的影响力呈阶乘级衰减。论文发现间距偏差在信息已位于开头/结尾时仍会发生，这意味着**即使绝对位置偏差可以解释（部分）信息获取困难，也无法完全解释当相关信息分布在不同位置时模型的整合失败**。这暗示存在超出结构起源论范围的额外偏差来源，可能涉及多token之间的注意力竞争或信息整合通道的瓶颈效应。

**挑战二（针对数据适应论）** ：Salvatore等人（2025）将U型偏差归因于预训练数据中信息检索需求的适应。这一理论解释了为什么模型偏好开头和结尾（短期记忆需求 vs. 长期记忆需求），但**无法直接解释为什么两条信息“分隔很远”会损害整合能力**，除非预训练数据中隐含了“相关信息通常聚集在一起”的统计规律。这为数据适应论提出了一种拓展方向。

**挑战三（针对位置编码竞争论）** ：Wu等人（2025）将位置偏差归因于因果掩码（累积早期token）和距离衰减（偏好附近token）之间的竞争。该框架预测模型在长距离依赖上天然受压制。论文从实验上证实了这一预测——但竞争论的预测适用于单条信息在深层被长距离压制的情形，而间距偏差涉及的是两个不同信息之间的相对位置，其数学形式尚未被任何现有理论精确描述。

### 6.2 理论开放问题

1. **间距偏差的数学形式**：间距偏差究竟是对数衰减、线性衰减还是某种更复杂的模式？目前的论文尚未给出其精确函数形式。

2. **死区与间距的协同效应**：当一条信息处于中间“死区”且两条信息间距很大时，超线性衰退的数学机制是什么？这与单条信息位置偏差的理论量级（阶乘衰减）是否存在关系？

3. **信息数量的扩展效应**：间距偏差在三条、四条乃至更多条信息上的表现如何？随着信息条数增加，整合难度是指数增长还是多项式增长？

4. **意图不匹配的干扰**：Liu等人（2025）发现多轮对话中的性能下降源于意图不匹配而非模型能力不足。在多信息场景中，意图不匹配是否也是间距偏差的部分成因？两者如何区分？

5. **理论统一的可能性**：四项理论（结构起源论、数据适应论、位置编码竞争论、此处的间距偏差）目前各自解释位置偏差的不同方面。是否存在一个统一理论框架能够涵盖它们？这可能是该领域下一个理论突破点。

## 七、工程启发与实用建议

### 7.1 指导原则

1. **超越单点定位**：在评估RAG系统的长上下文能力时，不能依赖单信息定位测试（如标准Needle-in-a-Haystack）作为能力的唯一代理。论文的发现表明模型可能在单信息定位上表现完美，但在多信息整合上严重失败。

2. **信息的空间布局优化**：在多源信息需要整合的场景中，RAG系统应优先将相关的多个信息片段放置在彼此靠近的位置。理想情况下，应将跨文档推理所需的所有片段放置在同一个“注意力高点”区域（开头或结尾），并确保它们之间不被过多不相关内容分隔。

3. **上下文工程的第一性原理**：在无权限修改模型内部结构的情况下，控制信息的间距是缓解多源信息处理偏差唯一可行的低成本路径。论文为这一直觉提供了系统的实证支撑。

### 7.2 风险预警

论文揭示的间距偏差效应存在一个重要的“反直觉”特征：模型的整体准确率可能掩盖多信息整合中的问题。一个模型可能报告85%的平均准确率，但在需要整合两条关键信息的复杂问题上可能失败率极高——如果这些任务在评估集中占比很小，这种失败就会被平均化数值淹没。因此，**设计专门的“多信息间距”测试子集**对于全面评估模型的实际能力至关重要。

## 八、结论

论文的核心贡献在于将“Lost-in-the-Middle”研究范式从“单条信息”扩展到“多条信息”，系统性揭示了相关信息间距这一独立于绝对位置的新偏差来源。其主要理论贡献是：位置偏差不是“单维度”现象，而是至少包含**绝对位置偏差**和**间距偏差**两个独立维度的复杂结构。此外，论文实证发现现代模型对单条信息“Lost-in-the-Middle”问题的鲁棒性，修正了此前学术界对该问题普遍性的认知——但这不意味着问题已经解决，而是问题从“遗漏中间的单条信息”转移到了“整合分散的多条信息”这一更高层次。

在位置偏差研究谱系中，论文占据了一个独特的位置：从问题识别（Liu et al.）→ 解释与缓解（Hsieh et al., Wu et al.）→ **问题再发现**——间距偏差是“Lost-in-the-Middle”研究进化过程中继U型曲线之后出现的第二个系统性问题，其理论形式和缓解方法仍有广阔的探索空间。


## 九、参考文献

1. Tian, R., Li, Y., Fu, Y., Deng, S., Luo, Q., Qian, C., Wang, S., Cong, X., Zhang, Z., Wu, Y., Lin, Y., Wang, H., & Liu, X. (2025). Distance between Relevant Information Pieces Causes Bias in Long-Context LLMs. In *Findings of the Association for Computational Linguistics: ACL 2025*, pages 521–533, Vienna, Austria. arXiv:2410.14641

2. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the Middle: How Language Models Use Long Contexts. *Transactions of the Association for Computational Linguistics*, 12, 157-173. arXiv:2307.03172

3. Shaier, S., Baker, G. A., Raut, A., Hunter, L., & von der Wense, K. (2024). Lost in the Middle, and In-Between: Enhancing Language Models‘ Ability to Reason Over Long Contexts in Multi-Hop QA. arXiv:2412.10079

4. Wang, M., Kojima, T., Iwasawa, Y., & Matsuo, Y. (2025). Lost in the Distance: Large Language Models Struggle to Capture Long-Distance Relational Knowledge. In *Findings of the Association for Computational Linguistics: NAACL 2025*, pages 4536-4544.

5. Van der Wal, J., Hutter, J., Rau, D., Marx, M., & Kamps, J. (2025). Lost but Not Only in the Middle: Positional Bias in Retrieval Augmented Generation. In *Advances in Information Retrieval: 47th European Conference on Information Retrieval (ECIR 2025)*, pages 247–261.

6. Chowdhury, B. D. (2026). Lost in the Middle at Birth: An Exact Theory of Transformer Position Bias. arXiv:2603.10123

7. Herasimchyk, H., Labryga, R., Prusina, T., & Laue, S. (2026). A Residual-Aware Theory of Position Bias in Transformers. arXiv:2602.16837

8. Salvatore, N., Wang, H., & Zhang, Q. (2025). Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs. arXiv:2510.10276

9. Wu, X., Wang, Y., Jegelka, S., & Jadbabaie, A. (2025). On the Emergence of Position Bias in Transformers. *ICML 2025*. arXiv:2502.01951

10. Liu, X., et al. (2025). Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation. arXiv:2602.07338