#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


PY_FENCE_START_RE = re.compile(r"^```python\s*$")
ANY_FENCE_START_RE = re.compile(r"^(```+|~~~+)([^`]*)$")


def _is_fence_end(line: str, fence: str) -> bool:
    # Closing fence: same marker char, at least same length, and nothing else.
    stripped = line.strip()
    if not stripped:
        return False
    if not stripped.startswith(fence[0] * len(fence)):
        return False
    return stripped == fence[0] * len(stripped)


@dataclass(frozen=True)
class Snippet:
    source_path: Path
    start_line: int
    code: str


def iter_markdown_files(repo_root: Path) -> list[Path]:
    md_files: list[Path] = []
    for path in repo_root.rglob("*.md"):
        parts = set(path.parts)
        if "node_modules" in parts or "_book" in parts:
            continue
        md_files.append(path)
    return sorted(md_files)


def extract_python_snippets(path: Path) -> list[Snippet]:
    lines = path.read_text(encoding="utf-8").splitlines()
    snippets: list[Snippet] = []

    in_python_fence = False
    buf: list[str] = []
    fence_start_line = 0
    active_fence: str | None = None  # tracks any fence (```... or ~~~...)

    for idx, line in enumerate(lines, start=1):
        if active_fence is None:
            m = ANY_FENCE_START_RE.match(line)
            if not m:
                continue

            fence = m.group(1)
            active_fence = fence

            if PY_FENCE_START_RE.match(line):
                in_python_fence = True
            fence_start_line = idx
            buf = []
            continue

        if active_fence is not None and _is_fence_end(line, active_fence):
            if in_python_fence:
                snippets.append(
                    Snippet(
                        source_path=path,
                        start_line=fence_start_line,
                        code="\n".join(buf).rstrip() + "\n",
                    )
                )
            in_python_fence = False
            buf = []
            fence_start_line = 0
            active_fence = None
            continue

        if in_python_fence:
            buf.append(line)

    return snippets


def run_snippet(snippet: Snippet, repo_root: Path, timeout_s: int) -> tuple[bool, str]:
    program = snippet.code

    # --- INJECT SHIM SUBSTITUTIONS ---
    # To keep markdown examples using real SDKs but validate locally using shims
    program = re.sub(r"^(\s*)from openai import OpenAI", r"\1from examples.shims.openai_sdk import OpenAI", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from anthropic import Anthropic", r"\1from examples.shims.anthropic_sdk import Anthropic", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)import google\.generativeai as genai", r"\1from examples.shims import google_genai as genai", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from google\.generativeai\.types import GenerationConfig", r"\1from examples.shims.google_genai import GenerationConfig", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)import ollama", r"\1from examples.shims import ollama_shim as ollama", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from langchain_core\.prompts import", r"\1from examples.shims.langchain_prompts import", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from llama_index\.core import PromptTemplate", r"\1from examples.shims.llamaindex_prompts import PromptTemplate", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)import promptlayer", r"\1from examples.shims import promptlayer_shim as promptlayer", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)import wandb", r"\1from examples.shims import wandb_shim as wandb", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from wandb\.sdk\.data_types\.trace_tree import Trace", r"\1from examples.shims.wandb_shim import Trace", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)import dspy", r"\1from examples.shims import dspy_shim as dspy", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from dspy\.teleprompt import BootstrapFewShot", r"\1from examples.shims.dspy_shim import BootstrapFewShot", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from langgraph\.graph import", r"\1from examples.shims.langgraph_shim import", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from crewai import", r"\1from examples.shims.crewai_shim import", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)import autogen", r"\1from examples.shims import autogen_shim as autogen", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)from autogen import", r"\1from examples.shims.autogen_shim import", program, flags=re.MULTILINE)
    program = re.sub(r"^(\s*)import tiktoken", r"\1from examples.shims import tiktoken_shim as tiktoken", program, flags=re.MULTILINE)
    # --------------------------------

    with tempfile.TemporaryDirectory(prefix="pe_guide_snippet_") as td:
        tmp_path = Path(td) / "snippet.py"
        tmp_path.write_text(program, encoding="utf-8")

        env = dict(os.environ)
        env.setdefault("PYTHONWARNINGS", "ignore")
        env["PYTHONPATH"] = str(repo_root) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")

        try:
            proc = subprocess.run(
                [sys.executable, str(tmp_path)],
                cwd=str(repo_root),
                env=env,
                capture_output=True,
                text=True,
                timeout=timeout_s,
            )
        except subprocess.TimeoutExpired:
            return False, f"Timeout after {timeout_s}s"

        if proc.returncode == 0:
            return True, proc.stdout.strip()

        stderr = (proc.stderr or "").strip()
        stdout = (proc.stdout or "").strip()
        msg = "\n".join([s for s in [stdout, stderr] if s]).strip()
        return False, (msg or f"Exited with code {proc.returncode}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate runnable ```python snippets in markdown files.")
    parser.add_argument("--repo-root", default=".", help="Path to repo root (default: .)")
    parser.add_argument("--timeout-s", type=int, default=8, help="Per-snippet timeout in seconds (default: 8)")
    parser.add_argument("--max-failures", type=int, default=200, help="Stop after N failures (default: 200)")
    parser.add_argument("--verbose", action="store_true", help="Print full stderr/stdout for failures")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    md_files = iter_markdown_files(repo_root)

    snippets: list[Snippet] = []
    for md in md_files:
        snippets.extend(extract_python_snippets(md))

    failures: list[tuple[Snippet, str]] = []
    for snip in snippets:
        ok, out = run_snippet(snip, repo_root=repo_root, timeout_s=args.timeout_s)
        if not ok:
            failures.append((snip, out))
            if len(failures) >= args.max_failures:
                break

    print(f"Snippets found: {len(snippets)}")
    print(f"Failures: {len(failures)}")

    if failures:
        print("\nFailing snippets:")
        for snip, err in failures:
            rel = snip.source_path.relative_to(repo_root)
            print(f"- {rel}:{snip.start_line}: {one_line}")
            print(f"  Code: {snip.code.splitlines()[0]}")
            print(f"  Error details: {err}")

        if args.verbose:
            print("\nFailure details:")
            for snip, err in failures:
                rel = snip.source_path.relative_to(repo_root)
                print(f"\n--- {rel}:{snip.start_line} ---")
                print(err)
        print("\nTip: open the first failure and fix missing imports/deps/undefined names.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
