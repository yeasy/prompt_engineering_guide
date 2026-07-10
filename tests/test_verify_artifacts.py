from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    from tools import verify_artifacts as verifier
except ImportError:
    verifier = None


class ArtifactVerifierTests(unittest.TestCase):
    def setUp(self):
        if verifier is None:
            self.fail("tools.verify_artifacts is missing")

    def test_html_requires_title_all_mermaid_and_no_fallback(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            html = root / "book.html"
            html.write_text('<title>大模型提示词工程指南</title><figure class="diagram"><svg></svg></figure>')
            verifier.verify_html(html, "大模型提示词工程指南", 1)
            html.write_text('<title>大模型提示词工程指南</title><pre class="diagram-fallback">x</pre>')
            with self.assertRaises(verifier.ArtifactVerificationError):
                verifier.verify_html(html, "大模型提示词工程指南", 1)

    def test_pdf_signature_and_checksums_detect_tampering(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pdf = root / "book.pdf"
            html = root / "book.html"
            manifest = root / "SHA256SUMS"
            pdf.write_bytes(b"%PDF-1.7\nbody")
            html.write_text("html", encoding="utf-8")
            with mock.patch.object(verifier.shutil, "which", return_value="pdfinfo"), mock.patch.object(
                verifier, "command_output", return_value="Title: 大模型提示词工程指南\nPages: 10\n"
            ):
                verifier.verify_pdf(pdf, "大模型提示词工程指南")
            verifier.write_checksums([pdf, html], manifest)
            verifier.verify_checksums(manifest)
            html.write_text("changed", encoding="utf-8")
            with self.assertRaises(verifier.ArtifactVerificationError):
                verifier.verify_checksums(manifest)


if __name__ == "__main__":
    unittest.main()
