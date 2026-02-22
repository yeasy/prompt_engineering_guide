from __future__ import annotations

from dataclasses import dataclass
from typing import Any


def chat(*, model: str, messages: list[dict[str, str]], **kwargs: Any) -> dict[str, Any]:
    last_user = next((m["content"] for m in reversed(messages) if m.get("role") == "user"), "")
    return {"model": model, "message": {"role": "assistant", "content": f"(示例) 收到：{last_user}"}}

