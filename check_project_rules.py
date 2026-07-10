#!/usr/bin/env python3
"""Lightweight Markdown project checks for book repositories."""

from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {
    ".agent",
    ".git",
    ".mdpress",
    "_book",
    "_site",
    "dist",
    "node_modules",
}
LINK_RE = re.compile(r"(!?)\[[^\]]*\]\(([^)\s]+(?:\s+\"[^\"]*\")?)\)")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
VOLATILE_META_RE = re.compile(
    r"<!--\s*volatile-meta:\s*verified_at=(\d{4}-\d{2}-\d{2})\s+"
    r"expires_at=(\d{4}-\d{2}-\d{2})\s+ttl_days=(\d+)\s*-->"
)
VOLATILE_STATUS_RE = re.compile(r"<!--\s*volatile-status:\s*(.*?)\s*-->")
VOLATILE_ATTR_RE = re.compile(r"([a-z_]+)=([^\s]+)")
PRODUCTION_STAGE_RE = re.compile(
    r"<!--\s*production-stage:\s*order=(\d+)\s+id=([^\s]+)\s+"
    r"link=([^\s]+)\s+artifact=([^\s]+)\s*-->"
)
PRODUCTION_STAGE_ORDER = (
    "prompt-contract",
    "eval",
    "context",
    "deterministic-workflow",
    "single-agent",
    "multi-agent",
)
REQUIRED_VOLATILE_FACT_IDS = {
    "openai-gpt-5.6",
    "anthropic-sonnet-5",
    "anthropic-fable-access",
    "anthropic-sonnet-pricing",
    "google-gemini-models",
}
VOLATILE_MIRRORS = {
    "openai-gpt-5.6": {
        "02_llm_basics/2.2_major_models.md": ("GPT-5.6",),
        "13_platform_specific/13.1_openai_gpt.md": (
            "gpt-5.6-sol",
            "gpt-5.6-terra",
            "gpt-5.6-luna",
            "Responses API",
        ),
        "13_platform_specific/summary.md": ("GPT-5.6",),
        "14_future/14.2_multi_agent.md": ("GPT-5.6", "beta"),
    },
    "anthropic-sonnet-5": {
        "02_llm_basics/2.2_major_models.md": ("Claude Sonnet 5",),
        "06_chain_of_thought/6.5_reasoning_models.md": ("Claude Sonnet 5",),
        "13_platform_specific/13.2_anthropic_claude.md": ("Claude Sonnet 5",),
        "13_platform_specific/summary.md": ("Claude Sonnet 5",),
    },
    "anthropic-fable-access": {
        "02_llm_basics/2.2_major_models.md": ("2026-07-01", "恢复"),
        "13_platform_specific/13.2_anthropic_claude.md": ("2026-07-01", "恢复"),
        "13_platform_specific/summary.md": ("2026-07-01", "恢复"),
    },
    "google-gemini-models": {
        "02_llm_basics/2.2_major_models.md": ("Gemini 3.5 Flash", "Gemini 3.1 Pro Preview"),
        "13_platform_specific/13.3_google_gemini.md": ("Stable", "Preview"),
        "13_platform_specific/summary.md": ("Stable", "Preview"),
    },
}


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def strip_fenced_blocks(text: str) -> str:
    output: list[str] = []
    in_fence = False
    fence_marker = ""
    fence_len = 0
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)
            char = marker[0]
            length = len(marker)
            if not in_fence:
                in_fence = True
                fence_marker = char
                fence_len = length
            elif char == fence_marker and length >= fence_len:
                in_fence = False
            output.append("")
            continue
        output.append("" if in_fence else line)
    return "\n".join(output)


def check_fences(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    stack: list[tuple[str, int, int]] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        match = FENCE_RE.match(line)
        if not match:
            continue
        marker = match.group(1)
        char = marker[0]
        length = len(marker)
        if not stack:
            stack.append((char, length, line_no))
            continue
        open_char, open_len, _ = stack[-1]
        if char == open_char and length >= open_len:
            stack.pop()
        else:
            stack.append((char, length, line_no))
    for _, _, line_no in stack:
        issues.append(f"{path.relative_to(ROOT)}:{line_no}: unclosed fenced code block")
    return issues


def is_local_target(target: str) -> bool:
    parsed = urlparse(target)
    return not parsed.scheme and not parsed.netloc and not target.startswith("#")


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if " " in target and target.count('"') >= 2:
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def check_links(path: Path, text: str) -> list[str]:
    issues: list[str] = []
    body = strip_fenced_blocks(text)
    for match in LINK_RE.finditer(body):
        raw_target = match.group(2).strip()
        target = normalize_target(raw_target)
        if not target or not is_local_target(raw_target):
            continue
        target_path = (path.parent / target).resolve()
        try:
            target_path.relative_to(ROOT)
        except ValueError:
            continue
        if not target_path.exists():
            line_no = body[: match.start()].count("\n") + 1
            issues.append(
                f"{path.relative_to(ROOT)}:{line_no}: missing local link target: {raw_target}"
            )
    return issues


def check_summary_links() -> list[str]:
    summary = ROOT / "SUMMARY.md"
    if not summary.exists():
        return []
    return check_links(summary, summary.read_text(encoding="utf-8", errors="ignore"))


def _parse_iso(value: str, field: str, issues: list[str]) -> date | None:
    try:
        return date.fromisoformat(value)
    except ValueError:
        issues.append(f"appendix/h_volatile_facts.md: invalid {field}={value!r}")
        return None


def check_volatile_facts(
    root: Path = ROOT,
    as_of: date | None = None,
    required_fact_ids: set[str] | None = None,
) -> list[str]:
    """Validate the dated volatile-fact ledger and its state transitions."""

    ledger = root / "appendix/h_volatile_facts.md"
    if not ledger.exists():
        return ["appendix/h_volatile_facts.md: missing volatile-fact ledger"]
    text = ledger.read_text(encoding="utf-8", errors="ignore")
    issues: list[str] = []
    meta = VOLATILE_META_RE.search(text)
    if not meta:
        return ["appendix/h_volatile_facts.md: missing volatile-meta contract"]
    verified = _parse_iso(meta.group(1), "verified_at", issues)
    expires = _parse_iso(meta.group(2), "expires_at", issues)
    ttl_days = int(meta.group(3))
    if ttl_days != 30:
        issues.append("appendix/h_volatile_facts.md: ttl_days must equal 30")
    if verified and expires and expires != verified + timedelta(days=ttl_days):
        issues.append("appendix/h_volatile_facts.md: expires_at must equal verified_at + ttl_days")
    today = as_of or date.today()
    if expires and today > expires:
        issues.append(f"appendix/h_volatile_facts.md: volatile facts expired on {expires.isoformat()}")

    observed: set[str] = set()
    for match in VOLATILE_STATUS_RE.finditer(text):
        attrs = dict(VOLATILE_ATTR_RE.findall(match.group(1)))
        fact_id = attrs.get("id", "<missing-id>")
        status = attrs.get("status", "<missing-status>")
        if fact_id in observed:
            issues.append(f"appendix/h_volatile_facts.md: duplicate volatile fact id {fact_id}")
        observed.add(fact_id)
        if status not in {"current", "future", "conflict", "resolved-conflict"}:
            issues.append(f"appendix/h_volatile_facts.md: {fact_id} has unknown status {status}")
            continue
        if status == "future":
            effective = attrs.get("effective_at")
            if not effective:
                issues.append(f"appendix/h_volatile_facts.md: {fact_id} future status requires effective_at")
            elif verified:
                parsed = _parse_iso(effective, f"{fact_id}.effective_at", issues)
                if parsed and parsed <= verified:
                    issues.append(f"appendix/h_volatile_facts.md: {fact_id} effective_at must be after verified_at")
        elif status == "conflict":
            if not attrs.get("next_review_at"):
                issues.append(f"appendix/h_volatile_facts.md: {fact_id} conflict status requires next_review_at")
        elif status == "resolved-conflict":
            if attrs.get("previous") != "conflict":
                issues.append(f"appendix/h_volatile_facts.md: {fact_id} requires previous=conflict")
            if not attrs.get("resolved_at"):
                issues.append(f"appendix/h_volatile_facts.md: {fact_id} resolved status requires resolved_at")

    required = REQUIRED_VOLATILE_FACT_IDS if required_fact_ids is None else required_fact_ids
    for missing in sorted(required - observed):
        issues.append(f"appendix/h_volatile_facts.md: missing volatile fact id {missing}")
    return issues


def check_volatile_mirrors(root: Path = ROOT) -> list[str]:
    """Ensure repeated model/platform/future guidance references the ledger."""

    issues: list[str] = []
    for fact_id, files in VOLATILE_MIRRORS.items():
        marker = f"<!-- volatile-ref: {fact_id} -->"
        for relative, required_tokens in files.items():
            path = root / relative
            if not path.exists():
                issues.append(f"{relative}: missing volatile mirror")
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if marker not in text:
                issues.append(f"{relative}: missing {marker}")
            for token in required_tokens:
                if token not in text:
                    issues.append(f"{relative}: volatile mirror {fact_id} missing {token!r}")
            if fact_id == "anthropic-fable-access" and "2026-06-12 起访问暂停" in text:
                issues.append(f"{relative}: stale Fable access suspension remains active")
    return issues


def check_production_spine(root: Path = ROOT) -> list[str]:
    """Validate the ordered production path without renumbering the book."""

    relative = Path("appendix/i_production_spine.md")
    path = root / relative
    if not path.exists():
        return [f"{relative}: missing production spine"]
    text = path.read_text(encoding="utf-8", errors="ignore")
    rows = PRODUCTION_STAGE_RE.findall(text)
    issues: list[str] = []
    if len(rows) != len(PRODUCTION_STAGE_ORDER):
        issues.append(f"{relative}: expected {len(PRODUCTION_STAGE_ORDER)} production stages")
        return issues
    for expected_order, expected_id in enumerate(PRODUCTION_STAGE_ORDER, 1):
        order_raw, stage_id, link, artifact = rows[expected_order - 1]
        if int(order_raw) != expected_order or stage_id != expected_id:
            issues.append(
                f"{relative}: stage {expected_order} must be {expected_id}, got {stage_id}"
            )
        target = (path.parent / link).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            issues.append(f"{relative}: stage {stage_id} link escapes repository")
        else:
            if not target.is_file():
                issues.append(f"{relative}: stage {stage_id} missing link target {link}")
        if not artifact or artifact in {"none", "TBD", "TODO"}:
            issues.append(f"{relative}: stage {stage_id} lacks an acceptance artifact")
    return issues


def main() -> int:
    issues: list[str] = []
    files = iter_markdown_files()
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        issues.extend(check_fences(path, text))
        issues.extend(check_links(path, text))
    issues.extend(check_summary_links())
    issues.extend(check_volatile_facts())
    issues.extend(check_volatile_mirrors())
    issues.extend(check_production_spine())

    if issues:
        print("\n".join(sorted(set(issues))))
        print(f"\n{len(set(issues))} issue(s) found across {len(files)} Markdown files.")
        return 1
    print(f"All {len(files)} Markdown files passed project checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
