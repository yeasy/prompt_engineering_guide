from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

import check_project_rules as rules


ROOT = Path(__file__).resolve().parents[1]


class VolatileFactsContractTests(unittest.TestCase):
    def check_status(
        self,
        status: str,
        *,
        as_of: date,
        verified_at: str = "2026-07-10",
        expires_at: str = "2026-08-09",
    ) -> list[str]:
        check = getattr(rules, "check_volatile_facts", lambda **_: ["missing checker"])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            appendix = root / "appendix"
            appendix.mkdir()
            (appendix / "h_volatile_facts.md").write_text(
                "# Facts\n\n"
                f"<!-- volatile-meta: verified_at={verified_at} "
                f"expires_at={expires_at} ttl_days=30 -->\n"
                f"<!-- volatile-status: id=boundary-fact {status} -->\n",
                encoding="utf-8",
            )
            return check(root=root, as_of=as_of, required_fact_ids=set())

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

    def test_verification_date_cannot_be_future_and_expiry_is_inclusive(self):
        invalid_verified = self.check_status(
            "status=current",
            as_of=date(2026, 7, 10),
            verified_at="2026-02-30",
            expires_at="2026-04-01",
        )
        self.assertTrue(
            any("verified_at" in issue and "invalid" in issue for issue in invalid_verified),
            invalid_verified,
        )
        invalid_expiry = self.check_status(
            "status=current",
            as_of=date(2026, 7, 10),
            expires_at="2026-02-30",
        )
        self.assertTrue(
            any("expires_at" in issue and "invalid" in issue for issue in invalid_expiry),
            invalid_expiry,
        )
        future = self.check_status(
            "status=current",
            as_of=date(2026, 7, 10),
            verified_at="2026-07-11",
            expires_at="2026-08-10",
        )
        self.assertTrue(
            any("verified_at" in issue and "future" in issue for issue in future),
            future,
        )

        valid_on_expiry = self.check_status(
            "status=current",
            as_of=date(2026, 8, 9),
        )
        self.assertEqual(valid_on_expiry, [])
        expired_next_day = self.check_status(
            "status=current",
            as_of=date(2026, 8, 10),
        )
        self.assertTrue(any("expired" in issue for issue in expired_next_day))

        wrong_expiry = self.check_status(
            "status=current",
            as_of=date(2026, 7, 10),
            expires_at="2026-08-08",
        )
        self.assertTrue(any("expires_at must equal" in issue for issue in wrong_expiry))

    def test_future_status_requires_valid_date_and_transition_at_boundary(self):
        invalid = self.check_status(
            "status=future effective_at=not-a-date",
            as_of=date(2026, 7, 10),
        )
        self.assertTrue(any("effective_at" in issue and "invalid" in issue for issue in invalid), invalid)

        before = self.check_status(
            "status=future effective_at=2026-07-11",
            as_of=date(2026, 7, 10),
        )
        self.assertEqual(before, [])
        at_boundary = self.check_status(
            "status=future effective_at=2026-07-11",
            as_of=date(2026, 7, 11),
        )
        self.assertTrue(
            any("status=future" in issue and "transition" in issue for issue in at_boundary),
            at_boundary,
        )

    def test_conflict_review_date_is_valid_and_only_overdue_after_boundary(self):
        invalid = self.check_status(
            "status=conflict next_review_at=not-a-date",
            as_of=date(2026, 7, 10),
        )
        self.assertTrue(
            any("next_review_at" in issue and "invalid" in issue for issue in invalid),
            invalid,
        )

        on_review_date = self.check_status(
            "status=conflict next_review_at=2026-07-11",
            as_of=date(2026, 7, 11),
        )
        self.assertEqual(on_review_date, [])
        overdue = self.check_status(
            "status=conflict next_review_at=2026-07-11",
            as_of=date(2026, 7, 12),
        )
        self.assertTrue(
            any("status=conflict" in issue and "overdue" in issue for issue in overdue),
            overdue,
        )

    def test_resolved_conflict_date_is_valid_and_not_after_verification_or_as_of(self):
        valid_boundary = self.check_status(
            "status=resolved-conflict previous=conflict resolved_at=2026-07-10",
            as_of=date(2026, 7, 10),
        )
        self.assertEqual(valid_boundary, [])

        invalid = self.check_status(
            "status=resolved-conflict previous=conflict resolved_at=not-a-date",
            as_of=date(2026, 7, 10),
        )
        self.assertTrue(any("resolved_at" in issue and "invalid" in issue for issue in invalid), invalid)
        historical_resolution = self.check_status(
            "status=resolved-conflict previous=conflict resolved_at=2026-07-09",
            as_of=date(2026, 7, 10),
        )
        self.assertEqual(historical_resolution, [])

        after_verification = self.check_status(
            "status=resolved-conflict previous=conflict resolved_at=2026-07-11",
            as_of=date(2026, 7, 12),
        )
        self.assertTrue(
            any("status=resolved-conflict" in issue and "verified_at" in issue for issue in after_verification),
            after_verification,
        )
        after_today = self.check_status(
            "status=resolved-conflict previous=conflict resolved_at=2026-07-11",
            as_of=date(2026, 7, 10),
        )
        self.assertTrue(
            any("status=resolved-conflict" in issue and "as_of" in issue for issue in after_today),
            after_today,
        )

    def test_resolved_conflict_history_survives_the_next_ttl_verification(self):
        issues = self.check_status(
            "status=resolved-conflict previous=conflict resolved_at=2026-07-10",
            as_of=date(2026, 8, 1),
            verified_at="2026-08-01",
            expires_at="2026-08-31",
        )
        self.assertEqual(issues, [])

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
