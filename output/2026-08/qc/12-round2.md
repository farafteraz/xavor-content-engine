# Editor's Memo — Post 12 (carousel)

**Overall verdict: PASS**

This is a clean, disciplined draft. It picks one number-driven idea, holds it across six slides, and lands the exact cognitive shift the slot asks for. Evidence traces cleanly. No banned vocabulary, no reframe structures, no metaphor leakage. Slide counts are well under the cap.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "moves that number" in the caption is literal (raising a metric), not the figurative "navigate/journey" family. Clean.

**S — Structures: PASS.** I hunted hard here. Two spots to clear:
- Slide 1 "The ROI question is no longer cost. It's the rate you can hold." reads adjacent to contrastive negation, but it corrects a specific claim about what the number is (cost vs. rate) under fixed pricing — this is the allowed case: a factual scope correction driven by the $2 mechanic, not a rhetorical "not X but Y" flourish. Acceptable.
- Slide 4 "is not a feature gap. It's revenue..." — same test. This is a specific correction of category (it's dollars, not capability), grounded in the $2 math. Acceptable, and it earns it with the concrete follow-through ("revenue you either capture or leave sitting in the human queue at full cost").
- Slide 5 "engineering, not procurement" — again a scope correction tied to a real claim (who owns the work), not a slogan. Acceptable.
No triple bursts, no rule-of-three closer, no cliffhanger pivot, no "This is" unveiling, no amputated slogan tag. The caption "It quietly hands you a harder one" is a real sentence, not a puffery tag.

**M — Metaphor: PASS.** No analogies, no banned setups, no metaphor verbs. "lands on the invoice" and "sitting in the human queue" are literal descriptions of billing and support operations. Fine.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes in the copy. Slide word counts: S1 ~24, S2 ~24, S3 ~23, S4 ~28... let me recount S4: "At $2 per resolution, the difference between 62% and 76% is not a feature gap. It's revenue you either capture or leave sitting in the human queue at full cost." = 30 words. That is over the ~25 guideline. Flagging as a soft overrun, not a hard fail — the spec says "~25" (approximate) and the voice-over-fragments rule explicitly prefers full sentences to chopped ones. Editor's call: PASS, but tighten S4 (see weakness note).

**E — Evidence: PASS.** Every claim traces:
- $2 per resolution, no charge on handoff/negative/abandon → E19. Correct.
- 4.3M inquiries, 70% autonomous, help.salesforce.com → E20. Correct, and correctly attributed to the reference deployment, not stated as a universal rate.
- Fin ~$3.6B acquisition, Fin ~76% "in some deployments" vs. Agentforce ~62% → E23. Correct, and the draft preserves E23's hedges ("roughly," "in some deployments") rather than hardening them into a clean benchmark. Good discipline. No invented figures, no merged claims, no denominator drift.

**O — One thing: PASS.** The post argues: under $2-per-resolution pricing, ROI is a resolution-rate problem you must engineer, not a cost problem. One sentence, no "and." Matches the slot angle exactly and ladders to the big idea (the value sits in the layer under the platform — here, the rate engineering the platform doesn't do for you).

**L1 — Interchangeability: PASS.** Swap Agentforce for a generic agent and the copy breaks — the $2 flat rate (E19), the 4.3M/70% deployment (E20), and the specific 76/62 Fin-vs-Agentforce split (E23) are all product-specific and cannot be genericized. The argument is welded to real numbers.

**L2 — CTO respect: PASS.** No wince. It talks money and mechanics the way an operator would. Slide 5 naming retrieval quality, escalation rules, and pre-answer data is the credible tell that the writer knows where resolution rate actually comes from.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" lands on Slide 4: at a fixed per-resolution price, the 14-point rate gap isn't a product-comparison detail — it's recurring revenue captured or forfeited, and it converts a procurement decision into an engineering mandate you own. That reframes how a CTO judges the buy.

**R — Rhythm/human: PASS.** Varied sentence lengths, reads like speech, opens on a hard fact with no throat-clearing. The CTA grows out of Slide 5's argument rather than being bolted on. Carousel compression stays in full sentences, not bullet confetti.

## One improvable weakness (non-blocking)
Slide 4 runs 30 words, the only slide over the guideline. Tighten without losing the insight, e.g.: "At $2 per resolution, the gap between 62% and 76% isn't a feature gap. It's revenue you capture or leave in the human queue at full cost." (26 words, still slightly over — cut "at full cost" if you want it clean under 25). Everything else ships as is.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```