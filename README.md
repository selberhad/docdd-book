# AI Meta Docs (mdBook)

A curated, versioned documentation set for Doc‑Driven Development (DDD), toy models, and AI‑legible engineering practices. This repo uses mdBook to present the docs as a searchable site with a sidebar and clean navigation.

## Quick Start
- Prereqs: rustup + cargo installed (Rust stable).
- Install tools: `make setup` (installs `mdbook` and `mdbook-linkcheck`).
- Develop locally: `make serve` (opens http://127.0.0.1:3000 with live reload).
- Validate links/build: `make check` (runs `mdbook build` with link checking).
- Build static site: `make build` (outputs to `book/`).

## Project Structure
- `book.toml`: mdBook configuration (HTML output + linkcheck).
- `src/`: mdBook sources
  - `SUMMARY.md`: table of contents.
  - `guides/`: DDD, debuggers (CLI+JSON), toy‑dev, writing guides.
  - `playbooks/`: consolidated playbook.
  - `specs/`: Spec Writing Guide (canonical).
  - `appendices/`: optional examples/templates.
- `scripts/`: helper scripts
  - `bootstrap_mdbook.sh`: installs mdBook + linkcheck.
  - `serve_local.sh`, `ci_local.sh`.
  - `migrate_to_mdbook.py`: copies from legacy docs (non‑destructive; optional).
- `docs/legacy/`: original source Markdown; kept for reference/history.

## Editing & Conventions
- One H1 per page; use ATX headings (`#`, `##`, `###`).
- Use relative links within `src/` (e.g., `[Plan Writing](./guides/writing/plan.md)`).
- Keep pages concise and instructional; prefer bullets and concrete examples.
- Run `make check` before committing to catch broken links.

## Migrating Legacy Docs (optional)
- The migration script cleans `src/` and copies curated files from `docs/legacy/`.
- Run manually if you need to regenerate: `make migrate`.
- By default we exclude `DOC_MAP` and `FINAL_COMP` from the book.

## Deploying
- Build locally with `make build` and serve `book/` via any static host.
- For GitHub Pages, a simple workflow can publish `book/` on push to `main`.
