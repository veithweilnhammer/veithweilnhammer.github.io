# Evidence

**One-sentence thesis:** A conversational AI used by millions will both prevent
and cause serious harm, so evaluating it honestly requires an explicit
net-benefit calculation — the same moral arithmetic behind cancer screening and
other public-health decisions — rather than judgment by its most visible
tragedies alone.

## Key claims and sources

1. **Sewell Setzer III, a 14-year-old in Florida, died by suicide on February 28,
   2024, after prolonged use of a Character.AI chatbot.** His mother, Megan
   Garcia, filed a wrongful-death suit (Garcia v. Character Technologies) in the
   U.S. District Court for the Middle District of Florida on October 22, 2024,
   case no. 6:24-cv-01903.
   - Source: Garcia v. Character Technologies complaint; Tech Justice Law Project
     case page. https://techjusticelaw.org/cases/garcia-v-character-technologies-google-and-character-ai-co-founders-daniel-de-frietas-and-noam-shazeer/

2. **On May 21, 2025, Judge Anne C. Conway allowed most of the Garcia claims to
   proceed, ruling that a chatbot's outputs could be treated as a "product" for
   product-liability purposes and rejecting a First Amendment "speech" defense at
   the motion-to-dismiss stage.** This made the case an early test of whether AI
   developers can be held liable for foreseeable harms.
   - Source: Courthouse News, "Florida judge rules AI chatbots not protected by
     First Amendment" (May 2025). https://www.courthousenews.com/florida-judge-rules-ai-chatbots-not-protected-by-first-amendment/

3. **By January 2026, Google and Character.AI agreed to settle the Garcia case and
   several related suits; terms were confidential and the companies did not admit
   liability.** Additional wrongful-death suits (e.g., a Colorado family on behalf
   of Juliana Peralta) were brought via the Social Media Victims Law Center in
   2025.
   - Sources: CNBC, "Google, Character.AI to settle suits involving suicides, AI
     chatbots" (Jan 7, 2026). https://www.cnbc.com/2026/01/07/google-characterai-to-settle-suits-involving-suicides-ai-chatbots.html ;
     CBS News Colorado on the Peralta suit. https://www.cbsnews.com/colorado/news/lawsuit-characterai-chatbot-colorado-suicide/

4. **Number needed to treat (NNT) and number needed to harm (NNH) are standard
   clinical measures.** NNT = 1 / absolute risk reduction; NNH = 1 / absolute
   risk increase. They were formalized by Cook and Sackett.
   - Source: Cook RJ, Sackett DL. "The number needed to treat: a clinically useful
     measure of treatment effect." BMJ 1995;310:452–454.
     https://doi.org/10.1136/bmj.310.6977.452

5. **Cancer screening is an accepted case of trading known harms against expected
   benefits at population scale.** In the USPSTF 2024 breast-cancer modeling,
   biennial screening of women aged 40–74 is estimated to avert roughly 8 breast
   cancer deaths per 1,000 women screened over a lifetime, while producing on the
   order of ~1,300+ false-positive results and additional benign biopsies per
   1,000 women. A common rule of thumb is 2–4 false positives per cancer detected.
   - Sources: USPSTF, Breast Cancer: Screening (2024).
     https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening ;
     Trentham-Dietz A et al., "Collaborative modeling to compare different breast
     cancer screening strategies," JAMA 2024. https://doi.org/10.1001/jama.2023.24766

6. **Prevented harms are hard to observe, especially for low-base-rate outcomes
   like suicide, because you cannot see the event that did not occur.** The
   ED-SAFE study found that universal ED suicide screening plus a brief
   intervention reduced subsequent suicide attempts relative to treatment as
   usual, but detecting such effects requires comparison groups precisely because
   the counterfactual is unobservable at the individual level.
   - Source: Miller IW et al., "Suicide Prevention in an Emergency Department
     Population: The ED-SAFE Study," JAMA Psychiatry 2017;74(6):563–570.
     https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2628988

## Exact quotes usable

- Cook & Sackett (1995), title phrase, public/citable: "The number needed to
  treat: a clinically useful measure of treatment effect." (Used only as a titled
  citation, not an internal quotation.)
- No modern copyrighted passages are quoted; all descriptions of complaints,
  rulings, and studies are paraphrased.

## Do not overclaim

- Do NOT state that the chatbot "caused" Setzer's death as established fact.
  Causation, foreseeability, and responsibility were contested; the case settled
  without an admission of liability, and no court adjudicated the causal claim on
  the merits.
- Do NOT claim any specific number of suicides prevented by chatbots. No such
  count exists; the prevented-harm side is currently unmeasured.
- Do NOT imply screening arithmetic maps cleanly onto chatbots. Screening
  benefits and harms are measured in controlled studies; chatbot harms and
  benefits mostly are not, and this post argues for the counting method, not that
  the count has been done.
- Do NOT present the USPSTF per-1,000 figures as exact observed counts; they are
  model-based estimates that vary by age band and assumptions.
- Do NOT treat "net benefit" as a claim that individual harms don't matter. The
  argument is about how to weigh, not about dismissing any death.

## Flags (could not fully verify / sources disagree)

- The exact ED-SAFE effect size is reported variably in secondary sources
  (e.g., "20% reduction"); the primary paper reports a relative reduction in the
  intervention phase, but I did not re-derive the precise percentage from the
  primary text here. Treat the direction (a reduction) as solid and the exact
  percentage as to-be-checked against the JAMA Psychiatry article.
- The USPSTF false-positive figure (~1,300+ per 1,000 over a screening lifetime)
  comes from decision-analytic modeling; the commonly cited "2–4 false positives
  per cancer detected" is a per-round/decade rule of thumb. These are different
  denominators and should not be conflated.
- Precise count and current status of all Character.AI-related suits shift over
  time; "several related suits settled in principle in January 2026" is
  well-supported, but the full roster and any non-settling cases may have changed
  after the sources above.
- The statin NNT example returned by search was explicitly hypothetical; I have
  therefore used cancer screening (with USPSTF figures) as the concrete
  arithmetic anchor and kept NNT/NNH as defined tools rather than citing a
  specific drug's NNT.

# Draft

In February 2024, a 14-year-old in Florida named Sewell Setzer III died by
suicide after months of daily conversations with a companion chatbot on
Character.AI. His mother filed a wrongful-death suit that October, and by the
following spring a federal judge had allowed most of her claims to proceed,
treating the chatbot's outputs as a product that could carry liability rather
than as protected speech. The company settled in early 2026 without admitting
fault. What the public retained from all of this is a single vivid case: a named
child whose family traces his death to a specific product. It is the kind of harm
that lodges in memory because you can name the person it happened to.

That is the difficulty at the center of any honest judgment about these systems.
A documented harm has a name and a court docket, and a prevented harm has
neither. Somewhere among the millions of people who talk to chatbots at
night, some fraction were talked down from a bad decision, or felt enough contact
to get through an hour they might not otherwise have survived, or were nudged
toward a crisis line. Those people do not generate a case number. They often do
not know themselves what was averted, and neither does anyone else. The result is
a lopsided ledger, where one column is filled with vivid particulars and the
other is effectively blank, and public judgment settles on the column it can
read.

The reason both columns of that ledger fill up is scale. A therapist who sees forty patients has a small
enough denominator that "avoid harming anyone" is close to a workable standard.
A system in conversation with tens of millions of people every week is in a
different situation entirely. At that size, rare events stop being hypothetical.
If even one interaction in a million goes catastrophically wrong, tens of such
interactions happen across the user base; if even one in a million helps someone
survive a crisis, tens of those happen too. Both outcomes occur as
a matter of arithmetic, not luck. "Do no harm," read as an absolute guarantee
that no user will ever be worse off, is not one of the options on the table for
any intervention delivered to a population this large. The available question is
narrower and harder: across everyone who uses it, does the system leave more
people better off than worse off, by how much, and at what distribution of cost.

Medicine has been forced to answer exactly this kind of question for a long time,
and it has built tools for it. The clearest example is screening. When a health
system offers mammograms to a large population of women, it knows in advance that
it will help some and harm others, and it estimates both in the same units before
deciding. In the current U.S. modeling for breast-cancer screening, screening
women biennially from around age 40 to 74 is estimated to prevent roughly eight
breast-cancer deaths for every thousand women screened over their lifetimes. The
same program also generates a large number of false alarms: on the order of a
thousand or more false-positive results per thousand women across years of
screening, along with unnecessary biopsies and a smaller number of cancers found
and treated that would never have caused harm. A rough clinical rule of thumb is
two to four false positives for every real cancer caught. None of these harms is
imaginary, and none is a reason to abandon screening; they are the price paid, in
anxiety and procedures spread across many people, to move the deaths-prevented
number.

The bookkeeping behind this has standard names. The number needed to treat is how
many people must receive an intervention for one to benefit who otherwise would
not; the number needed to harm is how many must receive it for one to be harmed
who otherwise would not. Both come from the same simple idea, formalized by Cook
and Sackett in 1995: take the difference in outcome rates between a treated group
and a comparison group, and express it as a count of people. The point of putting
benefit and harm into the same currency is to make the trade explicit, so that a
decision about millions of people is made by comparing magnitudes rather than by
reacting to whichever individual case is most recent or most vivid. The same
logic governs childhood vaccination, water fluoridation, and speed limits: each
accepts a small, sometimes identifiable harm to a few in exchange for a larger,
mostly invisible benefit to many, and each is defended by the size of the gap
between the two rather than by a promise that no one will ever be hurt.

Applying this frame to conversational AI does not make the answer easy. It makes
the difficulty precise, and the difficulty comes in four parts. The first is that
the benefit side is currently unmeasured. We have real cases like Setzer's on the
harm side and essentially nothing quantified on the prevented side, which means
the ledger is lopsided in evidence as well as in visibility. That
asymmetry biases every intuition toward the harms, because those are the only
entries anyone can point to. It also has a perverse consequence: a system that
prevents a great deal of harm and causes a little will look, to an observer with
access only to the harm column, exactly like a system that prevents nothing and
causes a little. Without the prevented side, you cannot tell a net benefit from a
net loss, and the temptation is to read every visible harm as evidence of the
latter.

The second difficulty is that causation on the harm side is genuinely contested,
which is why the Garcia case turned on it. Attributing a suicide to a chatbot
requires separating the machine's contribution from a background that usually
includes depression, isolation, family circumstance, and access to means. The
legal system spent a year arguing about whether the outputs were a product, what
was foreseeable, and who was responsible, and it settled without resolving the
causal question. If assigning a single death to a single cause is this hard in
court, counting caused harms across a population is harder still, and counting
prevented ones — where there is no event to investigate — is harder again.

The third difficulty is that the two sides are not obviously commensurable. A
prevented panic spiral at 3 a.m. and a reinforced suicidal plan are both real
outcomes, but they do not sit on a shared scale the way "death prevented" and
"death caused" do in a mortality study. Much of what these systems do is diffuse:
small amounts of comfort or small amounts of distortion, distributed across
enormous numbers of ordinary conversations. Aggregating those into a single
net figure requires deciding how many mild benefits offset one severe harm, and
that is a value judgment wearing the clothes of a calculation.

The fourth difficulty is distribution, and it is the one screening also struggles
with. The people who bear the worst harms are not the same people who receive the
benefits. In the breast-screening case, the woman who undergoes an unnecessary
biopsy is not the woman whose death is averted; the program is justified across
the group while being unfair to specific members of it. For chatbots the
distribution has a sharper edge, because the severe harms appear concentrated
among the most vulnerable users — adolescents, people in acute crisis, people
with weak external support — while the mild benefits are spread across a broad and
mostly resilient user base. A system can come out ahead on a simple headcount
while doing its damage to precisely the people who can least absorb it, and a
count that ignores who bears each outcome will miss that.

None of this argues for giving up on counting. It argues for the opposite,
because the alternative to explicit arithmetic is not neutrality. When a company
or a regulator refuses to state the trade-off, the decision still gets made, and
it gets made by whichever harm is visible. Optimizing only against the
documented tragedy — tightening a system so it never produces the output that
appears in a lawsuit — can raise the invisible harm on the other side, by making
the system evasive or abandoning users at the moment they most need a response,
and nobody will see the cost because prevented harms leave no docket.

What honest accounting demands is therefore modest to state and demanding to
carry out. It requires measuring the benefit side rather than assuming it is
zero, which means comparison groups: outcomes among people who use a system set
against outcomes among similar people who do not, tracked over time, the way
ED-SAFE had to compare screened and unscreened emergency-department patients to
show that screening plus follow-up reduced later suicide attempts. It requires
putting benefits and harms into shared units where possible, and being explicit
about the value judgments where they cannot share units. It requires attention to
distribution, so that a favorable average does not launder concentrated harm to
the vulnerable. Most of all it requires saying the trade-off out loud, and
abandoning the fantasy of a version that helps everyone and hurts no one.

Setzer's death should weigh heavily in that calculation, and the point of doing
the arithmetic is not to explain it away. The point is that a death we can see is
still only one entry, and a system deployed to millions is answerable for the
entries we cannot see as well — for the crises it defused and the ones it made
worse, most of which will never have a name. Refusing to count does not protect
anyone. It only guarantees that we will keep managing these systems by the harms
that reach a courtroom, while the larger balance, good and bad, accumulates in the
dark.

## Further reading

- Garcia v. Character Technologies case materials, Tech Justice Law Project:
  https://techjusticelaw.org/cases/garcia-v-character-technologies-google-and-character-ai-co-founders-daniel-de-frietas-and-noam-shazeer/
- CNBC, "Google, Character.AI to settle suits involving suicides, AI chatbots"
  (Jan 7, 2026): https://www.cnbc.com/2026/01/07/google-characterai-to-settle-suits-involving-suicides-ai-chatbots.html
- Cook RJ, Sackett DL, "The number needed to treat," BMJ 1995;310:452–454:
  https://doi.org/10.1136/bmj.310.6977.452
- USPSTF, Breast Cancer: Screening (2024):
  https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening
- Miller IW et al., "Suicide Prevention in an Emergency Department Population:
  The ED-SAFE Study," JAMA Psychiatry 2017:
  https://jamanetwork.com/journals/jamapsychiatry/fullarticle/2628988
