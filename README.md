# Document‑Driven Development — The Book

[![Deploy mdBook to GitHub Pages](https://github.com/selberhad/docdd-book/actions/workflows/gh-pages.yml/badge.svg)](https://github.com/selberhad/docdd-book/actions/workflows/gh-pages.yml)

This repository is an mdBook about the Document‑Driven Development (DocDD) methodology.  The book teaches how to use specs, plans, and tight feedback loops (with toy models and a CLI+JSON “debugger mindset”) to build software with clarity and speed.

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

**Note**: The project scaffolding (build tools, scripts, configuration) is MIT-licensed and freely reusable for your own books. However, the DocDD book content itself (`src/` directory) is copyrighted material under Personal-Use license - see the License section below.

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

This is my personal book project - I'm the sole author and prefer to maintain full editorial control during the writing process.

- **Feedback welcome**: Please open an issue at https://github.com/selberhad/docdd-book/issues for typos, suggestions, or questions
- **No PRs**: Pull requests will be closed without review, but I appreciate the interest!

## AI-First Technical Writing Example

This repository serves as a practical example of "vibe-writing" a technical book using mdBook and AI coding agents like Anthropic's Claude Code CLI and OpenAI's Codex CLI, demonstrating effective human-AI collaboration:

- Original agent-oriented documentation in `docs/legacy/` was migrated using `scripts/migrate_to_mdbook.py`
- Book content collaboratively developed through iterative human-AI editing
- Automated statistics, pre-commit hooks, and CI/CD provide quality gates without heavyweight process

**Note on AI collaboration**: As a working draft developed with AI assistance, this book may contain unintended redundancies, inconsistencies, or hallucinated details. If you notice such issues while reading, please file an issue at https://github.com/selberhad/docdd-book/issues to help improve the content.

## Deploying
- Published via GitHub Pages on pushes to `main` (see workflow badge above).

## License
- **Book content** (`src/` directory): Personal-Use license (no redistribution). See `LICENSE.md`.
- **Project scaffolding** (build tools, scripts, configuration): MIT license - feel free to fork this setup for your own books!
- **Code samples within the book**: MIT license.
- Permissions/requests: open an issue on the GitHub repo.
