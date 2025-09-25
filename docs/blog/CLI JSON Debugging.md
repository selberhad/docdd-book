# CLI + JSON as Debugger: Giving LLM Agents Deterministic Legs

In [Doc Driven Development](Doc%20Driven%20Development.md), I argued that code is now cheap and disposable, while durable value comes from clarity extracted into documents. But once you have docs, plans, and specs, there remains a practical bottleneck: **how do you let an LLM agent *actually run* a system without getting lost in hidden state?**

The answer is to treat your tools as if they’re running in **debugger mode** — exposing every step of execution in machine-readable form. The simplest universal substrate for this is **CLI + JSON**.

---

## Why LLMs Need a Debugger Mode

Human developers lean on debuggers to single-step, inspect, and bisect. LLMs need an equivalent — not at the source line level, but at the **system execution** level. Opaque logs and hidden globals confuse them. Deterministic JSON I/O gives the agent transparent, falsifiable state to reason over.

---

## The Contract

Every functional module should expose a pure CLI:

- stdin: JSON input  
- stdout: JSON output  
- stderr: structured error JSON  

The rules are simple:

- Same input → same output (no hidden state)  
- Logs are allowed, but outputs must stay pure  
- Errors must be machine-parsable, e.g.

    { "type": "ERR_CODE", "message": "human text", "hint": "actionable fix" }

---

## Pipelines as Execution Traces

When tools all speak JSON, they chain cleanly:

    modA < in.json > a.json
    modB < a.json > b.json
    modC --flag X < b.json > out.json

This UNIX-style composition is a gift to LLMs. They can now “walk the pipeline” step by step, verifying each intermediate artifact against the spec — exactly like setting breakpoints in a debugger.

---

## Golden Tests as Breakpoints

Each CLI should ship with a one-liner golden test path. Agents can run it before any modification, ensuring they understand the system’s baseline behavior. These golden tests act as **deterministic checkpoints**, anchoring the LLM’s reasoning and preventing drift.

---

## Why This Matters

Building “AI-debuggable” systems isn’t about clever abstractions. It’s about **legibility**. Humans may tolerate hidden state; LLMs cannot. CLI + JSON provides the narrow waist where humans, agents, and pipelines all meet on equal terms.  

This pattern makes the difference between agents flailing blindly and agents running in clean, repeatable loops.

---

## Closing Thought

If DDD is about turning code into disposable drafts and clarity into durable artifacts, CLI + JSON is about making execution equally disposable and inspectable. It gives LLMs the deterministic legs they need to walk through systems, one step at a time — and gives humans a reliable way to stay in the driver’s seat.