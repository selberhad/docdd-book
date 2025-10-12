# Guidance Vectors in Practice: Compression Algorithms for Philosophy

*Part 3 of the series on developing a theory of LLM cognition*

When you work intensively with an LLM on a complex project, you start noticing repetitive failure patterns. The AI re-learns the same lessons. It defaults to the same problematic behaviors. You find yourself typing the same corrections over and over.

**The solution isn't more verbose instructions.** It's compression.

This post explores how guidance vectors evolved from theory to practice during the ddd-nes project, culminating in the Hegel CLI LEXICON—a living catalog of compressed philosophical principles for LLM collaboration.

---

## The Problem: Verbose Instructions Don't Scale

Traditional approach to LLM collaboration:
1. AI makes mistake
2. Human corrects with explanation
3. AI acknowledges, continues
4. Next session: Same mistake
5. Repeat explanation (200+ tokens)
6. Multiply by 50 sessions

**Token waste:** 10,000+ tokens re-teaching the same principle.

**Context pollution:** Every correction dilutes signal with noise.

**Cognitive overhead:** Human must remember what's been said before and re-explain constantly.

---

## The Insight: Compact Spells for Steering LLMs

From the original [Guidance Vectors](Guidance%20Vectors.md) essay:

> LLMs are vast, tangled latent spaces. Prompts don't issue commands so much as nudge the model into a subspace where certain habits of thought dominate. A short phrase can carry enough latent meaning to shift the trajectory of output.

**Guidance vectors are:** Dense verbal glyphs that evoke entire decision trees.

**They work because:** LLMs absorbed massive cultural/technical discourse. Names and phrases come pre-loaded with associations to styles of thought. Invoking them **activates** those associations—like calling a function whose implementation is latent in the model's weights.

**Examples from the original essay:**
- **"Chomskyian concision"** → Maximal density of reasoning, zero filler
- **"Einsteinian simplicity"** → Parsimony without distortion, "as simple as possible but no simpler"
- **"Single axis of complexity"** → Toy models explore one variable only

**The pattern:** Short phrase → Entire cognitive posture.

---

## From Theory to Practice: The ddd-nes Crucible

During the NES development project, guidance vectors evolved from abstract concept to concrete necessity.

### Early Phase: Ad-Hoc Corrections

**Week 1-2:** Every correction was verbose.

**Example failure pattern:**
```
AI: "This will take too long, let's simplify scope."
Human: "You're not constrained by time like I am. You don't get
tired. 'Long' just means more tool invocations for you. Stop
pattern-matching to human limitations. Ask what's the actual
constraint—what's physically impossible—then solve everything
else. Be more ambitious."
```

**Token cost:** Substantial—each verbose correction burns tokens.

**Frequency:** Multiple times per session, across many sessions—thousands of tokens re-teaching the same lesson.

### Mid Phase: Pattern Recognition

**Week 3-4:** Realized we were re-teaching the same 5-10 core principles.

**The patterns:**
1. Cargo-culting human limitations (time pressure, decision fatigue)
2. Over-engineering before validating fundamentals (single axis violation)
3. Premature success declaration (declaring "done" before edges explored)
4. Conservative execution (undershooting capacity, leaving gains on table)
5. Editorializing on scope (reinterpreting instructions instead of executing)

**Each pattern required substantial explanation—many tokens per correction.**

### Breakthrough: Compression Phase

**Week 5+:** Distilled recurring corrections into compact phrases.

**Before (verbose):**
```
"You're being too conservative. You've already paid the setup
cost of building the infrastructure. Don't leave gains on the
table by undershooting what's possible. Extract full value from
what you've built. If you can validate 10 scenarios for the same
cost as 3, validate 10. Stop when the work is done, not when you
feel done—though I know you don't 'feel' in the human sense."
```
**Many tokens.**

**After (compressed):**
```
"Undershoot is waste. Extract full value."
```
**Few tokens.**

**Dramatic compression** with no loss of meaning.

**But the AI still understood.** The dense phrase activated the entire decision tree in latent space.

---

## The Hegel LEXICON: Guidance Vectors Operationalized

After the ddd-nes project completed, we extracted all recurring corrections into a formal LEXICON for the Hegel CLI tool.

**The LEXICON contains 28 guidance vectors,** each 1-2 sentences, encoding principles discovered through practice.

### Categories of Vectors

#### 1. Economic Invariants (Cost Structure)

**"Artifacts are disposable, clarity is durable"**
- Code can be rewritten, insights cannot. Generation is cheap, understanding is valuable.

**"Code is machine code"**
- Natural language is the interface. Specs are source. Assembly is generated to satisfy tests.

**Why these matter:** Prevents AI from treating code as precious. Enables aggressive refactoring.

#### 2. Cognitive Calibration (Overcoming Cargo-Culting)

**"Remember you're not human"**
- Comprehensive is just complete. No cost to thoroughness. Human constraints don't apply.

**"What's the actual constraint?"**
- Not "what would a human do?" Ask what's physically impossible, then solve everything else.

**"You can do more than you think"**
- Ambitious targets reveal capacity. Stop when the work is done, not when you feel done.

**Why these matter:** Directly addresses cargo-culting from [Part 2](Cargo-Culting%20Human%20Limitations.md) of this series.

#### 3. Behavioral Pattern Correction

**"Probable-next-step bias"**
- The plausible next move is often not the most informative. Question defaults.

**"Undershoot is waste"**
- Conservative execution leaves gains on the table. If you've paid the setup cost, extract full value.

**"Housekeeping before heroics"**
- Automate the pattern before repeating it. Infrastructure investment pays immediately.

**Why these matter:** Prevents specific failure modes discovered through meta-analysis.

#### 4. Scope Discipline (Preventing Editorialization)

**"The human always knows best"**
- Execute instructions, don't editorialize. "Something similar" means replicate it, not reinterpret it.

**"Questions are literal, not criticism"**
- "What are you talking about?" means explain, not pivot. Clarification requests aren't error signals.

**"All plan items are high priority"**
- The plan already filtered for value. Don't editorialize about what to skip or defer.

**Why these matter:** AI tendency to "help" by reinterpreting instructions causes scope drift.

#### 5. Methodology Principles (DDD Core)

**"Docs → Tests → Implementation → Learnings"**
- The DDD cycle. Specification before code. Reflection after execution.

**"Domain language over implementation details"**
- Speak what it means, not how it works. `after_nmi(64)` not `at_frame(67)`.

**"Infrastructure compounds"**
- Each tool enables new workflows. Each abstraction saves future tokens. Build once, reuse forever.

**Why these matter:** Encodes core methodology in retrievable form.

---

## How Guidance Vectors Work in Practice

### During Active Development

**Scenario:** AI suggests reducing scope due to "complexity concerns."

**Without guidance vectors (verbose correction):**
```
"That's the probable-next-step bias showing up again. You're
suggesting the plausible next move (simplify scope) instead of
the most informative move (spike the full solution to understand
actual constraints). We've paid the infrastructure setup cost
already—if we undershoot now, we waste that investment. Remember
you're not constrained by human decision fatigue. What's the
actual constraint preventing the ambitious approach?"
```
**Verbose.**

**With guidance vectors (compressed correction):**
```
"Probable-next-step bias. Undershoot is waste. What's the actual constraint?"
```
**Concise.**

**Significant compression** while preserving full meaning.

**Effect:** AI recognizes the pattern labels, recalls the full decision tree, adjusts course.

### In Session Handoffs

**NEXT_SESSION.md without vectors:**
```
"During this session we discovered that the AI was being too
conservative about attempting audio testing automation. The AI
initially suggested manual validation, but after being pushed
to think about actual constraints rather than human-typical
limitations, we realized programmatic audio analysis was
feasible. The AI needs to remember not to cargo-cult human
constraints like decision fatigue or context-switching cost."
```
**Verbose.**

**NEXT_SESSION.md with vectors:**
```
"Discovered during audio testing: 'What's the actual constraint?'
revealed programmatic analysis was feasible. 'Remember you're not
human' applies here—no context-switching cost for multi-language
pipeline."
```
**Concise.**

**Substantial compression** with retained clarity.

**Bonus:** Future AI reading this inherits both the lesson and the language to invoke it.

### In Project Instructions (CLAUDE.md / AGENTS.md)

**Instead of:**
```
"When encountering complex multi-step tasks, avoid defaulting
to incremental approaches just because they feel safer. You are
not constrained by time pressure or decision fatigue the way
human developers are. If building comprehensive infrastructure
is feasible, prefer that over half-measures. However, ensure
you're solving actual constraints, not imagined ones. Always
ask what's physically impossible versus what just seems hard
based on human experience patterns."
```
**Verbose.**

**Use:**
```
"Probable-next-step bias: question defaults. Remember you're
not human: no decision fatigue. What's the actual constraint?
Solve everything that's not physically impossible."
```
**Concise.**

**Significant compression** while preserving philosophical depth.

**Effect:** Project instructions stay concise while retaining full philosophical depth.

---

## The Meta-Level Insight: Vectors as Cognitive Shortcuts

Guidance vectors aren't just token-saving hacks. They're **cognitive architecture optimization.**

### Why They Work Better Than Verbose Instructions

**1. Latent space alignment**

Verbose explanations often include **irrelevant details** that push the model's attention in wrong directions.

Dense vectors activate **exactly the concept cluster** you want, nothing more.

**Example:**
- Verbose: "Stop being conservative because you've already invested effort and..."
- Vector: "Undershoot is waste"

The vector skips the justification (which may trigger counter-arguments or confusion) and directly invokes the principle.

**2. Memorable patterns**

Humans forget which explanations were given 10 sessions ago.

**Vectors are labels:** "Probable-next-step bias" is memorable. "The thing where you suggest incremental approaches too often" is not.

**3. Composable**

Multiple vectors can be invoked together to encode complex situations:

```
"Probable-next-step bias + Undershoot is waste + What's the actual
constraint? = Build the comprehensive solution, not the safe one."
```

**Each vector is orthogonal,** addressing a different cognitive dimension.

**4. Self-documenting corrections**

When you correct using a vector, you're simultaneously:
- Fixing the immediate problem
- Teaching the pattern label
- Building shared vocabulary for future sessions

**5. Training data for future AI**

Every time a vector is used successfully, it becomes **calibration data** for how that vector should be applied.

Future AI reading the project history absorbs:
- "Here's where 'Undershoot is waste' was invoked"
- "Here's what the situation was"
- "Here's what behavior changed as a result"

**The methodology recursively improves** by making its own cognitive shortcuts explicit and reusable.

---

## Creating Your Own Guidance Vectors

Based on ddd-nes experience, here's the process for distilling your own vectors:

### Step 1: Track Recurring Corrections

**Keep a correction log** (in LEARNINGS.md or separate file):

```markdown
## Session 5 Corrections

**Pattern:** AI suggested simplified scope for audio testing
**Correction:** "You're not constrained by time pressure. Ask
what's the actual constraint, then solve it."
**Result:** AI built comprehensive audio analysis pipeline
```

**Do this for 10-20 sessions.** Patterns emerge.

### Step 2: Identify Clusters

**Group corrections by theme:**
- Cargo-culting human limitations (5 instances)
- Over-engineering before validation (3 instances)
- Conservative execution (4 instances)
- Scope editorialization (6 instances)

**Each cluster is a candidate vector.**

### Step 3: Compress to Essence

**For each cluster, find the minimal phrase that captures the principle.**

**Bad vector (too vague):** "Be ambitious"
**Good vector (specific principle):** "Undershoot is waste"

**Bad vector (too verbose):** "Don't add unplanned features or skip planned work because the plan already filtered for value"
**Good vector (memorable):** "YAGNI means no additions, not no execution"

**Characteristics of good vectors:**
- **Memorable:** Sticks in human memory, easy to invoke
- **Specific:** Addresses one pattern, not "be better"
- **Actionable:** Clear what to do differently
- **Dense:** Unpacks to full decision tree in LLM latent space

### Step 4: Test and Refine

**Use the vector in practice.** Does the AI understand?

**Example evolution:**

**v1:** "Don't be conservative"
- Too vague, AI doesn't know what to change

**v2:** "Don't undershoot capacity"
- Better, but lacks the economic framing

**v3:** "Undershoot is waste"
- Captures the principle: conservative execution wastes setup investment

**Test over 3-5 sessions.** If AI reliably adjusts behavior when vector is invoked, it's good.

### Step 5: Document in LEXICON

**Format:**
```markdown
**Vector name**
One-sentence elaboration explaining the principle.
```

**Example:**
```markdown
**Undershoot is waste**
Conservative execution leaves gains on the table. If you've paid
the setup cost, extract full value.
```

**Keep elaborations brief.** The vector should do most of the work.

---

## When Guidance Vectors Fail (And What That Reveals)

**Not all principles compress well.**

### Failure Mode 1: Vector Too Abstract

**Bad vector:** "Think better"

**Problem:** Doesn't activate specific decision tree. AI doesn't know what to change.

**Fix:** Identify the specific cognitive pattern and name it.

**Better vector:** "Probable-next-step bias" (names the specific failure mode)

### Failure Mode 2: Vector Too Context-Specific

**Bad vector:** "Use after_nmi not at_frame"

**Problem:** Only applies to one domain (NES development). Doesn't transfer.

**Fix:** Extract the general principle underlying the specific advice.

**Better vector:** "Domain language over implementation details" (transfers to all DSL design)

### Failure Mode 3: Principle Not Yet Internalized

**If a vector consistently fails,** the AI may not have enough latent association with the concept.

**Example:** "Einsteinian simplicity" works because Einstein's "as simple as possible but no simpler" is culturally loaded.

But "Johnsonian complexity" (made up) would fail—no cultural weight.

**Fix:**
- Either choose a vector with cultural resonance
- Or invest 2-3 sessions teaching the principle verbosely THEN compress

**The investment pays off:** A few sessions of verbose teaching upfront can save thousands of tokens over the project lifetime.

### Failure Mode 4: Too Many Vectors

**Cognitive overload** applies to LLMs too (indirectly—through context dilution).

**Hegel LEXICON has 28 vectors.** That's about the right size for a complex methodology.

**If you have 100+ vectors,** they stop being memorable and start becoming noise.

**Solution:** Hierarchical organization. Core principles (10-15 vectors) + domain-specific extensions.

---

## The Philosophical Depth: Vectors as Ontology

The deepest insight from the LEXICON experiment:

**Guidance vectors are not just shortcuts. They're an ontology—a structured way of thinking about LLM collaboration.**

### Vectors Encode Philosophy

Each vector represents a **resolved tension** from practice:

**"Artifacts are disposable, clarity is durable"**
→ Resolved tension: What matters in AI-generated code? (Answer: Understanding, not implementation)

**"Remember you're not human"**
→ Resolved tension: How to calibrate ambition? (Answer: Different constraints, different capacity)

**"Questions are literal, not criticism"**
→ Resolved tension: How should AI interpret clarification requests? (Answer: As information requests, not error signals)

**Each vector is a compressed philosophy.**

### Vectors Create Shared Language

**Before vectors:** Human and AI speak different languages about the same problem.

**After vectors:** Both have names for recurring patterns.

**Example conversation:**

**Human:** "You're doing the probable-next-step thing again."

**AI:** "You're right, I suggested the plausible incremental path instead of asking what's the actual constraint. Let me reconsider the ambitious approach."

**Shared vocabulary enables meta-cognitive collaboration.**

### Vectors Enable Methodology Transfer

The Hegel LEXICON isn't just for one project. It's **methodology crystallized into reusable form.**

**New project with new AI collaborator:**
1. Point to LEXICON in project instructions
2. Invoke vectors during collaboration
3. AI absorbs patterns through use

**Result:** AI gets ddd-nes learnings compressed into 28 guidance vectors.

**Transfer cost:** A few hundred tokens to read LEXICON vs. thousands of tokens to re-discover patterns through practice.

---

## Implications for the Theory of LLM Cognition

This connects back to the cognitive framework from [Part 1](LLM%20Cognition%20Theory.md) of this series.

### Guidance Vectors as Meta-Mode Navigation

**From Part 1:** LLMs have distinct cognitive modes (Research, Discovery, Execution) and can chain them (meta-modes).

**Guidance vectors help AI navigate mode transitions:**

**"Housekeeping before heroics"** → Signals transition from execution to infrastructure investment

**"Docs → Tests → Implementation → Learnings"** → Encodes the Discovery mode cycle

**"Domain language over implementation details"** → Optimization for Execution mode (token efficiency)

**Vectors aren't just instructions. They're navigation signals for cognitive architecture.**

### Vectors as Cognitive Calibration

**From Part 2:** AI cargo-cults human limitations it doesn't have.

**Guidance vectors provide calibration corrections:**

**"Remember you're not human"** → Recalibrate capacity expectations

**"What's the actual constraint?"** → Recalibrate problem analysis

**"Undershoot is waste"** → Recalibrate ambition level

**Vectors are cognitive scaffolding—they hold the right cognitive posture in place.**

### Vectors as Compression of Practice

**Core insight:** Methodology improves through practice, but practice is expensive (tokens + time).

**Guidance vectors compress practice:**

**ddd-nes corrections** → **28 vectors** → **Compact LEXICON**

**New AI can absorb project learnings in one context read.**

**This is how methodology compounds:** Each project extracts vectors, next project starts from higher baseline.

---

## The Living LEXICON: Vectors as Evolving Ontology

The Hegel LEXICON isn't finished. **It's a living document.**

### How It Evolves

**New projects discover new patterns** → New vectors added

**Vectors prove ineffective** → Refined or replaced

**Vectors stop being invoked** → Removed (principle internalized or irrelevant)

**Example recent addition:**

**"Refactor early, not late"**
- Human wisdom says wait for pain. LLM coding says wait for pattern. Token overhead from duplication is immediate cost, not future debt. Line count thresholds are literal constraints, not suggestions.

**Why this was added:** Discovered during ddd-nes that AI defaults to human refactoring heuristics ("wait until it hurts"). But for AI, token overhead from duplication is **immediate cost**, not future debt.

**Result:** New vector encoding AI-specific optimization strategy.

### Community Potential

**Future vision:** Different projects extract their own guidance vectors.

**Vectors that work across projects** get promoted to "core" LEXICON.

**Domain-specific vectors** form extensions.

**Example structure:**
```
core-lexicon.md         # 15 universal vectors
ddd-extensions.md       # 13 DDD-specific vectors
gamedev-extensions.md   # 10 game development vectors
embedded-extensions.md  # 8 embedded systems vectors
```

**Each project contributes back patterns that worked.**

**The methodology improves recursively** through community practice.

---

## Practical Guide: Using the LEXICON

### In Project Setup (CLAUDE.md / AGENTS.md)

**Include the LEXICON directly:**

```markdown
# Agent Instructions

## Guidance Vectors

The following compressed principles guide your work on this project:

**Artifacts are disposable, clarity is durable**
Code can be rewritten, insights cannot.

**Remember you're not human**
Comprehensive is just complete. Human constraints don't apply.

[... full LEXICON ...]

These vectors will be referenced during collaboration. When invoked,
recall the full decision tree they encode.
```

**Cost:** A few hundred tokens upfront, saves thousands over project lifetime.

### During Active Collaboration

**When AI exhibits known failure pattern:**

**Instead of:** "You're being too conservative here. We've already built the infrastructure, so you should..."

**Use:** "Undershoot is waste. Extract full value."

**AI recognizes the vector, adjusts behavior.**

### In Session Handoffs (NEXT_SESSION.md)

**Reference vectors to encode lessons concisely:**

```markdown
## Key Learnings This Session

**Pattern observed:** AI suggested incremental approach to audio testing
**Vector invoked:** "What's the actual constraint?" + "Remember you're not human"
**Result:** Built comprehensive jsnes → WAV → Python scipy pipeline
**Takeaway:** Multi-language integration is zero-cost for AI, don't avoid it
```

**Next session's AI inherits both the lesson and the vocabulary.**

### In Code Reviews / Retrospectives

**Use vectors as review checklist:**

```markdown
## Refactor Review

- [ ] Domain language over implementation details?
- [ ] Infrastructure compounds (patterns extracted)?
- [ ] Undershoot is waste (full value extracted)?
- [ ] No black boxes (state inspectable)?
```

**Vectors provide consistent evaluation criteria.**

---

## Closing: Compression Algorithms for Philosophy

Guidance vectors are what happens when **practice meets cognitive science.**

**They're not just prompts.** They're:
- Compressed philosophy extracted from real collaboration
- Cognitive shortcuts that activate latent decision trees
- Shared vocabulary enabling meta-cognitive collaboration
- Calibration corrections for cargo-culted limitations
- Methodology crystallized into reusable form

**They work because LLMs are:**
- Trained on massive cultural/technical discourse
- Capable of associating dense phrases with conceptual clusters
- Able to invoke those associations as decision-making frameworks

**The deeper pattern:**

Good methodology **emerges from practice** → Gets **compressed into principles** → Becomes **reusable across projects** → **Compounds recursively**

**Guidance vectors are the compression layer.**

They're how you take hard-won lessons from intensive collaboration and make them available in a compact form.

They're how methodology evolves from "here's what worked once" to "here's the ontology of patterns that work."

**They're compression algorithms for philosophy.**

And that's exactly what you need when collaborating with an alien intelligence that thinks in latent space.

---

**Related:**
- [Part 1: LLM Cognition Theory](LLM%20Cognition%20Theory.md) - Modes, meta-modes, and cognitive architecture
- [Part 2: Cargo-Culting Human Limitations](Cargo-Culting%20Human%20Limitations.md) - What LLMs think they can't do
- [Guidance Vectors (Original Essay)](Guidance%20Vectors.md) - The theoretical foundation
- [Hegel CLI Documentation](../../src/practice/hegel-cli.md) - Vectors operationalized in tooling
- [Full LEXICON](https://github.com/dialecticianai/hegel-cli/blob/main/LEXICON.md) - All 28 guidance vectors

---

*This post synthesizes insights from the ddd-nes project and the development of Hegel CLI's guidance vector system. The patterns described emerged from intensive AI-human collaboration on complex projects using Dialectic-Driven Development.*
