# PLAYBOOK Comparison — Versions 1 through 6

This compares all six playbook drafts found in `docs`:
- V1: `PLAYBOOK_V1.md`
- V2: `PLAYBOOK_V2.md`
- V3: `PLAYBOOK_V3.md`
- V4: `PLAYBOOK_V4.md`
- V5: `PLAYBOOK_V5.md`
- V6: `PLAYBOOK_V6.md`

It summarizes scope, structure, tone, and coverage; highlights overlaps, gaps, and divergences; and recommends a best‑of synthesis path.

---

## Scope & Method

- Listed the docs directory and verified the presence of V1–V6 and the prior 1–3 comparison.
- Read V4–V6 fully; reviewed the existing V1–V3 comparison and cross‑checked against the source drafts.
- Focused on: structure, breadth of topics, depth of guidance, tone, domain neutrality, and contradictions.

---

## One‑Paragraph Summaries (V1–V6)

- V1 (`PLAYBOOK_V1.md`): Most comprehensive and procedural. Covers principles, DDD loop, meta‑docs, Napkin Physics, Toy Models, CLI+JSON debugger, pipelines/golden tests, planning/testing, guardrails/self‑audit, heuristics, adoption, and appendices (templates/checklists/conventions). Includes many “Why this matters” callouts.
- V2 (`PLAYBOOK_V2.md`): Compact, agent‑centric doctrine. DDD philosophy, core principles, primitive→integration loop, four meta‑docs, Napkin Physics, Toy Models, a brief genealogy. Skimmable; light on operational detail.
- V3 (`PLAYBOOK_V3.md`): Doctrinal narrative. Purpose, principles, loop, Napkin Physics, Toy Models, JSON+CLI convention, integration path, roles, philosophy. Clear integration discipline (two‑at‑a‑time), readable tone.
- V4 (`PLAYBOOK_V4.md`): Adds Binary‑Weave Kickoff to V3’s doctrine. Strict alternation: one new primitive → integrate with current product; sequential stages; end state. Retains concise operational chapters (CLI+JSON, pipelines/golden tests, planning/testing, guardrails/heuristics) and a kickoff template.
- V5 (`PLAYBOOK_V5.md`): Streamlined V4. Keeps binary‑weave center; compresses operational sections; adds Roles and Templates sections; emphasizes clarity of weave and JSON+CLI convention.
- V6 (`PLAYBOOK_V6.md`): Further tightened. Similar doctrine and kickoff; notes that pipelines/CLI composition should be used when it makes sense; includes README in the DDD loop and cross‑links to meta‑doc guides. Short, directive tone.

---

## Structure Comparison (What’s Covered Where)

- Core principles: V1, V2, V3, V4, V5, V6
- DDD loop: V1, V2, V3, V4, V5, V6 (V6 also lists README in the loop)
- Meta‑docs (SPEC/PLAN/LEARNINGS/README): V1 (detailed), V2/V3 (brief), V4/V5 (concise pointers), V6 (concise with cross‑links)
- Napkin Physics: V1, V2, V3, V4, V5, V6
- Toy models (axis/integration discipline): V1, V2, V3, V4, V5, V6
- Kickoff (Binary‑Weave): V4 (full), V5 (full), V6 (full); not in V1–V3
- CLI + JSON convention/contract: V1 (detailed), V3 (convention), V4/V5 (detailed/concise), V6 (concise)
- Pipelines & golden tests: V1 (detailed), V4 (detailed), V5 (concise), V6 (advises use when appropriate)
- Planning & testing specifics: V1 (detailed), V4 (concise), V5 (concise), V6 (concise)
- Guardrails, self‑audit, heuristics: V1 (detailed), V4 (concise), V5 (concise), V6 (concise)
- Adoption & repo layout: V1 (detailed), V4 (concise), V5 (templates), V6 (omits layout details)
- Roles (agent/human): V3, V5, V6
- Genealogy (influences): V2 only

---

## Tone & Style

- V1: Operational manual — exhaustive, checklists, patterns, value callouts. Dense but very actionable.
- V2: Minimal doctrine — agent‑oriented, skimmable, emphasizes parsimony and integration discipline.
- V3: Doctrinal narrative — readable and motivating; sets roles and final‑system framing.
- V4: V3 + kickoff rigor — adds strict binary‑weave, keeps concise ops content and templates.
- V5: Streamlined V4 — same center; fewer words; keeps roles and templates visible.
- V6: Tightest doctrine — adds pragmatism note on when to apply pipelines (“use when it makes sense”), includes README in loop; directive tone.

---

## Strengths & Weaknesses by Version

- V1
  - Strengths: Full coverage (testing, pipelines, guardrails, self‑audit, adoption, templates). “Why this matters” improves comprehension.
  - Weaknesses: Length and density risk bloat and onboarding friction.
- V2
  - Strengths: Compact, agent‑centric; easy to remember core ideas.
  - Weaknesses: Lacks operational guidance for execution and review.
- V3
  - Strengths: Clear roles, purpose, and two‑at‑a‑time integration doctrine.
  - Weaknesses: Light on pipelines/testing/guardrails details.
- V4
  - Strengths: Introduces Binary‑Weave Kickoff with strict sequencing; keeps needed ops chapters; includes kickoff template.
  - Weaknesses: Still longer than V5/V6; some overlap with V1 sections.
- V5
  - Strengths: Streamlined; keeps kickoff central; balanced depth with roles and templates.
  - Weaknesses: Less explicit than V1 on guardrails/self‑audit details.
- V6
  - Strengths: Tight; pragmatic note on when to apply pipelines; integrates README into the loop; cross‑links to guides.
  - Weaknesses: Omits repo layout/adoption detail; few examples.

---

## Redundancies & Gaps Across 1–6

Redundancies (good to unify once):
- Principles, loop, Napkin Physics, toy models, JSON+CLI legibility appear in all; wording varies.

New coverage brought by later drafts:
- Binary‑Weave Kickoff (V4–V6): strict sequential alternation (primitive → integrate with current product), end‑state articulation, and a simple checklist.
- Roles (V3, V5, V6): clear agent vs human responsibilities.

Gaps to watch:
- V6 relaxes pipeline emphasis (“use when it makes sense”) versus V1/V4’s stronger prescription.
- V6 references SPEC/PLAN/LEARNINGS/README writing guides explicitly; ensure those links resolve.
- Only V1 contains repo layout/adoption detail; later drafts assume it or omit it.

---

## Best‑Of Synthesis (What to Carry Forward)

- Doctrine: Use V3/V5/V6 tone for purpose, roles, and two‑at‑a‑time integration framing.
- Kickoff: Adopt V4/V5/V6 Binary‑Weave as the default planning format (with the checklist and end‑state summary).
- Operations: Keep V1’s depth for CLI+JSON contract, pipelines/golden tests, planning/testing specifics, guardrails/self‑audit, and repo adoption/layout.
- Pragmatism: Include V6’s note that pipelines/CLI composition are applied when they increase clarity/legibility.
- Aids: Retain V1/V4 templates and V1’s “Why this matters” callouts for key sections.

---

## Recommendations

- Start with a doctrinal core (V3/V5/V6): purpose, principles, roles, DDD loop, and two‑at‑a‑time integration.
- Add the Binary‑Weave Kickoff section early (V4/V5): Napkin Physics → sequential stages → end state + checklist.
- Follow with operational chapters from V1 (trimmed): CLI+JSON contract, pipelines & golden tests, planning & testing, guardrails & self‑audit, heuristics, adoption & repo layout.
- Close with templates/checklists (V1/V4) and optional genealogy note (V2) for context.

---

## Suggested Final Outline (Unified 1–6)

1) Purpose, Principles, Roles (V3/V5/V6)  
2) DDD Loop (V3 + V6’s README inclusion)  
3) Kickoff: Binary‑Weave (V4/V5/V6)  
4) Napkin Physics (all)  
5) Toy Models: Axes & Integration Discipline (all)  
6) CLI + JSON: Contract & Conventions (V1/V4)  
7) Pipelines & Golden Tests (V1/V4 with V6 pragmatism)  
8) Planning & Testing (V1)  
9) Guardrails & Self‑Audit (V1)  
10) Heuristics & Anti‑Patterns (V1)  
11) Adoption & Repository Layout (V1)  
12) Templates & Checklists (V1/V4)  
13) Optional: Genealogy (V2)  

---

## Decision Matrix (Picking a Version in Practice)

- Need to execute today with reviewable artifacts: use V1 or V5 as the base; add V4 kickoff.
- Onboarding a new teammate/agent: V3 or V6 doctrine first; then link to V1 ops sections.
- Presenting the approach: V2 doctrine slide + V4 kickoff diagram.

---

## Final Notes

- Versions 4–6 converge on the Binary‑Weave Kickoff while preserving the legibility substrate (JSON + CLI).  
- The unified outline above preserves V1’s operational utility and V3’s clarity, while adopting V4–V6’s kickoff discipline and streamlined tone.

*** End of Comparison 1–6 ***
