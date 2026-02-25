# 第三章：提示词的基本结构

## 本章小结

本章系统性地介绍了提示词的基本结构，涵盖核心组成要素、指令设计原则、上下文构建和输出格式定义。以下是本章的核心要点回顾：

### 关键概念

- **提示词结构**：由角色、指令、上下文、输入、格式、示例六大要素组成
- **指令设计**：遵循清晰、具体、行动导向、正向表达等原则
- **上下文**：为模型提供背景知识、约束条件和参考材料
- **输出格式**：通过模板和约束控制输出的结构和形式

### 核心要点

1. **六大核心要素**

   | 要素 | 功能 | 设计要点 |
   |------|------|----------|
   | 角色 | 设定专业视角和风格 | 明确专业领域和经验 |
   | 指令 | 定义任务目标 | 使用行动动词，具体化 |
   | 上下文 | 提供背景信息 | 相关、简洁、结构化 |
   | 输入 | 待处理的内容 | 清晰分隔，标签标注 |
   | 格式 | 规范输出形式 | 提供模板，明确约束 |
   | 示例 | 展示期望模式 | 代表性、多样性 |

2. **指令设计七大原则**
   - 清晰明确：避免模糊表达
   - 具体细致：指定数量、质量标准
   - 行动导向：使用明确的动词
   - 逻辑顺序：按合理结构组织
   - 正向表达：告诉模型"做什么"
   - 边界考虑：处理异常情况
   - 迭代优化：持续测试改进

3. **上下文管理**
   - 类型：背景知识、场景描述、目标受众、约束条件、参考材料
   - 组织：使用标签分隔，分层呈现
   - 原则：相关、简洁、不冲突

4. **输出格式控制**
   - 常用格式：JSON、Markdown、表格、列表
   - 控制方法：模板示例、长度限制、取值范围
   - 高级技巧：预填充、格式验证

5. **结构化输出**
   - 格式对比：JSON、XML、YAML 的适用场景
   - JSON 模式：清晰指令、提供 Schema、设计逃生通道
   - 平台特性：OpenAI Structured Outputs、Claude XML、Gemini JSON
   - 容错策略：自动清理、多重重试、反射纠错

### 提示词结构模板

```markdown
# 角色定义
[模型应扮演的角色和具备的能力]

# 任务背景
[任务的上下文和相关信息]

# 具体任务
[清晰的任务指令和要求]

# 约束条件
[必须遵守的规则和限制]

# 输出格式
[期望的输出结构和形式]

# 示例（可选）
[输入输出示例]

# 待处理内容
[实际输入数据]
```

### 实践检查清单

设计提示词时，可以使用以下清单自检：

- [ ] 角色设定是否有助于任务完成？
- [ ] 指令是否清晰、具体、无歧义？
- [ ] 是否提供了必要的上下文信息？
- [ ] 输入数据是否已清晰标识？
- [ ] 输出格式是否明确定义？
- [ ] 是否需要添加示例来消除歧义？
- [ ] 是否考虑了边界情况的处理？
- [ ] 提示词长度是否在合理范围内？

### 延伸阅读

#### 3.1 核心要素
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - OpenAI 官方提示词指南
- [Anthropic Prompt Design](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-structure) - Claude 提示词结构指南
- [Google Prompt Design Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) - Gemini 提示词策略

#### 3.2 指令设计
- [Tactic: Include Details](https://platform.openai.com/docs/guides/prompt-engineering#tactic-include-details-in-your-query-to-get-more-relevant-answers) - OpenAI 具体化指令技巧
- [Give Claude a Role](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/give-claude-a-role) - Anthropic 角色设定指南

#### 3.3 上下文
- [Provide Reference Text](https://platform.openai.com/docs/guides/prompt-engineering#tactic-provide-reference-text) - OpenAI 提供参考文本技巧
- [Use XML Tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) - Anthropic XML标签使用指南
- [Long Context Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips) - Claude 长上下文技巧

#### 3.4 输出格式
- [Control Output Format](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/control-output-format) - Anthropic 输出格式控制
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) - OpenAI 结构化输出指南
- [JSON Mode](https://platform.openai.com/docs/guides/json-mode) - OpenAI JSON 模式

### 下一章预告

第四章将介绍提示词设计的最佳实践，包括清晰性与具体性原则、分隔符的使用、角色设定技巧以及迭代优化方法。这些实践技巧将帮助读者在实际应用中设计出更高效的提示词。

---

[下一章：提示词设计最佳实践 →](../04_best_practices/README.md)
