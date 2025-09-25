# Toy‑Model Rationale

Toy models are scientific experiments, not products. Their purpose is to learn, reduce risk, and sharpen architectural clarity — not to ship.

What toy models are
- Focused experiments: each toy validates a single idea.
- Cheap and discardable: code is expendable; insight is what matters.
- Architectural probes: test assumptions, reveal edge cases, expose integration challenges.
- Learning accelerators: fast cycles of build → test → document.

What they are not
- Not production systems or comprehensive solutions; not sacred code; not shortcuts to “done”.

Cycle
1) SPEC.md — define data, operations, success criteria, and failure cases.
2) PLAN.md — sequence minimal test‑first steps and risks.
3) Implementation — write only enough code to pass tests.
4) LEARNINGS.md — record what worked/failed, patterns, integration implications.

Guiding principles
- TDD is mandatory (red → green → next).
- Errors are specific and actionable; structure them.
- Event sourcing helps you replay and inspect state evolution.
- Minimal dependencies, maximum clarity; avoid frameworks.
- Export insights in multiple formats when useful (JSON/DOT/CSV).

Patterns that work
- Single‑class toys for small cohesive experiments.
- Module‑based toys when responsibilities split naturally.
- Adapters when integrating external systems.

Testing philosophy
- Prefer properties (invariants) over ad‑hoc examples.
- Include complex end‑to‑end scenarios and deliberate error paths.

Strategic guidance
- Pivot early when a better approach appears; persist only when gains are real.
- Preserve learnings even when discarding code; keep APIs/data consistent across toys.

North star
Gardening, not construction: cultivate understanding; clarity over permanence.
