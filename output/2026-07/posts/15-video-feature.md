<!-- QC: PASS after 1 round(s) -->

# Post 15 — 2026-07-28 — video feature
**Angle:** FinOps now reports to the CTO or CIO at most teams, so accounting for AI spend against value has become an engineering responsibility, not a finance afterthought.

## Caption
FinOps moved under the CTO for a reason. When AI spend is metered, attribution stops being a monthly reconciliation and becomes an architecture decision you make on day one. Here is what that looks like when we build it.

## Copy

**Video feature — 75 second treatment**

**Beat 1 (0:00–0:08)**
We see: A quiet office at end of quarter. A finance lead slides a printed cloud bill across a desk to a CTO. The number is large. Neither person can explain the top line.
Spoken: "The bill arrives every month. The value it bought is a lot harder to find on the page."

**Beat 2 (0:08–0:20)**
We see: One org chart, the FinOps box under the CTO. A counter beside it climbs from 61% in 2023 to 78% in 2026.
Spoken: "In 2023, 61 percent of FinOps teams reported to the CTO or CIO. By 2026 it is 78 percent. The reason is simple. Metered AI is an engineering decision before it is a budget line."

**Beat 3 (0:20–0:34)**
We see: A Xavor engineer at a whiteboard drawing a request as it moves through an agent, a retrieval step, a model call, a tool call. Each hop gets a small tag.
Spoken: "Flat-rate budgeting assumed a fixed price for a fixed seat. Agents don't work that way. One request can fan out into ten model calls and six tool calls, and the cost lands per token, per run, per resolution. If you can't tag the spend at the point it happens, you can't reconstruct it later. Nobody can."

**Beat 4 (0:34–0:48)**
We see: A dashboard on a wall monitor. Spend broken out by agent, by workflow, by business outcome. An engineer points at one line that is climbing and traces it to a specific workflow.
Spoken: "So we build attribution into the pipeline itself. Every call carries which agent made it, which workflow it served, and what it resolved. When a line climbs, you see the workflow behind it in seconds, not after the close."

**Beat 5 (0:48–1:02)**
We see: The FinOps lead and the CTO now looking at the same dashboard together, agreeing. The Yarken framing on a card: spend is growing, and nobody can see why, who drives it, or what value it generates.
Spoken: "The common failure isn't overspending. It's spending you cannot account for. When 98 percent of FinOps teams now manage AI spend, the ones who win are the ones who wired the accounting in before the first agent shipped."

**Beat 6 (1:02–1:15)**
We see: Wide shot of the Xavor engineering floor. Cut to the Xavor mark. Text resolves on screen with the closing line.
Spoken: "Reconstruction after the bill lands is a guess. Attribution built into the architecture is a fact. Account for every dollar of AI spend now. Get in touch."

## Evidence used
- [E27]: FinOps reports to CTO or CIO at 78% of teams in 2026, up from 61% in 2023 — used in Beat 2 as the structural fact behind the angle.
- [E21]: 98% of FinOps teams manage AI spend in 2026 — used in Beat 5.
- [E26]: Spend growing while nobody can see why, who drives it, or what value it generates (Yarken / FinOps X 2026) — used as the on-screen framing in Beat 5.
- Note: Beat 2 states E27's reporting-line shift exactly (61% in 2023 to 78% in 2026); the earlier "under finance in 2023" framing was removed as unsupported.

## Design note
Keep the palette cool and restrained. The one recurring visual motif is a single spend line on a dark dashboard that goes from unexplained (Beat 1) to traceable (Beat 4), so the payoff reads without narration. On-screen numbers should match the spoken figures exactly.