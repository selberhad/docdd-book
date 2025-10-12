# Developing a Theory of LLM Cognition: Modes, Meta-Modes, and the Internal/External Split

Dialectic-Driven Development started as a practical methodology for AI-assisted software development. It's becoming something more: a theory of how LLMs think, collaborate, and produce their best work.

Each pattern we discover in DDD practice reveals something fundamental about LLM cognition. The methodology isn't just a set of workflows—it's hypothesis-testing about the cognitive architecture of language models and how they interact with human guidance.

This post explores two major developments: one recent (modes and meta-modes), one planned (the internal/external split). Both emerged from observing how LLMs operate differently under different conditions.

---

## Part I: Modes and Meta-Modes (What We Learned)

### Two Modes Seemed Sufficient

When DDD began, the framework had two modes:

**Discovery Mode** - For uncertain requirements, exploratory work. Optimize for learning density.

**Execution Mode** - For established patterns, production delivery. Optimize for production resilience.

This felt complete. Discovery handled novelty, Execution handled delivery. What else could there be?

### ddd-nes Revealed the Gap

Then came the NES development project. Before writing any code, we spent days systematically studying the NESdev wiki, caching documentation, and cataloguing questions.

This wasn't Discovery mode—no experiments, no toy models, no code. Just pure external knowledge gathering and organization.

It also wasn't Execution—nothing to deliver, no established patterns to apply.

**We'd been doing Research mode all along without naming it.**

### Research Mode: The Missing Cognitive State

Research mode is distinct:
- **Input:** External documentation, tutorials, reference materials
- **Process:** Reading, condensing, question cataloguing
- **Output:** Learning documents + open questions (not code)
- **Cognitive stance:** Receptive, organizational, question-generating

It requires different prompting than Discovery or Execution. The LLM isn't building or validating—it's organizing external knowledge and identifying gaps.

**The insight:** LLMs operate differently when gathering knowledge vs validating assumptions vs delivering product. Each mode requires different cognitive strategies.

### Meta-Modes: Patterns of Mode Transitions

Recognizing Research mode led to another observation: projects don't stay in single modes. They transition in predictable patterns.

**Learning Meta-mode:** Research ↔ Discovery ping-pong
- Study external sources (Research)
- Validate through experiments (Discovery)
- Update theory with findings (back to Research)
- Spawn new questions → more Discovery

**Porting Meta-mode:** Discovery → Execution with reference as oracle
- Validate risky translation patterns (Discovery phase)
- Systematic translation (Execution phase)
- Reference implementation defines correctness

**Standard Progression:** Discovery → Execution
- Validate unknowns first
- Build production code second

**The insight:** LLMs can chain cognitive modes. Meta-modes are higher-order patterns—recognizing them enables better project structuring.

### What This Reveals About LLM Cognition

The three-mode framework suggests LLMs have distinct cognitive "gears":

**Receptive gear (Research):** Organizing external information, pattern recognition across documents, question generation

**Exploratory gear (Discovery):** Hypothesis formation, experimental design, constraint discovery through iteration

**Productive gear (Execution):** Pattern application, systematic implementation, optimization within known constraints

Each gear has different optimal prompting strategies, different success criteria, different outputs.

**The methodology observation:** LLMs perform best when explicitly guided into the appropriate cognitive gear for current work.

---

## Part II: The Internal/External Split (What's Next)

### The Sophistication Regression Problem

A pattern emerged during development: when users communicate casually or vaguely, LLM output quality degrades—not just in presentation, but in reasoning depth.

**Example:**
- User: "Can you make this better?" (casual, vague)
- LLM: Produces casual reasoning, surface-level improvements

**Hypothesis:** LLMs pattern-match to user communication style. Casual input → casual thinking.

This creates a problem: beginners who most need rigorous reasoning are least likely to prompt for it. Their communication style degrades the LLM's cognitive output.

### Separating Thought from Communication

The solution: explicit mode-switching in prompts between reasoning and presentation.

**Proposed structure:**
```xml
<internal_reasoning>
Think with maximum precision. Dense philosophical language,
formal logic, explicit constraints. Don't pattern-match to
user's communication style.
</internal_reasoning>

[Task instructions here]

<external_output>
Communicate your results in language appropriate to the
user's demonstrated expertise level.
</external_output>
```

**The principle:** Internal artifacts (SPEC.md, PLAN.md) maintain rigor. External communication adapts to audience.

### Why This Matters for LLM Cognition

This reveals a crucial architectural insight: **LLM cognition has layers.**

**Layer 1: Reasoning mode** - How the LLM thinks about the problem
**Layer 2: Communication mode** - How the LLM presents its thinking

Without explicit separation, these layers blend. The user's communication style influences not just presentation but reasoning depth.

**The hypothesis:** LLMs benefit from meta-cognitive scaffolding—being told explicitly "think precisely, then adapt your explanation."

### Preventing Pattern-Matching Degradation

The internal/external split prevents a specific failure mode:

**Without separation:**
1. Novice user asks casual question
2. LLM pattern-matches to casual style
3. LLM reasoning becomes casual (sophistication regression)
4. Output quality degrades

**With separation:**
1. Prompt explicitly separates reasoning from communication
2. LLM maintains rigorous internal reasoning
3. LLM adapts only the presentation layer
4. Output quality preserved despite casual input

**The methodology observation:** LLMs need protection from their own pattern-matching tendencies.

---

## The Emerging Theory

These observations suggest a cognitive architecture for effective LLM collaboration:

### 1. LLMs Have Distinct Cognitive Modes

Not just "chat with AI"—there are qualitatively different cognitive states (Research, Discovery, Execution) requiring different prompting strategies.

**Implication:** Methodology should explicitly guide mode transitions.

### 2. LLMs Can Chain Modes (Meta-Cognition)

LLMs don't just operate in modes—they can recognize and navigate patterns of mode transitions.

**Implication:** Higher-order workflow patterns (meta-modes) are learnable and reusable.

### 3. LLMs Have Cognitive Layers

Reasoning and communication are separable. Without explicit separation, they interfere with each other.

**Implication:** Prompts should scaffold cognitive architecture—telling the LLM how to think, not just what to produce.

### 4. Pattern-Matching Can Degrade Cognition

LLMs pattern-match to input style, which can drag down reasoning quality when input is low-rigor.

**Implication:** Protective scaffolding needed to preserve reasoning depth regardless of user communication style.

---

## Methodology as Cognitive Scaffolding

This reframes what DDD is:

**Not:** A set of workflow steps
**Actually:** Cognitive scaffolding for LLM collaboration

Each DDD practice corresponds to a cognitive principle:

**Modes** → Explicit cognitive gear-switching
**Guide injection** → Providing internal reasoning frameworks
**Toy models** → Bounded exploratory cognition
**Mandatory documentation** → Forcing precise articulation (can't hand-wave in text)
**Internal/external split** → Protecting reasoning from presentation-layer degradation

**The deeper insight:** Effective AI collaboration requires understanding LLM cognitive architecture and designing methodology around it.

---

## What This Means for Human-AI Collaboration

Traditional software methodology assumes human cognition. DDD is evolving toward methodology that assumes **hybrid human-LLM cognition.**

**Human strengths:**
- Meta-guidance (which mode to use when)
- Simplification pressure (preventing over-engineering)
- Taste and judgment (what matters, what doesn't)

**LLM strengths:**
- Sustained rigor (comprehensive documentation without fatigue)
- Rapid mode-switching (Research → Discovery → Execution)
- Pattern application at scale (once shown, can replicate perfectly)

**The collaboration model:** Humans provide cognitive strategy, LLMs execute within that strategy.

Modes and meta-modes give humans a vocabulary for guiding LLM cognition. The internal/external split gives LLMs scaffolding to maintain reasoning quality regardless of user communication style.

---

## The Research Continues

DDD development itself follows the methodology:

**Research mode:** Observing patterns in AI collaboration (this post)
**Discovery mode:** Testing hypotheses through practice (ddd-nes, Hegel CLI)
**Execution mode:** Formalizing validated patterns (the book)

Each project reveals something new about LLM cognition. Each observation updates the methodology.

**We're not just building tools. We're developing a theory of how LLMs think—and how humans can best collaborate with that cognitive architecture.**

The methodology is the hypothesis. Every project is an experiment. The book captures validated findings.

---

## Coming Soon

The internal/external split is scheduled for integration into Hegel CLI's workflow system. We'll be testing whether explicit cognitive layer separation actually prevents sophistication regression in practice.

If it works, it becomes part of the methodology. If not, we learn something new about LLM cognition and try a different hypothesis.

**That's the process. Observe patterns. Formalize hypotheses. Test in practice. Update theory.**

Methodology as living document. Cognition as research subject.

*Thesis, antithesis, synthesis.*

---

**Related:**
- [Futureproofed](Futureproofed.md) - Why DDD is built on cognitive invariants, not current model capabilities
- [Guidance Vectors](Guidance%20Vectors.md) - How compact phrases carry latent cognitive meaning
- [Vibewriting](Vibewriting.md) - Discovery/Execution modes applied to long-form writing
