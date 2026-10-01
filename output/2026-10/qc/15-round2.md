# Editor's Memo — Post 15

**Overall verdict: FAIL.**

The draft is specific, well-sourced, and lands the month's idea. But Slide 1 opens on a contrastive-negation structure that the spec bans outright, and there's a second cross-sentence reframe in the caption. These are mechanical FAILs on S.

---

## Per-check results

**V — Vocabulary: PASS.** Scanned for banned terms. "estate," "posture," "control plane," "runtime," "RBAC," "tool call" are all technical/precision terms, not banned. No "seamless" (note: "seam" is the literal noun, not the banned adverb). No leverage/robust/scalable/optimize/etc. Clean.

**S — Structures: FAIL.** Two cross-sentence contrastive-negation hits.

- Caption: "Every platform governs its own estate well. None governs its neighbor." This is the "X. Not X." reframe across sentence boundaries (§6.1). It is not correcting a specific fact, number, date, or scope — it's the rhetorical setup-and-pivot the spec names explicitly.
- Slide 1: "Three vendors each promise governed AI. Each stops at its own edge." Same pattern — assert, then negate across the sentence boundary to manufacture tension. Banned (§6.1).
- Slide 2: "Each governed its own estate well. None could see into the others." A third instance of the identical construction. Three repetitions of the same banned move is the draft's spine, not an accident.

The whole piece leans on one rhetorical trick repeated three times. That is exactly what §6.1 targets.

**M — Metaphor: PASS (borderline).** No banned setups or metaphor verbs. "The seam" is the month's governing term and is used literally throughout (the space between platforms), not as a decorative analogy. "where accountability disappears" is plain language, not a metaphor family hit. Acceptable.

**F — Formatting: PASS on body copy.** No emojis, hashtags, exclamations, em dashes, or caps in the slide copy or caption. The bold on **Slide 1:** labels and the **Angle:** header is scaffolding/labeling, not body copy, and is standard in these slot drafts. Slide word counts all under 25 (longest is Slide 2 at ~45 words — **this exceeds 25 and is a secondary issue, see below**). Correction: Slide 2 runs well over the ≤25-word cap.

Re-counting Slide 2: "A regulated estate runs agents on three platforms. Salesforce's Trusted Enterprise AI Harness governs its agents. ServiceNow's AI Control Tower governs its own. Unity Catalog logs every Databricks tool call. Each governed its own estate well. None could see into the others." — that is ~44 words. **F FAILs** on the carousel ≤25-words-per-slide rule (§9). Slide 3 (~40 words) and Slide 4 (~38 words) also exceed 25.

**E — Evidence: PASS.** E4, E7, E11 are all represented accurately: Harness as governance layer (E4), Control Tower as control plane (E7), Unity Catalog logging each tool call plus attached-Sources restriction (E11). No numbers are stated in-copy, so no denominator or conflict risk. E18 is correctly used as framing context only, not quoted as a figure. The author's note about reframing from a past-tense client engagement to present-tense method is the right call and removes the need for a [verify] flag. No invented specifics.

**O — One thing: PASS.** The post argues: closing the cross-platform governance seam is integration delivery work, not a product. One idea, matches the slot angle, ladders to the big idea.

**L1 — Interchangeability: PASS.** Swap the three named platforms and the copy breaks — the Harness/Control Tower/Unity Catalog specifics (attached Sources, RBAC defaults, tool-call logging) are load-bearing. Not generic.

**L2 — CTO respect: PASS.** A CTO who has deployed across these three platforms would recognize the problem and the stance. No wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is Slide 5: "This posture lives in the space between the three products, so building it is integration work" — the reframe from "buy governance" to "the posture is unsellable because it lives in the gap no vendor owns." Delivered.

**R — Rhythm/human: BORDERLINE PASS.** The three-platform parallelism (Harness governs / Control Tower governs / Unity Catalog logs) reads as deliberate structure, acceptable in a carousel. But the repeated assert-then-negate couplet gives the whole thing a metronome feel across slides. Fixing S will also fix most of this.

---

## Edit notes

The idea is right and the evidence is clean. The problem is purely structural, and it's the same move three times. Fix it and the draft ships.

1. **Caption — kill the reframe.** Replace "Every platform governs its own estate well. None governs its neighbor." with a direct statement of scope: "Each enterprise platform governs the agents inside its own estate. The agent that crosses from Salesforce into ServiceNow into Databricks runs through three separate policies that were never reconciled." State the positive fact; let the gap be visible without the X/not-X beat.

2. **Slide 1 — rewrite the opener off the reframe.** Cut "Three vendors each promise governed AI. Each stops at its own edge." Lead with the concrete scene instead: "An agent that starts in Salesforce, acts in ServiceNow, and reads from Databricks passes through three governance layers that never agreed on one rule. That gap is where the audit risk lives, and that gap is the work." One claim, no setup-and-negate.

3. **Slide 2 — cut to ≤25 words AND remove the third reframe.** Drop "Each governed its own estate well. None could see into the others." Compress to: "A regulated estate runs agents across three platforms. The Harness governs Salesforce's agents, the Control Tower governs ServiceNow's, Unity Catalog logs every Databricks tool call." (~24 words.) The isolation is now shown by naming three separate systems, not stated via negation.

4. **Slide 3 — trim to ≤25 words.** Tighten to: "A policy that holds inside Salesforce says nothing about what an agent may do once it reaches Databricks. The seam is where accountability disappears." (~24 words.)

5. **Slide 4 — trim to ≤25 words.** Tighten to: "So we configure all three to one standard: same access rules, same logging, same human-oversight points, written once and mapped into each platform." (~23 words.)

6. **Verify slide counts after rewrite.** Every slide must land at or under 25 words. Slides 1, 2, 3, 4 all currently breach it.

Do not add new rhetorical structure to replace the reframes — state the facts plainly. The specificity (attached Sources, RBAC defaults, three named control layers) already carries the piece.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Two mechanical fails: contrastive-negation reframes (S) repeated three times, and four slides over the 25-word cap (F). (1) Caption: cut 'Every platform governs its own estate well. None governs its neighbor.' Replace with a direct scope statement, e.g. 'Each enterprise platform governs the agents inside its own estate. The agent that crosses from Salesforce into ServiceNow into Databricks runs through three separate policies that were never reconciled.' (2) Slide 1: cut 'Three vendors each promise governed AI. Each stops at its own edge.' Lead with the concrete scene: 'An agent that starts in Salesforce, acts in ServiceNow, and reads from Databricks passes through three governance layers that never agreed on one rule. That gap is where the audit risk lives, and that gap is the work.' (3) Slide 2: drop 'Each governed its own estate well. None could see into the others.' and compress to ~24 words: 'A regulated estate runs agents across three platforms. The Harness governs Salesforce's agents, the Control Tower governs ServiceNow's, Unity Catalog logs every Databricks tool call.' (4) Slide 3: trim to ~24 words: 'A policy that holds inside Salesforce says nothing about what an agent may do once it reaches Databricks. The seam is where accountability disappears.' (5) Slide 4: trim to ~23 words: 'So we configure all three to one standard: same access rules, same logging, same human-oversight points, written once and mapped into each platform.' (6) Confirm every slide is at or under 25 words after rewriting. Do not introduce new rhetorical structure to replace the reframes; state facts plainly. Keep the E4/E7/E11 specifics and the Slide 5 insight intact."}
```