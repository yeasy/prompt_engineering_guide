from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools/render_mermaid.py"


class RenderMermaidTests(unittest.TestCase):
    def book(self, root: Path, diagrams: int = 1) -> Path:
        book = root / "book"
        book.mkdir()
        (book / "marker").write_text("keep", encoding="utf-8")
        (book / "SUMMARY.md").write_text("* [C](c.md)\n", encoding="utf-8")
        (book / "c.md").write_text(
            "\n".join(f"```mermaid\ngraph TD\nA{i}-->B{i}\n```" for i in range(diagrams)),
            encoding="utf-8",
        )
        return book

    def fake_tools(self, root: Path, partial: bool = False, hang: bool = False) -> tuple[Path, Path]:
        binary = root / "bin"
        binary.mkdir()
        chrome = binary / "chrome"
        chrome.write_text("", encoding="utf-8")
        mmdc = binary / "mmdc"
        count_expr = "1 if 'A0-->B0' in text else 0" if partial else "text.count('```mermaid')"
        delay = "import time; time.sleep(3)" if hang else ""
        mmdc.write_text(
            textwrap.dedent(
                f"""\
                #!{sys.executable}
                import pathlib, sys
                args = sys.argv[1:]
                {delay}
                src = pathlib.Path(args[args.index('-i') + 1])
                out = pathlib.Path(args[args.index('-o') + 1])
                text = src.read_text()
                count = {count_expr}
                for i in range(1, count + 1):
                    out.with_name(f'{{out.stem}}-{{i}}.svg').write_text('<svg></svg>')
                """
            ),
            encoding="utf-8",
        )
        mmdc.chmod(0o755)
        return binary, chrome

    def run_renderer(self, book: Path, output: Path, env: dict[str, str], *flags: str):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--book-dir", str(book), "--svg-out", str(output), "--strict", *flags],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_output_must_not_overlap_source_and_unrelated_files_survive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = self.book(root)
            result = self.run_renderer(book, book / "svg", os.environ.copy())
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue((book / "marker").is_file())

            output = root / "output"
            output.mkdir()
            (output / "keep.txt").write_text("keep", encoding="utf-8")
            binary, chrome = self.fake_tools(root)
            env = os.environ.copy()
            env.update({"PATH": f"{binary}{os.pathsep}{env['PATH']}", "CHROME_BIN": str(chrome)})
            self.assertEqual(self.run_renderer(book, output, env).returncode, 0)
            self.assertTrue((output / "keep.txt").is_file())

    def test_strict_mode_fails_when_rendering_is_partial(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = self.book(root, 2)
            binary, chrome = self.fake_tools(root, partial=True)
            env = os.environ.copy()
            env.update({"PATH": f"{binary}{os.pathsep}{env['PATH']}", "CHROME_BIN": str(chrome)})
            result = self.run_renderer(book, root / "out", env)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("failed for diagrams", result.stderr)

    def test_hung_renderer_times_out_and_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = self.book(root)
            binary, chrome = self.fake_tools(root, hang=True)
            env = os.environ.copy()
            env.update({"PATH": f"{binary}{os.pathsep}{env['PATH']}", "CHROME_BIN": str(chrome)})
            result = self.run_renderer(book, root / "out", env, "--timeout", "1")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("timed out", result.stderr)


if __name__ == "__main__":
    unittest.main()
