# AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research Agents

- **arXiv**: [2605.11732](https://arxiv.org/abs/2605.11732)
- **Authors**: Jiarui Jin, Zexuan Yan, Shijian Wang, Wenxiang Jiao, Yuan Lu (Xiaohongshu Inc.)
- **Published**: 2026-05-12
- **Categories**: cs.IR, cs.CL, cs.MA, cs.MM

## 1. 核心问题

现有 Deep Research Agent 存在一个共性的架构瓶颈：**信息探索（information exploration，即搜索信息）和信息利用（information exploitation，即综合生成报告）被耦合在同一个模块中**（如 outline generator 或 report generator）。这导致：

1. 缺乏显式的优化目标和反馈信号，模型无法知道 outline 的哪些部分需要改进
2. 迭代优化时容易"过度修改"或"修改不足"，难以收敛
3. 搜索查询的规划与报告生成绑定在一起，限制了各自的优化潜力

## 2. 核心创新

### 2.1 解耦的 Critic-Generator 架构

AgentDisCo 将深度研究形式化为一个**对抗优化问题**，引入两个特化 agent：

| Agent | 角色 | 状态 | 动作 |
|-------|------|------|------|
| **Critic Agent** | 信息探索 (Exploration) | Generator State — outline + references | 评估当前 outline，生成 blueprints + 搜索查询 |
| **Generator Agent** | 信息利用 (Exploitation) | Critic State — blueprints + search queries | 执行搜索，根据结果更新 outline + references |

两者形成 **minimax-style yet cooperative loop**：critic 不断"攻击"当前 outline 的信息缺口（推动探索），generator 则"防守"性地吸收新证据完善 outline（巩固利用），两者在共同奖励函数下协同演化。

### 2.2 形式化建模

将交互过程建模为 **Dual-Agent Cooperative MDP**：

$$
\mathcal{M} = \langle \mathcal{S}_c, \mathcal{S}_g, \mathcal{A}_c, \mathcal{A}_g, \mathcal{P}, \mathcal{R}, \mathcal{T} \rangle
$$

- 每轮迭代 t，critic 和 generator 顺序行动
- Critic 先动，生成 blueprints（关键要点）+ 针对性搜索查询
- Generator 后动，执行搜索并更新 outline
- Joint state transition 是确定性的（agent 的输出直接构成下一状态）
- Reward 由 critic 对最终 outline 的评估分数构成

### 2.3 Meta-Optimization Harness

通过在 critic-generator loop 外部构建一个**元优化框架**实现自动策略发现：

- 利用 **Claude-Code / Codex** 等代码生成 agent 自动探索 agent 配置空间
- 构建 **Policy Bank**：结构化存储可复用的设计策略（搜索查询生成策略）
- Generator agent 被重用作 **Scoring Agent**，评估 critic 输出并产生质量信号
- 支持 criteria：completeness, diversity, search coverage, internal correlation
- 核心洞察：LLM 擅长提取和总结信息，但不擅长生成异构搜索查询 → 因此 harness 聚焦优化 critic 的搜索查询生成

### 2.4 Document Bank

解决多轮 outline 优化中的参考管理问题：
- 每轮搜索后并行评分文档 → 过滤低分文档 → 提取关键证据三元组
- 维护 persistent 的参考视图，避免上下文窗口被陈旧/冗余内容污染
- 保证前一轮的已验证证据跨轮次可用

### 2.5 Planner Agent

- 将查询分类为 **information seeking** 和 **decision making** 两大类（共 10 个细分子类）
- 推断预期回复风格，condition 下游 critic 和 generator

### 2.6 Writer Agent

- 将 outline + references 按结构化分区 → 序列化的自包含 chunks
- 每个 chunk 从 Document Bank 中直接检索相关证据
- 采用 intra-sectional reasoning cycle：逐块写作，前块作为后块的 context
- 输出 Markdown 格式报告，每条引用附带 URL

### 2.7 Render Agent

- 将结构化报告转为可视化呈现（HTML 网页 / Rednote 风格海报 / Slide）
- 支持可插拔模板和样式组件
- 使用 Gemini 模型作为 content planner 和 slide generator

## 3. GALA Benchmark

### 动机

现有 benchmarks（DeepResearchBench, DeepConsult, DeepResearchGym）过度聚焦学术和领域咨询类查询，与真实用户日常生活信息需求脱节。

### 方法

- 从小红书平台收集 **10,000+ 高活跃用户**的浏览和评论历史
- Agentic workflow 自动挖掘潜在深度研究兴趣，合成个性化查询
- LLM-based 自动筛选 + 人工验证，从 260,000 候选 query 中精炼出 **100 个高质量 query**

### 分布特征

| Benchmark | 主导话题 |
|-----------|---------|
| DeepResearchBench | Science & Technology (26.8%), Finance & Business (17.0%) |
| DeepConsult | Finance & Business (85.3%) |
| DeepResearchGym | Finance & Business (20.0%), Science & Technology (15.0%) |
| **GALA (Ours)** | **Home & Hobbies (25.0%), Travel (18.0%), Fashion & Beauty (18.0%)** |

### 评估协议

- 采用 **RACE** 指标（参考报告 + pairwise scoring by LLM judge）
- 四个维度：Comprehensiveness, Insight, Instruction-Following, Readability
- Judge model：Gemini-3-Flash

## 4. 实验验证

### 4.1 DeepResearchBench（RACE 分数）

| System | Overall | Comp. | Insight | Inst. | Read. | Eff.c. | C.acc. |
|--------|---------|-------|---------|-------|-------|--------|--------|
| **AgentDisCo (Claude-Opus-4.6)** | **54.02** | **53.38** | **56.65** | **53.11** | 51.53 | 89.88 | **93.56** |
| AgentDisCo w/ Harness (Gemini-2.5-Pro) | 52.11 | 51.89 | 53.43 | 51.87 | 50.45 | 69.65 | 89.55 |
| AgentDisCo (Gemini-2.5-Pro) | 51.44 | 51.23 | 52.49 | 51.57 | 50.39 | 63.94 | 89.06 |
| Gemini-2.5-Pro-Deepresearch | 49.71 | 49.51 | 49.45 | 50.12 | 50.00 | — | 78.30 |
| OpenAI-DeepResearch | 46.45 | 46.46 | 43.73 | 49.39 | 47.22 | 39.79 | 75.01 |

### 4.2 DeepConsult & DeepResearchGym

- AgentDisCo w/ Harness (Gemini-2.5-Pro)：DeepConsult win rate 56.86%, overall 6.86
- AgentDisCo (Claude-Opus-4.6)：DeepConsult win rate **65.88%**, DeepResearchGym overall **97.54**
- Harness 优化在 DeepResearchGym 上提升 overall score 从 95.63 → 96.21

### 4.3 GALA

| System | Overall | Comp. | Insight | Inst. | Read. |
|--------|---------|-------|---------|-------|-------|
| **AgentDisCo w/ Rednote & Harness** | **51.90** | 51.61 | **53.44** | **51.78** | 50.67 |
| AgentDisCo w/ Rednote | 51.02 | 50.88 | 51.11 | 51.25 | **50.95** |
| AgentDisCo w/ Harness | 50.58 | 50.41 | 51.24 | 50.16 | 49.85 |
| AgentDisCo (reference) | 50.00 | 50.00 | 50.00 | 50.00 | 50.00 |
| Doubao-Research | 49.82 | 50.87 | 47.42 | 50.65 | 50.86 |

### 4.4 消融与分析

- **Outline Optimization 轮数**：随着轮数增加，Overall score 稳步上升，comprehensiveness 和 insight 提升最显著
- **Harness 一致性验证**：Search Coverage 从 round 0 的 62.50 提升到 round 20 的 82.05，与 end-to-end 分数趋势一致
- **检索源对比**：Rednote 搜索在 lifestyle 场景下优于 Google 搜索，因 Rednote 提供用户生成的经验导向、场景化的内容。结合两者时 comprehensiveness 提升但 insight 和 readability 下降（噪音增多）

## 5. 关键洞察

1. **解耦的价值**：将探索和利用分离为两个特化 agent 比耦合设计能产生更深、更全面的研究内容。优势主要来自更好的内容支持 and 论证结构，而非表面写作流畅性。
2. **Harness 自动优化的有效性**：无需人力干预即可自动发现搜索策略，且优化信号与下游 benchmark 表现一致。
3. **Domain-specific 检索源优势**：在 lifestyle 场景下，社区驱动的垂直内容源（Rednote）优于通用搜索引擎。
4. **Scalability**：框架随 backbone 模型能力增强而一致提升，Claude-Opus-4.6 实例化取得最佳结果。

## 6. 局限与未来工作

- Harness 优化聚焦于搜索查询生成，outline 组织部分留给未来工作
- Writer agent 的优化尚未纳入 harness scope
- 人工设定轮次数/阈值等超参数
- Policy bank 的 BM25 检索器较为简单
- 渲染 agent 的评估指标有待建立

## 7. 关联工作

| 系统 | 架构特点 | 与 AgentDisCo 区别 |
|------|---------|-------------------|
| OpenAI Deep Research | 闭源 | 探索与利用耦合在同一模块 |
| Gemini Deep Research | 闭源 | 同上 |
| WebWeaver (Li et al., 2025) | 动态 Outline 迭代 | 无显式 critic-generator 对立 |
| RhinoInsight (Lei et al., 2025) | Control mechanisms | 无 Agent 间的对抗协作 |
| Meta-Harness (Lee et al., 2026) | 外部元优化 | 论文以此为基础构建 harness |

---

*笔记由 Scholar Agent 编写 | 日期: 2026-05-13*