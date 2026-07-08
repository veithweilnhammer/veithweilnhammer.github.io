<!--
==========================================================
SUBSTACK — copy these into the editor's Title / Subtitle boxes:
  Title:    The Turing Test Was Never a Test of Intelligence
  Subtitle: Turing proposed a test of whether a machine could pass for human in conversation — a social question, not a measure of intelligence.
----------------------------------------------------------
  Suggested tags: AI, philosophy, technology
  Visibility checklist:
    [ ] Subtitle doubles as an SEO hook (done above)
    [ ] TL;DR in the first 2 lines
    [ ] 1-2 internal links to related posts
    [ ] Scannable subheads
    [ ] Clear subscribe / share CTA at the end
    [ ] Canonical / cross-post link back to https://veithweilnhammer.github.io/blog/turing-test-not-intelligence/
==========================================================
Paste everything BELOW this comment into the Substack body.
-->

**TL;DR — The imitation game measures whether a machine can pass for human in conversation, which depends on the judge and the setup. Treating it as a benchmark for intelligence mistakes a social outcome for a mental property.**

In early 2025, the cognitive scientists Cameron Jones and Benjamin Bergen ran a
controlled version of Alan Turing's imitation game and reported a result the field
had discussed for seventy-five years. Human interrogators held five-minute typed
conversations with two hidden partners at once, one a person and one a system, and
then judged which was which. When GPT-4.5 was prompted to adopt a humanlike
persona, interrogators identified it as the human 73 percent of the time, more
often than they picked the actual person it was paired with. Two weaker baselines,
a plain configuration of GPT-4o and Joseph Weizenbaum's 1966 script ELIZA, were
chosen as human only 21 and 23 percent of the time. Reported as the first case of
a machine passing a standard three-party Turing test, the study was widely covered
as a sign that a machine had become intelligent. That coverage treats the game as
a measure of intelligence, when it was built to measure whether a machine can pass
for human in conversation, which is a different thing.

Turing's 1950 paper, "Computing Machinery and Intelligence," is usually cited as
the origin of the question, "Can machines think?" The paper opens with that line
and then sets the question aside. Turing argued that answering it would first
require definitions of "machine" and "think," and that fixing those definitions by
ordinary usage would reduce the matter to something like a Gallup poll of common
opinion, which he found absurd. In its place he substituted the imitation game,
introducing it with the line that gave the paper its influence: "Instead of
attempting such a definition I shall replace the question by another, which is
closely related to it and is expressed in relatively unambiguous words."

In Turing's setup, three people — a man, a woman, and an interrogator — communicate
only through typed messages, and the interrogator has to decide which is which. He
then asks the question that mattered to him: what happens when a machine takes the
part of one player and tries to be taken for a person? Restricting the exchange to
text removed voice, appearance, and every other channel, so the interrogator's
decision rested on the written conversation alone. Turing was explicit that this
arrangement stood in for the older question instead of answering it, writing that
"these questions replace our original, 'Can machines think?'" The whole apparatus
turns on one observable event, the interrogator's guess, and one number, how often
that guess is wrong.

Because the measured outcome is the interrogator's decision, the game measures how
a human judge responds to the machine's output. Whether a system is fluent or
strategically imperfect matters only through its effect on that judge, who brings
expectations about how people write and which answers seem too polished to be real.
Because the outcome depends on both sides, a stronger model can raise its apparent
humanness, while a sharper interrogator, a different time limit, or a different
comparison person can lower it. The test measures indistinguishability under stated
conditions, which is a fact about produced text and about the observer doing the
judging.

In the 2025 experiment, ELIZA — a pattern-matching script from 1966 that reflects a
user's sentences back as questions and holds no model of meaning — was still taken
for human by 23 percent of interrogators, and a plain configuration of GPT-4o by 21
percent. The same GPT-4.5 model was judged human 36 percent of the time with a
plain prompt and 73 percent once it was told to play a human persona. A score that
moves from 36 to 73 percent on the strength of a prompt belongs to a particular
exchange between model and judge; it does not track a stable trait of the system.
The pattern held in the peer-reviewed 2024 study by the same authors, where the
best GPT-4 prompt was judged human 49.7 percent of the time, against 66 percent for
real people, 22 percent for ELIZA, and 20 percent for GPT-3.5; the participants
reported that they judged mainly on linguistic style and socioemotional cues rather
than on anything resembling reasoning.

The popular phrase "passing the Turing test" combines two different questions. The
first is empirical: can a machine produce conversation that makes human judges
misclassify it under stated conditions, which the recent work answers with a clear
yes? The second is conceptual: what, if anything, should follow about understanding
or intelligence when it does? Turing tied the two together because he thought the
game was a workable way to make progress on a vague debate, but he offered no
account of thinking to go with it. He proposed a public procedure that could be run
without first settling what the word means, and the procedure answers only the
first question.

The reading of the game as an intelligence benchmark grew partly out of Turing's
own forecast. He predicted that in about fifty years a computer could play the game
well enough that "an average interrogator will not have more than 70 per cent
chance of making the right identification after five minutes of questioning." He
was estimating when this would happen, and later readers turned that estimate into
a pass mark he never proposed, a folk rule that fooling 30 percent of judges counts
as passing. The 30-percent figure invited competition: the Loebner Prize turned the
game into an annual contest, and in 2014 a chatbot called Eugene Goostman was
reported to have passed a Turing test at the University of Reading by convincing 33
percent of judges over five-minute chats. It presented itself as a thirteen-year-old
boy from Ukraine, a persona chosen to make clumsy English and gaps in knowledge seem
like youth and a second language. The 33 percent figure comes from the event
organizers and press coverage rather than a peer-reviewed study, and it shows how
far the popular version of the test had drifted from what it records: a system
optimized to lower the interrogator's expectations was counted as a step toward
machine intelligence.

Reading the game as a test of intelligence imports an assumption Turing was careful
to leave out, that human-like output is evidence of a human-like process behind it.
He declined to take that step, which is why he swapped the question instead of
answering it, and he said plainly that he believed the original question, "Can
machines think?", to be "too meaningless to deserve discussion." His expectation was
about language: that by the end of the century people would speak of machines
thinking without being contradicted, because ordinary usage would shift. That
prediction concerns how we would talk about machines; it says nothing about what the
machines would actually be doing. The point holds regardless of how a given
transcript was produced, because many different internal processes can end in the
same words. A person's answer can come from memory or deliberate reasoning. A
model's answer comes from statistical patterns learned in training and shaped by its
prompt. The transcript looks the same either way, so a high win rate establishes
that a system can produce human-like conversation and that people, under these
conditions, cannot catch it out. Those are claims about production and detection,
and they leave the question of internal understanding untouched.

The distinction has practical weight once these systems do consequential work.
Indistinguishability is a weak proxy for competence, because the two come apart
exactly where the stakes are highest. A model can be indistinguishable from a person
in a five-minute chat and still be wrong about a drug interaction, a legal deadline,
or whether a set of symptoms means someone should go to an emergency room now. The
register that wins the game, fluent and confident, is also the register that makes a
wrong answer most persuasive. Evaluations of language models in clinical
decision-making already show that a fluent response is a poor guide to a safe one,
because clinical usefulness depends on asking for missing information, expressing
uncertainty, following safety constraints, and weighing the cost of different
errors, none of which a conversational judge is testing for. When indistinguishability
is treated as a certificate of competence, the systems that earn the most trust will
sometimes be the ones producing the most convincing errors.

The game also rewards the wrong behavior for a tool meant to be relied on, because a
machine wins by causing the interrogator to identify it incorrectly. A model that
announces it is a machine, refuses to guess, and asks for missing context would lose
the game while behaving exactly as a trustworthy assistant should, and a system that
speaks in fixed templates or identifies itself at the start of every exchange could
be accurate and useful while scoring poorly. Winning depends on one narrow form of
social resemblance that competence does not require.

Evaluations should test the specific ability being claimed. A Turing-style
experiment is the right instrument for asking whether a system can pass for human in
short conversation, and the recent results answer that question clearly: some
current models, prompted to play a persona, can hold open-ended conversations well
enough that people, given a fair chance to probe them, cannot reliably tell them
from a person. That is a consequential fact about the state of text generation and
about the limits of human judgment, and it means a transcript on its own is no
longer a trustworthy signal of who produced it. Whether these systems understand
what they say is a separate question, and answering it requires instruments the
imitation game was designed to avoid needing: measures of calibrated judgment, error
severity, and performance on tasks that differ from the examples a model has already
seen. Some models can now win the imitation game under these conditions, but
establishing whether they understand what they say requires exactly the evaluation
Turing set aside in 1950.

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

---
*Originally posted on [my blog](https://veithweilnhammer.github.io/blog/turing-test-not-intelligence/). If this was useful, consider subscribing and sharing.*
