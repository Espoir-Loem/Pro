import tempfile
import unittest
from pathlib import Path

import check_code_style


class TestComments(unittest.TestCase):
    def test_typescript_accepts_doc_comment(self):
        failures = check_code_style.check_text("/** Doc. */\nexport const value = 1;\n", "a.ts")
        self.assertEqual(failures, [])

    def test_typescript_rejects_line_comment(self):
        failures = check_code_style.check_text("// note\nexport const value = 1;\n", "a.ts")
        self.assertTrue(any("commentaire" in failure for failure in failures))

    def test_typescript_rejects_plain_block_comment(self):
        failures = check_code_style.check_text("/* note */\nexport const value = 1;\n", "a.ts")
        self.assertTrue(any("commentaire" in failure for failure in failures))

    def test_rust_accepts_doc_comment(self):
        failures = check_code_style.check_text("/// Doc.\nfn main() {}\n", "a.rs")
        self.assertEqual(failures, [])

    def test_rust_rejects_line_comment(self):
        failures = check_code_style.check_text("// note\nfn main() {}\n", "a.rs")
        self.assertTrue(any("commentaire" in failure for failure in failures))

    def test_url_inside_string_is_not_a_comment(self):
        failures = check_code_style.check_text('const url = "https://example.com";\n', "a.ts")
        self.assertEqual(failures, [])


class TestMaps(unittest.TestCase):
    def test_accepts_single_map(self):
        failures = check_code_style.check_text("items.map(render)\n", "a.tsx")
        self.assertEqual(failures, [])

    def test_rejects_two_maps(self):
        failures = check_code_style.check_text("items.map(render)\nothers.map(render)\n", "a.tsx")
        self.assertTrue(any("map" in failure for failure in failures))


class TestRunChecks(unittest.TestCase):
    def test_accepts_clean_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            app = root / "apps" / "web"
            app.mkdir(parents=True)
            (app / "a.tsx").write_text("/** Doc. */\nexport const view = () => null;\n", encoding="utf-8")
            report = check_code_style.run_checks(root)
            self.assertEqual(report.failures, [])
            self.assertEqual(report.files, 1)

    def test_detects_bad_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            app = root / "apps" / "web"
            app.mkdir(parents=True)
            (app / "a.ts").write_text("// note\nexport const value = 1;\n", encoding="utf-8")
            report = check_code_style.run_checks(root)
            self.assertTrue(report.failures)


if __name__ == "__main__":
    unittest.main(verbosity=2)
