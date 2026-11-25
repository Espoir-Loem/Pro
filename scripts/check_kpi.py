from pathlib import Path
import sys

REQUIRED_IDS = (
    "BUG-01",
    "BUG-02",
    "BUG-03",
    "UX-01",
    "UX-02",
    "UX-03",
    "PRD-01",
    "PRD-02",
    "SEO-01",
    "SEO-02",
)
REQUIRED_SECTIONS = ("## 2. Bugs", "## 3. UX", "## 4. Produit", "## 5. SEO web")


def check_text(text):
    failures = []
    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append("section absente: " + section)
    for identifiant in REQUIRED_IDS:
        if identifiant not in text:
            failures.append("identifiant absent: " + identifiant)
    return failures


def run_checks(root):
    target = root / "docs" / "Product" / "kpi.md"
    if not target.is_file():
        return ["fiche KPI absente"]
    return check_text(target.read_text(encoding="utf-8", errors="replace"))


def main():
    root = Path(__file__).resolve().parent.parent
    failures = run_checks(root)
    print("identifiants KPI verifies:", len(REQUIRED_IDS))
    if failures:
        print("echecs:", len(failures))
        for failure in failures:
            print("- " + failure)
        return 1
    print("aucun echec")
    return 0


if __name__ == "__main__":
    sys.exit(main())
