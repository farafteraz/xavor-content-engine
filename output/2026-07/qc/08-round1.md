# Editor's Memo — Post 8 (MCP surface, explainer reel)

**Overall verdict: PASS**

The draft is disciplined. It argues one thing, it grounds its specifics in the two solidly evidenced platforms, and it handles the Oracle [verify] problem honestly rather than papering over it. I went hunting for the usual tells and found no hard violations.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Attack surface" is a literal security term, not figurative "landscape." "Standing services" is precise. No "seamless," "robust," "leverage," etc.

**S — Structures: PASS.** I read every sentence pair for reframes and other tells.
- Frame 4: "The easy connection and the wider attack surface are the same decision." This is an *equation*, not a contrastive negation. It's the actual insight of the piece stated positively. Passes.
- Frame 6: "So the open question is no longer which protocol wins. It is how you secure the MCP servers you already turned on." I checked this hard — it looks like a "not X, but Y" reframe. But it corrects a specific scope (the protocol question is settled; the open question moved), and it's sourced directly to E46's framing ("MCP declared the winning protocol; the open question is securing MCP servers"). This is contrast correcting a real fact/scope, which §6.1 explicitly permits. Passes.
- No triple bursts, no rule-of-three closer, no cliffhanger pivot, no "This is" unveiling, no amputated slogan tags, no puffery, no meta commentary.

**M — Metaphor: PASS.** "Doorway" / "doorways" / "entry point" appears in Frames 2, 4, and the caption. This is borderline. It's a light spatial figure for network access, but it's the plain-English word a security engineer uses for an exposed endpoint, it's shorter than the literal alternative, and it reads normally aloud. Not a banned setup ("think of it as," "it's like") and not a banned family. Under an explainer-reel budget I'll allow it. No journey/engine/map metaphors, no banned verbs.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Longest frame (Frame 5) is 21 words. All frames under 25. Explainer reel is 7 frames — spec says 6–8. Within range.

**E — Evidence: PASS.** Every specific claim traces cleanly:
- Frame 2 → E43 (Action Fabric, GA MCP server, every Now Assist SKU). Exact.
- Frame 3 → E45 (SObject, Data 360, Tableau; Claude, ChatGPT, Cursor). Exact.
- Frames 1 & 6 → E46 (MCP winning protocol; securing servers is the open question). Exact.
- Frame 5 → E47 (IAM/RBAC can't keep pace with short-lived agents across hundreds of services). Exact.
- Oracle: correctly held to a general "standard across" statement in Frame 1 and kept out of the specific claims, because E9 is single-source [verify]. This is exactly the right call. No invented figures, no CONFLICT figures stated as single numbers.

**O — One thing: PASS.** The post argues: standardizing on MCP made cross-platform agents easy and widened the external attack surface in the same move. One idea, matches the slot angle, ladders to the operability gap (capability arrived everywhere; the constraint moved to what you can govern and secure).

**L1 — Interchangeability: PASS.** Swap MCP for another protocol and the piece breaks — the named servers (Action Fabric, Salesforce-hosted MCP), the specific tool sources, and the IAM/RBAC failure mode are all MCP-specific. Not generic.

**L2 — CTO respect: PASS.** No wince. The IAM/RBAC point and the "same decision" framing are the kind of thing a security engineer nods at.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" line is Frame 4: the ease of connection and the widened attack surface are not two consequences to weigh against each other, they're one decision. An integration lead who thinks of MCP as a productivity win gets shown it's also a security event, inseparably. That's the intended jolt.

**R — Rhythm/human: PASS.** Frame lengths vary (short openers, a longer Frame 5). Real transitions ("So the open question..."). Opens on a fact, no throat-clearing. CTA lands in register. Not metronomic, not staccato-hype.

## One improvable weakness (non-blocking)

Frame 1's "Cross-platform agents got easy overnight" leans slightly toward marketing cadence; "overnight" is doing rhetorical work the evidence doesn't strictly need. Consider "Cross-platform agents got easy fast" or cutting the sentence to tighten — but this is a style nicety, not a failure.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["E9 (Oracle Integration MCP servers) is single-source, Strength Medium — draft correctly keeps Oracle to a general 'standard across' claim in Frame 1 and does not attach specific MCP detail to it; confirm the general inclusion is acceptable before publish."],
 "edit_notes": ""}
```