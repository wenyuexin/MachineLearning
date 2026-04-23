# Being-H0.5：以人为中心的跨形态机器人学习

**论文信息**
- 论文标题：Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization
- 中文标题：Being-H0.5：以人为中心的跨形态机器人学习规模化
- 作者：Hao Luo, Ye Wang, Wanpeng Zhang, Sipeng Zheng, Ziheng Xi, Chaoyi Xu, Haiweng Xu, Haoqi Yuan, Chi Zhang, Yiqing Wang, Yicheng Feng, Zongqing Lu
- 机构：BeingBeyond Team
- 会议：ICLR 2026
- arXiv: [2601.12993](https://arxiv.org/abs/2601.12993)
- 项目主页: https://research.beingbeyond.com/being-h05

> **核心创新**：将人类交互轨迹作为物理交互的"通用母语"，构建**35,000小时**多模态数据，实现跨30种机器人形态的统一学习

---

## 一、论文整体思路

### 1.1 研究背景

机器人形态各异，不仅是外观不同，更重要的是：

**跨形态挑战**：
- 不同的运动学结构
- 不同的传感器配置
- 不同的动作约定
- 不同的时序特性

**现有问题**：VLA模型往往针对特定机器人设计，难以跨形态迁移

### 1.2 核心思想

**核心直觉**：人类交互蕴含丰富的结构，这些结构在不同硬件上保持意义

**关键洞察**：
```
人类交互轨迹 = 可复用的操作语法
跨形态迁移 = 翻译问题，而非重新发明
```

### 1.3 三大核心创新

1. **Unified Action Space**：统一动作空间，映射异构机器人控制
2. **Mixture-of-Flow (MoF)**：混合流架构，解耦共享原语与形态特定专家
3. **Human-Centric Pre-training**：以人为中心的预训练范式

---

## 二、方法架构

### 2.1 整体框架

```
┌────────────────────────────────────────────────────────┐
│                Being-H0.5 框架                         │
├────────────────────────────────────────────────────────┤
│                                                        │
│  层1: UniHand-2.0 数据                                 │
│  ┌──────────────────────────────────────────┐         │
│  │ • 35,000+ 小时多模态数据                  │         │
│  │ • 30种不同机器人形态                      │         │
│  │ • 人类交互轨迹作为"母语"                  │         │
│  └──────────────────────────────────────────┘         │
│                       │                                │
│                       ▼                                │
│  层2: Unified Action Space                             │
│  ┌──────────────────────────────────────────┐         │
│  │ • 异构控制映射到语义对齐的槽位            │         │
│  │ • 低资源机器人从人类数据引导              │         │
│  │ • 统一状态-动作接口                       │         │
│  └──────────────────────────────────────────┘         │
│                       │                                │
│                       ▼                                │
│  层3: Mixture-of-Transformers                          │
│  ┌──────────────────────────────────────────┐         │
│  │ • 多模态理解路径                          │         │
│  │ • 动作生成路径                            │         │
│  │ • 共享注意力机制                          │         │
│  └──────────────────────────────────────────┘         │
│                       │                                │
│                       ▼                                │
│  层4: Mixture of Flow (MoF)                            │
│  ┌──────────────────────────────────────────┐         │
│  │ • 共享层：学习可迁移的运动原语            │         │
│  │ • 专家路由：形态特定的动态捕获            │         │
│  │ • 稀疏路由：高效推理                      │         │
│  └──────────────────────────────────────────┘         │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 2.2 Unified Action Space

**设计理念**：将异构机器人控制映射到语义对齐的动作槽位

**关键特性**：
- 低资源机器人可以从人类数据引导技能
- 高资源平台的知识可以迁移到低资源平台
- 统一的状态-动作接口

**数据分类**：

| 类型 | 描述 |
|------|------|
| "Grp" | 平行夹持器 (Parallel Gripper) |
| "Dex" | 灵巧手 (Dexterous Hand) |
| "Real" | 真实世界数据 |
| "Sim" | 仿真数据 |

### 2.3 Mixture of Flow (MoF)

**核心问题**：统一动作语言迫使模型覆盖非常不同的动态特性

**MoF解决方案**：

| 组件 | 功能 |
|------|------|
| 共享层 | 学习可迁移的运动原语 |
| 专家路由 | 捕获形态特定和任务特定的动态 |
| 稀疏路由 | 容量扩展而不增加推理成本 |

**优势**：
- 避免低DoF夹持器和高DoF灵巧手之间的负迁移
- 保持共享能力的同时支持专业化

### 2.4 部署机制

**两大关键设计**：

1. **Manifold-Preserving Gating**：在感知偏移下保持鲁棒性
2. **Universal Async Chunking**：适应不同延迟和控制特性的分块控制

---

## 三、数据：UniHand-2.0

### 3.1 数据规模

| 指标 | 数量 |
|------|------|
| 总数据量 | **35,000+ 小时** |
| 机器人形态 | **30种** |
| 交互记录 | **14,000 小时** |
| 数据来源 | 人类视频 + 机器人演示 |

### 3.2 数据多样性

**高多样性维度**：
- 相机视角变化
- 运动学结构差异
- 操作环境多样性

**末端执行器分类**：
- Grp (Parallel Gripper)：平行夹持器
- Dex (Dexterous Hand)：灵巧手

**数据来源分类**：
- Real：真实世界物理环境
- Sim：仿真环境

### 3.3 数据处理

**关键设计选择**：
- 限制仿真数据比例，避免其主导
- 保留仿真用于覆盖范围
- 不让仿真定义动作流形

---

## 四、实验与结果

### 4.1 仿真基准测试

**LIBERO基准**：

| 设置 | 成功率 |
|------|--------|
| Specialist | **98.9%** |
| Generalist | **97.6%** |

**RoboCasa Human-50基准**：

| 设置 | 成功率 |
|------|--------|
| Specialist | **53.9%** |
| Generalist | **53.3%** |

**实验设置**：
- 仅RGB输入 (224×224分辨率)
- 2B参数骨干网络

### 4.2 真实机器人实验

**评估范围**：
- 5种不同机器人形态
- 10个任务
- 涵盖：空间操作、长时域、双臂协调、泛化测试

**关键发现**：
1. 单一通用checkpoint接近专家性能
2. 长时域和双臂任务最容易暴露鲁棒性问题

### 4.3 消融实验

**脆弱点分析**：
- 长时域任务：时序假设被挑战
- 双臂任务：协调鲁棒性暴露

---

## 五、关键贡献

### 5.1 概念贡献

| 贡献 | 描述 |
|------|------|
| Human-Centric Learning | 人类轨迹作为通用操作语法 |
| Unified Action Space | 异构控制的统一表示 |
| Cross-Embodiment Transfer | 跨形态迁移的系统方案 |

### 5.2 架构贡献

1. **Mixture-of-Transformers**：分离理解路径和动作路径
2. **Mixture-of-Flow (MoF)**：共享原语 + 专家路由
3. **部署机制**：Manifold-Preserving Gating + Universal Async Chunking

### 5.3 数据贡献

- UniHand-2.0：最大规模的具身预训练数据
- 30种形态、35,000+小时
- 标准化数据处理流程

---

## 六、技术细节

### 6.1 模型架构

- Mixture-of-Transformers设计
- 强多模态理解路径
- 强动作生成路径
- 共享注意力机制

### 6.2 训练策略

- 统一序列建模
- 多任务预训练
- 连接人类演示和机器人执行

### 6.3 部署优化

- 感知偏移鲁棒性
- 异步控制适配
- 跨形态稳定性

---

## 七、与其他VLA对比

| 维度 | Being-H0.5 | RT-2 | OpenVLA | π₀ |
|------|------------|------|---------|-----|
| **核心理念** | Human-Centric | VLM迁移 | 开源VLA | Flow Matching |
| **预训练数据** | 35K小时 | 互联网数据 | 机器人数据 | 混合数据 |
| **跨形态** | **原生支持** | 单一形态 | 单一形态 | 有限支持 |
| **动作表示** | Unified Space | Token | 连续 | 连续 |
| **模型大小** | 2B | 大型 | 7B | 中型 |

---

## 八、局限性与未来方向

### 8.1 局限性

1. **计算成本**：大规模预训练需要大量资源
2. **形态覆盖**：仍有未覆盖的机器人类型
3. **实时性能**：复杂场景的推理延迟

### 8.2 未来方向

1. 更高效的训练方法
2. 更广泛的形态支持
3. 在线学习与适应
4. 强化学习后训练

---

## 九、BibTeX引用

```bibtex
@article{beingbeyond2026beingh05,
  title={Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization},
  author={Luo, Hao and Wang, Ye and Zhang, Wanpeng and Zheng, Sipeng and Xi, Ziheng and Xu, Chaoyi and Xu, Haiweng and Yuan, Haoqi and Zhang, Chi and Wang, Yiqing and Feng, Yicheng and Lu, Zongqing},
  journal={arXiv preprint arXiv:2601.12993},
  year={2026}
}
```

---

## 参考文献

1. Luo H, Wang Y, Zhang W, et al. Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization[J]. ICLR 2026.
2. OpenVLA: An Open-Source Vision-Language-Action Model. 2024.
3. π₀: A Vision-Language-Action Flow Model. 2024.

---

## 相关资源

- 项目主页: https://research.beingbeyond.com/being-h05
- 论文PDF: https://research.beingbeyond.com/projects/being-h05/being-h05.pdf
- arXiv: https://arxiv.org/abs/2601.12993
- HuggingFace: https://huggingface.co/papers/2601.12993

---

*文档创建日期：2026-04-21*
*最后更新：2026-04-21*
*论文来源：ICLR 2026, BeingBeyond Team*