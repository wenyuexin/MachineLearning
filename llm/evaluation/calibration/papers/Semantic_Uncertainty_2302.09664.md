# Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation

**论文信息**
- 论文标题：Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation
- 中文标题：语义不确定性：自然语言生成中不确定性估计的语言不变性
- 作者：Lorenz Kuhn, Yarin Gal, Sebastian Farquhar
- 机构：University of Oxford, OATML Group
- arXiv: [2302.09664](https://arxiv.org/abs/2302.09664)
- 发表：ICLR 2023 (Spotlight)

---

## 一、论文整体思路

### 1.1 研究背景

大语言模型（LLM）在自然语言生成（NLG）任务中表现出色，但其输出的可靠性难以评估。传统的不确定性估计方法（如预测熵）在自然语言场景中面临独特挑战：

**语义等价问题**：
- "巴黎" 和 "法国首都" 语义相同但词汇不同
- "是的" 和 "对的" 表达相同意思
- 传统的token级别熵会错误地将这些视为不同的答案

### 1.2 核心问题

**传统预测熵的局限性**：

$$H(p) = -\sum_{x} p(x) \log p(x)$$

当模型在语义等价的不同表达之间"摇摆"时：
- 传统熵会误判为高不确定性
- 实际上模型对答案的含义是确定的

### 1.3 主要贡献

1. **识别问题**：揭示自然语言生成中不确定性估计的独特挑战——语义等价
2. **提出方法**：语义熵（Semantic Entropy）——考虑语言不变性的不确定性度量
3. **验证有效性**：在TriviaQA和CoQA数据集上验证方法优于传统基线

---

## 二、核心方法：语义熵（Semantic Entropy）

### 2.1 方法概述

```mermaid
flowchart LR
    A[输入问题] --> B[生成多个回答]
    B --> C[语义聚类]
    C --> D[计算语义熵]
    D --> E[不确定性估计]
```

### 2.2 三步计算流程

**Step 1: 生成多个回答**

对同一输入生成 $K$ 个候选回答：

$$\{s_1, s_2, \ldots, s_K\}$$

**Step 2: 语义聚类**

将语义等价的回答聚类到同一组：

$$C_1, C_2, \ldots, C_M$$

其中 $M \leq K$，每个聚类包含语义相同的回答。

**判断语义等价的方法**：
- 使用NLI（自然语言推理）模型
- 判断两个回答是否相互蕴含

**Step 3: 计算语义熵**

$$SE = -\sum_{m=1}^{M} P(C_m) \log P(C_m)$$

其中 $P(C_m)$ 是聚类 $C_m$ 的概率（该聚类中回答的概率之和）。

### 2.3 与传统熵的对比

| 方法 | 计算方式 | 问题 |
|------|---------|------|
| **预测熵** | Token级别概率熵 | 忽略语义等价 |
| **序列熵** | 多个序列的概率熵 | 词汇级别，不考虑语义 |
| **语义熵** | 语义聚类后的熵 | 考虑语义等价 ✓ |

### 2.4 算法伪代码

```python
def semantic_entropy(model, question, num_samples=10):
    # Step 1: 生成多个回答
    responses = []
    probabilities = []
    for _ in range(num_samples):
        response, prob = model.generate_with_prob(question)
        responses.append(response)
        probabilities.append(prob)
    
    # Step 2: 语义聚类
    clusters = semantic_clustering(responses, nli_model)
    
    # Step 3: 计算语义熵
    cluster_probs = {}
    for cluster_id, members in clusters.items():
        cluster_probs[cluster_id] = sum(
            probabilities[i] for i in members
        )
    
    # 归一化
    total_prob = sum(cluster_probs.values())
    semantic_entropy = 0
    for prob in cluster_probs.values():
        p = prob / total_prob
        if p > 0:
            semantic_entropy -= p * np.log(p)
    
    return semantic_entropy
```

---

## 三、实验结果

### 3.1 数据集与设置

| 数据集 | 任务类型 | 特点 |
|--------|---------|------|
| **TriviaQA** | 开放域问答 | 事实性问题 |
| **CoQA** | 对话式问答 | 多轮对话 |

### 3.2 主要结果

**预测模型准确率的能力（AUROC）**：

| 方法 | TriviaQA | CoQA |
|------|----------|------|
| 最大概率 | 0.72 | 0.68 |
| 预测熵 | 0.75 | 0.71 |
| p(True) | 0.78 | 0.74 |
| **语义熵** | **0.82** | **0.79** |

### 3.3 关键发现

1. **语义熵优于所有基线**：在所有模型规模上都表现最佳
2. **大模型收益更大**：模型越大，语义熵的优势越明显
3. **无监督方法**：不需要额外训练，直接应用于现成模型

---

## 四、应用场景

### 4.1 幻觉检测

```
低语义熵 → 模型确定 → 可能正确
高语义熵 → 模型不确定 → 可能是幻觉
```

### 4.2 人机协作

| 语义熵 | 策略 |
|--------|------|
| 低 | 直接输出模型回答 |
| 中 | 提示用户确认 |
| 高 | 转交人工处理 |

### 4.3 主动学习

选择高语义熵的样本进行人工标注，提高标注效率。

---

## 五、关键见解与总结

### 5.1 核心贡献

1. **识别核心问题**：语义等价是自然语言不确定性估计的关键挑战
2. **提出优雅解决方案**：语义熵，简单而有效
3. **验证广泛有效**：多种任务、多种模型规模

### 5.2 局限性

- 依赖NLI模型进行语义聚类（可能引入误差）
- 计算成本较高（需要多次生成）
- 对长文本生成的适用性待验证

### 5.3 后续影响

- 被广泛应用于幻觉检测
- 衍生出多种改进方法（Evidential Semantic Entropy等）
- 成为LLM不确定性量化的基础方法

---

## 参考资源

- 论文链接: https://arxiv.org/abs/2302.09664
- 代码实现: https://github.com/lorenzkuhn/semantic-uncertainty
- 后续工作: "Detecting Hallucinations in LLMs Using Semantic Entropy"

---

*文档创建日期：2026年4月28日*
*论文来源：arXiv:2302.09664, ICLR 2023*