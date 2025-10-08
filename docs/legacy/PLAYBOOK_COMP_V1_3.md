# PLAYBOOK Comparison — Versions 1, 2, and 3

This document compares the three playbook versions in `docs`:
- `PLAYBOOK.md` (V1)
- `PLAYBOOK_V2.md` (V2)
- `PLAYBOOK_V3.md` (V3)

It summarizes scope, structure, tone, and coverage; highlights overlaps, gaps, and redundancies; and recommends a synthesis path.

---

## Scope & Method

- Read all three files in full and extracted their headings and themes.
- Focused on: structure, breadth of topics, depth of guidance, tone, and domain neutrality.
- No extrapolation beyond the content of these files and the supporting generalized docs.

---

## One‑Paragraph Summaries

- V1 (`PLAYBOOK.md`): The most comprehensive and procedural. Covers principles, DDD loop, meta‑docs, Napkin Physics, Toy Models, CLI+JSON debugger, pipelines/golden tests, planning/testing, guardrails/self‑audit, heuristics, adoption, and appendices (templates/checklists/conventions). Emphasizes “why this matters” callouts.
- V2 (`PLAYBOOK_V2.md`): Concise and agent‑centric. Defines DDD philosophy, core principles, a primitive→integration loop, the four meta‑docs, Napkin Physics, Toy Models, and a brief genealogy. Most compact; light on implementation detail.
- V3 (`PLAYBOOK_V3.md`): Doctrinal and narrative. Clarifies purpose, principles, loop, Napkin Physics, Toy Models, JSON+CLI convention, integration path, roles, and philosophy. Balanced middle ground: clearer narrative than V2; less procedural depth than V1.

---

## Structure Comparison

- V1 sections (13): Preface; Core Principles; DDD Loop; Meta‑Docs; Napkin Physics; Toy Models; CLI+JSON Contract; Pipelines & Golden Tests; Planning & Testing; Guardrails & Self‑Audit; Heuristics & Anti‑Patterns; Adoption Guide; Appendices (templates/checklists/schemas/glossary).
- V2 sections (7): Purpose & Audience; Core Principles; Development Loop; Meta‑Docs; Napkin Physics; Toy Models; Methodological Genealogy.
- V3 sections (9): Purpose; Core Principles; DDD Loop; Napkin Physics; Toy Models; JSON+CLI Convention; Integration & Final System; Roles; Philosophy.

Observations:
- V1 is exhaustive and operational; V2 is minimal and philosophical; V3 is doctrinal with a clean integration narrative.
- Only V1 explicitly covers guardrails, self‑audit, planning/testing detail, adoption patterns, and templates.
- Only V2 includes a short “genealogy” (influences). Only V3 includes roles and an explicit final‑system framing.

---

## Coverage Matrix (Topics → Versions)

- Core principles: V1, V2, V3
- DDD loop: V1, V2, V3
- Meta‑docs (SPEC/PLAN/LEARNINGS/README): V1 (detailed), V2 (brief), V3 (brief)
- Napkin Physics: V1, V2, V3
- Toy Models (axis/integration discipline): V1, V2, V3
- CLI + JSON (contract/convention): V1 (detailed), V3 (convention), V2 (mentions legibility)
- Pipelines & golden tests: V1 (detailed), V3 (implied via JSON+CLI legibility)
- Planning & testing (unit/golden/contract/snapshot): V1 only
- Guardrails & self‑audit (deps, complexity, security, metrics, review gates): V1 only
- Heuristics & anti‑patterns: V1 only
- Adoption guide & repo layout: V1 only
- Roles (agent/human): V3 only
- Genealogy (influences): V2 only

---

## Tone & Style

- V1: Practical and procedural. Many lists and checklists, explicit contracts and patterns, plus “Why this matters” callouts. Strong operational utility; denser to read.
- V2: Brief, agent‑centered, “rules of thumb” oriented. Most skimmable; assumes context; may leave implementers wanting more.
- V3: Narrative doctrine with clear purpose and philosophy. Readable and motivating; moderate implementation guidance.

---

## Strengths & Weaknesses

- V1 Strengths: Most complete; actionable; includes testing, guardrails, self‑audit, and templates. Good for execution and review.
- V1 Weaknesses: Dense; risks overwhelming newcomers; needs narrative framing to avoid feeling purely prescriptive.

- V2 Strengths: Compact; easy to keep in working memory; emphasizes agent orientation and parsimony.
- V2 Weaknesses: Lacks operational depth (testing, guardrails, adoption); genealogy is interesting but not directly actionable.

- V3 Strengths: Clear doctrine; crisp articulation of integration path; defines roles and final‑system orientation; establishes JSON+CLI as a legibility convention.
- V3 Weaknesses: Less explicit about pipelines, testing strategy, and guardrails; fewer concrete checklists/templates.

---

## Redundancies & Gaps

Redundancies (safe to unify once):
- Core principles, DDD loop, Napkin Physics, Toy Models appear in all versions (wording differs).

Gaps (present only in one version):
- V1‑only: planning/testing specifics; guardrails and self‑audit; pipelines + golden tests detail; adoption guide; templates/checklists.
- V2‑only: methodological genealogy.
- V3‑only: roles; explicit integration path to final system; concise JSON+CLI convention.

---

## Best‑Of Synthesis (What to Keep)

- Keep V3’s narrative framing: purpose, philosophy, roles, two‑at‑a‑time integration toward the final system.
- Keep V1’s operational core: CLI+JSON contract; pipelines + golden tests; planning/testing; guardrails/self‑audit; heuristics; adoption guide; templates.
- Optionally keep V2’s short genealogy as a footnote/appendix (for context without distracting from operations).

Rationale:
- This yields a doc that is readable (V3) and executable (V1), without losing the concise origin context (V2).

---

## Recommendations

- Lead with a short doctrinal core (V3 tone): purpose, core principles, roles, the DDD loop, and the two‑at‑a‑time integration path.
- Follow with the operational chapters (V1 depth): CLI+JSON contract; pipelines & golden tests; planning/testing; guardrails/self‑audit; heuristics; adoption.
- Conclude with appendices (V1): templates, checklists, error JSON, pipeline pattern, glossary. Add the V2 genealogy as a brief note.
- Maintain “Why this matters” callouts (from V1) to connect advice to value.

---

## Suggested Final Outline (Merged)

1) Purpose & Principles (V3+V2 phrasing, consolidated)  
2) Roles & Responsibilities (V3)  
3) The DDD Loop (V1/V3)  
4) Napkin Physics (all, unified)  
5) Toy Models: Axes & Integration Discipline (all, unified)  
6) CLI + JSON: Contract & Conventions (V1 detail, V3 framing)  
7) Pipelines & Golden Tests (V1 detail)  
8) Planning & Testing (V1)  
9) Guardrails & Self‑Audit (V1)  
10) Heuristics & Anti‑Patterns (V1)  
11) Adoption & Repository Layout (V1)  
12) Appendices (V1) + Genealogy note (V2)  

---

## Decision Matrix (When Choosing Among Versions)

- Need a single doc to work from today: Start with V1; add V3’s Roles & Purpose section up front.
- Onboarding a new contributor/agent: Use V3’s doctrinal sections; link into V1’s operational chapters.
- Executive summary or presentation: Use V2 (compact) + one slide from V3 on integration discipline.

---

## Final Notes

- All three versions are domain‑agnostic and compatible; the choice is about depth vs. readability.
- The merged outline above reflects the smallest set that preserves V1’s execution utility and V3’s clarity, while keeping V2’s context minimal.

*** End of Comparison ***
