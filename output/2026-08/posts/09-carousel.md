<!-- QC: PASS after 1 round(s) -->

# Post 9 — 2026-08-19 — carousel
**Angle:** GPU spend is now the top FinOps concern for AI-first organizations, yet 44% still lack cloud-cost visibility, and the platform's own tools don't attribute agentic spend to a team.

## Caption
GPU spend just became the number one FinOps concern for AI-first companies, ahead of general cloud costs for the first time. The catch: one agentic query fans out into calls no dashboard ties back to a team. Here is why attribution breaks, and how to fix it before the invoice arrives.

## Copy

**Slide 1:**
GPU spend is now the top FinOps concern for AI-first organizations, ahead of general cloud costs for the first time. Your dashboard can't see most of it.

**Slide 2:**
44% of companies report limited visibility into cloud spend even with cost tools running. You bought the tooling. The spend still walks out unassigned.

**Slide 3:**
Here is where it breaks. One banking query triggers an orchestrator, 3 retrievers, 4 tool calls, and 7 model invocations across providers. The bill lands as one aggregated tenant number.

**Slide 4:**
No team owns that number. So no team defends it in planning. Granular monitoring of tokens, LLM requests, and GPU utilization is the single most requested FinOps capability for a reason.

**Slide 5:**
AI cost management is also the number one skill gap, with 58% of practitioners prioritizing it in the next 12 months. The tools you licensed don't close it. The attribution layer under them does.

**Slide 6:**
Get a FinOps baseline that assigns spend before the invoice does. Start the six-week baseline now. Get in touch.

## Evidence used
- [E49]: GPU spend now #1 FinOps concern for AI-first organizations, surpassing general cloud costs for the first time — slide 1.
- [E47]: 44% report limited visibility into cloud expenditure despite cost-management tools — slide 2.
- [E50]: one banking query triggers orchestrator + 3 retrievers + 4 tool calls + 7 model invocations across providers, billed at aggregated tenant level — slide 3.
- [E48]: granular AI spend monitoring (tokens, LLM requests, GPU utilization) is #1 requested capability; AI cost management is #1 skill gap, 58% prioritizing next 12 months — slides 4 and 5.

## Design note
Slide 3 is the anchor: lay the attribution chain as a single query at top splitting into the 7 model calls, ending in one grey lump labeled "one bill." Keep the type plain and the numbers large; let the fan-out do the visual work.