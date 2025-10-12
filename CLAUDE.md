# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an mdBook documenting the Dialectic-Driven Development (DDD) methodology. The book teaches using specs, plans, and tight feedback loops with toy models and a CLI+JSON "debugger mindset" to build software with clarity and speed.

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
1. **Foundations** (`src/foundations/`) - Core DDD principles, napkin physics, toy models
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
- **When to commit:** Only commit when explicitly prompted by the user
- **Commit messages:** Keep concise for small changes (one short descriptive line)
- **Commit and push:** When user explicitly requests "commit and push", always chain: `git commit ... && git push origin main`
- Use conventional commit format: `type(scope): description`

## Writing Case Studies and Technical Documentation

**CRITICAL: Never estimate timelines from intuition.** Temporal claims systematically hallucinate toward human-baseline velocity, erasing evidence of AI-assisted speed gains.

### Temporal Claims Require Evidence

**Always verify timing with git log:**
```bash
# Get project timeline
git log --pretty=format:"%ai %s" --reverse | head -1  # First commit
git log --pretty=format:"%ai %s" | head -1             # Latest commit

# Check specific milestones
git log --pretty=format:"%ai %s" | grep "milestone_keyword"

# Count days between events
git log --oneline --after="2025-10-05" --before="2025-10-09" | wc -l
```

**The pattern:** Without checking git history, temporal estimates default to "what would be reasonable for average human developer" (~1 month, ~1 week). Actual AI-assisted timelines are often 5-10x faster.

**Examples of systematic error:**
- ❌ "Research phase lasted ~1 week" (hallucination)
- ✅ "Research phase completed same day as toy0 (Oct 5)" (git log verified)
- ❌ "~1 month for study phase + 5 toys" (hallucination)
- ✅ "~5 days total (Oct 5-9, 2025)" (git log verified)

**If git history unavailable:** Say "timeline unknown" rather than estimate. Human-calibrated intuitions don't apply to AI-assisted workflows.

**Why this matters for DDD book:** The methodology's core value proposition is velocity multiplication. Hallucinating human-baseline timelines directly undermines the book's purpose.

### Other Quantitative Claims

This principle extends to all measurable claims:
- ❌ Lines of code (count them: `find src -name "*.rs" | xargs wc -l`)
- ❌ Test coverage (measure it: `cargo tarpaulin` or equivalent)
- ❌ Number of files (count them: `find . -type f | wc -l`)
- ❌ Dependencies (check them: `grep dependencies Cargo.toml | wc -l`)

**Heuristic:** If it's a number and you didn't measure it, don't claim it. "Unknown" > plausible hallucination.

## CI/CD Notes

- Deploys to GitHub Pages on `main` branch pushes
- CI runs are skipped for changes to `docs/**`, `*.md` at root, and `.gitignore`
- Build failures block deployment
- Link validation runs as part of every build