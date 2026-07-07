# Post 5 — 2026-07-08 — carousel
**Angle:** The 88% pilot failure rate traces to unclear success criteria, missing data access, and evaluation drift, all fixable engineering and governance problems.

## Caption
Your stalled pilot probably didn't die on model quality. It died on the three things nobody scoped before the first sprint. Here is what the failure data actually says.

## Copy

Slide 1:
88% of agent pilots never reach production. The reason is rarely the model. It's what happened before anyone wrote a prompt.

Slide 2:
Forrester traced the failures. 41% died on unclear success criteria. 33% on insufficient tool or data access. 26% on evaluation drift. None of those is a model problem.

Slide 3:
Unclear success criteria means the pilot had no number to hit. When "better support" replaces "resolve 70% of tier-one tickets," nobody can tell you if it worked.

Slide 4:
Missing data access means the agent can see the demo data and nothing else. Production data lives behind permissions, stale ETL, and systems the pilot never touched.

Slide 5:
Evaluation drift means the thing you measured in week one stopped mapping to the thing that matters by week twelve. No standing evaluation, no way to catch it.

Slide 6:
Fix your scoping before your next pilot now. Get in touch.

## Evidence used
- [E14]: 88% of agent pilots fail to reach production (slide 1); used as the headline failure rate.
- [E15]: Root-cause breakdown, 41% unclear success criteria, 33% insufficient tool/data access, 26% evaluation drift (slides 2–5).
- [E16]: Not directly cited; the governance-tooling multiplier informed the framing that these are governance-fixable problems but the specific number was left out to keep the deck focused.

## Design note
Six clean slides on a single dark ground, one accent color for the three percentages on slide 2 so they read as a set. Keep the numbers large and the supporting line small underneath; no icons, no stock robots.