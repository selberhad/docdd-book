# Debugger Mindset

Once documentation provides structure and AI agents have clear specifications, a critical challenge remains: **how can agents execute systems reliably without becoming lost in hidden state?** The solution lies in adopting a debugger mindset — treating all system components as if they operate in debugger mode, with every execution step exposed in machine-readable form.

## System Legibility for AI Agents

Traditional software development tolerates hidden state, implicit context, and opaque execution flows. Human developers navigate these complexities through experience and debugging tools. AI agents, however, require explicit, deterministic interfaces to maintain consistency across execution sessions.

The core principle is **system legibility**: making all execution state visible and falsifiable. This enables agents to:

- Verify intermediate results against specifications
- Reproduce exact execution sequences
- Identify failure points without ambiguity
- Maintain consistent behavior across sessions

## CLI + JSON Architecture

The most effective substrate for AI-legible systems combines command-line interfaces with JSON data interchange:

**Interface Contract:**
- **stdin**: JSON input parameters
- **stdout**: JSON output results
- **stderr**: Structured error JSON

**Execution Rules:**
- Deterministic behavior: identical inputs produce identical outputs
- No hidden state dependencies
- Pure functions with explicit side effects
- Machine-parsable error handling

**Error Format:**
```json
{
  "type": "ERR_CODE",
  "message": "human-readable description",
  "hint": "actionable remediation steps"
}
```

## Pipeline Composition

JSON-based CLIs enable UNIX-style pipeline composition that agents can inspect and validate:

```bash
moduleA < input.json > intermediate.json
moduleB < intermediate.json > result.json
moduleC --transform < result.json > output.json
```

Each pipeline stage produces inspectable artifacts. Agents can:

- Validate intermediate results against expected schemas
- Isolate failure points by examining individual stages
- Reproduce partial executions for testing and debugging
- Generate comprehensive execution traces

## Golden Test Integration

Every module should provide a canonical golden test demonstrating expected behavior:

```bash
# Single command that validates core functionality
./module --golden-test
```

Golden tests serve as **deterministic checkpoints** that:

- Establish baseline behavior before modifications
- Prevent specification drift during development
- Provide concrete examples of correct input/output pairs
- Enable agents to verify their understanding of system behavior

## Implementation Patterns

**Module Structure:**
- Single executable per logical function
- JSON schema validation for inputs/outputs
- Comprehensive error handling with structured messages
- Built-in golden test modes

**System Design:**
- Prefer composition over complex monolithic tools
- Minimize interdependencies between modules
- Expose all configuration through explicit parameters
- Maintain audit trails of execution decisions

## Benefits for AI Development

The debugger mindset transforms AI-system interaction from guesswork to systematic execution:

**Predictability**: Agents can reason about system behavior through explicit interfaces rather than implicit behavior patterns.

**Testability**: Every system interaction produces verifiable artifacts that can be validated against specifications.

**Debuggability**: Execution traces provide clear failure attribution and remediation paths.

**Reproducibility**: Deterministic interfaces enable exact recreation of execution sequences for analysis and refinement.

This approach establishes a foundation where human oversight and AI execution can coexist productively, with clear boundaries and verifiable outcomes at every step.