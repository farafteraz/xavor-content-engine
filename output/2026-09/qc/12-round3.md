# Editor's memo — Post 12 (case-study carousel)

**Overall verdict: FAIL** — on evidence integrity. Two distinct robots (Figure 02 at BMW, and Navi) are fused into a single implied proof, and the ledger cannot support the core numeric claim as applied to Navi. Slide 4 also carries a soft contrastive-negation problem. Details below.

## Per-check

**V — Vocabulary: PASS.** No banned words. "Mission-critical," "seamless," etc. all absent. Good.

**S — Structures: PASS, borderline.** Watched for the reframe pattern hard. Slide 1 "The accuracy came from the robot. Deployability comes from the layer around it." is a legitimate factual distinction (which capability comes from which component), not a "not-X-but-Y" insight simulation — allowed under §6.1's fact/scope exception. Slide 5 "The integration around it is still the work" and slide 2 "is an edge-compute and data-pipeline problem" are direct claims, not setups. No triple bursts, no rule-of-three closers, no cliffhangers. Passes, but slide 1's two-beat structure repeats across caption and slide 1 verbatim — see R.

**M — Metaphor: PASS.** "Fed and watched" (slide 3) is borderline anthropomorphic but reads as literal ops language (data-fed, observed), not a banned metaphor family or verb. No "bridge/engine/backbone," no journey/machine metaphors. Clear.

**F — Formatting: FAIL-adjacent, technically PASS on bans.** No emojis, hashtags, exclamations, em dashes, caps in body. Slide word counts all under 25. But note: the bold on `**Slide 1:**` labels and `**Angle:**` is scaffolding, not body copy, so it does not trip check F. **PASS.**

**E — Evidence: FAIL.** Two hard violations:

1. **Composite/merged claim across E30 and Navi.** The caption and slides 1–3 build a single argument: a humanoid hit 99% across 90,000 parts on a BMW line (E30, real, Figure 02), *therefore* the operating layer is what makes robots deployable, *and* Navi runs at 99% (unverified). The 99% figure appears twice — once sourced to Figure 02 (E30) and once to Navi (flagged) — using the identical number. E30 is Figure AI's Figure 02 with Figure's own Helix VLA. Xavor did not build Figure 02's edge compute or pipelines. The carousel's implicit claim — "we built the layer that produced this 99%" — is not what E30 supports. The design note ("keep the two robots visually separate") is an admission that the piece is engineering a reader inference it knows is false. Presenting E30's proof-of-hardware adjacent to Navi's unproven 99%, using the same headline number, is exactly the merged-composite failure the rubric names.

2. **The central case-study claim is unverified.** This is a *case-study carousel* whose job (per slot) is to make a manufacturing leader trust a *delivered practice shown through Navi*. The one fact that would do that — Navi at 99% task accuracy, built on Xavor's edge/pipeline layer — is `[verify: Navi 99% task-accuracy production figure]`. The big idea cites [E30] for "the robot works at 99%," but E30 is Figure 02, not Navi. There is no ledger entry for Navi at all. A case study cannot ship on a flagged core figure plus a borrowed competitor's number standing in for the proof. Slide 3 is the entire point of the post and it is unverified.

**O — One thing: PASS on structure, but the "one thing" rests on unverified evidence.** The post argues exactly one idea: the operating layer (edge compute + pipelines), not the robot, determines deployability. Ladders cleanly to the big idea. No "and." The problem is E, not O.

**L1 — Interchangeability: WEAK PASS.** Swap "humanoid/Navi" for "a vision system" and slide 2's "local inference, fleet data paths, and connectivity that keep every unit observable" still largely works — it's specific to fleets-of-units, which is the right specificity, so it survives. But slide 4 ("run the machine, watch it in real time, and account for its work") is generic enough to describe any monitored system. Not a standalone FAIL; tighten in rewrite.

**L2 — CTO respect: FAIL.** A manufacturing VP who knows the humanoid space will recognize the BMW/90,000-parts figure as Figure AI's public number, then read three slides later that "Navi" hits the same 99%, and conclude Xavor is borrowing Figure's proof to dress up an unproven internal robot. That wince is fatal for a case study. The credibility of the format depends on the case being ours.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" is real and lands on slide 2: deployability of a humanoid is an edge-compute and data-pipeline problem, not a robotics problem. That reframes where a manufacturing leader should look. Genuinely differentiated. This is the post's strength and worth preserving in the rewrite.

**R — Rhythm/human: WEAK PASS with one flag.** Sentence lengths vary, transitions are real, opens on a hard fact with no throat-clearing, CTA lands in register. One problem: the caption and slide 1 share two identical sentences ("A humanoid placed 90,000-plus parts... The accuracy came from the robot"). A caption and slide 1 should not be a copy-paste. Differentiate them.

## Edit notes

The post fails because it cannot prove what a case study must prove. Two paths:

**Path A (preferred, if the figure can be sourced):** Get Navi's real production numbers into the ledger — task accuracy, hours run, unit count, the line or pilot it ran on. Rebuild the carousel entirely around Navi's own numbers. Then E30 (Figure 02) is not needed at all; drop it. If you keep one industry data point for context, use E33 (a16z capital) on the closing slide only, clearly framed as market context, never as our proof.

**Path B (if Navi has no shippable production figure yet):** Do not run this as a case-study carousel. A case study with a `[verify]` on its central claim cannot ship. Either reslot to a non-case-study format that argues the *principle* (deployability is an edge/pipeline problem) without claiming a specific Navi result, or hold until Navi's numbers are corpus-backed.

Specific fixes regardless of path:
- Remove the E30 Figure 02 number entirely, or if kept for context, it must be explicitly attributed ("Figure's humanoid at BMW hit...") and must not sit adjacent to Navi's number using the identical "99%." Never let two robots share one headline figure.
- Delete the design-note instruction to "keep the two robots visually separate." If you have to stage-manage the reader away from a false inference, the copy is making a claim the evidence doesn't.
- Replace the flagged slide 3 with a Navi fact the corpus supports, or cut the specific figure and state the qualitative claim you *can* stand behind about what Xavor built.
- Rewrite the caption so it does not duplicate slide 1 verbatim.
- Tighten slide 4 so it names what is monitored and accounted for specifically to a governed line, not any system.

The insight (slide 2) is strong and should anchor the rebuild. The evidence spine must become Navi's, not Figure's.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "FAIL", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["Navi 99% task-accuracy production figure — no ledger entry exists for Navi; the core case-study claim cannot ship until corpus-backed with task accuracy, hours, unit count, and the line/pilot it ran on"],
 "edit_notes": "FAIL on E and L2: the carousel merges Figure 02's real BMW numbers (E30) with Navi's unverified 99% into one implied proof, using the identical headline figure for two different robots, and the central case-study claim (Navi at 99% on Xavor's edge/pipeline layer) is a [verify] flag with no ledger support. Path A (preferred): source Navi's real production numbers into the ledger (accuracy, hours, unit count, line/pilot), rebuild the carousel entirely on Navi's own figures, and drop E30 (Figure 02) completely. Path B: if Navi has no shippable figure, do not run this as a case study — reslot to a principle-only format or hold until corpus-backed. Regardless of path: (1) remove the E30 Figure 02 99% number or attribute it explicitly to Figure and never place it adjacent to Navi's number sharing '99%'; (2) delete the design-note line 'keep the two robots visually separate' — if you must stage-manage the reader away from a false inference, the copy is over-claiming; (3) replace flagged slide 3 with a corpus-supported Navi fact or state only the qualitative claim you can stand behind about what Xavor built; (4) rewrite the caption so it does not duplicate slide 1 verbatim; (5) tighten slide 4 to name specifically what is monitored and accounted for on a governed line rather than any system. Preserve slide 2's insight (deployability is an edge-compute and data-pipeline problem, not a robotics problem) as the spine of the rebuild."}
```