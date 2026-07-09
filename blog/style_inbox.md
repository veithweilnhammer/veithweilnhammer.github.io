# Style inbox

A staging area for refining `writing_style.md`. Paste examples here as you write
and edit; when you're ready, tell me to **"consolidate the style inbox"** and I'll
fold each entry into the right part of `writing_style.md` (a hard ban, a
before/after pair, a Voice bullet, or a checklist item), then move what I
processed into the "Processed" section at the bottom with the date.

This file is never read by the generation pipeline — only `writing_style.md` is.
So nothing here affects a post until it's been consolidated.

## How to add an entry

Copy the template, fill it in, leave it above the `--- Processed ---` line.
Keep it quick; a verdict and the excerpt are enough, the rest is optional.

- **verdict**: `GOOD` (keep doing this), `BAD` (never do this), or `RULE` (a
  direct preference, not tied to a specific excerpt).
- **excerpt**: the actual sentence(s), as a blockquote. For `RULE`, skip it.
- **why**: one line on what makes it good/bad, or the rule it implies.
- **fix** (optional, for BAD): the plain rewrite you'd prefer.
- **source** (optional): where it's from — post slug, a draft, or "my manuscript".

### Template

```
### BAD — short label
> paste the offending line here

why: what's wrong with it / the rule it suggests
fix: the version you'd prefer (optional)
source: (optional)
```

---

<!-- Add new entries below this line -->

### BAD — "honest back channels" / "runs far past the card table"
> there is no practiced version of how quickly a hand reaches for a chip, or how steadily an arm carries it, because these are channels almost no one is taught to perform. The effort spent managing the front-facing signals is what leaves the back channels honest, and the same gap runs far past the card table, through the ordinary movements of everyday life.

why: personifies channels ("honest") and reaches for a travelling-metaphor coda ("runs far past the card table"); mood over content.
fix: state the mechanism plainly — some signals are easy to control and rehearse (face, speech), others are not (the speed and steadiness of a reach), and the un-rehearsed ones carry information whether or not the person intends it. Then generalize to everyday non-verbal behavior in one flat sentence.
source: the-tell

### BAD — "Most of what we know … we get by asking" + "assume the same three things"
> Most of what we know about a person's mental state, we get by asking. A clinical interview, a questionnaire such as the PHQ-9 for depression, or the plain question of how someone is doing all assume the same three things: that the person can observe their own state, is willing to report it, and can find the words for it. Each assumption fails often enough to matter, and in mental health they tend to fail together.

why: folksy framing ("we get by asking", "assume the same three things", "fails often enough to matter") where a direct methodological statement is wanted.
fix: "Clinical assessment of mental state relies mainly on self-report, which depends on three conditions: that the person can observe their own state, is willing to report it, and can put it into words. In mental health these conditions often fail together."
source: the-tell

### BAD — "sliding into a depressive episode" (poetic + low-content)
> Limited insight is a documented feature of psychosis, mania, and severe depression, and someone sliding into a depressive episode may report feeling fine, or fail to register the change until it is well advanced.

why: "sliding into" is a poetic motion image, and the trailing clause restates the point without adding information.
fix: stop at the documented fact — "reduced insight is a documented feature of psychosis, mania, and severe depression."
source: the-tell

### BAD — "drains its vigor" / "the path it took … has changed shape"
> a slowing of thought and movement that lengthens the pause before an action and drains its vigor. Anxiety can instead speed and roughen motor output, a psychomotor agitation. The movement may still reach its target, so the change is easy to miss, but the path it took to get there has changed shape.

why: decorative verbs ("drains its vigor", "roughen", "changed shape") stand in for measurable terms.
fix: use the quantitative description — psychomotor retardation increases the latency before an action and reduces its speed and amplitude; agitation produces faster, less regular output; the movement still reaches its target but its timing and trajectory differ.
source: the-tell

### BAD — "What it lacks is measurement" beat
> What it lacks is measurement. The cues are noticed and described in the moment, but rarely recorded in a way that can be compared across people or checked against what happens next.

why: short dramatic setup line ("What it lacks is measurement.") followed by a softer restatement.
fix: fold it into one flat sentence — "What it lacks is quantification: the cues are noted in the moment but rarely recorded in a form that can be compared across people or tested against later outcomes."
source: the-tell

### BAD — "still waits on tools … the eye is too slow to catch"
> Darwin worked from observation and correspondence, without any instrument to measure movement, and the project he began still waits on tools fast and fine enough to record what the eye is too slow to catch.

why: "the project he began still waits on tools" and "what the eye is too slow to catch" are literary flourishes.
fix: "Darwin worked from observation alone, without any instrument to measure movement, and recording these signals precisely still depends on tools finer and faster than the human eye."
source: the-tell

### RULE — avoid "manner" as a stand-in for "how a person moves"
why: "the manner of a movement / an action" recurs as a vague, slightly literary tic; the plain phrasing is clearer.
fix: write "how a person moves" or name the concrete property (timing, speed, steadiness) instead of "manner".
source: the-tell

### RULE — cut filler qualifiers like "sharpened by practice"
why: appended phrases such as "sharpened by practice" add cadence, not information.
fix: delete them, or replace with a concrete claim if one is actually meant.
source: the-tell

### BAD — overstated clean dichotomy ("distorts speech but leaves movement intact")
> These failures share a structure: they distort what a person says while leaving much of what a person does intact. Stigma changes a spoken answer, but it does not change how a person walks, gestures, or holds their body.

why: the tidy binary is false — stigma and deliberate concealment can also shape posture, face, and gesture. Clean "A but not B" splits read as AI-confident and overclaim.
fix: state it as a difference of degree — the least-voluntary channels (speed and steadiness of a reach, speech rhythm) are hardest to suppress and most likely to retain signal when self-report fails, while acknowledging movement is not immune.
source: the-tell

<!-- Add new entries above this line -->

--- Processed ---

<!-- I move consolidated entries here, newest first, with the date and where
     they landed in writing_style.md. Nothing below this line is re-applied. -->

### 2026-07-08 — from *The Oldest Form of Mind-Reading* (first draft + pipeline)

These are the examples that shaped the current hard bans, the standalone rule,
and before/after pair #5. Kept here as worked examples of the format.

### BAD — punchy setup / announcement sentence
> Point-light experiments show how little of the body observers actually need.

why: opens a paragraph by advertising the point instead of stating it; reads as AI.
fix: give the finding directly — "In 1973 Johansson filmed people in the dark with lights on their joints; observers still recognized a walking figure from the moving dots alone."
source: oldest-form-of-mind-reading (rejected draft)
→ landed: Hard bans, "No punchy 'setup' or announcement sentences."

### BAD — sentence fragment for effect
> And the visible signal is real.

why: fragment used as a rhetorical beat; no content of its own.
fix: state it inside a full sentence, or cut it.
source: oldest-form-of-mind-reading (rejected draft)
→ landed: Hard bans, "No sentence fragments for emphasis."

### BAD — antithesis / "opposite trade" pair
> Behaviorism kept the movement and set the mind aside. Psychoanalysis made the opposite trade. It kept the inner life — it made hidden mental life the whole subject — and drifted away from measurement.

why: clever-sounding parallel "trade" construction plus dramatic dash-asides; hollow rhythm.
fix: describe what each field actually did, plainly and separately (see before/after #5).
source: oldest-form-of-mind-reading (rejected draft)
→ landed: Hard bans ("No antithesis / parallel 'trade' constructions") + before/after pair #5.

### BAD — rhetorical understatement opener
> Measurement is not the whole problem, though.

why: coy setup that withholds the point instead of making it.
fix: say the positive point — "Measurement alone does not solve the problem, because…"
source: oldest-form-of-mind-reading (rejected draft)
→ landed: Hard bans, "No rhetorical understatement openers."

### BAD — series framing / forward CTA
> That is the gap this series is about. … [poker "tell" teaser pointing to the next post]

why: posts must stand alone; no "this series", no next-post teaser, no CTA.
fix: close on the post's own substantive point.
source: oldest-form-of-mind-reading (rejected draft)
→ landed: new "Each post stands alone" section + Structure items 3 & 5 + checklist.

### BAD — pseudo-poetic scene-setting / image-list
> People read each other through movement. A pause, a turned face, a change in pace signals something inward before a word is said.

why: mood-building fragment-enumeration; the exact "poetic tell" the author rejects.
fix: name the cues plainly and say what they indicate.
source: earlier draft the author flagged
→ landed: Hard bans, "No evocative sensory fragment-enumeration."
