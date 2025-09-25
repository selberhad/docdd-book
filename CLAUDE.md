# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an mdBook documenting the Document-Driven Development (DocDD) methodology. The book teaches using specs, plans, and tight feedback loops with toy models and a CLI+JSON "debugger mindset" to build software with clarity and speed.

**Key Architecture:**
- `src/` contains all book content organized into logical sections
- `SUMMARY.md` defines the table of contents and navigation structure
- `book.toml` configures mdBook with HTML output and linkcheck validation
- Pre-commit hooks automatically run builds, link validation, and update statistics

## Essential Commands

```bash
# Initial setup (installs mdbook and mdbook-linkcheck)
make setup

# Development workflow
make serve           # Live preview at http://127.0.0.1:3000 with hot reload
make check          # Build + linkcheck validation (run before commits)
make build          # Static build to book/ directory

# Statistics and maintenance
make stats          # Generate book statistics (console format)
python3 scripts/book_stats.py --markdown  # Markdown format for STATS.md

# Git workflow
make install-hooks  # Install pre-commit hook (run once per clone)
```

## Content Structure

**Four main sections:**
1. **Foundations** (`src/foundations/`) - Core DocDD principles, napkin physics, toy models
2. **Practice** (`src/practice/`) - AGENTS.md template and operational guidance
3. **Authoring Guides** (`src/authoring/`) - Agent-oriented writing templates for SPEC, PLAN, etc.
4. **Patterns & Examples** (`src/patterns/`) - Real-world examples using flat file structure

**Agent-oriented guides:** The authoring guides are designed to be copied into repositories and referenced by AI agents before writing documentation. They provide structured templates and constraints.

## Development Workflow

**Pre-commit automation:** The repository has a pre-commit hook that:
- Runs `make check` (mdbook build + linkcheck)
- Auto-generates `STATS.md` with current word counts and reading time
- Blocks commits if build fails or mdbook is missing

**File organization:**
- Keep one H1 per page with concise, bullet-first writing
- Use relative links within `src/`
- File names should be lowercase, hyphen-separated
- Update `SUMMARY.md` when adding/moving chapters

**Examples structure:** Uses flat file naming with prefixes (e.g., `archive-browser-plan.md`, `archive-browser-spec.md`) to support multiple example projects while working within mdBook's single-level nesting limitation.

**Git workflow:**
- **Commit messages:** Keep concise for small changes (one short descriptive line)
- **Commit and push:** When user explicitly requests "commit and push", always chain: `git commit ... && git push origin main`
- Use conventional commit format: `type(scope): description`

## CI/CD Notes

- Deploys to GitHub Pages on `main` branch pushes
- CI runs are skipped for changes to `docs/**`, `*.md` at root, and `.gitignore`
- Build failures block deployment
- Link validation runs as part of every build