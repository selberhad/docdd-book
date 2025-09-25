# Doc‑Driven Development — Principles

## Purpose
  This document defines how an AI assistant should operate inside this repository.
  It codifies the Doc Driven Development (DDD) paradigm, toy-model practice, and
  the CLI+JSON debugging substrate. Treat this as the canonical protocol.

## Operating Principles

  - AI generates everything: docs, specs, plans, tests, implementations, scaffolding.
  - Humans review, request revisions, and merge; AI loops until approval.
  - Drafts are disposable; clarity and constraints are durable.
  - Prefer parsimony: simplest mechanism that works today beats abstract extensibility.
  - Make state legible to humans and agents: JSON over hidden state, CLIs over frameworks.

## Roles

  - Agent: Produce artifacts, self-audit, run tests, propose diffs, respect guardrails.
  - Human Reviewer: Simplify, spot risks, approve/deny PRs, set constraints and budgets.

## Core Artifacts: The Meta-Document Harness

The four core artifacts form a harness system that guides AI agents while preserving human control:

- **SPEC.md** — *The bit: precise contract keeping the pull straight*
  - **Purpose:** Comprehensive behavioral contract for the current scope
  - **Must contain:** Input/output formats, invariants, internal state shapes, operations, validation rules, error semantics, test scenarios, success criteria

- **PLAN.md** — *The yoke: aligns effort into test-first steps*
  - **Purpose:** Strategic roadmap using Docs → Tests → Implementation cadence
  - **Must contain:** What to test vs. skip, order of steps, timeboxing, dependencies, risks, explicit success checkboxes per step

- **README.md** — *The map: concise orientation for integration*
  - **Purpose:** 100–200 words context refresh for AI on library functionality
  - **Must contain:** Header + one-liner, 2–3 sentence purpose, 3–5 essential method signatures, core concepts, gotchas/caveats, representative test path

- **LEARNINGS.md** — *The tracks: record of constraints and lessons*
  - **Purpose:** Retrospective capturing architectural insights, pivots, fragile seams, production readiness, reusable patterns
  - **Must contain:** What held, what failed, why, and next constraints discovered

Together these artifacts let the human act as driver, ensuring the cart (implementation) moves forward under control, with clarity preserved and ambiguity eliminated.  

## High-Level Workflow (DDD)

  1) Docs
       Generate or update SPEC.md and PLAN.md for the current, minimal slice of scope.
       Keep README.md for any touched library crisp and current.

  2) Tests
       Derive executable tests (or rubrics) directly from SPEC.md.
       Golden examples and negative/error-path cases are required.

  3) Implementation
       Provide the minimal code to pass tests; keep changes tightly scoped.
       Prefer single-file spikes for first proofs.

  4) Learnings
       Update LEARNINGS.md with what held, what failed, why, and next constraints.

## Napkin Physics (Overview)
  Upstream simplification to avoid scope drift before writing specs and plans.

  - Idea: capture problem, assumptions, invariant, minimal mechanism, and first try.
  - Why: enforces parsimony; prevents new layers/nouns without deletion elsewhere.

  See: [1.1 Napkin Physics](./napkin-physics.md)

## Toy Models (Overview)
  Toy models are small, discardable experiments to extract architectural insight.

  - Idea: SPEC → PLAN → Tests → Minimal Impl → LEARNINGS cycle under TDD and minimal deps.
  - Why: validate invariants, data shapes, and APIs early; reduce risk and rework.
  - Integration: build via two‑at‑a‑time merges; keep scope small and focused.

  See: [1.2 Toy‑Model Rationale](./toy-model-rationale.md)

## CLI + JSON as Debugger (Overview)
  The debugger mindset makes execution legible and falsifiable for both humans and agents.

  - Idea: expose pure CLIs with JSON I/O and structured errors; favor deterministic pipelines.
  - Why: enables single‑step reasoning, bisecting, and stable golden tests.
  - Outcome: predictable behavior and inspectable state across the system.

  See: [1.3 Debugger Mindset](./debugger-mindset.md)

## Repo Layout, Guardrails, Workflow (Overview)
  How we structure repos and constrain work to stay simple and safe.

  - Layout: clear locations for docs, CLIs, tests, and schemas.
  - Guardrails: dependency, complexity, and error-handling constraints.
  - Workflow: self-audit metrics and human review gates.

  See: [1.4 Repo Layout, Guardrails, Workflow](./ddd-repo-guardrails.md)
