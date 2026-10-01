# Editor's memo — Post 12 (video feature)

## Overall verdict: PASS

A rare clean one. The draft does the slot's job: it shows engineers doing the cross-platform configuration work, names the three real control planes, and lands the thesis without sloganeering. Let me walk the checks.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Posture," "scope," "policy," "control plane," "audit trail" are all precise technical usage, not filler. No "seamless," "robust," "scalable," "leverage," etc.

**S — Structures: PASS.** Checked every sentence pair for reframes.
- "Not a second standard bolted next to the first" (Beat 3) — tested as a contrastive negation. It survives because it corrects a specific scope claim: it clarifies that the ServiceNow policy is the same object, not a parallel one. This is the permitted use ("to correct a specific fact, number, date, name, or scope"). Marginal but clean.
- "Three platforms. One posture." (Beat 5) — tested as a dramatic triple burst / amputated slogan. It is two short VO fragments inside spoken video dialogue, immediately followed by a full explanatory sentence ("When an auditor asks the same question..."). In a video script this reads as natural spoken cadence, not a slogan tag. Acceptable.
- "One posture. Every platform." (Beat 7, on-screen text) — this is on-screen title card text, not body prose. Title cards are allowed compression. Not a violation.
- "No vendor sells the thing that holds across all of them. That's integration work." — checked for "This is" unveiling and setup-and-negate. It's neither; it states a claim then names it directly. Fine.

**M — Metaphor: PASS.** No analogies, no banned setups, no metaphor verbs. "Steps out of line" is idiomatic plain speech, not a metaphor family hit. Literal verbs throughout: set, map, restrict, scope, logged, compare.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Bold appears only in scaffolding labels (Beat headers, "Runtime," "Angle," "Caption") — production structure, not body copy. VO lines and caption are clean. This is a video script, so word-count caps don't apply; runtime ~85s is within the 60–90s spec.

**E — Evidence: PASS.** Three claims, three ledger traces, all accurate to scope.
- Beat 2 Harness → E4. Correct; E4 is the Salesforce Trusted Enterprise AI Harness governance layer.
- Beat 3 Control Tower → E7. Correct; E7 names it the control plane for governing/auditing AI across the enterprise.
- Beat 4 Genie Agent restricted to attached Sources + tool-call logging → E11. Verbatim match to E11.
- "runs agents in five places" (Beat 1) — supported by the big-idea frame (five platforms) and E61 (average company runs 12 agents across platforms). Framed as a scenario, not a hard stat, so no drift.
- "a fine attached" (Beat 6) — gestures at E23/E24 without stating a number. Safe.
No invented figures, no CONFLICT figure stated as single, no merged denominators.

**O — One thing: PASS.** The post argues: Xavor's engineers set one governance posture across three real platforms, and that cross-platform integration is the work no vendor sells. One idea, ladders directly to the big idea's seam thesis and the slot's job ("work Xavor's engineers actually do, not a slide").

**L1 — Interchangeability: PASS.** You cannot swap the named platforms out. The whole piece depends on the Harness, the Control Tower, and Unity Catalog being three different vendors' control planes with the same policy mapped across them. Swap any one and the "when an auditor asks the same question in any of them, the answer matches" beat collapses. Specificity is load-bearing.

**L2 — CTO respect: PASS.** The "real work, no stock-footage gloss" framing and the concrete actions (restrict a Genie Agent to its attached Sources, show the tool-call log) read like people who have done it. A CTO would not wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment: "When an auditor asks the same question in any of them, the answer matches" (Beat 5). It reframes cross-platform governance from a feature-parity problem into an audit-consistency problem — the thing the CTO's five vendors each promise and none deliver jointly. That is the slot's intended insight, delivered in one line.

**R — Rhythm/human: PASS.** VO lines vary in length, sound like speech, and the on-camera Beat 6 line carries the human stance well. CTA grows naturally out of the settled final shot. No metronome, no throat-clearing, no assistant chatter.

## One improvable weakness (non-blocking)
Beat 1's "where things break" is the one slightly soft phrase — it's the only place the specificity dips to generic. If you reshoot or re-record, consider naming the failure concretely (an unattributed token, an agent reaching data it shouldn't, an audit answer that differs by platform) to match the precision of the later beats. Not required to ship.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```