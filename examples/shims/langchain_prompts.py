from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


@dataclass
class PromptTemplate:
    input_variables: list[str]
    template: str

    def format(self, **kwargs: Any) -> str:
        return self.template.format(**kwargs)


@dataclass
class ChatPromptTemplate:
    _messages: list[tuple[str, str]]

    @classmethod
    def from_messages(cls, messages: Iterable[tuple[str, str]]) -> "ChatPromptTemplate":
        return cls(list(messages))

    def format(self, **kwargs: Any) -> list[dict[str, str]]:
        rendered: list[dict[str, str]] = []
        for role, content in self._messages:
            rendered.append({"role": role, "content": content.format(**kwargs)})
        return rendered


@dataclass
class FewShotPromptTemplate:
    examples: list[dict[str, Any]]
    example_prompt: PromptTemplate
    prefix: str
    suffix: str
    input_variables: list[str]

    def format(self, **kwargs: Any) -> str:
        example_text = "\n\n".join(self.example_prompt.format(**ex) for ex in self.examples)
        suffix = self.suffix.format(**kwargs)
        parts = [self.prefix.strip(), example_text.strip(), suffix.strip()]
        return "\n\n".join(p for p in parts if p)

