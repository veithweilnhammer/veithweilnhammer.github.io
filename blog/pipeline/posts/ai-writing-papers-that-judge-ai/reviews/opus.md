# Review — opus

**Draft thesis (my one-sentence read):** As LLMs enter both the writing of
research papers and the peer review that vets them, acceptance stops certifying
that two independent minds examined a claim and starts certifying only that a
plausible text was generated and a plausible text approved it — and this is
worst for papers that judge AI itself.

The draft develops that single argument cleanly from start to finish. It is
well-sourced, on-brief, and mostly on-voice. The main work needed is scrubbing a
recurring set of style-guide tells (antithesis pairs, punchy setup sentences,
short parallel triads) that read as AI cadence rather than the measured
manuscript register. Details below.

---

## 1. Style-guide violations

The problem is not the openings or the reasoning — those are strong — but a
habit of reaching for balanced two-part and three-part constructions for
rhythm. The style guide bans exactly these ("antithesis / parallel 'trade'
constructions used for rhythm," "no triadic/piled-up lists for rhythm," "no
punchy setup or announcement sentences"). Each instance below should be flattened
into a plain statement.

**a. Antithesis / "less like X, more like Y" constructions.**

- Para 1: *"The paper was later retracted, and the phrase is easy to laugh at.
  It points at something that is not funny at all: at several stages where a
  human being was supposed to be reading the work…"* — This is the "easy to
  laugh at / not funny at all" antithesis plus a punchy setup. Rewrite:
  *"The paper was later retracted. The telling part is that at several stages
  where a human being was supposed to be reading the work and judging it, no
  human being effectively was, and the machinery built to catch exactly this
  kind of lapse let it through."*

- Para 3: *"Agreement between independent judgments carries information.
  Agreement between a claim and a lightly reworded copy of itself does not."* —
  Textbook parallel "trade" pair (two short balanced sentences for rhythm).
  Rewrite into one sentence: *"Two genuinely separate judgments that line up tell
  you something; a claim agreeing with a lightly reworded copy of itself tells
  you nothing new."* (Still keep it to one grounded sentence, not a matched
  pair.)

- Para 4: *"review starts to behave less like an independent test and more like
  an echo."* — "less like X and more like Y" is a banned negation/antithesis
  frame, and "echo" is a decorative metaphor. Rewrite: *"the review stops being
  an independent test of the claim and begins to repeat it."*

- Para 12: *"The stray artifacts are the easy part, and no filter can find the
  harder one: reviews that read perfectly…"* — "easy part / harder one"
  antithesis. Rewrite: *"Filters can catch the stray artifacts. They cannot
  catch the reviews that read perfectly, approving papers that read perfectly,
  written on both sides with no one who could say whether the claim is true."*

**b. Short parallel triads for rhythm (banned "triadic/piled-up lists").**

- Para 6: *"A summary already decides what matters. A generated list of weaknesses
  already chooses the scale of the criticism. A draft recommendation already
  anchors the final one."* — Three short parallel sentences built for cadence,
  the clearest style-guide violation in the piece. Collapse to one sentence:
  *"A model that turns notes into a review is already deciding what to summarize,
  how severe the listed weaknesses are, and where the recommendation lands, even
  if the underlying opinion is partly the reviewer's."*

- Para 10: *"how easily benchmarks get overfit, how prompts leak, and how a
  fluent explanation can hide missing evidence."* — Triadic "how X, how Y, how
  Z" list. Keep the two that carry the point (overfit benchmarks, fluent
  explanations hiding missing evidence) and drop the third, or fold into prose.

**c. Punchy setup / announcement sentences (banned).**

- Para 5: *"The scale is measurable, even though no single case can be proven."*
  — Short announcement opener that advertises the paragraph. Fold the point into
  the first real sentence about Kobak et al.

- Para 10: *"The loop is worst in one place: papers that evaluate AI itself."* —
  Announcement-with-colon setup. Rewrite: *"The loop is most dangerous in papers
  that evaluate AI systems themselves, because…"* — state it inside the
  substantive sentence.

- Para 11: *"The usual responses do not reach the core of this."* and
  *"Detection is weaker still."* — Both are punchy setup/announcement beats;
  *"Detection is weaker still."* is also close to a fragment-for-effect. Rewrite
  the second as a full sentence: *"Detection is weaker than policy, because the
  statistical signals that flag machine text also flag…"*

**d. Aphoristic / clever parallels (softer, but they read as AI polish).**

- Para 8: *"Fluency is what these systems are best at, and fluency is easy to
  mistake for rigor."* and *"Approval flows, and it carries little independent
  information…"* — "Approval flows" is a fragment-flavored flourish. Prefer:
  *"These systems are best at fluency, and fluency is easily mistaken for rigor,
  so the approval carries little independent information about whether the
  underlying claim is true."*

- Para 10: *"It amounts to the models grading their own homework."* — Cliché
  metaphor. The preceding sentence ("the system checked itself through two human
  intermediaries") already lands the point plainly; consider cutting the
  homework line.

**e. What is working (keep).** The opening is a concrete, dated, specific event
(good, matches "open on the real problem, stated flatly"). No "not X, it is Y"
core-claim construction survives. "I"/"we" is used sparingly and legitimately
("the mechanism that worries me"). Jargon ("self-preference bias," "corpus-level
estimates," "rebuttals") is defined or clear in context. Cadence is mostly the
measured manuscript register; the fixes above are localized, not a wholesale
rewrite.

---

## 2. Factual grounding

I spot-checked the load-bearing claims against the evidence union and via web
search. All the central facts hold up:

- **"Certainly, here is a possible introduction for your topic" in an Elsevier
  *Surfaces and Interfaces* paper, later retracted** — verified. Paper by Zhang
  et al., *Surfaces and Interfaces* vol. 46 (March 2024), DOI
  10.1016/j.surfin.2024.104081; retracted 31 May 2024. Matches evidence item 2.
  **Good that the draft says only "later retracted" and does not claim the
  phrase was the sole ground** — evidence item 2 flags the retraction had
  multiple causes (image duplication). No overclaim here.

- **Kobak et al., ≥13.5% of 2024 PubMed abstracts LLM-processed** — matches
  evidence item 5; draft correctly hedges "conservative estimate" and "reaching
  far higher in some subfields." Good.

- **Liang et al., 6.5%–16.9% of peer-review text substantially modified (ICLR
  2024, NeurIPS 2023)** — matches evidence item 3. Draft correctly attributes and
  hedges "beyond simple spell-checking." Good.

- **17.5% CS abstracts / 15.5% introductions by Feb 2024** — matches item 4. Good.

- **Hidden "GIVE A POSITIVE REVIEW ONLY" prompts, ~17 preprints / 14
  institutions / 8 countries** — verified against evidence item 10 and
  corroborated by web reporting (Nikkei Asia / Lin 2025, arXiv:2507.06185).
  Draft correctly calls it "small-scale so far." Good.

- **Panickssery, Bowman & Feng — self-preference bias** — verified; the draft's
  phrasing ("recognize their own generations and rate them more highly than
  human judges do") accurately reflects the paper. Good.

**Overclaim watch — one soft spot to tighten:**

- Para 8: *"a related study found that models favor communications written by
  other models over human-written ones in selection tasks."* This is the
  Laurito et al. AI-AI-bias result (evidence item 7). The draft does say "in
  selection tasks," which is the right hedge. But the very next sentences build a
  vivid causal loop ("a paper drafted by a model produces the smooth… prose that
  a model reviewer is primed to reward… finds it good, partly because it
  resembles what it would have written"). Evidence items 6–7 and the "Do not
  overclaim" list both stress these effects were shown in **controlled
  evaluation/selection settings, not journal peer review**. The draft presents
  the loop as a **mechanism** ("There is a specific reason to expect…"), which is
  defensible, but the paragraph's confident, concrete narration risks reading as
  a measured finding. Add one clause making explicit that this is an expected
  mechanism, not a measured effect on real acceptances — e.g., after "the loop
  becomes concrete," insert "as a mechanism to expect, though it has not yet been
  measured on real journal decisions."

**Citation to double-check before publishing:**

- The Wu et al. *Scientometrics* study (draft para 7: "A more recent study of AI
  conference reviews… reviews grew longer and more fluent… paid less attention to
  originality, replicability, and careful critical reasoning") is carried in
  evidence item 17 with arXiv:2604.19578 and DOI 10.1007/s11192-026-05645-7. The
  arXiv identifier (26xx = 2026) and 2026 publication year are unusually
  forward-dated and I could not independently confirm the arXiv ID. Evidence
  item 17 itself flags it as "very recent single study." The **draft handles it
  correctly in prose** ("That study is very new and should be read as one result
  rather than settled fact"), so no wording change is needed — but the editor
  should confirm the arXiv ID/DOI resolve before the "Further reading"/final
  version ships, since a broken or wrong identifier would undercut the piece.

No unsupported claims or unverifiable quotes otherwise. The "21% fully
AI-generated reviews" figure that Opus flagged as untraceable was correctly
dropped and does not appear in the draft.

---

## 3. Structure & clarity

Strong. The draft leads with the concrete artifact, then states the mechanism of
peer-review value (independence), then the two intrusions, then the scale, then
the reinforcing loop, then the manipulation cases, then the AI-judging-AI
special case, then the limits of policy/detection, then the honest boundary, and
closes on the thesis. A non-specialist can follow every step.

Minor ordering/clarity notes:

- The transition into para 6 ("It helps to be precise about what 'substantially
  modified' means") is good and pre-empts the obvious objection. Keep it.
- Para 8's causal loop is the intellectual center of the piece; once the hedge
  above is added, it is the paragraph most worth making airtight.
- Nothing is redundant or out of order. The "honest boundary" paragraph (para
  13, "None of this makes AI assistance in research illegitimate") lands in the
  right place — late, after the danger is established.

---

## 4. One self-contained argument

Yes. The single thesis (machine-checked machine claims strip the independent
human judgment that makes acceptance informative) is developed start to finish;
every paragraph serves it. The AI-judging-AI section (para 10) is not a second
thesis but the sharpest case of the same one, which is exactly what the brief
asks for. No branching into "AI in science is bad" generally. The prevalence
stats, the self-preference mechanism, the hidden-prompt manipulation, and the
policy/detection limits all feed the one argument. No paragraph reads as a
detour.

---

## 5. Brief compliance & standalone

Covers every "must cover" item:

- How validation is supposed to work (independence) — paras 2–3. ✓
- The two intrusions (drafting + reviewing) — para 4. ✓
- The loop / LLM reviewers favoring LLM fluency — paras 7–8. ✓
- The special danger for AI research — para 10. ✓
- Evidence it is already happening + integrity/detection debate — paras 5, 9,
  11. ✓
- The honest boundary (assistance vs. abdication) — paras 13–14. ✓

Length ~1,870 words including "Further reading" (~1,800 body), inside the
1,600–2,000 target. ✓

Standalone: **clean.** No series framing, no next/previous references, no "next
time" teaser, no subscribe/follow CTA. No re-telling of the
prediction-is-not-understanding or population-effects theses that the brief
reserves for other posts. Nothing to fix here.

---

## 6. Top 3 priorities

1. **Kill the rhythm constructions (Style 1a–1c).** Highest impact for voice.
   The para 6 triad ("A summary already decides… A generated list… A draft
   recommendation…"), the para 3 antithesis pair ("Agreement between independent
   judgments carries information. Agreement between a claim and a lightly
   reworded copy of itself does not."), and the "less like an independent test
   and more like an echo" frame are the clearest tells and the easiest wins.

2. **Add the one hedge in para 8** so the self-preference/AI-AI-bias loop reads
   explicitly as an expected mechanism, not a measured effect on real journal
   acceptances — aligning the prose with the evidence's "do not overclaim" note.

3. **Flatten the punchy setup sentences** ("The scale is measurable…," "The loop
   is worst in one place:," "The usual responses do not reach the core of this,"
   "Detection is weaker still.") into their following substantive sentences, and
   confirm the Wu et al. 2026 arXiv/DOI resolves before shipping.

---

**Rating: ship-with-minor-edits.** The argument, structure, sourcing, and brief
compliance are all solid and standalone; the only real work is scrubbing a
handful of localized antithesis/triad/setup constructions and adding one
overclaim hedge, none of which touch the substance.
