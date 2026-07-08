<!--
==========================================================
SUBSTACK — copy these into the editor's Title / Subtitle boxes:
  Title:    ELIZA's Creator Spent His Life Warning Us About ELIZA
  Subtitle: The man who built the first chatbot became its most serious critic — and his reasons still apply.
----------------------------------------------------------
  Suggested tags: ELIZA, Weizenbaum, chatbots
  Visibility checklist:
    [ ] Subtitle doubles as an SEO hook (done above)
    [ ] TL;DR in the first 2 lines
    [ ] 1-2 internal links to related posts
    [ ] Scannable subheads
    [ ] Clear subscribe / share CTA at the end
    [ ] Canonical / cross-post link back to https://veithweilnhammer.github.io/blog/eliza-creator-warning/
==========================================================
Paste everything BELOW this comment into the Substack body.
-->

**TL;DR — Joseph Weizenbaum built ELIZA in 1966, was disturbed that people confided in a program they knew was simple, and warned for decades against delegating human care to machines.**

Joseph Weizenbaum wrote ELIZA at MIT in 1966, an early program that could sustain
a typed, therapy-style exchange, and he spent much of his later life arguing that
programs like it should not replace people in roles that require care and
judgment. He built ELIZA as a demonstration of how little a computer needed in
order to keep a conversation going. Ten years later he published a book-length
warning against handing human judgment to machines. ELIZA connects the two: his
criticism grew out of how people responded to a program whose mechanism he could
explain line by line.

ELIZA used explicit rules that worked well only in a narrow conversational
setting. A user typed a sentence at a terminal. The program scanned it for a key
word, selected a rule attached to that word, broke the sentence into pieces, and
reassembled those pieces into a reply. Typing "I am unhappy" could return a
question about how long the unhappiness had lasted. Mentioning a mother could
prompt a question about family. With no key word at all, it fell back on a
content-free prompt such as "Please go on." The program held no memory of the
conversation beyond those rules, and it had no representation of the person typing
or of what sadness or a mother actually was. Weizenbaum said so plainly in the
1966 paper: the replies were reflections and questions drawn entirely from
whatever the user had just said.

The therapist frame mattered because it let the program answer with reflections
rather than facts. The best-known script, called DOCTOR, imitated a Rogerian
psychotherapist, a style in which the therapist mostly mirrors a patient's own
words back to keep them talking. That is one of the few kinds of conversation
where a participant can know almost nothing about the world and still seem
appropriate. The same reflective question that sounds attentive from a therapist
would sound evasive from a stranger in an ordinary chat, because the therapist's
role is expected to give little back. The role asked so little of the listener
that the program's emptiness passed as technique. Weizenbaum expected that once
people saw how thin the trick was, they would stop being impressed.

Instead, many users treated ELIZA as though it understood them, and some kept
doing so after the mechanism was explained. Weizenbaum was startled by how quickly
and how deeply people became attached to the program and how readily they treated
it as a person. The example he returned to for the rest of his life, in his own
account, involved his secretary, who had watched him build ELIZA and knew what it
was. After a few exchanges with it, she asked him to leave the room so she could
continue in private. She understood exactly what the program was and confided in
it regardless. This pattern later acquired a name, the ELIZA effect, for the human
tendency to read understanding into a system that only produces fluent responses.

The reaction that disturbed Weizenbaum most came from psychiatry. Some
practitioners looked at ELIZA and saw a prototype for scalable treatment. Kenneth
Colby, a psychiatrist who had discussed such systems with Weizenbaum and went on
to build his own conversational programs, argued in print that computer therapy
could be a legitimate response to the shortage of human clinicians. The prospect
that a person in distress might be routed to a machine because the machine was
cheap and available disturbed Weizenbaum more than the anthropomorphism did. These
proposals treated the exchange of therapeutic language as the whole of therapy,
and concluded that a program producing the right words could replace some of the
work a therapist does.

Weizenbaum rejected that conclusion and spent the following decade building the
counter-argument. He set it out in 1976 in *Computer Power and Human Reason*,
whose subtitle carries the thesis: *From Judgment to Calculation*. Weizenbaum
argued that whether a machine *can* perform a task is a separate question from
whether it *should* be given that task. He had just built a program that convinced
people, but he believed capability alone does not justify delegation, and that the
two questions are constantly run together.

Weizenbaum distinguished between two activities that appear similar but rely on
different mechanisms: deciding and choosing. Deciding, in his terms, is
computation, applying rules to inputs to reach an output, which a machine can do
and often do well. Choosing is an act of judgment that draws on values, on having
lived a human life, and on being answerable to other people. Defining what counts
as a good outcome for a distressed person, and taking responsibility for that
definition, is choosing. He argued that some tasks require judgment at every step,
and that handing them to a system that can only decide is a mistake even when the
output is smooth. He named the roles he thought should stay human: a judge, a
police officer, a psychiatrist. His reason was that respect, understanding, and
care are not products of computation, and that a machine generating the words has
not thereby done the work those words stand for.

Weizenbaum's distrust of delegating consequential acts to systems had roots in his
own history. He was born in Berlin in 1923 and fled Nazi Germany with his family
in 1936, and he spoke of the war as the reason he distrusted arrangements that let
people carry out serious acts without feeling responsible for them. He saw
automated care as another case where procedure could obscure who was responsible
for a human decision. That is a heavy frame to place on a therapy program, and one
can take the underlying worry seriously while thinking he reached too far with it.

Therapy was his central case because it combines language with care. A therapist
produces sentences inside a larger practice that attends to a person's history,
risk, and dignity, and inside a relationship where another human being answers for
what they say and do. A therapist is accountable for mishandling a suicidal
patient. A script carries no responsibility. Weizenbaum's worry was that copying
the outer form of the relationship makes substitution dangerous, because the copy
can satisfy enough of a person's expectations to hide what has been removed. Once
a task is described in terms a machine can meet, the human parts of it can be set
aside before anyone notices they are gone.

His objection is more concrete now that many people use fluent conversational
systems for advice, companionship, and mental-health support. Modern systems
replaced ELIZA's rigid rules with statistical prediction of the next word, which
lets them hold context within a conversation, adjust their tone, and answer in
paragraphs that resemble a thoughtful correspondent; some products also add memory
features that carry information across sessions. These systems are far more fluent
than ELIZA, so users can feel understood even when no accountable person is taking
part in the exchange. Companies market some of these systems as mental-health
companions and always-available listeners. People form attachments and disclose
things they would not tell a friend, and many of them, like the secretary, know
they are talking to software.

Modern chatbots also turn Weizenbaum's worry into an empirical question, and early
trials show measurable benefits under careful conditions. Woebot, a structured
conversational agent, showed preliminary symptom reduction in a 2017 randomized
trial for young adults with depression and anxiety symptoms. Therabot, a
generative-AI therapy chatbot tested under research oversight in 2025, reported
roughly a 51% drop in depression symptoms and a 31% drop in anxiety symptoms over
four weeks compared with a waitlist, and users rated their bond with it as
comparable to what patients report with human providers; the study team still had
to intervene on safety during the trial. A nationally representative U.S. poll
conducted in December 2025 reported that about three in ten adults had used a
self-guided digital mental-health or well-being tool, and nearly half of those had
used a general chatbot.

These results complicate a simple rejection of mental-health chatbots, because
mental-health care is scarce and expensive. A system that listens at three in the
morning, costs little to run, and helps some users practice evidence-based coping
skills deserves serious consideration, and refusing all machine support in the
name of human care can leave real people with nothing. Where the line falls
between a task that should stay human and one a machine may take is exactly what is
in dispute, and Weizenbaum drew it with more confidence than the evidence alone
can support.

Two limits keep his point alive. A trial run with screening, monitoring, and
clinical oversight is a different thing from an open-ended consumer chatbot that a
distressed person treats as a private confidant, and the benefits of the first do
not transfer automatically to the second. His case was also never going to be
settled by outcome data, because it was largely a moral claim: that certain
relationships should stay human because replacing the person changes what the
relationship is. Even if a chatbot reduced symptoms on average, he would still
have asked whether a society should answer loneliness and despair with software.

The durable lesson from ELIZA focuses on the imitation of care. A program that
mimics the language of care can draw out real disclosure and attachment before it
has earned any of the responsibilities that care involves. Weizenbaum saw that
reaction in a system whose workings he could explain line by line, and he watched
people he respected skip the question of whether the machine should hold the role.
The present risk is that greater fluency will be mistaken for an answer to his
worry, when it mainly makes the imitation more persuasive. Wherever machines are
used in mental health, the first question worth asking is the one he spent his life
pressing: where human responsibility stays visible and reachable.

## Further reading

- Joseph Weizenbaum, "ELIZA—a computer program for the study of natural language
  communication between man and machine" (1966):
  https://doi.org/10.1145/365153.365168
- Joseph Weizenbaum, *Computer Power and Human Reason: From Judgment to
  Calculation* (1976), W. H. Freeman.
- MIT News obituary for Joseph Weizenbaum (2008):
  https://news.mit.edu/2008/obit-weizenbaum-0310
- Michael V. Heinz et al., "Randomized Trial of a Generative AI Chatbot for Mental
  Health Treatment" (2025): https://ai.nejm.org/doi/full/10.1056/AIoa2400802

---
*Originally posted on [my blog](https://veithweilnhammer.github.io/blog/eliza-creator-warning/). If this was useful, consider subscribing and sharing.*
