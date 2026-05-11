# LLM (大语言模型)

## 分类依据

LLM 目录按"基础 → 模型 → 训练 → 推理 → 评估 → 应用 → 解释 → 多模态"的能力生命周期组织：

- **01（基础）**：Transformer 架构原理、分词、Scaling Law
- **02（模型全景）**：各开源模型系列及其架构变体
- **03（训练）**：预训练 → 微调 → 对齐的完整训练管线
- **04（推理与部署）**：推理优化、服务框架、提示工程
- **05（评估）**：基准测试、评估方法与框架
- **06（应用）**：Agent、Wiki、安全对齐、社会影响
- **07（可解释性）**：机制解释、归因、探测
- **08（多模态）**：LLM 扩展至视觉、语音、视频

## 边界说明

| 内容 | 适合放 LLM | 不适合放 LLM |
|------|-----------|-------------|
| Transformer 架构原理 | 01-foundations | 通用 Transformer 原理放 `deep-learning/03-architectures/transformers/` |
| 开源模型技术报告 | 02-model-zoo | 模型评估结果放 `05-evaluation/benchmarks/` |
| 预训练、微调、对齐技术 | 03-training | 分布式训练基础设施放 `training-infra/` |
| 推理优化、服务框架 | 04-serving | 训练框架对比放 `training-infra/03-frameworks-and-tools/` |
| LLM 评估基准与方法 | 05-evaluation | RAG 评估放 `rag/06-evaluation/` |
| Agent 应用 | 06-applications/agents（LLM 视角） | Agent 体系知识放 `agentic/` |
| 安全与对齐 | 06-applications/safety-and-alignment | — |
| 视觉为中心的多模态模型（BLIP） | — | 放 `cv/05-generative-and-multimodal/` |
| LLM 为中心的多模态模型（LLaVA） | 08-multimodal/vlm | — |
| 音频/语音（WhisperX） | 08-multimodal/audio | — |

```
llm/
├── 01-foundations/                  # 基础
│   ├── transformer-architecture/    # Transformer架构
│   ├── tokenization/                # 分词
│   └── scaling-laws/                # 缩放定律
│
├── 02-model-zoo/                    # 模型全景
│   ├── open-source-models/          # 开源模型
│   │   ├── gpt-series/
│   │   ├── llama-series/
│   │   ├── qwen-series/
│   │   ├── deepseek-series/
│   │   ├── mistral-series/
│   │   └── gemma-series/
│   ├── architectural-variants/      # 架构变体
│   │   ├── encoder-only/
│   │   ├── decoder-only/
│   │   ├── encoder-decoder/
│   │   └── mixture-of-experts/
│   └── emergent-abilities/          # 涌现能力
│
├── 03-training/                     # 训练
│   ├── pre-training/                # 预训练
│   ├── fine-tuning/                 # 微调
│   └── alignment/                   # 对齐
│       ├── rlhf/
│       └── dpo/
│
├── 04-serving/     # 推理与部署
│   ├── optimization-techniques/     # 优化技术
│   ├── serving-frameworks/          # Serving框架
│   └── prompt-engineering/          # 提示工程
│
├── 05-evaluation/                   # 评估
│   ├── benchmarks/                  # 基准测试
│   ├── evaluation-methods/          # 评估方法
│   └── evaluation-frameworks/       # 评估框架
│
├── 06-applications/                 # 应用与伦理
│   ├── agents/                      # LLM 智能体应用
│   ├── llm-wiki/                    # LLM 知识库/wiki
│   ├── safety-and-alignment/        # 安全与对齐
│   └── social-impact/               # 社会影响
│
├── 07-explainability/               # 可解释性
│   ├── mechanistic/                 # 机制可解释性
│   ├── attribution/                 # 归因方法
│   ├── probing/                     # 探测技术
│   └── counterfactual/              # 反事实解释
│
└── 08-multimodal/                   # 多模态
    ├── vlm/                         # 视觉语言模型
    ├── audio/                       # 音频语言模型
    ├── video/                       # 视频语言模型
    └── any2any/                     # 全模态模型
```

## 开源仓库与工具存放指南

LLM 相关的开源仓库、框架笔记和项目实践，按功能主题放入对应目录：

| 内容类型 | 放入目录 | 示例 |
|---------|---------|------|
| 开源模型系列（GPT, Llama, Qwen 等） | `02-model-zoo/open-source-models/` | 各系列模型技术报告与复刻 |
| 预训练数据工程 | `03-training/pre-training/data-curation/` | 数据构建与质量控制工具 |
| 微调与对齐方法 | `03-training/fine-tuning/` / `03-training/alignment/` | LoRA, RLHF, DPO |
| 推理优化框架 | `04-serving/optimization-techniques/` | vLLM, TensorRT-LLM |
| 提示工程工具 | `04-serving/prompt-engineering/` | PromptFlow, LangChain Prompts |
| 评估基准 | `05-evaluation/benchmarks/` | MMLU, C-Eval, HumanEval |
| LLM 知识库/wiki | `06-applications/llm-wiki/` | Karpathy's LLM Wiki, Obsidian Copilot |
| 可解释性工具 | `07-explainability/` | TransformerLens, Ecco |
| 多模态模型 | `08-multimodal/` | LLaVA, Qwen-VL |

## 学习路径

**基础阶段**
- `01-foundations/` — 理解Transformer及变体
- `02-model-zoo/` — 阅读各开源模型技术报告

**进阶阶段**
- `03-training/` — 掌握预训练、微调和对齐方法
- `04-serving/` — 学习推理优化和使用技巧
- `05-evaluation/` — 掌握评估方法

**深入阶段**
- `06-applications/` — 应用与伦理
- `07-explainability/` — 探索模型内部机制
- `08-multimodal/` — 扩展到多模态

## 相关资源

- [RAG (检索增强生成)](../rag/) - LLM与外部知识结合
- [知识图谱](../knowledge-graph/) - 结构化知识源
- [强化学习](../reinforce-learning/) - RLHF基础理论

---

*最后更新: 2026-05-11*
