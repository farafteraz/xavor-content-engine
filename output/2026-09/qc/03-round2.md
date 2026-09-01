# Editor's memo — Post 3 (explainer reel, N3)

## Overall verdict: FAIL

One mechanical failure on S (banned structure). Evidence is clean, one thing holds, depth is present. But the structure hit is disqualifying, and there's a secondary evidence-framing concern on Frame 5 worth flagging.

## Per-check

**V — Vocabulary: PASS.** No banned words. "meters/metered" is literal (a meter on a spend line), not figurative jargon. Clean.

**S — Structures: FAIL.**
- Frame 4: "That's the tell." This is a cliffhanger pivot / unveiling in the §6.5 family — a bare pointer sentence that primes a reveal instead of stating the claim. Combined with "A line no one owns is a line no one meters," it reads as the reframe machinery the spec flags.
- Frame 4 as a whole is also close to a §6.1 contrastive construction ("no one owns → no one meters") used rhetorically rather than to correct a fact.
- Frame 2 → Frame 3 is a setup-and-negate rhythm (§6.8): "finance sees the number. Then someone asks who owns it. / 52% say no one does." The setup-question-then-deflate beat is exactly the pattern §6.8 names, even though the underlying content is real.

The idea is sound; the delivery leans on staged reveals. That fails S.

**M — Metaphor: PASS.** "where the money leaks" is a mild figurative verb but sits inside the allowance for a live, normal phrase and isn't from a banned family. "gets a name / has a name" is literal (attribution to a named owner). No analogy setups. Pass, narrowly.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes, caps. Bold appears only in the scaffolding labels ("**Angle:**", "**Evidence used**"), not in body copy — acceptable as production metadata. Every frame is well under 25 words. Seven frames is within the 6–8 explainer range.

**E — Evidence: PASS, with one framing caution.**
- Frame 1: 31% → 98% two-year swing. E22 supports it, and the draft correctly uses the reconciled 2024 baseline. Clean.
- Frame 3: 52%, accountability splits four ways. E23 verbatim. Clean.
- Frame 5: "funded by whatever it saves elsewhere" traces to E27 (self-funding through optimization savings). The claim that this causes it to "never get right-sized" and "just grows" is an inference, not in the ledger. It's a reasonable reading of E27, not an invented number, so it does not fail E. But note it: the causal chain (unowned → never right-sized → grows) is the writer's, not the ledger's. Acceptable as argument, not as fact.
- No CONFLICT figures misused. No composite claims. Denominators correct (FinOps respondents throughout).

**O — One thing: PASS.** The post argues one thing: the AI cost line has no owner, and ownership is engineering work (attribution). Matches the slot angle exactly. Ladders to the big idea's cost layer. No "and" needed.

**L1 — Interchangeability: PASS.** Swap "AI spend" for "cloud spend" and the post breaks — the whole point (token-level attribution to team/product/BU, the two-year jump from 31% to 98%, the four-way split) is specific to how AI cost behaves. E25's token-vs-compute-hour logic is implied and load-bearing. Not generic.

**L2 — CTO respect: PASS.** A CTO reading this doesn't wince. The financial framing is credible and the "ownership is engineering, not procurement" turn is the right register for the audience.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is Frame 5: an unowned line gets self-funded by its own savings, so it never gets right-sized — it just grows. That reframes the cost problem from "is this worth it" to "nothing is applying pressure to it." That's the non-obvious beat the slot needs.

**R — Rhythm/human: WEAK (not a standalone fail, but reinforces S).** The frames lean short and punchy across the board, and Frames 2–4 chain into a staccato reveal rhythm. That's partly the format, but the reveal cadence is what tips S into failure. Fix S and R improves with it.

## Edit notes

The content is right and the evidence holds. The problem is delivery mechanics in Frames 2–4. Rewrite those three so the claims land flat, not staged.

1. **Kill "That's the tell." (Frame 4).** Replace the pointer-then-reveal with the claim stated directly. Something like: "A line no one owns is a line no one meters, and a line no one meters only grows." State it; don't announce that you're about to.

2. **Break the setup-and-negate across Frames 2–3.** Right now it's: finance sees the number → someone asks who owns it → 52% say no one does. Collapse the rhetorical question beat. Lead with the fact: e.g. Frame 2 "Finance can see the AI number. It can't map it to a team, a product, or a business unit." Frame 3: "52% of finance teams say no one owns AI cost. Accountability splits four ways and lands nowhere." That removes the question-then-deflate rhythm and adds the E25 token-mapping specific, which strengthens L1 further.

3. **Frame 5 causal chain:** keep it, but tighten so it reads as the writer's argued conclusion, not a stated fact. It's fine as inference from E27; just make sure it doesn't sound like a surveyed statistic. Current wording is acceptable if you keep it — the E flag is a caution, not a required change.

4. **After the rewrite, re-read for rhythm:** vary at least one frame's length so the whole thing isn't seven clipped beats. The explainer format allows compression, but the current cadence is metronomic and that's what surfaced the reveal patterns in the first place. Let one frame carry a fuller line.

Do not touch Frames 1, 6, or 7 — the numbers, the "ownership is engineering: token attribution mapped to team, product, and business unit" line, and the CTA are all correct and load-bearing.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Fix banned structures in Frames 2-4. (1) Delete 'That's the tell.' in Frame 4 (cliffhanger/unveiling pivot, §6.5); state the claim directly, e.g. 'A line no one owns is a line no one meters, and a line no one meters only grows.' (2) Break the setup-and-negate rhythm across Frames 2-3 (§6.8): drop the 'someone asks who owns it' question beat. Lead Frame 2 with a fact — e.g. 'Finance can see the AI number. It can't map it to a team, a product, or a business unit.' (uses E25 token-mapping logic, strengthens L1). Frame 3: '52% of finance teams say no one owns AI cost. Accountability splits four ways and lands nowhere.' (3) Frame 5 causal chain (unowned -> never right-sized -> grows) is the writer's inference from E27, not a stated stat; keep but ensure it reads as argument, not survey fact. (4) Vary one frame's length so the reel isn't seven clipped beats. Leave Frames 1, 6, 7 untouched — numbers, the 'ownership is engineering: token attribution' line, and CTA are correct."}
```