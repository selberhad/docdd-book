# Document‑Driven Development — The Book

[![Deploy mdBook to GitHub Pages](https://github.com/selberhad/docdd-book/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/selberhad/docdd-book/actions/workflows/gh-pages.yml)

This repository is an mdBook about the Document‑Driven Development (DocDD) methodology. It is not product documentation for a software project. The book teaches how to use specs, plans, and tight feedback loops (with toy models and a CLI+JSON “debugger mindset”) to build software with clarity and speed.

- Read online: https://selberhad.github.io/docdd-book/
- Book statistics: [STATS.md](STATS.md)

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
- `scripts/`: helper scripts (`bootstrap_mdbook.sh`, `serve_local.sh`, `ci_local.sh`).

## Contributing
- Start with issues/PRs for typos, structure, or new examples.
- Follow repository guidelines in `AGENTS.md` (style and commit guidance).
- Keep pages focused (one topic per page); prefer bullets and concrete examples.
- Run `make check` before committing to catch broken links and build errors.

## Deploying
- Published via GitHub Pages on pushes to `main` (see workflow badge above).
