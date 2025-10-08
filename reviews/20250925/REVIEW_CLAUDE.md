# REVIEW.md - Running Questions

## Initial Questions from SUMMARY.md

- What exactly is Dialectic-Driven Development and how does it differ from other development methodologies?
- What is "napkin physics" in the context of DDD?
- What makes toy models important for DDD and how are they different from other modeling approaches?
- What is the "debugger mindset" and how does it apply to documentation?
- What specific repo layout, guardrails, and workflow are recommended?
- What is the AGENTS.md template and how is it used in practice?
- How do the authoring guides work together as a system?
- What are the key patterns shown in the examples?
- What common questions or misconceptions does the FAQ address?

## Questions Resolved

- What exactly is Dialectic-Driven Development and how does it differ from other development methodologies? → **ANSWERED**: DDD is AI-driven development where AI generates all artifacts (docs, specs, plans, tests, implementations) while humans review and control the process through four core meta-documents (SPEC, PLAN, README, LEARNINGS)
- What is "napkin physics" in the context of DDD? → **ANSWERED**: A structured upstream simplification technique to prevent scope drift, consisting of Problem (1 sentence), Assumptions (3-5 bullets), Invariant/Contract (1 precise property), Mechanism (≤5 bullets for minimal path), and First Try (short paragraph with simplest approach)
- What makes toy models important for DDD and how are they different from other modeling approaches? → **ANSWERED**: Toy models are cheap, discardable experiments (not products) that validate single technical ideas through SPEC→PLAN→Implementation→LEARNINGS cycles. They follow the "axis principle" (max 2 axes of complexity per toy) and prioritize learning/insight over code preservation
- What is the "debugger mindset" and how does it apply to documentation? → **ANSWERED**: The debugger mindset makes system execution legible and falsifiable for AI agents through CLI+JSON architecture with deterministic behavior, no hidden state, structured error handling, and golden tests for validation checkpoints
- What specific repo layout, guardrails, and workflow are recommended? → **ANSWERED**: Standard layout with /docs/{SPEC,PLAN,LEARNINGS}.md, /libs/*/README.md, /cli/*, /schemas/*.json, /tests/*. Guardrails include dependency allowlists, complexity limits (≤120 lines per file, ≤25 lines per function), and self-audit metrics before PRs
- What is the AGENTS.md template and how is it used in practice? → **ANSWERED**: A repository template that guides AI agents in DDD practice, covering the 5-step loop (SPEC→PLAN→Implementation→LEARNINGS→README), napkin physics, binary-weave kickoff pattern, toy model discipline, and CLI+JSON conventions
- How do the authoring guides work together as a system? → **ANSWERED**: Five agent-oriented templates that provide structured constraints and examples: Spec (contracts/falsifiable behavior), Plan (TDD roadmaps), Kickoff (napkin physics + binary-weave), README (100-200 word AI refresh docs), Learnings (dense retrospectives with evidence/pivots/impact)
- What are the key patterns shown in the examples? → **ANSWERED**: The Archive Browser example shows complete DDD cycle from kickoff to shipped NPM package, demonstrating: napkin physics → binary-weave plan (10 stages: A,B,C=A+B,D,E=C+D,...) → specs with JSON I/O contracts → TDD plans → successful real product
- What common questions or misconceptions does the FAQ address? → **ANSWERED**: Clarifies that AI writes docs (not human), distinguishes toy models from prototypes, explains "one axis of complexity" principle, justifies CLI+JSON over frameworks for visibility, addresses speed concerns (slower Day 1, faster Day 5), supports both solo and team use

## New Questions Raised

- How exactly does the "meta-document harness" system work in practice? What does a complete cycle look like? → **PARTIALLY ANSWERED**: The Archive Browser example shows a complete real-world cycle (napkin physics → kickoff → SPEC → PLAN → TDD implementation → shipped NPM package), but more detail on the harness dynamics would be helpful
- What does "event sourcing as your microscope" mean practically for toy models?
- How do you determine when to pivot vs. persist in toy model experiments?

## Questions from Reading Process

- How does DDD handle integration with existing codebases that weren't built with this methodology?
- What are the failure modes of DDD? When doesn't this approach work well?
- How does the methodology scale to larger teams (beyond solo + AI agent)?
- What tools could be built to support DDD workflows (automated SPEC validation, PLAN tracking, etc.)?

---

## Claude's Analysis of Key Takeaways and Remaining Questions

### Key Takeaways from Book Review

**1. Core Philosophy**
- DDD inverts traditional development: AI generates all artifacts (docs, specs, plans, code) while humans maintain control through review and constraints
- The methodology addresses AI consistency problems through structured documentation that acts as "memory" across sessions
- Four meta-documents (SPEC, PLAN, README, LEARNINGS) form a harness system that keeps AI aligned while preserving human oversight

**2. Strategic Simplification Techniques**
- Napkin Physics prevents scope creep through 5-component upstream simplification
- Toy Models validate ideas cheaply through disposable experiments following the "axis principle" (max 2 complexity axes)
- Binary-weave integration pattern (A, B, C=A+B, D, E=C+D...) prevents combinatorial explosion in complex builds

**3. Technical Architecture Principles**
- CLI+JSON substrate provides AI-legible, deterministic interfaces with no hidden state
- Golden tests serve as validation checkpoints for consistent behavior
- System legibility makes execution transparent and falsifiable for both humans and AI agents
- Strict guardrails (≤120 lines per file, ≤25 lines per function) maintain manageable complexity

**4. Practical Implementation**
- Complete workflow: Napkin Physics → SPEC → PLAN → TDD Implementation → LEARNINGS
- Repository structure with clear artifact locations (/docs/, /libs/, /cli/, /schemas/, /tests/)
- Self-audit metrics and pre-commit validation ensure quality gates
- Real-world validation through Archive Browser example (shipped NPM package)

### Critical Unanswered Questions

**1. Methodology Boundaries**
- *Failure modes*: When does DDD break down? What project types or team dynamics make it ineffective?
- *Legacy integration*: How do you retrofit existing codebases that lack the meta-document structure?
- *Scale limits*: Does the methodology work beyond solo developer + AI agent scenarios?

**2. Practical Implementation Gaps**
- *Tooling ecosystem*: What automated validation, tracking, and workflow tools could support DDD?
- *Organizational adoption*: How does DDD integrate with existing engineering cultures and processes?
- *Learning curve*: What's the actual skill ramp-up time and common pitfalls for new practitioners?

**3. Deeper Architectural Questions**
- *Event sourcing details*: What does "event sourcing as your microscope" mean for toy model practice?
- *Pivot decisions*: How do you determine when to abandon vs. persist with toy model experiments?
- *Meta-document evolution*: How do the four core documents change as projects mature from toy to production systems?

**4. Strategic Context**
- *Competitive analysis*: How does DDD compare to other AI-assisted development approaches emerging in 2024-2025?
- *Long-term sustainability*: Will these practices remain effective as AI capabilities evolve?
- *Measurement*: What metrics validate DDD's claimed benefits (speed, quality, maintainability)?

The book provides a comprehensive methodology but leaves significant questions about boundaries, failure modes, and practical adoption challenges that would benefit from additional research and real-world case studies.