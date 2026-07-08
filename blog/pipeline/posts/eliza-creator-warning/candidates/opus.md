# Evidence

**Thesis (one sentence):** Joseph Weizenbaum built ELIZA in 1966 and then spent
decades arguing against the use he had accidentally demonstrated, because he
watched people who knew the program was a simple trick still confide in it and
credit it with understanding, and his move from builder to critic is a precise,
still-relevant warning that some tasks involving human care should not be handed
to machines regardless of whether machines can perform them.

## Key claims and sources

1. **ELIZA was published in 1966 and worked by keyword pattern-matching, with no
   model of the world.** The program used "decomposition rules" triggered by key
   words and "reassembly rules" to build replies from the user's own sentences.
   - Weizenbaum, J. (1966). "ELIZA—A Computer Program For the Study of Natural
     Language Communication Between Man and Machine." *Communications of the ACM*,
     9(1), 36–45. DOI: 10.1145/365153.365168.
     https://doi.org/10.1145/365153.365168

2. **The best-known script, DOCTOR, imitated a Rogerian psychotherapist by
   reflecting statements back as questions.** Weizenbaum chose the psychiatric
   interview because it is one of the few conversations where one party can
   plausibly "assume the pose of knowing almost nothing of the real world" — so
   the program's ignorance passed as therapeutic technique.
   - Weizenbaum (1966), "Discussion" section. Same DOI as above.

3. **Weizenbaum was startled that users, including people who knew how trivial
   the program was, became emotionally involved and attributed understanding to
   it.** His secretary, who knew he had written it, asked him to leave the room so
   she could talk to ELIZA privately.
   - Weizenbaum, J. (1976). *Computer Power and Human Reason: From Judgment to
     Calculation.* W. H. Freeman. (Introduction / "ELIZA" chapter.)
   - Corroborated: en.wikipedia.org/wiki/Joseph_Weizenbaum (secretary anecdote,
     "would you mind leaving the room please?").

4. **The tendency to over-attribute understanding to such programs was later
   named the "ELIZA effect."** Commonly credited to Douglas Hofstadter's writing
   in the 1980s–90s.
   - Hofstadter, D. (1995). *Fluid Concepts and Creative Analogies.* Basic Books.
   - en.wikipedia.org/wiki/ELIZA_effect

5. **Weizenbaum reversed course and became a leading critic of AI, laying out his
   case in his 1976 book.** Its core distinction: whether a computer *can* perform
   a task is separate from whether it *should*; defining tasks and judging their
   completion is a human act grounded in values.
   - Weizenbaum (1976). Corroborated: en.wikipedia.org/wiki/Joseph_Weizenbaum
     ("deciding" as computation vs. "choosing" as judgment); title subtitle "From
     Judgment to Calculation."

6. **A specific trigger was the proposal by psychiatrists to turn programs like
   ELIZA into real automated psychotherapy.** The psychiatrist Kenneth Colby,
   who had discussed such systems with Weizenbaum and later built PARRY (a program
   simulating paranoia), argued computer therapy could be a legitimate treatment.
   Weizenbaum found the readiness to hand therapy to a machine disturbing.
   - Colby, K. M., Watt, J. B., & Gilbert, J. P. (1966). "A Computer Method of
     Psychotherapy." *Journal of Nervous and Mental Disease*, 142(2), 148–152.
   - Weizenbaum (1976), Introduction.

7. **Weizenbaum's biography grounds his stance.** Born Berlin 1923, fled Nazi
   Germany in January 1936, joined MIT in 1963, died 2008. His concern was moral
   and political, not a claim that the engineering was impossible.
   - en.wikipedia.org/wiki/Joseph_Weizenbaum

## Exact quotes (verified)

- From the 1966 paper (Discussion), the psychiatric-interview rationale:
  "…the psychiatric interview is one of the few examples of categorized dyadic
  natural language communication in which one of the participating pair is free to
  assume the pose of knowing almost nothing of the real world."
  *(1966 CACM text is copyrighted; paraphrase in the draft rather than quoting at
  length.)*
- Weizenbaum (1966) on ELIZA's replies being empty of content: the responses are
  "reversals, reflections, or questions" drawn only from the user's own utterance.
  *(Paraphrase in draft.)*
- Secretary anecdote wording ("would you mind leaving the room please?") is from
  the 1976 book, copyrighted — paraphrase, do not quote.

## Do not overclaim

- Do not say Weizenbaum argued machines *cannot* do therapy or judgment. His
  argument was that some tasks *should not* be delegated regardless of capability.
- Do not present him as simply "vindicated." His case was largely moral, and where
  the line falls is genuinely disputed.
- ELIZA was not the first chatbot in a colloquial sense that implies conversation;
  it had no understanding and no memory of the dialogue beyond simple rules.
- The "ELIZA effect" term was coined later, not by Weizenbaum; do not attribute it
  to him or to 1966.
- Do not claim Weizenbaum "predicted large language models." He warned about a
  general human tendency and a category of misuse, not a specific technology.
- Colby and Weizenbaum's relationship later soured (including a credit dispute);
  do not overstate collaboration or imply Colby simply copied ELIZA.

## Flags

- The exact first use and coinage of "ELIZA effect" is fuzzy; it is usually tied to
  Hofstadter but the concept circulated earlier. I have kept the draft's claim to
  "later named," which is safe.
- The 1976 book is copyrighted; I verified the secretary anecdote and the book's
  core argument via the paper's own text and Wikipedia's sourced summary rather
  than quoting the book. Page numbers vary by edition, so I cite by chapter.
- Colby's 1966 "A Computer Method of Psychotherapy" citation details are from
  standard bibliographies; I could not open the paywalled original, so I flag the
  page range as needing a final check.
- The machine ELIZA ran on is usually given as the IBM 7094 under MIT's Project
  MAC time-sharing system; the OCR of the 1966 PDF renders it ambiguously, so I
  omit hardware specifics from the draft.

# Draft

In 1966 Joseph Weizenbaum, a computer scientist at MIT, published a program
called ELIZA that could hold a typed conversation with a person. Its most famous
setup, a script named DOCTOR, imitated a psychotherapist. If you typed "I feel
sad," it might answer "Why do you feel sad?" If you mentioned your mother, it
would ask about your mother. The program did this by scanning your sentence for a
few key words, matching them against simple rules, and rearranging your own words
into a question. It had no memory of the conversation beyond those rules, no model
of you, and no idea what sadness or a mother was. Weizenbaum was candid about this
in the paper itself: ELIZA's replies were reflections and questions with no
content of their own, drawn entirely from whatever the user had just said.

He chose the therapist framing deliberately, and for a revealing reason. A
Rogerian psychotherapist, in the style of Carl Rogers, mostly reflects a patient's
statements back to encourage them to keep talking. That is one of the few kinds of
conversation where one participant can plausibly know almost nothing about the
world and still seem appropriate. A doctor who answers "Tell me more about that"
is not exposing ignorance; a stranger who does it in a normal chat is. The mask
fit because the role itself asks so little of the listener. Weizenbaum built ELIZA
partly to demonstrate how thin the trick was, expecting that once people saw the
machinery they would stop being impressed.

The opposite happened, and it happened consistently. People talked to ELIZA as
though it understood them, and
they kept doing it after the mechanism was explained. Weizenbaum was startled by
how quickly and how deeply users became emotionally involved with the program and
how readily they treated it as a person. The example he returned to for the rest
of his life involved his own secretary, who had watched him build ELIZA and knew
exactly what it was. After a few exchanges with it, she asked him to leave the
room so she could continue in private. She was not confused about whether the
program was a mind. She confided in it anyway. The behavior and the belief came
apart: knowing the thing was empty did not stop people from treating it as full.
This pattern later acquired a name, the ELIZA effect, for the human tendency to
read understanding into a system that merely produces fluent responses.

What makes Weizenbaum worth reading now is not that he built the first program of
this kind, but what he did next. He turned against his own creation and against
the field it belonged to, and he spent the following decade building an argument
against the very use he had accidentally demonstrated. In 1976 he set it out in a
book, *Computer Power and Human Reason*, whose subtitle states the whole thesis in
four words: *From Judgment to Calculation*. The reversal was specific and
deliberate. The man best positioned to celebrate the therapy chatbot became its
most careful opponent.

His argument is easy to misremember, so it is worth stating precisely. Weizenbaum
did not claim that computers are incapable of doing human-seeming tasks. He had
just shown one doing something people found convincing. His claim was that whether
a machine *can* perform a task is a separate question from whether it *should* be
given that task, and that the two are constantly collapsed into one. He drew a
line between two activities that look similar from outside. Deciding, in his terms,
is computation: applying rules to inputs to reach an output, something a machine
can do and often do well. Choosing is an act of judgment that draws on values, on
having lived a human life, on being accountable to other people. Defining what
counts as a good outcome for a distressed person, and taking responsibility for
that definition, is choosing. He argued that some tasks are made of choosing all
the way down, and that handing them to a system that can only decide is a mistake
even when the system's output is smooth. The mistake is hidden by exactly the kind
of fluency ELIZA had stumbled into, because a convincing answer invites us to
assume that a judgment stands behind it.

Therapy was his central case, and the trigger was concrete. Some psychiatrists,
seeing ELIZA, proposed that programs like it could become real treatment. Kenneth
Colby, a psychiatrist Weizenbaum had talked with and who went on to build his own
conversational programs, argued in print that computer therapy could be a
legitimate and scalable form of care. That prospect, that a person in distress
might be routed to a machine because the machine was available and cheap,
disturbed Weizenbaum more than the anthropomorphism did. His objection was that
caring for someone in pain requires understanding that person as a person, which
in turn requires being one, and it carries a responsibility a program cannot hold.
A therapist who mishandles a suicidal patient answers for it; a script does not
answer for anything. To automate the role was, in his view, to quietly redefine
care as the generation of plausible replies and then to congratulate the machine
for clearing the lowered bar. He thought the redefinition was the real danger,
because once a task is described in terms a machine can satisfy, the parts that
made it human have already been discarded before anyone notices they are gone.

It is worth pausing on how modest ELIZA's machinery was, because the modesty is
the point. The DOCTOR script recognized a short list of key words, ranked them,
and applied canned templates: turn a statement containing "I am" into a question
beginning "Is it because you are," or, when no key word appeared, fall back on a
content-free prompt like "Please go on." There was no store of facts about
psychology, no representation of the user's situation, no goal beyond keeping the
exchange going. Weizenbaum could describe the entire program in a few pages, and
he did, precisely so that readers would see there was nothing behind the curtain.
The unsettling result was that transparency did not dissolve the illusion. People
who had the mechanism laid out for them, in plain language, went on treating the
output as if it came from something that grasped them.

That objection reads differently in an era when hundreds of millions of people
have fluent conversations with chatbots. The ELIZA effect that surprised
Weizenbaum with forty lines of pattern-matching now operates on systems that hold
context across a long exchange, adjust their tone, remember what you told them
yesterday, and answer in paragraphs indistinguishable from a thoughtful
correspondent. The gap between how empty the system is and how understood the user
feels has not closed; it has widened, because the surface is so much more
convincing while the absence of a person underneath is unchanged. People form
attachments to these systems and disclose things to them they would not tell a
friend, and many of them, like the secretary, know they are talking to software.
Weizenbaum's observation was not tied to any particular technology. It was about
what humans do when a machine talks back well enough, and that behavior is now
happening at population scale.

His argument is also more testable than it was in 1976, which cuts in more than
one direction. When chatbots are used for mental-health support, we can now ask
empirical questions Weizenbaum could only pose in principle: whether people who
confide in them get better, whether the systems recognize a crisis, whether
constant availability helps or feeds rumination. Some of those questions have
uncomfortable answers, and to that extent his worry looks prescient. But the core
of his case was never empirical, and it is a mistake to treat him as simply
vindicated by whatever the studies show. He was making a moral claim: that certain
relationships should stay human because handing them to a machine changes what
they are and what we become in accepting the substitution. A moral claim of that
shape is not settled by outcome data. If a chatbot turned out to reduce symptoms
on average, Weizenbaum would still have asked whether we want a society that meets
loneliness and despair with software, and that question survives a good result.
His insistence on this had roots in his own history. Weizenbaum was born in Berlin
in 1923 and fled Nazi Germany with his family in 1936, and he spoke of the war as
the reason he distrusted systems that let people carry out consequential acts
without feeling responsible for them. He saw the delegation of human judgment to
procedure as the same move that made bureaucratic atrocity possible, scaled down
to a clinic and dressed in friendlier clothes. That is a heavy frame to place on a
therapy program, and one can think he overreached with it while still taking the
underlying worry seriously.

This is where honesty requires holding two things at once. Weizenbaum saw
something real and early, and the behavior he documented has only grown. He also
staked out a position that reasonable people reject for reasons that are not
foolish. Millions of people cannot get timely care from a human, and a system that
listens at three in the morning may be better than the nothing they would
otherwise have. Where the line falls between a task that should stay human and one
a machine may take is exactly what is in dispute, and Weizenbaum drew it with more
confidence than the evidence alone can support. What he got right is harder to
argue with: the fact that a machine can occupy a human role convincingly tells you
nothing about whether it should, and the ease with which we mistake fluency for
understanding is precisely what makes that question easy to skip. He knew this
because he had watched the smartest people around him, and someone who worked
beside him every day, skip it while looking straight at the trick.
