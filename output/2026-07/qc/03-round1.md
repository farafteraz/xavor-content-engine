# Editor's memo — Post 3 (carousel)

**Overall verdict: FAIL.** Two mechanical hits: a banned "This is" unveiling on Slide 3, and a setup-and-negate structure on Slide 4. Everything else is close to clean and the evidence traces cleanly, so this is a light rewrite, not a rebuild.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Value" appears twice but as literal financial value, not filler. No dead openers, no engagement bait.

**S — Structures: FAIL.** Two hits:
- Slide 3: "This is no longer a finance edge case." — banned §6.6, a "This is" opener used as an unveiling. Lead with the subject.
- Slide 4: "Not because spend is high. Because nobody can tie it back to value." — banned §6.8 setup-and-negate (dismiss the obvious reason, pivot to the real one). Also flirts with §6.1 contrastive negation. Skip the setup; state the point directly.
- Borderline, not a fail: Slide 1's "Your AI bill is metered by the token. Your budget is still flat-rate." is a factual contrast of two real states, permitted under §6.1 (corrects a specific scope mismatch). It reads fine.
- Slide 5's "Design it in, or reverse-engineer it forever." is an either/or, not a banned reframe. Acceptable.

**M — Metaphor: PASS.** "The meter does not care about your annual plan" (Slide 2) is a light personification of a literal meter, not an analogy family from §7. It's exact and sounds normal aloud. Clears.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes. Slide word counts all under 25 (highest is Slide 5 at ~35 across two sentences — recount below). Actually Slide 5 runs 34 words. That exceeds 25.

Correction: **F — FAIL.** Slide 5 is 34 words ("Attribution cannot be reconstructed from an invoice. Tag by team, workload, and outcome at the point of consumption, or you are guessing after the fact. Design it in, or reverse-engineer it forever."). Cap is ~25. Slide 1 is ~34 words too ("Your AI bill is metered by the token. Your budget is still flat-rate. That mismatch is why the invoice arrives before anyone can explain what it bought."). Both need compression. Slides 2, 3, 4 are within range.

**E — Evidence: PASS.** Every claim traces:
- Slide 2 Uber four months → E25. Clean.
- Slide 3 31%→98% → E21. Clean.
- Slide 4 58% most desired skill → E23. Clean.
- No CONFLICT-marked figures used (E21 has no conflict). No invented specifics.

**O — One thing: PASS.** The post argues: metered AI pricing broke flat-rate budgeting, so attribution must be architected in at the point of consumption. One idea, matches the slot angle, ladders to the operability gap (the dollars face).

**L1 — Interchangeability: PASS.** The Uber budget-burn specific and the point-of-consumption tagging by team/workload/outcome are not swappable for a generic service. Anchored to metered token billing specifically.

**L2 — CTO respect: PASS.** Reads like a peer who has watched FinOps inherit a mess. No content-marketing wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" lands on Slide 5: attribution is a design-time decision, not a reporting problem — you either tag at consumption or you guess forever. A CTO who thinks of cost as a finance reporting layer gets the reframe that it's an architecture layer.

**R — Rhythm/human: PASS, with one note.** Sentences vary, sounds like speech, CTA lands. The one weakness: Slide 2's three short sentences edge toward a clipped beat. Fixing the word-count compressions should not make it more staccato.

## Edit notes

1. **Slide 3** — Remove the "This is" unveiling. Replace "This is no longer a finance edge case. FinOps teams owning AI spend jumped from 31% in 2024 to 98% in 2026. The bill is already on every desk." with a subject-led version, e.g.: "Two years ago 31% of FinOps teams managed AI spend. Now it's 98%. The bill already sits on every desk." (~20 words, subject leads, keeps E21.)

2. **Slide 4** — Kill the setup-and-negate. Replace "Not because spend is high. Because nobody can tie it back to value." Lead with the real reason directly, e.g.: "AI cost management is now the most wanted FinOps skill, named by 58% of businesses polled. The scarce skill is tying spend back to value." (~24 words, keeps E23, states the point without dismissing a strawman.)

3. **Slide 5** — Compress to ≤25 words. Suggested: "You cannot reconstruct attribution from an invoice. Tag by team, workload, and outcome at the point of consumption, or you guess after the fact." (~24 words. Drop "Design it in, or reverse-engineer it forever" or fold it into the caption if you want to keep it.)

4. **Slide 1** — Compress to ≤25 words. Suggested: "Your AI bill is metered by the token. Your budget is still flat-rate. The invoice arrives before anyone can explain what it bought." (~23 words.)

5. Recheck Slide 2 word count after edits (currently ~29 words: "Uber burned its entire 2026 AI coding budget in four months. It had budgeted a metered utility as a fixed line item. The meter does not care about your annual plan."). That's over 25 — trim to e.g.: "Uber burned its entire 2026 AI coding budget in four months. It had budgeted a metered utility as a flat line item." (~22 words; drop the "meter does not care" line or move it.)

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Slide 3: remove banned 'This is no longer a finance edge case' unveiling (§6.6); lead with subject, e.g. 'Two years ago 31% of FinOps teams managed AI spend. Now it's 98%. The bill already sits on every desk.' Slide 4: remove setup-and-negate 'Not because spend is high. Because nobody can tie it back to value' (§6.8); state directly, e.g. 'AI cost management is now the most wanted FinOps skill, named by 58% of businesses polled. The scarce skill is tying spend back to value.' Slide 5 exceeds 25-word cap (34 words); compress to ~24, e.g. 'You cannot reconstruct attribution from an invoice. Tag by team, workload, and outcome at the point of consumption, or you guess after the fact.' Slide 1 exceeds cap (~34 words); trim to ~23, e.g. 'Your AI bill is metered by the token. Your budget is still flat-rate. The invoice arrives before anyone can explain what it bought.' Slide 2 also runs ~29 words; trim to ~22, e.g. 'Uber burned its entire 2026 AI coding budget in four months. It had budgeted a metered utility as a flat line item.' Preserve all evidence (E21, E23, E25) and do not add staccato fragments while compressing."}
```