# 知识图谱 (Knowledge Graph)

## 目录结构

```
knowledge-graph/
├── foundations/               # 基础理论
│
├── knowledge-representation/  # 知识表示
│   # RDF、OWL、属性图等表示方法
│
├── knowledge-extraction/      # 知识抽取
│   # NER、关系抽取、事件抽取
│
├── knowledge-fusion/          # 知识融合
│   # 实体对齐、实体消解
│
├── knowledge-graph-construction/  # 知识图谱构建
│
├── knowledge-storage/         # 知识存储
│   # Neo4j、SPARQL、图数据库
│
├── knowledge-reasoning/       # 知识推理
│
├── llm-kg-integration/        # LLM与知识图谱结合
│   # GraphRAG、知识增强LLM
│
├── datasets/                  # 数据集
│   # Freebase、Wikidata等
│
├── tools/                     # 工具与框架
│
└── papers/                    # 论文笔记
```

## 知识图谱生命周期

```
知识表示 → 知识抽取 → 知识融合 → 图谱构建 → 知识存储 → 知识推理
                                                          ↓
                                                    LLM与KG结合
```

## 学习路径

**入门阶段**
- `foundations/` — 了解知识图谱的基本概念
- `knowledge-representation/` — 掌握RDF、OWL、属性图等表示方法

**构建阶段**
- `knowledge-extraction/` — 学习实体识别和关系抽取
- `knowledge-fusion/` — 掌握实体对齐和知识融合
- `knowledge-graph-construction/` — 完整图谱构建流程
- `knowledge-storage/` — 图数据库使用

**应用阶段**
- `knowledge-reasoning/` — 知识推理方法
- `llm-kg-integration/` — LLM与知识图谱结合（GraphRAG等）
- `papers/` — 领域核心论文

## 与仓库其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| GraphRAG检索架构 | [../rag/architectures/graph-rag/](../rag/architectures/graph-rag/) | RAG视角的图增强检索 |
| LLM推理 | [../llm/inference/](../llm/inference/) | LLM作为抽取/推理工具 |
| 可解释性 | [../llm/explainability/](../llm/explainability/) | KG驱动的模型解释 |

---

*最后更新: 2026-05-02*
