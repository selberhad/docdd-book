# Open Questions Tracking

Systematic question cataloguing transforms research from passive reading into active preparation for experimentation. What you don't know is as valuable as what you do—when documented explicitly.

## The Central Questions Document

Maintain a single, organized catalog of open questions:

### File Location

```
learnings/.ddd/5_open_questions.md       # Meta-learning artifact
```

**Alternative locations:**
- `docs/open_questions.md`
- `QUESTIONS.md` (root level)
- `.ddd/questions.md`

**The principle:** One authoritative location. No scattered question lists.

### Document Structure

**Organized by category:**

```markdown
# Open Questions

## 1. Toolchain & Build Pipeline (8 open)
**Q1.1**: How to integrate assembler + asset tools into workflow?
- Makefile? Shell script? Both?
- Answer via: Build first test project

**Q1.2**: Symbol file generation for debugging?
- Which assembler flag enables symbols?
- Answer via: Check tool documentation

## 2. Graphics System (5 open)
**Q2.1**: How to handle attribute table granularity?
- Design around 16×16 blocks?
- Accept color bleeding?
- Answer via: Build test ROM, measure constraints

## 3. Audio Implementation (3 open, 2 answered)
**Q3.1**: ✅ **ANSWERED**: Which sound engine to use?
- Decision: FamiTone2 (beginner-friendly)
- Source: learnings/audio.md comparison

**Q3.2**: Cycle budget allocation for audio?
- Target: 1000-1500 cycles/frame?
- Answer via: Profile engine in test ROM
```

**Key elements:**
- **Numbering**: Q1.1, Q1.2 (hierarchical, stable references)
- **Category summary**: Count open vs answered questions
- **Validation approach**: "Answer via" field (how to resolve)
- **Status tracking**: Mark answered questions, link to findings
- **Cross-references**: Link to relevant learning documents

### Lifecycle Management

**Adding questions:**
1. Document question clearly (what specifically is unknown?)
2. Assign category and number
3. Note validation approach (measurement, experiment, integration test)
4. Link to source learning document if applicable

**Answering questions:**
1. Mark with ✅ **ANSWERED**
2. Document decision/finding inline
3. Link to source (toy LEARNINGS.md, measurement, test results)
4. Keep question visible (don't delete—shows reasoning history)

**Spawning follow-up questions:**
1. Answered questions often reveal new uncertainties
2. Add new question to appropriate category
3. Reference parent question if related

**Archiving:**
- Don't delete answered questions (historical value)
- Mark status clearly (✅ ANSWERED vs ⏭️ DEFERRED vs ❌ BLOCKED)
- Maintain as project memory

## Question Quality

Good questions enable focused experiments. Bad questions lead to unfocused exploration.

### High-Quality Questions

**Specific and measurable:**
- ❌ "How does scrolling work?"
- ✅ "What's the cycle cost of updating 30 nametable tiles during vblank?"

**Validation approach clear:**
- ❌ "Is CHR-RAM better than CHR-ROM?"
- ✅ "What's CHR-RAM copy performance? (measure in test ROM)"

**Scope contained:**
- ❌ "How to build complete audio system?"
- ✅ "Which sound engine: FamiTone2 vs FamiStudio? (compare cycle budgets)"

**Links to context:**
- Reference learning documents where question originated
- Note external documentation that raised uncertainty
- Cross-reference related questions

### Question Types

**Measurement questions:**
- Require empirical testing
- Discovery mode with instrumentation
- Example: "How many sprites can update per frame?"

**Decision questions:**
- Require comparison or trade-off analysis
- May need Discovery experiments or pure research
- Example: "Mapper selection: NROM vs UNROM vs MMC1?"

**Integration questions:**
- Require combining validated subsystems
- Discovery mode with integration toy
- Example: "Does DPCM audio interfere with controller reads?"

**Theory validation questions:**
- External documentation makes claim, needs reality check
- Discovery mode comparing theory vs measurement
- Example: "Wiki says 27 sprite updates/frame—verify actual timing"

Different question types suggest different validation approaches.

## Cross-Referencing with Learning Documents

Questions don't exist in isolation—they're spawned from research.

### Bidirectional Linking

**In learning document:**
```markdown
# learnings/sprite_techniques.md

## OAM DMA Timing
NESdev wiki states: "513 cycles for full OAM transfer"

**Open question**: Does this include NMI overhead?
See: Q4.3 in `.ddd/5_open_questions.md`
```

**In questions document:**
```markdown
**Q4.3**: OAM DMA timing includes NMI overhead?
- Wiki says 513 cycles, unclear if NMI entry/exit included
- Source: learnings/sprite_techniques.md
- Answer via: Measure in Mesen debugger (toy1_sprite_dma)
```

**After validation:**
```markdown
**Q4.3**: ✅ **ANSWERED**: OAM DMA timing includes NMI overhead?
- Finding: 513 cycles for DMA, 7 cycles NMI entry, 6 cycles RTI
- Total: 526 cycles measured
- Source: toys/toy1_sprite_dma/LEARNINGS.md
- Updated: learnings/sprite_techniques.md with actual measurements
```

Bidirectional links ensure questions trace back to origin and forward to resolution.

## Prioritization

Not all questions need immediate answers. Prioritize systematically.

### Priority Levels

**P0 (Blocking):**
- Blocks other work
- Uncertainty prevents progress
- Answer immediately or work is stuck

**P1 (High):**
- Affects core architecture decisions
- Needed soon but not immediately blocking
- Answer before dependent work starts

**P2 (Medium):**
- Optimization or refinement questions
- Can proceed with placeholder assumptions
- Answer when convenient

**P3 (Low):**
- Nice-to-know, not need-to-know
- Won't affect current work
- Answer if time permits, defer otherwise

### Marking Priority

```markdown
## 1. Toolchain & Build Pipeline
**Q1.1 [P0]**: How to integrate assembler into workflow?
- Blocks: First build attempt
- Answer via: Set up minimal Makefile

**Q1.2 [P2]**: Symbol file generation for debugging?
- Can debug without symbols initially
- Answer via: Check tool documentation (later)
```

Priority drives Discovery mode experiment ordering.

## Transition to Discovery Mode

Questions are the bridge from Research to Discovery.

### Discovery Planning

When questions catalogued and prioritized:

**1. Group related questions**
- Which questions test same subsystem?
- Which can be answered by one experiment?

**2. Design minimal experiments**
- One toy per isolated question (base toys)
- Integration toys for interaction questions
- Follow toy axis principle (1-2 complexity axes)

**3. Create toy SPEC/PLAN**
- Link SPEC to relevant open questions
- Mark questions as "in progress" during experiment
- Update questions tracker with findings

**4. Validate and iterate**
- Discovery findings answer questions
- Update learning documents with validated theory
- Spawn new questions from surprises
- Return to Research or continue Discovery

**The cycle:**
```
Research → Questions catalogued → Discovery planned
    ↑                                      ↓
    └─── New questions ← Findings documented
```

Questions make mode transitions explicit and purposeful.

## Anti-Patterns

**Don't:**
- Keep questions in memory or scattered notes (centralize)
- Delete answered questions (keep as history)
- Ask vague, unmeasurable questions
- Skip "Answer via" field (makes validation unclear)
- Leave questions in "unknown status" limbo

**Do:**
- Maintain single authoritative questions document
- Mark status clearly (answered/deferred/blocked)
- Write specific, measurable questions
- Document validation approach for each question
- Update learning docs when questions answered

## Tools and Automation

Question management can be automated:

**Example workflows:**
```bash
# Add question to tracker
./tools/add-question.sh "How many sprites per frame?" "Graphics" "P1"

# Mark question answered
./tools/answer-question.sh "Q4.3" "toys/toy1/LEARNINGS.md"

# Generate Discovery plan from questions
./tools/plan-from-questions.sh --priority P0,P1
```

These tools reduce friction but aren't required. Manual tracking in markdown works fine.

## Value of Explicit Unknowns

The open questions document serves multiple purposes:

**Planning:** Discovery roadmap emerges from prioritized questions

**Reasoning trail:** Shows what was uncertain when, how decisions were made

**Team coordination:** Everyone sees what's known vs unknown

**Momentum maintenance:** Clear next steps prevent "what should I work on?" paralysis

**Learning validation:** Compare initial questions to final answers (reveals growth)

**The insight:** Documented unknowns are more valuable than undocumented assumptions. Make ignorance explicit, then systematically eliminate it.

---

Open questions tracking transforms research from passive reading into active preparation. When you know what you don't know, Discovery mode can systematically make it known.
