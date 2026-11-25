import tempfile
import unittest
from pathlib import Path

import check_kpi


def complete_text():
    lines = [
        "# KPI",
        "## 2. Bugs",
        "## 3. UX",
        "## 4. Produit",
        "## 5. SEO web",
    ]
    rows = [
        "| " + identifiant + " | nom | formule | source | proprietaire | cible |"
        for identifiant in check_kpi.REQUIRED_IDS
    ]
    lines += rows
    return "\n".join(lines) + "\n"


class TestKpiChecks(unittest.TestCase):
    def test_accepts_complete_text(self):
        self.assertEqual(check_kpi.check_text(complete_text()), [])

    def test_reports_missing_identifier(self):
        text = complete_text().replace("BUG-03", "BUG-99")
        failures = check_kpi.check_text(text)
        self.assertTrue(any("BUG-03" in failure for failure in failures))

    def test_reports_missing_section(self):
        text = complete_text().replace("## 3. UX", "## 3. Divers")
        failures = check_kpi.check_text(text)
        self.assertTrue(any("UX" in failure for failure in failures))


class TestRunChecks(unittest.TestCase):
    def test_accepts_complete_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "docs" / "Product" / "kpi.md"
            target.parent.mkdir(parents=True)
            target.write_text(complete_text(), encoding="utf-8")
            self.assertEqual(check_kpi.run_checks(root), [])

    def test_reports_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(check_kpi.run_checks(Path(tmp)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
