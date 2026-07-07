# Editor's Memo — Post 14 (carousel)

## Overall verdict: FAIL

The draft is clean on mechanics and evidence, but it fails formatting on slide count (7 slides against a 5–6 cap) and — more seriously — it argues one thing too many. The slot allows exactly one angle: integration vs. piloting drives revenue. Slide 6 imports the month's operability-gap thesis ("run the agents you already bought") into a post that isn't authorized to make that turn. That's an O failure.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. "Integrated / integration" is the slot's own vocabulary, not banned. No hits on the §5 list. "Unglamorous" is fine. No filler crutches.

**S — Structures: FAIL.**
- Slide 2: "The winners put the model where the work happens... Model quality was never the variable." This is a setup-and-negate / contrastive negation across sentences — assert the positive, then knock down "model quality." The fix is to state what integration does without the negation.
- Slide 5: "Experimentation is common; integration is rare." Contrastive reframe (X is common, Y is rare) dressed as a closer. The two stats already say this; the tag restates it as a rhetorical pairing.
- Slide 3: "It can be impressive and still change nothing." Borderline setup-and-negate. Passable alone, but it stacks with the others.

The recurring move across slides 2, 3, and 5 is the same rhetorical shape: build a thing up, then negate. That pattern is exactly what §6 flags.

**M — Metaphor: PASS.** "Lives in a sandbox" is near a metaphor family but reads as literal industry usage (sandbox environment), not a decorative analogy. No banned setups or verbs. Let it stand.

**F — Formatting: FAIL.** Seven slides. Spec §9 caps carousel at 5–6 slides. No emojis, hashtags, exclamations, bold/italics/caps, or em dashes in body copy. Every slide is under 25 words. The only formatting failure is slide count, but it's a hard one.

**E — Evidence: PASS.** Both claims trace cleanly. Slide 1 / caption: 58% vs. 15%, nearly 4x → [E69], stated exactly as the ledger has it. Slide 5: two-thirds experimented, under 10% scaled → [E52], accurate. No invented specifics, no CONFLICT figures stated as single numbers. Grant Thornton and McKinsey both attributed. Clean.

**O — One thing: FAIL.** The post argues: integrated AI drives revenue where piloting doesn't — AND — the real question is whether you can operate the agents you already bought. That second clause (slide 6) is the month's big idea, not this slot's angle. The slot's job is to make a transformation lead see that integration, not piloting, separates revenue from stalled programs. Slide 6 changes the subject from "integration produces revenue" to "operability is the constraint." Pick one. This post owns the first.

**L1 — Interchangeability: PASS.** The 58/15 gap and the pilot-vs-integrated distinction are specific to AI deployment and can't be swapped for another technology without breaking. The pilot definition on slide 3 (no live data, no downstream system, no owner) is concrete.

**L2 — CTO respect: PASS.** No wince. The pilot anatomy on slide 3 and the "measure what it moves" line read like a peer who has shipped, not content marketing.

**L3 — Cognitive depth: PASS, narrowly.** The "I hadn't considered that" beat is slide 2's claim that placement, not model quality, is the revenue variable — reframed against the reader's likely instinct to keep upgrading the model. That earns the slot. Slide 3's definition of a pilot as something that "can be impressive and still change nothing" sharpens it. The insight survives even after you cut slide 6.

**R — Rhythm/human: PASS with a note.** Sentence lengths vary, transitions are real, it reads like speech. The one weakness: slides 2, 3, and 5 all lean on the same negate-the-obvious cadence, which starts to feel like a tic by slide 5. Fixing the S failures will also fix this.

## Edit notes

1. **Cut to six slides.** Remove slide 6 entirely. It smuggles the month's operability thesis ("run the agents you already bought... engineering and governance") into a post that is only allowed to argue integration-drives-revenue. Do not blend it in elsewhere; it's a different argument. That drops you to six slides (1–5 plus CTA), which is in spec.

2. **Fix the setup-and-negate on slide 2.** Replace "Model quality was never the variable" with a direct positive claim. Something like: "The revenue comes from placement: live data, a real workflow, an owned outcome. That's the variable the 58% got right." State what drives revenue; don't define it by what it isn't.

3. **Fix the reframe closer on slide 5.** Cut "Experimentation is common; integration is rare." The two stats (two-thirds experimented, under 10% scaled) already carry that point. End slide 5 on the numbers, or add a forward-looking line that stays inside the revenue angle, e.g., "The gap between those two numbers is where revenue is won or lost."

4. **Renumber** the CTA to slide 6 after the cut.

5. **Optional, improves rhythm:** slide 3's "It can be impressive and still change nothing" is fine to keep now that slides 2 and 5 are de-negated — with the pattern no longer repeating, it lands as a single sharp line rather than a tic.

The evidence, angle fit, and core insight are sound. This is a structure-and-scope rewrite, not a rethink.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "FAIL", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "1) Cut slide 6 entirely — it imports the month's operability-gap thesis ('run the agents you already bought,' 'engineering and governance') into a post only authorized to argue integration-drives-revenue. Do not fold it in elsewhere; it is a separate argument. This also brings the deck to 6 slides, within the 5–6 cap (F fix). 2) Slide 2: replace the setup-and-negate 'Model quality was never the variable' with a direct positive claim, e.g. 'The revenue comes from placement: live data, a real workflow, an owned outcome. That's the variable the 58% got right.' 3) Slide 5: cut the contrastive-reframe closer 'Experimentation is common; integration is rare' — the two stats already say it. End on the numbers or add a forward line that stays inside the revenue angle. 4) Renumber the CTA to slide 6. 5) Keep slide 3's 'impressive and still change nothing' — once slides 2 and 5 are de-negated it no longer stacks into a repeated pattern."}
```