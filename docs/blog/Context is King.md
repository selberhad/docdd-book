# Context is King: Why We Pivoted from MCP to CLI

*Part 4 of the series on developing a theory of LLM cognition*

When we started building Hegel, the workflow orchestration tool for Dialectic-Driven Development, the obvious choice seemed to be MCP—the Model Context Protocol. MCP is designed exactly for this: exposing tools and data to AI agents through a standardized protocol.

We built it. It worked. But something felt off.

The output quality was... flat. Generic. The AI would invoke the tools correctly, follow the workflows, but the **reasoning felt bureaucratic**. Like filling out forms instead of thinking through problems.

So we pivoted. Rebuilt the entire thing as a CLI tool. Named it "Hegel."

And the output quality changed immediately.

This post is about why that happened, and what it reveals about a design surface most developers don't even know exists: **context composition**.

---

## The Phenomenon: Same Functionality, Different Feel

Let me show you what changed.

**With MCP (the original approach):**

The AI would interact with the workflow server through generic tool calls:
```
Tool: get_workflow_state
Result: {"current_node": "spec", "mode": "discovery"}

Tool: transition_phase
Parameters: {"to": "plan", "claim": "spec_complete"}
Result: {"success": true, "new_node": "plan"}
```

Functional. Clean. Completely generic.

**With CLI (the pivot):**

The AI would suggest commands:
```bash
$ hegel start discovery

$ hegel next '{"spec_complete": true}'
Transitioned: spec → plan

$ hegel status
Mode: discovery
Current node: plan
```

Same functionality. But now every interaction puts **"hegel"** in the context.

By the end of a session, "hegel" appears 15-25 times in the conversation history.

**And the output quality measurably improved.**

The AI's reasoning became more systematic. More dialectical. More focused on synthesis and progression. Not because we changed the underlying workflow logic—we didn't. But because **the name itself was shaping the output**.

---

## The Mechanism: Context Accumulation

Here's what's actually happening:

**LLM output is a function of context.** Everything that appears in the conversation history influences what the model generates next. This isn't controversial—it's how transformers work.

**Tool invocations appear in context.** When the AI calls a tool or suggests a command, that invocation becomes part of the context for subsequent outputs.

**Repetition compounds effects.** The first time "hegel" appears, it might activate some latent associations. The twentieth time, those associations are significantly reinforced.

**This is measurable.** We could observe it directly: sessions using the CLI produced more coherent, more methodologically-aligned reasoning than sessions using the MCP server, even though the underlying workflow logic was identical.

### Why MCP Hides This

**MCP tool invocations are invisible in the user-facing interface.**

The user doesn't see:
```
Calling tool: ddd_server.get_workflow_state
Result: {...}
```

They might see the AI say "Let me check the workflow state," but the actual tool name is hidden.

**CLI commands are visible and explicit:**
```
Let me start the discovery workflow:
$ hegel start discovery
```

The command is right there in the conversation. Visible to both user and AI. Part of the shared context.

**Every subsequent invocation reinforces the pattern.**

---

## Names Carry Latent Associations

Let's talk about what "Hegel" brings to the table.

**Georg Wilhelm Friedrich Hegel** is known for:
- **Dialectical method**: Thesis → Antithesis → Synthesis
- **Systematic progression**: Moving through contradictions toward higher understanding
- **Historical consciousness**: Understanding present through its development
- **Philosophical rigor**: Dense, precise reasoning

When an LLM sees "hegel" repeatedly in context, these associations activate.

**Not because we explicitly tell it "think dialectically."** But because the name itself carries cultural/philosophical weight that the model absorbed during training.

**This isn't speculation—it's observable in output.**

### The Counterfactual

What if we'd named it differently?

**"workflow-manager":**
- Generic, bureaucratic
- No philosophical weight
- Associations: administration, process compliance
- Would reinforce form-filling behavior, not dialectical thinking

**"ddd-tool":**
- Descriptive but flat
- Associations: tooling, utilities, helpers
- Would reinforce "I am a tool being used" rather than "we are collaborating on systematic methodology"

**"assistant":**
- Wrong frame entirely
- Positions AI as subordinate helper, not autonomous collaborator
- Would undermine the collaborative stance DDD requires

**"Hegel":**
- Philosophical weight
- Dialectical associations
- Systematic progression
- **Primes exactly the cognitive mode we want**

The name isn't branding. **It's a guidance vector.**

---

## Every Repeated Element is a Vector

Once you see this pattern, you see it everywhere.

**It's not just the top-level tool name.**

### Command Names Matter

Compare these:

**Option A:**
```bash
hegel start discovery
hegel next '{"spec_complete": true}'
hegel status
```

**Option B:**
```bash
hegel begin explore
hegel advance '{"spec_done": true}'
hegel check
```

**Option C:**
```bash
hegel init research
hegel proceed '{"specification_completed": true}'
hegel info
```

Each version activates slightly different associations:
- **start/next/status**: Systematic, state-machine, deterministic
- **begin/advance/check**: Organic, progressive, observational
- **init/proceed/info**: Technical, administrative, informational

We chose "start/next/status" deliberately for their clarity and systematic connotations.

### File Paths Accumulate

```bash
$ hegel analyze
Reading: .hegel/state.json
Reading: .hegel/hooks.jsonl
Reading: .hegel/states.jsonl
```

Every invocation shows `.hegel/` in the output.

The directory name reinforces the tool's identity. It's not `.workflow/` or `.ddd/` or `.state/`—it's `.hegel/`.

**The filesystem structure itself is part of the context composition.**

### Error Messages Shape Thinking

**MCP server error:**
```json
{
  "error": "InvalidTransition",
  "message": "Cannot transition from spec to code without plan"
}
```

**Hegel CLI error:**
```
Error: Invalid transition
Cannot advance from spec → code without completing plan phase

Suggestion: Run `hegel next '{"plan_complete": true}'` first
```

The CLI version:
- Uses workflow-appropriate language ("advance," "phase")
- Suggests the next command with the tool name
- **Reinforces the systematic progression model**

Even errors are context design opportunities.

---

## The Broader Pattern: Everything That Repeats is a Vector

This extends far beyond CLI tools.

### Variable and Function Names

**In your codebase:**
```python
# Generic
result = process(data)
output = transform(input)

# Weighted
insight = synthesize(observations)
understanding = distill(experiences)
```

If you're working with an AI on philosophy-heavy code, the second style primes more conceptual thinking. The names themselves guide interpretation.

### API Design

**Generic REST API:**
```
POST /api/v1/workflows
GET /api/v1/workflows/{id}
PUT /api/v1/workflows/{id}/state
```

**Conceptually-weighted API:**
```
POST /api/v1/dialectic/begin
GET /api/v1/dialectic/{id}/synthesis
PUT /api/v1/dialectic/{id}/advance
```

Same functionality. Different semantic weight in documentation, discussions, and AI interactions.

### Documentation Language

**Technical documentation** that uses generic language:
> "The system processes inputs through a series of transformations..."

**Conceptually-weighted documentation:**
> "The system synthesizes inputs through dialectical progression..."

When AI reads this documentation (or when you reference it repeatedly), the language shapes how problems are framed.

---

## Design Implications: Choosing Names Intentionally

So how do you apply this?

### The Cumulative Weight Test

**Ask:** If an AI sees this name 20+ times in a session, will it **improve or degrade** the quality of reasoning?

**Positive examples:**
- Names with philosophical/methodological weight: "hegel," "socrates," "dialectic"
- Names that encode process: "synthesis," "distill," "refine"
- Names that prime desired cognitive modes: "explore," "validate," "integrate"

**Negative examples:**
- Generic bureaucratic terms: "manager," "handler," "processor"
- Vague helpers: "assistant," "utility," "tool"
- Over-technical jargon that obscures meaning
- Names that prime wrong cognitive modes: "execute" (sounds robotic), "comply" (sounds subordinate)

### Cultural Associations Matter

Not everyone knows Hegel's philosophy in detail. That's fine.

**What matters is:**
- The name carries *some* cultural weight (not generic)
- The associations align with your intended use (dialectical → systematic methodology)
- The LLM absorbed these associations during training

**Test this empirically:**
- Try alternative names in practice
- Observe whether output quality/style changes
- Choose names that produce better reasoning

### Intentional vs. Accidental Vectors

**Accidental vectors** happen by default:
- You name things descriptively
- Generic terms accumulate in context
- Output quality drifts toward generic/bureaucratic

**Intentional vectors** require deliberate choice:
- You consider semantic weight of names
- Philosophically/methodologically-loaded terms accumulate
- Output quality aligns with desired cognitive mode

**The difference is awareness.**

Once you know context composition is a design surface, you can optimize for it.

---

## Why This Was Invisible to Most Developers

The standard view of tool design:
- **Functionality**: Does it work?
- **Usability**: Is it easy to use?
- **Performance**: Is it fast?
- **Reliability**: Does it break?

**Missing from this list: Context composition.**

"What accumulates in the LLM's attention when this tool is used repeatedly?"

### The Utilitarian Blindspot

**Most developers think:**
- "Names are just identifiers"
- "As long as it's clear what the function does, the name doesn't matter"
- "The AI doesn't care about naming—it's all the same to the model"

**This is wrong.**

Names aren't just labels. They're **repeated semantic signals** that shape how problems are framed and solutions are generated.

**But you can't see this if you think tools are purely functional.**

### Why I Saw It

I came to software development with a philosophical background. I'd spent years thinking about:
- How tools shape users (Ivan Illich, "Tools for Conviviality")
- How symbolic forms structure perception (Ernst Cassirer)
- How metaphors create ontologies (Owen Barfield)
- How technology encodes worldviews (Lewis Mumford, James C. Scott)

**So when the MCP version felt "flat," I had a framework to diagnose why:**

The tool names were purely functional. Generic. They carried no symbolic weight. Every invocation was bureaucratic noise rather than conceptual reinforcement.

**The CLI pivot was obvious from that perspective.**

But for most developers—trained to think about functionality, not symbolic weight—it would be invisible.

---

## The Meta-Insight: Context Design is Interface Design

We obsess over interface design:
- API ergonomics
- CLI argument structure
- Error message clarity
- Documentation organization

**But we ignore the interface that matters most for AI collaboration: the accumulated context.**

### Traditional Interface Design

**Goal:** Make it easy for humans to understand and use the tool

**Optimization targets:**
- Discoverability (can users find features?)
- Learnability (how quickly can users become proficient?)
- Efficiency (how fast can users accomplish tasks?)
- Error prevention (how do we guide users away from mistakes?)

### Context Design for AI

**Goal:** Shape what accumulates in the LLM's attention to improve reasoning quality

**Optimization targets:**
- **Semantic weight** (do repeated elements prime useful cognitive modes?)
- **Conceptual coherence** (do names reinforce the underlying methodology?)
- **Association alignment** (do cultural connotations match intended use?)
- **Cumulative reinforcement** (does repetition improve or degrade thinking?)

**These are orthogonal design dimensions.**

You can have excellent traditional interface design with terrible context design.

Or vice versa.

**The MCP → CLI pivot was choosing for context design over protocol standardization.**

---

## Practical Framework: Naming for Context Composition

Here's how to apply this when building tools for AI collaboration:

### Step 1: Identify Repeated Elements

**What will appear in context 10+ times per session?**
- Tool/command names
- Subcommand names
- File paths
- Error codes
- Variable names in generated code
- Documentation section headers

**Everything on this list is a context design opportunity.**

### Step 2: Choose for Semantic Weight

**For each repeated element, ask:**
- What associations does this name carry?
- What cognitive mode does it prime?
- Does repetition reinforce or dilute meaning?
- Would seeing this 20 times improve or degrade reasoning?

**If the answer is "degrade" or "neutral," reconsider the name.**

### Step 3: Test Empirically

**Names aren't chosen by philosophy alone—validate in practice:**

Try alternative names in real sessions. Observe whether:
- Output quality changes
- Reasoning style shifts
- Methodology adherence improves
- Problem-framing becomes clearer

**Choose names that measurably improve outcomes.**

### Step 4: Iterate on Context Composition

**This isn't a one-time decision—it's an ongoing optimization:**

As you use the tool:
- Notice which names appear most frequently
- Identify which context elements seem most influential
- Experiment with refinements
- Update based on observed effects

**Context design compounds over time, just like traditional interface design.**

---

## Connection to Earlier Articles in This Series

### Part 1: Cognitive Architecture

From [LLM Cognition Theory](LLM%20Cognition%20Theory.md), we explored how LLMs have distinct cognitive modes (Research, Discovery, Execution) and can chain them in meta-modes.

**Context composition reinforces mode-switching:**
- Seeing "hegel start discovery" primes exploratory thinking
- Seeing "hegel start execution" primes systematic delivery
- The **tool name + mode name** combination encodes the cognitive state

**Names aren't just labels—they're mode activation triggers.**

### Part 2: Cargo-Culting Human Limitations

From [Cargo-Culting Human Limitations](Cargo-Culting%20Human%20Limitations.md), we saw how LLMs inherit constraints they don't actually have.

**Tool names can reinforce or counteract cargo-culting:**
- Generic names ("workflow-manager," "task-runner") reinforce bureaucratic patterns
- Philosophically-weighted names ("hegel," "dialectic") prime more ambitious thinking
- **The choice of name affects whether the AI defaults to human-scale thinking or remembers its actual capacity**

### Part 3: Guidance Vectors

From [Guidance Vectors in Practice](Guidance%20Vectors%20in%20Practice.md), we explored how compact phrases compress philosophical principles.

**Tool names are guidance vectors that compound through repetition:**
- LEXICON vectors appear in guides: "Artifacts are disposable, clarity is durable"
- Tool names appear in every command: "hegel start," "hegel next," "hegel status"
- **Both create semantic scaffolding through accumulated context**

The difference is frequency: vectors might appear 2-3 times per session, while tool names appear 15-25 times.

**Tool names are the highest-frequency guidance vectors in your system.**

---

## Advanced Application: The Hegel LEXICON Integration

There's a deeper pattern here worth exploring.

**Hegel doesn't just rely on its own name for context composition.**

When Hegel injects writing guides into workflow prompts, those guides contain **guidance vectors from the LEXICON:**

```yaml
# workflows/discovery.yaml
nodes:
  spec:
    prompt: |
      You are in the SPEC phase of Discovery Mode.

      {{SPEC_WRITING}}

      Remember:
      - Artifacts are disposable, clarity is durable
      - Domain language over implementation details
      - What's the actual constraint?
```

**Every phase transition injects both:**
1. The workflow guide (SPEC_WRITING.md, PLAN_WRITING.md, etc.)
2. Relevant LEXICON vectors

**So the context accumulates:**
- Tool name: "hegel" (15-25 times per session)
- LEXICON vectors: "Artifacts are disposable, clarity is durable" (3-5 times per session)
- Workflow language: "thesis, antithesis, synthesis" (implicit in dialectical framing)

**All three layers compound to create semantic scaffolding.**

The tool name primes dialectical thinking. The lexicon vectors reinforce methodology principles. The workflow guides provide specific phase context.

**This is context composition by design, not accident.**

---

## Why the MCP → CLI Pivot Mattered

Let me bring this full circle.

**The MCP approach was functionally correct:**
- Standard protocol
- Clean tool abstractions
- Proper separation of concerns
- Would work with any MCP-compatible client

**But it failed at context composition:**
- Generic tool names hidden from user/AI view
- No repeated semantic reinforcement
- Bureaucratic framing (client-server, request-response)
- **Output quality suffered as a result**

**The CLI approach prioritized context composition:**
- Tool name visible and repeated in every interaction
- Philosophically-weighted name ("hegel")
- Systematic command structure (start/next/status)
- File paths reinforcing identity (.hegel/)
- **Output quality improved measurably**

**The pivot wasn't about features—it was about optimizing for what matters most in AI collaboration: the accumulated context.**

---

## Implications Beyond Hegel

This pattern applies to **any tool used in AI collaboration.**

### For CLI Tools

Choose names that:
- Carry cultural/philosophical weight aligned with the tool's purpose
- Prime the cognitive mode you want activated
- Won't feel silly/pretentious when repeated 20+ times

### For APIs

Design endpoints and methods with:
- Semantically-weighted names over generic CRUD
- Domain language that reinforces methodology
- Error messages that guide thinking, not just report failures

### For Libraries

Choose:
- Function names that encode meaning, not just actions
- Variable names that prime conceptual thinking
- Type names that clarify ontology

### For Documentation

Write with awareness that:
- AI will read this repeatedly
- Language choices compound through repetition
- Conceptually-weighted terms improve reasoning
- Generic/bureaucratic language degrades it

**In every case: names are not just labels—they're repeated semantic signals shaping how problems are understood and solutions are generated.**

---

## The Deeper Pattern: Tools Encode Thinking

Here's the uncomfortable truth:

**You can't separate a tool's functionality from its symbolic weight.**

Every tool **teaches a way of thinking** through repeated use:
- Git teaches distributed version control **and** a model of collaborative work
- Unix pipes teach composition **and** a philosophy of simple, focused tools
- Spreadsheets teach tabular thinking **and** a worldview where everything is a number in a cell

**The same is true for AI collaboration tools.**

When you choose to build an MCP server vs. a CLI:
- You're not just choosing a technical architecture
- You're choosing what will accumulate in the LLM's context
- **You're choosing which cognitive patterns get reinforced**

When you name your tool "Hegel" vs. "workflow-manager":
- You're not just choosing branding
- You're choosing what associations activate 20 times per session
- **You're choosing which mode of thinking gets primed**

**This is unavoidable.**

The only question is: **Do you choose intentionally or accidentally?**

---

## Closing: Context is King

We pivoted from MCP to CLI because **context composition matters more than protocol standardization** for AI collaboration tools.

**The lesson isn't "CLIs are better than MCP."**

The lesson is: **Context design is a first-class design dimension that most developers don't even know exists.**

Every repeated element in an AI collaboration session—tool names, command names, file paths, error messages, variable names, documentation language—is an opportunity to shape thinking through accumulated semantic weight.

**You can optimize for this intentionally, or let it happen accidentally.**

But you can't avoid it.

**Names are guidance vectors. Repetition compounds effects. Context is king.**

Choose accordingly.

---

**Related:**
- [Part 1: LLM Cognition Theory](LLM%20Cognition%20Theory.md) - Cognitive modes and meta-modes
- [Part 2: Cargo-Culting Human Limitations](Cargo-Culting%20Human%20Limitations.md) - What LLMs think they can't do
- [Part 3: Guidance Vectors in Practice](Guidance%20Vectors%20in%20Practice.md) - Compression algorithms for philosophy
- [Hegel CLI Documentation](../../src/practice/hegel-cli.md) - The tool itself
- [Guidance Vectors (Original)](Guidance%20Vectors.md) - Theoretical foundation

---

*This post documents the MCP → CLI pivot during Hegel CLI development and extracts principles about context composition as a design surface for AI collaboration tools. The insights emerged from practical observation: measurable output quality differences between architecturally-equivalent implementations that differed primarily in what accumulated in context.*
