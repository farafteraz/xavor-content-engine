# Editor's memo — Post 5 (2026-09-08, article)

**Overall verdict: FAIL.** The prose is strong and the argument is genuinely non-obvious — this is the best kind of draft to fail, because one mechanical evidence error is the only thing sinking it. Two other checks flirt with the line but survive. Details below.

---

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. "reveal/revealing" is fine, "friction" is the slot's own term (not the banned "frictionless"), "control surface/plane" is literal. No hits on the §5 list. "mission-critical" does not appear in body copy.

**S — Structures: FAIL... on review, PASS.** This draft is built on a reframe, so I read every pivot carefully.

- The whole piece is a "governance is not X, it's Y" argument. But §6.1 explicitly permits contrast "to correct a specific fact, number, date, name, or scope." The correction here is anchored to the 57% blocker and the sequencing claim, not floated as empty antithesis. The headline "don't die of governance. They die of governance done late" is a scope/timing correction, not a hollow reframe.
- "The 57% is what 'later' costs." — short, earned, tied to a real number. Legal.
- "The control is the permission." — assertion, not a banned structure.
- "It is not a maturity curve... It is a cliff" — this is the closest call. It corrects the reader's likely mental model with a specific claim (4% at the bottom, having already shipped). It reads as argument, not slogan. I'll allow it, but flag it under R as the one spot that leans on rhetoric.
- Closing "Governance is not the thing standing between your pilot and production. Wired at the front, it is the gate that ships." — this is the payload reframe the slot exists to deliver, anchored to the whole argument. Permitted.

No triple bursts, no rule-of-three closer, no cliffhanger pivots, no "This is" unveiling, no slogan tags. **PASS.**

**M — Metaphor: PASS, narrowly.** "toll booth on a road you already paid for" is an analogy, and "borrowing it, and the 57% is the interest rate" is a second one. The piece is over 800 words, the subject (why governance-at-the-gate feels like friction) is abstract, and each is shorter and more exact than a literal explanation. But §7 sets the budget at ONE analogy. This draft runs two. That is a mechanical overrun.

Reassessing: the toll-booth line and the interest-rate line are distinct analogies in distinct metaphor families (tolls/roads, then lending/interest). §7: "A single analogy is permitted." Two is a FAIL by the letter of the rubric.

**M — Metaphor: FAIL.**

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy. No em dashes (checked every dash — all are hyphens or sentence punctuation). Word count is roughly 850, under 1,000. Headline is sentence case.

**E — Evidence: FAIL.** This is the primary kill.

The draft's own evidence note admits the problem and then ships it anyway:

> "shadow AI showed up in 43% of breaches this year, at an average cost of $4.99 million... [E20]"

E20 does **not** contain the 43% or the $4.99M figures. Those are E19 (IBM Cost of a Data Breach). E20 covers 67% believe they've suffered a leak, 36% lack a supervision plan, 35% couldn't shut down a rogue agent. The draft cites [E20] for numbers that live in [E19], and the slot's authorized evidence list is [E16, E13, E20] — E19 is not in the slot. The writer's parenthetical ("the $4.99M figure and 43% originate in E19/IBM and are surfaced through E20's cluster") is a rationalization, not a citation. You cannot borrow E19's numbers under an E20 tag and outside the slot's evidence grant.

Also: "two-thirds of the breached organizations had no governance in place to limit unauthorized AI" is again E19 ("two-thirds had no governance to limit unauthorized AI"), tagged [E20]. Same defect.

Every number is individually real. But the citation is wrong and the source entry is outside the slot's evidence budget. Per the rubric ("a real figure attached to the wrong statistic or population... is a FAIL even though every number is individually real"), this fails.

The E16 and E13 uses are clean and correctly attributed.

**O — One thing: PASS.** The post argues: wiring governance into the agent from the first commit is what gets it to production, because governance only feels like friction when it arrives late. One idea, no "and." Matches the slot angle exactly and ladders to the operating-gap big idea.

**L1 — Interchangeability: PASS.** Swap "agent" for another technology and it collapses — the 57%/88%/5.1-month structure, the kill switch, the decision boundary, the access log are specific to agent deployment. Not generic.

**L2 — CTO respect: PASS.** "The pilot didn't fail its review. It failed to be buildable in the first place" is the kind of line a VP of Engineering nods at. No content-marketing wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is clean and locatable: "It failed to be buildable in the first place, and the review is just where you found out." That reframes governance from gatekeeper to build spec. Delivers the slot's intended shift.

**R — Rhythm/human: PASS.** Varied lengths, real transitions, reads aloud like speech. "Read that order again the way a budget committee reads it" skirts the banned "read that again" engagement bait but is redirected into a specific instruction, so it clears. One weakness: the "cliff most companies are standing at the bottom of" leans harder on rhetoric than the rest; acceptable but the softest sentence in the piece.

---

## Edit notes

Two fixes, both surgical. Do not touch the argument, the structure, or the voice — they work.

1. **Evidence (mandatory).** The 43%, the $4.99M, and the "two-thirds had no governance" claims are E19, not E20, and E19 is not in this slot's authorized evidence list [E16, E13, E20]. Two clean options:
   - **Preferred:** replace the shadow-AI breach sentence with a figure the slot actually grants. E20 gives you "35% of executives admit they couldn't immediately shut down a rogue agent" — which is a sharper fit for a piece about kill switches and control-at-the-gate than a generic breach-cost stat. Rewrite the sentence to: "...the exposure between those two facts is concrete: 35% of executives admit they couldn't immediately shut down a rogue agent already in production [E20]." This stays in-slot, needs no new grant, and tightens the through-line.
   - **Alternative:** if you want the breach cost, get E19 added to the slot's evidence list through the human reviewer first, then cite it correctly as [E19]. Do not ship the E19 numbers under an [E20] tag under any circumstance.
   - Delete the parenthetical confession in the evidence note either way.

2. **Metaphor budget (mandatory).** You have two analogies; the spec allows one. Keep "borrowing it, and the 57% is the interest rate" — it's the more exact and it lands the closing move. Cut the "toll booth on a road you already paid for" and state it literally: "...then legal and risk arrive to slow the launch with a review the team already assumed it had cleared." That removes the second analogy and keeps the sentence's meaning.

After those two changes, re-run E and M only. Nothing else needs to move.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "PASS", "M": "FAIL", "F": "PASS", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Two surgical fixes; do not alter argument, structure, or voice. (1) EVIDENCE: The 43% breach share, $4.99M average cost, and 'two-thirds had no governance' claims belong to E19 (IBM), not E20, and E19 is NOT in this slot's authorized list [E16,E13,E20]. Preferred fix: replace the shadow-AI breach sentence with an in-slot E20 figure that fits the kill-switch through-line: '...the exposure between those two facts is concrete: 35% of executives admit they couldn't immediately shut down a rogue agent already in production [E20].' Alternative: get E19 formally added to the slot evidence list via human review, then cite those numbers as [E19] correctly. Never ship E19 numbers under an [E20] tag. Delete the self-justifying parenthetical in the evidence-used note. (2) METAPHOR: two analogies present; spec allows one. Keep 'borrowing it, and the 57% is the interest rate.' Cut the 'toll booth on a road you already paid for' analogy and restate literally, e.g. '...then legal and risk arrive to slow the launch with a review the team already assumed it had cleared.' Re-run checks E and M only after edits."}
```