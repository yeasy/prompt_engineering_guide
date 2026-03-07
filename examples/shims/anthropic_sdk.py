from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ContentBlock:
    type: str
    thinking: str | None = None
    text: str | None = None


@dataclass
class MessageResponse:
    content: list[ContentBlock]


class _Messages:
    def create(self, *, model: str, max_tokens: int, messages: list[dict[str, str]], thinking: dict[str, Any] | None = None) -> MessageResponse:
        last = messages[-1]["content"] if messages else ""
        prefill = ""
        for m in messages:
            if m.get("role") == "assistant":
                prefill = m.get("content", "")
        text = (prefill + ' "mixed", "details": "示例输出"}').strip()
        blocks: list[ContentBlock] = []
        if thinking and thinking.get("type") == "enabled":
            blocks.append(ContentBlock(type="thinking", thinking="(示例) 内部推理内容已折叠"))
        blocks.append(ContentBlock(type="text", text=f"[{model}] {text or last}"))
        return MessageResponse(content=blocks)


class Anthropic:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.messages = _Messages()

