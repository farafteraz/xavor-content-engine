# Post 10 — 2026-09-16 — carousel
**Angle:** Enterprise GPU sits near 5% utilization and cost-per-answer fell from $0.41 to $0.07 with routing, caching, and right-sizing, so the money is in operating what you run.

## Caption
Most enterprises are paying full price for inference and running their GPUs at a fraction of capacity. The spend isn't the problem. The lack of an owner is. Here's where the money actually hides, and how far it moves once someone runs the numbers.

## Copy

Slide 1:
Your GPUs are running at 5% utilization. You're paying for all of them. The AI invoice is the largest line item most enterprises can't attribute to anyone.

Slide 2:
52% of teams say no one owns AI cost. Accountability splits four ways: engineering, finance, product, platform. When four people own it, nobody operates it.

Slide 3:
Average enterprise GPU utilization runs near 5% across 23,000 clusters measured. That's not a capacity problem. It's idle hardware nobody is right-sizing.

Slide 4:
Across 84 Bedrock deployments, cost-per-answer fell from $0.41 to $0.07. An 83% cut. The levers: route requests to the right model, cache what repeats, size the hardware to the load.

Slide 5:
None of that is a new purchase. It's operating work on infrastructure you already run. The savings fund the next thing you want to build.

Slide 6:
Recover the spend hiding in idle compute now. Get in touch.

## Evidence used
- [E23]: 52% report no clear owner of AI costs; accountability split four ways.
- [E24]: Cast AI 2026 Kubernetes report, 23,000 clusters, average enterprise GPU utilization roughly 5%.
- [E28]: Opslyft analysis of 84 Bedrock deployments, cost-per-answer dropped from $0.41 to $0.07 (83% reduction) after routing, caching, right-sizing.

## Design note
Keep it numbers-forward: each middle slide anchors on one large figure (5%, 52%, $0.41 to $0.07) in the dominant type, supporting line beneath in a lighter weight. Consistent left alignment, restrained palette, no icons competing with the numbers.