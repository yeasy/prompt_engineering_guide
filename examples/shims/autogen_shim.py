from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class AssistantAgent:
    name: str
    system_message: str
    llm_config: dict[str, Any] | None = None


@dataclass
class UserProxyAgent:
    name: str


@dataclass
class GroupChat:
    agents: list[Any]
    messages: list[Any]

