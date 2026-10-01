# Post 1 — 2026-10-01 — article
**Angle:** Every major platform shipped a governed agent runtime this quarter, and each governs only its own estate, which leaves the handoffs between them ungoverned.

## Copy

### Five control planes, and nothing between them

In one quarter, every platform you run put a governed agent runtime into general availability. Salesforce unveiled the Trusted Enterprise AI Harness the same day it closed Fin. ServiceNow brought its AI Control Tower forward as the place to discover, govern, secure, observe, and measure AI across the enterprise, with AI Gateway v3.4 enforcing one policy set across every MCP connection underneath it. Databricks restricted Genie Agents to explicitly attached sources and made Unity Catalog log each tool call. Snowflake shipped restricted session scope and agent data lineage. Aras put a governed agentic layer on top of Innovator PLM. If you had asked for this list a year ago, you would have been told it was two years out. It arrived in ninety days.

Each of these does what it claims. The Harness governs Salesforce agents inside Salesforce. The Control Tower governs ServiceNow. Unity Catalog governs what runs on Databricks. Every one of them is a real control plane, built by people who understand their own estate better than any outside integrator ever will. Read the release notes and you can see the care in them.

Now put them on the same org chart. A Salesforce agent resolves a case, then hands the enriched record to a ServiceNow workflow, which pulls a figure from a model running against Databricks, which reads a lineage-governed table in Snowflake. Four control planes touched one transaction. Each logged its own leg. None logged the handoff. The Harness has no opinion about what happens after the record leaves Salesforce. The Control Tower cannot see what the Databricks model was allowed to read. You have five governance postures and no single one that spans the path the work actually took.

This is the part the vendor conversation skips, because no vendor is selling it. A platform's control plane is scoped to the platform by design. That is not a flaw in the Harness or the Control Tower. It is the correct boundary for a product. The boundary only becomes a problem when you own five of them and the work crosses all five in a single task. The Salesforce 2026 Connectivity Benchmark puts the average company at 12 AI agents today, heading to 20 by 2027, with half of them already operating in isolation. Isolation is not the dangerous state. The dangerous state is the agent that talks to three others across three platforms, where the request is authorized at every stop and governed as a whole at none.

Most governance programs are still built as if the risk lived inside a system. So the question executives ask their platform owners is the wrong one. "Can Salesforce govern its agents" has a yes answer that tells you nothing, because the breach does not happen inside Salesforce. AvePoint's 2026 survey of 750 IT leaders found 88.4% had at least one agent-related security breach in the past twelve months, with data leakage the most common failure. A leak is a handoff problem. Something moved from where it was governed to where it was not, and no single control plane was watching the move.

The audit math follows the same shape. Schellman's 2026 survey of more than 500 U.S. leaders found 74% believe they could pass an AI compliance audit today, while only 27% are actually mature. The gap is not false confidence inside each platform. It is the quiet assumption that five well-governed estates add up to one governed enterprise. They do not add up. An auditor does not grade your platforms one at a time. The auditor follows a decision from input to outcome, and that decision does not respect your vendor boundaries.

What this asks of a technical executive is a different unit of analysis. Not "is this platform governed" but "is this path governed end to end," where the path is the real route a task takes across every runtime it touches. That posture is the one thing none of the five vendors ships, because none of them can see past their own edge. It has to be configured deliberately, across the Harness, the Control Tower, Unity Catalog, and the rest, to one standard, by one hand that treats the handoff as the object worth governing.

That is the work Xavor does. Thirty years of integration in regulated sectors means we have spent our career in the space between systems, where the data moves and the accountability blurs. The platforms are not the problem. The seams between them are, and they belong to you whether or not anyone sold them to you.

Map your cross-platform control gaps now. Get in touch.

## Evidence used
- [E4]: Salesforce Trusted Enterprise AI Harness, launched the day Fin closed.
- [E7]: ServiceNow AI Control Tower as the plane to discover, govern, secure, observe, measure AI.
- [E8]: AI Gateway v3.4 as runtime enforcement applying one policy set across every MCP connection.
- [E11]: Databricks Genie Agents restricted to attached sources; Unity Catalog logs each tool call.
- [E61]: Average company runs 12 agents, 20 by 2027, 50% in isolation.
- [E9]: Snowflake restricted session scope and Cortex Agent data lineage visibility.
- [E12]: Aras governed agentic layer on Innovator PLM.
- [E22]: AvePoint 2026, 750 IT leaders, 88.4% had an agent-related breach, data leakage most common.
- [E18]: Schellman 2026, 500+ leaders, 74% believe they'd pass an audit, 27% fully mature.

## Design note
Open on a clean diagram of five platform boxes, each with its own control-plane badge, and a single transaction line threading through all five with the handoffs between boxes left unshaded. Keep it schematic and quiet, one accent color for the ungoverned gaps only.