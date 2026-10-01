# Editor's memo — Post 14 (Navi case-study carousel)

## Overall verdict: FAIL

The draft has a clean surface: no banned vocabulary, no em dashes, slide counts in range, and the seam framing ladders to the month's idea. But the slot asks this carousel to prove the physical-AI integration claim with built work — and the draft never shows the work. Worse, the carousel is nearly interchangeable with the week-4 generic "seam" argument. It fails L1 and L3, and R is weak. The evidence check has one concern worth flagging.

## Per-check

**V — PASS.** Scanned word by word. No banned terms. "posture" appears (Slide 5) but it isn't on the list and reads fine. "accountability," "boundary," "governance" all clean.

**S — PASS, barely.** I hunted for reframes. Slide 2 "The vendor governs the fleet. You still govern the floor, the data, and the rules it has to obey" is a contrast across sentences, but it corrects a specific scope (who owns what), which §6.1 explicitly permits. Slide 3 "no vendor owns it" and Slide 4 same — scope correction, allowed. "On Navi, we did" (Slide 4) is a short confirming beat, not a cliffhanger. No triple bursts, no rule-of-three closer (Slide 5 lists three real deliverables, which is a factual enumeration, not a punchy slogan). Clears the check.

**M — PASS.** "Between those two sides sits a boundary," "where accountability... actually lives," "engineer the join," "seam line" — these are literal spatial descriptions of a robot in a plant, not metaphor families. "seam" is the month's named concept, used literally here (a physical boundary on a plant floor). No banned setups or metaphor verbs.

**F — PASS.** No emojis, hashtags, exclamations, caps. Bold appears only in slide labels ("Slide 1:") and scaffolding, not body copy. No em dashes. Slide word counts: Slide 1 ~34 words — over the 25 cap. Let me recount: "Robotics raised $55.8B in 2026, nearly double the prior record. That capital builds robots. The engineering that makes one run inside your plant is a separate job, and it's the one we do." That's ~34 words. **Slide 1 exceeds 25.** Slide 2 ~32. Slide 5 ~30. Multiple slides blow the ≤25 cap.

Correction: F is a **FAIL** on the carousel word limit (§4, §9).

**E — PASS with one flag.** E45 ($55.8B, nearly double prior record) — supported, used correctly in caption and Slide 1. E51 (RaaS = fleet management, maintenance, 24/7 support) — supported, Slide 2 states it accurately. No invented figures. No Navi stats claimed, correctly. The "Evidence used" note says E48 was dropped; that's fine, the slot lists it but doesn't mandate all three. No conflict figures mishandled.

**O — PASS.** One idea: the integration layer between robot and running environment is engineering Xavor already ships. Matches the slot, ladders to the seam. No "and" needed.

**L1 — FAIL.** Swap "Navi" for any system integrator's robot deployment and the copy survives intact. "On Navi, we did" and "On Navi we built all three" are the only Xavor-specific lines, and they assert the work without showing a single concrete detail — no plant, no robot function, no integration specifics, no named embedded platform, no numbers. "edge inference on the device, embedded systems linking perception to action, and fleet governance holding the deployment to one posture" is a generic description of what physical-AI integration *is*, not what Xavor *did*. Replace Navi with "our robot" and nothing breaks. That is the interchangeability failure.

**L2 — borderline PASS.** A CTO wouldn't wince at the framing. But the payoff slides are thin enough that a skeptical CTO reads "On Navi, we did" and thinks "did what, exactly?" The respect is provisional and collapses into the L3 problem.

**L3 — FAIL.** The slot's job is to make a CTO believe the floor-integration gap is closable *because Xavor already built across it*. The "I hadn't considered that" moment should be a specific piece of Navi engineering that proves the seam is a buildable problem, not a funding problem. Instead the carousel restates the seam thesis (correct, but already said in week 4) and then asserts Navi exists without evidence. There is no sentence that delivers new cognitive depth about the integration itself. Naming three capabilities the reader already knows a robot needs is awareness-level, not insight.

**R — weak, near FAIL.** Read aloud, the slides are competent but the back half goes abstract exactly where it should get concrete. Slides 3 and 4 circle the same boundary idea twice ("no vendor owns it" / "where accountability actually lives") without advancing. The CTA lands fine. It doesn't read machine-made, but it reads like a thesis restatement wearing a case-study label.

## Edit notes

The core failure: this is billed as a case study and contains no case. Fix L1, L3, and F together by replacing abstraction with specific Navi engineering.

1. **Get the real Navi specifics from the brand corpus before rewriting.** You need at least two of: what environment Navi runs in (eldercare facility floor, per the big-idea corpus — Navi is Xavor's eldercare robot), what the edge inference actually does on-device (what it perceives and decides without round-tripping to cloud), what embedded systems it bridges, and what "one posture" fleet governance concretely enforces. One named integration detail with a number beats all six current slides.

2. **Collapse Slides 3 and 4.** They say the same thing twice (the boundary exists, nobody owns it). Merge into one slide, then spend the reclaimed slide on a concrete Navi detail.

3. **Rewrite Slide 5 to show, not list.** Replace "we built all three: edge inference..., embedded systems..., fleet governance..." with one specific instance: what Navi's edge inference decides locally, what embedded link it closed, what the fleet posture actually holds to. If the corpus gives a latency figure, a facility count, or a specific perception-to-action loop, use it. That is the "I hadn't considered that" slide.

4. **Cut every slide to ≤25 words.** Slide 1 (~34), Slide 2 (~32), Slide 5 (~30) all exceed. Compress by cutting words, not voice. Slide 1 example fix: "Robotics raised $55.8B in 2026, nearly double the prior record. That money builds robots. Making one run inside your plant is a different job, and ours." (~27 — still trim further.)

5. **Make Navi un-swappable.** After the edit, run the L1 test yourself: swap "Navi" for "our robot." If the slide still reads, it isn't specific enough yet.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "PASS", "M": "PASS", "F": "FAIL", "E": "PASS",
            "O": "PASS", "L1": "FAIL", "L2": "PASS", "L3": "FAIL", "R": "PASS"},
 "verify_flags": [],
 "edit_notes": "This is billed as a case study but contains no case. Fix L1, L3, and F together. (1) Pull real Navi specifics from the brand corpus: Navi is Xavor's eldercare robot, so name the environment (facility floor), what its on-device edge inference actually perceives and decides without cloud round-trips, which embedded systems it bridges, and what the fleet governance posture concretely enforces. One named detail with a number beats all six current slides. (2) Collapse Slides 3 and 4 — they state the 'boundary exists, nobody owns it' idea twice; merge to one slide and reclaim the other for a concrete Navi detail. (3) Rewrite Slide 5 to show, not list: replace the generic 'edge inference on the device, embedded systems linking perception to action, and fleet governance holding the deployment to one posture' with a specific instance of what Navi decides locally, what embedded link Xavor closed, what the posture holds to — ideally with a latency, facility-count, or loop specific. This is the 'I hadn't considered that' slide the slot requires. (4) Cut all slides to <=25 words: Slide 1 (~34), Slide 2 (~32), Slide 5 (~30) exceed the cap; compress by cutting words, not by chopping voice. (5) Run the L1 swap test: replace 'Navi' with 'our robot' — if any slide still reads cleanly, it is not specific enough. Keep E45 in caption/Slide 1 and E51 in Slide 2; both are used correctly. Preserve the CTA."}
```