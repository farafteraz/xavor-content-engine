# Post 7 — 2026-10-13 — article
**Angle:** The EU AI Act's full penalty regime is live, fines reach €35M or 7% of turnover, and the Commission's information requests target HR, credit, and medical-triage workflows that run across several systems, where the weakest link is the handoff between them.

## Copy

### The audit you're sure you'd pass runs across four systems

The European Commission sent its first formal information requests to more than 30 AI companies on September 1. The targets tell you where this is going: resume screening, credit assessment, medical triage. Not model cards. Not single systems. Decisions. And every one of those decisions moves through several platforms before anyone acts on it.

Take a hiring decision. A candidate's resume lands in one system, gets scored by an agent in a second, routed through a workflow in a third, and logged in a fourth. Each of those platforms ships its own governance now. Salesforce has its Trusted Enterprise AI Harness. ServiceNow has the AI Control Tower and the AI Gateway. Snowflake logs lineage and token usage. Databricks restricts agent scope through Unity Catalog. Inside each estate, the controls are real and they work.

The regulator does not read your estate one platform at a time. An inspector follows the candidate. They ask who made the decision, on what data, with what human in the loop, and whether you can produce the log that proves it. That path crosses the seams between your systems, and the seam is the one place no vendor's control plane reaches. The Harness governs what happens inside Salesforce. It has nothing to say about what Snowflake did to the data before it arrived, or what ServiceNow did with the output after it left.

That is the gap the penalty regime now has a price for. The full enforcement regime is live, with fines up to €35M or 7% of global annual turnover for high-risk violations. Those numbers were written to make the risk register move. For a company with €15B in turnover, 7% is a billion euros against a handoff nobody owns.

Here is the uncomfortable part. Confidence is usually highest exactly where cross-system control is weakest. A team that has configured the Harness correctly, locked down Unity Catalog, and stood up the Control Tower will feel audit-ready, because each of those projects closed cleanly and each produced a dashboard that reads green. The dashboards are honest. They just stop at the vendor's edge. The HR decision the inspector is tracing does not.

So the real question is not whether any single platform is compliant. It is whether you can reconstruct a full cross-platform decision on demand: the data that fed it, the agent that scored it, the person who could have overridden it, and the log that survives scrutiny months later. Most organizations have never tested that end to end, because no procurement motion ever required them to. You buy platforms one at a time. You govern them one at a time. The decision runs through all of them at once.

The Act gives you the structure to check your own work. It names seven things every high-risk system must have: risk management, data governance, logging, transparency, human oversight, cybersecurity resilience, and post-market monitoring. Read those as properties of a decision rather than a platform and the gaps surface fast. Logging inside Salesforce is not logging of the handoff from Snowflake. Human oversight configured in ServiceNow does not prove a person could have stopped the decision upstream, where the credit model actually ran. Each pillar has to hold across the full path, not in one system that happens to own one leg of it.

This is where thirty years of regulated-sector integration earns its keep. We configure the Harness, the Control Tower, and Unity Catalog to one posture, so a single decision carries one consistent record of control from the first data pull to the final action. Not three green dashboards that each tell the truth about a third of the story. One record an inspector can follow without hitting a wall at a vendor boundary.

The deadline is not theoretical and it is not next year. Enforcement is current, the requests are out, and the inspectors are reading the kind of workflows most Fortune 500 operations run every day across EU-exposed functions. The companies that fare well will be the ones who stopped grading their systems and started grading their decisions.

Run your EU readiness against the seven pillars, scored across every platform a high-risk decision touches, not platform by platform. Get in touch.

## Evidence used
- [E24]: Fines up to €35M or 7% of global annual turnover for high-risk violations; used for the penalty framing and the €15B/7% example.
- [E25]: September 1 information requests to 30+ companies; targets of resume screening, credit assessment, medical triage. [verify: sourcing for the "first wave of inspections" and named authorities looked thin in the digest — I kept the claim scoped to the information requests to 30+ companies and dropped the named-authority detail, per the territory caution.]
- [E28]: The seven pillars (risk management, data governance, logging, transparency, human oversight, cybersecurity resilience, post-market monitoring); used to structure the self-check section and the CTA.
- Platform governance named products (Trusted Enterprise AI Harness, AI Control Tower, AI Gateway, Unity Catalog, Snowflake lineage/token logging) drawn from E4, E7, E8, E9/E10, E11 to ground the seam argument.
- [verify] repeated: E25 named authorities and "first wave of inspections" framing — not stated in the copy; claim held to the information requests only.

## Design note
Header image: a single decision path drawn as one unbroken line passing through four labeled platform boxes, with the gaps between boxes highlighted rather than the boxes themselves. Keep it monochrome with one accent color on the seams only.