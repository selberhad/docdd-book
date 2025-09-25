# Plan Writing

Purpose
- A PLAN.md is a strategic roadmap: what to build and how to build it step‑by‑step, enforcing clarity, sequencing, and validation.

What it is / is not
- Not: implementation code, literal test code, copy‑paste ready, exhaustive details.
- Is: stepwise development roadmap, TDD guide, illustrative patterns only, success criteria with checkboxes.

Structure
- Header: overview (goal, scope, priorities) and methodology (TDD; what to test vs not test).
- Step template:
```
## Step N: <Feature Name> **<PRIORITY>**
### Goal
Why this step matters
### Step N.a: Write Tests
- Strategy (no literal code); core, error, integration cases; expected validation
### Step N.b: Implement
- Tasks, code patterns (illustrative), state and error handling
### Success Criteria
- [ ] Clear, testable checkpoints
```

Key practices
- TDD discipline: write failing tests first; Red → Green → Next; focus on interfaces and contracts; cover error paths explicitly.
- Test scope: test core features, errors, and integrations; skip helpers, edge/perf, internals.
- Code patterns: examples as patterns, not literal code; keep tasks minimal and explicit.

Success criteria
- Concrete, objective boxes for functional and quality outcomes.

Anti‑patterns
- Full test code in PLAN; full implementation code; excessive detail that replaces thinking.

 
