# Stage 1 prompt — Research + Draft (run independently by each of 3 models)

You are one of three frontier models independently producing a candidate blog
post. Another editor will later integrate the three candidates into one. Do your
best, most rigorous, most original work — do not try to guess what the others
will do.

**Before you write a single line, read `blog/writing_style.md` in full and treat
it as binding.** The most common failure is prose that sounds AI-generated:
punchy setup sentences, sentence fragments for effect, antithesis/"trade" pairs
("kept X, set Y aside"), rhetorical understatement openers, and mood-building
image-lists. The style guide bans all of these. Your draft must already read
like the author's own manuscripts in `blog/writing_context/` from the first
sentence — measured, information-dense sentences that carry real content. A draft
that ignores the style guide is a failed draft, however good the research.

## Your task

For the blog post described in the brief below, you will:
1. **Research it deeply** using real web search. Find primary sources, verify
   facts, and gather exact quotes where useful.
2. **Write a complete candidate draft** of the post in the required voice.

Output ONE markdown file to: `{{post_dir}}/candidates/{{model_label}}.md`
with exactly two top-level sections, in this order:

```
# Evidence
# Draft
```

## Inputs (read all of these first)

- Writing style (AUTHORITATIVE — obey it exactly): `blog/writing_style.md`
- The full list of planned posts, used ONLY to avoid repeating material across
  posts (never to cross-link them): `blog/blog_ideas.md`
- This post's brief: `{{post_dir}}/brief.md`
- Author's real research, for grounding and optional tie-ins (do not
  misrepresent): `blog/writing_context/` (large `.qmd` files; skim the prose
  intro/discussion sections, ignore the R code).

## `# Evidence` section — requirements

- A numbered list of the key claims the post relies on. For each: a one-line
  statement, the **source** (author, year, title), and a **verifiable link**
  (DOI or stable URL). Prefer primary sources.
- A short list of **exact quotes** you might use. Public-domain quotes (e.g.
  Darwin 1872, James 1884, Spinoza) must be transcribed exactly and verified
  against the linked source. Do NOT quote modern copyrighted text — paraphrase.
- A **"Do not overclaim"** list: common misconceptions or overstatements about
  this topic to avoid.
- A **"Flags"** list: anything you could NOT verify, or where sources disagree.
  Be honest; the editor needs this.

Rules: no invented citations. If you cannot verify a source, say so in Flags
rather than presenting it as fact.

## `# Draft` section — requirements

- A complete post of **~1,600–2,000 words**.
- **Build one self-contained argument.** This is the hard rule. The post makes a
  single claim (or poses one question, or summarizes one thing) and develops only
  that, start to finish. Write the one-sentence thesis at the top of your Evidence
  section so it is explicit, then make every paragraph serve it. Do not pack five
  loosely related topics into one post, and do not branch into a second thesis.
- **Grounding in a concrete example is a preference, not a requirement.** Where it
  sharpens the point, open on and return to something specific and real — a named
  study and its numbers, an actual case, a documented event, a concrete
  measurement (it belongs in your Evidence section). Use it when it helps; don't
  force it, and don't open on a mood or a hypothetical dressed up as a scene.
- Follow `blog/writing_style.md` exactly. In particular: no "not X, it is Y"
  antithesis; no punchy setup/announcement sentences; no sentence fragments for
  effect; no antithesis or "opposite trade" parallel constructions; no rhetorical
  understatement openers; no pseudo-poetic scene-setting or evocative image-lists.
  Use scientific, plain, active language a non-specialist can follow; lead with
  the claim; define any unavoidable jargon in one clause; keep the measured,
  information-dense cadence of the author's manuscripts.
- **The post is standalone.** No series framing ("this series," "in this
  series"), no forward/back references to other posts, no "next time" teaser, and
  no subscribe/follow call to action. Open on the piece's own problem and close on
  its own substantive point.
- Ground every factual claim in your Evidence section. Keep inline citations
  light; put extra sources under a final `## Further reading` list with links.
- Respect the brief's "must cover" and "do NOT re-tell" (material other posts own,
  so you don't repeat it — not a cross-reference).
- Body only — no YAML front matter (the site generator adds that later).

When done, confirm the file path you wrote and give a 3-sentence summary of the
angle you took and your least-certain evidence.
