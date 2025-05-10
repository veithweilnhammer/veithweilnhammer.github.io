---
layout: distill
title: "How Does the Brain Balance Exploration and Exploitation in Perception?"
description: "Perception and cognition alternate between external sampling and internal prediction."
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

Perception is not passive. It involves a continuous tradeoff between **exploration** — sampling new sensory information — and **exploitation**—relying on prior knowledge and expectations. Our research shows that the brain actively alternates between two functional modes: an **external mode**, where behavior is driven by sensory inputs, and an **internal mode**, where perceptual and cognitive processes are shaped by internal predictions and memory.

These fluctuations reflect a fundamental cognitive strategy: switching between information-seeking and belief-based inference. Crucially, we show that this dynamic balance can break down in psychotic states, offering a mechanistic explanation for hallucinations and delusions.

## Key Findings

### Dynamic Explore-Exploit Fluctuations

Analyzing behavioral data from large-scale experiments, we found that perception fluctuates rhythmically between an **external, exploratory mode** (high accuracy, driven by current input) and an **internal, exploitative mode** (strong reliance on perceptual history). These dynamics help balance sensitivity to novelty with the stability of interpretation.

### Internal Predictions and False Percepts

In internal mode, the brain relies on **predictive templates**, which can lead to misperceptions or **false alarms** — a hallmark of hallucinations. Computational modeling using GLM-HMM shows that these templates fluctuate spontaneously and are amplified in individuals with psychosis-proneness.

### NMDAR Hypofunction Disrupts the Balance

Pharmacological manipulation with **S-ketamine**, which blocks NMDA receptors, shifts the brain into a prolonged internal (exploitative) mode, disrupting adaptive switching. This mimics perceptual disturbances seen in schizophrenia and demonstrates a causal link between neurotransmission, cognitive mode dynamics, and psychotic symptoms.

## Methods

We used an integrated approach across multiple domains:

- **Behavior experiments** to induce competition between internal and external interpretations.
- **GLM-HMM** models to infer latent mode dynamics from behavior.
- **S-ketamine experiments** to simulate NMDA receptor hypofunction.
- **Clinical comparisons** between schizophrenia patients and healthy controls.

## Implications

Our findings suggest that the **explore-exploit balance in perception** is a core computational principle—and a potential **biomarker** for psychiatric disorders like schizophrenia. Stabilizing these dynamics could form the basis for targeted therapies aimed at restoring cognitive flexibility and perceptual accuracy.

## Future Directions

- Real-time monitoring of explore-exploit mode dynamics as a diagnostic tool.
- Closed-loop interventions to support flexible perceptual inference.
- Expanding the framework to domains like memory recall, belief formation, and social cognition.

---

## Resources

- [Interactive Demo: Internal and External Modes](https://veithweilnhammer.github.io/assets/reveal/modes_Basel_2.html)