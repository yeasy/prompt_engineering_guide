# 附录 H：快变事实核验表

> Last verified: 2026-06-17. 本表用于维护提示词工程中模型、API、上下文、成本、MCP 与 benchmark 的高波动事实。

| 类别 | 当前维护口径 | 权威入口 | 编辑要求 |
| --- | --- | --- | --- |
| OpenAI | GPT-5.x、Responses API、Agents SDK、built-in tools 以官方 docs 为准。 | [OpenAI Models](https://developers.openai.com/api/docs/models/all/), [Responses API](https://platform.openai.com/docs/api-reference/responses) | 新示例优先使用当前推荐 API；历史 API 标注 legacy。 |
| Anthropic | Claude Fable 5 / Mythos 5（2026-06-09 GA/受邀；2026-06-12 起访问暂停）与 Claude 4.x、thinking、tool use、Claude Code 以官方文档为准。 | [Claude Models](https://platform.claude.com/docs/en/about-claude/models/overview), [Fable/Mythos access statement](https://www.anthropic.com/news/fable-mythos-access), [Claude Code Docs](https://code.claude.com/docs/) | 不预测未发布模型，不把 beta 当 GA；“最强/旗舰”须区分发布规格、当前可用性、Fable 5（全系）与 Opus 4.8（Opus 档）。 |
| Gemini | Gemini 3.x、实时多模态、Deep Think 以 Google AI docs 为准。 | [Gemini Models](https://ai.google.dev/gemini-api/docs/models) | 同一书内只使用官方命名。 |
| MCP | MCP prompt/resource/tool/server 语义以规范为准。 | [MCP Spec](https://modelcontextprotocol.io/specification) | token 节省等数字必须有来源或标为示意。 |
| 评估与成本 | PromptOps、A/B eval、token 成本、benchmark 只作为 dated snapshot。 | 官方 pricing、eval 工具文档、论文 | 不能把示例数据写成通用收益。 |
