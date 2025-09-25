# Toy Patterns

The following patterns are extracted from the Toy Model Development guide.

Patterns That Work
- Single-class toys for small, cohesive experiments.
- Module-based toys when responsibilities split naturally.
- Adapter patterns when integrating external systems (LLMs, APIs, etc.).

Testing Philosophy
- Properties over examples: assert invariants that must always hold.
- Complex scenarios: end-to-end tests that mimic real workflows.
- Error paths: failures should be tested as deliberately as successes.

 
