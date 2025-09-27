# Archive Browser Code Map

This example demonstrates a complete CODE_MAP.md file from the Archive Browser project. This architectural documentation provided ongoing orientation for both human developers and AI agents throughout development of the shipped NPM package.

---

```markdown
# CODE_MAP.md

This document orients you to the project structure, what each file does, and how the pieces fit together at a high level.

## Architecture Overview

- Purpose: Terminal-based tools to explore ChatGPT export ZIPs quickly with keyboard-centric UX.
- Design: Small composable CLIs built on a thin library layer.
  - UI: `terminal-kit` powers list menus, panes, and key handling.
  - ZIP I/O: `yauzl` streams metadata and file contents without full extraction.
  - GPT utils: Helpers reduce OpenAI export mappings into readable message sequences.
  - OS helpers: Minimal macOS integration for "open externally" convenience.
- Data Flow (typical):
  1. CLI parses args or JSON from stdin (`lib/io.js`).
  2. ZIP operations query or stream entries (`lib/zip.js`).
  3. TUI renders lists/panels and handles keys (`lib/terminal.js`).
  4. Optional: spawn specialized viewers (JSON tree, GPT browser) or export to files.

## Key Directories

- `cli/`: Executable entry points for each tool (users run these via npm scripts).
- `lib/`: Reusable helpers for ZIP I/O, GPT export reduction, terminal UI, and small OS shims.
- `backup1/`: Example data from a ChatGPT export (for local dev/testing).
- `zips/`: Sample export ZIPs used by the tools.
- `artifacts/`: Logs/JSON artifacts from runs.

## Libraries (`lib/`)

- `lib/zip.js`
  - Thin wrappers around `yauzl` for reading ZIPs:
    - `listNames(zipPath)`: stream all entry names.
    - `readMetadata(zipPath)`: emit metadata for each entry (name, sizes, method, crc32, directory flag, last_modified).
    - `readEntryText(zipPath, entryName)`: read a specific entry as UTF-8 text.
    - `extractEntry(zipPath, entryName, destPath)`: extract one entry to disk.
    - `extractToTemp(zipPath, entryName, prefix)`: extract a single entry into a unique temp dir; returns `{ dir, file }`.
    - `cleanupTemp(path)`: best-effort recursive removal.

- `lib/gpt.js`
  - Utilities to transform ChatGPT export structures:
    - `extractTextFromContent(content)`: normalize message content to text (handles common shapes, multimodal parts).
    - `extractAuthor(message)`: infer `user`/`assistant`/fallback from message author fields.
    - `buildMainPathIds(mapping, currentNodeId)`: follow parent pointers to root.
    - `autoDetectLeafId(mapping)`: choose a reasonable leaf when `current_node` is absent.
    - `reduceMappingToMessages(mapping, { currentNodeId, includeRoles })`: produce a minimal `[{ author, text }]` sequence along the main path.
    - `buildPlainTextTranscript(messages)`: render a readable transcript string.
    - `exportConversationPlain(title, messages)`: write a plain-text transcript to `exports/` and return the file path.

- `lib/open_external.js`
  - `openExternal(path)`: cross‑platform opener. macOS: `open`; Windows: `cmd /c start`; Linux/Unix: try `xdg-open`, `gio open`, `gnome-open`, `kde-open`, `wslview`.

- `lib/terminal.js`
  - Terminal helpers built on `terminal-kit`:
    - Exported `term` instance plus utilities: `paneWidth`, `status`, `statusKeys`, `statusSearch`, `printHighlighted`, `drawMetaPanel`.
    - Cursor/cleanup: `ensureCursorOnExit()`, `restoreCursor()`, `terminalEnter()`, `terminalLeave()`.
    - Menus: `withMenu()` (callback-based singleColumnMenu), `listMenu()` (fixed viewport, keyboard-driven; supports highlight query), `listMenuWrapped()` (wrapped multi-line items), `makeListSearch()` (reusable "/" + n/N search wiring for lists), `wrapLines()` (text wrapper).
    - Note: `cursorToggle()` wraps terminal-kit’s `hideCursor()`, which actually toggles cursor visibility (misnamed upstream). Our name reflects the real behavior.

- `lib/io.js`
  - I/O utilities shared by CLIs:
    - `emitError(type, message, hint)`: structured JSON errors to stderr.
    - `readStdin()`: read entire stdin as UTF-8.
    - `resolvePathFromArgOrStdin({ key })`: accept arg or JSON stdin for paths.
    - `jsonParseSafe(text)`: tolerant JSON parse.
    - `safeFilename(title)`: sanitize to a portable file name base.
    - `ensureDir(dirPath)`, `writeFileUnique(dir, base, ext, content)`: mkdir -p + non-clobbering writes.

- `lib/viewers.js`
- `showJsonTreeFile(filePath)`: spawn the JSON tree viewer for a file.
- `showJsonTreeFromObject(obj, opts)`: write a temp JSON and spawn the viewer; cleans up temp dir.

## CLIs (`cli/`)

- `cli/zipmeta.js`
  - Emits ZIP metadata as JSON. Accepts path via argv or stdin JSON (`{"zip_path":"..."}`) and writes an array of entry objects to stdout.

- `cli/listzip.js`
  - Scrollable list of ZIP entry names using `terminal-kit`'s single-column menu. Pure navigation; Enter exits.

- `cli/tuilist.js`
  - Scrollable list sourced from stdin JSON array of strings. Useful as a standalone picker component.

- `cli/jsontree.js`
  - Inline JSON tree viewer with expand/collapse, arrow/j/k/h/l movement, page/top/bottom, and a compact status line.
  - Accepts a file path arg or JSON via stdin.

- `cli/browsezip.js`
  - Two-pane browser for a ZIP:
    - Left: instant-scroll list of entries (keyboard-driven viewport).
    - Right: live metadata panel (`drawMetaPanel`).
    - Enter: inline JSON tree preview for `*.json` (extracts to temp, spawns JSON tree via `lib/viewers.js`).
    - `o`: open highlighted entry externally (extracts to temp, calls macOS `open`).
    - `v`: if `conversations.json` at ZIP root, launches `cli/gptbrowser.js` for a specialized view.

- `cli/mapping_reduce.js`
  - Utility to convert a `mapping` (or an item from `conversations.json`) into a minimal message sequence JSON.

- `cli/gptbrowser.js`
  - Specialized viewer for ChatGPT export ZIPs:
    - Reads `conversations.json` from the ZIP, shows a searchable conversation list with live match highlighting.
    - Opens a conversation into a large scrollable text view with role-colored lines, next/prev message jumps, and in-text search (`/`, `n/N`).
    - Export: writes plain-text transcripts to `exports/<title>.txt` (non-clobbering).

## Root and Supporting Files

- `package.json`
  - Declares `type: module`, `bin` entries for each CLI, and npm scripts for local runs.
  - Dependencies: `terminal-kit`, `yauzl`, `string-kit`.

- `README.md`
  - User-facing overview, requirements, usage examples, and key bindings.

- `KICKOFF.md`
  - Project kickoff notes (context and initial direction).

- `split_chapter.sh`
  - Shell script utility (repo-local helper; not used by the CLIs).

- `readme.html`
  - HTML export of the README for viewing in a browser.

- Data/example folders:
  - `backup1/`: Sample JSON files (e.g., `conversations.json`) for local experiments.
  - `zips/`: Example ChatGPT export ZIPs.
  - `artifacts/`: Run logs and metadata captures.

## How Things Work Together

- ZIP Browsing Path
  - `cli/browsezip.js` → `lib/io.js` (args) → `lib/zip.js` (metadata) → `lib/terminal.js` (list + panel) →
    - Enter: extract + spawn `cli/jsontree.js` for JSON.
    - `o`: extract + `lib/open_external.js` to open externally.
    - `v`: spawn `cli/gptbrowser.js` for GPT-specialized browsing.

- GPT Browsing Path
  - `cli/gptbrowser.js` → `lib/zip.js.readEntryText('conversations.json')` → `lib/gpt.js.reduceMappingToMessages()` →
    UI render via `lib/terminal.js` (search, highlight, navigation) →
    Optional export via `lib/io.js.writeFileUnique()`.

- Safety and UX
  - Cursor visibility and TTY cleanup are handled centrally by `ensureCursorOnExit()`.
  - CLIs print structured JSON errors to stderr for deterministic automation.
  - Temporary files are isolated and cleaned when possible; external open uses a temp cache on macOS.

## Notes / Known Issues

- `cli/gptbrowser.js` references `statusSearch` in its message view but must import it from `lib/terminal.js` to avoid a `ReferenceError`.
- Cursor control: terminal-kit's `hideCursor()` is a toggle; we expose it as `cursorToggle()` to make that explicit. Cursor is restored on exit by `ensureCursorOnExit()`.
- Inline preview in `cli/browsezip.js` is JSON-only; consider extending to small text types (`.txt`, `.md`) or surfacing a status hint when Enter does nothing.
```
