---
layout: distill
title: "How does perception balance prior knowledge with new information?"
description: "External and internal modes of inference."
tags: [schizophrenia, psychosis, hallucinations, ketamine, HMM-GLM]
categories: [science]
giscus_comments: true
date: 2024-08-01
featured: true
toc:
  sidebar: left

authors:
  - name: Veith Weilnhammer
    url: "https://veithweilnhammer.github.io"
    affiliations:
      name: UC Berkeley, Helen Wills Neuroscience Institute

toc:
  - name: Overview
  - name: Key Findings
  - name: Synthesis
  - name: Methods
  - name: Implications
  - name: Future Directions

_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 14px;
  }
---

## Overview

Perception actively integrates new sensory information with internal predictions based on prior experiences. My research explores how the brain dynamically shifts between two perceptual modes: an **external mode** (focused on immediate sensory input) and an **internal mode** (guided by past experiences). These shifts are key to understanding psychotic disorders such as schizophrenia.

---

## Key Findings

### 1. Internal vs External Modes

Using large-scale behavioral data, we demonstrated systematic fluctuations in perception between an external mode (high accuracy, minimal reliance on previous experiences) and an internal mode (strongly biased by perceptual history)[^1]. These fluctuations optimize perception, balancing novelty detection and stability.

### 2. Predictive Templates & Hallucinations

False perceptions ("false alarms") arise from internal predictions ("predictive templates"), especially during internal mode[^2]. Computational modeling (HMM-GLM) revealed these templates fluctuate dynamically, linking them closely to mechanisms underlying hallucinations.

### 3. NMDAR Dysfunction & Psychosis

We showed pharmacologically-induced NMDAR hypofunction (using S-ketamine) prolongs external mode dominance, causing erratic perceptual inferences. This mirrors key aspects of perceptual disruptions seen in schizophrenia and offers a mechanistic explanation for episodic psychotic symptoms[^3].

---

## Synthesis

Dynamic interplay between external and internal perceptual modes significantly influences psychosis. Over-reliance on external sensory input can produce unstable perceptions, leading to maladaptive internal predictions. When perception shifts to internal mode, these maladaptive predictions dominate, triggering hallucinations and delusions.

---

## Methods

We combined multiple complementary methodologies:

- Behavioral experiments using ambiguous visual stimuli.
- Computational models (Hidden Markov and General Linear Models, GLM-HMM) to quantify perceptual mode dynamics.
- Pharmacological experiments with S-ketamine.
- Clinical studies comparing schizophrenia patients with controls.

---

## Implications

Clarifying these perceptual dynamics offers important implications for psychiatric care. Dynamic perceptual mode shifts might serve as biomarkers for psychosis, informing novel neuromodulatory treatments targeting NMDAR function and perceptual stability.

---

## Future Directions

- Developing real-time monitoring of perceptual mode shifts as predictive tools for psychosis.
- Exploring closed-loop neuromodulation techniques to stabilize perceptual inference.
- Extending our computational framework to related cognitive domains, such as memory and decision-making.

---

## Resources

### Talks and Slides:

- [External and Internal Modes in Perception](https://veithweilnhammer.github.io/assets/reveal/modes_Basel_2.html)

---


[^1]: Weilnhammer et al., PLOS Biology, 2023.
[^2]: Weilnhammer et al., Current Biology, 2024.
[^3]: Weilnhammer et al., Brain, 2024.