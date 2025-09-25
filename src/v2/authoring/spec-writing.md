# Spec Writing

Purpose
- Make behavior falsifiable before code exists. A reader should be able to write tests from your spec alone.

Principles
- Concrete over abstract: use realistic data and full structures.
- Single axis: spec one cohesive capability; split when scope drifts.
- Validation first: define invariants and error semantics clearly.

Recommended structure
1) Header
   - Title: System Name Specification
   - One‑line purpose and scope
2) Overview
   - What it does (2–3 sentences)
   - Key principles and integration context
3) Data Model
   - Full example structures (JSON or domain format)
   - Fields, types, ranges, and meanings; schemas if helpful
4) Operations
   - For each command/API: Syntax → Parameters → Examples → Behavior → Validation
   - Include error conditions and edge cases
5) Test Scenarios
   - Simple, Complex, Error (and Integration if necessary)
6) Success Criteria
   - Checkbox list of falsifiable outcomes
7) Error Handling
   - Shapes, codes, and example messages; guidance for consumers

Common pitfalls (and fixes)
- Vague behavior → Add step‑by‑step outcomes and invariants.
- Placeholder data → Replace with realistic values and nested structures.
- Missing errors → List the top 2–3 failure modes with examples.
- Scope creep → Split into smaller specs; keep each about one axis.

Template excerpt
```
## Data Model
{
  "entity": {
    "id": "e1",
    "label": "entry_hall",
    "geometry": { "x": -8.5, "y": -8.5, "width": 17, "height": 17 }
  }
}

## Operations
#### `aggregate <rules> [scope]`
Applies aggregation rules.

Parameters:
- `<rules>`: "indoor_standard" | "outdoor_large"
- `[scope]`: optional selector

Examples:
```
aggregate indoor_standard
aggregate outdoor_large rooms:west
```

Behavior:
- Explains transformations and invariants preserved

Validation:
- Input ranges, error conditions, edge cases
```

See also: [Doc‑Driven Principles](../foundations/ddd-principles.md)
