# Repository Layout, Guardrails, Workflow

Document-Driven Development requires minimal repository structure to enable parallel experimentation through toy models. Each toy is a self-contained experiment with complete meta-documentation.

DocDD is inherently **flexible and modular** - different projects require different flavors. A spatial database benefits from CLI+JSON debugging and strict TDD practices, while a TUI project might emphasize human user testing over JSON pipelines. This book provides foundational patterns to help you discover the right DocDD variant for your specific problem domain.

*Note: If this were an RFC, most recommendations would be SHOULDs not MUSTs - adapt the patterns to fit your context rather than following them rigidly.*

## Toy-Based Structure

```
toys/
  toy1_short_name/
    SPEC.md      - Initial contract for this experiment
    PLAN.md      - Initial implementation roadmap
    SPEC_2.md    - Refined contract after first iteration
    PLAN_2.md    - Updated roadmap for next stage
    README.md    - Living orientation document (updated each stage)
    LEARNINGS.md - Accumulating insights (updated each stage)
    [implementation files as needed]
  toy2_another_name/
    [same structure]
```

## Core Principles

**Toy Independence**: Each toy contains everything needed to understand and reproduce the experiment. No shared dependencies on global documentation or complex directory hierarchies.

**Language Agnostic**: Directory structure and conventions emerge naturally from language choice (Python, Rust, JavaScript, etc.). DocDD imposes no language-specific requirements.

**Iteration Cheapness**: Code can be rewritten freely since LLMs make implementation cheap. The meta-documents capture lasting insights while code remains malleable.

**Staged Evolution**: SPEC and PLAN documents can be versioned (SPEC_2.md, PLAN_2.md) for major iterations within a toy. README and LEARNINGS are living documents updated after each stage to accumulate insights.

## Essential Constraints

**Constrained Vocabulary**: When working with LLMs for content generation, limit vocabulary to well-defined terms to reduce hallucination and improve consistency.

**Meta-Document Discipline**: The four-document pattern (SPEC, PLAN, README, LEARNINGS) provides structure without prescribing implementation details.

**Clear Error Handling**: Structure errors for machine parsing when building CLI tools. Avoid leaking secrets or credentials in error messages or logs.

## What DocDD Doesn't Prescribe

- File organization within toys (language-dependent)
- Testing frameworks or strategies (project-dependent)
- Code complexity metrics (emerge from practice)
- Dependency management approaches (language-dependent)
- Directory structures beyond the basic toy pattern

## Toy to Production Evolution

The README serves as production documentation, written and updated alongside implementation. README and LEARNINGS must reflect current reality - stale documentation is not permitted for these living documents. Historical SPEC and PLAN versions can remain as archival documentation or be cleaned up according to preference.

When a toy proves valuable enough to ship, its mature meta-documents become the definitive production specs. Archive Browser demonstrates this path: the toy's evolved documentation serves as the shipped NPM package's complete specification.

The methodology's strength lies in its minimal constraints that enable focused experimentation rather than comprehensive rules that must be followed.