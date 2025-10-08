# Case Study III: Discovering Porting Mode

## When Discovery and Execution Aren't Enough

This case study documents the discovery of **Porting Mode** - a specialized DDD workflow that emerged from translating an 11k LOC C++ codebase to Rust in ~2 days.

The work revealed that reference-driven translation requires a hybrid approach distinct from pure Discovery (exploratory) or Execution (delivery) modes, with unique constraints and practices.

**Project context:** [okros](https://github.com/selberhad/okros) - a Rust port of MCL (a text-based network client)

## The Problem: Neither Mode Fits

When starting the port, we faced a dilemma:

**Discovery Mode didn't fit:**
- Not exploring uncertain requirements - we had a working reference implementation
- Goal wasn't learning density - it was behavioral equivalence
- Success wasn't "what constraints did we discover?" - it was "does it match the original?"

**Execution Mode didn't fit:**
- Too much uncertainty for direct translation (FFI, unsafe Rust, platform-specific APIs)
- No existing codebase to refactor - building from scratch
- Risk of mid-port architectural rewrites if we guessed wrong on translation approaches

**The insight:** Porting is neither greenfield exploration nor production delivery - it's **reference-driven translation** requiring its own workflow.

## What Emerged: Porting Mode

Porting Mode combines Discovery and Execution in a specialized way:

### Phase 1: Discovery (De-risk Translation Patterns)

**Goal:** Validate risky translation approaches before production use

Build isolated toy models to answer:
- Which target language idioms vs which source patterns to preserve?
- How to handle FFI/unsafe boundaries?
- Which platform-specific APIs work how?

Each toy validates one translation decision:
- FFI patterns (how to call C libraries from target language)
- State management (how to port global state)
- Platform APIs (how to handle OS-specific code)
- Language embedding (how to integrate scripting languages)

**Output:** LEARNINGS.md documenting portable patterns ready for production

**Key difference from Discovery Mode:** Questions are about "how to translate X" not "what should we build?"

### Phase 2: Execution (Systematic Translation)

**Goal:** Apply validated patterns tier-by-tier with reference as oracle

Translate in dependency order:
- Foundation types → Core abstractions → UI → Logic → Integration
- Apply patterns from Phase 1 toys
- Golden tests against reference implementation
- "Same inputs → same outputs" as measurable success

**Output:** Production code with behavioral equivalence to reference

**Key difference from Execution Mode:** Reference implementation defines correctness, not human judgment

### The "Simplicity First" Principle

Unlike pure translation (preserve all source patterns), Porting Mode allows choosing target idioms when simpler:

**Use target idioms when:**
- Standard library provides equivalent functionality
- Target language has better abstraction
- Reduces complexity without losing behavior

**Preserve source patterns when:**
- Matches behavior more directly
- Reduces translation complexity
- FFI/unsafe boundaries require it

**Example:** C++ custom string class → Rust `String` (target idiom wins because stdlib is simpler and equivalent)

This principle prevents cargo-cult translation while maintaining behavioral equivalence.

## Critical Methodological Discoveries

### 1. Toys Prevent Mid-Port Rewrites

The Discovery phase validated 12 risky patterns before production:
- FFI approaches
- State management patterns
- Platform-specific APIs
- Language interop strategies

**Result:** Zero architectural rewrites during Execution phase. All risky decisions de-risked upfront.

**Lesson:** Even when you have a reference implementation, translation approaches need validation. Toys isolate this uncertainty.

### 2. Reference Implementation as Oracle

Golden tests against the original codebase prevented behavioral drift:
- Input/output pairs from reference become test fixtures
- Side-by-side comparison during translation
- Measurable goal: "same behavior" not "good enough"

**Lesson:** Reference implementation makes correctness falsifiable. Use it as your oracle.

### 3. Brutal Honesty in Gap Tracking

Initial completion claim: "98% complete"

Systematic gap analysis revealed: Actually ~50% complete for interactive mode (focused on headless mode only)

Created PORT_GAPS.md documenting:
- Method-by-method comparison with reference
- Quantified completion (file X: Y% ported)
- Root cause analysis (why gaps exist)
- Prioritized restoration plan

**Lesson:** Porting is easy to overestimate. Systematic comparison with reference catches wishful thinking.

### 4. Economic Inversion Validated

Mandatory refactoring after every feature kept quality rising instead of decaying.

With AI assistance:
- Refactoring cost approaches zero
- Test-first discipline becomes sustainable
- Code quality improves through iteration

**Lesson:** Economic inversion (cheap generation/refactoring) isn't just theory - it works in practice for complex porting work.

### 5. Scope Evolution is Normal

Original goal: 1:1 port of all features

Reality: Some features intentionally deferred, new features added

**Intentionally deferred:** Niche features better handled by scripts
**Newly added:** Test infrastructure, new operational modes

**Lesson:** Porting reveals opportunities for scope reduction and improvement. Let the port evolve.

## When to Use Porting Mode

**Use Porting Mode when:**
- Translating existing codebase to different language/framework
- Reference implementation exists and defines correct behavior
- Goal is behavioral equivalence, not innovation
- Translation patterns need validation (FFI, unsafe, platform APIs)

**Don't use Porting Mode when:**
- No reference implementation exists (use Discovery Mode)
- Requirements are uncertain (use Discovery Mode)
- Building on existing codebase (use Execution Mode)
- Pure refactoring within same language (use Execution Mode)

## Artifacts That Enable Porting Mode

**From Discovery phase (toys):**
- `toys/toyN_*/SPEC.md` - What C++ behavior to replicate
- `toys/toyN_*/LEARNINGS.md` - Validated translation patterns
- Toy code - Reference implementations of risky patterns

**From Execution phase (production):**
- `PORTING_HISTORY.md` - Tier-by-tier completion record
- `CODE_MAP.md` - Source → target file mapping
- `PORT_GAPS.md` - Systematic gap analysis (unique to porting)

**Throughout:**
- Golden tests - Input/output pairs from reference
- Side-by-side comparison - Always have source open

## Impact on DDD Methodology

Porting Mode revealed DDD's flexibility:

**Discovery and Execution are cognitive modes, not rigid phases:**
- Discovery = "optimize for learning density"
- Execution = "optimize for production resilience"
- Porting = "optimize for behavioral equivalence"

**The methodology adapts to different goals:**
- Uncertain requirements → Discovery Mode
- Established patterns → Execution Mode
- Reference-driven translation → Porting Mode

**Core principles persist across modes:**
- Document-first workflow
- Toys/tests before production
- Mandatory refactoring
- Brutal honesty in tracking
- Economic inversion enabling discipline

## Key Takeaways

1. **Porting needs its own mode** - Neither Discovery nor Execution alone handles reference-driven translation
2. **Toys de-risk translation** - Validate patterns before production to prevent mid-port rewrites
3. **Reference is oracle** - Golden tests make behavioral equivalence measurable
4. **Simplicity first** - Use target idioms when equivalent, preserve source patterns when necessary
5. **Gap analysis matters** - Systematic comparison catches completion overconfidence
6. **Economic inversion works** - AI-assisted refactoring enables sustainable TDD discipline

**Timeline:** ~2 days for 11k LOC translation demonstrates methodology's effectiveness at scale.
