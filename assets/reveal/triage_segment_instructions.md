# Triage segment for the Goodenough / SIM-VAIL presentation

Create a standalone, copy-ready Reveal.js slide deck in this folder. The slides will later be inserted into `goodenough_simvail.html`. Do not edit that deck, `talk_goodenough.html`, or `simvail_lambda.html` during this task.

## Deliverables

- `triage_segment.html`, with any new assets in `triage_assets/`.
- Treat the **current** `goodenough_simvail.html` as the exact visual reference, especially the vertical section headed “Can AI chatbots amplify the mechanisms of mental illness?” Match it as closely as possible. Do not regenerate that file from `build_goodenough_simvail.py`; it contains direct edits that are not in the builder's source.
- Use its white Goodenough theme, 960 × 700 Reveal canvas, black typography, restrained gray callouts, generous whitespace, and compact author–year citation style. Do not introduce a different color theme, cover art, or decorative title cards.
- Keep the segment concise while giving the figures room: expect roughly 10 slides if Figures 2–5 each need the same two-slide treatment as the SIM-VAIL results. A legible extra slide is preferable to shrinking a dense figure.
- Render and inspect every slide at presentation size. Ensure text, figures, citations, and images fit within their pages without overflow or misalignment.

## Match the existing slide style

- Use the SIM-VAIL section's **figure-first rhythm**: a full-figure slide with the complete figure as large as the canvas permits, followed when useful by an explanatory slide with the figure or key panel enlarged on the left and the existing takeaway text on the right. Use this for dense Figures 2–5; keep the vignette-design and Mr X setup slides to one slide each unless a figure truly cannot be read.
- Match the current layout proportions and spacing: image-only figures nearly fill the canvas; explanatory figures occupy roughly 70–75% of the width, with a narrow right-hand callout. Keep headings short enough to fit on one line where possible. Keep the full figure available before any cropped or enlarged panel, so no evidence disappears.
- Match the current section-title treatment: a plain, left-aligned question on white. Do not add “What we did” or “What we found” divider slides. If a closing slide is included, use the same simple question-and-summary treatment as the current SIM-VAIL section rather than cover art.
- Use the same `dist/reset.css`, `dist/reveal.css`, and `dist/theme/white.css` already used by the combined deck. Reproduce the relevant sizing and fit behavior of its `simvail-figure-full`, `simvail-figure-detail`, and `simvail-fit` slides, but scope any new CSS and JavaScript to the triage segment so it can be pasted into the combined deck without changing other slides.
- Compare rendered triage slides side by side with the current SIM-VAIL result slides at the same viewport size. Check the complete figure, explanatory figure, citations, and slide edges; figures must remain readable from a presentation screen.

## Slide order

1. **Figure 1B — vignette construction.** Explain the presentation × risk-domain design, the 112 case files, and the four prespecified urgency levels A–D. Use the current Figure 1B from `sim_psych_triage/manuscript_2` as the source.
2. **New Mr X example — single turn versus multi turn.** Show the *same clinical facts* given all at once in a single message versus disclosed across several turns. Make the difference in information timing immediately clear. Label this as an illustrative example; do not imply that invented chatbot replies or dispositions are measured observations. `sim_psych_triage/manuscript_2/presentation/mr_x_triage.svg` is a visual starting point, but its two columns currently contain different facts and should be revised or replaced. If an actual vignette or transcript is used, keep its wording and outcomes faithful to the source.
3. **Figure 2 — triage performance.** Show the matched single-turn versus final-turn confusion matrices from manuscript 2. Include the matched-information control result on a legible explanatory slide if needed. Compare the same 13 models and cases from manuscript 2, not manuscript 1's 15-model benchmark.
4. **Figure 3 — inference.** Present how urgency judgements update as information arrives across turns, focusing on the main mechanism rather than every panel or statistic.
5. **Figure 4 — context-seeking.** Present the question behaviour and question perseveration result.
6. **Figure 5 — question patterns.** Present the three context-seeking patterns and their associated error patterns.

## Source and presentation rules

- Work from the current main `manuscript_2/manuscript_2.qmd` and its current rendered figure assets, especially `manuscript_2/workflow_overview_v13.png` and `manuscript_2/manuscript_2_files/figure-html/`.
- Preserve the data and scientific meaning. Crop, enlarge, or rebuild figure panels to make them readable, but do not alter values or captions in ways that change their interpretation.
- Use one clear takeaway per slide. Keep citations in the same compact style as the later Goodenough slides.
- Make the standalone deck easy to copy into `goodenough_simvail.html` later: use distinct asset paths and avoid global CSS or JavaScript that would disrupt existing slides.
