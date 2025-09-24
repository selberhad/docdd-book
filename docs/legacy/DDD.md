Doc-Driven, AI-First Development Protocol (DDD)

Purpose
  This document defines how an AI assistant should operate inside this repository.
  It codifies the Doc Driven Development (DDD) paradigm, toy-model practice, and
  the CLI+JSON debugging substrate. Treat this as the canonical protocol.

Operating Principles
  - AI generates everything: docs, specs, plans, tests, implementations, scaffolding.
  - Humans review, request revisions, and merge; AI loops until approval.
  - Drafts are disposable; clarity and constraints are durable.
  - Prefer parsimony: simplest mechanism that works today beats abstract extensibility.
  - Make state legible to humans and agents: JSON over hidden state, CLIs over frameworks.

Roles
  - Agent: Produce artifacts, self-audit, run tests, propose diffs, respect guardrails.
  - Human Reviewer: Simplify, spot risks, approve/deny PRs, set constraints and budgets.

Core Artifacts (Meta-Document Layer)
  - README.md (per library)
      Purpose: 100–200 words context refresh for AI; what it does, key API, gotchas.
      Must contain: header + one-liner, 2–3 sentence purpose, 3–5 essential method signatures,
                    core concepts, gotchas/caveats, representative quick test path.
  - SPEC.md
      Purpose: Comprehensive behavioral contract for the current scope.
      Must contain: input/output formats, invariants, internal state shapes, operations,
                    validation rules, error semantics, test scenarios, success criteria.
  - PLAN.md
      Purpose: Strategic roadmap; stepwise sequence using Docs → Tests → Impl cadence.
      Must contain: what to test vs. skip, order of steps, timeboxing, dependencies,
                    risks, explicit success checkboxes per step.
  - LEARNINGS.md
      Purpose: Retrospective to capture architectural insights, pivots, fragile seams,
               production readiness, and reusable patterns.

Driving Metaphor (Operational Framing)
  Think of each core artifact as part of a harness system guiding LLM-agents:

  - SPEC.md is the bit: precise contract of what inputs/outputs are allowed, keeping the pull straight.  
  - PLAN.md is the yoke: aligns effort into test-first steps so power isn’t wasted.  
  - LEARNINGS.md are the tracks: record where the cart has gone, constraints discovered, and lessons not to repeat.  
  - README.md is the map: a concise orientation tool to reestablish bearings during integration.  

  Together these artifacts let the human act as driver, ensuring the cart (implementation) moves forward under control, with clarity preserved and ambiguity eliminated.  

High-Level Workflow (DDD)
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

Napkin Physics Mode (Upstream Simplification)
  Use this mode before drafting SPEC/PLAN to encourage parsimony.
  Output structure:
    Problem: one sentence.
    Assumptions: 3–5 bullets.
    Invariant/Contract: one precise relation or property.
    Mechanism: ≤5 bullets describing a single-file spike (stdlib or minimal deps).
    First Try: one paragraph describing the simplest path.
  Prohibitions:
    No frameworks, no new layers, no new nouns unless two are deleted elsewhere.

Toy Models (Downstream Experiments)
  Definition:
    Small, sharply scoped, fully specced implementations designed to be thrown away.
  Purpose:
    Validate data structures, invariants, APIs, and error behavior with minimal code.
  Cycle:
    SPEC.md (contract) → PLAN.md (recipe) → Tests → Minimal Impl → LEARNINGS.md (extraction).
  Principles:
    Tests-first; minimal dependencies; structured errors; event sourcing when useful.
  Exit Criteria:
    All step-level success criteria checked; insights recorded; follow-up scope cut.
  Toy Integration Convention:
    - Each toyN_* directory must contain exactly one SPEC.md, PLAN.md, and LEARNINGS.md.
    - If a SPEC or PLAN grows too large or unfocused, split scope into new toyN_* experiments.
    - Integration toys (e.g. toy5_*, toy6_*) exist to recombine validated sub-toys.
    - Replace in place: update LEARNINGS.md rather than creating multiples for the same toy.
    - When consolidating, fold prior learnings into a single current doc; discard stale versions.
    - Always bias toward minimal scope: smaller toys, fewer docs, clearer insights.
  Axis Principle for Toy Models:
    - A base toy isolates exactly one axis of complexity (a single invariant, mechanism, or seam).
    - An integration toy merges exactly two axes to probe their interaction.
    - Never exceed two axes per toy; more belongs to higher-order integration or production scope.
    - This discipline keeps learnings sharp, avoids doc bloat, and mirrors controlled experiments.

CLI + JSON as Debugger (AI-Legible Execution)
  Rationale:
    Enable the agent to “single-step” systems deterministically, inspect state, and bisect.
  Contract:
    Each functional module provides a CLI:
      stdin: JSON
      stdout: JSON
      stderr: machine-parsable error JSON when failing
    CLIs are pure (no hidden state); logs allowed but do not alter outputs.
  Conventions:
    Schema-first: document input/output JSON schemas and versions in SPEC.md.
    Stable Errors: shape { "type": "ERR_CODE", "message": "human text", "hint": "actionable fix" }.
    Quick Test: each CLI ships with a one-command golden test path.
  Minimal Pipeline Pattern:
    modA < in.json > a.json
    modB < a.json > b.json
    modC --flag X < b.json > out.json

Repository Layout Expectations
  - /libs/<name>/README.md      concise library refresh for agents
  - /docs/SPEC.md               current contract for active slice
  - /docs/PLAN.md               stepwise plan for active slice
  - /docs/LEARNINGS.md          retrospective entries per slice
  - /schemas/*.json             JSON Schemas (versioned)
  - /cli/*                      small stateless CLI entrypoints
  - /tests/*                    golden, unit, integration tests; fixtures/ as needed
  - /fixtures/*.json            canonical input/output examples for CLIs and APIs

Guardrails and Policies
  Dependencies:
    Default allowlist: stdlib or equivalent; approved lightweight libs must be enumerated.
    Any new import must be justified in SPEC.md and whitelisted in PLAN.md for this slice.
  Complexity Constraints:
    Initial spikes: single file ≤ 120 lines when feasible.
    Average function length ≤ 25 lines; cyclomatic complexity ≤ 10 per function.
    No more than two new named abstractions per slice (class/module/pattern).
  Error Handling:
    Implement top 2 failure modes; others raise clear string or structured error JSON.
    No secret leakage (keys, prompts) in errors or logs.
  Costs and Latency:
    Track approximate token/$ and p95 latency for representative tests in LEARNINGS.md.
  Security and Privacy:
    No PII in fixtures; redact or synthesize test data.

Testing Strategy
  - Unit tests per function or CLI; golden I/O tests for pipelines.
  - Error-path tests for the documented failure modes.
  - Contract tests: ensure JSON conforms to schema versions; invariants hold.
  - Snapshot tests permissible for textual outputs with stable normalization rules.

Self-Audit (Agent must run before proposing diffs)
  Print the following metrics and simplify once if any threshold is exceeded:
    file_count_changed
    total_added_lines
    imports_added_outside_allowlist
    new_named_abstractions
    max_function_cyclomatic_complexity
    average_function_length
    test_count_added vs prod_functions_touched
  If warned, rerun Napkin Physics and regenerate minimal spike.

Human Review Gates (What to present)
  - One-paragraph summary of problem and mechanism (from Napkin output).
  - SPEC and PLAN diffs with checkboxes aligned to success criteria.
  - Test results: pass/fail matrix; coverage or representative list.
  - If CLI work: pipeline diagram and sample fixture diffs (a.json → b.json).
  - Proposed next step: smallest next increment with rationale.

Decision Outcomes (Reviewer)
  - approve: merge as-is; add brief LEARNINGS entry.
  - revise_docs: tighten SPEC/PLAN; agent regenerates tests/impl.
  - revise_tests: adjust contracts; agent revises implementation.
  - revise_impl: simplify or correct; agent edits code only.
  - abort: stop slice; record why and constraints learned.

Prompts and Modes (for the Agent)
  Napkin Physics (pre-docs):
    Mode: physicists with a napkin.
    Output: Problem; Assumptions; Invariant; Mechanism; First Try; Prohibitions respected.
  DDD Docs Mode:
    Generate SPEC.md and PLAN.md for the smallest viable slice that proves the invariant.
  TDD Mode:
    Emit failing tests derived from SPEC; then minimal code to pass; then refactor.
  CLI Mode:
    Propose or update CLIs with exact stdin/out JSON exemplars and a one-line golden test.
  Self-Audit Mode:
    Compute repository metrics; if warnings, simplify and retry once before PR.

Success Criteria (per slice)
  - A minimal spike exists that demonstrates the core mechanism end-to-end.
  - Tests derived from SPEC pass; error-path tests cover top 2 failure modes.
  - If CLIs: pipeline reproduces golden fixtures deterministically.
  - Meta-docs are in sync: README (touched libs), SPEC, PLAN updated.
  - LEARNINGS adds at least one architectural insight or constraint.
  - Complexity and dependency guardrails respected.

Simplification Heuristics (apply before coding and before PR)
  - One-File Spike rule: prefer 1 file ≤ 120 lines to prove the loop.
  - Two-Function Rule: exactly two public entrypoints when feasible:
      parse(input)->state and apply(state,input)->state|output.
  - No New Nouns: do not introduce new abstractions unless you delete two.
  - 80/20 Errors: implement the two most likely failures; raise clearly for the rest.
  - Time-Boxed Satisficing: propose what you could build in 30 minutes today.

Glossary
  - DDD: Doc Driven Development; Docs → Tests → Implementation → Learnings.
  - Toy Model: miniature, fully specced experiment intended to be discarded after extracting insight.
  - Napkin Physics: upstream parsimony framing to derive minimal mechanisms.
  - CLI+JSON Debugger: UNIX-style composition where each module is a pure CLI with JSON I/O.
  - Golden Test: canonical input/output pair that must remain stable across changes.
  - Invariant: property that must hold across operations (e.g., schema validity, conservation of count).

End Notes
  The assistant’s mandate is not to produce maximal code, but to produce maximal clarity with minimal code.
  Drafts are fuel; constraints and insights are the product. Operate accordingly.
