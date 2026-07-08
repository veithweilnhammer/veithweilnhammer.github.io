# Evidence

**Thesis:** Accurate prediction and genuine understanding are separable
achievements — a system can forecast the next observation extremely well while
grasping nothing about the causes behind it — so predictive success, in a model
or a brain, is not by itself evidence of comprehension.

## Verified claims and sources (union of the three drafts)

1. **The Ptolemaic system predicted planetary positions accurately for centuries
   using a geometrically false, Earth-centered model.** Ptolemy's *Almagest*
   (c. 150 CE) used epicycles, deferents, eccentric centers, and the equant to
   reproduce observed planetary motion, including retrograde loops, and remained
   the standard predictive tool for astronomers until the early seventeenth
   century.
   Sources: Kuhn, T. S. (1957), *The Copernican Revolution* —
   https://archive.org/details/copernicanrevolu00kuhn ;
   Encyclopaedia Britannica, "Ptolemaic system" —
   https://www.britannica.com/science/Ptolemaic-system ;
   Encyclopaedia Britannica, "Almagest" —
   https://www.britannica.com/topic/Almagest ;
   Wikipedia, "Deferent and epicycle" / "Equant" —
   https://en.wikipedia.org/wiki/Deferent_and_epicycle ,
   https://en.wikipedia.org/wiki/Equant

2. **Kepler replaced circular epicycles with elliptical orbits (1609),
   superseding the epicycle machinery.** Kepler, *Astronomia Nova* (1609).
   Link: https://en.wikipedia.org/wiki/Astronomia_nova

3. **Ancient astronomy often treated mathematical description/prediction and
   physical explanation as distinct aims**, prioritizing description of the
   apparent motions. Source: O'Connor & Robertson, "Greek astronomy," MacTutor
   History of Mathematics — https://mathshistory.st-andrews.ac.uk/HistTopics/Greek_astronomy/

4. **Large language models are trained by next-token prediction** — given prior
   text, they estimate the probability of the next unit and sample from it.
   Sources: Radford et al. (2019), "Language Models are Unsupervised Multitask
   Learners" (GPT-2) —
   https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf ;
   Brown et al. (2020), "Language Models are Few-Shot Learners" (GPT-3) —
   https://arxiv.org/abs/2005.14165

5. **The "stochastic parrots" argument holds that an LM assembles sequences of
   linguistic form from training-data statistics without reference to grounded
   meaning, while also reproducing biases and harms in its data.** Source:
   Bender, Gebru, McMillan-Major & Shmitchell (2021), "On the Dangers of
   Stochastic Parrots: Can Language Models Be Too Big?", FAccT '21.
   DOI: 10.1145/3442188.3445922

6. **Othello-GPT, a transformer trained only to predict legal Othello moves,
   develops an internal representation of the board that can be decoded and
   causally intervened on** — editing the internal board representation changes
   the model's move predictions as if the board had actually changed. Source:
   Li, Hopkins, Bau, Viégas, Pfister & Wattenberg (2022/ICLR 2023), "Emergent
   World Representations: Exploring a Sequence Model Trained on a Synthetic
   Task" — https://arxiv.org/abs/2210.13382

7. **A follow-up showed the board state is stored in a player-relative ("mine"
   vs. "theirs") frame recoverable by a linear probe.** Source: Nanda, Lee &
   Wattenberg (2023), "Emergent Linear Representations in World Models of
   Self-Supervised Sequence Models" — https://arxiv.org/abs/2309.00941

8. **Probing of Llama-2 found linear encodings of spatial and temporal
   information across several datasets**, interpreted as ingredients of world
   models. Source: Gurnee & Tegmark (2023), "Language Models Represent Space and
   Time" — https://arxiv.org/abs/2310.02207

9. **Predictive-processing accounts describe the brain as continuously
   generating top-down predictions of sensory input and updating on prediction
   error.** Source: Clark, A. (2013), "Whatever next? Predictive brains,
   situated agents, and the future of cognitive science," *Behavioral and Brain
   Sciences* 36(3), 181–204. DOI: 10.1017/S0140525X12000477

10. **The free-energy principle frames the brain as using generative models to
    minimize prediction error / free energy**, one influential version of the
    predictive-brain view. Source: Friston, K. (2010), "The free-energy
    principle: a unified brain theory?", *Nature Reviews Neuroscience* 11,
    127–138. DOI: 10.1038/nrn2787

11. **Causal reasoning requires tools for intervention and counterfactuals that
    go beyond association and prediction.** Source: Pearl, J. (2019), "The seven
    tools of causal inference, with reflections on machine learning." DOI:
    10.1145/3241036

## Quotes

- Li et al. (2022): the internal representation "can be used to control the
  output of the network and create 'latent saliency maps' that help explain
  predictions." (Othello-GPT paper; used as paraphrase in the draft.)
- Bender et al. (2021) coined "stochastic parrot" and characterize such a system
  as assembling linguistic forms by probabilistic co-occurrence without
  reference to meaning. **Modern copyrighted text — paraphrased in the draft,
  not reproduced verbatim.**

## Do not overclaim

- Do not claim LLMs are "just" parrots with no internal structure. Othello-GPT,
  Nanda et al., and Gurnee & Tegmark show next-token training can build usable
  internal representations in at least some settings.
- Do not claim Othello-GPT proves general chatbots "understand" the world. It is
  a small, synthetic, fully specified game with clear rules; generalization to
  natural language is not established.
- "World model" is contested terminology; describe the concrete findings (linear
  decoding, causal editing) rather than lean on the label.
- Do not claim predictive processing says the brain is only a next-token
  predictor or that it settles the metaphysics of comprehension. It is a
  computational account of embodied perception and action.
- Do not imply Ptolemy's system matched modern accuracy or that Ptolemy was
  naive. It was a sophisticated, empirically successful instrument resting on a
  false cosmology — that is the point.
- Do not equate causal understanding with verbal explanation alone; a system may
  hold useful structural knowledge it cannot describe in human terms.
- Do not blur into the Turing-test, anthropomorphism, or empathy-simulation
  arguments (owned by sibling posts).

## Flags

- The boundary between prediction, representation, causal modeling, and
  understanding is philosophical and operational, not settled by one experiment.
- Probing shows information is *present* in activations; whether the model *uses*
  it in the relevant behavior is a separate question (partly addressed by the
  Othello causal-editing result).
- The Ptolemaic example is a simplified historical illustration; scholars differ
  on how to separate Ptolemy's mathematical astronomy from physical cosmology.
  The claim is kept to "accurate enough to remain the standard predictive tool
  for centuries," which is safe.

## Dropped as unverifiable

- Gemini's Andy Clark line ("The predictive brain … continually trying to
  predict the incoming sensory signal," attributed to *Surfing Uncertainty*,
  2016) is labeled "paraphrased/quoted" and could not be confirmed verbatim. It
  is not used as a direct quotation; the same idea is carried by the verified
  Clark (2013) citation.
- Gemini's "person operating a machine by rote" story and the "heavy rock vs.
  feather" line are illustrations, not sourced facts; the rote-competence point
  is retained through the sourced Ptolemy and Pearl material instead.

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
occasional backward drift across the sky, closely enough to guide calendars and
navigation, and it stayed the standard predictive tool until Kepler swapped the
circles for ellipses in the early seventeenth century.

The Ptolemaic system is a clean case of a general fact: a model can forecast what
a system will do while being mistaken about why the system does it. Predicting
the next observation and understanding the causes behind it are separate
achievements, and either can occur without the other. A system that predicts well
has shown that it captured some regularity in the data. It has not, by that
success alone, shown that it grasped the structure that generates the data.
Reading accurate prediction as proof of comprehension is a specific inferential
mistake, and it is worth seeing clearly, because the same mistake is now made
about large language models and about the brain.

Start with what each word is doing. Prediction, in the sense that matters here,
is forecasting the next observation from the preceding ones — where Mars will
appear, which word comes next, how a patient's blood pressure will move over the
next hour. Understanding is having a grip on the causal or structural reasons
those observations take the values they do, the kind of grip that lets you say
what would happen if the situation were changed in some specific way. The two
usually travel together, which is why it is easy to treat them as one thing.
Someone who understands tides can also predict them. But they come apart at the
edges, and the edges are where the interesting questions live. You can predict
without understanding, as Ptolemy did, by fitting a flexible enough description
to the appearances. You can also understand without predicting well, as a
physician who knows exactly how a fever is produced still cannot say which hour
it will break.

This distinction has become the whole content of a live argument about language
models. A large language model is trained to do one thing: given a stretch of
text, estimate the probability of the next token, the next chunk of characters,
and sample from that distribution. Repeat this across most of the written
internet and the result is a system that produces fluent, on-topic, frequently
correct text. Modern chatbots layer on instruction tuning, reinforcement
learning, tool use, and retrieval, but the central capability still grows out of
that predictive objective. The fluency is real and worth taking seriously. The
question is what to infer from it. One reading, associated with the 2021
"stochastic parrots" paper by Emily Bender, Timnit Gebru, and colleagues, treats
the fluency as sophisticated pattern completion: the model assembles sequences of
linguistic form according to how often such forms co-occur in training data, with
no purchase on what any of it means. A competing reading treats the same fluency
as a sign that, to predict text about the world this well, the model must have
built some internal representation of the world the text describes. Both sides
are looking at identical behavior. They disagree only about whether that behavior
licenses the further claim of understanding. The dispute is the
prediction-versus-understanding question, restated for transformers.

What settles a question like this is not more staring at the output. It is
evidence about the internal process, and for once there is a clean example of how
to get it. Kenneth Li and colleagues trained a small transformer, Othello-GPT,
to do nothing but predict legal moves in the board game Othello, feeding it only
sequences of moves with no picture of the board and no rules. If prediction were
always shallow, the model would have learned move-to-move correlations and
stopped there. Instead, probing its internal activations recovered the full state
of the eight-by-eight board at each step, and a later analysis showed the board
is stored in a tidy player-relative frame, the squares that are currently mine
versus currently yours. The decisive step was causal: when the researchers
reached in and edited that internal board representation, flipping a square, the
model's move predictions changed to match the altered board, as though the game
had really gone differently. The model had built a working model of the game and
used it to predict. Prediction produced something that deserves to be called an
internal model of the domain.

Othello-GPT cuts against the flat "just a parrot" claim, and it cuts against the
opposite claim just as hard. What it shows is that you cannot tell from the
forecasts alone whether prediction rests on a real model or on surface
correlation. Two systems can post identical predictive scores while one carries a
structured internal model and the other leans on shortcuts, and the only way to
tell them apart was to open the network and intervene. The behavior
underdetermines the mechanism. That is why "it predicts well, therefore it
understands" fails as an inference: the premise is consistent with both a system
that understands and a system that has merely fit the appearances, so it cannot
by itself favor either. Othello is also a warning against generalizing too fast.
It is a tiny world with a fully specified state and clear rules, and a model
recovering its board is a modest result next to the claim that a language model
has internalized the structure of the physical and social world. Later work found
that Llama-2 encodes linear representations of space and time — coordinates for
places, dates for events — which makes a pure "surface statistics only" story
harder to hold. But those findings leave the interpretive gap open rather than
closing it. A map-like encoding of cities can help predict text about geography
while saying nothing about whether the model tracks how transport, borders, and
economies change when something intervenes. The method transfers across these
cases; the conclusion has to be earned separately in each one.

The same caution applies, pointing the other way, to the brain. Over the past two
decades a powerful framework in neuroscience, predictive processing, has recast
perception as prediction. On Andy Clark's and Karl Friston's accounts, the brain
constantly generates top-down guesses about incoming sensory signals and updates
on the mismatch, the prediction error, rather than passively receiving the world.
The framework earns its keep by explaining a wide range of findings, from
illusions to the way expectation shapes what we see. It is tempting to run the
machine argument in reverse: if the brain is a prediction engine, and prediction
is shallow, then perhaps our own grip on the world is shallower than it feels.
The temptation should be resisted for exactly the reason the Othello case gives.
That a process minimizes prediction error tells you its computational job. It
does not, on its own, tell you whether that process built a rich causal model or
is exploiting a serviceable correlation, any more than a model's low next-token
loss tells you which of those it is doing. Predictive success is the thing that
needs explaining in both brains and models, and it cannot serve as its own
explanation.

If prediction alone will not settle understanding, something else has to, and it
is worth being concrete about what. Judea Pearl's account of causal inference is
useful here because it separates three questions that prediction runs together:
what tends to happen next, what happens if you intervene and change a variable,
and what would have happened under a different condition. Predictive accuracy
answers only the first. Three kinds of evidence bear on the other two.
Generalization: does performance hold up on cases drawn from outside the training
distribution, where a surface fit would break but a causal grip would not? Causal
intervention: when you change a variable the system should be tracking, do its
outputs move the way the underlying structure requires, as Othello-GPT's did when
its internal board was edited? Transfer: can what the system learned be
redeployed on a genuinely new task that shares the same deep structure but none
of the surface form? None of these is a perfect test, and each can be gamed, but
together they probe the thing predictive accuracy leaves open — what the system
does when the correlations it memorized stop being available. Ptolemy's model,
pushed outside the regime it was tuned on, would have failed all three, and that
failure would have been more informative than its centuries of accurate
forecasts.

The honest position is empirical rather than sweeping. Some predictive systems
learn genuine internal models because a model is the most efficient way to
compress and forecast their data. Some exploit correlations that collapse the
moment the input drifts out of distribution. Many real systems do both at once,
carrying real structure in one part of a task and a brittle shortcut in another,
and the two are invisible to anyone who only reads the outputs. The practical job
is to find out which case you are in before you rely on the answer.

The reason to insist on the distinction is that the two readings carry a system
in opposite directions once stakes are attached. Read a fluent model's
predictions as comprehension and you get both the hype cycle, in which every
benchmark score is announced as a step toward machines that understand, and the
quieter, more dangerous move of trusting such a system in a setting where being
right for the wrong reasons has a cost. In medicine, law, hiring, and
mental-health support, a model can produce text that matches expert language
while missing the causal structure that makes the expert judgment safe. It can
recommend a plausible next step because similar cases in its training text led
there, while failing to track the hidden variable that should change the
decision. A system that has fit the appearances of a domain can be accurate
across every case you happened to test and wrong in precisely the case that falls
outside them, and its fluency gives no warning, because fluency was never
evidence about the mechanism. Ptolemy's astronomers were not fools, and their
model was not useless; it was an excellent instrument that told you where the
planets would be and nothing true about why. The task with any predictor that
matters, silicon or biological, is to find out which of those two things you are
holding, and to remember that its record of correct guesses will not tell you.

## Further reading

- Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Shmargaret Shmitchell,
  "On the Dangers of Stochastic Parrots," FAccT 2021.
  https://doi.org/10.1145/3442188.3445922
- Kenneth Li et al., "Emergent World Representations," ICLR 2023.
  https://arxiv.org/abs/2210.13382
- Neel Nanda, Andrew Lee, Martin Wattenberg, "Emergent Linear Representations in
  World Models of Self-Supervised Sequence Models," 2023.
  https://arxiv.org/abs/2309.00941
- Wes Gurnee, Max Tegmark, "Language Models Represent Space and Time," 2023.
  https://arxiv.org/abs/2310.02207
- Andy Clark, "Whatever Next? Predictive Brains, Situated Agents, and the Future
  of Cognitive Science," *Behavioral and Brain Sciences*, 2013.
  https://doi.org/10.1017/S0140525X12000477
- Karl Friston, "The free-energy principle: a unified brain theory?", *Nature
  Reviews Neuroscience*, 2010. https://doi.org/10.1038/nrn2787
- Judea Pearl, "The seven tools of causal inference," 2019.
  https://doi.org/10.1145/3241036
- Thomas S. Kuhn, *The Copernican Revolution* (1957), on the Ptolemaic system as
  accurate prediction from a false model.
