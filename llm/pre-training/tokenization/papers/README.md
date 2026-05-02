# 分词研究论文索引

**主题**: Tokenization（分词）相关核心论文与研究

**创建日期**: 2026-04-30

---

## 论文列表

### 分词公平性与基础设施偏见

| 论文 | 文档 | arXiv/来源 | 核心内容 | 重要性 |
| --- | --- | --- | --- | --- |
| Tokenization Disparities as Infrastructure Bias | [`Tokenization_Disparities_2510.12389`](./Tokenization_Disparities_2510.12389.md) | FLLM 2025 (2510.12389) | 200+语言分词差异的系统性研究，提出"基础设施偏见"框架 | ⭐⭐⭐ 必读 |

### 分词算法与优化

| 论文 | arXiv | 核心内容 | 状态 |
|------|-------|---------|------|
| Neural Machine Translation of Rare Words with Subword Units | 1508.07909 | BPE算法原始论文 | 待添加 |
| SentencePiece: A simple and language independent subword tokenizer | 1808.06226 | SentencePiece无预分词方案 | 待添加 |
| Byte-level BPE (BBPE) | - | 字节级BPE，更好地处理Unicode | 待添加 |

### 多语言分词

| 论文 | arXiv | 核心内容 | 状态 |
|------|-------|---------|------|
| Optimal Subword Tokenization for Cross-lingual Transfer | - | 跨语言迁移的最优分词 | 待添加 |
| Tokenization and the Impact on Deep Learning for Biblical Hebrew | - | 低资源语言分词分析 | 待添加 |

### 无分词/替代架构

| 论文 | arXiv | 核心内容 | 状态 |
|------|-------|---------|------|
| ByT5: Towards a token-free future | 2105.13626 | 字节级T5，无需显式分词 | 待添加 |
| CANINE: Pre-training an Efficient Tokenization-Free Encoder | 2103.06874 | 无分词编码器 | 待添加 |
| MegaByte: Predicting Million-byte Sequences | 2305.07185 | 百万字节序列预测 | 待添加 |

---

## 主题分类

### 按研究方向

```
分词研究
├── 分词算法
│   ├── BPE (Byte-Pair Encoding)
│   ├── WordPiece
│   ├── Unigram Language Model
│   └── SentencePiece
│
├── 分词公平性
│   ├── 跨语言分词差异
│   ├── 低资源语言分词
│   └── 基础设施偏见
│
├── 分词优化
│   ├── 语料选择对分词的影响
│   ├── 词汇表大小优化
│   └── 领域自适应分词
│
└── 替代方案
    ├── 字节级模型 (ByT5, CANINE)
    ├── 字符级模型
    └── 无分词架构
```

### 按阅读路线

```
入门路线
├── 1. Tokenization Disparities (2510.12389)
│      └── 理解分词差异的现实影响
├── 2. BPE原始论文 (1508.07909)
│      └── 了解经典分词算法
└── 3. SentencePiece (1808.06226)
       └── 无预分词的分词方案

进阶路线
├── 4. 多语言分词优化研究
├── 5. ByT5/CANINE 无分词架构
└── 6. 分词与下游任务性能关系

实践路线
├── 7. Hugging Face Tokenizers实践
├── 8. 自定义分词器训练
└── 9. 特定领域分词优化
```

---

## 核心概念

### 分词效率指标

| 指标 | 定义 | 用途 |
|------|------|------|
| **Token Inflation Rate (TIR)** | 语言平均token数 / 英语平均token数 | 衡量相对于英语的分词效率 |
| **Fragmentation Index** | 碎片化程度 | 衡量词语被拆分程度 |
| **Fertility** | 词语数 / token数 | 传统分词效率指标 |
| **Unknown Token Rate** | `<unk>`比例 | 衡量OOV问题严重程度 |

### 分词器类型对比

| 分词器 | 预分词 | 特点 | 代表模型 |
|--------|--------|------|---------|
| **BPE** | 需要 | 合并频率最高的字符对 | GPT系列、LLaMA |
| **WordPiece** | 需要 | 基于语言模型概率 | BERT、DistilBERT |
| **Unigram** | 不需要 | 从大规模词汇表中剪枝 | T5、XLNet |
| **SentencePiece** | 不需要 | 将空格视为特殊字符 | ALBERT、Marian |

---

## 工具与资源

### 分词工具

| 工具 | 说明 | 链接 |
|------|------|------|
| **tiktoken** | OpenAI GPT系列分词器 | [GitHub](https://github.com/openai/tiktoken) |
| **Hugging Face Tokenizers** | 快速分词库 | [Docs](https://huggingface.co/docs/tokenizers) |
| **SentencePiece** | Google无预分词方案 | [GitHub](https://github.com/google/sentencepiece) |
| **fastBPE** | 快速BPE实现 | [GitHub](https://github.com/glample/fastBPE) |

### 多语言语料

| 语料 | 语言数 | 特点 |
|------|--------|------|
| **FLORES-200** | 200+ | 平行语料，评估基准 |
| **CC100** | 100+ | Common Crawl多语言提取 |
| **OSCAR** | 150+ | 高质量多语言语料 |
| **mC4** | 101 | 多语言C4语料 |

### 在线工具

- **Tokenizer Playground**: https://platform.openai.com/tokenizer
- **Hugging Face Tokenizer Viewer**: 可视化不同分词器效果

---

## 相关资源

### arXiv搜索

- Tokenization: https://arxiv.org/search/?query=tokenization
- Subword: https://arxiv.org/search/?query=subword+tokenization
- Multilingual Tokenization: https://arxiv.org/search/?query=multilingual+tokenization

### 相关主题

- [LLM校准与不确定性](../../evaluation/calibration/papers/) - ECE、语义熵
- [多语言模型](../../models/) - mBERT、XLM-R、BLOOM
- [LLM预训练](../) - 预训练策略与优化

---

## 更新日志

- 2026-04-30: 创建分词论文目录
  - 添加 Tokenization_Disparities_Infrastructure_Bias 详细文档
  - 创建 README 索引

---

*最后更新: 2026-04-30*
