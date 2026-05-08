# Graphify 技术全景

> **仓库**: [safishamsi/graphify](https://github.com/safishamsi/graphify)  
> **Stars**: 44,798 | **Forks**: 4,864 | **Version**: 0.7.10  
> **License**: MIT | **Python**: >=3.10

## 领域定位

Graphify 属于**代码库知识图谱（Codebase Knowledge Graph）**工具，其核心目标是将软件项目的多模态资产（源代码、文档、图像、音频）统一建模为显式关系图谱，以支持结构化查询与语义检索。

在知识图谱应用谱系中，Graphify 位于以下交叉点：

- **纵向**：代码理解工具（静态分析、代码搜索）→ 知识图谱（关系建模）→ RAG 系统（检索增强生成）
- **横向**：单模态代码分析工具（如 Sourcegraph）↔ 多模态项目知识库（Graphify）

## 技术分类

| 工具/方法 | 模态支持 | 图谱构建方式 | 查询方式 | 与 Graphify 的关系 |
|---------|---------|-----------|---------|----------------|
| Sourcegraph | 代码 | 代码图（调用、引用） | 代码搜索 | 单模态先行者，无语义层 |
| GitHub Copilot Chat | 代码+注释 | 隐式（模型内部） | 自然语言问答 | 端到端生成，不可解释 |
| GraphRAG | 文档 | 文本知识抽取+社区检测 | 图遍历+生成 | 文本域的相似思路 |
| **Graphify** | **代码+文档+图像+音频+视频** | **结构化代码图+语义文档图+多模态关联** | **图遍历查询** | **多模态统一入图** |

### 支持的具体格式

| 类型 | 格式数量 | 代表性格式 |
|------|---------|-----------|
| 代码 | 23 种语言 | Python, JS/TS, Go, Rust, Java, C/C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Obj-C, Julia, Verilog, Fortran |
| 文档 | 5 种 | Markdown, HTML, YAML, RST, TXT |
| Office | 2 种 | DOCX, XLSX |
| 论文 | 1 种 | PDF |
| 图像 | 4 种 | PNG, JPG, WebP, GIF |
| 视频 | 多平台 | YouTube/本地视频 (faster-whisper 转录) |
| SQL | 数据库 | 表、视图、函数、外键、FROM/JOIN 关系 |

## 能力边界

### 能做什么

- 将 **23 种编程语言**的代码解析为 AST 级别的结构化图谱（本地完成，隐私安全）
- 融合 PDF、Markdown 等文档的语义信息
- 关联图像、视频、音频等非文本资产与代码实体
- 通过 **Leiden 算法**自动识别模块社区，生成**交互式可视化**（vis.js）
- 预构建图谱后，后续查询无需重复读取原始文件（Token 压缩）
- 增量更新支持：代码变更时无需全量重建
- 多平台集成：Claude Code、Codex、Cursor、Gemini CLI、VS Code（MCP）、Obsidian

### 不能做什么

- 不替代代码编辑器或 IDE 的导航功能（无实时跳转、重构）
- 不直接生成代码（无补全/生成功能，纯查询与分析）
- 不保证跨项目的知识融合（以单项目为边界）
- 不处理运行时行为（静态分析，无动态追踪）
- 非代码内容的语义提取仍需调用 LLM API（需自备密钥）

## 关键 Trade-off

| 维度 | 选择 | 代价 |
|-----|------|------|
| **Token 压缩** | 预构建图谱，查询时只读图结构 | 初始构建成本高；图谱需随代码更新而同步 |
| **本地优先** | 代码解析在本地，不上传 | 非代码内容的语义提取依赖本地 API 调用（仍需自己的密钥）|
| **结构化 vs 语义** | 代码用结构化图（AST），文档用语义图（嵌入） | 两种图模型的对齐与关联是技术难点 |
| **多模态统一** | 图像、音频入图 | 多模态特征提取的质量直接影响图谱可用性 |

## 技术栈详情

| 层级 | 组件 | 具体技术 |
|------|------|---------|
| 代码解析 | AST 提取 | tree-sitter (23 种语言 parser) |
| 图存储 | 内存图 | NetworkX (默认), 可选 Neo4j |
| 去重 | 相似检测 | datasketch (MinHash LSH) |
| 模糊匹配 | 字符串匹配 | rapidfuzz |
| 社区检测 | 聚类算法 | graspologic (Leiden) |
| 可视化 | 前端渲染 | vis.js |
| 视频处理 | 转录 | faster-whisper + yt-dlp |
| 语义提取 | LLM | Claude, GPT-4, Gemini 等 |

### 可选依赖

```bash
pip install graphifyy[all]       # 完整版
pip install graphifyy[mcp]       # MCP Server 支持
pip install graphifyy[neo4j]     # Neo4j 存储后端
pip install graphifyy[video]     # 视频转录
pip install graphifyy[sql]       # SQL 解析
pip install graphifyy[pdf]       # PDF 处理
pip install graphifyy[office]    # DOCX/XLSX
```

## 与知识图谱技术栈的关系

- **知识表示**：Graphify 使用属性图模型（Property Graph），非 RDF/OWL 语义网标准
- **知识构建**：代码侧基于 tree-sitter 的规则抽取（非学习式），文档侧依赖 LLM 语义提取
- **存储与查询**：生成静态 HTML 可视化（graph.html），非持久化图数据库
- **推理**：依赖图遍历（如社区检测）而非符号推理或神经推理
