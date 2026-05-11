# 知识图谱 (Knowledge Graph)

## 分类依据

Knowledge Graph 目录按"表示 → 构建 → 存储 → 推理 → 应用 → 质量"的全生命周期组织：

- **01（知识表示）**：如何形式化描述知识（符号表示、嵌入表示）
- **02（知识构建）**：从非结构化数据中抽取实体和关系
- **03（存储与查询）**：图数据库存储与查询语言
- **04（知识推理）**：基于已有知识推导新知识
- **05（应用）**：KG 在下游任务中的应用
- **06（质量）**：知识图谱的维护、补全与评估

## 边界说明

| 内容 | 适合放 KG | 不适合放 KG |
|------|----------|------------|
| 知识表示方法（RDF、OWL、嵌入模型） | 01 | — |
| 实体识别、关系抽取等构建技术 | 02 | 抽取工具在 LLM 场景下的应用放 `llm/` |
| 图数据库选型与查询 | 03 | 向量数据库放 `rag/02-retrieval/vector-databases/` |
| 知识推理方法（规则推理、神经符号推理） | 04 | LLM 自身推理能力放 `llm/` |
| LLM + KG 应用 | 05 (概念层面) | 具体 RAG 项目（GraphRAG）放 `rag/05-implementations/` |
| 端到端 KG 工具（Graphify） | 05/applications/ | — |
| 知识图谱质量与补全 | 06 | — |

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
│   ├── domain-specific-kg/
│   └── graphify/                     # 代码项目知识图谱工具
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
| 抽取/融合/构建工具 | `02-construction/` | OpenIE, DeepKE |
| 代码项目知识图谱工具 | `05-applications/graphify/` | Graphify |
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
| GraphRAG检索架构 | [../rag/05-implementations/graph-rag/](../rag/05-implementations/graph-rag/) | RAG视角的图增强检索，集中rag/不分散 |
| LLM推理 | [../llm/04-serving/](../llm/04-serving/) | LLM作为抽取/推理工具 |
| 可解释性 | [../llm/07-explainability/](../llm/07-explainability/) | KG驱动的模型解释 |

---

*最后更新: 2026-05-11*
