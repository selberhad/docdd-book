# Meta-Modes & Mode Transitions

Real projects don't stay in a single mode. They transition between Research, Discovery, and Execution based on the work's nature and current needs. Understanding these transition patterns—meta-modes—helps structure projects effectively.

## Meta-Modes Defined

A **meta-mode** is a recurring pattern of mode transitions that characterizes a project or project phase. Different meta-modes suit different goals.

**Common meta-modes:**
- **Learning Meta-mode**: Research ↔ Discovery ping-pong
- **Porting Meta-mode**: Discovery → Execution with reference as oracle
- **Standard Progression**: Discovery → Execution typical flow

The methodology is deliberately multi-stable—projects naturally find their appropriate meta-mode.

## Learning Meta-Mode

Learning meta-mode alternates between Research and Discovery to build comprehensive knowledge of a domain. Common in knowledge-building projects, educational work, and unfamiliar technology exploration.

**The pattern:** Research phase catalogs questions from external sources → Discovery phase validates through experiments → findings reveal new questions → back to Research. Continue ping-ponging until domain understanding comprehensive.

**Primary deliverable:** Knowledge artifact (documentation, book, reference guide), not production code. Toys remain as permanent reference implementations.

**When to use:** Primary goal is knowledge capture rather than product delivery. Building reference material, validating hardware behavior, creating domain guides, or documenting poorly-documented systems.

**See:** [Research Workflow](./research-workflow.md) for detailed practices. [Case Study IV: NES Development](../patterns/ddd-nes.md) demonstrates Learning meta-mode across 52 wiki pages and 8+ toy ROMs.

## Porting Meta-Mode

Porting meta-mode provides structured approach to reference-driven translation: translating existing codebase to different language or framework while maintaining behavioral equivalence.

**The pattern:** Discovery phase validates risky translation patterns (FFI, unsafe, platform APIs) through focused toys → Execution phase applies validated patterns tier-by-tier with reference as oracle. Golden tests verify behavioral equivalence throughout.

**Primary deliverable:** Production codebase functionally matching reference implementation, not exploratory learning.

**Key principle:** Reference implementation defines correctness. Use target language idioms when simpler, preserve source patterns when necessary for equivalence.

**When to use:** Translating existing codebase where behavioral equivalence is measurable and translation patterns need validation before production use.

**When not to use:** No reference exists, requirements uncertain, or building on existing codebase in same language (use Discovery or Execution instead).

**See:** [Discovery Workflow](./discovery-workflow.md) and [Execution Workflow](./execution-workflow.md) for mode details. [Case Study III: C++ to Rust Port](../patterns/mcl-rust-port.md) demonstrates Porting meta-mode translating 11k LOC in ~2 days.

## Standard Progression

Standard progression is the typical Discovery → Execution flow for feature development once core patterns are established. This is the default meta-mode for most projects after initial exploration.

**The pattern:** Discovery phase validates unknowns through focused toys → Execution phase builds features on established foundation. Occasional returns to Discovery when genuine uncertainty emerges, but Execution dominates once patterns proven.

**Primary deliverable:** Shipped product with production codebase. Toys serve as reference artifacts, not the end product.

**Key characteristic:** Discovery is bounded (focused validation) rather than open-ended exploration. Most work happens in Execution mode after initial pattern validation.

**When to use:** Building typical software products where core architecture decisions made early and most work is feature implementation with occasional uncertainty.

**See:** [Discovery Workflow](./discovery-workflow.md) and [Execution Workflow](./execution-workflow.md) for mode details. [Case Study I: ChatGPT Export Viewer](../patterns/chatgpt-export-viewer.md) demonstrates Standard Progression for shipped NPM package.

## Mode Transition Triggers

Transition between modes deliberately when triggers occur, don't drift unconsciously.

**Research → Discovery:** Questions catalogued and prioritized. Sufficient theory to design experiments. Reading hits diminishing returns—time to validate.

**Discovery → Research:** Experiments reveal unexpected behavior or gaps between theory and practice. New questions spawn from findings requiring external documentation.

**Discovery → Execution:** Patterns validated and extracted. Key uncertainties resolved. Ready to apply patterns to production with confidence.

**Execution → Discovery:** New genuine uncertainty blocks progress. Performance constraints or technology integration require experimentation beyond simple iteration.

**The principle:** Each mode has clear entry/exit criteria. Recognize triggers, transition deliberately.

## Choosing the Right Meta-Mode

Match meta-mode to project goals:

**Learning meta-mode:** Primary goal is knowledge artifact (book, guide, documentation). External knowledge needs validation. No production codebase planned.

**Porting meta-mode:** Translating existing codebase where reference defines correctness. Behavioral equivalence measurable. Translation patterns need de-risking.

**Standard Progression:** Building typical software product. Core decisions made early. Most work is feature implementation with occasional uncertainty.

**Wrong meta-mode signals:** Endless research without production progress (Learning when should be Standard). Repeatedly hitting fundamental knowledge gaps (Standard when should be Learning). No reference to validate against (Porting when should be Discovery).

**The fix:** Recognize mismatch, transition deliberately.

## Meta-Modes Are Descriptive

Meta-modes aren't rules—they're observed patterns helping structure work. If your project doesn't match cleanly, use atomic modes as needed. Core practices persist across all meta-modes: documentation-first, toys before production, mandatory refactoring.

The goal isn't rigid adherence—it's deliberate choice of appropriate workflow for current project needs.
