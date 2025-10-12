# Research Workflow

Research mode is DDD's approach for external knowledge gathering and systematic question cataloguing. Before building anything, understand what's already known, what documentation exists, and what questions need answering through experimentation.

Use research mode when entering unfamiliar territory: new technologies, complex domains, poorly-documented systems, or any situation where external knowledge exists but needs organized capture.

Research mode uses a **knowledge-capture approach** built around systematic study, documentation caching, and question tracking.

## The Knowledge-Capture Approach

Research mode inverts typical "just start coding" workflows: understanding precedes experimentation.

Traditional development jumps to implementation and encounters surprises. Research mode catalogs surprises upfront, then systematically addresses them.

**Begin with inventory:**
- What external knowledge exists? (Documentation, tutorials, reference implementations)
- What concepts need understanding before experimentation?
- What questions can't be answered by reading alone?

**Study systematically:**
- Cache documentation locally for AI context and offline access
- Condense external sources into focused learning documents
- Track attribution to source materials
- Identify gaps between theory and practice

**End with questions:**
- What assumptions need validation?
- What constraints require measurement?
- What integration patterns need testing?

This disciplined approach ensures you understand the landscape before experimenting, avoiding repeated false starts.

## Core Practices

Research mode combines knowledge capture with question tracking to bridge theory and practice.

### External Knowledge Capture — Building the Foundation

Before experimenting, capture and organize external knowledge systematically.

**The practice:**
- Cache external documentation to `.webcache/` directory
- Create focused learning documents in `learnings/` or equivalent
- Condense verbose sources into essential concepts
- Link to original sources for reference
- Track what theory says vs what needs validation

**Why it helps research:**
- Prevents re-reading same documentation repeatedly
- Makes external knowledge available to AI agents as local files
- Distinguishes established knowledge from open questions
- Provides foundation for designing targeted experiments
- Enables offline work and version stability

The `.webcache/` pattern is particularly valuable: fetch documentation once, reference many times, provide as context to AI agents without network dependency.

See: [External Knowledge Capture](./external-knowledge.md)

### Open Questions Tracking — Mapping the Unknowns

Research mode's primary output: a systematic catalog of questions that Discovery mode will answer.

**The practice:**
- Maintain central questions document (`learnings/.ddd/5_open_questions.md` or equivalent)
- Categorize questions by subsystem, domain, or concern
- Link questions to learning documents they originated from
- Mark questions as answered when validated through Discovery
- Spawn new questions as research reveals gaps

**Why it helps research:**
- Prevents losing track of uncertainties during study
- Prioritizes experiments by question importance
- Provides clear transition to Discovery mode (questions → experiments)
- Documents what was uncertain when, showing reasoning evolution
- Enables parallel research across different domains

Questions are first-class artifacts. The act of cataloguing "what we don't know" is as valuable as documenting "what we learned."

See: [Open Questions Tracking](./open-questions.md)

### Study Plans — Organizing Systematic Learning

For complex domains, study plans provide structure to avoid getting lost in documentation sprawl.

**The practice:**
- Identify major areas requiring study (subsystems, concepts, APIs)
- Prioritize based on project needs
- Track completion as areas are researched
- Extract key concepts to learning documents
- Generate open questions for Discovery mode

**Why it helps research:**
- Large documentation sets become manageable
- Prevents premature deep-dives into low-priority areas
- Shows research progress and remaining scope
- Enables stopping/resuming research across sessions

Study plans are optional but valuable for domains with >20 pages of documentation.

## The Research Cycle

Research workflow follows a systematic pattern:

**1. Survey**
- Identify external knowledge sources
- Assess scope and organization
- Plan study priorities

**2. Cache**
- Download documentation to `.webcache/`
- Organize cached files by topic/system
- Ensure local availability for AI context

**3. Study**
- Read systematically (follow study plan if complex)
- Extract key concepts to learning documents
- Track sources and attribution
- Note differences between sources (conflicting documentation)

**4. Question**
- Document uncertainties in open questions tracker
- Categorize by validation approach (measurement, experiment, integration test)
- Link questions to relevant learning documents
- Prioritize questions for Discovery mode

**5. Transition**
- When sufficient questions catalogued, transition to Discovery mode
- Design experiments to answer highest-priority questions
- Return to Research mode when new gaps emerge

The cycle repeats as needed. Research and Discovery often ping-pong as validated findings reveal new questions.

## Research Outputs

Research mode produces durable artifacts distinct from Discovery outputs:

**Learning Documents** (`learnings/` directory):
- Theory from external sources
- Condensed reference material
- Links to cached documentation
- Known constraints and capabilities
- Distinction: External knowledge, not experimental findings

**Cached Documentation** (`.webcache/` directory):
- Local copies of external docs
- Version-locked for stability
- Available for AI agent context
- Offline access enabled

**Open Questions** (centralized tracker):
- Systematic catalog of unknowns
- Categorized by domain/subsystem
- Links to source learning docs
- Priority ordering for Discovery work

**Study Plans** (when applicable):
- Research roadmap for complex domains
- Progress tracking across documentation
- Completion status by topic

These artifacts provide the foundation for Discovery mode experiments.

## Relationship to Discovery Mode

Research and Discovery are complementary, often alternating:

**Research → Discovery:**
- Research catalogs questions
- Discovery builds experiments to answer them
- Findings validate or challenge theory

**Discovery → Research:**
- Experiments reveal new questions
- Back to Research to study related documentation
- Update learning docs with validated findings
- Spawn new questions for next Discovery cycle

**The ping-pong pattern** (Learning meta-mode):
- Common in knowledge-building projects
- Research provides theory, Discovery provides ground truth
- Iterates until domain understanding is comprehensive

See: [Meta-Modes & Mode Transitions](./meta-modes.md) for detailed patterns.

## When Research Stops

Research mode has clear stopping criteria:

**Stop researching when:**
- Core concepts understood well enough to begin experimentation
- Open questions catalogued and prioritized
- Cached documentation sufficient for Discovery work
- Diminishing returns on additional reading (time to validate)

**Don't stop researching when:**
- Open questions still emerging from documentation
- Core concepts remain unclear
- Missing critical reference material
- Haven't identified what needs experimental validation

Research isn't about perfect understanding—it's about identifying the right questions to answer through practice.

---

**Example in Practice**: [Case Study IV: NES Development with Learning Meta-Mode](../patterns/ddd-nes.md) demonstrates research workflow in action, showing how systematic wiki study and question cataloguing enabled targeted experimental validation through 8+ toy models.
