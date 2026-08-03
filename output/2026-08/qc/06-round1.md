# Editor's memo — Post 6 (carousel)

## Overall verdict: FAIL

One mechanical hit on S (banned structure). The rest of the draft is strong and would pass with a single-slide fix. Details below.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Governed," "identity-verified," "auditable," "control surface" are precise technical language, not filler. No "leverage," "seamless," "robust," etc.

**S — Structures: FAIL.** The caption contains engagement bait: "Read that as a location change." This is the "Read that again" family — a directive telling the reader how to process the sentence rather than just delivering the claim. It also functions as a soft unveiling ("read that as X"). Fix required.

Two more borderline items to watch, neither a hard fail on its own:
- Slide 3: "So the agent market matters less than the layer under it." This is a comparative claim, not a contrastive-negation reframe (it doesn't reject one half to elevate the other with "not X but Y"). Legal, but sits near the line. It's earned because the following sentence gives the specific reason.
- Slide 1 / Slide 2: "Notice where that leaves the value." / "Notice where..." is a mild directive but reads as a natural analytic hand-off, not bait. Acceptable, but if you're already editing the caption, keep an eye on the repetition of the "notice/read as" instruction pattern across caption + slide 1.

**M — Metaphor: PASS.** "The layer under it" is the month's literal frame (governance/data/cost layer), not a metaphor. "Where the value sits," "the surface it calls" are literal architecture. No banned setups, families, or verbs.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps, em dashes. Slide word counts: S1 ~26 — borderline over the ~25 cap; S2 ~27; S4 ~30; S5 ~28. Several slides run slightly over ~25 words. The spec says "~25" (approximate), so I won't hard-fail F, but see edit notes: tighten S4 and S2, which are the heaviest. Flagging as the improvable weakness rather than a fail.

**E — Evidence: PASS.** Every factual claim traces to [E15]: any agent (Claude, Copilot, customer stack) triggering governed, identity-verified, auditable ServiceNow workflows, Anthropic as first design partner. The draft correctly does not invent numbers or drag in ARR/ACV figures that don't belong in this slot. [E14] used as unstated context only, as declared. No unsupported specifics.

**O — One thing: PASS.** The post argues one thing: when any agent can trigger governed workflows through a control surface, value and accountability move to the surface, which is yours to build and prove. Matches the slot angle exactly and ladders to "the layer under the platform."

**L1 — Interchangeability: PASS.** Swap ServiceNow for another vendor and the copy breaks — the argument depends on the specific fact that ServiceNow opened its governed workflows to external agents via MCP Server, with named clients calling in. The point about the caller being a client and the surface holding identity/audit is specific to this architecture.

**L2 — CTO respect: PASS.** Reads like a peer making an architectural observation. The "agent is now a client, it calls in" framing is the kind of precise reframing a technical exec respects. The caption bait is the one moment that would make a CTO wince — fix it and this is clean.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" lands on Slide 2–3: the agent becomes a client calling in, so whichever agent wins the market, the value stays at the surface it calls. That inverts the default assumption (agent choice is the strategic decision) into an architectural one. Genuine.

**R — Rhythm/human: PASS.** Varied sentence length, real analytic transitions ("So...", "That surface is where..."), reads like speech. CTA grows naturally from the argument. Not metronomic.

## Edit notes

Single required fix for the S fail:

- **Caption, sentence 2:** delete the directive "Read that as a location change:". Rewrite to state the claim plainly. Replacement: "That is a location change. The value and the accountability now sit at the control surface, not the agent calling it." (Drops the reader-instruction; keeps the insight.)

Recommended while you're in there (not blocking):
- Trim the heaviest slides toward the ~25-word cap by cutting words, not voice. Slide 4 (~30) and Slide 2 (~27) are the priorities. Example for S4: "That surface is also where accountability sits. When an auditor asks who authorized an action, the answer comes from your control layer, not the agent's vendor." Cut words only; keep full sentences.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Fix the one S violation in the caption: delete the engagement-bait directive 'Read that as a location change:' (same family as 'Read that again'). Replace with a plain statement, e.g. 'That is a location change. The value and the accountability now sit at the control surface, not the agent calling it.' Do not add any other reader-instruction phrasing; note that 'Notice where that leaves the value' in Slide 1 already uses a mild directive, so avoid stacking a second one. Non-blocking cleanup: trim Slide 4 (~30 words) and Slide 2 (~27 words) toward the ~25-word cap by cutting words, not by fragmenting the voice, e.g. Slide 4: 'That surface is also where accountability sits. When an auditor asks who authorized an action, the answer comes from your control layer, not the agent's vendor.'"}
```