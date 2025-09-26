# Archive Browser Spec

This example demonstrates a complete SPEC.md file from the Archive Browser project. This specification guided development of the shipped NPM package for viewing ChatGPT conversation exports.

---

```markdown
# SPEC.md

Archive Browser, Stage 1 (Toy A + Toy B)

Scope: Implement the first two primitives for the Archive Browser kickoff (Stage 1), without integration.
- Toy A: ZIP Metadata Reader (`zipmeta`)
- Toy B: TUI List (`tuilist`)

No extrapolation beyond existing docs: this SPEC defines minimal contracts and invariants to enable TDD for Stage 1.

## 1. Invariants

- Determinism: Same input → same output; no hidden state in outputs.
- Legibility: JSON I/O; structured error JSON on stderr.
- Parsimony: Avoid unnecessary work; stream and avoid file content reads for Toy A.
- Responsiveness (Toy B): Rendering a large list (≥10k items) does not visibly lag on navigation.

---

## 2. Toy A — ZIP Metadata Reader (`zipmeta`)

### Purpose
Read a ZIP file’s central directory and emit a JSON array of entries (metadata only). Do not read file contents.

### Input (stdin JSON)

    {
      "zip_path": "./path/to/archive.zip"
    }

### Output (stdout JSON)
Array of entry objects, ordered by central directory order.

    [
      {
        "name": "conversations/2024-09-30.json",
        "compressed_size": 12345,
        "uncompressed_size": 67890,
        "method": "deflate",
        "crc32": "89abcd12",
        "last_modified": "2024-09-30T12:34:56Z",
        "is_directory": false
      }
    ]

Notes:
- `method` is a human label derived from the ZIP method code.
- `last_modified` is normalized UTC ISO8601 if available; otherwise omit.

### Errors (stderr JSON)
On failure, emit a single JSON object to stderr; no stdout payload.

    { "type": "ERR_ZIP_OPEN", "message": "cannot open zip", "hint": "check path and permissions" }
Other representative errors:
- `ERR_ZIP_NOT_FOUND` — path does not exist
- `ERR_ZIP_INVALID` — invalid/corrupt ZIP central directory

---

## 3. Toy B — TUI List (`tuilist`)

### Purpose
Render a scrollable list of strings with instant navigation. Stage 1 validates rendering performance and interaction loop structure; selection semantics may be finalized during integration.

### Input / Output
- Input: JSON array of strings on stdin.
- Output: For Stage 1, stdout may be empty or a minimal confirmation object; interaction is the focus. Errors use structured JSON on stderr if startup fails.

Example input (stdin):

    ["a.json", "b.json", "c.html"]

Example minimal output (stdout):

    { "ok": true }

### Errors (stderr JSON)

    { "type": "ERR_TUI_INIT", "message": "terminal init failed", "hint": "verify terminal supports required features" }

---

## 4. Operations

- Toy A `zipmeta`:
  - Open ZIP, iterate central directory entries, map metadata to the output schema.
  - Never read file contents; stream and collect metadata only.
  - Normalize fields (method label, crc32 hex, optional last_modified).
- Toy B `tuilist`:
  - Initialize terminal UI, render list from stdin array.
  - Provide non-blocking navigation; ensure smooth, low-latency scroll.

---

## 5. Validation Rules

- Toy A produces identical JSON given the same `zip_path`.
- Toy A handles non-existent/invalid ZIP paths with structured errors.
- Toy B starts without throwing; renders lists up to ≥10k items without visible lag.
- Toy B exits cleanly on user quit (e.g., Esc/Ctrl-C), leaving terminal in a good state.

---

## 6. Test Scenarios (Golden + Error Cases)

- Toy A Golden: small known ZIP → stable JSON array (order and fields match).
- Toy A Large: large ZIP central directory streams without memory blow-up; completes.
- Toy A Errors: missing path; corrupt file → structured error.
- Toy B Golden: feed 100 sample items → UI initializes and returns `{ "ok": true }` on immediate quit.
- Toy B Stress: feed ≥10k items → navigation is smooth; startup succeeds.

---

## 7. Success Criteria

- [ ] `zipmeta` emits correct JSON metadata without reading file contents.
- [ ] `zipmeta` error paths return structured JSON on stderr only.
- [ ] `tuilist` initializes, renders, and exits cleanly.
- [ ] `tuilist` remains responsive with large lists (subjective but observable).
- [ ] Both tools follow CLI + JSON purity (no hidden state in outputs; logs allowed).

*** End of Stage 1 SPEC ***
```
