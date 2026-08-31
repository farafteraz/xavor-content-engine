# Editor's Memo — Post 13 (carousel)

**Overall verdict: FAIL** (one hard structure violation on Slide 1).

The four-requirement spine is clean, well-mapped to [E44], and the evidence sits accurately on the right claims. But Slide 1 carries a contrastive-negation reframe that the spec bans outright, and it repeats in the caption and CTA. That's a mechanical FAIL on S. Everything else holds.

## Per-check

**V — Vocabulary: PASS.**
Scanned word by word. No banned terms. "cost with a story" is fine (not "narrative/journey"). "shutdown" is literal, not the banned "shut down a rogue agent" pattern. Clean.

**S — Structures: FAIL.**
- Slide 1: "That is exposure, not production." — contrastive negation (§6.1). The whole slide is also built as a setup-and-negate: "The ones that survive fail a second test... That is exposure, not production." Same pattern echoes the angle line but the angle is internal; the slide copy is the violation.
- Caption: "shipped without an owner or a payback number attached" then the pivot — borderline, but the sharper hit is the repeated "exposure, not production" logic driving the piece.
- Slide 5: "the agent is a cost with a story, not an investment." — second contrastive negation (§6.1). "X, not Y."
- CTA Slide 6 is clean.

Two clear "X, not Y" reframes. Either one is a FAIL on its own.

**M — Metaphor: PASS.**
No analogies, no banned setups or metaphor verbs. "exposure wearing a production label" appears only in the internal angle line, not in ship copy. "cost with a story" is idiom, not metaphor family. Clean.

**F — Formatting: PASS.**
Bold appears only in the scaffolding labels (Slide 1:, Caption), not in body copy that ships — treat as production markup. No emojis, hashtags, exclamations, caps, em dashes. Slide word counts all under 25 (Slide 4 is the longest at ~38 words — recount below).

Correction: Slide 4 runs long. "An escalation path. When the agent hits its boundary or goes wrong, who catches it and how fast. And a shutdown you have actually tested, because 35% of executives admit they couldn't stop a rogue agent today." That is ~44 words. **This fails the ≤25 cap.** Slide 5 is ~40 words. Slide 3 is ~35. Several slides breach.

Revising F to **FAIL** — multiple slides exceed 25 words.

**E — Evidence: PASS.**
- 88% pilots fail to production → [E16]. Correct.
- 5.1-month median payback → [E16]. Correct, same entry.
- 35% couldn't shut down a rogue agent → [E20]. Correct.
- Four-part standard (owner, boundary, escalation, metric) → [E44]. Correct and faithfully applied.
No invented figures, no merged composites, no denominator drift. Solid.

**O — One thing: PASS.**
Argues: an agent isn't production-ready until it has an owner, a boundary, an escalation path, and a payback in view. One idea, four facets of the same standard. Ladders to the operating gap. Matches the slot.

**L1 — Interchangeability: PASS.**
Swap "agent" for "model" and Slides 2–5 lose their teeth — decision boundary and rogue-agent shutdown are agent-specific. Holds.

**L2 — CTO respect: PASS.**
"a cost with a story" and the tested-shutdown point land as peer talk. A CTO would respect the payback-date demand.

**L3 — Cognitive depth: PASS.**
The moment: "shipped with no owner... That is exposure, not production" — reframing surviving pilots as the real risk. The insight survives even after we fix the phrasing: a passed pilot with no owner is the exposure, not the failed one. That's the "hadn't considered that" beat.

**R — Rhythm: PASS.**
Varied, speech-like, CTA grows naturally. No metronome. Good.

## Edit notes

Two mechanical fixes, both required.

1. **Kill the contrastive negations (S).**
   - Slide 1: replace "That is exposure, not production." Rewrite the slide to state the positive claim directly. Example: "88% of agent pilots die before production. The survivors get shipped with no owner, no boundary, no number. A production label on that is exposure." (States the claim without the "X, not Y" pivot; keeps the depth.)
   - Slide 5: replace "the agent is a cost with a story, not an investment." with a direct statement: "If you can't name the metric and the date it clears, you're funding a cost you can't defend in budget season." Removes the reframe, keeps the CTO edge.

2. **Cut every slide to ≤25 words (F).** At least Slides 3, 4, and 5 breach. Compress by removing words, not by chopping into fragments.
   - Slide 4 (~44 → ≤25): "An escalation path. When the agent hits its boundary or fails, who catches it and how fast. Plus a shutdown you have tested. 35% of executives admit they couldn't stop a rogue agent today." Still long — cut further: "An escalation path. When the agent hits its boundary, who catches it and how fast. And a shutdown you have actually tested. 35% of executives can't stop a rogue agent today." (~30, keep trimming to 25: drop "actually," tighten the last clause.)
   - Slide 5 (~40 → ≤25): "A payback number. Median agent payback runs 5.1 months. Name the metric and the date it clears, or you can't defend the spend." (~24)
   - Slide 3 (~35 → ≤25): "A decision boundary. The exact actions the agent may take alone, and where it must stop and hand off. Written down before launch." (~24)
   - Recount every slide after editing.

No evidence or argument changes needed. Fix the two reframes and the word counts, and this ships.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "S: Remove two contrastive-negation reframes (§6.1). Slide 1 'That is exposure, not production.' → state positively, e.g. 'The survivors get shipped with no owner, no boundary, no number. A production label on that is exposure.' Slide 5 'a cost with a story, not an investment' → 'Name the metric and the date it clears, or you can't defend the spend.' F: Multiple slides exceed the 25-word carousel cap. Slide 4 (~44 words), Slide 5 (~40), Slide 3 (~35) must all be cut to <=25 by removing words, not fragmenting the voice. Suggested trims: Slide 3 'A decision boundary. The exact actions the agent may take alone, and where it must stop and hand off. Written down before launch.' (~24); Slide 4 'An escalation path. When the agent hits its boundary, who catches it and how fast. And a shutdown you have tested. 35% of executives can't stop a rogue agent today.' (trim to 25); Slide 5 'A payback number. Median agent payback runs 5.1 months. Name the metric and the date it clears, or you can't defend the spend.' (~24). Recount every slide after editing. Evidence and argument unchanged; [E16][E20][E44] all correctly applied."}
```