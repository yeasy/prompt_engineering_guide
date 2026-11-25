import json
import re
import unittest
from pathlib import Path


CASE_STUDY = Path(__file__).resolve().parents[1] / "07_prompt_chaining" / "7.4_case_study.md"


class CompetitorAnalysisCaseStudyTests(unittest.TestCase):
    def test_workflow_templates_preserve_json_after_substitution(self):
        templates = re.findall(
            r"^(`{3,4})markdown\n(.*?)^\1$",
            CASE_STUDY.read_text(encoding="utf-8"),
            re.MULTILINE | re.DOTALL,
        )
        steps = (
            (("raw_product_info",), {"target_product", "competitors"}),
            (
                ("step1_output",),
                {"feature_matrix", "target_advantages", "target_disadvantages", "analysis_summary"},
            ),
            (
                ("step1_output",),
                {"pricing_comparison", "pricing_strategy_analysis", "price_competitiveness"},
            ),
            (
                ("step2_output", "step3_output"),
                {"strengths", "weaknesses", "opportunities", "threats"},
            ),
            (("step1_output", "step2_output", "step3_output", "step4_output"), set()),
            (("step5_output",), {"quality_score", "issues_found", "suggestions", "approved"}),
        )
        for number, ((_, template), (fields, output_keys)) in enumerate(
            zip(templates, steps, strict=True), 1
        ):
            with self.subTest(step=number):
                inputs = {field: json.dumps({field: "{literal}"}) for field in fields}
                prompt = template.format(**inputs)
                for value in inputs.values():
                    self.assertIn(value, prompt)
                example = re.search(r"^```\n(.*?)\n```$", prompt, re.MULTILINE | re.DOTALL)
                if output_keys:
                    self.assertIsNotNone(example)
                    self.assertEqual(set(json.loads(example.group(1))), output_keys)
                else:
                    self.assertIsNone(example)
