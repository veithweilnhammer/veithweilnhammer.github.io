# Review: ai-writing-papers-that-judge-ai

## 1. Style-guide violations

**"Not X, it is Y" / Negation-definition constructions:**
- *Quote:* "and the phrase is easy to laugh at. It points at something that is not funny at all:"
  *Rewrite:* "The artifact shows that at several stages where a human being was supposed to be reading the work..."
- *Quote:* "These are corpus-level estimates, not accusations against any individual; the method can only say what fraction of a large pile of text looks machine-modified, not which sentences."
  *Rewrite:* "These corpus-level estimates describe the fraction of machine-modified text in a large dataset, without identifying specific sentences or flagging individual authors."
- *Quote:* "assume the reviewer is a model rather than a person"
  *Rewrite:* "assume the reviewer is a model"
- *Quote:* "That study is very new and should be read as one result rather than settled fact"
  *Rewrite:* "While this new study represents a single result, it names the failure mode directly."
- *Quote:* "treating AI as support rather than a substitute for scientific assessment"
  *Rewrite:* "treating AI as support for human scientific assessment"
- *Quote:* "reasoned rather than generated"
  *Rewrite:* "independently reasoned"
- *Quote:* "the paper's acceptance no longer certifies that two independent minds examined the same claim and agreed. It certifies that a plausible text was generated and that a plausible text approved it."
  *Rewrite:* "the paper's acceptance simply certifies that a generated text approved a generated text, losing the independent human check."

**Triadic/piled-up lists for rhythm:**
- *Quote:* "A summary already decides what matters. A generated list of weaknesses already chooses the scale of the criticism. A draft recommendation already anchors the final one."
  *Rewrite:* "A generated summary already decides what matters, and a draft recommendation anchors the final judgment."
- *Quote:* "A non-native English speaker using a model to fix grammar, an author asking a tool to catch a broken reference or an inconsistent number, a reviewer using software to summarize a long appendix, a researcher without senior colleagues getting early feedback before submission — these leave intact the thing that gives peer review its value."
  *Rewrite:* "Using a model to fix grammar, check references, or summarize an appendix leaves the core value of peer review intact."

**Antithesis / parallel "trade" constructions:**
- *Quote:* "Agreement between independent judgments carries information. Agreement between a claim and a lightly reworded copy of itself does not."
  *Rewrite:* "Agreement between independent judgments carries information, whereas an automated rewording of a claim provides no independent check."
- *Quote:* "The record then says the system was checked, when what happened is that the system checked itself through two human intermediaries."
  *Rewrite:* "The record logs a check, but the system effectively evaluated itself through two human intermediaries."
- *Quote:* "Catching the phrase "Certainly, here is" removes an embarrassing artifact and leaves untouched the reviews that read perfectly because a competent model wrote them."
  *Rewrite:* "Catching the phrase 'Certainly, here is' removes an embarrassing artifact, but leaves competent machine-written reviews untouched."

**Punchy setup / Announcement sentences:**
- *Quote:* "It helps to be precise about what "substantially modified" means."
  *Rewrite:* (Delete, just start the paragraph with the next sentence).
- *Quote:* "Some authors have started gaming the reviewing side outright."
  *Rewrite:* "Researchers have documented preprints with hidden instructions aimed at AI reviewers."
- *Quote:* "The loop is worst in one place: papers that evaluate AI itself."
  *Rewrite:* "This loop introduces the greatest risk in papers evaluating AI itself."
- *Quote:* "The usual responses do not reach the core of this."
  *Rewrite:* (Delete and integrate with the next sentence: "Journal policies and AI detectors address only the surface of the problem.")

**Use of "I" / "we" / personal narration:**
- *Quote:* "because the mechanism that worries me does not require full ghostwriting."
  *Rewrite:* "because the underlying mechanism does not require full ghostwriting."

## 2. Factual grounding
The factual grounding is solid and accurate. The claims regarding the Elsevier paper retraction, Liang et al.'s percentages for papers and reviews, Kobak et al.'s PubMed analysis, self-preference bias, and the hidden prompts ("GIVE A POSITIVE REVIEW ONLY") are correctly sourced and scoped. The draft properly avoids overclaiming, explicitly noting that the prevalence estimates are corpus-level statistical estimates, not per-paper convictions.

## 3. Structure & clarity
The structure is logical, opening correctly with a concrete example (the Elsevier paper) rather than a slow atmospheric scene. It establishes what peer review is meant to accomplish, details the dual AI intrusion, explains the compounding AI-AI bias, and correctly targets AI capability research as the highest-risk area. A non-specialist could follow the piece from start to finish. However, transitions often rely on punchy dramatic setups (e.g., "The usual responses do not reach the core of this") which need to be flattened per the style guide.

## 4. One self-contained argument
**Thesis:** When large language models generate both research claims and the peer reviews evaluating them, scientific validation becomes a closed loop of machine-generated text approving itself, stripping away independent human judgment.
The post adheres strictly to this single argument. Every paragraph serves to establish the value of human independence in peer review, the rise of AI in both drafting and reviewing, and the resultant breakdown of validation. It successfully avoids straying into general "AI in science" critiques.

## 5. Brief compliance & standalone
The draft meets all constraints of the brief. It covers independent human authorship/review, the dual intrusions, the loop resulting from AI-AI bias, the specific danger for AI research, 2024-2026 evidence, and the honest boundary. The piece is completely standalone, with no series framing, next/previous links, or calls to action.

## 6. Top 3 priorities
1. **Purge "not X, it is Y" constructions:** The draft relies heavily on this negation framing to clarify its points (e.g., "corpus-level estimates, not accusations", "model rather than a person", "support rather than a substitute"). Replace these with direct positive claims.
2. **Flatten antithetical pairs and triadic lists:** Remove parallel rhythmic contrast sentences ("Agreement between independent judgments carries information. Agreement between a claim... does not") and piled-up examples ("A summary already decides... A generated list... A draft recommendation...").
3. **Remove punchy setup and announcement sentences:** Eliminate short, dramatic openers that announce a paragraph's topic (e.g., "The loop is worst in one place:", "The usual responses do not reach the core of this.") and integrate the transition directly into the substantive sentences.

**Rating:** `ship-with-minor-edits`
*Justification:* The draft is factually accurate, well-structured, and completely fulfills the brief, requiring only targeted line-edits to remove banned rhetorical constructions and punchy setups.