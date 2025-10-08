# PLAYBOOK.md — Dialectic‑Driven Development with Binary‑Weave Kickoff (V4)

A clarity‑first, agent‑oriented methodology that expands the V3 doctrine with a strict, sequential kickoff format, while avoiding the prescriptive bloat that crept into V1.

---

## 1. Purpose

Dialectic‑Driven Development (DDD) turns ambiguous problems into deterministic, legible systems by cycling through lightweight docs, disposable toy models, and incremental integrations. This version adds a binary‑weave kickoff: new primitive → integrate with the prior product, repeated until the final product emerges.

---

## 2. Core Principles

- Docs as control surfaces (SPEC, PLAN, LEARNINGS, README).
- Toys, not monuments: intermediate code is disposable; insight is durable.
- Parsimony: simplest mechanism that works today.
- Determinism: same input → same output; minimize hidden state.
- Legibility: make state inspectable to humans and agents (often via JSON and simple CLIs).
- Two‑at‑a‑time integration: never combine more than two at once.

See also: [[DDD]], [[TOY_DEV]].

---

## 3. The DDD Loop

1. SPEC.md — Define minimal behavioral contract (inputs, outputs, invariants, error cases).
2. PLAN.md — Outline the smallest step to test the contract (sequence, risks, success criteria).
3. Implementation — Write the minimal code needed to pass the tests.
4. LEARNINGS.md — Record what worked, what failed, and the constraints/invariants discovered.

Repeat until the slice is validated or retired.

---

## 4. Napkin Physics

Upstream simplification before SPEC/PLAN:
- Problem (one sentence)
- Assumptions (3–5 bullets)
- Invariant/Contract (one precise property)
- Mechanism (≤5 bullets describing the minimal spike)
- First Try (one paragraph with the simplest path)

Prohibitions: no frameworks, no new layers, no new nouns unless two are deleted elsewhere.

See: [[DDD]].

---

## 5. Kickoff: The Binary‑Weave Plan

The goal is a single, explicit weave — not a flat list of toys, not parallel streams. The weave always alternates: new primitive → integration with prior product.

Core shape:
1) Napkin Physics (problem, assumptions, invariant, mechanism)
2) Binary‑Weave Plan:
   - Introduce exactly one new primitive at a time (Toy A, Toy B, Toy C …)
   - Integrate it with the prior product (A+B=C, C+D=E, …)
   - Each integration produces the new “current product”
   - No step introduces more than one new primitive
   - No integration combines more than two things
   - Continue until the final product emerges
3) End State:
   - Name the final product
   - Summarize woven primitives and integrations
   - State the durable invariants
   - Final docs + system remain; toys are discarded; learnings are kept

Formatting expectations:
- Stage numbering is sequential (no parallel numbering)
- Each stage has: Name (Toy or Integration), What it does (one sentence), Invariant
- Avoid over‑specification: the kickoff is a weave map, not a spec
- Avoid skipping: follow the weave pattern strictly

One‑shot checklist:
- [ ] Napkin Physics included
- [ ] Sequential stages
- [ ] Exactly one new primitive per stage
- [ ] Integration always combines current product with one new primitive
- [ ] Final product and invariants stated at end

Source: [[KICKOFF_WRITING]].

---

## 6. Toy Models

Definition: small, sharply scoped, fully specced implementations designed to be thrown away.

Cycle: SPEC.md → PLAN.md → Tests → Minimal implementation → LEARNINGS.md.

Principles:
- Tests‑first; minimal dependencies; structured errors; event sourcing when useful.
- Axis discipline: a base toy isolates one axis (invariant, mechanism, or seam). An integration toy merges exactly two axes to probe interaction. Never exceed two axes per toy.

Exit criteria: all step‑level success criteria checked; insights recorded; follow‑up scope cut.

See: [[TOY_DEV]], [[DDD]].

---

## 7. JSON + CLI Convention (Debugger Mode)

Goal: enable the agent to single‑step systems deterministically, inspect state, and bisect.

Contract (per module):
- stdin: JSON input
- stdout: JSON output
- stderr: machine‑parsable error JSON when failing
- Purity and determinism: same input → same output (no hidden state); logs allowed; outputs remain pure

Error JSON shape:
```
{ "type": "ERR_CODE", "message": "human text", "hint": "actionable fix" }
```

Schema‑first: document input/output JSON schemas and versions in SPEC.md.

Quick test: each CLI ships with a one‑command golden test path.

See: [[DEBUGGERS]], [[DDD]].

---

## 8. Pipelines & Golden Tests

Minimal pipeline pattern (UNIX‑style composition):
```
modA < in.json > a.json
modB < a.json > b.json
modC --flag X < b.json > out.json
```

Execution traces: chain modules to produce inspectable intermediates; walk step by step, verify against SPEC.

Golden tests as breakpoints: one‑liner baselines to verify behavior before changes; deterministic checkpoints to prevent drift.

Snapshot tests: permissible for textual outputs with stable normalization rules.

See: [[DDD]], [[DEBUGGERS]].

---

## 9. Planning & Testing (Concise)

Planning (PLAN.md): step template with tests‑first, then implementation; success criteria checkboxes; explicitly state what to test vs. skip; outline risks and dependencies.

Testing strategy: unit tests per function/CLI; golden I/O tests for pipelines; error‑path tests; contract/schema validation; snapshot tests with stable normalization.

See: [[PLAN_WRITING]], [[DDD]].

---

## 10. Guardrails & Self‑Audit (Concise)

Dependencies and complexity:
- Default allowlist; justify new imports in SPEC and whitelist in PLAN
- Prefer single‑file spikes when feasible
- Constrain new abstractions; keep function length and complexity in check

Errors, cost, and privacy:
- Handle top two failure modes with structured errors; no secret leakage
- Track representative token/$ and p95 latency in LEARNINGS
- No PII in fixtures; redact or synthesize test data

Self‑audit metrics before proposing diffs:
- file_count_changed; total_added_lines; imports_added_outside_allowlist; new_named_abstractions; max_function_cyclomatic_complexity; average_function_length; test_count_added vs prod_functions_touched

Review gates and outcomes: present summary, SPEC/PLAN diffs, test results, pipeline diffs; outcomes include approve, revise_docs, revise_tests, revise_impl, abort.

See: [[DDD]].

---

## 11. Heuristics & Anti‑Patterns (Concise)

Simplification heuristics:
- One‑File Spike (≤120 lines when feasible)
- Two‑Function Rule: parse(input)→state; apply(state,input)→state|output
- No New Nouns unless two are deleted
- 80/20 Errors; Time‑Boxed Satisficing

Plan anti‑patterns:
- No full test code in Plan; no full implementation code; avoid over‑detail

See: [[DDD]], [[PLAN_WRITING]].

---

## 12. Adoption & Layout (Concise)

Retrofitting to CLI+JSON:
- Expose pure CLI (stdin JSON, stdout JSON, stderr structured error JSON)
- Ensure determinism; document schemas; add a one‑command golden test
- Compose into a minimal pipeline; capture intermediate artifacts

Repository layout expectations:
- /libs/<name>/README.md; /docs/SPEC.md; /docs/PLAN.md; /docs/LEARNINGS.md
- /schemas/*.json; /cli/*; /tests/*; /fixtures/*.json

See: [[DDD]].

---

## 13. Appendices (Templates)

KICKOFF.md — skeleton:
```
# KICKOFF.md — Binary‑Weave Plan

## Napkin Physics
- Problem (1 sentence)
- Assumptions (3–5 bullets)
- Invariant (one crisp property)
- Mechanism (≤5 bullets)

## Stages (sequential)
- Stage 1 — Primitive A
  - What it does: …
  - Invariant: …
- Stage 2 — A + B = C (Integration)
  - What it does: …
  - Invariant: …
- Stage 3 — Primitive D
  - What it does: …
  - Invariant: …
# …continue until final product

## End State
- Final product: …
- Woven primitives/integrations: …
- Durable invariants: …
- Final docs + system remain; toys discarded; learnings kept
```

PLAN.md — step template (tests‑first; then implementation; success criteria checkboxes).

LEARNINGS.md — header, summary (Built/Worked/Failed/Uncertain), evidence (Validated/Challenged/Failed/Uncertain), pivots, impact; one page, dense and factual.

README.md — header + one‑liner; purpose (2–3 sentences); key API (3–5 methods); core concepts; gotchas; quick test.

See: [[KICKOFF_WRITING]], [[PLAN_WRITING]], [[LEARNINGS_WRITING]], [[README_WRITING]].

---

End notes: the true product is clarity (contracts, constraints, invariants, working integrations). Everything else is scaffolding.

*** End of V4 ***
