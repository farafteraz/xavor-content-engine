# Post 11 — 2026-07-17 — carousel
**Angle:** Traditional IAM and RBAC cannot keep pace with short-lived dynamic agents, so identity for agents is now its own engineering problem.

## Caption
MCP won the protocol war, which means external agents can now touch your workflow runtime directly. Your IAM was built for humans and services that stay put. Agents don't. Here is why identity for agents is now a distinct engineering problem, and what a security architect has to build for it.

## Copy

Slide 1:
Your IAM governs people and services. An external agent is neither. It spins up, touches forty systems, and is gone before your access review runs.

Slide 2:
MCP is now standard across ServiceNow, Salesforce, and Oracle. ServiceNow's Action Fabric opens the workflow runtime to external agents. Salesforce hosts MCP servers Claude and ChatGPT can query directly.

Slide 3:
So the identity you have to govern is short-lived and dynamic, spanning hundreds of services at once. Traditional IAM and RBAC were not built for that speed or that spread.

Slide 4:
RBAC assumes a role you assign once and audit later. An agent's scope changes per task, per data source, per invocation. The role model has nothing to bind to.

Slide 5:
This is identity engineering, not a policy checkbox. Every agent needs its own credential, scoped to one task, expiring on completion, logged to a system that can answer who touched what.

Slide 6:
Rebuild identity for agents now. Get in touch.

## Evidence used
- [E43]: ServiceNow Action Fabric opens the workflow runtime to external agents via GA MCP Server (slide 2).
- [E45]: Salesforce-hosted MCP servers GA, queryable by external agents like Claude and ChatGPT (slide 2).
- [E47]: Traditional IAM and RBAC can't keep pace with short-lived dynamic agents across hundreds of services (slides 1, 3, 4).

## Design note
Six clean slides, one idea per slide, dark background with a single accent color for the load-bearing phrase on each (agent, MCP, short-lived, role model, credential). Keep type large and the slide sparse so the sentences read as full thoughts, not fragments.