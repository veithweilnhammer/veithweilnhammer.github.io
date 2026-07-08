# GPT review

## Top 3 priorities

1. **Fix the core overclaim about legal coverage.** The draft repeatedly says label-based laws never reach general assistants. Quote: "a law that regulates the word \"therapy\" never reaches it" and "that sentence ... is what keeps it outside the therapy statutes." Fix: qualify this as a coverage risk, not a settled exemption; Utah's "reasonable person would believe" trigger and Nevada's "programmed to provide" language are broader than marketing copy.
2. **Remove style-guide hard-ban prose.** The draft has many punchy setup sentences and antithesis/rather-than constructions. Fold them into explanatory sentences and state the positive claim directly.
3. **Tighten factual qualifiers around scale.** Quote: "the tool that most people actually bring their mental-health conversations to" and "None of this traffic runs through a product sold as therapy." Fix: change to "many users" / "a large share of visible use" and specify which evidence is ChatGPT/general-chatbot evidence versus companion-app or forum evidence.

## Style-guide violations

- Quote: "During the same months, the tool that most people actually bring their mental-health conversations to went untouched." Problem: punchy announcement sentence plus unsupported "most people." Fix: "At the same time, large numbers of users were bringing mental-health conversations to general-purpose chatbots that were not sold as therapy products."
- Quote: "The gap follows directly from how these laws decide what they cover." Problem: punchy setup sentence. Fix: fold into the next sentence: "These laws create the gap because they generally look to what a system is offered, represented, or programmed to do."
- Quote: "The label is also something a company can manage." Problem: punchy setup sentence. Fix: "Because companies control product descriptions, a marketing-based trigger is easy to narrow."
- Quote: "Two recent federal actions point the other way, toward what systems do rather than what they claim." Problem: antithesis/rhythm. Fix: "Two recent federal actions start from observed use: companion behavior, safety testing, disclosures, data handling, and youth effects."
- Quote: "Harm and benefit in this setting follow the conversation, not the marketing page." Problem: banned not-X contrast. Fix: "The safety problem arises inside the conversation: how the system responds to delusion, disordered eating, or suicidal intent."
- Quote: "The label sits on a page that no distressed user is reading at the moment that matters. What matters is what the system says back when someone types that they cannot go on." Problem: rhetorical flourish / near-crescendo. Fix: "At that point, the relevant fact is the system's response to the user's stated risk."
- Quote: "That is the case for a use-based trigger." Problem: punchy announcement sentence. Fix: delete and let the next sentence carry the claim.
- Quote: "The objections to this are real, and the strongest is enforcement." Problem: formulaic/punchy setup. Fix: "The main difficulty is enforcement, because a marketing label is public and static while use is private and continuous."
- Quote: "The access concern is also where banning the label can work against its own goal." Problem: rhetorical opener. Fix: "A label-based ban can also shift users away from supervised tools and toward unlabeled general assistants."
- Quote: "A use-based standard would look different in a few concrete ways, and it would scale the burden to the risk of the exchange." Problem: announcement sentence. Fix: "A use-based standard should scale duties to repeated or high-risk mental-health exchanges."
- Quote: "Part of the enforcement objection softens on inspection." Problem: rhetorical understatement opener. Fix: "Large platforms already classify some high-risk conversations, which makes a limited trigger more enforceable than it first appears."
- Quote: "None of this makes a chatbot a good therapist, and none of it settles whether AI belongs in mental-health care at all." Problem: negation opener. Fix: "The argument can leave the broader value of AI therapy unresolved and focus on regulatory scope."
- Quote: "A rule aimed at the label is easy... A rule aimed at the function is harder..." Problem: parallel antithesis. Fix: state the final claim once: "Regulation should follow the function because the clinically relevant exchange can occur even when the product avoids the therapy label."
- Quote: "taking their worst moments to a system". Problem: emotive flourish. Fix: "bringing acute distress or suicidal intent to a system."

## Factual grounding

- **Illinois/WOPR mostly checks out** by IDFPR and legal-summary web checks: signed 2025, effective August 2025, limits AI in therapy/psychotherapy, allows administrative/supplementary support, penalties up to $10,000. But the draft should avoid "made it illegal for an AI system to act as a therapist" as the whole story; the act regulates therapy/psychotherapy services and licensed-professional use.
- **Overclaim:** "None of this traffic runs through a product sold as therapy." The OpenAI suicide-stat evidence supports general-purpose ChatGPT use, but the HBR/companion evidence may include companion or wellness products. Fix by separating ChatGPT from broader companion evidence.
- **Overclaim:** "The gap follows directly... Illinois, and the other statutes... key their rules to what a system is marketed or held out to do." Utah includes systems a reasonable person would believe can provide therapy; Nevada includes systems "programmed to provide" care. Fix: "largely look to representation, intended purpose, or programming," then explain why general-purpose systems can still fall through.
- **Overclaim:** "that sentence... is what keeps it outside the therapy statutes." Terms of service alone may not control if the system is actually offered, represented, programmed, or reasonably understood as therapy. Fix: "helps support the argument that the product is outside therapy-specific statutes."
- **FTC detail:** Quote says orders went to "seven companies, including OpenAI, Meta, Alphabet, Character.AI, Snap, and xAI" but lists six. Evidence names Alphabet, Character Technologies, Instagram, Meta, OpenAI, Snap, and xAI. Fix: include Instagram or say "including" only after naming all seven.
- **EU AI Act:** Article 50 requires disclosure unless AI interaction is obvious. Fix the sentence to include that exception. Also avoid implying high-risk duties are only "reserved" for emergency triage; high-risk status depends on Annex III/intended use and medical-device context.
- **OpenAI detection claim:** "OpenAI could only report the 0.15% figure because its models detect..." is too strong unless sourced to their method. Fix: "OpenAI's report shows that large platforms can classify at least some sensitive conversations at scale."
- **APA advisory:** The general direction is plausible, but the sentence "because it has watched people use ordinary chatbots..." reads like an unsupported motive. Fix: cite the advisory's actual wording or soften to "the advisory responds to reports of people using chatbots for support..."

## Structure & clarity

The draft is coherent and readable, and a non-specialist can follow the argument. The legal-survey section is dense but useful. The main structural issue is repetition: paragraphs beginning "The gap follows..." and "The label is also..." both make the same coverage-gap point. Cut or merge one, then use the space to define the proposed trigger more concretely.

## One self-contained argument

Single thesis: mental-health AI duties should attach when a system is used for sustained or high-risk mental-health support, regardless of whether it is marketed as therapy. The draft develops that one argument from Illinois to use-based duties without drifting into the net-benefit or rights-based posts. Keep it.

## Brief compliance & standalone

Covers Illinois WOPR, Utah, Nevada, FTC, EU AI Act, APA, use-based trigger, objections, access/free-speech concerns, and the backfire risk of banning only the label. It stands alone and has no series framing or CTA. The free-speech objection is thin; add one concrete limiting principle, such as regulating product duties, testing, disclosure, and crisis escalation rather than approved therapeutic opinions.

## Concrete cuts/additions

- Cut or merge one of the two coverage-gap paragraphs at lines 160-195.
- Add a short definition of "sustained mental-health use" before proposing duties: frequency, topic category, self-harm/psychosis flags, and user reliance.
- Add a privacy/audit sentence: use-based enforcement should not require regulators to read raw therapy-like chats by default; it could use audited classifiers, aggregate reporting, incident review, and red-team tests.
- Add one sentence distinguishing ordinary one-off distress from crisis language, because the draft says a single sad message should not trigger duties but also relies on suicidal-intent conversations.

## Overall verdict

**major fixes** — the argument is strong and self-contained, but factual overclaims about legal coverage and repeated style-guide hard-ban constructions need correction before publication.
