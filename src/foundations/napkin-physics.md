# Napkin Physics

The term derives from Fermi estimation and "back-of-the-envelope" calculations — rough approximations simple enough to sketch on a restaurant napkin. In software development, napkin physics applies this same principle to problem framing: upstream simplification to prevent scope drift by capturing the essential mechanism at the highest level of abstraction.

The technique draws inspiration from Einstein's principle: "Everything should be made as simple as possible, but no simpler." Rather than diving directly into implementation details, napkin physics forces problem definition at the conceptual level — as if sketching the core mechanism on a restaurant napkin.

This approach counters the natural tendency of AI systems to generate comprehensive, layered solutions. By establishing conceptual constraints upfront, the methodology guides subsequent SPEC and PLAN generation toward parsimony without losing essential complexity.

## Structure

**Problem**: Single sentence defining what needs to be solved.

**Assumptions**: 3–5 bullets listing what can be taken as given.

**Invariant/Contract**: One precise property that must hold across all operations.

**Mechanism**: ≤5 bullets describing the minimal viable path (single‑file spike preferred).

**First Try**: Short paragraph outlining the simplest possible approach.

## Constraints

**Prohibitions**: No frameworks, no new architectural layers, no new abstractions unless two existing ones are removed.

**Scope Limitation**: Focus on the essential mechanism only — defer integration, optimization, and edge cases to subsequent phases.

## Application

Napkin physics serves as the foundation step before SPEC and PLAN generation. By establishing conceptual boundaries first, it prevents scope drift and over-engineering in downstream documentation.

The exercise forces identification of the core problem without implementation assumptions. This clarity propagates through the entire development cycle, maintaining focus on essential functionality rather than comprehensive feature sets.

## Effectiveness

The technique leverages AI systems' sensitivity to framing. Abstract, constraint-focused prompts produce fundamentally different outputs than implementation-focused ones. The napkin physics format consistently guides AI toward minimal viable solutions rather than maximal complete ones.

See also: [Dialectic‑Driven Principles](./ddd-principles.md), [DDD AGENTS.md Template](../practice/ddd-agents-template.md)
