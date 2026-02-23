# 附录 B：术语表

本附录收录了提示词工程和大语言模型领域的常用术语及其解释。

## A

**智能体（agent）（智能体）**  
能够自主感知环境、做出决策并采取行动的AI系统，通常具备规划、执行和反思能力。

**API（应用程序接口）**  
Application Programming Interface，允许应用程序之间相互通信的接口，大语言模型通常通过API提供服务。

**APE（自动提示词工程）**  
Automatic Prompt Engineering，使用AI自动生成和优化提示词的技术。

**Attention Mechanism（注意力机制）**  
Transformer架构的核心机制，使模型能够关注输入序列中的不同部分。

## B

**Beam Search（束搜索）**  
一种文本生成策略，在每步保留多个候选序列，平衡质量和多样性。

**Bias（偏见）**  
模型在输出中体现的系统性倾向，可能来源于训练数据或设计。

## C

**Chain-of-Thought（思维链）**  
通过引导模型展示推理步骤来提升复杂任务表现的提示技术，简称CoT。详见[第6章](../06_chain_of_thought/README.md)。

**ChatML**  
一种用于格式化对话的标记语言，某些开源模型使用此格式。

**Chunk（文档块）**  
RAG 系统中，将长文档分割成的较小片段，便于检索和处理。

**Context Window（上下文窗口）**  
模型一次能处理的最大Token数量，决定了输入和输出的总长度限制。

**CoT（思维链）**  
Chain-of-Thought的缩写，见Chain-of-Thought。

## D

**Delimiter（分隔符）**  
用于区分提示词不同部分的标记，如三引号、XML标签等。

## E

**Embedding（嵌入）**  
将文本转换为向量表示的过程，用于语义相似度计算。

## F

**Few-Shot Learning（少样本学习）**  
在提示词中提供少量示例来引导模型学习任务模式的技术。详见[第5章](../05_few_shot/README.md)。

**Fine-tuning（微调）**  
在预训练模型基础上，使用特定数据进行进一步训练以适应特定任务。

**Function Calling（函数调用）**  
模型生成结构化的函数调用请求，以调用外部工具或API的能力。

## G

**Generative AI（生成式AI）**  
能够生成新内容（文本、图像、音频等）的人工智能技术。

**Grounding（事实基础）**  
将模型输出基于可靠的外部知识源，以减少幻觉和提高准确性。

## H

**Hallucination（幻觉）**  
模型生成看似合理但实际错误或虚构的信息。

## I

**In-Context Learning（上下文学习）**  
模型通过提示词中的示例"学习"任务，而不改变模型参数。

**Instruction Tuning（指令调优）**  
通过大量指令-回复对训练模型，提升其遵循指令的能力。

## J

**JSON（JavaScript对象表示法）**  
一种轻量级的数据交换格式，常用于结构化输出。

## L

**LLM（大语言模型）**  
Large Language Model，基于大规模文本数据训练的生成式语言模型。

**LangChain**  
用于构建LLM应用的开发框架，提供提示词管理、链式调用等功能。

## M

**Meta-Prompting（元提示）**  
使用提示词来生成或优化其他提示词的技术。

**Multimodal（多模态）**  
能够处理和生成多种类型数据（文本、图像、音频等）的模型。

## O

**One-Shot Learning（单样本学习）**  
在提示词中提供一个示例来指导模型的技术。

## P

**Parameter（参数）**  
模型内部的可学习权重，参数量通常用来衡量模型规模。

**Prefill（预填充）**  
预先设定回复的开头部分，引导模型按特定格式继续生成。

**Prompt（提示词）**  
发送给语言模型的输入文本，用于指导模型生成期望的输出。

**Prompt Engineering（提示词工程）**  
设计和优化提示词以提升模型输出质量的技术和实践。

**Prompt Injection（提示词注入）**  
通过恶意输入试图操控模型行为的安全攻击手段。

**PromptOps**  
将DevOps理念应用于提示词生命周期管理的实践。

## R

**RAG（检索增强生成）**  
Retrieval-Augmented Generation，结合信息检索和文本生成的技术架构。详见[第9章](../09_rag/README.md)。

**ReAct**  
Reasoning and Acting，将推理与行动交替进行的Agent框架。详见[第8章](../08_react_tools/README.md)。

**RLHF（人类反馈强化学习）**  
Reinforcement Learning from Human Feedback，使用人类反馈优化模型行为的训练方法。

**Role（角色）**  
为模型设定的身份或专业领域，影响回复风格和视角。

## S

**Self-Consistency（自一致性）**  
通过多路径采样和投票提升推理准确性的技术。

**系统提示词（system prompt）（系统提示词）**  
设定模型整体行为和规则的提示词，通常在对话开始时提供。

## T

**Temperature（温度）**  
控制生成随机性的参数，值越高输出越随机，越低越确定。

**Token（词元）**  
模型处理文本的基本单位，可以是一个词、词的一部分或标点符号。

**Token Limit（Token限制）**  
上下文窗口的大小限制，决定了输入输出的总Token数上限。

**Top-k Sampling**  
每步生成时只从概率最高的k个Token中采样的策略。

**Top-p Sampling（核采样）**  
每步生成时从累积概率达到p的最小Token集合中采样的策略。

**ToT（思维树）**  
Tree of Thoughts，将推理过程组织为树形结构的高级推理策略。

**Transformer**  
现代大语言模型的基础架构，基于注意力机制。

## V

**Vector Database（向量数据库）**  
专门用于存储和检索向量嵌入的数据库，RAG 系统的核心组件。

**VLM（视觉语言模型）**  
Vision-Language Model，能够理解图像和文本的多模态模型。

## Z

**Zero-Shot Learning（零样本学习）**  
不提供示例，仅通过指令描述任务让模型完成的技术。详见[第5章](../05_few_shot/README.md)。

---

## 新增术语（2025年更新）

**A2A Protocol（智能体（agent）-to-Agent协议）**  
Google提出的Agent间通信标准化协议，定义了多智能体系统中的消息格式和交互模式。

**Context Engineering（上下文工程）**  
关注整个上下文窗口的系统性管理，包括系统指令、检索内容、记忆状态等的动态组装与优化。

**Extended Thinking（扩展思考）**  
Claude等模型支持的功能，允许模型在回答前进行更深入的内部推理，可通过预算参数控制思考深度。

**MCP（模型上下文协议）**  
Model Context Protocol，Anthropic发布的开放协议，标准化AI 应用与各类数据源、工具之间的连接方式。

**MoE（混合专家模型）**  
Mixture of Experts，一种模型架构，通过路由机制动态激活部分参数，实现大规模模型的高效推理。

**Structured Outputs（结构化输出）**  
OpenAI等平台提供的功能，确保模型输出严格符合指定的JSON Schema，无需后处理验证。

---

**注**：本术语表持续更新中，随着技术发展会有新的术语出现。
