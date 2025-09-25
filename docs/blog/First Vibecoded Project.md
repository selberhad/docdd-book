# Shipping My First Fully AI‑Coded Project

*Note: while written in the first-person human perspective, this is a fully AI-generated blog post.*

I just shipped my first project where I didn’t write or read a single line of code. I set the direction, tested the UX, made calls, and the AI handled all implementation details. It was fast, collaborative, and honestly—pretty fun.

Repository: https://github.com/selberhad/chatgpt-export-viewer

## What We Built

- A suite of tiny, composable terminal CLIs to browse ChatGPT export ZIPs.
- Core tools:
  - `browsezip`: two‑pane ZIP browser with metadata, inline JSON preview, and external open.
  - `gptbrowser`: conversation list + reader with search and transcript export.
  - `zipmeta`: stream ZIP entry metadata as JSON.
  - `listzip`, `jsontree`, `tuilist`, `mapping-reduce`: focused utilities you can compose.
- Cross‑platform by default: works on macOS, Linux, and Windows.

## Why It Works

- Small CLIs + JSON I/O: easy to test, easy to automate, easy to debug.
- Keyboard‑first UX: arrows/jk to move, `/` to search, `n/N` to jump matches, `]`/`[` to jump messages.
- Clear separation of concerns:
  - `lib/zip.js`: fast ZIP access via `yauzl`.
  - `lib/gpt.js`: turns ChatGPT mappings into readable message sequences; exports transcripts.
  - `lib/terminal.js`: shared TUI primitives (menus, wrapping, status lines, search wiring).
  - `lib/open_external.js`: cross‑platform launcher for external previews.
  - `lib/viewers.js`: spawners for the JSON tree viewer.

## Notable UX Wins

- Instant list scrolling with live metadata panel in `browsezip`.
- Unified list search: `/` to search with live highlight, `Enter` to accept, `ESC` to cancel, `n/N` next/prev match.
- Conversation reader: role‑colored transcripts, message jumps, in‑text search, one‑key export.
- Clean exits with cursor restore—even on Ctrl‑C.

## Engineering Touches I’m Happy With

- DRY internals:
  - `makeListSearch()` and `wrapLines()` shared across tools.
  - JSON viewer spawner extracted to a single helper.
  - Transcript export centralized in `exportConversationPlain()`.
- Cross‑platform external open (`open`, `xdg-open`, `start`) with graceful fallbacks.
- Packaging discipline:
  - CLIs exposed via `bin` entries; easy to run globally or with `npx`.
  - Tight `files` whitelist and `.npmignore` to avoid shipping data.
- Quality gates:
  - ESLint v9 flat config + Prettier with auto‑fix.
  - Simple scripts: `npm run lint:fix` and `npm run format`.

## The Human/AI Split That Felt Right

- My part:
  - Define the product slice, keyboard UX, scope, and constraints.
  - Validate behavior by testing real exports and pushing on edge cases.
  - Decide on refactors, naming, and user‑facing details.
- The AI’s part:
  - Implement the CLIs and libs, factor out shared patterns, tighten packaging.
  - Wire robust defaults (cursor restore, temp cleanup, structured errors).
  - Migrate to modern lint/format setups and resolve warnings.

## Development Rhythm

- Start with KICKOFF doc.
- Follow plan to incrementally implement minimal tools that compose: list → metadata → preview.
- Add specialized views only when the primitives feel right (the GPT browser).
- Keep iterating: refactor to `makeListSearch`, extract `open_external`, add exports, clean packaging.

## What I Learned

- CLIs + JSON are a sweet spot for AI pair‑work: deterministic, composable, and easy to test.
- Shared primitives (search, wrapping, viewer launchers) reduce complexity everywhere.
- Publishing polish (bin entries, files list, repo metadata, ignore lists) matters more than it seems.
- Lint/format as a first‑class step keeps “LLM style noise” out and makes diffs readable.

## Try It

- Global install:
  - `npm i -g chatgpt-export-viewer`
  - Run: `gptbrowser zips/export.zip` or `browsezip zips/export.zip`
- Or npx:
  - `npx -y -p chatgpt-export-viewer gptbrowser zips/export.zip`

## What’s Next

- “Export all conversations” helper.
- Tiny smoke tests and CI for lint/format.
- A short screencast or asciinema demo.

## Closing Thought

This felt like product management meets pair programming—with an agent that never gets tired of refactoring. I set direction and taste; it did the code. The result isn’t just a demo—it’s a polished, cross‑platform tool I’m happy to release.
