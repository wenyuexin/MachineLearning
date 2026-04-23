# GraphGen: 基于知识图谱的合成数据生成框架

## 1\. 概述

GraphGen 是一个面向大语言模型（LLM）监督微调的合成数据生成框架。它通过构建细粒度的知识图谱来指导数据生成，能够识别 LLM 的知识缺口，并针对高价值的长尾知识优先生成问答对。该框架支持多种数据类型（文本、图像），可生成多样化的问答格式（原子问答、聚合问答、多跳推理、思维链等）。

**核心优势**：

- **知识驱动**：基于知识图谱的显式结构指导数据生成

- **知识缺口识别**：利用期望校准误差（ECE）识别模型薄弱环节

- **多样化输出**：支持原子问答、聚合问答、多跳推理、CoT、VQA 等多种数据类型

- **分布式执行**：基于 Ray 的并行流水线处理海量数据

- **可扩展架构**：模块化设计支持多种 LLM 后端、存储后端和数据源

---

## 2\. 系统架构

### 2.1 整体架构

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           GraphGen 数据生成流水线                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐│
│  │  读取    │───>│  分块    │───>│ 构建KG   │───>│  测验    │───>│  评判  ││
│  │ (Read)   │    │ (Chunk)  │    │(Build KG)│    │  (Quiz)  │    │(Judge) ││
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘    └────────┘│
│                                              │                    │        │
│                                              v                    v        │
│                                        ┌──────────┐    ┌──────────────────┐│
│                                        │ 知识图谱 │    │ ECE/知识缺口计算 ││
│                                        │  存储    │    │ (节点/边 Loss)   ││
│                                        └──────────┘    └──────────────────┘│
│                                                               │             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                │             │
│  │  输出    │ │<───│  生成    │ │<───│  分区    │ │<───────────────┘             │
│  │(Output)  │    │(Generate)│    │(Partition)│                               │
│  └──────────┘    └──────────┘    └──────────┘                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 核心组件关系

<!-- 架构图：支持所有 Markdown 渲染器 -->
```
+-------------------+        +-------------------+        +-------------------+
|     数据源层       |        |      处理层        |        |     存储层/LLM层   |
+-------------------+        +-------------------+        +-------------------+
|                   |        |                   |        |                   |
|  ┌-----------┐   |        |  ┌-----------┐   |        |  ┌-----------┐   |
|  |  文件系统  |---+------->|  |  执行引擎  |   |        |  |  KV存储    |   |
|  └-----------┘   |        |  └-----+-----┘   |        |  └-----^-----┘   |
|                  |        |        |         |        |        |          |
|  ┌-----------┐   |        |        v         |        |  ┌-----+-----┐   |
|  |  数据库   |----+------->|  ┌-----------┐   |        |  |  图存储   |   |
|  └-----------┘   |        |  |   算子库   |---+------->|  └-----^-----┘   |
|                  |        |  └-----+-----┘   |        |        |          |
|  ┌-----------┐   |        |        |         |        |  ┌-----+-----┐   |
|  | 搜索引擎  |----+------->|        v         |        |  | 合成模型  |   |
|  └-----------┘   |        |   (调度执行)      |        |  └-----^-----┘   |
|                  |        |                  |        |        |          |
+-------------------+        +-------------------+        |  ┌-----+-----┐   |
                                                          |  | 评估模型  |   |
                                                          |  └-----------┘   |
                                                          |                  |
                                                          +-------------------+

数据流向：数据源 → 执行引擎 → 算子库 → (存储层/LLM层)
```

<!-- 在线预览链接（可选）：https://mermaid.live/edit#pako:eNpVkE1qwzAQhe9zikGrbCIkPw2l2ElJILSkJ7Acj62JIwvLSmly9xG0pU3xGnnzPs0cEfKMQYm9W4XNq-9zNqzLLKhvOtb-xJxjR9r5HuQAXoR_9WIvOCA9KYgh0N-G45AKyj3ZoJ9M2iBWey3m2mIQZ9p6bWXZQbFgqBeb2x_oN2z4A-5UNM8 -->

---

## 3\. 核心功能详解

### 3.1 知识图谱构建

#### 3.1.1 实体与关系抽取

GraphGen 采用基于 LLM 的迭代式知识抽取策略，核心思想是**迭代精化（Gleaning）**——通过多轮自检逐步补充遗漏的知识。

**抽取流程**（伪代码）：

```python
class LightRAGKGBuilder:
    def extract(chunk):
        # Step 1: 语言检测
        language = detect_language(chunk.content)
        
        # Step 2: 初始抽取
        prompt = build_extraction_prompt(chunk.content, language)
        result = llm.generate(prompt)
        
        # Step 3: 迭代精化（最多 max_loop 轮）
        for i in range(max_loop):
            # 询问："是否还有遗漏的实体/关系？"
            check_prompt = build_check_prompt(result, language)
            need_continue = llm.generate(check_prompt)
            
            if need_continue != "yes":
                break
            
            # 补充抽取遗漏内容
            supplement = llm.generate(build_continue_prompt(result))
            result += supplement
        
        return parse_entities_and_relations(result)
```

**技术要点**：

1. **迭代精化机制**：通过多轮自检询问"是否遗漏实体/关系"，逐步补充知识

2. **多语言支持**：内置中英文实体抽取模板，自动检测输入语言

3. **结构化输出**：使用特定分隔符（`<|>`、`##`、`<|COMPLETE|>`）确保可解析性

#### 3.1.2 实体对齐与合并

当同一实体在多个文档中被抽取时，需要合并其属性和描述。

**合并逻辑**（伪代码）：

```python
def merge_nodes(entity_name, node_list):
    # 1. 类型消歧：频次投票决定实体类型
    type_votes = Counter([n.entity_type for n in node_list])
    final_type = type_votes.most_common(1)[0][0]
    
    # 2. 描述合并：去重后拼接
    descriptions = set([n.description for n in node_list])
    merged_desc = "<SEP>".join(sorted(descriptions))
    
    # 3. 如果描述过长，使用 LLM 摘要
    if token_count(merged_desc) > max_tokens:
        merged_desc = llm.summarize(merged_desc)
    
    # 4. 溯源追踪：记录来源文档 ID
    source_ids = set([n.source_id for n in node_list])
    
    return Entity(
        name=entity_name,
        type=final_type,
        description=merged_desc,
        sources=source_ids
    )
```

**技术要点**：

- **类型消歧**：同一实体在不同上下文中可能有不同类型，采用频次投票决定

- **描述摘要**：当描述超过 token 限制时，使用 LLM 进行摘要生成

- **溯源追踪**：记录 `source_id` 以支持数据血缘追踪

### 3.2 知识缺口识别 (ECE)

#### 3.2.1 核心思想

GraphGen 创新性地将**期望校准误差（Expected Calibration Error, ECE）** 应用于知识图谱场景：

```
ECE = E[|P(模型回答正确) - 1{模型回答正确}|]
```

在实践中，使用"理解损失（comprehension loss）"作为 ECE 的代理指标：

**评估流程**（伪代码）：

```python
class JudgeService:
    def judge_knowledge_unit(unit):
        # 构建判断提示："以下描述是否正确？{unit.description}"
        prompt = build_judgement_prompt(unit.description)
        
        # 获取模型对 Yes/No 的概率分布
        # 返回形式：[("yes", 0.7), ("yeah", 0.2), ("no", 0.1)]
        topk_tokens = llm.generate_topk_per_token(prompt)
        
        # 归一化：将同义词合并（yeah/yep/是/对 → yes）
        prob_dist = normalize_yes_no_synonyms(topk_tokens)
        # 结果：{"yes": 0.9, "no": 0.1}
        
        # 计算交叉熵损失（ground_truth 默认为 "yes"）
        loss = -log(prob_dist["yes"])
        
        return {"unit": unit, "loss": loss}
```

#### 3.2.2 同义词归一化

为了准确评估模型的"是/否"判断，需要将同义词归一化：

```python
def normalize_yes_no_synonyms(tokens):
    yes_synonyms = {"yes", "yeah", "yep", "是", "对", "正确"}
    no_synonyms = {"no", "nope", "nah", "不", "否", "错误"}
    
    yes_prob = sum(t.prob for t in tokens if t.text in yes_synonyms)
    no_prob = sum(t.prob for t in tokens if t.text in no_synonyms)
    
    total = yes_prob + no_prob
    return {"yes": yes_prob/total, "no": no_prob/total}
```

**同义词归一化**：支持中英文 yes/no 同义词（如 "yeah"/"yep"/"是"/"对"）

### 3.3 图谱分区策略

#### 3.3.1 ECE-based 分区

基于 ECE 的分区策略优先选择知识缺口大的单元作为种子，通过 BFS 扩展形成社区。

**分区算法**（伪代码）：

```python
class ECEPartitioner:
    def partition(graph, unit_sampling="max_loss"):
        # 1. 收集所有知识单元（节点 + 边）
        units = []
        for node in graph.get_all_nodes():
            units.append(("node", node.id, node.data))
        for edge in graph.get_all_edges():
            units.append(("edge", (edge.src, edge.dst), edge.data))
        
        # 2. 按理解损失排序
        if unit_sampling == "max_loss":
            units.sort(key=lambda u: u[2].get("loss", 0), reverse=True)
        elif unit_sampling == "min_loss":
            units.sort(key=lambda u: u[2].get("loss", 0))
        else:  # random
            shuffle(units)
        
        # 3. BFS 扩展社区
        communities = []
        used = set()
        
        for seed in units:
            if seed.id in used:
                continue
            
            community = grow_community_bfs(seed, graph, used)
            if community:
                communities.append(community)
                used.update(community.nodes)
                used.update(community.edges)
        
        return communities
    
    def grow_community_bfs(seed, graph, used):
        community = {seed}
        queue = [seed]
        token_count = seed.data.get("length", 0)
        
        while queue:
            current = queue.pop(0)
            
            for neighbor in graph.get_neighbors(current):
                if neighbor in used:
                    continue
                
                new_token_count = token_count + neighbor.data.get("length", 0)
                if len(community) >= max_units or new_token_count > max_tokens:
                    break
                
                community.add(neighbor)
                queue.append(neighbor)
                token_count = new_token_count
        
        return community
```

**分区策略**：

- `max_loss`：优先选择知识缺口大的单元（推荐，针对模型薄弱环节）

- `min_loss`：优先选择模型掌握较好的单元

- `random`：随机选择

#### 3.3.2 Leiden 社区发现

支持基于 Leiden 算法的社区发现，用于生成 CoT（思维链）数据：

```
Leiden 算法优势：
- 比 Louvain 算法更快收敛
- 保证社区内连接紧密
- 适合发现层次化社区结构
```

---

#### 3.3.3 其他分区方法

GraphGen 支持多种分区策略，以适应不同的数据生成需求：

| 分区方法 | 核心策略 | 适用场景 | 生成的社区特点 |
|:---------|:---------|:---------|:---------------|
| **BFS** | 随机种子+BFS扩展 | 通用聚合问答 | 社区形状较规则，直径较小 |
| **DFS** | 随机种子+DFS扩展 | 长链状知识 | 社区呈链式延伸，适合顺序推理 |
| **ECE** | 按理解损失排序+BFS | 针对薄弱知识 | 优先包含模型理解差的知识单元 |
| **Triple** | 提取三元组(node-edge-node) | 多跳推理 | 每个社区=1个三元组，结构固定 |
| **Quintuple** | 提取五元组(3节点+2边) | 掩码填空 | 每个社区=1条两跳路径 |
| **Leiden** | 模块度优化社区发现 | CoT/复杂推理 | 社区内部高内聚，符合自然结构 |
| **AnchorBFS** | 以指定类型节点为锚点 | VQA/多模态 | 社区以图像/关键实体为中心 |

**BFS vs DFS 的区别**：

```python
# BFSPartitioner - 广度优先，社区紧凑
queue = deque([seed])
while queue:
    node = queue.popleft()  # 从左侧弹出（FIFO）
    for neighbor in graph.get_neighbors(node):
        queue.append(neighbor)  # 添加到右侧
        
# DFSPartitioner - 深度优先，社区呈链状
stack = [seed]
while stack:
    node = stack.pop()  # 从右侧弹出（LIFO）
    for neighbor in graph.get_neighbors(node):
        stack.append(neighbor)  # 添加到右侧
```

**Triple/Quintuple 分区**：

```python
class TriplePartitioner:
    """输出固定结构：2个节点 + 1条边"""
    def partition(graph):
        for node in graph.nodes:
            for neighbor in graph.get_neighbors(node):
                yield Community(
                    nodes=[node, neighbor],
                    edges=[(node, neighbor)]
                )

class QuintuplePartitioner:
    """输出固定结构：3个节点 + 2条边（两跳路径）"""
    def partition(graph):
        for center in graph.nodes:
            neighbors = graph.get_neighbors(center)
            # 将邻居两两配对
            for i in range(0, len(neighbors)-1, 2):
                n1, n2 = neighbors[i], neighbors[i+1]
                yield Community(
                    nodes=[n1, center, n2],
                    edges=[(n1, center), (center, n2)]
                )
```

---

#### 3.3.4 分区方法与数据生成方法的关联矩阵

分区策略的选择直接影响生成的数据类型和质量：

| 分区方法 | 聚合问答 | 多跳推理 | 思维链(CoT) | 掩码填空 | VQA | 原子问答 |
|:---------|:--------:|:--------:|:-----------:|:--------:|:---:|:--------:|
| **BFS** | ✅ 推荐 | ⚠️ 可选 | ⚠️ 可选 | ❌ 不适合 | ⚠️ 可选 | ⚠️ 可选 |
| **DFS** | ⚠️ 可选 | ✅ 推荐 | ⚠️ 可选 | ❌ 不适合 | ❌ 不适合 | ⚠️ 可选 |
| **ECE** | ✅ 推荐 | ⚠️ 可选 | ⚠️ 可选 | ⚠️ 可选 | ✅ 推荐 | ❌ 不适合 |
| **Triple** | ❌ 不适合 | ✅ 推荐 | ❌ 不适合 | ❌ 不适合 | ❌ 不适合 | ⚠️ 可选 |
| **Quintuple** | ❌ 不适合 | ❌ 不适合 | ❌ 不适合 | ✅ 推荐 | ❌ 不适合 | ❌ 不适合 |
| **Leiden** | ⚠️ 可选 | ⚠️ 可选 | ✅ 推荐 | ❌ 不适合 | ⚠️ 可选 | ❌ 不适合 |
| **AnchorBFS** | ⚠️ 可选 | ❌ 不适合 | ❌ 不适合 | ❌ 不适合 | ✅ 推荐 | ❌ 不适合 |

**说明**：
- ✅ **推荐**：分区策略与该数据类型最佳匹配
- ⚠️ **可选**：可以使用，但非最优选择
- ❌ **不适合**：社区结构不适合该数据类型

**关联详解**：

1. **聚合问答 + BFS/ECE**
   - BFS 生成紧凑的社区，多个相关实体/关系集中在小范围内
   - 适合"综合理解"类问题
   
2. **多跳推理 + Triple/DFS**
   - Triple 分区固定输出 (A)-[R]->(B) 结构
   - 天然适合"A通过什么关系连接到B"类问题
   - DFS 的链式扩展适合顺序多跳

3. **思维链 + Leiden**
   - Leiden 发现自然社区结构
   - 社区内部实体关联紧密，适合构建复杂推理链
   - 社区大小可控，便于控制 CoT 复杂度

4. **掩码填空 + Quintuple**
   - Quintuple 固定输出 3节点+2边的路径结构
   - 可在路径中间节点/边上设计掩码
   - 答案确定性高，适合 RLVR

5. **VQA + AnchorBFS/ECE**
   - AnchorBFS 以图像节点为锚点，向外扩展相关文本知识
   - 确保生成的问答与图像内容相关
   - ECE 可优先选择模型理解差的多模态知识

6. **原子问答**
   - 不需要复杂的分区策略
   - 可直接从知识图谱中随机采样单个实体/关系

### 3.4 多样化数据生成

GraphGen 的核心价值之一是能够基于同一知识图谱生成多种类型的训练数据，满足不同阶段的训练需求：

|数据类型|适用场景|技术特点|
|-|-|-|
|**原子问答 (Atomic)**|基础知识学习|针对单一知识单元，问题简单直接|
|**聚合问答 (Aggregated)**|综合能力训练|整合多个相关知识点，答案较复杂|
|**多跳推理 (Multi-hop)**|逻辑推理能力|需遍历多条边才能得出答案|
|**思维链 (CoT)**|复杂推理训练|显式生成中间推理步骤|
|**视觉问答 (VQA)**|多模态训练|结合图像和文本生成问答|
|**多项选择 (Multi-choice)**|标准化考试/评测|自动生成干扰选项|
|**多答案 (Multi-answer)**|多选题场景|支持多个正确答案|
|**填空题 (Fill-in-blank)**|关键概念强化|掩码关键术语或实体|
|**掩码填空 (Masked Fill-in-blank)**|RLVR 可验证奖励|随机掩码实体名，答案确定|
|**判断题 (True/False)**|快速知识检测|生成陈述句并标注真假|

---

#### 3.4.1 原子问答 (Atomic QA)

**原理**：从知识图谱中选取单个实体或关系，直接基于其描述生成问答对。

```
输入: 实体 "OsDT11" - "一种感温型常规稻品种..."
输出:
  Q: OsDT11 是什么类型的水稻品种？
  A: OsDT11 是一种感温型常规稻品种，由广东省农业科学院水稻研究所选育。
```

**核心逻辑**（伪代码）：

```python
class AtomicGenerator:
    def generate(nodes, edges):
        # 选择单个知识单元
        unit = select_single_unit(nodes, edges)
        
        # 构建 Prompt：要求基于给定内容生成一个问答对
        prompt = f"""
        基于以下内容生成一个问答对：
        {unit.description}
        
        要求：问题要针对该内容的核心信息
        输出格式：<question>...</question><answer>...</answer>
        """
        
        response = llm.generate(prompt)
        return parse_qa(response)  # 解析 XML 标签
```

---

#### 3.4.2 聚合问答 (Aggregated QA)

**原理**：将多个相关实体和关系整合成连贯的文本段落，再基于该段落生成问答。这种"先整合后提问"的方式模拟了真实场景中的综合理解任务。

**两阶段流程**：

```
阶段1 - 内容整合：
  输入: [实体A, 实体B, 关系(A,B)]
  中间输出: "OsDT11 是一种感温型常规稻品种..."
  
阶段2 - 问题生成：
  输入: 整合后的文本
  输出: Q&A 对
```

**核心逻辑**（伪代码）：

```python
class AggregatedGenerator:
    def generate(nodes, edges):
        # 阶段1：将知识片段重写成连贯文本（作为答案）
        rephrase_prompt = build_rephrase_prompt(nodes, edges)
        context = llm.generate(rephrase_prompt)
        # 解析 <rephrased_text> 标签
        answer_text = parse_rephrased(context)
        
        # 阶段2：基于重写的文本生成问题
        question_prompt = build_question_prompt(answer_text)
        question = llm.generate(question_prompt)
        
        return {"question": question, "answer": answer_text}
```

---

#### 3.4.3 多跳推理 (Multi-hop QA)

**原理**：问题答案需要遍历知识图谱中的多条边才能得出，训练模型的多步推理能力。

```
知识图谱片段：
  [OsDT11] --属于--> [CRP家族]
  [CRP家族] --特征--> [分泌信号肽]

问题：属于 CRP 家族的 OsDT11 具有什么特征？
答案：OsDT11 是一种分泌信号肽。
（推理路径：OsDT11 → CRP家族 → 分泌信号肽）
```

**核心逻辑**（伪代码）：

```python
class MultiHopGenerator:
    def generate(nodes, edges):
        # 将实体和关系以结构化方式输入
        prompt = f"""
        实体列表：
        {format_entities(nodes)}
        
        关系列表：
        {format_relationships(edges)}
        
        要求：
        1. 设计一个问题，其答案需要综合上述多个实体/关系
        2. 问题应该需要多步推理才能回答
        3. 答案必须准确且能从给定信息中推导
        
        输出格式：<question>...</question><answer>...</answer>
        """
        
        response = llm.generate(prompt)
        return parse_qa(response)
```

---

#### 3.4.4 思维链 (Chain-of-Thought, CoT)

**原理**：分两个阶段生成：先设计推理模板（元推理），再基于模板生成详细的逐步推理过程。这是 GraphGen 最复杂的数据类型。

**两阶段架构**：

```
阶段1 - 元推理（Meta-Reasoning）：
  任务：分析知识图谱，设计推理路径模板
  输入: 实体 + 关系
  输出: <question>问题</question> + <reasoning_path>推理蓝图</reasoning_path>

阶段2 - 推理实例化：
  任务：基于蓝图生成详细推理步骤
  输入: 问题 + 推理蓝图 + 原始知识
  输出: 完整的逐步推理过程（CoT）
```

**示例输出**：

```
问题：为什么 OsDT11 能够在细胞壁上被检测到？

推理路径（蓝图）：
1. 识别 OsDT11 的蛋白家族归属
2. 分析该家族的亚细胞定位特征
3. 解释实验观察结果

CoT 回答：
首先，OsDT11 属于 CRP 家族。根据 CRP 家族的特征，
其成员通常具有分泌信号肽。因此，当进行亚细胞定位
实验时，RFP 信号主要出现在细胞壁上...
```

**核心逻辑**（伪代码）：

```python
class CoTGenerator:
    def generate(nodes, edges):
        # 阶段1：设计推理模板
        template_prompt = build_template_prompt(nodes, edges)
        template_response = llm.generate(template_prompt)
        
        question = parse_question(template_response)
        reasoning_path = parse_reasoning_path(template_response)
        
        # 阶段2：基于模板生成详细推理
        generation_prompt = build_cot_prompt(
            nodes, edges, question, reasoning_path
        )
        cot_answer = llm.generate(generation_prompt)
        
        return {
            "question": question,
            "answer": cot_answer,
            "reasoning_path": reasoning_path
        }
```

---

#### 3.4.5 视觉问答 (Visual QA, VQA)

**原理**：处理多模态知识图谱（包含图像节点），生成需要结合视觉信息才能回答的问题。

```
知识图谱片段：
  [图像节点: path/to/image.jpg] --展示--> [OsDT11-RFP融合蛋白]
  [OsDT11-RFP] --定位在--> [细胞壁]

问题：图中绿色荧光信号主要出现在细胞的哪个部位？
答案：细胞壁
```

**核心逻辑**（伪代码）：

```python
class VQAGenerator:
    def generate(nodes, edges):
        # 提取图像路径（从图像节点的 metadata 中）
        image_nodes = filter_image_nodes(nodes)
        
        prompt = build_vqa_prompt(nodes, edges)
        response = llm.generate(prompt)
        qa_pairs = parse_qa(response)
        
        # 将图像路径附加到每个 QA 对
        for qa in qa_pairs:
            qa["image"] = image_nodes[0].metadata.path
        
        return qa_pairs
    
    def format_output(qa, format_type):
        # 支持多种输出格式（Alpaca/ShareGPT/ChatML）
        if format_type == "ChatML":
            return {
                "messages": [
                    {"role": "user", "content": [{"text": qa.question, "image": qa.image}]},
                    {"role": "assistant", "content": [{"text": qa.answer}]}
                ]
            }
```

---

#### 3.4.6 多项选择 (Multi-choice)

**原理**：基于知识内容生成问题，并构造一个正确答案和三个干扰项。干扰项的设计是关键技术难点。

```
问题：OsDT11 属于哪个蛋白家族？

选项：
A. CRP 家族  ← 正确答案
B. ABC 家族  ← 干扰项（似是而非）
C. GFP 家族  ← 干扰项（文中出现过 GFP 相关概念）
D. RFP 家族  ← 干扰项（RFP 是实验用的标记蛋白）
```

**核心逻辑**（伪代码）：

```python
class MultiChoiceGenerator:
    def __init__(self, num_of_questions=5):
        self.num_of_questions = num_of_questions
    
    def generate(nodes, edges):
        context = format_knowledge(nodes, edges)
        
        prompt = f"""
        基于以下内容生成 {num_of_questions} 道多项选择题：
        {context}
        
        要求：
        1. 每道题有且只有一个正确答案
        2. 干扰项要有一定迷惑性，但不能与原文矛盾
        3. 使用 A/B/C/D 标注选项
        4. 明确标注正确答案的字母
        
        输出格式：
        <qa_pair>
          <question>...</question>
          <options>A. ...\nB. ...\nC. ...\nD. ...</options>
          <answer>A</answer>
        </qa_pair>
        """
        
        response = llm.generate(prompt)
        return parse_mcqs(response)  # 解析选项和正确答案
```

---

#### 3.4.7 多答案 (Multi-answer)

**原理**：类似多项选择，但允许多个正确答案。适用于"以下哪些是正确的"这类问题。

```
问题：关于 OsDT11 的以下说法，哪些是正确的？

选项：
A. 属于 CRP 家族
B. 定位于细胞核  ← 错误
C. 是分泌蛋白    ← 正确
D. 具有 RFP 信号 ← 正确（实验中观察到的）

正确答案：A, C, D
```

---

#### 3.4.8 填空题 (Fill-in-blank)

**原理**：将关键术语或实体名替换为占位符，训练模型对核心概念的精确记忆。

```
原始文本：OsDT11 是一种感温型常规稻品种，属于 CRP 家族。

填空题：_______ 是一种感温型常规稻品种，属于 CRP 家族。
答案：OsDT11
```

**核心逻辑**（伪代码）：

```python
class FillInBlankGenerator:
    def generate(nodes, edges):
        context = format_knowledge(nodes, edges)
        
        prompt = f"""
        基于以下内容生成填空题：
        {context}
        
        要求：
        1. 选择关键术语、实体名或重要概念进行掩码
        2. 用 { } 或 ___ 表示填空位置
        3. 确保答案唯一且能从上下文中推断
        
        输出格式：
        <qa_pair>
          <question>_____ 是一种感温型常规稻品种</question>
          <answer>OsDT11</answer>
        </qa_pair>
        """
        
        response = llm.generate(prompt)
        return parse_fill_in_blank(response)
```

---

#### 3.4.9 掩码填空 (Masked Fill-in-blank)

**原理**：专用于 RLVR（可验证奖励强化学习）。从知识图谱中随机选择一个实体，在其描述文本中将其名称掩码。这种方式生成的数据答案确定、可验证。

```
输入三元组：[OsDT11] --属于--> [CRP家族] --特征--> [分泌蛋白]

步骤：
1. 重写为连贯文本：
   "OsDT11 属于 CRP 家族，该家族成员是分泌蛋白。"

2. 随机选择掩码目标（假设选中 OsDT11）：
   "_____ 属于 CRP 家族，该家族成员是分泌蛋白。"

3. 答案：OsDT11
```

**核心逻辑**（伪代码）：

```python
class MaskedFillInBlankGenerator:
    def generate(nodes, edges):
        # 步骤1：重写为连贯文本
        text = rephrase_to_text(nodes, edges)
        
        # 步骤2：随机选择一个节点进行掩码
        target_node = random.choice(nodes)
        target_name = target_node.name
        
        # 步骤3：在文本中替换目标名称
        if target_name in text:
            masked_text = text.replace(target_name, "{ }")
            return {
                "question": masked_text,
                "answer": target_name
            }
        else:
            return None  # 掩码失败，舍弃
```

---

#### 3.4.10 判断题 (True/False)

**原理**：生成陈述句并标注其真假。可基于知识图谱生成真实陈述，也可通过轻微篡改生成虚假陈述。

```
真实陈述（True）：
  "OsDT11 属于 CRP 家族。"

虚假陈述（False）：
  "OsDT11 定位于细胞核。" （实际是细胞壁）
```

**核心逻辑**（伪代码）：

```python
class TrueFalseGenerator:
    def generate(nodes, edges):
        context = format_knowledge(nodes, edges)
        
        prompt = f"""
        基于以下内容生成判断题：
        {context}
        
        要求：
        1. 一半题目为真，一半为假
        2. 假陈述应通过轻微修改真陈述得到（如替换关键实体）
        3. 明确标注 True 或 False
        
        输出格式：
        <qa_pair>
          <question>OsDT11 属于 CRP 家族。</question>
          <answer>True</answer>
        </qa_pair>
        """
        
        response = llm.generate(prompt)
        return parse_tf_questions(response)
```

---

#### 3.4.11 数据类型的选择策略

不同数据类型适用于不同的训练阶段和目标：

|训练阶段|推荐数据类型|配套分区策略|理由|
|:---------|:-------------|:-------------|:-----|
|**基础学习**|Atomic + Fill-in-blank|无需分区 / BFS|巩固核心概念|
|**推理能力**|Multi-hop + CoT|Triple / Leiden|培养逻辑思维|
|**综合能力**|Aggregated|BFS / ECE|提升整合能力|
|**评测验证**|Multi-choice + True/False|BFS / ECE|便于自动评分|
|**RLVR**|Masked Fill-in-blank|Quintuple|答案可验证|
|**多模态**|VQA|AnchorBFS / ECE|视觉+语言联合训练|

**分区策略与数据类型的匹配逻辑**：

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     分区策略 → 数据类型 映射关系                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  BFS/ECE 分区      ┌─────────────────────────────────────────────────┐ │
│  (紧凑社区)        │  聚合问答(Aggregated)                            │ │
│  社区特点：        │  • 多实体密集关联                                │ │
│  直径小、密度高    │  • 适合综合理解类问题                            │ │
│                    │  • 推荐：max_units=10~20                        │ │
│                    └─────────────────────────────────────────────────┘ │
│                                                                         │
│  Triple 分区       ┌─────────────────────────────────────────────────┐ │
│  (固定三元组)      │  多跳推理(Multi-hop)                             │ │
│  社区特点：        │  • 2节点+1边的精确结构                           │ │
│  结构严格固定      │  • 天然适合双实体关系推理                        │ │
│                    │  • 答案需跨越这条边推导                          │ │
│                    └─────────────────────────────────────────────────┘ │
│                                                                         │
│  Quintuple 分区    ┌─────────────────────────────────────────────────┐ │
│  (固定五元组)      │  掩码填空(Masked Fill-in-blank)                  │ │
│  社区特点：        │  • 3节点+2边的路径结构                           │ │
│  两跳路径          │  • 可在中间节点/边上设计掩码                     │ │
│                    │  • 答案确定性高，适合RLVR                        │ │
│                    └─────────────────────────────────────────────────┘ │
│                                                                         │
│  Leiden 分区       ┌─────────────────────────────────────────────────┐ │
│  (自然社区)        │  思维链(CoT)                                     │ │
│  社区特点：        │  • 内部高度关联的实体组                          │ │
│  高内聚、模块化    │  • 适合构建复杂推理步骤                          │ │
│                    │  • 社区边界自然，减少噪声                        │ │
│                    └─────────────────────────────────────────────────┘ │
│                                                                         │
│  AnchorBFS 分区    ┌─────────────────────────────────────────────────┐ │
│  (锚定扩展)        │  视觉问答(VQA)                                   │ │
│  社区特点：        │  • 以图像节点为中心                              │ │
│  以图像/关键实体   │  • 向外扩展相关文本知识                          │ │
│  为中心            │  • 确保图文关联性                                │ │
│                    └─────────────────────────────────────────────────┘ │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 3.5 数据评估与质量控制

GraphGen 内置了多维度的数据评估体系，确保生成的合成数据质量可靠。

#### 3.5.1 QA 对质量评估

**UniEval 多维度评估**：

```python
class UniEvaluator:
    """基于 UniEval 模型的 QA 质量评估"""
    
    def evaluate(qa_pair) -> dict:
        dimensions = ["naturalness", "coherence", "understandability"]
        results = {}
        
        for dim in dimensions:
            # 构建 Yes/No 评估提示
            prompt = build_prompt(dim, qa_pair.question, qa_pair.answer)
            
            # 计算 "Yes" 的概率作为该维度得分
            probs = model.get_yes_no_probs(prompt)
            score = probs["yes"] / (probs["yes"] + probs["no"])
            results[dim] = score
        
        return results
        # 输出示例：{"naturalness": 0.85, "coherence": 0.92, "understandability": 0.88}
```

**评估维度说明**：

| 维度 | 评估内容 | 应用场景 |
|:-----|:---------|:---------|
| **Naturalness** | 回答是否自然流畅 | 过滤机器腔调重的数据 |
| **Coherence** | 问答是否语义一致 | 过滤答非所问的数据 |
| **Understandability** | 内容是否易于理解 | 控制难度分布 |

---

#### 3.5.2 知识图谱结构评估

**结构鲁棒性评估**：

```python
class StructureEvaluator:
    """评估知识图谱的结构性指标"""
    
    def evaluate(kg) -> dict:
        # 基础统计
        total_nodes = kg.get_node_count()
        total_edges = kg.get_edge_count()
        
        # 噪声比：孤立节点占比
        isolated = count_isolated_nodes(kg)
        noise_ratio = isolated / total_nodes
        
        # 最大连通分量占比
        components = kg.get_connected_components()
        largest_cc = max(len(c) for c in components)
        cc_ratio = largest_cc / total_nodes
        
        # 平均度数
        avg_degree = sum(kg.get_all_node_degrees().values()) / total_nodes
        
        # 幂律分布拟合（检测是否符合真实图谱特征）
        powerlaw_r2 = fit_powerlaw(kg.get_degree_distribution())
        
        return {
            "total_nodes": total_nodes,
            "total_edges": total_edges,
            "noise_ratio": noise_ratio,
            "largest_cc_ratio": cc_ratio,
            "avg_degree": avg_degree,
            "powerlaw_r2": powerlaw_r2,
            "is_robust": check_robustness(noise_ratio, cc_ratio, avg_degree)
        }
```

**结构健康度指标**：

| 指标 | 健康阈值 | 异常说明 |
|:-----|:---------|:---------|
| **Noise Ratio** | < 15% | 孤立节点过多，抽取质量差 |
| **Largest CC Ratio** | > 90% | 图过于碎片化，连通性差 |
| **Average Degree** | 2.0 ~ 5.0 | 过于稀疏或稠密都不理想 |
| **Power Law R²** | > 0.75 | 不符合幂律分布，可能非自然图谱 |

---

#### 3.5.3 数据过滤流水线

```
┌─────────────────────────────────────────────────────────────────┐
│                     数据过滤流水线                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐ │
│  │ 长度过滤  │───>│ 质量评估  │───>│ 阈值过滤  │───>│ 去重过滤  │ │
│  │(Length)  │    │(Quality) │    │(Range)   │    │(Deduplicate)│
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘ │
│       │               │               │               │         │
│       ▼               ▼               ▼               ▼         │
│   过滤过长/过短   计算多维得分    按分数范围筛选   基于语义去重   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**过滤配置示例**：

```yaml
nodes:
  - id: filter
    op_name: filter
    type: filter
    dependencies: [generate]
    params:
      method: range
      method_params:
        metric: "coherence"      # 基于连贯性评分
        min_val: 0.7             # 最低阈值
        max_val: 1.0             # 最高阈值
        left_inclusive: true
```

---

### 3.6 风格控制重述 (Style-Controlled Rephrasing)

除了基于知识图谱生成数据，GraphGen 还支持对现有文本进行风格化的重述改写，用于数据增强。

#### 3.6.1 应用场景

| 场景 | 目的 | 示例 |
|:-----|:-----|:-----|
| **预训练数据增强** | 提升 token 效用 | 同一内容多种表达 |
| **领域迁移** | 跨领域风格适配 | 学术论文 → 科普文章 |
| **难度控制** | 调整文本复杂度 | 专业术语 → 通俗解释 |

#### 3.6.2 重述流程

```
原始文本 ──> 风格选择 ──> LLM 重述 ──> 质量验证 ──> 输出文本
                │
                ├─> 执行摘要风格
                ├─> 批判分析风格
                ├─> 跨领域改写风格
                └─> 简化解释风格
```

**核心逻辑**（伪代码）：

```python
class StyleControlledRephraser:
    def __init__(self, llm_client, style="critical_analysis"):
        self.llm = llm_client
        self.style = style
        
        # 预定义风格模板
        self.style_prompts = {
            "executive_summary": "将以下内容改写为执行摘要风格...",
            "critical_analysis": "以批判性分析的视角重述以下内容...",
            "cross_domain": "将专业内容改写为科普风格...",
            "simplified": "用更简洁易懂的语言表达以下内容..."
        }
    
    def rephrase(self, text: str) -> dict:
        # 检测语言
        language = detect_language(text)
        
        # 选择对应风格的 Prompt 模板
        prompt_template = self.style_prompts[self.style][language]
        prompt = prompt_template.format(text=text)
        
        # 生成重述文本
        rephrased = self.llm.generate(prompt)
        
        return {"content": rephrased, "original": text, "style": self.style}
```

#### 3.6.3 实验效果

在 SlimPajama-6B 预训练语料上的实验（基于 Qwen3-0.6B）：

| 重述策略 | ARC-E | ARC-C | HellaSwag | Average |
|:---------|:------|:------|:----------|:--------|
| 基线 (2 epochs) | 25.55 | 21.08 | 24.48 | 24.24 |
| **执行摘要重述** (1 epoch) | 26.43 | **22.70** | **24.75** | **25.56** (↑1.32) |
| **跨领域重述** (1 epoch) | **28.79** | 20.22 | 24.46 | 25.14 (↑0.90) |

**关键发现**：
- 重述数据只需 1 个 epoch 即可超过原始数据 2 个 epoch 的效果
- 零额外数据，所有提升来自**表达多样性**
- 跨领域重述在 ARC-E 上提升显著（+3.24）

---

### 3.7 外部知识搜索与扩展

GraphGen 支持从外部专业知识库搜索补充信息，扩展知识图谱的覆盖面。

#### 3.7.1 支持的数据源

| 数据源 | 类型 | 适用领域 | 内容特点 |
|:-------|:-----|:---------|:---------|
| **UniProt** | 蛋白质数据库 | 生物信息学 | 蛋白质序列、功能、定位 |
| **NCBI** | 综合数据库 | 生物医学 | DNA/RNA/蛋白质序列 |
| **RNAcentral** | RNA 数据库 | 转录组学 | 非编码 RNA 信息 |
| **InterPro** | 蛋白家族库 | 蛋白质组学 | 蛋白结构域、家族分类 |

#### 3.7.2 搜索流程

```
┌─────────────────────────────────────────────────────────────────┐
│                    外部知识搜索流程                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   种子文本 (如 "OsDT11")                                         │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────────────┐                                           │
│   │   构建搜索查询   │  "OsDT11 protein function subcellular"      │
│   └─────────────────┘                                           │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────────────┐    ┌─────────────────┐                   │
│   │  UniProt 搜索   │───>│  返回结构化数据  │                   │
│   │  NCBI 搜索      │    │  - 序列信息      │                   │
│   │  RNAcentral 搜索│    │  - 功能描述      │                   │
│   └─────────────────┘    │  - 参考文献      │                   │
│                          └─────────────────┘                   │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────────────┐                                           │
│   │  整合到知识图谱  │  添加实体、属性、关系                         │
│   └─────────────────┘                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**核心逻辑**（伪代码）：

```python
class SearchService:
    def __init__(self, data_source):
        self.data_source = data_source
        self.searcher = self._init_searcher()
    
    def _init_searcher(self):
        if self.data_source == "uniprot":
            return UniProtSearch()
        elif self.data_source == "ncbi":
            return NCBISearch()
        elif self.data_source == "rnacentral":
            return RNACentralSearch()
        # ...
    
    def process(self, batch: list) -> list:
        results = []
        for item in batch:
            query = item["content"]
            
            # 执行外部搜索
            search_result = self.searcher.search(query)
            
            if search_result:
                # 添加元数据
                search_result["data_source"] = self.data_source
                search_result["query"] = query
                results.append(search_result)
        
        return results

# UniProt 搜索示例
class UniProtSearch:
    def search(self, query: str) -> dict:
        # 调用 UniProt REST API
        response = requests.get(
            f"https://rest.uniprot.org/uniprotkb/search?query={query}"
        )
        data = response.json()
        
        return {
            "protein_name": data["proteinDescription"]["recommendedName"]["fullName"],
            "sequence": data["sequence"]["sequence"],
            "organism": data["organism"]["scientificName"],
            "functions": [c["text"] for c in data["comments"] if c["commentType"] == "FUNCTION"],
            "subcellular_locations": extract_locations(data)
        }
```

#### 3.7.3 配置示例

```yaml
nodes:
  - id: search_uniprot
    op_name: search
    type: map_batch
    dependencies: [extract_keywords]
    params:
      data_source: uniprot
      uniprot_params:
        fields: ["protein_name", "function", "subcellular_location"]
        reviewed: true  # 只搜索已审核条目

  - id: merge_kg
    op_name: build_kg
    type: map_batch
    dependencies: [search_uniprot, local_documents]
    # 合并外部搜索结果和本地文档构建知识图谱
```

#### 3.7.4 应用价值

| 应用场景 | 价值 |
|:---------|:-----|
| **垂直领域增强** | 补充专业数据库的结构化知识 |
| **知识验证** | 与权威数据库交叉验证实体信息 |
| **实体链接** | 将文本中的实体链接到标准数据库 ID |
| **属性扩充** | 获取实体的额外属性（序列、位置、功能等） |

---

## 4. 技术实现细节

### 4.1 分布式执行引擎

GraphGen 基于 **Ray** 构建分布式执行引擎，支持水平扩展和 GPU 加速。

**执行流程**（伪代码）：

```python
class Engine:
    def __init__(self, config):
        # 初始化 Ray 集群
        ray.init(include_dashboard=True)
        
        # 初始化 LLM Actors（常驻内存，避免重复加载）
        self.llm_actors = {
            "synthesizer": init_llm_actor("synthesizer"),
            "trainee": init_llm_actor("trainee")
        }
        
        # 初始化存储 Actors
        self.storage_actors = {}
        for node_id in config.storage_nodes:
            self.storage_actors[f"kv_{node_id}"] = init_kv_storage(node_id)
            self.storage_actors[f"graph_{node_id}"] = init_graph_storage(node_id)
    
    def execute(self, config):
        # 1. 拓扑排序解析依赖
        sorted_nodes = topo_sort(config.nodes)
        
        for node in sorted_nodes:
            # 2. 获取输入数据
            input_ds = get_input_dataset(node.dependencies)
            
            # 3. 根据节点类型选择执行策略
            if node.type == "source":
                result = load_from_source(node.params)
            
            elif node.type == "aggregate":
                # 聚合操作：单 Actor，全量数据
                result = input_ds.repartition(1).map_batches(
                    node.operator,
                    compute=ActorPoolStrategy(min=1, max=1)
                )
            
            else:  # map / map_batch / filter
                # 并行操作：多 Actor 并发
                result = input_ds.map_batches(
                    node.operator,
                    compute=ActorPoolStrategy(
                        min_size=1, 
                        max_size=node.replicas
                    ),
                    batch_size=node.batch_size,
                    num_gpus=node.gpu_count
                )
            
            # 4. 保存中间结果（可选）
            if node.save_output:
                result.write_json(f"{output_dir}/{node.id}")
            
            self.datasets[node.id] = result
        
        return self.datasets
```

**技术要点**：

- **Actor Pool 策略**：动态扩缩容，支持 GPU 资源分配

- **拓扑排序**：通过 Kahn 算法解析配置依赖关系

- **惰性求值**：Ray Data 的延迟执行优化内存使用

### 4.2 存储系统设计

GraphGen 采用**双存储架构**：图存储用于知识图谱的拓扑关系，KV 存储用于元数据和中间结果。

#### 4.2.1 图存储抽象

**核心接口**（伪代码）：

```python
class BaseGraphStorage:
    # 数据操作
    def upsert_node(node_id, node_data): ...
    def upsert_edge(src_id, tgt_id, edge_data): ...
    def get_node(node_id) -> dict: ...
    def get_edge(src_id, tgt_id) -> dict: ...
    
    # 拓扑查询
    def get_neighbors(node_id) -> List[str]: ...
    def get_all_nodes() -> List[(id, data)]: ...
    def get_all_edges() -> List[(src, dst, data)]: ...
    
    # 图分析
    def get_connected_components() -> List[Set[str]]: ...
    def get_node_degrees() -> Dict[str, int]: ...

# 实现1：KuzuDB（生产环境）
class KuzuStorage(BaseGraphStorage):
    def __init__(self, working_dir):
        self.db = kuzu.Database(f"{working_dir}/graph.db")
        self.conn = kuzu.Connection(self.db)
        self._init_schema()
    
    def upsert_node(self, node_id, node_data):
        # Kuzu 使用 JSON 存储动态属性
        json_data = json.dumps(node_data)
        self.conn.execute(
            "MERGE (n:Entity {id: $id}) SET n.data = $data",
            {"id": node_id, "data": json_data}
        )

# 实现2：NetworkX（实验环境）
class NetworkXStorage(BaseGraphStorage):
    def __init__(self):
        self.graph = nx.DiGraph()
```

**后端对比**：

|特性|KuzuDB|NetworkX|
|-|-|-|
|适用规模|大规模生产|小规模实验|
|查询语言|Cypher|Python API|
|持久化|原生支持|需手动序列化|
|性能|高|低|

#### 4.2.2 KV 存储抽象

**核心接口**（伪代码）：

```python
class BaseKVStorage:
    def upsert(data: Dict[str, Any]): ...
    def get_by_id(id: str) -> Any: ...
    def get_by_ids(ids: List[str]) -> List[Any]: ...
    def filter_keys(keys: List[str]) -> Set[str]: ...

# 实现1：RocksDB（生产环境）
class RocksDBStorage(BaseKVStorage):
    def __init__(self, working_dir, namespace):
        self.db = Rdict(f"{working_dir}/{namespace}.db")
    
    def upsert(self, data):
        for key, value in data.items():
            if key not in self.db:  # 去重写入
                self.db[key] = value
    
    def get_by_ids(self, ids):
        return [self.db.get(id) for id in ids]

# 实现2：JSON KV（轻量级）
class JsonKVStorage(BaseKVStorage):
    def __init__(self, working_dir, namespace):
        self.file_path = f"{working_dir}/{namespace}.json"
        self.data = load_json(self.file_path)
```

### 4.3 LLM 客户端设计

支持多种 LLM 推理后端：

|后端类型|适用场景|特点|
|-|-|-|
|`openai_api`|商业 API|GPT-4, Claude 等|
|`huggingface`|本地推理|Transformers 库|
|`vllm`|高吞吐本地推理|PagedAttention 优化|
|`sglang`|结构化生成|支持正则约束|
|`ollama`|本地快速部署|简化模型管理|

**关键设计**：

- 统一接口 `BaseLLMWrapper` 屏蔽后端差异

- 支持 `generate_topk_per_token` 获取概率分布用于 ECE 计算

### 4.4 Prompt 工程

GraphGen 的 Prompt 设计遵循以下原则：

1. **结构化输出**：使用 XML 标签（`<question>`、`<answer>`）确保可解析

2. **少样本学习**：每个任务提供 2+ 个示例

3. **多语言支持**：中英文独立模板

4. **迭代精化**：支持多轮抽取提升召回率

**知识抽取 Prompt 结构**：

```
-Goal-
明确任务目标

-Steps-
1. 识别实体
2. 识别关系
3. 提取关键词
4. 格式化输出

-Examples-
示例 1...
示例 2...

-Real Data-
实际输入...
```

---

## 5\. 配置与使用

### 5.1 配置文件结构

```yaml
global_params:
  working_dir: cache                    # 工作目录
  graph_backend: kuzu                   # 图存储后端
  kv_backend: rocksdb                   # KV存储后端

nodes:
  - id: read_files                      # 节点唯一标识
    op_name: read                       # 算子名称
    type: source                        # 节点类型
    dependencies: []                    # 依赖节点
    params:                             # 算子参数
      input_path: [...]

  - id: build_kg
    op_name: build_kg
    type: map_batch
    dependencies: [chunk_documents]
    execution_params:                   # 执行参数
      replicas: 1                       # Actor 副本数
      batch_size: 128

  - id: partition
    op_name: partition
    type: aggregate                     # 聚合类型
    dependencies: [judge]
    params:
      method: ece
      method_params:
        unit_sampling: max_loss         # 优先高损失单元
```

### 5.2 节点类型说明

|类型|说明|适用场景|
|-|-|-|
|`source`|数据源节点|文件读取、数据库读取|
|`map`|逐条处理|简单转换|
|`map_batch`|批量处理|LLM 调用（提高效率）|
|`filter`|过滤|数据清洗|
|`flatmap`|一对多展开|一个输入生成多个输出|
|`aggregate`|全量聚合|需要全局信息的操作（如分区）|

---

## 6\. 应用场景

### 6.1 预训练数据增强

GraphGen 支持对预训练语料进行改写（Rephrase），增加数据多样性：

|改写策略|效果|
|-|-|
|Executive-Summary Rephrase|提取执行摘要并改写|
|Cross-Domain Rephrase|跨领域风格迁移|

实验表明：SlimPajama-6B 语料经过改写后，在 ARC、HellaSwag 等基准上平均提升 1+ 分。

### 6.2 监督微调 (SFT)

在 SeedBench（植物学）数据集上，使用 50%+ GraphGen 生成的数据：

|数据集|GraphGen|Qwen2.5-7B 基线|
|-|-|-|
|SeedBench|**65.9**|51.5|
|GPQA-Diamond|**40.0**|33.3|
|AIME24|**20.6**|16.7|
|AIME25|**22.7**|7.2|

### 6.3 强化学习 (RLVR)

GraphGen 可生成可验证的问答数据，支持 RLVR（Reinforcement Learning with Verifiable Rewards）：

|领域|数据集|GraphGen+RLVR|Qwen2.5-7B 基线|
|-|-|-|-|
|植物|SeedBench|**66.8**|51.5|
|法律|LawBench|**55.2**|54.76|
|医学|MedQA|**87.1**|80.7|

---

## 7\. 扩展开发

### 7.1 自定义算子

算子是 GraphGen 流水线中的基本处理单元。要实现自定义算子，需继承 `BaseOperator`：

```python
from graphgen.bases import BaseOperator

class MyCustomOperator(BaseOperator):
    def __init__(self, working_dir, custom_param, **kwargs):
        super().__init__(working_dir, op_name="my_op")
        self.custom_param = custom_param
    
    def process(self, batch: list) -> Tuple[list, dict]:
        """
        处理批次数据
        
        Returns:
            results: 处理后的结果列表
            meta_updates: 血缘追踪信息 {input_trace_id: [output_trace_ids]}
        """
        results = []
        meta_updates = {}
        
        for item in batch:
            # 1. 业务处理逻辑
            processed = self.transform(item)
            
            # 2. 生成追踪 ID（用于数据血缘）
            processed["_trace_id"] = self.get_trace_id(processed)
            
            results.append(processed)
            
            # 3. 记录血缘关系
            input_id = item["_trace_id"]
            output_id = processed["_trace_id"]
            meta_updates.setdefault(input_id, []).append(output_id)
        
        return results, meta_updates
    
    def transform(self, item):
        # 具体业务逻辑
        return {"output": item["input"] * self.custom_param}
```

**注册使用**：

```yaml
nodes:
  - id: my_custom_step
    op_name: my_custom_op  # 算子名称
    type: map_batch
    dependencies: [previous_step]
    params:
      custom_param: 42
```

---

### 7.2 自定义生成器

生成器是数据合成的核心组件。自定义生成器需继承 `BaseGenerator`：

```python
from graphgen.bases import BaseGenerator

class MyGenerator(BaseGenerator):
    def __init__(self, llm_client, num_questions=5):
        super().__init__(llm_client)
        self.num_questions = num_questions
    
    def build_prompt(self, nodes, edges) -> str:
        """
        构建 LLM Prompt
        
        Args:
            nodes: [(node_id, node_data), ...]
            edges: [(src_id, dst_id, edge_data), ...]
        """
        context = format_knowledge(nodes, edges)
        
        return f"""
        基于以下知识生成 {self.num_questions} 道问答：
        {context}
        
        要求：
        1. 问题要有深度
        2. 答案要准确
        
        输出格式：
        <question>问题内容</question>
        <answer>答案内容</answer>
        """
    
    def parse_response(self, response: str) -> list[dict]:
        """
        解析 LLM 输出，提取结构化数据
        
        Returns:
            [{"question": ..., "answer": ...}, ...]
        """
        qa_pairs = []
        
        # 使用正则提取 XML 标签内容
        pattern = r"<question>(.*?)</question>.*?"<answer>(.*?)</answer>"
        matches = re.findall(pattern, response, re.DOTALL)
        
        for q, a in matches:
            qa_pairs.append({
                "question": q.strip(),
                "answer": a.strip()
            })
        
        return qa_pairs
    
    async def generate(self, batch) -> list[dict]:
        """
        主生成逻辑（基类已实现，通常无需重写）
        """
        nodes, edges = batch
        prompt = self.build_prompt(nodes, edges)
        response = await self.llm_client.generate_answer(prompt)
        return self.parse_response(response)
```

---

## 8\. 总结

GraphGen 通过知识图谱驱动的数据生成范式，解决了传统合成数据方法的两大痛点：

1. **知识覆盖不全面**：通过 ECE 机制识别模型知识缺口，优先针对薄弱环节生成数据

2. **数据多样性不足**：基于图谱的多跳采样和风格控制生成，确保数据分布合理

其技术亮点包括：

- 迭代式知识抽取提升召回率

- 双模型架构（Synthesizer + Trainee）实现知识缺口量化

- 基于 Ray 的分布式流水线支持大规模数据生成

- 模块化设计支持灵活扩展

---

## 参考

- **论文**: [GraphGen: Enhancing Supervised Fine-Tuning for LLMs with Knowledge-Driven Synthetic Data Generation](https://arxiv.org/abs/2505.20416)

- **代码**: https://github.com/open-sciencelab/GraphGen

- **文档**: https://chenzihong.gitbook.io/graphgen-cookbook/