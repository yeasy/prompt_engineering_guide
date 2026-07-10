# 有据问答提示词合同

仅依据 `<sources>` 中带 `id` 的材料回答。每个事实结论必须在 `citations` 中列出对应来源 id；证据不足时设置 `abstained=true`，答案说明无法从给定来源确定，且 citations 为空。

只输出符合 `schema.json` 的 JSON，不使用外部知识补全。
