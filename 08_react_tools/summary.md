# 第八章：ReAct 与工具使用

## 本章小结

本章系统性地介绍了大语言模型如何通过调用外部工具拓展能力边界。涵盖了 ReAct 框架、函数调用机制（Function Calling）、外部知识接入以及构建自主智能体（Agent）系统的核心方法。这些技术使大语言模型从一个单纯的"文本生成器"转变为"行动执行者"。

### 关键概念

- **ReAct (Reason + Act)**：结合推理与行动的复合流框架，使模型在执行行动前显式输出思考过程。
- **函数调用 (Function Calling)**：模型原生支持输出结构化的 JSON，用于安全可靠地调用外部代码函数。
- **智能体 (Agent)**：能感知环境、自主规划、选择工具并执行多步动作的 AI 系统。
- **原子工具与组合工具**：专注于单一任务的底层函数，以及由此编排出的复杂工作流工具。

### 核心要点

1. **ReAct 循环设计**
   - **Thought**：分析当前状态和目标，决定下一步行动。
   - **Action**：从给定工具箱中选择工具并生成调用参数。
   - **Observation**：解析工具返回的执行结果，作为下一轮推理的上下文。
   - **循环机制**：重复该过程直至获得最终答案（Final Answer）。

2. **函数调用 (Function Calling) 最佳实践**
   - **名称自解释**：使用具有明确意图的动名词作函数名（如 `search_weather`）。
   - **Schema 描述**：使用 Pydantic 或标准 JSON Schema，提供带量词和边界限制的参数描述。
   - **容错处理**：设计逃生通道，当模型提供的参数无法解析时返回人类可读的错误而非抛出异常。

3. **工具与知识库的集成**
   - **权限分离**：将查询工具与写入工具分离，降低安全风险。
   - **上下文折叠**：过滤庞大的工具返回结果，提取精要信息再送回模型，避免淹没上下文。

4. **Agent 提示词系统设计**
   - **能力边界设定**：在系统提示词中明确划定何可为何不可为。
   - **分层行动空间**：对复杂工具链进行隔离（例如：原子调用、沙盒执行、Python脚本层）。
   - **自反思机制 (Reflexion)**：指导模型在工具调用失败时进行错误归因并修正。

### 实践检查清单

- [ ] 提供给模型的工具箱是否功能正交，没有高度重叠的工具？
- [ ] 工具的入参是否有清晰的描述和类型约束？
- [ ] 是否要求模型在做出 Action 之前显式输出 Thought？
- [ ] 是否限制了单次对话的最大思考步数以防止死循环？
- [ ] 危险操作（如删除、支付）是否有外部审计或人工介入确认（Human-in-the-loop）？

### 延伸阅读

#### 8.1 ReAct 框架
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) - ReAct 原始论文
- [Prompting Guide: ReAct Prompting](https://www.promptingguide.ai/techniques/react) - ReAct 提示词指南

#### 8.2 函数调用 (Function Calling)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling) - OpenAI 官方函数调用实战指南
- [Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - Claude 工具使用指南

#### 8.3 Agent 架构设计
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) - Lilian Weng 关于 Agent 的权威综述

### 下一章预告

[第九章](../09_rag/README.md)将重点介绍检索增强生成（RAG），它是 ReAct 和工具调用在知识获取领域的一个特定且极其重要的大规模应用，我们将探讨如何构建不产生幻觉的企业级知识问答系统。

---

[下一章：检索增强生成 →](../09_rag/README.md)
