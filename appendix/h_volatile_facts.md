# 附录 H：快变事实核验表

<!-- volatile-meta: verified_at=2026-07-10 expires_at=2026-08-09 ttl_days=30 -->

本表是模型、API、平台状态与已公布未来切换点的唯一快变事实入口。超过 `expires_at` 后，项目检查会失败；正文与本表冲突时，应先按官方来源更新本表，再同步带 `volatile-ref` 标记的章节。

## 状态约定

- `current`：核验日已经生效且官方来源一致。
- `future`：官方已公布、但尚未到生效日；必须记录 `effective_at`，不能写成已生效事实。
- `conflict`：官方一手来源暂时矛盾；必须记录 `next_review_at`，正文不得自行选边。
- `resolved-conflict`：先前冲突已被新公告解决；必须保留 `previous=conflict` 与 `resolved_at`，避免旧结论复活。

## 当前事实

<!-- volatile-status: id=openai-gpt-5.6 status=current -->

| 提供方 | 当前维护口径 | 权威入口 | 编辑要求 |
| --- | --- | --- | --- |
| OpenAI | 2026-07-09 发布 GPT-5.6 系列：`gpt-5.6-sol` 面向前沿能力，`gpt-5.6-terra` 平衡能力与成本，`gpt-5.6-luna` 面向高吞吐；`gpt-5.6` 别名路由到 Sol。Responses API 支持该系列，并新增 Programmatic Tool Calling、显式 prompt caching、持久化 reasoning，以及 beta 的 multi-agent orchestration。 | [API changelog](https://developers.openai.com/api/docs/changelog), [GPT-5.6 model guidance](https://developers.openai.com/api/docs/guides/latest-model) | 新工作流以 Responses API 为主；multi-agent 必须标 beta。模型别名会隐藏具体路由，生产记录必须保存实际 model snapshot。 |

<!-- volatile-status: id=anthropic-sonnet-5 status=current -->
<!-- volatile-status: id=anthropic-fable-access status=resolved-conflict previous=conflict resolved_at=2026-07-01 -->

| 提供方 | 当前维护口径 | 权威入口 | 编辑要求 |
| --- | --- | --- | --- |
| Anthropic | `claude-sonnet-5` 于 2026-06-30 发布，1M 上下文、128K 最大输出，Adaptive Thinking 默认开启。Claude Fable 5 / Mythos 5 于 6 月 9 日发布、6 月 12 日暂停，并于 7 月 1 日恢复访问；Fable 5 为 GA，规格含 1M 上下文、128K 输出、Adaptive Thinking 常开和 $10/$50 价格，Mythos 5 仅限 Project Glasswing 获批客户。 | [Claude release notes](https://platform.claude.com/docs/en/release-notes/overview), [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview), [Introducing Fable 5 and Mythos 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5), [Access statement](https://www.anthropic.com/news/fable-mythos-access) | 不再沿用“Fable 5 访问暂停”的冲突期结论；不预测未发布模型，不把 beta 当 GA。“最强/旗舰”须区分 Fable 5（全系）与 Opus 4.8（Opus 档），Fable 与 Sonnet 的 thinking、拒绝和可用性行为必须分别处理。 |

<!-- volatile-status: id=google-gemini-models status=current -->

| 提供方 | 当前维护口径 | 权威入口 | 编辑要求 |
| --- | --- | --- | --- |
| Google | Gemini 3.x、实时多模态与 Deep Think 以 Google AI 文档为准。当前模型页将 `gemini-3.5-flash` 标为 Stable，将 `gemini-3.1-pro-preview` 标为 Preview；生产默认优先固定 Stable model ID，Preview 只用于接受预览变动的评测。 | [Gemini models](https://ai.google.dev/gemini-api/docs/models), [Gemini API release notes](https://ai.google.dev/gemini-api/docs/changelog) | 同一书内只使用官方命名；不把 `latest` 别名或 Preview 当作固定生产快照，升级前记录精确 ID 并重跑评测。 |

## 其他快变事实

| 类别 | 当前维护口径 | 权威入口 | 编辑要求 |
| --- | --- | --- | --- |
| MCP | MCP prompt、resource、tool 与 server 的语义以当前规范为准。 | [MCP Specification](https://modelcontextprotocol.io/specification) | token 节省等数字必须有来源或标为示意。 |
| 评估与成本 | PromptOps、A/B eval、token 成本与 benchmark 只作为 dated snapshot。 | 官方 pricing、eval 工具文档和论文 | 不能把示例数据写成通用收益。 |

## 已公布的未来切换点

<!-- volatile-status: id=anthropic-sonnet-pricing status=future effective_at=2026-09-01 -->

| 事项 | 尚未生效的官方口径 | 权威入口 | 到期动作 |
| --- | --- | --- | --- |
| Claude Sonnet 5 价格 | $2/$10 每百万 token 的介绍价适用至 2026-08-31；2026-09-01 起标准价为 $3/$15。 | [Claude release notes](https://platform.claude.com/docs/en/release-notes/overview) | 成本示例必须同时给出介绍价截止日，9 月复核后才能把标准价写成当前价。 |

## 维护规则

1. 每次核验只使用厂商官方文档、官方 changelog 或正式公告。
2. `verified_at + ttl_days` 必须精确等于 `expires_at`；TTL 固定为 30 天。
3. 任何 `future` 事项在生效日前不得改成 `current`；任何冲突从 `conflict` 迁移为 `resolved-conflict` 时必须保留解决证据与日期。
4. benchmark、价格、上下文和模型推荐只作为 dated snapshot；生产选择必须由自己的评测、成本和延迟预算决定。
