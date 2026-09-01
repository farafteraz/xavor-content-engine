# Editor's memo — Post 15 (case-study carousel)

**Overall verdict: FAIL.** One hard structural violation on Slide 4 ("This is" unveiling opener), and a genuine miss on the format claim: this is billed as a case-study carousel but contains no case. Beyond the mechanical fail, that format gap weakens L2/L3. Details below.

## Per-check

**V — Vocabulary: PASS.** Scanned for banned terms. "mission-critical," "leverage," "seamless," etc. — none present. "return," "boundary," "meter," "attribution," "escalation" are all clean. No banned filler ("crucial/critical/important/significant") in body copy.

**S — Structures: FAIL.**
- Slide 4 opens: "This is engineering, and it's scoped." Direct §6.6 violation — sentence opening with "This is" as an unveiling. Lead with the subject.
- Slide 1 borderline: "You deployed the agents, and so did 97% of executives. Only 29% see real return, because the agents launched with no operating layer under them" — reads close to a setup-and-negate rhythm but the causal "because" clause is a genuine explanation, not a negate-the-setup pivot. Allowed.
- No triple bursts, no rule-of-three closer (the four-item list on Slide 3 is a real enumeration of four distinct requirements, permitted under §6.4). No amputated slogan tags.

**M — Metaphor: PASS.** "sits on top of," "under them," "floors" (factory floor) are literal, not figurative journey/engine/map families. No banned setups or metaphor verbs.

**F — Formatting: PASS.** Six slides. Word counts per slide: S1 ~30, S2 ~30, S3 ~30, S4 ~30, S5 ~28, S6 ~9. Several exceed the ~25-word target but the spec caps carousel at "~25 words each" as an approximate; none is egregiously over and all are full sentences in voice. No emojis, hashtags, exclamations, bold in body, em dashes. Flagging as a soft note, not a fail: tighten S1–S4 toward 25.

**E — Evidence: PASS.**
- 97% deployed / 29% ROI → E16. Exact. ✓
- 35% couldn't shut down a rogue agent → E35. Exact. ✓
- Four-part operating layer (owner, decision boundary, escalation path, success metric) → E50. Exact. ✓
- "88% of pilots stall short of production" is *not* stated — Slide 3 says "the pilot stalls short of production" as a general claim, not a number, so no E17 attribution needed. Clean. No invented figures, no CONFLICT figure stated as single number.

**O — One thing: PASS.** The post argues: every production agent needs an owner, boundary, escalation, and metric, and building that layer is one commissionable scope. Single thesis, matches the slot angle, ladders to the operator's gap.

**L1 — Interchangeability: PASS.** The four requirements (owner, decision boundary, escalation path, success metric) and the rogue-agent kill-switch consequence are specific to autonomous agents. Swap "agents" for "dashboards" or "microservices" and Slides 2–4 break. Anchored.

**L2 — CTO respect: FAIL (soft, judgment).** The prose would pass on its own. The problem is the format promise. The slot format is **case-study carousel**, and the spec (§9) defines that as a carousel that carries a case. There is no case here: no named deployment, no before/after, no customer, no result. It reads as a straight argument carousel wearing a case-study label. A CTO scanning for proof gets assertion ("we build it as one bounded scope") with no evidence Xavor has built it. That is the wince: the close of the month's proof arc should show the work, and this tells.

**L3 — Cognitive depth: PASS (thin).** The "I hadn't considered that" beat lands on Slide 2→3: the reframe from "who owns this agent?" (most floors have no answer) to "that unanswered ownership question is the same thing as the 35% kill-switch gap." Connecting unowned-agent to can't-kill-agent is the non-obvious move. It survives, but it's carried by one line.

**R — Rhythm/human: PASS.** Sentence lengths vary, real causal transitions ("because," "which is why"), reads like speech. CTA lands in register. No metronome, no throat-clearing opener. Slide 1 drops straight into the fact.

## Edit notes

Two fixes, one mechanical and mandatory, one to honor the format:

1. **Kill the "This is" opener on Slide 4 (mandatory, S fail).** Rewrite leading with the subject. For example: "The work is scoped like any engineering job: you assign the owner, wire boundaries into the agent, route escalation to a human, and set metrics a CFO will accept." Do not open any slide with "This is."

2. **Make it an actual case-study carousel (L2/format).** The slot format demands a case. Either (a) anchor Slides 2–5 to a concrete deployment from the ledger — the strongest available is a real production agent context, but note the ledger's case-grade material (Figure/BMW E28–E30, Agentforce/US Army E55, Salesforce Agentforce E54) is physical-robotics or vendor-product, not a Xavor governance engagement — so a fabricated Xavor case is off the table and must not be invented. Or (b) if no Xavor case exists in the corpus, the honest move is to reframe the "case" as the anatomy of a single production agent: pick one agent archetype (e.g. an invoice-approval agent), walk Slides 2–5 through what its owner, boundary at what dollar threshold, escalation to which human, and success metric actually look like in production. That gives the carousel a concrete spine instead of a general argument and earns the case-study label. Add a [verify] flag if any specific deployment detail is asserted.

3. **Tighten S1–S4 toward 25 words** by cutting connective words, not by chopping voice into fragments.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "FAIL", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["If any concrete production-agent deployment detail is added to satisfy the case-study format, confirm it against the corpus or mark it as illustrative; do not present an invented Xavor engagement as real."],
 "edit_notes": "1) MANDATORY (S fail): Rewrite Slide 4 to remove the 'This is engineering, and it's scoped' opener — §6.6 'This is' unveiling. Lead with the subject, e.g. 'The work is scoped like any engineering job: you assign the owner, wire boundaries into the agent, route escalation to a human, and set metrics a CFO will accept.' No slide may open with 'This is'. 2) FORMAT/L2: The slot format is case-study carousel but the draft carries no case — no named deployment, before/after, or result. The ledger has no Xavor governance case, so do NOT invent one. Instead give the carousel a concrete spine: pick one production-agent archetype (e.g. an invoice-approval agent) and walk Slides 2–5 through its actual owner, its decision boundary at a specific dollar threshold, its escalation to a named human role, and its success metric in production. This turns the general argument into a walkable anatomy and earns the case-study label. Mark any specific detail [verify] or flag it as illustrative. 3) SOFT: Tighten Slides 1–4 toward 25 words by cutting connective words, keeping full sentences, not fragments."}
```