# Review: Prediction Is Not Understanding, in Brains or in Machines

## 1. Style-guide violations

- **"Not X, it is Y" / "Not X but Y" constructions:**
  - *Draft:* "What settles a question like this is not more staring at the output. It is evidence about the internal process..."
    *Rewrite:* "Evidence about the internal process settles this question, and for once there is a clean example of how to get it."
  - *Draft:* "...rather than passively receiving the world."
    *Rewrite:* Cut this clause; just end the sentence at "prediction error."
  - *Draft:* "That a process minimizes prediction error tells you its computational job. It does not, on its own, tell you whether that process built a rich causal model..."
    *Rewrite:* "Minimizing prediction error is a computational job that can be achieved either by building a rich causal model or by exploiting a serviceable correlation."
  - *Draft:* "The honest position is empirical rather than sweeping."
    *Rewrite:* "The reality varies empirically across systems."
  - *Draft:* "Ptolemy's astronomers were not fools, and their model was not useless; it was an excellent instrument that told you where the planets would be and nothing true about why."
    *Rewrite:* "Ptolemy's astronomers built an excellent instrument that told you where the planets would be without revealing why they moved that way."

- **Punchy setup / announcement sentences:**
  - *Draft:* "Start with what each word is doing."
    *Rewrite:* Delete entirely. Begin the paragraph with "Prediction, in the sense that matters here..."
  - *Draft:* "The question is what to infer from it."
    *Rewrite:* Delete and integrate: "The question is what to infer from this fluency: one reading, associated with..."
  - *Draft:* "The same caution applies, pointing the other way, to the brain."
    *Rewrite:* "A similar caution applies to neuroscience, where predictive processing has recast perception as prediction."
  - *Draft:* "If prediction alone will not settle understanding, something else has to, and it is worth being concrete about what."
    *Rewrite:* Delete. Go straight to Judea Pearl: "Judea Pearl's account of causal inference separates three questions that prediction runs together..."
  - *Draft:* "Three kinds of evidence bear on the other two."
    *Rewrite:* "Generalization, causal intervention, and transfer test the other two."

- **Rhetorical fragments, abstractions, and antithesis trades:**
  - *Draft:* "But they come apart at the edges, and the edges are where the interesting questions live." (Rhetorical crescendo/abstraction).
    *Rewrite:* "But the two often diverge."
  - *Draft:* "Othello-GPT cuts against the flat 'just a parrot' claim, and it cuts against the opposite claim just as hard." (Parallel "trade" construction).
    *Rewrite:* "The Othello-GPT results show that you cannot tell from the forecasts alone whether prediction rests on a real model or on surface correlation."
  - *Draft:* "The behavior underdetermines the mechanism." (Fragment-like punchy statement).
    *Rewrite:* Integrate into the next sentence: "Because identical behavior can arise from different mechanisms, 'it predicts well, therefore it understands' fails as an inference."

## 2. Factual grounding
The factual claims are solid and well-supported by the evidence base. The historical description of the Ptolemaic system accurately reflects Kuhn's account. The treatment of LLMs, specifically Othello-GPT (Li et al., 2022) and Llama-2 (Gurnee & Tegmark, 2023), matches the literature. The draft is careful not to overclaim on behalf of predictive processing in the brain (Clark, Friston) or the limits of current AI. The reference to Judea Pearl's causal inference tools (intervention, counterfactuals) is accurate and effectively applied. Web searches confirm that Othello-GPT and the "stochastic parrots" references are correctly represented.

## 3. Structure & clarity
The structure is highly logical and clear. Opening with Ptolemy is a strong, concrete way to introduce the distinction between prediction and understanding. The draft seamlessly moves into the LLM debate and the Othello-GPT experiment before applying the same logic to the brain. Finally, it uses Pearl's criteria to offer concrete tests for understanding, making it highly accessible to a non-specialist. The only clarity issues stem from the style violations flagged above (e.g., philosophical shorthand like "The behavior underdetermines the mechanism" can trip up lay readers).

## 4. One self-contained argument
**Thesis:** Accurate prediction does not imply causal understanding; a system can forecast observations flawlessly while remaining ignorant of the underlying mechanisms.
The draft stays strictly on message. Every section—from the history of astronomy to LLMs, to predictive processing, to Judea Pearl's causal criteria—serves to untangle prediction from comprehension. There are no tangents or secondary theses.

## 5. Brief compliance & standalone
The post adheres perfectly to the brief. It covers the core distinction, Ptolemy, LLMs (Stochastic Parrots vs. World Models), the brain case, Pearl's criteria, and the stakes of over-relying on predictive performance. It correctly avoids the topics designated to other posts (the Turing test, anthropomorphism, empathy simulation). It is completely standalone, without any series framing, previous/next links, or calls to action.

## 6. Top 3 priorities
1. **Purge "Not X, it is Y" constructions:** Systematically replace negations and "rather than" phrasing with direct, positive statements of fact (especially regarding Ptolemy, the brain, and the internal process).
2. **Remove punchy setup/announcement sentences:** Delete short meta-sentences that announce what the paragraph will do (e.g., "Start with what each word is doing", "The question is what to infer from it") and instead just make the point.
3. **Smooth out rhetorical fragments and abstractions:** Revise the poetic abstractions ("the edges are where the interesting questions live") and parallel antitheses ("cuts against... and cuts against") into the measured, information-dense cadence required by the style guide.

**Rating:** `ship-with-minor-edits`
*Justification:* The draft delivers a cohesive, well-grounded argument that perfectly matches the brief, needing only targeted line edits to remove style-guide violations like announcement sentences and negation-based phrasing.
