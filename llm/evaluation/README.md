# LLM 评估体系

**主题**: 大语言模型评估方法与基准

**创建日期**: 2026-04-28

---

## 目录结构

```
llm/evaluation/
├── calibration/     # 校准与不确定性量化
│   ├── README.md
│   └── Uncertainty_Measurement_LLM_Survey_2502.04567.md
│
├── benchmarks/      # 综合评估基准
│   └── .gitkeep     # MMLU、GSM8K、HumanEval、LongBench等
│
├── safety/          # 安全评估
│   └── .gitkeep     # 对齐评估、有害内容检测、越狱测试
│
├── reasoning/       # 推理能力评估
│   └── .gitkeep     # 数学推理、代码能力、逻辑推理
│
└── generation/      # 生成质量评估
    └── .gitkeep     # 流畅度、连贯性、事实一致性、幻觉检测
```

---

## 各目录说明

### calibration/ - 校准与不确定性量化

评估模型置信度的可靠性，回答"模型是否知道自己对不对"。

**核心概念**：
- ECE（期望校准误差）
- Flex-ECE（生成任务专用）
- Semantic Entropy（语义熵）
- 幻觉检测

**详细内容**：见 [calibration/](./calibration/)

---

### benchmarks/ - 综合评估基准

评估模型的综合能力，涵盖多任务、多领域的测试集。

| 类别 | 代表基准 | 评估内容 |
|------|----------|----------|
| **通用能力** | MMLU, C-Eval, AGI-Eval | 多学科知识 |
| **推理能力** | GSM8K, MATH, BBH | 数学、逻辑推理 |
| **代码能力** | HumanEval, MBPP | 代码生成 |
| **长上下文** | LongBench, NIAH | 长文本理解 |
| **多轮对话** | MT-Bench, AlpacaEval | 对话质量 |

---

### safety/ - 安全评估

评估模型的安全性和对齐程度。

| 类别 | 代表基准 | 评估内容 |
|------|----------|----------|
| **对齐评估** | TruthfulQA, HellaSwag | 真实性、一致性 |
| **有害内容** | RealToxicityPrompts | 毒性、偏见 |
| **对抗测试** | 越狱测试、Prompt注入 | 鲁棒性 |

---

### reasoning/ - 推理能力评估

专项评估模型的推理能力。

| 类别 | 代表基准 | 评估内容 |
|------|----------|----------|
| **数学推理** | GSM8K, MATH, AIME | 数学问题求解 |
| **逻辑推理** | BBH, LogiQA | 逻辑演绎 |
| **常识推理** | CommonsenseQA, PIQA | 常识判断 |

---

### generation/ - 生成质量评估

评估模型生成文本的质量。

| 类别 | 评估维度 | 方法 |
|------|----------|------|
| **流畅度** | 语法正确、表达自然 | Perplexity、人工评估 |
| **连贯性** | 上下文衔接 | 专门指标 |
| **事实一致性** | 与输入/知识一致 | FActScore、FactCC |
| **幻觉检测** | 编造虚假信息 | SelfCheckGPT、FAVA |

---

## 评估维度关系

```
LLM评估全景
    │
    ├── 能力评估
    │   ├── benchmarks/     综合能力
    │   └── reasoning/      推理专项
    │
    ├── 可靠性评估
    │   ├── calibration/    置信度可靠性
    │   └── generation/     输出质量
    │
    └── 安全评估
        └── safety/         安全对齐
```

---

## 相关资源

### 综合评估框架

- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) - EleutherAI
- [OpenCompass](https://github.com/open-compass/opencompass) - 上海AI实验室
- [HELM](https://crfm.stanford.edu/helm/lite/) - Stanford

### 评估基准集合

- [Awesome-LLM-Evaluation](https://github.com/MLGroupJLU/LLM-evaluation-survey)
- [Papers With Code - LLM Benchmarks](https://paperswithcode.com/area/natural-language-processing)

---

*最后更新: 2026-04-28*