# Plan Writing

This chapter provides agent-oriented documentation for writing PLAN.md files in DDD projects. Drop this guide into your repository as `PLAN_WRITING.md` to help AI agents create strategic roadmaps for toy model implementation.

---

```markdown
# PLAN_WRITING.md

## What a PLAN.md Actually Is

A **PLAN.md is a strategic roadmap** describing **what to build and how to build it step-by-step**. It enforces clarity, sequencing, and validation.

### ❌ NOT:

- Implementation code
- Literal test code
- Copy-paste ready
- Exhaustive details

### ✅ IS:

- Stepwise development roadmap
- TDD methodology guide
- Illustrative code patterns only
- Success criteria with checkboxes

---

## Structure

### Header

- **Overview**: Goal, scope, priorities
- **Methodology**: TDD principles; what to test vs. not test

### Step Template

    ## Step N: <Feature Name> **<PRIORITY>**

    ### Goal
    Why this step matters

    ### Step N.a: Write Tests

    - Outline test strategy (no literal code)
    - Key cases: core, error, integration
    - Expected validation behavior

    ### Step N.b: Implement

    - Tasks: file/module creation, core ops, integration
    - Code patterns for illustration only
    - State and error handling guidance

    ### Success Criteria

    - [ ] Clear, testable checkpoints
    - [ ] Functional + quality standards met

---

## Key Practices

### TDD Discipline

- Write failing tests first
- Red → Green → Next
- Focus on interfaces and contracts
- Cover error paths explicitly

### Test Scope

- ✅ Test: core features, errors, integration points
- ❌ Skip: helpers, edge cases, perf, internals

### Code Patterns
Use examples as **patterns**, not literal code:

    cmdWalk(cells, direction) {
        if (!(direction in DIRECTIONS)) throw Error(`Invalid: ${direction}`);
        const [dx, dy] = DIRECTIONS[direction];
        this.cursor.x += cells * dx; this.cursor.y += cells * dy;
    }

### Tasks
Break implementation into minimal units:

    1. Create directory/files
    2. Implement core command parsing
    3. Add integration test path
    4. Error handling

### Success Criteria
Always check with concrete, objective boxes:

- [ ] Parser initializes cleanly  
- [ ] Commands mutate state correctly  
- [ ] Errors raised for invalid input  
- [ ] Test suite runs with single command  

---

## Anti-Patterns

- ❌ Full test code in Plan (use bullet outlines)
- ❌ Full implementation code (use patterns only)
- ❌ Over-detail (Plan guides, does not replace dev thinking)

---

## Why This Works

- **Clear sequencing**: prevents scope drift  
- **TDD enforcement**: quality-first mindset  
- **Concrete validation**: objective step completion  
- **Minimal guidance**: gives direction without over-specifying  

---

## Conclusion
A good PLAN.md is a **map, not the territory**. It sequences work, enforces TDD, and defines success. It avoids detail bloat while ensuring implementers know exactly **what to test, what to build, and when it's done**.
```