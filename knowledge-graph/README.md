# 知识图谱 (Knowledge Graph)

知识图谱的表示、构建、存储、推理、应用与质量管理。

## 分类依据

Knowledge Graph 目录按"基础 → 构建 → 存储 → 推理 → 应用 → 质量"的全生命周期组织：

- **01（基础）**：知识表示方法（符号表示、嵌入表示）与本体建模
- **02（构建）**：从非结构化数据中抽取实体和关系
- **03（存储与查询）**：图数据库存储与查询语言
- **04（推理）**：基于已有知识推导新知识
- **05（应用）**：KG 在下游任务中的应用
- **06（质量）**：知识图谱的维护、补全与评估

## 边界说明

| 内容 | 适合放 KG | 不适合放 KG |
|------|----------|------------|
| 知识表示方法（RDF、OWL、嵌入模型） | 01-foundations | — |
| 本体建模与 Schema 设计 | 01-foundations/ontology-and-schema | — |
| 实体识别、关系抽取等构建技术 | 02-construction | 抽取工具在 LLM 场景下的应用放 `llm/` |
| 图数据库选型与查询 | 03-storage-and-query | 向量数据库放 `rag/02-retrieval/vector-databases/` |
| 知识推理方法（规则推理、神经符号推理） | 04-reasoning | LLM 自身推理能力放 `llm/` |
| LLM + KG 应用 | 05-applications (概念层面) | 具体 RAG 项目（GraphRAG）放 `rag/03-advanced-patterns/graph-rag/` |
| 端到端 KG 工具（Graphify） | 05-applications/graphify/ | — |
| 知识图谱质量与补全 | 06-quality | — |

## 目录结构

```
knowledge-graph/
├── 01-foundations/                  # 基础
│   ├── symbolic-representation/     # 符号表示
│   │   ├── rdf-and-owl/
│   │   └── property-graphs/
│   ├── embedding-based-representation/ # 嵌入表示
│   │   ├── translational-models/
│   │   ├── bilinear-models/
│   │   └── neural-models/
│   └── ontology-and-schema/         # 本体与Schema
│
├── 02-construction/                 # 知识构建
│   ├── named-entity-recognition/    # 实体识别
│   ├── relation-extraction/         # 关系抽取
│   ├── entity-linking/              # 实体链接
│   ├── event-extraction/            # 事件抽取
│   └── knowledge-fusion/            # 知识融合
│       ├── entity-alignment/
│       └── conflict-resolution/
│
├── 03-storage-and-query/            # 存储与查询
│   ├── graph-databases/
│   ├── query-languages/
│   └── distributed-storage/
│
├── 04-reasoning/                    # 知识推理
│   ├── rule-based-reasoning/
│   ├── embedding-based-reasoning/
│   ├── neuro-symbolic-reasoning/
│   └── temporal-and-spatial-reasoning/
│
├── 05-applications/                 # 应用
│   ├── question-answering/
│   ├── recommender-systems/
│   ├── dialogue-systems/
│   ├── domain-specific-kg/
│   ├── graphify/                    # 代码项目知识图谱工具
│   └── synthetic-data/              # 合成数据生成
│
└── 06-quality/                      # 质量与演化
    ├── knowledge-completion/
    ├── error-detection/
    └── kg-versioning/
```

## 开源仓库与工具存放指南

| 仓库功能 | 放入目录 | 示例 |
|---------|---------|------|
| 知识表示框架/嵌入库 | `01-foundations/` | RDFlib, PyKEEN |
| 抽取/融合/构建工具 | `02-construction/` | OpenIE, DeepKE |
| 代码项目知识图谱工具 | `05-applications/graphify/` | Graphify |
| 图数据库/查询引擎 | `03-storage-and-query/` | Neo4j, NebulaGraph |
| 推理引擎 | `04-reasoning/` | RLvLR, KGEM |
| 应用框架 | `05-applications/` | KG4LLM |
| 质量评估/补全工具 | `06-quality/` | 知识图谱质量评估套件 |

## 学习路径

**入门阶段**
- `01-foundations/` — 了解知识图谱的基本概念与表示方法
- `02-construction/` — 掌握实体识别和关系抽取

**构建阶段**
- `03-storage-and-query/` — 图数据库使用
- `04-reasoning/` — 知识推理方法

**应用阶段**
- `05-applications/` — LLM 与知识图谱结合
- `06-quality/` — 知识图谱质量与演化

## 相关资源

| 本目录内容 | 关联目录 | 说明 |
|-----------|---------|------|
| GraphRAG 检索架构 | [../rag/03-advanced-patterns/graph-rag/](../rag/03-advanced-patterns/graph-rag/) | RAG 视角的图增强检索 |
| LLM 推理 | [../llm/04-serving/](../llm/04-serving/) | LLM 作为抽取/推理工具 |
| 可解释性 | [../llm/06-explainability/](../llm/06-explainability/) | KG 驱动的模型解释 |

---

*最后更新: 2026-05-11*
