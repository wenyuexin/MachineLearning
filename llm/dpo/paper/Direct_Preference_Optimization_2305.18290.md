# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

> **一句话总结**：DPO 发现了一个数学恒等式——在 Bradley-Terry 偏好模型下，奖励函数可以用策略的 log-ratio 重新表达，配分函数在偏好差值中自动消去——这使得 RLHF 的两阶段训练可以被一个简单的分类损失替代。

## 基本信息
- **论文**：Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- **作者**：Rafael Rafailov*, Archit Sharma*, Eric Mitchell*, Stefano Ermon, Christopher D. Manning, Chelsea Finn
- **机构**：Stanford University, CZ Biohub
- **发表**：NeurIPS 2023
- **链接**：https://arxiv.org/abs/2305.18290

## 1. 问题与动机

### 解决什么问题

RLHF（强化学习从人类反馈中学习）是当前对齐语言模型的主流方法，但它有一个根本性的工程困境：**优化目标和优化手段之间的错配**。

我们真正想要的是"让模型更符合人类偏好"，但 RLHF 把这个问题拆成了两步——先用 Bradley-Terry 模型学一个奖励函数，再用 PPO 去优化这个奖励。这种拆分导致了三重困难：

1. **多模型开销**：需要同时维护 SFT 模型、奖励模型、策略模型、价值网络，训练时至少 4 个模型在 GPU 上
2. **RL 采样瓶颈**：PPO 需要在训练循环中从策略模型采样，计算开销大且不可并行
3. **管线不一致**：奖励模型和策略训练是两个独立阶段，奖励模型的优化目标（Eq.2）和策略的最终目标（Eq.3）并不完全对齐

### 现有方法的具体不足

标准 RLHF 流程的三步：
1. **SFT**：在高质量数据上监督微调，得到 $\pi^{\text{SFT}}$
2. **奖励建模**：用 Bradley-Terry 模型拟合人类偏好，训练奖励模型 $r_\phi$，损失为 Eq.2
3. **RL 优化**：用 PPO 最大化奖励，同时用 KL 散度约束防止偏离参考策略，目标为 Eq.3

**关键的错配**：步骤 2 的损失函数只关心奖励的排序是否正确（分类损失），步骤 3 关心的是奖励的绝对值能否指导策略更新（回归信号）。奖励模型训练时没有考虑 KL 约束，但策略优化时却受 KL 约束影响。这种割裂是 PPO 不稳定的根源之一——论文 5.2 节从数学上证明了这一点。

### 本文的核心假设

如果能找到一种奖励模型的参数化方式，使得其对应的最优策略可以**解析求解**（closed-form），就可以跳过显式的奖励建模和 RL 训练，直接用偏好数据训练策略。

## 2. 技术演进脉络

DPO 不是凭空出现的，它站在三个思想脉络的交汇点上：

| 思想脉络 | 代表工作 | 核心思路 | DPO 的继承与突破 |
|----------|---------|----------|-----------------|
| **RLHF** | Christiano et al. 2017, Ouyang et al. 2022 | 学奖励 → RL 优化 | 保留相同的优化目标（KL 约束的奖励最大化），但绕过了 RL |
| **Control as Inference** | Levine 2018, Korbak et al. 2022 | RL 目标可以转化为概率推断问题 | 利用了 KL 约束问题有解析解这一事实 |
| **偏好学习** | Bradley-Terry 1952, Plackett-Luce 1975 | 偏好是奖励的函数 | 关键洞察：偏好只依赖奖励的差值，使配分函数可消去 |

DPO 的核心贡献不在以上任何一条脉络内部，而在于**发现了一条隐含的通道**：从"控制即推断"脉络中取出解析解（Eq.4），从偏好学习脉络中取出配分函数消去（Eq.6），两者组合后 RLHF 的整个 RL 阶段变成了一个简单的分类问题。

## 3. 方法

### 3.1 最优策略的解析形式——问题的"半成品解"

RLHF 的 RL 阶段优化目标为：

$$\max_{\pi_\theta} \mathbb{E}_{x \sim \mathcal{D}, y \sim \pi_\theta(y|x)} \left[ r(x,y) \right] - \beta \mathbb{D}_{\text{KL}} \left[ \pi_\theta(y|x) \| \pi_{\text{ref}}(y|x) \right]$$

这个优化问题有一个优雅的解析解（附录 A.1 给出了完整推导）：

$$\pi_r(y|x) = \frac{1}{Z(x)} \pi_{\text{ref}}(y|x) \exp\left(\frac{1}{\beta} r(x,y)\right)$$

其中 $Z(x) = \sum_y \pi_{\text{ref}}(y|x) \exp\left(\frac{1}{\beta} r(x,y)\right)$ 是配分函数。

**为什么这是"半成品"**：这个解早就知道了（Peters & Schaal 2007, Peng et al. 2019），但一直没人用过，因为 $Z(x)$ 不可计算——它需要对所有可能的补全 $y$ 求和，而语言模型的词表和序列空间是天文数字。传统 RLHF 选择绕过这个解析解，转而用 PPO 做梯度上升。DPO 的突破在于：**不需要计算 $Z(x)$，因为偏好模型会帮你消掉它**。

### 3.2 奖励函数的重新参数化——"变量替换"的关键一步

对解析解取对数并重排，把奖励函数用策略表达出来：

$$r(x,y) = \beta \log \frac{\pi_r(y|x)}{\pi_{\text{ref}}(y|x)} + \beta \log Z(x)$$

**直觉理解**：一个策略比参考策略更倾向于生成某个回复 $y$，本身就说明 $y$ 的奖励更高。$\beta \log \frac{\pi_r(y|x)}{\pi_{\text{ref}}(y|x)}$ 就是"策略对 $y$ 的偏好程度"，$\beta \log Z(x)$ 是一个与 $y$ 无关的常数（只依赖 prompt $x$）。

这个重排的意义在于：**把"奖励函数"这个未知量替换成了"策略的 log-ratio"这个可计算量**。但还有一个障碍——$\beta \log Z(x)$ 仍然是未知的。

### 3.3 配分函数消去——DPO 可行的数学关键

Bradley-Terry 模型只关心两个回复的偏好概率：

$$p^*(y_w \succ y_l | x) = \sigma\left(r^*(x,y_w) - r^*(x,y_l)\right)$$

把重参数化代入后，$Z(x)$ 出现在 $r^*(x,y_w)$ 和 $r^*(x,y_l)$ 中各一次，做差时**完美消去**：

$$p^*(y_w \succ y_l | x) = \sigma\left(\beta \log \frac{\pi^*(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi^*(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\right)$$

**为什么能消去**：因为 $Z(x)$ 只依赖 $x$ 不依赖 $y$，而偏好判断只看两个回复的奖励**差值**。就像比较两座山的高度时，不需要知道海平面的绝对海拔——你只需要量两座山的相对高度差。$Z(x)$ 就是那个"海平面"，在比较中被消掉了。

**这是整篇论文最关键的数学洞察**：不是 $Z(x)$ 变得可计算了，而是 $Z(x)$ 根本不需要计算。

### 3.4 DPO 损失函数

有了消去配分函数后的偏好模型，直接套用最大似然估计就得到 DPO 损失：

$$\mathcal{L}_{\text{DPO}}(\pi_\theta; \pi_{\text{ref}}) = -\mathbb{E}_{(x,y_w,y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} \right) \right]$$

**实现极简**：论文附录 B 提供了 7 行 PyTorch 代码。核心就是计算两组 log-ratio 的差值，过 sigmoid，取 log，取负。不需要采样，不需要价值网络，不需要 KL 惩罚项。

### 3.5 梯度分析——DPO 为什么不会让模型退化

DPO 的梯度为：

$$\nabla_\theta \mathcal{L}_{\text{DPO}} = -\beta \mathbb{E} \left[ \underbrace{\sigma(\hat{r}_\theta(x,y_l) - \hat{r}_\theta(x,y_w))}_{\text{隐式奖励估计错误时权重更高}} \left( \underbrace{\nabla_\theta \log \pi(y_w|x)}_{\text{增加 } y_w \text{ 概率}} - \underbrace{\nabla_\theta \log \pi(y_l|x)}_{\text{降低 } y_l \text{ 概率}} \right) \right]$$

其中隐式奖励 $\hat{r}_\theta(x,y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}$。

**关键机制**：权重 $\sigma(\hat{r}_\theta(x,y_l) - \hat{r}_\theta(x,y_w))$ 是一个**自适应的重要性权重**。当隐式奖励已经正确排序（$y_w$ 的奖励高于 $y_l$），这个权重接近 0，梯度几乎不更新——模型已经学对了，不需要进一步调整。当隐式奖励排序错误（$y_l$ 的奖励反而更高），权重接近 1，梯度全力矫正。

**与朴素方法的对比**：如果去掉这个权重（即 Unlikelihood 训练），模型会无差别地降低 $y_l$ 的概率——即使 $y_l$ 本身并不差，只是不如 $y_w$ 好。附录 Table 3 展示了 Unlikelihood 在摘要和对话任务上生成无意义文本，证实了这一分析。这个自适应权重是 DPO 区别于"简单增大 $y_w$ 概率、降低 $y_l$ 概率"的关键。

### 3.6 DPO 流程

1. 对每个 prompt $x$，从 $\pi_{\text{ref}}$ 采样补全 $y_1, y_2$，标注人类偏好，构建数据集 $\mathcal{D}$
2. 优化语言模型 $\pi_\theta$ 最小化 $\mathcal{L}_{\text{DPO}}$，给定 $\pi_{\text{ref}}$、$\mathcal{D}$ 和 $\beta$

实践中，如果 $\pi^{\text{SFT}}$ 可用，初始化 $\pi_{\text{ref}} = \pi^{\text{SFT}}$；否则用 Preferred-FT 在偏好数据上训练 $\pi_{\text{ref}}$，缓解分布偏移。

## 4. 实验

### 4.1 实验设置

| 任务 | 模型 | 数据 | 奖励来源 | 评估方式 |
|------|------|------|---------|---------|
| 情感控制 | GPT-2-large | IMDb 前缀 | 预训练情感分类器（ground-truth） | reward-KL 前沿 |
| 摘要生成 | GPT-2-large (1.3B) SFT | Reddit TL;DR | 人类偏好标注 | GPT-4 胜率 + 人工评估 |
| 单轮对话 | Pythia-2.8B | Anthropic HH（170k 对话） | 人类偏好标注 | GPT-4 胜率 |

对比方法：PPO、PPO-GT（用真实奖励的 oracle）、Preferred-FT、Unlikelihood、Best-of-N。

### 4.2 主要结果

**情感控制（reward-KL 前沿，Figure 2 左）**：

DPO 的 reward-KL 前沿严格优于所有方法，包括 PPO-GT（有 ground-truth 奖励的 oracle）。这意味着 DPO 在相同 KL 预算下实现了更高的奖励——优化效率甚至超过了"开卷考试"的 PPO。

**为什么 DPO 能超过 PPO-GT**：PPO-GT 虽然有真实奖励，但仍需通过 PPO 做梯度估计，策略梯度的方差限制了优化效率。DPO 虽然只有隐式奖励，但它的梯度直接来自偏好数据的似然，信号更干净。

**摘要生成（GPT-4 胜率，Figure 2 右）**：

| 方法 | 最优温度 | 胜率 vs 参考 |
|------|---------|-------------|
| DPO | 0.0 | ~61% |
| PPO | 0.0 | ~57% |
| Best-of-128 | 0.0 | ~59% |
| Preferred-FT | — | 与 SFT 持平 |

DPO 的一个显著优势是**对采样温度的鲁棒性**：PPO 在高温时性能急剧退化至基线水平，而 DPO 在各温度下表现稳定。人工评估中 DPO 胜率 58% vs PPO。

**单轮对话（Figure 3 左）**：

DPO 是唯一一个在计算效率合理的方法中超越 Anthropic HH 数据集首选回复的方法，性能与 Best-of-128 相当，但推理开销远小。

### 4.3 消融实验与关键发现

**分布外泛化（Table 1）**：在 CNN/DailyMail 新闻数据上测试 TL;DR 训练的策略，DPO 胜率 0.36 vs PPO 0.26。说明 DPO 策略的泛化能力至少不弱于 PPO——尽管 DPO 没有使用 PPO 额外的无标注 prompt。

**Unlikelihood 失败（Table 3）**：去掉自适应重要性权重后，模型在摘要和对话任务上生成无意义文本（重复 token、空白输出）。这证实了梯度分析中的核心论点：**无约束的概率降低会导致模型退化，DPO 的自适应权重是必要的**。

**Best-of-N 基线**：Best-of-128 是一个强基线（与 DPO 性能相当），但推理时需要采样 128 个回复再排序，计算成本在部署时不可接受。

### 4.4 实验的遗漏

- **规模限制**：最大模型仅 6B 参数，未验证 DPO 在更大模型上的效果
- **PPO 基线可能偏弱**：对话任务中 PPO 的公开实现甚至不如基线模型，可能存在实现问题
- **$\beta$ 未充分调优**：论文承认"几乎没调 DPO 的 $\beta$"，DPO 的潜力可能被低估

## 5. 分析与讨论

### 5.1 关键洞察

**DPO 的本质是变量替换（change of variables）**。它没有改变 RLHF 的优化目标，也没有引入新的假设——它只是发现了同一个目标在策略空间中有一个等价但更简单的表达。就像同一个方程在不同坐标系下有不同的形式，DPO 选择了那个不需要 RL 的坐标系。

**语言模型本身就是隐式的奖励模型**：$\hat{r}_\theta(x,y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{\text{ref}}(y|x)}$。这个洞察后来被大量后续工作采用——RLHF-V/DPO-Zoo/Iterative DPO 等都用这个隐式奖励做在线迭代。

**为什么 PPO 不稳定（5.2 节的分析）**：PPO 优化的目标等价于 Eq.10，其中有一项 $f(r_\phi, \pi_{\text{ref}}, \beta) = r_\phi(x,y) - \beta \log \sum_y \pi_{\text{ref}}(y|x) \exp\left(\frac{1}{\beta} r_\phi(x,y)\right)$，这就是参考策略的 soft 价值函数。这项不影响最优解，但它的方差极大——用单样本估计（人类补全基线）引入高方差梯度，用学习到的价值函数又引入额外的优化难度。**DPO 的重参数化恰好选中了等价类中那个不需要价值函数的奖励**，从根源上消除了这个问题。

### 5.2 局限性（含根因分析）

**1. 只在 6B 以下参数验证**
- **根因**：论文发表时的计算资源限制。这不是方法本身的局限，但直到后续工作（如 Zephyr、Iterative DPO）才验证了更大规模的可行性
- **影响**：DPO 是否存在规模效应的"相变"未知——在更大模型上隐式奖励的校准性可能变化

**2. 奖励过度优化（Reward Over-optimization）**
- **现象**：Figure 3 右图显示训练后期 DPO 的胜率有轻微下降
- **根因**：DPO 的偏好数据是离线的，当策略偏离数据分布后，隐式奖励的估计可能变得不准确。PPO 有在线采样可以缓解这个问题，但 DPO 缺乏这一机制
- **后续方向**：Iterative DPO（在线 DPO）通过多轮数据采集解决了这个问题

**3. DPO 学到的隐式奖励可能与显式奖励模型不同**
- **根因**：Theorem 1 保证了 DPO 的奖励参数化**不损失表达能力**（所有等价类都可表示），但 DPO 选中了等价类中一个特定的成员——满足 $\sum_y \pi(y|x) = 1$ 的那个。这意味着 DPO 的隐式奖励自动归一化，而显式奖励模型没有这个约束
- **影响**：当需要显式使用奖励值（如 Best-of-N 采样、多模型协作）时，DPO 的隐式奖励可能不如显式奖励灵活

**4. GPT-4 评估的 prompt 敏感性**
- **现象**：GPT-4(S) prompt 倾向于选择更长、更重复的摘要；GPT-4(C) prompt 加入简洁性要求后结果更可靠
- **根因**：GPT-4 的判断受到 prompt 中的隐性偏好的影响，这不是 DPO 的问题，但影响了实验结论的可靠性

### 5.3 未来方向

- **在线/迭代 DPO**：多轮采集偏好数据，缓解分布偏移和奖励过度优化
- **扩展到更大模型**：验证 DPO 在 70B+ 参数上的效果和稳定性
- **其他模态**：DPO 的推导不依赖文本的特殊性质，理论上可应用于图像生成、代码等
- **奖励过度优化的理论分析**：DPO 中奖励 hacking 的机制与 PPO 有何不同？

## 6. 结论

DPO 的核心贡献不是一个新的训练技巧，而是一个**数学观察**：在 Bradley-Terry 偏好模型下，配分函数 $Z(x)$ 在偏好差值中自动消去，使得奖励函数可以用策略的 log-ratio 完全表达。这个观察把 RLHF 从"先学奖励再用 RL 优化"的两阶段问题，变成了"直接用偏好数据训练策略"的单阶段分类问题。

从更通用的原则来看，DPO 揭示了一种**变量替换**的思路：当优化问题的某个组件（配分函数）不可计算时，检查它是否在最终目标中可以被消去——如果可以，就不需要计算它。这个原则可能适用于其他需要配分函数的场景（如能量模型、归一化流等）。
