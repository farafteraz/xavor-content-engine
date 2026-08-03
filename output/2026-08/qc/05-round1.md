# Editor's memo — Post 5 (explainer reel)

**Overall verdict: FAIL.** One mechanical hit on S. The evidence and thesis work hold up well, and the reel mostly reads clean, but Frame 4 opens with a banned cliffhanger pivot that has to go.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Scaling," "control," "governance" all used literally and in-scope. No filler "critical/crucial." Clean.

**S — Structures: FAIL.** Frame 4: "Here is the part that reshapes the math." This is a cliffhanger pivot (§6.5 — the "The result?" / "Here's the thing" family), plus a soft puffery reveal that inflates the following claim before stating it. Delete it and lead with the fact.

Also worth flagging (not a standalone FAIL, but adjacent): Frame 5 → "makes the accountability gap worse, not smaller" is contrastive negation (§6.1). "Worse, not smaller" is a redundant reframe — worse already carries the meaning. Cut "not smaller." And the caption's "It widens the gap" following "doesn't hold the line" leans on the same setup-and-negate rhythm; tolerable but tighten.

**M — Metaphor: PASS.** "Hold the line" in the caption is a mild idiom, not a banned family (not journey/battlefield/engine/etc. in the structural sense the spec polices), and it reads normal aloud. "Control has to live inside the workflow" — "live inside" is literal enough for embedded software. No banned setups or metaphor verbs. Clears.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Frame word counts all well under 25. Reel is 8 frames — spec allows 6–8. Fine.

**E — Evidence: PASS.** Every claim traces:
- Frame 1 "two-thirds accountable for AI they don't fully control" → [E7]. ✓
- Frame 2 "2,000 executives" and "77% say adoption is outpacing governance" → [E7] (n=2,000), [E8]. ✓
- Frame 3 "only 11% feel fully ready for agents to scale next year" → [E8]. ✓
- Frame 4 "manual governance sees 25% more incidents than embedded control" → [E9]. ✓
Denominators and populations are correctly matched — all three cited entries are the same IBM IBV study, and the draft doesn't merge them into a composite or misattribute the 77%/11% to the wrong base. No invented specifics. No CONFLICT figures touched. Clean.

**O — One thing: PASS.** The post argues: scaling accountability you don't control with manual governance widens the gap; embedded control is the fix. One idea, matches the slot angle, ladders to "the layer under the platform" (governance you can demonstrate at audit).

**L1 — Interchangeability: PASS.** The 25% manual-vs-embedded incident delta and the identity-verified/logged-as-it-happens control surface are specific to governance architecture, not swappable boilerplate. You can't drop in a different technology and keep the sentence true.

**L2 — CTO respect: PASS.** Reads as a peer stating a structural problem the reader already half-feels. No wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" lands in Frame 5: adding reviewers and checklists — the obvious response — makes the gap worse. That inversion of the instinctive fix is the earned insight, and it's backed by the 25% figure rather than asserted.

**R — Rhythm/human: PASS.** Varied line lengths, real short-long alternation ("Only 11% feel fully ready... The agents are scaling anyway."), CTA grows from the audit line before it. Not metronomic. Once Frame 4's opener is cut it reads fully human.

## Edit notes

1. **Frame 4 — remove the cliffhanger pivot.** Delete "Here is the part that reshapes the math." Lead directly with the fact. Rewrite the frame as: "When AI scales, manual governance sees 25% more incidents than embedded control." That is the whole frame — the number carries its own weight, especially with the design note giving it the strongest visual emphasis.
2. **Frame 5 — kill the contrastive negation.** Change "makes the accountability gap worse, not smaller" to "makes the accountability gap worse." "Worse" is sufficient; "not smaller" is the reframe.
3. **Caption (optional tighten, not blocking):** "It widens the gap" is fine on its own, but consider "Scaling that with manual governance widens the gap it was meant to close." — removes the two-beat setup-and-negate and adds a specific.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Frame 4: delete the cliffhanger pivot 'Here is the part that reshapes the math.' (banned §6.5). Lead directly with the fact: 'When AI scales, manual governance sees 25% more incidents than embedded control.' Let the number carry the frame; the design note already gives it top visual weight. Frame 5: remove the contrastive negation 'worse, not smaller' (banned §6.1) — change to 'makes the accountability gap worse.' Optional: tighten the caption's setup-and-negate ('doesn't hold the line. It widens the gap') to a single specific line such as 'Scaling that with manual governance widens the gap it was meant to close.' No evidence changes needed; all claims trace cleanly to E7/E8/E9."}
```