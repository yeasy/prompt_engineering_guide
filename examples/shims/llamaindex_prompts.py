from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class PromptTemplate:
    template: str

    def format(self, **kwargs: Any) -> str:
        return self.template.format(**kwargs)

