# 附录 I：生产落地脊柱

本路径不改变既有章节编号，而是把分散知识组织成六道递进验收门。只有当前阶段的验收产物可复现、预算可接受，才进入下一阶段；复杂度不是成熟度的替代品。

## 1. 提示词合同

<!-- production-stage: order=1 id=prompt-contract link=../03_prompt_structure/3.5_structured_output.md artifact=prompt.md+schema.json -->

先在[结构化输出](../03_prompt_structure/3.5_structured_output.md)中固定任务、输入边界、拒绝条件和输出 schema。验收产物是受版本控制的 `prompt.md` 与严格 `schema.json`；字段含义、必填项或失败行为不清晰时不得进入评测。

可执行起点：[structured_extraction](../examples/packages/structured_extraction/prompt.md)。

## 2. 评测

<!-- production-stage: order=2 id=eval link=../12_automated_pe/12.3_evaluation.md artifact=cases.jsonl+grader-report.json -->

按[评估体系](../12_automated_pe/12.3_evaluation.md)建立正常、边界与拒绝 case，并先运行确定性 grader。验收产物是 `cases.jsonl` 与带 grader 版本、通过率和失败样本的 `grader-report.json`。

## 3. 上下文

<!-- production-stage: order=3 id=context link=../09_rag/9.3_rag_prompt_optimization.md artifact=evidence-pack.json+citation-audit.json -->

只有离线合同通过后才接入[检索与上下文组装](../09_rag/9.3_rag_prompt_optimization.md)。验收产物是可重放的 `evidence-pack.json` 与逐条核对引用覆盖率的 `citation-audit.json`。

可执行起点：[grounded_qa](../examples/packages/grounded_qa/prompt.md)。

## 4. 确定性工作流

<!-- production-stage: order=4 id=deterministic-workflow link=../07_prompt_chaining/7.4_case_study.md artifact=workflow-trace.json+replay-result.json -->

能用普通代码表达的分支、校验、重试和状态转换，先按[多步骤工作流](../07_prompt_chaining/7.4_case_study.md)实现为确定性流程。验收产物是 `workflow-trace.json` 与相同输入得到相同结果的 `replay-result.json`。

可执行起点：[deterministic_workflow](../examples/packages/deterministic_workflow/prompt.md)。

## 5. 单智能体

<!-- production-stage: order=5 id=single-agent link=../08_react_tools/8.4_agent_prompts.md artifact=tool-policy.json+agent-trace.json -->

当任务确实需要模型在运行时选择工具或动态改计划时，再进入[单智能体提示设计](../08_react_tools/8.4_agent_prompts.md)。验收产物是最小权限 `tool-policy.json` 与记录调用、批准、成本、延迟和终止原因的 `agent-trace.json`。

## 6. 多智能体

<!-- production-stage: order=6 id=multi-agent link=../14_future/14.2_multi_agent.md artifact=task-graph.json+handoff-trace.json -->

只有存在可并行、边界清晰的独立工作流，且[多智能体编排](../14_future/14.2_multi_agent.md)相对单智能体基线带来可测收益时才升级。验收产物是带依赖关系的 `task-graph.json` 与可追踪责任、输入、输出和聚合规则的 `handoff-trace.json`。

## 共同发布门

每一阶段都必须保存精确 model snapshot、试验次数、单次成本和延迟；付费试验只能由人工触发或计划任务执行，不能在普通 push / pull request 上自动消耗预算。任何阶段失败都回退到最近一个已通过的简单阶段。
