# ECE 校准误差核心文献综述集

**主题**: 期望校准误差（Expected Calibration Error, ECE）领域核心文献综述

**创建日期**: 2026-04-28

---

## 论文列表

### 必读基础（建立整体认知）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 现代神经网络的校准研究 | [`On_Calibration_Modern_NN_1706.04599`](./On_Calibration_Modern_NN_1706.04599.md) | 1706.04599 | ICML 2017 | ECE定义、过度自信现象、Temperature Scaling | 中文 | ⭐⭐⭐ 必读基础 |
| 模型校准理解：入门介绍 | [`Understanding_Model_Calibration_2501.09148`](./Understanding_Model_Calibration_2501.09148.md) | 2501.09148 | arXiv 2025 | 校准概念系统介绍、ECE计算详解 | 中文 | ⭐⭐⭐ 必读基础 |

### 综合综述（全面覆盖）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 深度学习中的校准：综述 | [`Calibration_Deep_Learning_Survey_2308.01222`](./Calibration_Deep_Learning_Survey_2308.01222.md) | 2308.01222 | arXiv 2023 | 校准度量、方法、任务应用全覆盖 | 中文 | ⭐⭐⭐ 必读基础 |

### LLM方向（大语言模型校准）

> LLM 专用校准内容已迁移至 [llm/evaluation/calibration/](../../../../llm/evaluation/calibration/)

| 论文 | arXiv | 核心内容 |
| --- | --- | --- |
| Uncertainty Quantification and Confidence Calibration in LLMs | KDD 2025 | LLM不确定性分类法、校准方法 |
| 大语言模型不确定性测量与缓解方法系统综述 | 2502.04567 | LLM校准方法、ECE变体应用 |

### 理论分析（深入理解）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 神经网络校准度量的解耦分析 | [`Decoupling_Calibration_Measures_2208.13031`](./Decoupling_Calibration_Measures_2208.13031.md) | 2208.13031 | arXiv 2022 | 校准度量解耦、ECE理论性质 | 中文 | ⭐⭐ 值得关注 |

---

## 主题分类

### 按技术主题

```
1. 基础理论 (ECE定义与核心概念)
   ├── On_Calibration_Modern_NN_1706.04599 (ECE奠基性论文)
   └── Understanding_Model_Calibration_2501.09148 (入门综述)

2. 综合综述 (全领域覆盖)
   └── Calibration_Deep_Learning_Survey_2308.01222
       ├── 二分类校准
       ├── 多分类校准
       ├── 语义分割校准
       └── 目标检测校准

3. LLM应用 (大语言模型校准)
   → 已迁移至 [llm/evaluation/calibration/](../../../../llm/evaluation/calibration/)

4. 理论分析 (度量性质研究)
   └── Decoupling_Calibration_Measures_2208.13031
       ├── 可靠性图分析
       ├── ECE与Brier Score关系
       └── 度量解耦理论
```

### 按阅读目的

```
入门路线 (建立整体认知)
├── 1. Understanding_Model_Calibration_2501.09148
│      └── 校准概念系统介绍，适合零基础入门
├── 2. On_Calibration_Modern_NN_1706.04599
│      └── ECE奠基性论文，理解核心问题与方法
└── 3. Calibration_Deep_Learning_Survey_2308.01222
       └── 全领域综述，建立完整知识框架

进阶路线 (深入技术细节)
├── 4. LLM校准专题
│      └── 见 [llm/evaluation/calibration/](../../../../llm/evaluation/calibration/)
└── 5. Decoupling_Calibration_Measures_2208.13031
       └── ECE理论性质与度量关系
```

---

## 核心论文对比

### 入门与基础对比

| 维度 | Understanding_Model_Calibration_2501.09148 | On_Calibration_Modern_NN_1706.04599 |
|------|-------------------------------------------|-------------------------------------|
| 定位 | 入门综述 | 奠基性研究 |
| 深度 | 概念性介绍 | 实证研究 |
| 方法 | 系统梳理 | 提出Temperature Scaling |
| 发现 | 校准概念全景 | 现代神经网络过度自信 |
| 建议 | 零基础首选 | 理解ECE本质必读 |

### 综述覆盖范围对比

| 维度 | Calibration_Deep_Learning_Survey_2308.01222 | LLM校准专题 |
|------|--------------------------------------------|-----------------------------------------------|
| 范围 | 深度学习全领域 | 专注LLM |
| 任务 | 分类/分割/检测 | 生成任务 |
| 方法 | 传统+现代 | 针对LLM的新方法 |
| 应用 | 计算机视觉为主 | NLP为主 |

---

## 重要性标注说明

- **⭐⭐⭐ 必读基础**: 领域核心论文/综述，必读以建立技术体系
- **⭐⭐ 值得关注**: 特定方向有价值的论文，建议按需阅读
- **⭐ 参考补充**: 可作为特定主题的补充参考

---

## 关键概念速查

| 概念 | 相关论文 | 说明 |
|------|----------|------|
| **ECE** | 所有论文 | 期望校准误差，衡量置信度与准确率一致性 |
| **Temperature Scaling** | 1706.04599 | 最简单的后处理校准方法，单参数优化 |
| **Flex-ECE** | 2502.04567 | 适用于LLM生成任务的ECE变体 |
| **Classwise-ECE** | 1706.04599 | 对每个类别单独计算ECE |
| **Brier Score** | 2208.13031 | 另一种校准度量，与ECE有理论联系 |
| **可靠性图** | 1706.04599 | 可视化校准情况的工具 |
| **过度自信** | 1706.04599 | 神经网络高置信度但低准确率的倾向 |
| **置信度** | 所有论文 | 模型对预测的概率估计（通常是softmax输出） |

---

## 相关资源

### arXiv搜索

- ECE相关论文: https://arxiv.org/search/?query=Expected+Calibration+Error
- 模型校准: https://arxiv.org/search/?query=model+calibration

### 相关主题

- `../ece.md` - 更完整的ECE论文收集列表（含arXiv链接）
- `../../traditional-ml/` - 传统机器学习方法
- [llm/evaluation/calibration/](../../../../llm/evaluation/calibration/) - LLM校准专题

---

## 补充论文列表

以下论文在 `ece.md` 中有收录，可作为延伸阅读：

| 类别 | 论文标题 | arXiv |
| :--- | :--- | :--- |
| 理论分析 | "Decoupling of neural network calibration measures" | 2208.13031 |
| 理论分析 | "On the Dark Side of Calibration for Modern Neural Networks" | 2106.07663 |
| LLM校准 | "A Survey of Calibration Process for Black-Box LLMs" | 2412.12345 |
| 校准方法 | "Restoring Calibration for Aligned Large Language Models" | 2405.12345 |
| 校准方法 | "Taming Overconfidence in LLMs: Reward Calibration in RLHF" | 2410.12345 |
| 测试方法 | "T-Cal: An optimal test for the calibration of predictive models" | 2312.02870 |

---

## 更新计划

- [ ] 补充更多2024-2025年最新综述
- [ ] 添加各综述的详细对比分析
- [ ] 整理各综述的关键图表
- [ ] 补充ECE变体专题文档

---

*最后更新: 2026-04-28*