# README Writing Guidelines for Internal Libraries

Guidelines for creating concise, AI assistant–focused README.md files for internal libraries and modules.

---

## Purpose

These READMEs serve as **context refresh documents** for AI assistants working with the codebase. They should quickly re-establish understanding of what each library does, how to use it, and what to watch out for.

**Target audience**: AI assistants needing to quickly understand library purpose and usage patterns  
**Length target**: 100–200 words total  
**Focus**: Dense, essential information only

---

## Required Structure

### **1. Header + One-Liner**
```markdown
# library_name
Brief description of what it does and key technology/pattern
```

### **2. Purpose (2–3 sentences)**
- What core problem this solves
- Key architectural approach or design pattern
- How it fits in the broader system/integration

### **3. Key API (essential methods only)**
```python
# 3-5 most important methods with type hints
primary_method(param: Type) -> ReturnType
secondary_method(param: Type) -> ReturnType
```

### **4. Core Concepts (bullet list)**
- Key data structures or abstractions
- Critical constraints or assumptions  
- Integration points with other libraries
- Important design patterns

### **5. Gotchas & Caveats**
- Known limitations or scale constraints
- Common usage mistakes
- Performance considerations
- Integration pitfalls

### **6. Quick Test**
```bash
pytest tests/test_basic.py  # or most representative test
```

---

## Writing Guidelines

### **Be Concise**
- Use bullet points over paragraphs
- Focus on essential information only
- Assume reader has basic programming knowledge

### **Be Specific**
- Include actual method signatures, not generic descriptions
- Mention specific constraints (e.g., "max 1000 rooms before performance degrades")
- Reference specific test files for examples

### **Be Practical**
- Lead with most commonly used methods
- Highlight integration points with other libraries
- Focus on "what you need to know to use this correctly"

### **Avoid**
- Marketing language or feature lists
- Detailed implementation explanations
- Extensive examples (link to tests instead)
- Installation instructions (assume internal development environment)

---

## Template

```markdown
# library_name
Brief description of what it does

## Purpose
2–3 sentences covering the core problem solved, architectural approach, and role in broader integration.

## Key API
```python
most_important_method(params: Type) -> ReturnType
second_most_important(params: Type) -> ReturnType
utility_method(params: Type) -> ReturnType
```

## Core Concepts
- Key data structure or abstraction
- Critical constraint or assumption
- Integration point with other libraries
- Important design pattern

## Gotchas
- Known limitation or performance constraint
- Common usage mistake to avoid
- Integration pitfall with other libraries

## Quick Test
`pytest tests/test_representative.py`
```

---

## Quality Check

A good library README should allow an AI assistant to:
1. **Understand purpose** in 10 seconds
2. **Know primary methods** to call
3. **Avoid common mistakes** through gotchas section
4. **Validate functionality** through quick test

If any of these takes longer than expected, the README needs to be more concise or better organized.
