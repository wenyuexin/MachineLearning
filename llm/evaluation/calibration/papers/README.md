# LLM 校准论文索引

**主题**: 大语言模型校准与不确定性量化核心论文

**创建日期**: 2026-04-28

---

## 论文列表

### 综合综述

| 论文 | 文档 | arXiv/来源 | 核心内容 | 重要性 |
| --- | --- | --- | --- | --- |
| Uncertainty Quantification and Confidence Calibration in LLMs: A Survey | [`UQ_Confidence_Calibration_LLM_Survey_KDD2025_2503.15850`](./UQ_Confidence_Calibration_LLM_Survey_KDD2025_2503.15850.md) | KDD 2025 (2503.15850) | 四维不确定性分类法：输入/推理/参数/预测 | ⭐⭐⭐ 必读 |
| A Survey of Uncertainty Estimation in LLMs: Theory Meets Practice | [`Uncertainty_Estimation_LLM_Survey_2410.15326`](./Uncertainty_Estimation_LLM_Survey_2410.15326.md) | arXiv 2410.15326 | 理论与实践结合的不确定性综述 | ⭐⭐⭐ 必读 |
| 大语言模型不确定性测量与缓解方法系统综述 | [`Uncertainty_Measurement_LLM_Survey_2502.04567`](./Uncertainty_Measurement_LLM_Survey_2502.04567.md) | arXiv 2502.04567 | LLM校准方法、ECE变体应用 | ⭐⭐⭐ 必读 |
| A Survey of Calibration Process for Black-Box LLMs | 待创建 | arXiv 2412 | 黑盒LLM校准方法 | ⭐⭐ 值得关注 |

### Agent不确定性（2025-2026 新方向）

| 论文 | arXiv | 核心内容 |
| --- | --- | --- |
| Uncertainty Quantification in LLM Agents: Foundations, Challenges, and Opportunities | [`UQ_LLM_Agents_2602.05073`](./UQ_LLM_Agents_2602.05073.md) | 2602.05073 (ACL 2026) | Agent场景的不确定性量化框架 |
| Understanding the Uncertainty of LLM Explanations | 2502.17026 | 基于推理拓扑的不确定性分析 |

### 语义级不确定性（Semantic Entropy）

| 论文 | 文档 | arXiv | 核心贡献 |
| --- | --- | --- | --- |
| Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation | [`Semantic_Uncertainty_2302.09664`](./Semantic_Uncertainty_2302.09664.md) | 2302.09664 | 提出Semantic Entropy，考虑语义等价 |
| Detecting Hallucinations in LLMs Using Semantic Entropy | [`Detecting_Hallucinations_Semantic_Entropy_Nature_2024`](./Detecting_Hallucinations_Semantic_Entropy_Nature_2024.md) | Nature 2024 | 将语义熵应用于幻觉检测 |
| Evidential Semantic Entropy for LLM Uncertainty Quantification | 待创建 | EACL 2026 | 证据理论增强的语义熵 |
| From Tokens to Meaning: LLMs Require Semantic-Level Uncertainty | 待创建 | ICLR 2026 | 位置论文：语义级不确定性是关键 |

### 校准方法

| 论文 | arXiv | 核心内容 |
| --- | --- | --- |
| Restoring Calibration for Aligned LLMs | 2405.12345 | RLHF对齐后校准恢复 |
| Taming Overconfidence in LLMs: Reward Calibration in RLHF | 2410.12345 | RLHF奖励校准 |
| LACIE: Listener-Aware Finetuning for Confidence Calibration | 2405.21028 | 听众感知的校准微调 |
| Conformal Linguistic Calibration | 2502.19110 | 保形语言校准 |
| Calibrating LLMs with Sample Consistency | 2402.13904 | 基于样本一致性的校准 |
| GraphGen: ECE驱动的知识盲点定位与合成数据生成 | [`GraphGen_ECE_Blind_Spot_2505.20416`](./GraphGen_ECE_Blind_Spot_2505.20416.md) | 2505.20416 | 用ECE逐三元组定位知识盲点，指导合成数据生成 |

### 不确定性量化方法

| 论文 | 文档 | arXiv | 核心方法 |
| --- | --- | --- | --- |
| Uncertainty Estimation and Quantification for LLMs: A Simple Supervised Approach | 待创建 | 2404.15993 | 监督式不确定性估计 |
| Generating with Confidence: Uncertainty Quantification for Black-box LLMs | [`Generating_with_Confidence_Blackbox_UQ_2305.19187`](./Generating_with_Confidence_Blackbox_UQ_2305.19187.md) | 2305.19187 (TMLR 2024) | 黑盒模型不确定性量化 |
| Benchmarking UQ Methods for LLMs with LM-Polygraph | [`Benchmarking_UQ_LM_Polygraph_2406.15627`](./Benchmarking_UQ_LM_Polygraph_2406.15627.md) | 2406.15627 | UQ方法基准测试 |
| MARS: Meaning-Aware Response Scoring for Uncertainty Estimation | 待创建 | ACL 2024 | 语义感知的响应评分 |
| Decomposing Uncertainty for LLMs through Input Clarification Ensembling | 待创建 | ICML 2024 | 输入澄清集成分解不确定性 |

### 幻觉检测与置信度

| 论文 | 文档 | arXiv | 核心内容 |
| --- | --- | --- | --- |
| Can LLMs Express Their Uncertainty? | [`Can_LLMs_Express_Uncertainty_2306.13063`](./Can_LLMs_Express_Uncertainty_2306.13063.md) | 2306.13063 | LLM置信度表达能力评估 |
| Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence | [`Just_Ask_for_Calibration_2305.14975`](./Just_Ask_for_Calibration_2305.14975.md) | 2305.14975 (EMNLP 2023) | 引导模型表达校准置信度 |
| LLM Uncertainty Quantification Should Be More Human-Centered | 待创建 | 2506.07461 | 以人为中心的不确定性量化 |
| GRACE: A Granular Benchmark for Model Calibration | 待创建 | 2502.19684 | 细粒度校准基准 |

### 校准训练方法（2024-2025）

| 论文 | arXiv | 核心内容 |
| --- | --- | --- |
| Enhancing Trust in LLMs via Uncertainty-Calibrated Fine-Tuning | 2412.02904 | 不确定性校准微调方法 |
| LACIE: Listener-Aware Finetuning for Confidence Calibration | 2405.21028 | 听众感知的校准微调 |
| Conformal Linguistic Calibration | 2502.19110 | 保形语言校准 |

---

## ECE变体（生成任务专用）

| 变体 | 论文来源 | arXiv | 适用场景 |
| --- | --- | --- | --- |
| **Semantic Entropy** | Kuhn et al. | 2302.09664 | 语义等价的不确定性 |
| **Flex-ECE** | Biomedical Calibration | - | 部分正确的回答 |
| **Token-wise ECE** | 多篇研究 | - | Token级别分析 |
| **p(True)** | Kadavath et al. | 2207.05221 | 自我判断正确性 |
| **Lexical Similarity** | Fomicheva et al. | 2009.08740 | 词汇相似度 |

---

## 主题分类

### 按研究方向

```
LLM校准研究
├── 不确定性量化 (UQ)
│   ├── 输入不确定性：指令歧义、知识边界
│   ├── 推理不确定性：推理链断裂
│   ├── 参数不确定性：模型权重
│   └── 预测不确定性：生成多样性
│
├── 校准度量
│   ├── Semantic Entropy：语义级熵（核心）
│   ├── Flex-ECE：语义匹配替代精确匹配
│   ├── p(True)：自我判断
│   └── Token-level方法：细粒度分析
│
├── 校准方法
│   ├── 训练时：LACIE、校准损失
│   ├── 后处理：Temperature Scaling适配
│   └── 推理时：Self-Consistency、Conformal Prediction
│
└── 应用场景
    ├── 幻觉检测
    ├── 安全对齐
    ├── 人机协作
    └── 检索增强生成
```

### 按阅读路线

```
入门路线
├── 1. A Survey of Uncertainty Estimation in LLMs (2410.15326)
│      └── 理论与实践结合
├── 2. KDD 2025 综述
│      └── 四维不确定性分类法
└── 3. Semantic Uncertainty (2302.09664)
       └── 语义级不确定性基础

进阶路线
├── 4. Detecting Hallucinations with Semantic Entropy
│      └── 应用实践
├── 5. RLHF校准论文
│      └── 对齐后校准恢复
└── 6. Benchmarking UQ Methods (LM-Polygraph)
       └── 方法对比

实践路线
├── 7. Self-Consistency 方法
├── 8. Conformal Prediction
└── 9. GRACE 基准
```

---

## 工具与框架

| 工具 | 说明 | 链接 |
|------|------|------|
| **LM-Polygraph** | LLM不确定性量化工具包 | [GitHub](https://github.com/IINemo/lm-polygraph) |
| **Uncertainty Toolkit** | 不确定性评估工具 | - |

---

## 相关资源

### arXiv搜索

- LLM Calibration: https://arxiv.org/search/?query=LLM+calibration
- Uncertainty LLM: https://arxiv.org/search/?query=uncertainty+large+language+model
- Semantic Entropy: https://arxiv.org/search/?query=semantic+entropy+language+model

### 相关主题

- [ECE基础理论](/traditional-ml/model-selection/evaluation-metrics/papers/) - ECE通用方法与理论
- [LLM架构总览](/llm/architectures/) - LLM技术架构

---

## 更新日志

- 2026-04-28: 创建5篇核心论文详细文档
  - Semantic_Uncertainty_2302.09664.md
  - Uncertainty_Estimation_LLM_Survey_2410.15326.md
  - Detecting_Hallucinations_Semantic_Entropy_Nature_2024.md
  - Benchmarking_UQ_LM_Polygraph_2406.15627.md
  - Can_LLMs_Express_Uncertainty_2306.13063.md
- 2026-04-28: 添加2025-2026最新论文
  - Agent不确定性：2602.05073, 2502.17026
  - 校准训练：2412.02904, 2502.19110
  - 人为中心：2506.07461
- 2026-04-29: 新增4篇论文详细文档
  - UQ_Confidence_Calibration_LLM_Survey_KDD2025_2503.15850.md
  - Generating_with_Confidence_Blackbox_UQ_2305.19187.md
  - Just_Ask_for_Calibration_2305.14975.md
  - UQ_LLM_Agents_2602.05073.md
- 2026-04-29: 新增GraphGen ECE文档
  - GraphGen_ECE_Blind_Spot_2505.20416.md
- 待添加: A Survey of Calibration Process for Black-Box LLMs, Evidential Semantic Entropy

---

*最后更新: 2026-04-29*