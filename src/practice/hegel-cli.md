# Hegel CLI: Workflow Orchestration Tool

Hegel is a command-line tool that operationalizes Dialectic-Driven Development through state-based workflow management. It guides you through structured development cycles while capturing metrics and enforcing methodology discipline.

**Designed for AI agents, ergonomic for humans.** Hegel provides deterministic workflow guardrails for AI-assisted development while remaining comfortable for direct human use.

## Installation

Hegel is written in Rust and distributed as source:

```bash
git clone https://github.com/dialecticianai/hegel-cli
cd hegel-cli
cargo build --release
```

The binary will be available at `./target/release/hegel`.

**Requirements:**
- Rust toolchain (cargo, rustc)
- Works on macOS, Linux, Windows
- No external dependencies or API keys required

## Core Concepts

### State Machine Workflows

Hegel uses YAML-based workflow definitions that specify:
- **Nodes** - Development phases with specific prompts
- **Transitions** - Rules for advancing between phases based on claims
- **Mode** - Discovery (exploration) or Execution (delivery)

State is stored locally in `.hegel/state.json` (in your current working directory), making it fully offline with no cloud dependencies.

### Available Workflows

**Discovery Mode** (learning-focused):
- SPEC → PLAN → CODE → LEARNINGS → README
- Optimized for learning density
- Full four-document harness

**Execution Mode** (delivery-focused):
- KICKOFF → SPEC → PLAN → CODE → REFACTOR → CODE_MAP
- Optimized for production resilience
- Mandatory refactoring phase

**Minimal Mode** (simplified):
- Reduced ceremony for quick iterations
- Testing and experimentation

## Basic Usage

### Starting a Workflow

Initialize a new workflow in your project:

```bash
hegel start discovery
```

Hegel creates `.hegel/state.json` and displays the first phase prompt, which includes relevant writing guides injected into the template.

### Advancing Through Phases

Transition to the next phase by providing claims:

```bash
hegel next '{"spec_complete": true}'
```

**Common claims:**
- `spec_complete` - SPEC phase finished
- `plan_complete` - PLAN phase finished
- `code_complete` - Implementation finished
- `learnings_complete` - LEARNINGS documented
- `restart_cycle` - Return to SPEC phase

Hegel validates the claim against workflow rules and advances you to the next node if the transition is valid.

### Checking Status

View your current workflow position:

```bash
hegel status
```

Output shows:
- Current mode (discovery/execution)
- Current node/phase
- Full history of nodes visited
- Workflow metadata

### Resetting State

Clear all workflow state to start fresh:

```bash
hegel reset
```

## Writing Guide Injection

Hegel workflows include template placeholders that inject writing guides into phase prompts:

**Template syntax:**
```yaml
prompt: |
  You are in the SPEC phase.

  {{SPEC_WRITING}}

  Your task: Write a minimal behavioral contract.
```

**At runtime**, `{{SPEC_WRITING}}` is replaced with the full contents of `guides/SPEC_WRITING.md`, ensuring agents receive consistent methodology guidance.

**Available guides:**
- `SPEC_WRITING` - Behavioral contract guidance
- `PLAN_WRITING` - TDD roadmap planning
- `CODE_MAP_WRITING` - Code mapping guidelines
- `LEARNINGS_WRITING` - Insight extraction guidance
- `README_WRITING` - Summary documentation guidance
- `HANDOFF_WRITING` - Session handoff protocol
- `KICKOFF_WRITING` - Project kickoff guidance

## Claude Code Integration

Hegel integrates with Claude Code to capture development activity as you work, enabling metrics collection and workflow analysis.

### Hook Configuration

Configure Claude Code to send hook events to Hegel by adding to `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": "hegel hook PostToolUse"
  }
}
```

Hook events are captured to `.hegel/hooks.jsonl` with timestamps, building a detailed log of development activity (tool usage, bash commands, file modifications).

### Captured Events

**Hook events logged:**
- Tool usage (Bash, Read, Edit, Write, Grep, etc.)
- Bash commands executed
- File modifications with paths
- Transcript references for token metrics

**Workflow state transitions logged** (`.hegel/states.jsonl`):
- Phase changes (from_node → to_node)
- Timestamps for correlation
- Workflow mode and session metadata

## Metrics and Analysis

### Analyze Command

View captured development activity and metrics:

```bash
hegel analyze
```

**Output includes:**
- Session ID and workflow summary
- Token usage (input/output/cache metrics from transcripts)
- Activity summary (bash commands, file modifications)
- Top commands and most-edited files
- Workflow state transitions
- **Per-phase metrics:**
  - Duration (time spent in each phase)
  - Token usage (input/output tokens per phase)
  - Activity (bash commands and file edits per phase)
  - Status (active or completed)
- **Workflow graph:**
  - ASCII visualization of phase transitions
  - Node metrics (visits, tokens, duration, commands, edits)
  - Cycle detection (identifies workflow loops)

### Interactive Dashboard

Launch a real-time terminal UI:

```bash
hegel top
```

**Features:**
- **4 interactive tabs**: Overview, Phases, Events, Files
- **Live updates**: Auto-reloads when event logs change
- **Scrolling**: Arrow keys, vim bindings (j/k), jump to top/bottom (g/G)
- **Navigation**: Tab/BackTab to switch tabs
- **Colorful UI**: Emoji icons, syntax highlighting, status indicators

**Keyboard shortcuts:**
- `q` - Quit
- `Tab` / `BackTab` - Navigate tabs
- `↑↓` / `j`/`k` - Scroll
- `g` / `G` - Jump to top/bottom
- `r` - Reload metrics manually

**What's tracked:**
- Overview tab: Session summary, token usage, activity metrics
- Phases tab: Per-phase breakdown (duration, tokens, activity)
- Events tab: Unified timeline of hooks and states (scrollable)
- Files tab: File modification frequency (color-coded by intensity)

### Metrics Correlation

Hegel correlates three independent event streams by timestamp:

1. **hooks.jsonl** - Claude Code activity (tool usage, bash commands, file edits)
2. **states.jsonl** - Workflow transitions (phase changes)
3. **Transcripts** - Token usage from `~/.claude/projects/<project>/<session_id>.jsonl`

**Correlation strategy:**
- All hooks after workflow start belong to that workflow (workflow_id is start timestamp)
- Hooks attributed to phases by timestamp ranges (state transitions define boundaries)
- Token metrics extracted from transcripts and correlated to workflow phases

This enables questions like:
- "How many bash commands during SPEC phase?"
- "Token usage in PLAN phase?"
- "Which files were edited most during CODE phase?"

## Deterministic Guardrails

Workflows can include rules that detect problematic patterns and interrupt with warning prompts:

**Example rules** (from discovery.yaml CODE phase):
```yaml
rules:
  - type: repeated_command
    pattern: "cargo (build|check|test)"
    threshold: 6
    window: 180
  - type: repeated_file_edit
    path_pattern: "src/.*"
    threshold: 10
    window: 300
  - type: token_budget
    max_tokens: 10000
```

**Rule types:**
- `repeated_command` - Detects command patterns repeated beyond threshold
- `repeated_file_edit` - Detects excessive edits to same file pattern
- `token_budget` - Enforces maximum token usage per phase

When rules are violated, Hegel injects warning prompts into the workflow, encouraging reflection before proceeding.

## State Directory Configuration

By default, Hegel uses `.hegel/` in the current working directory. You can override this:

**Via command-line flag:**
```bash
hegel --state-dir /tmp/my-project start discovery
```

**Via environment variable:**
```bash
export HEGEL_STATE_DIR=/tmp/my-project
hegel start discovery
```

**Precedence:** CLI flag > environment variable > default (`.hegel/` in cwd)

**Use cases:**
- Testing: Isolate test runs in temporary directories
- Multi-project workflows: Override default per-project location
- CI/CD: Configure non-default state locations in automated environments

## When to Use DDD Workflows

Hegel is a general workflow orchestration tool. The DDD-opinionated guides included are defaults, not requirements.

**Use full DDD workflows for:**
- Hard problems requiring novel solutions
- Projects needing rigorous documentation
- Complex domains where mistakes are expensive
- Learning-dense exploration (discovery mode)

**Skip DDD overhead for:**
- Straightforward implementations agents can handle autonomously
- Simple CRUD applications or routine features
- Projects where the agent doesn't need structured guidance

The workflow steps and token usage are designed for problems that need that rigor. Many projects don't require it.

## Example Workflow Session

**Starting discovery workflow:**
```bash
$ hegel start discovery
Workflow started: discovery mode
Current node: spec

You are in the SPEC phase of Dialectic-Driven Development (Discovery Mode).

[SPEC_WRITING guide content injected here...]

Your task: Write a minimal behavioral contract.
```

**Advancing after completing SPEC:**
```bash
$ hegel next '{"spec_complete": true}'
Transitioned: spec → plan

You are in the PLAN phase of Dialectic-Driven Development (Discovery Mode).

[PLAN_WRITING guide content injected here...]

Your task: Create a test-driven implementation plan.
```

**Checking status:**
```bash
$ hegel status
Mode: discovery
Current node: plan
History: spec → plan
Workflow ID: 2025-10-12T10:30:00Z
```

**Analyzing metrics after completion:**
```bash
$ hegel analyze
Session: abc123def
Workflow: discovery (complete)

Token Usage:
  Input: 45,230 tokens
  Output: 12,450 tokens
  Cache read: 8,900 tokens

Activity:
  Bash commands: 87
  File edits: 34

Per-Phase Breakdown:
  spec: 15 min, 8.2k tokens, 12 commands, 5 file edits
  plan: 22 min, 12.1k tokens, 18 commands, 8 file edits
  code: 45 min, 24.8k tokens, 45 commands, 18 file edits
  learnings: 10 min, 4.2k tokens, 8 commands, 2 file edits
  done: 5 min, 1.9k tokens, 4 commands, 1 file edit
```

## Integration with DDD Methodology

Hegel operationalizes the methodology by:

**Enforcing structure:** State machine prevents skipping phases or advancing prematurely

**Providing context:** Writing guides injected at each phase ensure consistency

**Capturing metrics:** Hook integration enables post-hoc analysis of workflow efficiency

**Enabling iteration:** Cycle transitions (LEARNINGS → SPEC) support Discovery mode loops

**Maintaining discipline:** Deterministic rules detect problematic patterns without LLM judgment

**The goal:** Make DDD practical through tooling, not just theoretical through documentation.

## Project Repository

Hegel is open source (SSPL license):

**Repository:** https://github.com/dialecticianai/hegel-cli

**Documentation:** README.md, CODE_MAP.md (architecture), workflow definitions in `workflows/`

**Guides:** Writing templates in `guides/` directory

For more information about Dialectic-Driven Development methodology, visit [dialectician.ai](https://dialectician.ai).
