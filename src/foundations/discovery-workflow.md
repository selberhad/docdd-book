# Discovery Workflow

Discovery mode is DDD's approach for uncertain requirements, novel solutions, or exploratory work. Instead of optimizing for production code, discovery optimizes for **learning density**: extracting architectural insights, validating assumptions, and discovering constraints as efficiently as possible.

Use discovery mode when you're working with unfamiliar technology, exploring solution spaces, or building foundational components where the right approach isn't yet clear. The output isn't production-ready code—it's validated insights that inform how to build the real thing.

**Relationship to Research mode:** Discovery often follows Research mode (external knowledge gathering), validating documented theory through hands-on experiments. In Learning meta-mode, Discovery and Research alternate as experiments reveal new questions requiring study. See [Research Workflow](./research-workflow.md) and [Meta-Modes](./meta-modes.md).

Discovery mode uses a **learning-first approach** built around four core documents that form an integrated harness for systematic experimentation.

## The Learning-First Approach

Discovery mode inverts typical development: learning is the goal, code is the tool to extract it.

Traditional development starts with solutions and ends with documentation. Discovery starts with questions and ends with answers. The process centers on **LEARNINGS.md as both roadmap and artifact**:

**Begin with questions:**
- What do we need to learn about this problem space?
- What decisions must we make before production?
- Which assumptions need validation?

**Iterate to discover:**
- Build minimal experiments (toy models) to answer specific questions
- Update LEARNINGS.md continuously as insights emerge
- Treat code as disposable; insights are the durable output

**End with answers:**
- What held? What failed? Why?
- Which patterns are ready for production?
- What constraints did we discover?

This disciplined approach ensures you're always learning efficiently, not building prematurely.

## The Four-Document Harness

The four core artifacts form a harness system that guides AI agents while preserving human control:

- **SPEC.md** — *The bit: precise contract keeping the pull straight*
  - **Purpose:** Comprehensive behavioral contract for the current scope
  - **Must contain:** Input/output formats, invariants, internal state shapes, operations, validation rules, error semantics, test scenarios, success criteria

- **PLAN.md** — *The yoke: aligns effort into test-first steps*
  - **Purpose:** Strategic roadmap using Docs → Tests → Implementation cadence
  - **Must contain:** What to test vs. skip, order of steps, timeboxing, dependencies, risks, explicit success checkboxes per step

- **LEARNINGS.md** — *The tracks AND the compass: where you've been and where to go*
  - **Purpose (dual role):**
    - **Roadmap:** Define learning goals and open questions upfront
    - **Artifact:** Capture architectural insights, pivots, fragile seams, production-ready patterns
  - **Must contain:**
    - What we need to learn (goals)
    - What held, what failed, why (results)
    - Portable patterns for production (extraction)
  - **Status:** Required in discovery mode (central organizing document)

- **README.md** — *The map: concise orientation for integration*
  - **Purpose:** 100–200 words context refresh on library functionality
  - **Must contain:** Header + one-liner, 2–3 sentence purpose, 3–5 essential method signatures, core concepts, gotchas/caveats, representative test path

Together these artifacts let the human act as driver, ensuring the cart (implementation) moves forward under control, with clarity preserved and ambiguity eliminated.

## Discovery Cycle

The discovery workflow follows four sequential phases:

**1. Documentation**
- Define learning goals in LEARNINGS.md (what questions to answer)
- Generate or update SPEC.md and PLAN.md for the current, minimal slice of scope
- Keep README.md for any touched library crisp and current

**2. Tests**
- Derive executable tests (or rubrics) directly from SPEC.md
- Golden examples and negative/error-path cases are required

**3. Implementation**
- Build minimal code to pass tests and answer learning questions
- Prefer single-file spikes for first proofs
- Keep changes tightly scoped

**4. Learnings**
- Update LEARNINGS.md with what held, what failed, why, and next constraints
- Extract portable patterns ready for production use
- Identify follow-up questions or declare learning goals complete

The cycle repeats until all learning goals are met and patterns are validated.

## Supporting Practices

These practices strengthen discovery work by encouraging simplicity, focus, and inspectable behavior.

### Napkin Physics — Why Start Simple

Before writing SPEC.md and PLAN.md, use Napkin Physics to force parsimony and avoid premature complexity.

**The practice:** Treat the problem like physicists with a napkin—capture just the essentials:
- Problem (one sentence)
- Assumptions (3-5 bullets)
- Invariant/Contract (one precise property)
- Mechanism (≤5 bullets, single-file spike, minimal deps)
- First Try (one paragraph describing simplest path)

**Why it helps discovery:**
- Prevents over-engineering before you understand the problem
- Enforces deletion: no new layers/nouns without removing two elsewhere
- Gives you a minimal starting point to test assumptions against reality
- Makes it easy to throw away and restart when you learn something fundamental

Napkin Physics is upstream simplification—it keeps you from building elaborate solutions to problems you don't yet understand.

See: [Napkin Physics](./napkin-physics.md)

### Toy Models — Why Isolate Experiments

Toy models are small, sharply-scoped experiments designed to answer specific questions. Unlike prototypes, they're kept as reference artifacts after completion.

**The practice:**
- Build minimal implementations in isolated directories (toys/, experiments/)
- Each toy isolates exactly **one axis of complexity**:
  - **Base toys** test a single primitive (one invariant, mechanism, or seam)
  - **Integration toys** test integration between de-risked primitives (integration is the single axis)
- Follow full cycle: SPEC → PLAN → Tests → Minimal Impl → LEARNINGS
- Retain in repository as intermediate artifacts documenting the discovery process

**Why it helps discovery:**
- Validates assumptions cheaply before committing to production architecture
- Isolates complexity so you can reason about one problem at a time
- Feeds direct, falsifiable evidence into LEARNINGS.md
- Provides reference implementations when porting patterns to production
- Integration toys test "do these work together?" after primitives are already validated

**Key principle:** Every toy addresses exactly one source of uncertainty. Base toys validate primitives. Integration toys validate that de-risked primitives compose correctly. The primitives are no longer uncertain, so integration is the single remaining axis.

Toy models are controlled experiments. They answer: "Does this approach actually work?" before you build it for real.

See: [Toy-Model Rationale](./toy-model-rationale.md)

### CLI + JSON Debugger — When Inspectable Behavior Helps

**Applicability:** This pattern fits data pipelines, transformation tools, and CLI-based systems. Many projects (web apps, GUIs, embedded systems, real-time software) won't match this model—that's expected and fine.

**The practice (when applicable):**
- Expose functional modules as pure CLIs with JSON stdin/stdout
- Use structured error JSON on stderr
- Build systems as composable pipelines: `modA < in.json | modB | modC > out.json`

**Why it helps discovery (when it fits):**
- Enables single-stepping: run each transformation independently to inspect intermediate state
- Makes failures falsifiable: exact inputs that trigger errors are trivial to capture and replay
- Supports bisecting: when a pipeline breaks, binary search which stage failed
- Golden tests become trivial: save input/output JSON pairs as fixtures
- Both humans and AI agents can reason about behavior mechanically

**When to use:** If your discovery work involves data transformations, parsers, formatters, or stateless operations, CLI+JSON provides a low-friction debugging substrate. If not, skip it—there are other ways to make behavior inspectable.

See: [Debugger Mindset](./debugger-mindset.md)

### Repo Layout & Guardrails — Why Constrain Experiments

Even exploratory work benefits from lightweight structure and constraints.

**Layout principles:**
- Clear locations for experiments (toys/, experiments/), documentation, tests
- Each toy directory contains its own SPEC.md, PLAN.md, LEARNINGS.md, README.md

**Guardrails that aid discovery:**
- Dependency constraints: default to stdlib; justify any additions in SPEC.md
- Complexity limits: single-file spikes ≤120 lines when feasible; functions ≤25 lines
- Error handling: implement top 2 failure modes; others raise clear structured errors
- No more than two new abstractions per experiment

**Why it helps discovery:**
- Constraints force clarity: if you can't express it simply, you don't understand it yet
- Small scopes = fast iteration = more learning per hour
- Self-audit metrics reveal when experiments are growing too complex
- Structured errors make failures informative instead of mysterious

Discovery thrives on disciplined constraints. They're not bureaucracy—they're feedback mechanisms that surface when you're exploring unproductively.

See: [General Practices](./general-practices.md)

---

**Examples in Practice**:

[Case Study II: Spatial MUD Database](../patterns/spatial-mud-database.md) demonstrates discovery workflow in action, showing how toy model discipline and systematic experimentation addressed complex technical challenges through four focused prototypes and multi-system integration.

[Case Study IV: NES Development](../patterns/ddd-nes.md) shows Research ↔ Discovery ping-pong (Learning meta-mode), where systematic wiki study catalogs questions, Discovery validates theory through test ROMs, and findings update external knowledge documents.
