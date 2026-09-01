# Editor's memo

## Overall verdict: FAIL

The draft is clean and well built, but it fails the slot on evidence scope and misstates the slot's own angle. The slot commits to "four blockers," the draft delivers three. That is not a style nit; it changes the diagnostic the reader is supposed to run against their own pilots.

## Per-check results

**V — Vocabulary: PASS**
Scanned word by word. No banned terms. "Mission-critical," "leverage," "seamless," etc. all absent.

**S — Structures: PASS (one thing to watch)**
No reframes, no triple bursts, no rule-of-three closer, no cliffhanger pivot, no "This is" unveiling.
"They don't all die the same death. Three blockers." reads close to setup-but it states a positive fact and follows with the count, not a negate. Allowed.
"the failure stops being 'not ready'" is a correction of a specific mislabel, not a contrastive reframe. Allowed.

**M — Metaphor: PASS**
"kills the most," "the biggest killer," "die the same death" are literal-register mortality framing on pilots, not a banned metaphor family (journey, engine, battlefield, etc.). No "think of it as," no metaphor verbs from §7. Design note explicitly bans metaphor icons. Fine.

**F — Formatting: PASS on body**
No emojis, hashtags, exclamations, em dashes, or ALL CAPS in slide copy. The bold on "Slide 1:" labels is scaffolding, not body copy, and the headings are sentence case. Slide word counts all under 25 (slide 5 is the longest at ~40 words across three sentences — recount below).
Correction: slide 5 runs "Sort your stalled pilots into these three and the failure stops being 'not ready.' Each one is a specific engineering scope. The pilots that shipped paid back in a median of 5.1 months." That is roughly 41 words, over the 25-word cap. **F FAILS on slide 5.**

**E — Evidence: FAIL**
The three numbers (88%, 64/57/51, 5.1 months) all trace cleanly to E17 and E21, and the draft honestly notes the 64/57/51 overlap rather than fabricating a composite. That part is disciplined.
The failure is scope, not fabrication. The slot's angle names "four blockers." E17 lists exactly three (evaluation gaps 64%, governance friction 57%, model reliability 51%). There is no fourth blocker anywhere in E17, E18, or E19. So either the slot's "four" is wrong and the draft silently corrected it to three without flagging the discrepancy, or a fourth blocker exists and is missing. Given the ledger, three is correct and four is unsupported. The draft should not quietly diverge from its own slot spec without a [verify] flag raising the mismatch. Additionally, **E19 is listed as slot evidence and goes entirely unused** — the 22.8% deployed-and-meeting-ROI figure (HyperFRAME, 544 enterprises) is never engaged. Not a fabrication, but the slot assigned it and the draft dropped it.

**O — One thing: PASS**
Argues exactly one idea: each blocker kills a distinct class of pilot, so a VP can diagnose which one killed each of theirs. Ladders to the big idea (the operator's gap is fixable engineering scope). Good.

**L1 — Interchangeability: PASS**
Swap "agent pilots" for "RPA pilots" and the 64/57/51 breakdown and the evaluation-pipeline detail stop being true. The specifics (demo-to-production, decision boundary, escalation path) are agent-specific. Holds.

**L2 — CTO respect: PASS**
Concrete, numeric, non-vendor. A VP of Engineering would respect the diagnostic framing.

**L3 — Cognitive depth: PASS**
The moment lands: "the failure stops being 'not ready.' Each one is a specific engineering scope." That reframes an undifferentiated write-off into a per-blocker diagnosis. That is the "I hadn't considered that."

**R — Rhythm/human: PASS**
Varied lengths, real speech cadence, no throat-clearing, CTA lands in register. Slide 4's "broke on the messy ones production actually sends" reads human.

## Edit notes

1. **Resolve the three-vs-four blocker contradiction (E, primary).** The slot angle says "four blockers," the ledger (E17) supports only three: evaluation gaps 64%, governance friction 57%, model reliability 51%. The draft chose three, which is correct against evidence — but it must not silently override the slot. Either (a) confirm the slot spec is wrong and proceed with three, adding a `verify_flag` so the human reviewer signs off on the deviation, or (b) if a fourth blocker is intended, it must trace to a ledger entry, and none exists. Recommend proceeding with three and flagging. Update the draft's own top-line "**Angle:**" note (it currently says "three blockers" while the slot JSON says "four") so the mismatch is explicit for the reviewer, not buried.

2. **Cut slide 5 to under 25 words (F).** Current: 41 words. Drop the middle sentence or the payback tail. Suggested rewrite (~24 words): "Sort your stalled pilots into these three and the failure stops being 'not ready.' Each one is a specific engineering scope, and the ones that shipped paid back in a median of 5.1 months." — that is still ~34, so cut harder. Tighter: "Sorted into these three, each stalled pilot is a specific engineering scope, not a dead end. The ones that shipped paid back in 5.1 months." (~24 words). Confirm final count is ≤25.

3. **Use or drop E19 deliberately.** The slot assigned E19 (only 22.8% of AI projects deployed and meeting ROI, HyperFRAME, 544 enterprises). It is unused. Either work it into slide 1 as a corroborating scale figure (distinct denominator from the 88% — do not merge them into a composite, they measure different things) or note explicitly in "Evidence used" why it was left out. Do not leave assigned evidence silently dropped.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "FAIL", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["Slot angle specifies FOUR blockers between pilot and production; ledger E17 supports only THREE (evaluation gaps 64%, governance friction 57%, model reliability 51%). Confirm the slot spec should be corrected to three, or supply a ledger-backed fourth blocker.", "E19 (22.8% deployed-and-meeting-ROI, HyperFRAME 544 enterprises) was assigned to this slot but unused; confirm intentional."],
 "edit_notes": "1) Resolve the three-vs-four blocker contradiction: the slot angle says 'four blockers' but E17 supports only three. Proceed with three (correct against evidence) but do NOT override the slot silently — raise a verify flag for human sign-off and fix the draft's own top-line Angle note, which already inconsistently says 'three' while the slot JSON says 'four.' No fourth blocker exists in E17/E18/E19, so a fourth cannot be written without fabrication. 2) Slide 5 is ~41 words, over the 25-word cap. Cut to <=25, e.g. 'Sorted into these three, each stalled pilot is a specific engineering scope, not a dead end. The ones that shipped paid back in 5.1 months.' Recount to confirm <=25. 3) E19 was assigned to this slot and is unused. Either add it to slide 1 as a corroborating scale figure (keep its denominator separate from the 88% — do not merge into a composite claim) or state in 'Evidence used' why it was dropped. Do not leave assigned evidence silently unused."}
```