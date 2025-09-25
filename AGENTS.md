# Repository Guidelines (AI + Humans)

This repo contains an mdBook about the Document‑Driven Development (DocDD) methodology. Keep changes focused, minimal, and verifiable.

## Workflow
- Prefer small PRs scoped to one topic.
- Update `SUMMARY.md` when adding/moving chapters.
- Run a local build before pushing; ensure links are valid.

## Pre‑commit Hook
- Install once per clone to enforce local checks:
  - `make install-hooks`
- What it does: runs `make check` (mdbook build + linkcheck) and blocks commits on failure or when `mdbook` is missing.
- Install tools if needed: `make setup`.

## Style
- One H1 per page; concise, bullet‑first writing.
- Use relative links within `src/`.
- Keep file names lowercase, hyphen‑separated.

## Commits & PRs
- Conventional commits preferred (e.g., `docs(authoring): …`).
- Include a brief rationale and screenshots/links when helpful.
- Let CI run; fix any build/link failures prior to review.

