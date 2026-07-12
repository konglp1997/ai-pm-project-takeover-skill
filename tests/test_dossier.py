from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skill" / "ai-pm-project-takeover" / "scripts"
SCAFFOLD = SCRIPTS / "scaffold_dossier.py"
BUILD = SCRIPTS / "build_dossier.py"
VERIFY = SCRIPTS / "verify_dossier.py"


class DossierTest(unittest.TestCase):
    def run_tool(self, script: Path, target: Path, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, "-B", str(script), str(target)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(result.returncode, expected, msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        return result

    def scaffold(self, target: Path) -> None:
        self.run_tool(SCAFFOLD, target)

    def build(self, target: Path) -> None:
        self.run_tool(BUILD, target)

    def test_full_twenty_page_pipeline(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            self.build(target)
            result = self.run_tool(VERIFY, target)
            self.assertIn("Checked 20 page(s)", result.stdout)
            self.assertIn("Verification passed", result.stdout)
            self.assertTrue((target / "index.html").is_file())
            self.assertTrue((target / "pages" / "ai-system.html").is_file())
            self.assertTrue((target / "pages" / "takeover-plan.html").is_file())
            self.assertTrue((target / "assets" / "search-index.js").is_file())

    def test_scaffold_preserves_existing_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            config = target / "dossier.json"
            config.write_text('{"sentinel": true}\n', encoding="utf-8")
            result = self.run_tool(SCAFFOLD, target)
            self.assertEqual(config.read_text(encoding="utf-8"), '{"sentinel": true}\n')
            self.assertIn("preserved 24 existing file(s)", result.stdout)

    def test_required_chapter_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            path = target / "dossier.json"
            config = json.loads(path.read_text(encoding="utf-8"))
            for section in config["sections"]:
                section["pages"] = [page for page in section["pages"] if page["slug"] != "product-debt"]
            path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            self.build(target)
            result = self.run_tool(VERIFY, target, 1)
            self.assertIn("required AI PM chapter missing: product-debt", result.stderr)

    def test_unknown_page_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            page = target / "content" / "executive-brief.html"
            page.write_text(page.read_text(encoding="utf-8") + '\n<a href="page:not-configured">Bad</a>\n', encoding="utf-8")
            self.build(target)
            result = self.run_tool(VERIFY, target, 1)
            self.assertIn("page:not-configured is not configured", result.stderr)

    def test_secret_is_reported_without_value(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            secret = "sk-" + "A" * 32
            page = target / "content" / "ai-system.html"
            page.write_text(page.read_text(encoding="utf-8") + f"\n<pre><code>{secret}</code></pre>\n", encoding="utf-8")
            self.build(target)
            result = self.run_tool(VERIFY, target, 1)
            combined = result.stdout + result.stderr
            self.assertIn("possible OpenAI-style token", combined)
            self.assertNotIn(secret, combined)

    def test_page_requires_source_or_rationale(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            path = target / "dossier.json"
            config = json.loads(path.read_text(encoding="utf-8"))
            page = config["sections"][0]["pages"][1]
            page["sources"] = []
            page.pop("rationale", None)
            path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            self.build(target)
            result = self.run_tool(VERIFY, target, 1)
            self.assertIn("add sources or a rationale", result.stderr)

    def test_unsafe_href_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            page = target / "content" / "index.html"
            page.write_text(page.read_text(encoding="utf-8") + '\n<a href="javascript:alert(1)">Bad</a>\n', encoding="utf-8")
            self.build(target)
            result = self.run_tool(VERIFY, target, 1)
            self.assertIn("unsafe href scheme", result.stderr)

    def test_remote_css_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            style = target / "assets" / "style.css"
            style.write_text(style.read_text(encoding="utf-8") + '\n@import url("https://example.invalid/x.css");\n', encoding="utf-8")
            self.build(target)
            result = self.run_tool(VERIFY, target, 1)
            self.assertIn("@import is not allowed", result.stderr)

    def test_asset_traversal_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "dossier"
            self.scaffold(target)
            page = target / "content" / "index.html"
            page.write_text(page.read_text(encoding="utf-8") + '\n<img src="asset:../private.png" alt="Bad path">\n', encoding="utf-8")
            self.build(target)
            result = self.run_tool(VERIFY, target, 1)
            self.assertIn("unsafe asset path", result.stderr)


if __name__ == "__main__":
    unittest.main()
