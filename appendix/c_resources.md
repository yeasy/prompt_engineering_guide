# 附录C：资源与工具推荐

本附录推荐学习提示词工程的优质资源和实用工具。

## C.1 官方文档

### OpenAI

**Prompt Engineering Guide**  
https://platform.openai.com/docs/guides/prompt-engineering  
OpenAI官方提示词工程指南，包含最佳实践和技巧。

**GPT Best Practices**  
https://platform.openai.com/docs/guides/gpt-best-practices  
GPT系列模型的使用最佳实践。

### Anthropic

**Claude Prompt Engineering**  
https://docs.anthropic.com/claude/docs/prompt-engineering  
Claude官方提示词设计指南，特别介绍XML标签和预填充技术。

**Claude Prompt Library**  
https://docs.anthropic.com/claude/page/prompts  
官方提供的提示词示例库。

### Google

**Gemini Prompting Guide**  
https://ai.google.dev/docs/prompting_intro  
Gemini模型的提示词设计指南。

## C.2 学习资源

### 在线课程

**DeepLearning.AI - ChatGPT Prompt Engineering for Developers**  
由OpenAI和DeepLearning.AI联合推出的免费课程。

**Prompt Engineering Guide (DAIR.AI)**  
https://www.promptingguide.ai/  
全面的提示词工程学习指南，涵盖各种技术。

### 论文与研究

**[Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)**  
Wei et al., 2022 - 思维链提示的开创性论文。

**[ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629)**  
Yao et al., 2022 - ReAct框架论文。

**[Tree of Thoughts](https://arxiv.org/abs/2305.10601)**  
Yao et al., 2023 - 思维树推理策略。

**[Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171)**  
Wang et al., 2022 - 自一致性方法论文。

**[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)**  
Lewis et al., 2020 - RAG 原始论文。

**[A Systematic Survey of Prompt Engineering in Large Language Models](https://arxiv.org/abs/2402.07927)**  
Mizrahi et al., 2024 - 全面的提示词工程技术综述，涵盖分类体系和应用领域。

**[Unleashing the Potential of Prompt Engineering for Large Language Models](https://arxiv.org/abs/2310.14735)**  
Comprehensive review (2023) covering foundational and advanced techniques, VLM prompting, security, and evaluation.

**[The Prompt Report: A Systematic Survey of Prompt Engineering Techniques](https://arxiv.org/abs/2406.06608)**  
白等 et al., 2024 - 迄今最全面的提示词工程综述：58种LLM技术、40种多模态技术、33个标准术语。

### 博客与社区

**Lil'Log (Lilian Weng)**  
https://lilianweng.github.io/  
OpenAI研究员的技术博客，深入浅出。

**Reddit - r/PromptEngineering**  
提示词工程社区，经验分享和讨论。

**Discord - LangChain**  
LangChain官方Discord，活跃的开发者社区。

## C.3 开发工具

### 框架与库

**LangChain**  
https://github.com/langchain-ai/langchain  
功能全面的LLM应用开发框架。

特点：
- 提示词模板管理
- 链式调用
- Agent构建
- 丰富的集成

**LlamaIndex**  
https://github.com/run-llama/llama_index  
专注于数据接入和RAG的框架。

特点：
- 多种数据源连接器
- 灵活的索引结构
- 查询引擎

**AutoGen**  
https://github.com/microsoft/autogen  
微软的多Agent协作框架。

特点：
- Agent对话协作
- 人机协作
- 代码执行

**CrewAI**  
https://github.com/joaomdmoura/crewAI  
轻量级的Agent团队协作框架。

### 提示词管理

**PromptLayer**  
https://promptlayer.com/  
提示词版本控制和监控平台。

功能：
- API调用日志
- 提示词版本管理
- 性能分析

**LangSmith**  
https://www.langchain.com/langsmith  
LangChain官方的调试和监控工具。

### 向量数据库

**Pinecone**  
托管的向量数据库服务。

**Weaviate**  
开源向量搜索引擎。

**Chroma**  
轻量级的嵌入式向量数据库。

**Qdrant**  
高性能的向量相似度搜索引擎。

## C.4 实用工具

### 提示词测试

**OpenAI Playground**  
https://platform.openai.com/playground  
OpenAI官方的交互式测试环境。

**Anthropic Console**  
https://console.anthropic.com/  
Claude的测试控制台。

### Token计算

**OpenAI Tokenizer**  
https://platform.openai.com/tokenizer  
可视化Token分词工具。

**tiktoken (Python库)**  
```python
import tiktoken
encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode("your text")
```

### 提示词优化

**PromptPerfect**  
https://promptperfect.jina.ai/  
AI驱动的提示词优化工具。

**Prompt Generator**  
各种在线的提示词生成器工具。

## C.5 数据集与Benchmark

**MMLU (Massive Multitask Language Understanding)**  
评估模型多任务理解能力的基准数据集。

**HumanEval**  
代码生成能力评估数据集。

**GSM8K**  
数学推理能力评估数据集。

**SuperGLUE**  
自然语言理解任务集合。

## C.6 持续学习

### 新闻与更新

**AI News Aggregators**
- https://www.aiweekly.co/
- https://www.deeplearning.ai/the-batch/

**Research Papers**
- arXiv.org (cs.CL, cs.AI)
- Papers with Code

### Twitter关注

- @OpenAI
- @AnthropicAI
- @GoogleAI
- @omarsar0 (DAIR.AI创始人)
- @lilianweng (OpenAI研究员)

### YouTube频道

- Andrej Karpathy
- Two Minute Papers
- AI Explained

## C.7 实践项目

### 开源项目学习

**awesome-chatgpt-prompts**  
https://github.com/f/awesome-chatgpt-prompts  
精选的ChatGPT提示词集合。

**LangChain Templates**  
https://github.com/langchain-ai/langchain/tree/master/templates  
LangChain官方模板项目。

### 竞赛与挑战

**Kaggle - LLM相关竞赛**  
实践提示词工程技能。

## 使用建议

1. **从官方文档开始**：打下扎实基础
2. **动手实践**：使用Playground测试想法
3. **参与社区**：学习他人经验
4. **关注前沿**：跟踪最新研究和技术
5. **构建项目**：在实际应用中深化理解

---

*注：链接和推荐基于2026年1月的信息，请访问时验证最新版本。*
