# Spec Writing

This chapter provides agent-oriented documentation for writing SPEC.md files in DDD projects. Drop this guide into your repository as `SPEC_WRITING.md` to help AI agents understand how to create precise behavioral contracts for toy models.

---

```markdown
# SPEC_WRITING.md

## Purpose

A **SPEC.md is a contract spike**: it defines what the system must accept, produce, and guarantee.  
It exists to make implementation falsifiable — to ensure tests and validation have clear ground truth.

---

## What a SPEC.md Is / Is Not

### ❌ Not

- Implementation details (classes, functions, algorithms)
- Internal design notes (unless exposed in the contract)
- Tutorials, manuals, or user guides
- Vague aspirations ("the system should work well")

### ✅ Is

- Precise input/output formats
- Defined state transitions or invariants
- Operation semantics (commands, APIs, behaviors)
- Error and validation rules
- Concrete test scenarios and acceptance criteria

---

## Core Structure

### 1. Header
Toy Model N: [System Name] Specification

One-line purpose statement

### 2. Overview

- **What it does:** core purpose in 2–3 sentences
- **Key principles:** 3–5 bullets on design philosophy
- **Integration context:** if relevant, note inputs/outputs to other toys

### 3. Data Model
Define external data formats with **realistic examples**:

- All required fields shown
- Nested structures expanded
- Field purposes explained
- JSON schemas when clarity demands

### 4. Core Operations
Document commands or APIs with a consistent pattern:

- **Syntax** (formal usage)
- **Parameters** (required/optional, ranges, defaults)
- **Examples** (simple + complex)
- **Behavior** (state changes, outputs, side effects)
- **Validation** (rules, errors, edge cases)

### 5. Test Scenarios
3 categories:

1. **Simple** — minimal case
2. **Complex** — realistic usage
3. **Error** — invalid inputs, edge handling  
Optionally, **Integration** — only if toy touches another system.

### 6. Success Criteria
Checkboxes phrased as falsifiable conditions, e.g.:

- [ ] Operation X preserves invariant Y
- [ ] Error messages are structured JSON
- [ ] Round-trip import/export retains labels

---

## Quality Heuristics

High-quality SPECs are:

- **Precise** — eliminate ambiguity
- **Minimal** — only cover one axis of complexity
- **Falsifiable** — every statement testable
- **Contextual** — note integration points when they matter

Low-quality SPECs are:

- Vague ("system processes data")
- Over-prescriptive (dictating implementation)
- Bloated with internal details
- Missing testable criteria

---

## Conclusion

A SPEC.md is not a design novel.
It is a **minimal, precise contract** that locks in what must hold true, so tests and implementations can be judged unambiguously. If multiple axes of complexity emerge, split them into separate toy models.
```
