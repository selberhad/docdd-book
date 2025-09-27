# Doc‑Driven Development — Principles

## The Problem with Current AI-Coding Approaches

Software development is experiencing a fundamental shift as AI agents become capable programming partners. The industry has responded with various methodologies: spec-driven development, AI-enhanced TDD, structured prompting frameworks, and workflow optimizations. While these approaches offer incremental improvements, they share a critical limitation — they are human programming practices remixed for AI, not ground-up designs for AI capabilities.

Most current AI-coding methodologies ask: "How can we modify existing development workflows to work better with AI?" But this misses the deeper question: "If we designed software development from scratch for AI agents, what would it look like?"

The difference is significant. Human-oriented practices evolved around human cognitive limitations: working memory constraints, context-switching costs, and the difficulty of maintaining mental models across large codebases. AI agents have entirely different constraints: they excel at rapid iteration and pattern generation but struggle with consistency across sessions, maintaining context over long conversations, and distinguishing between hallucination and valid solutions.

Traditional approaches try to fit AI into human-shaped processes. They focus on better prompts, more structured inputs, and clearer specifications — essentially teaching AI to work within frameworks designed for human cognition. This is like optimizing horse carriages instead of inventing the automobile.

Document-Driven Development takes the alternative approach: redesigning the entire development process around AI capabilities and limitations. Rather than asking how to make AI better at human workflows, it asks what programming methodology would emerge if we started from first principles with AI as the primary implementer.

## The Economic Shift

AI assistants have fundamentally altered the economics of software creation. Activities that once consumed significant human effort — writing code, updating documentation, refactoring existing implementations — can now be automated or substantially accelerated. This economic inversion transforms the traditional development calculus across multiple dimensions:

**Code Generation**: Scaffolding, boilerplate, tests, and even complex implementations can be generated in minutes rather than hours.

**Documentation Maintenance**: Updating specs, refreshing README files, and maintaining API documentation become automated workflow steps rather than manual overhead.

**Refactoring Operations**: Restructuring code that already works — traditionally a hard-to-justify business expense due to the effort-to-benefit ratio — becomes routine maintenance within the development cycle.

The result is a shifted value equation: individual artifacts become expendable, while clarity, architectural insight, and strategic decision-making become the primary sources of durable value.

Document-Driven Development emerges from this shifted landscape, reversing the traditional implementation-first flow.

## Core Principles

**AI as Generator, Human as Editor**: The AI produces comprehensive artifacts (documentation, specifications, plans, tests, implementations) while the human focuses on simplification, risk identification, and constraint setting. This division leverages each party's strengths — AI's generative capacity and human's editorial judgment.

**Disposable Artifacts, Durable Insight**: All implementations, documentation, and tests are treated as expendable drafts. The lasting value lies in the clarity extracted through the development process and captured in meta-documentation. This removes psychological barriers to refactoring and experimentation.

**Parsimony Over Extensibility**: Prefer the simplest mechanism that solves today's problem rather than abstract frameworks designed for hypothetical future needs. This principle counters AI systems' tendency toward comprehensive, layered solutions.

**System Legibility**: Design for transparent, inspectable execution that both humans and AI can reason about reliably.

## Core Artifacts: The Meta-Document Harness

The four core artifacts form a harness system that guides AI agents while preserving human control:

- **SPEC.md** — *The bit: precise contract keeping the pull straight*
  - **Purpose:** Comprehensive behavioral contract for the current scope
  - **Must contain:** Input/output formats, invariants, internal state shapes, operations, validation rules, error semantics, test scenarios, success criteria

- **PLAN.md** — *The yoke: aligns effort into test-first steps*
  - **Purpose:** Strategic roadmap using Docs → Tests → Implementation cadence
  - **Must contain:** What to test vs. skip, order of steps, timeboxing, dependencies, risks, explicit success checkboxes per step

- **README.md** — *The map: concise orientation for integration*
  - **Purpose:** 100–200 words context refresh on library functionality
  - **Must contain:** Header + one-liner, 2–3 sentence purpose, 3–5 essential method signatures, core concepts, gotchas/caveats, representative test path

- **LEARNINGS.md** — *The tracks: record of constraints and lessons*
  - **Purpose:** Retrospective capturing architectural insights, pivots, fragile seams, production readiness, reusable patterns
  - **Must contain:** What held, what failed, why, and next constraints discovered

Together these artifacts let the human act as driver, ensuring the cart (implementation) moves forward under control, with clarity preserved and ambiguity eliminated.  

## High-Level Workflow

The Document-Driven Development cycle follows four sequential phases:

**1. Documentation**
- Generate or update SPEC.md and PLAN.md for the current, minimal slice of scope
- Keep README.md for any touched library crisp and current

**2. Tests**
- Derive executable tests (or rubrics) directly from SPEC.md
- Golden examples and negative/error-path cases are required

**3. Implementation**
- Provide the minimal code to pass tests; keep changes tightly scoped
- Prefer single-file spikes for first proofs

**4. Learnings**
- Update LEARNINGS.md with what held, what failed, why, and next constraints

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
