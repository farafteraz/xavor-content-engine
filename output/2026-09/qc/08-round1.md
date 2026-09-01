# Editor's memo — Post 8 (explainer reel)

**Overall verdict: FAIL.** One banned-structure hit in Frame 2 (contrastive negation) and a supporting soft version in the caption. Everything else holds up well — evidence is clean, the depth is real, the CTO respect is there. This is a one-fix fail.

## Per-check

**V — Vocabulary: PASS.** Scanned against §5. "mission-critical" appears in Frames 3 and 5, but both are direct quotations of the Google/Credo survey language (E51 uses "mission-critical agents"). Quoted survey terminology is permitted. No other banned words.

**S — Structures: FAIL.**
- Frame 2: "The gap isn't a missing policy. Most companies wrote the policy. The operating layer... was never built." This is contrastive negation across sentences — the exact §6.1 pattern ("not X, it's Y" in disguise). It sets up a rejected half ("isn't a missing policy") and pivots to the positive claim. The contrast here is not correcting a specific fact/number/scope; it's a rhetorical reframe.
- Caption: "Governance at scale is not a policy you write once. It is infrastructure you wire..." Same §6.1 pattern, softer but still a "not X, it's Y" reframe.
- Frame 6: "This is engineering scope, not a procurement line." Another contrastive negation, and it also opens with the banned §6.6 "This is" unveiling.

**M — Metaphor: PASS.** "wire / wiring" and "operating layer" are literal engineering terms here, not figurative metaphor. "renders on demand" is literal (audit trails do render). No banned setups, families, or metaphor verbs.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold in body, caps, or em dashes. Bold appears only in the scaffold labels (Angle/Caption), not body copy. Frames counted — longest is Frame 5 at ~40 words but this is an explainer reel (§9: one line of VO per frame, no ≤25-word cap; that cap is carousel-only). Six frames, within the 6–8 spec.

**E — Evidence: PASS.** Both claims trace cleanly. 60%/4% and 61%→92% → E52. 83%/17% → E51. Populations stated correctly (371 senior leaders, 1,400+ IT leaders). No CONFLICT figures invoked, no composite merges, no invented specifics. This is the strongest part of the draft.

**O — One thing: PASS.** Argues exactly one idea: governance at scale fails because the operating layer under the policy was never built. Matches the slot angle verbatim and ladders to the operator's-gap thesis.

**L1 — Interchangeability: PASS.** The specifics (per-agent inventory, decision boundaries, token attribution, audit trail, the 61%→92% scale threshold) are not swappable for a generic technology. This is about agentic AI governance specifically.

**L2 — CTO respect: PASS.** No wince. The distinction between a written policy and enforced wiring is one a technical executive would nod at.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands in Frame 5: governance urgency jumps 61%→92% at exactly the moment of scale, so the unbuilt layer becomes the blocker precisely when you need production. That reframes governance from a compliance chore into a scaling gate. Real, not restated.

**R — Rhythm/human: PASS (with note).** The frame-by-frame form is inherently clipped, which the spec allows for reels. Sentences vary within frames. CTA grows naturally from Frame 6's claim. The one weakness: Frames 2, 4, and 6 all lean on the same "document vs. wiring / policy vs. enforcement" antithesis, which compounds the structural problem below.

## Edit notes

The draft fails on S alone. Three contrastive-negation reframes need to be rewritten as direct positive claims. The insight is already there — just stop staging it as a "not X, but Y."

1. **Frame 2** — Cut the negation. Replace with a direct statement of the mechanism. Something like: "Most companies wrote the governance policy. What they never built is the layer that enforces it across every deployed agent." State the positive claim; drop "The gap isn't a missing policy."

2. **Caption** — Rewrite "Governance at scale is not a policy you write once. It is infrastructure you wire" as a direct claim. Example: "Governance at scale is infrastructure you wire into every agent, and most stacks were never built for it. Sixty percent deploy across departments; four percent govern at scale." Remove the "not X" opener.

3. **Frame 6** — Remove both the "This is" unveiling (§6.6) and the "not a procurement line" negation (§6.1). Replace with a direct lead-in to the CTA. Example: "Closing this is engineering work, and it has a defined scope. Close the gap between deployed and governed now. Get in touch." Or lead straight with the outcome and let the CTA carry.

4. **While there**, vary the antithesis. Frames 2, 4, and 6 all run the same policy-vs-enforcement contrast. Keep it sharp in one frame (Frame 4's "Policy lives in a document. Enforcement lives in wiring" is the cleanest expression and is not itself a banned negation — it's a parallel, not a "not X"). Let Frame 2 do mechanism and Frame 6 do scope, so the reel doesn't hammer one rhetorical move three times.

No evidence, depth, or formatting changes needed. This is a clean rewrite of three lines.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Fix three contrastive-negation reframes (banned S6.1) plus one 'This is' unveiling (S6.6). (1) Frame 2: cut 'The gap isn't a missing policy.' State it directly, e.g. 'Most companies wrote the governance policy. What they never built is the layer that enforces it across every deployed agent.' (2) Caption: remove the 'not a policy you write once' opener; rewrite as a direct claim, e.g. 'Governance at scale is infrastructure you wire into every agent, and most stacks were never built for it. Sixty percent deploy across departments; four percent govern at scale.' (3) Frame 6: remove both 'This is engineering scope' (S6.6 'This is' unveiling) and 'not a procurement line' (S6.1 negation); replace with a direct lead-in, e.g. 'Closing this is engineering work with a defined scope. Close the gap between deployed and governed now. Get in touch.' (4) Vary the antithesis: Frames 2, 4, 6 all run the same policy-vs-enforcement contrast. Keep Frame 4's clean parallel ('Policy lives in a document. Enforcement lives in wiring') and diversify the other two so one rhetorical move isn't repeated three times. No evidence, metaphor, or formatting changes needed."}
```