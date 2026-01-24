# 第二章：大语言模型基础

## 本章小结

本章介绍了大语言模型的核心基础知识，这些知识是理解和实践提示词工程的重要支撑。以下是本章的核心要点回顾：

### 关键概念

- **语言建模**：模型通过预测"下一个 Token"来学习语言规律
- **Token**：模型处理文本的基本单位，影响成本计算和长度限制
- **Transformer**：现代大语言模型的核心架构，通过注意力机制处理语言
- **上下文窗口**：模型单次推理能处理的最大 Token 数量

### 核心要点

1. **模型工作原理**
   - 大语言模型本质是复杂的"下一词预测器"
   - Transformer 的注意力机制使模型能理解长距离依赖
   - 预训练获得通用能力，微调实现指令遵循
   - 涌现能力使大模型具备小模型不具备的高级功能

2. **主流模型特点**

   | 模型系列 | 核心优势 | 提示词特点 |
   |----------|----------|------------|
   | OpenAI GPT | 生态完善，推理能力强 | 系统提示词、函数调用 |
   | Claude | 安全性高，长上下文 | XML 标签、预填充 |
   | Gemini | 原生多模态，超长上下文 | 多模态混合提示 |
   | Llama | 开源可控，社区活跃 | 特定模板格式 |

3. **模型参数作用**
   - **Temperature**：控制输出随机性（0 确定，1+ 创意）
   - **Top-p**：核采样，限制采样范围
   - **Max Tokens**：限制输出长度
   - **惩罚参数**：控制重复程度

4. **上下文窗口管理**
   - 信息位置影响关注度（开头和结尾更重要）
   - 长上下文面临"迷失在中间"问题
   - 需要有效的历史管理和压缩策略
   - Token 预算规划是提示词设计的重要环节

### 与提示词工程的关联

理解模型基础对提示词设计的指导意义：

```
模型原理 → 设计启示
─────────────────────
模式匹配特性    → 激活相关知识的提示词
Token 机制      → 简洁高效的表达
注意力分布      → 合理的信息布局
采样参数        → 任务适配的参数选择
上下文限制      → 有效的信息组织
```

### 实践建议

1. **了解所用模型**：熟悉目标模型的特性、长处和限制
2. **参数先固定后调优**：从推荐参数开始，基于效果逐步调整
3. **Token 意识**：在设计提示词时考虑 Token 成本
4. **结构化长内容**：使用清晰的格式组织复杂信息
5. **测试多模型**：重要应用在多个模型上验证效果

### 思考题

1. 对于一个需要高度一致性的自动化任务，Temperature 应该如何设置？为什么？

2. 在处理一份 10 万字的合同文档时，如何有效利用有限的上下文窗口？

3. 同样的提示词在不同模型上效果可能不同，这告诉了我们什么？

### 延伸阅读

#### 2.1 原理与架构
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Transformer 架构的原始论文
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) - Transformer 可视化详解
- [What Is ChatGPT Doing… and Why Does It Work?](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/) - Stephen Wolfram 的深入解析
- [Emergent Abilities of Large Language Models](https://arxiv.org/abs/2206.07682) - 涌现能力研究论文

#### 2.2 主流模型
- [OpenAI Models](https://platform.openai.com/docs/models) - OpenAI 模型官方文档
- [Anthropic Claude Models](https://docs.anthropic.com/en/docs/about-claude/models/all-models) - Claude 模型官方文档
- [Google Gemini Models](https://ai.google.dev/gemini-api/docs/models/gemini) - Gemini 模型官方文档
- [Meta Llama](https://llama.meta.com/) - Llama 开源模型官网
- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) - 开源模型排行榜

#### 2.3 参数与控制
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/chat/create) - OpenAI 参数完整说明
- [Anthropic API Reference](https://docs.anthropic.com/en/api/messages) - Claude 参数完整说明
- [The Curious Case of Temperature in LLMs](https://www.lesswrong.com/posts/t5LGHMGQ7Gxq6TbJ4/the-curious-case-of-neural-network-test-time-training) - 温度参数深入解析

#### 2.4 上下文窗口
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) - 长上下文中位置效应的研究论文
- [Leave No Context Behind](https://arxiv.org/abs/2404.07143) - Gemini 无限上下文技术论文
- [Anthropic Context Windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows) - Claude 上下文窗口最佳实践

### 下一章预告

第三章将进入提示词设计的实践环节，详细介绍提示词的基本结构，包括核心组成要素、指令设计原则、上下文提供策略和输出格式定义，帮助读者掌握构建有效提示词的基本技能。

---

[下一章：提示词的基本结构 →](../03_prompt_structure/README.md)
