# Napkin Physics

Upstream simplification to prevent scope drift. Capture the problem and constraints on a “napkin” before writing detailed docs.

Structure

- Problem: one sentence.
- Assumptions: 3–5 bullets.
- Invariant/Contract: one precise property that must hold.
- Mechanism: ≤5 bullets describing the minimal path (single‑file spike if possible).
- First Try: a short paragraph with the simplest approach.

Prohibitions

- No frameworks; no new layers; no new nouns unless two are deleted elsewhere.

Use it before SPEC/PLAN to encourage parsimony. Keep it short and actionable.

See also: [Doc‑Driven Principles](./ddd-principles.md), [DocDD AGENTS.md Template](../practice/docdd-agents-template.md)
