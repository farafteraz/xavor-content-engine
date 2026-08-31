# Editor's memo — Post 11 (explainer reel)

## Overall verdict: FAIL

The draft is clean on mechanics and mostly sounds human, but it trips a banned structure (contrastive reframe) in two places, including the caption. That's a hard fail. Evidence, formatting, and depth are otherwise solid.

## Per-check

**V — Vocabulary: PASS.** No banned words. "Runtime" and "GA" are precision, kept correctly. No filler crucial/critical/leverage.

**S — Structures: FAIL.**
- Caption: "Most kill switches live in a policy document, not in production." This is contrastive negation (X, not Y). The slot angle itself is phrased as a reframe ("an operating capability, not a policy line"), and the caption inherits it. §6.1 allows contrast only to correct a specific fact/number/scope — this is a rhetorical A-not-B, so it fails.
- Frame 2: "the kill switch has only ever been a line in a governance policy, one no one has run against a live agent." Borderline, but this is the same policy-vs-production reframe restated. The larger problem is the repeated setup-and-negate rhythm across caption + Frame 2 + Frame 4/5 ("The new part:").
- Frame 5: "The new part:" is a cliffhanger pivot (§6.5 family — "The result?" / "Here's the thing"). Write the sentence: "Those kill switches now reach agents running outside ServiceNow..." Cut the label.

**M — Metaphor: PASS.** "Pull the plug" is a mild idiom but literal enough for a physical kill-switch context; it reads normally aloud and isn't in a banned family. No analogy setups.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Bold appears only in the scaffolding labels (**Angle:**, **Caption**), not in body copy — acceptable as structural markup. Longest frame (Frame 5, ~24 words) is under 25. Reel is 8 frames; spec §9 says 6–8, so it's at the ceiling but compliant.

**E — Evidence: PASS.**
- Frame 1 "35%" → [E20], exact. Good.
- Frames 4–5 GA August, AWS/Azure/GCP → [E7], exact.
- Frames 4/5/6 real-time detect/shutdown + cross-platform kill switch "for the first time" → [E9], exact, including the "outside its own platform for the first time" claim mapped correctly.
- No invented figures, no CONFLICT figure stated as single number, no merged claims.

**O — One thing: PASS.** Argues: the kill switch is now a runtime, cross-platform operating capability you can wire in and own. One idea, matches the slot angle, ladders to the operating-gap thesis (you can now operate a control you previously only wrote down).

**L1 — Interchangeability: PASS.** Named capability (Control Tower, cross-platform kill switch reaching outside ServiceNow) is specific; swap in another platform and the "reaches agents outside its own platform for the first time" claim breaks. Not generic.

**L2 — CTO respect: PASS.** Reads like a peer. Frame 3 (find it, trace it, pull the plug by hand under time pressure) is the operational reality a security lead recognizes. No content-marketing wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands in Frame 6: the control runs at runtime, stopping an agent mid-action — reframing the kill switch from a post-hoc policy to a live intervention. Frame 7 adds the ownership/escalation point that separates buying from operating.

**R — Rhythm/human: PASS.** Sentence lengths vary, Frame 3 breathes, CTA lands naturally. No metronome. One caution: the caption and Frame 2 restate the same policy-vs-production idea, which is slightly repetitive across an 8-frame budget.

## Edit notes

Fix the structures; everything else holds.

1. **Caption, sentence 1** — Replace the A-not-B. Rewrite "Most kill switches live in a policy document, not in production." with a direct statement plus the specific: "35% of executives admit they couldn't immediately shut down a rogue agent. The kill switch has lived in a governance policy, never run against a live one." Keep the rest of the caption as is. (If you keep any contrast, tie it to the [E20] number so it corrects a fact, not a vibe.)

2. **Frame 2** — De-duplicate with the caption and drop the reframe rhythm. Replace with a plain operational statement, e.g.: "In most enterprises no one has ever executed that shutdown against a running agent. It stayed a policy line." Avoid restating "policy document, not production" a third time.

3. **Frame 5** — Delete the "The new part:" label. Lead with the subject: "Those kill switches now reach agents running outside ServiceNow, across AWS, Azure, and GCP, for the first time." (Preserves the [E9] "for the first time" claim.)

4. Optional tightening: with caption and Frame 2 no longer both hammering policy-vs-production, consider whether Frame 2 earns its place or should carry a fresh beat (e.g., the manual-shutdown cost you already gesture at in Frame 3). Not required for PASS.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Fix banned structures only; evidence and depth hold. (1) Caption sentence 1 'Most kill switches live in a policy document, not in production.' is contrastive negation — rewrite as a direct claim anchored to the 35% figure, e.g. '35% of executives admit they couldn't immediately shut down a rogue agent. The kill switch has lived in a governance policy, never run against a live one.' (2) Frame 2 restates the same policy-vs-production reframe — replace with a plain operational statement and remove the duplication, e.g. 'In most enterprises no one has ever executed that shutdown against a running agent. It stayed a policy line.' (3) Frame 5 'The new part:' is a cliffhanger-pivot label — delete it and lead with the subject: 'Those kill switches now reach agents running outside ServiceNow, across AWS, Azure, and GCP, for the first time.' Keep the 'for the first time' claim (E9). Optional: with caption/Frame 2 de-duplicated, give Frame 2 a fresh beat (manual-shutdown cost) rather than a third policy-vs-production restatement."}
```