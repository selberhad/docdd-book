# PLAYBOOK_V5.md — Dialectic-Driven Development with Binary-Weave Kickoff

Clarity-first, agent-oriented methodology. Streamlined from V4 to eliminate redundancy while keeping the binary-weave kickoff at the center.

---

## 1. Purpose

Dialectic-Driven Development (DDD) turns ambiguous problems into deterministic, legible systems by cycling through lightweight docs, disposable toy models, and incremental integrations.  

V5 centers on the binary-weave kickoff: new primitive → integrate with prior product → repeat until the final product emerges.

See also: [[DDD]].

---

## 2. Core Principles

- **Docs as control surfaces** — SPEC, PLAN, LEARNINGS, README.  
- **Toys, not monuments** — intermediate code is disposable; insight is durable.  
- **Parsimony** — simplest mechanism that works today.  
- **Determinism** — same input → same output; minimize hidden state.  
- **Legibility** — make state inspectable (JSON, simple CLIs).  
- **Two-at-a-time integration** — never combine more than two at once.

---

## 3. The DDD Loop

1. SPEC.md — minimal behavioral contract (inputs, outputs, invariants).  
2. PLAN.md — smallest step to test the contract.  
3. Implementation — minimal code to pass the tests.  
4. LEARNINGS.md — record outcomes and constraints.

Repeat until validated or retired.

See: [[PLAN_WRITING]], [[LEARNINGS_WRITING]].

---

## 4. Napkin Physics

Quick pre-spec simplification:  
- Problem (one sentence)  
- Assumptions (3–5 bullets)  
- Invariant (one crisp property)  
- Mechanism (≤5 bullets)  
- First Try (short paragraph, simplest path)

Rules: no frameworks, no new layers, no new nouns unless two are deleted.

See: [[DDD]].

---

## 5. Kickoff: The Binary-Weave Plan

The kickoff is a single sequential weave, not parallel threads.  

Steps:  
1. Write Napkin Physics.  
2. Build Binary-Weave Plan:  
   - Introduce exactly one new primitive (Toy A, Toy B, …).  
   - Integrate it with the current product (A+B=C, C+D=E, …).  
   - Each integration yields the new “current product.”  
   - No step adds more than one primitive; no integration combines more than two.  
3. End State: name the final product, summarize woven primitives, state durable invariants, discard toys, keep docs and learnings.

Checklist:  
- Napkin Physics included  
- Sequential stages, no skips  
- One new primitive per stage  
- Integrations always combine current product + one new primitive  
- Final product and invariants stated

See: [[KICKOFF_WRITING]].

---

## 6. Toy Models

Small, sharply scoped, fully specced implementations designed to be thrown away.  

Cycle: SPEC → PLAN → Tests → Minimal implementation → LEARNINGS.  

Principles:  
- Tests-first; minimal dependencies.  
- Axis discipline: base toy isolates one axis; integration toy merges exactly two axes.  

Exit criteria: step-level success criteria met, insights recorded, scope cut.

See: [[TOY_DEV]].

---

## 7. JSON + CLI Convention

Modules behave like deterministic debuggers:  
- stdin: JSON input  
- stdout: JSON output  
- stderr: structured error JSON  
- Purity: same input → same output; logs allowed, outputs remain pure

Error JSON shape (inline):  
    { "type": "ERR_CODE", "message": "human text", "hint": "actionable fix" }

Schema-first: document I/O schemas in SPEC.  
Each CLI ships with a one-command golden test.

See: [[DEBUGGERS]].

---

## 8. Pipelines & Golden Tests

Compose CLIs in UNIX-style pipelines with inspectable intermediates.  
Golden tests act as checkpoints to prevent drift.  
Snapshot tests allowed for textual outputs with stable normalization.

See: [[DDD]], [[DEBUGGERS]].

---

## 9. Guardrails & Heuristics

- Default import allowlist; justify exceptions in SPEC/PLAN.  
- Prefer single-file spikes; constrain abstractions.  
- One-File Spike (≤120 lines when feasible).  
- Two-Function Rule: parse(input)→state; apply(state,input)→state|output.  
- No new nouns unless two removed.  
- Handle top failure modes with structured errors.  
- Record cost/latency/privacy notes in LEARNINGS.

---

## 10. Roles

- **Agent** — drives forward: generates docs, toys, integrations, and attempts simplification/refactoring on its own.  
- **Human** — acts as a spotter: observes, nudges when the agent stalls or drifts, and intervenes on judgment calls the agent can’t yet resolve.

---

## 11. Templates

KICKOFF.md — weave skeleton.  
PLAN.md — step template with tests-first + success criteria.  
LEARNINGS.md — Built/Worked/Failed/Uncertain, evidence, pivots, impact.  
README.md — purpose, API sketch, quick test.

See: [[KICKOFF_WRITING]], [[PLAN_WRITING]], [[LEARNINGS_WRITING]], [[README_WRITING]].

---

**Clarity is the product.** Everything else is scaffolding.

*** End of V5 ***