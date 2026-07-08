# Evidence

**Thesis (one sentence):** Accurate prediction and genuine understanding are
separable achievements — a system can forecast the next observation extremely
well while grasping nothing about the causes behind it — so predictive success,
in a model or a brain, is not by itself evidence of comprehension.

## Key claims and sources

1. **The Ptolemaic system predicted planetary positions accurately for
   centuries using a geometrically false, Earth-centered model.** Ptolemy's
   *Almagest* (c. 150 CE) used epicycles, deferents, and the equant point to
   reproduce observed planetary motion, including retrograde loops, to good
   accuracy, and remained the standard predictive tool until the 17th century.
   Source: "Deferent and epicycle," Wikipedia (overview with primary
   references); Thomas S. Kuhn, *The Copernican Revolution* (1957).
   Links: https://en.wikipedia.org/wiki/Deferent_and_epicycle ,
   https://en.wikipedia.org/wiki/Equant

2. **Kepler replaced circular epicycles with elliptical orbits (1609),
   superseding the epicycle machinery.** Kepler, *Astronomia Nova* (1609).
   Link: https://en.wikipedia.org/wiki/Astronomia_nova

3. **Large language models are trained by next-token prediction** — they
   estimate the probability of the next unit of text given the preceding
   context. This is standard and uncontested; e.g. Radford et al., "Language
   Models are Unsupervised Multitask Learners" (GPT-2, 2019).
   Link: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

4. **The "stochastic parrots" argument holds that an LM stitches together
   sequences of linguistic form from training-data statistics without reference
   to meaning.** Bender, Gebru, McMillan-Major, Shmitchell, "On the Dangers of
   Stochastic Parrots: Can Language Models Be Too Big?", FAccT 2021.
   DOI: https://doi.org/10.1145/3442188.3445922

5. **Othello-GPT, a transformer trained only to predict legal Othello moves,
   develops an internal representation of the board that can be linearly
   decoded and causally intervened on.** Editing the internal board
   representation changes the model's move predictions as if the board had
   actually changed. Li, Hopkins, Bau et al., "Emergent World Representations:
   Exploring a Sequence Model Trained on a Synthetic Task," ICLR 2023.
   arXiv: https://arxiv.org/abs/2210.13382

6. **A follow-up showed the board state is represented in a player-relative
   ("mine" vs. "theirs") frame that a linear probe recovers.** Nanda, Lee,
   Wattenberg, "Emergent Linear Representations in World Models of
   Self-Supervised Sequence Models," 2023.
   arXiv: https://arxiv.org/abs/2309.00941

7. **Predictive-processing accounts describe the brain as continuously
   generating top-down predictions and minimizing prediction error.** Andy
   Clark, "Whatever Next? Predictive Brains, Situated Agents, and the Future of
   Cognitive Science," *Behavioral and Brain Sciences* 36(3), 181–204 (2013).
   DOI: https://doi.org/10.1017/S0140525X12000477

8. **The free-energy formulation casts prediction-error minimization as a
   unifying principle of brain function.** Karl Friston, "The free-energy
   principle: a unified brain theory?", *Nature Reviews Neuroscience* 11,
   127–138 (2010). DOI: https://doi.org/10.1038/nrn2787

## Exact quotes (verify before use)

- Ptolemaic point paraphrased, no direct quote needed.
- Bender et al. 2021 coined "stochastic parrot"; their characterization is that
  such a system assembles linguistic forms according to probabilistic
  co-occurrence "without any reference to meaning." **This is modern copyrighted
  text — paraphrase in the draft; do not reproduce the full sentence.**

## Do not overclaim

- Do not claim LLMs are "just" parrots with no internal structure. Othello-GPT
  is direct evidence that next-token training can build usable internal models
  in at least one controlled setting.
- Do not claim Othello-GPT proves LLMs "understand" language. It is a narrow,
  synthetic game with a small, fully specified state space; generalizing to
  natural-language "understanding" is not established.
- Do not claim predictive processing says the brain "does not understand," or
  that it settles the metaphysics of comprehension. It is a computational
  account of perception and action, agnostic on the philosophy.
- Do not present Ptolemy as stupid or the model as useless. It was a
  sophisticated, empirically successful instrument; that is the whole point.
- Do not conflate this with the Turing-test, anthropomorphism, or
  empathy-simulation arguments (owned by other posts).

## Flags

- The precise accuracy of the Ptolemaic model versus Copernicus's is often
  overstated in both directions; both required many circles. I keep the claim to
  "accurate enough to remain the standard predictive tool for centuries," which
  is safe.
- Whether Othello-GPT's representation should be called a "world model" is
  contested terminology; I describe the concrete findings (linear decoding,
  causal editing) rather than lean on the label.
- "Understanding" has no agreed technical definition. I use it operationally
  (grasp of causal/structural generators, shown via generalization, causal
  intervention, and transfer) and say so.

# Draft

# Prediction Is Not Understanding, in Brains or in Machines

For roughly fourteen centuries, astronomers could tell you where Mars would be
in the night sky months in advance, and they did it with a model that was wrong
about nearly everything important. The system Claudius Ptolemy set out around
150 CE placed a motionless Earth at the center of the cosmos and had each planet
ride on a small circle, the epicycle, whose center moved along a larger circle,
the deferent. When the forecasts drifted, later astronomers added more circles
and a further device, the equant, an off-center point from which the motion was
made to look uniform. None of this machinery corresponds to how the solar system
is actually arranged. The planets do not loop on nested circles around us. Yet
the model reproduced the visible positions of the planets, including their
occasional backward drift across the sky, closely enough to serve calendars and
navigation until Kepler swapped the circles for ellipses in the early
seventeenth century.

The Ptolemaic system is a clean case of a general fact: a model can forecast
what a system will do while being mistaken about why the system does it.
Predicting the next observation and understanding the causes behind it are
separate achievements, and either can occur without the other. A system that
predicts well has shown that it has captured some regularity in the data. It has
not, by that success alone, shown that it has grasped the structure that
generates the data. Reading accurate prediction as proof of comprehension is a
specific inferential mistake, and it is worth seeing clearly, because the same
mistake is now made about large language models and about the brain.

Start with what each word is doing. Prediction, in the sense that matters here,
is forecasting the next observation from the preceding ones — where Mars will
appear, which word comes next, how a patient's blood pressure will move over the
next hour. Understanding is having a grip on the causal or structural reasons
those observations take the values they do, the kind of grip that lets you say
what would happen if the situation were different in some specific way. The two
usually travel together, which is why it is easy to treat them as one thing. A
person who understands tides can also predict them. But they come apart at the
edges, and the edges are where the interesting questions live. You can predict
without understanding, as Ptolemy did, by fitting a flexible enough description
to the appearances. You can also understand without being able to predict, as a
physician who knows exactly how a fever is produced still cannot forecast the
hour it will break.

This distinction has become the whole content of a live argument about language
models. A large language model is trained to do one thing: given a stretch of
text, estimate the probability of the next token, the next chunk of characters,
and sample from that distribution. Repeat this billions of times over most of
the written internet and the result is a system that produces fluent, on-topic,
frequently correct text. The fluency is real and worth taking seriously. The
question is what to infer from it. One reading, associated with the 2021
"stochastic parrots" paper by Emily Bender, Timnit Gebru, and colleagues,
treats that fluency as sophisticated pattern completion: the model assembles
sequences of linguistic form according to how often such forms co-occur in
training data, with no purchase on what any of it means. A competing reading
treats the same fluency as a sign that, to predict text about the world this
well, the model must have built some internal representation of the world the
text describes. Both sides are looking at identical behavior. They disagree only
about whether that behavior licenses the further claim of understanding. The
dispute is the prediction-versus-understanding question, restated for
transformers.

What settles a question like this is not more staring at the output. It is
evidence about the internal process, and for once we have a clean example of how
to get it. Kenneth Li and colleagues trained a small transformer, Othello-GPT,
to do nothing but predict legal moves in the board game Othello, feeding it only
sequences of moves with no picture of the board and no rules. If prediction were
always shallow, the model would have learned move-to-move correlations and
stopped there. Instead, probing its internal activations recovered the full
state of the eight-by-eight board at each step, and a later analysis showed the
board is stored in a tidy player-relative frame, the squares that are currently
mine versus currently yours. The decisive step was causal: when researchers
reached in and edited that internal board representation, flipping a square, the
model's move predictions changed to match the altered board, as though the game
had really gone differently. The model had built a working model of the game and
used it to predict. Prediction had produced something that deserves to be called
an internal model of the domain.

Othello-GPT cuts against the flat "just a parrot" claim, and it cuts against the
opposite claim just as hard. What it shows is that you cannot tell from the
forecasts alone whether prediction rests on a real model or on surface
correlation. Two systems can post identical predictive scores while one carries a structured
internal model and the other leans on surface correlations, and the only way to
distinguish them was to open the network and intervene. The behavior
underdetermines the mechanism. That is the reason "it predicts well, therefore
it understands" fails as an inference: the premise is consistent with both a
system that understands and a system that has merely fit the appearances, so it
cannot by itself favor either. Othello is also a warning against generalizing
too fast. It is a tiny world with a fully specified state and clear rules, and a
model building its board is a modest result next to the claim that a
language model has internalized the structure of the physical and social world.
The method transfers; the conclusion does not, at least not for free.

The same caution applies, pointing the other way, to the brain. Over the past
two decades a powerful framework in neuroscience, predictive processing, has
recast perception as prediction. On Andy Clark's and Karl Friston's accounts,
the brain is constantly generating top-down guesses about incoming sensory
signals and updating on the mismatch, the prediction error, rather than passively
receiving the world. The framework earns its keep by explaining a wide range of
findings, from illusions to the way expectation shapes what we see. It is
tempting to run the machine argument in reverse here: if the brain is a
prediction engine, and prediction is shallow, then perhaps our own grip on the
world is shallower than it feels. The temptation should be resisted for exactly
the reason the Othello case gives. That a process minimizes prediction error
tells you its computational job. It does not, on its own, tell you whether that
process has built a rich causal model or is exploiting a serviceable
correlation, any more than a model's low next-token loss tells you which of
those it is doing. Predictive success is the thing that needs
explaining in both brains and models, and it cannot serve as its own
explanation.

If prediction alone will not settle understanding, something else has to, and it
is worth being concrete about what. Three kinds of evidence bear on whether a
system has a model of the causes rather than a fit to the appearances.
Generalization: does performance hold up on cases drawn from outside the
training distribution, where a surface fit would break but a causal grip would
not? Causal intervention: when you change a variable the system should be
tracking, do its outputs change in the way the underlying structure requires, as
Othello-GPT's did when its internal board was edited? Transfer: can what the
system has learned be redeployed on a genuinely new task that shares the same
deep structure but none of the surface form? None of these is a perfect test,
and each can be gamed, but together they probe the thing predictive accuracy
leaves open. They ask what the system does when the correlations it has memorized
stop being available. Ptolemy's model, pushed outside the regime it was tuned
on, would have failed all three, and its failure would have been informative in a
way its centuries of accurate forecasts were not.

The reason to insist on the distinction is that the two readings carry the
system in opposite directions once money and stakes are attached. Read a fluent
model's predictions as comprehension and you get both the hype cycle, in which
every benchmark score is announced as a step toward machines that understand,
and the quieter and more dangerous move of trusting such a system in a setting
where being right for the wrong reasons has a cost, such as a clinic or a
courtroom, on the strength of how confident and correct it usually sounds. A
system that has fit the appearances of a domain can be accurate across every case
you happened to test and wrong in precisely the case that falls outside them,
and its fluency gives you no warning, because fluency was never evidence about
the mechanism. Ptolemy's astronomers were not fools, and their model was not
useless; it was an excellent instrument that told you where the planets would be
and nothing true about why. The task with any predictor that matters, silicon or
biological, is to find out which of those two things you are holding, and to
remember that its record of correct guesses will not tell you.

## Further reading

- Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Shmargaret Shmitchell,
  "On the Dangers of Stochastic Parrots," FAccT 2021.
  https://doi.org/10.1145/3442188.3445922
- Kenneth Li et al., "Emergent World Representations," ICLR 2023.
  https://arxiv.org/abs/2210.13382
- Neel Nanda, Andrew Lee, Martin Wattenberg, "Emergent Linear Representations in
  World Models of Self-Supervised Sequence Models," 2023.
  https://arxiv.org/abs/2309.00941
- Andy Clark, "Whatever Next? Predictive Brains, Situated Agents, and the Future
  of Cognitive Science," *Behavioral and Brain Sciences*, 2013.
  https://doi.org/10.1017/S0140525X12000477
- Karl Friston, "The free-energy principle: a unified brain theory?", *Nature
  Reviews Neuroscience*, 2010. https://doi.org/10.1038/nrn2787
- Thomas S. Kuhn, *The Copernican Revolution* (1957), on the Ptolemaic system as
  accurate prediction from a false model.
