# 第四章：提示词设计最佳实践

## 本章小结

本章介绍了四项核心的提示词设计最佳实践，这些实践源自主流AI厂商的官方指南和业界的实战经验。以下是本章的核心要点回顾：

### 关键概念

- **清晰性**：使用简单直接、无歧义的语言表达
- **具体性**：量化要求、定义标准、说明目的
- **分隔符**：用于区分提示词不同部分的标记
- **角色设定**：为模型定义特定身份和行为准则
- **迭代优化**：通过系统化测试持续改进提示词

### 核心要点

1. **清晰性与具体性原则**
   - 使用简单直接的语言
   - 避免歧义表达
   - 量化所有要求
   - 说明目的和受众
   - 在保持清晰的同时追求简洁

2. **分隔符与结构化表达**

   | 分隔符类型 | 示例 | 适用场景 |
   |----------|------|----------|
   | 三引号 | `"""内容"""` | 文本内容包裹 |
   | XML标签 | `<tag>内容</tag>` | 结构化最高，Claude偏好 |
   | Markdown | `## 标题` | 文档类提示词 |
   | 符号 | `###`, `===` | 通用分隔 |

3. **角色设定框架**
   - 身份定义：职业/角色
   - 专业背景：经验/技能
   - 沟通风格：语气/特点
   - 行为准则：应该/避免
   - 目标受众：服务对象

4. **迭代优化五步法**
   - 建立基准：定义成功标准与测试用例
   - 系统化测试：多次运行与对照测试
   - 问题诊断：分析输出缺陷的根源
   - 策略优化：逐步细化、添加示例、强化约束
   - 验证固化：回归测试与文档记录
5. **System Prompt 系统设计**
   - 核心定位：最高优先级、全局生效
   - 结构化范式：身份使命、能力边界、业务逻辑、输出格式
   - 长提示词管理：模块化拼接、核心指令后置
   - 最佳协同：System 存放稳定规则，User 存放本次任务输入

### 最佳实践速查表

```
✓ 首句点题：开头直接点明任务
✓ 量化要求：数量、长度、范围都要具体
✓ 正向表达：告诉模型"做什么"而非"不做什么"
✓ 使用分隔符：清晰区分不同部分
✓ 提供示例：消除歧义的最有效方式
✓ 设定角色：聚焦专业视角和风格
✓ 迭代测试：持续优化直到满意
```

### 常见问题与解决方案

| 问题 | 解决方案 |
|------|----------|
| 输出太冗长 | 添加明确的字数限制 |
| 格式不一致 | 提供精确的输出模板 |
| 遗漏关键点 | 使用清单列出必须包含的内容 |
| 理解偏差 | 简化语言，添加示例 |
| 风格不对 | 强化角色定义和风格说明 |
| 结果不稳定 | 降低Temperature，增加约束 |

### 延伸阅读

#### 4.1 清晰与具体
- [Write Clear Instructions](https://platform.openai.com/docs/guides/prompt-engineering#write-clear-instructions) - OpenAI 清晰指令指南
- [Be Specific and Direct](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct) - Anthropic 清晰直接原则
- [Prompt Engineering Best Practices](https://ai.google.dev/gemini-api/docs/prompting-intro#best-practices) - Google 最佳实践

#### 4.2 分隔符
- [Use Delimiters](https://platform.openai.com/docs/guides/prompt-engineering#tactic-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input) - OpenAI 分隔符使用技巧
- [Use XML Tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) - Anthropic XML 标签指南

#### 4.3 角色设定
- [System Prompt Examples](https://platform.openai.com/docs/guides/prompt-engineering#tactic-ask-the-model-to-adopt-a-persona) - OpenAI 角色设定示例
- [Give Claude a Role](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/give-claude-a-role) - Anthropic 角色设定指南

#### 4.4 迭代优化
- [Test Changes Systematically](https://platform.openai.com/docs/guides/prompt-engineering#strategy-test-changes-systematically) - OpenAI 系统化测试策略
- [Iterate on Prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/iterate-prompts) - Anthropic 提示词迭代指南

### 下一章预告

第五章将进入核心技术篇，首先介绍少样本学习与示例驱动技术。这是最有效的提示词技术之一，通过在提示词中提供少量示例，可以显著提升模型在各种任务上的表现。

---

[下一章：少样本学习与示例驱动 →](../05_few_shot/README.md)
