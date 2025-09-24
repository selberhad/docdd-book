# Toy Model Development Manifesto

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

## Patterns That Work

- **Single-class toys** for small, cohesive experiments.  
- **Module-based toys** when responsibilities split naturally.  
- **Adapter patterns** when integrating external systems (LLMs, APIs, etc.).  

---

## Testing Philosophy

- **Properties over examples**: Assert invariants that must always hold.  
- **Complex scenarios**: End-to-end tests that mimic real workflows.  
- **Error paths**: Failures should be tested as deliberately as successes.  

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