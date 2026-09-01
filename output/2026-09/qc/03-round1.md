# Editor's Memo — Post 3 (explainer reel, N3)

**Overall verdict: FAIL.** One hard structural violation in Frame 4 (contrastive negation / reframe). The rest of the draft is strong — the evidence is clean, the voice is disciplined, the cognitive turn lands — but the reframe is a black-and-white spec violation and the fix is trivial.

---

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "right-sized" is a literal financial term, not "optimize"; acceptable. No filler copulas — "gets funded," "grows," "has a name" are literal verbs.

**S — Structures: FAIL.** Frame 4: "The AI line isn't a value problem. It's an ownership problem." This is textbook contrastive negation (§6.1) across sentence boundaries — reject-half then assert-half. The spec permits contrast only to correct a specific fact, number, date, name, or scope; "value problem vs ownership problem" is a conceptual reframe, not a factual correction. FAIL.

Secondary flag, same family: Frame 2→3 leans on the setup-and-negate cadence ("So finance sees the number. Then someone asks who owns it. / 52% say no one does."). This one is closer to a legitimate reveal because the 52% is a real fact the reader needs, and it's not a "you'd think X, actually Y" negation. I'd let it stand, but it's worth watching in the rewrite so the fix to Frame 4 doesn't push the whole reel into a reframe rhythm.

**M — Metaphor: PASS.** No analogies, no banned setups or verbs. "the money leaks" / "the room goes quiet" (caption) are plain physical description of a real scene, not metaphor for abstract work. Clean.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes. Frame word counts all well under 25 (longest is Frame 6 at ~19). Bold appears only in the scaffolding labels (Angle:, Caption headers), not body copy. Fine.

**E — Evidence: PASS.** Every figure traces cleanly.
- 31% → 98% (Frame 1): E22, and the draft correctly uses the reconciled 2024 baseline (31% → 63% → 98%) rather than mis-stating "two years" as 63%. Good — this is exactly the CONFLICT the ledger warns about, and the writer handled it right.
- 52% / splits four ways (Frame 3): E23, verbatim.
- Self-funding through savings (Frame 5): E27, correctly applied — "gets funded by whatever it saves elsewhere."
No invented specifics, no composite claims, no denominator drift. The "token attribution" line in Frame 6 is Xavor's own scope, not a stat, so it needs no ledger support.

**O — One thing: PASS.** The post argues one thing: the AI cost line has no owner, and ownership is engineering work. Ladders directly to the big idea's cost layer and matches the slot job ("no owner rather than no value").

**L1 — Interchangeability: PASS.** Swap "AI spend" for "cloud spend" and Frame 6 breaks — token attribution mapped to team/product/BU is specific to the token-as-unit problem (E25). The 98%/52% pairing is specific to this survey. Not swappable.

**L2 — CTO respect: PASS.** Reads like a peer stating a hard finance fact, not content marketing. The "goes quiet" caption is confident without being cute.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is Frame 5: an unowned line self-funds from its own savings, so it never gets right-sized — it only grows. That reframes the CFO's problem from "is this worth it" to "nothing is metering this." Genuinely non-obvious.

**R — Rhythm/human: PASS (with one note).** Varied lengths, reads like speech, CTA lands naturally out of the ownership thread. Not metronomic. The only risk is that fixing Frame 4 could introduce staccato; see edit note.

---

## Edit notes

Single fix required.

**Frame 4** currently: "That's the tell. The AI line isn't a value problem. It's an ownership problem." — This is a banned contrastive negation. Delete the rejected half and state the positive claim directly. Replace with something like:

> "That's the tell. The problem was never whether the AI is worth it. It's that no one is metering what it costs."

That still trips the reframe rule ("never whether X / it's that Y"). Go further — cut the negation entirely and assert only the positive:

> "That's the tell. The spend has no owner, so no one is accountable for what it costs."

Or, keeping it tighter to the reel's logic:

> "That's the tell. A line no one owns is a line no one meters."

Any of these states the ownership claim without rejecting a strawman "value problem." Do not reintroduce "value" as a foil anywhere — the slot's whole job is to make the CTO realize the line has "no owner rather than no value," so you can name value once as the thing they've been debating, but never in a not-X-but-Y construction. Cleanest: assert the ownership fact directly and let the reader supply the contrast in their own head.

Recheck after the swap that Frames 4→5 don't read as three consecutive short assertions in a row (metronome risk). If they do, let Frame 5's longer sentence carry more of the line, which it already does.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Fix Frame 4 only. It currently reads 'The AI line isn't a value problem. It's an ownership problem.' — a banned contrastive negation (§6.1) across sentence boundaries. This is not a factual correction, so it's not permitted. Delete the rejected 'value problem' half and state the ownership claim directly. Suggested replacement: 'That's the tell. The spend has no owner, so no one is accountable for what it costs.' or 'That's the tell. A line no one owns is a line no one meters.' Do not reintroduce 'value' as a foil in any not-X-but-Y form anywhere in the reel; let the reader supply the contrast. After the swap, verify Frames 4-5 don't become three consecutive short assertions (metronome risk); Frame 5's longer sentence should carry the line. Everything else passes — evidence, one-thing, depth, and voice are all clean; the 31%/63%/98% baseline conflict was handled correctly."}
```