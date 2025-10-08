# FINAL Comparison — PLAYBOOK V1–V6 (V6 as Canon)

This document treats `PLAYBOOK_V6.md` as the canonical doctrine and compares earlier drafts (V1–V5) against it using directional tags:
- REPUDIATED: dropped as incorrect or counter‑productive
- SOFTENED: kept but de‑emphasized or trimmed
- REFRAMED: kept but expressed differently for clarity/fit
- ELEVATED: made more central/explicit than before
- PRAGMATIZED: turned from rule/ideal into context‑dependent guidance

It also includes a Wrongness Register for V1: concepts that conflict with V6’s principles of parsimony, legibility, determinism, two‑at‑a‑time integration, and the human spotter role.

---

## Method

- Read V6 fully and treated its principles as ground truth.
- Read V1–V5 and mapped major concepts to V6 outcomes.
- Only content present in the drafts was used; no extrapolation beyond the docs.

---

## V1 → V6 (Directional Changes)

- PRAGMATIZED: CLI+JSON as default substrate → “use when it makes sense” (V6 notes pipelines/CLI composition should be applied when they increase clarity/legibility).
- SOFTENED: Pipelines as execution traces (detailed, prescriptive in V1) → concise mention with appropriateness caveat in V6.
- SOFTENED: Guardrails/self‑audit (long metric/checklist blocks in V1) → concise habits and heuristics in V6.
- SOFTENED: Adoption/repo layout (explicit structure in V1) → omitted in V6 (assumed or deferred).
- REFRAMED: DDD loop (V1 operational) → V6 loop includes README explicitly and cross‑links to meta‑doc guides.
- ELEVATED: Two‑at‑a‑time integration discipline (present as “never exceed two axes” in V1) → a core doctrine in V6 and enforced via kickoff.
- ELEVATED: Human spotter role (implicit in V1 via review gates) → explicit “Agent/Human” roles section in V6.

---

## V2 → V6 (Directional Changes)

- ELEVATED: Roles (V2 lacks explicit roles) → V6 adds Agent/Human spotter clarity.
- REFRAMED: Minimal doctrine and genealogy (V2) → V6 keeps doctrine, drops genealogy.
- ELEVATED: Binary‑weave kickoff absent in V2 → central in V6.

---

## V3 → V6 (Directional Changes)

- ELEVATED: Binary‑weave kickoff (not explicit in V3) → explicit in V6.
- PRAGMATIZED: JSON+CLI convention (V3 suggests broadly) → V6 adds “use when it makes sense.”
- ELEVATED: README in loop (V6 names it in the loop and links guides).

---

## V4 → V6 (Directional Changes)

- REFRAMED: Binary‑weave kickoff (full template in V4) → retained but overall doc tightened in V6.
- PRAGMATIZED: Pipelines/CLI emphasis (strong in V4) → “when it makes sense” in V6.
- SOFTENED: Templates and repo layout pointers (V4) → less prominent/omitted in V6.

---

## V5 → V6 (Directional Changes)

- REFRAMED: Streamlined kickoff (V5) → similar in V6 with even tighter doctrine.
- PRAGMATIZED: Adds explicit note in V6 that pipelines/CLI composition are optional based on fit.
- REFRAMED: Roles/Templates organization (V5) → V6 integrates roles in doctrine and references meta‑doc guides inline.

---

## Wrongness Register (V1 vs V6 Principles)

For each V1 concept that doesn’t align with V6’s principles, we note the tag, why it’s wrong under V6, and its replacement in V6.

- Concept: Pipelines as universal execution substrate
  - Tag: PRAGMATIZED
  - Why wrong: Violates parsimony when enforced universally; not all projects benefit equally.
  - V6 Replacement: Pipelines & CLI composition “used when it makes sense” (legibility/benefit‑driven).

- Concept: Extensive prescriptive checklists for guardrails/self‑audit
  - Tag: SOFTENED
  - Why wrong: Over‑specifies; reduces parsimony and obscures the core signals.
  - V6 Replacement: Concise habits and heuristics; focus on constraints and a few key practices.

- Concept: Detailed adoption & repository layout as mandated pattern
  - Tag: SOFTENED
  - Why wrong: Over‑constrains structure; can conflict with parsimony and context‑fit.
  - V6 Replacement: Omitted layout mandates; rely on doctrine + guides; let context dictate structure.

- Concept: Implicit reviewer role without explicit “spotter” framing
  - Tag: ELEVATED
  - Why wrong: Weakens the human‑in‑the‑loop model; unclear boundaries dilute legibility of process.
  - V6 Replacement: Explicit roles section (Agent drives; Human acts as spotter/judgment).

- Concept: Implicit/loose integration discipline (integration toys recombine sub‑toys)
  - Tag: ELEVATED / REFRAMED
  - Why wrong: Lacks strict sequencing; risks combinatorial drift against determinism.
  - V6 Replacement: Binary‑Weave Kickoff — strict alternation (one new primitive → integrate with current product) and two‑at‑a‑time rule.

- Concept: CLI+JSON as a de facto mandate
  - Tag: PRAGMATIZED
  - Why wrong: Can reduce parsimony; determinism/legibility need not require CLI+JSON in every case.
  - V6 Replacement: JSON+CLI as a convention; apply when it increases legibility and debuggability.

- Concept: Over‑detailed “Why this matters” everywhere
  - Tag: SOFTENED
  - Why wrong: Adds verbosity and can obscure doctrine; legibility prefers tight doctrine plus links.
  - V6 Replacement: Tighter doctrine with cross‑links to SPEC/PLAN/LEARNINGS/README guides.

---

## Bottom Line

- V6 narrows doctrine to parsimony, legibility, determinism, two‑at‑a‑time integration, and explicit human spotter role.
- Earlier drafts (especially V1) contributed valuable operational content but introduced bloat and over‑prescription. V6 retains the useful parts while reframing or softening the rest.
- The Binary‑Weave Kickoff is the major elevation from later drafts (V4–V6), ensuring disciplined integration and compounding clarity without combinatorial drift.

*** End of FINAL_COMP ***
