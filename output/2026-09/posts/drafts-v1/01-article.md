# Post 1 — 2026-09-01 — article
**Angle:** In one 30-day window ServiceNow, Databricks, Oracle, and Salesforce shipped governance control planes into platforms you already run, and owning them is a different job from operating them.

## Copy

### The control plane you didn't ask to operate

In one 30-day window, four platforms you already run shipped governance surfaces you never requested. Databricks Unity AI Gateway reached general availability on August 4, giving one entry point for every agent, model, and MCP call, with governance over spend, access, and security. ServiceNow AI Control Tower hit GA the same month with 30 new integrations across AWS, Azure, GCP, SAP, Oracle, and Workday, and something new: the ability to detect and shut down a rogue agent in real time, including outside its own platform. Oracle wired natural-language SQL and MCP into OCI Enterprise AI and Fusion Data Intelligence. Salesforce made Agentforce compile every agent to portable JSON under baseline security standards, and as of mid-July the New Agent button opens only the new governed builder.

Read the release notes together and a pattern appears. Your vendors stopped shipping features and started shipping control. You now hold kill switches, agent inventories, spend gateways, and audit surfaces across your stack. None of it arrived with an operator.

That is the part worth sitting with. A GA release is a capability, not a running function. Unity AI Gateway can govern every model call, but only if someone routes the traffic through it and reads what it reports. Control Tower can shut down a rogue agent, but only if someone owns the definition of "rogue," sets the threshold, and answers the escalation at 2 a.m. The button exists. The role behind the button does not.

The gap between those two states is where most enterprises now sit, and the numbers describe it plainly. Sixty percent of organizations deploy AI across departments, yet only 4 percent govern it at scale (Credo AI, 371 senior leaders). The deployment is real. The operating layer under it is mostly absent, and this month's releases just made that absence visible on your own dashboards.

There is a version of this that looks like progress and isn't. A team turns on Control Tower, connects the integrations, and files the project as done. The surface is live. But live and operated are different conditions. An operated control plane has a named owner, a decision boundary that says what the agent may and may not do without a human, an escalation path, and a metric that says whether it is working. Without those four things, you have bought the instrument panel and left the cockpit empty. The dashboard will faithfully show you the crash.

This is why owning the surface and operating it are two different jobs, and only one of them shipped in August. Ownership came free with the release. Operation is engineering work, and it is specific: you inventory every agent already running against the new gateway, you assign each one an owner and a decision boundary, you set the thresholds the kill switch fires on, you wire the escalation to a person, and you attach a number that tells you whether the whole arrangement earns its keep. That work does not appear in a release note because no vendor can do it for you. It depends on which agents you run, what they touch, and what your regulators expect.

The regulators are not waiting. EU AI Act enforcement went live on August 2, with the AI Office and national authorities now active. The control surfaces your vendors shipped are, in part, a response to that. But a governance surface you own and cannot operate is not compliance. It is a documented record that you had the tool and did not run it, which is a worse position than not having bought it at all.

None of this is an argument against the platforms. Xavor implements all four, and the surfaces they shipped this month are the right capabilities to hold. The point is narrower and more useful: the capability is now yours, and the operating function that makes it real is the piece still missing from most stacks. Between "we have Control Tower" and "we can prove which agents run, who owns them, and what they cost" sits a body of engineering work with an owner and a payback number attached.

That work is the job for Q4. Not more AI. The AI is already running. The task is to operate the control planes you already hold: inventory the agents, name the owners, set the boundaries, wire the kill switches to real thresholds, and put a number on it. Build the owner for the control planes you already hold. Get in touch.

## Evidence used
- [E1]: Unity AI Gateway GA August 4, single entry point, governance over spend/access/security.
- [E7]: ServiceNow AI Control Tower GA August 2026, extends governance across AWS, Azure, GCP.
- [E8]: Control Tower's 30 integrations across AWS/GCP/Azure/SAP/Oracle/Workday (used for the integration list).
- [E9]: Control Tower detects and shuts down rogue agents in real time, including outside its own platform.
- [E4]: Oracle NL-SQL and MCP toolset in OCI Enterprise AI.
- [E5]: Oracle Fusion Data Intelligence added MCP support.
- [E11]: Agentforce Builder GA, New Agent button opens only the new builder from mid-July.
- [E12]: Agentforce baseline security standards; every agent compiles to portable JSON.
- [E13]: 60% deploy AI across departments, only 4% govern at scale (Credo AI, 371 senior leaders).
- [E6]: EU AI Act enforcement live August 2, AI Office and national authorities active.
- [E44]: Every production agent needs a defined owner, decision boundary, escalation path, and success metric (used to frame the four-part operating definition).

## Design note
Set the headline in sentence case over a plain dark field with a single muted control-panel motif behind it, low contrast, no icons. Keep it text-forward so the article reads as an editorial piece, not a product page.