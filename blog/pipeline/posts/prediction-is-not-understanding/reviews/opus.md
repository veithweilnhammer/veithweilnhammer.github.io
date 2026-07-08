# Review — Prediction Is Not Understanding, in Brains or in Machines (opus)

Reviewer note: the draft is factually sound, well-structured, and on-brief. Its
weakness is stylistic: it repeatedly reaches for exactly the constructions the
style guide bans hardest ("not X. It is Y", antithesis/"opposite trade" pairs,
negation-definition, punchy setup beats). These are line-level fixes, but there
are enough of them that a merge editor has real work to do.

## 1. Style-guide violations

**(a) Hard ban — "not X. It is Y" negation-definition.** This is the guide's
single biggest ban, and the draft commits it in a load-bearing spot:

> "What settles a question like this is not more staring at the output. It is
> evidence about the internal process, and for once there is a clean example of
> how to get it."

Rewrite: *"A question like this is settled by evidence about the internal
process rather than by the outputs alone, and Othello-GPT is a clean example of
how to get that evidence."* (Also drop "for once there is a clean example" — a
mild flourish.)

**(b) Hard ban — antithesis / "opposite trade" parallel constructions.**

> "Othello-GPT cuts against the flat 'just a parrot' claim, and it cuts against
> the opposite claim just as hard."

Rewrite: *"Othello-GPT undercuts the flat 'just a parrot' claim, and it also
undercuts the confident claim that fluency proves an internal model."* (Name the
second claim instead of gesturing at "the opposite claim just as hard.")

> "Ptolemy's astronomers were not fools, and their model was not useless; it was
> an excellent instrument that told you where the planets would be and nothing
> true about why."

This stacks two negations ("were not fools… was not useless") with an antithesis
tail ("where the planets would be and nothing true about why"). Rewrite: *"The
Ptolemaic model was a sophisticated, empirically successful instrument: it told
astronomers where the planets would appear while resting on a false account of
why they moved."*

> "A system that predicts well has shown that it captured some regularity in the
> data. It has not, by that success alone, shown that it grasped the structure
> that generates the data."

The "has shown… has not shown" pairing is antithesis-for-rhythm. Rewrite:
*"Predicting well shows only that a system captured some regularity in the data;
it leaves open whether the system grasped the structure that generates the
data."*

> "You can predict without understanding, as Ptolemy did, by fitting a flexible
> enough description to the appearances. You can also understand without
> predicting well, as a physician who knows exactly how a fever is produced still
> cannot say which hour it will break."

This is a "you can X / you can also Y" mirrored-trade pair. It is closer to
content than the others, but it still reads as constructed parallelism. Consider
merging into one explanatory sentence or breaking the symmetry so the two
examples don't sit in identical frames.

> "A system that has fit the appearances of a domain can be accurate across every
> case you happened to test and wrong in precisely the case that falls outside
> them…"

"accurate across every case… and wrong in precisely the case" is antithesis for
effect. Rewrite: *"A system that has only fit the appearances of a domain can
pass every case you tested and still fail on the one case that falls outside
your test set…"*

**(c) Hard ban — punchy setup / announcement sentences and fragments for
effect.**

> "Start with what each word is doing."

Imperative announcement opener. Rewrite by folding into the definition: *"The two
words carry precise meanings here."* — then give them.

> "The fluency is real and worth taking seriously. The question is what to infer
> from it."

Two short dramatic beats. Rewrite: *"The fluency is real, and the open question
is what it licenses us to infer about the model's grasp of meaning."*

> "The behavior underdetermines the mechanism."

Short sentence set off for punch. It states a real point but reads as a beat;
either fold it into the preceding sentence or expand it: *"Because two systems
can post identical scores by different means, the behavior underdetermines the
mechanism that produced it."*

**(d) Rhetorical-understatement / "X rather than Y" openers.**

> "The honest position is empirical rather than sweeping."

Rewrite to the positive: *"The right position here is empirical: it depends on the
system."*

**(e) Pseudo-poetic flourish.**

> "But they come apart at the edges, and the edges are where the interesting
> questions live."

"the edges are where the interesting questions live" is a decorative line.
Rewrite: *"But they come apart in the cases that matter most: where a system
predicts well without understanding, or understands without predicting well."*

**(f) Decorative adjective pair / em-dash aside.**

> "…and the quieter, more dangerous move of trusting such a system in a setting
> where being right for the wrong reasons has a cost."

"the quieter, more dangerous move" is mood-building. Rewrite: *"…and the more
consequential mistake of trusting such a system where being right for the wrong
reasons carries a cost."*

**(g) Closing coda — borderline.**

> "The task with any predictor that matters, silicon or biological, is to find
> out which of those two things you are holding, and to remember that its record
> of correct guesses will not tell you."

"silicon or biological" is a decorative parallel and the tail leans slightly
rhetorical. It is close to acceptable given the guide allows a plainly stated
close; tighten to remove the flourish: *"With any predictor that matters, in a
model or a brain, the task is to find out which of the two you have — and its
record of correct guesses will not tell you."*

**What complies (worth keeping):** the opening — *"For roughly fourteen
centuries, astronomers could tell you where Mars would be in the night sky months
in advance, and they did it with a model that was wrong about nearly everything
important."* — is exactly the flat, concrete, problem-first opening the guide
asks for. Jargon is defined on first use (token, epicycle/deferent/equant,
prediction error, predictive processing). Cadence is mostly measured and
information-dense. The three-way evidence list (generalization / causal
intervention / transfer) is substantive, not rhythm-padding, and should stay.

## 2. Factual grounding

Solid overall; every load-bearing claim traces to the candidates' evidence.
Spot-checks:

- **Fourteen centuries / Ptolemaic dominance until Kepler.** Verified: Almagest
  c. 150 CE to Kepler's *Astronomia Nova* (1609) is ~1,459 years ≈ 14.5
  centuries. Matches evidence #1–2. Fine.
- **Othello-GPT causal editing.** Verified against Li et al. (ICLR 2023, arXiv
  2210.13382): editing the internal board representation changes the model's
  move predictions as if the board had changed. The draft's description is
  accurate and matches evidence #6.
- **Player-relative ("mine" vs. "theirs") frame** — matches Nanda et al. (2023),
  evidence #7. **Llama-2 linear space/time encodings** — matches Gurnee &
  Tegmark (2023), evidence #8. Both correctly hedged.
- **Stochastic parrots** attribution (Bender, Gebru et al., 2021) — correct, and
  the draft paraphrases rather than quoting, as the evidence requires.
- **Andy Clark / Karl Friston predictive processing** — paraphrased, no direct
  quote. Good: the evidence explicitly dropped the unverifiable *Surfing
  Uncertainty* quote, and the draft does not use it.

Minor overstatements to watch (not errors, but soften if convenient):
- *"a model that was wrong about nearly everything important"* — rhetorical; the
  evidence's own caution ("do not present Ptolemy as stupid") is honored later,
  so this is acceptable, but "nearly everything important" is a shade strong.
- *"Repeat this across most of the written internet"* — colloquial hyperbole;
  fine for a blog but technically unsupported.
- The physician-and-fever line is an unsourced illustration, not a claimed fact.
  Acceptable as an everyday example.

No unverifiable citations or overclaims of "understanding" were found; the draft
correctly keeps Othello-GPT as a narrow, synthetic result and does not claim it
proves chatbots understand.

## 3. Structure & clarity

Leads with the claim via a concrete case (Ptolemy), then generalizes, then
defines terms, then applies to LLMs, then the brain, then what evidence would
actually settle it, then stakes. The order earns each step and a non-specialist
can follow it start to finish. Two small notes:

- The definitions paragraph ("Start with what each word is doing…") arrives
  *after* the Ptolemy generalization. That ordering is fine, but the punchy
  opener should go (see 1c).
- The Llama-2 material sits inside the long Othello paragraph. It is relevant but
  the paragraph is doing a lot (Othello result + generalization warning + Llama-2
  + interpretive-gap caveat). Consider splitting so the "the method transfers;
  the conclusion is earned separately" point lands cleanly.

## 4. One self-contained argument

Thesis in one sentence: **accurate prediction and genuine understanding are
separable, so predictive success — in a model or a brain — is not by itself
evidence of comprehension.** The post develops exactly this one argument from
start to finish; every paragraph serves it (definition → Ptolemy → LLM debate →
Othello mechanism → brain caution → what evidence counts → stakes). No second
thesis, no branching into a generic "is AI thinking" essay. Good.

## 5. Brief compliance & standalone

All "must cover" items are present: the core distinction; prediction-without-
understanding (Ptolemy); the LLM case (next-token training, stochastic parrots
vs. world models); the brain case used cautiously (predictive processing, Clark
and Friston); why "predicts well, therefore understands" is invalid plus the
generalization/intervention/transfer evidence; and the stakes (hype + misplaced
trust in medicine, law, hiring, mental-health support). Length ~1,868 words, in
the 1,600–2,000 target.

Standalone: no series framing, no next/previous references, no "next time"
teaser, no subscribe/follow CTA. It does not blur into the Turing-test,
anthropomorphism, or empathy-simulation territory owned by sibling posts. Fully
compliant.

## 6. Top 3 priorities

1. **Kill the hard-ban "not X. It is Y" and antithesis/"opposite-trade"
   constructions** (1a and 1b): "not more staring at the output. It is evidence…",
   "cuts against the opposite claim just as hard", "were not fools… was not
   useless; it was…", and the "accurate across every case… and wrong in
   precisely the case" pair. These are the guide's cardinal sins and there are
   several.
2. **Remove the punchy setup/announcement beats** (1c): "Start with what each
   word is doing.", "The fluency is real and worth taking seriously. The question
   is what to infer from it.", "The behavior underdetermines the mechanism." Fold
   each into a full, information-carrying sentence.
3. **Strip the small flourishes** (1e/1f/1g): "the edges are where the
   interesting questions live", "the quieter, more dangerous move", and the
   "silicon or biological" coda — and split the overloaded Othello/Llama-2
   paragraph (3) so the transfer point lands.

---

**Rating: needs-rewrite** — the structure, argument, and facts are sound, but the
draft repeatedly uses the exact hard-ban constructions the style guide was built
to eliminate, so it needs a focused sentence-level rewrite pass (not a structural
one) before it ships.
