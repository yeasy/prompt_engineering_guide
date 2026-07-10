from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools import build_html_reader


ROOT = Path(__file__).resolve().parents[1]


class HtmlReaderSafetyTests(unittest.TestCase):
    def test_summary_entry_cannot_escape_book_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = root / "book"
            book.mkdir()
            (root / "outside.md").write_text("outside", encoding="utf-8")
            (book / "SUMMARY.md").write_text("* [Escape](../outside.md)\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                build_html_reader.parse_summary(str(book))

    def test_builder_uses_isolated_temporary_directory(self):
        source = (ROOT / "tools/build_html_reader.py").read_text(encoding="utf-8")
        self.assertIn("TemporaryDirectory", source)
        self.assertNotIn('"_combined_tmp.md"', source)
        self.assertNotIn('"/tmp/_book_template.html"', source)


if __name__ == "__main__":
    unittest.main()
