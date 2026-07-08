# Evidence

**Thesis:** The way a person interacts with a device involuntarily leaks
information about their mental state that self-report routinely misses, because
stigma, limited insight, and the difficulty of putting feelings into words all
distort what people say while leaving much of how they behave intact.

## Key claims and sources

1. **Observers judged the strength of professional poker players' hands better
   than chance from arm motion alone, and worse than chance from faces alone.**
   78 undergraduates rated two-second silent World Series of Poker clips showing
   only the face, only the arms, or the upper body, without seeing the cards.
   Face-only ratings came out below chance, arm-only ratings above chance,
   upper-body at chance; the authors linked the arm signal to the
   smoothness/confidence of the betting motion. — Slepian, Young, Rutchick &
   Ambady (2013), *Psychological Science*, 24(11), 2335–2338.
   DOI: 10.1177/0956797613487384.
2. **Darwin treated the outward signs of emotion as part of the biology of
   emotion, observable from outside and, in his account, more reliable than
   words.** — Charles Darwin (1872), *The Expression of the Emotions in Man and
   Animals*. Full text: https://www.gutenberg.org/ebooks/1227
   - Concluding chapter: "The movements of expression … reveal the thoughts and
     intentions of others more truly than do words, which may be falsified."
   - Ch. I / early chapters: "the muscles which are least under the separate
     control of the will are the most liable still to act, causing movements
     which we recognize as expressive."
   - Ch. XII on fear: "One of the best-marked symptoms is the trembling of all
     the muscles of the body; and this is often first seen in the lips."
3. **Mental-health-related stigma is among the most common reasons people delay
   or avoid disclosing and seeking care; disclosure concerns are the most
   frequently reported stigma barrier.** — Clement, S. et al. (2015), *Psychological
   Medicine*, 45(1), 11–27. Systematic review, 144 studies, 90,189 participants.
   DOI: 10.1017/S0033291714000129.
4. **Alexithymia — marked difficulty identifying and describing one's own
   emotions — was named by Peter Sifneos in 1973 and affects roughly one in ten
   people.** — Sifneos (1973), *Psychotherapy and Psychosomatics*, 22(2), 255–262,
   DOI: 10.1159/000286529; measurement via the 20-item Toronto Alexithymia Scale,
   Bagby, Parker & Taylor (1994), DOI: 10.1016/0022-3999(94)90005-1; prevalence
   e.g. Salminen et al. (1999), DOI: 10.1016/S0022-3999(98)00053-1.
5. **Limited insight is a recognized feature of psychosis, mania, and severe
   depression, making first-person report an incomplete source of clinical
   information.** — David (1990), "Insight and Psychosis," *BJP*, 156, 798–808,
   DOI: 10.1192/bjp.156.6.798; Amador et al. (1993), DOI: 10.1176/ajp.150.6.873.
6. **Digital phenotyping is the inference of health states from moment-to-moment
   data produced by personal devices (typing dynamics, cursor/scroll behavior,
   etc.).** — Insel & Jain (2015), *Nature Biotechnology*, 33(5), 462–464,
   DOI: 10.1038/nbt.3223; Onnela & Rauch (2016), *Neuropsychopharmacology*, 41(9),
   1691–1696, DOI: 10.1038/npp.2016.7.
7. **Passively collected smartphone keystroke metadata (typing speed, timing,
   correction patterns — not message content) tracks the severity of depressive
   and manic symptoms over time.** — Zulueta et al. (2018), BiAffect,
   *JMIR mHealth uHealth*, 6(7):e241, DOI: 10.2196/mhealth.9775.
8. **Related keyboard findings:** less phone movement while typing was associated
   with more anhedonia in a suicidal-ideation sample (Knol et al., 2024,
   DOI: 10.1038/s41746-024-01048-1); mobile-keyboard backspace behavior has been
   associated with depression and mania symptoms (Liu et al., 2024,
   DOI: 10.2196/51269).
9. **Cursor/mouse evidence is weaker and task-dependent.** Mouse trajectories
   have a long history in cognitive science as a readout of indecision and choice
   competition, but a large study of stress detection from mouse usage found
   little reliable signal, with classification close to chance. — Zimmermann et al.
   (2021), *Behavior Research Methods*, DOI: 10.3758/s13428-021-01568-8.
10. **Motor-control theory grounds the mind–movement link:** deliberate movement
    is continuously planned and corrected against internal predictions, on neural
    systems that also carry arousal, mood, and attention, so shifts in state are
    expected to leave signatures in the fine structure of movement. — Wolpert &
    Ghahramani; Shadmehr et al., motor-control literature.
11. **Passive mental-health inference raises consent and misuse risks, because
    sensitive inferences are drawn from traces users experience as incidental.**
    — Torous et al. (2016), DOI: 10.2196/mental.5165; Huckvale, Torous & Larsen
    (2019), *JAMA Network Open*, DOI: 10.1001/jamanetworkopen.2019.2542.
12. **Author's MAILA work (light tie-in only, no numbers):** cursor and
    touchscreen activity recorded during ordinary computer/phone use carries
    mental-health information, including signal only partially reflected in
    verbal self-report. — `writing_context/cursor_mind.qmd` (unpublished; used as
    a general illustration, not summarized).

## Do not overclaim

- The Slepian study used 78 undergraduate raters and short clips; it shows a real
  above-chance signal in arm motion, not that anyone can reliably read an
  individual player in real time.
- Device traces do not diagnose mental illness on their own; no single keystroke,
  pause, cursor path, or scroll has a fixed psychological meaning.
- Keystroke/cursor signals are correlational and noisy; a slow, error-filled
  typing bout has many innocent causes (fatigue, a cheap phone, cold hands, a
  motor condition, walking while typing).
- Reported accuracies are often group-level averages; separating two groups on
  average is not a reliable readout for one person on one day.
- Behavioral data are not bias-free: device type, task, culture, disability, age,
  and context all change interaction patterns.
- Scrolling-specific evidence is less mature than keyboard/cursor evidence; treat
  scrolling as a plausible interaction trace, not a validated stand-alone marker.
- MAILA is a general illustration only — no sample sizes, accuracy figures, or
  numbers.

## Flags

- Darwin quotes verified against the Project Gutenberg text (an 1899 Appleton
  edition of the 1872 work); wording can vary by edition.
- Alexithymia "~10%" is a reasonable consensus figure but varies (roughly 8–13%)
  by instrument and sample; stated as "about one in ten."
- The Slepian "worse than chance for faces" direction is documented in the
  abstract and APS write-up; exact effect sizes not transcribed from the primary
  PDF here.
- BiAffect and related keyboard work report modest predictive accuracy; the draft
  states direction of effect, not accuracy numbers, to avoid overclaiming.
- The HCI mental-health literature is heterogeneous: keyboard studies are stronger
  examples of mood-related signal than general mouse-stress studies, where the
  evidence is mixed.
- Gemini's uncited poker-physiology claims (adrenaline tremor, breathing rate)
  were dropped in favor of the cited Slepian arm-motion result.

# Draft

In 2013 a group of psychologists showed undergraduates two-second silent clips
from the World Series of Poker and asked them to rate the strength of each hand
without ever seeing the cards. When the clips showed only the players' faces, the
ratings came out worse than chance, because professionals train their faces to
give nothing away and the little that does leak tends to mislead. When the same
clips showed only the players' arms as they pushed chips into the pot, the ratings
came out better than chance. The confidence that comes with a strong hand traveled
down into the arm and changed how a chip was placed, through a channel the player
was not watching and probably could not manage to control.

That gap between what a person controls and what escapes anyway is the whole point
of a tell. A poker player chooses every word, arranges the face, and holds the
shoulders still, and a professional spends years rehearsing exactly those signals,
which is why the face turned out to be the worst place to look. Almost nobody
rehearses the manner of a movement. There is no practiced version of how quickly a
hand reaches for a chip, or how a cursor decelerates as it nears a button, because
these are channels we were never taught to perform. The effort we spend managing
the front-facing signals is what leaves the back channels honest, and the question
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
words are genuinely hard to locate rather than deliberately withheld. Even setting
stigma and vocabulary aside, people are unreliable observers of their own minds,
because the state being judged can distort the faculty doing the judging. Limited
insight is a documented feature of psychosis, mania, and severe depression, and
someone sliding into a depressive episode may report feeling fine, or fail to
register the change until it is well advanced.

What these failures share is that they corrupt what a person says while leaving
much of what a person does intact. Stigma changes the answer to "how are you," not
the rhythm with which the answer is typed. A person who cannot name their low mood
still moves through a screen differently while low. The manner of an action, its
timing and hesitations and corrections, sits mostly outside the reach of the
judgment and willingness that shape speech, which is what makes it worth measuring.
A patient may describe a steady week to a clinician while the record of their
typing shows something rougher, and neither account is a lie. The two are sampling
different things, because one asks what the person concluded about themselves and
the other captures how they were actually moving while they did it.

The mechanism behind this is well understood. Every deliberate movement is planned
and then corrected on the fly against an internal prediction of how it should go,
the loop that lets you steer a cursor onto a small button or catch a typo before
your finger finishes the word. That planning and correction runs on neural systems
that also carry arousal, mood, and attention, so when those states shift, the fine
structure of a movement shifts with them. Depression frequently produces
psychomotor retardation, a slowing of thought and movement that lengthens the pause
before an action and drains its vigor. Anxiety can produce the opposite, a
psychomotor agitation that speeds and roughens motor output. The movement still
reaches its target, which is why the person notices nothing, but the path it took
to get there has changed shape.

The idea that inner states show up in movement, and that movement can be read from
outside, is much older than any device. Charles Darwin gave a whole book to it in
1872, *The Expression of the Emotions in Man and Animals*, arguing that the outward
signs of emotion, a trembling muscle or a change in the set of the face, belong to
the biology of the emotion itself, inherited responses you can observe rather than
a coating laid over a private feeling. He noted that when people try to repress an
expression, "the muscles which are least under the separate control of the will
are the most liable still to act," which is close to a physiology of the tell.
Near the end of the book he made a claim that reads almost as a definition of one:
the movements of expression, he wrote, "reveal the thoughts and intentions of
others more truly than do words, which may be falsified." Darwin had only his eyes,
his correspondence, and careful notes to work with. Reading the timing of a
keystroke or the path of a cursor pursues the same project with instruments that
record what an observer's eye is far too slow to catch.

Everyday interaction with a device records that manner continuously. How long
someone pauses before starting to type, how fast and how evenly the keys fall, how
often a sentence is deleted and rewritten, how a cursor accelerates and overshoots
and corrects, how a thumb scrolls and stops, and how long the hesitation runs
before a message is finally sent are all generated as a by-product of normal use.
Researchers call the inference of health states from these traces digital
phenotyping, and its appeal is that the raw material costs nothing extra to gather
and arrives at a scale and in a setting a clinic cannot match, in the middle of a
person's real day rather than in a fifteen-minute appointment they first have to
recognize they need. Keystroke analysis turns this into specific measurements:
dwell time, the duration a finger holds a key, and flight time, the gap between
releasing one key and striking the next. The BiAffect study is a concrete case. It
recorded the metadata of smartphone typing, timing and error patterns rather than
the content of any message, and found that slower typing, more corrections, and
altered rhythms tracked the rise and fall of depressive and manic symptoms over
time. Related work has linked less phone movement while typing to greater
anhedonia, the loss of interest or pleasure, and mobile-keyboard backspace
behavior to mood-disorder symptoms. In my own work, cursor and touchscreen
movements recorded while people used a computer normally carried information about
their mental health, including some that the same people's questionnaire answers
did not fully capture.

None of this turns behavior into a clear window. The signals are noisy: a slow,
error-filled bout of typing can mean low mood, or a cheap phone, or a message
thumbed out while walking down stairs. They are correlational, tracking states
without explaining them, and a pattern that holds across thousands of people can
still be wrong for one person on one afternoon. Some interaction channels carry
much less than others. Mouse trajectories have a long history in cognitive science
as a readout of indecision, yet a large study that tried to detect stress from
mouse usage found little reliable signal, with classification close to chance, and
scrolling remains a plausible trace rather than a validated marker. A model that
separates two groups on average may be close to useless where a decision about a
single person is actually made, and a model trained on one group using one device
can quietly lose its footing on another. The property that makes a tell valuable
is also what makes it fraught, because a tell is leaked rather than offered.
Someone who fills in a questionnaire knows what they have disclosed, while someone
whose typing rhythm is being read has volunteered nothing and may not know the
reading is possible. A measurement that works because it bypasses a person's
control also bypasses their consent, and that has to be treated as a first-order
problem. Sensitive inferences drawn from incidental behavior can harm people
through discrimination, unwanted intervention, or the simple loss of control over
intimate facts, so responsible use has to be opt-in, transparent, limited to clear
purposes, evaluated against outcomes that matter, and tested for bias across
devices, disabilities, languages, and clinical groups.

The reason to take these signals seriously despite the noise and the risk is the
population they might reach. Self-report scales work well for people who already
sense that something is wrong, can name it, and are willing to say so, and those
are roughly the people who already find their way to care. The people such scales
miss are the ones who cannot yet see the change in themselves, who lack the words
for it, or who have good reason to stay quiet, and they are missed at the point
where noticing would help most, before a problem has grown obvious enough to name.
A readout that leans on none of those abilities, drawing instead on how a person
already moves through an ordinary day of typing and scrolling, could register a
shift in some of them earlier than any question would. Used carefully, and with
the consent problem taken seriously, the same principle that lets a poker player's
arm give away a hand the face has hidden could help us notice distress that a
person cannot yet see, cannot name, or has decided not to speak.

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
  Keystroke Metadata" (2018): https://doi.org/10.2196/mhealth.9775
- Zimmermann et al., "Tracking stress via the computer mouse? Promises and
  challenges" (2021): https://doi.org/10.3758/s13428-021-01568-8
