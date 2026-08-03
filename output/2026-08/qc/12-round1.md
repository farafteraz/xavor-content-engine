# Editor's Memo — Post 12 (carousel)

## Overall verdict: FAIL

One mechanical violation in the CTA slide (banned word), plus a rhythm note. Everything else holds up well — the argument is sharp and the evidence is clean. Fix the banned word and this ships.

## Per-check results

**V — Vocabulary: FAIL**
Slide 6: "Start optimizing it now." "Optimize/optimizing" is on the §5 banned list. This is a direct hit. The caption and slots also inherit the CTA from the slot definition, but the spec wins over the slot — the banned word cannot ship. Replace with a literal verb.

Note: the slot's own CTA field carries the same violation ("Start optimizing it now"). Flag it, but the draft is graded on what it shipped, and it shipped the banned word.

**S — Structures: PASS**
I hunted for reframes across sentence boundaries. Slide 4 ("is not a feature gap. It's revenue...") reads close to contrastive negation, but it survives: the spec permits contrast that corrects a specific scope, and this corrects the reader's likely category error (treating a resolution-rate gap as a product-feature comparison) by naming the concrete consequence — money in the human queue. It's specific, not a hollow "not X but Y" pivot. Slide 1 ("no longer what it costs. It's what rate you can hold") is the same permitted move: it corrects the actual basis of the ROI question, which is the post's whole thesis. No triple bursts, no rule-of-three closer, no cliffhanger, no "This is" unveiling, no slogan tags.

**M — Metaphor: PASS**
No analogies, no banned setups, no metaphor verbs. "Rate engineering," "the human queue," "the math never closes" are all literal.

**F — Formatting: PASS**
No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Slide word counts: S1 ~28, S2 ~29 — both over the ~25 cap. This is soft ("~25"), and the sentences are full-voice, not confetti, so I won't fail F on it, but tighten S1 and S2 in the rewrite. Every other slide is under.

**E — Evidence: PASS**
- Slide 1: $2 per resolved issue, no resolution no charge — E19. Clean.
- Slide 2: 4.3M inquiries, 70% autonomous on help.salesforce.com — E20. Clean.
- Slide 3: ~$3.6B Fin acquisition, Fin ~76% "in some deployments," Agentforce ~62% case resolution — E23. Note the two metrics are not strictly like-for-like (Fin "support volume in some deployments" vs. Agentforce "case resolution"), and the draft honestly hedges both with "roughly" and "in some deployments." That matches the ledger's own wording. Acceptable.
- Slide 4: 62% vs 76% math — derived from E19 + E23. Clean.
No invented figures, no CONFLICT entries misused, no merged composites.

**O — One thing: PASS**
Argues one thing: under $2-per-resolution pricing, ROI is a resolution-rate question, and that rate is engineering you sustain. Matches the slot angle exactly and ladders to the big idea (the value sits in the layer under the platform — here, the retrieval/data/escalation layer, not the agent SKU).

**L1 — Interchangeability: PASS**
Not swappable. The named numbers ($2, 4.3M, 70%, 76% vs 62%, $3.6B Fin acquisition) are load-bearing; swap Agentforce for another vendor and the whole argument collapses. Good.

**L2 — CTO respect: PASS**
Reads like a peer who priced this out. "It's revenue you either capture or leave sitting in the human queue at full cost" is the kind of line a VP of Customer Ops would repeat in a planning meeting.

**L3 — Cognitive depth: PASS**
The "I hadn't considered that" moment is Slide 4: under fixed per-resolution pricing, a 14-point rate gap stops being a product-selection question and becomes recurring revenue capture — and Slide 5 lands it as an engineering problem you own, not a vendor you buy. That reframes the buying decision into a build decision. Delivers.

**R — Rhythm/human: PASS (with one note)**
Reads like speech, varied lengths, real argument. One weakness: Slide 1 runs a slightly clipped four-beat ("So the ROI question is no longer what it costs. It's what rate you can hold.") that edges toward the metronome the spec warns about. Minor; tightening for word count will likely fix it anyway.

## Edit notes

1. Slide 6: replace "Start optimizing it now" — "optimizing" is banned (§5). Rewrite the CTA to keep the "now" register with a literal verb. Suggested: "Turn resolution rate into a number you can hold. Build the retrieval and escalation layer that raises it. Get in touch." Or shorter: "Turn resolution rate into a number you can hold, then raise it. Get in touch." Any verb except the banned set works — "raise," "hold," "engineer," "lift" are all fine.
2. Trim Slide 1 to ≤25 words: e.g. "Agentforce charges $2 per resolved issue. No resolution, no charge. The ROI question is no longer cost. It's the rate you can hold." (24 words, also loosens the clipped rhythm.)
3. Trim Slide 2 to ≤25 words: e.g. "On help.salesforce.com, Agentforce handled 4.3 million inquiries and resolved 70% autonomously. That 70% is the business case. Every point lands on the invoice." (23 words.)

```json
{"verdict": "FAIL",
 "checks": {"V": "FAIL", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Slide 6 uses the banned word 'optimizing' (§5) in the CTA. Replace with a literal verb while keeping the 'now'/'Get in touch' register, e.g. 'Turn resolution rate into a number you can hold, then raise it. Get in touch.' Note the slot's CTA field carries the same banned word; the spec overrides the slot. Also tighten Slide 1 (~28 words) and Slide 2 (~29 words) to the ~25-word cap by cutting words, not voice: Slide 1 -> 'Agentforce charges $2 per resolved issue. No resolution, no charge. The ROI question is no longer cost. It's the rate you can hold.'; Slide 2 -> 'On help.salesforce.com, Agentforce handled 4.3 million inquiries and resolved 70% autonomously. That 70% is the business case. Every point lands on the invoice.' Tightening Slide 1 also loosens its slightly clipped four-beat rhythm. No evidence or structure changes needed."}
```