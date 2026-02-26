# 第九章：检索增强生成 (RAG)

## 本章小结

本章全面剖析了检索增强生成（Retrieval-Augmented Generation, RAG）的原理及其在提示词工程中的具体实现。RAG 架构通过外部知识库有效弥补了大语言模型知识的时效性缺陷、领域局限性以及固有的幻觉问题。针对 RAG 的提示词设计需要特别强调资料引用的严格性。

### 关键概念

- **RAG (检索增强生成)**：结合信息检索和文本生成，利用检索到的实时、私有数据作为上下文增强生成的技术。
- **上下文拼接**：将检索结果（Chunks）与用户原问题融合成一个完整的提示词的过程。
- **引用出处 (Citation)**：生成最终回答时，附带原文来源标记，增强可信度和追溯性。
- **闭卷测试限制**：一种提示词技术，严令模型"仅使用给定的资料回答问题"，禁止利用先天预训练知识。

### 核心要点

1. **RAG 基础原理与工作流**
   - **切分与向量化 (Indexing)**：将长文档切分为短块 (Chunks) 并转为向量。
   - **检索 (Retrieval)**：基于用户提问，使用余弦相似度、BM25或混合搜索找到相关块。
   - **生成 (Generation)**：拼接检索块和问题，编写防御性提示词进行加工生成。

2. **RAG 提示词设计四大法则**
   - **来源隔离**：使用 XML 或特定分隔符清晰划定"资料区"与"指令区"。
   - **严格引用**：指令要求不仅回答问题，而且每句话必须附带对应 Chunk 的引用 ID。
   - **应对信息不足**：提供标准逃生通道，声明"如果提供的资料不足以回答，说你不知道，禁止脑补"。
   - **处理冲突**：指导模型在不同资料存在矛盾时，指出矛盾点而非简单盲从最新或最长的资料。

3. **检索增强的高级架构 (Advanced RAG)**
   - **查询重写 (Query Rewriting)**：使用 LLM 先将用户口语化的提问改写为更利于向量匹配的标准检索词。
   - **多步检索 / 路由 (Routing)**：根据问题类型分发给不通的索引库进行查询。
   - **重排序 (Reranking)**：先召回大批量结果，再利用 Cross-Encoder 或 LLM 进行相关性深度打分和排序。

4. **从评估到调优**
   - 使用 RAGAS 或 TruLens 等框架，从上下文相关度、答案相关度、事实一致性三个维度进行评测。
   - 根据评估结果，动态调优 Chunk 大小、检索 `Top-K` 数量和提示词约束力度。

### 实践检查清单

- [ ] 上下文中提供的检索结果是否使用了清晰的分隔符加以隔离？
- [ ] 提示词中是否明确限定了模型仅能使用所提供的资料？
- [ ] 测试过"故意不提供相关资料"时，模型是否能诚实拒绝回答？
- [ ] 是否指导模型在答案中加入文档索引标号以便追溯？

### 延伸阅读

#### 9.1 RAG 原理与架构
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) - RAG 的重要开山之作
- [LangChain RAG Documentation](https://python.langchain.com/docs/use_cases/question_answering/) - 标准 RAG 实现指南

#### 9.2 提示词与重排高级技巧
- [Advanced RAG Techniques](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/) - LlamaIndex 提供的高阶 RAG 策略
- [Anthropic Embeddings and RAG](https://docs.anthropic.com/en/docs/build-with-claude/embeddings) - Claude 相关的 RAG 参考资料

#### 9.3 评测框架
- [RAGAS: Automated Evaluation of RAG](https://github.com/explodinggradients/ragas) - RAG 自动化评分框架

### 下一章预告

在接下来的[第十章](../10_multimodal/README.md)中，我们将把视野从纯文本拓展到更广阔的维度，学习如何编写和优化处理图像、图表甚至是音视频的多模态提示词。

---

[下一章：多模态提示工程 →](../10_multimodal/README.md)
