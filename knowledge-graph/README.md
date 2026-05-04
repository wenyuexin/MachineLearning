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
└── 06-quality/                       # 质量与演化
    ├── knowledge-completion/
    ├── error-detection/
    └── kg-versioning/
```

## 开源仓库与工具存放指南

知识图谱相关的开源仓库/工具笔记，按功能主题优先放入对应技术目录：

| 仓库功能 | 放入目录 | 示例 |
|---------|---------|------|
| 知识表示框架/嵌入库 | `01-representation/` | RDFlib, PyKEEN |
| 抽取/融合/构建工具 | `02-construction/` | OpenIE, DeepKE, graphify |
| 图数据库/查询引擎 | `03-storage-and-query/` | Neo4j, NebulaGraph |
| 推理引擎 | `04-reasoning/` | RLvLR, KGEM |
| 应用框架 | `05-applications/` | GraphRAG, KG4LLM |
| 质量评估/补全工具 | `06-quality/` | 知识图谱质量评估套件 |

## 学习路径

**入门阶段**
- `01-representation/` — 了解知识图谱的基本概念
- `02-construction/` — 掌握实体识别和关系抽取

**构建阶段**
- `03-storage-and-query/` — 图数据库使用
- `04-reasoning/` — 知识推理方法

**应用阶段**
- `05-applications/` — LLM与知识图谱结合（GraphRAG等）
- `06-quality/` — 知识图谱质量与演化

## 与仓库其他目录的关系

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| GraphRAG检索架构 | [../rag/04-advanced-rag-patterns/graph-rag/](../rag/04-advanced-rag-patterns/graph-rag/) | RAG视角的图增强检索 |
| LLM推理 | [../llm/04-serving/](../llm/04-serving/) | LLM作为抽取/推理工具 |
| 可解释性 | [../llm/07-explainability/](../llm/07-explainability/) | KG驱动的模型解释 |

---

*最后更新: 2026-05-03*
