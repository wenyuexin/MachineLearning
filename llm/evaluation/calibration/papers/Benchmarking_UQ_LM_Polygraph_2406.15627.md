# Benchmarking Uncertainty Quantification Methods for Large Language Models with LM-Polygraph

**论文信息**
- 论文标题：Benchmarking Uncertainty Quantification Methods for Large Language Models with LM-Polygraph
- 中文标题：使用LM-Polygraph对大语言模型不确定性量化方法进行基准测试
- 作者：Roman Vashurin, Ekaterina Fadeeva, Artem Vazhentsev, Lyudmila Rvanova, Akim Tsvigun, Daniil Vasilev, Rui Xing, Abdelrahman Boda Sadallah, Kirill Grishchenkov, Sergey Petrakov, Alexander Panchenko, Timothy Baldwin, Preslav Nakov, Maxim Panov, Artem Shelmanov
- 机构：Mohamed bin Zayed University of AI, INSAIT, University of Melbourne, etc.
- arXiv: [2406.15627](https://arxiv.org/abs/2406.15627)
- 发表：TACL 2025, ACL 2025

---

## 一、论文整体思路

### 1.1 研究背景

大语言模型（LLM）的不确定性量化（UQ）方法众多，但缺乏统一的评估框架：
- 不同方法在不同任务上表现不一
- 缺乏公平对比的基准
- 实际应用中方法选择困难

### 1.2 核心贡献

1. **LM-Polygraph工具**：开源的LLM不确定性量化框架
2. **系统基准测试**：在多种任务上对比20+种UQ方法
3. **最佳实践**：针对不同场景的方法选择建议
4. **开源社区**：推动UQ研究的标准化

---

## 二、LM-Polygraph工具

### 2.1 工具架构

```
LM-Polygraph
├── 数据加载模块
│   ├── 问答数据集
│   ├── 对话数据集
│   └── 生成任务数据集
│
├── UQ方法库
│   ├── 基于概率的方法
│   ├── 基于采样的方法
│   └── 基于模型的方法
│
├── 评估模块
│   ├── AUROC
│   ├── AURC
│   └── ECE
│
└── 可视化模块
    ├── 可靠性图
    └── 拒绝曲线
```

### 2.2 支持的UQ方法

#### 2.2.1 基于概率的方法

| 方法 | 说明 | 白盒/黑盒 |
|------|------|----------|
| **Maximum Probability** | 最大token概率 | 白盒 |
| **Perplexity** | 困惑度 | 白盒 |
| **Mean Token Entropy** | 平均token熵 | 白盒 |
| **Length-normalized Probability** | 长度归一化概率 | 白盒 |

#### 2.2.2 基于采样的方法

| 方法 | 说明 | 白盒/黑盒 |
|------|------|----------|
| **Semantic Entropy** | 语义熵 | 白盒 |
| **Self-Consistency** | 自一致性 | 黑盒 |
| **p(True)** | 模型自我判断 | 黑盒 |
| **Monte Carlo Dropout** | MC Dropout | 白盒 |

#### 2.2.3 基于模型的方法

| 方法 | 说明 | 白盒/黑盒 |
|------|------|----------|
| **EigenScore** | 特征值分数 | 白盒 |
| **Mahalanobis Distance** | 马氏距离 | 白盒 |
| **PPL-based** | 基于困惑度的方法 | 白盒 |

### 2.3 使用示例

```python
from lm_polygraph import Polygraph

# 初始化
polygraph = Polygraph(model="gpt-3.5-turbo")

# 计算不确定性
result = polygraph.estimate_uncertainty(
    question="法国的首都是哪里？",
    methods=["semantic_entropy", "p_true", "self_consistency"]
)

print(result.uncertainties)
# {'semantic_entropy': 0.2, 'p_true': 0.85, 'self_consistency': 0.9}
```

---

## 三、基准测试设置

### 3.1 数据集

| 数据集 | 任务类型 | 样本量 | 特点 |
|--------|---------|--------|------|
| **TriviaQA** | 开放问答 | 10K | 事实性问题 |
| **CoQA** | 对话问答 | 5K | 多轮对话 |
| **GSM8K** | 数学推理 | 1K | 多步推理 |
| **TruthfulQA** | 真实性 | 800 | 测试幻觉 |
| **BioASQ** | 生物医学 | 500 | 专业领域 |

### 3.2 评估模型

| 模型 | 参数量 | 类型 |
|------|--------|------|
| **GPT-3.5** | 175B | 闭源 |
| **GPT-4** | ~1T | 闭源 |
| **LLaMA-2** | 7B/13B/70B | 开源 |
| **Vicuna** | 7B/13B | 开源 |
| **Mistral** | 7B | 开源 |

### 3.3 评估指标

| 指标 | 用途 | 说明 |
|------|------|------|
| **AUROC** | 预测准确性 | 不确定性预测准确率的能力 |
| **AURC** | 拒绝效果 | 拒绝不确定样本的效果 |
| **ECE** | 校准质量 | 置信度与准确率一致性 |

---

## 四、主要发现

### 4.1 方法排名

**问答任务（AUROC）**：

| 排名 | 方法 | AUROC | 计算成本 |
|------|------|-------|---------|
| 1 | **Semantic Entropy** | 0.82 | 中 |
| 2 | Self-Consistency | 0.79 | 高 |
| 3 | p(True) | 0.76 | 低 |
| 4 | Mean Token Entropy | 0.74 | 低 |
| 5 | Maximum Probability | 0.71 | 低 |

### 4.2 关键发现

#### 发现1：语义方法最优

```
语义感知方法 > 传统概率方法

原因：考虑语义等价，避免误判
```

#### 发现2：模型规模影响

| 模型规模 | 最佳方法 | 效果提升 |
|---------|---------|---------|
| 小模型 (<10B) | p(True) | +5% |
| 中模型 (10-70B) | Self-Consistency | +8% |
| 大模型 (>70B) | Semantic Entropy | +12% |

#### 发现3：任务相关性

| 任务类型 | 推荐方法 |
|---------|---------|
| 事实问答 | Semantic Entropy |
| 数学推理 | Self-Consistency |
| 对话任务 | p(True) |
| 代码生成 | Mean Token Entropy |

### 4.3 计算效率对比

| 方法 | 相对成本 | 适用场景 |
|------|---------|---------|
| Maximum Probability | 1x | 实时应用 |
| p(True) | 1.5x | 资源受限 |
| Semantic Entropy | 5x | 高价值决策 |
| Self-Consistency | 10x | 离线分析 |

---

## 五、最佳实践

### 5.1 方法选择指南

```mermaid
flowchart TD
    A[选择UQ方法] --> B{是否白盒访问?}
    B -->|是| C{计算资源?}
    B -->|否| D{计算资源?}
    
    C -->|充足| E[Semantic Entropy]
    C -->|有限| F[Mean Token Entropy]
    
    D -->|充足| G[Self-Consistency]
    D -->|有限| H[p(True)]
```

### 5.2 实践建议

| 场景 | 推荐方法 | 理由 |
|------|---------|------|
| 实时系统 | Max Probability / p(True) | 计算效率高 |
| 高风险决策 | Semantic Entropy | 准确性最高 |
| 黑盒API | Self-Consistency | 无需内部访问 |
| 多样化任务 | 集成多种方法 | 互补优势 |

### 5.3 阈值设置

```
幻觉检测阈值建议

高风险领域（医疗、法律）：
├── 语义熵 > 0.3 → 需要验证
└── 语义熵 > 0.5 → 拒绝输出

一般应用：
├── 语义熵 > 0.5 → 附不确定性声明
└── 语义熵 > 0.7 → 转人工处理
```

---

## 六、工具使用

### 6.1 安装

```bash
pip install lm-polygraph
```

### 6.2 快速开始

```python
from lm_polygraph import Polygraph, Estimators

# 创建评估器
estimators = [
    Estimators.SemanticEntropy(),
    Estimators.PTrue(),
    Estimators.SelfConsistency()
]

# 初始化
pg = Polygraph(
    model_name="meta-llama/Llama-2-7b-chat-hf",
    estimators=estimators
)

# 评估
results = pg.evaluate_dataset("trivia_qa")
print(results.summary())
```

### 6.3 自定义评估

```python
# 自定义阈值
pg.set_threshold("semantic_entropy", 0.4)

# 批量评估
results = pg.batch_evaluate(
    questions=question_list,
    save_path="results.json"
)
```

---

## 七、关键见解与总结

### 7.1 核心贡献

1. **统一框架**：LM-Polygraph提供标准化UQ评估
2. **系统对比**：首次大规模基准测试LLM UQ方法
3. **实用指南**：帮助实践者选择合适方法

### 7.2 主要结论

- **语义熵最佳**：综合效果最好，推荐作为首选
- **效率权衡**：根据计算资源选择方法
- **任务相关**：不同任务最佳方法不同

### 7.3 未来方向

- 更多任务类型
- 多模态UQ
- 高效近似方法
- 与RAG结合

---

## 参考资源

- 论文链接: https://arxiv.org/abs/2406.15627
- GitHub: https://github.com/IINemo/lm-polygraph
- 文档: https://lm-polygraph.readthedocs.io/

---

*文档创建日期：2026年4月28日*
*论文来源：arXiv:2406.15627, TACL 2025*