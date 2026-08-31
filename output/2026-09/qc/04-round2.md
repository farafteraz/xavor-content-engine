# Editor's Memo — Post 4 (static, 2026-09-04)

**Overall verdict: PASS.**

Clean, disciplined static. It says one uncomfortable thing, backs both numbers to the ledger correctly, and lands the CTA in register. No AI tells survive a close read.

## Per-check

**V — Vocabulary: PASS.** No banned words. "Manage," "owner," "spend," "accountability" are all plain. No leverage/optimize/scalable/etc.

**S — Structures: PASS.** I went hunting for the reframe, because "no single person answers for it" is the kind of place a contrastive negation hides. It doesn't. "Almost every finance team now manages AI spend. More than half of them can't tell you who owns it." — this is a genuine factual contrast (98% do X, but ownership is absent), not a rhetorical "not X but Y" reframe. It corrects the reader's likely assumption with a specific number, which §6.1 explicitly permits. No triple bursts, no rule-of-three closer, no "This is" unveiling, no slogan tags, no puffery, no meta.

**M — Metaphor: PASS.** Zero analogies. "The largest new line item" is literal finance language, not metaphor.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Bold appears only in structural labels ("Image copy," "Supporting line") which are production scaffolding, not body copy. Word count trivially under. No caps abuse (52%, 98% are figures).

**E — Evidence: PASS, and notably careful.** Two claims, both traced:
- 52% + four-way split → [E23], stated verbatim, correct population (FinOps Foundation respondents).
- 98% manage AI spend → [E22]. This is a CONFLICT-marked entry, and the draft handled it correctly: 98% is the reconciled top-line figure (not one of the disputed "up from" baselines), and the draft deliberately did not import any "up from 31%/63%" baseline that would have required picking a side. The "Evidence used" note explicitly states no E22 breakdown was merged into E23's split — exactly the composite-claim trap the rubric warns about, avoided.
- No number is attached to the wrong denominator: 98% is finance teams managing spend; 52% is respondents with no owner. Kept distinct.

**O — One thing: PASS.** The post argues: the largest new AI line item runs with no accountable owner in most enterprises. One sentence, no "and." Matches the slot angle exactly and ladders to the operating gap (the financial face of "we bought it vs. someone runs it, governed, with a number").

**L1 — Interchangeability: PASS.** You cannot swap the subject out — "AI spend" is load-bearing. Swap in "cloud spend" and the sentence collapses, because cloud FinOps ownership is mature and the 52% figure is specifically about AI cost being new and unowned. The novelty is the point.

**L2 — CTO respect: PASS.** A finance-literate CTO reads "the largest new line item has no one whose job is to answer for it" and feels the wince the slot's job asks for. No content-marketing shine.

**L3 — Cognitive depth: PASS.** The moment: "98% of finance teams now manage AI spend" followed by "no single person answers for it." The insight a CTO hadn't fully considered is that *managing* spend and *owning* spend have quietly diverged — near-universal management coexists with majority non-ownership. That gap is the "I hadn't considered that."

**R — Rhythm/human: PASS.** The caption reads aloud like speech: short, short, longer. Not metronomic, not staccato-punchy-everywhere. CTA grows from the stakes rather than bolting on.

## One improvable weakness (non-blocking)
The supporting line and the caption both carry the "splits four ways" detail and the "more than half / no single person" beat, so the static repeats itself across blocks. On a single image that's fine, but if space is tight, the supporting line could drop "The accountability for it splits four ways, and" and lead straight to "in more than half of companies no single person answers for it" — tighter, same punch. Optional.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```