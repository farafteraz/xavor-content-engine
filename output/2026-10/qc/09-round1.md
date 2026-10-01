# Editor's memo — Post 9 (explainer reel)

## Overall verdict: FAIL

The angle is genuinely sharp and the evidence core is clean. But there's a banned-structure hit in Frame 4 and a rhythm problem that runs through the whole reel: it's a chain of staccato fragments, exactly the "chopping the voice into staccato fragments" the spec warns against. Both are fixable without touching the idea.

## Per-check results

**V — Vocabulary: PASS.** No banned words. "right-sizing" is a literal FinOps term, not puffery. Clean.

**S — Structures: FAIL.**
- Frame 4: "Here is why." — this is a cliffhanger pivot (§6.5, "The result?" / "Here's the thing" family). Write the next sentence instead.
- Frame 7 opens with "That is the number to chase." followed by "Not price per token. Cost per answer..." — this is a contrastive negation (§6.1, "Not X. Y."). It is not correcting a fact, number, or scope; it's reframing for drama. FAIL.
- Borderline but worth flagging: Caption "Both things are true, and the gap between them is where the budget wall forms" leans on a setup cadence but survives — it's a direct statement, not a negate. OK.

**M — Metaphor: PASS.** "budget wall forms" and "space between systems" are literal enough. No banned setups or metaphor verbs.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics in body, no em dashes. This is a reel, not a carousel, so the ≤25-word slide cap doesn't bind; frames are all short regardless. Good.

**E — Evidence: PASS, with one note.**
- $0.41 → $0.07, 83%, 84 Bedrock deployments: E36. Clean.
- Gartner 90% per-inference drop by 2030, bills climb because agentic workloads multiply tokens: E31. Clean, and correctly attributed.
- Frame 6 names Salesforce, Snowflake, ServiceNow illustratively, not as a statistic — supported by E4/E7/E52 context. Acceptable as framing, not a quantified claim.
- No invented numbers, no CONFLICT figure misstated. The author's evidence table is honest about what's illustrative. Pass.

**O — One thing: PASS.** The post argues: cheaper tokens raise your bill because agentic tasks fire more calls across systems faster than price falls. One idea, matches the slot job exactly, ladders to the seam in Frame 6. No "and" needed.

**L1 — Interchangeability: PASS.** Swap Bedrock for another inference platform and the $0.41→$0.07 specific, the per-answer-vs-per-token distinction, and the cross-platform attribution point all stay load-bearing. Not generic.

**L2 — CTO respect: PASS.** The "number to chase is cost per answer attributed to a team and product, not price per token" lands with a FinOps-literate executive. No wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is Frame 6: no single vendor's cost tool can attribute spend when a task crosses three platforms, so the overspend lands in the seam. That reframes a FinOps problem as a governance-boundary problem. Real.

**R — Rhythm/human: FAIL.** The reel is almost entirely short declarative fragments, one after another: "An 83% cut." / "The total bill still went up." / "Bills keep rising anyway." A reel is the compressed voice, but §9 says frames should still be "same voice compressed; no staccato hype," and §4 forbids chopping the voice into fragments. Right now it reads as metronome. Several frames need one flowing line instead of two clipped ones.

## Edit notes

1. **Frame 4 — kill the cliffhanger.** Delete "Here is why." Open directly: "One agentic task no longer makes one call. It fires dozens across several systems to finish a single job." That already flows better and removes the §6.5 hit.

2. **Frame 7 — kill the contrastive negation.** Replace "That is the number to chase. Not price per token. Cost per answer, attributed to a team and a product, across every platform the task touches." with a positive statement: "The number that matters is cost per answer, attributed to a team and a product, across every platform the task touches. Price per token tells you almost nothing on its own." The second sentence keeps the contrast but states it as a plain claim, not a "Not X. Y." reframe.

3. **Rhythm pass across Frames 1–3.** Don't flatten everything into fragments. Combine where it reads like speech. Frame 1 can be: "Opslyft tuned 84 production Bedrock deployments and cut cost per answer from $0.41 to $0.07, an 83% drop." Frame 2: "Routing, caching, right-sizing. Everything FinOps prescribes. The engineers did all of it, and it worked." Keep Frame 3 ("The total bill still went up.") short on purpose — one deliberate short beat after two fuller lines is the varied rhythm the spec wants, instead of ten short beats in a row.

4. Leave Frame 5, Frame 6, and the CTA as they are. Frame 6 is the strongest frame and carries the depth; don't touch it.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "FAIL"},
 "verify_flags": [],
 "edit_notes": "S fixes: (1) Frame 4 delete the cliffhanger pivot 'Here is why.' and open directly with 'One agentic task no longer makes one call. It fires dozens across several systems to finish a single job.' (2) Frame 7 remove the contrastive-negation 'That is the number to chase. Not price per token.' Rewrite as a positive claim: 'The number that matters is cost per answer, attributed to a team and a product, across every platform the task touches. Price per token tells you almost nothing on its own.' R fixes: break the metronome fragment chain in Frames 1-3. Frame 1: 'Opslyft tuned 84 production Bedrock deployments and cut cost per answer from $0.41 to $0.07, an 83% drop.' Frame 2: 'Routing, caching, right-sizing. Everything FinOps prescribes. The engineers did all of it, and it worked.' Keep Frame 3 ('The total bill still went up.') as a single deliberate short beat for contrast. Do not touch Frames 5, 6, or the CTA; Frame 6 is the load-bearing insight. Evidence is clean, no verify flags."}
```