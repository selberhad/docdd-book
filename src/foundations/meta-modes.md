# Meta-Modes & Mode Transitions

Real projects don't stay in a single mode. They transition between Research, Discovery, and Execution based on the work's nature and current needs. Understanding these transition patterns—meta-modes—helps structure projects effectively.

## Meta-Modes Defined

A **meta-mode** is a recurring pattern of mode transitions that characterizes a project or project phase. Different meta-modes suit different goals.

**The three atomic modes:**
- **Research**: External knowledge capture (optimizes for knowledge capture)
- **Discovery**: Experimental validation (optimizes for learning density)
- **Execution**: Production delivery (optimizes for production resilience)

**Common meta-modes:**
- **Learning Meta-mode**: Research ↔ Discovery ping-pong
- **Porting Meta-mode**: Discovery → Execution sequence with reference as oracle
- **Standard Progression**: Discovery → Execution typical flow

The methodology is deliberately multi-stable—projects naturally find their appropriate meta-mode.

## Learning Meta-Mode

Learning meta-mode alternates between Research and Discovery to build comprehensive knowledge of a domain. Common in knowledge-building projects, educational work, and unfamiliar technology exploration.

### The Research ↔ Discovery Cycle

**Research phase:**
1. Study external sources (documentation, tutorials, wikis)
2. Cache documentation locally
3. Create learning documents
4. Catalog open questions

**Transition to Discovery:**
- Questions prioritized and ready for validation
- Enough theory understood to design experiments
- Uncertainty requires hands-on testing

**Discovery phase:**
1. Build toy models to answer specific questions
2. Measure actual behavior vs documented theory
3. Extract validated patterns
4. Document findings in toy LEARNINGS.md

**Transition back to Research:**
- Experiments reveal new questions
- Need to study related documentation
- Update learning docs with validated measurements
- Document gaps between theory and practice

**Repeat:** Continue ping-ponging until domain understanding comprehensive.

### Characteristics

**Primary deliverable:** Knowledge artifact (documentation, book, reference guide)

**Toys as permanent artifacts:** Not deleted after validation—serve as reference implementations

**Theory validation focus:** "What does documentation say?" vs "What does reality do?"

**Never reaches Execution:** No production codebase—the documentation is the product

**Question-driven:** Each Discovery cycle answers specific catalogued questions

### When to Use

**Use Learning meta-mode when:**
- Primary goal is knowledge capture, not product delivery
- Entering unfamiliar domain requiring systematic study
- Building reference material or educational content
- External documentation needs validation through practice
- Multiple subsystems require independent exploration

**Example projects:**
- Learning new technology by building teaching materials
- Validating hardware behavior through test programs
- Creating domain-specific development guides
- Documenting poorly-documented systems through experimentation

**See:** [Case Study IV: NES Development](../patterns/ddd-nes.md) for extended example.

## Porting Meta-mode

Porting meta-mode provides structured approach to reference-driven translation: translating existing codebase to different language or framework while maintaining behavioral equivalence.

### Two-Phase Structure

**Phase 1: Discovery (De-risk Translation)**

Build toy models to validate risky translation patterns:
- FFI/unsafe boundary handling
- Platform-specific API differences
- State management pattern translations
- Language idiom conversions

**Goal:** Validate translation approaches before production use

**Output:** LEARNINGS.md documents with portable patterns

**Duration:** Until all risky patterns validated and catalogued

**Phase 2: Execution (Systematic Translation)**

Apply validated patterns to production translation:
- Translate in dependency order (foundation → core → UI → logic)
- Use reference implementation as oracle
- Golden tests for behavioral equivalence
- Side-by-side comparison during translation

**Goal:** Behavioral equivalence with reference

**Output:** Production codebase functionally matching reference

**Duration:** Until translation complete or intentionally scoped out

### Key Principles

**Reference as oracle:** Original implementation defines correct behavior

**Simplicity first:** Use target idioms when simpler, preserve source patterns when necessary

**Side-by-side work:** Always have reference implementation open during translation

**Validate incrementally:** Golden tests verify behavioral equivalence tier-by-tier

**Document deviations:** All intentional changes from reference documented with rationale

### Characteristics

**Discovery phase is focused:** Not exploratory—validates specific translation approaches

**Execution phase is measured:** Success is "matches reference behavior" not "good enough"

**Toys de-risk patterns:** Prevents mid-translation architectural rewrites

**Scope evolution expected:** Some features deferred, others added based on translation insights

**Gap analysis required:** Systematic comparison prevents completion overconfidence

### When to Use

**Use Porting meta-mode when:**
- Translating existing codebase to different language/framework
- Reference implementation exists and defines correct behavior
- Goal is behavioral equivalence, not innovation
- Translation patterns need validation (FFI, unsafe, platform APIs)

**Don't use Porting meta-mode when:**
- No reference implementation exists (use Discovery or Standard Progression)
- Requirements are uncertain (use Learning or Discovery)
- Building on existing codebase in same language (use Execution)
- Pure refactoring without translation (use Execution)

**See:** [Case Study III: C++ to Rust Port](../patterns/mcl-rust-port.md) for detailed example.

## Standard Progression

Standard progression is the typical Discovery → Execution flow for feature development once core patterns are established.

### The Linear Flow

**Discovery phase:**
1. Identify unknowns requiring validation
2. Build toy models to test approaches
3. Extract validated patterns
4. Document findings in toy LEARNINGS.md

**Transition to Execution:**
- Uncertainties resolved through experimentation
- Patterns validated and ready for production
- Architecture decisions made with confidence

**Execution phase:**
1. Apply validated patterns to production code
2. Build features on established foundation
3. Mandatory refactoring after each feature
4. CODE_MAP.md maintained as architecture evolves

**Occasional return to Discovery:**
- New uncertainty surfaces during Execution
- Technology integration requires validation
- Performance constraints demand experimentation

**Mostly Execution:** Once patterns established, majority of work is production delivery

### Characteristics

**Discovery is bounded:** Focused validation, not open-ended exploration

**Execution dominates:** Most work after initial pattern validation

**Returns to Discovery rare:** Only when genuinely novel work emerges

**Production codebase primary:** Features shipped, toys are reference artifacts

### When to Use

**Use Standard Progression when:**
- Building typical software product
- Core architecture decisions made early
- Most work is feature implementation
- Unknowns appear occasionally, not continuously

**This is the default:** Most projects follow this pattern after initial exploration.

## Mode Transition Triggers

How to recognize when mode transitions are needed:

### Research → Discovery

**Transition when:**
- Open questions catalogued and prioritized
- Sufficient theory to design meaningful experiments
- Reading hits diminishing returns (time to validate)
- "I wonder if..." questions emerge from study

**Don't transition if:**
- Core concepts still unclear
- Missing critical reference material
- Questions vague or unmeasurable

### Discovery → Research

**Transition when:**
- Experiments reveal unexpected behavior
- Need to study related documentation
- Gaps between theory and practice emerge
- New questions spawned from findings

**Don't transition if:**
- Current experiments incomplete
- Questions answerable through iteration
- More measurement needed, not more reading

### Discovery → Execution

**Transition when:**
- Patterns validated and extracted
- Uncertainties resolved to acceptable level
- Ready to apply patterns to production
- Architecture decisions made with confidence

**Don't transition if:**
- Key risks still unvalidated
- Patterns not yet extracted
- Core approach uncertain

### Execution → Discovery

**Transition when:**
- New uncertainty blocks progress
- Performance constraints require experimentation
- Technology integration needs validation
- Architectural assumption proves wrong

**Don't transition if:**
- Uncertainty is implementation detail (iterate in Execution)
- Refactoring can resolve issue
- Pattern already validated elsewhere

**The principle:** Transition modes deliberately, with clear triggers. Don't drift between modes unconsciously.

## Multi-Mode Projects

Complex projects often use multiple meta-modes simultaneously or sequentially.

### Parallel Modes

Different parts of project in different modes:
- **Core system**: Execution (established patterns)
- **New feature**: Discovery (uncertain approach)
- **External API study**: Research (unfamiliar technology)

**Coordination:** Track mode per subsystem in project docs

### Sequential Meta-Modes

Project evolves through meta-modes:
1. **Learning meta-mode** (initial exploration)
2. **Standard progression** (first features)
3. **Execution-dominant** (production work)
4. **Porting meta-mode** (platform migration later)

**Each meta-mode serves project phase needs**

### Meta-Mode Switching

Projects can switch meta-modes:
- Shipped product → educational material (Execution → Learning)
- Prototype → production (Discovery → Execution)
- New platform (Execution → Porting → Execution)

**The methodology adapts to evolving goals**

## Choosing the Right Meta-Mode

Consider project goals and constraints:

### Decision Matrix

| Goal | Suggested Meta-Mode | Rationale |
|------|-------------------|-----------|
| Build knowledge artifact | Learning | Research ↔ Discovery validates theory |
| Port existing codebase | Porting | Structured de-risking + systematic translation |
| Ship new product | Standard Progression | Discovery unknowns, then Execution delivery |
| Add features to established system | Execution-dominant | Occasional Discovery only when needed |

### Signs You're in Wrong Meta-Mode

**Learning meta-mode but should be Standard Progression:**
- Endless research without production progress
- Toys never transition to production code
- "Just one more thing to validate" syndrome

**Standard Progression but should be Learning:**
- Repeatedly hitting gaps in fundamental understanding
- External documentation unclear or conflicting
- Need systematic domain study, not just validation

**Porting but should be Discovery:**
- No reference implementation to compare against
- "Translating" but actually redesigning
- Behavioral equivalence not measurable

**The fix:** Recognize mismatch, transition deliberately to appropriate meta-mode.

## Meta-Modes Are Descriptive, Not Prescriptive

Meta-modes aren't rules—they're observed patterns that help structure work.

**Don't force meta-mode fit:** If your project doesn't match any meta-mode cleanly, that's fine. Use atomic modes as needed.

**Meta-modes guide, not constrain:** Understanding common patterns helps recognize when you're in one, but inventing new meta-mode patterns is valid.

**The core methodology persists:** Whether in Learning, Porting, or Standard Progression, the fundamental practices (documentation-first, toys before production, mandatory refactoring) remain constant.

---

Meta-modes help name and navigate common mode transition patterns. The goal isn't rigid adherence—it's deliberate choice of appropriate workflow for current project needs.
