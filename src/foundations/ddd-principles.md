# Dialectic‑Driven Development — Principles

## The Problem with Current AI-Coding Approaches

Software development is experiencing a fundamental shift as AI agents become capable programming partners. The industry has responded with various methodologies: spec-driven development, AI-enhanced TDD, structured prompting frameworks, and workflow optimizations. While these approaches offer incremental improvements, they share a critical limitation — they are human programming practices remixed for AI, not ground-up designs for AI capabilities.

Most current AI-coding methodologies ask: "How can we modify existing development workflows to work better with AI?" But this misses the deeper question: "If we designed software development from scratch for AI agents, what would it look like?"

The difference is significant. Human-oriented practices evolved around human cognitive limitations: working memory constraints, context-switching costs, and the difficulty of maintaining mental models across large codebases. AI agents have entirely different constraints: they excel at rapid iteration and pattern generation but struggle with consistency across sessions, maintaining context over long conversations, and distinguishing between hallucination and valid solutions.

Traditional approaches try to fit AI into human-shaped processes. They focus on better prompts, more structured inputs, and clearer specifications — essentially teaching AI to work within frameworks designed for human cognition. This is like optimizing horse carriages instead of inventing the automobile.

Dialectic-Driven Development takes the alternative approach: redesigning the entire development process around AI capabilities and limitations. Rather than asking how to make AI better at human workflows, it asks what programming methodology would emerge if we started from first principles with AI as the primary implementer.

## The Economic Shift

AI assistants have fundamentally altered the economics of software creation. Activities that once consumed significant human effort — writing code, updating documentation, refactoring existing implementations — can now be automated or substantially accelerated. This economic inversion transforms the traditional development calculus across multiple dimensions:

**Code Generation**: Scaffolding, boilerplate, tests, and even complex implementations can be generated in minutes rather than hours.

**Documentation Maintenance**: Updating specs, refreshing README files, and maintaining API documentation become automated workflow steps rather than manual overhead.

**Refactoring Operations**: Restructuring code that already works — traditionally a hard-to-justify business expense due to the effort-to-benefit ratio — becomes routine maintenance within the development cycle.

The result is a shifted value equation: individual artifacts become expendable, while clarity, architectural insight, and strategic decision-making become the primary sources of durable value.

Dialectic-Driven Development emerges from this shifted landscape, reversing the traditional implementation-first flow.

## Core Principles

**AI as Generator, Human as Editor**: The AI produces comprehensive artifacts (documentation, specifications, plans, tests, implementations) while the human focuses on simplification, risk identification, and constraint setting. This division leverages each party's strengths — AI's generative capacity and human's editorial judgment.

**Disposable Artifacts, Durable Insight**: All implementations, documentation, and tests are treated as expendable drafts. The lasting value lies in the clarity extracted through the development process and captured in meta-documentation. This removes psychological barriers to refactoring and experimentation.

**Parsimony Over Extensibility**: Prefer the simplest mechanism that solves today's problem rather than abstract frameworks designed for hypothetical future needs. This principle counters AI systems' tendency toward comprehensive, layered solutions.

**System Legibility**: Design for transparent, inspectable execution that both humans and AI can reason about reliably.

## Two Modes of DDD

Dialectic-Driven Development operates in two distinct modes depending on the project phase and level of uncertainty:

**Discovery Mode**: For novel solutions, uncertain requirements, or exploratory work where you need to validate concepts and discover constraints. Uses the full four-document harness (SPEC/PLAN/README/LEARNINGS) with toy model discipline to systematically explore and validate approaches.

**Execution Mode**: For established architectures where the patterns are known and you're building on proven foundations. Uses CODE_MAP.md as the central orchestration document plus mandatory refactoring after each feature implementation or integration step.

### When to Use Discovery Mode
- Implementing novel algorithms or approaches
- Uncertain requirements or problem definition
- Exploring new technologies or frameworks
- Building foundational components where the patterns aren't established
- Any work that requires systematic experimentation

### When to Use Execution Mode
- Adding features to established codebases
- Building on proven architectural patterns
- Straightforward implementations without novel components
- Post-MVP development where core patterns are validated
- Any work where the main challenge is orchestration rather than discovery

The key insight: most development is execution work that doesn't require the heavy documentation discipline of discovery mode. But when uncertainty exists, the discovery approach prevents costly architectural mistakes through systematic exploration.