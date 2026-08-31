# Editor's Memo — Post 15 (explainer reel)

## Overall verdict: FAIL

Two mechanical violations: a contrastive-negation reframe in the caption (§6.1) and a banned "This is" unveiling in Frame 3 (§6.6). Everything else is clean and the evidence is disciplined. These are surgical fixes.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Tooling" and "governance" are fine; no filler copulas ("is," "needs," "run" are literal).

**S — Structures: FAIL.**
- Caption: "The fix isn't a new tool. It's knowing which agents you run and who owns each one." This is a textbook contrastive-negation reframe across sentence boundaries (§6.1). It does not correct a specific fact, number, or scope — it rejects a strawman ("a new tool") to pivot to the positive claim. FAIL.
- Frame 5: "The gap isn't tooling. It's that nobody wrote down which agents run..." Same pattern, second instance. FAIL.
- Frame 3: "This is the AI you already have." Opens with "This is" as an unveiling (§6.6). Lead with the subject. FAIL.

**M — Metaphor: PASS.** No analogies, no banned setups, no metaphor verbs. "Wired to your data" is literal enough to survive (agents are literally connected to data sources). "Closes the gap" is idiomatic, not a banned metaphor family.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes, bold/caps in body copy. The bold in `**Angle:**` and `**Evidence used:**` is scaffolding metadata, not body copy. Frame word counts all well under 25 (longest, Frame 6, is 19 words). Explainer reel is 8 frames — at the top of the 6–8 spec band but within it.

**E — Evidence: PASS.**
- Frame 1: "43% of data breaches in 2026, up from about 20%" — traces to [E19]. Correct.
- Frame 2: "$4.99M... Two-thirds... had no governance to limit unauthorized AI" — [E19]. Both figures and the two-thirds attach to the same IBM population. Correct, no merge.
- Frame 4: "35%... couldn't immediately shut down a rogue agent. 36% have no plan to supervise agents" — [E20]. Both figures live in [E20], correctly attributed (IBM/Writer). Correct.
- Frame 6: ownership standard — [E44]. Correctly used as the standard, not stated as a stat.
- No invented numbers, no CONFLICT figure stated as single, no denominator drift. Clean.

**O — One thing: PASS.** The post argues: the cost of unowned shadow AI is real and the fix is inventory-plus-ownership. One idea, ladders directly to the operating gap (owner and inventory = the operating work). Matches slot N2 exactly.

**L1 — Interchangeability: PASS.** The claim is specific to shadow AI, agent inventory, and rogue-agent shutdown. You cannot swap the subject and keep the sentences ("35% couldn't shut down a rogue agent" is not generic content-marketing copy).

**L2 — CTO respect: PASS.** The rogue-agent-shutdown and named-owner framing reads like an engineer, not a vendor. No wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands in Frame 5→6: the reframe isn't a security-tool problem, it's that nobody wrote down which agents run on what data answering to whom — and the fix is the same ownership work as the operating gap. That connects breach cost to an operations discipline the CTO hasn't filed under "security." Real.

**R — Rhythm/human: PASS.** Frame lengths vary, reads like speech, CTA lands naturally in the "now" register. Not metronomic.

## Edit notes

Two reframe fixes and one opener fix. Preserve the meaning; state the positive claim directly.

1. **Caption** — kill the "isn't a new tool. It's..." reframe. Rewrite to state the fix positively:
   "Shadow AI showed up in 43% of breaches this year, at an average cost of $4.99M. The fix is knowing which agents you run and who owns each one." (Delete "The fix isn't a new tool." entirely.)

2. **Frame 3** — remove the "This is" unveiling; lead with the subject:
   "The AI you already have. Bought by a department, wired to your data, running without an owner." (Or, if you want a full sentence: "You already run this AI — bought by a department, wired to your data, with no owner." Note: no em dash — use a comma or period.) Recommended clean version: "The AI you already own. Bought by a department, wired to your data, running with no owner."

3. **Frame 5** — kill the second "isn't tooling. It's that..." reframe. State it straight:
   "The gap is operational: nobody wrote down which agents run, on what data, answering to whom." (This also strengthens the L3 payload by naming it as operational work, which ladders harder to the big idea.)

Nothing else needs to move. Re-run S after these three edits and the draft ships.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Three fixes, all §6 structure violations. (1) Caption: delete the contrastive-negation reframe 'The fix isn't a new tool.' and state the positive claim directly: 'Shadow AI showed up in 43% of breaches this year, at an average cost of $4.99M. The fix is knowing which agents you run and who owns each one.' (2) Frame 3: remove the 'This is' unveiling; lead with the subject: 'The AI you already own. Bought by a department, wired to your data, running with no owner.' (3) Frame 5: delete the second reframe 'The gap isn't tooling. It's that...' and state it straight, which also sharpens the L3 ladder: 'The gap is operational: nobody wrote down which agents run, on what data, answering to whom.' No em dashes in any replacement. Re-run check S after edits; all other checks pass as-is."}
```