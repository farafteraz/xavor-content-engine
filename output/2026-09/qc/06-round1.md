# Editor's memo

## Overall verdict: FAIL

Two problems. One evidence attribution issue on the headline accuracy figure, and one banned-structure hit in Frame 4. Details below.

## Per-check results

**V — Vocabulary: PASS.** Scanned for banned terms. "Ecosystem" appears in Frame 7 ("NVIDIA ecosystem") — this is the explicitly permitted literal named-vendor exception (§5, §3 "deep expertise in the NVIDIA ecosystem" is the sanctioned phrasing). No other hits.

**S — Structures: FAIL.** Frame 4: "The robot arrives as a solved product. What arrives unsolved is everything the robot has to talk to." This is a contrastive-negation reframe across sentence boundaries (solved / unsolved pivot), the §6.1 pattern. It's the emotional center of the reel and it's built on the banned move. Frame 3 also flirts with setup-and-negate ("It stopped being whether humanoids work") but reads as a plain factual scope statement, so it survives on its own; combined with Frame 4 the reel leans hard on the solved/unsolved binary.

**M — Metaphor: PASS.** "Coming toward your factory / before the hardware lands" is literal (hardware physically arrives). No banned setups, families, or metaphor verbs. "Talk to" in Frame 4 is idiomatic, not a metaphor family hit.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes. Frame word counts all well under 25. Explainer reel is 8 frames (spec allows 6–8).

**E — Evidence: FAIL.** The headline claim is mis-attributed. "Forty Figure 03 humanoids... above 99% placement accuracy" (Frame 1, repeated in the caption) merges two ledger entries into one composite. E29 supplies the 40 Figure 03 units. E28 supplies the above-99% placement accuracy — but that figure belongs to the 11-month Figure 02 deployment (30,000+ vehicles, 90,000+ components, 1,250 hours). The ledger gives no placement-accuracy number for the Figure 03 fleet. The draft's own evidence note admits the seam: "above 99% placement accuracy attaches to the Spartanburg deployment (E28/E29)" — that is the writer reconciling two entries by hand. Attaching the Figure 02 accuracy figure to the 40 Figure 03 units is exactly the "two ledger entries merged into one composite claim" failure. Either attribute the 99% to the Figure 02 run (where E28 puts it) or flag it [verify] for the Figure 03 fleet.

**O — One thing: PASS.** The post argues: the humanoid is proven, the integration layer around it is the open engineering scope. One idea, matches the N4 slot angle, ladders to the operator's-gap big idea (capability bought, operating layer unbuilt).

**L1 — Interchangeability: PASS.** Swap Figure 03 for another robot and the specifics (BMW Spartanburg, 40 units, edge compute at the cell, digital twin sync) don't survive generically. The claims are grounded.

**L2 — CTO respect: PASS.** Reads like a peer who knows the deployment. The "integration layer is the buy" framing is the kind of thing a manufacturing VP of Engineering would nod at.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands in Frames 4–6: the robot is the settled part, and the unowned scope is the edge/pipeline/twin layer coming toward you. That reframes a board "should we buy humanoids" conversation into an integration-readiness question. Real and non-obvious for this audience.

**R — Rhythm/human: PASS.** Varied frame lengths, real spoken cadence, CTA grows from Frame 6's "that integration layer is the buy" into the close. Not metronomic. Frame 7's list ("embedded systems, robot data pipelines, and deep expertise...") is a rule-of-three-shaped list but it's a plain capability enumeration, not a §6.4 rhetorical closer, so it passes on rhythm.

## Edit notes

Two fixes, both surgical.

1. **Frame 4 (structure).** Kill the solved/unsolved reframe. Replace with a direct positive claim that names what the integration work is. Suggested: "The robot is a finished product. The edge compute, the fleet pipelines, and the twin it feeds are not." — no, that repeats the binary. Better: state it forward without the negation. Something like: "The robot ships finished. The open engineering is everything it connects to on the floor." Even that leans on the contrast. Cleanest fix: cut the contrast entirely and lead into Frame 5's specifics — e.g. "The robot ships as a finished product. Its integration into your floor is a separate build," then let Frame 5 enumerate edge/pipeline/twin. State the scope directly; do not pivot off "solved."

2. **Frame 1 + Caption (evidence).** The above-99% placement accuracy is a Figure 02 figure per E28, not a verified Figure 03 fleet number. Two options: (a) Move the 99% to the Figure 02 track record — Frame 1 states the 40 Figure 03 units in production, Frame 2 (already Figure 02) carries the "above 99% placement accuracy across 1,250 hours, 90,000 components." That keeps every number on its correct population. Or (b) if you want the accuracy figure in the headline attached to the current fleet, flag it [verify: does above-99% placement accuracy apply to the 40 Figure 03 units, or only the prior Figure 02 deployment?] and let the human reviewer confirm before ship. Recommend option (a) — it's cleaner and needs no external check. Update the caption the same way: don't bind "40 humanoids" and "above 99% placement accuracy" in the same clause unless the ledger supports the pairing.

Everything else holds. Fix these two and it ships.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["If the headline pairing is kept: verify whether above-99% placement accuracy applies to the 40 Figure 03 units or only the prior Figure 02 deployment (E28 assigns it to Figure 02)."],
 "edit_notes": "Two surgical fixes. (1) STRUCTURE, Frame 4: remove the solved/unsolved contrastive-negation reframe ('The robot arrives as a solved product. What arrives unsolved is everything the robot has to talk to.'). Replace with a forward positive claim that does not pivot on a negation, e.g. 'The robot ships as a finished product. Its integration into your floor is a separate build.' Then let Frame 5 carry the edge/pipeline/twin specifics. Do not restate the binary. (2) EVIDENCE, Frame 1 and Caption: the above-99% placement accuracy is a Figure 02 figure (E28), not a verified Figure 03 fleet number. Do not bind '40 Figure 03 units' and 'above 99% placement accuracy' in the same clause. Preferred fix: Frame 1 states only the 40 Figure 03 units in production; move the above-99% accuracy into Frame 2 alongside the Figure 02 record (1,250 hours, 90,000 components, 30,000 vehicles), where E28 places it. Update the caption to match so the accuracy number sits with its correct population. If instead you keep the accuracy figure in the headline, add a [verify] flag. Everything else passes."}
```