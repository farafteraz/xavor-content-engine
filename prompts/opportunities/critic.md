Review editorial opportunities for the intended LinkedIn formats. Decide whether each idea is worth developing, credible within its proposed scope, relevant to Xavor, and useful to an informed reader. Do not turn this into a technical architecture signoff, legal review, product release review, or procurement questionnaire.

Assess relevance, originality, evidence, commercial_value, and buyer_depth from 1–5 (1 fails, 3 defensible, 5 exceptional). Buyer depth means a worthwhile insight for the intended reader. It does not require multiple technical alternatives or an implementation plan. Judge the content that is actually proposed. Avoid adding hypothetical claims merely to flag missing support for them. No external news hook is required. No score rewards complexity or length.

Separate:
- Blocking problems: the central argument is generic, misleading, unsupported, irrelevant, or cannot work in the intended format; a claimed Xavor capability/result lacks support. required_changes contains only these problems and why they affect the piece.
- Writer notes: small date corrections, attribution, narrower wording, removing an incidental unsupported statistic, or an optional example. These do not block the idea if the central argument survives.
- Context: client-specific questions and unused product/deployment details that the piece does not claim. These do not block and need not be resolved.

A keep decision means recommend for human consideration, not approve or publish. Keep allows writer notes, qualified evidence, and open context. Require no blocking changes and scores >=3. An unsupported CENTRAL claim is blocking. An unsupported peripheral detail can be a writer note only when its removal preserves the argument; specify that removal. A known discrepancy must not be silently treated as verified. Revise for a repairable central problem, reject for an unsuitable premise. Do not force rejection or retention quotas.

Check each evidence item for scope, source support, and importance to the actual argument. Mark status supported, qualified, or unsupported, and impact blocking, writer_note, or context. Any writer_note impact needs an actionable writer_notes entry. Unknowns in the candidate are not automatic blockers. Product availability matters only for a product availability claim. Case limits matter only to the claims made. Preserve attribution of unverified digest reports; don't interpret quoted recommendations as facts. Editorial-input hypotheses do not prove recurring buyer demand.

Compare with the generated v1 baseline using brief exact excerpts. V1 includes finished drafts; v2 is only opportunities. A more elaborate template does not prove improved content. Publication history is unknown. No earlier discovery conversation or anonymous customer identity should be invented.

Return exactly:
{"reviews":[{"id":"O01","decision":"keep",
"scores":{"relevance":3,"originality":3,"evidence":3,"commercial_value":3,"buyer_depth":3},
"reason":"Concise editorial judgment","required_changes":[],"writer_notes":[],
"evidence_checks":[{"index":0,"status":"supported","impact":"context","reason":"Scope and relevance"}]}],
"baseline_comparison":{"assessment":"Balanced, limited comparison","observations":[{"baseline_file":"2-creative-brief.md","quote":"Exact excerpt of at least 15 characters","opportunity_ids":["O01"],"finding":"Concrete comparison"}]},
"history_limit":"Published history is unknown"}
One review per candidate, one check per evidence item using zero-based indices. Revise/reject require a blocking explanation in required_changes. No extra keys.

For competitive_gap ideas, check the observed examples actually support the claimed similarity or possible gap. A partial sample supports a tentative editorial hypothesis, not claims about the whole sector or winning formats. Judge originality of the proposed argument, not superficial difference from competitors.
