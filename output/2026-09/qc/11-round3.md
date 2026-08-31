# Editor's memo — Post 11 (explainer reel)

## Overall verdict: FAIL

One structural violation in the caption. Everything else holds up well, but the reframe is a hard fail.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Real-time" is literal and technical, not the banned figurative use. No filler copulas ("detects," "shuts down," "runs," "reaches" — all live verbs).

**S — Structures: FAIL.** The caption ends with a contrastive-negation reframe embedded in the slot angle: the framing "not a policy line" pattern surfaces directly in the caption's second sentence.

> "The kill switch has lived in a governance policy, never run against a live one."

This is the "X but not Y" reframe (§6.1) in disguise: it sets up the kill switch as a policy artifact that has never been operational, using the contrast as the payload rather than stating the positive claim. The contrast isn't correcting a specific fact, number, date, or scope — it's rhetorical setup. The slot angle itself carries "not a policy line," and the writer imported that framing into the copy. Fix required.

Checked everything else: no triple bursts, no rule-of-three closers, no "This is" unveilings, no cliffhanger pivots, no amputated slogan tags. Frame 7 ("your platforms, your ownership model, your escalation path") is a rule-of-three list but it's three concrete engineering nouns, not a punchy closer — that's allowed, it's specific.

**M — Metaphor: PASS.** No analogies, no metaphor setups, no banned verbs. "The clock runs" and "while the clock runs" is borderline idiom but reads as literal time pressure, not a banned metaphor family. Acceptable.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics in body, caps, or em dashes. Explainer reel is 8 frames (spec allows 6–8). Each frame is one line of VO. Frame word counts are all comfortably short. The ≤25-word carousel cap doesn't apply to reels, but frames are compact anyway.

**E — Evidence: PASS.** Every claim traces:
- "35% ... couldn't immediately shut down a rogue agent" → [E20]. Correct figure, correct population (executives). Good.
- "Control Tower reached GA in August" → [E7]. Correct.
- "kill switches now reach agents running outside ServiceNow ... for the first time" → [E9]. Correct, and "for the first time" is directly supported by the ledger wording.
- "across AWS, Azure, and GCP" → [E7]. Correct.
No invented specifics, no CONFLICT figures stated as single numbers, no merged composites.

**O — One thing: PASS.** The post argues: the kill switch is now a runtime platform capability you can operate across clouds. One idea, no "and." Ladders to the big idea (operating what you bought) and matches the slot job exactly.

**L1 — Interchangeability: PASS.** Swap ServiceNow Control Tower for a generic tool and the copy breaks — the cross-platform kill switch reaching outside its own platform "for the first time" is a specific, named capability. Not swappable.

**L2 — CTO respect: PASS.** No wince. The manual-shutdown sequence in Frames 2–3 is concrete and true to how a security lead actually experiences the problem. The Frame 7 honesty ("the work is wiring it in") reads like an engineer, not a marketer.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands in Frame 6: the control runs at runtime, stopping an agent mid-action while it's still executing. A CTO who filed "kill switch" under policy checkbox realizes it's now an operable runtime control across clouds. That's the slot's job, delivered.

**R — Rhythm/human: PASS.** Frame lengths vary, VO sounds like speech, opens on a hard fact with no throat-clearing, CTA lands in the slot register. Not metronomic. One minor note below.

## Edit notes

The draft fails on one mechanical structure violation. Fix only the caption; leave the frames alone.

Rewrite the caption's second sentence. Current:

> "The kill switch has lived in a governance policy, never run against a live one."

This is a contrastive reframe (policy artifact vs. live agent) used as rhetoric. Replace with a direct positive statement of the same fact. Options:

- "Most kill switches exist as a line in a governance policy. Control Tower now runs one against a live agent in real time, including agents outside its own platform across AWS, Azure, and GCP."

Wait — that still leans on the same contrast. Cleaner: cut the setup entirely and state what the capability now does.

- "35% of executives admit they couldn't immediately shut down a rogue agent. Control Tower now detects and stops a rogue agent in real time at runtime, including agents running outside its own platform across AWS, Azure, and GCP."

That removes the "has lived in policy / never run live" reframe and leads with the capability. The [E20] stat carries the problem; the [E9]/[E7] capability carries the answer. No rhetorical contrast needed.

Minor improvable weakness (not a fail): Frames 2 and 3 both describe the manual-shutdown pain and slightly overlap. Consider tightening Frame 3 or merging its "across systems they don't fully control" point into Frame 2, freeing a frame — but this is optional; 8 frames is within spec.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Fix the caption only; frames are clean. The caption's second sentence — 'The kill switch has lived in a governance policy, never run against a live one.' — is a banned contrastive-negation reframe (§6.1): it uses the policy-artifact vs. live-agent contrast as rhetorical payload, not to correct a fact/number/date/scope. Delete it and state the capability directly. Replacement: '35% of executives admit they couldn't immediately shut down a rogue agent. Control Tower now detects and stops a rogue agent in real time at runtime, including agents running outside its own platform across AWS, Azure, and GCP.' This keeps the [E20] stat as the problem and the [E9]/[E7] capability as the answer without any 'not X, but Y' framing. Do not import the slot angle's 'not a policy line' phrasing into body copy. Optional tightening: Frames 2 and 3 overlap on manual-shutdown pain; fold Frame 3's 'across systems they don't fully control' into Frame 2 if you want to reclaim a frame, but 8 frames is within spec so this is not required."}
```