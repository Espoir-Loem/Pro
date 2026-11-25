import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

TEXT_SUFFIXES = {".md", ".txt", ".json", ".yml", ".yaml", ".py"}
TEXT_NAMES = {".gitignore", ".gitattributes", ".editorconfig"}
IGNORED_PARTS = {".git", "node_modules", "dist", "build", "coverage", ".tmp"}
IGNORED_NAMES = {"package-lock.json", "pnpm-lock.yaml", "yarn.lock", "Cargo.lock"}
SKIPPED_PREFIXES = ("http://", "https://", "mailto:", "#", "data:", "file:")
MARKERS = ("TO" + "DO", "FI" + "XME", "T" + "BD", "X" + "X" + "X")
CJK_RANGES = ((0x3400, 0x9FFF), (0x3040, 0x30FF), (0xAC00, 0xD7AF))
CJK_RE = re.compile("[" + "".join(chr(start) + "-" + chr(end) for start, end in CJK_RANGES) + "]")
SEQUENCES = (("FS-", 2, 11, "FS"), ("US-", 2, 17, "US"), ("D-", 3, 24, "D"), ("A-", 2, 13, "A"))


@dataclass
class Report:
    failures: list = field(default_factory=list)
    text_files: int = 0
    markdown_files: int = 0
    links: int = 0


def forbidden_typography(text):
    labels = []
    if chr(0x2014) in text:
        labels.append("tiret long U+2014")
    if chr(0x2013) in text:
        labels.append("tiret court U+2013")
    if CJK_RE.search(text):
        labels.append("CJK")
    for marker in MARKERS:
        if re.search(re.escape(marker), text, re.IGNORECASE):
            labels.append("marqueur " + marker)
    return labels


def relative_link_targets(text):
    targets = []
    fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        clean = re.sub(r"`[^`]*`", "", line)
        for match in re.finditer(r"\]\(([^)]+)\)", clean):
            target = match.group(1).strip()
            if target.startswith(SKIPPED_PREFIXES):
                continue
            target = target.split("#", 1)[0]
            if target:
                targets.append(target)
    return targets


def find_ids(text, prefix, width):
    pattern = re.escape(prefix) + r"(\d{" + str(width) + r"})"
    return sorted({int(value) for value in re.findall(pattern, text)})


def check_sequence(text, prefix, width, maximum, label):
    found = find_ids(text, prefix, width)
    missing = [value for value in range(1, maximum + 1) if value not in found]
    extra = [value for value in found if value > maximum]
    if not missing and not extra:
        return None
    return "serie " + label + ": manquants " + str(missing) + ", hors perimetre " + str(extra)


def mermaid_open(text):
    fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fence = not fence
    return fence


def text_files(root):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in IGNORED_PARTS for part in path.parts):
            continue
        if path.name in IGNORED_NAMES:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in TEXT_NAMES:
            yield path


def canonical_markdown(root):
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        relative = path.relative_to(root)
        if relative.parent == Path(".") or relative.parts[0] in ("docs", "reports"):
            yield path


def check_typography(paths, root):
    failures = []
    for path in paths:
        labels = forbidden_typography(path.read_text(encoding="utf-8", errors="replace"))
        if labels:
            failures.append(
                str(path.relative_to(root)) + ": typographie interdite: " + ", ".join(labels)
            )
    return failures


def check_links(paths, root):
    failures = []
    contents = []
    links = 0
    for path in paths:
        content = path.read_text(encoding="utf-8", errors="replace")
        contents.append(content)
        for target in relative_link_targets(content):
            links += 1
            if not (path.parent / target).resolve().exists():
                failures.append(str(path.relative_to(root)) + ": lien relatif absent: " + target)
    return failures, contents, links


def check_blocks(paths, contents, root):
    failures = []
    for path, content in zip(paths, contents, strict=False):
        if mermaid_open(content):
            failures.append(str(path.relative_to(root)) + ": bloc de code non ferme")
    return failures


def check_sequences(text):
    failures = []
    for prefix, width, maximum, label in SEQUENCES:
        failure = check_sequence(text, prefix, width, maximum, label)
        if failure:
            failures.append(failure)
    return failures


def check_doc_count(root, expected):
    count = sum(1 for path in (root / "docs").rglob("*") if path.is_file())
    if count == expected:
        return []
    return ["docs: " + str(count) + " fichiers, attendu " + str(expected)]


def run_checks(root, expected_doc_count=61):
    texts = list(text_files(root))
    markdowns = list(canonical_markdown(root))
    failures = check_typography(texts, root)
    link_failures, contents, links = check_links(markdowns, root)
    failures += link_failures
    failures += check_blocks(markdowns, contents, root)
    failures += check_sequences("\n".join(contents))
    failures += check_doc_count(root, expected_doc_count)
    return Report(failures, len(texts), len(markdowns), links)


def main():
    root = Path(__file__).resolve().parent.parent
    report = run_checks(root)
    print("fichiers textuels:", report.text_files)
    print("fichiers markdown canoniques:", report.markdown_files)
    print("liens relatifs verifies:", report.links)
    if report.failures:
        print("echecs:", len(report.failures))
        for failure in report.failures:
            print("- " + failure)
        return 1
    print("aucun echec")
    return 0


if __name__ == "__main__":
    sys.exit(main())
