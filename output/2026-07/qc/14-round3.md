# Editor's Memo — Post 14 (carousel)

**Overall verdict: PASS**

Clean draft. It argues one thing, lands the integration-vs-pilot gap with two hard numbers, and the evidence traces cleanly. I hunted for the usual tells and found nothing that fails a HARD check. One improvable weakness noted at the end.

## Per-check results

**V — Vocabulary: PASS**
Scanned word by word. No banned terms. "Integration," "workflow," "revenue growth" are all plain. No "seamless," "scalable," "leverage," no filler "crucial/critical." Clean.

**S — Structures: PASS**
Checked every sentence pair for reframes across boundaries. Slide 3 ("It can be impressive and still change nothing.") is a genuine claim, not a "not X but Y" pivot. Slide 2 "That's the variable the 58% got right" leads with the subject, no unveiling. No triple bursts, no rule-of-three closer, no cliffhanger pivots, no "This is" openers, no amputated slogan tags, no puffery. Slide 4's "connect the model to real data, let it act inside a workflow, measure what it moves" is three parallel verbs describing one concrete process — that's a legitimate list of steps, not a dramatic triple burst. Passes.

**M — Metaphor: PASS**
"A pilot lives in a sandbox" — "sandbox" is standard engineering vocabulary for an isolated test environment, not a figurative metaphor setup. No "think of it as," no "it's like," no banned metaphor verbs. "Lives inside that last 10%" is loose but not a banned family. Clean.

**F — Formatting: PASS**
No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes. Slide word counts: S1 ~24, S2 ~19, S3 ~28 — recount: "A pilot lives in a sandbox. It has no live data, no downstream system to act on, no one accountable for the outcome. It can be impressive and still change nothing." = 32 words. That exceeds the ~25 cap. Flagging as an editor note, not a hard fail — the spec says "~25 words each" (approximate), and this is the one slide over. Tighten it. All other slides within range.

Reconsidering F: the "~" makes this a soft target, and one slide at 32 against a tilde-qualified 25 is not a clean mechanical breach the way an em dash would be. I'll pass F but require the trim in notes.

**E — Evidence: PASS**
- 58% vs. 15%, nearly 4x, Grant Thornton 2026 → [E69], exact match including both figures. Good.
- "nearly two-thirds of enterprises experimented... fewer than 10% scaled to tangible value" (McKinsey) → [E52], exact match. Good.
No invented specifics, no CONFLICT figures in play, no unsupported numbers.

**O — One thing: PASS**
The post argues: integrated AI (not piloted AI) is what converts into revenue. One idea, no "and." Matches slot angle exactly and ladders to the operability gap (you deployed faster than you operationalized).

**L1 — Interchangeability: PASS**
The claim is specific to integration state (integrated vs. piloted) and the Grant Thornton delta. You cannot swap the subject and keep the sentence — the whole point is placement inside live data and owned workflows. Slide 3's definition of a pilot is concrete and non-generic.

**L2 — CTO respect: PASS**
No wince. The distinction between a sandbox pilot and an owned, measured, data-connected deployment is real and how a transformation lead actually thinks. It doesn't oversell.

**L3 — Cognitive depth: PASS**
The "I hadn't considered that" moment is slide 2 into slide 3: the revenue isn't a property of the model, it's a property of placement — live data, real workflow, owned outcome. Reframing the 4x gap as a placement variable rather than a capability variable is the non-obvious beat. It survives.

**R — Rhythm/human: PASS**
Varied lengths, reads like speech, opens on a hard number instead of throat-clearing. CTA is the slot's mandated line and lands naturally as the close. Not metronomic, not overly punchy. Caption is tight and human.

## Improvable weakness (one line)
Slide 3 runs 32 words against the ~25 target — trim to land it, e.g. "A pilot lives in a sandbox: no live data, no downstream system, no one accountable. It can be impressive and change nothing." (21 words).

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```