# 长上下文模型技术索引

各模型长上下文技术论文索引，按技术路线分类。

---

## 模型论文索引

| 模型/项目 | 技术路线 | 技术论文标题 | arXiv ID / URL | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| **Google Gemini 1.5 Pro** | 🏛️ **原生架构** | *Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context* | [`arXiv:2403.05530`](http://arxiv.org/abs/2403.05530) | 业界首个宣布原生支持1M上下文的模型的核心技术报告。 |
| **MiniMax M1** | 🏛️ **原生架构** | *MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention* | [`arXiv:2506.13585`](http://arxiv.org/abs/2506.13585) | 全球首个开源1M上下文推理模型，介绍了其核心的Lightning Attention机制。 |
| **DeepSeek-V4** | 🛠️ **后期扩展** | *DeepSeek-V4 Technical Report* | [`arXiv:2604.02433`](http://arxiv.org/abs/2604.02433) | 详细阐述了其突破性的CSA+HCA混合注意力架构，显著降低了长文本处理的计算量。 |
| **OpenAI GPT-4.1 系列** | 🛠️ **后期扩展** | 暂未发布对应论文 | 仅为官方博客/API文档 | OpenAI官方发布日志，简要说明了其1M上下文窗口和在编码、指令遵循等方面的提升。 |
| **阿里云 Qwen2.5-1M** | 🛠️ **后期扩展** | *Qwen2.5-1M Technical Report* | [`arXiv:2501.15383`](http://arxiv.org/abs/2501.15383) | 首个将百万长文本能力开源并实用的模型，详细介绍了其训练和推理框架的设计。 |
| **UC Berkeley LWM** | 🛠️ **后期扩展** | *World Model on Million-Length Video And Language With RingAttention* | [`arXiv:2402.08268`](http://arxiv.org/abs/2402.08268) | 学术界首个开源1M上下文模型，提出了RingAttention技术用于训练极长序列。 |
| **Gradient (Llama 3 扩展)** | 🛠️ **后期扩展** | 无对应arXiv论文 | 仅为技术博客/演示 | 通过调整RoPE参数和微调，将Llama 3的上下文从8K低成本扩展到1M+。 |

---

## 关键研究点速查

| 关键研究点 | 推荐模型/论文 (arXiv ID) |
| :--- | :--- |
| **原生长文本架构**<br>**(MoE + Lightning Attention)** | Google Gemini 1.5 Pro ([`2403.05530`](http://arxiv.org/abs/2403.05530))<br>MiniMax M1 ([`2506.13585`](http://arxiv.org/abs/2506.13585)) |
| **后期扩展：压缩/稀疏注意力**<br>**(Token 压缩、环状并行)** | DeepSeek-V4 ([`2604.02433`](http://arxiv.org/abs/2604.02433))<br>UC Berkeley LWM ([`2402.08268`](http://arxiv.org/abs/2402.08268)) |
| **后期扩展：RoPE 参数调优** | Gradient (Llama 3 扩展) (技术博客) |
| **开源长文本模型工程实践** | MiniMax M1 ([`2506.13585`](http://arxiv.org/abs/2506.13585))<br>阿里云 Qwen2.5-1M ([`2501.15383`](http://arxiv.org/abs/2501.15383))<br>UC Berkeley LWM ([`2402.08268`](http://arxiv.org/abs/2402.08268)) |
