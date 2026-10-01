# Editor's Memo — Post 1, "Five control planes, and nothing between them"

**Overall verdict: FAIL** (one hard-structure violation; everything else is strong).

This is a genuinely good piece. The seam idea lands, the handoff transaction walks cleanly across all five planes, and the evidence is clean. But there's a clear "This is" unveiling that the spec bans outright, and that's a mechanical FAIL I can't wave through. The fix is one sentence.

---

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Governed," "control plane," "runtime," "lineage" are precision, not jargon. "Mature" is used as the survey's own word, fine. No "crucial/critical/leverage/seamless/robust" anywhere. Clean.

**S — Structures: FAIL.** One clear hit:

- "This is the part the vendor conversation skips, because no vendor is selling it." — §6.6, sentence opening with "This is" as an unveiling. Lead with the subject.

Checked the rest carefully for cross-sentence reframes, since this draft leans on contrast as its whole argument. The contrasts here survive because they correct specific scope, which §6.1 explicitly permits:
- "Isolation is not the dangerous state. The dangerous state is the agent that talks to three others..." — this reads as a reframe, but it's correcting a factual claim about *which* condition carries the risk, grounded in the E61 isolation figure. It states a positive claim (the connected agent) with specifics. Allowed.
- "The gap is not false confidence inside each platform. It is the quiet assumption that five well-governed estates add up to one governed enterprise." — same: this narrows the scope of a real gap (the 74/27 delta from E18), not a rhetorical not-X-but-Y. Allowed, but it's riding the edge; see the note below.
- "They do not add up." — short declarative, not a burst. Fine.
- "Not 'is this platform governed' but 'is this path governed end to end'" — this is a genuine redefinition of the unit of analysis, tied to a concrete object (the path). Allowed under the fact-correction carve-out.

No triple bursts, no rule-of-three closers, no amputated slogan tags, no puffery, no meta commentary. The single "This is" is the only structural failure.

**M — Metaphor: PASS.** "The seam" / "the space between systems" is the month's literal governing concept, not a decorative analogy — it names a real ungoverned location (the handoff). "The seams between them... belong to you" is literal ownership language. No banned setups, no journey/engine/ecosystem families, no metaphor verbs. "Threading through" appears only in the design note, not body copy.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Word count ~770, under 1,000. Headings in sentence case.

**E — Evidence: PASS.** Every claim traces:
- Harness same day as Fin close → E4. ✓
- Control Tower five verbs → E7. ✓
- AI Gateway v3.4, one policy set across MCP → E8. ✓
- Genie restricted to attached sources, Unity Catalog logs each tool call → E11. ✓
- Snowflake restricted session scope + data lineage → E9. ✓
- Aras agentic layer on Innovator PLM → E12. ✓
- 12 agents, 20 by 2027, half isolated → E61. ✓
- AvePoint, 750 IT leaders, 88.4% breach, data leakage most common → E22. ✓ (50.1% is the leakage figure; draft says "most common" without the number, accurate.)
- Schellman, 500+ leaders, 74% / 27% → E18. ✓
No CONFLICT figures touched (the PwC/E15 mess is avoided entirely). No E25/E26/E38/E58 [verify] items used. No composite claims, no denominator drift. Clean.

**O — One thing: PASS.** The post argues: every platform's governance stops at its own edge, so the handoffs between platforms are the ungoverned surface. One idea, no "and." Matches the slot angle exactly and ladders straight to the big idea (the seam).

**L1 — Interchangeability: PASS.** You cannot swap the technologies. "The Control Tower cannot see what the Databricks model was allowed to read" names a specific cross-plane blind spot that only works with these named planes. The transaction walk (Salesforce → ServiceNow → Databricks → Snowflake) is load-bearing and specific.

**L2 — CTO respect: PASS.** "Each logged its own leg. None logged the handoff" is the kind of precise observation a technical executive respects. The piece credits the vendors ("built by people who understand their own estate better than any outside integrator ever will") instead of disparaging them, which reads as confidence, not content marketing.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment is explicit and well-placed: "A leak is a handoff problem. Something moved from where it was governed to where it was not, and no single control plane was watching the move." Reframing the 88.4% breach stat as a *seam* phenomenon rather than a platform failure is the insight the big idea wanted. Also: "An auditor does not grade your platforms one at a time."

**R — Rhythm/human: PASS.** Varied sentence lengths, real transitions, opens on a hard fact with no throat-clearing. "It arrived in ninety days" lands. CTA grows out of the final paragraph naturally. Not metronomic, not staccato. Sounds signed by a human.

---

## Edit notes

One required fix, one optional tightening.

**Required (S):** Rewrite the sentence "This is the part the vendor conversation skips, because no vendor is selling it." Lead with the subject, drop the "This is" unveiling. Suggested replacement: "No vendor is selling the fix, because no vendor's conversation reaches this far." Or more directly: "The vendor conversation skips this entirely, because no vendor sells the thing that spans their edges." Either removes the §6.6 violation while keeping the beat. Keep the sentence that follows ("A platform's control plane is scoped to the platform by design.") untouched.

**Optional (polish, not a fail):** The two scope-correcting contrasts ("Isolation is not the dangerous state..." and "The gap is not false confidence...") are both legal but they sit close together and the piece leans on the same rhetorical move twice in adjacent paragraphs. If you want to lower the not-X-but-Y density, consider restating one of them as a flat declarative — e.g. open the audit paragraph with "The 74/27 gap is an assumption that five well-governed estates add up to one governed enterprise. They do not." That's a style call, not a rubric failure; ship it either way once the "This is" sentence is fixed.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "One required fix. Rewrite the sentence 'This is the part the vendor conversation skips, because no vendor is selling it.' — it violates S6.6 (sentence opening with 'This is' as an unveiling). Lead with the subject instead, e.g. 'The vendor conversation skips this entirely, because no vendor sells the thing that spans their edges.' Keep the following sentence ('A platform's control plane is scoped to the platform by design.') unchanged. Optional polish (not required to pass): the two legal scope-correcting contrasts in adjacent paragraphs ('Isolation is not the dangerous state...' and 'The gap is not false confidence...') repeat the same not-X-but-Y beat; consider recasting one as a flat declarative to lower the density, but this is a style call, not a failure."}
```