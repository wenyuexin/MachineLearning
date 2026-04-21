# EgoZero：从智能眼镜学习机器人操作

**论文信息**
- 论文标题：EgoZero: Robot Learning from Smart Glasses
- 中文标题：EgoZero：从智能眼镜学习机器人操作
- 作者：V. Liu, A. Adeniji, H. Zhan, S. Haldar, R. Bhirangi, P. Abbeel, L. Pinto
- 机构：UC Berkeley
- arXiv: [2505.20290](https://arxiv.org/abs/2505.20290)

---

## 一、论文整体思路

### 1.1 研究背景

智能眼镜（如Project Aria）可以轻松收集第一人称视频。如何利用这些数据训练机器人？

### 1.2 核心创新

EgoZero提出完全从智能眼镜采集的视频学习机器人策略，无需机器人数据。

---

## 二、方法架构

### 2.1 核心流程

```
智能眼镜采集
        │
        ▼
    第一人称视频
        │
        ▼
    手部轨迹提取
        │
        ▼
    机器人策略学习
        │
        ▼
    零样本机器人部署
```

---

## 三、关键贡献

| 贡献 | 描述 |
|------|------|
| 零机器人数据 | 完全从智能眼镜学习 |
| 普通人可用 | 降低数据采集门槛 |
| 零样本部署 | 无需机器人训练 |

---

## 参考文献

1. Liu V, Adeniji A, Zhan H, et al. EgoZero: Robot Learning from Smart Glasses[J]. arXiv preprint arXiv:2505.20290, 2025.

---

*文档创建日期：2026-04-21*
*论文来源：arXiv 2025*