<!--
==========================================================
SUBSTACK — copy these into the editor's Title / Subtitle boxes:
  Title:    The Tell: Reading Mental Health From Human-Computer Interaction
  Subtitle: A poker player's tell leaks the hand they hide; the way we type and move a cursor can leak mental health that words conceal or never reach.
----------------------------------------------------------
  Suggested tags: neuroscience, mental health, technology
  Visibility checklist:
    [ ] Subtitle doubles as an SEO hook (done above)
    [ ] TL;DR in the first 2 lines
    [ ] 1-2 internal links to related posts
    [ ] Scannable subheads
    [ ] Clear subscribe / share CTA at the end
    [ ] Canonical / cross-post link back to https://veithweilnhammer.github.io/blog/the-tell/
==========================================================
Paste everything BELOW this comment into the Substack body.
-->

**TL;DR — How someone interacts with a device carries mental-health signal that words often miss, because stigma, limited insight, and alexithymia distort what people say but not how they move.**

In 2013 a group of psychologists showed undergraduates two-second silent clips
from the World Series of Poker and asked them to rate the strength of each hand
without ever seeing the cards. When the clips showed only the players' faces, the
ratings came out worse than chance, because professionals train their faces to
give nothing away and the little that does leak tends to mislead. When the same
clips showed only the players' arms as they pushed chips into the pot, the ratings
came out better than chance. The arm motion carried real information about the
hand, most likely because a confident bet was placed more smoothly, through a
channel the players attended to far less than their faces.

A tell lives in the gap between what a person controls and what escapes anyway. A
poker player chooses every word, arranges the face, and holds the shoulders still,
and a professional spends years rehearsing exactly those signals, which is why the
face turned out to be the worst place to look. The manner of a movement gets
almost none of that rehearsal: there is no practiced version of how quickly a hand
reaches for a chip, or how a cursor decelerates as it nears a button, because these
are channels we were never taught to perform. The effort we spend managing the
front-facing signals is what leaves the back channels honest, and the question
worth asking is how far this reaches past the card table, into the ordinary
behavior that now runs through keyboards, touchscreens, and cursors.

Most of what we know about a person's mental state, we get by asking. A clinical
interview, a questionnaire such as the PHQ-9 for depression, or the plain question
of how someone is doing all assume the same three things: that the person can
observe their own state, is willing to report it, and can find the words for it.
Each assumption fails often enough to matter, and in mental health they tend to
fail together. Shame and the fear of a diagnostic label keep people from
disclosing; a systematic review of 144 studies and more than 90,000 participants
found mental-health stigma among the most common reasons people delay or avoid
care, with disclosure concerns the most frequently reported barrier. About one
person in ten has marked difficulty identifying and describing their own emotions,
a trait the psychiatrist Peter Sifneos named alexithymia in 1973, and for them the
words are genuinely hard to locate. Even setting stigma and vocabulary aside,
people are unreliable observers of their own minds, because the state being judged
can distort the faculty doing the judging. Limited insight is a documented feature
of psychosis, mania, and severe depression, and someone sliding into a depressive
episode may report feeling fine, or fail to register the change until it is well
advanced.

These failures share a structure: they distort what a person says while leaving
much of what a person does intact. Stigma changes the spoken answer while the
typing rhythm behind it stays the same, and a person who cannot name a low mood
may still move through a screen differently while it lasts. The manner of an
action, its timing and hesitations and corrections, sits mostly outside the reach
of the judgment and willingness that shape speech, which is what makes it worth
measuring. A patient may describe a steady week to a clinician while the record of
their typing shows something rougher, and neither account is a lie; the two are
sampling different things, one asking what the person concluded about themselves
and the other capturing how they were moving while they did it.

One plausible mechanism comes from motor control. Every deliberate movement is
planned and then corrected on the fly against an internal prediction of how it
should go, the loop that lets you steer a cursor onto a small button or catch a
typo before your finger finishes the word. That planning and correction runs on
neural systems that also carry arousal, mood, and attention, so when those states
shift, the fine structure of a movement shifts with them. Depression frequently
produces psychomotor retardation, a slowing of thought and movement that lengthens
the pause before an action and drains its vigor. Anxiety can instead speed and
roughen motor output, a psychomotor agitation. The movement may still reach its
target, so the change is easy to miss, but the path it took to get there has
changed shape.

The idea that inner states show up in movement, and that movement can be read from
outside, is much older than any device. Charles Darwin gave a whole book to it in
1872, *The Expression of the Emotions in Man and Animals*, arguing that the outward
signs of emotion, a trembling muscle or a change in the set of the face, belong to
the biology of the emotion itself, inherited responses that an outside observer can
see. He noted that when people try to repress an expression, "the muscles which
are least under the separate control of the will are the most liable still to
act," which describes why some expressive movements persist even when a person
works to suppress them. Near the end of the book he made a claim that reads almost
as a definition of a tell: the movements of expression, he wrote, "reveal the
thoughts and intentions of others more truly than do words, which may be
falsified." Darwin worked from observation and correspondence, without any
instrument to measure movement. Reading the timing of a keystroke or the path of a
cursor pursues the same project with instruments that record what an observer's eye
is far too slow to catch.

Everyday interaction with a device records that manner continuously. Ordinary use
captures the pause before typing starts, the evenness of the keystrokes, how often
a sentence is deleted and rewritten, and the path a cursor takes as it corrects
toward a target, all as a by-product of normal activity. Researchers call the
inference of health states from these traces digital phenotyping, and its appeal is
that the raw material costs nothing extra to gather and arrives at a scale a clinic
cannot match, during a person's ordinary day instead of inside a short appointment
they first have to recognize they need. Keystroke analysis turns this into specific
measurements: dwell time, the duration a finger holds a key, and flight time, the
gap between releasing one key and striking the next. In one concrete case, the
BiAffect study recorded the metadata of smartphone typing — the timing and error
patterns of the keystrokes, with no access to the content of any message — and
found that slower typing, more corrections, and altered rhythms tracked the rise
and fall of depressive and manic symptoms over time. Related work has linked less
phone movement while typing to greater anhedonia, the loss of interest or pleasure,
and mobile-keyboard backspace behavior to mood-disorder symptoms. In my own work,
cursor and touchscreen movements recorded while people used a computer normally
carried information about their mental health, including some that the same
people's questionnaire answers did not fully capture; there it was a research
signal, not a diagnostic readout.

None of this makes behavior a clear readout of mental state. The signals are
noisy: a slow, error-filled bout of typing can mean low mood, or a cheap phone, or
a message thumbed out while walking down stairs. They are correlational, tracking
states without explaining them, and a pattern that holds across thousands of people
can still be wrong for one person on one afternoon. Some channels carry much less
than others; mouse trajectories have a long history in cognitive science as a
readout of indecision, yet a large study that tried to detect stress from mouse
usage found little reliable signal, with classification close to chance, and
scrolling remains a plausible trace short of a validated marker. A model that
separates two groups on average may be close to useless where a decision about a
single person is actually made, and a model trained on one group using one device
can quietly lose its footing on another. The same feature that makes a tell useful
also makes it fraught, since it is leaked without the person choosing to share it.
Someone who fills in a questionnaire knows what they have disclosed, while someone
whose typing rhythm is being read has volunteered nothing and may not know the
reading is possible. A measurement that works by bypassing a person's
self-presentation can also bypass their consent, and that has to be treated as a
first-order problem. Sensitive inferences drawn from incidental behavior can harm
people through discrimination, unwanted intervention, or the loss of control over
intimate facts, so responsible use has to be opt-in, transparent, and tested for
bias across the devices, languages, and clinical groups it will be applied to.

These signals matter most for the people that self-report scales miss. Those
scales work best for people who already sense that something is wrong, can name it,
and are willing to say so, and those are roughly the people who already find their
way to care. The people such scales miss are the ones who cannot yet see the change
in themselves, who lack the words for it, or who have good reason to stay quiet,
and they are missed at the point where noticing would help most, before a problem
has grown obvious enough to name. A readout that leans on none of those abilities,
drawing instead on how a person already moves through an ordinary day of typing and
scrolling, could register a shift in some of them earlier than any question would.
Used carefully, and with the consent problem taken seriously, the same principle
that lets a poker player's arm give away a hand the face has hidden could help us
notice distress that a person cannot yet see, cannot name, or has decided not to
speak.

## Further reading

- Charles Darwin, *The Expression of the Emotions in Man and Animals* (1872):
  https://www.gutenberg.org/ebooks/1227
- Slepian et al., "Quality of Professional Players' Poker Hands Is Perceived
  Accurately From Arm Motions" (2013): https://doi.org/10.1177/0956797613487384
- Clement et al., "What is the impact of mental health-related stigma on
  help-seeking?" (2015): https://doi.org/10.1017/S0033291714000129
- Onnela & Rauch, "Harnessing smartphone-based digital phenotyping" (2016):
  https://doi.org/10.1038/npp.2016.7
- Zulueta et al., "Predicting Mood Disturbance Severity with Mobile Phone
  Keystroke Metadata" (2018): https://doi.org/10.2196/jmir.9775
- Zimmermann et al., "Tracking stress via the computer mouse? Promises and
  challenges" (2021): https://doi.org/10.3758/s13428-021-01568-8

---
*Originally posted on [my blog](https://veithweilnhammer.github.io/blog/the-tell/). If this was useful, consider subscribing and sharing.*
