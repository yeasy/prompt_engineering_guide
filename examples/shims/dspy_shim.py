from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


class Signature:
    pass


class InputField:
    def __init__(self, **kwargs: Any) -> None:
        self.kwargs = kwargs


class OutputField:
    def __init__(self, **kwargs: Any) -> None:
        self.kwargs = kwargs


@dataclass
class ChainOfThought:
    signature: type[Signature]


class BootstrapFewShot:
    def __init__(self, metric: Callable[..., Any]) -> None:
        self.metric = metric

    def compile(self, module: Any, trainset: list[dict[str, Any]]) -> Any:
        return module

