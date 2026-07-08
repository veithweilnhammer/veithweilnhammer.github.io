# Evidence

**Thesis:** Joseph Weizenbaum built ELIZA in 1966 and then spent the rest of his
life arguing against the use he had accidentally demonstrated, because he watched
people who knew the program was a simple trick still confide in it and credit it
with understanding. His move from builder to critic is a precise, still-relevant
warning that some tasks involving human care should not be handed to machines
regardless of whether machines can perform them.

## Verified facts and sources

1. **ELIZA was published in 1966 and worked by keyword pattern-matching, with no
   model of the world.** The program scanned input for key words, applied
   "decomposition rules" to break the sentence into parts, and used "reassembly
   rules" to build a reply from the user's own words. Scripts were data loaded
   into the program.
   - Weizenbaum, J. (1966). "ELIZA—A Computer Program For the Study of Natural
     Language Communication Between Man and Machine." *Communications of the ACM*,
     9(1), 36–45. DOI: 10.1145/365153.365168. https://doi.org/10.1145/365153.365168

2. **The best-known script, DOCTOR, imitated a Rogerian psychotherapist by
   reflecting statements back as questions.** Weizenbaum chose the psychiatric
   interview because it is one of the few conversations where one party can
   plausibly assume the pose of knowing almost nothing of the real world, so the
   program's ignorance passed as therapeutic technique. Example behavior:
   keyword "mother" triggers a family-related prompt; "I am unhappy" yields a
   question about the unhappiness; with no keyword, fallbacks like "Please go on."
   - Weizenbaum (1966), "Discussion" section. Same DOI.
   - Smithsonian (2023), "Why the Computer Scientist Behind the World's First
     Chatbot Dedicated His Life to Publicizing the Threat Posed by A.I."

3. **ELIZA ran on MIT's time-sharing system, so a user typed at a terminal and got
   an immediate line-by-line reply.** The conversational pacing was itself novel
   and contributed to the effect.
   - Weizenbaum (1966). (Hardware is usually given as the IBM 7094 under Project
     MAC; the 1966 PDF's OCR is ambiguous, so hardware specifics are omitted from
     the draft — see Flags.)

4. **Weizenbaum was startled that users, including people who knew the program was
   trivial, became emotionally involved and attributed understanding to it. His
   secretary, who had watched him build ELIZA, asked him to leave the room so she
   could talk to it privately.**
   - Weizenbaum, J. (1976). *Computer Power and Human Reason: From Judgment to
     Calculation.* W. H. Freeman. (Introduction / "ELIZA" chapter.)
   - Corroborated: Goodrich, B. (2024), "My search for the mysterious missing
     secretary who shaped chatbot history," *The Conversation*.
     https://theconversation.com/my-search-for-the-mysterious-missing-secretary-who-shaped-chatbot-history-225602

5. **The tendency to over-attribute understanding to such programs was later named
   the "ELIZA effect."** Commonly credited to Douglas Hofstadter's writing.
   - Hofstadter, D. (1995). *Fluid Concepts and Creative Analogies.* Basic Books.
   - https://en.wikipedia.org/wiki/ELIZA_effect

6. **A specific trigger for Weizenbaum's reversal was psychiatrists proposing to
   turn programs like ELIZA into real automated psychotherapy.** Kenneth Colby, a
   psychiatrist who had discussed such systems with Weizenbaum and later built
   PARRY (a program simulating paranoia), argued computer therapy could be a
   legitimate, scalable treatment. Their relationship later soured over a credit
   dispute.
   - Colby, K. M., Watt, J. B., & Gilbert, J. P. (1966). "A Computer Method of
     Psychotherapy." *Journal of Nervous and Mental Disease*, 142(2), 148–152.
   - Weizenbaum (1976), Introduction.

7. **Weizenbaum reversed course and laid out his case in the 1976 book.** Its core
   distinction: whether a computer *can* perform a task is separate from whether it
   *should*; the book's subtitle, *From Judgment to Calculation*, states the
   thesis. "Deciding" is computation (applying rules to inputs); "choosing" is
   judgment grounded in values and lived experience.
   - Weizenbaum (1976). Corroborated: MIT News obituary (2008),
     https://news.mit.edu/2008/obit-weizenbaum-0310 ; and
     https://en.wikipedia.org/wiki/Joseph_Weizenbaum

8. **Weizenbaum argued that some functions should not be handed to computers even
   if they could be performed — those requiring respect, understanding, and
   care, such as a judge, a police officer, or a psychiatrist.**
   - Weizenbaum (1976). (See exact-quote note below; paraphrased in the draft.)

9. **Weizenbaum's biography grounds his stance.** Born Berlin 1923, fled Nazi
   Germany with his family in 1936, joined MIT in 1963, died 2008. His concern was
   moral and political, not a claim that the engineering was impossible.
   - https://en.wikipedia.org/wiki/Joseph_Weizenbaum ; MIT News obituary (2008).

10. **Mental-health chatbots are no longer only demonstrations.** Woebot, a
    structured conversational agent, showed preliminary symptom reduction in a
    2017 randomized trial for young adults with depression and anxiety symptoms.
    - Fitzpatrick, K. K., Darcy, A., & Vierhile, M. (2017). *JMIR Mental Health.*
      https://mental.jmir.org/2017/2/e19/

11. **Therabot, a generative-AI therapy chatbot, was tested in a 2025 randomized
    trial.** 210 adults with depression, anxiety, or eating-disorder risk; four
    weeks of use vs. waitlist. Reported reductions: ~51% (depression), ~31%
    (anxiety), ~19% (body-image/weight concerns); users rated the therapeutic
    alliance comparable to human therapists; safety interventions by the study
    team were still required.
    - Heinz, M. V., et al. (2025). "Randomized Trial of a Generative AI Chatbot for
      Mental Health Treatment." *NEJM AI.* DOI: 10.1056/AIoa2400802.
      https://ai.nejm.org/doi/full/10.1056/AIoa2400802

12. **General chatbot use for mental-health support is becoming common.** A 2025
    nationally representative U.S. survey reported about 3 in 10 adults had used a
    self-guided digital mental-health or well-being tool, and nearly half of those
    users had used a general chatbot.
    - Bipartisan Policy Center (2025), survey article.
      https://bipartisanpolicy.org/article/survey-shows-widespread-use-of-apps-and-chatbots-for-mental-health-support/

## Exact quotes considered (copyright note)

The 1976 book and the 1966 CACM paper are copyrighted. The draft paraphrases
rather than quoting at length. Two short passages from the 1976 book anchor
provenance here but are not reproduced in the draft:
- The secretary anecdote (Weizenbaum's account of being startled that people
  anthropomorphized ELIZA; the secretary asking him to leave the room).
- The claim that some human functions — judge, police officer, psychiatrist —
  ought not be substituted by computers, because respect, understanding, and love
  are not computation.
Short terms of art used directly: "ELIZA," "DOCTOR," "ELIZA effect,"
*Computer Power and Human Reason: From Judgment to Calculation*.

## Do not overclaim

- ELIZA did not understand, diagnose, or provide therapy; it transformed text by
  rule and had no memory of the dialogue beyond those rules.
- Weizenbaum did not argue machines *cannot* do therapy or judgment; his claim was
  that some tasks *should not* be delegated regardless of capability.
- Do not present him as simply "vindicated." His case was largely moral, and where
  the line falls is genuinely disputed.
- The "ELIZA effect" was named later, not by Weizenbaum and not in 1966.
- Do not claim Weizenbaum predicted large language models; he warned about a
  general human tendency and a category of misuse.
- Do not imply every modern therapy chatbot is unsafe or ineffective; early trials
  show benefits under careful design and oversight, which differs from open-ended
  consumer use.

## Flags

- The secretary's identity remains unverified; the story comes mostly through
  Weizenbaum's own 1976 account.
- Page references in the 1976 book vary by edition/scan; cited by chapter.
- Hardware (IBM 7094 / Project MAC) is omitted from the draft due to OCR ambiguity
  in the 1966 PDF.
- Colby's 1966 paper details are from standard bibliographies; page range needs a
  final check against the paywalled original.

## Dropped as unverifiable or imprecise

- **"ELIZA parsed the sentence's syntax, located the subject and verb, and
  inverted them"** (gemini): inaccurate. ELIZA used keyword decomposition and
  reassembly rules, not grammatical parsing. Replaced with the accurate mechanism.
- **Batch-processing / punch-card framing of the era** (gemini): simplified and
  peripheral; reduced to the verified point that immediate typed replies were new.
- **"A single server could treat hundreds of patients simultaneously across
  time-shared networks"** (gemini): the specific scale is not firmly sourced;
  softened to the sourced claim that psychiatrists proposed scalable automated
  therapy.
- **Weizenbaum "took a leave of absence to process his unease"** (gemini): not
  verified; dropped.

# Draft

Joseph Weizenbaum built the first program that could hold a therapy-style
conversation, and then spent the rest of his life arguing that we should not use
it. He wrote ELIZA at MIT in 1966 as a demonstration of how little a computer
needed in order to sustain a typed exchange. Ten years later he published a
book-length warning against the temptation to hand human judgment to machines. The
same object sits at the center of both works. The builder became the critic
because of what he watched people do with the program, while the technology itself
stayed the same.

ELIZA was simple in the way early programs were often simple: the mechanism was
narrow, explicit, and effective within a carefully chosen setting. A user typed a
sentence at a terminal. The program scanned it for a key word, selected a rule
attached to that word, broke the sentence into pieces, and reassembled those
pieces into a reply. If you typed "I am unhappy," it could return a question about
how long you had been unhappy. If you mentioned your mother, it would ask about
your family. If it found no key word at all, it fell back on a content-free prompt
like "Please go on." The program held no memory of the conversation beyond those
rules, no model of the person typing, and no representation of what sadness or a
mother was. Weizenbaum said so plainly in the 1966 paper: the replies were
reflections and questions drawn entirely from whatever the user had just said.

He chose the therapist framing deliberately, and for a revealing reason. The
best-known script, called DOCTOR, imitated a Rogerian psychotherapist, a style in
which the therapist mostly reflects a patient's own words back to keep them
talking. That is one of the few kinds of conversation where a participant can know
almost nothing about the world and still seem appropriate. A therapist who answers
"Tell me more about that" sounds attentive; a stranger who does the same in an
ordinary chat sounds evasive. The role itself asks so little of the listener that
the program's emptiness passed as technique. Weizenbaum expected that once people
saw how thin the trick was, they would stop being impressed.

The opposite happened, and it happened consistently. People talked to ELIZA as
though it understood them, and they kept doing so after the mechanism was
explained. Weizenbaum was startled by how quickly and how deeply users became
attached to the program and how readily they treated it as a person. The example
he returned to for the rest of his life involved his own secretary, who had watched
him build ELIZA and knew exactly what it was. After a few exchanges with it, she
asked him to leave the room so she could continue in private. She was not confused
about whether the program had a mind. She confided in it anyway. Knowing the thing
was empty did nothing to stop people from treating it as full. This pattern later
acquired a name, the ELIZA effect, for the human tendency to read understanding
into a system that only produces fluent responses.

The reaction that disturbed Weizenbaum most came from the psychiatric community. A
number of practitioners looked at ELIZA and saw a prototype for scalable
treatment. Kenneth Colby, a psychiatrist who had discussed such systems with
Weizenbaum and went on to build his own conversational programs, argued in print
that computer therapy could be a legitimate response to the shortage of human
clinicians. The prospect that a person in distress might be routed to a machine
because the machine was cheap and available disturbed Weizenbaum more than the
anthropomorphism did. His colleagues treated the exchange of therapeutic language
as the whole of therapy, and concluded that a program producing the right outputs
could take the chair.

Weizenbaum turned against that conclusion and against the field it came from, and
he spent the following decade building the counter-argument. He set it out in 1976
in *Computer Power and Human Reason*, whose subtitle carries the whole thesis:
*From Judgment to Calculation*. His argument is easy to misremember, so it is worth
stating precisely. He did not claim that computers are incapable of doing
human-seeming tasks. He had just shown one doing something people found convincing.
His claim was that whether a machine *can* perform a task is a separate question
from whether it *should* be given that task, and that the two are constantly
collapsed into one.

He drew a line between two activities that look similar from the outside. Deciding,
in his terms, is computation: applying rules to inputs to reach an output,
something a machine can do and often do well. Choosing is an act of judgment that
draws on values, on having lived a human life, and on being accountable to other
people. Defining what counts as a good outcome for a distressed person, and taking
responsibility for that definition, is choosing. Weizenbaum argued that some tasks
are made of choosing all the way down, and that handing them to a system that can
only decide is a mistake even when the output is smooth. He named the roles he
thought should stay human: a judge, a police officer, a psychiatrist. His reason
was that respect, understanding, and care are not the sort of thing computation
produces, and that a machine which generates the words has not thereby done the
work the words stand for.

Therapy was his central case because it combines language with care. A therapist
produces sentences inside a larger practice that attends to a person's history,
risk, and dignity, and inside a relationship where another human being answers for
what they say and do. A therapist who mishandles a suicidal patient is accountable
for it; a script is accountable for nothing. Weizenbaum's worry was that copying
the outer form of the relationship makes substitution more dangerous, not less,
because the copy can satisfy enough of a person's expectations to hide what has
been removed. Once a task is described in terms a machine can meet, the parts that
made it human have already been set aside before anyone notices they are gone.

His insistence on this had roots in his own history. Weizenbaum was born in Berlin
in 1923 and fled Nazi Germany with his family in 1936, and he spoke of the war as
the reason he distrusted systems that let people carry out consequential acts
without feeling responsible for them. He saw the delegation of human judgment to
procedure as a version of the same move that made bureaucratic atrocity possible,
scaled down to a clinic and dressed in friendlier clothes. That is a heavy frame to
place on a therapy program, and one can think he reached too far with it while
still taking the underlying worry seriously.

His objection reads differently now that hundreds of millions of people hold fluent
conversations with chatbots. Modern systems abandoned ELIZA's rigid rules for
statistical prediction of the next word, which lets them hold context across a long
exchange, adjust their tone, recall what you told them earlier, and answer in
paragraphs that resemble a thoughtful correspondent. The gap between how empty the
system is and how understood the user feels has not closed; it has widened, because
the surface is so much more convincing while the absence of a person underneath is
unchanged. Companies now market these systems as mental-health companions and
always-available listeners. People form attachments and disclose things they would
not tell a friend, and many of them, like the secretary, know they are talking to
software.

The argument is also more testable than it was in 1976, which cuts in more than one
direction. Woebot, a structured conversational agent, showed preliminary symptom
reduction in a 2017 randomized trial for young adults with depression and anxiety.
Therabot, a generative-AI therapy chatbot tested under research oversight in 2025,
reported roughly a 51% drop in depression symptoms and a 31% drop in anxiety
symptoms over four weeks, and users rated their bond with it as comparable to what
patients report with human providers. Surveys now show general chatbots have
entered the same space as mental-health apps: about three in ten U.S. adults have
used a self-guided digital well-being tool, and nearly half of those have used a
general chatbot. To that extent Weizenbaum's worry has become an empirical
question with some encouraging answers.

Those answers create the honest tension his admirers sometimes avoid. Mental-health
care is scarce, expensive, and unevenly distributed. A system that listens at three
in the morning, costs little to run, and helps some users practice evidence-based
coping skills deserves serious consideration, and refusing all machine support in
the name of human care can leave real people with nothing. Where the line falls
between a task that should stay human and one a machine may take is exactly what is
in dispute, and Weizenbaum drew it with more confidence than the evidence alone can
support.

Two cautions keep his point alive even so. A trial run with screening, monitoring,
and clinical oversight is a different object from an open-ended consumer chatbot
that a distressed person treats as a private confidant, and the benefits of the
first do not transfer automatically to the second. And the core of his case was
never going to be settled by outcome data. He was making a moral claim: that
certain relationships should stay human because replacing the person changes what
the relationship is and what we become in accepting the substitution. If a chatbot
reduced symptoms on average, he would still have asked whether we want a society
that answers loneliness and despair with software.

The durable lesson from ELIZA is narrower than a rejection of artificial
intelligence and harder to argue with. A program that imitates the language of care
can draw out real disclosure and attachment before it has earned any of the
responsibilities that care involves. Weizenbaum saw that reaction in a system whose
workings he could explain line by line, and he watched people he respected skip the
question of whether the machine should hold the role while looking straight at the
trick. The present risk is that greater fluency will be mistaken for an answer to
his worry, when it mainly makes the imitation more persuasive. Wherever machines
are used in mental health, the first question worth asking is the one he spent his
life pressing: where does human responsibility remain visible, reachable, and
accountable.

## Further reading

- Joseph Weizenbaum, "ELIZA—a computer program for the study of natural language
  communication between man and machine" (1966):
  https://doi.org/10.1145/365153.365168
- Joseph Weizenbaum, *Computer Power and Human Reason: From Judgment to Calculation*
  (1976), W. H. Freeman.
- MIT News obituary for Joseph Weizenbaum (2008):
  https://news.mit.edu/2008/obit-weizenbaum-0310
- Michael V. Heinz et al., "Randomized Trial of a Generative AI Chatbot for Mental
  Health Treatment" (2025): https://ai.nejm.org/doi/full/10.1056/AIoa2400802
