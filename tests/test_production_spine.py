from __future__ import annotations

import unittest
from pathlib import Path
import re

import check_project_rules as rules


ROOT = Path(__file__).resolve().parents[1]
SPINE = ROOT / "appendix/i_production_spine.md"
STAGES = (
    "prompt-contract",
    "eval",
    "context",
    "deterministic-workflow",
    "single-agent",
    "multi-agent",
)


class ProductionSpineTests(unittest.TestCase):
    def setUp(self):
        if not SPINE.is_file():
            self.fail("production spine is missing")

    def test_spine_is_linked_without_renumbering_existing_chapters(self):
        summary = (ROOT / "SUMMARY.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("appendix/i_production_spine.md", summary)
        self.assertIn("appendix/i_production_spine.md", readme)
        self.assertIn("第十四章", summary)

    def test_six_stages_are_ordered_and_have_acceptance_artifacts(self):
        text = SPINE.read_text(encoding="utf-8")
        positions = []
        for order, stage in enumerate(STAGES, 1):
            marker = f"<!-- production-stage: order={order} id={stage}"
            positions.append(text.index(marker))
            self.assertRegex(
                text,
                rf"<!-- production-stage: order={order} id={stage} link=[^ ]+ artifact=[^ ]+ -->",
            )
        self.assertEqual(positions, sorted(positions))

    def test_checker_enforces_production_spine_contract(self):
        check = getattr(rules, "check_production_spine", lambda **_: ["missing checker"])
        self.assertEqual(check(root=ROOT), [])

    def test_package_prompts_are_in_publication_graph(self):
        summary = (ROOT / "SUMMARY.md").read_text(encoding="utf-8")
        for package in ("structured_extraction", "deterministic_workflow", "grounded_qa"):
            self.assertIn(f"examples/packages/{package}/prompt.md", summary)

    def test_summary_titles_match_first_source_heading(self):
        mismatches = []
        for number, line in enumerate((ROOT / "SUMMARY.md").read_text(encoding="utf-8").splitlines(), 1):
            match = re.match(r"^\s*[-*]\s+\[([^]]+)\]\(([^)#]+\.md)", line)
            if not match:
                continue
            title, relative = match.groups()
            path = ROOT / relative
            if not path.is_file():
                continue
            heading = next(
                (item.lstrip("# ").strip() for item in path.read_text(encoding="utf-8").splitlines() if item.startswith("#")),
                "",
            )
            if title != heading:
                mismatches.append(f"SUMMARY.md:{number}: {title!r} != {relative}:{heading!r}")
        self.assertEqual(mismatches, [])


if __name__ == "__main__":
    unittest.main()
