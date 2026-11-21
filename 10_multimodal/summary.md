## 本章小结

<!-- volatile-ref: openai-gpt-5.6 -->
<!-- volatile-ref: anthropic-sonnet-5 -->
<!-- volatile-ref: google-gemini-models -->

本章讨论了涉及视觉和听觉内容的多模态大模型（如 GPT-6 与 GPT-5.6 系列、Gemini 3.8 Flash / Gemini 3.1 Pro Preview、Claude Opus 5.5）的提示词技术。与纯文本相比，多模态提示工程既要传递文字指令，也要精准引导模型将视觉特征与文本逻辑锚定和对齐。

### 关键概念

- **多模态对齐**：模型将图像像素、音频频谱等非结构化信号与文本语义对应起来的能力。
- **空间与时间锚点**：在提示词中通过坐标、区域描述或时间戳来精确指代媒体材料中的特定部分。
- **视觉幻觉**：模型因小物体丢失、文字识别（OCR）偏差或过度联想，强行“看出”不存在的信息。

### 核心要点

1. **多模态模型的特性与局限**
   - 原生多模态模型在架构层面融合多种模态，不再是“先看图后说话”的分离式处理；各模型支持的输入模态不同，音频与视频输入并非都具备。
   - 文档、表格、图表的 OCR 与结构化提取已属擅长任务；像素级测量与定位、极小或模糊文字的识别、专业领域图像的诊断性判读仍有局限。

2. **图像分析的提示词策略**
   - 坐标引导：在图像上画出网格或标记出数字边界框，并在提示词中要求模型返回相应的标记名。
   - 多阶推理：要求模型遵循 `观察 -> 描述局部特征 -> 联系上下文 -> 得出结论` 的思路（类似多模态 CoT）。
   - 聚焦任务：通过裁剪不相关的边缘甚至高斯模糊背景，从源头减少噪声干扰。

3. **长视频与音频的前处理策略**
   - 受底层限制，大多数模型采用“抽帧”方法分析长视频。
   - 需要在外部进行关键帧提取、重复帧去冗和音频转文字，再混合输入大模型处理。

4. **防幻觉设计法则**
   - 始终提供“内容不清”作为退路（例如：“如果图像分辨率不足以辨认车牌号，直接回答'无法辨认'”）。
   - 不要问带有极强暗示引导的封闭式问题（“图里那只猫是站着的对吧？”），而应使用开放描述：“描述图中有没有动物，它在做什么”。

### 实践检查清单

- [ ] 是否尽可能裁剪了图像中不需要大模型关注的无关区域？
- [ ] 若需要提取精确坐标或结构化表格提取，是否结合了传统 OCR 和布局解析工具辅助处理？
- [ ] 提示词是否足够开放，避免把模型的视觉判断引向歧途？
- [ ] 是否在多图比较的任务中，对不同的图像进行了明确的编号（Image 1, Image 2）并在指令中精准调用？

### 延伸阅读

#### 10.1 多模态大模型进展

- [GPT-4V(ision) System Card](https://cdn.openai.com/papers/GPTV_System_Card.pdf) - OpenAI 视觉大模型的官方技术报告
- [Gemini 1.5 Technical Report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf) - Gemini 官方技术报告

#### 10.2 多模态提示词指南

- [Anthropic Vision Guide](https://platform.claude.com/docs/en/build-with-claude/vision) - Claude 视觉提示词官方最佳实践
- [OpenAI Vision API](https://developers.openai.com/api/docs/guides/images-vision) - OpenAI 图像处理指南

### 下一章预告

大语言模型接入的自动化流程越来越多，其中一些还掌握敏感业务逻辑，安全性因此成为核心议题。[第十一章](../11_safety_reliability/README.md)讨论大模型常见的安全漏洞（如提示词注入）及其体系化防御手段。

---

[下一章：安全性与可靠性 →](../11_safety_reliability/README.md)
---

> 📝 **发现错误或有改进建议？** 欢迎提交 [Issue](https://github.com/yeasy/prompt_engineering_guide/issues) 或 [PR](https://github.com/yeasy/prompt_engineering_guide/pulls)。
