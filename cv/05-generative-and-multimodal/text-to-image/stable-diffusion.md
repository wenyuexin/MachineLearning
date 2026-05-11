# Stable Diffusion

Stable Diffusion（SD）是一种在**潜在空间（Latent Space）**进行扩散的文本到图像生成模型。

---

## 核心思想

传统扩散模型直接在像素空间操作，计算成本极高。Stable Diffusion 将图像压缩到低维潜在空间后再进行扩散和去噪，大幅降低了计算量。

```
文本编码 → 潜在空间扩散/去噪 → VAE 解码 → 输出图像
```

---

## 关键特性

- **计算效率**：在潜在空间而非像素空间操作，显著降低硬件门槛
- **开源生态**：庞大的社区贡献了丰富的插件、LoRA 微调模型和预训练权重
- **可控生成**：支持 ControlNet、IP-Adapter 等条件控制方法

---

## LoRA 微调

在特定领域中，可以用 LoRA 对 SD 进行微调，注入领域知识的先验，使生成的插图更准确。

```python
# 使用 LoRA 微调 SD
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe.unet.load_attn_procs("path/to/domain-lora")
```

---

## 应用场景

在内容创作中，SD 用于根据脚本的文字描述生成对应的插图。

