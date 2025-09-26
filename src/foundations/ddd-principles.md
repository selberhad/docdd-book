# Doc‑Driven Development — Principles

## The Economic Shift

AI assistants have fundamentally altered the economics of software creation. Activities that once consumed significant human effort — writing code, updating documentation, refactoring existing implementations — can now be automated or substantially accelerated. This economic inversion transforms the traditional development calculus across multiple dimensions:

**Code Generation**: Scaffolding, boilerplate, tests, and even complex implementations can be generated in minutes rather than hours.

**Documentation Maintenance**: Updating specs, refreshing README files, and maintaining API documentation become automated workflow steps rather than manual overhead.

**Refactoring Operations**: Restructuring code that already works — traditionally a hard-to-justify business expense due to the effort-to-benefit ratio — becomes routine maintenance within the development cycle.

The result is a shifted value equation: individual artifacts (code, docs, tests) become disposable and cheap to regenerate, while clarity, architectural insight, and strategic decision-making become the primary sources of durable value.

Document-Driven Development emerges from this shifted landscape. Rather than starting with implementation and documenting afterward, the methodology reverses the flow: **Docs → Tests → Implementation → Learnings**. The AI generates all artifacts, while the human acts as reviewer, simplifier, and strategic guide.

## Core Principles

**AI as Generator, Human as Editor**: The AI produces comprehensive artifacts (documentation, specifications, plans, tests, implementations) while the human focuses on simplification, risk identification, and constraint setting. This division leverages each party's strengths — AI's generative capacity and human's editorial judgment.

**Disposable Code, Durable Insight**: Individual implementations are treated as expendable drafts. The lasting value lies in the clarity extracted through the development process and captured in meta-documentation. This removes psychological barriers to refactoring and experimentation.

**Parsimony Over Extensibility**: Prefer the simplest mechanism that solves today's problem rather than abstract frameworks designed for hypothetical future needs. This principle counters AI systems' tendency toward comprehensive, layered solutions.

**System Legibility**: Design for transparent, inspectable execution. Favor JSON data interchange, CLI interfaces, and deterministic behavior over hidden state and complex frameworks. This enables both humans and AI to reason about system behavior reliably.

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
