# Documentation Overview

Executive summary of how the documentation set fits together, the core concepts at work, and how to navigate from ideas to validated, working slices in an AI-enabled system.

## Big Picture

- Philosophy: Doc-Driven Development (DDD) + Toy Models.  
  Write the contract and plan first, validate with tests and minimal code, extract learnings, and iterate.
- Validation: CLI + JSON as debugger + tests.  
  Treat tools as pure CLIs with JSON I/O so agents can single-step, bisect, and replay deterministically.

## How the Docs Relate

- Process and Method
  - [Doc‑Driven Development (DDD)](./guides/ddd.md): The operating protocol—docs → tests → implementation → learnings—with guardrails and self‑audit.
  - [Toy Model Development](./guides/toy-dev.md): Why we use toy models, and how to keep them small, disciplined, and discardable.
  - [Plan Writing](./guides/writing/plan.md): Stepwise, test‑first plans with objective success criteria.
  - [Learnings Writing](./guides/writing/learnings.md): Capture validated insights, failures, and open questions concisely.
  - [README Writing](./guides/writing/overview.md): Library‑level READMEs optimized for AI assistants.
- Diagnostics and Verification
  - [CLI + JSON as Debugger](./guides/debuggers.md): Contract, pipelines as traces, and golden tests as breakpoints.

## Core Concepts

- Doc-Driven Development (DDD): Specifications and plans lead; code is the minimum to satisfy tests. Meta-docs remain the source of truth.
- Toy Models: Focused, low-cost experiments to validate invariants, data shapes, and APIs before integration. The code is disposable; the learnings are durable.
- CLI + JSON as Debugger: Prefer pure, stateless interfaces with JSON I/O, enabling deterministic pipelines, bisection, and agent legibility.
- Guardrails: Constraints on complexity and dependencies; explicit error handling; security hygiene; and self-audits to keep work small and reviewable.

## Typical Flow

1) Draft SPEC and PLAN for the smallest viable slice ([DDD](./guides/ddd.md), [Plan Writing](./guides/writing/plan.md)).  
2) Derive tests and a minimal implementation.  
3) Validate using CLI+JSON pipelines, logs, and golden tests.  
4) Capture LEARNINGS, adjust constraints, and iterate or integrate.  
5) Keep pages current and cross‑linked for fast orientation.

## What Matters

- Clarity over code volume; constraints over features.  
- Small, testable slices with explicit contracts.  
- Tools and docs that let both humans and agents understand, act, and debug effectively.
