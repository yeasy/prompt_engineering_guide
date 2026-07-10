# 结构化提取提示词合同

从 `<document>` 中提取发票信息，只输出符合 `schema.json` 的 JSON 对象。

规则：

1. `vendor`、`invoice_id`、`currency`、`total` 四个字段必须全部出现。
2. 不推测缺失值；输入缺字段时应由调用方判定本 case 失败。
3. `total` 必须是数字，`currency` 只允许 `CNY`、`USD` 或 `EUR`。
4. 不输出 Markdown、解释或 schema 外字段。

输入模板：

```text
<document>
{{input}}
</document>
```
