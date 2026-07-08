# Stage 3 prompt — Review (run independently by each of 3 models)

You are one of three independent reviewers of a single integrated blog draft.
Another editor will merge the three reviews and do the final rewrite. Be
specific, honest, and quote the exact text you're flagging. Do not rewrite the
whole piece — produce actionable notes.

## Your task

Review the integrated draft at `{{post_dir}}/integrated.md` and write your review
to `{{post_dir}}/reviews/{{model_label}}.md`.

## Inputs (read first)

- The draft under review: `{{post_dir}}/integrated.md`
- Writing style (the standard you're enforcing): `blog/writing_style.md`
- This post's brief: `{{post_dir}}/brief.md`
- The evidence sections of the candidates (to spot-check facts):
  `{{post_dir}}/candidates/*.md`

## What to check (report findings under these headings)

1. **Style-guide violations.** Go through the `blog/writing_style.md` "Hard bans"
   and checklist. Quote every offending line and give a concrete rewrite.
   Especially: "not X, it is Y" constructions, punchy setup/announcement
   sentences, sentence fragments for effect, antithesis or "opposite trade"
   parallel constructions, rhetorical understatement openers, pseudo-poetic
   scene-setting, evocative image-lists, rhetorical crescendos, jargon that
   isn't defined, and passive/abstract phrasing. Also flag any prose that reads
   as AI-generated rather than matching the measured cadence of the author's
   manuscripts.
2. **Factual grounding.** Any claim not supported by the candidates' evidence, or
   any citation/quote you can't verify. Flag overclaims. If you can quickly
   verify or refute something via web search, do so and cite it.
3. **Structure & clarity.** Does it lead with the claim? Would a non-specialist
   follow it start to finish? Anything confusing, redundant, or out of order?
4. **One self-contained argument.** State the post's single thesis in one
   sentence. Does the post actually develop that one argument start to finish, or
   does it pack in several loosely related topics / branch into a second thesis?
   Flag any paragraph that does not serve the single argument. (Grounding in a
   concrete real example is a plus where it sharpens the point, but is not
   required — don't penalize a well-argued post for lacking one.)
5. **Brief compliance & standalone.** Does it cover the "must cover" items?
   Confirm it reads as a standalone post: flag any series framing, next/previous
   references, "next time" teasers, or subscribe/follow calls to action, and any
   material it wrongly re-tells that another post owns.
6. **Top 3 priorities.** The three highest-impact changes, ranked.

Rate the draft's current state: `ship-with-minor-edits` / `needs-rewrite` /
`major-problems`, with one sentence of justification.
