# Editor's Memo — Post 7 (case-study carousel)

## Overall verdict: FAIL

The draft is close and mostly disciplined, but it contains a banned structure on Slide 5 (a "This is" unveiling) and a cross-sentence contrastive-negation setup on Slide 1/2 that the spec treats as a hard fail. Details below.

## Per-check results

**V — Vocabulary: PASS.** No banned words. "governance," "evaluation," "production," "access" are all literal and precise. No filler copulas ("wire that access," "get more projects," "design the evaluation" — all live verbs).

**S — Structures: FAIL.**
- Slide 5 opens with "**This is** why it matters at portfolio scale." — §6.6 bans sentences opening with "This is" as an unveiling. Direct hit. Lead with the subject.
- Slide 1 / Slide 2 form a contrastive-negation pair across the slide boundary: "Your agent pilot **didn't** stall on the model. It stalled on what the agent could see..." followed on Slide 2 by "88% of agent pilots never reach production... **None of those is a smarter model.**" This is the "Most teams think they have a hiring problem. They have a standards problem." pattern named in §6.1 — a negate-the-obvious reframe repeated twice (Slide 1 "didn't stall on the model," Slide 2 "None of those is a smarter model"). §6.1 permits contrast only to correct a specific fact, number, date, or scope. "The model" is a category, not a corrected figure, so this does not qualify. The doubling makes it worse.

**M — Metaphor: PASS.** "production stops being a wall" in the caption is a mild figurative touch but it's a dead-standard business phrase, not one of the banned families or setups, and it reads normal aloud. No "think of it as," no journey/engine/map. Clean.

**F — Formatting: PASS on the copy itself.** No emojis, hashtags, exclamations, em dashes, or ALL CAPS in body. Slide word counts all under 25 (highest is Slide 3 at ~40 words — recount below). Correction: Slide 3 runs ~42 words ("So we start where the pilot broke... before a single prompt runs"), Slide 4 runs ~38, Slide 2 ~35. **These exceed the ~25-word cap in §4 and §9.** Reclassifying F to **FAIL** — three slides breach the slide limit. The bold labels ("Slide 1:") are scaffolding, not body copy, so they don't count against the bold ban, but the word counts do.

**E — Evidence: PASS.** E14 (88%, blocker cluster) correctly attributed to Forrester/Anaconda. E16 (12x, Databricks) correct — note the ledger says "12x+"; "12x" is a fair rendering. E52 used for framing only, not quoted. No invented figures, no CONFLICT figure stated as single (E14 has no conflict). Good discipline.

**O — One thing: PASS.** The post argues exactly one idea: getting an agent to production is a data-access and evaluation-design job first, and that work is why governance-tooled programs ship more. Matches the slot angle and ladders to the operability gap.

**L1 — Interchangeability: PASS.** Swap Salesforce/ServiceNow for a generic "AI platform" and Slide 3–4 still hold specificity ("what data can the agent read at runtime, under what permissions, with what freshness"; "a scored gate the agent has to pass to ship"). The sequencing detail is not generic.

**L2 — CTO respect: PASS.** The runtime-permissions-and-freshness framing and the "scored gate to ship" language read like someone who has actually done the work. A VP of Engineering would not wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands on Slide 5: governance tooling is not overhead, it *enforces the access and evaluation work by default* — reframing governance as the mechanism that produces the 12x, not a compliance tax. That's the non-obvious turn.

**R — Rhythm/human: PASS, borderline.** Sentence lengths vary, transitions are real ("So we start," "Then we design"). Does not read metronome. The one weakness noted below.

## Edit notes

Three fixes required; the piece is otherwise shippable.

1. **Kill the "This is" opener on Slide 5.** Replace "This is why it matters at portfolio scale." Lead with the subject: e.g., "At portfolio scale the payoff compounds. Companies running AI governance tooling get 12x more projects into production (Databricks), because the tooling enforces the access and evaluation work by default."

2. **Remove the doubled contrastive negation (Slide 1 + Slide 2).** The "didn't stall on the model / none of those is a smarter model" reframe is banned. Rewrite Slide 1 to state the positive claim directly: e.g., "Your agent pilot stalled on what the agent could reach and how you decided it was working. Both are engineering problems, not model problems — " no: avoid the "not" pivot entirely. Use: "Your agent pilot stalled on two engineering problems: what the agent could see at runtime, and how you decided it was good enough." Then on Slide 2, drop the "None of those is a smarter model" sentence entirely and let the blocker cluster speak: "88% of agent pilots never reach production. The blockers cluster on evaluation gaps, insufficient tool and data access, and unclear success criteria (Forrester/Anaconda)."

3. **Cut Slides 2, 3, 4 to the ~25-word cap.** Compress by removing words, not by chopping voice.
   - Slide 3 target: "We start where the pilot broke. What data can the agent read at runtime, under what permissions, at what freshness. We wire and prove that access first."
   - Slide 4 target: "Then the evaluation the pilot never had: a written definition of a correct outcome, a test set of real cases, a scored gate to ship."
   - Recount every slide after editing.

The caption is fine and can stay as written.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "1) Slide 5: remove the banned 'This is why it matters' unveiling (§6.6); lead with the subject, e.g. 'At portfolio scale the payoff compounds. Companies running AI governance tooling get 12x more projects into production (Databricks), because the tooling enforces the access and evaluation work by default.' 2) Remove the doubled contrastive-negation reframe (§6.1): Slide 1 'didn't stall on the model' and Slide 2 'None of those is a smarter model.' Rewrite Slide 1 as a positive claim with no not/pivot, e.g. 'Your agent pilot stalled on two engineering problems: what the agent could see at runtime, and how you decided it was good enough.' On Slide 2 delete the sentence 'None of those is a smarter model.' entirely: 'The blockers cluster on evaluation gaps, insufficient tool and data access, and unclear success criteria (Forrester/Anaconda).' 3) Cut Slides 2, 3, and 4 to the ~25-word cap by removing words, not chopping voice. Slide 3 e.g. 'We start where the pilot broke. What data can the agent read at runtime, under what permissions, at what freshness. We wire and prove that access first.' Slide 4 e.g. 'Then the evaluation the pilot never had: a written definition of a correct outcome, a test set of real cases, a scored gate to ship.' Recount every slide after editing. Caption and evidence attribution are fine as written."}
```