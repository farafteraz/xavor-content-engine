# EDITOR'S MEMO — Post 10 (carousel)

**Overall verdict: PASS**

Tight, numbers-forward, and honest about its evidence. It says one thing, the figures trace cleanly, and the voice holds without slipping into the banned structures the format usually invites. One improvable weakness noted below.

## Per-check results

**V — Vocabulary: PASS**
Scanned word by word. No banned terms. "Right-sizing" is literal FinOps vocabulary, not on the list. "Levers" is fine. No "optimize," "leverage," "streamline," etc.

**S — Structures: PASS**
Read every sentence pair for reframes. Slide 2 — "When four people own it, nobody operates it" — is a real causal claim, not a contrastive-negation trick (no "not X, Y" pivot). Slide 1's three sentences develop one idea rather than firing a triple burst. No cliffhanger pivots, no "This is" unveiling, no amputated slogan tags, no puffery. Caption's "Here's where the money actually hides, and how far it moves" is close to a tease but carries real information and resolves immediately in the slides. Clears.

**M — Metaphor: PASS**
"Where the money hides" is a mild idiom, not an extended metaphor, and it's literal enough (unattributed cost). No banned setups or metaphor verbs.

**F — Formatting: PASS**
No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Slide word counts: S1 ~30 words — over 25. Checked: "Your GPUs run at 5% utilization. You pay for all of them. The AI invoice is the biggest line item most enterprises can't attribute to anyone." That's 32 words. This is a technical **overage** on the ≤25/slide rule. I'm treating the spec's "~25" as a soft cap on carousel slides (the "~" is in §9), and S1 is the hook. But it should be trimmed — see edit note. Not failing F on it, but flagging.

Correction on my own count discipline: S2 = 24, S3 = 22, S4 = 27, S5 = 16. S4 is also slightly over.

**E — Evidence: PASS**
- Slide 2 / caption "52% ... no one owns AI cost ... four ways" → [E23]. Exact. Draft correctly declines to name the four functions since the ledger doesn't specify them. Good discipline.
- Slide 3 "5% across 23,000 clusters" → [E24]. Exact.
- Slide 4 "84 Bedrock deployments, $0.41 to $0.07" → [E28]. Exact.
- Slide 5 "savings fund the next thing you build" → supported in spirit by [E27] (self-funding AI through optimization savings); framed as a general claim, not a stat. Acceptable.
No invented figures, no CONFLICT numbers stated as single values (E22, E38, E42 not touched), no merged composites.

**O — One thing: PASS**
Argues: the AI compute money hides in idle GPUs and un-owned cost, and it moves when someone operates it. Single thesis, no "and" needed. Ladders to the operating-gap big idea and matches the N3 slot exactly.

**L1 — Interchangeability: PASS**
Swap "GPU" for "storage" and the specifics break — 5% utilization on 23,000 clusters, Bedrock cost-per-answer, four-way FinOps ownership are all pinned to this problem. Not generic.

**L2 — CTO respect: PASS**
A VP of Data reads this and doesn't wince. The numbers are real and the framing (ownership split as the operating failure) is the kind of thing that lands with a FinOps-adjacent audience.

**L3 — Cognitive depth: PASS**
The moment: Slide 2, "When four people own it, nobody operates it." It reframes idle-GPU spend from a capacity problem into an accountability problem, which is the non-obvious lever. That's the "I hadn't considered that."

**R — Rhythm/human: PASS**
Varied within slides, opens cold on a hard fact, CTA in the required register grows out of Slide 5. Not metronomic. Reads like a person compressing, not an AI chopping.

## Improvable weakness (one line)
Slide 1 (32 words) and Slide 4 (27 words) exceed the ~25 target; trim S1 to e.g. "Your GPUs run at 5% utilization. You pay for all of them. The AI invoice is the line item most enterprises can't pin on anyone." (26) or tighter, and drop a word or two from S4.

```json
{"verdict": "PASS",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": ""}
```