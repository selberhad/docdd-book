# Documentation Map

- [[DDD]]: Doc-Driven, AI-First Development Protocol. Defines roles, core meta-docs (README/SPEC/PLAN/LEARNINGS), the Docs→Tests→Impl workflow, Napkin Physics, toy-model discipline, CLI+JSON debugging contract, repo layout expectations, guardrails (deps/complexity/errors/security), testing strategy, self-audit metrics, review gates, operative modes, success criteria, simplification heuristics, glossary, and guiding end notes.

- [[DEBUGGERS]]: CLI + JSON as Debugger for LLM agents. Defines the contract (stdin/out JSON, structured error JSON, purity/determinism), pipelines as execution traces, and golden tests as breakpoints enabling single-step, bisect, and replay.

- [[LEARNINGS_WRITING]]: How to write LEARNINGS.md. Defines purpose, what it is/is not, essential sections (header, summary, evidence, pivots, impact), and style guidance focused on short, factual, reusable insights capturing successes, failures, and unknowns.

- [[PLAN_WRITING]]: How to write a PLAN.md. Presents purpose, structure, a step template (tests-first then implementation), TDD discipline, what to test vs skip, code-pattern guidance, task breakdown, success criteria checkboxes, anti-patterns, and rationale for why plans improve sequencing and quality.

- [[README_WRITING]]: README guidelines for internal libraries aimed at AI assistants. Specifies required sections (header, purpose, key API, core concepts, gotchas, quick test), writing principles (concise, specific, practical), a template, and a quality checklist for fast comprehension and validation.

- [[TOY_DEV]]: Toy Model Development Manifesto. Clarifies the goal of toy models as discardable experiments to extract architectural insight. Describes the cycle (SPEC → PLAN → Impl → LEARNINGS), guiding principles (TDD, actionable errors, event sourcing, minimal deps, multi-format export), proven patterns, testing philosophy, strategic guidance, and the “gardening not construction” ethos.
