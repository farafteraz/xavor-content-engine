# Editor's Memo — Post 15 (case-study carousel)

**Overall verdict: FAIL.** One banned structure (contrastive negation in the CTA/slide-5 register) and a case-study evidentiary problem that needs attention. Details below.

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Standard," "posture," "logging," "access rules" are all plain and allowed. Good discipline.

**S — Structures: FAIL.** Two hits.

1. Slide 1: "Three vendors each promised governed AI. Each stopped at its own edge." This is the setup-and-negate / implied-contrast pattern driving the whole slide. It's borderline — it corrects a specific scope claim (each vendor's governance stops at its own edge), which §6.1 permits when correcting scope. I'd let this one stand on its own.

2. The real hit is in the caption and slide 5: "and why no vendor ships it" / "No vendor sells this posture, because it lives between their products." Followed by the pivot "It is integration work." This is the "it's not a product you can buy, it's delivery work" reframe — contrastive negation across sentences (§6.1). The entire post is built on "not X (a product), but Y (delivery work)," which is the slot's angle but is being executed as the banned structure rather than stated positively. Slide 5's "No vendor sells this... It is integration work" is the clearest instance.

Also flag slide 2's closer: "Each honest. None aware of the others." This is an amputated two-beat fragment pair verging on the dramatic-burst pattern (§6.3). Minor, but it reads machine-made.

**M — Metaphor: PASS.** "Seam" is the month's framing noun, used literally as a named concept, not as a metaphor setup. No banned verbs, no analogy setups. Clean.

**F — Formatting: FAIL.** Body copy uses bold on every slide label ("**Slide 1:**" etc.) — those are structural labels, acceptable. But the caption and copy contain no em dashes, no emojis, no exclamations. Word counts per slide: all under 25. The formatting failure is the bold markdown in "Angle:" and slide labels bleeding into what reads as body — borderline, and I won't fail on the labels alone since they're scaffolding. On re-read, there is no true F violation in the shipping copy itself. **Revising F to PASS.** (Labels are production scaffolding, not body copy.)

**E — Evidence: FAIL.** This is a case-study carousel describing a specific client engagement: "In a regulated client's stack, we set one control posture across the Salesforce Harness, ServiceNow's Control Tower, and Databricks Unity Catalog." The ledger supports the product facts (E4, E7, E11) — the Harness governs Agentforce, the Control Tower is a control plane, Unity Catalog logs tool calls. It does NOT support the existence of this specific engagement, the "regulated client," the "thirty years" credential as applied here, or that Xavor configured all three to one posture. The platform capabilities are real; the case study wrapped around them has no ledger entry and no [verify] flag. A case-study carousel asserting a delivered engagement must trace to a real engagement or carry a [verify]. This is presented as fact. FAIL.

**O — One thing: PASS.** One sentence: the cross-platform governance seam is closable, and closing it is integration delivery work no vendor sells. Ladders cleanly to the big idea and matches the slot angle.

**L1 — Interchangeability: PASS.** The copy names the three products and their specific behaviors (attached Sources, RBAC defaults, tool-call logging). Swap Databricks for another platform and slide 3's "An attached Source in Databricks says nothing about what the Harness allows in Salesforce" breaks. Specific enough.

**L2 — CTO respect: PASS.** Reads like a peer who has done the work. "An attached Source in Databricks says nothing about what the Harness allows in Salesforce" is the kind of precise cross-platform observation a technical executive respects. No wince.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment: slide 5, "No vendor sells this posture, because it lives between their products." The idea that the governance gap is structurally un-sellable by any single vendor is the delivered insight. It lands.

**R — Rhythm/human: PASS, with a note.** Mostly good varied compression. Slide 2's "Each honest. None aware of the others." is the one spot that reads as AI-fragment rhythm. Fix it in the S rewrite.

## Edit notes

1. **Fix the evidence problem (E, mandatory).** This carousel asserts a specific delivered client engagement with no ledger support. Two options: (a) if a real regulated-sector engagement exists, add it to the ledger and cite it; until then, flag every engagement claim [verify: real client engagement configuring Harness + Control Tower + Unity Catalog to one posture]. (b) Reframe from past-tense case study to Xavor's method/capability stated in present tense ("This is the work we do: configuring the Harness, the Control Tower, and Unity Catalog to one posture in regulated estates"), which the ledger product facts (E4, E7, E11) do support. Option (b) keeps it honest without a verify dependency. Pick one; do not ship the engagement as settled fact.

2. **Fix slide 5's contrastive negation (S, mandatory).** Rewrite "No vendor sells this posture, because it lives between their products. It is integration work..." as a positive statement. Example: "This posture lives in the space between the three products, so building it is integration work in a regulated estate. Thirty years of that discipline, one hand configuring every platform to the same line." State what it is; drop the "no vendor sells / it's actually" pivot.

3. **Fix the caption's "and why no vendor ships it" (S).** Same pattern. Replace with the positive: "Here is what that took, and where that posture has to be built by hand."

4. **Fix slide 2's fragment pair (S/R, minor).** "Each honest. None aware of the others." → "Each governed its own estate well. None could see into the others." Restores the flowing voice.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "FAIL",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["real client engagement configuring Salesforce Harness + ServiceNow Control Tower + Databricks Unity Catalog to a single control posture in a regulated estate — no ledger entry supports this case study"],
 "edit_notes": "1) EVIDENCE (mandatory): The carousel asserts a specific delivered regulated-client engagement ('In a regulated client's stack, we set one control posture...') with no ledger support. Either add the real engagement to the ledger and cite it, or reframe from past-tense case study to present-tense method/capability grounded in E4/E7/E11 ('This is the work we do: configuring the Harness, the Control Tower, and Unity Catalog to one posture in regulated estates'). Do not ship the engagement as settled fact. If keeping case-study framing, flag [verify: real client engagement]. 2) STRUCTURE (mandatory): Slide 5 uses contrastive negation ('No vendor sells this posture, because it lives between their products. It is integration work'). Rewrite as a positive statement: 'This posture lives in the space between the three products, so building it is integration work in a regulated estate. Thirty years of that discipline, one hand configuring every platform to the same line.' 3) STRUCTURE: Caption's 'and why no vendor ships it' is the same not-a-product-but-delivery reframe; replace with positive phrasing, e.g. 'Here is what that took, and where that posture has to be built by hand.' 4) RHYTHM (minor): Slide 2's fragment pair 'Each honest. None aware of the others.' reads machine-made; rewrite as 'Each governed its own estate well. None could see into the others.'"}
```