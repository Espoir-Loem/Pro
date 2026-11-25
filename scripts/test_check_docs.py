import tempfile
import unittest
from pathlib import Path

import check_docs


def write_clean_fixture(root):
    docs = root / "docs"
    docs.mkdir()
    ids = []
    ids += ["FS-" + str(n).zfill(2) for n in range(1, 12)]
    ids += ["US-" + str(n).zfill(2) for n in range(1, 18)]
    ids += ["D-" + str(n).zfill(3) for n in range(1, 25)]
    ids += ["A-" + str(n).zfill(2) for n in range(1, 14)]
    (docs / "README.md").write_text(
        "Contenu sans défaut. " + " ".join(ids) + "\n", encoding="utf-8"
    )
    return docs


class TestForbiddenTypography(unittest.TestCase):
    def test_detects_long_and_short_dashes(self):
        text = "abc" + chr(0x2014) + "def" + chr(0x2013) + "ghi"
        labels = check_docs.forbidden_typography(text)
        self.assertIn("tiret long U+2014", labels)
        self.assertIn("tiret court U+2013", labels)

    def test_detects_marker_built_from_parts(self):
        marker = "TO" + "DO"
        labels = check_docs.forbidden_typography("texte " + marker)
        self.assertTrue(any("marqueur" in label for label in labels))

    def test_detects_cjk(self):
        labels = check_docs.forbidden_typography("texte " + chr(0x4E00))
        self.assertTrue(any("CJK" in label for label in labels))

    def test_accepts_clean_text(self):
        self.assertEqual(check_docs.forbidden_typography("Texte français sans défaut."), [])


class TestLinks(unittest.TestCase):
    def test_ignores_external_code_and_anchors(self):
        text = "\n".join(
            [
                "[interne](docs/Product/prd.md)",
                "[web](https://example.com/page)",
                "[ancre](#section)",
                "`[faux](code.md)`",
                "```",
                "[faux](bloque.md)",
                "```",
            ]
        )
        self.assertEqual(check_docs.relative_link_targets(text), ["docs/Product/prd.md"])


class TestIdentifiers(unittest.TestCase):
    def test_finds_padded_identifiers(self):
        text = "FS-01 puis FS-03 et D-024"
        self.assertEqual(check_docs.find_ids(text, "FS-", 2), [1, 3])
        self.assertEqual(check_docs.find_ids(text, "D-", 3), [24])

    def test_reports_gaps_and_extras(self):
        failure = check_docs.check_sequence("FS-01 FS-03 FS-25", "FS-", 2, 11, "FS")
        self.assertIsNotNone(failure)
        self.assertIn("manquants", failure)
        self.assertIn("hors perimetre", failure)


class TestMermaid(unittest.TestCase):
    def test_detects_open_block(self):
        self.assertTrue(check_docs.mermaid_open("```mermaid\ngraph TD\n"))

    def test_accepts_closed_block(self):
        self.assertFalse(check_docs.mermaid_open("```mermaid\ngraph TD\n```\n"))


class TestGeneratedFiles(unittest.TestCase):
    def test_ignores_dependencies_and_lockfile(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_clean_fixture(root)
            (root / "README.md").write_text("[guide](docs/README.md)\n", encoding="utf-8")
            dependency = root / "node_modules" / "paquet" / "note.md"
            dependency.parent.mkdir(parents=True)
            dependency.write_text("texte " + chr(0x2014), encoding="utf-8")
            (root / "package-lock.json").write_text("TO" + "DO", encoding="utf-8")
            report = check_docs.run_checks(root, expected_doc_count=1)
            self.assertEqual(report.failures, [])


class TestRunChecks(unittest.TestCase):
    def test_accepts_clean_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_clean_fixture(root)
            (root / "README.md").write_text("[guide](docs/README.md)\n", encoding="utf-8")
            report = check_docs.run_checks(root, expected_doc_count=1)
            self.assertEqual(report.failures, [])
            self.assertEqual(report.links, 1)

    def test_detects_broken_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_clean_fixture(root)
            (root / "README.md").write_text("[absent](docs/absent.md)\n", encoding="utf-8")
            report = check_docs.run_checks(root, expected_doc_count=1)
            self.assertTrue(any("lien relatif" in failure for failure in report.failures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
