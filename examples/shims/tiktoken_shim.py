from __future__ import annotations

from dataclasses import dataclass


@dataclass
class _Encoding:
    name: str

    def encode(self, text: str) -> list[int]:
        # Extremely simplified: split on whitespace.
        return [hash(tok) % 10000 for tok in text.split()]


def get_encoding(name: str) -> _Encoding:
    return _Encoding(name=name)

