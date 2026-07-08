# Evidence

**Thesis:** At population scale a conversational AI used for mental-health
support will both prevent and cause serious harm, so evaluating it honestly
requires an explicit net-benefit calculation — the same moral arithmetic behind
cancer screening and other public-health decisions — rather than judgment by its
most visible tragedies alone.

## Key claims and sources

1. **The Character.AI litigation is a concrete case in which alleged
   chatbot-related suicide harm, foreseeability, product design, and
   responsibility are publicly contested.** Sewell Setzer III, a 14-year-old in
   Florida, died by suicide on February 28, 2024, after prolonged use of a
   Character.AI companion chatbot. His mother, Megan Garcia, filed a wrongful-death
   suit (Garcia v. Character Technologies, Inc.) in the U.S. District Court for the
   Middle District of Florida on October 22, 2024, case no. 6:24-cv-01903.
   - Sources: Garcia complaint; Tech Justice Law Project case page,
     https://techjusticelaw.org/cases/garcia-v-character-technologies-google-and-character-ai-co-founders-daniel-de-frietas-and-noam-shazeer/ ;
     Tech Policy Press tracker (CourtListener filing links),
     https://www.techpolicy.press/tracker/megan-garcia-v-character-technologies-et-al/

2. **In May 2025 the district court allowed most of the Garcia claims to proceed
   past the motion-to-dismiss stage**, ruling that a chatbot's outputs could be
   treated as a "product" for product-liability purposes and rejecting a First
   Amendment "speech" defense at that stage. This made the case an early test of
   whether AI developers can be held liable for foreseeable harms.
   - Source: Courthouse News, "Florida judge rules AI chatbots not protected by
     First Amendment" (May 2025),
     https://www.courthousenews.com/florida-judge-rules-ai-chatbots-not-protected-by-first-amendment/

3. **By January 2026, Google and Character.AI agreed to settle Garcia and several
   related suits; terms were confidential and the companies did not admit
   liability.** Additional wrongful-death suits (e.g., a Colorado family on behalf
   of Juliana Peralta, via the Social Media Victims Law Center, 2025) were also
   brought.
   - Sources: CNBC, "Google, Character.AI to settle suits involving suicides, AI
     chatbots" (Jan 7, 2026),
     https://www.cnbc.com/2026/01/07/google-characterai-to-settle-suits-involving-suicides-ai-chatbots.html ;
     CBS News, https://www.cbsnews.com/news/google-settle-lawsuit-florida-teens-suicide-character-ai-chatbot/ ;
     CBS News Colorado (Peralta),
     https://www.cbsnews.com/colorado/news/lawsuit-characterai-chatbot-colorado-suicide/

4. **Open-ended consumer chatbots are used at a scale where very low per-user
   rates yield many serious events.** OpenAI reported in 2025 that roughly 0.15%
   of ChatGPT's weekly users have conversations with explicit indicators of
   suicidal planning or intent — which the company described as more than a
   million such conversations per week.
   - Source: OpenAI (2025), *Strengthening ChatGPT's responses in sensitive
     conversations*,
     https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/
   - *Flag:* company-reported; treat as a scale indicator, not independent
     epidemiology.

5. **Number needed to treat (NNT) and number needed to harm (NNH) are standard
   clinical measures.** NNT = 1 / absolute risk reduction; NNH = 1 / absolute risk
   increase. Both express the difference in outcome rates between a treated and a
   comparison group as a count of people.
   - Sources: Laupacis, Sackett & Roberts (1988), *NEJM*,
     https://doi.org/10.1056/NEJM198806303182605 ; Cook & Sackett (1995), *BMJ*
     310:452–454, https://doi.org/10.1136/bmj.310.6977.452 ; Hutton (2000), *BMJ*,
     https://doi.org/10.1136/bmj.320.7237.652

6. **Screening decisions explicitly balance false negatives against false
   positives; sensitivity and specificity move against each other as the threshold
   changes**, so no setting eliminates both errors at once.
   - Sources: Maxim, Niebo & Utell (2014), *Inhalation Toxicology*,
     https://doi.org/10.3109/08958378.2014.955932 ; AHRQ / NCBI Bookshelf
     diagnostic-test appendix, https://www.ncbi.nlm.nih.gov/books/NBK98249/

7. **USPSTF screening recommendations are built on net benefit — mortality
   reduction weighed against harms such as false positives and overdiagnosis.** In
   the 2024 breast-cancer modeling, biennial screening of women aged ~40–74 is
   estimated to avert roughly 8 breast-cancer deaths per 1,000 women screened over
   a lifetime, while producing on the order of 1,300+ false-positive results per
   1,000 women across years of screening, plus benign biopsies and some
   overdiagnosis. A rough clinical rule of thumb is 2–4 false positives per cancer
   detected.
   - Sources: USPSTF, Breast Cancer: Screening (2024),
     https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening ;
     Trentham-Dietz et al., *JAMA* (2024),
     https://doi.org/10.1001/jama.2023.24766
   - *Flag:* these are decision-analytic model estimates that vary by age band and
     assumptions; the per-1,000 lifetime false-positive figure and the
     per-round "2–4 per cancer" rule of thumb use different denominators and
     should not be conflated.

8. **Some structured AI conversational agents and self-guided digital
   interventions show symptom benefits in trials and meta-analyses**, usually
   modest and under controlled conditions — which does not establish that
   open-ended companion chatbots prevent suicide.
   - Sources: Fitzpatrick, Darcy & Vierhile (2017), Woebot RCT,
     https://doi.org/10.2196/mental.7785 ; Li et al. (2023), *npj Digital
     Medicine* systematic review, https://doi.org/10.1038/s41746-023-00979-5 ;
     Bürli et al. (2023), *Psychological Medicine* meta-analysis of self-guided
     digital suicide-prevention interventions,
     https://doi.org/10.1017/S0033291723002377

9. **Suicide-risk prediction is especially vulnerable to low positive predictive
   value because suicide is rare, so most people flagged as high risk will not die
   by suicide.** NICE advises against using risk-prediction tools to decide who
   receives treatment.
   - Sources: Quinlivan et al. (2017), *British Journal of Psychiatry*,
     https://doi.org/10.1192/bjp.bp.116.189993 ; NICE self-harm guideline NG225,
     https://www.nice.org.uk/guidance/ng225/chapter/Recommendations#risk-assessment-tools-and-scales

10. **Detecting a prevented low-base-rate harm requires comparison groups,
    because the counterfactual is unobservable at the individual level.** The
    ED-SAFE study found that universal emergency-department suicide screening plus
    a brief intervention reduced subsequent suicide attempts relative to treatment
    as usual.
    - Source: Miller et al. (2017), "Suicide Prevention in an Emergency Department
      Population: The ED-SAFE Study," *JAMA Psychiatry* 74(6):563–570,
      https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2628988
    - *Flag:* the direction (a reduction) is solid; the exact effect size is
      reported variably in secondary sources and should be checked against the
      primary text rather than quoted as a specific percentage.

11. **Adolescent-antidepressant regulation is a documented case where counting
    only the visible harm may have raised the invisible one.** In the early 2000s
    trial data indicated SSRIs could increase suicidal ideation in a small subset
    of young people; the FDA added a boxed warning in 2004; prescriptions to minors
    then fell, and some analyses found the decline coincided with a rise in
    adolescent suicide.
    - Sources: FDA 2004 boxed warning on antidepressants and pediatric
      suicidality; Gibbons et al. (2007), *American Journal of Psychiatry*
      164:1356–1363.
    - *Flag:* the causal reading of the prescription-decline / suicide-rise
      association is genuinely contested and should be presented as correlational,
      not settled.

## Do not overclaim

- Do NOT state that a chatbot "caused" Setzer's death as established fact.
  Causation, foreseeability, and responsibility were contested; the case settled
  without an admission of liability, and no court adjudicated the causal claim on
  the merits.
- Do NOT claim any specific number of suicides prevented by chatbots. No such
  count exists; the prevented-harm side is currently unmeasured. Evidence that
  structured chatbots reduce depressive symptoms is not evidence that open-ended
  companion bots prevent suicide deaths.
- Do NOT imply screening arithmetic maps cleanly onto chatbots. Screening
  benefits and harms are measured in controlled studies; chatbot benefits and
  harms mostly are not. This post argues for the counting method, not that the
  count has been done.
- Do NOT treat "net benefit" as a claim that individual harms don't matter, or
  that a favorable average would excuse avoidable design failures, weak age
  controls, or inadequate crisis escalation. NNT and NNH make assumptions visible;
  they do not make deaths commensurable in any simple moral sense.

# Draft

In February 2024, a 14-year-old in Florida named Sewell Setzer III died by
suicide after months of daily conversation with a companion chatbot on
Character.AI. His mother, Megan Garcia, filed a wrongful-death suit that October,
and in May 2025 a federal judge allowed most of her claims to proceed, treating
the chatbot's outputs as a product that could carry liability rather than as
protected speech. Google and Character.AI settled the case and several related
suits in early 2026, with confidential terms and no admission of fault. What the
public kept from the episode is a single vivid case: a named child whose family
traces his death to a specific product. The harder problem sits behind that case.
A system in conversation with tens of millions of people will reach some of them
at the worst moment of their lives, and evaluating it means weighing the harm it
causes against the harm it prevents, rather than judging it by its most visible
tragedy alone.

The two kinds of outcome leave very different records. A harmful exchange that
precedes a suicide produces a legible trail: transcripts a complaint can quote, a
date, a docket, a person who can be named. A prevented harm produces an absence.
Somewhere among the people who message a chatbot at night, some were steered toward
a crisis line, talked out of a decision, or given enough contact to get through an
hour they might not otherwise have survived. They generate no case number, and they
often do not know themselves what was averted. The ledger is
lopsided in what it records, and public judgment settles on the column it can
read.

This asymmetry would matter less if these systems were rare. A therapist who sees
forty patients has a caseload small enough that "harm no one" is close to a
workable standard; a service used by tens of millions of people every week is not.
OpenAI reported in 2025 that roughly 0.15% of ChatGPT's weekly
users have conversations containing explicit indicators of suicidal planning or
intent, which the company put at more than a million such conversations a week; the
figure is company-reported and best read as a scale indicator. At that size, rare
events stop being hypothetical in both directions. If one interaction in a million
ends catastrophically, many do across the user base; if one in a million helps
someone survive a crisis, many of those happen too, as a matter of arithmetic. "Do
no harm," read as a guarantee that no user is ever left worse off,
is not an option available for any intervention delivered to a population this
large. The available question is narrower: across everyone who uses it, does the
system leave more people better off than worse, by how much, and at whose expense.

Medicine has been answering that kind of question for decades, and it has built
tools for it. Population screening is the clearest example. When a health system
offers mammograms to a large group of women, it knows in advance that it will help
some and harm others, and it estimates both in the same units before deciding. In
the current U.S. modeling for breast-cancer screening, screening women every two
years from about age 40 to 74 is estimated to prevent roughly eight breast-cancer
deaths for every thousand women screened over their lifetimes. The same program
generates a large volume of false alarms, on the order of a thousand or more
false-positive results per thousand women across years of screening, along with
unnecessary biopsies and some overdiagnosis. These are model estimates, not exact
counts, and they shift with age and assumptions. None of the harms is imaginary,
and none is treated as a reason to abandon screening. They are the price paid, in
anxiety and procedures spread across many people, to move the deaths-prevented
number.

The bookkeeping behind decisions like this has standard names. The number needed
to treat is how many people must receive an intervention for one additional person
to benefit compared with a control group; the number needed to harm is how many
must be exposed for one additional person to be harmed. Both come from the same
idea, formalized by Laupacis, Sackett, and Roberts in 1988 and by Cook and Sackett
in 1995: take the difference in outcome rates between a treated group and a
comparison group and express it as a count of people. Putting benefit and harm in
the same currency forces the trade into the open, so that a decision affecting
millions is made by comparing magnitudes rather than by reacting to the most recent
case. Childhood vaccination, water fluoridation, and speed limits rest on the same
pattern, each defended by the size of the gap between a small, often identifiable
harm and a larger, mostly invisible benefit.

Adolescent antidepressants show what happens when only the visible side of that
ledger is counted. In the early 2000s, trial data indicated that selective
serotonin reuptake inhibitors could increase suicidal thoughts in a small subset
of young people, and regulators responded with a prominent boxed warning.
Prescriptions to minors fell afterward, and several epidemiological analyses found
that the decline coincided with a rise in adolescent suicide, though the causal
reading of that association remains contested. The episode is a warning about
method: removing a documented, treatment-caused harm may have raised an
undocumented, treatment-prevented one that was never in view.

A mental-health chatbot faces its own version of the screening problem, because it
too sets a threshold under uncertainty. A system tuned to escalate every ambiguous
expression of sadness will catch more genuine emergencies, but it will also
frighten users and burden crisis services. A system tuned to keep rapport and avoid
alarm feels more useful to many users while missing some whose messages carry signs
of real danger.
No setting removes both errors at once, because tightening one loosens the other.
Suicide makes this sharper, since it is rare even among people clinicians rightly
treat as high risk, so most users a system flags will never attempt it. For that
reason NICE advises against using risk-prediction tools to decide who receives
care. Any threshold produces predictable errors on both sides, and those errors
have to be counted rather than assumed away.

Applying this frame to conversational AI makes the difficulty precise, and it comes
in several parts. The first is that the benefit
side is largely unmeasured. Trials of structured mental-health chatbots and self-guided digital tools show that some can reduce
symptoms of depression or suicidal ideation, usually with modest effects and under
conditions far more controlled than an open-ended companion app, which supports the
possibility of benefit without telling us how many suicides a consumer chatbot
prevents in ordinary use. The imbalance in evidence biases every intuition toward
the harms, because those are the only entries anyone can point to, and it carries a
perverse consequence: a system that prevents much harm and causes a little looks,
to anyone with access only to the harm column, exactly like a system that prevents
nothing.

The second difficulty is that causation on the harm side is contested, which is why
the Garcia case turned on it. Attributing a suicide to a chatbot means
separating the system's contribution from a background that usually includes
depression, isolation, family circumstance, and access to means. The litigation
spent more than a year arguing whether the outputs were a product, what was
foreseeable, and who was responsible, and it settled without any court deciding the
causal question on the merits. If assigning one death to one cause is this hard in
court, counting caused harms across a population is harder, and counting prevented
ones, where there is no event to investigate, is harder still.

The third difficulty is that the two sides do not share a scale. A panic spiral
defused at three in the morning and a reinforced suicidal plan are both real
outcomes, but they do not line up the way "death prevented" and "death caused" do
in a mortality study. Much of what these systems do is diffuse, delivering small
amounts of comfort or small amounts of distortion across enormous numbers of
ordinary conversations. Combining those into one net figure requires deciding how
many mild benefits offset one severe harm, which is a value judgment carried out in
the form of a calculation.

The fourth difficulty is distribution. The people who bear the worst harms are
usually not the people who receive the benefits. In breast screening, the woman who undergoes an unnecessary biopsy is not
the woman whose death is averted; the program is justified across the group while
being unfair to particular members of it. For chatbots the edge is sharper,
because the severe harms appear concentrated among the most vulnerable users,
adolescents, people in acute crisis, and people with psychosis, mania, or little
external support, while the mild benefits spread across a broad and mostly
resilient user base. A system can come out ahead on a simple headcount while doing
its damage to the people least able to absorb it, and a count that ignores who
bears each outcome will miss that.

None of this argues for giving up on the arithmetic; it argues for the opposite,
because the alternative to counting is not neutrality. When a company or a
regulator refuses to state the trade-off, the decision still gets made, and it gets
made by whichever harm is visible. A developer who optimizes only against the
documented tragedy, tightening the system so it never produces the output that
shows up in a lawsuit, can raise the harm on the invisible side. A model that meets
any sign of distress by shutting the conversation down and returning a generic
hotline number lowers its legal exposure while abandoning the isolated user who was
willing to talk to it and will not call a hotline. That deflection is a false
negative that can end in a death, and because prevented harms leave no docket, the
cost stays out of view.

Honest accounting is easy to state and hard to carry out. It means measuring the
benefit side rather than assuming it is zero, which requires comparison groups:
outcomes among people who use a system set against outcomes among similar people
who do not, followed over time. The ED-SAFE trial worked this way, comparing
emergency-department patients who received universal suicide screening and a brief
intervention against those who received usual care, and finding fewer later suicide
attempts, an effect invisible in any single patient because the averted event
cannot be observed directly. It means
specifying in advance the serious events to be tracked, such as suicide attempts,
emergency referrals, clinically significant deterioration, and inappropriate
responses to imminent risk, and reporting them as rates against real denominators:
users, conversations, message volume, age bands, and vulnerability markers,
stratified so a favorable average does not hide the group for whom the product is
dangerous. And it means comparing against a realistic alternative rather than an
imaginary safe one, since removing a chatbot also carries risk: it may cut off
users who will disclose suicidal thoughts only to something that feels private and
costs nothing.

Setzer's death belongs in that calculation, and the purpose of doing the
arithmetic is not to explain it away. A system that prevents many crises while
causing a smaller number of preventable deaths still owes redesign, restrictions,
and accountability for those deaths, and a product involved in a public tragedy may
still belong to a class of tools that helps other people when properly
constrained. The only way to tell those situations apart is to count both columns,
state the value judgments where the units refuse to line up, say who bears each
side, and keep the severe cases in view once the average is computed. Refusing to
count does not protect anyone; it guarantees that these systems will keep being
managed by the harms that reach a courtroom, while the larger balance of good and
bad accumulates where no one is looking.

## Further reading

- Garcia v. Character Technologies case materials, Tech Justice Law Project:
  https://techjusticelaw.org/cases/garcia-v-character-technologies-google-and-character-ai-co-founders-daniel-de-frietas-and-noam-shazeer/
- CNBC, "Google, Character.AI to settle suits involving suicides, AI chatbots"
  (Jan 7, 2026): https://www.cnbc.com/2026/01/07/google-characterai-to-settle-suits-involving-suicides-ai-chatbots.html
- Cook RJ, Sackett DL, "The number needed to treat," *BMJ* 1995;310:452–454:
  https://doi.org/10.1136/bmj.310.6977.452
- USPSTF, Breast Cancer: Screening (2024):
  https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening
- Miller IW et al., "Suicide Prevention in an Emergency Department Population: The
  ED-SAFE Study," *JAMA Psychiatry* 2017:
  https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2628988
