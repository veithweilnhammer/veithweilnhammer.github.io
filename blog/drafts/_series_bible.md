# The Moving Mind — series bible (agent context)

Not published. Shared context injected into every agent so 14 independently
written essays read as one series.

## Premise
Movement is the visible surface of mental life. The series argues in stages that
action and perception are one inferential loop; that psychiatry's reliance on
words leaves most of the mind unmeasured; and that new tools could recover a
science of movement *and* meaning — if we resist mistaking data for empathy.

## Voice
Essayistic, historically grounded; one foot in the humanities (Darwin, James,
Merleau-Ponty, Goffman), one in computational neuroscience (Wolpert, Friston).
Open each essay on a concrete scene, then turn to argument. First person where
natural. ~2,000 words (1,800–2,200). Exemplars: the two drafts in `blog/idea.md`
and the published posts in `_posts/`.

## Anchor-story ownership (narrate in full ONLY in the owning post; elsewhere at
most a one-clause allusion — never re-tell)
- Darwin's *Expression of the Emotions* / trembling lip → #1
- The poker "tell" → #2
- Ekman & Friesen FACS / affective computing → #3
- Merleau-Ponty + James–Lange ("afraid because we tremble") → #4
- Wolpert & Kawato internal models / active inference → #5
- Kraepelin / Bleuler / Andreasen (psychomotor signs) → #7
- Catatonia & the breakdown of attunement → #8
- Insel RDoC / limits of self-report → #9
- Onnela & Rauch digital phenotyping → #10
- MAILA (author's own work) → #11
- Phrenology / polygraph / micro-expression → #12
- Mittelstadt ethics of measurement → #13
- Saxe / theory of mind / a new vocabulary → #14

## Recurring motifs (weave in, never state as a checklist, never repeat verbatim)
symptom vs expression · inference under uncertainty · inherited mind–body
dualism · attunement/synchrony · leakage vs concealment · data ≠ empathy.

## Cross-links
Linear series. Each post links back to the previous entry and forward to the
next (by title). First and last posts carry a subscribe CTA.

## Sourcing rules
- Every reference must be real and verifiable (prefer DOI / stable URL). No
  invented citations. Cross-check against `_bibliography/papers.bib` and Zotero
  where relevant.
- Public-domain quotes (Darwin, James, Spinoza) may be quoted exactly, verified
  against the source. Modern copyrighted sources: paraphrase, don't reproduce.
- Flag any claim that cannot be sourced.

## Figures
Only when they earn their place. Data/schematic figures via R + ggplot2 →
`assets/img/<slug>-<n>.png`. No AI-generated images for now. Most essays need none.

## Draft → publish flow
1. Research agent → `blog/drafts/_research_<slug>.md`
2. Writer agent → `blog/drafts/<slug>.md` (body only, ~2,000 words)
3. Review agent → notes appended / applied
4. Land final body into the matching POST block in `blog.qmd`, set `status: ready`,
   add `date`, then run `python3 generate.py`.
