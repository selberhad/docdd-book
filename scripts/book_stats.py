#!/usr/bin/env python3
"""
Generate statistics for the mdBook including word counts, chapter counts, etc.
"""

import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple


def extract_text_from_markdown(content: str) -> str:
    """Extract readable text from markdown, removing code blocks and metadata."""
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content = re.sub(r'`[^`]+`', '', content)

    # Remove links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)

    # Remove headers markup but keep text
    content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)

    # Remove other markdown syntax
    content = re.sub(r'[*_]+([^*_]+)[*_]+', r'\1', content)  # bold/italic
    content = re.sub(r'^\s*[-*+]\s+', '', content, flags=re.MULTILINE)  # lists
    content = re.sub(r'^\s*\d+\.\s+', '', content, flags=re.MULTILINE)  # numbered lists

    return content.strip()


def count_words(text: str) -> int:
    """Count words in text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def analyze_file(file_path: Path) -> Dict[str, int]:
    """Analyze a single markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        text = extract_text_from_markdown(content)

        return {
            'words': count_words(text),
            'lines': len(content.splitlines()),
            'chars': len(content),
            'text_chars': len(text)
        }
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {'words': 0, 'lines': 0, 'chars': 0, 'text_chars': 0}


def print_console_output(file_stats: List[Tuple[str, Dict[str, int]]], totals: Dict[str, int], total_files: int):
    """Print stats in console format."""
    print("📊 Book Statistics")
    print("=" * 50)
    print(f"Total files: {total_files}")
    print(f"Total words: {totals['words']:,}")
    print(f"Total lines: {totals['lines']:,}")
    print(f"Total characters: {totals['chars']:,}")
    print(f"Reading time: ~{totals['words'] // 200} minutes")
    print()

    print("📄 Per-File Breakdown")
    print("-" * 50)
    print(f"{'File':<40} {'Words':<8} {'Lines':<8}")
    print("-" * 50)

    for file_path, stats in file_stats:
        print(f"{file_path:<40} {stats['words']:<8} {stats['lines']:<8}")

    print("-" * 50)
    print(f"{'TOTAL':<40} {totals['words']:<8} {totals['lines']:<8}")


def print_markdown_output(file_stats: List[Tuple[str, Dict[str, int]]], totals: Dict[str, int], total_files: int):
    """Print stats in markdown format."""
    print("# Book Statistics")
    print()
    print("## Overview")
    print()
    print(f"- **Total files:** {total_files}")
    print(f"- **Total words:** {totals['words']:,}")
    print(f"- **Total lines:** {totals['lines']:,}")
    print(f"- **Total characters:** {totals['chars']:,}")
    print(f"- **Reading time:** ~{totals['words'] // 200} minutes")
    print()

    print("## Per-File Breakdown")
    print()
    print("| File | Words | Lines |")
    print("|------|------:|------:|")

    for file_path, stats in file_stats:
        print(f"| {file_path} | {stats['words']:,} | {stats['lines']:,} |")

    print(f"| **TOTAL** | **{totals['words']:,}** | **{totals['lines']:,}** |")


def main():
    parser = argparse.ArgumentParser(description="Generate mdBook statistics")
    parser.add_argument("--markdown", "-md", action="store_true",
                       help="Output in markdown format")
    args = parser.parse_args()

    src_dir = Path('src')
    if not src_dir.exists():
        print("Error: src/ directory not found. Run from project root.")
        return 1

    # Find all markdown files
    md_files = list(src_dir.rglob('*.md'))

    # Analyze each file
    file_stats: List[Tuple[str, Dict[str, int]]] = []
    totals = {'words': 0, 'lines': 0, 'chars': 0, 'text_chars': 0}

    for md_file in sorted(md_files):
        relative_path = md_file.relative_to(src_dir)
        stats = analyze_file(md_file)
        file_stats.append((str(relative_path), stats))

        for key in totals:
            totals[key] += stats[key]

    # Output results
    if args.markdown:
        print_markdown_output(file_stats, totals, len(md_files))
    else:
        print_console_output(file_stats, totals, len(md_files))

    return 0


if __name__ == '__main__':
    exit(main())