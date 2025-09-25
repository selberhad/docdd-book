# Document‑Driven Development — The Book

[![Deploy mdBook to GitHub Pages](https://github.com/selberhad/docdd-book/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/selberhad/docdd-book/actions/workflows/gh-pages.yml)

This repository is an mdBook about the Document‑Driven Development (DocDD) methodology. It is not product documentation for a software project. The book teaches how to use specs, plans, and tight feedback loops (with toy models and a CLI+JSON “debugger mindset”) to build software with clarity and speed.

- Read online: https://selberhad.github.io/docdd-book/
- Book statistics: [STATS.md](STATS.md)
- Blog posts: [docs/blog/README.md](docs/blog/README.md)

## What You’ll Learn
- Foundations (why): principles of DocDD, Napkin Physics, Toy‑Model rationale, Debugger mindset.
- Practice (how): the DocDD loop, kickoff, checklists, and workflow.
- Authoring guides: writing SPECs, PLANs, READMEs, and LEARNINGS.
- Patterns & examples: toy patterns and an examples archive.

## Develop Locally
- Prereqs: rustup + cargo (Rust stable).
- Setup tools: `make setup` (installs `mdbook` and `mdbook-linkcheck`).
- Live preview: `make serve` (http://127.0.0.1:3000, hot reload).
- Build + link check: `make check`.
- Static build: `make build` (outputs to `book/`).

## Repository Layout
- `book.toml`: mdBook configuration (HTML output + linkcheck).
- `src/`: book sources
  - `SUMMARY.md`: table of contents.
  - `foundations/`: principles and overviews.
  - `practice/`: AGENTS.md template and operational guidance.
  - `authoring/`: writing guides (SPEC, PLAN, README, LEARNINGS).
  - `patterns/`: patterns and examples archive.
- `docs/`: additional content
  - `blog/`: related blog posts and essays.
  - `legacy/`: original agent-oriented docs migrated to create this book.
- `scripts/`: helper scripts and `migrate_to_mdbook.py` used to transform legacy docs.

## Contributing
- Start with issues/PRs for typos, structure, or new examples.
- Follow repository guidelines in `AGENTS.md` (style and commit guidance).
- Keep pages focused (one topic per page); prefer bullets and concrete examples.
- Run `make check` before committing to catch broken links and build errors.

## AI-First Development Example

This repository serves as a practical example of "vibe-writing" a technical book using mdBook and AI coding agents like Anthropic's Claude Code CLI and OpenAI's Codex CLI, demonstrating effective human-AI collaboration:

- Original agent-oriented documentation in `docs/legacy/` was migrated using `scripts/migrate_to_mdbook.py`
- Book content collaboratively developed through iterative human-AI editing
- Automated statistics, pre-commit hooks, and CI/CD provide quality gates without heavyweight process

## Deploying
- Published via GitHub Pages on pushes to `main` (see workflow badge above).
