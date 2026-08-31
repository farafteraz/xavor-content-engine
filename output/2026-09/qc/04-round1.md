# Editor's memo

**Overall verdict: FAIL** — on a structure violation (S).

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "manage," "owner," "accountable," "split" are all clean.

**S — Structures: FAIL.** Two contrastive-negation hits.
- Caption: "That's not a budget problem. It's a missing job." This is the §6.1 not-X-it's-Y reframe across sentence boundaries, the exact "Most teams think they have a hiring problem. They have a standards problem." pattern named in the spec. It is not a factual correction of a number, date, name, or scope, so it is not exempt.
- The angle line itself uses the same shape implicitly, but the caption is the clear hit. One clear hit fails the check.

**M — Metaphor: PASS.** No analogies, setups, or metaphor verbs. "does the work" is in the design note, not body copy, and reads literally.

**F — Formatting: PASS on the bans that matter to body copy.** No emojis, hashtags, exclamations, em dashes, caps, italics. Note: the draft carries bold on structural labels ("Image copy," "Supporting line," etc.) — these are production scaffolding/labels, not body copy, so not a formatting fail. Word count fine. Static format, no slide count.

**E — Evidence: PASS.** Two claims, both traced.
- 52% no dedicated owner + four-way split → [E23], stated exactly. Good.
- 98% manage AI spend → [E22]. This figure is CONFLICT-marked in the ledger (31% vs 63% base year), but the conflict is in the *base-year comparison*, not the 98% headline, which Week 4 reconciles. The draft states 98% alone with no dangling "up from X" comparison, which correctly sidesteps the unreconciled part. The evidence note explicitly confirms no E22 breakdown was merged into E23's split. Denominators are kept separate. Clean.

**O — One thing: PASS.** The post argues: nobody owns AI cost. One idea, no "and." Matches the slot angle (N4, N3 territory) and ladders to the operating gap.

**L1 — Interchangeability: PASS.** The claim is specific to AI cost ownership and the FinOps population. Swap "AI spend" for "cloud spend" and the 52%/98% figures break — they're AI-specific survey numbers. Not generic.

**L2 — CTO respect: PASS.** No wince. The framing (largest new line item, nobody answers for it) is the kind of thing a CTO defending Q4 budget actually feels.

**L3 — Cognitive depth: PASS, narrowly.** The "I hadn't considered that" lands on "It's a missing job" — reframing an unowned cost line as an absent role rather than a budget overrun. That is the intended discomfort. The problem is the depth is delivered *through* the banned structure, which is why S fails while L3 passes on substance.

**R — Rhythm/human: PASS.** Reads like speech, varied lengths, CTA lands in the right register. The caption's two-sentence snap is the only weak spot, and it's the same spot S flags.

## Edit notes

The insight is right and the evidence is clean. The only real problem is that the payload sentence is built on a banned reframe. Fix the caption and keep everything else.

1. **Caption, kill the "not X, it's Y."** Replace "That's not a budget problem. It's a missing job." with a direct positive claim that states the missing-role idea without the negation. Something like: "The largest new line item on the budget has no one whose job is to answer for it." Or: "Nobody's job description says they own it." State the absent role directly; don't set up "budget problem" to knock it down.

2. **Check the new caption sentence doesn't reintroduce a reframe** — no "isn't a budget line, it's a role" either. Lead with the role gap as the subject.

3. Everything else stays. E23/E22 handling is correct, denominators are separated, the design note and CTA are fine. This is a one-sentence fix, not a rewrite.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Caption contains a §6.1 contrastive-negation reframe across sentence boundaries: 'That's not a budget problem. It's a missing job.' This is not a factual correction of a number/date/name/scope, so it is not exempt. Replace it with a direct positive statement of the missing-role idea, e.g. 'The largest new line item on the budget has no one whose job is to answer for it.' or 'Nobody's job description says they own it.' Do not reintroduce any not-X-it's-Y shape (avoid 'isn't a budget line, it's a role'). Lead with the role gap as the subject. Everything else passes: E23/E22 evidence is clean, denominators are correctly separated, the 98% is stated without the unreconciled base-year comparison, the CTA and design note are correct. One-sentence fix only."}
```