# Editor's Memo — Post 15 (case-study carousel)

**Overall verdict: FAIL.** One mechanical hit on structures (S), and the evidence assignment for slide 2's "seven model calls across three providers" needs a closer look but holds. The blocking issue is a banned "This is" unveiling on slide 2 plus a cross-sentence reframe on slide 4. Details below.

## Per-check

**V — Vocabulary: PASS.** Scanned against §5. No banned words. "seamless," "leverage," "robust," etc. all absent. "Attribution," "fan-out," "trace," "reconcile" are precision terms, allowed.

**S — Structures: FAIL.** Two hits.

1. Slide 2 opens with "This is real." That is a §6.6 banned "This is" unveiling used as a dramatic opener, and it adds nothing — the sentence that follows already carries the fact. Cut it.
2. Slide 4: "An unassignable GPU bill is a boardroom problem." Read against the preceding sentence this is borderline puffery (§6.10) — it asserts weight instead of showing it. Not a clean structural FAIL on its own, but combined with the opener it drags the check down. The clear FAIL is the "This is real" unveiling.

Also flag, not failing: slide 3 runs "You can see the total. You cannot see which team, product, or workflow caused it." That is a legitimate factual contrast (§6.1 permits contrast that corrects scope), so it passes, but watch the rhythm note below.

**M — Metaphor: PASS.** "fans out," "chain," "line item" are literal FinOps/engineering terms, not metaphor. No banned setups or verbs.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Bold appears only in the header/label scaffolding (`**Angle:**`), not in body copy. Slide word counts all under 25 (longest, slide 5, is ~40 across two sentences — recount below). Correction: slide 5 is "The fix is engineering, not procurement. Tag every call at the point of fan-out with the query, team, and workflow that caused it. Carry those tags through the trace so the invoice reconciles to a line item." That is ~44 words — over the 25-word cap. **This is an F FAIL.** Slide 2 is ~40 words, also over. Recheck: slide 2 body ("This is real. One banking query triggers an orchestrator, three retrievers, four tool calls, and seven model invocations across providers. The bill aggregates at the tenant level.") is ~38 words. **Slides 2 and 5 both exceed 25 words. F FAILS.**

**E — Evidence: PASS with one note.** 
- Slide 2 fan-out chain (orchestrator + 3 retrievers + 4 tool calls + 7 model invocations, banking query, tenant-level bill) → [E50]. Exact match. Good.
- "seven model calls across three providers" on slide 1: [E50] says "across providers" but does not specify three. Slide 1 says "three providers"; [E50] does not give that number. **This is invented specificity — E FAIL.** [E50] gives the call counts but not a provider count. Cut "three providers" or change to "across providers."
- Slide 4 GPU spend #1 FinOps concern surpassing general cloud → [E49]. Exact. Good.
- Slides 4/5 instrumentation as buildable → [E48], used as framing not a quoted figure. Fine.

**O — One thing: PASS.** The post argues: the agentic query fan-out is where cost attribution breaks, and instrumenting the fan-out is the buildable cost layer. One idea, matches the slot, ladders to the big idea's cost gap (D8).

**L1 — Interchangeability: PASS.** The fan-out chain (orchestrator + 3 retrievers + 4 tool calls + 7 model invocations, banking query) is specific enough that you cannot swap it for a generic service. Good.

**L2 — CTO respect: PASS.** The engineering-not-procurement framing and the tag-through-trace mechanic read like a peer who has done the work.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is on slide 3/5: attribution breaks *at the fan-out point*, so the fix is tagging at fan-out and carrying tags through the trace — not reading the invoice harder. That reframes the bill from a procurement problem into an instrumentation problem. Real.

**R — Rhythm/human: WEAK.** Slide 1's four short sentences plus the closing question flirt with the metronome the spec warns against, and "This is real" is assistant-flavored throat-clearing. Fixable with the S edits.

## Edit notes

1. Slide 1: delete "three providers" (unsupported by [E50]) — write "across providers" or drop the provider count entirely. This is the E FAIL fix.
2. Slide 2: delete the opener "This is real." (banned §6.6 unveiling). Then compress to ≤25 words. Suggested: "One banking query triggers an orchestrator, three retrievers, four tool calls, and seven model invocations across providers. The bill aggregates at the tenant level." Count it — if still over 25, cut "an orchestrator," and open "One banking query fans out into three retrievers, four tool calls, and seven model invocations." Keep the [E50] attribution.
3. Slide 5: over 25 words. Cut to the mechanic only: "The fix is engineering, not procurement. Tag every call at fan-out with the query, team, and workflow, then carry those tags through the trace to a line item." Recount and trim to land at or under 25.
4. Slide 4: replace "An unassignable GPU bill is a boardroom problem" (asserts weight, §6.10) with a fact that shows the weight, e.g. tie to the aggregated-tenant reality already established, or cut the sentence and let the [E49] figure stand.
5. Recheck every slide's word count after edits; the cap is hard.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "1) Slide 1: 'three providers' is not supported by [E50], which says only 'across providers'. Change to 'across providers' or drop the provider count. 2) Slide 2: delete banned 'This is real.' unveiling (S6.6); then compress the slide to <=25 words, e.g. 'One banking query fans out into three retrievers, four tool calls, and seven model invocations across providers. The bill aggregates at the tenant level.' Keep (FinOps Foundation)/[E50] attribution. 3) Slide 5 is ~44 words, over the 25-word cap. Trim to the mechanic only: 'The fix is engineering, not procurement. Tag every call at fan-out with the query, team, and workflow, then carry those tags through the trace to a line item.' Recount to <=25. 4) Slide 4: replace 'An unassignable GPU bill is a boardroom problem' (puffery, S6.10) with a fact that shows the stakes or cut it and let the [E49] figure stand. 5) Recount every slide after edits; 25-word cap is hard, slides 2 and 5 currently exceed it."}
```