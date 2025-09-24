# Playbook: Doc‑Driven Development, Toy Models, and CLI+JSON Debugging

Informal, practical guidance for producing clarity-first software with AI assistance. This playbook consolidates the generalized documents into one comprehensive reference without introducing new concepts beyond the existing docs.

---

## 1. Preface: Purpose, Audience, How to Use This

- Purpose: Capture a working method where documents drive development; tests and minimal code validate behavior; and execution remains legible to both humans and agents via CLI + JSON.
- Audience: Practitioners building AI-enabled systems who value determinism, parsimony, and repeatable workflows.
- How to use: Skim Core Principles, then the Doc‑Driven loop. Use Toy Models and Napkin Physics for scope. Adopt the CLI + JSON debugger mode and minimal pipelines. Lean on templates and checklists as you iterate.

Why this matters:
- Clarity first: turning ambiguity into explicit contracts and plans reduces rework.
- Determinism and legibility let agents and humans reason, bisect, and replay reliably.
- Small, well‑scoped slices accelerate learning and keep risk contained.

---

## 2. Core Principles: Clarity, Determinism, Parsimony, Legibility

Operating principles (from the DDD protocol):
- AI generates everything: docs, specs, plans, tests, implementations, scaffolding.
- Humans review, request revisions, and merge; AI loops until approval.
- Drafts are disposable; clarity and constraints are durable.
- Prefer parsimony: simplest mechanism that works today beats abstract extensibility.
- Make state legible to humans and agents: JSON over hidden state, CLIs over frameworks.

Additional guardrails and orientation:
- Keep changes tightly scoped; prefer single-file spikes when feasible.
- Use structured errors and explicit contracts; document schemas and versions.
- Validate with golden examples and error-path tests.

Why this matters:
- Parsimony prevents premature abstraction; you ship learning sooner.
- Deterministic, JSON‑visible state makes systems AI‑debuggable.
- Structured errors and schemas create stable interfaces and faster feedback loops.

---

## 3. Doc‑Driven Development: Loop and Roles

High-level workflow (DDD):
1) Docs: Generate or update SPEC.md and PLAN.md for the current, minimal slice of scope. Keep library READMEs crisp and current.
2) Tests: Derive executable tests (or rubrics) directly from SPEC.md. Include golden examples and negative/error-path cases.
3) Implementation: Provide the minimal code to pass tests; keep changes tightly scoped; prefer single-file spikes for first proofs.
4) Learnings: Update LEARNINGS.md with what held, what failed, why, and next constraints.

Roles:
- Agent: Produce artifacts, self-audit, run tests, propose diffs, respect guardrails.
- Human Reviewer: Simplify, spot risks, approve/deny PRs, set constraints and budgets.

Driving metaphor (mapping docs to control surfaces):
- SPEC.md = the bit: precise input/output contract.
- PLAN.md = the yoke: aligns effort into test-first steps.
- LEARNINGS.md = the tracks: record constraints and lessons.
- README.md = the map: concise orientation during integration.

Why this matters:
- Docs → Tests → Impl enforces a single source of truth and reduces drift.
- Golden examples and error paths prove behavior before broad investment.
- Clear roles and artifacts make review faster and changes safer.

---

## 4. The Meta‑Docs: Intent and Minimal Content

Core artifacts (meta-document layer):
- README.md (per library)
  - Purpose: 100–200 words context refresh for AI; what it does, key API, gotchas.
  - Must contain: header + one-liner; 2–3 sentence purpose; 3–5 essential method signatures; core concepts; gotchas/caveats; representative quick test path.
- SPEC.md
  - Purpose: Comprehensive behavioral contract for the current scope.
  - Must contain: input/output formats; invariants; internal state shapes; operations; validation rules; error semantics; test scenarios; success criteria.
- PLAN.md
  - Purpose: Strategic roadmap using Docs → Tests → Impl cadence.
  - Must contain: what to test vs. skip; order of steps; timeboxing; dependencies; risks; explicit success checkboxes per step.
- LEARNINGS.md
  - Purpose: Retrospective capturing architectural insights, pivots, fragile seams, production readiness, and reusable patterns.

Why this matters:
- README orientates quickly so assistants act correctly without spelunking.
- SPEC removes ambiguity; contracts enable reproducible tests and pipelines.
- PLAN sequences effort, limits scope creep, and defines objective completion.
- LEARNINGS preserves durable insight even when code is discarded.

---

## 5. Napkin Physics: Upstream Simplification

Use this mode before drafting SPEC/PLAN to encourage parsimony.

Output structure:
- Problem: one sentence.
- Assumptions: 3–5 bullets.
- Invariant/Contract: one precise relation or property.
- Mechanism: ≤5 bullets describing a single-file spike (stdlib or minimal deps).
- First Try: one paragraph describing the simplest path.

Prohibitions:
- No frameworks, no new layers, no new nouns unless two are deleted elsewhere.

Why this matters:
- Forces a minimal mechanism and a crisp invariant before any code.
- Prevents new nouns and layers that slow learning without adding proof.

---

## 6. Toy Models: Cycle, Exit Criteria, Integration

Definition: Small, sharply scoped, fully specced implementations designed to be thrown away.

Purpose: Validate data structures, invariants, APIs, and error behavior with minimal code.

Cycle: SPEC.md (contract) → PLAN.md (recipe) → Tests → Minimal Impl → LEARNINGS.md (extraction).

Principles:
- Tests-first; minimal dependencies; structured errors; event sourcing when useful.

Exit criteria:
- All step-level success criteria checked; insights recorded; follow-up scope cut.

Toy integration convention:
- Each toyN_* directory contains exactly one SPEC.md, PLAN.md, LEARNINGS.md.
- Split unfocused scope into new toyN_* experiments.
- Integration toys recombine validated sub-toys.
- Replace in place: update LEARNINGS.md rather than creating multiples.
- Bias toward minimal scope.

Axis principle for toy models:
- A base toy isolates exactly one axis (invariant, mechanism, or seam).
- An integration toy merges exactly two axes to probe interaction.
- Never exceed two axes per toy.

Why this matters:
- Toy models de‑risk by validating one thing at a time.
- Axis limits keep experiments sharp; integration toys recombine only what’s proven.
- Insights outlive code; you can discard spikes without losing value.

---

## 7. CLI + JSON Debugger Mode: Contract

Goal: Enable the agent to single-step systems deterministically, inspect state, and bisect.

Contract (per module):
- stdin: JSON input
- stdout: JSON output
- stderr: machine-parsable error JSON when failing

Purity and determinism:
- Same input → same output (no hidden state)
- Logs are allowed; outputs must remain pure

Error shape:
```
{ "type": "ERR_CODE", "message": "human text", "hint": "actionable fix" }
```

Schema-first:
- Document input/output JSON schemas and versions in SPEC.md.

Quick test:
- Each CLI ships with a one-command golden test path.

Why this matters:
- Deterministic, pure CLIs give agents “debugger legs” to single‑step and bisect.
- Machine‑parsable errors and documented schemas make failures actionable.

---

## 8. Pipelines & Golden Tests: Execution Traces, Breakpoints, Replay

Minimal pipeline pattern (UNIX-style composition):
```
modA < in.json > a.json
modB < a.json > b.json
modC --flag X < b.json > out.json
```

Pipelines as execution traces:
- Chain modules to produce inspectable intermediate artifacts.
- Walk the pipeline step by step; verify each artifact against SPEC.

Golden tests as breakpoints:
- Provide a one-liner golden path to verify baseline behavior before changes.
- Use as deterministic checkpoints to anchor reasoning and prevent drift.

Snapshot tests:
- Permissible for textual outputs with stable normalization rules.

Replay and bisect (operational use):
- Use pipeline stages to isolate failures and compare against golden artifacts.

Why this matters:
- Pipelines turn execution into inspectable traces—breakpoints with artifacts.
- Golden paths anchor behavior, preventing drift as changes land.
- Replay and bisection compress debugging time and reduce guesswork.

---

## 9. Planning & Testing: Stepwise Plans and Test Scope

Planning (PLAN.md guidance):
- Step template (tests first, then implementation) with success criteria checkboxes.
- Prioritize minimal units: files/modules, core operations, integration points, and error handling.
- Explicitly state what to test vs. skip; outline risks and dependencies.

Testing strategy (DDD):
- Unit tests per function or CLI; golden I/O tests for pipelines.
- Error-path tests for documented failure modes.
- Contract tests: ensure JSON conforms to schema versions; invariants hold.
- Snapshot tests permissible with stable normalization rules.

Why this matters:
- Stepwise planning keeps effort focused and test‑first.
- Contract/schema tests lock interfaces; error‑path tests catch the top failures.
- Snapshot norms avoid flaky approvals and keep outputs stable.

---

## 10. Guardrails & Self‑Audit: Constraints, Security, Reviews

Dependencies:
- Default allowlist: stdlib or equivalent; approved lightweight libs must be enumerated.
- Any new import must be justified in SPEC.md and whitelisted in PLAN.md for this slice.

Complexity constraints:
- Initial spikes: single file ≤ 120 lines when feasible.
- Average function length ≤ 25 lines; cyclomatic complexity ≤ 10 per function.
- No more than two new named abstractions per slice (class/module/pattern).

Error handling:
- Implement top 2 failure modes; others raise clear string or structured error JSON.
- No secret leakage (keys, prompts) in errors or logs.

Costs and latency:
- Track approximate token/$ and p95 latency for representative tests in LEARNINGS.md.

Security and privacy:
- No PII in fixtures; redact or synthesize test data.

Self‑audit (pre‑PR):
- Print and evaluate: file_count_changed; total_added_lines; imports_added_outside_allowlist; new_named_abstractions; max_function_cyclomatic_complexity; average_function_length; test_count_added vs prod_functions_touched. If warned, rerun Napkin Physics and regenerate minimal spike.

Human review gates (what to present):
- One‑paragraph summary of problem and mechanism (from Napkin output).
- SPEC and PLAN diffs with checkboxes aligned to success criteria.
- Test results: pass/fail matrix; coverage or representative list.
- If CLI work: pipeline diagram and sample fixture diffs (a.json → b.json).
- Proposed next step: smallest next increment with rationale.

Decision outcomes (reviewer):
- approve, revise_docs, revise_tests, revise_impl, abort (with why and constraints learned).

Why this matters:
- Dependency and complexity caps prevent silent growth in risk and cost.
- Self‑audit metrics reveal when to simplify before proceeding.
- Review gates ensure changes remain small, testable, and well‑justified.

---

## 11. Heuristics & Anti‑Patterns

Simplification heuristics:
- One‑File Spike rule: prefer 1 file ≤ 120 lines to prove the loop.
- Two‑Function Rule: exactly two public entrypoints when feasible: parse(input)→state and apply(state,input)→state|output.
- No New Nouns: avoid new abstractions unless you delete two.
- 80/20 Errors: implement the two most likely failures; raise clearly for the rest.
- Time‑Boxed Satisficing: propose what you could build in 30 minutes today.

Plan anti‑patterns (from PLAN guidance):
- Full test code in Plan (use bullet outlines).
- Full implementation code (use patterns only).
- Over‑detail (Plan guides, does not replace dev thinking).

Why this matters:
- Heuristics bias toward proving mechanisms quickly.
- Avoiding new nouns and over‑detailed plans keeps momentum and clarity.

---

## 12. Adoption Guide: Retrofitting Modules and Layout

Retrofitting a module to CLI+JSON (from debugger and DDD sections):
- Expose a pure CLI: stdin JSON, stdout JSON, stderr structured error JSON.
- Ensure determinism: same input → same output; no hidden state in outputs.
- Document schemas and versions in SPEC.md.
- Add a one‑command golden test path.
- Compose into a minimal pipeline and capture intermediate artifacts.

Repository layout expectations (DDD):
- /libs/<name>/README.md — concise library refresh for agents
- /docs/SPEC.md — current contract for active slice
- /docs/PLAN.md — stepwise plan for active slice
- /docs/LEARNINGS.md — retrospective entries per slice
- /schemas/*.json — JSON Schemas (versioned)
- /cli/* — small stateless CLI entrypoints
- /tests/* — golden, unit, integration tests; fixtures/ as needed
- /fixtures/*.json — canonical input/output examples for CLIs and APIs

Why this matters:
- Retrofitting to CLI+JSON unlocks determinism, pipelines, and golden tests.
- A predictable layout helps assistants and humans locate contracts, tests, and fixtures fast.

---

## 13. Appendices: Templates, Checklists, Schemas, Glossary

### A. SPEC.md (intent and required content)
- Input/output formats; invariants; internal state shapes; operations; validation rules; error semantics; test scenarios; success criteria.

### B. PLAN.md (structure and step template)
- Header: Overview (goal, scope, priorities); Methodology (TDD; what to test vs. not test)
- Step Template:
  - Goal: why this step matters
  - Step N.a: Write Tests: outline strategy; core/error/integration cases; expected validation
  - Step N.b: Implement: tasks (files/modules, core ops, integration); illustrative patterns; state and error handling guidance
  - Success Criteria: clear, testable checkpoints; functional + quality standards met

Plan Key Practices:
- TDD discipline: Red → Green → Next; focus on interfaces and contracts; cover error paths explicitly.
- Test scope: test core features, errors, integration points; skip helpers, perf, internals where appropriate.
- Tasks: minimal units (create files; implement core parsing/ops; add integration path; error handling).
 
Plan Anti‑Patterns:
- No full test code; no full implementation code; avoid over‑detail.

### C. LEARNINGS.md (essential sections and style)
- Header: title, duration, status, estimate
- Summary: Built; Worked; Failed; Uncertain
- Evidence: Validated; Challenged; Failed; Uncertain
- Pivots: from → to, why, and remaining unknowns
- Impact: reusable patterns; architectural consequence; estimate calibration

Style:
- Short and factual; bullets over prose; explicit about failures and unknowns; one page max (dense, parsimonious, reusable).

Why this matters:
- Templates and checklists compress setup time and increase consistency.
- Shared shapes (error JSON, pipeline pattern) standardize how tools compose.

### D. README.md (library orientation)
- Header + one‑liner; Purpose (2–3 sentences)
- Key API: 3–5 most important methods with type hints
- Core Concepts: structures, constraints, integration points, patterns
- Gotchas & Caveats: limitations, common mistakes, performance constraints, integration pitfalls
- Quick Test: representative test command

## Core Concepts
- Key data structure or abstraction
- Critical constraint or assumption
- Integration point with other libraries
- Important design pattern

## Gotchas
- Known limitation or performance constraint
- Common usage mistake to avoid
- Integration pitfall with other libraries

### E. CLI + JSON details

Contract at a glance:
- stdin: JSON input
- stdout: JSON output
- stderr: structured error JSON
- process returns error code on failure
- Purity: same input → same output (no hidden state)
- Logs allowed (JSONL preferred); outputs must remain pure
- Schema‑first: document I/O JSON schemas and versions in SPEC.md
- Golden test: each CLI ships with a one‑command baseline

### F. Testing strategy (summary)
- Unit tests per function/CLI; golden I/O tests for pipelines; error-path tests; contract/schema validation; snapshot tests with stable normalization.

### G. Guardrails (summary)
- Dependencies: allowlist; justify new imports in SPEC and whitelist in PLAN.
- Complexity: single-file spikes when feasible; function length and cyclomatic limits; constrain new abstractions.
- Error handling: top two failure modes handled; structured errors; no secret leakage.
- Costs/Latency: track representative token/$ and p95 latency in LEARNINGS.
- Security/Privacy: no PII in fixtures.

### H. Glossary (selected)
- DDD: Doc Driven Development; High-Level Docs → Tests → Implementation → Learnings → User-Facing Docs.
- Toy Model: miniature, fully specced experiment intended to be discarded after extracting insight.
- Napkin Physics: upstream parsimony framing to derive minimal mechanisms.
- CLI+JSON Debugger: UNIX-style composition where each module is a pure CLI with JSON I/O.
- Golden Test: canonical input/output pair that must remain stable across changes.
- Invariant: property that must hold across operations (e.g., schema validity, conservation of count).

---

End notes:
- The mandate is not to produce maximal code, but to produce maximal clarity with minimal code. Drafts are fuel; constraints and insights are the product.
