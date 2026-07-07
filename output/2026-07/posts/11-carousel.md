<!-- QC: NEEDS HUMAN after 3 round(s) | verify: Oracle Integration projects-as-MCP-servers claim (E9, single-source, Strength Medium) before any reader-facing naming of Oracle in slide 2 -->
<!-- Editor's two prescribed fixes (qc/11-round3.md) have been applied verbatim below: slide 4 negation removed, Oracle dropped from slide 2. Give slides 2 and 4 a final read. -->

# Post 11 — 2026-07-17 — carousel
**Angle:** Traditional IAM and RBAC cannot keep pace with short-lived agents spanning hundreds of services, so identity for agents is now its own engineering problem.

## Caption
MCP won the protocol war, which means external agents can now touch your workflow runtime directly. Your IAM was built for two identity types: people and long-lived services. An agent is a third type that exists for one invocation and spans dozens of services in that window. Here is why identity for agents is now a distinct engineering problem, and what a security architect has to build for it.

## Copy

Slide 1:
Your IAM governs people and services. An external agent is neither. It spins up, touches dozens of services, and is gone before your access review runs.

Slide 2:
MCP is now standard across ServiceNow and Salesforce. ServiceNow's Action Fabric opens the workflow runtime to external agents. Salesforce hosts MCP servers Claude and ChatGPT query directly.

Slide 3:
So the identity you govern is short-lived and spread across hundreds of services at once. Traditional IAM and RBAC were not built for that speed or spread.

Slide 4:
An agent's scope shifts per task, per data source, per invocation. RBAC binds permissions to a role, and here that role never holds still long enough to review.

Slide 5:
Identity engineering is the work here. Every agent needs its own credential, scoped to one task, expiring on completion, logged to a system that can answer who touched what.

Slide 6:
Rebuild identity for agents now. Get in touch.

## Evidence used
- [E43]: ServiceNow Action Fabric opens the workflow runtime to external agents via GA MCP Server (slide 2).
- [E45]: Salesforce-hosted MCP servers GA, queryable by external agents like Claude and ChatGPT (slide 2).
- [E47]: Traditional IAM and RBAC can't keep pace with short-lived agents across hundreds of services (slides 1, 3, 4).
- Note for reviewer: the Oracle side of the MCP claim (slide 2) rests on E9, which is single-source. [verify: Oracle Integration projects-as-MCP-servers claim before publish.]

## Design note
Six clean slides, one idea per slide, dark background with a single accent color for the load-bearing phrase on each (agent, MCP, short-lived, role model, credential). Keep type large and the slide sparse so the sentences read as full thoughts, not fragments.