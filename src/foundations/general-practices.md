# General Practices

Dialectic-Driven Development requires minimal repository structure to enable parallel experimentation through toy models. Each toy is a self-contained experiment with complete meta-documentation.

DDD is inherently **flexible and modular** - different projects require different flavors. A spatial database benefits from CLI+JSON debugging and strict TDD practices, while a TUI project might emphasize human user testing over JSON pipelines. This book provides foundational patterns to help you discover the right DDD variant for your specific problem domain.

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

**Language Agnostic**: Directory structure and conventions emerge naturally from language choice (Python, Rust, JavaScript, etc.). DDD imposes no language-specific requirements.

**Iteration Cheapness**: Code can be rewritten freely since LLMs make implementation cheap. The meta-documents capture lasting insights while code remains malleable.

**Staged Evolution**: SPEC and PLAN documents can be versioned (SPEC_2.md, PLAN_2.md) for major iterations within a toy. README and LEARNINGS are living documents updated after each stage to accumulate insights.

## Essential Constraints

**Constrained Vocabulary**: When working with LLMs for content generation, limit vocabulary to well-defined terms to reduce hallucination and improve consistency.

**Meta-Document Discipline**: The four-document pattern (SPEC, PLAN, README, LEARNINGS) provides structure without prescribing implementation details.

**Clear Error Handling**: Structure errors for machine parsing when building CLI tools. Avoid leaking secrets or credentials in error messages or logs.

## Dependency Philosophy

External dependencies are technical debt. Each dependency added is a maintenance burden, security surface, and complexity multiplier. DDD encourages aggressive minimalism.

**When to add a dependency:**
- **High impact**: Solves a genuinely hard problem you shouldn't solve yourself (cryptography, parsers, protocol implementations)
- **Well-vetted**: Mature, widely-used, actively maintained
- **Documented**: Clear, comprehensive documentation you can cache locally
- **Justified**: Document the decision in SPEC.md - why this dependency is worth the cost

**When to avoid dependencies:**
- Trivial functionality stdlib can handle
- Frameworks that impose architectural constraints
- Libraries with poor documentation or frequent breaking changes
- "Convenience" wrappers around well-documented APIs

**Default bias**: Prefer stdlib. If you're reaching for a dependency, pause and ask: "Can we build this ourselves in <100 lines?" Often the answer is yes.

## External Documentation as First-Class Artifact

In dialectic-driven development, **external documentation is as important as internal documentation**. Dependencies and third-party APIs require RTFM (Read The Fine Manual) discipline.

### The `.webcache/` Pattern

Treat external documentation like code dependencies - cache it locally for offline access and AI context:

**Directory structure:**
```
.webcache/
  fastmcp_server_middleware.md
  pyo3_getting_started.md
  rust_std_collections.md
```

**Workflow:**
1. **Fetch before using**: When planning to use a dependency or API, fetch its documentation first
   ```bash
   wget https://docs.example.com/guide -O .webcache/example_guide.md
   ```
2. **Read before coding**: Review cached docs before implementation or asking AI to use the dependency
3. **Reference during development**: Provide cached docs as context to AI agents when implementing features
4. **Update when needed**: Refresh cached docs when troubleshooting or when API versions change

**Why this works:**
- **Offline access**: Documentation available without network dependency
- **AI context**: Local files can be provided to AI agents for accurate implementation
- **Version stability**: Cached docs match your dependency versions, not latest docs
- **Prevents flailing**: Reading first prevents trying wrong approaches (e.g., custom auth classes when simple strings work)

**Version control considerations:**

Whether to commit `.webcache/` to your repository depends on your context:

**Don't version-control** (add to `.gitignore`):
- Solo projects where you maintain your own cache
- Fast-moving dependencies where docs change frequently
- Prefer keeping repository lean
- Docs can be rebuilt from URLs as needed

**Do version-control**:
- Team projects where everyone needs the same documentation
- Ensures all team members reference identical docs
- Onboarding new team members (docs available immediately)
- Archived projects where external docs might disappear

Default bias: `.gitignore` it. But if your team benefits from shared cached docs, commit them.

### RTFM Before Features

When developing with dependencies:

1. **Planning phase**: Fetch and read relevant documentation
2. **SPEC.md**: Reference specific documentation sections for API contracts
3. **Implementation**: Provide cached docs to AI agents as context
4. **Troubleshooting**: Re-read docs before debugging, refresh cache if stale

External documentation is not optional. Treat it as required reading before using any dependency or third-party API.

## What DDD Doesn't Prescribe

- File organization within toys (language-dependent)
- Testing frameworks or strategies (project-dependent)
- Code complexity metrics (emerge from practice)
- Dependency management approaches (language-dependent)
- Directory structures beyond the basic toy pattern

## Toy to Production Evolution

The README serves as production documentation, written and updated alongside implementation. README and LEARNINGS must reflect current reality - stale documentation is not permitted for these living documents. Historical SPEC and PLAN versions can remain as archival documentation or be cleaned up according to preference.

When a toy proves valuable enough to ship, its mature meta-documents become the definitive production specs. Archive Browser demonstrates this path: the toy's evolved documentation serves as the shipped NPM package's complete specification.

The methodology's strength lies in its minimal constraints that enable focused experimentation rather than comprehensive rules that must be followed.