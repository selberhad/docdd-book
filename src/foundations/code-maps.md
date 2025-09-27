# Code Maps

CODE_MAP.md serves as living architectural documentation that provides structural orientation for both humans and AI agents. It's the central orchestration document in Execution Mode, updated with every commit to reflect the current system state.

## Purpose and Philosophy

Code maps bridge the gap between high-level architecture and implementation details. They give both humans and AI a clear mental model of how the codebase is organized without requiring them to reverse-engineer structure from code.

**For Humans**: Quick orientation when returning to a project or understanding unfamiliar areas
**For AI Agents**: Essential context for understanding existing structure before making changes
**For Teams**: Shared understanding of system organization and component responsibilities

## Structure and Contents

### Architecture Overview
High-level purpose, design philosophy, and data flow patterns that define the system's approach.

### Key Directories
Functional organization with clear responsibilities - what each major directory contains and why.

### Component Documentation
Each major module/library documented with:
- Key functions and their purposes
- Primary interfaces and data shapes
- How the component fits into the larger system

### Integration Patterns
How components connect and depend on each other:
- Data flow between major systems
- Interface boundaries and contracts
- Orchestration and coordination patterns

### Practical Insights
- Known issues and gotchas that developers encounter
- Fragile areas that require careful modification
- Safety patterns and common pitfalls
- Performance considerations and optimization notes

## Maintenance Discipline

### Updated with Every Commit
The CODE_MAP must always reflect current reality. When code structure changes, the map changes too.

### Focus on Structure Over Details
Capture architectural insight, not implementation specifics. The goal is orientation, not exhaustive documentation.

### AI-Agent Friendly
Written to help agents understand the system quickly and make appropriate changes that fit existing patterns.

### Change-Sensitive Sections
Explicitly flag areas that are fragile, experimental, or require special care when modifying.

## Writing Effective Code Maps

### Start with Purpose
Begin with a clear statement of what the system does and its core design philosophy.

### Show Data Flow
Trace typical execution paths through the system to illustrate how components interact.

### Document the Why
Explain architectural decisions and trade-offs, not just what exists.

### Keep It Current
Treat the CODE_MAP as a living document that evolves with the codebase.

### Be Selective
Include what helps understanding, skip what adds noise. Focus on the most important 80% of the system.

## Integration with Execution Workflow

Code maps work best when integrated into the standard development cycle:

1. **Orient**: Read CODE_MAP.md before starting work
2. **Plan**: Consider how changes fit existing architecture
3. **Implement**: Build following established patterns
4. **Refactor**: Clean up integration seams
5. **Update**: Refresh CODE_MAP.md for structural changes

The code map becomes the foundation that enables confident refactoring and consistent architectural decisions across the development cycle.