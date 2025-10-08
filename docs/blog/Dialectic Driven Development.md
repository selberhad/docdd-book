# Doc Driven Development in the Age of AI

AI assistants have upended the economics of software creation. Code that once took human hours to write — even the “obvious” scaffolding, boilerplate, and tests — can now be generated in minutes. This flips the traditional calculus: code itself becomes cheap and disposable, while the real value lies in the clarity and insight you extract from building it.

This inversion is the core of **Doc Driven Development (DDD)** — an AI‑first methodology where the assistant generates every artifact (docs, specs, plans, tests, code), and the human acts as reviewer, simplifier, and arbiter. Rather than starting with implementation and writing docs later, the cycle flows in the opposite direction:

**Docs → Tests → Implementation → Learnings.**

---

## The Meta‑Document Layer

In DDD, documentation is not an afterthought but the substrate for development. Four document types serve as the backbone of the cycle:

* **SPEC.md** → comprehensive behavioral contract: data formats, operations, test scenarios, success criteria.
* **PLAN.md** → strategic roadmap: step‑by‑step development sequence, testing approach, integration points.
* **README.md** → context refresh: concise guides for libraries, APIs, and usage patterns.
* **LEARNINGS.md** → retrospective: architectural insights, pivots, and reusable patterns.

These meta‑docs keep the assistant aligned and ensure every cycle produces durable knowledge, even if the code is discarded.

---

## From Napkin Physics to Toy Models

The human’s key role in this loop is not producing artifacts but **spotting opportunities for simplification**. Left alone, LLMs tend to over‑engineer — layering abstractions and generating maximal completeness. To counter this, you can shift the frame of thought before any code is written.

One powerful technique is “**napkin physics**”: framing problems abstractly, as if two physicists were sketching ideas on a restaurant napkin. This pulls the model into a mode of conceptual parsimony — seeking elegant, minimal structures rather than verbose implementations.

Once the abstractions are clarified, the assistant can generate **toy models**: small, sharply scoped reference implementations designed to be discarded. These act like lab experiments in science — valuable not for production readiness, but for the learnings they yield:

* They are cheap to build.
* They are safe to discard.
* They validate assumptions about data structures, APIs, and edge cases.

The true artifact is not the toy code itself, but the **clarity extracted** and recorded in LEARNINGS.md.

---

## The Human’s Role as Alchemist

This intervention has an alchemical quality, echoing George Soros’s notion of alchemy in finance. Soros argued that market participants’ perceptions don’t just describe reality — they *shape* it, feeding back into outcomes through reflexivity. Likewise, the human’s framing of problems doesn’t just simplify the assistant’s response; it actively changes the system’s behavior.

By nudging context — napkin sketches instead of specs, toy models instead of production builds — the human alters what the assistant produces and how the development process unfolds. The gold is not in the raw output, but in the transformed understanding.

---

## The Payoff

By embracing DDD with toy models and napkin physics, you:

* Stop treating code as precious.
* Stop fearing rewrites or sunk costs.
* Gain architectural clarity quickly and cheaply.
* Build a durable library of docs, specs, and learnings that compound over time.

In this paradigm, the AI generates endlessly disposable drafts, while the human distills durable insight. The process itself becomes reflexive — a feedback loop where framing changes outcomes, and outcomes reshape framing. That is the essence of context engineering.
