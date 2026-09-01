<!-- QC: PASS after 3 round(s) | verify: Slot JSON specifies 'four blockers' but E17/E18/E19 support only three (evaluation 64%, governance 57%, reliability 51%). Draft correctly wrote three. Human must fix the slot spec's 'four' before publish. -->

# Post 2 — 2026-09-02 — carousel
**Angle:** Each blocker between pilot and production kills a specific class of pilot, and evaluation gaps kill the most at 64%. [verify: slot JSON says "four blockers"; E17/E18/E19 support only three (evaluation 64%, governance 57%, reliability 51%). Proceeding with three as the evidence-correct count. No fourth blocker exists in the ledger and cannot be written without fabrication. Needs human sign-off on the slot spec.]

## Caption
A stalled pilot gets written off as "not ready." Usually it's one of three specific failures, and you can name which one killed each of yours. Evaluation gaps kill the most.

## Copy

**Slide 1:**
88% of agent pilots never reach production (Forrester/Anaconda). Separately, only 22.8% of AI projects launched this year are deployed and meeting ROI (HyperFRAME). They don't all die the same death.

**Slide 2:**
Evaluation gaps: 64% of failures, the biggest killer by far. The agent worked in a demo and no one built the pipeline to prove it kept working on real inputs.

**Slide 3:**
Governance friction: 57%. The agent passed testing and stalled at an approval it couldn't clear. No decision boundary, no escalation path, no owner to sign off.

**Slide 4:**
Model reliability: 51%. The agent held up on clean cases and broke on the messy ones production actually sends. The demo hid the failure modes that mattered.

**Slide 5:**
Sorted into these three, each stalled pilot is a specific engineering scope, not a dead end. The ones that shipped paid back in 5.1 months.

**Slide 6:**
Map your stalled pilots to their blocker now. Get in touch.

## Evidence used
- [E17]: 88% of agent pilots fail to reach production; evaluation gaps 64%, governance friction 57%, model reliability 51% — the three-blocker spine across slides 1–4.
- [E18]: Origin/replication of the 88% figure (Anaconda/Forrester, replicated by a16z and MIT Sloan) — supports confidence in the headline claim; not quoted directly.
- [E19]: 22.8% of AI projects launched in the past 12 months are deployed and meeting original ROI (HyperFRAME, 544 enterprises) — added to slide 1 as a corroborating scale figure. Kept on its own denominator and flagged "separately" so it does not merge with the 88% into a composite claim.
- [E21]: Median payback of 5.1 months on agent deployments — closes slide 5 on the upside of getting through.
- Note: the three named blockers (64/57/51) sum past 88% because failures overlap, so slides frame them as classes of failure, not mutually exclusive buckets. No composite claim invented.
- [verify]: slot JSON specifies "four blockers"; evidence supports three. Human sign-off needed on the slot spec before publish.

## Design note
Six clean slides on a consistent grid. Slide 1 carries two distinct figures (88% and 22.8%) with clear visual separation so they don't read as one number; slides 2–4 each anchor on their single percentage (64, 57, 51) in the same position so the eye tracks the descending count. Type sentence case, no icons that imply a metaphor.