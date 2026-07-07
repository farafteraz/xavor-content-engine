# Editor's memo — Post 14 carousel

**Overall verdict: FAIL.** One mechanical violation on S (contrastive negation), and the caption plus slide 2 lean on the exact reframe structures the spec bans. The evidence and depth are solid; the fix is structural, not conceptual.

## Per-check

**V — Vocabulary: PASS.** Scanned against §5. "revenue growth," "integrated," "workflow," "engineering," "governance" are all clean. No banned filler. "operate the ones you already have" is fine.

**S — Structures: FAIL.** Multiple contrastive-negation hits, the banned pattern §6.1:
- Caption: "The gap between a pilot and revenue isn't a better model. It's whether the AI is wired into how the business actually runs." — textbook "not X, it's Y." Not a factual correction; it's a rhetorical reframe.
- Slide 2: "Most transformation leads assume the winners simply bought better models. They didn't. They put the model where the work happens." — cross-sentence setup-and-negate / contrastive reframe (§6.1 sneaky form: "Most people think X..." then a pivot). Also brushes §6.8.
- Slide 5: "So the revenue question isn't which agent to pilot next. It's whether you can operate the ones you already have." — another "not X, it's Y." This one echoes the big-idea line, but it's still the banned structure in body copy.

That's three instances of the same prohibited move. Automatic FAIL.

**M — Metaphor: PASS.** "wired into," "sandbox," "put the model where the work happens" are all literal enough. "Sandbox" is standard technical usage for a pilot environment, not a metaphor family hit. No banned setups or verbs.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics in body, no em dashes. Slide word counts all under 25 (slide 4 is the longest at ~40 — recount below). Actually slide 4: "Integration is the unglamorous part: connecting the model to real data, giving it permission to act inside a workflow, and measuring what it moves. McKinsey found nearly two-thirds of enterprises experimented, fewer than 10% scaled to value." That's ~42 words. **This is an F FAIL too** — §9 caps carousel slides at ~25 words. Slide 4 nearly doubles it.

Correcting the check: **F — FAIL** (slide 4 over the 25-word cap).

**E — Evidence: PASS.** E69 supports 58% vs 15%, nearly 4x, Grant Thornton 2026 — verbatim match. E52 supports "two-thirds experimented, fewer than 10% scaled to value" — matches. No invented figures, no conflict-marked stats stated as single numbers. Clean.

**O — One thing: PASS.** The post argues one thing: integrated AI, not piloted AI, is what correlates with revenue growth. Matches the slot angle and ladders to the operability gap.

**L1 — Interchangeability: PASS.** The 58/15 gap and the pilot-vs-integration distinction are specific to AI deployment; you can't swap in another technology and keep the sentence true.

**L2 — CTO respect: PASS.** No wince. The argument respects a transformation lead who's already past demos.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" lands on slide 3: a pilot "can be impressive and still change nothing" because it has no live data, no downstream system, no accountable owner. That reframes the pilot as structurally incapable of producing revenue, not just immature. Good.

**R — Rhythm: PASS with a note.** Reads like speech, varied lengths, CTA lands. The one weakness: slides 2 and 5 both run the same rhetorical shape, so the deck feels repetitive even before you notice it's the banned structure. Fixing S will fix this.

## Edit notes

The insight is right and the evidence is clean. Every failure is the same tic: you keep reaching for "not X, it's Y" to create emphasis. Convert each to a direct positive claim.

1. **Caption.** Replace the first two sentences. Cut "The gap between a pilot and revenue isn't a better model. It's whether the AI is wired into..." Write it straight: "Revenue growth tracks with one thing, and it isn't model quality. It's whether the AI runs inside how the business actually operates." — no, still a reframe. Do this instead: "Integrated AI runs inside how the business operates. That placement, not model quality, is what shows up in revenue." Then keep the Grant Thornton sentence.

2. **Slide 2.** Kill the "Most leads assume... They didn't..." setup-and-negate entirely. State the causal claim directly: "The winners didn't buy better models. They put the model where the work happens, on live data with a workflow to act on." If you want to avoid even the mild negation, open with the positive: "The winners put the model where the work happens: live data, a real workflow, an owned outcome. Model quality was never the variable."

3. **Slide 5.** Rewrite the reframe. Direct version: "So the revenue question is operational. Can you run the agents you already bought, on real data, with someone accountable? That work is engineering and governance, not another demo." Drop "isn't which agent to pilot next / it's whether."

4. **Slide 4 (F fail).** Cut to ~25 words. Split the McKinsey stat into its own beat or compress: "Integration is the unglamorous part: connect the model to real data, let it act inside a workflow, measure what it moves." Then move the McKinsey figure to a trimmed line or fold one clause. If you keep both, this becomes two slides (you have room — deck can run 6, this splits cleanly).

5. After edits, reread slides 2 and 5 back to back to confirm they no longer share the same rhetorical shape.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Three contrastive-negation violations (§6.1) must be converted to direct positive claims. (1) Caption: cut 'The gap... isn't a better model. It's whether...' — rewrite as 'Integrated AI runs inside how the business operates. That placement, not model quality, is what shows up in revenue.' then keep the Grant Thornton sentence. (2) Slide 2: cut the 'Most leads assume... They didn't...' setup-and-negate; state it straight: 'The winners put the model where the work happens: live data, a real workflow, an owned outcome. Model quality was never the variable.' (3) Slide 5: cut 'isn't which agent to pilot next. It's whether...'; write 'So the revenue question is operational. Can you run the agents you already bought, on real data, with someone accountable? That work is engineering and governance, not another demo.' (4) F FAIL: Slide 4 runs ~42 words, over the 25-word cap. Compress to 'Integration is the unglamorous part: connect the model to real data, let it act inside a workflow, measure what it moves.' and move the McKinsey stat (two-thirds experimented, under 10% scaled) to its own slide or a trimmed line — deck can expand to a clean 6-7 slides. (5) After edits, confirm slides 2 and 5 no longer share the same rhetorical shape. Evidence, one-thing, and depth all pass; do not touch the argument."}
```