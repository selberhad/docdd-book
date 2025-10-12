# Execution Workflow

Execution mode is for building features within established systems. Once core patterns are proven and architectural approaches validated, the heavy experimentation discipline of Discovery mode becomes unnecessary overhead. Execution mode focuses on maintaining system legibility and architectural consistency while building quickly.

**Use Execution mode when:**
- Core abstractions and patterns are established
- Requirements are clear and well-defined
- Technical constraints are documented
- Building on existing codebase (not exploring from scratch)

**Note:** Execution mode typically follows Discovery mode in standard progression. For complex domains, Research mode may precede Discovery to build foundational knowledge before experimentation. See [Meta-Modes & Mode Transitions](./meta-modes.md) for workflow patterns.

## Central Artifact: CODE_MAP.md

CODE_MAP.md is the primary coordination mechanism in Execution mode—a living architectural document that stays current through discipline.

**Key principle:** Update CODE_MAP.md before every commit that adds, removes, or renames files, or changes module purposes.

**Convention:** One CODE_MAP.md per directory containing source files (non-recursive). Each CODE_MAP.md describes only files/folders in its own directory, not subdirectories.

Example structure:
```
./CODE_MAP.md                    # Root-level files only
src/CODE_MAP.md                  # Source modules
tests/CODE_MAP.md                # Test organization
tests/unit/CODE_MAP.md           # Unit test files
```

Why this matters: CODE_MAP.md provides rapid orientation for both humans and AI agents. It prevents reverse-engineering system structure from implementation details.

See: [Code Maps](./code-maps.md)

## Feature Documentation Structure

Features are documented in dedicated directories during development:

**In-progress features:**
```
.ddd/feat/<feature_name>/
  KICKOFF.md      - Binary-weave planning (what primitive + which integration)
  SPEC.md         - Behavioral contract
  PLAN.md         - TDD implementation steps
  ORIENTATION.md  - Working notes (deleted on completion)
  LEARNINGS.md    - Optional (only if architectural insights emerge)
```

**Completed features:**
```
.ddd/done/<feature_name>/
  KICKOFF.md      - Preserved for historical record
  SPEC.md         - Preserved for historical record
  PLAN.md         - Preserved for historical record
  LEARNINGS.md    - Preserved if it exists
  (ORIENTATION.md deleted - it's a working document)
```

**LEARNINGS.md is optional in Execution mode** - Only write it if unexpected insights, architectural pivots, or valuable failures emerged. Unlike Discovery mode (where LEARNINGS is central), Execution mode assumes things go according to plan.

## The Execution Cycle

### 1. Orient

**Read CODE_MAP.md** to understand current architecture and constraints. Start in the directory where you'll work, check parent directories as needed.

Understand:
- How the system is organized
- Where new code should live
- Which patterns to follow
- What constraints exist

### 2. Kickoff

**Create `.ddd/feat/<feature_name>/` and write KICKOFF.md** using binary-weave pattern:
- Which primitive are you introducing?
- What existing product does it integrate with?
- What's the new integrated capability?

Example: "Introduce authentication primitive (A), integrate with existing API layer (B), creating authenticated endpoints (A+B=C)"

See: [Kickoff Writing](../authoring/kickoff-writing.md)

### 3. Specify

**Write SPEC.md** defining the behavioral contract:
- Input/output formats
- Invariants and state shapes
- Operations and validation rules
- Error semantics
- Test scenarios
- Success criteria

Execution mode SPECs are lighter than Discovery mode—assume established patterns, focus on what's specific to this feature.

See: [Spec Writing](../authoring/spec-writing.md)

### 4. Plan

**Write PLAN.md** with TDD implementation steps:
- Numbered steps following test-first discipline
- Each step: write test → implement → refactor
- Explicit success checkboxes per step
- Integration points with existing code
- Risks and dependencies

See: [Plan Writing](../authoring/plan-writing.md)

### 5. Implement

**Follow PLAN.md steps** with TDD discipline:
- Write failing test (red)
- Implement minimal code to pass (green)
- Commit after each step completes
- Use conventional commit format: `feat(scope): complete Step N - description`
- Update ORIENTATION.md with working notes as needed

Build on existing patterns. Keep CODE_MAP.md open for reference.

### 6. Refactor

**Default practice: refactor after feature completion.**

Why the default: AI assistance makes refactoring cheap. This prevents gradual quality degradation by ensuring the system maintains consistent quality through continuous small improvements.

Refactor to:
- Clean up integration seams between new and existing components
- Extract emerging patterns and eliminate duplication
- Ensure new code follows established architectural patterns
- Improve naming, structure, and clarity

**When to skip:** Porting work where 1:1 correspondence with reference implementation matters (refactoring would break golden tests and systematic gap analysis). Other contexts where refactoring conflicts with project goals.

The mindset: refactoring is cheap with AI, so do it unless you have a good reason not to.

See: [Refactoring with AI Agents](./refactoring-with-ai.md)

### 7. Update Documentation

**Update affected CODE_MAP.md files** to reflect structural changes (new files, renamed modules, changed purposes).

**Update project-level docs** (README, architecture docs) if feature changes user-facing behavior or system design.

### 8. Complete

**Move feature to done:**
1. Delete ORIENTATION.md (working document, no historical value)
2. Move directory: `.ddd/feat/<name>` → `.ddd/done/<name>`
3. Keep KICKOFF.md, SPEC.md, PLAN.md, and LEARNINGS.md (if exists) for historical record

## Commit Discipline

**Use conventional commit format:**
- Format: `type(scope): subject`
- Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`
- Include step numbers: `feat(auth): complete Step 3 - add token validation`

**Commit frequency:**
- After every numbered step in PLAN.md (red → green cycle)
- Before switching contexts or tasks
- When CODE_MAP.md updated (often same commit as structural change)

**History:**
- Keep linear history (prefer rebase, avoid merge commits)
- Link issues if applicable: `Refs #123`

## When to Switch Modes

**Switch to Discovery mode when:**
- Requirements reveal gaps in established patterns
- New technologies need evaluation before production use
- Performance constraints require architectural changes
- Significant uncertainty emerges that needs systematic experimentation

**Switch to Research mode when:**
- Need to study unfamiliar APIs or documentation
- External knowledge exists but isn't yet understood
- Building foundational knowledge before experimentation
- Cataloguing questions before designing experiments

The methodology is flexible—use the right mode for the current challenge. Most work in established systems benefits from Execution workflow's lighter approach, but when uncertainty emerges, switch modes deliberately. See [Meta-Modes & Mode Transitions](./meta-modes.md) for detailed transition patterns.

---

**Example in Practice**: [Case Study I: ChatGPT Export Viewer](../patterns/chatgpt-export-viewer.md) demonstrates execution workflow in action, showing how CODE_MAP.md and refactoring discipline supported the development of a shipped NPM package with clean human-AI collaboration boundaries.
