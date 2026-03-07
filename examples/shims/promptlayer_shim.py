from __future__ import annotations

from dataclasses import dataclass
from typing import Any


api_key: str | None = None


@dataclass
class _PLResponse:
    model: str
    messages: list[dict[str, str]]
    pl_tags: list[str] | None = None


class _ChatCompletions:
    def create(self, *, model: str, messages: list[dict[str, str]], pl_tags: list[str] | None = None, **kwargs: Any) -> _PLResponse:
        return _PLResponse(model=model, messages=messages, pl_tags=pl_tags)


class _Chat:
    def __init__(self) -> None:
        self.completions = _ChatCompletions()


class _OpenAI:
    def __init__(self) -> None:
        self.chat = _Chat()


openai = _OpenAI()

