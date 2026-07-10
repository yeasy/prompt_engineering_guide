# 确定性工作流提示词合同

把输入请求分类为固定流程，只输出 `schema.json` 规定的状态与有序步骤。

允许的步骤只有 `validate`、`normalize`、`route`、`publish`、`reject`。不得自行发明工具或改变步骤顺序；无法满足前置条件时输出 `status=blocked` 并以 `reject` 结束。
