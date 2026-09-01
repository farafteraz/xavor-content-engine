# Editor's memo — Post 2 (carousel, N1)

**Overall verdict: PASS (with one flagged item for human sign-off).**

This is a clean, disciplined draft. The writer caught a real defect in the slot spec (the "four blockers" claim) and handled it correctly: flagged it, refused to fabricate a fourth, and wrote to the evidence-correct three. That is exactly the behavior the evidence check is meant to reward. The verify flag must go to a human, but it does not fail the draft — the copy that ships is evidence-true.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Evaluation," "governance," "reliability," "escalation path," "decision boundary," "engineering scope" are all precise technical usage, not filler. No "crucial/critical/leverage/robust/seamless" hiding anywhere.

**S — Structures: PASS.** Checked every sentence pair for reframes. "They don't all die the same death" (slide 1) is a plain assertion, not a contrastive negation. "a specific engineering scope, not a dead end" (slide 5) reads as a candidate reframe, but it corrects the exact false belief the post is built to correct (the "written off as not ready" verdict) with a specific reclassification, and it lands on the positive claim first. It's allowed. No triple bursts, no rule-of-three closer, no cliffhanger pivot, no "This is" unveiling, no slogan tags, no puffery. The three-blocker structure is content, not a rule-of-three rhetorical flourish.

**M — Metaphor: PASS.** "the same death" / "the biggest killer" / "die" is light personification, normal business speech, well under any analogy budget and not a banned family (no journey/engine/battlefield extended metaphor). No banned setups or metaphor verbs. Design note explicitly bans metaphor icons — good.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Bold appears only on slide labels and structural headers ("Caption," "Copy"), not in body copy — acceptable as production scaffolding. Slide word counts all under 25 (slide 2 is the longest at ~24). Sentence case throughout.

**E — Evidence: PASS.** Every figure traces:
- 88% pilots fail → E17. ✓
- 64/57/51 blocker breakdown → E17. ✓ And critically, the writer kept these on E17's own denominator (share of *failures*) and did not merge them with the 88% or the 22.8%.
- 22.8% deployed and meeting ROI → E19, correctly attributed to HyperFRAME's 544-enterprise base, explicitly walled off with "Separately" so it does not fuse into a composite with E17's 88%. This is the exact merge-trap the rubric warns about, and the writer defused it deliberately.
- 5.1 months payback → E21. ✓
- The overlap note (blockers sum past 88% because failures overlap) is honest and prevents a false composite.
No invented specifics. The one CONFLICT-adjacent risk (merging two surveys) was actively avoided.

**O — One thing: PASS.** The post argues: a stalled pilot is one of three diagnosable failure classes, not a generic "not ready." One idea, ladders cleanly to the big idea (the operator's gap made diagnosable) and matches the slot job.

**L1 — Interchangeability: PASS.** Swap "agent pilots" for another technology and the copy breaks — the blockers (evaluation pipeline, decision boundary/escalation/owner, messy-input failure modes) are specific to agentic deployment. Not generic.

**L2 — CTO respect: PASS.** No wince. The demo-vs-production framing on slides 2–4 is how engineers actually talk about why pilots die.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" lands on slide 5: the reader stops treating dead pilots as one undifferentiated pile and realizes each maps to a distinct, fixable scope. That's the reclassification the slot job asks for.

**R — Rhythm/human: PASS.** Varied lengths, sounds like speech, opens on a hard fact with no throat-clearing, CTA in register. Slides 2–4 share a parallel structure by design (descending count), which is deliberate scaffolding, not metronome monotony.

## One improvable weakness (non-blocking)

Slide 5's "The ones that shipped paid back in 5.1 months" is the weakest line — the payback figure is true but slightly bolted on to a slide whose real job is the reclassification. Consider whether the 5.1-month proof earns its place or dilutes the diagnostic payoff. Optional.

## Human sign-off required

The slot JSON says "four blockers"; the evidence supports three. The writer correctly wrote three. A human must reconcile the slot spec before publish — this is a spec defect, not a draft defect.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["Slot JSON specifies 'four blockers' but E17/E18/E19 support only three (evaluation 64%, governance 57%, reliability 51%). Draft correctly wrote three. Human must fix the slot spec's 'four' before publish."],
 "edit_notes": ""}
```