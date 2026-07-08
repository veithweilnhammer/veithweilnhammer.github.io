# GPT review

## Prioritized actionable fixes

1. **Fix the BiAffect citation DOI/journal.**
   - Offending text: `Zulueta et al., "Predicting Mood Disturbance Severity with Mobile Phone Keystroke Metadata" (2018): https://doi.org/10.2196/mhealth.9775`
   - Fix: use `https://doi.org/10.2196/jmir.9775` and list it as *Journal of Medical Internet Research* 20(7):e241. Crossref returns 404 for `10.2196/mhealth.9775` and resolves the article under `10.2196/jmir.9775`.

2. **Soften the poker mechanism and control claims.**
   - Offending text: `The confidence that comes with a strong hand traveled down into the arm and changed how a chip was placed, through a channel the player was not watching and probably could not manage to control.`
   - Problem: the Slepian study supports above-chance arm-motion information and links it to smoothness/confidence, but it does not prove the causal mechanism or that players could not control it.
   - Fix: `The arm motion carried information about hand strength, possibly because confident bets were smoother, even when the players' faces did not help observers.`

3. **Remove banned antithesis around words versus behavior.**
   - Offending text: `Stigma changes the answer to "how are you," not the rhythm with which the answer is typed.`
   - Fix: `Stigma can change what a person reports, while typing rhythm may still reflect arousal, mood, or attention.`
   - Offending text: `What these failures share is that they corrupt what a person says while leaving much of what a person does intact.`
   - Fix: `These failures affect verbal report more directly than interaction traces, which is why behavior can add information rather than replace self-report.`

4. **Replace overconfident mechanism language.**
   - Offending text: `The mechanism behind this is well understood.`
   - Problem: motor-control theory supports the general plausibility, but the mapping from mood to device traces is not fully understood and is noisy.
   - Fix: `One plausible mechanism comes from motor control.`
   - Offending text: `The movement still reaches its target, which is why the person notices nothing`
   - Fix: `The movement may still reach its target, so the change can be easy to miss.`

5. **Cut punchy setup sentences banned by the style guide.**
   - Offending text: `Almost nobody rehearses the manner of a movement.`
   - Fix: fold into the previous sentence: `Professionals rehearse facial and verbal signals far more than the timing and smoothness of ordinary movements.`
   - Offending text: `The BiAffect study is a concrete case.`
   - Fix: merge with the next sentence: `In the BiAffect study, researchers recorded smartphone typing metadata...`
   - Offending text: `Some interaction channels carry much less than others.`
   - Fix: merge with the mouse sentence: `The evidence is weaker for some channels: mouse trajectories...`
   - Offending text: `The reason to take these signals seriously despite the noise and the risk is the population they might reach.`
   - Fix: `These signals matter most for people self-report scales miss.`

6. **Reduce the piled-up interaction list.**
   - Offending text: `How long someone pauses before starting to type, how fast and how evenly the keys fall, how often a sentence is deleted and rewritten, how a cursor accelerates and overshoots and corrects, how a thumb scrolls and stops, and how long the hesitation runs before a message is finally sent...`
   - Fix: `Typing latency, correction patterns, cursor trajectories, and scroll timing are generated as by-products of normal device use.`

7. **Remove rhetorical negation/metaphor in the limits section.**
   - Offending text: `None of this turns behavior into a clear window.`
   - Fix: `These signals are noisy and indirect.`
   - Offending text: `The property that makes a tell valuable is also what makes it fraught, because a tell is leaked rather than offered.`
   - Fix: `The consent problem follows from the fact that these traces can be collected and interpreted without an explicit mental-health disclosure.`
   - Offending text: `A measurement that works because it bypasses a person's control also bypasses their consent`
   - Fix: `If collected without explicit opt-in, a measurement that bypasses self-presentation can also bypass consent.`

8. **Trim literary/clever phrasing in the Darwin paragraph.**
   - Offending text: `a coating laid over a private feeling`
   - Fix: `a separate display added after the emotion`
   - Offending text: `which is close to a physiology of the tell`
   - Fix: `which explains why some expressive movements persist despite voluntary control.`
   - Offending text: `Darwin had only his eyes, his correspondence, and careful notes to work with.`
   - Fix: `Darwin worked from observation and correspondence rather than instrumented movement data.`

9. **Qualify universal behavioral claims.**
   - Offending text: `A person who cannot name their low mood still moves through a screen differently while low.`
   - Fix: `A person who cannot name low mood may still show changes in how they move through a screen.`
   - Offending text: `Self-report scales work well for people who already sense that something is wrong...`
   - Fix: `Self-report scales work best when people sense that something is wrong...`

10. **Keep the MAILA tie-in light but add one clarifying boundary.**
    - Offending text: `In my own work, cursor and touchscreen movements... carried information about their mental health...`
    - Fix: keep it, but add or revise to make clear this is an illustration, not a clinical claim: `In my own work, this was a research signal rather than a diagnostic readout.`

## Factual grounding checked

- Slepian et al. poker claim is broadly supported by the APS summary and DOI metadata: 78 undergraduates, two-second WSOP clips, face-only worse than chance, arms-only better than chance. Mechanism/control wording should be softened as above.
- Darwin quotes are accurate against Project Gutenberg text, including `the muscles which are least under the separate control of the will are the most liable still to act` and `reveal the thoughts and intentions of others more truly than do words, which may be falsified`.
- Clement et al. stigma claim checks out: 144 studies, 90,189 participants, disclosure concerns most common stigma barrier.
- Knol et al. 2024 checks out via article metadata: less phone movement while typing associated with more anhedonia. Zimmermann et al. 2021 checks out: no clear stress-mouse relationship; classifications close to chance.
- Main factual error found: Zulueta DOI/journal in Further reading.

## Structure, argument, and brief compliance

- Single thesis: device interaction traces can reveal mental-health information that self-report misses because stigma, limited insight, and difficulty naming feelings affect words more than behavior.
- The post develops that one argument from poker tell to self-report limits, Darwin, digital phenotyping, limits, consent, and why it matters. No major second thesis.
- Brief coverage is complete: poker tell, stigma/alexithymia/limited insight, timing/hesitation/typing/cursor/scrolling, digital phenotyping, Darwin, noisy/correlational limits, consent, and why self-report misses people.
- Standalone check: no series framing, previous/next references, or CTA. It does not re-tell the prohibited sibling-post material.

## Top 3 priorities

1. Correct the Zulueta DOI/journal.
2. Remove the style-guide hard-ban patterns: antithesis, punchy setup sentences, piled-up list, and rhetorical negation.
3. Soften overclaims about mechanism, involuntary control, and individual-level readout.

Overall verdict: **minor fixes (ship-with-minor-edits)** — the argument and coverage are strong, but it needs citation correction, style-guide cleanup, and a few factual hedges before publication.
