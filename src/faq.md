# FAQ: Doc-Driven Development

## What problem is DocDD actually solving?

It solves the chaos of AI-assisted coding without context. Jumping into codegen with just a PRD leads to drift, inconsistency, and broken features. DocDD gives the AI structure and memory — so you stay in control.

## Is this just another spec-first approach with fancy terms?

Nope. The key difference is: **you don't write the docs — the AI does**. You just ask it to generate everything up front (specs, plans, tests, code) and you play reviewer/editor. That flips the whole flow.

## Why not just use a PRD and vibe code from there?

PRDs describe *what* to build, but not *how*. Without technical scaffolding, the AI will guess — and its guesses change session to session. DocDD makes it spell out its reasoning, structure, and plan before it touches the code.

## What's the difference between a toy model and a prototype?

Toy models are intentionally tiny and throwaway — built to learn, not to ship. They help validate structure or assumptions early. Prototypes often turn into half-baked production code. Toy models are lab experiments.

## What does "one axis of complexity" mean?

It means keeping every step simple: build a new primitive, combine two things, or add one thing to an existing system. Nothing more. This keeps both you and the AI from getting overwhelmed.

## Why JSON and CLI? Why not a full framework or GUI?

Because JSON + CLI = total visibility. You can inspect the whole state, write golden tests, and keep everything small and composable. Frameworks tend to hide structure — this makes it explicit.

## Do I need to be an AI whisperer to use this?

Nope. You just need to get into the habit of asking the AI to explain itself — with SPECs, PLANs, and LEARNINGS — before and during coding. The system helps you keep it aligned.

## Is this for solo devs or teams?

Works great for solo builders using AI as a partner. But the doc artifacts also make async teamwork smoother — people can ramp into the context just by reading the SPEC/PLAN.

## What if I already wrote code — can I still apply this retroactively?

Yep. Just ask the AI to generate docs based on the existing codebase. Use that to lock in structure, then resume with the DocDD flow going forward. Think of it as reverse-engineering clarity.

## Why is this worth the upfront structure? Doesn't it slow me down?

It feels slower on Day 1, but you gain huge speed by Day 5. You'll spend less time debugging, rewriting, and explaining stuff to the AI — because now it's building from a shared understanding.