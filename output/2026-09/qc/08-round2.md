# Editor's memo — Post 8 (explainer reel)

**Overall verdict: FAIL** on one mechanical check (S). The draft is strong, the evidence is clean, and the insight lands, but Frame 2 contains a cross-sentence contrastive negation that the spec bans outright.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. "Mission-critical" appears in Frames 3 and 5, but both are direct quotes of the Google/Credo survey language carried in the ledger (E51, E52), so they fall under the "unless quoting" exemption. No other banned terms. Note for the writer: "mission-critical" is on the banned list (§5); keeping it is defensible only because it's the surveyed language. Watch it.

**S — Structures: FAIL.**
- Frame 2: "Most companies wrote the governance policy. What they never built is the layer that enforces it..." This is a contrastive negation across sentence boundaries — the exact "Most teams think they have a hiring problem. They have a standards problem." pattern named in §6.1. The setup (they wrote the policy) exists only to be negated by the pivot (what they never built). It is not correcting a specific fact, number, date, or scope, so it does not qualify for the allowed exception.
- Frame 4: "Policy lives in a document. Enforcement lives in wiring..." Borderline. This reads as a parallel definition rather than a setup-and-negate, and it's carrying real specifics (inventory, decision boundaries, token attribution). I'd let it stand, but it's close enough that a rewrite should make sure it doesn't tip into the same reframe rhythm as Frame 2.

**M — Metaphor: PASS.** "Wire into," "wiring," "layer," "carry a mission-critical agent," "standing between you and production" are all literal engineering language, not banned metaphor families or verbs. "Renders on demand" is literal (audit trails render). No analogies, no banned setups.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes. Frame word counts all well under 25. This is a reel, not a carousel, but the compression discipline holds.

**E — Evidence: PASS.** Every claim traces cleanly.
- Frame 1: 60% / 4% → E52. Correct denominator (371 senior leaders, Credo AI). ✓
- Frame 3: 83% / 17% → E51. Correct denominator (1,400+ senior IT leaders, Google). ✓
- Frame 5: 61%→92% governance urgency at scaled programs → E52. ✓
No composite claims, no CONFLICT figures stated as single numbers, no invented specifics. Source lines are attached to the right populations. Clean.

**O — One thing: PASS.** The post argues one thing: governance at scale fails because the enforcement layer under the policy was never built (an infrastructure problem, not a policy problem). Matches the slot's N2 job exactly and ladders to the operator's-gap thesis (capability deployed, unowned, unaccounted).

**L1 — Interchangeability: PASS.** The specifics (per-agent inventory, decision boundaries, token attribution, audit trail, the 4%/17%/92% figures) are not swappable for another technology. This is about agentic AI governance specifically.

**L2 — CTO respect: PASS.** The frames name the real mechanics and don't oversell. A CTO would not wince. Frame 4's enumeration (inventory, decision boundaries, token attribution, audit trail) is the kind of concrete scope that earns respect.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is Frame 5: governance urgency doesn't rise gradually, it jumps 61%→92% at the exact moment of scale, which reframes governance as a threshold event tied to an unbuilt layer rather than a policy you can write ahead of time. That converts a policy mindset into an infrastructure one, which is the slot's whole job.

**R — Rhythm/human: PASS, with a note.** Sentence lengths vary within frames, transitions are real, the CTA grows out of Frame 6 rather than being bolted on. It doesn't read metronomic. The one risk: reel frames naturally tend toward stat-then-claim uniformity, and Frames 1/3/5 all follow that shape. It works here because the claims differ in kind, but the rewrite of Frame 2 should not add a fourth stat-claim beat.

## Edit notes

One fix required.

**Frame 2** — Remove the contrastive negation. Currently: "Most companies wrote the governance policy. What they never built is the layer that enforces it across every deployed agent." Rewrite as a direct positive claim that states the gap without the "they did X, but never Y" setup. Something like: "The governance policy exists in most companies. Enforcing it across every deployed agent takes a layer the stack was never built to hold." Or lead with the enforcement layer directly: "Enforcing a governance policy across every deployed agent takes a layer most stacks were never built to hold. That layer is what's missing." Keep it to the reel's compressed register, keep it under 25 words, and do not convert it into a stat frame. The point of Frame 2 is the conceptual bridge from Frame 1's numbers to Frame 4's mechanics; state that bridge as a fact, not a reframe.

While you're in there: confirm you're comfortable keeping "mission-critical" as surveyed language in Frames 3 and 5. It's exempt as a quote, but if you can attribute it visually (source line) without leaning on the phrase in the VO, cleaner is better.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Frame 2 contains a banned cross-sentence contrastive negation (§6.1): 'Most companies wrote the governance policy. What they never built is the layer that enforces it...' The setup exists only to be negated and does not correct a specific fact/number/date/scope, so it fails. Rewrite as a direct positive claim stating the enforcement-layer gap. Example: 'Enforcing a governance policy across every deployed agent takes a layer most stacks were never built to hold. That layer is what's missing.' Keep under 25 words, keep the reel's compressed voice, do not turn it into a fourth stat frame (Frames 1/3/5 are already stat-then-claim). Frame 2's job is the conceptual bridge from Frame 1's numbers to Frame 4's mechanics: state it as fact, not reframe. Secondary: 'mission-critical' in Frames 3 and 5 is banned vocabulary but exempt as surveyed quote language (E51/E52); keep only if attributed to the source, and prefer not to lean on the phrase in VO."}
```