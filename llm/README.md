# LLM (大语言模型)

## 目录结构

```
llm/
├── architectures/           # 基础架构
│   ├── attention/           # 注意力机制
│   ├── long-context/        # 长上下文建模
│   ├── moe/                 # 混合专家模型
│   ├── position-encoding/   # 位置编码
│   └── ssm/                 # 状态空间模型
│
├── models/                  # 开源模型技术报告
│   ├── anthropic/
│   ├── deepseek/
│   ├── gemma/
│   ├── gpt/
│   ├── llama/
│   ├── mistral/
│   └── qwen/
│
├── pre-training/            # 预训练
│   └── tokenization/        # 分词
│
├── post-training/           # 后训练（SFT + 对齐）
│   ├── sft/                 # 监督微调
│   ├── dpo/                 # 直接偏好优化
│   └── rlhf/                # 人类反馈强化学习
│
├── inference/               # 推理与使用
│   ├── prompt-engineering/  # Prompt工程
│   └── decoding/            # 解码策略
│
├── explainability/          # 可解释性
│   ├── mechanistic/         # 机制可解释性
│   ├── attribution/         # 归因方法
│   ├── probing/             # 探测技术
│   └── counterfactual/      # 反事实解释
│
├── evaluation/              # 模型评估
│   ├── benchmarks/          # 综合评估基准
│   ├── calibration/         # 校准与不确定性量化
│   ├── reasoning/           # 推理能力评估
│   ├── safety/              # 安全评估
│   └── generation/          # 生成质量评估
│
└── multimodal/              # 多模态大模型
    ├── vlm/                 # 视觉语言模型
    ├── audio/               # 音频语言模型
    ├── video/               # 视频语言模型
    └── any2any/             # 全模态模型
```

## 学习路径

```
基础阶段
├── architectures/           # 理解Transformer及变体
├── pre-training/            # 了解预训练流程和分词
└── models/                  # 阅读各开源模型技术报告

进阶阶段
├── post-training/           # 掌握SFT和对齐方法
│   ├── sft/                 # 先学监督微调
│   └── alignment/           # 再学DPO、RLHF等偏好对齐
├── inference/               # 学习推理优化和使用技巧
│   ├── prompt-engineering/  # Prompt设计
│   └── decoding/            # 解码策略
└── evaluation/              # 掌握评估方法

深入阶段
├── explainability/          # 探索模型内部机制
├── multimodal/              # 扩展到多模态
└── evaluation/              # 深入特定评估维度
```

## 相关资源

- [RAG (检索增强生成)](../rag/) - LLM与外部知识结合
- [知识图谱](../knowledge-graph/) - 结构化知识源
- [强化学习](../reinforce-learning/) - RLHF基础理论

---

*最后更新: 2026-05-02*
