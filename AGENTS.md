# Repository Guidelines

This repository contains curated, versioned documentation for AI meta workflows. All content lives as Markdown files in the repo root; there is no build step or runtime.

## Project Structure & Module Organization
- Root docs: `README.md`, `DOC_MAP.md`, playbooks (`PLAYBOOK_V*.md`), specs (`SPEC_*.md`), plans (`PLAN*.md`), guides (e.g., `DEBUGGERS.md`).
- Versioning pattern: keep prior versions, add new files with suffixes like `_V2`, `_V6` (e.g., `PLAYBOOK_V6.md`).
- When adding or replacing docs, update cross-links and lists in `README.md` and `DOC_MAP.md`.

## Build, Test, and Development Commands
- No build required: open `.md` files in your editor and use Markdown preview.
- Optional linting (if installed locally): `markdownlint **/*.md`
- Optional spell/links (if installed): `cspell **/*.md`, `markdown-link-check README.md`

## Coding Style & Naming Conventions
- Headings: use ATX style (`#`, `##`, `###`); one H1 per file.
- Tone: instructional, concise, repository-specific; avoid fluff.
- Lists: hyphen bullets; keep lines short and scannable.
- Code blocks: use fenced blocks with language tags when relevant.
- Filenames: UPPER_SNAKE_CASE with topic and optional version suffix (e.g., `SPEC_V2.md`).

## Testing Guidelines
- Validate: headings hierarchy, internal anchors, and relative links.
- Check: examples render correctly and commands are copy-pastable.
- Run optional linters if available; otherwise, manual pass for spelling and clarity.
- Preferred link style: relative paths (e.g., `[Spec](./SPEC_V2.md)`).

## Commit & Pull Request Guidelines
- Commits: imperative mood, scope-first; prefer Conventional Commits (e.g., `docs(spec): clarify data contracts`).
- PRs should include:
  - Summary of changes and motivation.
  - Linked issues (if any).
  - List of affected files and key sections.
  - Confirmation that `README.md` and `DOC_MAP.md` are updated as needed.

## Architecture & Maintenance Notes
- Treat major changes as new versions; leave historical files intact.
- Add a short “Changelog” section at the top of new versions summarizing deltas.
- Keep examples practical; prefer shell-agnostic commands when possible.
