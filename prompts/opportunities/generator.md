Generate up to eight distinct, defensible opportunities using the August corpus and persistent strategy. Fewer is acceptable when evidence is thin; return at least one candidate for critique. Do not impose a single campaign thesis or allocate calendar slots. Consider the usual platform/specialist priorities, cross-business AI positioning, and repeatable offerings' development status. State a reason if a commercially relevant angle cannot be supported, using its unknowns rather than filling gaps.

Each candidate must advance a specific argument for a buyer decision. Connect the business requirement to the technical choices determining the outcome, including at least two plausible approaches and their tradeoffs. Make why_now relative to August 2026, not today's date. Explain Xavor's credible role using the supplied evidence, with accurate stage and scope. next_step is a discussion or evaluation the proposed content could invite; never imply an unready product can be bought. unknowns lists factual prerequisites needing resolution before proceeding, and may be empty for a fully qualified argument.

Support every external factual assertion in the candidate with an evidence item. Each item has a source ID, a narrow claim, and an exact supporting excerpt copied from that referenced input. Corpus quotes come from the paragraph text. Library quotes come from a string in the case or capability record. Quotes must be at least 15 characters, brief, and verbatim. Label basis as source_report or inference. Each candidate needs both a corpus signal and a case or capability record. Keep source attribution inside the claim. A quote from a corpus marketing recommendation is not proof of delivery.

Return this shape, using actual values rather than these descriptions:
{
  "opportunities": [{
    "id": "O01",
    "title": "Specific opportunity title",
    "thesis": "One arguable, qualified thesis",
    "primary_reader": "Role and buying situation",
    "business_decision": "Outcome, constraint, and decision",
    "technical_decision": "Implementation choice and business consequence",
    "alternatives": ["Approach one and tradeoff", "Approach two and tradeoff"],
    "why_now": "Dated corpus signal and implication for August",
    "why_xavor": "Evidence-supported role tied to the offering",
    "offering_ids": ["Exact offering ID"],
    "evidence": [{"kind": "corpus", "ref": "C0001", "claim": "Attributed claim", "basis": "source_report", "quote": "Exact input excerpt"}, {"kind": "case", "ref": "Exact case ID", "claim": "Scoped Xavor claim", "basis": "source_report", "quote": "Exact record excerpt"}],
    "unknowns": [],
    "next_step": "Appropriate buyer discussion or evaluation"
  }]
}
Use kind capability for service-description evidence. IDs must be unique O01, O02, etc. There is no access to earlier model reasoning or to the v1 baseline in this stage.
