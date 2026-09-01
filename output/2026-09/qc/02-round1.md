# Editor's memo

## Overall verdict: FAIL

The draft is clean, well-paced, and mechanically strong on vocabulary, metaphor, and formatting. It fails on two counts: a mislabeled evidence claim (the angle promises "four blockers" but only three exist in the ledger, and the copy openly contradicts itself on the count), and a structural reframe in the caption and slide 5.

---

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Scope" used as a verb literally, fine. No filler crutches.

**S — Structures: FAIL.**
- Caption: "'Not ready' is what a stalled pilot looks like from the outside. From the inside, it's usually one of four specific failures." This is a cross-sentence contrastive reframe (outside appearance vs. inside reality — "on the surface X... actually Y"). It sets up a false surface reading to pivot. §6.1.
- Slide 5: "you didn't have a model problem. You had an engineering problem you can now scope." Textbook contrastive negation across sentences ("Most teams think they have a hiring problem. They have a standards problem." is the exact pattern named in §6.1). This is not a factual correction of a number/date/scope, so it is not the permitted exception.

**M — Metaphor: PASS.** No analogies, no banned setups or verbs. "Die the same death" / "the one that killed it" is a light personification but reads normal and isn't in the banned families. Acceptable.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes. Slide word counts all under 25 (slide 5 is the longest at ~45 words across two sentences — recount below).

Wait: slide 5 word count. "Sort your stalled pilots into those three and the pattern shows: you didn't have a model problem. You had an engineering problem you can now scope. The ones that shipped paid it back in a median of 5.1 months." That is ~46 words. **This exceeds the 25-word cap.** Slide 2 is ~40 words, slide 3 ~28, slide 4 ~30. Multiple slides break the ≤25-word carousel limit (§9, §4). **F — FAIL.**

**E — Evidence: FAIL.**
- The angle and slide 1 both claim "four blockers." The ledger (E17) lists exactly three: evaluation gaps 64%, governance friction 57%, model reliability 51%. There is no fourth blocker anywhere in E17, E18, or E19. Slides 2–4 then deliver only three. The draft even admits this: slide 5 says "Sort your stalled pilots into those three." The post argues four, ships three, and names three. This is an unsupported claim contradicted by its own copy.
- Note also E19 is listed in the slot's evidence array but never used, and it would have been the honest way to add a fourth data point (22.8% deployed and meeting ROI). Not a violation on its own, but it exposes that the "four" was never grounded.
- 5.1 months (E21): correctly supported.
- 88% and 64/57/51 (E17): correctly supported, and the overlap note is honest and correct.

**O — One thing: PASS (with the count caveat).** The post argues: a stalled pilot died from one identifiable blocker, and you can name which. Single idea, ladders to N1's "make the gap diagnosable." Good. But the "four vs three" defect undercuts the very spine, so this only passes conditional on the E fix.

**L1 — Interchangeability: PASS.** The percentages and the named failure modes (evaluation pipeline, decision boundary, escalation path, messy production inputs) are specific to agent pilots. Swapping the subject breaks the copy. Good.

**L2 — CTO respect: PASS.** The diagnostic framing (worked in a demo, no pipeline to prove it held) is the language of someone who has watched pilots die. A VP of Engineering would not wince.

**L3 — Cognitive depth: PASS.** The moment lands: "you didn't have a model problem. You had an engineering problem you can now scope." The reader reclassifies dead pilots from "not ready" to a specific, fixable blocker. That is the intended "I hadn't considered that." (The sentence delivering it must be rewritten to kill the reframe, but the insight itself is real.)

**R — Rhythm/human: PASS.** Varied lengths, reads like speech, opens on a hard fact with no throat-clearing, CTA lands naturally. Not metronomic. Good.

---

## Edit notes

1. **Fix the count. This is the priority.** The ledger supports three blockers, not four. Change the angle-in-copy and slide 1 from "four blockers" to "three blockers." Slide 1 becomes: "88% of agent pilots never reach production (Forrester/Anaconda). They don't all die the same way. Three blockers, and you can match each stalled pilot to the one that killed it." Keep slides 2–4 as the three. Slide 5's "those three" then agrees. (If a fourth is genuinely wanted, it must come from a real ledger entry — E19's 22.8% deployed-and-meeting-ROI is a different statistic and a different population, so do not fold it in as a fourth blocker; that would be an E fail of its own.)

2. **Kill the caption reframe.** Replace "'Not ready' is what a stalled pilot looks like from the outside. From the inside, it's usually one of four specific failures" with a direct statement. Suggested: "A stalled pilot gets written off as 'not ready.' Usually it's one of three specific failures, and you can name which one killed each of yours. Evaluation gaps kill the most."

3. **Kill the slide 5 reframe.** Remove the "you didn't have X, you had Y" construction. State the positive claim directly. Suggested rewrite (also trims to word limit): "Sort your stalled pilots into these three and the failure stops being 'not ready.' Each one is a specific engineering scope. The pilots that shipped paid back in a median of 5.1 months." Then check word count.

4. **Word count on every slide.** Slides 2, 3, 4, and 5 exceed ~25 words. Compress by cutting words, not by chopping into fragments. Slide 2 example under limit: "Evaluation gaps: 64% of failures. The agent worked in a demo, and no one built the pipeline to prove it held on real inputs. The biggest killer by far." (~30 — still over; cut further: drop "The biggest killer by far" since slide already says 64% is largest.) Target every slide at or under 25.

5. Leave the overlap note in the evidence section as-is; it is honest and correct.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "1) EVIDENCE: The ledger (E17) supports exactly three blockers (evaluation 64%, governance 57%, model reliability 51%), not four. The draft claims 'four blockers' in the angle and slide 1 but ships and names only three, and slide 5 contradicts itself by saying 'those three.' Change all references to three. Do NOT invent a fourth or fold in E19 (22.8% is a different statistic and population). 2) STRUCTURE: Remove the caption reframe ('from the outside... from the inside'); state directly, e.g. 'A stalled pilot gets written off as \"not ready.\" Usually it's one of three specific failures, and you can name which one killed each of yours. Evaluation gaps kill the most.' 3) STRUCTURE: Remove the slide 5 contrastive negation ('you didn't have a model problem. You had an engineering problem'). Replace with a direct positive claim, e.g. 'Sort your stalled pilots into these three and the failure stops being \"not ready.\" Each one is a specific engineering scope. The pilots that shipped paid back in a median of 5.1 months.' 4) FORMATTING: Slides 2, 3, 4, and 5 exceed the 25-word carousel cap. Compress by cutting words, not fragmenting. Get every slide to 25 or fewer. 5) Keep the evidence-overlap note as-is; it is correct."}
```