# DocDD Loop & Kickoff

---

## 1. Purpose

Doc-Driven Development (DocDD) turns ambiguous problems into deterministic, legible systems through lightweight docs, disposable toy models, and incremental integrations.  

See: [Doc-Driven Development (DDD)](../foundations/ddd-principles.md).

---

## 2. Core Principles

- **Docs as control surfaces** — SPEC, PLAN, LEARNINGS, README.  
- **Toys, not monuments** — throwaway code, durable insights.  
- **Parsimony** — the simplest mechanism that works today.  
- **Determinism** — same input → same output; minimize hidden state.  
- **Legibility** — JSON + simple CLIs; human + agent inspectable.  
- **Two-at-a-time integration** — never combine more than two at once.

---

## 3. The DocDD Loop

1. SPEC — define minimal contract (inputs, outputs, invariants). 
2. PLAN — outline the smallest testable step.  
3. Implementation — write only enough to satisfy the contract.  
4. LEARNINGS — capture outcomes and constraints.
5. README - publish tool/API docs for future use.

See:  [Spec Writing](../authoring/spec-writing.md), [Plan Writing](../authoring/plan-writing.md), [Learnings Writing](../authoring/learnings-writing.md), [README Writing](../authoring/readme-writing.md)

---

## 4. Napkin Physics

Quick pre-spec simplification:  
- Problem (1 sentence)  
- Assumptions (a few bullets)  
- Invariant (one crisp property)  
- Mechanism (≤5 bullets)

Rule: no frameworks, no new nouns unless two are deleted.  

See: [Doc-Driven Development (DDD)](../foundations/ddd-principles.md).

---

## 5. Kickoff: The Binary-Weave

The kickoff is a sequential weave:  

- Introduce exactly one primitive (Toy A, Toy B …).  
- Integrate it with the current product (A+B=C, C+D=E …).  
- Each integration yields the new current product.  
- Continue until the final product emerges.  

End state: name the final product, summarize woven primitives, state durable invariants, discard toys, keep docs and learnings.  

Goal: compounding clarity

Anti-Goal: combinatorial drift

See: [Kickoff Writing](../guides/writing/kickoff.md).

---

## 6. Toy Models

Small, sharply scoped, fully specced implementations designed to be discarded.  

Cycle: SPEC → PLAN → Tests → Minimal code → LEARNINGS.  

Axis discipline: a base toy isolates one axis; an integration toy merges exactly two.  

See: [Toy Model Development](../guides/toy-dev.md).

---

## 7. CLI + JSON Convention

Modules behave like debuggers:  

- stdin: JSON input  
- stdout: JSON output  
- stderr: structured error JSON  
- Purity: same input → same output  

Error JSON shape:  
    { "type": "ERR_CODE", "message": "text", "hint": "fix" }

Schema-first: document I/O schemas in SPEC.  

See: [CLI + JSON as Debugger](../foundations/debugger-mindset.md).

---

## 8. Pipelines & Golden Tests

Compose CLIs as UNIX-style pipelines with inspectable intermediates, but only when this makes sense. It's not a good fit for every project.

See: [Doc-Driven Development (DDD)](../foundations/ddd-principles.md), [CLI + JSON as Debugger](../foundations/debugger-mindset.md).

---

## 9. Guardrails & Heuristics

Habits to constrain complexity:  
- Default import allowlist; justify exceptions.  
- Prefer single-file spikes.  
- Two-Function Rule: parse(input)→state; apply(state,input)→state|output.  
- No new nouns unless two removed.  
- Handle top errors with structured JSON.  
- Record cost, latency, privacy notes in LEARNINGS.

---

## 10. Roles

- **Agent** — generates docs, toys, integrations; pushes forward.  
- **Human** — spotter: nudges when the agent stalls or drifts, and makes judgment calls the agent cannot.

---

## Kickoff Writing Guide — Binary-Weave Kickoff Docs

This document instructs the agent how to write a kickoff document for a new DocDD project.  
The goal is to produce a single, explicit binary-weave plan — not a flat list of toys, not parallel streams.  
The weave always alternates: *new primitive → integration with prior product*.  

---

## Core Shape of a Kickoff

1. **Napkin Physics**:  
   - Problem (1 sentence)  
   - Assumptions (3–5 bullets)  
   - Invariant (one crisp property that must always hold)  
   - Mechanism (≤5 bullets describing the minimal path)  

2. **Binary-Weave Plan**:  
   - Always introduce **one new primitive at a time** (Toy A, Toy B, Toy C …).  
   - Always follow by **integrating it with the prior product** (A+B=C, C+D=E, …).  
   - Each integration produces the **new “current product”**.  
   - No step introduces more than one new primitive.  
   - No integration combines more than two things.  
   - Continue until the final product emerges.  

3. **End State**:  
   - Name the final product.  
   - Summarize which primitives and integrations were woven.  
   - State the durable invariants.  
   - Clarify that only the final docs + system remain; toys are discarded but learnings are kept.  

---

## Formatting Expectations

- **Stage numbering is sequential.**  
  - *Stage 1*: Primitive A, Primitive B  
  - *Stage 2*: A + B = C  
  - *Stage 3*: Primitive D  
  - *Stage 4*: C + D = E  
  - *Stage 5*: Primitive F  
  - *Stage 6*: E + F = G  
  - …continue until final product.  

- **Each stage entry must have**:  
  - **Name** (Toy or Integration)  
  - **What it does** (one sentence)  
  - **Invariant** (instantaneous, non-blocking, etc.)  

- **Avoid parallel numbering.** Don’t list “Stage 2.3” or “Stage 2.4”.  
- **Avoid over-specification.** The kickoff is a weave map, not a spec.  
- **Avoid skipping.** Each stage should follow the weave pattern strictly.  

---

## Tone & Style

- Write plainly and compactly — scaffolding, not prose.  
- Prioritize clarity of the weave over detail of implementation.  
- Keep invariants crisp and behavioral, not vague.  
- Use ≤2 bullets per primitive/integration when possible.  

---

## One-Shot Checklist

- [ ] Napkin Physics included?  
- [ ] Sequential stages?  
- [ ] Exactly one new primitive per stage?  
- [ ] Integration always combines current product with one new primitive?  
- [ ] Final product and invariants stated at end?  

If all are checked, the kickoff is valid.  

---
