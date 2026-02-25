# 第十一章：安全性与可靠性

## 本章小结

大语言模型（LLM）的黑盒性质为在企业级生产系统中的部署引入了大量不可控因素。本章系统性地梳理了阻碍 LLM 落地应用的两大核心拦路虎——安全性漏洞（特别是指令注入）和可靠性缺陷（主要是各种形式的幻觉），并提出了防御性的提示词编写和系统架构方案。

### 关键概念

- **提示词注入 (Prompt Injection)**：恶意用户通过精心构造的输入文本，覆盖或篡改开发者预设的 System Prompt，从而控制模型行为。
- **越狱 (Jailbreak)**：绕过模型自身的伦理与安全审核策略，迫使模型输出违规或敏感内容。
- **幻觉 (Hallucination)**：模型产生流畅但事实上不准确、缺乏根据、或者违背常识逻辑的内容。
- **数据泄露**：模型不经意间在输出中吐露了属于训练上下文的敏感商业数据或个人隐私。

### 核心要点

1. **防御提示词注入的体系化方法**
   - **定界符隔离**：使用 XML 标签或者多重随机字符（如 `###` 或 `%%%`）将系统指令与用户提供的无信任数据彻底切开。
   - **指令后置**：在上下文的最末尾（甚至紧靠 `user` prompt 的地方）再重申一次核心安全边界，利用注意力机制抵抗近期的注入冲击。
   - **白名单限制**：对模型预期处理的数据格式和回答格式施加最严格的白名单校验。

2. **化解各种形式的幻觉**
   - 对于"知识盲区"引发的幻觉，采用 RAG 等外部知识库增强，并在提示词中设立强烈的"免责/无知声明"出口。
   - 对于"逻辑推导"引发的幻觉，使用分解任务（CoT、Prompt Chaining）来将长路径降维成可以步步为营的短环节。

3. **内容审核系统集成**
   - 不要仅仅依靠单模型的内建红线，应增加额外的验证网关层（例如 OpenAI Moderation API）或独立的审查模型（LLM-as-a-Judge）专门检查最终结果。

4. **企业隐私防护**
   - 尽可能将个人识别信息（PII）在传入大模型前进行匿名化遮盖（Data Masking）。
   - 在提示词中反复声明"不可将当前对话中的敏感参数作为推荐记忆"。

### 实践检查清单

- [ ] 是否将用户的原始输入放入了 XML 或自定义的定界符内，且在处理前去除了转义字符？
- [ ] 如果使用了 RAG，提示词是否明确约束了模型"如果不符合资料请直接输出我不确定"？
- [ ] 系统的 System Prompt 是否有泄露或者被套出的机制风险？是否做了相应的过滤？
- [ ] 调用第三方 API 或数据库时，Agent 的执行环境是否有最少权限控制（Least Privilege）？

### 延伸阅读

#### 11.1 安全漏洞与防护机制
- [OWASP Top 10 for Large Language Models](https://owasp.org/www-project-top-10-for-large-language-model-applications/) - 权威的 LLM 安全漏洞与防御指南
- [Prompt Injection Attacks](https://simonwillison.net/series/prompt-injection/) - Simon Willison 著名的提示词注入系列研究
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - 保护 LLM 对话的安全围栏框架

#### 11.2 模型对齐与越狱
- [Training language models to follow instructions with human feedback (InstructGPT)](https://arxiv.org/abs/2203.02155) - RLHF 与人类对齐原理
- [Jailbreaking ChatGPT via Prompt Engineering](https://arxiv.org/abs/2305.13860) - 针对大语言模型越狱技术的综述研究

### 下一章预告

既然大语言模型已经不再是闲聊的玩具，我们如何将散落在开发人员笔记里的"魔法咒语"改造为工程化的流水线？在第十二章，我们将学习提示词工程向 "PromptOps" 的演进历程，探索如何利用框架自动优化并评估海量的提示词。

---

[下一章：自动化提示词工程 →](../12_automated_pe/README.md)
