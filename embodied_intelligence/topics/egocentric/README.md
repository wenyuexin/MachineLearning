# Egocentric2Embodiment 论文集

**研究主题**: 如何将人类第一人称视角视频转换为机器人可用的训练数据

**创建日期**: 2026-04-21

---

## 论文列表

### 2023-2024：基础性工作

| 论文 | 文档 | arXiv | 会议 | 核心贡献 | 重要性 |
|------|------|-------|------|----------|--------|
| MimicPlay | [`MimicPlay_2302.12422.md`](./MimicPlay_2302.12422.md) | 2302.12422 | CoRL 2023 Oral | 分层学习：人类视频学规划 + 机器人数据学执行 | ⭐⭐⭐ 必读基础 |
| HRP | [`HRP_2407.18911.md`](./HRP_2407.18911.md) | 2407.18911 | RSS 2024 | 视频预训练：提取可操作性先验 | ⭐⭐⭐ 必读基础 |

### 2024-2025：联合训练与零样本方法

| 论文 | 文档 | arXiv | 会议 | 核心贡献 | 重要性 |
|------|------|-------|------|----------|--------|
| EgoMimic | [`EgoMimic_2410.24221.md`](./EgoMimic_2410.24221.md) | 2410.24221 | arXiv 2024 | 联合训练：人类+机器人数据同等对待 | ⭐⭐⭐ 必读基础 |
| Phantom | [`Phantom_2503.00779.md`](./Phantom_2503.00779.md) | 2503.00779 | CoRL 2025 | 零机器人数据训练 | ⭐⭐⭐ 必读基础 |
| ZeroMimic | [`ZeroMimic_ICRA2025.md`](./ZeroMimic_ICRA2025.md) | - | ICRA 2025 | 从网络视频蒸馏技能 | ⭐⭐ 值得关注 |

### 2025：视频生成/编辑与VLA

| 论文 | 文档 | arXiv/会议 | 核心贡献 | 重要性 |
|------|------|-----------|----------|--------|
| GR00T N1 | [`GR00T_N1_2503.14734.md`](./GR00T_N1_2503.14734.md) | 2503.14734 | NVIDIA 2025 | 三层数据预训练，开源人形VLA | ⭐⭐⭐ 必读基础 |
| Gen2Act | [`Gen2Act_2409.16283.md`](./Gen2Act_2409.16283.md) | - | CoRL 2025 | 生成人类视频→翻译机器人动作 | ⭐⭐ 值得关注 |
| Masquerade | [`Masquerade_2508.09976.md`](./Masquerade_2508.09976.md) | - | arXiv 2025 | 视频编辑：人手→机器人渲染 | ⭐⭐ 值得关注 |
| EgoVLA | [`EgoVLA_2507.12440.md`](./EgoVLA_2507.12440.md) | - | arXiv 2025 | 从第一人称视频学习VLA | ⭐⭐ 值得关注 |
| EgoZero | [`EgoZero_2505.20290.md`](./EgoZero_2505.20290.md) | - | arXiv 2025 | 从智能眼镜学习 | ⭐⭐ 值得关注 |
| EgoDex | [`EgoDex_2505.11709.md`](./EgoDex_2505.11709.md) | - | arXiv 2025 | 灵巧操作视频数据集 | ⭐ 简单参考 |

### 2026：跨形态与统一动作空间

| 论文 | 文档 | arXiv/会议 | 数据规模 | 核心贡献 | 重要性 |
|------|------|-----------|----------|----------|--------|
| EgoScale | [`EgoScale_2602.16710.md`](./EgoScale_2602.16710.md) | 2602.16710 | 20,854小时 | 对数线性缩放定律，+54%成功率 | ⭐⭐⭐ 必读基础 |
| Being-H0.5 | [`BeingH05_ICLR2026.md`](./BeingH05_ICLR2026.md) | ICLR 2026 | 35,000小时/30形态 | Human-Centric + Unified Action Space | ⭐⭐⭐ 必读基础 |
| CLAP | [`CLAP_2601.04061.md`](./CLAP_2601.04061.md) | 2601.04061 | - | 对比潜在动作预训练，解决视觉纠缠问题 | ⭐⭐ 值得关注 |

### 2026：零样本与轨迹迁移

| 论文 | 文档 | arXiv/会议 | 核心贡献 | 重要性 |
|------|------|-----------|----------|--------|
| LAP | [`LAP_2602.10556.md`](./LAP_2602.10556.md) | 2602.10556 | 语言-动作表示，零样本跨形态 | ⭐⭐⭐ 必读基础 |
| Traj2Action | [`Traj2Action_2510.00491.md`](./Traj2Action_2510.00491.md) | ICLR 2026 | 3D轨迹统一表示，+27%提升 | ⭐⭐ 值得关注 |
| HRT1 | [`HRT1_2510.21026.md`](./HRT1_2510.21026.md) | 2510.21026 | One-Shot人类到机器人轨迹迁移 | ⭐⭐ 值得关注 |
| X-Diffusion | [`X-Diffusion_2511.04671.md`](./X-Diffusion_2511.04671.md) | ICRA 2026 | 跨形态扩散策略，噪声阈值选择性融合 | ⭐⭐ 值得关注 |

### 2026：特征对齐与数据集

| 论文 | 文档 | arXiv/会议 | 数据规模 | 核心贡献 | 重要性 |
|------|------|-----------|----------|----------|--------|
| Lidea | [`Lidea_2604.10677.md`](./Lidea_2604.10677.md) | 2604.10677 | - | 隐式特征蒸馏+显式几何对齐 | ⭐⭐ 值得关注 |
| LatentActionDiff | [`LatentActionDiff_2506.14608.md`](./LatentActionDiff_2506.14608.md) | ICRA 2026 | - | 对比学习统一跨形态动作空间，+13.4% | ⭐⭐ 值得关注 |
| ActiveGlasses | [`ActiveGlasses_2604.08534.md`](./ActiveGlasses_2604.08534.md) | 2604.08534 | - | 智能眼镜+主动视觉+零样本迁移 | ⭐⭐ 值得关注 |
| VITRA | [`VITRA_Microsoft2026.md`](./VITRA_Microsoft2026.md) | ICRA 2026 | 1M episodes/26M frames | 全自动人类活动分析→VLA数据 | ⭐⭐ 值得关注 |

### 2026：数据集与采集系统

| 论文 | 文档 | arXiv/会议 | 核心贡献 | 重要性 |
|------|------|-----------|----------|--------|
| EgoVerse | [`EgoVerse_2604.07607.md`](./EgoVerse_2604.07607.md) | 2604.07607 | 全球多实验室大规模人类视频数据集 | ⭐⭐ 值得关注 |
| AoE | [`AoE_2602.23893.md`](./AoE_2602.23893.md) | 2602.23893 | Always-on持续采集egocentric视频 | ⭐ 简单参考 |
| OpenEgo | [`OpenEgo_2509.05513.md`](./OpenEgo_2509.05513.md) | 2509.05513 | 1107小时多模态灵巧操作数据集 | ⭐ 简单参考 |
| XDex | [`XDex_ICLR2026.md`](./XDex_ICLR2026.md) | ICLR 2026 | 1000种手的跨形态灵巧抓取 | ⭐ 简单参考 |

---

## 方法分类

### 按技术路线分类

```
1. 分层学习
   └── MimicPlay: 人类视频→高层规划，机器人数据→底层执行

2. 联合训练
   ├── EgoMimic: 人类+机器人数据统一训练
   └── X-Diffusion: 噪声阈值选择性融合跨形态数据

3. 视频预训练
   ├── HRP: 提取可操作性先验
   ├── EgoScale: 大规模视频预训练
   ├── Being-H0.5: Physical Instruction Tuning
   └── CLAP: 对比潜在动作预训练

4. 零样本/少样本
   ├── Phantom: 零机器人数据
   ├── EgoZero: 智能眼镜零样本
   ├── LAP: 零样本跨形态
   └── HRT1: One-Shot轨迹迁移

5. 视频生成/编辑
   ├── Gen2Act: 生成人类视频
   └── Masquerade: 编辑机器人化

6. 特征对齐
   ├── Lidea: 隐式特征蒸馏+显式几何对齐
   └── LatentActionDiff: 对比学习统一动作空间

7. 数据集与采集
   ├── EgoVerse: 全球多实验室数据集
   ├── AoE: Always-on持续采集
   └── OpenEgo: 大规模多模态数据集

8. 跨形态抓取
   └── XDex: 1000种手的统一抓取策略
```

### 主流解决方案对比

```
方案1: 分层学习 (MimicPlay)
┌─────────────┐     ┌─────────────┐
│ 人类视频     │ ──► │ 高层规划     │
│ (学做什么)   │     │ (子目标)     │
└─────────────┘     └─────────────┘
                          │
                          ▼
┌─────────────┐     ┌─────────────┐
│ 机器人数据    │ ──► │ 底层执行     │
│ (学怎么做)   │     │ (动作生成)    │
└─────────────┘     └─────────────┘

方案2: 联合训练 (EgoMimic)
┌─────────────┐
│ 人类视频     │ ──┐
└─────────────┘   │    ┌─────────────┐
                  ├──► │ 统一策略     │
┌─────────────┐   │    │ (联合训练)   │
│ 机器人数据    │ ──┘    └─────────────┘
└─────────────┘

方案3: 视频预训练 (HRP, SWIM)
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 人类视频     │ ──► │ 预训练表示    │ ──► │ 机器人微调  │
└─────────────┘     └─────────────┘     └─────────────┘

方案4: 视频编辑 (Masquerade)
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 人类视频     │ ──► │ 编辑机器人化  │ ──► │ 直接训练    │
└─────────────┘     │ (人手→机械臂) │     └─────────────┘
                    └─────────────┘
```

---

## 核心挑战

1. **感知差距**: 人类视角 ≠ 机器人摄像头视角
2. **动作空间差距**: 人手动作 ≠ 机械臂动作
3. **形态差距**: 人体运动学 ≠ 机器人运动学
4. **无动作标签**: 视频只有视觉信息，无精确动作

### 数据对齐技术

| 技术 | 描述 | 使用方法 |
|------|------|----------|
| 时间对齐 | 调整人类和机器人操作速度差异 | EgoMimic: 人类数据慢放4倍 |
| 动作空间对齐 | 将人手轨迹映射到机器人末端执行器 | 3D手部姿态估计 + IK |
| 视觉对齐 | 统一人类和机器人的视觉表示 | 共享视觉编码器 |
| 跨域对齐 | 学习域无关的表示 | 对比学习、域适应 |

---

## 技术演进

```
2023-2024: 视频预训练 → 机器人微调
    ├── MimicPlay: 分层学习 (人类视频→规划，机器人→执行)
    └── HRP: 预训练可操作性先验
    ↓
2024-2025: 联合训练、零样本迁移
    ├── EgoMimic: 人类+机器人联合训练
    ├── Phantom: 零机器人数据训练
    └── GR00T N1: 人形机器人基础模型
    ↓
2026: 以人为中心、跨形态泛化
    ├── EgoScale: 大规模验证缩放定律 (R²=0.9983)
    ├── Being-H0.5: Human-Centric统一动作空间 (35K小时/30形态)
    ├── LAP: 语言-动作表示零样本迁移
    ├── ActiveGlasses: 智能眼镜主动视觉学习
    ├── Traj2Action: 3D轨迹共去噪框架 (+27%)
    └── VITRA: 非脚本化视频自动转换 (1M episodes)
```

---

## 重要性标注说明

- **⭐⭐⭐ 必读基础**: 领域奠基性工作，必读论文，理解核心技术路线的关键
- **⭐⭐ 值得关注**: 有创新点或特定场景有价值，建议浏览了解
- **⭐ 简单参考**: 数据集或特定应用，快速了解即可

---

## 阅读建议

### 入门路线（必读基础 ⭐⭐⭐）

1. **MimicPlay** → 理解分层学习思想（CoRL 2023 Oral）
2. **EgoMimic** → 理解联合训练方法
3. **HRP** → 理解预训练表示学习（RSS 2024）
4. **Phantom** → 理解零样本可能性（CoRL 2025）
5. **GR00T N1** → 理解工业界人形VLA方案

### 进阶路线（必读基础 ⭐⭐⭐）

6. **EgoScale** → 大规模验证缩放定律（20K+小时，R²=0.9983）
7. **Being-H0.5** → Human-Centric新训练范式（35K小时/30形态，ICLR 2026）
8. **LAP** → 语言-动作表示零样本跨形态迁移

### 扩展阅读（值得关注 ⭐⭐）

- **Traj2Action**: 3D轨迹统一表示（ICLR 2026）
- **Lidea/LatentActionDiff**: 特征对齐方法
- **Gen2Act/Masquerade**: 视频生成/编辑路线
- **EgoVerse**: 大规模协作数据集

### 快速参考（简单参考 ⭐）

- **EgoDex/OpenEgo/XDex**: 灵巧操作数据集
- **AoE**: 持续采集系统

---

## 数据集

| 数据集 | 规模 | 用途 | 链接 |
|--------|------|------|------|
| Ego4D | 3670小时 | 第一人称视频预训练 | [ego4d-data.org](https://ego4d-data.org) |
| Ego-Exo-4D | 1286小时 | 多视角同步 | [ego-exo4d-data.org](https://ego-exo4d-data.org) |
| Something-Something V2 | 220k视频 | 动作识别 | [developer.qualcomm.com](https://developer.qualcomm.com) |
| EPIC-KITCHENS | 100小时 | 厨房环境 | [epic-kitchens.github.io](https://epic-kitchens.github.io) |
| Project Aria | - | 智能眼镜采集 | [projectaria.com](https://projectaria.com) |
| **EgoVerse** | 多实验室 | 全球协作采集 | arXiv 2604.07607 |
| **AoE** | 大规模 | Always-on采集 | arXiv 2602.23893 |
| **OpenEgo** | 1107小时 | 灵巧操作多模态 | arXiv 2509.05513 |

---

## 开源项目与代码

| 项目 | 链接 | 特点 |
|------|------|------|
| EgoMimic | [egomimic.github.io](https://egomimic.github.io/) | 完整框架，包含硬件设计 |
| MimicPlay | [github.com/j3newton/mimicplay](https://github.com/j3newton/mimicplay) | 分层学习 |
| GR00T N1 | NVIDIA | 开源人形机器人基础模型 |
| OpenVLA | [github.com/openvla/openvla](https://github.com/openvla/openvla) | 开源VLA基准 |

---

## 研究方向

1. **数据效率**: 如何用更少的人类视频达到更好效果
2. **跨形态泛化**: 从人类到不同机器人的迁移
3. **多模态融合**: 结合触觉、力觉等多传感器
4. **安全迁移**: 确保人类行为到机器人的安全映射
5. **长时任务**: 长序列操作的规划与执行

---

## 参考文献 BibTeX

```bibtex
% 2026年论文
@article{zheng2026egoscale,
  title={EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data},
  author={Zheng, Ruijie and Niu, Dantong and Xie, Yuqi and others},
  journal={arXiv preprint arXiv:2602.16710},
  year={2026}
}

@article{luo2026beingh,
  title={Vision-Language-Action Pretraining from Large-Scale Human Videos},
  author={Luo, Hao and Feng, Yicheng and Zhang, Wanpeng and others},
  booktitle={ICLR},
  year={2026}
}

% 2024-2025年论文
@article{kareer2024egomimic,
  title={EgoMimic: Scaling Imitation Learning via Egocentric Video},
  author={Kareer, Simar and Patel, Dhruv and Punamiya, Ryan and others},
  journal={arXiv preprint arXiv:2410.24221},
  year={2024}
}

@article{wang2023mimicplay,
  title={MimicPlay: Long-Horizon Imitation Learning by Watching Human Play},
  author={Wang, Chen and Fan, Lin and Sun, Jiafei and others},
  journal={arXiv preprint arXiv:2302.12422},
  booktitle={CoRL},
  year={2023}
}

@article{srirama2024hrp,
  title={HRP: Human Affordances for Robotic Pre-training},
  author={Srirama, M. K. and Dasari, S. and Bahl, S. and Gupta, A.},
  journal={arXiv preprint arXiv:2407.18911},
  booktitle={RSS},
  year={2024}
}

@article{lepert2025phantom,
  title={Phantom: Training Robots Without Robots Using Only Human Videos},
  author={Lepert, M. and Fang, J. and Bohg, J.},
  journal={arXiv preprint arXiv:2503.00779},
  year={2025}
}

@article{bjorck2025groot,
  title={GR00T N1: An Open Foundation Model for Generalist Humanoid Robots},
  author={Bjorck, Johan and others},
  journal={arXiv preprint arXiv:2503.14734},
  year={2025}
}
```

---

*最后更新: 2026-04-21*