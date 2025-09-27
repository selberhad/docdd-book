# Execution Workflow

Most software development happens within established systems. Once you've moved past the research and experimentation phase—once the core patterns are proven and the architectural approach is validated—the heavy documentation discipline of discovery mode becomes unnecessary overhead. Execution mode addresses this common reality with a lighter, more focused approach.

Execution workflow recognizes that the primary challenge shifts from discovery to orchestration. Instead of validating uncertain approaches through systematic experimentation, you're building features within known constraints, following established patterns, and maintaining architectural coherence across a growing system.

## The Economic Reality of Established Systems

When working within mature codebases, the development economics change fundamentally. The core abstractions already exist. The data patterns are established. The integration points are defined. The technology choices have been made and validated through use.

In this context, the four-document harness of discovery mode—with its emphasis on systematic experimentation and risk mitigation—becomes process overhead that slows development without adding proportional value. The uncertainty that discovery mode addresses has already been resolved through earlier work.

Execution mode emerged from recognizing this shifted context. Rather than applying discovery discipline uniformly across all development work, DocDD adapts its approach to match the actual challenges: maintaining system legibility, ensuring architectural consistency, and preventing quality degradation as the system grows.

## Living Architecture Through Code Maps

The cornerstone of execution workflow is the CODE_MAP.md—a living architectural document that serves as the primary coordination mechanism between human developers, AI agents, and the evolving codebase.

Unlike traditional architectural documentation that becomes stale and misleading over time, the code map maintains currency through discipline: it's updated with every commit that changes system structure. This creates a reliable source of truth that both humans and AI can depend on for understanding how the system is organized.

The code map serves multiple audiences simultaneously. For human developers returning to a project or working in unfamiliar areas, it provides rapid orientation without requiring them to reverse-engineer system structure from implementation details. For AI agents, it supplies the architectural context necessary to make changes that fit existing patterns rather than introducing inconsistencies.

See: [Code Maps](./code-maps.md)

## Refactoring as System Maintenance

Execution workflow treats refactoring not as an occasional cleanup activity, but as mandatory system maintenance performed after every feature implementation or integration step. This shift from optional to required reflects the economic reality that AI assistance has made refactoring dramatically less expensive.

Traditionally, refactoring was difficult to justify because the effort-to-benefit ratio was poor. Improving working code consumed significant developer time while providing unclear business value. With AI assistance, refactoring becomes routine maintenance—similar to how automatic garbage collection eliminated manual memory management as a developer concern.

The mandatory refactoring step serves multiple purposes. It cleans up integration seams between new and existing components, maintaining clean boundaries and clear interfaces. It extracts emerging patterns and eliminates duplication that accumulates during feature development. Most importantly, it ensures that new code follows established architectural patterns rather than introducing inconsistencies that compound over time.

This discipline prevents the gradual degradation that typically occurs in software systems. Instead of accumulating technical debt that eventually requires expensive remediation, the system maintains consistent quality through continuous small improvements.

See: [Refactoring with AI Agents](./refactoring-with-ai.md)

## The Integration Development Cycle

Execution workflow follows a five-step cycle designed for efficiency within established systems:

**Orient** by reading the CODE_MAP.md to understand current architecture and constraints. This step ensures that new work builds on existing foundations rather than working against them.

**Plan** with brief, focused planning that emphasizes integration points and architectural fit. Unlike discovery mode's systematic experimentation planning, execution planning assumes known approaches and focuses on execution details.

**Implement** the feature following established patterns and architectural guidelines. The implementation phase benefits from clear constraints and proven approaches, enabling faster development cycles.

**Refactor** to clean up integration seams and improve code quality. This mandatory step ensures that the system's quality improves continuously rather than degrading over time.

**Update** the CODE_MAP.md to reflect any structural changes introduced during implementation. This maintains the currency and reliability of the architectural documentation.

## When Execution Mode Applies

Execution workflow works best when uncertainty has been resolved through previous work. The architectural approaches are proven and understood. Requirements are clear and well-defined. Technical constraints and limitations are documented and stable. Core systems and interfaces have matured through use.

These conditions indicate that the primary development challenge has shifted from discovery to execution. The system's fundamental patterns are established, and new work primarily involves extending these patterns to address additional requirements.

Execution mode acknowledges this shift explicitly. Rather than applying discovery-oriented processes to execution-oriented work, it provides lightweight discipline that maintains system quality without unnecessary overhead.

## Relationship to Discovery Mode

Execution workflow doesn't replace discovery mode—it complements it. When uncertainty arises during execution work, the methodology supports switching back to discovery mode's systematic experimentation approach. This might happen when requirements reveal gaps in the established patterns, when new technologies need evaluation, or when performance constraints require architectural changes.

The key insight is recognizing which mode fits the current development challenge. Most work in established systems benefits from execution workflow's lighter approach. But when uncertainty emerges, discovery mode's more rigorous discipline becomes valuable again.

This flexibility prevents the common antipattern of applying heavy process uniformly across all development work. Instead, DocDD adapts its methodology to match the actual challenges and uncertainty levels present in different phases of system development.

---

**Example in Practice**: [Case Study I: ChatGPT Export Viewer](../patterns/chatgpt-export-viewer.md) demonstrates execution workflow in action, showing how CODE_MAP.md and refactoring discipline supported the development of a shipped NPM package with clean human-AI collaboration boundaries.