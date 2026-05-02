# 计算机视觉 (Computer Vision)

## 目录结构

```
cv/
├── traditional/               # 传统方法
│   ├── edge-detection/        # 边缘检测（Canny、Sobel等）
│   ├── feature-extraction/    # 特征提取（SIFT、HOG等）
│   ├── image-processing/      # 图像处理
│   └── segmentation/          # 图像分割（传统方法）
│
├── deep-learning/             # 深度学习方法
│   ├── architectures/         # 网络架构（ResNet、ViT等）
│   ├── classification/        # 图像分类
│   ├── detection/             # 目标检测（YOLO、Faster R-CNN等）
│   ├── segmentation/          # 图像分割（UNet、SAM等）
│   ├── pose-estimation/       # 姿态估计
│   ├── face/                  # 人脸相关
│   ├── ocr/                   # 文字识别
│   ├── tracking/              # 目标跟踪
│   ├── 3d-vision/             # 3D视觉（NeRF、深度估计）
│   ├── video/                 # 视频理解
│   └── generative/            # 图像生成（Stable Diffusion等）
│
└── applications/              # 应用场景
    ├── augmented-reality/     # 增强现实
    ├── autonomous-driving/    # 自动驾驶
    ├── industrial-inspection/ # 工业检测
    ├── medical-imaging/       # 医学影像
    └── surveillance/          # 安防监控
```

## 学习路径

**基础阶段**
- `traditional/` — 了解传统图像处理方法（边缘检测、特征提取）

**核心阶段**
- `deep-learning/architectures/` — 掌握经典网络架构
- `deep-learning/classification/` — 图像分类
- `deep-learning/detection/` — 目标检测
- `deep-learning/segmentation/` — 图像分割

**进阶阶段**
- `deep-learning/` 其他子目录 — 根据兴趣选择专项（3D视觉、视频、生成等）
- `applications/` — 了解实际应用场景

## 相关资源

- [深度学习基础](../deep-learning/) — CNN等基础架构
- [多模态LLM](../llm/multimodal/vlm/) — 视觉语言模型
- [具身智能](../embodied-intelligence/) — 视觉在机器人中的应用
- [世界模型](../world-models/) — 视频生成与预测

---

*最后更新: 2026-05-02*
