#!/usr/bin/env python3
"""
Migrate this repo's Markdown docs into an mdBook structure by COPYING files
into ./src/ (non-destructive). Assumes a single canonical page per topic.

Creates:
- book.toml (if missing)
- src/ directory with organized copies
- src/SUMMARY.md based on canonical layout

Idempotent: re-running will overwrite copies in ./src but not originals.
"""
from __future__ import annotations

import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


def ensure_dirs():
    (SRC / "playbooks").mkdir(parents=True, exist_ok=True)
    (SRC / "specs").mkdir(parents=True, exist_ok=True)
    (SRC / "guides" / "writing").mkdir(parents=True, exist_ok=True)
    (SRC / "appendices").mkdir(parents=True, exist_ok=True)


def choose_latest_version(pattern: str) -> Path | None:
    """Find the highest *_Vn.md matching pattern (glob pattern relative to ROOT)."""
    candidates = sorted(ROOT.glob(pattern))
    latest = None
    max_n = -1
    version_re = re.compile(r"_V(\d+)\.md$")
    for p in candidates:
        m = version_re.search(p.name)
        if not m:
            continue
        n = int(m.group(1))
        if n > max_n:
            max_n = n
            latest = p
    return latest


def copy_file(src: Path, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"Copied: {src} -> {dest}")


def create_book_toml():
    book_toml = ROOT / "book.toml"
    if book_toml.exists():
        print("book.toml exists; leaving as-is.")
        return
    content = (
        "[book]\n"
        "title = \"AI Meta Docs\"\n"
        "authors = [\"Contributors\"]\n"
        "language = \"en\"\n"
        "multilingual = false\n"
        "src = \"src\"\n\n"
        "[output.html]\n"
        "default-theme = \"light\"\n"
        "git-repository-url = \"\"\n"
    )
    book_toml.write_text(content, encoding="utf-8")
    print("Created book.toml")


def migrate():
    ensure_dirs()

    mapping: list[tuple[str, str]] = [
        ("README.md", "introduction.md"),
        ("DOC_MAP.md", "doc-map.md"),
        ("SPEC_WRITING.md", "specs/spec-writing.md"),
        ("DEBUGGERS.md", "guides/debuggers.md"),
        ("DDD.md", "guides/ddd.md"),
        ("TOY_DEV.md", "guides/toy-dev.md"),
        ("PLAN_WRITING.md", "guides/writing/plan.md"),
        ("LEARNINGS_WRITING.md", "guides/writing/learnings.md"),
        ("README_WRITING.md", "guides/writing/readme.md"),
        ("KICKOFF_WRITING.md", "guides/writing/kickoff.md"),
        ("SPEC_V2.md", "specs/spec.md"),
        ("PLAN.md", "appendices/plan.md"),
        ("FINAL_COMP.md", "appendices/final-comp.md"),
    ]

    # Copy canonical single-version files if present
    for src_name, dest_rel in mapping:
        src_path = ROOT / src_name
        if src_path.exists():
            copy_file(src_path, SRC / dest_rel)
        else:
            print(f"Skip missing: {src_name}")

    # Choose latest playbook version
    latest_playbook = choose_latest_version("PLAYBOOK_V*.md")
    if latest_playbook:
        copy_file(latest_playbook, SRC / "playbooks" / "playbook.md")
    else:
        print("No PLAYBOOK_V*.md found")

    # Optionally copy the latest composite as an appendix (not listed in SUMMARY)
    latest_comp = choose_latest_version("PLAYBOOK_COMP_V*.md")
    if latest_comp:
        safe_name = latest_comp.stem.lower().replace("_", "-") + ".md"
        copy_file(latest_comp, SRC / "appendices" / safe_name)


def write_summary():
    parts = []
    parts.append("# Summary\n")
    def line(text: str) -> str:
        return text + "\n"

    parts.append(line("- [Introduction](./introduction.md)"))
    parts.append(line("- [Documentation Map](./doc-map.md)"))
    parts.append("\n")

    parts.append(line("## Core Guides"))
    parts.append(line("- [Doc-Driven Development (DDD)](./guides/ddd.md)"))
    parts.append(line("- [Debuggers: CLI+JSON](./guides/debuggers.md)"))
    parts.append(line("- [Toy Model Development](./guides/toy-dev.md)"))
    parts.append("\n")

    parts.append(line("## Playbook"))
    parts.append(line("- [Playbook](./playbooks/playbook.md)"))
    parts.append("\n")

    parts.append(line("## Specs"))
    parts.append(line("- [Product Spec](./specs/spec.md)"))
    parts.append(line("- [Spec Writing Guide](./specs/spec-writing.md)"))
    parts.append("\n")

    parts.append(line("## Writing Guides"))
    parts.append(line("- [Plan Writing](./guides/writing/plan.md)"))
    parts.append(line("- [Learnings Writing](./guides/writing/learnings.md)"))
    parts.append(line("- [README Writing](./guides/writing/readme.md)"))
    parts.append(line("- [Kickoff Writing](./guides/writing/kickoff.md)"))
    parts.append("\n")

    parts.append(line("## Appendices"))
    parts.append(line("- [Plan (Example/Template)](./appendices/plan.md)"))
    parts.append(line("- [Final Compilation](./appendices/final-comp.md)"))

    (SRC / "SUMMARY.md").write_text("".join(parts), encoding="utf-8")
    print("Wrote src/SUMMARY.md")


def main():
    create_book_toml()
    migrate()
    write_summary()
    print("\nDone. You can now run: mdbook serve -o")


if __name__ == "__main__":
    main()
