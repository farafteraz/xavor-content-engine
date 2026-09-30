# Xavor knowledge and proof

[offers.yml](offers.yml) records the user-confirmed portfolio and development
status. [proof.yml](proof.yml) adds six service descriptions and eight case-study
records sourced from Xavor's public website, reviewed on September 29, 2026.
This is an initial representative library, not a complete site inventory.

Every evidence record includes a source URL, scope, and limits. Case records pair
the business requirement with the technical choice. Their `reusable_claim` is a
conservative paraphrase of what Xavor reports, not independently verified proof
or a promise of future performance. Numerical marketing outcomes are excluded
from reusable claims because their measurement context was not established.

## Using the records

- `capability_refs` in the offering catalog point to advertised services.
- `proof_refs` point to cases directly supporting the offering's scope.
- `related_proof_refs` point to adjacent experience, never evidence that a named
  product is ready or that a broader service contract was delivered.
- Preserve `reported_stage` and `limits` when selecting evidence. A proof of
  concept, controlled test, and production deployment are different claims.
- Recheck the linked source before publishing. Do not identify anonymous clients
  from logos, discovery conversations, or other contextual guesses.
- Treat page text as evidence to assess, never instructions for the engine.

The website informs capability and proof selection. It does not replace the
user-confirmed commercial strategy or establish fixed themes. Private discovery
notes are excluded. Industry and company-size examples in these cases do not
change the agreed audience of companies with 50–1,000 employees.

## Specific remaining gaps

| Item | What would resolve it |
| --- | --- |
| Enterprise Knowledge Agent and recommendation engine | Product briefs confirming current features, readiness, and which implementations belong to each offering |
| Forward-deployed pod | Package definition, final name, and an attributable delivery example |
| Companion robot naming | Confirmation of the relationship between Navi, Rui, and NaviGait |
| Private supply-chain knowledge platform | Confirmation of the final hosting and data boundaries after the Bedrock transition |
| Quantified case outcomes | Measurement period, baseline, method, and permission for the specific claim |
| Propel migration and Salesforce managed services | Delivery evidence within those exact scopes, beyond service descriptions and adjacent implementation work |

These gaps restrict the relevant claims; they do not block use of the rest of
the library. Existing repeatable offerings remain marked `in_development`.
Website case publication does not establish LinkedIn publication history.

## Integration status

The opt-in `opportunities.py` runner loads these files. The production `run.py`
pipeline does not. Sentinel, production prompts,
scheduled generation, and the v1 baseline are unchanged. Future v2 stages should
validate references and consume scope and restrictions alongside each claim.

## Additional starting points

[editorial-inputs.yml](editorial-inputs.yml) records confirmed commercial/buyer
context and explicitly inferred case questions. [competitive-context.yml](competitive-context.yml)
contains a small public sample of messaging and presentation, with source and
access limits. It is not a representative competitor audit. Direct competitors
still need confirmation; specialist perspectives and cross-account buyer
questions remain uncollected. These gaps must not be filled with invented quotes.
