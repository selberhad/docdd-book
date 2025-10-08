# OVERALL_REVIEW — Synthesis of Agent Reviews

Purpose: Consolidate findings from Claude’s review (REVIEW_CLAUDE.md) and Codex’s running questions (REVIEW_CODEX.md) into a single, actionable summary.

## Confirmed Principles (Consensus)
- DDD flow: AI drafts everything; humans review using SPEC, PLAN, README, LEARNINGS as control surfaces.
- Upstream simplification: Napkin Physics before specs/plans to prevent scope drift.
- Toy discipline: Single axis per toy; two-at-a-time integrations; discard code, keep insights.
- Debugger mindset: CLI + JSON I/O; deterministic behavior; structured errors; golden tests.
- Guardrails: Dependency allowlists, small spikes, complexity caps, explicit error handling.
- Repo layout: Clear locations for docs, CLIs, schemas, tests, fixtures.
- Proof by example: Archive Browser shows the complete DDD cycle from kickoff to shipped tool.

## Resolved or Well-Addressed Topics
- What DDD is and how it differs (AI-first docs/tests/code under human control).
- Napkin Physics structure and intent; binary‑weave kickoff pattern.
- Toy model cycle and axis/integration constraints.
- CLI+JSON substrate, structured error format, and golden-test purpose.
- Layout/guardrails/workflow expectations and human review gates.
- Authoring guide roles and outputs for SPEC, PLAN, README, LEARNINGS.

## Open Questions (Consolidated)

### Contracts & Authoring
- SPEC format: JSON Schema dialect/tooling; when schemas are mandatory vs. illustrative examples.
- PLAN checkboxes: Any CI-parsed convention or plain Markdown only.
- README: 100–200 words as a hard cap or guidance; per-language API signature style.
- LEARNINGS: Location policy across /docs vs toyN_*; duration/estimate capture standards.

### JSON/CLI & Testing
- Golden tests: Canonical flag/command (e.g., `--golden-test`), directory layout for fixtures.
- Error codes: Naming convention (domain-prefixed?) beyond `{type,message,hint}`.
- Input transport: When stdin/stdout is required vs. file-path modes for large inputs.
- Non-determinism: Time/randomness/concurrency strategies and normalization rules.
- JSON Schema: Dialect (Draft‑07 vs 2020‑12), validation tooling, and schema referencing.

### Guardrails & Tooling
- Enforcement: Lint/format/complexity tools or scripts to check constraints automatically.
- Import allowlist: Location/format (repo-level file vs per-slice in PLAN) and versioning.
- Self‑audit metrics: Computation method and expected reporting format.
- Audit/event logs: Standard JSONL format, file layout, and retention guidance.

### Toys, Pipelines, Examples
- Toy naming: Collisions across branches/PRs; reset policy; integration toy naming.
- Artifacts: Where to store DOT/CSV exports; logs/fixtures layout.
- Pipelines: Criteria for when UNIX‑style JSON pipelines are a bad fit and alternatives.
- Examples: Inclusion criteria and location to keep archive minimal and current.

### Methodology Boundaries (Claude)
- Failure modes: Where DDD struggles; antipatterns and team constraints.
- Legacy adoption: Retrofitting existing codebases lacking meta‑docs.
- Scale: Multi‑team practices; cross‑repo coordination.
- Event sourcing: Concrete patterns for “microscope” usage in toys.
- Pivot criteria: When to abandon vs. persist with a toy.
- Meta‑doc evolution: How SPEC/PLAN/README/LEARNINGS change from toy → production.
- Measurement: Metrics validating DDD benefits (speed, quality, maintainability).

## Synthesis — What’s Missing vs. What’s Implied
- The core methodology is well-specified; operational defaults are underspecified (schemas, error codes, goldens, allowlists, metrics).
- The Archive Browser proves feasibility; broader adoption guidance (scale, legacy, failure modes) needs codification.
- Authoring guides are strong; housekeeping policies (placement, naming, retention) should be tightened to improve repeatability.

## Recommendations (Small, High‑Leverage Additions)
- Add a short “Conventions” chapter or appendix covering:
  - JSON Schema dialect + validation tooling and referencing rules.
  - Error code naming convention and required fields.
  - Golden test flag, fixtures directory, and layout.
  - Import allowlist location/format and enforcement script.
  - Audit/event log JSONL format and file locations.
  - Napkin notes: filename/location and commit policy.
- Expand FAQ with “Boundaries & Adoption”:
  - Failure modes, legacy retrofits, multi‑team scaling, pivot heuristics, event-sourcing examples, and success metrics.
- Examples archive policy:
  - Size/complexity limits; criteria for inclusion; standard paths for ancillary artifacts.

## Next Actions (Doc Updates)
- Draft “Conventions” appendix PR with concrete defaults for schemas, errors, goldens, allowlists, metrics, and logs.
- Extend FAQ with boundaries/adoption topics from Claude’s open questions.
- Add a brief “Examples Policy” note inside `src/patterns/examples-archive.md` linking to conventions.

References
- REVIEW_CLAUDE.md (Claude’s findings)
- REVIEW_CODEX.md (Codex’s running questions)
- `src/SUMMARY.md` (chapter map)
