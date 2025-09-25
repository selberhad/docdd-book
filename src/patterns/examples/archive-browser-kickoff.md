# Project Kickoff

A clarity-first, agent-oriented development plan for building a lightning-fast TUI archive browser for ChatGPT export ZIPs.  
This document is disposable scaffolding: clarity and validated integrations are the true outputs.

---

## Napkin Physics

- **Problem**: We need a non-laggy, lightning-fast TUI to browse ChatGPT export ZIPs containing JSON, HTML, and hundreds of image files.
- **Assumptions**:
  - Archives can grow large (thousands of entries, gigabytes in size).
  - Performance > developer ergonomics (the developer is an LLM).
  - Implementation target: Node.js v20 with `yauzl` (ZIP) + `terminal-kit` (TUI).
  - Responsiveness depends on lazy rendering, precomputed metadata, and diff-based screen updates.
- **Invariant**: Every user interaction (scrolling, searching, previewing) must feel instantaneous — no noticeable lag.
- **Mechanism**:
  1. Use `yauzl` to stream central directory and precompute metadata.
  2. Render scrollable file list with `terminal-kit`.
  3. Display metadata in side panel; update on highlight.
  4. Lazy-load previews (JSON/HTML inline, images as stubs/external).
  5. Add fuzzy search to filter entries without slowing navigation.

---

## Binary-Weave Plan

Each stage introduces at most one new primitive, then integrates it with an existing validated toy. This continues until the final product emerges.

### Stage 1 — Primitives

- **Toy A**: ZIP Reader  
  Reads central directory, outputs JSON metadata for all entries.
- **Toy B**: TUI List  
  Displays an array of strings in a scrollable, instant navigation list.

### Stage 2 — First Integration

- **C = A + B** → Archive Lister  
  Combine ZIP Reader with TUI List.  
  Behavior: display archive entries in a scrollable list.  
  Invariant: open + scroll is instant regardless of archive size.

### Stage 3 — New Primitive

- **Toy D**: Metadata Panel  
  Displays key-value metadata (size, method, CRC, etc.) in a side panel.

### Stage 4 — Second Integration

- **E = C + D** → Entry Browser  
  Combine Archive Lister with Metadata Panel.  
  Behavior: highlight an entry in list, show details in panel.  
  Invariant: panel update is instant on keypress.

### Stage 5 — New Primitive

- **Toy F**: File Previewer (text only)  
  Opens JSON/HTML entries, streams to popup.  
  Must be cancelable and non-blocking.

### Stage 6 — Third Integration

- **G = E + F** → Text Browser  
  Combine Entry Browser with File Previewer.  
  Behavior: press Enter on a JSON/HTML file to preview inline.  
  Invariant: browsing stays snappy; previews load lazily.

### Stage 7 — New Primitive

- **Toy H**: Image Stub  
  Detects image files, shows placeholder `[IMG] filename`.  
  Optional: launch via external viewer.

### Stage 8 — Fourth Integration

- **I = G + H** → Full Viewer  
  Combine Text Browser with Image Stub.  
  Behavior: one interface handles JSON, HTML, and image entries.  
  Invariant: non-text files never block UI.

### Stage 9 — New Primitive

- **Toy J**: Search/Filter  
  Provides fuzzy filename search.  
  Invariant: filtering large lists is instant.

### Stage 10 — Final Integration

- **K = I + J** → Archive Browser Product  
  Combine Full Viewer with Search/Filter.  
  Final features:
  - Scrollable list of entries
  - Metadata side panel
  - Inline preview for JSON/HTML
  - Image handling stub
  - Fuzzy search/filter  
    Invariant: every keypress (nav, search, preview) feels immediate.

---

## End State

- **Final Product**: Lightning-fast Node.js archive browser for ChatGPT exports.
- **Process**: 5 primitives (A, B, D, F, H, J) woven into 5 integrations (C, E, G, I, K).
