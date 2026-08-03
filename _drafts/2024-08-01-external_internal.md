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

Perception depends on a balance between **exploration** and **exploitation**. At some moments, the brain needs to stay open to new sensory evidence. At others, it needs to rely on prior knowledge to stabilize perception. Too much exploration makes perception noisy and unstable; too much exploitation makes it rigid and prone to circular inference.

Our research suggests that the brain manages this tradeoff by alternating between two functional modes: an **external mode**, in which perception is dominated by current sensory input, and an **internal mode**, in which perception is shaped more strongly by knowledge, memory, and perceptual history. We show that this balance is a basic feature of perception and that it can break down in psychotic states.

## Key Findings

### Dynamic explore-exploit fluctuations

Across large-scale behavioral datasets, perception fluctuated between an **external, exploratory mode** that tracked current input closely and an **internal, exploitative mode** that relied more strongly on perceptual history. These fluctuations appear to balance sensitivity to change with the need for stable perception under noisy and ambiguous conditions.

### NMDAR hypofunction shifts the balance

Pharmacological manipulation with **S-ketamine**, which blocks NMDA receptors, shifted the system into a prolonged external mode. This leaves perception more exposed to noise and ambiguity and may contribute to models of the world that drift away from reality. We observed a related mode imbalance in people living with schizophrenia, pointing to a causal link between NMDAR neurotransmission, mode switching, and psychotic symptoms.

### Internal predictions can drive false percepts

During the internal mode, the brain exploits **predictive templates** to guide perceptual decisions. When those templates are misaligned with reality, they can produce misperceptions or **false alarms**. GLM-HMM analyses indicate that these templates are amplified in individuals with psychosis-proneness.

## Methods

We used an integrated approach across:

- **Behavioral experiments** to induce competition between internal and external interpretations.
- **GLM-HMM** models to infer latent mode dynamics from behavior.
- **S-ketamine experiments** to simulate NMDA receptor hypofunction.
- **Clinical comparisons** between schizophrenia patients and healthy controls.

## Implications

Our findings suggest that the **explore-exploit balance** is a core computational principle of perception and a potential **biomarker** for psychiatric disorders such as schizophrenia. Stabilizing these dynamics could become a path toward therapies that restore cognitive flexibility and more adaptive inference in people living with delusions and hallucinations.

## Future Directions

- Real-time monitoring of explore-exploit dynamics as a diagnostic tool.
- Closed-loop interventions to support flexible perceptual inference.
- Extending the framework to memory, planning, and social cognition.

---

## Resources

- [Interactive Presentation: Internal and External Modes](https://veithweilnhammer.github.io/assets/reveal/modes_Basel_2.html)
- Weilnhammer, Veith, Yuki Murai, and David Whitney. “Dynamic Predictive Templates in Perception.” *Current Biology* 34, no. 18 (September 23, 2024): 4301–4306.e2. https://doi.org/10.1016/j.cub.2024.07.087
- Weilnhammer, Veith, Marcus Rothkirch, Deniz Yilmaz, Merve Fritsch, Lena Esther Ptasczynski, Katrin Reichenbach, Lukas Rödiger, Philip Corlett, and Philipp Sterzer. “N-Methyl-d-Aspartate Receptor Hypofunction Causes Recurrent and Transient Failures of Perceptual Inference.” *Brain*, January 16, 2025, awaf011. https://doi.org/10.1093/brain/awaf011
- Weilnhammer, Veith, Heiner Stuke, Kai Standvoss, and Philipp Sterzer. “Sensory Processing in Humans and Mice Fluctuates between External and Internal Modes.” *PLOS Biology* 21, no. 12 (August 12, 2023): e3002410. https://doi.org/10.1371/journal.pbio.3002410
