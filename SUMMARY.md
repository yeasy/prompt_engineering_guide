# Summary

* [前言](README.md)

## 第一部分：基础篇

* [第一章：提示词工程概述](01_introduction/README.md)
  * [1.1 什么是提示词工程](01_introduction/1.1_what_is_prompt_engineering.md)
  * [1.2 提示词工程的发展历程](01_introduction/1.2_history.md)
  * [1.3 为什么提示词工程如此重要](01_introduction/1.3_importance.md)
  * [1.4 提示词工程的核心价值与应用场景](01_introduction/1.4_value_and_scenarios.md)
  * [1.5 提示词技术分类体系](01_introduction/1.5_taxonomy.md)
  * [本章小结](01_introduction/summary.md)

* [第二章：大语言模型基础](02_llm_basics/README.md)
  * [2.1 大语言模型的工作原理](02_llm_basics/2.1_how_llm_works.md)
  * [2.2 主流大语言模型概览](02_llm_basics/2.2_major_models.md)
  * [2.3 模型参数与输出控制](02_llm_basics/2.3_parameters.md)
  * [2.4 上下文窗口与信息处理](02_llm_basics/2.4_context_window.md)
  * [本章小结](02_llm_basics/summary.md)

* [第三章：提示词的基本结构](03_prompt_structure/README.md)
  * [3.1 提示词的核心组成要素](03_prompt_structure/3.1_core_elements.md)
  * [3.2 指令设计的基本原则](03_prompt_structure/3.2_instruction_principles.md)
  * [3.3 上下文与背景信息的提供](03_prompt_structure/3.3_context.md)
  * [3.4 输出格式的定义与约束](03_prompt_structure/3.4_output_format.md)
  * [本章小结](03_prompt_structure/summary.md)

* [第四章：提示词设计最佳实践](04_best_practices/README.md)
  * [4.1 清晰性与具体性原则](04_best_practices/4.1_clarity_specificity.md)
  * [4.2 分隔符与结构化表达](04_best_practices/4.2_delimiters.md)
  * [4.3 角色设定与人格赋予](04_best_practices/4.3_role_setting.md)
  * [4.4 迭代优化与测试方法](04_best_practices/4.4_iteration.md)
  * [本章小结](04_best_practices/summary.md)

## 第二部分：核心技术篇

* [第五章：少样本学习与示例驱动](05_few_shot/README.md)
  * [5.1 零样本与少样本提示](05_few_shot/5.1_zero_shot_few_shot.md)
  * [5.2 示例的选择与设计策略](05_few_shot/5.2_example_design.md)
  * [5.3 少样本学习的应用场景](05_few_shot/5.3_applications.md)
  * [5.4 常见问题与解决方案](05_few_shot/5.4_troubleshooting.md)
  * [5.5 本章实战练习](05_few_shot/5.5_practice.md)
  * [本章小结](05_few_shot/summary.md)

* [第六章：思维链与推理增强](06_chain_of_thought/README.md)
  * [6.1 思维链提示的原理与价值](06_chain_of_thought/6.1_cot_principles.md)
  * [6.2 零样本与少样本思维链](06_chain_of_thought/6.2_zero_few_shot_cot.md)
  * [6.3 自一致性与多路径推理](06_chain_of_thought/6.3_self_consistency.md)
  * [6.4 思维树与高级推理策略](06_chain_of_thought/6.4_tree_of_thought.md)
  * [6.5 本章实战练习](06_chain_of_thought/6.5_practice.md)
  * [本章小结](06_chain_of_thought/summary.md)

* [第七章：提示词链与任务分解](07_prompt_chaining/README.md)
  * [7.1 复杂任务的分解艺术](07_prompt_chaining/7.1_task_decomposition.md)
  * [7.2 提示词链的设计模式](07_prompt_chaining/7.2_chaining_patterns.md)
  * [7.3 上下文传递与状态管理](07_prompt_chaining/7.3_context_passing.md)
  * [7.4 实战案例：构建多步骤工作流](07_prompt_chaining/7.4_case_study.md)
  * [本章小结](07_prompt_chaining/summary.md)

## 第三部分：高级应用篇

* [第八章：ReAct 与工具使用](08_react_tools/README.md)
  * [8.1 ReAct 框架：推理与行动的结合](08_react_tools/8.1_react_framework.md)
  * [8.2 函数调用与工具集成](08_react_tools/8.2_function_calling.md)
  * [8.3 外部知识源的接入](08_react_tools/8.3_external_knowledge.md)
  * [8.4 Agent 系统的提示词设计](08_react_tools/8.4_agent_prompts.md)
  * [本章小结](08_react_tools/summary.md)

* [第九章：检索增强生成（RAG）](09_rag/README.md)
  * [9.1 RAG 系统的核心原理](09_rag/9.1_rag_principles.md)
  * [9.2 检索策略与上下文组装](09_rag/9.2_retrieval_strategies.md)
  * [9.3 RAG 系统的提示词优化](09_rag/9.3_rag_prompt_optimization.md)
  * [9.4 高级 RAG 架构与实践](09_rag/9.4_advanced_rag.md)
  * [本章小结](09_rag/summary.md)

* [第十章：多模态提示工程](10_multimodal/README.md)
  * [10.1 多模态模型概述](10_multimodal/10.1_multimodal_overview.md)
  * [10.2 图像理解与视觉提示](10_multimodal/10.2_image_prompting.md)
  * [10.3 音频与视频处理](10_multimodal/10.3_audio_video.md)
  * [10.4 跨模态推理与融合](10_multimodal/10.4_cross_modal_reasoning.md)
  * [本章小结](10_multimodal/summary.md)

* [第十一章：安全性与可靠性](11_safety_reliability/README.md)
  * [11.1 提示词注入与防护策略](11_safety_reliability/11.1_prompt_injection.md)
  * [11.2 幻觉问题与事实性保障](11_safety_reliability/11.2_hallucination.md)
  * [11.3 偏见识别与公平性考量](11_safety_reliability/11.3_bias_fairness.md)
  * [11.4 企业级安全架构设计](11_safety_reliability/11.4_enterprise_security.md)
  * [11.5 本章实战练习](11_safety_reliability/11.5_practice.md)
  * [本章小结](11_safety_reliability/summary.md)

## 第四部分：进阶与展望

* [第十二章：自动化提示词工程](12_automated_pe/README.md)
  * [12.1 自动化提示词生成技术](12_automated_pe/12.1_auto_generation.md)
  * [12.2 提示词优化与调优工具](12_automated_pe/12.2_optimization_tools.md)
  * [12.3 评估体系与质量度量](12_automated_pe/12.3_evaluation.md)
  * [12.4 PromptOps：提示词运维实践](12_automated_pe/12.4_promptops.md)
  * [本章小结](12_automated_pe/summary.md)

* [第十三章：平台特定策略](13_platform_specific/README.md)
  * [13.1 OpenAI GPT 系列最佳实践](13_platform_specific/13.1_openai_gpt.md)
  * [13.2 Anthropic Claude 提示技巧](13_platform_specific/13.2_anthropic_claude.md)
  * [13.3 Google Gemini 提示策略](13_platform_specific/13.3_google_gemini.md)
  * [13.4 开源模型的提示词适配](13_platform_specific/13.4_open_source.md)
  * [13.5 跨模型提示词策略](13_platform_specific/13.5_cross_platform_strategy.md)
  * [本章小结](13_platform_specific/summary.md)

* [第十四章：未来趋势与展望](14_future/README.md)
  * [14.1 从提示词工程到上下文工程](14_future/14.1_context_engineering.md)
  * [14.2 多 Agent 协作与编排](14_future/14.2_multi_agent.md)
  * [14.3 提示词工程的职业发展](14_future/14.3_career.md)
  * [14.4 行业应用案例与最佳实践](14_future/14.4_industry_cases.md)
  * [本章小结](14_future/summary.md)

## 附录

* [附录A：提示词模板库](appendix/a_templates.md)
* [附录B：常用术语表](appendix/b_glossary.md)
* [附录C：学习资源与工具推荐](appendix/c_resources.md)
