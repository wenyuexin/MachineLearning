# AI 智能体 (Agentic AI)

## 目录结构

```
agentic/
├── 01-core-concepts/                  # 核心概念
│   ├── definition-and-taxonomy/
│   ├── reactive-vs-deliberative/
│   └── cognitive-architectures-intro/
│
├── 02-cognitive-capabilities/         # 认知能力
│   ├── planning/
│   │   ├── task-decomposition/
│   │   ├── plan-and-execute/
│   │   └── tree-of-thoughts/
│   ├── memory/
│   │   ├── short-term-memory/
│   │   ├── long-term-memory/
│   │   └── retrieval-methods/
│   ├── tool-use/
│   │   ├── api-calling/
│   │   ├── code-interpreter/
│   │   └── web-browsing/
│   └── self-reflection/
│       ├── critique-models/
│       └── iterative-refinement/
│
├── 03-agent-architectures/            # 智能体架构
│   ├── single-agent-patterns/
│   │   ├── react/
│   │   ├── ra-aid/
│   │   └── autogpt-pattern/
│   ├── multi-agent-systems/
│   │   ├── collaborative/
│   │   ├── competitive/
│   │   └── organizational-structures/
│   └── human-agent-interaction/
│
├── 04-environment-and-simulation/     # 环境与仿真
│   ├── simulated-environments/
│   ├── sandboxing-and-safety/
│   └── benchmarking-frameworks/
│
├── 05-frameworks-and-tools/           # 框架与工具
│   ├── langchain-agents/
│   ├── autogen/
│   ├── crewai/
│   └── custom-agent-dev/
│
└── 06-evaluation-and-reliability/     # 评估与可靠性
    ├── task-completion-metrics/
    ├── safety-and-robustness/
    └── human-evaluation/
```

## 学习路径

按编号顺序学习：

```
01-core-concepts → 02-cognitive-capabilities
                           ↓
03-agent-architectures ← 04-environment-and-simulation
        ↓
   05-frameworks-and-tools → 06-evaluation-and-reliability
```

## 相关资源

- [LLM](../llm/) — Agent的核心引擎
- [RAG](../rag/) — Agent的知识检索能力
- [知识图谱](../knowledge-graph/) — Agent的结构化知识
- [具身智能](../embodied-intelligence/) — Agent的物理落地

---

*最后更新: 2026-05-02*
