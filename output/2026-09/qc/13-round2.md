# Editor's memo — Post 13 (video feature, N4)

## Overall verdict: FAIL

Two problems. One mechanical evidence violation in Beat 2's framing (a banned contrastive-negation structure), and a hard structure hit that I have to call. The evidence itself is clean and well-scoped. But Beat 2 opens on "circling the wrong buy" as a reframe, and that pattern recurs. Let me walk it.

## Per-check

**V — Vocabulary: PASS.**
Scanned word by word. No banned terms. "signal" in Beat 4 is used literally (telemetry), not as figurative puffery. Clean.

**S — Structures: FAIL.**
Beat 1: "The robot works. That part is settled." followed by Beat 2: "The board conversation is circling the wrong buy. What matters is what carries the data off the floor." This is a cross-sentence contrastive reframe — the robot is the settled/easy thing, the real thing is the integration layer. The whole script is built on "not the robot, the layer around it." §6.1 explicitly extends across sentence boundaries and names exactly this shape: "Most teams think they have a hiring problem. They have a standards problem." The angle is legitimate; the execution states it as a not-X-but-Y pivot. Also flagged: the caption's "is the easy part now... What most board conversations skip is the integration layer" is the same reframe in prose.

Beat 4: "One robot generates data. Forty generate a fleet." — this is a triple-burst-adjacent parallel setup used for drama, and it borders on the rule-of-three cadence. On its own I'd let it pass; combined with the reframe spine it reinforces the pattern. Fixable in the same pass.

**M — Metaphor: PASS.**
"carries the data off the floor," "sits beside the arm," "wired to the real line" are all literal. No banned setups, families, or verbs. "one signal your engineers can read" is literal telemetry language. Clean.

**F — Formatting: PASS.**
No emojis, hashtags, exclamations, em dashes in body copy. Bold appears only in beat labels and structural markers (scaffolding, not body copy). 75-second script, within the 60–90s video spec. Fine.

**E — Evidence: PASS.**
Every number traces and is scoped honestly.
- "11 months... 30,000 vehicles, above 99% placement accuracy" → E28. Correct. (E28 says 30,000+ X3 vehicles; "30,000" is a fair floor.)
- "Forty generate a fleet" → E29 (40 Figure 03 units at BMW Spartanburg). Correct.
- E31 and E58 are used as directional framing with no figures quoted, and the evidence note says so. Good discipline. No CONFLICT figures stated as single numbers. No composite claims. This is the strongest part of the draft.

One small note, not a fail: Beat 1 pairs "Figure ran 11 months" (E28, Figure 02) with the implied same-site fleet of forty (E29, Figure 03 units). Both are real and both at Spartanburg, so no drift, but the script blurs the 02/11-month deployment with the 03/40-unit milestone. Keep them distinct in VO if possible.

**O — One thing: PASS.**
Argues one idea: the integration layer around the humanoid (edge compute, fleet pipelines, digital twin) is the real buy. Matches the slot angle and ladders to the operator's-gap big idea (capability sits deployed, the operating layer is the engineering work). Clean.

**L1 — Interchangeability: PASS.**
Swap "humanoid" for a generic robot and the specifics collapse — edge inference beside the arm, forty-unit fleet telemetry, digital-twin-to-line wiring are all particular to this deployment. Beat 3's "answers in milliseconds" and Beat 5's simulation-to-floor claim are not generic filler. Holds.

**L2 — CTO respect: PASS.**
A manufacturing CTO would respect this. "inference at the edge, not a round trip to a data center" and "the digital twin is only worth building when it's wired to the real line" are practitioner-true. Doesn't oversell Navi (it isn't mentioned — correct for this slot). No wince.

**L3 — Cognitive depth: PASS.**
The "I hadn't considered that" moment lands in Beat 5: "The digital twin is only worth building when it's wired to the real line." That reframes the twin from a showpiece into a connectivity dependency, which is the non-obvious take for a board circling the robot purchase. Beat 3's point that the accuracy number is an edge-compute claim, not a robot claim, also delivers depth.

**R — Rhythm/human: PASS, with one weakness.**
Reads like speech, varied lengths, real VO cadence. Beat 1's "The robot works. That part is settled." is two clipped fragments back to back — slightly staccato, and it's the same spot driving the S fail. The CTA grows naturally out of Beat 6. Overall human.

## Edit notes

The draft is one rewrite away from passing. The evidence, depth, and specificity are all there. The problem is purely structural: the script's spine is a not-the-robot-but-the-layer reframe, and it surfaces as a hard §6.1 hit in the caption and Beats 1–2.

Fix the reframe by stating the positive claim directly instead of negating the robot first:

1. **Caption.** Cut "is the easy part now" and "What most board conversations skip." Rewrite to lead with the integration layer as the claim: e.g. "Figure ran 11 months at BMW Spartanburg above 99% placement accuracy. The edge compute, fleet pipelines, and digital-twin connectivity behind that number are the engineering work. Here is where it lives." State what the layer is; don't frame it against the robot.

2. **Beat 1 VO.** Replace "The robot works. That part is settled." Do not open by settling/dismissing the robot — that sets up the reframe. Open on the fact directly: "Figure ran 11 months at BMW Spartanburg. 30,000 vehicles, above 99% placement accuracy." Let the accuracy number stand as the entry point.

3. **Beat 2 VO.** This is the core violation: "The board conversation is circling the wrong buy. What matters is what carries the data off the floor." Cut "circling the wrong buy" and "What matters is." Name the buy positively: "That accuracy number is an integration result. It comes from what carries the data off the floor and where the decisions run." Now Beat 3 (edge compute) and Beat 4 (pipelines) pay it off without a pivot.

4. **Beat 5** already states its insight positively ("only worth building when it's wired to the real line") — leave it. That's the model for the rest.

5. **Beat 4 optional tighten.** "One robot generates data. Forty generate a fleet." reads as a dramatic parallel. Soften to a single flowing line: "Forty units at Spartanburg generate a fleet's worth of data. We build the pipelines that pull every unit into one view your engineers can act on." Keeps the E29 specific, drops the burst cadence.

None of this touches the evidence or the angle. Once the reframe spine is replaced with direct positive claims, S clears and R's one weak spot resolves with it.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "The script's spine is a banned §6.1 contrastive reframe (not-the-robot-but-the-layer), surfacing across sentences in the caption and Beats 1-2. Fix by stating the positive claim directly. (1) Caption: cut 'is the easy part now' and 'What most board conversations skip'; lead with the integration layer as the claim, e.g. 'Figure ran 11 months at BMW Spartanburg above 99% placement accuracy. The edge compute, fleet pipelines, and digital-twin connectivity behind that number are the engineering work. Here is where it lives.' (2) Beat 1 VO: cut 'The robot works. That part is settled.'; open directly on the fact: 'Figure ran 11 months at BMW Spartanburg. 30,000 vehicles, above 99% placement accuracy.' (3) Beat 2 VO: cut 'The board conversation is circling the wrong buy' and 'What matters is'; name the buy positively, e.g. 'That accuracy number is an integration result. It comes from what carries the data off the floor and where the decisions run.' (4) Beat 4: soften the 'One robot generates data. Forty generate a fleet.' parallel burst to one flowing line keeping the E29 forty-unit specific. Beat 5 already states its insight positively; use it as the model. Do not touch the evidence or the angle."}
```