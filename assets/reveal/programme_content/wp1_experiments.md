# WP1 experiments within the expanded overview

Updated following the layout correction: the standalone experiment slides are replaced by successive states of the expanded Mechanisms overview. Its left-hand explanation and the compact Measurement and Applications rows stay in place.

## Current sequence

1. Patient and flowchart (`munich-programme-wp1`), unchanged.
2. Person playing the research game, then Zhang’s cortical result: two fMRI states.
3. Weak/strong priors, then the perception-in-noise paradigm (`cursor_mind/currbio_001.png`, Weilnhammer, Murai & Whitney, Current Biology 2024), then the remaining original cumulative modes results.
4. Text-only TMS.
5. Four Measurement states with the original Decode / Simulate / Validate text fixed on the left. Only the right-hand pictures change: general mapping; conversation embedding trajectories; MAILA time of day; MAILA valence/arousal (time of day and valence/arousal).

The MAILA SVG headlines are removed from derived overview assets (`overview_maila_daily.svg`, `overview_maila_mood.svg`); original source assets remain unchanged.

All previous scientific notes and fMRI/TMS references remain, with obsolete references to the removed TMS illustration deleted. Original research stacks remain unchanged. The source assets are untouched.

Validated at 960 × 700: all figure paths load, forward/back navigation passes through every new state, no JavaScript errors, and sampled auto-animation shows no text stretching. The game, Zhang result, modes and text-only TMS states were visually inspected.

Changed in this revision: `new_project.html` and this report. No new assets.

## Original reference and asset record

The following implementation record predates the layout correction above; its source and reference information remains useful. Its standalone-slide arrangement and three-added-slide count no longer describe the current layout.

# WP1 experimental slides

Added exactly three slides inside `munich-mechanisms-bridge`, immediately after `munich-programme-wp1` and before `munich-programme-wp2`. All three use fade transitions and the label “WP1 – Mechanisms”.

## Final visible text

### munich-wp1-meg

- WP1 – Mechanisms · MEG — Cognitive modes
- How does the brain transition between cognitive modes?
- Behavioural modes
- Neural activity · mouse pilot
- Do neural-state transitions predict changes in cognition?
- MEG during cognitive tasks · Hidden Markov and state-space models
- Weilnhammer et al. · Current Biology 2024 · Brain 2025Neural figure: Weilnhammer · mouse pilot data (2025)

### munich-wp1-fmri

- WP1 – Mechanisms · fMRI — Naturalistic behaviour
- How does the brain represent information during naturalistic behaviour?
- Our proposed MRI-compatible research game
- Previous study · cortical navigation mapZhang, Meschke & Gallant
- Use encoding models to test neural representations.
- Proposed targets: beliefs, uncertainty, goals and prediction errors
- Huth et al. · Nature 2016 — meaning in natural languageZhang, Meschke & Gallant · Nature Neuroscience, in press (2026)

### munich-wp1-tms

- WP1 – Mechanisms · TMS — Causal mechanisms
- Can we causally change cognitive processing?
- Previous inferior-frontal-cortex study
- Identify candidate cortical regions.
- Apply neuronavigated TMS with control conditions.
- Model changes in cognition and behaviour.
- Test causal hypotheses from prior research and neural findings.
- Weilnhammer et al. · Current Biology 2021Journal of Neuroscience 2013 · 2018

## Scientific figures and assets

- `wp1_mode_transitions.svg`: standalone viewport of the original `cursor_mind/project_presentation_2.png`, retaining the plotted evidence and hiding only its small bibliography; original asset unchanged.
- MEG reuses `project_presentation/mouse_pilot_2.png` unchanged. The visible caption identifies mouse pilot evidence. This is not human MEG data. The existing figure does not specify acquisition modality; no modality was inferred.
- `wp1_research_game.svg`: the original research-game image, clip and transform extracted from `erc_approach.svg` (B1 Figure 2 overview); no global paradigm/overview image is used.
- `zhang_navigation_figure2.jpg`: original Figure 2 downloaded from the public preprint: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/d937/12724663/e3e63f8975de/nihpp-2025.12.16.694742v1-f0002.jpg .
- `zhang_navigation_cortex.svg`: standalone viewport of Figure 2B, including the original cortical maps and navigation-preference colour scale. Chosen instead of the paradigm figure following the user’s correction.
- TMS reuses `mechanisms_content/wp1_tms.svg`, the existing extraction of the cortical map and stimulation sites from the earlier inferior-frontal-cortex research. Original source: `Content/TMS_brain.svg` / `Content/Virtual_lesions.svg`.

## Verified references

- Huth et al. (2016), *Natural speech reveals the semantic maps that tile human cerebral cortex*, Nature 532, 453–458. https://doi.org/10.1038/nature17637 . Encoding-model precedent for meaning in natural language.
- Zhang, Meschke & Gallant, *A map of the cortical functional network mediating naturalistic navigation*. Nature Neuroscience, in press (2026), verified against https://gallantlab.org/publications/ on 30 October 2026. Author page also reports acceptance: https://www.tianjiao-zhang.com/publications/cortical-network-naturalistic-navigation/ . Public preprint and source figure: https://doi.org/10.64898/2025.12.16.694742 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12724663/ . No final journal DOI is asserted.
- Weilnhammer et al. (2021), *An active role of inferior frontal cortex in conscious experience*, Current Biology 31, 2868–2880.e8. https://doi.org/10.1016/j.cub.2021.04.043 . Prior TMS-induced virtual lesions, not structural lesions in patients.
- Weilnhammer et al. (2013), *Frontoparietal Cortex Mediates Perceptual Transitions in Bistable Perception*, Journal of Neuroscience. https://doi.org/10.1523/JNEUROSCI.1418-13.2013 .
- Weilnhammer et al. (2018), *The Neural Correlates of Hierarchical Predictions for Perceptual Decisions*, Journal of Neuroscience. https://doi.org/10.1523/JNEUROSCI.2901-17.2018 .
- Existing modes references retained: Weilnhammer, Murai & Whitney, Current Biology 2024, https://doi.org/10.1016/j.cub.2024.07.087 ; Weilnhammer et al., Brain 2025, https://doi.org/10.1093/brain/awaf011 .

## Scientific scope

Neural states and cognitive modes are a proposed correspondence. fMRI encoding models use shared feature extraction with participant-specific voxelwise fits, held-out gameplay evaluation and tests of cortical consistency; details are in speaker notes. Beliefs, uncertainty, goals and prediction errors are proposed targets, not claims attributed to Huth or Zhang. TMS targets and tasks follow mechanistic hypotheses; not all domains are promised.

## Validation

- 117 original leaf slides → 120 leaf slides: exactly three added. Every original leaf slide is identical to the pre-edit snapshot.
- All subsequent research stacks, beginning at `wp1-perceptual-mechanisms`, are byte-for-byte unchanged.
- Browser checked at 960 × 700. All image paths load; no JavaScript errors. All three slides rendered and visually inspected.
- Forward navigation: expanded Mechanisms → MEG → fMRI → TMS → Measurement. Reverse navigation passes the same sequence.
- Scoped CSS affects only the three new slides. No original scientific figure was modified.

## Changed files

- Modified: `new_project.html`.
- Added under `programme_content/`: `wp1_mode_transitions.svg`, `wp1_research_game.svg`, `zhang_navigation_figure2.jpg`, `zhang_navigation_cortex.svg`, `wp1_experiments.md`.

MAILA refinement: stacked the two right-hand plots, matched viewports and fonts, removed their SVG headlines and the dark zero-reference gridline from the daytime trajectory. Data paths, points and error bars remain unchanged.

Final MAILA layout: separate consecutive states `munich-programme-wp2-maila` (time of day) and `munich-programme-wp2-maila-mood` (valence/arousal), each in the full 415 × 400 right-hand image slot. Left-hand explanations remain identical. SVG headlines and the dark zero-reference gridline remain removed.
