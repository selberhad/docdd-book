# PLAYBOOK.md — Dialectic-Driven Development (Agent-Oriented)

This playbook defines the methodology agents must follow when building software in this repository. It encodes **Dialectic-Driven Development (DDD)**: an AI-first approach that treats documentation and code as equally disposable artifacts, organizes work around toy models, and relies on clear, composable interfaces for debuggability.

---

## 1. Purpose and Audience

- **Purpose:** Provide agents with a repeatable process for clarity-first development.  
- **Audience:** AI agents participating in this repository. Humans serve as reviewers and constraint-setters.  
- **Use:** Keep this playbook in context while working. Every decision should be justifiable against these principles.

---

## 2. Core Principles

- **Docs First:** Every artifact begins with SPEC.md and PLAN.md.  
- **Toys as Units:** All work is done as toy models — small experiments meant to be thrown away once their insights are captured.  
- **One Axis at a Time:** Each toy isolates one dimension of complexity. Integration toys may combine *two* at a time.  
- **Disposable Intermediates:** Code and docs are cheap and discardable until the final assembly. Learnings are durable.  
- **Agent-Oriented:** Humans lean on intuition, aesthetics, GUIs, and tacit knowledge. Agents lean on explicit contracts, JSON, determinism, and pipelines.  
- **Parsimony:** Prefer the simplest mechanism that works.  

---

## 3. Development Loop

1. **Primitive Discovery**  
   - Ask: *Do I need another primitive toy?*  
   - If yes: write SPEC.md, implement a toy, verify with tests, record learnings.  

2. **Integration Step**  
   - If no primitives remain: select the simplest two toys.  
   - Write SPEC.md for the integration.  
   - Implement as a new toy, verify by combining outputs.  

3. **Iteration**  
   - Repeat until all primitives and integrations have been merged into a single final assembly.  

---

## 4. Meta-Docs

Maintain four document types as the backbone of the loop:

- **README.md** — context refresh for a component.  
- **SPEC.md** — behavioral contract: I/O, invariants, test cases.  
- **PLAN.md** — roadmap: order of steps, risks, success criteria.  
- **LEARNINGS.md** — distilled insights that outlive discarded code.  

Both code and docs are cheap in intermediate stages; only learnings and the final assembly are durable.

---

## 5. Napkin Physics (Upstream Simplification)

The point is clarity, not structure. Before drafting, collapse the problem into its simplest form: a sentence problem statement, a few assumptions, one invariant, a minimal mechanism. The goal is to strip away excess and surface the essentials, so toys are framed around sharp, testable ideas.

---

## 6. Toy Models

**Definition:** Minimal experiments that do one thing clearly. They should speak in formats that make debugging easy (often CLI+JSON, but not always).  

**Cycle:** SPEC → PLAN → Tests → Toy → LEARNINGS.  

**Rules of thumb:**  
- A base toy isolates one axis.  
- An integration toy combines exactly two.  
- Interfaces should make state visible and reproducible.  

---

## 7. Methodological Genealogy

DDD borrows selectively:  
- **From TDD:** start with specifications before code.  
- **From DDD:** decompose into bounded contexts → here, toy models.  
- **From FP/Redux:** pure functions, no hidden state, explicit contracts.  
- **From UNIX philosophy:** “do one thing well” with composable tools.  
- **From Agile/XP:** progressive iteration and discardability.  

All adapted for **agents, not humans.**