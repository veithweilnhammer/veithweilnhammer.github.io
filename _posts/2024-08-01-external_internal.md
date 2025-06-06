---
layout: distill
title: "Exploration and exploitation in perception"
description: "Perception alternates between external and internal modes."
tags: [explore-exploit, perception, cognition, hallucinations, ketamine, GLM-HMM]
categories:
giscus_comments: false
date: 2024-08-01
featured: false

authors:
  - name: Veith Weilnhammer
    url: "https://veithweilnhammer.github.io"
    affiliations:
      name: UC Berkeley, Helen Wills Neuroscience Institute

toc:
  - name: Overview
  - name: Key Findings
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

Perception involves a tradeoff between **exploration** — where the brain samples new information — and **exploitation** — where the brain relies on prior knowledge and expectations. Exploration makes perception sensitive to change but makes it vulnerable to ambiguity and noise. Knowledge about the world can help deal with ambiguity but increases the risk of circular inferences. Adaptive perception thus requires a balance between exploration and exploitation.

Our research shows that the brain solves this problem by alternating between two functional modes: an **external mode**, where perception is determined by sensory inputs, and an **internal mode**, where perception is shaped by knowledge and memory. These fluctuations reflect a fundamental cognitive strategy: switching between information-seeking (exploration) and belief-based inference (exploitation). We show that this dynamic balance can break down in psychotic states, offering a mechanistic explanation for hallucinations and delusions.

## Key Findings

### Dynamic Explore-Exploit Fluctuations

Analyzing behavioral data from large-scale experiments, we found that perception fluctuates between an **external, exploratory mode** (high accuracy, driven by current input) and an **internal, exploitative mode** (strong reliance on perceptual history). These dynamics help balance sensitivity to new information with the ability to have stable and robust perceptual experiences, even when sensory signals are ambiguous and noisy.

### NMDAR Hypofunction Disrupts the Balance

Pharmacological manipulation with **S-ketamine**, which blocks NMDA receptors, shifts the brain into a prolonged external (explorative) mode. This exposes perception to the destabilizing effects of noise and ambiguity and may cause people to build models of the world that don't align with reality. We replicated the effect of NMDAR antagonism on mode in people living with schizophrenia, a diagnosis often associated with NMDAR hypofunction. These results point to a causal link between NMDAR neurotransmission, mode switching, and psychotic symptoms.

### Internal Predictions and False Percepts

During the internal mode, the brain exploits **predictive templates** for perceptual decision-making. Predictive templates that don't align with reality can lead to misperceptions or **false alarms** — a hallmark of hallucinations. GLM-HMMs indicate that these templates are amplified in individuals with psychosis-proneness.

## Methods

We used an integrated approach across:

- **Behavior experiments** to induce competition between internal and external interpretations.
- **GLM-HMM** models to infer latent mode dynamics from behavior.
- **S-ketamine experiments** to simulate NMDA receptor hypofunction.
- **Clinical comparisons** between schizophrenia patients and healthy controls.

## Implications

Our findings suggest that the **explore-exploit balance** is a core computational principle of perception — and a potential **biomarker** for psychiatric disorders like schizophrenia. Stabilizing these dynamics could form the basis for targeted therapies aimed at restoring cognitive flexibility and adaptive perception in people living with delusions and hallucinations.

## Future Directions

- Real-time monitoring of explore-exploit mode dynamics as a diagnostic tool.
- Closed-loop interventions to support flexible perceptual inference.
- Expanding the framework to domains like memory recall, planning, and social cognition.

---

## Resources

- [Interactive Presentation: Internal and External Modes](https://veithweilnhammer.github.io/assets/reveal/modes_Basel_2.html)
- Weilnhammer, Veith, Yuki Murai, and David Whitney. “Dynamic Predictive Templates in Perception.” *Current Biology* 34, no. 18 (September 23, 2024): 4301–4306.e2. https://doi.org/10.1016/j.cub.2024.07.087
- Weilnhammer, Veith, Marcus Rothkirch, Deniz Yilmaz, Merve Fritsch, Lena Esther Ptasczynski, Katrin Reichenbach, Lukas Rödiger, Philip Corlett, and Philipp Sterzer. “N-Methyl-d-Aspartate Receptor Hypofunction Causes Recurrent and Transient Failures of Perceptual Inference.” *Brain*, January 16, 2025, awaf011. https://doi.org/10.1093/brain/awaf011
- Weilnhammer, Veith, Heiner Stuke, Kai Standvoss, and Philipp Sterzer. “Sensory Processing in Humans and Mice Fluctuates between External and Internal Modes.” *PLOS Biology* 21, no. 12 (August 12, 2023): e3002410. https://doi.org/10.1371/journal.pbio.3002410