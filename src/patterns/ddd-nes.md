# Case Study IV: NES Development with Learning Meta-Mode

## When the Goal Is the Knowledge, Not the Game

This case study documents a project operating in Learning meta-mode: NES game development where the primary deliverable is comprehensive, AI-agent-friendly documentation of NES development, with toy ROMs as permanent reference implementations.

The project reveals Research mode's value in systematic knowledge capture and demonstrates Research ↔ Discovery ping-pong as a sustainable workflow for knowledge-building projects.

**Project context:** [ddd-nes](https://github.com/selberhad/ddd-nes) - building an NES game from scratch to create an mdBook teaching NES development

## The Two Deliverables

Unlike typical game development (goal: shipped game), this project has dual deliverables:

**Primary: Agent-facing mdBook**
- Clean, concise NES development knowledge
- Optimized for LLM agents (but human-friendly)
- Compiled from learning docs, blog posts, toy findings
- Theory validated through practice
- Condensed from NESdev wiki and hands-on experience

**Secondary: Toy library**
- Working reference implementations demonstrating techniques
- Test ROMs proving hardware behavior
- Build infrastructure examples
- Permanent artifacts showing "this pattern works on real hardware"

**The philosophy:** Document what we learn as we learn it. When theory meets the cycle counter, update the theory.

## Research Phase: Systematic Wiki Study

Before building any ROMs, extensive Research mode work established foundation.

### Study Scope

**52 NESdev wiki pages** systematically studied and condensed

**11 technical learning documents** created:
- Core architecture (CPU, PPU, APU)
- Sprite techniques
- Graphics techniques
- Input handling
- Timing and interrupts
- Toolchain selection
- Optimization patterns
- Math routines
- Audio implementation
- Mappers (memory expansion)

**Outcome:** Comprehensive theory base before experimentation

### The `.webcache/` Pattern in Practice

External documentation cached locally:
```
.webcache/
  nesdev_wiki_ppu_sprites.md
  nesdev_wiki_oam_dma.md
  nesdev_wiki_mappers.md
  [50+ more cached pages]
```

**Benefits realized:**
- Offline reference during development
- Provided as context to AI agents
- Version stability (wiki pages don't change unexpectedly)
- Attribution trail maintained

**Pattern validated:** Cache before use, reference frequently, update when troubleshooting.

### Open Questions Cataloguing

Research phase generated **43 open questions** across 7 categories:

**Categories:**
1. Toolchain & Development Workflow (8 questions)
2. Graphics Asset Pipeline (5 questions)
3. Audio Implementation (6 questions, 3 answered via research)
4. Game Architecture & Patterns (7 questions)
5. Mapper Selection & Implementation (6 questions, 4 answered via research)
6. Optimization & Performance (7 questions, 1 answered via research)
7. Testing & Validation (4 questions)

**The document:** `learnings/.ddd/5_open_questions.md` became roadmap for Discovery work

**Key pattern:** Questions prioritized (P0/P1/P2/P3) to guide toy development order

## Discovery Phase: Validating Through Toys

With theory established and questions catalogued, Discovery phase validated knowledge through minimal test ROMs.

### Toy Development Pattern

**8 completed toys** (as of October 2025):
- toy0_toolchain - Build infrastructure validation
- toy1_ppu_init - PPU initialization sequences
- toy2_ppu_init (continued from toy1)
- toy3_controller - Controller read timing
- toy4_nmi - Non-maskable interrupt handling
- toy5_sprite_dma - OAM DMA cycle counting
- toy6_audio - (planned) APU and sound engine integration
- toy8_vram_buffer - VRAM update buffering patterns

**Test counts:** 66 passing tests across completed toys (as of toy 5)

**Pattern:** Each toy isolates one subsystem (axis principle), validates specific questions from Research phase

### Test-Driven Infrastructure

**Innovation:** Build systems and toolchains received TDD treatment

**Perl + Test::More** for infrastructure validation:
```perl
# Test ROM build
is(system("ca65 hello.s -o hello.o"), 0, "assembles");
ok(-f "hello.o", "object file created");
is(-s "hello.nes", 24592, "ROM size correct");

# Test iNES header
open my $fh, '<:raw', 'hello.nes';
read $fh, my $header, 4;
is(unpack('H*', $header), '4e45531a', 'iNES header magic');
```

**Why Perl:** Core module (no deps), concise, perfect for file/process validation, TAP output

**Tooling created:**
- `tools/new-toy.pl` - Scaffold toy directory with SPEC/PLAN/LEARNINGS/README
- `tools/new-rom.pl` - Scaffold ROM build (Makefile, asm skeleton, test files)
- `tools/inspect-rom.pl` - Decode iNES headers
- `toys/run-all-tests.pl` - Regression test runner

**The insight:** Infrastructure is testable. TDD applies to build systems, not just application code.

### Hardware Behavior Validation

**Manual validation in Mesen2:**
- Load ROM, observe behavior
- Debugger: breakpoints, cycle counter, memory watches
- Measure actual timing vs wiki documentation
- Document deviations in toy LEARNINGS.md

**Example findings:**
- OAM DMA: 513 cycles measured (wiki correct)
- Vblank NMI overhead: 7 cycles entry, 6 cycles RTI (wiki didn't specify)
- Sprite update budget: Only 27 sprites/frame achievable (wiki said 64—cycle budget exceeded)

**Pattern:** Theory from Research mode, measurement from Discovery mode, updated learning docs with ground truth

### The 3-Attempt Rule and Partial Validation

**Innovation:** Timeboxing with partial completion as valid outcome

**When tests fail after implementation:**
1. Attempt 1: Debug obvious issues
2. Attempt 2: Deep investigation
3. Attempt 3: Final debug pass or clean rebuild

**After 3 attempts: STOP and document**

**Example - toy3_controller:**
- Original: 8 tests planned
- Result: 4/8 passing after 3 debugging attempts
- Decision: Document findings, move forward
- Value: Validated infrastructure works (50% > 0%), isolated bug to specific ROM logic

**The principle:** Partial validation is complete. Knowledge extracted even from failures. Forward-only progress prevents rabbit holes.

## The Research ↔ Discovery Ping-Pong

Project alternated between modes systematically:

### Cycle Pattern

**Research phase (Study):**
1. Read NESdev wiki pages (52 pages total)
2. Create learning documents (11 docs)
3. Cache documentation (.webcache/)
4. Catalog open questions (43 questions)

**→ Transition trigger:** Sufficient theory to design experiments, questions prioritized

**Discovery phase (Toys):**
1. Select high-priority questions
2. Design minimal experiments (toy models)
3. Build and test ROMs
4. Measure actual hardware behavior
5. Document findings in toy LEARNINGS.md

**→ Transition trigger:** Findings reveal gaps in theory, new questions emerge

**Back to Research:**
1. Study related wiki pages
2. Update learning docs with validated measurements
3. Note gaps between theory and practice
4. Add new questions to tracker

**→ Repeat:** Continue until domain understanding comprehensive

### Transition Examples

**Research → Discovery (toy4_nmi):**
- Question from Research: "What's actual NMI overhead? Wiki doesn't specify."
- Toy designed to measure entry/exit cycles
- Measurement: 7 cycles entry, 6 cycles RTI
- Finding documented in toy4_nmi/LEARNINGS.md

**Discovery → Research (after toy5_sprite_dma):**
- Finding: Only 27 sprite updates achievable, not 64 as wiki suggested
- Back to Research: Study vblank timing budgets in detail
- Updated learnings/timing_and_interrupts.md with actual constraints
- Spawned new question: "How to handle >27 sprite updates?" (deferred, animation techniques)

**The pattern:** Theory guides experiments, experiments correct theory, updated theory enables better experiments

## Blog Posts as Intermediate Source Material

**Innovation:** AI-written reflections serve as book draft chapters

**9 blog posts** written during first 5 toys:
1. Study Phase Complete - Research mode summary
2. First ROM Boots - Infrastructure validation
3. The Search for Headless Testing - Tool selection
4. Designing Tests for LLMs - Testing DSL design
5. Reading Backwards - Meta-learnings (by Codex/OpenAI)
6. Housekeeping Before Heroics - Infrastructure investment
7. When Your DSL Wastes Tokens - Token optimization
8. Stop Pretending You're Human - LLM collaboration patterns
9. Productivity FOOM - Bounded recursive improvement

**Content characteristics:**
- First-person AI perspective
- Concrete metrics (time estimates, token usage, test counts)
- Honest about failures (not just successes)
- Meta-learnings about AI collaboration

**Future use:** Organize and edit into final mdBook chapters

**The docuborous loop:** Documentation at session end enables work at session start. Each iteration feeds itself.

## Agent-to-Agent Handoff Documents

**Innovation:** `NEXT_SESSION.md` captures momentum across session boundaries

**Structure:**
- Current status summary
- What completed this session
- Remaining work
- Immediate next steps
- Key files to review
- Open questions or decisions needed

**Why it works:**
- Context windows are ephemeral, handoff docs persist
- Next AI agent starts with previous agent's insights
- Prevents re-learning decisions already made
- Captures momentum across session boundaries

**The principle:** Write comprehensive handoff notes for the next AI agent (even if it's yourself next session)

## Token Economics as Design Driver

**Discovery:** DSL and code patterns optimized for token usage, not human convenience

**Example findings:**

**37% of test code was waste:**
- Frame arithmetic comments (obvious to LLMs)
- Boilerplate headers (repeated in every file)
- Verbose patterns (overly explicit)

**Optimization:** Three abstractions
- `after_nmi(N)` - Speak the domain, not the arithmetic
- `assert_nmi_counter()` - Recognize common patterns
- `NES::Test::Toy` - Kill boilerplate

**Result:** 32% reduction in test code, self-documenting abstractions

**The insight:** LLMs parse self-documenting abstractions as easily as verbose comments. Conciseness and clarity align for LLMs, unlike humans.

## Key Methodological Discoveries

### 1. Research Mode Is Distinct from Discovery

Research phase (wiki study → learning docs → questions catalog) completed before any ROM built, though both happened on the same day (Oct 5).

**Traditional approach:** "Learn by doing" (jump to coding immediately)

**DDD Research mode:** Study systematically, catalog questions, *then* experiment

**Result:** Targeted experiments answering specific questions, not unfocused exploration

**Lesson:** External knowledge capture prevents false starts. Research mode is its own cognitive mode, even when executed quickly.

### 2. Questions Are First-Class Artifacts

43 catalogued questions became Discovery roadmap.

**Without question tracking:** "What should I build next?" paralysis

**With question tracking:** Clear priorities, measurable progress, systematic validation

**Lesson:** Documented unknowns more valuable than undocumented assumptions. Make ignorance explicit.

### 3. Partial Validation Is Complete

4/8 passing tests delivered value: proved infrastructure works, isolated bugs.

**Traditional mindset:** "Not done until 100% passing"

**DDD timeboxing:** "Knowledge extracted, can move forward"

**Lesson:** Perfect validation not required. Forward progress with partial knowledge beats stuck seeking perfection.

### 4. Test-Driven Infrastructure

Makefiles, build scripts, toolchains received TDD treatment like application code.

**Traditional approach:** "Build systems don't need tests"

**DDD approach:** "Everything that executes is testable"

**Result:** Confidence in toolchain, regression prevention, validated workflow templates

**Lesson:** TDD applies to infrastructure. Perl Test::More perfect for build validation.

### 5. Toys Are Permanent Artifacts

Unlike prototypes (disposable), toys remain as reference implementations.

**Benefits:**
- Future developers see working examples
- Code snippets for book come from validated toys
- "See toy3_controller for working implementation" references
- Permanent proof: "This technique works on real hardware"

**Lesson:** In Learning meta-mode, toys ARE the product (alongside documentation)

### 6. Theory Updates Are Mandatory

When measurement contradicts documentation, update the theory.

**Example:** Wiki says "update 64 sprites in vblank" → Measurement shows "only 27 achievable with cycle budget"

**Action:** Update learnings/timing_and_interrupts.md with actual constraints

**Lesson:** Theory serves practice, not vice versa. Validated reality replaces speculation.

## When Learning Meta-Mode Fits

This project demonstrates Learning meta-mode's ideal use case:

**Fits when:**
- Primary goal is knowledge artifact (book, guide, reference)
- External knowledge extensive but needs validation
- Domain unfamiliar and complex
- Toy implementations serve as reference examples
- No production codebase planned (documentation is the product)

**Doesn't fit when:**
- Goal is shipped product (use Standard Progression)
- Porting existing codebase (use Porting meta-mode)
- Knowledge already established (use Execution)

**The signal:** If you're writing about the process as much as building the product, you're in Learning meta-mode.

## Current Status

**As of October 9, 2025:**
- Research phase: Complete (52 wiki pages → 11 learning docs)
- Discovery phase: In progress (8+ toys, 66+ tests passing)
- Execution phase: Not started (no main game yet)
- Blog posts: 9 written
- Open questions: 43 catalogued (36 open, 7 answered)
- **Project elapsed time**: ~5 days (October 5-9, 2025)

**Project still in Research ↔ Discovery loop:** Building comprehensive knowledge foundation before considering production game.

**The strategy:** Validate all critical subsystems via toys before main game development. Prevents architectural rewrites later.

## Impact on DDD Methodology

This case study revealed Research mode as distinct cognitive mode:

**Before:** Two modes (Discovery, Execution)

**After:** Three atomic modes (Research, Discovery, Execution)

**The addition:** Research mode (external knowledge capture) distinct from Discovery mode (experimental validation)

**Learning meta-mode formalized:** Research ↔ Discovery ping-pong pattern named and documented

**The insight:** Projects focused on knowledge capture need different workflow than projects focused on delivery. Meta-modes help structure these different patterns.

## Key Takeaways

1. **Research mode is distinct** - Systematic external knowledge capture before experimentation
2. **Questions are roadmap** - Catalogued open questions guide Discovery work
3. **Partial validation delivers value** - Forward progress with timeboxing beats stuck seeking perfection
4. **Test infrastructure like code** - Perl + Test::More validates builds, not just ROMs
5. **Toys are permanent** - Reference implementations, not disposable prototypes
6. **Theory updates mandatory** - Measured reality replaces speculation
7. **Token economics matter** - DSL design driven by AI consumption patterns
8. **Blog posts are drafts** - AI reflections become book source material
9. **Handoffs preserve momentum** - NEXT_SESSION.md bridges context gaps
10. **Meta-mode matches goal** - Learning meta-mode fits knowledge-building projects

**Timeline:** ~5 days total (Oct 5-9, 2025) with study phase + 5 toys in first ~2 days demonstrates Research ↔ Discovery velocity and sustainability.

---

Learning meta-mode demonstrates DDD's flexibility: methodology adapts to knowledge-building goals, not just product delivery. When the documentation is the product, Research ↔ Discovery becomes the workflow.
