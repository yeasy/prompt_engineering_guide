from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github/workflows"
EXPECTED = ("ci.yaml", "preview-pdf.yml", "auto-release.yml", "dependabot-automerge.yml")
PUBLICATION_WORKFLOWS = ("ci.yaml", "preview-pdf.yml", "auto-release.yml")
FULL_SHA = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")
STEPS = ("Synchronize mutable preview tag", "Create or update preview release", "Replace preview assets")


FAKE_GH = r'''#!/usr/bin/env python3
import json, os, sys
args = sys.argv[1:]
with open(os.environ["GH_LOG"], "a", encoding="utf-8") as stream:
    stream.write(json.dumps(args) + "\n")
scenario = os.environ["GH_SCENARIO"]
repo, sha = "owner/repo", "a" * 40
get_ref = ["api", "--include", "--method", "GET", f"repos/{repo}/git/ref/tags/preview-pdf"]
if args == get_ref:
    if scenario.startswith("ref_404"):
        print("HTTP/2.0 404 Not Found"); raise SystemExit(1)
    if scenario.startswith("ref_200"):
        print("HTTP/2.0 200 OK"); raise SystemExit(0)
    print("HTTP/2.0 503 Error"); raise SystemExit(1)
if args == ["release", "view", "preview-pdf"]:
    if "release_missing" in scenario:
        print("release not found", file=sys.stderr); raise SystemExit(1)
    if "release_unauthorized" in scenario:
        print("HTTP 401", file=sys.stderr); raise SystemExit(1)
    raise SystemExit(0)
if args[:3] in (["api", "--silent", "--method"], ["release", "edit", "preview-pdf"], ["release", "create", "preview-pdf"], ["release", "upload", "preview-pdf"]):
    raise SystemExit(0)
print(f"unexpected argv: {args!r}", file=sys.stderr); raise SystemExit(2)
'''


def step_names(text: str) -> list[str]:
    publish = text.split("\n  publish:\n", 1)[1]
    return [
        match.group(1).strip()
        for match in re.finditer(r"(?m)^      - name:\s*(.+?)\s*$", publish)
        if match.group(1).strip() in STEPS
    ]


def step_script(text: str, name: str) -> str:
    marker = f"      - name: {name}\n"
    start = text.index(marker) + len(marker)
    run = text.index("        run: |\n", start) + len("        run: |\n")
    end = text.find("\n      - name:", run)
    return textwrap.dedent(text[run : end if end >= 0 else len(text)])


class WorkflowSafetyTests(unittest.TestCase):
    def text(self, name: str) -> str:
        return (WORKFLOWS / name).read_text(encoding="utf-8")

    def test_actions_are_full_sha_pinned_and_checkout_is_non_persistent(self):
        failures = []
        for name in EXPECTED:
            lines = self.text(name).splitlines()
            for number, line in enumerate(lines, 1):
                match = re.search(r"\buses:\s*([^\s#]+)(?:\s+#\s*(\S+))?", line)
                if match and (not FULL_SHA.fullmatch(match.group(1)) or not (match.group(2) or "").startswith("v")):
                    failures.append(f"{name}:{number}:{line.strip()}")
                if "uses: actions/checkout@" in line:
                    self.assertIn("persist-credentials: false", "\n".join(lines[number - 1 : number + 8]))
        self.assertEqual(failures, [])

    def test_publication_workflows_build_and_verify_pdf_html_strictly(self):
        for name in EXPECTED:
            self.assertIn("\npermissions: {}\n", self.text(name), name)
        required = (
            "checksums.txt",
            "PANDOC_SHA256",
            "sha256sum -c -",
            "npm ci --prefix tools/mermaid --ignore-scripts",
            "python3 -m unittest discover",
            "check_project_rules.py",
            "tools/render_mermaid.py",
            "--strict",
            "tools/build_html_reader.py",
            "tools/verify_artifacts.py",
            "SHA256SUMS",
            "if-no-files-found: error",
        )
        for name in PUBLICATION_WORKFLOWS:
            text = self.text(name)
            for marker in required:
                self.assertIn(marker, text, f"{name}: {marker}")
            self.assertNotIn("continue-on-error: true", text)
        release = self.text("auto-release.yml")
        self.assertIn("actions/attest-build-provenance@", release)
        self.assertIn("fail_on_unmatched_files: true", release)

    def test_mermaid_dependency_is_exactly_locked(self):
        package_path = ROOT / "tools/mermaid/package.json"
        lock_path = ROOT / "tools/mermaid/package-lock.json"
        self.assertTrue(package_path.is_file(), "Mermaid package manifest is missing")
        self.assertTrue(lock_path.is_file(), "Mermaid lockfile is missing")
        package = json.loads(package_path.read_text(encoding="utf-8"))
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
        self.assertEqual(package["dependencies"]["@mermaid-js/mermaid-cli"], "11.16.0")
        self.assertEqual(lock["packages"][""]["dependencies"]["@mermaid-js/mermaid-cli"], "11.16.0")

    def run_preview(self, scenario: str):
        text = self.text("preview-pdf.yml")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fake = root / "gh"
            fake.write_text(FAKE_GH, encoding="utf-8")
            fake.chmod(0o755)
            log = root / "log"
            env = os.environ.copy()
            env.update(
                {
                    "PATH": f"{root}{os.pathsep}{env['PATH']}",
                    "GH_LOG": str(log),
                    "GH_SCENARIO": scenario,
                    "GH_REPO": "owner/repo",
                    "GITHUB_SHA": "a" * 40,
                    "GH_TOKEN": "test",
                }
            )
            result = None
            for name in step_names(text):
                result = subprocess.run(
                    ["/bin/bash", "-c", step_script(text, name)],
                    cwd=ROOT,
                    env=env,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                if result.returncode:
                    break
            commands = [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []
            return result, commands

    def test_preview_order_and_404_only_creation(self):
        text = self.text("preview-pdf.yml")
        self.assertIn("\n  publish:\n", text)
        self.assertEqual(step_names(text), list(STEPS))
        success, commands = self.run_preview("ref_404_release_missing")
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertTrue(any(command[:3] == ["release", "create", "preview-pdf"] for command in commands))

        unauthorized, commands = self.run_preview("ref_200_release_unauthorized")
        self.assertNotEqual(unauthorized.returncode, 0)
        self.assertFalse(any(command[:3] == ["release", "create", "preview-pdf"] for command in commands))

        unavailable, commands = self.run_preview("ref_503")
        self.assertNotEqual(unavailable.returncode, 0)
        self.assertEqual(len(commands), 1)

    def test_preview_release_notes_preserve_short_sha_and_branch_as_markdown(self):
        script = step_script(self.text("preview-pdf.yml"), "Write release notes")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dist").mkdir()
            env = os.environ.copy()
            env.update(
                {
                    "GITHUB_SHA": "8279d934da2a49afa9f331c895f1ace5cf1b954f",
                    "GITHUB_REF_NAME": "feature/release-notes",
                    "GITHUB_RUN_ID": "12345",
                    "GH_REPO": "owner/repo",
                }
            )
            result = subprocess.run(
                ["/bin/bash", "-euo", "pipefail", "-c", script],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
                check=False,
            )
            notes = (root / "dist/release-notes.md").read_text(encoding="utf-8")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("command not found", result.stderr)
        self.assertIn("`8279d93`", notes)
        self.assertIn("`feature/release-notes`", notes)
        self.assertIn("https://github.com/owner/repo/commit/8279d934", notes)

    def test_dependabot_checks_before_approve_and_merge(self):
        text = self.text("dependabot-automerge.yml")
        check = text.index("Confirm required checks are configured")
        approve = text.index("Approve low-risk Dependabot PR")
        merge = text.index("Enable auto-merge for low-risk Dependabot PRs")
        self.assertLess(check, approve)
        self.assertLess(approve, merge)


if __name__ == "__main__":
    unittest.main()
