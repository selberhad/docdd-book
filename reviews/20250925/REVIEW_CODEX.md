# REVIEW_CODEX — Running Questions

Status: after reading “FAQ”

Current questions (unresolved):

- SPEC format: Should input/output and invariants use a specific JSON Schema style or table format? Any required sections beyond what’s listed?
- PLAN checkboxes: Is there a standard syntax that CI or tools parse, or are plain Markdown checkboxes sufficient?
- README length: The 100–200 word target — is exceeding okay when necessary, or should longer details always move to other docs?
- LEARNINGS organization: For non-toy repos and toyN_* dirs, where should LEARNINGS.md live (per slice in /docs vs per toy dir) and how to handle cross-module slices?
- Testing stack: Any preferred test frameworks or runners per language (e.g., pytest, jest), or entirely repo-specific?
- Golden tests command: Is there a canonical flag/command (e.g., --golden-test) expected across modules?
- JSON Schema: Which dialect/tooling to use for validation (Draft-07, 2020-12) and how modules reference schemas?
- Error semantics: Is there a standard error code naming convention (domain-prefixed?) beyond the {type,message,hint} shape?
- CLI I/O transport: Always stdin/stdout/stderr JSON, or are file-path based modes acceptable when inputs are large?
- Non-determinism: Recommended strategies for time, randomness, concurrency (e.g., fixed seeds, clock injection, normalization rules)?
- Audit/event logs: Standard format/location for execution traces (e.g., JSONL), and naming/retention guidance?
- Guardrails enforcement: Are there lint/format/complexity tools or scripts provided to check constraints, or is enforcement manual?
- Import allowlist: Where is the allowlist declared/versioned (repo-level file vs per-slice in PLAN)? Any standard format?
- Self-audit metrics: How are metrics (lines changed, complexity, etc.) computed — provided script or expectations for agents to estimate?
- Costs/latency: How to estimate and record token/$ and p95 latency consistently? Any rubric or example?
- Binary assets: Guidance for handling binaries in toys/fixtures (size limits, storage, git-lfs)?
- Cross-cutting docs: Best practice for updating multiple READMEs when changes span libraries.
- Pipeline diagrams: Preferred format (DOT/Graphviz?) and storage location when presenting CLI pipelines during review.
- Pipelines fit: Criteria for when UNIX-style JSON pipelines are a bad fit and recommended alternatives.
- Schema requirement: When are JSON Schemas mandatory in SPECs versus illustrative examples being sufficient?
- README language: For non-Python projects, should Key API use language-native signatures or pseudo-code? Any per-language templates?
- Learnings timing: The LEARNINGS header expects Duration/Estimate — how should these be captured/estimated consistently across toys?
- Examples archive: Where should new examples live and what qualifies (size/complexity limits) to keep the archive minimal and current?
- Toy naming: How to assign and increment toyN_* indices across branches/PRs to avoid collisions? Any reset policy per project phase?
- Export artifacts: Where to store non-JSON exports produced by toys (DOT/CSV) — /fixtures, /artifacts, or inside the toy dir?
- Integration toy naming: Convention for naming integration toys and mapping back to source axes.
- Discard procedure: Recommended workflow to remove toy code while preserving LEARNINGS and insights.
- Napkin notes: Location/filename convention, commit vs ephemeral policy, and whether pre-test spikes are allowed at this stage.
