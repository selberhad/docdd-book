# Checklists & Workflow

Use these condensed lists to keep slices small, testable, and reviewable.

## Slice Readiness (Docs)

- SPEC is falsifiable (I/O, invariants, operations, validation, errors).
- PLAN has minimal test‑first steps with explicit success criteria and risks.
- Napkin Physics done to cut scope and avoid new nouns.

## Tests

- Derive tests from SPEC; include error paths and an end‑to‑end case.
- Prefer properties/invariants; normalize textual outputs before snapshotting.

## Implementation

- Small spike first (≤ one file when feasible); minimal dependencies.
- Structured, actionable errors; log without altering outputs.

## Self‑Audit (Before PR)

- file_count_changed
- total_added_lines
- imports_added_outside_allowlist
- new_named_abstractions
- max_function_cyclomatic_complexity
- average_function_length
- test_count_added vs prod_functions_touched

## Review Gates

- One‑paragraph summary (from Napkin output).
- SPEC and PLAN diffs aligned to success criteria.
- Test results: pass/fail matrix; representative coverage list.
- If CLIs: pipeline diagram and sample fixture diffs (a.json → b.json).
- Proposed next step: smallest next increment with rationale.

## Decision Outcomes

- approve / revise_docs / revise_tests / revise_impl / abort (record why and constraints learned).

## Guardrails & Policies

- Dependencies: default allowlist; justify exceptions in SPEC/PLAN.
- Complexity: single‑file spike ≤120 lines when feasible; function length and complexity kept low.
- Errors: top 2 failure modes implemented; no secrets in logs.
- Security/Privacy: no PII in fixtures.
- Costs/Latency: track representative p95 and token/$ in LEARNINGS when relevant.

See also: [Doc‑Driven Principles](../foundations/ddd-principles.md), [DocDD AGENTS.md Template](../practice/docdd-agents-template.md), [Debugger Mindset](../foundations/debugger-mindset.md)
