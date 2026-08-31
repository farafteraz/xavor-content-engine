# Editor's Memo — Post 12 (case-study carousel)

## Overall verdict: PASS

The draft is careful in exactly the places this slot is dangerous. It keeps the BMW Figure 02 machine and Navi distinct, flags the unverified Navi figure rather than shipping it, and argues one clean idea: accuracy comes from the robot, deployability comes from the operating layer Xavor builds. Clean read, human rhythm, no reframes.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "operable"/"operate"/"operating layer" are the month's territory, not banned. No "seamless," "robust," "leverage," "scalable." Clean.

**S — Structures: PASS.** Watched hard for the reframe, since the angle sits on a natural "not X, Y" ("the accuracy came from the robot… deployability comes from the layer"). This survives because it is a factual attribution split, not a rhetorical negation: it assigns two real things to two real sources rather than rejecting a strawman. No triple bursts, no rule-of-three closer, no "This is" unveiling, no cliffhanger pivot, no slogan tag. Slide 5's "The integration around it is still the work" is a plain claim, not puffery.

**M — Metaphor: PASS.** No analogies, no "think of it as," no metaphor verbs. "Fed and watched" on slide 3 is literal to a robot fleet (data path, observability), not a figurative flourish. Acceptable.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. The bold on slide labels ("Slide 1:") is structural scaffolding, not body copy. Word counts per slide: all well under 25 (longest, slide 2, is ~30 words — see note below). Actually slide 2 runs 31 words. Recheck: "Deploying a humanoid on a live line is an edge-compute and data-pipeline problem: local inference, fleet data paths, and connectivity that keep every unit observable while it works." = 30 words. This exceeds the 25-word cap.

Holding on that. Re-reading §9: "≤25 words per slide." Slide 2 is over. Slide 3 is ~40 words including the verify flag; excluding the bracketed flag it's ~34. Slide 4 is ~34. Several slides exceed 25.

Reversing my F call: **F — FAIL on slide word count.** Slides 2, 3, and 4 each exceed the 25-word cap.

**E — Evidence: PASS.** Every claim traces. Slide 1 / caption: E30 (90,000+ parts, above 99%, 1,250 hours, BMW) — accurate, and correctly not attributed to Navi. Slide 5: E33 ($1.1B, August, hardware above 20% of deal flow) — accurate. Navi 99% figure is flagged [verify], not shipped as fact — correct handling; E30's 99% belongs to Figure, not Navi, and the draft keeps them separate. No composite claims, no denominator drift.

**O — One thing: PASS.** The post argues: the operating layer, not the robot, decides whether a humanoid runs on your floor. One idea, ladders to the big idea (the operating gap) and matches the slot.

**L1 — Interchangeability: PASS.** The claims are specific to humanoids on a line (edge inference, fleet data paths, unit observability). Swap in a chatbot and slides 2–4 break. Grounded.

**L2 — CTO respect: PASS.** The honesty about attribution (accuracy is the robot's, deployability is the engineering) is exactly what a manufacturing VP respects. The [verify] discipline would not embarrass anyone.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" lands on slide 5 into 4: capital is chasing the hardware, but the deployability is the integration around it, and that's the unglamorous part nobody funds. For an ops leader watching robot demos, that reframing of where the risk actually sits is non-obvious.

**R — Rhythm: PASS.** Varied lengths, reads like speech, CTA grows out of the capital point. Not metronomic.

## Edit notes

Single mechanical failure: three slides exceed the 25-word cap (§9, §4). Fix by compression only, without chopping voice into fragments.

- **Slide 2** (30 words) → cut to ≤25. Suggested: "Deploying a humanoid on a live line is an edge-compute and data-pipeline problem: local inference, fleet data paths, and connectivity that keep every unit observable." (25 words.) Drop "while it works."
- **Slide 3** (~34 words excl. flag) → trim the body. Suggested: "Navi is Xavor's own robot, running at 99% task accuracy [verify: Navi 99% task-accuracy production figure]. We built the inference at the edge and the data path that keeps every unit fed and watched." Count the body without the bracket: ~30. Trim further: "We built the edge inference and the data path that keeps every unit fed and watched." Body now ~26; tighten "Navi is Xavor's own robot, running at 99% task accuracy" to fit under 25 excluding the flag.
- **Slide 4** (~34 words) → cut. Suggested: "That layer lets you run the machine, watch it in real time, and account for its work on a governed floor." (21 words.) Drop "next to the parts it places."

No other checks require changes. The verify flag on Navi's 99% figure must be confirmed by a human before publish; do not ship the Navi accuracy number as fact until the corpus supports it.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["Navi 99% task-accuracy production figure (slide 3) — confirm against corpus before publish; E30's 99% belongs to Figure 02 at BMW, not Navi"],
 "edit_notes": "Only F fails: slides 2, 3, and 4 exceed the 25-word cap (§9). Compress by cutting words, not by fragmenting the voice. Slide 2 (30 words): drop 'while it works' -> 'Deploying a humanoid on a live line is an edge-compute and data-pipeline problem: local inference, fleet data paths, and connectivity that keep every unit observable.' (25 words). Slide 3: trim body to under 25 words excluding the [verify] bracket -> e.g. 'Navi is Xavor's own robot, running at 99% task accuracy [verify: Navi 99% task-accuracy production figure]. We built the edge inference and the data path that keeps every unit fed and watched.' Slide 4 (34 words): drop 'next to the parts it places' -> 'That layer lets you run the machine, watch it in real time, and account for its work on a governed floor.' (21 words). Keep BMW Figure 02 and Navi visually and textually distinct; do not ship the Navi 99% figure as fact until the corpus confirms it. All other checks pass unchanged."}
```