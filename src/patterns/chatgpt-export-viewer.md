# Case Study I: ChatGPT Export Viewer

This archive lists concrete, working examples referenced throughout the book. It is intentionally small and current.

## Archive Browser Project

A complete DDD example demonstrating the full development cycle from kickoff to shipped product. This real-world project produced [chatgpt‑export‑viewer](https://www.npmjs.com/package/chatgpt-export-viewer), a suite of composable CLI tools for browsing ChatGPT export archives.

**Project outcome:** A cross-platform toolkit with clean human-AI collaboration boundaries:
- **Human role:** Product direction, UX decisions, constraint setting, edge case validation
- **Agent role:** Implementation, refactoring, shared pattern extraction, packaging polish

**Key architectural decisions:**
- CLI + JSON I/O for deterministic, testable composition
- Keyboard-first TUI with instant responsiveness (`/` search, `n/N` navigation)
- Modular libraries: ZIP access, terminal primitives, cross-platform launchers
- Publishing discipline: proper `bin` entries, dependency management, lint/format gates

The example demonstrates DDD's strength in AI-first development: clear documentation boundaries enable effective human-agent collaboration while maintaining code quality and user experience standards.

### Kickoff Document
Initial project definition using "napkin physics" to establish core constraints and approach.
- [Archive Browser Kickoff](./examples/archive-browser-kickoff.md)

### Spec Document
Technical specification defining invariants, contracts, and behaviors for Stage 1 primitives.
- [Archive Browser Spec](./examples/archive-browser-spec.md)

### Plan Document
Step-by-step implementation plan with TDD methodology, success criteria, and risk mitigation.
- [Archive Browser Plan](./examples/archive-browser-plan.md)

### Code Map Document
Living architectural documentation providing structural orientation for both humans and AI agents.
- [Archive Browser Code Map](./examples/archive-browser-code-map.md)

Notes
- Keep examples practical and minimal; link them from relevant chapters.
- Export formats: when useful, include small JSON/DOT/CSV snippets alongside examples.
