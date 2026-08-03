# Post 15 — 2026-08-27 — case-study carousel
**Angle:** The unassignable agentic bill becomes attributable once you instrument the query fan-out. Building that attribution into the pipeline is the cost layer the vendor invoice creates but never solves.

## Caption
One banking query fans out into seven model calls across three providers, and the invoice lands as a single tenant-level number no one can assign. That gap is not a billing quirk. It is the cost layer you have to build. Here is how the chain becomes a line item.

## Copy

Slide 1:
A user asks one question. The bill charges for seven model calls, three retrievers, and four tool calls. Then it arrives as a single number. Who owns it?

Slide 2:
This is real. One banking query triggers an orchestrator, three retrievers, four tool calls, and seven model invocations across providers. The bill aggregates at the tenant level (FinOps Foundation).

Slide 3:
Attribution breaks at the point the query fans out. By the time the invoice lands, the fan-out is gone. You can see the total. You cannot see which team, product, or workflow caused it.

Slide 4:
The reason it matters now: GPU spend is the top FinOps concern for AI-first organizations, ahead of general cloud costs for the first time (FinOps Foundation). An unassignable GPU bill is a boardroom problem.

Slide 5:
The fix is engineering, not procurement. Tag every call at the point of fan-out with the query, team, and workflow that caused it. Carry those tags through the trace so the invoice reconciles to a line item.

Slide 6:
Make every agentic query a line item you can assign. We build the attribution layer into your pipeline before the next bill arrives. Get in touch.

## Evidence used
- [E50]: the query fan-out chain (orchestrator + 3 retrievers + 4 tool calls + 7 model invocations across providers) and the aggregated tenant-level bill — used on slides 1, 2, 3.
- [E49]: GPU spend as the #1 FinOps concern for AI-first organizations, surpassing general cloud costs for the first time — slide 4.
- [E48]: granular AI spend monitoring (tokens, LLM requests, GPU utilization) as the top requested capability, supporting the buildable-instrumentation argument — informs slides 4 and 5 (not quoted as a figure).

## Design note
Build slides 2 and 3 as one query node branching into the labeled call chain, then collapsing into a single invoice box on slide 3 to show where attribution is lost. Slide 5 reintroduces the tags flowing through the same chain so the fix reads as the mirror of the break.