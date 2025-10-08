# PLAYBOOK_V6.md — Dialectic-Driven Development with Binary-Weave Kickoff

---

## 1. Purpose

Dialectic-Driven Development (DDD) turns ambiguous problems into deterministic, legible systems through lightweight docs, disposable toy models, and incremental integrations.  

See: [[DDD]].

---

## 2. Core Principles

- **Docs as control surfaces** — SPEC, PLAN, LEARNINGS, README.  
- **Toys, not monuments** — throwaway code, durable insights.  
- **Parsimony** — the simplest mechanism that works today.  
- **Determinism** — same input → same output; minimize hidden state.  
- **Legibility** — JSON + simple CLIs; human + agent inspectable.  
- **Two-at-a-time integration** — never combine more than two at once.

---

## 3. The DDD Loop

1. SPEC — define minimal contract (inputs, outputs, invariants). 
2. PLAN — outline the smallest testable step.  
3. Implementation — write only enough to satisfy the contract.  
4. LEARNINGS — capture outcomes and constraints.
5. README - publish tool/API docs for future use.

See:  [[SPEC_WRITING]], [[PLAN_WRITING]], [[LEARNINGS_WRITING]], [[README_WRITING]]

---

## 4. Napkin Physics

Quick pre-spec simplification:  
- Problem (1 sentence)  
- Assumptions (a few bullets)  
- Invariant (one crisp property)  
- Mechanism (≤5 bullets)

Rule: no frameworks, no new nouns unless two are deleted.  

See: [[DDD]].

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

See: [[KICKOFF_WRITING]].

---

## 6. Toy Models

Small, sharply scoped, fully specced implementations designed to be discarded.  

Cycle: SPEC → PLAN → Tests → Minimal code → LEARNINGS.  

Axis discipline: a base toy isolates one axis; an integration toy merges exactly two.  

See: [[TOY_DEV]].

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

See: [[DEBUGGERS]].

---

## 8. Pipelines & Golden Tests

Compose CLIs as UNIX-style pipelines with inspectable intermediates, but only when this makes sense. It's not a good fit for every project.

See: [[DDD]], [[DEBUGGERS]].

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
