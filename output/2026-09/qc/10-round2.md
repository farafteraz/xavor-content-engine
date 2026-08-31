# Editor's Memo — Post 10 (carousel)

**Overall verdict: FAIL** (one hard structural violation). Close otherwise; the fix is small.

## Per-check results

**V — Vocabulary: PASS.** No banned words. "right-sizing" is literal FinOps terminology, not "optimize." "Attribute" is used plainly.

**S — Structures: FAIL.** Two contrastive-negation hits (§6.1), and neither corrects a specific fact/number/scope, so the exemption doesn't apply.
- Caption: "The spend isn't the problem. The lack of an owner is." — cross-sentence "not X, but Y" reframe.
- Slide 3: "That's not a capacity problem. It's idle hardware nobody is right-sizing." — same pattern.
- Slide 2 closer, "When four people own it, nobody operates it," is a clean epigram, allowed. But note Slide 5 also flirts with reframe territory: "None of that is a new purchase. It's operating work..." — this one corrects a scope claim (purchase vs. operating work), which is arguably the permitted exemption, but stacked with the other two it reads as a tic. Fix the first two and reconsider this one.

**M — Metaphor: PASS.** No analogies, no banned setups, no metaphor verbs. "where the money hides" is idiom, not a metaphor family. Clean.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Slide word counts all under 25 (longest, Slide 2, is ~24). Bold appears only in scaffolding labels ("Angle:", "Caption"), not body copy.

**E — Evidence: PASS.** Every figure traces cleanly.
- 5% GPU utilization across 23,000 clusters → [E24]. Exact.
- 52% no owner, four-way split → [E23]. Exact, including the four owners named (engineering, finance, product, platform) — [E23] says "split four ways" without naming them; the four functions are a reasonable gloss but not in the ledger. Minor, not a fail, since the count and claim match. Watch it.
- $0.41 → $0.07 across 84 Bedrock deployments → [E28]. Exact. Good discipline not importing the "83%" or "20–25%" figures.
No composite claims, no CONFLICT figures stated as single numbers, no invented specifics.

**O — One thing: PASS.** The post argues: the money is in operating GPU/inference you already run, and the block is that no one owns the cost. That is one idea (ownership is the mechanism of the operating lever, not a second thesis). Ladders directly to the big idea and hits the slot's N3 job for VPs of Data.

**L1 — Interchangeability: PASS.** Not swappable. The 5%/$0.41→$0.07/23,000-cluster/84-Bedrock specifics are welded to GPU and inference economics; you can't drop in a different service and keep the sentences.

**L2 — CTO respect: PASS.** A VP of Data would respect this. Numbers-forward, no puffery, the levers named (route, cache, size to load) are real and correctly ordered.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is Slide 2: the four-way ownership split is *why* the 5% utilization persists — the reader arrives thinking idle GPU is a capacity/procurement issue and leaves seeing it as an unowned-accountability issue. That reframe of the problem's location is the insight.

**R — Rhythm/human: BORDERLINE PASS.** Carousel compression justifies shorter beats, and lengths do vary within slides. But the two contrastive-negation constructions are exactly the machine tic the spec targets, and removing them will also improve rhythm. Slide 1's "You pay for all of them" is a good human beat.

## Edit notes

Fix the two reframes in S; everything else holds.

1. **Caption**, replace "The spend isn't the problem. The lack of an owner is." with a direct positive claim, e.g.: "The invoice is real. What's missing is anyone accountable for it." Or simpler: "The bigger issue is that no one owns the bill." State the ownership point directly without negating "spend."

2. **Slide 3**, replace "That's not a capacity problem. It's idle hardware nobody is right-sizing." with a direct statement: "That is idle hardware no one is right-sizing." Drop the negated first clause entirely; lead with the fact.

3. **Slide 5** (optional): after fixing 1 and 2, "None of that is a new purchase. It's operating work..." can stay (it corrects scope, purchase vs. operating), but consider tightening to remove the third negation-shaped beat: "That's operating work on infrastructure you already run, not a new purchase — " no, avoid the dash. Try: "All of it is operating work on infrastructure you already run. The savings fund the next thing you build." Present tense "build" reads cleaner than "want to build."

4. Minor, non-blocking: the four named owners in Slide 2 (engineering, finance, product, platform) aren't in [E23]. Keep only if you're confident that's the standard four-way FinOps split; otherwise say "four functions" to stay inside the ledger.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Fix two contrastive-negation reframes (S, §6.1), neither of which corrects a specific fact/number/scope. (1) Caption: replace 'The spend isn't the problem. The lack of an owner is.' with a direct positive claim, e.g. 'The invoice is real. What's missing is anyone accountable for it.' (2) Slide 3: replace 'That's not a capacity problem. It's idle hardware nobody is right-sizing.' with 'That is idle hardware no one is right-sizing.' — drop the negated clause, lead with the fact. (3) Optional: Slide 5's 'None of that is a new purchase. It's operating work...' corrects scope so it's technically permitted, but after fixing 1 and 2 consider tightening to avoid a third negation-shaped beat: 'All of it is operating work on infrastructure you already run. The savings fund the next thing you build.' (4) Non-blocking evidence note: the four named owners in Slide 2 (engineering, finance, product, platform) are not specified in [E23], which only says 'split four ways'; keep only if confident in the standard FinOps split, otherwise say 'four functions.' All other checks pass; do not touch the numbers or the ownership thesis."}
```