# External Knowledge Capture

External documentation is a first-class artifact in Dialectic-Driven Development. Dependencies, APIs, and unfamiliar technologies require systematic capture of external knowledge before experimentation begins.

## The Documentation Cache Pattern

Treat external documentation like code dependencies: cache locally for offline access, AI context, and version stability.

### The `.webcache/` Directory

Store cached documentation in a dedicated directory:

```
.webcache/
  nesdev_wiki_ppu_sprites.md
  rust_std_collections.html
  fastmcp_server_middleware.pdf
```

**Workflow:**

**1. Fetch before using**
```bash
# Cache wiki page
wget https://docs.example.com/guide -O .webcache/example_guide.md

# Or fetch tool if available
./tools/fetch-wiki.sh PPU_sprites
```

**2. Read before coding**
- Review cached docs before implementation
- Provide cached files as context to AI agents
- Reference specific sections when writing SPECs

**3. Update when needed**
- Refresh when troubleshooting fails
- Update when dependency versions change
- Re-cache when external docs are updated

### Version Control Considerations

Whether to commit `.webcache/` depends on project context:

**Don't commit** (add to `.gitignore`):
- Solo projects where you maintain your own cache
- Fast-moving dependencies with frequently changing docs
- Keeping repository lean is priority
- Docs can be rebuilt from URLs

**Do commit**:
- Team projects where everyone needs same documentation
- Archived projects where external docs might disappear
- Onboarding efficiency (docs available immediately)
- Stable dependency versions with locked documentation

Default: `.gitignore` it. But shared caches benefit team coordination.

## Learning Documents Structure

Create focused documents that distill external knowledge for project use:

### Directory Organization

```
learnings/
  architecture.md          # Core system architecture
  api_reference.md         # API patterns and examples
  constraints.md           # Known limitations and gotchas
  integration_patterns.md  # How systems connect
  .ddd/                    # Meta-learning artifacts
    5_open_questions.md    # Questions spawned from study
```

**Non-recursive pattern**: Each learning doc covers one major topic. Avoid deep nesting.

### Content Guidelines

**Learning documents should contain:**
- **Condensed theory** from external sources (not copy-paste, synthesis)
- **Key concepts** essential for implementation
- **Known constraints** documented in source material
- **Attribution links** to original documentation
- **Cross-references** to cached documentation
- **Open questions** marked inline (linked to central tracker)

**Learning documents should NOT contain:**
- Experimental findings (those go in toy LEARNINGS.md)
- Copy-pasted documentation (condense, don't duplicate)
- Implementation code (reference via links only)
- Speculative assumptions (mark clearly if included)

### Attribution Practice

Always attribute external sources:

**Markdown footer pattern:**
```markdown
---

**Sources:**
- NESdev Wiki: [PPU Sprites](https://www.nesdev.org/wiki/PPU_sprites)
- Rust Documentation: [std::collections](https://doc.rust-lang.org/std/collections/)

**Cached:** `.webcache/nesdev_wiki_ppu_sprites.md`, `.webcache/rust_std_collections.html`
```

This enables:
- Verification of condensed information against sources
- Re-fetching when updates needed
- Academic integrity in knowledge synthesis
- AI agents understanding source authority

## When External Knowledge Helps

External knowledge capture pays dividends in specific situations:

**High value scenarios:**
- Complex APIs with comprehensive documentation
- Domain knowledge requiring study (NES hardware, cryptography, protocols)
- Reference implementations providing ground truth
- Tutorial series teaching unfamiliar concepts
- Troubleshooting documentation for known issues

**Lower value scenarios:**
- Simple, well-known patterns (array iteration, basic I/O)
- Minimal external documentation available
- Trial-and-error faster than reading docs
- Documentation known to be outdated or unreliable

**The heuristic:** If you'll reference it 3+ times, cache it. If AI agents will need it for implementation, cache it.

## Integration with AI Workflow

Cached documentation supercharges AI-assisted development:

**Provide as context:**
- AI agents can read local documentation files
- More reliable than LLM training data (version-specific)
- Prevents hallucination of API details
- Enables accurate implementation first try

**Example workflow:**
```markdown
# In SPEC.md
External dependencies:
- FastMCP middleware: See `.webcache/fastmcp_server_middleware.md`
- PyO3 bindings: See `.webcache/pyo3_getting_started.md`

Implementation should follow patterns documented in cached references.
```

AI reads cached docs, generates implementation matching documented APIs, reduces trial-and-error cycles.

## RTFM Before Features

Make reading documentation a required practice, not optional:

**Planning phase:**
1. Identify dependencies/APIs needed
2. Fetch and cache relevant documentation
3. Read critically (note gaps, inconsistencies, open questions)

**SPEC.md phase:**
- Reference specific documentation sections
- Note external contract requirements
- Document assumptions based on reading

**Implementation phase:**
- Provide cached docs to AI as context
- Reference while implementing
- Validate behavior matches documentation

**Troubleshooting phase:**
- Re-read cached docs before debugging
- Refresh cache if docs suspected stale
- Update learning documents with discoveries

**The principle:** Reading is not optional. External knowledge is as important as internal design.

## Maintaining Learning Documents

Learning documents are living artifacts during Research mode, stable references afterward:

**During active research:**
- Update frequently as understanding deepens
- Add cross-references between related documents
- Spawn open questions as gaps discovered
- Mark sections with confidence levels if uncertain

**After research phase:**
- Serve as stable reference material
- Update only when external sources change
- Validate against Discovery findings (mark divergences)
- Archive outdated information rather than deleting

**Update triggers:**
- Dependency version upgrades
- External documentation corrections
- Discovery mode findings contradict theory
- Integration reveals undocumented behavior

Learning documents bridge external knowledge and experimental validation. They're neither code nor static reference—they're curated knowledge.

## Anti-Patterns

**Don't:**
- Copy-paste documentation verbatim (condense and attribute instead)
- Skip attribution (always link sources)
- Mix external theory with experimental findings (separate concerns)
- Let cached documentation become stale unknowingly
- Cache documentation you'll never reference again

**Do:**
- Condense external sources into essential concepts
- Attribute sources clearly and completely
- Keep external knowledge separate from experimental findings
- Refresh caches when troubleshooting or upgrading
- Cache selectively (high-value documentation only)

**The balance:** Comprehensive coverage of what matters, sparse coverage of what doesn't.

## Tools and Automation

Projects often develop custom tooling for documentation management:

**Example patterns:**
```bash
# Fetch and cache wiki page
./tools/fetch-wiki.sh PageName

# Add attribution footer to learning doc
./tools/add-attribution.pl learnings/feature.md

# Check for stale cached documentation
./tools/check-cache-freshness.sh
```

These tools reduce friction in the research workflow. Build them when repetition emerges.

---

External knowledge capture is the foundation of Research mode. Done well, it prevents false starts, enables AI-assisted implementation, and creates durable reference material for the project lifecycle.
