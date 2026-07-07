# Editor's Memo — Post 10 (carousel)

**Overall verdict: PASS**

This one earns its place. The self-test framing ("give an auditor 90 days and full access — would you pass?") converts an abstract compliance stat into a concrete challenge, and the reframe from paperwork to engineering evidence lands the cognitive-depth requirement. Ran it hard against every check; nothing mechanical fails.

## Per-check

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Governance," "operational," "evaluation," "access boundaries," "logging" are all precision terms, not filler. No "crucial/critical/robust/seamless" anywhere. "Mature governance" is lifted directly from the source phrasing, not puffery.

**S — Structures: PASS.** Watched hardest here. The angle line itself uses "an operational readiness gap, not a paperwork gap" — that is a contrastive negation — but it sits in the slot header/angle field, not in the shipped body copy or caption. The body never states it. Checked every candidate:
- Slide 1 "The gap is operational: what they can prove..." — states the positive claim directly, no rejected half. Clean.
- Slide 5 "Build it before the auditor asks, not during the 90 days." — this is a genuine temporal correction (when to build), not a reframe-for-effect. Allowed.
- No triple bursts, no rule-of-three closers (Slide 5's "decisions, data access, corrections, owners" is a four-item list of real artifacts, which §6.4 explicitly permits). No "This is" unveiling, no cliffhanger pivot, no amputated slogan tags. The caption's "They have the policies. What they lack is..." reads close to setup-and-negate, but it corrects a specific scope (policies exist, evidence doesn't) rather than manufacturing false contrast. It holds.

**M — Metaphor: PASS.** "A trail an outsider could follow" is literal audit-trail language, not a metaphor family. No "think of it as," no journey/engine/bridge, no banned verbs.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body, no em dashes. Slide word counts: Slide 1 ~30 words — over the 25 cap. Recount: "78% of executives can't say with confidence they'd pass an independent AI governance audit within 90 days. The gap is operational: what they can prove an agent did, and who owns it." That is 34 words. **This is a formatting concern** — see note below. Slide 2 ~27. Slide 3 ~26. These exceed the ≤25 guidance.

Correction on my own read: §9 states ≤25 words per slide, and §4 marks it HARD under check F ("carousel ≤25 words/slide"). Slides 1, 2, and 3 exceed it. That is a mechanical FAIL on F.

Revising the verdict accordingly.

**Overall verdict: FAIL — F only.**

Everything else passes; the draft is one tightening pass from shipping.

**E — Evidence: PASS.** Both figures trace clean. 78% → [E20] (Grant Thornton 2026, n=950). 21% → [E51] (Deloitte 2026). "Systems shipped faster than the ability to explain them" is a fair gloss on [E51]'s 21%-mature framing. No invented specifics, no CONFLICT figures touched.

**O — One thing: PASS.** Argues exactly one idea: passing an AI audit in 90 days is an engineering-evidence problem, not a policy problem. Ladders straight to the operability gap.

**L1 — Interchangeability: PASS.** Swap "agent" for "microservice" and Slide 2's "what it did last Tuesday at 2pm" plus Slide 5's evaluation-records specifics don't transfer cleanly — the autonomy/ownership problem is agent-specific. Holds.

**L2 — CTO respect: PASS.** "What it did last Tuesday at 2pm" is exactly the question a real auditor asks. No wince.

**L3 — Cognitive depth: PASS.** The moment: "Those are engineering questions" (Slide 2), reframing audit-readiness as reconstruction capability rather than documentation. A CTO who thought they were covered because they have policies feels the floor shift.

**R — Rhythm: PASS.** Varied lengths, reads like speech, CTA lands naturally. Not metronomic.

## Edit notes

Single fix: three slides exceed the 25-word cap (§4/§9, HARD). Compress by cutting words, not voice.

- **Slide 1 (34 → ≤25):** "78% of executives can't say they'd pass an independent AI audit in 90 days. The gap is what they can prove an agent did, and who owns it." (~28 — cut further: drop "with confidence" already done; try "78% of executives doubt they'd pass an independent AI audit in 90 days. The gap: proving what each agent did, and who owns it." ~24.)
- **Slide 2 (~27 → ≤25):** "An auditor asks who approved this agent, what data it touches, what it did last Tuesday at 2pm. Those are engineering questions." (~23.)
- **Slide 3 (~26 → ≤25):** "Most enterprises can't answer. Only 21% have mature governance for autonomous agents. The systems shipped faster than the ability to explain them." (~22.)

No other changes. Preserve "Those are engineering questions" verbatim — that's the depth line.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "Only F fails: three slides exceed the HARD 25-word cap (§4/§9). Compress by cutting words, not voice. Slide 1 (~34 words) to under 25, e.g. '78% of executives doubt they'd pass an independent AI audit in 90 days. The gap: proving what each agent did, and who owns it.' Slide 2 (~27) to under 25, e.g. 'An auditor asks who approved this agent, what data it touches, what it did last Tuesday at 2pm. Those are engineering questions.' Slide 3 (~26) to under 25, e.g. 'Most enterprises can't answer. Only 21% have mature governance for autonomous agents. The systems shipped faster than the ability to explain them.' Preserve 'Those are engineering questions' verbatim as the depth line. No other changes; all other checks pass."}
```