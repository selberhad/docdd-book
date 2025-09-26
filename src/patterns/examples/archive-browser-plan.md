# Archive Browser Plan

This example demonstrates a complete PLAN.md file from the Archive Browser project. This strategic roadmap guided TDD implementation of the shipped NPM package for viewing ChatGPT conversation exports.

---

```markdown
# PLAN.md

Archive Browser, Stage 1 (Toy A + Toy B)

Overview: Build and validate the two Stage 1 primitives from KICKOFF — Toy A (`zipmeta`) and Toy B (`tuilist`) — using TDD. Keep changes minimal and test-first. Use A/B structure per Plan Writing guide.

Methodology: TDD discipline; tests-first; Red → Green → Next; explicit success criteria; focus on interfaces and contracts.

## Step 1: Toy A — ZIP Metadata Reader (HIGH)

### Step 1.a: Write Tests
- Golden: Small known ZIP → stable JSON array (fields: name, sizes, method label, crc32 hex, optional last_modified, is_directory). Order matches central directory.
- Large: Big ZIP central directory streams without memory blow-up; completes within acceptable time (manual check).
- Errors: Non-existent path → `ERR_ZIP_NOT_FOUND`; corrupt ZIP → `ERR_ZIP_INVALID`; open failure → `ERR_ZIP_OPEN`. No stdout on error.
- Determinism: Same input JSON (`{ zip_path }`) yields identical output JSON.

### Step 1.b: Implement
- Use `yauzl` to open and iterate central directory; do not read file contents.
- Map method code → human label; hex-encode crc32 to 8-char lowercase; include `is_directory`.
- Normalize optional `last_modified` to UTC ISO8601 if available (omit if unknown).
- Emit JSON array to stdout; on error, emit structured error JSON to stderr only.

### Success Criteria
- [ ] Golden output matches expected JSON exactly.
- [ ] Error cases emit structured JSON on stderr and no stdout payload.
- [ ] Determinism verified for repeated runs.
- [ ] No file content reads; central directory only.

---

## Step 2: Toy B — TUI List (HIGH)

### Step 2.a: Write Tests
- Startup: Given JSON array of ~100 strings on stdin, TUI initializes and exits cleanly on immediate quit; stdout may emit `{ "ok": true }`.
- Stress: Given ≥10k items, navigation remains smooth (manual check); startup is non-blocking.
- Error: TUI init failure emits `ERR_TUI_INIT` to stderr; no stdout payload.

### Step 2.b: Implement
- Use `terminal-kit` to render a scrollable list from stdin strings.
- Ensure non-blocking input handling; leave terminal state clean on exit.
- Keep Stage 1 output minimal (e.g., `{ "ok": true }`); finalize selection semantics post-integration.

### Success Criteria
- [ ] TUI starts, renders, and exits cleanly on quit.
- [ ] Stress navigation does not visibly lag (subjective but observable).
- [ ] Structured errors on init failure.

---

## Out of Scope (Stage 1)
- Integration (Stage 2) — combining A + B
- Metadata panel, previewer, image stub, search/filter (later stages)

---

## Risks & Mitigations
- Large ZIPs: stream central directory and avoid content reads to preserve memory.
- TUI responsiveness: keep drawing minimal; avoid synchronous blocking operations.
- Terminal variance: handle init errors gracefully; restore terminal state on exit.

---

## Completion Check
- [ ] Step 1 success criteria all pass
- [ ] Step 2 success criteria all pass
- [ ] SPEC and PLAN reflect actual behavior

*** End of Stage 1 PLAN ***
```
