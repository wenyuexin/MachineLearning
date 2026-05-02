# RAG (Retrieval-Augmented Generation)

检索增强生成：通过外部知识检索提升 LLM 的事实准确性和时效性。

## 核心流程

```
查询 → 检索模块 → 上下文构建 → LLM生成
         │
    ├─ Embedding模型
    ├─ 向量存储
    ├─ 混合检索
    └─ 重排序
```

## 目录结构

```
rag/
├── architectures/           # RAG架构范式
│   ├── naive-rag/           # 基础RAG：查询→检索→生成
│   ├── advanced-rag/        # 查询重写、子问题分解、迭代检索
│   ├── modular-rag/         # 模块化RAG：可组合的检索与生成组件
│   └── graph-rag/           # 图增强RAG（知识图谱+向量检索）
├── retrieval/               # 检索技术
│   ├── embedding-models/    # 文本Embedding模型（BGE、E5、GTE等）
│   ├── vector-store/        # 向量数据库（Milvus、Pinecone、Chroma）
│   ├── hybrid-retrieval/    # 稠密+稀疏混合检索
│   └── reranking/           # 重排序模型（Cross-Encoder等）
├── context/                 # 上下文管理
│   ├── context-compression/ # 上下文压缩技术
│   └── context-selection/   # 相关片段选择策略
├── evaluation/              # RAG评估
│   ├── ragas/               # RAGAS评估框架
│   ├── benchmark-datasets/  # 评测数据集
│   └── metrics/             # 检索准确率、忠实度、答案相关性指标
└── papers/                  # RAG相关论文笔记
```

## 与其他目录的边界

| 内容 | 归属 | 说明 |
|------|------|------|
| Prompt工程 | [llm/inference/prompt-engineering/](../llm/inference/prompt-engineering/) | 通用技术 |
| LLM推理优化 | [llm/inference/](../llm/inference/) | 通用推理优化 |
| 知识图谱构建 | [knowledge-graph/](../knowledge-graph/) | 知识本身的理论与构建 |
| GraphRAG的图谱部分 | [knowledge-graph/llm-kg-integration/](../knowledge-graph/llm-kg-integration/) | 知识图谱与LLM结合 |

## 相关资源

- [LLM推理](../llm/inference/) - 生成模块优化
- [知识图谱](../knowledge-graph/) - 结构化知识源
- [LLM评估](../llm/evaluation/) - 通用评估方法

---

*最后更新: 2026-05-02*
