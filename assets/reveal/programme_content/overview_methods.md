# Research programme overview

Four states in `new_project.html`: overview → Mechanisms → Measurement → Applications.

The overview now uses brief explanations and existing patient/MANIFEST artwork. Visible headings are Mechanisms, Measurement and Applications, without WP numbering. The later research stacks are unchanged.

## Animation

Only the title, work-package headings and fixed-height separators retain matching auto-animate identifiers. Text-bearing row containers no longer scale when a row expands. Headings keep consistent geometry and new content fades in. Browser checks sampled all three forward and three backward transitions: no animated text target had a non-unit scale.

## WP1 — Mechanisms

The original patient-with-flowchart illustration provides a perceptual-inference example. The text names all five domains. The summary uses paragraphs, with no bullets.

- Use Bayesian models and disentangled RNNs to understand predictive world models across these five domains.
- Test reliability and link individual differences to psychiatric symptoms.
- fMRI and MEG.
- Neuronavigated TMS.

Disentangled RNNs are included at the author's request. Attention remains specific to this overview; subsequent research stacks retain their existing four-domain design.

## WP2 — Measurement

- Measure cognition from language and everyday digital behaviour.
- Read language with linear probes and LLM autograders.
- Learn patterns in cursor, typing and touch behaviour with transformers.
- Check predictions against independent assessments, across people and over time.

The original psychological/digital map explains decoding and simulation. The pilot WildChat trajectories from “Follow psychological readouts through conversations” appear below it. The visible explanation covers decoding with linear probes and LLM autograders, simulating with profile-conditioned or steered transformers, and testing both against independent assessments and held-out behaviour. Regularised regression is removed from the overview. Technical details remain in the subsequent research material and the source proposal.

## WP3 — Applications

- Test psychological measurements in clinical and community cohorts.
- Use the original four-condition experimental diagram: history only, decoded, measured and population-average profiles.
- Test whether psychological profiles improve helpfulness, understanding and mood.

Participant counts are omitted from the overview diagram. Profile information varies while response instructions remain fixed, as explained in the notes. These are proposed human experiments, not demonstrated benefits in patients.

## Citations

- WP1: [PLOS Computational Biology 2017](https://doi.org/10.1371/journal.pcbi.1005536), [Current Biology 2024](https://doi.org/10.1016/j.cub.2024.07.087), [Brain 2025](https://doi.org/10.1093/brain/awaf011).
- WP2: [MAILA, arXiv 2025](https://arxiv.org/abs/2511.20179).
- WP3: [SIM-VAIL, Nature Medicine 2026](https://doi.org/10.1038/s41591-026-04577-2), personalised action policies, arXiv 2026 (status retained as instructed by the author).

## Reused artwork

- `cursor_mind/patient_bayes.png`: the original patient image with overlaid flowchart.
- `erc_human_ai_trajectories.svg`: original pilot conversation trajectories reused from the later research slide.
- `overview_mapping.svg`: the existing `erc_mapping.svg`, with the partial source-credit line excluded and the viewport adjusted to preserve axis labels.
- `overview_human_ai.svg`: the existing `erc_human_ai_design.svg`, with participant numbers and their heading omitted.

Original sources and the assets used by later slides are unchanged. Rendered at 960 × 700 with no missing assets or content overflow.


### Outcome, terminology and references
- Added `munich-programme-outcome` after the three animated expansions, using `programme_outcome.svg`: the original right-hand diagrams from B1 Figure 1, with challenge/opportunity/vision headings and MANIFEST prose omitted. The lower panel is moved up to close the gap. Original source SVG is unchanged.
- Use “psychological embeddings” throughout the overview explanations, compact summaries, notes and derived mapping/trial figure labels. Community and clinical cohorts test generalisation.
- Added Miller et al., NeurIPS 2023 (Cognitive Model Discovery via Disentangled RNNs), and Weilnhammer et al., Journal of Neuroscience 2013/2018 and Current Biology 2021 to the Mechanisms overview. Added the three neural-mechanism references to the detailed WP1 methods slide. DOI links and full titles are retained in citations/notes.
- Verified all overview states at 960 × 700, all six forward/back auto-animate transitions without text scaling, loaded figures, and forward/back navigation to the outcome slide. No browser JavaScript errors.
