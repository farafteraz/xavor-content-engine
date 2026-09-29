# V2 marketing foundation

[marketing-strategy.yml](marketing-strategy.yml) records the user's current
commercial direction, audience, and communication standards.
[../knowledge/offers.yml](../knowledge/offers.yml) defines the offering IDs and
records development status and unresolved descriptions.

Both files are planning inputs for the future v2 strategy stages. The current
`run.py` does not load them. Adding these files leaves production behavior,
Sentinel, prompts, and the preserved v1 baseline unchanged. API credits are
unnecessary for reviewing this foundation.

## Source and scope

The source is the user's direct business direction in this task. The portfolio,
commercial roles, buyer dynamics, and advanced audience standard are explicit
user inputs. Editorial implementation guidance and the forward-deployed pod's
classification are labeled separately where they remain interpretations.
Company size is confirmed as 50-1,000 employees.

The commercial direction replaces the earlier assistant proposal to rank
Enterprise Knowledge Agent and Agentic AI as primary and platform services as
secondary. Platform and specialist services are the usual commercial priorities;
AI services support positioning and relevance across the business; repeatable
AI offerings are intended to drive the AI business as they develop. No ordering
within the groups or fixed campaign allocations have been agreed.

Discovery examples helped explain buyer sophistication and decision-making.
Their details, names, figures, and proposed use cases are excluded here. They
establish no mandatory themes or public proof. Evidence review and approval are
required before any customer reference can enter publishable material.

## Integration requirements

Before connecting this foundation to v2 generation:

- Load the strategy and offering catalog together; validate referenced offering IDs.
- Apply the confirmed audience and commercial direction to v2 stages.
- Resolve the old Fortune 500 audience assumptions in `brand/style-spec.md`,
  `brand/about-me.md`, and `prompts/1-strategic-brief.md`,
  `prompts/2-creative-brief.md`, `prompts/4-draft.md`, and `prompts/5-qc.md`.
  Preserve the approved writing mechanics while adapting the audience context.
- Keep advanced evaluation of technologies and approaches within the technical
  reader's role. Technical readers also make buying decisions.
- Treat statements in existing prompts and illustrative style examples as
  material requiring verification before inclusion in the proof library.
- Preserve `in_development` status until readiness is explicitly confirmed.
- Leave missing geography, readiness, package details, proof, and publication
  records unspecified. The YAML open items describe each gap.

The next implementation step is a sourced Xavor knowledge and proof library.
Public claims and published-content history must have traceable evidence before
they can guide the opportunity generator and critic.
