# 知识图谱 (Knowledge Graph)

## 目录结构

```
knowledge-graph/
├── 01-representation/                # 知识表示
│   ├── symbolic-representation/
│   │   ├── rdf-and-owl/
│   │   └── property-graphs/
│   └── embedding-based-representation/
│       ├── translational-models/
│       ├── bilinear-models/
│       └── neural-models/
│
├── 02-construction/                  # 知识构建
│   ├── named-entity-recognition/
│   ├── relation-extraction/
│   ├── entity-linking/
│   ├── event-extraction/
│   └── knowledge-fusion/
│       ├── entity-alignment/
│       └── conflict-resolution/
│
├── 03-storage-and-query/             # 存储与查询
│   ├── graph-databases/
│   ├── query-languages/
│   └── distributed-storage/
│
├── 04-reasoning/                     # 知识推理
│   ├── rule-based-reasoning/
│   ├── embedding-based-reasoning/
│   ├── neuro-symbolic-reasoning/
│   └── temporal-and-spatial-reasoning/
│
├── 05-applications/                  # 应用
│   ├── question-answering/
│   ├── recommender-systems/
│   ├── dialogue-systems/
│   └── domain-specific-kg/
│
└── 06-quality-and-evolution/         # 质量与演化
    ├── knowledge-completion/
    ├── error-detection/
    └── kg-versioning/
```

## 知识图谱生命周期

```
知识表示 → 知识抽取 → 知识融合 → 图谱构建 → 知识存储 → 知识推理
                                                          ↓
                                                    LLM与KG结合
```

## 学习路径

**入门阶段**
- `01-representation/` — 了解知识图谱的基本概念
- `02-construction/` — 掌握实体识别和关系抽取

**构建阶段**
- `03-storage-and-query/` — 图数据库使用
- `04-reasoning/` — 知识推理方法

**应用阶段**
- `05-applications/` — LLM与知识图谱结合（GraphRAG等）
- `06-quality-and-evolution/` — 知识图谱质量与演化

## 与仓库其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| GraphRAG检索架构 | [../rag/04-advanced-rag-patterns/graph-rag/](../rag/04-advanced-rag-patterns/graph-rag/) | RAG视角的图增强检索 |
| LLM推理 | [../llm/04-inference-and-deployment/](../llm/04-inference-and-deployment/) | LLM作为抽取/推理工具 |
| 可解释性 | [../llm/07-explainability/](../llm/07-explainability/) | KG驱动的模型解释 |

---

*最后更新: 2026-05-02*
