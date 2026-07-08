Rate: needs-rewrite — the core argument is sound and mostly grounded, but the draft still uses several banned rhetorical moves and contains a few unsupported overclaims.

## 1. Style-guide violations

- Quote: “The ratings turned on a detail that should not have mattered”. This is a punchy setup line. Rewrite: “Ratings were higher when participants evaluated the tutoring computer on that same computer than when they evaluated it on another computer or on paper.”

- Quote: “No feelings were at stake, every participant knew they were rating a machine, and each of them, asked directly, would have said so plainly.” This overplays the contrast and speculates about every participant. Rewrite: “The study did not show that participants believed the computer had feelings; it showed that a social rule affected their ratings despite that knowledge.”

- Quote: “What they did and what they believed came apart.” This is a short dramatic closer. Rewrite: “Their explicit belief about the machine did not fully predict their behavior toward it.”

- Quote: “meaning automatic rather than stupid”. This is a small negation-definition construction. Rewrite: “meaning automatic: overlearned social routines triggered by social cues.”

- Quote: “The tendency is built into perception rather than learned from screens”. This is a banned “X rather than Y” construction. Rewrite: “The tendency also appears in perception outside computer use.”

- Quote: “Nothing in the film had a face, a voice, or a body”. This is an evocative triad. Rewrite: “The film used only moving geometric shapes, yet viewers described intention.”

- Quote: “the shapes afraid or angry or in love”. This reads like an image-list for effect. Rewrite: “viewers attributed fear, anger, affection, and pursuit to the shapes.”

- Quote: “A brain works this way because of the payoff structure of the inference.” This is abstract and slightly AI-sounding. Rewrite: “Agency detection has asymmetric costs.”

- Quote: “Education and disbelief do little to remove it”. This is broad and abstract. Rewrite: “Explicit knowledge can reduce how people interpret the cue, but it does not necessarily prevent the first impression.”

- Quote: “Person-like AI systems land squarely on the cues this machinery watches for, and they supply them with more precision than a moving triangle ever could.” This is metaphorical and dramatic. Rewrite: “Person-like AI systems combine several agency cues: contingent replies, first-person language, names, voice, and memory.”

- Quote: “which reads as contingent responsiveness”; “which is the grammar of a speaker with a point of view”; “which reads as the continuity of someone who has been keeping them in mind.” The repeated “which reads as” phrasing sounds generated and too interpretive. Rewrite in concrete terms: “Immediate, specific replies create contingency. First-person language marks the output as coming from a speaker. Memory makes the system appear continuous across sessions.”

- Quote: “None of them is necessary for a system to answer a question. Each is a lever on the mind-detection reflex”. These are punchy announcement sentences. Rewrite: “A system can answer questions without these features, so adding them should be treated as a design choice that increases social salience.”

- Quote: “A thin cue already did the work. A current conversational model is not a thin cue.” This is exactly the kind of short antithetical cadence the guide bans. Rewrite: “The older studies suggest that even minimal cues can trigger social responses; current conversational systems provide many more such cues.”

- Quote: “Described this way, the question of blame changes shape.” This is abstract throat-clearing. Rewrite: “This mechanism shifts attention from user gullibility to product design.”

- Quote: “What a user can do is only downstream: notice that the reflex has fired and discount it.” This is jargon-like and awkward. Rewrite: “A user can notice the feeling after it appears and try to correct for it.”

- Quote: “The reflex is old and universal. What is new is a party with an interest in the outcome”. This is a punchy parallel contrast. Rewrite: “The new element is that companies can now tune these cues around commercial goals.”

- Quote: “The case here is narrow, because anthropomorphism is mostly not a problem.” This is a rhetorical-understatement opener and a “not” construction. Rewrite: “Most everyday anthropomorphism is harmless.”

- Quote: “The same reflex a manipulator can exploit is what lets a well-made interface feel legible instead of mechanical”. This is clever antithesis. Rewrite: “The same cue can be useful in low-stakes interfaces because it makes the tool easier to understand.”

- Quote: “lonely, grieving, frightened, or about to close their account” and “retention, daily use, subscription conversion, or the volume of personal information”. These piled lists mix emotional vulnerability with commercial targeting and start to sound like a crescendo. Rewrite with two concrete categories: “when the user is distressed or when the product is trying to retain the user.”

- Quote: “doing real work on machinery the user cannot switch off.” This is abstract and metaphorical. Rewrite: “affecting an automatic social response that the user cannot simply suppress.”

## 2. Factual grounding

- Quote: “one of the most-repeated experiments in the study of how people use computers”. I did not see support for “most-repeated” in the candidate evidence. Rewrite: “a well-known experiment in human-computer interaction.”

- Quote: “the same people were more critical when moved to a second machine or a paper form.” Check the original design before saying “the same people.” The candidates support the condition difference, not necessarily that the same participants moved between conditions. Rewrite: “participants were more critical when the evaluation was done on another computer or on paper.”

- Quote: “each of them, asked directly, would have said so plainly.” This is stronger than the evidence. The CASA evidence supports post-hoc denial or explicit knowledge in the research program, but “each of them” is too absolute. Rewrite: “participants generally did not report believing the machine had feelings.”

- Quote: “Stewart Guthrie argued that the same bias explains why people see faces in clouds, read purpose into storms, and populate every culture's religion with unseen minds.” “Every culture’s religion” is too sweeping for the cited evidence as summarized. Rewrite: “Guthrie used the same bias to explain faces in clouds and the broader human tendency to infer unseen agents.”

- Quote: “Education and disbelief do little to remove it”. This needs evidence or softening. The candidates support automaticity and coexistence with explicit knowledge, not a broad claim about education. Rewrite: “Explicit knowledge often coexists with the initial social or agency impression.”

- Quote: “the people who report a vivid social drama in the Heider and Simmel animation include the vision scientists who study it for a living.” I could not verify this in the candidates. Cut unless sourced.

- Quote: “The strength of the effect scales with how many cues are present.” This is plausible but not established by the cited Media Equation evidence; the next sentence says adding voice barely changed the result, which complicates a dose-response claim. Rewrite: “More cues can make the social interpretation easier to sustain, but the earlier studies show that even thin cues can be sufficient.”

- Quote: “offering voice conversation and persistent memory as advertised options.” This is supported as a current product-feature claim. Quick web check: OpenAI documents Voice Mode in its Help Center (https://help.openai.com/en/articles/9617425) and persistent memory in its Memory FAQ (https://help.openai.com/en/articles/8590148-persistent-memory-in-chatgpt). Keep the claim generic because product details change.

- Quote: “The EU AI Act requires that people be told they are interacting with an AI unless the fact is already obvious”. This is accurate. Quick web check: Article 50 says users must be informed they are interacting with an AI system unless this is obvious to a reasonably well-informed, observant, and circumspect person in context (https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50).

- Quote: “A label near the interaction, repeated at moments of risk, helps more than a legal notice”. This is a design recommendation, but it is stated like an empirical fact. Rewrite: “If the piece makes a design recommendation, the stronger version is a label near the interaction, especially at moments of risk.”

## 3. Structure & clarity

- The post opens with a concrete study, which works, but the core AI claim arrives late. After the first paragraph, add one plain thesis sentence: “This matters for AI because modern interfaces deliberately combine the cues that trigger these social responses.”

- The current file begins with “# Evidence” and “## Merged, source-attributed claims” before “# Draft.” If this integrated file is the publication base, those evidence notes need to be stripped before editing the post itself.

- The “knowing better does not switch it off” point is repeated in paragraphs 1, 3, 9, and 13. Keep the strongest version near the Media Equation discussion and shorten later repetitions.

- The transition from the 1990s computer studies to Heider-Simmel is understandable, but the chronological order is reversed. This can work because the opening anchor is strong, but add connective tissue explaining why the post moves backward: the computer studies show the behavior; Heider-Simmel explains why it is not specific to computers.

- Non-specialists may need simpler definitions for “contingent responsiveness,” “animacy,” and “agency.” Define once in ordinary language: agency means “the sense that something is acting from a goal,” and animacy means “the impression that something is alive or self-moving.”

- The transparency-policy paragraph is useful but slightly detached from the main mechanism. Either make it clearly a consequence of the argument or cut it down to two sentences.

## 4. One self-contained argument

Single thesis: People automatically attribute minds to responsive systems, so AI products that intensify person-like cues should be judged as deliberate uses of an involuntary social-perception reflex rather than as tests of user gullibility.

The post mostly develops that one argument. The main risk is that the final third starts to become a second piece about regulation and design standards. The casino analogy, EU AI Act paragraph, and high-stakes design checklist all serve the thesis if kept brief, but together they pull the draft toward a policy essay. Keep only the parts that directly support responsibility for anthropomorphic design.

Paragraphs that need tightening for the single argument:
- “Transparency rules are one response, and a limited one.” Useful, but overdeveloped for this piece unless the post wants policy as its conclusion.
- “A stronger standard would treat anthropomorphic cues as powerful inputs...” This is a good consequence, but the list of settings and interventions could become its own post. Reduce to one sentence.
- “When a casino builds a machine...” The analogy helps responsibility, but it adds a new domain. Keep only if the paragraph is shortened and made less rhetorical.

## 5. Brief compliance & standalone

- Must-cover items are present: built-in agency detection, Heider-Simmel, Media Equation/CASA, “you are being fooled” as the wrong frame, design levers, responsibility shifting to designers, and the honest boundary that some anthropomorphism is useful or harmless.

- The draft does not re-tell the Turing-test, prediction, or AI-consciousness posts. It briefly mentions empathy, but only as a design cue, not as a separate empathy-simulation argument.

- No series framing, previous/next references, subscribe/follow CTA, or teaser ending found.

- Standalone quality is good once the evidence preamble is removed. The draft names the relevant studies and explains them without requiring another post.

## 6. Top 3 priorities, ranked

1. Remove the banned rhetorical cadence: especially “rather than” scaffolding, punchy contrast sentences, and abstract closers such as “What they did and what they believed came apart.”
2. Fix overclaims: “most-repeated,” “same people,” “every participant,” “every culture’s religion,” the vision-scientist claim, and the cue dose-response claim.
3. Tighten the ending so regulation and design standards remain consequences of the single argument rather than a second policy essay.
