from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class _ParsedMessage:
    parsed: Any
    content: str | None = None


@dataclass
class _Choice:
    message: _ParsedMessage


@dataclass
class _Response:
    choices: list[_Choice]


def _safe_json(obj: Any) -> str:
    try:
        return json.dumps(obj, ensure_ascii=False)
    except TypeError:
        return json.dumps(str(obj), ensure_ascii=False)


class _ChatCompletions:
    def create(self, *, model: str, messages: list[dict[str, str]], **kwargs: Any) -> _Response:
        user_text = ""
        for m in messages:
            if m.get("role") == "user":
                user_text = m.get("content", "")
        content = _safe_json({"model": model, "echo": user_text, "kwargs": kwargs})
        return _Response(choices=[_Choice(message=_ParsedMessage(parsed=None, content=content))])


class _BetaChatCompletions:
    def parse(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        response_format: Callable[..., Any],
        **kwargs: Any,
    ) -> _Response:
        sample = {
            "product_name": "智能手表",
            "sentiment": "positive",
            "key_points": ["续航优秀", "佩戴舒适"],
            "confidence_score": 0.92,
        }
        try:
            parsed = response_format(**sample)  # pydantic/dataclass-like
        except Exception:
            parsed = sample
        content = _safe_json(sample)
        return _Response(choices=[_Choice(message=_ParsedMessage(parsed=parsed, content=content))])


class _Chat:
    def __init__(self) -> None:
        self.completions = _ChatCompletions()


class _BetaChat:
    def __init__(self) -> None:
        self.completions = _BetaChatCompletions()


class _Beta:
    def __init__(self) -> None:
        self.chat = _BetaChat()


class OpenAI:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.chat = _Chat()
        self.beta = _Beta()

