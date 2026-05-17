# Backlog

本目录处于活跃建设期，以下为已识别但尚未覆盖的相关论文与内容缺口。

## ✅ 已完成

| 论文 | 来源 | 笔记 |
|------|------|------|
| Gold Panning: Turning Positional Bias into Signal (Byerly & Khashabi, 2025) | arXiv 2510.09770 | [GoldPanning_2510.09770.md](./papers/GoldPanning_2510.09770.md) |
| What Works for "Lost-in-the-Middle"? (Gupte et al., 2025) | arXiv 2511.13900 | [WhatWorks_LostInTheMiddle_2511.13900.md](./papers/WhatWorks_LostInTheMiddle_2511.13900.md) |
| A Residual-Aware Theory of Position Bias (Herasimchyk et al., 2026) | OpenReview / arXiv 2602.16837 | [ResidualAwareTheory_2602.16837.md](./papers/ResidualAwareTheory_2602.16837.md) |
| On the Emergence of Position Bias in Transformers (Wu et al., 2025) | arXiv 2502.01951 / ICML 2025 | [EmergenceOfPositionBias_2502.01951.md](./papers/EmergenceOfPositionBias_2502.01951.md) |
| Distance between Relevant Information Pieces Causes Bias (Tian et al., 2025) | ACL 2025 Findings, arXiv 2410.14641 | [DistanceBias_2410.14641.md](./papers/DistanceBias_2410.14641.md) |

## P2 中等优先级

| 论文 | 分类 | 来源 | 关联已有论文 | 为何需要 |
|------|------|------|------------|---------|
| Mitigate Position Bias via Scaling a Single Hidden Channel (Yu et al., 2025) | 缓解方法 | ACL 2025, arXiv 2406.06440 | FoundInTheMiddle | 单通道缩放即可缓解偏差，最高 +15.2%，与注意力校准正交；揭示位置偏差在表征空间中有独特集中的编码方式 |
| Never Lost in the Middle (Huang et al.) | 缓解方法 | arXiv 2509.06367 | FoundInTheMiddle | 从训练阶段增强模型的信息搜索和反思能力，与推理时缓解方法互补 |
| Positional Biases Shift as Inputs Approach Context Window Limits (Acharya et al., 2025) | 评估诊断 | arXiv 2508.08201 | EmergentProperty | 发现位置偏差在上下文逼近极限时变化，对 RAG 系统的上下文长度选择有重要参考 |
| Retrieval Quality at Context Limit (Acharya et al., 2025) | 评估诊断 | arXiv 2511.08201 | EmergentProperty | 探讨检索质量与上下文限制的关系（与上一条同作者但不同方向） |
| Self-Consistency Falls Short! Adverse Effects of Positional Bias (2026) | 方法论 | arXiv 2604.08528 | 全体 | 验证自洽性方法在长上下文下因位置偏差而失效，对 RAG 实践中的一个常见假设提出质疑 |

## P3 低优先级

| 内容 | 分类 | 说明 |
|------|------|------|
| Layer-Specific Scaling of Positional Encodings (2025) | 位置编码改进 | 与位置编码设计中的距离衰减/振荡问题一脉相承，放在 `positional-encoding/` 更合适 |
| HoPE: Hyperbolic Rotary Positional Encoding (Dai et al., 2025) | 位置编码改进 | arXiv 2509.05218，同上 |
| 注意力汇聚（Attention Sink）原论文 (Xiao et al., 2023) | 基础概念 | 放在 `attention-mechanisms/` 更合适，此处仅需引用链接 |
| LongBench, NIAH 等长上下文基准 | 评估 | 已在 `llm/05-evaluation/benchmarks/` 下，不需重复 |
| 多跳问答中的 Lost in the Middle (2024) | 扩展研究 | 可关注后决定是否单独笔记 |

---

*最后更新: 2026-05-17*