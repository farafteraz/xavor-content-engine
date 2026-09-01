# Editor's Memo — Post 14 (carousel, N2)

**Overall verdict: PASS**

This one holds up. The draft connects an unowned, unstoppable agent to a specific breach cost a CISO will have to explain, which is exactly the slot's job. Numbers trace cleanly. No AI tells survive a close read.

## Per-check results

**V — Vocabulary: PASS.** No banned words. "governance process" comes straight from E34's language, not filler. No "critical/crucial/robust/seamless" anywhere.

**S — Structures: PASS.** I hunted for reframes. Slide 5 opens "The fix is scope, not fear" — this is the risky one. It reads as contrastive negation ("not X, Y") on first pass. But the spec permits contrast when it corrects scope, and here it's naming the banned pattern the spec itself worries about (fear-based marketing) and asserting the positive claim (scope). It's borderline. It survives because the sentence immediately delivers the specific positive claim (named owner, decision boundary, tested kill switch) rather than trading on the contrast for effect. Not a triple burst, not a rule-of-three closer. Slide 4 "The connection is direct" leads with the subject, not a "This is" unveiling. No cliffhanger pivots. No amputated slogan tags.

**M — Metaphor: PASS.** Zero analogies. "moving the wrong way" is literal agent behavior, not a metaphor family. Verbs are literal (wired, deployed, stopped, tested).

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Bold appears only in slide labels and the angle line (scaffolding, not body copy). Slide word counts all under 25: slide 2 is the longest at roughly 24 words. Clear.

**E — Evidence: PASS, and carefully.** This is where I expected drift and didn't find it.
- Slide 1: 35% couldn't shut down a rogue agent → E35. Exact.
- Slide 2: 43% of breach incidents, up from ~one in five, two-thirds had no governance process → all E34. Exact, no merge.
- Slide 3: $4.99M, 12% jump, all-time high → E34. Exact.
- E36 correctly declared unused and no figure drawn from it. The writer's evidence note explicitly says so. Good discipline.
- No CONFLICT figures touched. No composite claims. Denominators respected (E35's 35% is executives, E34's 43% is incidents — the draft keeps them separate and doesn't fuse the two populations into one false stat).

**O — One thing: PASS.** The post argues: an agent deployed without an owner and a kill switch is a breach you can't stop and will have to explain at $4.99M. One idea, ladders to the operator's gap (the missing control layer). Matches the slot angle.

**L1 — Interchangeability: PASS.** Swap "agent" for "cloud service" and it breaks — the kill-switch/rogue-behavior/owner framing is specific to autonomous agents, and the 35%/43% numbers are agent- and shadow-AI-specific. Not generic.

**L2 — CTO respect: PASS.** No wince. The numbers are real, the causal claim is stated plainly, and "That work happens before the incident, or during it" is the kind of dry line a CISO respects. No fear-mongering past what the breach data supports.

**L3 — Cognitive depth: PASS.** The moment lands on slide 4–5: the reader reframes a rogue-agent breach from a security-tooling problem into a missing-owner-and-kill-switch engineering scope they can actually spec. The "I hadn't considered that" is that the kill switch is wiring you either did or didn't do at deploy time — not a runtime capability you can buy after. That's the slot's intended payload and it's delivered.

**R — Rhythm/human: PASS.** Sentence lengths vary within slides. Slide 4's three short declaratives risk a triple beat, but they carry distinct claims (no owner → no watcher → no stop) and the design note deliberately breaks rhythm there. CTA is the mandated register and lands naturally off slide 5. Caption reads like speech.

## One improvable weakness

Slide 5's "not fear" is the only line doing rhetorical work instead of factual work. It's defensible, but if a rewrite ever touches this, consider "The fix is scope. Every production agent gets a named owner..." — drop the "not fear" and let the specifics carry it. Not a blocker.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```