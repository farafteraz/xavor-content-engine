# Editor's Memo — Post 4 (carousel)

**Overall verdict: FAIL** (one structural violation; one rhythm concern). The evidence work is clean and careful, and the argument holds a single line. But slide 4 carries a banned contrastive-negation structure, and a couple of slides drift toward metronome fragment-chains.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Runtime is not semantics" uses "not" but as a factual distinction, not filler. No banned openers or bait.

**S — Structures: FAIL.**
- Slide 4: "AI does not have an intelligence problem, it has a context problem. Runtime is not semantics." The quoted line from Ghodsi is fine as a quote. But the appended sentence "Runtime is not semantics" is a writer-added contrastive-negation reframe (§6.1) — it sets up a not-X to imply a Y, and it's cryptic on its own. This is a hard hit.
- Watch also Slide 1: "the cause is usually below the model. It can't reliably tell what your data means." — this is a legitimate cause statement, reads clean, not a reframe. Passes.
- Slide 2: "Semantics is the variable." borders on an amputated slogan tag (§6.9), but it's a full sentence stating a specific claim, so it clears.

**M — Metaphor: PASS.** No analogies, no banned setups or verbs. "One layer down" / "below the model" is literal, not figurative here.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes, caps. Slide word counts all under 25 (highest is slide 5 at ~34 — recount below). Correction: Slide 5 runs "Gartner projects that by 2027, organizations with unified semantics raise agent accuracy up to 80% and cut agentic AI costs up to 60%. These gains come from the semantic layer, not from a bigger model." That is roughly 40 words. **This fails the ≤25 words/slide cap.** Reclassify F as **FAIL**.

**E — Evidence: PASS.** Strong. Every claim traces:
- Slide 2/5 to [E34], and critically the draft keeps the 80%/60% figures attached to the unified-semantics population and to 2027, not misapplied. Correct.
- Slide 3 "~85% of clients have a data problem before an AI problem" to [E33]. Correct.
- Slide 4 Ghodsi quote to [E36], verbatim. Correct.
- No invented specifics, no CONFLICT figure misused, no merged claims. This is the cleanest part of the draft.

**O — One thing: PASS.** The post argues: agent hallucination comes from the semantic/data foundation, not model choice, and unified semantics is what lifts accuracy and cuts cost. Single thesis, matches the slot angle, ladders to the big idea's second gap (the data/semantic layer).

**L1 — Interchangeability: PASS.** Swap "semantics" for "a bigger model" and the copy breaks — the whole point is the model isn't the lever. Named sources (Gartner, Accenture, Databricks) are specific and load-bearing.

**L2 — CTO respect: PASS.** Reads like a peer citing benchmark data, not content marketing. A VP of Data would not wince.

**L3 — Cognitive depth: PASS.** The moment lands on slide 5: the accuracy and cost gains come from the semantic layer, not a bigger model. For a VP of Data mid-pilot who's been A/B-testing models, "the cost lever is the semantic layer, not the model" is the "I hadn't considered that."

**R — Rhythm/human: WEAK (borderline).** Slides 1, 2, and 4 chain into short declarative fragments that start to feel metronomic when read in sequence ("Semantics is the variable." / "Runtime is not semantics." / "It can't reliably tell what your data means."). Not a hard fail alone, but combined with the S violation on slide 4, it reads slightly machine-cut. Fix it in the rewrite of slides 4 and 5.

## Edit notes

Two mechanical fixes required, one rhythm cleanup:

1. **Slide 4 (S fail):** Delete "Runtime is not semantics." It's a contrastive-negation reframe and it's cryptic. Keep the Ghodsi quote and add a plain consequence sentence instead, e.g.: "Databricks CEO Ali Ghodsi put it plainly at their summit: AI does not have an intelligence problem, it has a context problem. Context is the data your agent can resolve." (Verify final wording stays under 25 words.)

2. **Slide 5 (F fail — word count):** Currently ~40 words; cap is 25. Split or compress. Keep the payoff numbers as the anchor. Suggested compression: "Gartner projects that by 2027, organizations with unified semantics raise agent accuracy up to 80% and cut agentic AI cost up to 60%." That's ~24 words. Move "these gains come from the semantic layer, not a bigger model" into the design/VO or drop it — the number already makes the point, and cutting it also removes a near-reframe.

3. **Rhythm:** After fixing 4 and 5, read all six slides aloud in order. If slides 1, 2, 4 still land as three equal clipped beats, lengthen one — slide 2 can carry a fuller line ("Gartner found that without a unified semantic layer, agents are measurably more likely to hallucinate on what your data means.") to break the metronome.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Slide 4 (S): delete 'Runtime is not semantics.' — a contrastive-negation reframe and cryptic on its own. Replace with a plain consequence line, e.g. 'Context is the data your agent can resolve.' Keep the Ghodsi quote intact and attributed to [E36]. Slide 5 (F): currently ~40 words, over the 25-word cap. Compress to 'Gartner projects that by 2027, organizations with unified semantics raise agent accuracy up to 80% and cut agentic AI cost up to 60%.' (~24 words). Drop the trailing 'these gains come from the semantic layer, not a bigger model' sentence (it also reads as a near-reframe); push that idea into the design/VO note if needed. Keep both Gartner figures attached to the unified-semantics population and to 2027 [E34]. Rhythm: after edits, read slides 1/2/4 aloud; if they land as three equal clipped beats, lengthen slide 2 to a fuller line to break the metronome. Do not add new claims or figures beyond E33/E34/E36."}
```