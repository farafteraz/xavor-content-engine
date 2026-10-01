# Editor's memo — Post 14 (Navi case-study carousel)

## Overall verdict: PASS

A clean, specific carousel that lands the floor-integration claim without hype. The one swappable-robot trap is avoided because Navi's perception classes (fall detection, blocked corridor, medication cue) and the eldercare context anchor the specifics. The two [verify] flags are correctly placed and must be confirmed before publish, but they are flags, not unverified published claims.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Fleet governance," "edge inference," "embedded layer," "on-device" are precision technical terms, explicitly allowed. No "seamless," "robust," "scalable," no filler "crucial/critical."

**S — Structures: PASS.** Checked every pair for reframes.
- Slide 1 "That capital builds robots. Making one run inside your facility is a separate job." — this is a factual scope distinction (what the money buys vs. what it doesn't), not a contrastive-negation reframe. It corrects a real scope, which §6.1 explicitly permits.
- Slide 2 "The vendor governs its fleet. You still own the floor, the data, and the rules." — again a factual ownership split, not "it's not X it's Y." Legitimate.
- "the floor, the data, and the rules" is a rule-of-three, but it's three genuinely distinct things, not a punchy closer. Acceptable under §6.4 (use the number that's true).
- No cliffhanger pivots, no "This is" unveilings, no amputated slogan tags, no puffery.

**M — Metaphor: PASS.** "the join where edge inference meets your systems" — "join" is literal engineering vocabulary here (a physical/logical integration point), not a banned metaphor family. "reads a care facility floor" is literal perception description. No "think of it as," no journey/engine/bridge families.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics in body copy, no em dashes. Slide word counts: Slide 1 (26 words — borderline). Let me recount: "Robotics raised $55.8B in 2026, nearly double the prior record. That capital builds robots. Making one run inside your facility is a separate job." = 24 words. Slide 3 = 25. Slide 4 (excl. verify tag) = 28 — **recount:** "Navi reads a care facility floor on-device: a resident who has fallen, a blocked corridor, a medication cue. It decides locally, with no cloud round-trip." = 26 words. This nudges over the ~25 cap. Flagging as improvable, not a FAIL — the spec says "~25" and design overlays carry some of the load; trim to be safe (see note).

**E — Evidence: PASS.** Every ledger-sourced number traces correctly:
- $55.8B robotics 2026 YTD, nearly double prior record → E45, quoted exactly, correct scope (not conflated with the $8.7B humanoid figure).
- Robot-as-a-Service / fleet management, maintenance, 24/7 support → E51, accurate.
- All Navi specifics carry no ledger claim and are flagged [verify] on Slides 4 and 5. The Evidence-used section is explicit that no ledger figure is claimed about Navi. Correctly handled.

**O — One thing: PASS.** The post argues: the integration layer between a robot and a running environment is engineering Xavor already ships. One idea, matches the slot, ladders to the big idea (the seam nobody sells).

**L1 — Interchangeability: PASS.** Swap Navi for a generic robot and the copy breaks — "a resident who has fallen, a blocked corridor, a medication cue," "the facility's alerting and scheduling systems" are Navi-and-eldercare specific. Not generic.

**L2 — CTO respect: PASS.** Reads like a peer showing built work. "It decides locally, with no cloud round-trip" is the kind of engineering specific a technical executive respects. No vendor deference.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment: Slide 2–3, that RaaS governs the fleet but the floor, the data, and the rules stay with the buyer, and the integration between those two sides is a job no robot vendor sells. A robotics-shopping ops leader assumes the RaaS bundle covers the floor. This names the gap.

**R — Rhythm/human: PASS.** Varied sentence lengths, real transitions, caption opens on a hard fact without throat-clearing, CTA is the slot's required register. Not metronome.

## One improvable weakness
Slide 4 runs ~26 words, just over the cap. Trim to pull it clearly under 25: e.g. "Navi reads a care facility floor on-device: a fallen resident, a blocked corridor, a medication cue. It decides locally, no cloud round-trip." (22 words). Recommended before publish, but not a FAIL.

Reviewer must confirm both [verify] flags against the Navi corpus before this ships.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["Slide 4: Navi on-device perception and no-cloud-inference specifics (fall detection, blocked corridor, medication cue) — confirm against Navi corpus", "Slide 5: Navi embedded integrations (alerting/scheduling) and single-policy/single-audit-log fleet-governance posture — confirm against Navi corpus"],
 "edit_notes": ""}
```