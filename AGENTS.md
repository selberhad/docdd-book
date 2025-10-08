# Repository Guidelines (AI + Humans)

This repo contains an mdBook about the Dialectic‑Driven Development (DDD) methodology. Keep changes focused, minimal, and verifiable.

**See also:** `CLAUDE.md` for comprehensive development guidance.

## Workflow
- Prefer small PRs scoped to one topic.
- Update `SUMMARY.md` when adding/moving chapters.
- Run `make check` only when changing the book (`src/**`, `SUMMARY.md`, `book.toml`). Skip for other docs (`docs/**`, root `*.md`).

## Pre‑commit Hook
- Install once per clone: `make install-hooks`
- What it does:
  - Runs `make check` (mdbook build + linkcheck)
  - Auto-generates `STATS.md` with current word counts and reading time
  - Blocks commits on build failures or missing mdbook
- Install tools if needed: `make setup`

## Content Guidelines
- **One H1 per page** with concise, bullet-first writing
- **Agent-oriented guides:** Authoring guides in `src/authoring/` are templates for AI agents to copy into repositories
- **Examples structure:** Use flat file naming with prefixes (e.g., `archive-browser-plan.md`) for multiple example projects
- Use relative links within `src/`
- Keep file names lowercase, hyphen-separated

## Development Commands
```bash
make setup    # Install mdbook and linkcheck tools
make serve    # Live preview with hot reload
make check    # Build + linkcheck validation
make stats    # Generate book statistics
```

## Commits & PRs
- **Commit messages:** Use conventional format, keep concise for small changes (one short line)
  - Good: `docs(authoring): improve spec template`
  - Avoid: Long multi-paragraph commit messages for simple edits
- **Scope and subject:** Derive the one-line subject from the staged diff; describe the primary artifact change in imperative mood; avoid process details.
  - Sanity-check before committing: `git diff --cached --name-status`.
- **When to commit:** Only commit when explicitly prompted by the user
- **Commit and push:** When user explicitly asks to "commit and push", chain commands: `git commit ... && git push origin main`
- CI automatically skips runs for changes to `docs/**` or root `*.md` files
- Let CI run; fix any build/link failures before review
