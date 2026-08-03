# Editor's Memo — Post 11 (static)

**Overall verdict: FAIL** — on one structure hit that recurs across the caption and on-image copy.

The evidence is clean, the idea is single and on-slot, and the piece respects the CTO reader. But it leans on a contrastive-negation reframe as its central rhetorical move, and it does so twice in nearly identical form. That is exactly the pattern §6.1 bans, and it triggers a mechanical FAIL.

## Per-check

**V — Vocabulary: PASS.** No banned words. "context layer" in the angle is spec language, not banned. "underneath/under" is literal, fine.

**S — Structures: FAIL.** Contrastive negation (§6.1), across sentence boundaries, appears twice:
- Caption: "The agent you're piloting doesn't fail on model choice. It fails on the data underneath it." — This is the "Not X. Y." pattern split across two sentences. The exception in §6.1 (contrast allowed only to correct a specific fact, number, date, name, or scope) does not apply; this is a rhetorical reframe of an abstraction, not a factual correction.
- Kicker: "Your agent doesn't fail on the model. It fails on the data it queries." — Same pattern again, restated. Two instances of the banned structure, and they are the load-bearing lines of the post.

**M — Metaphor: PASS.** No analogies or banned metaphor verbs. "sitting under" / "underneath" is literal physical positioning of a data layer beneath an application, not figurative in the banned sense.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, em dashes. Headings in the draft scaffolding (Caption, Copy, etc.) are template labels, not body copy. Caption is 3 sentences, within the 2–5 static range. No slide-word cap applies to a static.

**E — Evidence: PASS.** Every claim traces:
- 85% data-problem-before-AI-problem, Accenture (Manish Sharma), Snowflake Summit 2026 → [E33], stated exactly as the ledger holds it.
- Attribution line "Accenture, at Snowflake Summit 2026" → [E33]. Correct.
- Data-quality-as-top-concern framing informing the kicker → [E35]. Used as framing, not as a fabricated second statistic. No composite claim, no denominator drift, no CONFLICT figure misused.

**O — One thing: PASS.** The post argues: enterprises have a data problem before an AI problem, so the data layer decides whether agents work. One idea, matches the slot angle, ladders to "the layer under the platform."

**L1 — Interchangeability: PASS.** The claim is anchored to a specific named source, a specific number, and a specific failure mode (the agent queries bad data). You cannot swap the subject out and keep the sentence.

**L2 — CTO respect: PASS.** A data leader would not wince. The Accenture attribution and the specific reframing of "where the agent fails" reads as a peer observation, not vendor content.

**L3 — Cognitive depth: PASS, marginally.** The "I hadn't considered that" moment is the reattribution of agent failure from model choice to the data layer — the CTO who has been evaluating models realizes the model was never the variable. That lands. It is close to the slot's stated job, delivered rather than merely asserted.

**R — Rhythm/human: PASS.** Reads like speech, varied lengths, CTA lands naturally in the "now" register.

## Edit notes

The only defect is mechanical and fixable without touching the evidence or the idea. Kill the "doesn't fail on X, it fails on Y" construction in both places and state the positive claim directly.

- Caption second sentence: replace "The agent you're piloting doesn't fail on model choice. It fails on the data underneath it." with a direct positive statement of the same fact, e.g. "Your pilot's accuracy is decided by the data it queries, before you ever pick a model." State where the outcome comes from; do not stage a rejected alternative first.
- Kicker: it currently duplicates the caption's move and the caption's content. Either cut the kicker entirely (the headline plus a single direct body line may be enough for a static) or rewrite it as a direct claim that adds something the headline does not, e.g. "Model choice is downstream. The data your agent reads decides the answer." — but note "downstream" flirts with the same reframe, so prefer a plain construction: "The data your agent queries decides its answers." Do not reintroduce a "not the model / but the data" contrast in any form.
- After the rewrite, confirm the caption and the on-image kicker are not saying the identical sentence twice; give each a distinct job (caption = source and stakes; kicker = the operational consequence).

Everything else ships as-is.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Remove the contrastive-negation reframe (§6.1) that appears twice as the load-bearing copy. (1) Caption: replace 'The agent you're piloting doesn't fail on model choice. It fails on the data underneath it.' with a direct positive statement, e.g. 'Your pilot's accuracy is decided by the data it queries, before you ever pick a model.' (2) Kicker: it duplicates the caption's banned move and its content. Either cut the kicker entirely, or rewrite it as a plain positive claim that adds new information, e.g. 'The data your agent queries decides its answers.' Do not reintroduce any 'not the model / but the data' contrast in any disguise (no 'downstream' pivots either). Ensure caption and kicker do distinct jobs: caption carries source and stakes, kicker carries the operational consequence. Evidence, one-thing, and idea are all clean and must be preserved."}
```