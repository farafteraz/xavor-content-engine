# Editor's memo — Post 14 (case-study carousel)

## Overall verdict: FAIL

The draft is close and mostly clean. It fails on two mechanical checks: an evidence attribution problem on Slide 4 and a structure violation on Slide 2. Details below.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Governance surfaces," "control planes," "runtime observability," "kill switches" are all precision technical terms, allowed.

**S — Structures: FAIL.** Slide 2: "The control planes shipped. The operating work didn't." This is a contrastive negation / setup-and-negate across sentence boundaries — the exact cross-sentence reframe §6.1 names ("Most teams think they have a hiring problem. They have a standards problem."). It is not a factual correction of a number, date, or scope; it's a rhetorical pivot. FAIL.

Checked the rest: Slide 5 "The method is proven. We bring it to your stack." — two direct declaratives, no negation, allowed. Slide 3 "A governed agent inventory is the fix:" leads with the subject, not a "This is" unveiling. No triple bursts, no rule-of-three closer, no cliffhanger pivots.

**M — Metaphor: PASS.** No analogies, no banned setups, no metaphor verbs. "Wire that across all four vendors" is literal engineering language.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Body copy bold is confined to slide labels and the caption/angle scaffolding, which is structural markup, not body-copy emphasis. Slide word counts all under 25 (Slide 4 is the longest at ~24). Sentence case headings.

**E — Evidence: FAIL.** Slide 4: "real-time kill switches that reach outside its own platform (E7)." The cross-platform kill switch claim lives in **E9** ("kill switches applicable outside its own platform for the first time"), not E7. E7 covers GA timing and cross-cloud governance reach; E8 covers runtime observability (Traceloop). The draft cites E7 for a runtime-observability-plus-external-kill-switch claim that is actually spread across E7, E8, and E9. The specific "reach outside its own platform" fact is uncited under its correct entry. This is a merged/misattributed composite — FAIL even though every fact is individually real in the corpus.

Note: the slot's evidence list authorizes E7, E1, E46, E13. E9 and E8 are not in the slot's evidence array. The claim is true in the corpus but the slide reaches beyond the slot's authorized evidence to make it. Either pull the external-kill-switch and observability specifics (keep GA + cross-cloud governance under E7) or get E8/E9 added to the slot.

Slides 2, 5, and 1 check out: E13 correctly attached to its base population, E46 kept on ServiceNow's own deployment, E1 used only to name Databricks as one of the four.

**O — One thing: PASS.** The post argues: a governed agent inventory is a deliverable outcome Xavor ships into platforms you already run. One idea, ladders to the operating gap.

**L1 — Interchangeability: PASS.** Named platforms and the four-column inventory (agent, access, owner, kill switch) are specific. Swap ServiceNow out and Slide 4/5 break, which is what we want.

**L2 — CTO respect: PASS.** Reads like a peer. The "$500M measured through its own Control Tower" proof point is the kind of concrete a CTO respects.

**L3 — Cognitive depth: PASS.** The moment lands on Slide 1–2: owning a governance surface and operating it are different jobs, and the second is unstaffed. That reframes the buyer's assumption that the purchase closed the gap.

**R — Rhythm/human: PASS, with one weak spot.** Reads like compressed speech, varied lengths, CTA lands naturally. The one weak spot is Slide 2's clipped "The control planes shipped. The operating work didn't." — which is also the S failure. Fixing it fixes both.

## Edit notes

1. **Slide 2 (S fix):** Remove the two-beat reframe. Replace "The control planes shipped. The operating work didn't." with a direct positive statement that keeps the gap without the pivot. Suggested: "The control planes arrived this quarter. Operating them is a separate, unstaffed job." Or fold the point into one flowing sentence: "The control planes arrived this quarter, and operating them is work no one has been assigned." Keep the Credo AI stat and its base population intact.

2. **Slide 4 (E fix):** The "reach outside its own platform" and "runtime observability" facts are from E9 and E8, not E7. Two options: (a) Restrict the slide to what E7 supports — GA in August, governance extending across AWS, Azure, GCP — and drop the external-kill-switch and observability specifics, changing the citation to sit only on facts E7 actually carries. (b) If you want to keep the external kill switch (it's a strong, differentiated fact), flag it and request E8 and E9 be added to the slot's authorized evidence, then cite each fact to its correct entry: observability (E8), cross-platform kill switch (E9), GA (E7). Do not leave three entries collapsed under a single (E7).

Everything else holds. Fix these two and it ships.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Slide 2 (S): Remove the cross-sentence contrastive negation 'The control planes shipped. The operating work didn't.' Replace with a direct positive statement, e.g. 'The control planes arrived this quarter, and operating them is work no one has been assigned.' Keep the Credo AI stat and its 371-leader base population. Slide 4 (E): The 'reach outside its own platform' kill-switch fact is E9 and 'runtime observability' is E8, not E7 — the draft merges three ledger entries under one citation. Either (a) restrict the slide to E7-supported facts (August GA, governance across AWS/Azure/GCP) and cite E7 only for those, dropping the external-kill-switch and observability specifics; or (b) request E8 and E9 be added to the slot's authorized evidence array (currently E7/E1/E46/E13 only) and then cite each fact to its correct entry: GA (E7), runtime observability (E8), cross-platform kill switch (E9). Do not leave three entries collapsed under a single (E7)."}
```