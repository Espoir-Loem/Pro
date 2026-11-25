import unittest

import check_pr_issue


class TestReference(unittest.TestCase):
    def test_finds_closing_keyword(self):
        self.assertEqual(check_pr_issue.find_reference("Closes #12"), 12)

    def test_finds_plain_reference(self):
        self.assertEqual(check_pr_issue.find_reference("Voir #9"), 9)

    def test_returns_none_without_reference(self):
        self.assertIsNone(check_pr_issue.find_reference("Aucune référence"))


class TestValidation(unittest.TestCase):
    def test_accepts_open_issue(self):
        self.assertEqual(check_pr_issue.run_checks("Closes #12", 12, "open"), [])

    def test_rejects_closed_issue(self):
        failures = check_pr_issue.run_checks("Closes #12", 12, "closed")
        self.assertTrue(any("fermée" in failure for failure in failures))

    def test_rejects_other_issue(self):
        failures = check_pr_issue.run_checks("Closes #12", 13, "open")
        self.assertTrue(any("référence" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
