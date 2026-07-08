# Evidence

**Thesis:** Turing's 1950 imitation game measures whether an interrogator can tell
a machine from a person in text-only conversation — an outcome that depends on
observable behavior and human judgment — so recent findings that large language
models "pass the Turing test" show that these systems can produce human-like
conversation without settling whether they understand or think.

## Verified claims and sources

1. **Turing's substitution.** Turing opened "Computing Machinery and Intelligence"
   with the question "Can machines think?" and immediately set it aside, arguing
   that defining "machine" and "think" by ordinary usage would reduce the matter
   to something like a Gallup poll, and replacing the question with the imitation
   game. Source: A. M. Turing (1950), "Computing Machinery and Intelligence,"
   *Mind* 59(236): 433–460. https://doi.org/10.1093/mind/LIX.236.433 (full text
   verified via https://courses.cs.umbc.edu/471/papers/turing.pdf).
2. **The game's structure.** The imitation game is a three-person setup: a man
   (A), a woman (B), and an interrogator (C) who communicates only by typed
   message and must decide which is which; Turing then asks what happens when a
   machine takes the part of a player. The criterion is imitation judged by an
   observer. Source: Turing (1950), Section 1.
3. **Turing's forecast, not a threshold.** Turing predicted that in about fifty
   years a computer could play the game so well that "an average interrogator
   will not have more than 70 per cent chance of making the right identification
   after five minutes of questioning," and called the original question "too
   meaningless to deserve discussion." The 70% figure is a dated prediction about
   interrogator accuracy, not a stated "pass mark." Source: Turing (1950),
   Section 6.
4. **2024 result (peer-reviewed).** In a two-party controlled study, the best
   GPT-4 prompt was judged human 49.7% of the time, versus 66% for real humans,
   22% for ELIZA, and 20% for GPT-3.5; participants reported judging mainly on
   linguistic style and socioemotional cues rather than reasoning. Source:
   Cameron R. Jones & Benjamin K. Bergen (2024), "Does GPT-4 pass the Turing
   test?", *Proceedings of NAACL 2024*. https://doi.org/10.18653/v1/2024.naacl-long.290
5. **2025 result (three-party).** Prompted to adopt a humanlike persona, GPT-4.5
   was judged to be the human 73% of the time — significantly more often than
   interrogators selected the real human it was paired with; LLaMa-3.1-405B
   reached 56% (not significantly different from the humans), while ELIZA and
   GPT-4o were below chance at 23% and 21%. Reported as the first empirical
   passing of a standard three-party Turing test. Source: Cameron R. Jones &
   Benjamin K. Bergen (2025), "Large Language Models Pass the Turing Test,"
   arXiv:2503.23674. https://arxiv.org/abs/2503.23674
6. **Prompt sensitivity.** The same GPT-4.5 model scores near 21% with a plain
   configuration and 73% with a persona prompt, and outcomes vary with the
   interrogator and time limit — evidence that the result measures a
   discrimination task, not a fixed property of the machine. Source: Jones &
   Bergen (2025).
7. **ELIZA.** Joseph Weizenbaum's 1966 pattern-matching script mirrored users'
   sentences back as questions in the style of a Rogerian therapist, with no
   model of meaning, yet users routinely treated it as understanding them. In the
   modern controlled runs it still convinced 22–23% of interrogators. Source:
   Joseph Weizenbaum (1966), "ELIZA," *Communications of the ACM* 9(1): 36–45,
   https://doi.org/10.1145/365153.365168 ; modern fooling rates from Jones &
   Bergen (2024, 2025).
8. **Empirical vs. conceptual question.** The Turing test's afterlife turns
   questions about intelligence into questions about performance and social
   judgment; the empirical question (can a machine pass the game?) is distinct
   from the conceptual one (what does passing warrant about thought?). Source:
   Graham Oppy & David Dowe (2021 rev.), "The Turing Test," *Stanford
   Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/turing-test/
9. **Clinical competence needs task-specific evaluation.** Fluent conversational
   performance is a poor guide to safe clinical decisions, which depend on asking
   for missing information, expressing uncertainty, following safety constraints,
   and weighing error costs. Source: Peter Hager et al. (2024), "Evaluating and
   mitigating limitations of large language models in clinical decision-making,"
   *Nature Medicine*. https://doi.org/10.1038/s41591-024-03097-1

## Exact quotes (verified against Turing 1950, UMBC PDF)

- "I propose to consider the question, 'Can machines think?'"
- "Instead of attempting such a definition I shall replace the question by
  another, which is closely related to it and is expressed in relatively
  unambiguous words."
- "These questions replace our original, 'Can machines think?'"
- "The original question, 'Can machines think?' I believe to be too meaningless
  to deserve discussion."
- "an average interrogator will not have more than 70 per cent chance of making
  the right identification after five minutes of questioning."

## Hedges and flags

- **Eugene Goostman (kept, hedged).** A chatbot was reported in 2014 to have
  "passed" a Turing test at the University of Reading by convincing 33% of judges
  over five-minute chats, using a persona of a 13-year-old non-native English
  speaker to excuse errors. The 33% figure comes from event organizers and press
  coverage (e.g., BBC and The Guardian, 8–9 June 2014), not a peer-reviewed
  study; reported as a claimed result illustrating format-gaming, not a
  controlled finding.
- **Conflicting 2024 figures (resolved).** Gemini/GPT cited the peer-reviewed
  NAACL paper (best GPT-4 prompt 49.7%; humans 66%); Opus cited a related
  preprint (arXiv:2405.08007) reporting 54%/67%. The peer-reviewed NAACL figures
  are used and the preprint dropped as the weaker source.
- **"66% for 2025 humans" (dropped).** Gemini attached a 66% human rate to the
  2025 study; the 2025 abstract states only that GPT-4.5 was picked "significantly
  more often than … the real human," so the specific 66% is not asserted for 2025.
- **Weizenbaum's secretary anecdote (kept, light).** Documented but anecdotal;
  used only to illustrate that observers project understanding onto simple
  systems, not as a measured result.
- **Mechanism claims (scoped out).** Detailed "next-token prediction ≠
  understanding" argument is deliberately not developed here; that forecasting-vs-
  comprehension thesis belongs to a separate post. This post stays on
  indistinguishability as an observer-relative criterion.
- **Volume typo.** Some reproductions mislabel *Mind* volume 59 (1950) as 49; the
  DOI and page range 433–460 are correct.
- **"Turing test" is later shorthand.** Turing's paper mainly uses "imitation
  game."

# Draft

In early 2025, the cognitive scientists Cameron Jones and Benjamin Bergen ran a
controlled version of Alan Turing's imitation game and reported a result the field
had discussed for seventy-five years. Human interrogators held five-minute typed
conversations with two hidden partners at once, one a person and one a system, and
then judged which was which. When GPT-4.5 was prompted to adopt a humanlike
persona, interrogators identified it as the human 73 percent of the time, more
often than they picked the actual person it was paired with. Two weaker baselines,
a plain configuration of GPT-4o and Joseph Weizenbaum's 1966 script ELIZA, were
chosen as human only 21 and 23 percent of the time. Reported as the first case of
a machine passing a standard three-party Turing test, the study was widely read as
evidence that a machine had become intelligent. That reading assumes the test
measures intelligence, and the test was built to measure something else.

Turing's 1950 paper, "Computing Machinery and Intelligence," is usually cited as
the origin of the question, "Can machines think?" The paper opens with that line
and then sets the question aside. Turing argued that answering it would first
require definitions of "machine" and "think," and that fixing those definitions by
ordinary usage would reduce the matter to something like a Gallup poll of common
opinion, which he found absurd. In its place he made the move that gave the paper
its influence: "Instead of attempting such a definition I shall replace the
question by another, which is closely related to it and is expressed in relatively
unambiguous words." The replacement was the imitation game.

The structure of the game shows what kind of question it is. Turing describes
three people, a man, a woman, and an interrogator who communicates with both only
through typed messages and has to decide which is which. He then asks the question
that mattered to him: what happens when a machine takes the part of one player and
tries to be taken for a person? Restricting the exchange to text removed voice,
appearance, and every other channel, so the interrogator's decision rested on the
written conversation alone. Turing was explicit that this arrangement stood in for
the older question rather than answering it, writing that "these questions replace
our original, 'Can machines think?'" The whole apparatus turns on one observable
event, the interrogator's guess, and one number, how often that guess is wrong.

Because the measured outcome is the interrogator's decision, the game records a
social interaction rather than a property of the machine on its own. Whether a
system is fluent, evasive, funny, or strategically imperfect matters only through
its effect on a human judge, and that judge brings expectations about how people
write, which mistakes read as human, and which answers seem too polished to be
real. The result depends on both sides. A stronger model can raise its apparent
humanness, and a sharper interrogator, a different time limit, or a different
comparison person can lower it. The test measures indistinguishability under
stated conditions, which is a fact about produced text and about the observer
doing the judging.

The recent studies make that dependence easy to see. In the 2025 experiment,
ELIZA, a pattern-matching script from 1966 that reflects a user's sentences back
as questions and holds no model of meaning, was still taken for human by 23
percent of interrogators, and a plain configuration of GPT-4o by 21 percent, while
the same GPT-4.5 model reached 73 percent once it was told to play a human
persona. A property that swings from below chance to above the human rate on the
strength of a prompt is a property of the exchange, not a stable trait of the
system. The pattern held in the peer-reviewed 2024 study by the same authors,
where the best GPT-4 prompt was judged human 49.7 percent of the time, against 66
percent for real people, 22 percent for ELIZA, and 20 percent for GPT-3.5; the
participants reported that they judged mainly on linguistic style and
socioemotional cues rather than on anything resembling reasoning.

Two different questions sit inside the popular phrase "passing the Turing test,"
and the studies pull them apart. The first is empirical: can a machine produce
conversation that makes human judges misclassify it under stated conditions? The
recent work answers that with a yes. The second is conceptual: what, if anything,
should follow about understanding or intelligence when it does? Turing tied the
two together because he thought the game was a workable way to make progress on a
vague debate, but he offered no account of thinking to go with it, biological,
computational, or psychological. He proposed a public procedure that could be run
without first settling what the word means, and the procedure answers only the
first question.

The reading of the game as an intelligence benchmark grew partly out of Turing's
own forecast. He predicted that in about fifty years a computer could play the
game well enough that "an average interrogator will not have more than 70 per cent
chance of making the right identification after five minutes of questioning." That
figure hardened into a folk rule that fooling 30 percent of judges counts as
passing, as though Turing had drawn a finish line; he was estimating a date, not
setting a threshold. A crisp number invites competition, and competition followed.
The Loebner Prize turned the game into an annual contest, and in 2014 a chatbot
called Eugene Goostman was reported to have passed a Turing test at the University
of Reading by convincing 33 percent of judges over five-minute chats. It presented
itself as a thirteen-year-old boy from Ukraine, a persona chosen so that clumsy
English and gaps in knowledge would read as youth and a second language rather than
as a program. The 33 percent figure comes from the event organizers and press
coverage rather than a peer-reviewed study, and it shows how far the popular
version of the test had drifted from what it records: a system optimized to lower
the interrogator's expectations was counted as a step toward machine intelligence.

Reading the game as a test of intelligence imports an assumption Turing was careful
to leave out, that human-like output is evidence of a human-like process behind it.
He declined to make that step, which is why he swapped the question rather than
answering it, and he said plainly that he believed the original question, "Can
machines think?", to be "too meaningless to deserve discussion." His expectation
was about language: that by the end of the century people would speak of machines
thinking without being contradicted, because ordinary usage would shift. That is a
prediction about how we would talk, not a demonstration of what machines would do.
The point holds regardless of how a given transcript was produced, because many
different internal processes can end in the same words. A person answers from
memory, perception, habit, or deliberate care; a model answers from patterns
learned in training, instructions in a prompt, or text retrieved from its context.
The game observes the final conversation and the judge's classification and leaves
these causes pooled together, so a high win rate establishes that a system can
produce human-like conversation and that people, under these conditions, cannot
catch it out. Those are claims about production and detection, and they leave the
question of internal understanding untouched.

The distinction has practical weight once these systems do consequential work.
Indistinguishability is a weak proxy for competence, because the two come apart
exactly where the stakes are highest. A model can be indistinguishable from a
person in a five-minute chat and still be wrong about a drug interaction, a legal
deadline, or whether a set of symptoms means someone should go to an emergency room
now. The register that wins the game, fluent, warm, and confident, is also the
register that makes a wrong answer most persuasive. Evaluations of language models
in clinical decision-making already show that a fluent response is a poor guide to
a safe one, because clinical usefulness depends on asking for missing information,
expressing uncertainty, following safety constraints, and weighing the cost of
different errors, none of which a conversational judge is testing for. When
indistinguishability is treated as a certificate of competence, the systems that
earn the most trust will sometimes be the ones producing the most convincing
errors.

The imitation game also rewards the wrong behavior for a tool meant to be relied
on. A machine wins by causing the interrogator to identify it incorrectly, which is
a reasonable rule for a thought experiment about human-like conversation and a poor
standard for a system that should disclose its limits. A model that announces it is
a machine, refuses to guess, and asks for context would lose the game while
behaving exactly as a trustworthy assistant should. The reverse case matters too: a
system can be useful and reliable while failing a short imitation game, because the
game rewards one narrow form of social resemblance. A diagnostic model that speaks
in fixed templates, or one that truthfully identifies itself at the start of every
exchange, would score poorly without that saying anything about its competence.

The practical lesson is to match the evaluation to the claim. A Turing-style
experiment is the right instrument for asking whether a system can pass for human
in short conversation, and the recent results answer that question clearly:
current models can hold open-ended conversations well enough that people, given a
fair chance to probe them, cannot reliably tell them from a person. That is a
consequential fact about the state of text generation and about the limits of
human judgment, and it means a transcript is no longer a trustworthy signal of who
produced it. It is a different fact from the one the popular reading claims, about
whether these systems understand what they say, and answering that requires
instruments the imitation game was designed to avoid needing: measures of
calibrated judgment, error severity, and performance on tasks that differ from the
examples a model has already seen. Machines can now win the imitation game, and the
questions Turing set aside in 1950 remain where he left them.

## Further reading

- A. M. Turing (1950), "Computing Machinery and Intelligence," *Mind* 59(236):
  433–460. https://doi.org/10.1093/mind/LIX.236.433
- Cameron R. Jones & Benjamin K. Bergen (2025), "Large Language Models Pass the
  Turing Test," arXiv:2503.23674. https://arxiv.org/abs/2503.23674
- Cameron R. Jones & Benjamin K. Bergen (2024), "Does GPT-4 pass the Turing
  test?", *Proceedings of NAACL 2024*. https://doi.org/10.18653/v1/2024.naacl-long.290
- Graham Oppy & David Dowe, "The Turing Test," *Stanford Encyclopedia of
  Philosophy*. https://plato.stanford.edu/entries/turing-test/
- Joseph Weizenbaum (1966), "ELIZA," *Communications of the ACM* 9(1): 36–45.
  https://doi.org/10.1145/365153.365168
