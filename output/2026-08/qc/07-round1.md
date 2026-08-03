# Editor's memo — Post 7 (video feature, Navi / BMW physical AI)

## Overall verdict: PASS

This is a strong draft. It carries the expertise register, argues exactly one thing, and delivers a real cognitive-depth moment for a manufacturing CTO. The evidence discipline (explicitly declining to state E27's 30,000-car figure as a hard number) is exactly the caution the spec wants. I hunted for AI tells and found nothing that fails a hard check.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "pipeline" is used literally (data/control pipeline), not figuratively. "physical AI integration blueprint" is the slot-mandated CTA phrasing and contains no banned word. No "seamless," "robust," "scalable," "leverage," etc.

**S — Structures: PASS.** Checked every sentence pair for reframes.
- "Figure built the humanoid. Figure did not build the connection..." — this reads like a contrastive negation candidate, but it survives: it corrects a specific scope claim (who built what), which §6.1 explicitly permits ("correct a specific fact, number, date, name, or scope"). It's not "not X, it's Y" reframe theatre; it's a factual boundary.
- "the hard part is rarely the machine. It is the pipeline underneath" — again scope-specific and grounded in a named product experience (Navi), not a manufactured pivot. Passes.
- Beat 3's three items (edge inference, MES handshake, OT/IT boundary) are three real, non-interchangeable technical requirements, not a rule-of-three closer or dramatic triple burst. They carry distinct content.
- CTA is the mandated wording, not an amputated slogan tag.
No "This is" unveilings, no cliffhangers, no setup-and-negate, no puffery.

**M — Metaphor: PASS.** "the layer under it / underneath" is the month's literal framing (a real integration layer), not a metaphor family hit. "does what it already did a thousand times in simulation" is literal. No banned setups or metaphor verbs.

**F — Formatting: PASS.** Bold appears only in the scaffolding labels (Angle, Caption, beat headers), not in body VO/caption copy — acceptable as structural markup. No emojis, hashtags, exclamations, em dashes, or caps in the spoken/caption copy. Video feature length is within the 60–90s treatment spec (runs to 1:20).

**E — Evidence: PASS.** Every claim traces cleanly.
- "just-in-sequence logistics at Spartanburg," "ten-month pilot" → E25. Correct.
- "moved production parts" is framed conservatively; E27's 30,000-car figure is deliberately not stated as a number. Good call, correctly declared.
- "vendors keep shipping better robots" → E24 (BotQ scale), used as premise not figure. Fine.
No invented specifics, no CONFLICT figure (E32 correctly untouched), no merged composites.

**O — One thing: PASS.** The post argues: a production humanoid still needs an integration layer (edge AI, MES, OT/IT) that the plant's own engineers build. One idea, matches the slot angle, ladders to "the layer under the platform" with the robot as the platform.

**L1 — Interchangeability: PASS.** The specifics resist swapping. "MES handshake so the robot knows what sequence to build," "OT and IT boundary so the plant network stays safe," and the Navi perception/real-time-control detail are all Figure/factory/Navi-specific. Swap in a different vendor and the MES/just-in-sequence detail breaks.

**L2 — CTO respect: PASS.** The "the connection lands on your engineers" framing and the digital-twin fault-recovery beat read like a peer who has done the OT/IT integration work, not a vendor. No wince.

**L3 — Cognitive depth: PASS.** The delivered moment: "Figure built the humanoid. Figure did not build the connection between that humanoid and the plant it works in. That connection is a project, and it lands on your engineers." A manufacturing leader watching a shipping humanoid demo assumes the robot is the deployment; this reframes the robot as the easy part and the MES/OT integration as the unfunded project. That is the "I hadn't considered that."

**R — Rhythm/human: PASS.** Sentence lengths vary within each VO block, transitions are real, and it sounds like spoken narration when read aloud. Not metronomic. The CTA grows out of Beat 6 rather than being bolted on.

## One improvable weakness (non-blocking)
Beat 4's "without failing quietly" is a nice, true detail but slightly abstract for a visual medium; if there's a way to show the silent-failure mode on screen (a log line, a missed handoff), it would land harder. Optional.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```