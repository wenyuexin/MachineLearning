# LLM长上下文综述论文集

**主题**: 大语言模型长上下文（Long Context）领域核心综述论文

**创建日期**: 2026-04-26

---

## 论文列表

### 综合入门（建立整体认知）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 长上下文语言建模综合综述 | [`Comprehensive_Survey_Long_Context_LM_2503.17407`](./Comprehensive_Survey_Long_Context_LM_2503.17407.md) | 2503.17407 | arXiv 2025 | 架构-训练-评估管线全覆盖 | 中文 | ⭐⭐⭐ 必读基础 |
| 论长上下文大语言模型 | [`Thus_Spake_Long_Context_LLM_2502.17129`](./Thus_Spake_Long_Context_LLM_2502.17129.md) | 2502.17129 | arXiv 2025 | 架构-基建-训练-评估四维全景 | 中文 | ⭐⭐⭐ 必读基础 |

### 侧重架构（Transformer架构改进）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 长上下文LLM中Transformer架构进展 | [`Advancing_Transformer_Architecture_Long_Context_2311.12351`](./Advancing_Transformer_Architecture_Long_Context_2311.12351.md) | 2311.12351 | arXiv 2024 | Transformer架构层面改进深度分析 | 中文 | ⭐⭐⭐ 必读基础 |

### 侧重方法（上下文扩展方法分类）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| Transformer上下文扩展方法与评估 | [`Transformer_Context_Extension_Survey_2503.13299`](./Transformer_Context_Extension_Survey_2503.13299.md) | 2503.13299 | arXiv 2025 | 四类增强方法分类：位置编码、压缩、检索、注意力 | 中文 | ⭐⭐⭐ 必读基础 |

### 侧重优化（推理优化技术）

| 论文 | 文档 | 链接 | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 长上下文LLM推理优化综述 | [`Long_Context_LLM_Inference_Optimization_Survey`](./Long_Context_LLM_Inference_Optimization_Survey.md) | [DOAJ](https://doaj.org/article/e23dc9d6d575493cb01595ee91ccb1b8) | 期刊 2025 | 模型优化、计算优化、系统优化三级体系 | 中文 | ⭐⭐ 值得关注 |
| 大语言模型长上下文推理优化综述 | [`Long_Context_Inference_Optimization_CN`](./Long_Context_Inference_Optimization_CN.md) | [大数据期刊](https://www.j-bigdataresearch.com.cn/CN/abstract/abstract370.shtml) | 大数据 2025 | 中文视角的推理优化综述 | 中文 | ⭐⭐ 值得关注 |

### 理论思辨（评估范式批判）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 如果只需检索就能解决，还算是真正的长上下文吗？ | [`Is_It_Really_Long_Context_EMNLP2024`](./Is_It_Really_Long_Context_EMNLP2024.md) | 2407.00402 | EMNLP 2024 | 批判性审视评估范式，提出Diffusion×Scope分类 | 中文 | ⭐⭐⭐ 必读基础 |

### 应用导向（上下文注入与服务部署）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 超越参数：上下文增强技术综述 | [`Beyond_Parameters_Context_Injection_2604.03174`](./Beyond_Parameters_Context_Injection_2604.03174.md) | 2604.03174 | arXiv 2026 | ICL→RAG→GraphRAG→CausalRAG谱系 | 中文 | ⭐⭐ 值得关注 |
| LLM服务的CAP原则 | [`CAP_Principle_LLM_Serving_2405.11299`](./CAP_Principle_LLM_Serving_2405.11299.md) | 2405.11299 | arXiv 2024 | CAP三角：上下文长度-准确性-性能 | 中文 | ⭐⭐ 值得关注 |

### 专项调查（基础方法回顾）

| 论文 | 文档 | arXiv | 发表 | 核心内容 | 语言 | 重要性 |
| --- | --- | --- | --- | --- | --- | --- |
| 基于Transformer的长文本建模综述 | [`Long_Text_Modeling_Transformers_2302.14502`](./Long_Text_Modeling_Transformers_2302.14502.md) | 2302.14502 | arXiv 2023 | 长文本建模的经典方法回顾 | 中文 | ⭐⭐ 值得关注 |

---

## 主题分类

### 按技术主题

```
1. 综合综述 (全管线覆盖)
   ├── Comprehensive_Survey_Long_Context_LM_2503.17407 (架构-训练-评估)
   └── Thus_Spake_Long_Context_LLM_2502.17129 (架构-基建-训练-评估)

2. 架构改进 (Transformer层面)
   ├── Advancing_Transformer_Architecture_Long_Context_2311.12351 (架构深度分析)
   ├── Transformer_Context_Extension_Survey_2503.13299 (四类方法)
   └── Long_Text_Modeling_Transformers_2302.14502 (经典方法回顾)

3. 推理优化 (部署效率)
   ├── Long_Context_LLM_Inference_Optimization_Survey (英文期刊)
   ├── Long_Context_Inference_Optimization_CN (中文期刊)
   └── CAP_Principle_LLM_Serving_2405.11299 (服务框架)

4. 评估与思辨 (评估范式)
   └── Is_It_Really_Long_Context_EMNLP2024 (批判性视角)

5. 上下文增强 (RAG与注入)
   └── Beyond_Parameters_Context_Injection_2604.03174 (ICL→CausalRAG)
```

### 按阅读目的

```
入门路线 (建立整体认知)
├── 1. Comprehensive_Survey_Long_Context_LM_2503.17407
│      └── 架构-训练-评估管线全覆盖
├── 2. Thus_Spake_Long_Context_LLM_2502.17129
│      └── 四维全景+10个开放问题
└── 3. Is_It_Really_Long_Context_EMNLP2024
       └── 建立正确的长上下文评估认知

进阶路线 (深入技术细节)
├── 4. Advancing_Transformer_Architecture_Long_Context_2311.12351
│      └── Transformer架构改进深度分析
├── 5. Transformer_Context_Extension_Survey_2503.13299
│      └── 四类上下文扩展方法
└── 6. Long_Text_Modeling_Transformers_2302.14502
       └── 长文本建模经典方法

工程路线 (部署与优化)
├── 7. Long_Context_LLM_Inference_Optimization_Survey
│      └── 推理优化三级体系
├── 8. Long_Context_Inference_Optimization_CN
│      └── 中文推理优化综述
└── 9. CAP_Principle_LLM_Serving_2405.11299
       └── 服务部署CAP框架

前沿路线 (新方向探索)
└── 10. Beyond_Parameters_Context_Injection_2604.03174
       └── 上下文增强技术谱系
```

---

## 核心内容对比

### 综合综述对比

| 维度 | 2503.17407 | 2502.17129 |
|------|-----------|-----------|
| 侧重点 | 管线全覆盖 | 生命周期四维 |
| 架构覆盖 | 数据+架构+工作流 | 位置编码+注意力+记忆 |
| 基础设施 | 训练+推理 | 训练+推理系统 |
| 评估 | 理解+生成+行为分析 | 多维度评估 |
| 特色 | GitHub知识库 | 10个开放问题+哲学视角 |
| 建议 | 入门首选 | 深入理解 |

### 推理优化综述对比

| 维度 | Inference_Optimization_Survey | Inference_Optimization_CN |
|------|------------------------------|--------------------------|
| 语言 | 英文 | 中文 |
| 机构 | 华中科技大学+平安科技 | 华中科技大学+平安科技 |
| 分类 | 模型+计算+系统 | 模型+计算+系统 |
| 特色 | DOAJ索引 | 中文期刊、面向中文社区 |
| 建议 | 英文文献参考 | 中文社区首选 |

---

## 重要性标注说明

- **⭐⭐⭐ 必读基础**: 领域核心综述，必读论文，建立技术体系的关键
- **⭐⭐ 值得关注**: 特定方向有价值的综述，建议按需阅读
- **⭐ 参考补充**: 可作为特定主题的补充参考


## 关键概念速查

| 概念 | 相关论文 | 说明 |
|------|----------|------|
| **RoPE缩放** | 2503.17407, 2502.17129, 2311.12351 | 旋转位置编码的上下文扩展方法 |
| **KV缓存优化** | 2503.17407, Inference_Optimization, CAP | 长上下文推理的核心瓶颈 |
| **稀疏注意力** | 2311.12351, 2503.13299, Inference_Optimization | 降低注意力复杂度的关键方法 |
| **Lost in the Middle** | 2503.17407, EMNLP2024 | 模型在上下文中间部分检索能力下降 |
| **RAG** | 2503.13299, 2604.03174 | 检索增强生成 |
| **GraphRAG** | 2604.03174 | 基于知识图谱的检索增强 |
| **CausalRAG** | 2604.03174 | 因果检索增强生成 |
| **CAP原则** | 2405.11299 | 上下文长度-准确性-性能三角权衡 |
| **量化** | Inference_Optimization, CAP | 模型压缩的核心方法 |
| **投机解码** | 2503.17407, Inference_Optimization, CAP | 加速自回归解码的方法 |
| **Diffusion×Scope** | EMNLP2024 | 长上下文任务难度的二维分类 |
| **SSM/Mamba** | 2311.12351, 2502.17129 | 线性复杂度的替代架构 |

---

## 相关资源

### GitHub仓库

| 仓库 | 链接 | 对应论文 |
|------|------|----------|
| LCLM-Horizon | [GitHub](https://github.com/LCLM-Horizon/A-Comprehensive-Survey-For-Long-Context-Language-Modeling) | 2503.17407 |
| Thus-Spake-Long-Context-LLM | [GitHub](https://github.com/OpenMOSS/Thus-Spake-Long-Context-LLM) | 2502.17129 |
| long-llms-learning | [GitHub](https://github.com/Strivin0311/long-llms-learning) | 2311.12351 |

### 相关主题

- [长上下文模型技术索引](../models/README.md) - 各模型长上下文技术论文
- [LLM架构总览](../../summary.md) - LLM架构领域技术总结

---

## 更新计划

- [ ] 补充更多2025-2026年最新综述
- [ ] 添加各综述的详细对比分析
- [ ] 整理各综述的关键图表
- [ ] 补充英文翻译版本

---

*最后更新: 2026-04-26*
