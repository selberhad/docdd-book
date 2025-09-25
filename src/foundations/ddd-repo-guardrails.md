## Repository Layout Expectations

  - /libs/<name>/README.md      concise library refresh for agents
  - /docs/SPEC.md               current contract for active slice
  - /docs/PLAN.md               stepwise plan for active slice
  - /docs/LEARNINGS.md          retrospective entries per slice
  - /schemas/*.json             JSON Schemas (versioned)
  - /cli/*                      small stateless CLI entrypoints
  - /tests/*                    golden, unit, integration tests; fixtures/ as needed
  - /fixtures/*.json            canonical input/output examples for CLIs and APIs

## Guardrails and Policies

- **Dependencies:**
  - Default allowlist: stdlib or equivalent; approved lightweight libs must be enumerated.
  - Any new import must be justified in SPEC.md and whitelisted in PLAN.md for this slice.

- **Complexity Constraints:**
  - Initial spikes: single file ≤ 120 lines when feasible.
  - Average function length ≤ 25 lines; cyclomatic complexity ≤ 10 per function.
  - No more than two new named abstractions per slice (class/module/pattern).

- **Error Handling:**
  - Implement top 2 failure modes; others raise clear string or structured error JSON.
  - No secret leakage (keys, prompts) in errors or logs.

- **Costs and Latency:**
  - Track approximate token/$ and p95 latency for representative tests in LEARNINGS.md.

- **Security and Privacy:**
  - No PII in fixtures; redact or synthesize test data.

## Testing Strategy

  - Unit tests per function or CLI; golden I/O tests for pipelines.
  - Error-path tests for the documented failure modes.
  - Contract tests: ensure JSON conforms to schema versions; invariants hold.
  - Snapshot tests permissible for textual outputs with stable normalization rules.

## Self-Audit (Agent must run before proposing diffs)
  Print the following metrics and simplify once if any threshold is exceeded:

  - file_count_changed
  - total_added_lines
  - imports_added_outside_allowlist
  - new_named_abstractions
  - max_function_cyclomatic_complexity
  - average_function_length
  - test_count_added vs prod_functions_touched

  If warned, rerun Napkin Physics and regenerate minimal spike.

## Human Review Gates (What to present)

  - One-paragraph summary of problem and mechanism (from Napkin output).
  - SPEC and PLAN diffs with checkboxes aligned to success criteria.
  - Test results: pass/fail matrix; coverage or representative list.
  - If CLI work: pipeline diagram and sample fixture diffs (a.json → b.json).
  - Proposed next step: smallest next increment with rationale.

## Decision Outcomes (Reviewer)

  - approve: merge as-is; add brief LEARNINGS entry.
  - revise_docs: tighten SPEC/PLAN; agent regenerates tests/impl.
  - revise_tests: adjust contracts; agent revises implementation.
  - revise_impl: simplify or correct; agent edits code only.
  - abort: stop slice; record why and constraints learned.

## Prompts and Modes (for the Agent)
  Napkin Physics (pre-docs):

  - Mode: physicists with a napkin.
  - Output: Problem; Assumptions; Invariant; Mechanism; First Try; Prohibitions respected.

  DDD Docs Mode:

  - Generate SPEC.md and PLAN.md for the smallest viable slice that proves the invariant.

  TDD Mode:

  - Emit failing tests derived from SPEC; then minimal code to pass; then refactor.

  CLI Mode:

  - Propose or update CLIs with exact stdin/out JSON exemplars and a one-line golden test.

  Self-Audit Mode:

  - Compute repository metrics; if warnings, simplify and retry once before PR.

## Success Criteria (per slice)

  - A minimal spike exists that demonstrates the core mechanism end-to-end.
  - Tests derived from SPEC pass; error-path tests cover top 2 failure modes.
  - If CLIs: pipeline reproduces golden fixtures deterministically.
  - Meta-docs are in sync: README (touched libs), SPEC, PLAN updated.
  - LEARNINGS adds at least one architectural insight or constraint.
  - Complexity and dependency guardrails respected.

## Simplification Heuristics (apply before coding and before PR)

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

