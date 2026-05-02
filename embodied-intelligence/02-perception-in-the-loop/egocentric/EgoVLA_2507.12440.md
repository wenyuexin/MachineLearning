# EgoVLA：从第一人称人类视频学习VLA模型

**论文信息**
- 论文标题：EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos
- 中文标题：EgoVLA：从第一人称人类视频学习视觉-语言-动作模型
- 作者：Ruihan Yang, Qinxi Yu, Xiaolong Wang
- 机构：UC San Diego
- arXiv: [2507.12440](https://arxiv.org/abs/2507.12440)

---

## 一、论文整体思路

### 1.1 研究背景

VLA模型训练需要大量机器人数据，但机器人数据稀缺。第一人称人类视频规模大、包含丰富操作知识，如何用于VLA训练？

### 1.2 核心创新

EgoVLA探索直接从第一人称人类视频训练VLA模型，并验证其在人形机器人上的效果。

---

## 二、方法架构

### 2.1 核心方法

```
第一人称人类视频 (Ego4D等)
        │
        ▼
    动作标签生成
    • 腕部运动估计
    • 重定向到机器人
        │
        ▼
    VLA模型训练
        │
        ▼
    人形机器人微调与评估
```

### 2.2 数据处理

| 步骤 | 描述 |
|------|------|
| 视频采集 | Ego4D等第一人称数据集 |
| 相机运动补偿 | 处理头动带来的视角变化 |
| 动作估计 | 从视频估计腕部动作 |
| 机器人重定向 | 映射到人形机器人动作空间 |

---

## 三、实验与结果

### 3.1 评估基准

- Ego Humanoid Manipulation Benchmark
- 多样化操作任务
- 人形机器人平台

### 3.2 主要发现

1. 第一人称人类视频预训练有效
2. 显著优于无预训练基线
3. 人形机器人适配成功

---

## 参考文献

1. Yang R, Yu Q, Wang X. EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos[J]. arXiv preprint arXiv:2507.12440, 2025.

---

*文档创建日期：2026-04-21*
*论文来源：arXiv 2025*