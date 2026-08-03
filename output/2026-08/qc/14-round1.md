# Editor's Memo — Post 14 (case-study carousel)

**Overall verdict: FAIL.** One mechanical hit on structures (S) sinks the draft. Everything else is close to clean, and the fix is small.

## Per-check results

**V — Vocabulary: PASS.** Scanned against §5. No banned words. "Real-time" is a technical descriptor, not "data-driven"-class filler. No "leverage," "seamless," "robust," etc.

**S — Structures: FAIL.** Contrastive negation appears in multiple places, most of it corrective and allowable, but at least one instance is the banned rhetorical reframe, not a fact correction.

- Slide 1: "Figure put a humanoid on the BMW line and it looks like a robot purchase. It was a ten-month integration sequence. The robot was the easy part." This is a cross-sentence "it's not X, it's Y" reframe (the whole hook is built on "looks like X / was actually Y"). It is not correcting a fact, number, date, or scope — it is reframing perception to manufacture insight. This is exactly the §6.1 pattern in its sneaky "on the surface X... actually Y" form. FAIL.
- The angle line itself carries the banned "not a robot purchase" reframe, but that's metadata, not body copy — still, it signals the frame the copy inherited.
- Borderline-but-acceptable: Slide 2 "not a better robot" and Slide 3 "That reading and writing is the work" and Slide 4 "Manufacturing the fleet is solved. Sequencing each unit into a live plant is the open problem" read as scope corrections grounded in specifics, so I'd let those stand on their own. But Slide 1's hook is the load-bearing reframe and it fails.

**M — Metaphor: PASS.** "The layer under the robot" is literal (there is an actual integration stack under a physical robot), not a figurative "backbone of" construction. "Rehearse" for a digital twin is literal simulation language. No banned setups or verbs.

**F — Formatting: PASS on the bans** (no emojis, hashtags, exclamations, em dashes in body). Slide word counts: S1 ~26, S2 ~25, S3 ~30, S4 ~29, S5 ~30, S6 ~26. The spec caps slides at ~25 words with a soft tilde. Several slides run 29–30. This is over the guideline but within tilde tolerance for a judgment read — not a hard fail on its own, but tighten in the rewrite. Note the bold on "Slide 1:" etc. is a label scaffold, not body copy, so it doesn't trip the bold ban.

**E — Evidence: PASS.** Every factual claim traces cleanly:
- 10-month Figure 02 pilot, just-in-sequence, Spartanburg → [E25]. ✓
- 30,000 cars → [E27]. ✓
- 1,000th Figure 03, July 23 2026, one robot/hour → [E24]. ✓
- Phased 2026–2027 expansion used as context, not stated as a figure → [E26], correctly handled. ✓
No invented numbers, no CONFLICT figures (the E32 funding trap is untouched), no denominator drift. Clean.

**O — One thing: PASS.** The post argues: the integration layer (edge AI, MES connectivity, digital twins), not the robot, is what makes a humanoid deploy. One idea, matches the slot angle, ladders to "the layer under the platform." Good.

**L1 — Interchangeability: PASS.** Swap Figure/BMW for another vendor and the copy breaks — the 10-month pilot, 30,000 cars, BotQ's 1,000th unit, and just-in-sequence logistics are all specific to this deployment. Not generic.

**L2 — CTO respect: PASS.** A manufacturing CTO reads this as someone who knows the difference between a demo and OT/IT integration. "Returns data the plant systems trust" and "reads the line state" are the right register.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands on Slide 4: "Manufacturing the fleet is solved. Sequencing each unit into a live plant is the open problem on your floor." That reframes the humanoid conversation away from hardware availability toward the buyer's own integration burden. Real.

**R — Rhythm/human: PASS, with a note.** Reads like a person, varied lengths, CTA grows naturally. The one weakness: Slide 1 is a three-beat staccato ("looks like a robot purchase / ten-month sequence / robot was the easy part") that leans hard on the reframe. Fixing S will also fix the rhythm dip.

## Edit notes

Only Slide 1 needs work; the rest ships once you also trim the three long slides toward 25 words.

1. **Rewrite Slide 1 to kill the "looks like X / was actually Y" reframe.** Do not open by stating the reader's assumption and then negating it. Lead with the specific fact and let it carry the idea. Replacement direction: open on the concrete sequence itself. Something like: "Figure's humanoid reached the BMW Spartanburg line through a ten-month integration sequence. Edge AI, MES connectivity, and OT/IT pipelines came first. The robot deployed last." That states the claim directly, keeps the hook informative, and drops the perception-reframe. Keep it under 25 words.

2. **Trim the over-length slides** (S3, S4, S5 at ~29–30 words) by cutting words, not voice. Example for S3: "Figure 02 helped assemble 30,000 cars in that pilot. A humanoid earns that only when it reads line state and returns data the plant trusts." Get each to ~25.

3. **Leave S2, S4's second half, and the CTA as-is** — those contrasts are scope corrections tied to specifics and are allowed. The only banned instance is the Slide 1 hook.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Slide 1 uses a banned contrastive-negation reframe (§6.1) in its sneaky 'looks like X / was actually Y' cross-sentence form: 'Figure put a humanoid on the BMW line and it looks like a robot purchase. It was a ten-month integration sequence. The robot was the easy part.' This reframes perception rather than correcting a fact/number/date/scope, so it is not the allowed exception. Rewrite Slide 1 to lead with the concrete fact and drop the assumption-then-negate move. Target: 'Figure's humanoid reached the BMW Spartanburg line through a ten-month integration sequence. Edge AI, MES connectivity, and OT/IT pipelines came first. The robot deployed last.' Keep under 25 words. Separately, trim Slides 3, 4, and 5 (currently ~29-30 words) down to ~25 by cutting words, not by chopping voice into fragments; e.g. S3: 'Figure 02 helped assemble 30,000 cars in that pilot. A humanoid earns that only when it reads line state and returns data the plant trusts.' Leave Slide 2 ('not a better robot'), Slide 4's 'Manufacturing the fleet is solved. Sequencing each unit into a live plant is the open problem', and the CTA unchanged — those contrasts are scope corrections tied to specifics and are permitted. Evidence, one-thing, and cognitive depth all pass; do not touch the facts."}
```