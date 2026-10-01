# Editor's Memo — Post 15 (case-study carousel)

**Overall verdict: FAIL.** One hard structure violation (S) plus a framing problem the slot explicitly warns against. The evidence handling is clean and the voice is mostly right, but the draft trips the contrastive-negation ban and leans on a "case study" label it doesn't earn.

## Per-check results

**V — Vocabulary: PASS.** No banned words. "Standard," "posture," "discipline," "integration work" are all clean and precise.

**S — Structures: FAIL.**
- Slide 5: "so building it is integration work in a regulated estate ... one hand configuring every platform to the same line" — the full thought here is a reframe. More damning, Slide 5 opens "This posture lives in the space between the three products" — a **"This is / This posture" unveiling opener** (§6.6). Lead with the subject, not the demonstrative-as-reveal.
- The slot angle itself contains "delivery work rather than a product you can buy." The draft renders this on Slide 5 as integration work, which is fine, but the caption states it as **"and where that posture has to be built by hand"** — acceptable. The sharper problem is Slide 1's "That gap is where the audit risk lives, and that gap is the work" — this is an **amputated/compressed reframe cadence** ("X is where the risk lives... X is the work") riding on anaphora. It reads as slogan compression, not a plain sentence. §6.9 territory.

One clear hit is enough. S fails.

**M — Metaphor: PASS.** "The seam," "the space between," "one line" are literal spatial descriptions of an integration topology, not figurative metaphor families. The design note's "thin line labeled one posture" is literal diagram instruction. Acceptable.

**F — Formatting: FAIL.** Body copy uses **bold** on every slide label ("**Slide 1:**", "**Slide 2:**", etc.) and on the caption header. §4 bans bold in body copy. The slide labels are scaffolding, not body — a borderline call — but the caption/copy structure carries bold markers that would need stripping. More importantly, check the word counts:
- Slide 1: ~35 words. **Over 25. FAIL.**
- Slide 4: ~27 words. **Over 25. FAIL.**
- Slide 5: ~34 words. **Over 25. FAIL.**

Three slides blow the ≤25-word cap. F fails hard.

**E — Evidence: PASS.** This is the draft's strongest check. Every claim traces: the Harness (E4), Control Tower (E7), Unity Catalog tool-call logging and RBAC default (E11) are all stated within ledger scope. No invented figures. The author correctly declined to cite a specific client engagement and flagged the present-tense-method framing instead of fabricating a case. Schellman (E18) is used as context, not quoted as a number — correct. No CONFLICT figures touched. Clean.

**O — One thing: PASS.** The post argues one thing: the cross-platform seam between governed agent platforms is closable only as integration work, not as a purchased product. Ladders cleanly to the big idea.

**L1 — Interchangeability: PASS, narrowly.** The three named platforms and their specific control planes (Harness, Control Tower, Unity Catalog tool-call logging) are load-bearing. Swap them and the sentences break. Good specificity.

**L2 — CTO respect: WEAK PASS.** The content is credible and the one-posture argument is real. But the slot calls this a **case-study carousel**, and there is no case. There is no estate named, no before/after, no measured result, no scope. A CTO reading a "case study" that contains zero evidence of a case will feel the gap. The author's own note admits it: "written as present-tense method ... not a specific past client engagement." That is a method explainer wearing a case-study label. A technical executive will clock the mismatch.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment lands on Slide 3/5: the posture that governs the seam physically cannot live inside any one platform because it exists in the space between them, which is why no vendor can sell it. That is the big idea's payload and it's delivered.

**R — Rhythm/human: WEAK.** Slides 1 and 5 are the longest and most slogan-flavored; the anaphora on Slide 1 ("that gap... that gap") reads as manufactured punch. Otherwise the slides sound like compressed speech, which is right for the format.

## Edit notes

1. **Fix the slot/format mismatch first.** This is sold as a case-study carousel but contains no case. Either (a) get a real anonymized engagement from the author ("a regulated medical-device manufacturer running agents across Salesforce, ServiceNow, and Databricks") with one concrete before/after detail and a [verify: real client engagement] flag, or (b) if no real case exists, the slot should be reclassified — but as written it cannot ship as a case study. Flag this to the human reviewer.

2. **Kill the Slide 1 reframe cadence.** Replace "That gap is where the audit risk lives, and that gap is the work" with a plain statement under 25 words. Suggested: "The audit risk lives in that gap between the three policies. Closing it is the work no vendor ships." Count words and trim to ≤25.

3. **Rewrite Slide 5's unveiling opener.** Drop "This posture lives in the space between..." Lead with the subject: "The posture sits between the three products, so building it is integration work. Thirty years of regulated-sector integration, one hand configuring every platform to the same line." Then cut to ≤25 words.

4. **Cut Slides 1, 4, 5 to ≤25 words each.** Compress by removing words, not by chopping into fragments. Slide 4 is close — trim "written once and mapped into each platform" to "written once, mapped into each."

5. **Strip bold** from all slide labels and the caption header in the body copy per §4.

6. **Resolve the Slide 1 "three governance layers that never agreed on one rule."** Fine as is, but ensure it doesn't drift into the contrastive "never X" pattern elsewhere once rewritten.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["Confirm whether a real anonymized client engagement exists to justify the case-study format; if so, add one concrete before/after detail with [verify: real client engagement]. If not, the slot's case-study classification cannot be satisfied by this present-tense method copy."],
 "edit_notes": "1) Slot/format mismatch: sold as a case-study carousel but contains no case (author admits present-tense method). Either supply a real anonymized engagement with one before/after specific and a [verify] flag, or escalate the format mismatch to human review — do not ship as a case study as written. 2) Slide 1: remove the reframe/anaphora cadence 'That gap is where the audit risk lives, and that gap is the work.' Replace with a plain statement ≤25 words, e.g. 'The audit risk lives in that gap between the three policies. Closing it is the work no vendor ships.' 3) Slide 5: remove the 'This posture lives in the space between...' unveiling opener (§6.6). Lead with the subject: 'The posture sits between the three products, so building it is integration work. Thirty years of regulated-sector integration, one hand configuring every platform to the same line.' Then trim to ≤25 words. 4) Word-count fails: Slides 1 (~35), 4 (~27), and 5 (~34) exceed the 25-word cap. Compress by cutting words, not fragmenting the voice. On Slide 4 trim 'written once and mapped into each platform' to 'written once, mapped into each.' 5) Strip all bold markers from slide labels and the caption header (§4). 6) After rewriting, re-scan Slide 1's 'three governance layers that never agreed on one rule' to ensure it does not become a 'never X' contrastive construction."}
```