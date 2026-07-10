from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

import check_project_rules as rules


ROOT = Path(__file__).resolve().parents[1]


class VolatileFactsContractTests(unittest.TestCase):
    def test_repository_volatile_facts_are_current_and_consistent(self):
        check = getattr(rules, "check_volatile_facts", lambda **_: ["missing checker"])
        self.assertEqual(check(root=ROOT, as_of=date(2026, 7, 10)), [])

    def test_contract_expires_after_exact_thirty_day_ttl(self):
        check = getattr(rules, "check_volatile_facts", lambda **_: ["missing checker"])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            appendix = root / "appendix"
            appendix.mkdir()
            (appendix / "h_volatile_facts.md").write_text(
                "# Facts\n\n"
                "<!-- volatile-meta: verified_at=2026-07-10 expires_at=2026-08-09 ttl_days=30 -->\n"
                "<!-- volatile-status: id=current-fact status=current -->\n",
                encoding="utf-8",
            )
            issues = check(root=root, as_of=date(2026, 8, 10), required_fact_ids=set())
        self.assertTrue(any("expired" in issue for issue in issues), issues)

    def test_future_conflict_and_resolved_transition_require_dates(self):
        check = getattr(rules, "check_volatile_facts", lambda **_: ["missing checker"])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            appendix = root / "appendix"
            appendix.mkdir()
            (appendix / "h_volatile_facts.md").write_text(
                "# Facts\n\n"
                "<!-- volatile-meta: verified_at=2026-07-10 expires_at=2026-08-09 ttl_days=30 -->\n"
                "<!-- volatile-status: id=future-fact status=future -->\n"
                "<!-- volatile-status: id=conflict-fact status=conflict -->\n"
                "<!-- volatile-status: id=resolved-fact status=resolved-conflict previous=current -->\n",
                encoding="utf-8",
            )
            issues = check(root=root, as_of=date(2026, 7, 10), required_fact_ids=set())
        joined = "\n".join(issues)
        self.assertIn("future-fact", joined)
        self.assertIn("effective_at", joined)
        self.assertIn("conflict-fact", joined)
        self.assertIn("next_review_at", joined)
        self.assertIn("resolved-fact", joined)
        self.assertIn("previous=conflict", joined)
        self.assertIn("resolved_at", joined)

    def test_current_provider_facts_and_official_sources_are_present(self):
        text = (ROOT / "appendix/h_volatile_facts.md").read_text(encoding="utf-8")
        required = (
            "gpt-5.6-sol",
            "gpt-5.6-terra",
            "gpt-5.6-luna",
            "https://developers.openai.com/api/docs/changelog",
            "claude-sonnet-5",
            "Claude Fable 5",
            "https://platform.claude.com/docs/en/release-notes/overview",
            "gemini-3.5-flash",
            "gemini-3.1-pro-preview",
            "https://ai.google.dev/gemini-api/docs/models",
        )
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, text)

    def test_repeated_model_platform_and_future_chapters_match_ledger(self):
        check = getattr(rules, "check_volatile_mirrors", lambda **_: ["missing checker"])
        self.assertEqual(check(root=ROOT), [])

    def test_retired_provider_claims_do_not_remain_in_active_prose(self):
        stale_claims = (
            "2026-06-12 起访问暂停",
            "GPT-5.5 | 官方当前前沿模型",
            "当前复杂任务默认候选",
        )
        offenders: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", ".agent", "node_modules"} for part in path.parts):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for stale in stale_claims:
                if stale in text:
                    offenders.append(f"{path.relative_to(ROOT)}: {stale}")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
