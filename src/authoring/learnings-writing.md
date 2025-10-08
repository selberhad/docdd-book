# Learnings Writing

This chapter provides agent-oriented documentation for writing LEARNINGS.md files in DDD projects. Drop this guide into your repository as `LEARNINGS_WRITING.md` to help AI agents create effective retrospective documentation that captures architectural insights and constraints.

---

```markdown
# LEARNINGS_WRITING.md

## Purpose

A **LEARNINGS.md** is a short, dense retrospective.  
Its job: extract maximum value from an experiment by recording **what worked, what failed, what remains uncertain, and why.**

---

## What It Is / Is Not

### ❌ Not

- A feature list  
- Implementation details  
- A user manual  
- Purely positive  
- Hype or speculation without evidence  

### ✅ Is

- A record of validated insights  
- A log of failures and limitations  
- A map of open questions  
- A pointer to architectural reuse  
- A calibration tool for future experiments  

---

## Essential Sections

### Header

    # Toy Model N: System Name – Learnings
    Duration: X days | Status: Complete/Incomplete | Estimate: Y days

### Summary

- Built: 1 line  
- Worked: 1–2 key successes  
- Failed: 1–2 key failures  
- Uncertain: open question

### Evidence

- ✅ Validated: concise finding with evidence  
- ⚠️ Challenged: difficulty, workaround, lesson  
- ❌ Failed: explicit dead end  
- 🌀 Uncertain: still unresolved

### Pivots

- Original approach → New approach, why, and what remains unknown.

### Impact

- Reusable pattern or asset  
- Architectural consequence  
- Estimate calibration (time/effort vs. outcome)

---

## Style

- Keep it **short and factual**.  
- Prefer **bullet points** over prose.  
- Note **failures and unknowns** as explicitly as successes.  
- One page max — dense, parsimonious, reusable.

LEARNINGS.md is not a diary. It is a **distilled record of architectural insights** that prevent future agents from repeating failures and help them understand what constraints actually matter.
```    
