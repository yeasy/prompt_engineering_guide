# 附录 C：资源、工具与参考文献

本附录汇总了全书中引用的重要论文、官方文档及业界优秀的开源实践库，同时推荐学习提示词工程的优质资源和实用工具，供读者进行更深入的拓展学习。

## C.1 官方指南与文档 (Official Guidelines)

### C.1.1 OpenAI
**Prompt Engineering Guide**
https://platform.openai.com/docs/guides/prompt-engineering
OpenAI官方提示词工程指南，包含最佳实践和技巧，非常务实。

**GPT Best Practices**
https://platform.openai.com/docs/guides/gpt-best-practices
GPT系列模型的使用最佳实践。

**OpenAI Cookbook**
https://cookbook.openai.com/
官方开源代码示例库。

### C.1.2 Anthropic
**Claude Prompt Engineering Interactive Tutorial**
https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
提供从基础到高级（尤其是 XML 标签约束）的详尽教程。

**Claude Prompt Library**
https://docs.anthropic.com/en/prompt-library/library
官方提供的提示词示例库。

### C.1.3 Google
**Gemini Prompting Guide**
https://ai.google.dev/gemini-api/docs/prompting-intro
Gemini模型的提示词设计指南，关注于长上下文和多模态输入的技巧。

## C.2 核心参考文献与研究论文 (Foundational Papers & Research)

### C.2.1 基础与综述类
**[Attention Is All You Need](https://arxiv.org/abs/1706.03762)**
Vaswani et al., 2017 - Transformer 架构奠基之作。

**[Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)**
Brown et al., 2020 - GPT-3 的发布论文，确立了大模型在不调参的情况下仅靠 Few-Shot 即可完成多种任务的范式。

**[A Systematic Survey of Prompt Engineering in Large Language Models](https://arxiv.org/abs/2402.07927)**
Mizrahi et al., 2024 - 全面的提示词工程技术综述，涵盖分类体系和应用领域。

**[Unleashing the Potential of Prompt Engineering for Large Language Models](https://arxiv.org/abs/2310.14735)**
Bang et al., 2023 - 一篇全面的提示词工程综述，涵盖基础和高级提示技术、多模态提示、安全性与评估机制。

**[The Prompt Report: A Systematic Survey of Prompt Engineering Techniques](https://arxiv.org/abs/2406.06608)**
Schulhoff et al., 2024 - 迄今最全面的提示词工程综述：58种LLM技术、40种多模态技术、33个标准术语。

### C.2.2 推理与思维链 (Reasoning & CoT)
**[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)**
Wei et al., 2022 - 谷歌大脑提出的 CoT，提示词工程领域最重要的里程碑之一。

**[Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171)**
Wang et al., 2022 - 提出多路径采样和多数投票的自一致性机制。

**[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)**
Yao et al., 2023 - 将 CoT 推进到树状结构搜索，适用于极高复杂度任务。

### C.2.3 工具调用与 智能体（agent） (ReAct & Agents)
**[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)**
Yao et al., 2022 - 提出了 Thought-Action-Observation 范式。

### C.2.4 自动化与评测 (Automated PE)
**[Large Language Models Are Human-Level Prompt Engineers](https://arxiv.org/abs/2211.01910)**
Zhou et al., 2022 - APE (Automatic Prompt Engineer) 论文。

### C.2.5 检索增强生成 (RAG)
**[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)**
Lewis et al., 2020 - RAG 原始论文。

## C.3 开源框架与开发工具 (Frameworks & Tools)

### C.3.1 开发框架
**LangChain**
https://github.com/langchain-ai/langchain
本书多次提及，目前应用最广的 LLM 开发框架，提供了丰富的工具链与 Pipeline 抽象。
特点：提示词模板管理、链式调用、Agent构建、丰富的集成。

**LlamaIndex**
https://github.com/run-llama/llama_index
专注于数据接入和RAG的框架。
特点：多种数据源连接器、灵活的索引结构、查询引擎。

**DSPy**
https://github.com/stanfordnlp/dspy
斯坦福大学推出的用于自动编译和优化模型提示词的框架。用代码与评估指标代替手工撰写长提示词。

**AutoGen**
https://github.com/microsoft/autogen
微软的多Agent协作框架。
特点：Agent对话协作、人机协作、代码执行。

**CrewAI**
https://github.com/joaomdmoura/crewAI
轻量级的Agent团队协作框架。

### C.3.2 测试与评测工具
**Promptfoo**
https://github.com/promptfoo/promptfoo
广受欢迎的开源提示词测试、评测和版本对齐工具，支持 LLM-as-a-judge。

**PromptLayer**
https://promptlayer.com/
提示词版本控制和监控平台。
功能：API调用日志、提示词版本管理、性能分析。

**LangSmith**
https://www.langchain.com/langsmith
LangChain官方的调试和监控工具。

### C.3.3 向量数据库
**Pinecone**: 托管的向量数据库服务。
**Weaviate**: 开源向量搜索引擎。
**Chroma**: 轻量级的嵌入式向量数据库。
**Qdrant**: 高性能的向量相似度搜索引擎。

### C.3.4 其他项目
**Awesome Prompt Engineering**
https://github.com/promptslab/Awesome-Prompt-Engineering
社区维护的提示词工程学习资源大列表。

**awesome-chatgpt-prompts**
https://github.com/f/awesome-chatgpt-prompts
精选的ChatGPT提示词集合。

## C.4 实用平台与测试工具 (Practical Toolings)

### C.4.1 提示词测试
**OpenAI Playground**
https://platform.openai.com/playground
OpenAI官方的交互式测试环境。

**Anthropic Console**
https://console.anthropic.com/
Claude的测试控制台。

**Google AI Studio**
https://aistudio.google.com/
Google提供的多模态提示词开发与API测试平台。

### C.4.2 Token计算
**OpenAI Tokenizer**
https://platform.openai.com/tokenizer
可视化Token分词工具。

**tiktoken (Python库)**
```python
import tiktoken

try:
    encoding = tiktoken.get_encoding("cl100k_base")
except Exception:
    import tiktoken

    encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode("your text")
print(tokens)
```

### C.4.3 提示词优化
**PromptPerfect**
https://promptperfect.jina.ai/
AI驱动的提示词优化工具。

**Prompt Generator**
各种在线的提示词生成器工具。

## C.5 扩展学习资源 (Extended Learning)

### C.5.1 在线课程
**DeepLearning.AI - ChatGPT Prompt Engineering for Developers**
由OpenAI和DeepLearning.AI联合推出的免费课程。

**Prompt Engineering Guide (DAIR.AI)**
https://www.promptingguide.ai/
全面的提示词工程学习指南，涵盖各种技术。

### C.5.2 博客与社区
**Lil'Log (Lilian Weng)**
https://lilianweng.github.io/
OpenAI研究员的技术博客，深入浅出。

**Reddit - r/PromptEngineering**
提示词工程社区，经验分享和讨论。

**Discord - LangChain**
LangChain官方Discord，活跃的开发者社区。

### C.5.3 数据集与Benchmark
**MMLU (Massive Multitask Language Understanding)**: 评估模型多任务理解能力的基准数据集。
**HumanEval**: 代码生成能力评估数据集。
**GSM8K**: 数学推理能力评估数据集。
**SuperGLUE**: 自然语言理解任务集合。

### C.5.4 持续学习
**资讯聚类:**
- https://www.aiweekly.co/
- https://www.deeplearning.ai/the-batch/

**前沿论文:**
- arXiv.org (cs.CL, cs.AI)
- Papers with Code

**知名人物:**
- @OpenAI, @AnthropicAI, @GoogleAI
- @omarsar0 (DAIR.AI创始人)
- @lilianweng (OpenAI研究员)

**YouTube频道:**
- Andrej Karpathy
- Two Minute Papers
- AI Explained

---

## 使用建议

1. **从官方文档开始**：打下扎实基础
2. **动手实践**：使用Playground测试想法
3. **参与社区**：学习他人经验
4. **关注前沿**：跟踪最新研究和技术
5. **构建项目**：在实际应用中深化理解

---

*注：链接和推荐基于2026年1月的信息，请访问时验证最新版本。*
