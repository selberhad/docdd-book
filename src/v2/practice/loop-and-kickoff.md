# DocDD Loop & Kickoff

This chapter contains the “how” once: the Docs → Tests → Implementation cadence, and the Binary‑Weave kickoff pattern for integrating primitives incrementally.

The loop (one slice)
1) Docs
   - SPEC: define the smallest viable contract (I/O, invariants, commands).
   - PLAN: list the minimal test‑first steps with success criteria and risks.
2) Tests
   - Derive tests directly from the SPEC; include error paths and an end‑to‑end case.
3) Implementation
   - Write only enough code to pass; prefer a single‑file spike first.
4) Learnings
   - Capture what held, what failed, constraints discovered, and the next cut.

Kickoff: Binary‑Weave
- Introduce exactly one new primitive at a time (Toy A, Toy B, …).
- Immediately integrate it with the current product (A+B=C, C+D=E, …).
- Each integration yields the new “current product”.
- Avoid multi‑merge steps; limit integrations to two inputs.

Napkin Physics before the loop
- Problem (1 sentence), Assumptions (3–5), Invariant (crisp property), Mechanism (≤5 bullets), First Try.
- Goal: upstream simplification to avoid over‑scoping; no frameworks/new nouns without deleting two.

Checklists
- Slice readiness: SPEC is falsifiable; PLAN has step‑level criteria; risks named.
- Test completeness: happy path, error path, and at least one end‑to‑end example.
- Review gate: SPEC/PLAN diffs, pass/fail, next step proposal.

Anti‑patterns
- Repeating the loop in multiple places; this chapter is the single source.
- Big Bang integration; prefer weave steps.
- Over‑detailed kickoffs; kickoff maps the weave, specs carry details.

Cross‑references
- Foundations: [Doc‑Driven Principles](../../v2/foundations/ddd-principles.md), [Napkin Physics](../../v2/foundations/napkin-physics.md)
- Guides: [Kickoff Writing](../../guides/writing/kickoff.md), [Playbook (legacy)](../../playbooks/playbook.md)
