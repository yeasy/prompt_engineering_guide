from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


END = "__END__"


class _App:
    def __init__(self, initial: dict[str, Any], runner: Callable[[dict[str, Any]], dict[str, Any]]) -> None:
        self._runner = runner

    def invoke(self, state: dict[str, Any]) -> dict[str, Any]:
        return self._runner(state)


class StateGraph:
    def __init__(self, state_type: Any) -> None:
        self._nodes: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {}
        self._edges: dict[str, str] = {}
        self._conditional: tuple[str, Callable[[dict[str, Any]], str], dict[str, str]] | None = None

    def add_node(self, name: str, fn: Callable[[dict[str, Any]], dict[str, Any]]) -> None:
        self._nodes[name] = fn

    def add_edge(self, a: str, b: str) -> None:
        self._edges[a] = b

    def add_conditional_edges(self, a: str, cond: Callable[[dict[str, Any]], str], mapping: dict[str, str]) -> None:
        self._conditional = (a, cond, mapping)

    def compile(self) -> _App:
        def runner(state: dict[str, Any]) -> dict[str, Any]:
            current = next(iter(self._nodes.keys()), None)
            while current:
                state = dict(state)
                state.update(self._nodes[current](state))
                if self._conditional and self._conditional[0] == current:
                    key = self._conditional[1](state)
                    nxt = self._conditional[2].get(key)
                    if nxt == END:
                        break
                    current = nxt
                else:
                    current = self._edges.get(current)
            return state

        return _App({}, runner)

