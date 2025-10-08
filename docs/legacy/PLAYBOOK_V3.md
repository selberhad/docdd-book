# PLAYBOOK.md — Dialectic-Driven Development (Core Doctrine)

A clarity-first, agent-oriented methodology for building complex systems out of simple, disposable experiments.  

---

## 1. Purpose

Dialectic-Driven Development (DDD) is a workflow designed for AI engineers and AI agents. Its goal is to turn ambiguous problem statements into deterministic, legible systems by cycling through lightweight docs, disposable toy models, and incremental integrations.  

---

## 2. Core Principles

- **Docs as control surfaces** — every step begins with a document (SPEC, PLAN, LEARNINGS, README).  
- **Toys, not monuments** — intermediate code is disposable; insight is the real output.  
- **Parsimony** — prove behavior with the simplest possible mechanism before adding complexity.  
- **Determinism** — same input, same output; minimize hidden state.  
- **Legibility** — make state inspectable to both humans and agents, often via JSON and simple CLIs.  
- **Two-at-a-time integration** — always combine exactly two validated parts (primitives or sub-assemblies) before moving on.  

---

## 3. The DDD Loop

1. **SPEC.md** — Define the minimal behavioral contract. Inputs, outputs, invariants, error cases.  
2. **PLAN.md** — Outline the smallest step to test the contract. No code, just sequence and risks.  
3. **Implementation** — Write the minimal code needed to pass the test.  
4. **LEARNINGS.md** — Record what worked, what failed, what constraints or invariants emerged.  

Repeat until the slice is validated or retired.  

---

## 4. Napkin Physics

Before writing a SPEC, sketch the problem in the smallest possible form:  

- Problem (one sentence)  
- Assumptions (3–5 bullets)  
- Invariant (a property that must always hold)  
- Mechanism (≤5 bullets describing the simplest spike)  

This prevents premature abstraction and anchors the design in clarity.  

---

## 5. Toy Models

Toys are minimal, fully specced experiments designed to be thrown away after their lesson is captured.  

- **Primitive toys** validate one axis (a data structure, invariant, or operation).  
- **Integration toys** validate one seam between two validated toys.  
- **Rule**: never combine more than two at a time. Build the system as a decision tree of 2-part integrations.  

Each toy directory contains SPEC.md, PLAN.md, LEARNINGS.md, and minimal code/tests.  

---

## 6. JSON + CLI Convention

Not every toy needs it, but where possible, expose experiments as small CLIs that read/write JSON.  

Why:  
- JSON is legible to agents and humans.  
- CLIs make toys composable (UNIX style).  
- Deterministic I/O makes them debuggable like stepping through a trace.  

This is a guiding principle, not a rule. Use when it increases clarity and legibility.  

---

## 7. Integration and Final System

The system emerges as toys are discarded and insights are carried forward.  

- Early toys: isolate primitives.  
- Mid toys: integrate pairs into stable sub-assemblies.  
- Final toys: integrate sub-assemblies until the full system exists.  

The only lasting artifacts are the **final implementation** and the **final docs**. Everything else is fuel.  

---

## 8. Roles

- **Agent** — drives forward: generates docs, toys, integrations, and attempts simplification and refactoring on its own.
- **Human** — acts as a spotter: observes, nudges when the agent gets stuck or drifts, and provides directional guidance — suggesting overlooked primitives or correcting faulty integrations so progress compounds rather than stalls.
---

## 9. Philosophy

- Code and docs are chickens and eggs, but both are disposable until the final generation.  
- The true product is clarity: contracts, constraints, invariants, and working integrations.  
- Everything else is scaffolding to get there.  
  