# QC Report — 2026-07

14/15 posts passed independent QC.

## Needs human attention

- Post 11: still failing after 3 rounds (see qc/11-round3.md)

## Facts flagged for human verification before publishing

- Post 01: E9: Oracle Age of AI launch date (June 18, 2026) and projects-as-MCP-servers framing is single-source, Strength Medium — confirm before publish.
- Post 02: E9: Oracle Integration 'Age of AI' June 18 2026 launch and projects-as-MCP-servers framing — single-source, Strength Medium; confirm before publish
- Post 08: E9 (Oracle Integration MCP servers) is single-source, Strength Medium — draft correctly keeps Oracle to a general 'standard across' claim in Frame 1 and does not attach specific MCP detail to it; confirm the general inclusion is acceptable before publish.
- Post 10: Slide 5 is 27 words (>25 cap); trim to 'Logging, access boundaries, evaluation records, an owner per agent. Build it before the auditor asks.' (21 words) before publishing.
- Post 11: Oracle Integration projects-as-MCP-servers claim (E9, single-source, Strength Medium) before any reader-facing naming of Oracle in slide 2
- Post 12: E9 (Oracle Integration 'Age of AI' launch) is single-source, Strength Medium in the ledger; the draft's 'four platforms shipped' count depends on it. Confirm Oracle Integration reached GA in the same June window before publishing.

## Per-post results

- Post 01: PASS, 2 round(s)
- Post 02: PASS, 1 round(s)
- Post 03: PASS, 2 round(s)
- Post 04: PASS, 3 round(s)
- Post 05: PASS, 1 round(s)
- Post 06: PASS, 1 round(s)
- Post 07: PASS, 2 round(s)
- Post 08: PASS, 1 round(s)
- Post 09: PASS, 2 round(s)
- Post 10: PASS, 3 round(s)
- Post 11: NEEDS HUMAN, 3 round(s) — final failed checks: S, E
- Post 12: PASS, 1 round(s)
- Post 13: PASS, 3 round(s)
- Post 14: PASS, 3 round(s)
- Post 15: PASS, 1 round(s)

---

## Post-run evidence audit (fresh-context, full corpus cross-check)

Two independent auditors traced every factual claim in all 15 final posts, the strategic
brief's 72-entry evidence ledger, the creative brief, and the calendar back to the raw
digest corpus. Findings, all corrected in place before delivery:

- Posts 05 and 07 attached Forrester's 41/33/26 root-cause breakdown (which belongs to
  the "22% of shipped deployments show negative ROI" statistic) to the separate "88% of
  pilots fail" statistic. Both slides now carry the correct pairing; the calendar angle
  for post 05 was corrected the same way.
- Post 02 overstated ServiceNow's June GA as spanning IT, HR, and finance; corpus
  supports IT AI specialists only. Corrected.
- Post 09 read Gartner's "3.4x more likely to achieve high effectiveness in their
  governance programs" as an AI-ROI figure; passage rewritten to the supported claim.
  "3,235 organizations" corrected to "3,235 enterprise leaders."
- Post 13 stated four platforms at GA; Oracle's release is a launch on a single
  [verify]-flagged source. Now "three at GA, plus Oracle's launch."
- Post 15 invented a "FinOps reported into finance in 2023" framing; corpus says 61%
  already reported to the CTO/CIO in 2023. Beat 2 rewritten to the exact figures.
- Post 06 softened to "84% of tech executives haven't fully operationalized." Post 10's
  27-word slide trimmed to the editor's suggested 21-word version. Post 11's two
  editor-prescribed fixes applied (slide 4 negation removed, Oracle dropped from slide 2).
- Ledger: E66 qualifier restored, E28 attributed as NEURA's own claim, week attributions
  corrected on E21, E24, E45, E46, E51.

No invented statistics, sources, or events were found anywhere. The remaining human
checks are the [verify] flags above, chiefly the single-source Oracle E9 item.

Prompts were hardened after this audit: prompts/4-draft.md and prompts/5-qc.md now
explicitly forbid and check for base-population transplants (a real number attached to
the wrong statistic), which was the one error pattern QC missed.
