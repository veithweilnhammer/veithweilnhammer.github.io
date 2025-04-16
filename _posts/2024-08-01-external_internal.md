---
layout: post
title: "Dynamic fluctuations between external and internal modes of perception: Neural mechanisms, predictive templates, and implications for psychosis"
date: 2024-08-01 09:00:00 -0400
description: "How does perception balance new infomration with prior knowledge?"
tags: [schizophrenia, psychosis, halluciantions, ketamine, HMM-GLM]
categories: [science]
giscus_comments: false
related_posts: false
featured: false
toc:
  sidebar: left
---

## Overview

Perception is not simply passive processing of sensory signals; rather, it involves actively integrating incoming sensory information with internal predictions shaped by prior experiences. Our work explores how perception dynamically alternates between two distinct states:

- **External mode**: Perception is strongly driven by immediate sensory input, enhancing the accurate processing of new information.
- **Internal mode**: Perception is biased toward previous experiences, reflecting internal predictive models rather than external reality.

These perceptual modes have important implications for understanding and treating psychosis, particularly schizophrenia, where perceptual inference frequently goes awry.

## Background

Predictive processing theories suggest that psychotic symptoms like hallucinations and delusions emerge from impaired integration of sensory information with internal expectations. OUr research investigates the neural and computational mechanisms underlying these failures of perceptual inference, particularly focusing on the role of **N-methyl-D-aspartate receptor (NMDAR)** hypofunction—a key neural abnormality in schizophrenia.

By combining human psychophysics, computational modeling, and pharmacological interventions, we've explored how transient, dynamic shifts between external and internal perceptual modes might explain the episodic and fluctuating nature of psychotic symptoms.

## Key Findings Across Studies

### 1. Perception alternates between external and internal modes (PLOS Biology)

- Using large-scale behavioral datasets from humans and mice, we found that perception systematically cycles between:
  - **External mode** (high accuracy, low serial dependence)
  - **Internal mode** (low accuracy, strong serial dependence)
- These mode fluctuations appear structured rather than random, suggesting a fundamental computational strategy to balance novelty detection (external mode) and stability through predictive modeling (internal mode).

### 2. Dynamic predictive templates drive perceptual false alarms (Current Biology)

- False alarms (perceiving signals when none exist) serve as a powerful model for understanding hallucinations.
- These false alarms are not random but driven by "predictive templates," internal predictions about sensory input shaped by recent experiences.
- Using Hidden Markov Models (HMMs), we revealed that these templates fluctuate dynamically, with false alarms becoming more frequent and strongly biased toward past experiences during internal modes.

### 3. NMDAR hypofunction causes recurrent perceptual inference failures (Brain)

- Pharmacological induction of NMDAR hypofunction using S-ketamine in healthy participants mimicked key perceptual disruptions observed in schizophrenia.
- Both S-ketamine administration and schizophrenia resulted in prolonged external mode, causing transient dissociations from internal predictive models.
- These recurring shifts toward external mode provide a mechanistic explanation for episodic psychotic experiences, suggesting that NMDAR dysfunction causes a shift in the natural oscillation between perceptual modes.

## Synthesis

The dynamic interplay between external and internal modes is crucial for understanding perceptual inference and psychosis. In the external mode, perception is overly reliant on immediate sensory signals, leading to erratic inferences when sensory information is ambiguous or noisy. Over time, this can result in the formation of maladaptive internal knowledge structures. Consequently, when the system switches into the internal mode, these maladaptive predictions dominate perception, potentially giving rise to psychotic experiences such as hallucinations and delusions. Understanding and potentially stabilizing these perceptual mode fluctuations thus represents a promising avenue for novel therapeutic interventions in schizophrenia and related psychotic disorders.

## Approach and Methodology

Across these studies, we used:

- **Behavioral psychophysics** with ambiguous sensory stimuli (structure-from-motion, signal-in-noise paradigms) to quantify perceptual mode shifts.
- **Computational modeling** using General Linear Models combined with Hidden Markov Models (GLM-HMMs) to capture dynamic fluctuations in perceptual inference.
- **Pharmacological interventions** (S-ketamine administration) and case-control clinical studies (schizophrenia patients vs. controls) to causally link perceptual dynamics to neural mechanisms.

## Relevance and Clinical Implications

Our work advances predictive processing accounts of psychosis by highlighting dynamic fluctuations between perceptual modes as a core computational mechanism underlying transient psychotic symptoms:

- **Neurocomputational models:** Clarifies how NMDAR hypofunction disrupt perceptual inference mechanisms.
- **Clinical translation:** Identifies potential biomarkers (dynamic mode fluctuations) for psychosis monitoring and suggests novel targets for therapeutic intervention, possibly through real-time neuromodulation to stabilize mode transitions.
- **Theoretical integration:** Strengthens the link between basic perceptual neuroscience and clinical psychiatry, providing a mechanistic framework for understanding why hallucinations and other psychotic symptoms are transient and episodic rather than constant.

## Future Directions

Several promising research avenues emerge from these findings:

- **Real-time mode tracking:** Developing methods to continuously monitor external-internal perceptual mode shifts as early indicators of psychotic episodes.
- **Closed-loop neuromodulation:** Investigating interventions (e.g., brain stimulation, pharmacological adjustments) that might stabilize perceptual inference, reducing symptom severity.
- **Broader cognitive domains:** Extending this computational approach to memory, decision-making, and other cognitive functions to understand their contributions to psychotic disorders comprehensively.

## Resources

### Papers and Presentations:
- 📄 [NMDAR hypofunction and perceptual inference](https://doi.org/10.1093/brain/awaf011) *(open access)*
- 📄 [Sensory processing in humans and mice](https://doi.org/10.1371/journal.pbio.3002410) *(open access)*
- 📄 [Dynamic predictive templates in perception](https://doi.org/10.1016/j.cub.2024.07.087) *(open access)*

### Talks and Slides:
- 🎞️ [Presentation: External and Internal Modes in Perception](https://veithweilnhammer.github.io/assets/reveal/modes_Basel_2.html)
---