---
layout: distill
title: "In a World Full of Convincing Fakes, Trust Moves Back to People You Can Verify"
description: "As synthetic text, voice, and faces become indistinguishable from real ones, verified human provenance becomes scarce — and scarcity is what makes it valuable."
tags: [trust, ai, identity]
categories:
giscus_comments: false
date: 2026-07-08
featured: false

authors:
  - name: Veith Weilnhammer
    url: "https://veithweilnhammer.github.io"
    affiliations:
      name: UC Berkeley, Helen Wills Neuroscience Institute

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

In January 2024, a finance employee at the engineering firm Arup joined a video call with what looked like the company's chief financial officer and several colleagues. The faces and voices matched people the employee recognized, and the request fit a senior finance meeting: authorize a set of confidential transfers. Over a short period the employee sent about 200 million Hong Kong dollars, roughly 25 million US dollars, across fifteen separate payments. Every person on that call except the employee had been synthesized from publicly available footage. The case has been widely reported as one of the largest deepfake frauds on record, and the funds were not recovered.

What failed here was an ordinary identity check. The employee was skeptical of the initial email and asked for a video meeting precisely to confirm that a real person stood behind the request. After the call, the request looked like it came from real, familiar colleagues, and the payments followed. For most of human history, seeing a face and hearing a voice in real time was a reliable way to confirm that a specific person was present. That check now returns the wrong answer, cheaply and at scale.

Synthetic text, voice, and images have crossed the point where the apparent realism of something no longer confirms that a human made it. A convincing face can be generated, a familiar voice cloned from a short recording, and fluent prose produced at near-zero cost per word. Several independent studies point the same way. Sarah Kreps and colleagues found that readers could barely distinguish AI-written news stories from human-written ones. Sophie Nightingale and Hany Farid showed that observers could not reliably separate AI-synthesized faces from real photographs, and rated the synthetic faces as slightly more trustworthy on average. Kimberly Mai and colleagues played people genuine and synthetic speech in English and Mandarin, and listeners caught the deepfakes only 73 percent of the time, even after training on examples. These studies use different methods and test different technologies, and together they show that ordinary perception has become a weak certificate of origin.

Detection tools reduce some of this risk, but they do not make visual, audio, or textual realism a reliable origin check again. A detector can flag a likely synthetic text or a manipulated image under one set of assumptions, and the next model or a simple paraphrase shifts the statistical pattern it was trained to recognize. Work on AI-text detection has shown that paraphrasing sharply reduces detection rates, and that watermarking schemes create their own spoofing problems. The generator, the detector, and the person trying to evade the detector all adapt over time, so detection stays a partial defense.

This uncertainty now affects ordinary online judgments about replies, reviews, profiles, and images. The "dead internet theory," posted on a small forum in 2021 and picked up by The Atlantic the same year, holds that much of what people encounter on the web is machine-generated and that genuine human activity is a shrinking fraction of the whole. In its strong form — a coordinated takeover of the web by bots — it is a conspiracy theory. The weaker worry it names has become common, and there are measurements behind it. The security firm Imperva, together with Thales, estimated that automated traffic made up 49.6 percent of internet traffic in 2023, and its later report put automated traffic above half for the first time in 2024, a rise it ties to generative AI making bots cheap to build. These figures measure the traffic the company's own network can see, which is a narrower thing than the share of online content that is synthetic. They still give readers a concrete reason to ask whether a given reply, review, or profile image was produced by a person. Default trust in anonymous online content erodes when automated activity and synthetic media become common enough to change what people reasonably expect.

Cheap synthetic media make credible origin signals more valuable, because a trustworthy sign that a specific real person produced a specific thing stays hard to fake at scale. This is a version of the problem George Akerlof described in the market for used cars: when buyers cannot separate good goods from imitations, the market needs credible information mechanisms or it collapses toward the worst case. Online media now faces that structure directly. Platforms and readers have more reason to value an account, publisher, or person with a checkable history and a reputation that carries real costs. Verification therefore moves away from the artifact and toward its origin, and the question shifts from whether content looks legitimate to whether the entity behind it can show that it is human.

Two different guarantees are at stake here, and they solve different parts of the problem. Provenance — a record of where a piece of content came from and how it has been altered — is a claim about a particular artifact: that this recording, image, or message came from a known source and was changed only in recorded ways. The Coalition for Content Provenance and Authenticity, an industry group that maintains a standard called Content Credentials, often shortened to C2PA, is building an open system for attaching this record to media through cryptographic signing, a math-based seal that lets anyone check whether the attached information was changed after it was created. A file can then carry tamper-evident details about the device, software, publisher, and edits behind it. Proof of personhood is a different claim, about an actor rather than a file: that one distinct human stands behind an account, without necessarily revealing who. The property that matters is uniqueness, because many online attacks depend on one operator creating thousands of accounts, reviews, or votes, and tying one action to one person changes the economics of those attacks.

The Arup fraud turned on the second kind of guarantee, though not on it alone. The employee needed to know that real, authorized colleagues were on the call, which is a question about who was present rather than about whether a video file was authentic. Proof of personhood on its own would not have established that those people held their claimed roles, or that the transfer was legitimate; it establishes only that a distinct human is present. That is still the harder guarantee to rebuild, because it means tying a digital action to a person in the world without turning the link into a tracking device.

Some platforms are already turning verified personhood into a commercially valuable feature. In 2025 Match Group began piloting World ID on Tinder in Japan, so that users could earn a badge certifying they are a real, unique person over eighteen, a measure aimed at romance scams and AI-generated profiles; World also announced a partnership with Visa. Services that once handed out a checkmark for a confirmed phone number are now attaching verification to a scarcer credential, treating "this action came from a real, distinct person" as information worth paying for, precisely because it can no longer be assumed from the content.

The most visible attempt to supply that credential is Worldcoin, co-founded by OpenAI's Sam Altman and since rebranded to World. Its premise is that as AI makes human and machine text indistinguishable, online services will need hardware that certifies humanness directly. A device called the Orb scans a person's iris and issues a credential, World ID, that lets them later prove they are a unique human without re-scanning. By late 2025 more than twelve million people held an Orb-verified World ID, and the project talks openly about reaching a billion. The design tries to limit exposure: it is meant to store a cryptographic derivative of the iris rather than raw images, and to use zero-knowledge proofs — a method that lets one party prove a statement is true while revealing nothing beyond the fact that it is true — so that an app can confirm a valid, unique credential without receiving the user's identity.

The regulatory response shows how hard this is to do cleanly. Spain's data-protection authority ordered a temporary halt to iris collection in March 2024. Germany's Bavarian regulator ordered corrective measures and deletion of non-compliant data at the end of that year. Portugal ordered a ninety-day suspension, and in May 2025 a Kenyan court ruled the collection unlawful and ordered the data deleted. The recurring objection is about the collection and control of biometric data, rather than whether an iris scan can tell one person from another. Regulators point to insufficient information given to participants, data gathered from minors, and the inability to withdraw consent, and to the special sensitivity of a biometric that cannot be changed if it leaks, held under a private system and often gathered from people who were offered tokens to take part. A remedy for the fakery problem that depends on a global biometric uniqueness system creates a different problem of surveillance and control, and regulators are treating that second problem as serious in its own right.

Vitalik Buterin set out the underlying tension in 2023. Any biometric personhood system, he argued, carries risks that are structural rather than fixable by better engineering: biometric leaks are irreversible, mandatory personhood checks erode the ability to use the internet anonymously, authoritarian governments can coerce enrollment, and it is difficult to be secure and decentralized at the same time. A single Orb network that everyone passes through is convenient because it is a single point of control, and that point of control is what a government or a company can later lean on.

The design question is whether verifying humanness must rely on a central gatekeeper holding biometrics, or whether it can be done in a more distributed, privacy-respecting way. Some projects try the second route. Social-graph systems such as BrightID and Proof of Humanity establish that an account is a unique person through webs of vouching rather than a scanned body, and zero-knowledge methods let someone prove they hold a valid credential without revealing which one. A peer-to-peer authenticator, in which people verify each other directly instead of routing every check through one authority, is a further illustration that the centralized-biometric model is one design choice among several. None of these alternatives is finished, and each has its own failure modes: social graphs can exclude the isolated and be gamed by tight-knit groups, and distributed systems are harder to make robust against a determined attacker. No design yet is inclusive, secure, decentralized, and privacy-preserving all at once, so the real choice is among imperfect systems, and the differences between them fall mostly on where the sensitive data sits and who can be excluded or coerced.

Because no design solves all four goals, the choices made now, while the standards are still being set, will shape the infrastructure that follows. The demand for proof of personhood is real and will grow, because the loss of default trust is already priced into how people behave. The danger is that the first system to reach global scale becomes the default by inertia, and if that system is a single private holder of everyone's biometrics, the fakery problem will have been answered by building the surveillance infrastructure that critics have warned about for decades. Requiring an iris scan through one company's device to prove personhood trades a problem of too many convincing fakes for a problem of one entity that decides who counts as real.

Verified human origin is likely to keep gaining value as synthetic media and automated accounts get cheaper. The unresolved question is whether that verification concentrates the most sensitive data a person has in a central system, or whether decentralized, privacy-respecting methods can provide the same assurance without exposing biometric data that cannot be replaced after a breach. The Arup employee needed a way to confirm that a real, accountable person stood behind a request. Supplying that assurance at internet scale is worth doing, and the architecture it takes will determine whether it reduces impersonation or becomes a new tracking system.

## Further reading

- Heather Chen and Kathleen Magramo, "Finance worker pays out $25 million after video call with deepfake 'chief financial officer'," CNN, Feb 4 2024. https://www.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk
- Sarah Kreps, R. Miles McCain, and Miles Brundage, "All the News That's Fit to Fabricate: AI-Generated Text as a Tool of Media Misinformation," Journal of Experimental Political Science, 2020. https://doi.org/10.1017/XPS.2020.37
- Sophie J. Nightingale and Hany Farid, "AI-synthesized faces are indistinguishable from real faces and more trustworthy," PNAS, 2022. https://doi.org/10.1073/pnas.2120481119
- Kimberly T. Mai et al., "Warning: Humans cannot reliably detect speech deepfakes," PLoS ONE, 2023. https://doi.org/10.1371/journal.pone.0285333
- Vinu Sadasivan et al., "Can AI-Generated Text be Reliably Detected?," 2023. https://arxiv.org/abs/2303.11156
- Imperva/Thales, "2024 Bad Bot Report." https://www.imperva.com/company/press_releases/bots-make-up-half-of-all-internet-traffic-globally/
- Kaitlyn Tiffany, "Maybe You Missed It, but the Internet 'Died' Five Years Ago," The Atlantic, Aug 31 2021. https://www.theatlantic.com/technology/archive/2021/08/dead-internet-theory-wrong-but-feels-true/619937/
- George Akerlof, "The Market for 'Lemons'," Quarterly Journal of Economics, 1970. https://doi.org/10.2307/1879431
- C2PA / Content Credentials. https://c2pa.org/
- TechCrunch, "World partners with Tinder, Visa to bring its ID-verifying tech to more places," Apr 30 2025. https://techcrunch.com/2025/04/30/world-partners-with-tinder-visa-to-bring-its-id-verifying-tech-to-more-places/
- Vitalik Buterin, "What do I think about biometric proof of personhood?," Jul 24 2023. https://vitalik.eth.limo/general/2023/07/24/biometric.html
