from __future__ import annotations

from dataclasses import dataclass
from typing import Any


def init(*, project: str, **kwargs: Any) -> None:
    print(f"[wandb] init project={project}")


def log(metrics: dict[str, Any]) -> None:
    print(f"[wandb] log {metrics}")


@dataclass
class Trace:
    name: str
    kind: str
    inputs: dict[str, Any]
    outputs: dict[str, Any]
    metadata: dict[str, Any] | None = None

