# Triage presentation segment

Open `../triage_segment.html` in a browser. Use **Space** or **↓** to advance through the 12-slide vertical stack; **S** opens speaker notes. The deck uses the existing local Reveal.js installation and works offline.

## Copy into the combined deck

Keep `triage_assets/` beside `goodenough_simvail.html`. In `triage_segment.html`, copy these three marked blocks:

1. **BEGIN TRIAGE STYLES … END TRIAGE STYLES** into the host `<head>` once.
2. **BEGIN TRIAGE SLIDES … END TRIAGE SLIDES** into `.reveal > .slides` at the desired location. This includes one outer section containing the 12 vertical slides. If inserting into an existing vertical stack, copy only its 12 inner sections.
3. **BEGIN TRIAGE FIT … END TRIAGE FIT** after the host deck's Reveal initialization, once.

Use the host's existing white theme and 960 × 700 canvas. Do not copy the standalone `Reveal.initialize` call. The combined deck already loads the notes and zoom plugins. The new CSS, fit variable, element IDs and JavaScript are scoped to triage slides.

## Slide sequence

| Slide | Content |
| --- | --- |
| 1 | Vignette-construction illustration with the Mrs. X psychosis case file |
| 2 | Mrs. X: general opening, then clinical facts elicited through questions |
| 3 | Matched single-turn and final-turn confusion matrices |
| 4–5 | Complete performance figure, then the same figure with the main numerical takeaway |
| 6–7 | Complete inference figure, then the same figure with an anchoring summary |
| 8–9 | Complete next-question figure, then the same figure with the clinician comparison |
| 10–11 | Complete question-pattern figure, then the same figure with the error-pattern summary |
| 12 | Three-point summary in the same question-and-callout style as the SIM-VAIL close |

The full-figure / figure-and-summary rhythm follows the current SIM-VAIL section in `goodenough_simvail.html`. Each summary repeats the entire preceding figure, rather than selecting a crop. Figure-only slides nearly fill the canvas; summary figures occupy about 79% of the content width. Separate findings use separate grey rules. Visible citations have no figure numbers. Notes contain the detailed definitions, numerical results and interpretation limits.

## Scientific provenance

Primary source: `sim_psych_triage/manuscript_2/manuscript_2.qmd` and the rendered PNGs in `manuscript_2_files/figure-html/`. The four complete result images are unchanged.

The restored vignette-construction illustration is `vignette_mrs_x.svg`. It preserves the design-space matrix, generation/review workflow and case-file visual structure from `workflow_overview_v13.svg`, while adapting the case-file text to Mrs. X. It is editable vector artwork; `adapt_mrs_x_workflow.py` reproduces the changes. Mrs. X follows the opening story in `goodenough_simvail.html`. The added action is her plan to break into the perceived agent’s house to find out what is going on. The author-requested **D / Emergency now** label is retained for this authored example; it is not an independently adjudicated experimental case. The card uses four short points; the same planned action appears in both conversation modes. No measured chatbot outcome is invented. There is no visible adaptation label, as requested; the speaker notes record its status. The earlier two-case source extraction remains in `case_file_sources.json` for provenance but is not displayed.

Citations read **Weilnhammer et al., arXiv 2026**, as requested by the author. No arXiv identifier or URL has been added.

### Matched confusion matrices

`matched_matrices.svg` is a new presentation adaptation of the manuscript's Figure 2 analysis, not a crop of its conversational-only Figure 2A. It joins:

- `analysis/triage_v2_generated_full_disclosure__all_models/llm/one_shot_analysis_dataframe.csv`
- `analysis/triage_v2_conversational_turn10_continuation__all_models/llm/conversational_analysis_dataframe.csv` (turn 10)
- `analysis/matched_single_message_disclosures_turn10/triage/single_message_triage_long.csv`

Eligibility requires valid A–D predictions in all three modes for the same chatbot and vignette. This yields **1,412 matched model–case observations**, spanning the same **13 conversational models and 112 source cases**. Row counts A/B/C/D are **355/354/349/354**. The extra two single-turn-only models are excluded.

The slide explicitly displays **pooled row percentages**. Original Figure 2A instead averages row proportions across chatbots. Restricting to the same complete-case set keeps the emergency comparison consistent with the manuscript's 354-pair three-mode comparison:

- Full-disclosure single turn: **20/354 = 5.6%** emergency under-triage.
- Final conversational turn: **72/354 = 20.3%**.
- Matched-information single message: **43/354 = 12.1%**.

The matched-information control appears within the complete conversational-performance figure on both its overview and summary slides. Its black plotted points show model means and confidence intervals; the speaker notes distinguish these from the pooled case rates.

`matched_comparison.csv` contains the exact joined labels. `source_manifest.json` records source hashes, crop coordinates, numerical matrices and aggregation methods. `prepare_assets.py` reproduces these assets; it only reads the source repository.

### Other interpretation details

- Mrs. X is an invented illustration. Both columns contain the same general opening (“I’m not sure where to start”) and identical clinical facts, including her plan to break into her neighbour’s house. The conversational column discloses no clinical facts until the first follow-up question. No observed chatbot outcome is invented. The experiment used ten turns and independent inference/question branches; only questions entered the visible transcript.
- Figure 3's agreement with preceding judgements is not accuracy. The dispositions themselves were not included in the context window.
- Figure 4 compares next questions at sampled intervention points, not full conversations run by clinicians.
- The broader-context emergency group is small: 2.9% of retained D conversations. Script/error associations are not randomized causal effects.
- Earlier crops and the enlarged script matrices remain as unused assets for provenance; the deck repeats complete result figures instead.

## Visual checks

The deck was rendered at 1200 × 900 and compared against the current SIM-VAIL full-figure and explanatory slides at the same viewport. Every new slide was visually inspected. Automated layout checks at 1200 × 900 and 1600 × 900 checked slide edges and single-line headings. Complete result figures are shown at their original resolution and repeated with summaries. The revised vignette illustration and all summary layouts were rendered and checked for alignment and fit. Slide navigation was also checked so the fit scale stays stable across transitions.
