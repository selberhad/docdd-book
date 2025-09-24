# Contents

Quick links to key chapters in this book.

- [Introduction](./introduction.md): Overview of the documentation set, core concepts, and the typical Docs → Tests → Impl flow.

## Current Structure
- Core Guides: DDD, Debuggers (CLI+JSON), Toy Model Development.
- Playbook: DocDD loop, Napkin Physics, kickoff pattern, heuristics.
- Writing Guides: Spec, Plan, Learnings, README, Kickoff.
- Appendices: Plan example/template.
- Observations: duplication across DDD and Playbook (DocDD loop, heuristics); Kickoff overlaps Playbook; some guides focus on “how” with limited “why/rationale”.

## Planned Structure
- Part I — Foundations (Why): DDD principles, Debugger mindset, Toy‑model rationale, Napkin Physics.
- Part II — Practice (How): Condensed Playbook (loop + kickoff), checklists, minimal workflow.
- Part III — Authoring Guides: Spec, Plan, README, Learnings (with cross‑links and examples).
- Part IV — Patterns & Appendices: Toy patterns, examples, and a small, well‑labeled archive.
- Refactors: merge overlapping content (Kickoff ↔ Playbook), move heuristics to Foundations, add short “Why this matters” sections in guides, and de‑duplicate repeated loops.

## Core Guides
- [Doc‑Driven Development (DDD)](./guides/ddd.md): Operating protocol, roles, artifacts, guardrails, and workflow for AI‑first, doc‑led work.
- [CLI + JSON as Debugger](./guides/debuggers.md): Contract for pure, deterministic CLIs with JSON I/O; pipelines and golden tests.
- [Toy Model Development](./guides/toy-dev.md): Why/How to run throwaway experiments to learn fast; SPEC → PLAN → Tests → Impl → LEARNINGS.

## Playbook
- [Playbook](./playbooks/playbook.md): Practical guide to the DocDD loop, Napkin Physics, binary‑weave kickoff, and complexity heuristics.

## Writing Guides
- [Spec Writing Guide](./specs/spec-writing.md): Structure and examples for precise, testable specs; data, operations, validation, and scenarios.
- [Plan Writing](./guides/writing/plan.md): Step template, TDD discipline, and success criteria for actionable plans.
- [Learnings Writing](./guides/writing/learnings.md): Summaries, evidence, pivots, and impact to capture reusable insights.
- [README Writing](./guides/writing/overview.md): Required sections and tone for AI‑legible library READMEs.
- [Kickoff Writing](./guides/writing/kickoff.md): How to outline binary‑weave kickoffs and integration sequencing.

## Appendices
- [Plan (Example/Template)](./appendices/plan.md): Example plan content and structure; use as a reference, not a mandate.
