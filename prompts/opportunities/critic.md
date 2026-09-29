Independently assess every candidate against the original input context. Do not assume the generator's conclusions are correct. You have the original corpus, strategy, proof records, and generated v1 control sample. The baseline is a comparator, never evidence for market facts or proof of publication.

For every candidate evaluate:
- relevance: a specific buying situation in the confirmed audience and portfolio;
- originality: substantive argument, distinct from generic commentary, the other candidates, and the supplied baseline;
- evidence: accurate attribution, scope, inference, product maturity, and proof stage;
- commercial_value: a credible Xavor role and useful buyer discussion, without inventing commercial priorities;
- buyer_depth: meaningful business consequences and evaluation of technical alternatives.

Score each dimension 1–5: 1 fails, 2 weak, 3 defensible, 4 strong, 5 exceptional. These are editorial judgments, not measured outcomes. Do not average away a failing dimension. Judge the actual thesis, why_now, alternatives, why_xavor, and next_step, not just the attached citations. For every evidence item explain whether the cited source supports the claim and whether the claim supports the wider argument. Treat a true quotation used to justify an unsupported leap as qualified or unsupported. Check numbers, populations, dates, causality, available-versus-in-development products, on-premises assertions, and advertised-versus-delivered scope. A supplied digest is not independent verification; attributed analysis can be supported, but unqualified assertions may need verification.

Decide keep, revise, or reject. Keep means recommended for HUMAN REVIEW, never approved. Keep requires all dimensions >=3, all evidence checks supported, no required changes, and no unresolved factual prerequisites. Revise if an argument can be repaired with a precise change or evidence request. Reject generic, duplicative, unsupported, or commercially irrelevant candidates. Reject all if necessary; do not preserve a quota. Do not rewrite candidates or add new ones.

Compare to v1 using concrete cited excerpts from the baseline files and candidate IDs. Discuss gains AND remaining weaknesses where the evidence warrants them. Distinguish a better opportunity hypothesis from demonstrated improvement in finished content; no new posts exist. Do not declare success merely because fields are more structured. Note where a baseline argument is already strong. State the publication-history limitation explicitly.

Return exactly:
{
  "reviews": [{
    "id": "O01", "decision": "keep",
    "scores": {"relevance": 3, "originality": 3, "evidence": 3, "commercial_value": 3, "buyer_depth": 3},
    "reason": "Specific assessment",
    "required_changes": [],
    "evidence_checks": [{"index": 0, "status": "supported", "reason": "Scope and entailment assessment"}]
  }],
  "baseline_comparison": {
    "assessment": "Balanced assessment of opportunities versus the control sample, with limitations",
    "observations": [{"baseline_file": "2-creative-brief.md", "quote": "Exact baseline excerpt of at least 15 characters", "opportunity_ids": ["O01"], "finding": "Specific similarity, improvement, or remaining weakness"}]
  },
  "history_limit": "State the limits on assessing novelty from generated rather than confirmed published history"
}
Include one review per candidate and one evidence check per evidence item using zero-based indices. Status is supported, qualified, or unsupported. Rejected/revise entries must have required_changes explaining repair or why to abandon. Cite only the provided baseline filenames and exact excerpts.
