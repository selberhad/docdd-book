# Doc‑Driven Development — Principles

Doc‑Driven Development (DDD) puts explanation before execution. We write down the contract and plan, test those claims, and ship only the minimum code required. Clarity and constraints are durable; code is disposable.

Why this matters
- Reduces rework: decisions are explicit, testable, and easy to review.
- Scales collaboration: shared artifacts (SPEC, PLAN, LEARNINGS, README) align contributors.
- Increases legibility: systems behave predictably and are easier to debug and evolve.

Core principles
- Clarity over code: express intent and constraints first; code follows tests.
- Parsimony: prefer the simplest mechanism that works today.
- Determinism: same input → same output; minimize hidden state and ambiguity.
- Legibility: prefer JSON, small CLIs, and observable state.

Roles
- Human reviewer: simplifies scope, sets constraints/budgets, and approves changes.
- Agent/implementer: proposes artifacts, self‑audits, runs tests, iterates until approval.

Canonical artifacts (what they must achieve)
- SPEC: precise behavioral contract (I/O, invariants, operations, validation, errors).
- PLAN: stepwise, test‑first sequence with explicit success criteria and risks.
- LEARNINGS: concise evidence, pivots, and constraints that feed the next slice.
- README: orientation document for consumers (purpose, key APIs, gotchas, quick test).

Guardrails and heuristics
- One‑File Spike: prove a loop in ≤120 lines when feasible.
- Two‑Function Rule: parse(input)→state; apply(state,input)→state|output.
- No New Nouns: don’t add new abstractions unless you delete two.
- Minimal deps: whitelist exceptions; justify them in SPEC/PLAN.
- Error hygiene: structured, actionable errors; no secrets in logs.
- Cost/latency awareness: track representative p95 and token/$ in LEARNINGS where relevant.

When to split or stop
- If a SPEC/PLAN drifts or bloats, split scope into smaller toys and re‑focus.
- Stop implementation once success criteria pass; capture learnings and cut the next slice.

Where the loop lives
- The mechanics of the Docs → Tests → Impl cadence are covered once in Practice → DocDD Loop & Kickoff.
- This chapter anchors the “why” and the guardrails; avoid repeating process details here.

Cross‑references
- Practice: [DocDD Loop & Kickoff](../../v2/practice/loop-and-kickoff.md)
- Foundations: [Debugger Mindset](../../v2/foundations/debugger-mindset.md), [Toy‑Model Rationale](../../v2/foundations/toy-model-rationale.md), [Napkin Physics](../../v2/foundations/napkin-physics.md)
