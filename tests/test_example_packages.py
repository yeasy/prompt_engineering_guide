from __future__ import annotations

import ast
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGES_ROOT = ROOT / "examples/packages"
PACKAGE_NAMES = ("structured_extraction", "deterministic_workflow", "grounded_qa")
REQUIRED_FILES = ("prompt.md", "cases.jsonl", "schema.json", "grader.py", "manifest.json")
ALLOWED_PAID_TRIGGERS = ["schedule", "workflow_dispatch"]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_cases(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_grader(path: Path):
    spec = importlib.util.spec_from_file_location(f"grader_{path.parent.name}", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def assert_value_matches_schema(test: unittest.TestCase, value, schema: dict) -> None:
    expected_type = schema.get("type")
    if expected_type == "object":
        test.assertIsInstance(value, dict)
        for key in schema.get("required", []):
            test.assertIn(key, value)
        if schema.get("additionalProperties") is False:
            test.assertLessEqual(set(value), set(schema.get("properties", {})))
        for key, item in value.items():
            assert_value_matches_schema(test, item, schema["properties"][key])
    elif expected_type == "array":
        test.assertIsInstance(value, list)
        for item in value:
            assert_value_matches_schema(test, item, schema["items"])
    elif expected_type == "string":
        test.assertIsInstance(value, str)
        if "enum" in schema:
            test.assertIn(value, schema["enum"])
    elif expected_type == "integer":
        test.assertIsInstance(value, int)
    elif expected_type == "number":
        test.assertIsInstance(value, (int, float))
    elif expected_type == "boolean":
        test.assertIsInstance(value, bool)


class ExamplePackageTests(unittest.TestCase):
    def setUp(self):
        if not PACKAGES_ROOT.is_dir():
            self.fail("examples/packages is missing")

    def test_packages_have_required_files_and_manifest_contract(self):
        self.assertEqual(
            sorted(path.name for path in PACKAGES_ROOT.iterdir() if path.is_dir()),
            sorted(PACKAGE_NAMES),
        )
        for name in PACKAGE_NAMES:
            package = PACKAGES_ROOT / name
            with self.subTest(package=name):
                for filename in REQUIRED_FILES:
                    self.assertTrue((package / filename).is_file(), filename)
                manifest = load_json(package / "manifest.json")
                self.assertEqual(manifest["name"], name)
                self.assertEqual(manifest["version"], "1.0.0")
                self.assertEqual(manifest["execution"], "offline_deterministic")
                self.assertGreaterEqual(manifest["minimum_cases"], 3)
                trial = manifest["trial_contract"]
                self.assertGreaterEqual(trial["minimum_trials"], 3)
                self.assertEqual(trial["model_snapshot"], "required")
                self.assertGreater(trial["max_cost_usd_per_trial"], 0)
                self.assertGreater(trial["max_latency_ms"], 0)
                self.assertEqual(sorted(trial["paid_run_triggers"]), ALLOWED_PAID_TRIGGERS)
                self.assertEqual(
                    set(trial["required_record_fields"]),
                    {"trial_id", "model_snapshot", "cost_usd", "latency_ms", "passed"},
                )

    def test_cases_match_strict_schema_and_minimum_count(self):
        for name in PACKAGE_NAMES:
            package = PACKAGES_ROOT / name
            schema = load_json(package / "schema.json")
            cases = load_cases(package / "cases.jsonl")
            manifest = load_json(package / "manifest.json")
            with self.subTest(package=name):
                self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
                self.assertEqual(schema["type"], "object")
                self.assertFalse(schema["additionalProperties"])
                self.assertGreaterEqual(len(cases), manifest["minimum_cases"])
                self.assertEqual(len({case["id"] for case in cases}), len(cases))
                for case in cases:
                    self.assertEqual(set(case), {"id", "input", "expected"})
                    self.assertTrue(case["input"])
                    assert_value_matches_schema(self, case["expected"], schema)

    def test_graders_are_offline_deterministic_and_reject_negative_predictions(self):
        forbidden_imports = {"openai", "anthropic", "google", "requests", "httpx", "socket", "subprocess"}
        for name in PACKAGE_NAMES:
            package = PACKAGES_ROOT / name
            source = (package / "grader.py").read_text(encoding="utf-8")
            tree = ast.parse(source)
            imported = {
                alias.name.split(".")[0]
                for node in ast.walk(tree)
                if isinstance(node, (ast.Import, ast.ImportFrom))
                for alias in node.names
            }
            grader = load_grader(package / "grader.py")
            case = load_cases(package / "cases.jsonl")[0]
            positive_a = grader.grade(case["expected"], case["expected"])
            positive_b = grader.grade(case["expected"], case["expected"])
            negative = grader.grade({"__invalid__": True}, case["expected"])
            with self.subTest(package=name):
                self.assertFalse(imported & forbidden_imports)
                self.assertEqual(positive_a, positive_b)
                self.assertEqual(set(positive_a), {"pass", "score", "reason"})
                self.assertTrue(positive_a["pass"])
                self.assertEqual(positive_a["score"], 1.0)
                self.assertFalse(negative["pass"])
                self.assertEqual(negative["score"], 0.0)


if __name__ == "__main__":
    unittest.main()
