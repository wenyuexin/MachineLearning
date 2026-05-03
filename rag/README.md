# RAG (Retrieval-Augmented Generation)

检索增强生成：通过外部知识检索提升 LLM 的事实准确性和时效性。

## 目录结构

```
rag/
├── 01-fundamentals/                  # 基础概念
│   ├── what-is-rag/
│   └── rag-pipeline-overview/
│
├── 02-retrieval/        # 索引与检索
│   ├── chunking-strategies/
│   │   ├── fixed-size/
│   │   └── semantic-chunking/
│   ├── embedding-models/
│   │   ├── sparse-embeddings/
│   │   └── dense-embeddings/
│   ├── vector-databases/
│   └── advanced-retrieval/
│       ├── hybrid-search/
│       ├── recursive-retrieval/
│       └── multi-hop-retrieval/
│
├── 03-generation/   # 生成与增强
│   ├── context-integration/
│   │   ├── prompt-templates/
│   │   └── context-compression/
│   ├── generation-strategies/
│   │   ├── post-hoc-citation/
│   │   └── chain-of-note/
│   └── evaluation-of-generation/
│       ├── faithfulness/
│       └── answer-relevance/
│
├── 04-advanced-rag-patterns/         # 高级RAG模式
│   ├── self-reflective-rag/
│   ├── graph-rag/
│   ├── agentic-rag/
│   └── multimodal-rag/
│
├── 05-evaluation/     # 评估与基准
│   ├── end-to-end-metrics/
│   │   ├── ragas/
│   │   └── truelens/
│   └── public-benchmarks/
│
└── 06-production/      # 生产与生态
    ├── frameworks/
    ├── caching-and-scaling/
    └── security-and-privacy/
```

## 与其他目录的边界

| 内容 | 归属 | 说明 |
|------|------|------|
| Prompt工程 | [../llm/04-serving/prompt-engineering/](../llm/04-serving/prompt-engineering/) | 通用技术 |
| LLM推理优化 | [../llm/04-serving/](../llm/04-serving/) | 通用推理优化 |
| 知识图谱构建 | [../knowledge-graph/](../knowledge-graph/) | 知识本身的理论与构建 |
| GraphRAG的图谱部分 | [../knowledge-graph/05-applications/](../knowledge-graph/05-applications/) | 知识图谱与LLM结合 |

## 相关资源

- [LLM推理](../llm/04-serving/) - 生成模块优化
- [知识图谱](../knowledge-graph/) - 结构化知识源
- [LLM评估](../llm/05-evaluation/) - 通用评估方法

---

*最后更新: 2026-05-02*
