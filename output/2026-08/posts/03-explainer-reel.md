<!-- QC: PASS after 1 round(s) -->

# Post 3 — 2026-08-05 — explainer reel
**Angle:** One agentic query fans out into a dozen model, retriever, and tool calls across providers, and the vendor invoice arrives at the tenant level with no way to attribute the spend.

## Caption
GPU spend is now the top FinOps concern for AI-first organizations. The reason isn't price. It's that one agentic query splinters into calls across providers, and the bill comes back to you as a single number nobody can assign.

## Copy
Frame 1:
A customer asks your banking assistant one question. On screen: "One query."

Frame 2:
That query wakes an orchestrator, then three retrievers, then four tool calls, then seven model invocations. Across providers.

Frame 3:
Fifteen billable events fire in under two seconds. Some run on your GPUs. Some run on someone else's.

Frame 4:
At month end the invoice arrives at the tenant level. One line. No team, no product, no query attached.

Frame 5:
This is why GPU spend is now the number one FinOps concern for AI-first organizations, ahead of general cloud cost for the first time (FinOps Foundation 2026).

Frame 6:
Granular tracking of tokens, LLM requests, and GPU use is the single most requested FinOps capability. Most stacks still can't do it.

Frame 7:
You can't defend a budget you can't split. Attribution has to happen at the query, before it collapses into the invoice.

Frame 8:
Assign your GPU and token spend before the bill does it for you. Talk to us now.

## Evidence used
- [E49]: GPU spend now the #1 FinOps concern for AI-first organizations, surpassing general cloud costs for the first time — Frame 5.
- [E50]: One banking query triggers orchestrator + 3 retrievers + 4 tool calls + 7 model invocations across providers; bill arrives at aggregated tenant level — Frames 1–4.
- [E48]: Granular AI spend monitoring (tokens, LLM requests, GPU utilization) is the #1 requested FinOps capability — Frame 6.

## Design note
Keep one running counter in a corner that ticks up with each fan-out (1 query, then 15 events), then in Frame 4 collapse everything into a single flat invoice line so the loss of detail is the visual. Monochrome data-viz look, one accent color for the counter.