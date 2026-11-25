import sys
from dataclasses import dataclass, field
from pathlib import Path

SOURCE_SUFFIXES = {".ts", ".tsx", ".rs"}
IGNORED_PARTS = {".git", "node_modules", "target", "dist", ".tmp"}


@dataclass
class Report:
    failures: list = field(default_factory=list)
    files: int = 0


def line_at(text, index):
    return text.count("\n", 0, index) + 1


def comment_failures(text, filename):
    failures = []
    rust = filename.endswith(".rs")
    index = 0
    size = len(text)
    while index < size:
        char = text[index]
        if char in ("'", '"', "`"):
            quote = char
            index += 1
            while index < size:
                if text[index] == "\\":
                    index += 2
                    continue
                if text[index] == quote:
                    index += 1
                    break
                index += 1
            continue
        if rust and char == "r" and index + 1 < size and text[index + 1] == "#":
            end = text.find('"#', index + 2)
            index = size if end < 0 else end + 2
            continue
        if not rust and text.startswith("//", index):
            failures.append(filename + ":" + str(line_at(text, index)) + ": commentaire interdit")
            index = text.find("\n", index)
            index = size if index < 0 else index
            continue
        if rust and text.startswith("//", index):
            allowed = index + 2 < size and text[index + 2] in ("/", "!")
            if not allowed:
                failures.append(
                    filename + ":" + str(line_at(text, index)) + ": commentaire interdit"
                )
            index = text.find("\n", index)
            index = size if index < 0 else index
            continue
        if text.startswith("/*", index):
            allowed = text.startswith("/**", index) or (rust and text.startswith("/*!", index))
            if not allowed:
                failures.append(
                    filename + ":" + str(line_at(text, index)) + ": commentaire interdit"
                )
            end = text.find("*/", index + 2)
            index = size if end < 0 else end + 2
            continue
        index += 1
    return failures


def map_failures(text, filename):
    if not filename.endswith(".tsx"):
        return []
    count = text.count(".map(")
    if count <= 1:
        return []
    return [filename + ": " + str(count) + " appels map, un seul autorise par fichier TSX"]


def check_text(text, filename):
    return comment_failures(text, filename) + map_failures(text, filename)


def source_files(root):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in SOURCE_SUFFIXES:
            continue
        if any(part in IGNORED_PARTS for part in path.parts):
            continue
        yield path


def run_checks(root):
    files = list(source_files(root))
    failures = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        failures += check_text(text, str(path.relative_to(root)))
    return Report(failures, len(files))


def main():
    root = Path(__file__).resolve().parent.parent
    report = run_checks(root)
    print("fichiers source verifies:", report.files)
    if report.failures:
        print("echecs:", len(report.failures))
        for failure in report.failures:
            print("- " + failure)
        return 1
    print("aucun echec")
    return 0


if __name__ == "__main__":
    sys.exit(main())
