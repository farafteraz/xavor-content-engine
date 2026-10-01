# Editor's Memo — Post 6 (explainer reel)

**Overall verdict: PASS**

The draft does the one hard thing this slot needs: it reframes a breach the CISO filed as a platform failure into a handoff failure, and it does it with the actual E22 numbers intact and correctly attributed. The rhythm reads like speech, not staccato hype, and the cognitive turn lands.

---

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Platform," "control plane," "governed system," "handoff" are all precise and allowed. No filler "crucial/critical/significant."

**S — Structures: PASS.** The dangerous one here is contrastive negation, because the whole piece pivots on "not inside, but between." I checked each instance:
- Frame 3: "Neither failure lives inside Salesforce, or Snowflake, or ServiceNow." / Frame 4: "Both failures live in the handoff." This is a correction of a specific factual claim about *where* a breach occurs — a scope/location correction, which §6.1 explicitly permits ("allowed ONLY to correct a specific fact, number, date, name, or scope"). It is not a rhetorical reframe simulating insight; it is the literal argument.
- Frame 5: "The breach you blamed on a platform happened between platforms." Same — a factual relocation, not a "not X, it's Y" slogan.
No triple bursts, no rule-of-three closer, no cliffhanger pivots, no "This is" unveiling, no slogan tags, no puffery, no meta commentary. Note the list in Frame 3 ("Salesforce, or Snowflake, or ServiceNow") is three named systems used as specifics, not a rhetorical triple — fine.

**M — Metaphor: PASS.** No analogies, no banned setups or verbs. "Carries data," "slips out," "walks in" are literal-enough physical verbs describing data movement, not abstract-work metaphors. Reel is under 800 words; zero analogies is correct.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Longest frame (Frame 4) is 32 words — but the §9 25-word cap is a carousel spec; this is an explainer reel, which §9 specs as "6–8 frames, each frame one line of VO/on-screen text" with no hard word cap. Seven frames, each a tight line. Compliant.

**E — Evidence: PASS, and this is the check I pushed hardest on.** Every number — 88.4%, 50.1%, 49.6%, "past twelve months" — traces to E22 and only E22. The author did not merge E22 with E16, E17, or E18 (the easy drift would have been to blend the breach rate with a deployment or audit stat). The base population is kept honest: 50.1% and 49.6% are stated as the two most common breach types *among the breached*, exactly as the ledger frames them, not recast as percentages of all enterprises. The "Evidence used" note explicitly confirms the breakdown is kept as a breakdown of the same statistic. No invented figures. The named platforms (Salesforce, Snowflake, ServiceNow) are real and supported across E4, E7, E9, E52.

**O — One thing: PASS.** In one sentence: agent breaches happen in the handoff between governed systems, not inside any one platform. No "and." Matches the slot job exactly and ladders straight to the big idea (the seam).

**L1 — Interchangeability: PASS.** Swap the platforms and the piece breaks, which is what we want — the argument depends on there being multiple separately-governed estates with gaps between them. The core claim ("the breach happened between platforms") is not generic; it only works for the specific multi-platform agent reality.

**L2 — CTO respect: PASS.** A CISO would not wince. The numbers are real, the mechanism (policy stops at the vendor edge) is technically true, and it doesn't disparage any vendor — it says each governs its own estate well. That earns trust.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is Frame 5: "The breach you blamed on a platform happened between platforms." That relocation of blame from a product to a seam is the non-obvious turn.

**R — Rhythm/human: PASS.** Sentence lengths vary (Frame 2 is three short beats, Frame 4 runs long and flowing). Opens cold on the stat with no throat-clearing. The CTA is the specified line and lands naturally after Frame 6 sets it up. Does not read as an AI imitating punchiness.

---

## One improvable weakness (non-blocking)

Frame 2's "Hit 50.1% of them / Hit 49.6%" repeats "hit" back to back and leans slightly staccato against the rest of the reel. If a rewrite happens for other reasons, vary the second verb. Not a FAIL — the rest of the piece carries enough flow that this reads as emphasis, not metronome.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```