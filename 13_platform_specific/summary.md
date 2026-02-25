# 第十三章：平台特定策略

## 本章小结

虽然提示词工程的基本原则（清晰、具体、提供示例等）在所有模型中通用，但各大主流模型因其后训练策略（RLHF 机制、数据集差异、安全对齐强度）的不同，在提示词的细微偏好上存在显著差异。本章深入剖析了 OpenAI GPT、Anthropic Claude、Google Gemini 以及典型开源模型的脾气秉性，并提供了平台针对性的优化策略。

### 关键概念

- **平台方言 (Platform Dialects)**：不同平台对于高亮、隔离、推理引导等指令的特殊格式偏好（如 Claude 的 XML 与 GPT 的 Markdown）。
- **预填充 (Prefilling)**：在支持的 API 中，预先写入 `Assistant` 角色的开头内容以强制模型按某种特定格式继续回答。
- **聊天模板 (Chat Template)**：开源模型中用于区分系统指令、用户提问和助手回复的特定词元结构（如 Llama 3 的 `<|start_header_id|>`）。

### 核心要点

1. **OpenAI GPT 系列 (GPT-4o / o1-preview)**
   - **Markdown 亲和**：对 Markdown 的层级结构理解最佳，极其适合使用带有 `##` 和代码块的结构化提示词。
   - **JSON Schema 与结构化输出**：拥有最成熟和严格的 Structured Outputs (结构化输出) 机制。
   - **系统提示词服从度极高**：对 `system` 角色的指令具有最高的服从性，适合放置极其严厉的行为约束。

2. **Anthropic Claude 系列 (Claude 3.5 Sonnet)**
   - **XML 标签狂热者**：官方极度推荐使用 `<document>` 等 XML 标签来区分数据源和划定指令范围。
   - **长文本寻觅者**：其超大上下文表现优异，但在极长文本中，经常需要配合在最后一段重复其核心任务。
   - **预填充的胜利**：在长 JSON 生成任务中，利用预填充技巧（提供大括号 `{` 作为 Assistant Response 开头）能有效阻止其生成寒暄废话。

3. **Google Gemini 系列 (Gemini 1.5 Pro)**
   - **绝对的超长上下文王者**：原生支持百万级 Token 窗口，在提示词设计中可以将厚厚的参考文档直接扔入而无需拆分。
   - **原生多模态混合交织**：非常擅长交错排列的处理，如 `[文本指令] -> [视频帧] -> [表格文本] -> [音频轨]` 的穿插式推理。

4. **开源模型策略 (Llama / Qwen 等)**
   - **精确的模板闭环**：如果不严格采用开发者训练时的 Jinja2 或特定 Token 模板组装会极速引发格式崩盘和严重幻觉。
   - **提纯与去冗余**：小模型（如 7B/8B）容易因为提示词过长造成灾难性遗忘，必须去掉高情商的人工寒暄语，只留最核心直接的动作动词。

### 实践检查清单

- [ ] 是否在切换底层模型后，重新评测甚至重写了基于前一个模型调优的超长系统提示词？
- [ ] 在调用 Claude API 时，是否将其长参考资料用 XML 切实包裹并在 User prompt 中进行了引用？
- [ ] 如果需要在应用中无缝兼容多个大厂模型，是否在架构侧准备了可以统一抹平并动态切换语言方言（如 LangChain PromptTemplate）的中间件？
- [ ] 测试开源模型时，是否确保应用的代码注入能够完美匹配官方所公布的对话模板（Chat Template）？

### 延伸阅读

#### 13.1 OpenAI 与结构化输出
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - OpenAI 官方最佳实践
- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) - 结构化输出技术文档

#### 13.2 Claude 与长文本/XML技巧
- [Claude Prompt Engineering Interactive Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) - 强烈推荐，Claude 官方互动式提示词教程
- [Claude Long Context Window Tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-window) - 处理超长文档的使用技巧

#### 13.3 Gemini 原生混合技巧
- [Google Gemini API Cookbook](https://github.com/google-gemini/cookbook) - 涵盖各种多模态提示词的配方与范例

#### 13.4 开源模型提示词范例
- [HuggingFace Chat Templates Guide](https://huggingface.co/docs/transformers/main/chat_templating) - 开源模型对话模板深入解析

### 下一章预告

经过对各大平台特性的细致拆解，我们的提示词工程体系已趋于完备。最后一章第十四章，我们将跳出眼前的技术细节，探讨未来一两年内提示词工程将走向何方（基于 Agent 系统的 Context Engineering 将逐渐替代单点 Prompt Engineering），并讨论在这个快速变迁的赛道上工程师的职业发展路径。

---

[下一章：未来趋势与展望 →](../14_future/README.md)
