from __future__ import annotations

from dataclasses import dataclass
from typing import Any


def configure(*, api_key: str | None = None, **kwargs: Any) -> None:
    return None


class GenerativeModel:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def generate_content(self, parts: Any, **kwargs: Any) -> dict[str, Any]:
        return {
            "model": self.model_name,
            "parts_type": type(parts).__name__,
            "kwargs": kwargs,
            "text": "(示例) 生成内容",
        }


@dataclass
class GenerationConfig:
    response_mime_type: str | None = None
    response_schema: dict[str, Any] | None = None

