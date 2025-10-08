# Documentation Overview

Executive summary of how the documentation set fits together, the core concepts at work, and how to navigate from ideas to validated, working slices in an AI-enabled system.

## Big Picture

- Philosophy: Dialectic-Driven Development (DDD) + Toy Models.  
  Write the contract and plan first, validate with tests and minimal code, extract learnings, and iterate.
- Validation: CLI + JSON as debugger + tests.  
  Treat tools as pure CLIs with JSON I/O so agents can single-step, bisect, and replay deterministically.

## How the Docs Relate

- Process and Method
  - DDD.md: The operating protocol—docs → tests → implementation → learnings—with guardrails (complexity, dependencies, security) and self-audit.
  - TOY_DEV.md: Why we use toy models, how to keep them small, disciplined, and discardable.
  - PLAN_WRITING.md: How to write stepwise, test-first plans with objective success criteria.
  - LEARNINGS_WRITING.md: How to capture validated insights, failures, and open questions concisely.
  - README_WRITING.md: How to write library-level READMEs optimized for AI assistants.
- Diagnostics and Verification
  - DEBUGGERS.md: CLI + JSON as debugger mode for LLM agents—contract, pipelines as traces, and golden tests as breakpoints.
- Index
  - DOC_MAP.md: One-page map with links and short summaries of each document.

## Core Concepts

- Dialectic-Driven Development (DDD): Specifications and plans lead; code is the minimum to satisfy tests. Meta-docs remain the source of truth.
- Toy Models: Focused, low-cost experiments to validate invariants, data shapes, and APIs before integration. The code is disposable; the learnings are durable.
- CLI + JSON as Debugger: Prefer pure, stateless interfaces with JSON I/O, enabling deterministic pipelines, bisection, and agent legibility.
- Guardrails: Constraints on complexity and dependencies; explicit error handling; security hygiene; and self-audits to keep small and reviewable.

## Typical Flow

1) Draft SPEC and PLAN for the smallest viable slice (DDD.md, PLAN_WRITING.md).  
2) Derive tests and a minimal implementation.  
3) Validate using CLI+JSON pipelines, logs, and golden tests.  
4) Capture LEARNINGS, adjust constraints, and iterate or integrate.  
5) Keep READMEs and DOC_MAP current for fast orientation.

## What Matters

- Clarity over code volume; constraints over features.  
- Small, testable slices with explicit contracts.  
- Tools and docs that let both humans and agents understand, act, and debug effectively.
