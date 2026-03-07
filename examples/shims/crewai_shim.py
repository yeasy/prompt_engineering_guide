from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Agent:
    role: str
    goal: str
    backstory: str
    tools: list[Callable[..., Any]] | None = None


@dataclass
class Task:
    description: str
    agent: Agent
    context: list["Task"] | None = None


@dataclass
class Crew:
    agents: list[Agent]
    tasks: list[Task]

    def kickoff(self, inputs: dict[str, Any]) -> dict[str, Any]:
        return {"status": "ok", "inputs": inputs, "tasks": [t.description for t in self.tasks]}

