import os
import re
import subprocess
import sys

CLOSING_RE = re.compile(r"(?i)(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)")
PLAIN_RE = re.compile(r"#(\d+)")


def find_reference(body):
    for pattern in (CLOSING_RE, PLAIN_RE):
        match = pattern.search(body or "")
        if match:
            return int(match.group(1))
    return None


def run_checks(body, issue_number, state):
    reference = find_reference(body)
    if reference is None:
        return ["aucune référence d'issue dans la pull request"]
    if reference != issue_number:
        return ["la référence #" + str(reference) + " ne correspond pas à l'issue attendue"]
    if state != "open":
        return ["issue #" + str(reference) + " fermée"]
    return []


def github_value(path, jq):
    command = ["gh", "api", path, "--jq", jq]
    return subprocess.check_output(command, text=True, stderr=subprocess.DEVNULL).strip()


def main():
    if len(sys.argv) != 2:
        print("usage: check_pr_issue.py numero")
        return 2
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not repository:
        print("GITHUB_REPOSITORY absent")
        return 2
    pull_number = sys.argv[1]
    body = github_value("repos/" + repository + "/pulls/" + pull_number, ".body")
    reference = find_reference(body)
    if reference is None:
        print("aucune référence d'issue dans la pull request")
        return 1
    state = github_value("repos/" + repository + "/issues/" + str(reference), ".state")
    failures = run_checks(body, reference, state)
    if failures:
        print("echecs:", len(failures))
        for failure in failures:
            print("- " + failure)
        return 1
    print("issue ouverte confirmée:", reference)
    return 0


if __name__ == "__main__":
    sys.exit(main())
