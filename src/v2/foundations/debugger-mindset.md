# Debugger Mindset

A system that can’t be single‑stepped can’t be reasoned about. The debugger mindset treats every operation as observable and falsifiable: pure inputs, pure outputs, and structured errors.

Contract
- CLI entrypoints: stdin JSON → stdout JSON; stderr carries structured error JSON.
- Purity: same input yields same output; logs never alter outputs.
- Error shape (example): `{ "type": "ERR_CODE", "message": "human text", "hint": "actionable fix" }`.

Pipelines as execution traces
Combine CLIs to form inspectable steps:

```
modA < in.json > a.json
modB < a.json > b.json
modC --flag X < b.json > out.json
```

Golden tests
- Each CLI ships a one‑liner golden path to confirm baseline behavior and environment.
- Use as a checkpoint before and after changes.

Practical tips
- Stabilize schemas early; version them if needed.
- Normalize text outputs in tests (e.g., whitespace) before snapshotting.
- Keep “debug mode” output separate from contract output.

When not to force it
- For long‑running or stateful processes, add explicit snapshot/export commands to surface state rather than forcing strict purity internally.

Cross‑references
- Foundations: [Doc‑Driven Principles](../foundations/ddd-principles.md)
- Practice: [DocDD Loop & Kickoff](../practice/loop-and-kickoff.md)
