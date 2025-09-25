# Toy‑Model Rationale

_Toy models are scientific experiments, not products. Their purpose is to learn, reduce risk, and sharpen architectural clarity—not to ship._

---

## What Toy Models Are

- **Focused experiments**: Each toy validates a single technical idea.  
- **Cheap and discardable**: Code is expendable; insight is what matters.  
- **Architectural probes**: They test assumptions, reveal edge cases, and expose integration challenges.  
- **Learning accelerators**: Fast cycles of building, testing, and documenting.  

## What Toy Models Are Not

- Not production systems  
- Not comprehensive solutions  
- Not sacred code to preserve  
- Not shortcuts to “done”  

---

## The Toy Model Cycle

### 1. Specification (SPEC.md)
Define the experiment before you run it.  

- Data structures, operations, and expected behaviors  
- Edge cases and failure conditions  
- Clear success criteria  

### 2. Planning (PLAN.md)
Lay out the steps like a recipe.  

- Sequence of test-first steps  
- Risks and dependencies  
- What to validate at each stage  

### 3. Implementation
Run the experiment under strict discipline.  

- Write failing tests first  
- Add only enough code to make them pass  
- Capture errors clearly and specifically  
- Stop when the hypothesis is validated  

### 4. Learning Extraction (LEARNINGS.md)
Distill the insight.  

- What worked, what failed  
- Patterns worth reusing  
- Integration implications  
- Strategic takeaways  

---

## Exit Criteria

- All step-level success criteria checked  
- Insights recorded  
- Follow-up scope cut  

---

## Guiding Principles

- **Test-Driven Development is mandatory**  
  The red-green cycle keeps experiments honest, forces clarity, and documents usage.  

- **Error messages are for humans and AIs**  
  Be specific, actionable, and structured. Good errors guide both debugging and future automation.  

- **Event sourcing is your microscope**  
  Record every operation so you can replay, inspect, and debug how state evolved.  

- **Minimal dependencies, maximum clarity**  
  Use proven libraries, avoid frameworks, keep the system transparent.  

- **Export in multiple formats**  
  JSON for state, DOT for graphs, CSV for tabular views. Make insights portable.  

---

## Strategic Guidance

- Pivot early when better approaches appear; persist when the gain is marginal.  
- Preserve learnings even when abandoning code.  
- Keep APIs clean and data formats consistent across toys.  
- Discard code without guilt—the artifact that matters is the documentation of insight.  

---

## North Star

Toy models are **gardening, not construction**.  
You’re cultivating understanding, not building monuments.  
The point is clarity, not permanence.  

---

## Toy Integration Convention

- Each toyN_* directory must contain exactly one SPEC.md, PLAN.md, and LEARNINGS.md.  
- If a SPEC or PLAN grows too large or unfocused, split scope into new toyN_* experiments.  
- Integration toys (e.g. toy5_*, toy6_*) exist to recombine validated sub-toys.  
- Replace in place: update LEARNINGS.md rather than creating multiples for the same toy.  
- When consolidating, fold prior learnings into a single current doc; discard stale versions.  
- Always bias toward minimal scope: smaller toys, fewer docs, clearer insights.  

---

## Axis Principle for Toy Models

- A base toy isolates exactly one axis of complexity (a single invariant, mechanism, or seam).  
- An integration toy merges exactly two axes to probe their interaction.  
- Never exceed two axes per toy; more belongs to higher‑order integration or production scope.  
- This discipline keeps learnings sharp, avoids doc bloat, and mirrors controlled experiments.  
