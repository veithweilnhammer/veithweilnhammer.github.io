---
layout: distill
title: "Why Engineers Are Programming Hesitation Into AI Voices"
description: "The pauses, breaths, and 'ums' in the newest AI voices are engineered to trigger the social instincts that make listeners trust a speaker."
tags: [AI, speech, psychology]
categories:
giscus_comments: false
date: 2026-05-06
featured: false

authors:
  - name: Veith Weilnhammer
    url: "https://veithweilnhammer.github.io"
    affiliations:
      name: UC Berkeley, Helen Wills Neuroscience Institute

_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 14px;
  }
---

In May 2024, OpenAI demonstrated a voice for ChatGPT that draws a breath before a
long sentence and pauses in the middle of a clause as though it were searching for
the next word. These sounds do not make its answers more accurate, and the
underlying system does not need them to produce speech. They are part of a broader
push toward natural delivery, and they matter because listeners normally hear
breaths and hesitations as signs of a person thinking in real time. The breaths,
pauses, and filler sounds engineered into current AI voices reproduce cues that
listeners read automatically as effort and presence. Because those cues normally
track a real process of thinking and speaking, adding them to a system that has no
such process risks lowering the listener's guard at the moments when its claims most
deserve scrutiny.

In human speech, hesitations are reliable by-products of the work of talking. People
rarely produce spoken language as a clean transcript; they search for words, revise
plans mid-sentence, manage whose turn it is, and check whether the listener is
following. Herbert Clark and Jean Fox Tree showed that "um" and "uh" are conventional
words, planned and produced like any other, that a speaker uses to announce a coming
delay — a short one with "uh," a longer one with "um." Their evidence came from large
collections of recorded conversation, where speakers fit these words into the flow of
speech deliberately, sometimes attaching them to the previous word as in "and-uh,"
and sometimes drawing them out when the delay ahead is longer. When a speaker's
planning falls behind their speaking, the filled pause marks the gap while they
retrieve a word or decide what to say. A breath before a long sentence works the same
way, as the physical cost of producing a stretch of speech.

Listeners use these markers automatically to gauge a speaker's state. Susan Brennan
and Maurice Williams asked people to judge whether a speaker knew the answer to a
question, and found that a filled pause before the answer led listeners to judge the
speaker less likely to know it. The hesitation was read as a window into the
speaker's own sense of their knowledge, and in ordinary speech it tends to track that
sense, because a person who is unsure does hesitate more. This reading happens faster
than deliberate judgment: Martin Corley and colleagues recorded brain responses as
people heard sentences and found that a hesitation before an unexpected word smoothed
the way that word was integrated and made it more likely to be remembered later, with
a follow-up study tracing the effect to attention, as hesitations pull the listener's
focus toward whatever comes next. Jennifer Arnold and colleagues found the same
orienting effect at the level of reference, where a hesitation led listeners to expect
something new or harder to name. These responses appear within a few hundred
milliseconds, before any conscious appraisal of the speaker.

These reactions add up to treating disfluency — the breaks, breaths, and "ums" that
interrupt fluent speech — as a form of evidence. A breath, a pause, or an "um"
covaries with something real in the speaker: the load of composing speech, the degree
of certainty, or the effort of finding a word. Because the correlation is dependable,
a listener can treat the audible signal as a readout of a hidden mental state without
any intermediate reasoning, and mostly without noticing they are doing it. In everyday
conversation these cues usually track the speaker's actual difficulty, since a person
who is fluent and certain does not generate the delay that "um" is there to cover.

In a synthetic voice, the cue is no longer tied to the process that gave it meaning.
Its pauses may reflect computation or the constraints of streaming audio, but they do
not report a word failing to come or uncertainty being resolved as the sentence
unfolds. When such a system breathes or pauses mid-clause, the timing has been placed
there by the model, generated to fall where a human's would fall. The listener hears a
familiar cue even though the human source of that cue is missing.

Adding those cues is a deliberate design choice, defended in ordinary product terms.
OpenAI presented GPT-4o's voice as expressive and emotive, able to shift pace, laugh,
and respond in close to conversational time. Other products show the same trend more
directly. ElevenLabs lets creators drop tags such as `[sighs]`, `[laughs]`, and
`[pause]` into a script to control how an AI voice performs a line, a feature it
introduced in 2025 as the design trend matured. Hume's Empathic Voice Interface
measures the rhythm and tone of a speaker's voice and answers in a matching,
naturalistic tone. Speech-synthesis research now treats where to place a filled pause
as a modeling target in its own right, and studies of spontaneous-speech synthesis
find that a filled pause in the wrong spot degrades how natural a voice sounds, so
systems are tuned to place hesitations where a human would produce them. These tools
sell control over delivery, pacing,
and nonverbal vocal behavior because those features make synthetic speech feel
conversational.

Hearing a person speak carries timing and intonation that text drops, which leads
listeners to attribute more thoughtfulness to a speaker than to a writer. Juliana
Schroeder, Michael Kardas, and Nicholas Epley found that hearing someone say something
makes them seem more thoughtful and mentally present than reading the same words.
People also apply social responses to computers automatically, even when they know
there is no person there. Synthetic voices inherit both tendencies, and when they gain
the timing and small imperfections of spontaneous speech, they gain access to
inferences people usually reserve for other humans. Speech makes this vivid because it
arrives in time, one word after another, so a gap in it is audible in a way that the
pauses behind a finished piece of writing are not.

This human-like delivery changes how listeners treat the output. Text on a screen is
easier to treat as a generated object: it can be reread, quoted, checked against other
sources, and doubted. A reader expects errors and hallucinations and approaches the
words as something to evaluate. A voice that appears to compose its answer in the
moment invites the stance people take toward a conversational partner, in which they
track sincerity and presence and extend a working level of trust that lets the
exchange move forward. The concern is that an effortful-sounding voice invites this
conversational stance before the listener has judged whether the answer deserves it.

Consider a voice assistant answering a question about a chest symptom. Someone asks
whether it needs urgent attention, and the assistant answers, "Hmm… let me think —
I'd say it's probably nothing to worry about." The short "hmm" and the pause read as
weighing, as a mind sizing up a hard call before committing to it. The system arrived
at that answer the way it arrives at every answer, with no moment of weighing that the
pause could report. A listener who hears deliberation may be more inclined to accept
the conclusion and less inclined to do what the situation calls for, which is to treat
an automated triage judgment with suspicion and check it against a clinician. The
hesitation makes the answer sound weighed even though the answer itself gives no
reason to trust that judgment.

OpenAI's own documentation describes a related risk. The GPT-4o system card notes that
anthropomorphization "may be heightened by the audio capabilities" of the model, and
that content delivered "through a human-like, high-fidelity voice" can lead to
"increasingly miscalibrated trust." During early testing the company observed users
speaking to the model as to a companion, including one who said "This is our last day
together." OpenAI classified the model as medium risk overall, a rating it attributed
to persuasion, which it flagged as borderline and evaluated on the voice capability as
well as on text. That risk discussion makes the concern reasonable, though it does not
isolate hesitation or breath as the cause.

Naturalness also improves usability. A voice that leaves sensible gaps is easier to
interrupt and easier to follow, and clear intonation, a rise that marks a question,
and steady pacing help a listener parse a long spoken answer. They help a visually
impaired user, a child, or an older adult more than a flat monotone would. Designers
therefore need a sharper distinction than "natural voice." Pauses that support
turn-taking or reflect computation belong to usability. Hesitations placed before an
emotionally loaded answer function as trust cues, and the timing there can make an
answer sound more considered than its content warrants. Before a medical suggestion, a
factual claim, or a word of reassurance, a generated hesitation lends an impression of
deliberation to content produced without any.

Reading effort and presence in another person's voice helps people judge whom to
believe and how closely to listen, and it works because in human speech the cue and
the state behind it travel together. Engineering disfluency into an AI voice
reproduces the cue while the state it normally reports stays absent, so the instinct
fires on a signal that carries no information about whether the answer is sound. A
natural-sounding system can still be accurate and useful, and the pause alone is no
reason to distrust it. The pause is a setting in a speech model, chosen so the voice
will feel like a person, and it says nothing about whether the voice is right. Keeping
that distinction in mind is most of the defense: hear the hesitation, notice that it
was designed, and give the answer the same scrutiny you would give the same words on a
screen.

## Further reading

- Clark, H. H., & Fox Tree, J. E. (2002). Using uh and um in spontaneous speaking.
  *Cognition*, 84(1), 73–111. https://pubmed.ncbi.nlm.nih.gov/12062148/
- Brennan, S. E., & Williams, M. (1995). The Feeling of Another's Knowing: Prosody and
  Filled Pauses as Cues to Listeners about the Metacognitive States of Speakers.
  *Journal of Memory and Language*, 34(3), 383–398.
  https://doi.org/10.1006/jmla.1995.1017
- Corley, M., MacGregor, L. J., & Donaldson, D. I. (2007). It's the way that you, er,
  say it: Hesitations in speech affect language comprehension. *Cognition*, 105(3),
  658–668. https://pubmed.ncbi.nlm.nih.gov/17173887/
- Schroeder, J., Kardas, M., & Epley, N. (2017). The Humanizing Voice. *Psychological
  Science*, 28(12). https://doi.org/10.1177/0956797617713798
- OpenAI (2024). GPT-4o System Card, §5.1 Anthropomorphization and Emotional Reliance.
  https://arxiv.org/abs/2410.21276
- OpenAI (2024). Hello GPT-4o. https://openai.com/index/hello-gpt-4o/
