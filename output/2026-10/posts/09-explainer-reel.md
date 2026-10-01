<!-- QC: PASS after 2 round(s) -->

# Post 9 — 2026-10-15 — explainer reel
**Angle:** Cost-per-answer fell from $0.41 to $0.07 across 84 production Bedrock deployments, yet total bills keep climbing because agentic tasks fire those calls across systems faster than the price per call drops.

## Caption
Your per-token price is falling. Your AI bill is still going up. Both things are true, and the gap between them is where the budget wall forms.

## Copy
Frame 1:
Opslyft tuned 84 production Bedrock deployments and cut cost per answer from $0.41 to $0.07, an 83% drop.

Frame 2:
Routing, caching, right-sizing. Everything FinOps prescribes. The engineers did all of it, and it worked.

Frame 3:
The total bill still went up.

Frame 4:
One agentic task no longer makes one call. It fires dozens across several systems to finish a single job.

Frame 5:
So the price per answer drops 83% while the number of answers per task climbs faster. Gartner expects per-inference cost to fall another 90% by 2030. Bills keep rising anyway.

Frame 6:
And when a task crosses Salesforce, Snowflake, and ServiceNow, no single vendor's tool can tell you which team to bill. The spend lands in the space between systems.

Frame 7:
The number that matters is cost per answer, attributed to a team and a product, across every platform the task touches. Price per token tells you almost nothing on its own.

Frame 8:
Cut cost-per-answer in your deployments now. Get in touch.

## Evidence used
- [E36]: the $0.41-to-$0.07 (83%) reduction across 84 production Bedrock deployments with routing, caching, right-sizing. Used as the opening hook and the core proof in Frames 1–2.
- [E31]: Gartner's projected further 90%+ per-inference cost drop by 2030, and the reason total bills still climb (agentic workloads multiply tokens per task). Used in Frames 4 and 5.
- The cross-platform attribution point in Frame 6 ladders to the month's seam idea; the named platforms (Salesforce, Snowflake, ServiceNow) are drawn from the month's governed-runtime context (E4, E7, E52), used illustratively rather than as a new statistic.

## Design note
Keep one running counter on screen: a per-answer price ticking down while a total-bill bar grows taller, so the eye sees both moving the wrong way together. Plain type, no motion gimmicks; let the two numbers carry it.