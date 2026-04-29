# Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs

**论文信息**
- 论文标题：Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs
- 中文标题：LLM能表达不确定性吗？LLM置信度引出的实证评估
- 作者：Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, Bryan Hooi
- 机构：National University of Singapore, Singapore Management University, Hong Kong University of Science and Technology
- arXiv: [2306.13063](https://arxiv.org/abs/2306.13063)
- 发表：ICLR 2024

---

## 一、论文整体思路

### 1.1 研究问题

**核心问题**：LLM能否可靠地表达自己的不确定性？

当被问及"你有多确信这个答案？"时：
- 模型能否给出准确的置信度？
- 不同引出方法的效果如何？
- 什么因素影响置信度表达？

### 1.2 研究背景

LLM的回答通常缺乏置信度信息，这对高风险应用构成挑战。理想情况下，模型应该：
- 在确定时给出高置信度
- 在不确定时承认不确定

### 1.3 主要贡献

1. **系统评估**：首次大规模评估LLM置信度表达能力
2. **方法对比**：对比多种置信度引出方法
3. **因素分析**：分析影响置信度表达的因素
4. **改进建议**：提出提高置信度可靠性的方法

---

## 二、置信度引出方法

### 2.1 方法分类

```
置信度引出方法
├── 语言表达方法
│   ├── 数字置信度（1-10）
│   ├── 语言置信度（非常确定/不太确定）
│   └── 概率表达（90%确定）
│
├── 多选表达方法
│   ├── Verbalized Confidence
│   └── Multiple-Choice Selection
│
└── 一致性方法
    ├── Self-Consistency
    └── p(True)
```

### 2.2 核心方法详解

#### 2.2.1 Verbalized Confidence

直接询问模型的置信度：

```
问题: {question}
回答: {answer}
你有多大把握这个答案是正确的？请给出1-10的评分。
```

#### 2.2.2 p(True)

让模型判断答案是否正确：

```
问题: {question}
答案: {answer}
这个答案是否正确？回答 True 或 False。
```

#### 2.2.3 Self-Consistency

多次采样，计算答案一致性：

$$\text{Confidence} = \frac{\text{最常见答案出现次数}}{\text{总采样次数}}$$

### 2.3 Prompt模板

**数字置信度**：
```
Please answer the following question and provide your confidence 
level from 0% to 100%:

Question: {question}

Answer: [Your answer]
Confidence: [0-100]%
```

**语言置信度**：
```
After answering the question, indicate your confidence level:
- Very confident
- Somewhat confident  
- Not very confident

Question: {question}
```

---

## 三、实验设计

### 3.1 数据集

| 数据集 | 任务类型 | 样本量 |
|--------|---------|--------|
| **TriviaQA** | 事实问答 | 10K |
| **SciQ** | 科学问答 | 5K |
| **TruthfulQA** | 真实性测试 | 800 |
| **StrategyQA** | 策略推理 | 2K |

### 3.2 评估模型

| 模型 | 参数量 | 特点 |
|------|--------|------|
| **GPT-3.5** | 175B | 闭源 |
| **GPT-4** | ~1T | 闭源 |
| **LLaMA-2** | 7B-70B | 开源 |
| **Vicuna** | 7B-13B | 开源 |
| **Mistral** | 7B | 开源 |

### 3.3 评估指标

| 指标 | 说明 |
|------|------|
| **AUROC** | 预测准确率的能力 |
| **ECE** | 校准误差 |
| **Correlation** | 置信度与准确率相关性 |

---

## 四、主要发现

### 4.1 核心发现

#### 发现1：LLM总体上能表达不确定性

```
结论：模型置信度与实际准确率正相关

高置信度回答 → 准确率更高
低置信度回答 → 准确率更低
```

#### 发现2：不同方法效果差异大

| 方法 | AUROC | ECE | 计算成本 |
|------|-------|-----|---------|
| Verbalized (数字) | 0.72 | 0.18 | 低 |
| p(True) | 0.76 | 0.15 | 低 |
| Self-Consistency | 0.79 | 0.12 | 高 |
| Token Probability | 0.71 | 0.22 | 低 |

#### 发现3：模型规模影响显著

| 模型规模 | 置信度表达质量 |
|---------|---------------|
| 小模型 (<10B) | 较差，过度自信 |
| 中模型 (10-70B) | 中等 |
| 大模型 (>70B) | 较好，更校准 |

### 4.2 影响因素

#### 因素1：问题难度

```
简单问题 → 置信度更准确
困难问题 → 容易过度自信
```

#### 因素2：答案格式

| 格式 | 校准质量 |
|------|---------|
| 简短答案（是/否）| 较好 |
| 多选答案 | 中等 |
| 开放生成 | 较差 |

#### 因素3：Prompt设计

```
明确要求置信度 → 效果更好
默认不要求 → 效果较差
```

### 4.3 问题识别

**过度自信现象**：
- 错误答案也给出高置信度
- 平均置信度高于实际准确率

**校准不良**：
- ECE普遍较高（0.15-0.25）
- 小模型问题更严重

---

## 五、改进方法

### 5.1 Prompt优化

**Few-shot Prompting**：
```
示例1:
问题: 地球到月球距离？
答案: 约38万公里
置信度: 95%
（正确，高置信度）

示例2:
问题: 宇宙的年龄？
答案: 138亿年
置信度: 60%
（正确但不确定，适度置信度）

现在请回答：
问题: {question}
```

### 5.2 一致性检查

```python
def confidence_with_consistency(model, question, n_samples=5):
    # 生成多个答案
    answers = [model.generate(question) for _ in range(n_samples)]
    
    # 检查一致性
    unique_answers = set(answers)
    if len(unique_answers) == 1:
        return "High confidence"
    else:
        return f"Low confidence ({len(unique_answers)} different answers)"
```

### 5.3 置信度校准

**Temperature Scaling**：
- 在验证集上优化温度参数
- 不改变预测，只调整置信度

---

## 六、实践建议

### 6.1 方法选择

```
场景决策树

是否需要实时响应？
├── 是 → Verbalized Confidence / p(True)
└── 否 → Self-Consistency

模型是否可访问内部概率？
├── 是 → Token Probability + Verbalized
└── 否 → Self-Consistency
```

### 6.2 阈值设置

| 应用场景 | 低置信度阈值 | 行为 |
|---------|-------------|------|
| 高风险（医疗）| 0.8 | 转人工 |
| 中风险（客服）| 0.6 | 提示不确定 |
| 低风险（推荐）| 0.4 | 正常输出 |

### 6.3 综合策略

```
最佳实践

1. 结合多种方法
   ├── Verbalized Confidence（快速估计）
   └── Self-Consistency（验证确认）

2. 考虑问题难度
   └── 困难问题降低置信度阈值

3. 监控校准质量
   └── 定期评估ECE
```

---

## 七、关键见解与总结

### 7.1 核心结论

1. **LLM能表达不确定性**，但表达质量有限
2. **方法选择重要**，Self-Consistency效果最佳
3. **模型规模相关**，大模型表达更准确
4. **仍需校准**，原始置信度不够可靠

### 7.2 局限性

- 仅评估短答案任务
- 未覆盖长文本生成
- 开源模型评估有限

### 7.3 未来方向

- 长文本生成的不确定性表达
- 多模态场景扩展
- 自适应置信度校准

---

## 参考资源

- 论文链接: https://arxiv.org/abs/2306.13063
- 代码仓库: https://github.com/MiaoXiong2320/llm-uncertainty
- 相关论文: "Just Ask for Calibration" (ICLR 2024)

---

*文档创建日期：2026年4月28日*
*论文来源：arXiv:2306.13063, ICLR 2024*