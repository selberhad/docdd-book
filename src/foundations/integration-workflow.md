# Integration Workflow

When working on established architectures where patterns are known and you're building on proven foundations, DocDD uses a lighter approach focused on maintaining architectural coherence and code quality.

## Core Artifacts: CODE_MAP.md + Refactoring

Integration mode centers on two key practices:

**CODE_MAP.md**: A living architectural document that provides structural orientation for both humans and AI agents. Updated with every commit to reflect the current system state.

**Mandatory Refactoring**: A required step after every feature implementation or integration that ensures code quality and prevents technical debt accumulation.

## CODE_MAP.md: Living Architecture Documentation

The CODE_MAP.md serves as the central orchestration document that gives both humans and AI a clear mental model of how the codebase is organized.

### Structure and Contents

**Architecture Overview**: High-level purpose, design philosophy, and data flow patterns

**Key Directories**: Functional organization with clear responsibilities

**Component Documentation**: Each major module/library documented with key functions and interactions

**Integration Patterns**: How components connect and depend on each other

**Practical Insights**: Known issues, gotchas, safety patterns, and common pitfalls

### Maintenance Discipline

- **Updated with every commit**: The CODE_MAP must always reflect current reality
- **Focus on structure over details**: Architectural insight, not implementation specifics
- **AI-agent friendly**: Written to help agents understand the system quickly
- **Change-sensitive sections**: Flag areas that are fragile or require careful modification

## Refactoring as Mandatory Step

After every feature implementation or integration, a refactoring step ensures the codebase remains clean and maintainable.

### What to Refactor

**Integration Seams**: Clean up interfaces between new and existing components

**Code Quality**: Extract patterns, eliminate duplication, improve naming

**Architectural Consistency**: Ensure new code follows established patterns

**Documentation Sync**: Update CODE_MAP.md to reflect any structural changes

### Why It's Mandatory

With AI assistance, refactoring shifts from expensive manual work to routine maintenance. The economic shift makes it feasible to continuously improve code quality rather than accumulate technical debt.

## Integration Mode Workflow

**1. Orient**: Read CODE_MAP.md to understand current architecture and constraints

**2. Plan**: Brief planning focused on integration points and architectural fit

**3. Implement**: Build the feature following established patterns

**4. Refactor**: Clean up integration seams and improve code quality

**5. Update**: Refresh CODE_MAP.md to reflect any structural changes

## When Integration Mode Works Best

- **Established patterns**: The architectural approaches are proven and understood
- **Clear requirements**: What needs to be built is well-defined
- **Known constraints**: Technical limitations and design decisions are documented
- **Stable foundations**: Core systems and interfaces are mature

## Differences from R&D Mode

**Documentation Weight**: Much lighter - CODE_MAP.md instead of four-document harness

**Planning Depth**: Tactical integration planning vs. systematic experimentation

**Risk Profile**: Lower risk due to established patterns and proven foundations

**Speed**: Faster development cycles without heavy documentation overhead

**Focus**: Orchestration and quality maintenance vs. discovery and validation

## Integration Mode Artifacts

**Primary**: CODE_MAP.md (architectural orientation)

**Secondary**: Brief integration plans for complex features

**Continuous**: Refactoring commits maintaining code quality

**Optional**: Component READMEs for complex modules (following R&D README format)

The key insight: Integration mode acknowledges that most software development is about building on existing foundations rather than solving novel problems. It provides the right level of process for this common case while preserving the option to switch to R&D mode when uncertainty arises.