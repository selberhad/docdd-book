# FAQ: Dialectic-Driven Development

## What problem is DDD actually solving?

It solves the chaos of AI-assisted coding without context. DDD adapts to different development phases: Discovery Mode for uncertain work uses systematic experimentation, while Execution Mode for established systems uses lightweight documentation and refactoring discipline. Both keep you in control.

## Is this just another spec-first approach with fancy terms?

Nope. The key difference is: **you don't write the docs — the AI does**. In Discovery Mode, the AI generates comprehensive docs (specs, plans, tests, code) and you review/edit. In Execution Mode, the AI maintains CODE_MAP.md and handles refactoring. Either way, you stay in the editor role.

## Why not just use a PRD and vibe code from there?

PRDs describe *what* to build, but not *how*. Without technical scaffolding, the AI will guess — and its guesses change session to session. DDD provides that scaffolding through different approaches depending on whether you're discovering new patterns or executing within established ones.

## What's the difference between a toy model and a prototype?

Toy models are intentionally tiny and throwaway — built to learn, not to ship. They help validate structure or assumptions early. Prototypes often turn into half-baked production code. Toy models are lab experiments.

## What does "one axis of complexity" mean?

It means keeping every step simple: build a new primitive, combine two things, or add one thing to an existing system. Nothing more. This keeps both you and the AI from getting overwhelmed.

## Why JSON and CLI? Why not a full framework or GUI?

Because JSON + CLI = total visibility. You can inspect the whole state, write golden tests, and keep everything small and composable. Frameworks tend to hide structure — this makes it explicit.

## Do I need to be an AI whisperer to use this?

Nope. You just need to get into the habit of asking the AI to explain itself — through Discovery Mode's four-document harness or Execution Mode's CODE_MAP.md and refactoring discipline. The system helps you keep it aligned.

## Is this for solo devs or teams?

Works great for solo builders using AI as a partner. But the doc artifacts also make async teamwork smoother — people can ramp into the context just by reading the SPEC/PLAN.

## What if I already wrote code — can I still apply this retroactively?

Yep. Just ask the AI to generate docs based on the existing codebase. Use that to lock in structure, then resume with the DDD flow going forward. Think of it as reverse-engineering clarity.

## Why is this worth the upfront structure? Doesn't it slow me down?

It feels slower on Day 1, but you gain huge speed by Day 5. You'll spend less time debugging, rewriting, and explaining stuff to the AI — because now it's building from a shared understanding.

## How do I know when to use Discovery Mode vs. Execution Mode?

If you're unsure about the approach, requirements, or architecture - use Discovery Mode. If you're adding features to an established codebase with proven patterns - use Execution Mode. Most development is actually Execution work, so when in doubt, try Execution first and switch to Discovery if you hit uncertainty.

## What do I do when the AI generates repetitive, verbose code despite asking for DRY principles?

Don't fight it upfront — let the AI write repetitive code until tests pass, then use the three-phase refactoring cycle: Generate to Green → Plan the Cleanup → Execute Refactoring. This works with AI tendencies rather than against them.

## How often should I update my CODE_MAP.md? Every commit seems excessive.

Every commit that changes the code map is correct — it would be excessive for human engineers, but it's optimal for LLM agents. If something in the code changes that requires the code map to change, then it needs to be updated as part of that commit. AI agents need current architectural context to make good decisions, and the economic shift makes constant updates feasible.